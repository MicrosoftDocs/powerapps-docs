---
title: Asynchronous client operations
description: Learn how to execute date operations asynchronously using the SDK for Python.
ms.author: kewear
author: kewear
ms.date: 05/28/2026
ms.reviewer: phecke
ms.topic: concept-article
contributors:
 - phecke
---

# Asynchronous client operations

The Dataverse SDK for Python includes a full asynchronous client named `AsyncDataverseClient`. It mirrors every operation of the synchronous client `DataverseClient` - the same namespaces (`records`, `query`, `tables`, `files`, `batch`), the same method signatures, and the same return types.

## Installation

The async client requires that [aiohttp](https://pypi.org/project/aiohttp/) be installed in your workspace. To install the client, run the following command.

```bash
pip install "PowerPlatform-Dataverse-Client[async]"
```

## Quick start

Here's some example code that uses the async client to connect to Dataverse, create and retrieve a contact, and then delete the contact.

```python
import asyncio
from azure.identity import InteractiveBrowserCredential
from PowerPlatform.Dataverse.aio import AsyncDataverseClient

async def main():

    # Connect to Dataverse
    credential = InteractiveBrowserCredential()

    async with DefaultAzureCredential() as credential:
        async with AsyncDataverseClient("https://myorg.crm.dynamics.com", credential) as client:

            # Create a contact
            contact_id = await client.records.create("contact", {"firstname": "John", "lastname": "Doe"})

            # Read it back
            contact = await client.records.retrieve("contact", contact_id, select=["firstname", "lastname"])
            print(f"Created: {contact['firstname']} {contact['lastname']}")

            # Clean up
            await client.records.delete("contact", contact_id)

asyncio.run(main())
```

> [!IMPORTANT]
> Async code snippets in following sections are fragments. Every example after the quick start code example assumes it is nested inside an `async def main(): ...` body, with `client` and `credential` already constructed. Copying a fragment into a top-level `.py` file raises `SyntaxError: 'await' outside function`. See [examples/aio/](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples/aio) for full runnable scripts.

## Alternate syntax

Here's another example that demonstrates simplified (standalone) invocation.

```python
# The credential creation and Dataverse connection code is not shown
client = AsyncDataverseClient("https://myorg.crm.dynamics.com", credential)

try:
    account_id = await client.records.create("account", {"name": "Contoso Ltd"})
finally:
    await client.aclose()
```

## Query builder

The async query builder API is identical to the sync (`DataverseClient`) API.

```python
# The credential creation and Dataverse connection code is not shown
from PowerPlatform.Dataverse.models.filters import col

# Execute and collect all results
result = await (
    client.query.builder("account")
    .select("name", "telephone1")
    .where(col("statecode") == 0)
    .top(10)
    .execute()
)
for record in result:
    print(record["name"])

# Lazy page-by-page iteration (memory-efficient for large sets)
async for page in (
    client.query.builder("account")
    .select("name")
    .page_size(500)
    .execute_pages()
):
    for record in page:
        print(record["name"])
```

## Batch and changesets

This example demonstrates batch operations and changesets.

```python
# The credential creation and Dataverse connection code is not shown
batch = client.batch.new()
batch.records.create("account", {"name": "Alpha"})
batch.records.create("account", {"name": "Beta"})
result = await batch.execute()
print(f"Created {len(result.entity_ids)} records")

# Atomic changeset
batch = client.batch.new()
async with batch.changeset() as cs:
    ref = cs.records.create("contact", {"firstname": "Alice"})
    cs.records.update("account", account_id, {"primarycontactid@odata.bind": ref})
result = await batch.execute()
```

For async equivalents of all `DataverseClient` sync examples, see [examples/aio/](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples/aio).

## Related information

- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started](get-started.md)
- [Quick guide to Dataverse](quick-guide-dataverse.md)
