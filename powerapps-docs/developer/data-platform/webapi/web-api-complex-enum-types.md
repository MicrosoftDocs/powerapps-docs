---
title: "Web API Complex and Enumeration types (Microsoft Dataverse)| Microsoft Docs"
description: "Describes OData Complex and Enumeration types elements defined for the Dataverse Web API."
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
# Web API Complex and Enumeration types

Within the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document), you will find `ComplexType` and `EnumType` elements.

## Complex types

Complex types are keyless named structured types consisting of a set of properties. Complex types are commonly used as property values in table definitions, or as parameters or return values for operations.

For example the <xref href="Microsoft.Dynamics.CRM.WhoAmI?text=WhoAmI Function" />  returns this <xref href="Microsoft.Dynamics.CRM.WhoAmIResponse?text=WhoAmIResponse ComplexType" />:

```xml
<ComplexType Name="WhoAmIResponse">  
  <Property Name="BusinessUnitId" Type="Edm.Guid" Nullable="false" />  
  <Property Name="UserId" Type="Edm.Guid" Nullable="false" />  
  <Property Name="OrganizationId" Type="Edm.Guid" Nullable="false" />  
</ComplexType>
```

## Enumeration types

Enumeration types are named primitive types whose values are named constants with underlying integer values.

For example, the following is the definition of the <xref href="Microsoft.Dynamics.CRM.AccessRights?text=AccessRights EnumType" />

```xml
<EnumType Name="AccessRights">  
  <Member Name="None" Value="0" />  
  <Member Name="ReadAccess" Value="1" />  
  <Member Name="WriteAccess" Value="2" />  
  <Member Name="AppendAccess" Value="4" />  
  <Member Name="AppendToAccess" Value="16" />  
  <Member Name="CreateAccess" Value="32" />  
  <Member Name="DeleteAccess" Value="65536" />  
  <Member Name="ShareAccess" Value="262144" />  
  <Member Name="AssignAccess" Value="524288" />  
</EnumType>
```

The `AccessRights` enum type is used for the `AccessMask` property of the <xref href="Microsoft.Dynamics.CRM.PrincipalAccess?text=PrincipalAccess ComplexType" />, which is used to set the `PrincipalAccess` parameter for the <xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />. This is the action used to change the access when sharing a record.
The example below grants `ReadAccess`, `WriteAccess`, `DeleteAccess`, `AppendAccess`, and `AssignAccess` access rights to the `account` record specified by the `Target` parameter to the `systemuser` designated by the `Principal` property of the `PrincipalAccess` complex type.

**Request**

```http
POST [Organization URI]/api/data/v9.0/ModifyAccess
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json; charset=UTF-8
Accept: application/json

{
    "Target": {
        "accountid": "cbcf8bbc-aa41-ec11-8c62-000d3a53893c",
        "@odata.type": "Microsoft.Dynamics.CRM.account"
    },
    "PrincipalAccess": {
        "Principal": {
            "systemuserid": "8061643d-ebf7-e811-a974-000d3a1e1c9a",
            "@odata.type": "Microsoft.Dynamics.CRM.systemuser"
        },
        "AccessMask": "ReadAccess,WriteAccess,DeleteAccess,AppendAccess,AssignAccess"
    }
}
```

**Response**

```http
HTTP/1.1 204 No Content
```

### See also  

[Use the Dataverse Web API](overview.md)<br />
[Web API types and operations](web-api-types-operations.md)<br />
[Web API Service Documents](web-api-service-documents.md)<br />
[Web API EntityTypes](web-api-entitytypes.md)<br />
[Web API Properties](web-api-properties.md)<br />
[Web API Navigation Properties](web-api-navigation-properties.md)<br />
[Web API Actions](web-api-actions.md)<br />
[OData Version 4.0. Part 3: Common Schema Definition Language (CSDL) Plus Errata 03 9.1 9 Complex Type](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part3-csdl/odata-v4.0-errata03-os-part3-csdl-complete.html#_Complex_Type)<br />
[OData Version 4.0. Part 3: Common Schema Definition Language (CSDL) Plus Errata 03 9.1 10 Enumeration Type](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part3-csdl/odata-v4.0-errata03-os-part3-csdl-complete.html#_Enumeration_Type)<br />


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]