---
title: "dataApi reference for generative pages"
description: "The article provides dataApi reference for generative pages."
ms.date: 10/19/2026
author: jasongre
ms.author: jasongre
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
  - ruxyrezidenttm
ai-usage: ai-assisted
---
# dataApi reference for generative pages

When you [generate a page using natural language](../../../../maker/model-driven-apps/generative-pages.md), the AI creates a React page in TypeScript. The generated page covers both the front-end user experience by selecting the right components and determining the best layout, and the corresponding business logic.

You can [view and edit the generated code to refine the output](../../../../maker/model-driven-apps/generative-pages.md#view-the-generated-code-iterate-and-publish). Data operations use a `dataApi` object that exposes public methods grouped into these categories:

|Category|Description|
|---|---|
|[Dataverse table methods](dataverse-table-methods.md)|Create, retrieve, update, and delete Dataverse table rows, and query choice columns.|
|[Connector methods](connector-methods.md)|Work with data exposed by a Power Platform connector bound to the page.|
|[Dataverse operation methods](dataverse-operation-methods.md)|Invoke Dataverse custom APIs bound to the page as actions or functions.|
|[Page methods](page-methods.md)|Control the generative page itself, such as returning a value when the page is used as a dialog.|

Connector methods and action and function methods are optional members of the `dataApi` contract. Some hosts don't implement them, so always check that a method exists (for example, `if (dataApi.executeAction) { ... }`) before calling it. A method being present doesn't mean the page has a connector or Dataverse custom API bound to it, or that the custom API is enabled or permitted for the current user. Handle unavailable functionality and custom API failures explicitly rather than assuming success.

## Dataverse table methods

Use the Dataverse table methods of the `dataApi` object to create, retrieve, update, and delete Dataverse table rows, and query choice columns.

|Method|Description|
|---|---|
|[`createRow`](dataverse-table-methods.md#createrow-method)|Creates a new row in the specified table.|
|[`deleteRow`](dataverse-table-methods.md#deleterow-method)|Deletes a row from the specified table.|
|[`getChoices`](dataverse-table-methods.md#getchoices-method)|Retrieves the choices for the specified choice column name.|
|[`queryTable`](dataverse-table-methods.md#querytable-method)|Queries a table with the specified options.|
|[`retrieveRow`](dataverse-table-methods.md#retrieverow-method)|Retrieves a row from the specified table with the specified options.|
|[`updateRow`](dataverse-table-methods.md#updaterow-method)|Updates an existing row in the specified table.|

## Connector methods

Use the connector methods of the `dataApi` object to work with data exposed by a Power Platform connector bound to the page.

|Method|Description|
|---|---|
|[`createConnectorRow`](connector-methods.md#createconnectorrow-method)|Creates a new row in the specified connector table.|
|[`deleteConnectorRow`](connector-methods.md#deleteconnectorrow-method)|Deletes a row from the specified connector table.|
|[`executeConnectorOperation`](connector-methods.md#executeconnectoroperation-method)|Invokes a named operation exposed by a REST (operation-keyed) connector, such as Office 365 Users.|
|[`getConnectorSwagger`](connector-methods.md#getconnectorswagger-method)|Retrieves the Swagger (OpenAPI) definition for the connector.|
|[`getConnectorTableSchema`](connector-methods.md#getconnectortableschema-method)|Retrieves the schema for a table (also called an entity or list) exposed by the connector.|
|[`listConnectorDatasets`](connector-methods.md#listconnectordatasets-method)|Lists the datasets available for the connector.|
|[`listConnectorOperations`](connector-methods.md#listconnectoroperations-method)|Lists the operations exposed by a REST (operation-keyed) connector.|
|[`listConnectorTables`](connector-methods.md#listconnectortables-method)|Lists the tables available in the specified connector dataset.|
|[`queryConnectorTable`](connector-methods.md#queryconnectortable-method)|Queries a table exposed by the connector with the specified options.|
|[`retrieveConnectorRow`](connector-methods.md#retrieveconnectorrow-method)|Retrieves a single row from the specified connector table.|
|[`updateConnectorRow`](connector-methods.md#updateconnectorrow-method)|Updates an existing row in the specified connector table.|

## Dataverse action and function  methods

Use the action and function methods of the `dataApi` object to invoke [Dataverse custom APIs](../../../data-platform/custom-api.md) bound to the page.

|Method|Description|
|---|---|
|[`executeAction`](dataverse-operation-methods.md#executeaction-method)|Invokes a Dataverse custom API bound to the page as an action.|
|[`executeFunction`](dataverse-operation-methods.md#executefunction-method)|Invokes a Dataverse custom API bound to the page as a function.|
|[`listBoundActions`](dataverse-operation-methods.md#listboundactions-method)|Lists the Dataverse custom APIs (actions and functions) bound to the page.|

## Page methods

Use the page methods of the `dataApi` object to control the generative page itself, such as returning a value when the page is used as a dialog.

|Method|Description|
|---|---|
|[`setPageOutput`](page-methods.md#setpageoutput-method)|Sets the value returned to the calling script when a generative page dialog closes.|
