---
title: "Dataverse SDK for Python overview (preview)"
description: "Use Dataverse to store and access data for use in data science and analyses."
ms.author: paulliew
author: paulliew
ms.date: 12/08/2025
ms.reviewer: phecke
ms.topic: overview
contributors:
 - phecke
---

# Dataverse SDK for Python overview (preview)

Dataverse SDK for Python enables Python developers to interact directly with Microsoft Dataverse, making it easy to access, manage, and manipulate data stored in Dataverse using familiar Python syntax — no .NET knowledge required.

[!INCLUDE [preview-note-pp](../../../../shared/preview-includes/preview-note-pp.md)]

Check out this video!
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=541974da-10b2-46d9-95da-53587c83f84e]

## Supporting Agentic Processes

The SDK empowers the development of automated, intelligent processes (agentic workflows) by allowing seamless integration with Python's ecosystem for data analysis, AI, and workflow orchestration.

## Key Features

The following list describes key features of the SDK.

- Data operations

    The SDK supports create, retrieve, update, and delete (CRUD) data operations using a single request, and also bulk operations. Data retrievals support OData options and paging, plus single or multiple "gets" in one call (as needed).
    Direct-SQL is supported for simple "SELECT" statements with paging.
- Metadata operations on tables

    The SDK supports create, update, and delete (CUD) of tables,  optional solution association, plus retrieve and list table definitions. <!-- TODO: What about prefix usage?-->
- Simplified authentication

     The SDK supports authentication using Azure identity [credentials](/python/api/azure-identity/azure.identity?view=azure-python&preserve-view=true) that supports getting a token (get_token() method).
- File upload

    Upload a file to a [File column](../../../maker/data-platform/types-of-fields.md#file-columns) in a table.
- OptionSet/enum handling

    OptionSet columns in an API call are mapped to enumeration values automatically.
- Integration with [pandas](https://pandas.pydata.org/)

    The API call return value is in JSON format, which can be mapped to a [DataFrame](https://pandas.pydata.org/docs/reference/frame.html).
- SDK is published under open source licensing

## Benefits

Dataverse SDK for Python lowers barriers for Python users, enabling rapid development of scalable, intelligent solutions on Microsoft Dataverse without .NET expertise.

The following list describes a few benefits of the SDK.

- No need to learn .NET or C# — work entirely in Python
- Accelerates automation, AI, and data-driven development
- Accessible to data scientists, developers, and engineers across platforms

## Limitations

Here are a few known limitations of the current (preview) release.

- General purpose OData batching, upsert, and association operations aren't supported.
- Dataverse DeleteMultiple functionality isn't yet available from the Python SDK.
- Minimal retry policy support is in the SDK. Currently, only network errors are retried. Our code examples include another backoff for transient Dataverse consistency.
<!-- TODO: move to the SQL article -->
- SQL JOINs are currently not supported, and there's limited support for a WHERE/TOP/ORDER BY clause.

## Related information

- [SDK for Python source](https://github.com/microsoft/PowerPlatform-DataverseClient-Python)
- [Blog: Introducing the Dataverse SDK for Python](https://www.microsoft.com/power-platform/blog/2025/12/03/dataverse-sdk-python/)
