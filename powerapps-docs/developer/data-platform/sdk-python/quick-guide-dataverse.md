---
title: "Quick guide to Dataverse"
description: "Learn some key concepts of Dataverse that every programmer needs to know for success."
ms.author: kewear
author: kewear
ms.date: 04/21/2026
ms.reviewer: phecke
ms.topic: concept-article
contributors:
 - phecke
---

# Quick guide to Dataverse

This article introduces key concepts about Dataverse that Python (and other non-.NET) programmers should know to be successful when working with Dataverse. It also provides links to more detailed information. Dataverse capabilities are extensive, but you can explore these other capabilities at your own pace.

Programmers coding in C#/.NET should read the extensive [Dataverse Developer Guide](../../data-platform/overview.md).

## Tables and messages

You store data in tables, which are organized into rows and columns. Messages are the operations that act on tables and table data. Tables are also known as *entities*, and rows are sometimes called *records* in the documentation.

### Tables

You commonly use three kinds of tables in Dataverse: system, customizable, and custom. System tables, also known as out-of-box tables, can't be changed and support the basic functionality of Dataverse. You can interactively or programmatically modify customizable and custom tables if you have the appropriate permissions.

To interactively [create or modify a table](../../../maker/data-platform/create-edit-entities-portal.md?tabs=excel), use the [Power Platform admin center](/power-platform/admin/) (PPAC). To programmatically create or modify a table, modify table metadata. The SDK for Python includes functions (in `client.tables`) that easily enable you to work with table metadata.

Dataverse table rows, also known as records, are represented as Python dictionaries with column schema names.

For more information, see [Web API EntityType Reference](xref:Microsoft.Dynamics.CRM.EntityTypeIndex) and [Use the Web API with table definitions](../../data-platform/webapi/use-web-api-metadata.md).

### Messages

Messages represent the web service operation to perform. Messages can be simpler operations like create, retrieve, update, and delete (CRUD). Messages can also invoke more complex operations like book or win, which might initiate a combination of other operations.

The entity type reference lists all known (noncustom) tables and the standard messages that each table supports. When you create a custom table, a default set of messages is available for that table.

## Security

Access to data in your Dataverse environment is limited based on the security role (or roles) that an administrator assigns to you, and the data management permissions of that role. Your role might grant access to an entire table, or security might restrict your access to a specific row and column.

For more information, see [Security overview](/power-platform/admin/security/security-overview) and [Security and data access](../../data-platform/security-model.md).

## Customizations and extensions

This section covers some ways to customize and extend Dataverse.

### More about tables

Dataverse supports customizable and custom tables. A customizable table is an existing table that ships with Dataverse that you can modify, for example, to add or delete columns, change the table name, and more.

Custom tables are tables that you (or a third party) create. As stated earlier in this article, the SDK provides Python functions that you can use to create and delete custom tables.

> [!IMPORTANT]
> You must include a customization prefix value for all operations on custom tables and columns (for example, "new_MyTestTable", not "MyTestTable").
>
> Always use table schema names ("account", "new_MyTestTable") and column schema names ("name", "new_MyTestColumn") in SDK API calls.
>
> For more information, see [Table definitions in Microsoft Dataverse](/power-apps/developer/data-platform/entity-metadata).

### Extensions

You can modify the functionality of Dataverse's data processing by using event handlers (called plug-ins) and custom workflow activities. These compiled custom code objects are registered on a certain table and message combination. A plug-in or workflow activity can modify data before or after the main data processing operation of Dataverse. If you see different data results than you expect, one of these extensions might be the cause.

Other ways to customize and extend Dataverse exist, but the complete list is beyond the scope of this article.

## Web API

The SDK provides a Python programming interface that internally calls the Dataverse [Web API](../../data-platform/webapi/overview.md). The `DataverseClient` class provides a simplified interface to OData 2.0 authorization as required by the Web API.

You can invoke Web API functions and actions directly from within your Python program. However, the SDK for Python provides a more natural programming syntax to access Dataverse data as expected by Python developers and data scientists.

## Solutions

A solution is a container of folders and files that extend and customize Dataverse. Solutions are the mechanism for packaging customizations and extensions into a single compressed file for export. You can import that solution file into other environments (also known as organizations).

Extensions and customizations always exist in a solution. In Dataverse, there's a default solution. If you add extensions or customizations to your environment without adding them to a custom solution, the default solution automatically contains them.

You can create, manage, export, and import solutions interactively by using PPAC or programmatically by using the Web API.

For more information, see [Solution concepts](/power-platform/alm/solution-concepts-alm).

## Related information
