---
title: FetchXml reference
description: The articles in this section describe elements you use to compose a query using FetchXml. FetchXml is a proprietary XML based language that is used in Microsoft Dataverse to retrieve data.
author: pnghub
ms.author: gned
ms.reviewer: jdaly
ms.date: 08/31/2023
ms.topic: reference
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# FetchXml reference

Use these elements to compose a query using FetchXml to retrieve data from Dataverse. To learn how to use these elements, see [Query data using FetchXml](../overview.md).

> [!NOTE]
> These elements are a subset of the elements described in the [FetchXml schema](../../fetchxml-schema.md). Use these elements to define queries to retrieve data in the following use cases:
>
> - Using the SDK for .NET [FetchExpression](xref:Microsoft.Xrm.Sdk.Query.FetchExpression) class with the `RetrieveMultiple` message.
> - Using the Dataverse Web API as described in [Use FetchXml with Web API](../../webapi/use-fetchxml-web-api.md).
> - Using a message that has a parameter that requires a query defined using FetchXml.
> 
> This reference does not include elements defined in the [FetchXml schema](../../fetchxml-schema.md) used in defining views for model-driven application or reports that use FetchXml to define the query.


|Element|Description|
|---|---|
|[all-attributes element](all-attributes.md)|[!INCLUDE [all-attributes-description](includes/all-attributes-description.md)]|
|[attribute element](attribute.md)|[!INCLUDE [attribute-description](includes/attribute-description.md)]|
|[condition element](condition.md)|[!INCLUDE [condition-description](includes/condition-description.md)]|
|[entity element](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[fetch element](fetch.md)|[!INCLUDE [fetch-description](includes/fetch-description.md)]|
|[filter element](filter.md)|[!INCLUDE [filter-description](includes/filter-description.md)]|
|[link-entity element](link-entity.md)|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|
|[order element](order.md)|[!INCLUDE [order-description](includes/order-description.md)]|
|[value element](value.md)|[!INCLUDE [value-description](includes/value-description.md)]|
