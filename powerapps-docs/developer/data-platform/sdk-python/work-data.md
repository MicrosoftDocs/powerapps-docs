---
title: "Working with data (preview)"
description: "Learn common scenarios for working with Dataverse data,
    and how to go about writing Python code for those scenarios."
ms.author: paulliew
author: paulliew
ms.date: 10/30/2025
ms.reviewer: phecke
ms.topic: example-scenario
contributors:
 - phecke
---

# Working with data (preview)

In this article, we demonstrate some example code that uses the SDK to work with Dataverse data and metadata. Be sure you read [Getting started (preview)](get-started.md) first before continuing with this article.

> [!NOTE]
> [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

## Basic operations

Here is some example code that operates on the account table.

```python
from azure.identity import DefaultAzureCredential
from dataverse_sdk import DataverseClient

base_url = "https://<myorg>.crm.dynamics.com"
client = DataverseClient(base_url=base_url, credential=DefaultAzureCredential())

# Create an account and set some properties (returns list[str] of new GUIDs)
account_id = client.create("account", {"name": "Acme, Inc.", "telephone1": "555-0100"})[0]

# Read an account 
account = client.get("account", account_id)

# Update an account (returns None)
client.update("account", account_id, {"telephone1": "555-0199"})

# Delete an account
client.delete("account", account_id)
```

## Bulk operations

Here we show a couple of examples that do bulk updates.

```python
# Bulk update (broadcast) – apply same patch to several IDs
ids = client.create("account", [
    {"name": "Contoso"},
    {"name": "Fabrikam"},
])
client.update("account", ids, {"telephone1": "555-0200"})  # broadcast patch

# Bulk update (1:1) – list of patches matches list of IDs
client.update("account", ids, [
    {"telephone1": "555-1200"},
    {"telephone1": "555-1300"},
])
print({"multi_update": "ok"})
```

Here we show an example that creates multiple accounts. Pass a list of payloads to `create(logical_name, payloads)` to invoke the collection-bound `Microsoft.Dynamics.CRM.CreateMultiple` action. The method returns `list[str]` of created record IDs.

```python
# Bulk create accounts (returns list of GUIDs)
payloads = [
    {"name": "Contoso"},
    {"name": "Fabrikam"},
    {"name": "Northwind"},
]
ids = client.create("account", payloads)
assert isinstance(ids, list) and all(isinstance(x, str) for x in ids)
print({"created_ids": ids})
```

Additional information about bulk operations:

- Returns `None` (same as single update) to keep semantics consistent.
- Broadcast vs per-record determined by whether the `changes` parameter is a dictionary or list.
- Primary key attribute is injected automatically when constructing [UpdateMultiple](../../data-platform/webapi/reference/updatemultiple.md) targets.
- If any payload omits @odata.type, it's stamped automatically (cached logical name lookup).
- Response includes only IDs - the SDK returns those GUID strings.
- Single-record create returns a one-element list of GUIDs.
- Metadata lookup for @odata.type is performed once per entity set (cached in-memory).

## File upload

Here are a couple examples of uploading a file named 'test.pdf' to the [File column](../../..//maker/data-platform/types-of-fields.md#file-columns) named "sample_filecolumn" of an account record. The first example is for a file size less than 128 MB, while the second example is for a file size over 128 MB.

```python
client.upload_file('account', record_id, 'sample_filecolumn', 'test.pdf')
client.upload_file('account', record_id, 'sample_filecolumn', 'test.pdf', mode='chunk', if_none_match=True)
```

Additional information about file uploads:

- `upload_file` picks one of the three methods to use based on the file size. If the file size is less than 128 MB the SDK uses `upload_file_small`, otherwise, the SDK uses `upload_file_chunk`
- `upload_file_small` makes a single Web API call and only supports file size < 128 MB.
- `upload_file_chunk` uses PATCH with Content-Range to upload the file (more aligned with HTTP standard compared to Dataverse messages). It consists of 2 stages - 1. PATCH request to get the headers used for actual upload, and 2. Actual upload in chunks. The function uses OData x-ms-chunk-size returned in the first stage to determine chunk size (normally 4 MB), and then uses Content-Range and Content-Length as metadata for the upload. The total number of Web API calls is the number of chunks + 1.

## Retrieve multiple with paging

Use the `get` function to stream results page-by-page. You can cap total results with `$top` and hint the per-page size with the `page_size` parameter. The SDK internally sets the OData prefer header `odata.maxpagesize`.

```python
pages = client.get(
    "account",
    select=["accountid", "name", "createdon"],
    orderby=["name asc"],
    top=10,          # stop after 10 total rows (optional)
    page_size=3,     # ask for ~3 per page (optional)
)

total = 0
for page in pages: # each page is a list[dict]
    print({"page_size": len(page), "sample": page[:2]})
    total += len(page)
print({"total_rows": total})
```

<!-- TODO: This info should be in the package reference once written -->
Here is a list of supported parameters where all are optional except `logical_name`.

- logical_name: str — Logical (singular) name, e.g., "account".
- select: list[str] | None — Columns -> $select (comma joined).
- filter: str | None — OData $filter expression (e.g., contains(name,'Acme') and statecode eq 0).
- orderby: list[str] | None — Sort expressions -> $orderby (comma joined).
- top: int | None — Global cap via $top (applied on first request; service enforces across pages).
- expand: list[str] | None — Navigation expansions -> $expand; pass raw clauses (e.g., primarycontactid($select=fullname,emailaddress1)).
- page_size: int | None — Per-page hint using Prefer: odata.maxpagesize=<N> (not guaranteed; last page may be smaller).

<!-- TODO: This info should be in the package reference once written -->
Here is a list of return values & semantics.

- $select, $filter, $orderby, $expand, $top map directly to corresponding OData query options on the first request.
- $top caps total rows; the service may partition those rows across multiple pages.
- page_size (Prefer: odata.maxpagesize) is a hint; the server decides actual page boundaries.
- Returns a generator yielding non-empty pages (list[dict]). Empty pages are skipped.
- Each yielded list corresponds to a value page from the Web API.
- Iteration stops when no @odata.nextLink remains (or when $top satisfied server-side).
- The generator does not materialize all results; pages are fetched lazily.

Let's see an example with all supported parameters plus expected response.

```python
pages = client.get(
  "account",
  select=["accountid", "name", "createdon", "primarycontactid"],
  filter="contains(name,'Acme') and statecode eq 0",
  orderby=["name asc", "createdon desc"],
  top=5,
  expand=["primarycontactid($select=fullname,emailaddress1)"],
  page_size=2,
)

for page in pages:  # page is list[dict]
# Expected page shape (illustrative)
# [
# {
# "accountid": "00000000-0000-0000-0000-000000000001"
# "name": "Acme West"
# "createdon": "2025-08-01T12:34:56Z"
# "primarycontactid": {
# "contactid": "00000000-0000-0000-0000-0000000000aa"
# "fullname": "Jane Doe"
# "emailaddress1": "<jane@acme.com>"
# }
# "@odata.etag": "W/\"123456\""
# }
#
# ]
  print({"page_size": len(page)})
```

## Table metadata

Let's take a look at example code for working with a custom table.

```python
# Support enumerations with labels in different languages
class Status(IntEnum):
    Active = 1
    Inactive = 2
    Archived = 5
    __labels__ = {
        1033: {
            "Active": "Active",
            "Inactive": "Inactive",
            "Archived": "Archived",
        },
        1036: {
            "Active": "Actif",
            "Inactive": "Inactif",
            "Archived": "Archivé",
        }
    }

# Create a simple custom table and a few columns
info = client.create_table(
    "SampleItem",  # friendly name; defaults to SchemaName new_SampleItem
    {
        "code": "string",
        "count": "int",
        "amount": "decimal",
        "when": "datetime",
        "active": "bool",
        "status": Status,
    },
)

logical = info["entity_logical_name"]  # for example, "new_sampleitem"

# Create a record in the new table
# Set your publisher prefix (used when creating the table). If you used the default, it's "new".
prefix = "new"
name_attr = f"{prefix}_name"
id_attr = f"{logical}id"

rec_id = client.create(logical, {name_attr: "Sample A"})[0]

# Clean up
client.delete(logical, rec_id)          # delete record
client.delete_table("SampleItem")       # delete table (friendly name or explicit schema new_SampleItem)
```

Additional information about working with custom table metadata:

- `create` always returns a list of GUIDs (length=1 for single input).
- `update` and `delete` return `None` for both single and multiple interfaces.
- Passing a list of payloads to `create` triggers a bulk create and returns list[str] of IDs.
- `get` supports single record retrieval with record ID or paging through result sets (prefer select to limit columns).
- For CRUD methods that take a record ID, pass the GUID string (36-char hyphenated). Parentheses around the GUID are accepted but not required.
<!-- TODO: Move this to the SQL article when written-->
- SQL queries are executed directly against the entity set endpoints using the `?sql=` parameter. Supported subset only (single SELECT, optional WHERE/TOP/ORDER BY, alias). Unsupported constructs will be rejected by the service.

## Using pandas with the SDK

`PandasODataClient` is a thin wrapper around the low-level client. All methods accept logical (singular) names (for example, account, new_sampleitem), not entity set (plural) names, are supported. See the SDK source repo [example](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples) named 'quickstart_pandas.py' for a `DataFrame` workflow.

## Related information

- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started (preview)](get-started.md)
- [Roadmap to Dataverse (preview)](roadmap.md)
