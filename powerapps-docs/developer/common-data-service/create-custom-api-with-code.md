---
title: "Create a Custom API with code (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can write code create custom APis." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/19/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Create a Custom API with code

[This topic is pre-release documentation and is subject to change.]

> [!NOTE]
> This is an advanced topic that assumes you have already read and understood these topics:
> - [Create and use Custom APIs](custom-api.md)
> - [Create a Custom API in the maker portal](create-custom-api-maker-portal.md)
>
> You should also understand how to create Common Data Service records, using either the Web API or Organization Service. For more information see:
> - [Create an entity record using the Web API](webapi/create-entity-web-api.md)
> - [Create entities using the Organization Service](org-service/entity-operations-create.md)

Because Custom API data is saved in entities, you can programmatically create new APIs using either the Web API or the Organization Service.

The tables in [Create and use Custom APIs](custom-api.md) describe all the properties you can set using code. For the following code examples, please refer to the following tables:

- [CustomAPI entity attributes](custom-api.md#customapi-entity-attributes)
- [CustomAPIRequestParameter entity attributes](custom-api.md#customapirequestparameter-entity-attributes)
- [CustomAPIResponseProperty entity attributes](custom-api.md#customapiresponseproperty-entity-attributes)

## Create a Custom API using the Web API

## Create a Custom API using the Web API