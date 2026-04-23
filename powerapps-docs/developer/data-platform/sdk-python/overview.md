---
title: "Dataverse SDK for Python overview"
description: "Use Dataverse to store and access data for use in data science and analyses."
ms.author: paulliew
author: paulliew
ms.date: 04/21/2026
ms.reviewer: phecke
ms.topic: overview
contributors:
 - phecke
---

# Dataverse SDK for Python overview

The Dataverse SDK for Python enables Python developers to interact directly with Microsoft Dataverse. You can easily access, manage, and manipulate data stored in Dataverse by using familiar Python syntax. You don't need any .NET knowledge.

Check out this video!
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=541974da-10b2-46d9-95da-53587c83f84e]

## Benefits

The SDK for Python empowers the development of automated, intelligent processes (agentic workflows) by allowing seamless integration with Python's ecosystem for data analysis, AI, and workflow orchestration.

The SDK for Python lowers barriers for Python users, enabling rapid development of scalable, intelligent solutions on Microsoft Dataverse without .NET expertise.

The following list describes a few benefits of the SDK.

- No need to learn .NET or C# - work entirely in Python
- Accelerates automation, AI, and data-driven development
- Accessible to data scientists, developers, and engineers across platforms

## Key features

The following list describes key features of the Dataverse SDK for Python.

### Authentication

- The SDK supports authentication by using Azure identity [credentials](/python/api/azure-identity/azure.identity?view=azure-python&preserve-view=true) that support getting a token (get_token() method).

### Data operations

| Feature | Description |
|---|---|
| CRUD operations | Support for create, retrieve, update, and delete data operations by using a single request. |
| Bulk operations | Specify multiple operations in a single web service call. This feature uses Dataverse's native CreateMultiple, UpdateMultiple, UpsertMultiple, and BulkDelete Web API operations for maximum performance and transactional integrity. |
| Automatic retries | Handle networking problems that might occur for operations that fail due to temporary problems, such as API throttling or service unavailability. |
| Data retrievals | Supports OData options and paging, plus single or multiple "gets" in one call (as needed). |
| Direct-SQL queries | Supports simple read-only "SELECT" statements with paging. |
| Fluent QueryBuilder | Support for type-safe query construction with method chaining, composable filter expressions, and automatic OData generation. |
| Relationship management | Create one-to-many and many-to-many relationships between tables with full metadata control. |
| [Pandas](https://pandas.pydata.org/) Dataframes | Client wrappers are provided for all CRUD operations where [DataFrames](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html) and [Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) data types are returned to the caller. |
| File operations | Upload files to a Dataverse [file column](../../../maker/data-platform/types-of-fields.md#file-columns) with automatic chunking for large files. |
| Batch operations | Send multiple CRUD, table metadata, and SQL query operations in a single HTTP request with optional transactional changesets. |
| OptionSet/enum handling | The SDK automatically maps OptionSet columns in an API call to enumeration values. |

### Metadata operations on tables

- The SDK supports create, update, and delete (CUD) of custom tables and columns,  optional solution association, plus retrieve and list table definitions.

### Error handling and logging

- Error handling: structured exception hierarchy with detailed error context and retry guidance.
- HTTP diagnostics logging: opt-in file-based logging of all HTTP requests and responses with automatic redaction of sensitive headers, such as authorization.

<!-- ## Limitations

Here are a few known limitations of the current release.

- General purpose OData batching, upsert, and association operations aren't supported.
- Dataverse DeleteMultiple functionality isn't yet available from the Python SDK.
- Minimal retry policy support is in the SDK. Currently, only network errors are retried. Our code examples include another backoff for transient Dataverse consistency.
- SQL JOINs are currently not supported, and there's limited support for a WHERE/TOP/ORDER BY clause.
-->

## Concepts

The SDK provides a simple, pythonic interface for Dataverse operations.

| Concept | Description |
|---------|-------------|
| **DataverseClient** | Main client entry point. |
| **Context Manager** | Use `with DataverseClient(...) as client:` for automatic cleanup and HTTP connection pooling |
| **Namespaces** | Operations are organized into `client.records` (CRUD & OData queries), `client.query` (QueryBuilder & SQL), `client.tables` (metadata), `client.files` (file uploads), and `client.batch` (batch requests) |
| **Records** | Dataverse table rows (records) are represented as Python dictionaries with column schema names |
| **Schema names** | Use table schema names (`"account"`, `"new_MyTestTable"`) and column schema names (`"name"`, `"new_MyTestColumn"`). More information: [Table definitions in Microsoft Dataverse](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/entity-metadata) |
| **Customization prefix values** | Custom tables and columns require a customization prefix value to be included for all operations (e.g., `"new_MyTestTable"`, not `"MyTestTable"`). More information: [Table definitions in Microsoft Dataverse](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/entity-metadata) |

## Licensing

The SDK for Python is published under open-source licensing.

## Related information

- [SDK for Python source](https://github.com/microsoft/PowerPlatform-DataverseClient-Python)
- [Blog: Introducing the Dataverse SDK for Python](https://www.microsoft.com/power-platform/blog/2025/12/03/dataverse-sdk-python/)
- [Analyze and automate business data with Dataverse SDK for Python](/power-platform/architecture/reference-architectures/dataverse-sdk-for-python)
