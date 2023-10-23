---
title: "Azure Active Directory user (AADUser) table (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "An Azure Active Directory user virtual table in Microsoft Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/20/2022
ms.reviewer: "pehecke"
ms.topic: "article"
author: "NHelgren" # GitHub ID
ms.service: powerapps
ms.subservice: dataverse-developer
ms.author: "nhelgren" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---
# Azure Active Directory user table

> [!NOTE]
> Azure Active Directory is now Microsoft Entra ID. [Learn more](/azure/active-directory/fundamentals/new-name)

Microsoft Dataverse includes a virtual table named AAD user (aaduser). This virtual table provides a connection to Azure Active Directory (AAD) and returns data about users within your AAD organization. No virtual table configuration is required to use the functionality. This is an online only feature.

> [!NOTE]
> Your results with AAD User may differ depending on where it is being used. AAD User in Dataverse will provide the full list of users on the Azure AD for the organization. AAD User in Dataverse for Teams is limited to providing all AAD Users who are also a member of the Team.
> 
> AAD User does not return groups or distribution lists.

## Lookups using AADUser

You can easily add a lookup to this virtual table from within the Power Apps portal.

:::image type="content" source="media/add-lookup-aaduser.png" alt-text="Create a lookup column with a related table of AADUser":::

## Permissions

The AADUser table functions using Microsoft Graph. Users in your organization need to be assigned Graph permissions in order to view and use the AADUser virtual table.

## Allowed operations

Only read and read-multiple operations are possible through the AADUser virtual table.

## AADUser table Web API examples

This section contains `HTTP` `GET` examples for accessing data from the AADUser table.

### Retrieving data

The following example demonstrate retrieving data from the AADUser table.

**Retrieve all AADUser table rows**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers  
```

**Retrieve AADUser records with surname 'admin'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=surname eq 'admin'
```

**Retrieve AADUser records with surname 'admin' or 'admin02'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=(surname eq 'Admin02') or (surname eq 'Admin')
```

**Retrieve AADUser records whose companyname is not null**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=companyname ne null
```

**Retrieve AADUser records whose usertype is 'Member'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=usertype eq 'Member'
```

**Retrieve AADUser records whose businessphones contains is '123-555-1212'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=contains(businessphones, '123-555-1212')
```

**Retrieve AADUser records whose givenname starts with 'test'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=startswith(givenname, 'test')
```

**Retrieve AADUser records whose givenname does NOT starts with 'test'**

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers?$filter=not startswith(givenname, 'test')
```

**Retrieve related Account records that referencing an AADUser record**  

Below, `new_aaduser_account` is the name of the 1:N relationship between the AADUser and the Account entity.

```http
https://[Organization URI].crm.dynamics.com/api/data/v9.1/aadusers(<user ID>)?$expand=new_aaduser_account($select=accountid,name)
```

### Referencing an AADUser row

The following example demonstrates referencing an AADUser table row.

**Set lookup field value referencing an AADUser row**  

In this example `new_testaaduserId` is the single-valued navigation property created with a custom 1:N relationship between AADUser and Account entity.  The name of this navigation property is defined in the  <xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.ReferencingEntityNavigationPropertyName?text=OneToManyRelationshipMetadata.ReferencingEntityNavigationPropertyName> property of the relationship. More information: [Single-valued navigation properties](webapi/web-api-navigation-properties.md#single-valued-navigation-properties)

```http
PATCH
https://[Organization URI].crm.dynamics.com/api/data/v9.0/accounts(<account ID>)
{
  new_testaaduserId@odata.bind : "/aadusers(user ID)"
}
```

### See also

[aaduser table/entity reference](reference/entities/aaduser.md)<br />
<xref:Microsoft.Dynamics.CRM.aaduser?text=aaduser EntityType reference><br />
[Security and data access](security-model.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
