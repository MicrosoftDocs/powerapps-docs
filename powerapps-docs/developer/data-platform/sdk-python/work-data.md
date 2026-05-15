---
title: "Work with Dataverse Data Using Python SDK"
description: "Learn common scenarios for working with Dataverse data using the Python SDK, including CRUD, bulk operations, upserts, and batching. Start coding today."
ms.author: paulliew
author: paulliew
ms.date: 05/13/2026
ms.reviewer: phecke
ms.topic: example-scenario
contributors:
 - phecke
---

# Work with Dataverse data using the Python SDK

This article demonstrates example code that uses the SDK to work with Dataverse data and metadata. Before continuing, be sure to read [Getting started](get-started.md).

## Basic operations

Here's some example code that operates on the account table.

```python
from azure.identity import InteractiveBrowserCredential
from PowerPlatform.Dataverse.client import DataverseClient

# Replace <myorg> with the name of a valid environment.
base_url = "https://<myorg>.crm.dynamics.com"
client = DataverseClient(base_url=base_url, credential=InteractiveBrowserCredential())

# Create a record
account_id = client.records.create("account", {"name": "Contoso Ltd"})

# Read a record
account = client.records.retrieve("account", account_id)
print(account["name"])

# Read with expand fetches a related record in the same HTTP request
account = client.records.retrieve(
    "account", account_id,
    select=["name"],
    expand=["primarycontactid"],
)
contact = (account.get("primarycontactid") or {})
print(contact.get("fullname"))

# Update a record
client.records.update("account", account_id, {"telephone1": "555-0199"})

# Delete a record
client.records.delete("account", account_id)
```

### Context manager

The Context Manager handles automatic cleanup and HTTP connection pooling. Use the following syntax to take advantage of the Context Manager.

```python
with DataverseClient("https://<myorg>.crm.dynamics.com", credential) as client:
```

The following working code demonstrates how to use the Context Manager.

```python
from azure.identity import InteractiveBrowserCredential
from PowerPlatform.Dataverse.client import DataverseClient

# Connect to Dataverse
credential = InteractiveBrowserCredential()

with DataverseClient("https://<myorg>.crm.dynamics.com", credential) as client:

    # Create a contact
    contact_id = client.records.create("contact", {"firstname": "John", "lastname": "Doe"})

    # Read the contact back
    contact = client.records.retrieve("contact", contact_id, select=["firstname", "lastname"])
    print(f"Created: {contact['firstname']} {contact['lastname']}")

    # Clean up
    client.records.delete("contact", contact_id)

# Session closed, caches cleared automatically
```

## Bulk operations

Here are a couple of examples that perform bulk operations.

```python
# Bulk create
payloads = [
    {"name": "Company A"},
    {"name": "Company B"},
    {"name": "Company C"}
]
ids = client.records.create("account", payloads)

# Bulk update (broadcast same change to all)
client.records.update("account", ids, {"industry": "Technology"})

# Bulk delete
client.records.delete("account", ids, use_bulk_delete=True)
```

The following example creates multiple accounts. Pass a list of payloads to `create(logical_name, payloads)` to invoke the collection-bound `Microsoft.Dynamics.CRM.CreateMultiple` action. The method returns `list[str]` of created record IDs.

```python
# Bulk create accounts (returns list of GUIDs)
payloads = [
    {"name": "Contoso"},
    {"name": "Fabrikam"},
    {"name": "Northwind"},
]
ids = client.records.create("account", payloads)
assert isinstance(ids, list) and all(isinstance(x, str) for x in ids)
print({"created_ids": ids})
```

For more information about bulk operations:

- Returns `None` (same as single update) to keep semantics consistent.
- Broadcast versus per-record is determined by whether the `changes` parameter is a dictionary or list.
- The primary key attribute is injected automatically when constructing [UpdateMultiple action](xref:Microsoft.Dynamics.CRM.UpdateMultiple) targets.
- If any payload omits @odata.type, the SDK stamps it automatically (cached logical name lookup).
- The response includes only IDs - the SDK returns those GUID strings.
- Single-record create returns a one-element list of GUIDs.
- Metadata lookup for `@odata.type` is performed once per entity set (cached in-memory).

## Upsert (create and update)

A common data access sequence is to first check if a table row exists. If the row exists, update it. Otherwise, create the row. You can make this sequence more efficient by using a single API call of the Upsert operation.

For more information, see [Use Upsert to Create or Update a record](../use-upsert-insert-update-record.md).

> [!IMPORTANT]
> The table must have an alternate key configured in Dataverse for the columns used in `alternate_key`. Define alternate keys in the table's metadata via the Power Apps maker portal or a Dataverse API call. Without a configured alternate key, Dataverse rejects upsert requests with a 400 error.

Use `client.records.upsert()` to create or update records identified by alternate keys. When the key matches an existing record, the method updates the record. Otherwise, it creates the record. A single item uses a PATCH request while multiple items use the `UpsertMultiple` bulk action.

```python
from PowerPlatform.Dataverse.models.upsert import UpsertItem

# Upsert a single record
client.records.upsert("account", [
    UpsertItem(
        alternate_key={"accountnumber": "ACC-001"},
        record={"name": "Contoso Ltd", "telephone1": "555-0100"},
    )
])

# Upsert multiple records (uses UpsertMultiple bulk action)
client.records.upsert("account", [
    UpsertItem(
        alternate_key={"accountnumber": "ACC-001"},
        record={"name": "Contoso Ltd"},
    ),
    UpsertItem(
        alternate_key={"accountnumber": "ACC-002"},
        record={"name": "Fabrikam Inc"},
    ),
])

# Composite alternate key (multiple columns identify the record)
client.records.upsert("account", [
    UpsertItem(
        alternate_key={"accountnumber": "ACC-001", "address1_postalcode": "98052"},
        record={"name": "Contoso Ltd"},
    )
])

# Plain dict syntax (no import needed)
client.records.upsert("account", [
    {
        "alternate_key": {"accountnumber": "ACC-001"},
        "record": {"name": "Contoso Ltd"},
    }
])
```

## DataFrames

The SDK provides pandas wrappers for all CRUD operations through the `client.dataframe` namespace. These wrappers use DataFrames and Series for input and output.

> [!NOTE]
> `client.dataframe.get()` is deprecated. Use the GA patterns shown in the following sections.

```python
import pandas as pd
from PowerPlatform.Dataverse.models.filters import col

# Query records as a single DataFrame (GA builder pattern)
df = (client.query.builder("account")
      .select("name", "telephone1")
      .where(col("statecode") == 0)
      .execute()
      .to_dataframe())
print(f"Found {len(df)} accounts")

# Limit results with top for large tables
df = client.query.builder("account").select("name").top(100).execute().to_dataframe()

# Fetch a single record as a one-row DataFrame
df = client.records.retrieve("account", account_id, select=["name"]).to_dataframe()

# Create records from a DataFrame (returns a Series of GUIDs)
new_accounts = pd.DataFrame([
    {"name": "Contoso", "telephone1": "555-0100"},
    {"name": "Fabrikam", "telephone1": "555-0200"},
])
new_accounts["accountid"] = client.dataframe.create("account", new_accounts)

# Update records from a DataFrame (id_column identifies the GUID column)
new_accounts["telephone1"] = ["555-0199", "555-0299"]
client.dataframe.update("account", new_accounts, id_column="accountid")

# Clear a field by setting clear_nulls=True (by default, NaN/None fields are skipped)
df = pd.DataFrame([{"accountid": new_accounts["accountid"].iloc[0], "websiteurl": None}])
client.dataframe.update("account", df, id_column="accountid", clear_nulls=True)

# Delete records by passing a Series of GUIDs
client.dataframe.delete("account", new_accounts["accountid"])

# SQL query directly to DataFrame (supports JOINs, aggregates, GROUP BY)
df = client.dataframe.sql(
    "SELECT a.name, COUNT(c.contactid) as contacts "
    "FROM account a "
    "JOIN contact c ON a.accountid = c.parentcustomerid "
    "GROUP BY a.name"
)
```

## Retrieve multiple records with paging

Use the `retrieve` function to stream results page-by-page. You can limit the total results with `$top` and suggest the per-page size with the `page_size` parameter. The SDK internally sets the OData prefer header `odata.maxpagesize`.

```python
pages = client.records.retrieve(
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

<!-- TODO This info should be in the package reference once written -->
Here's a list of supported parameters where all are optional except `logical_name`.

- logical_name: str — Logical (singular) name, for example, "account".
- select: list[str] | None — Columns -> $select (comma joined).
- filter: str | None — OData $filter expression (for example, contains(name,'Acme') and statecode eq 0).
- orderby: list[str] | None — Sort expressions -> $orderby (comma joined).
- top: int | None — Global cap via $top (applied on first request; service enforces across pages).
- expand: list[str] | None — Navigation expansions -> $expand; pass raw clauses (e.g., primarycontactid($select=fullname,emailaddress1)).
- page_size: int | None — Per-page hint using Prefer: odata.maxpagesize=\<N\> (not guaranteed; last page may be smaller).

<!-- TODO: This info should be in the package reference once written -->
Here's a list of return values and semantics.

- `$select`, `$filter`, `$orderby`, `$expand`, and `$top` map directly to corresponding OData query options on the first request.
- `$top` caps total rows; the service might partition those rows across multiple pages.
- `page_size` (`Prefer: odata.maxpagesize`) is a hint; the server decides actual page boundaries.
- Returns a generator that yields nonempty pages (list[dict]). The generator skips empty pages.
- Each yielded list corresponds to a value page from the Web API.
- Iteration stops when no @odata.nextLink remains (or when `$top` satisfies server-side).
- The generator doesn't materialize all results; it fetches pages lazily.

Here's an example with all supported parameters plus the expected response.

```python
pages = client.records.retrieve(
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

## Upload files to Dataverse

Here are two examples of uploading a file named `test.pdf` to the [File column](../../..//maker/data-platform/types-of-fields.md#file-columns) named `sample_filecolumn` of an account record. The first example is for a file size less than 128 MB, and the second example is for a file size over 128 MB.

```python
client.upload_file('account', record_id, 'sample_filecolumn', 'test.pdf')
client.upload_file('account', record_id, 'sample_filecolumn', 'test.pdf', mode='chunk', if_none_match=True)
```

> [!TIP]
> If the file column doesn't exist, the SDK creates it automatically.

Additional information about file uploads:

- `upload_file` picks one of three methods to use based on the file size. If the file size is less than 128 MB, the SDK uses `upload_file_small`. Otherwise, the SDK uses `upload_file_chunk`.
- `upload_file_small` makes a single Web API call and only supports file sizes less than 128 MB.
- `upload_file_chunk` uses PATCH with Content-Range to upload the file. This method is more aligned with the HTTP standard compared to Dataverse messages. It consists of two stages: 1. PATCH request to get the headers used for the actual upload, and 2. Actual upload in chunks. The function uses OData `x-ms-chunk-size` returned in the first stage to determine chunk size (normally 4 MB), and then uses `Content-Range` and `Content-Length` as metadata for the upload. The total number of Web API calls is the number of chunks plus one.

## Batch operations

Use `client.batch` to send multiple operations in one HTTP request. The batch namespace mirrors `client.records`, `client.tables`, and `client.query`.

```python
# Build a batch request and add operations
batch = client.batch.new()
batch.records.create("account", {"name": "Contoso"})
batch.records.create("account", [{"name": "Fabrikam"}, {"name": "Woodgrove"}])
batch.records.update("account", account_id, {"telephone1": "555-0100"})
batch.records.delete("account", old_id)
batch.records.retrieve("account", account_id, select=["name"], expand=["primarycontactid"])  # single record with expand
batch.records.list(                                                # multi-record, single page
    "account",
    filter="statecode eq 0",
    select=["name"],
    orderby=["name asc"],
    top=50,
)

result = batch.execute()
for item in result.responses:
    if item.is_success:
        print(f"[OK] {item.status_code} entity_id={item.entity_id}")
    else:
        print(f"[ERR] {item.status_code}: {item.error_message}")
```

### Transactional changeset

All operations in a changeset succeed or roll back together.

```python
batch = client.batch.new()
with batch.changeset() as cs:
    lead_ref = cs.records.create("lead", {"firstname": "Ada"})
    contact_ref = cs.records.create("contact", {"firstname": "Ada"})
    cs.records.create("account", {
        "name": "Babbage & Co.",
        "originatingleadid@odata.bind": lead_ref,
        "primarycontactid@odata.bind": contact_ref,
    })
result = batch.execute()
print(f"Created {len(result.entity_ids)} records atomically")
```

### Table metadata and SQL queries in a batch

```python
batch = client.batch.new()
batch.tables.create("new_Product", {"new_Price": "decimal", "new_InStock": "bool"})
batch.tables.add_columns("new_Product", {"new_Rating": "int"})
batch.tables.get("new_Product")
batch.query.sql("SELECT TOP 5 name FROM account")

result = batch.execute()
```

### Continue on error

Attempt all operations even when one fails.

```python
result = batch.execute(continue_on_error=True)
print(f"Succeeded: {len(result.succeeded)}, Failed: {len(result.failed)}")
for item in result.failed:
    print(f"[ERR] {item.status_code}: {item.error_message}")
```

### DataFrame integration

Feed pandas DataFrames directly into a batch.

```python
import pandas as pd

batch = client.batch.new()

# Create records from a DataFrame
df = pd.DataFrame([{"name": "Contoso"}, {"name": "Fabrikam"}])
batch.dataframe.create("account", df)

# Update records from a DataFrame
updates = pd.DataFrame([
    {"accountid": id1, "telephone1": "555-0100"},
    {"accountid": id2, "telephone1": "555-0200"},
])
batch.dataframe.update("account", updates, id_column="accountid")

# Delete records from a Series
batch.dataframe.delete("account", pd.Series([id1, id2]))

result = batch.execute()
```

For a complete batvh example see [examples/advanced/batch.py](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/examples/advanced/batch.py).

## Related information

- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started](get-started.md)
- [Quick guide to Dataverse](quick-guide-dataverse.md)
