---
title: "Work with an Azure Active Directory group team (Dataverse)| Microsoft Docs"
description: "Learn about working with an Azure Active Directory group team using the Web API."
ms.custom: ""
ms.date: 03/10/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 767f39d4-6a8e-48f0-bf7d-69ea1191acef
caps.latest.revision: 8
author: "paulliew" # GitHub ID
ms.author: "paulliew" # MSFT alias of Microsoft employees only
manager: "sunilg" # MSFT alias of manager or PM counterpart
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Work with an Azure Active Directory group team

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

<!-- TODO: Describe what the AAD group team is, and what it is used for -->

## Creating an AAD group team

Citizen developers wanting to programatically create a Microsoft Dataverse AAD group team can do so by providing the object ID of an existing AAD group as shown in the following HTTP command.

```http
POST https://<service-root>/api/data/v9.2/teams

Body:
{
  "azureactivedirectoryobjectid":"<object ID>",
  "membershiptype":0
}
```

## Security roles and privileges

Members of an AAD group can query all the security roles that are directly and indirectly assigned to them using the following HTTP command.

```http
GET https://<service-root>/api/data/v9.2/RetrieveAadUserRoles(DirectoryObjectId=<object ID)?$select=_parentrootroleid_value,name

RESPONSE
{
  "@odata.context": "https://contoso.crm2.dynamics.com/api/data/v9.2/$metadata#roles",
  "value": [
    {
      "@odata.etag": "W/\"1649865\"",
      "name": "System Administrator",
      "roleid": "ae0daa93-e566-eb11-bb2b-000d3ac4c3f6",
      "_parentrootroleid_value": "ae0daa93-e566-eb11-bb2b-000d3ac4c3f6",
      "t_x002e_azureactivedirectoryobjectid": "e1341054-98ed-489b-a522-15e9e277b737",
      "t_x002e_membershiptype": 0,
      "t_x002e_teamid": "26e477f8-3f6a-eb11-bb2b-000d3af6caae",
      "t_x002e_name": "testgroup"
    }
  ]
}
```

Members of an AAD group can check their security privileges without being a user of Dataverse using the following HTTp command.

```http
GET https://<service-root>/api/data/v9.2/RetrieveAadUserPrivileges(DirectoryObjectId=<object ID>)

RESPONSE
{
  "@odata.context": "https://contoso.crm2.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveAadUserPrivilegesResponse",
  "RolePrivileges": [
    {
      "Depth": "Global",
      "PrivilegeId": "0a620778-3e9f-46ec-9766-000624db57ba",
      "BusinessUnitId": "aa0daa93-e566-eb11-bb2b-000d3ac4c3f6",
      "PrivilegeName": "prvDeleteHierarchyRule"
    },
    …
   ]
}
```

## Assigning and sharing

An administrator can assign (share) a record for an AAD group member without the user being in Dataverse using the following HTTp command.

```http
PATCH https://<service-root>/api/data/v9.2/accounts(<account ID>)

Body
{ 
  "ownerid@odata.bind": "https://<service-root>/api/data/v9.2/systemusers(azureactivedirectoryobjectid=<AAD object ID>)"
}
```

An administrator can assign a security role to an AAD user or AAD group without the user or group being in Dataverse.

```http
POST https://<service-root>/api/data/v9.2/teams(azureactivedirectoryobjectid=<user or group object ID>,membershiptype=0)/teamroles_association/$ref

Body
{ 
  "@odata.id":"https://<service-root>/api/data/v9.2/roles(<role ID>)"
}
```

### See also


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]