---
title: "Web API Functions (Microsoft Dataverse)| Microsoft Docs"
description: "Describes OData Function elements defined for the Dataverse Web API."
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
# Web API Functions

Within the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document), you will find `Function` elements. Function operations are different from actions because they should not change data. They are typically used only to retrieve data.

Every function has a `Name` attribute. This name will be part of the URL when you use `HTTP` `GET`, sending any defined parameters for the function in the url of the request.

## Bound Functions

Functions may have a `IsBound="true"` attribute. This means it is a *bound* function. Functions without the `IsBound` attribute are *unbound*. A bound function means that the first parameter is a reference to a to a table record or to an entity set.

When an function is bound, it will have a reference to a specific item within the service namespace. To use the function, you must use the fully qualified name including the `Microsoft.Dynamics.CRM` namespace. More information: [Service namespace](web-api-service-documents.md#service-namespace)


## Composable functions

Functions may have a `IsComposable="true"` attribute. This means that you can append some system query options such as `$filter` or `$select` to the URL to specify the results returned. This option is only available for specific system functions. You cannot create a function using Custom API that is composable.

## Parameters

Functions usually have one or more `Parameter` elements. Each parameter will have the following attributes:

|Attribute  |Description  |
|---------|---------|
|`Name`|The name of the parameter.<br />The name is unique unless the `Function` is overloaded. More information: [Overloaded Functions](#overloaded-functions).|
|`Type`|The type of the parameter.|
|`Nullable="false"`|Whether the parameter can accept a null value|


## ReturnType

Functions MUST return values. It will always have a `ReturnType` element.

|Attribute  |Description  |
|---------|---------|
|`Type`|The type of the parameter. |
|`Nullable="false"`|Whether the value may be null.|

## Function definition examples

The following represent some examples of `Function` definitions showing different binding patterns. Each of these examples returns an integer value.

### Unbound functions

An unbound function with a single integer `Number` parameter.

```xml
<Function Name="UnBoundFunctionExample">
    <Parameter Name="Number" Type="Edm.Int32" Nullable="false" />
    <ReturnType Type="Edm.Int32" Nullable="false" />
</Function>
```

### Function bound to an entity

A function bound to the `account` entity with a single integer `Number` parameter.

```xml
<Function Name="EntityBoundFunctionExample" IsBound="true">
    <Parameter Name="entity" Type="mscrm.account" Nullable="false" />
    <Parameter Name="Number" Type="Edm.Int32" Nullable="false" />
    <ReturnType Type="Edm.Int32" Nullable="false" />
</Function>
```

### Function bound to an entity set

A function bound to the `account` EntitySet with a single integer `Number` parameter.

```xml
<Function Name="EntityCollectionBoundFunctionExample" IsBound="true">
    <Parameter Name="entityset" Type="Collection(mscrm.account)" Nullable="false" />
    <Parameter Name="Number" Type="Edm.Int32" Nullable="false" />
    <ReturnType Type="Edm.Int32" Nullable="false" />
</Function>
```

## Overloaded functions

Usually, each function you find in the $metadata will be the only function with that name. However bound functions can have multiple definitions when bound to different types. The system <xref href="Microsoft.Dynamics.CRM.RetrieveUnpublished?text=RetrieveUnpublished Function" /> and <xref href="Microsoft.Dynamics.CRM.RetrievedUnpublishedMultple?text=RetrievedUnpublishedMultple Function" /> functions are some examples. You cannot create an overloaded function using Custom API.

More information: [OData Version 4.0. Part 3: Common Schema Definition Language (CSDL) Plus Errata 03:12.2.1.1 Function Overload Rules](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part3-csdl/odata-v4.0-errata03-os-part3-csdl-complete.html#_Function_Overload_Rules)

### See also  

[Use the Dataverse Web API](overview.md)<br />
[Web API types and operations](web-api-types-operations.md)<br />
[Web API Service Documents](web-api-service-documents.md)<br />
[Web API EntityTypes](web-api-entitytypes.md)<br />
[Web API Properties](web-api-properties.md)<br />
[Web API Navigation Properties](web-api-navigation-properties.md)<br />
[Web API Actions](web-api-actions.md)<br />
[Web API Complex and Enumeration types](web-api-complex-enum-types.md)<br />
[OData Version 4.0. Part 3: Common Schema Definition Language (CSDL) Plus Errata 03 Element edm:Function](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part3-csdl/odata-v4.0-errata03-os-part3-csdl-complete.html#_Toc453752583)<br />


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
