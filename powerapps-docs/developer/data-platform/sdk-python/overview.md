---
title: "Dataverse SDK for Python overview (preview)"
description: "Use Dataverse to store and access data for use in data science and analyses."
ms.author: paulliew
author: paulliew
ms.date: 10/29/2025
ms.reviewer: phecke
ms.topic: overview
contributors:
 - phecke
---

# Dataverse SDK for Python overview (preview)

Dataverse SDK for Python enables Python developers to interact directly with Microsoft Dataverse, making it easy to access, manage, and manipulate data stored in Dataverse using familiar Python syntax—no .NET knowledge required.

> [!NOTE]
> [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

## Supporting Agentic Processes

The SDK empowers the development of automated, intelligent processes (agentic workflows) by allowing seamless integration with Python's ecosystem for data analysis, AI, and workflow orchestration.

## Key Features

The following list describes a key features of the SDK.

- Data operations

    The SDK supports create, retrieve, update, and delete (CRUD) data operations using a single request, and also bulk operations. Data retrievals support OData options and paging, plus single or multiple "gets" in one call (as needed).
    Direct-SQL is supported for simple "SELECT" statements with paging. SQL JOINs are currently not supported.
- Metadata operations on tables

    The SDK supports create, update, and delete (CUD) of tables,  optional solution association, plus retrieve and list table definitions. <!-- What about prefix usage?-->
- Simplified authentication

    You can use client secret and Service Principal authentication. The SDK supports [DefaultAzureCredentials](/dotnet/api/azure.identity.defaultazurecredential?view=azure-dotnet&preserve-view=true), and you can use your own token, for example from [InteractiveBrowserCredential](/dotnet/api/azure.identity.interactivebrowsercredential?view=azure-dotnet&preserve-view=true).
- File upload

    Upload a file to a [File column](../../../maker/data-platform/types-of-fields.md#file-columns) in a table.
- OptionSet/enum handling

    OptionSet columns in a API call are mapped to enumeration values automatically.
- Integration with [pandas](https://pandas.pydata.org/)

    The API call return value is in JSON format, which can be mapped to a [DataFrame](https://pandas.pydata.org/docs/reference/frame.html).
- SDK [source code](https://github.com/microsoft/PowerPlatform-DataverseClient-Python)
 is published under open source licensing

## Benefits

Dataverse SDK for Python lowers barriers for Python users, enabling rapid development of scalable, intelligent solutions on Microsoft Dataverse without .NET expertise.

The following list describes a few benefits of the SDK.

- No need to learn .NET or C# — work entirely in Python
- Accelerates automation, AI, and data-driven development
- Accessible to data scientists, developers, and engineers across platforms

## Limitations

Here are a few known limitations of the current (preview) release.

- General purpose OData batching, upsert, and association operations are not supported.
- Dataverse DeleteMultiple functionality is not yet available from the Python SDK.
- Minimal retry policy support in the library - currently network-error only. Our code examples include additional backoff for transient Dataverse consistency.

## Related information

- [Project source](https://github.com/microsoft/PowerPlatform-DataverseClient-Python)
- [Use the SDK for .NET](../../data-platform/org-service/overview.md)
