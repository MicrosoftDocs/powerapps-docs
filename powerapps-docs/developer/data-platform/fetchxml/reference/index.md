---
title: FetchXml reference
description: The articles in this section describe elements you use to compose a query using FetchXml. FetchXml is a proprietary XML based language that is used in Microsoft Dataverse to retrieve data.
author: pnghub
ms.author: gned
ms.reviewer: jdaly
ms.date: 02/29/2024
ms.topic: reference
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
---
# FetchXml reference

Use these elements to compose a query using FetchXml to retrieve data from Dataverse. [Learn how to query data using FetchXml](../overview.md).

Use these elements to define queries to retrieve data in the following use cases:

- Using the SDK for .NET [FetchExpression](xref:Microsoft.Xrm.Sdk.Query.FetchExpression) class with the `RetrieveMultiple` message.
- Using the Dataverse Web API as described in [Query data using FetchXml](../overview.md).
- [Using a message that has a parameter that requires a query defined using FetchXml](../overview.md#use-fetchxml-as-a-message-parameter).

This reference does not include elements or attributes used in defining views for model-driven application or reports that use FetchXml to define the query. [Learn more about customizing model-driven app views with code](../../../model-driven-apps/customize-entity-views.md).


|Element|Description|
|---|---|
|[all-attributes](all-attributes.md)|[!INCLUDE [all-attributes-description](includes/all-attributes-description.md)]|
|[attribute](attribute.md)|[!INCLUDE [attribute-description](includes/attribute-description.md)]|
|[condition](condition.md)|[!INCLUDE [condition-description](includes/condition-description.md)]|
|[entity](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[fetch](fetch.md)|[!INCLUDE [fetch-description](includes/fetch-description.md)]|
|[filter](filter.md)|[!INCLUDE [filter-description](includes/filter-description.md)]|
|[link-entity](link-entity.md)|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|
|[order](order.md)|[!INCLUDE [order-description](includes/order-description.md)]|
|[value](value.md)|[!INCLUDE [value-description](includes/value-description.md)]|

### See also

[Query data using FetchXml](../overview.md)   
[Use FetchXml to retrieve data](../retrieve-data.md)   
[Select columns using FetchXml](../select-columns.md)  
[Join tables using FetchXml](../join-tables.md)  
[Order rows using FetchXml](../order-rows.md)  
[Filter rows using FetchXml](../filter-rows.md)  
[Page results using FetchXml](../page-results.md)   
[Aggregate data using FetchXml](../aggregate-data.md)   
[Count rows using FetchXml](../count-rows.md)  
[Optimize performance using FetchXml](../optimize-performance.md)   
[FetchXml sample code](../sample.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
