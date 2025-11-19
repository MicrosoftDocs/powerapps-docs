---
title: "Quick guide to Dataverse (preview)"
description: "Learn some key concepts of Dataverse that every programmer needs to know for success."
ms.author: paulliew
author: paulliew
ms.date: 11/17/2025
ms.reviewer: phecke
ms.topic: concept-article
contributors:
 - phecke
---

# Quick guide to Dataverse (preview)

[!INCLUDE [preview-banner](../../../../shared/preview-includes/preview-banner.md)]

In this article, we explore some key concepts about Dataverse that Python (and other non-.NET) programmers should know in order to be successful when working with Dataverse. We also provide links to more detailed information. Dataverse capabilities are extensive, however, you can explore these other capabilities at your own pace should you choose to do so.

Programmers coding in C#/.NET should read our extensive [Dataverse Developer Guide](../../data-platform/overview.md).

## Tables and messages

Data is stored in tables, which are organized into rows and columns. Messages are the operations that act on tables and table data. Tables are also known and *entities*, and rows are sometimes called *records* in our documentation.

### Tables

There are three kinds of tables you would commonly use in Dataverse: system, customizable, and custom. System tables, also known as out-of-box tables, can't be changed and support the basic functionality of Dataverse. Customizable and custom tables can be interactively or programmatically modified by the user if that person has the appropriate permissions to do so.

To interactively [create or modify a table](../../../maker/data-platform/create-edit-entities-portal.md?tabs=excel), use the [Power Platform admin center](/power-platform/admin/) (PPAC). To programmatically create or modify a table, you modify table metadata. The SDK for Python includes functions (for example `create_table`, `delete_table`) that easily enable you to work with table metadata.

More information: [Web API EntityType Reference](xref:Microsoft.Dynamics.CRM.EntityTypeIndex), [Use the Web API with table definitions](../../data-platform/webapi/use-web-api-metadata.md)

### Messages

Messages represent the web service operation to be performed. Messages can be simpler operations like create, retrieve, update, and delete (CRUD). Messages can also invoke more complex operations like book, win, that may initiate a combination of other operations.

The entity type reference lists all known (noncustom) tables and the standard messages that each table supports. When you create a custom table, a default set of messages is made available for that table.

## Security

Access to data in your Dataverse environment is limited based on the security role (or roles) you're assigned by an administrator, and the data management permissions of that role. Your role may allow access to an entire table, or security can restrict your access to a specific row and column.

More information: [Security overview](/power-platform/admin/security/security-overview), [Security and data access](../../data-platform/security-model.md)

## Customizations and extensions

Here we cover some ways to customize and extend Dataverse.

### More about tables

Dataverse supports customizable and custom tables. A customizable table is an existing table that ships with Dataverse that can be modified, for example to add or delete columns, change the table name, etc.

Custom tables are tables that you (or a third party) create. As stated earlier in this article, the SDK provides Python functions enabling you to create and delete custom tables.

### Extensions

The functionality of Dataverse's data processing can be modified by event handlers (called plug-ins), and custom workflow activities. These compiled custom code objects are registered on a certain table and message combination. We only mention it here as a plug-in or workflow activity can modify data before or after the main data processing operation of Dataverse. If you're seeing different data results than you expect, one of these extensions may be the cause.

There are other ways to customize and extend Dataverse, but the complete list is beyond the scope of this article.

## Web API

The SDK provides a Python programming interface that internally calls the Dataverse [Web API](../../data-platform/webapi/overview.md). The `DataverseClient` class provides a simplified interface to OData 2.0 authorization as required by the Web API.

You can invoke Web API functions and actions directly from within your Python program. However, the SDK for Python provides a more natural programming syntax to access Dataverse data as expected by Python developers and data scientists.

## Solutions

A solution is a container of folders and files that extend and/or customize Dataverse. Solutions are the mechanism for customizations and extensions to be packaged up and exported into a single compressed file. That solution file can then be imported into other environments (also know as organizations).

Extensions and customizations always exist in a solution. In Dataverse, there exists a default solution. If you add extensions or customizations to your environment, and don't add them to a custom solution, they're automatically placed in the default solution.

You can create, manage, export, and import solutions interactively using PPAC or programmatically using the Web API.

More information: [Solution concepts](/power-platform/alm/solution-concepts-alm)

## Related information
