---
title: "Web API Actions (Microsoft Dataverse)| Microsoft Docs"
description: "Describes OData Action elements defined for the Dataverse Web API."
ms.custom: ""
ms.date: 11/24/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)" 
author: "JimDaly" # GitHub ID
ms.author: pehecke
manager: "sunilg"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Web API Actions

Within the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document), you will find `Action` elements that describe operations that change data.

Every action has a `Name` attribute. This name will be part of the URL when you use `HTTP` `POST`, sending any defined parameters for the action in the body of the request.

## Bound actions

Actions may have a `IsBound="true"` attribute. This means it is a *bound* action. Actions without the `IsBound` attribute are *unbound*. A bound action means that the first parameter is a reference to a to a table record or to an entity set.

When an action is bound, it will have a reference to a specific item within the service namespace. To use the action, you must use the fully qualified name including the `Microsoft.Dynamics.CRM` namespace. More information: [Service namespace](web-api-service-documents.md#service-namespace)

## Parameters

Actions usually have one or more `Parameter` elements. Each parameter will have the following attributes:


|Attribute  |Description  |
|---------|---------|
|`Name`|The name of the parameter.<br />The name is unique unless the `Action` is overloaded. More information: [Overloaded Actions](#overloaded-actions).|
|`Type`|The type of the parameter.|
|`Nullable="false"`|Whether the parameter can accept a null value|


## ReturnType

Actions may return values. When an action returns a value, it will have a `ReturnType` element.

|Attribute  |Description  |
|---------|---------|
|`Type`|The type of the parameter. |
|`Nullable="false"`|Whether the value may be null.|

## Action definition examples

The following represent some examples of `Action` definitions showing different binding patterns. Each of these examples returns an integer value.

### Unbound actions

An unbound action with a single integer `Number` parameter.

```xml
<Action Name="UnBoundActionExample">
    <Parameter Name="Number" Type="Edm.Int32" Nullable="false" />
    <ReturnType Type="Edm.Int32" Nullable="false" />
</Action>

```

### Action bound to an entity

An action bound to the `account` entity with a single integer `Number` parameter.

```xml
<Action Name="EntityBoundActionExample" IsBound="true">
    <Parameter Name="entity" Type="mscrm.account" Nullable="false" />
    <Parameter Name="Number" Type="Edm.Int32" Nullable="false" />
    <ReturnType Type="Edm.Int32" Nullable="false" />
</Action>

```

### Action bound to an entity set

An action bound to the `account` EntitySet with a single integer `Number` parameter.

```xml
<Action Name="EntityCollectionBoundActionExample" IsBound="true">
    <Parameter Name="entityset" Type="Collection(mscrm.account)" Nullable="false" />
    <Parameter Name="Number" Type="Edm.Int32" Nullable="false" />
    <ReturnType Type="Edm.Int32" Nullable="false" />
</Action>


```

## Overloaded Actions

Usually, each action you find in the $metadata will be the only action with that name. However bound actions can have multiple definitions when bound to different types. The `AddItemCampaign` action included the marketing solution is one example. You cannot create an overloaded action using Custom API.

More information: [OData Version 4.0. Part 3: Common Schema Definition Language (CSDL) Plus Errata 03: 12.1.1.1 Action Overload Rules](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part3-csdl/odata-v4.0-errata03-os-part3-csdl-complete.html#_Toc451407830)

### See also  

[Use the Dataverse Web API](overview.md)<br />
[Web API types and operations](web-api-types-operations.md)<br />
[Web API Service Documents](web-api-service-documents.md)<br />
[Web API EntityTypes](web-api-entitytypes.md)<br />
[Web API Properties](web-api-properties.md)<br />
[Web API Navigation Properties](web-api-navigation-properties.md)<br />
[Web API Functions](web-api-functions.md)<br />
[Web API Complex and Enumeration types](web-api-complex-enum-types.md)<br />
[OData Version 4.0. Part 3: Common Schema Definition Language (CSDL) Plus Errata 03 Element edm:Action](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part3-csdl/odata-v4.0-errata03-os-part3-csdl-complete.html#_Toc453752579)<br />


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
