---
title: "Work with Azure Active Directory group teams (Dataverse)| Microsoft Docs"
description: "Learn about working with an Azure Active Directory group team using the Web API."
ms.custom: ""
ms.date: 02/15/2022

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 767f39d4-6a8e-48f0-bf7d-69ea1191acef
caps.latest.revision: 8
author: "paulliew" # GitHub ID
ms.author: "paulliew" # MSFT alias of Microsoft employees only
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
---

# Work with Azure Active Directory group teams

An Azure Active Directory (AAD) group team, similar to an owner team, can own records and can have security roles assigned to the team. To read more about AAD group teams see [Manage group teams](/power-platform/admin/manage-group-teams).

## Just-in-time updates
Just-in-time updates mean that the actions are taken at run-time to eliminate the need for syncing data from Azure Active Directory and Microsoft Dataverse. These actions include creating AAD group teams, adding/removing AAD group members from AAD group teams, and adding users into Dataverse.

1. If the AAD group team doesn't exist and a security role is assigned or a record is assigned to the AAD group, the AAD group team is created just-in-time.

2. When an AAD group member accesses Dataverse interactively or through a non-interactive process makes a call on behalf of the user, the group member is added into the AAD group team at run-time. Similarly, when a member who was removed from the AAD group accesses Dataverse interactively or by a non-interactive process call, the group member is removed from the AAD group team.

3. When an AAD group member accesses Dataverse interactively or through a non-interactive process makes a call on behalf of the user, and the user doesn't exist in Dataverse, the user is added in Dataverse just-in-time.

The following sections describe how to work with AAD group teams using the Web API. 

## Impersonate another user
Your service can make calls on behalf of another system user by [impersonating the user](impersonate-another-user.md#impersonate-another-user-using-the-web-api). If the system user belongs to an AAD Security group and the AAD security group is a Dataverse group team, that user is added into Dataverse automatically (if the user doesn't already exist in Dataverse). The user is also automatically added into the Dataverse group team after being added to Dataverse or if the user already exists in Dataverse.

## Create an AAD group team
An AAD group team can be created in Dataverse by making an API call (programmatically) or by just-in-time when a security role is assigned to the AAD group, or when a record is assigned to the AAD group. 

Citizen developers wanting to programmatically create a Microsoft Dataverse AAD group team can do so by providing the object ID of an existing AAD group as shown in the following command.

**Request:**

```http
POST [Organization URI]/api/data/v9.0/teams
Accept: application/json

{
  "azureactivedirectoryobjectid":"<group object ID>",
  "membershiptype":0
}
```

Where:

- Membership type is defined in the [team property](/dynamics365/customer-engagement/web-api/team#properties) `membershiptype`
- Name of the team is the name of the AAD group
- Team type is based on the AAD group type - for example "Security" or "Microsoft 365"

## Assign a security role to an AAD group team

An administrator can assign a security role to an AAD group team after the AAD group is created in AAD. The AAD group team is created into Dataverse automatically if it doesn't exist in Dataverse.

**Request:**

```http
POST [Organization URI]/api/data/v9.0/teams(azureactivedirectoryobjectid=<group team ID>,membershiptype=0)/teamroles_association/$ref
Accept: application/json

{ 
  "@odata.id":"[Organization URI]/api/data/v9.0/roles(<role ID>)"
}
```

## Assign a security role to a user

An administrator can assign a security role to an AAD group user.  The user is added into Dataverse automatically if the user doesn't exist in Dataverse and the role is assigned directly to the user.

**Request:**

```http
POST [Organization URI]/api/data/v9.0/systemusers(azureactivedirectoryobjectid=<user object ID>)/systemuserroles_association/$ref
Accept: application/json

{ 
  "@odata.id":"[Organization URI]/api/data/v9.0/roles(<role ID>)"
}
```
## Assign a record to an AAD group

An administrator can assign a record to an AAD group.  The AAD group team is created into Dataverse automatically if it doesn't exist in Dataverse.

The example below shows the syntax for assigning an account record.

**Request:**

```http
PATCH [Organization URI]/api/data/v9.0/accounts(<account ID>)
Accept: application/json

{ 
  "ownerid@odata.bind": "[Organization URI]/api/data/v9.0/teams(azureactivedirectoryobjectid=<group object ID>,membershiptype:0)"
}
```

## Assign a record to an AAD group member

An administrator can assign a record to an AAD group member.  The AAD group member is added into Dataverse automatically if the user doesn't exist in Dataverse.

The example below shows the syntax for assigning an account record.

**Request:**

```http
PATCH [Organization URI]/api/data/v9.0/accounts(<account ID>)
Accept: application/json

{ 
  "ownerid@odata.bind": "[Organization URI]/api/data/v9.0/systemusers(azureactivedirectoryobjectid=<user object ID>)"
}
```
<!-- ## Share a record to an AAD group 

"An administrator or a record owner can share a record to an AAD group. The AAD group team is created into Dataverse automatically if it doesn't exist in Dataverse.

The example below shows the syntax for sharing an account record.

**Request:**

```http
POST [Organization URI]/api/data/v9.0/GrantAccess
Accept: application/json

{
  "Target":{
    "accountid":"<account ID>",
    "@odata.type":"Microsoft.Dynamics.CRM.account"
  },
  "PrincipalAccess":{
    "Principal":{
      "@odata.id":"[Organization URI]/api/data/v9.0/teams(azureactivedirectoryobjectid=<group object ID>,membershiptype:0)"
    },
    "AccessMask":"ReadAccess"
  }
}
``` -->

<!-- ## Share a record to an AAD group member

"An administrator or a record owner can share a record to an AAD group member. The AAD group member is added into Dataverse automatically if the user doesn't exist in Dataverse.

The example below shows the syntax for sharing an account record.

**Request:**

```http
POST [Organization URI]/api/data/v9.0/GrantAccess
Accept: application/json

{
  "Target":{
    "accountid":"<account ID>",
    "@odata.type":"Microsoft.Dynamics.CRM.account"
  },
  "PrincipalAccess":{
    "Principal":{
      "@odata.id":"[Organization URI]/api/data/v9.0/systemusers(azureactivedirectoryobjectid=<user object ID>)"
    },
    "AccessMask":"ReadAccess"
  }
}
``` -->

## Retrieve a user

You can retrieve a system user table row using an Azure user object identifier (ID). If the system user doesn't exist in Dataverse, the user is added to Dataverse automatically and added into the Dataverse group team if the user belongs to an AAD group that exists in Dataverse. **If the user exists in Dataverse, the user is not added to the Dataverse group team.** 

The example below shows the syntax for retrieving a user row.

**Request:**

```http
GET [Organization URI]/api/data/v9.0/SystemUser(azureactivedirectoryobjectid=<user object ID>)
```

## Security roles and privileges

Members of an AAD group can query all the security roles that are directly and indirectly assigned to them using the following command.

**Request:**

```http
GET [Organization URI]/api/data/v9.0/RetrieveAadUserRoles(DirectoryObjectId=<user object ID)?$select=_parentrootroleid_value,name
```

**Response:**

```json
{
  "@odata.context": "https://contoso.crm2.dynamics.com/api/data/v9.0/$metadata#roles",
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

Members of an AAD group can check their security privileges without being a user of Dataverse using the following command.

**Request:**

```http
GET [Organization URI]/api/data/v9.0/RetrieveAadUserPrivileges(DirectoryObjectId=<user object ID>)
```

**Response:**

```json
{
  "@odata.context": "https://contoso.crm2.dynamics.com/api/data/v9.0/$metadata#Microsoft.Dynamics.CRM.RetrieveAadUserPrivilegesResponse",
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

## Checking user or team's access rights on a record

If you have a non-interactive process where your service needs to check if the user has access rights to a record, you can make a [RetrievePrincipalAccess function](/dynamics365/customer-engagement/web-api/retrieveprincipalaccess) call on behalf of the user by specifying the `CallerID`.

More information: [Impersonate another user](impersonate-another-user.md)

### See also

[Manage app and resource access using Azure Active Directory groups](/azure/active-directory/fundamentals/active-directory-manage-groups)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
