---
title: "Impersonate another user using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Impersonation is used to execute business logic(code) on behalf of another Microsoft Dataverse user to provide a desired feature or service using the appropriate role and object-based security of that impersonated user. Read how you can impersonate another user in Dataverse using the Web API"
ms.custom: ""
ms.date: 05/04/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 74d07683-63ff-4d05-a434-dcfd44cd634d
caps.latest.revision: 9
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

<!-- TOD0: The higher level topic [Impersonate another user](../impersonate-another-user.md) should include all generic concepts.
This topic should only cover the Web API specific details -->

# Impersonate another user using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

There are times when your code will need to perform operations on behalf of another user. If the system account running your code has the necessary privileges, you can perform operations on behalf of other users.  
  
<a name="bkmk_Requirementsforimpersonation"></a>

## Requirements for impersonation

Impersonation is used to execute business logic (code) on behalf of another Microsoft Dataverse user to provide a desired feature or service using the appropriate role and object-based security of that impersonated user. This is necessary because the Dataverse Web services can be called by various clients and services on behalf of a Dataverse user, for example, in a workflow or custom ISV solution. Impersonation involves two different user accounts: one user account (A) is used when executing code to perform some task on behalf of another user (B).  
  
User account (A) needs the `prvActOnBehalfOfAnotherUser` privilege, which is included in the Delegate security role. The actual set of privileges that is used to modify data is the intersection of the privileges that the Delegate role user possesses with that of the user who is being impersonated. In other words, user (A) is allowed to do something if and only if user (A) and the impersonated user (B) have the privilege necessary for the action.  
  
<a name="bkmk_Howtoimpersonateauser"></a>

## How to impersonate a user

There are two ways you can impersonate a user, both of which are made possible by passing in a header with the corresponding user id.

 1. **Preferred:** Impersonate a user based on their Azure Active Directory (AAD) object id by passing that value along with the header `CallerObjectId`.
2. **Legacy:** To impersonate a user based on their systemuserid you can leverage `MSCRMCallerID` with the corresponding guid value.

 In this example, a new account entity is created on behalf of the user with an Azure Active Directory object id `e39c5d16-675b-48d1-8e67-667427e9c084`.   
  
 **Request**  
```http 
POST [Organization URI]/api/data/v9.0/accounts HTTP/1.1  
CallerObjectId: e39c5d16-675b-48d1-8e67-667427e9c084  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{"name":"Sample Account created using impersonation"}  
```  
  
 **Response**  
```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-000000000003)  
```  
  
<a name="bkmk_Determinetheactualuser"></a>

## Determine the actual user

When an operation such as creating an entity is performed using impersonation, the user who actually performed the operation can be found by querying the record including the `createdonbehalfby` single-valued navigation property. A corresponding modifiedonbehalfby single-valued navigation property is available for operations that update the entity.  
  
 **Request**

```http 
GET [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-000000000003)?$select=name&$expand=createdby($select=fullname),createdonbehalfby($select=fullname),owninguser($select=fullname) HTTP/1.1   
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response**  
```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
ETag: W/"506868"  
  
{
  "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#accounts(name,createdby(fullname,azureactivedirectoryobjectid),createdonbehalfby(fullname,azureactivedirectoryobjectid),owninguser(fullname,azureactivedirectoryobjectid))/$entity",
  "@odata.etag": "W/\"2751197\"",
  "name": "Sample Account created using impersonation",
  "accountid": "00000000-0000-0000-000000000003",
  "createdby": {
    "@odata.etag": "W/\"2632435\"",
    "fullname": "Impersonated User",
    "azureactivedirectoryobjectid": "e39c5d16-675b-48d1-8e67-667427e9c084",
    "systemuserid": "75df116d-d9da-e711-a94b-000d3a34ed47",
    "ownerid": "75df116d-d9da-e711-a94b-000d3a34ed47"
  },
  "createdonbehalfby": {
    "@odata.etag": "W/\"2632445\"",
    "fullname": "Actual User",
    "azureactivedirectoryobjectid": "3d8bed3e-79a3-47c8-80cf-269869b2e9f0",
    "systemuserid": "278742b0-1e61-4fb5-84ef-c7de308c19e2",
    "ownerid": "278742b0-1e61-4fb5-84ef-c7de308c19e2"
  },
  "owninguser": {
    "@odata.etag": "W/\"2632435\"",
    "fullname": "Impersonated User",
    "azureactivedirectoryobjectid": "e39c5d16-675b-48d1-8e67-667427e9c084",
    "systemuserid": "75df116d-d9da-e711-a94b-000d3a34ed47",
    "ownerid": "75df116d-d9da-e711-a94b-000d3a34ed47"
  }
}
```  
  
### See also

[Impersonate another user](../impersonate-another-user.md)<br />
[Impersonate another user using the Organization service](../impersonate-another-user.md#impersonate-another-user-using-the-organization-service)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Create a table using the Web API](create-entity-web-api.md)<br />
[Retrieve a table using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete tables using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate tables using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]