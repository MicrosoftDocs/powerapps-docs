---
title: "Impersonate another user using the Web API (Common Data Service for Apps)| Microsoft Docs"
description: "Impersonation is used to execute business logic(code) on behalf of another Common Data Service for Apps user to provide a desired feature or service using the appropriate role and object-based security of that impersonated user. Read how you can impersonate another user in Common Data Service for Apps using the Web API"
ms.custom: ""
ms.date: 06/15/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 74d07683-63ff-4d05-a434-dcfd44cd634d
caps.latest.revision: 9
author: "brandonsimons" # GitHub ID
ms.author: "jdaly"
manager: "amyla"
---

<!-- TOD0: The higher level topic [Impersonate another user](../impersonate-another-user.md) should include all generic concepts.
This topic should only cover the Web API specific details -->


# Impersonate another user using the Web API

There are times when your code will need to perform operations on behalf of another user. If the system account running your code has the necessary privileges, you can perform operations on behalf of other users.  
  
<a name="bkmk_Requirementsforimpersonation"></a>

## Requirements for impersonation

Impersonation is used to execute business logic (code) on behalf of another Common Data Service for Apps user to provide a desired feature or service using the appropriate role and object-based security of that impersonated user. This is necessary because the Common Data Service for Apps Web services can be called by various clients and services on behalf of a CDS for Apps user, for example, in a workflow or custom ISV solution. Impersonation involves two different user accounts: one user account (A) is used when executing code to perform some task on behalf of another user (B).  
  
User account (A) needs the `prvActOnBehalfOfAnotherUser` privilege, which is included in the Delegate security role. The actual set of privileges that is used to modify data is the intersection of the privileges that the Delegate role user possesses with that of the user who is being impersonated. In other words, user (A) is allowed to do something if and only if user (A) and the impersonated user (B) have the privilege necessary for the action.  
  
<a name="bkmk_Howtoimpersonateauser"></a>

## How to impersonate a user

To impersonate a user, add a request header named MSCRMCallerID with a GUID value equal to the impersonated user’s systemuserid before sending the request to the web service. In this example, a new account entity is created on behalf of the user with systemuserid 00000000-0000-0000-000000000002.  
  
 **Request**  
```http 
POST [Organization URI]/api/data/v9.0/accounts HTTP/1.1  
MSCRMCallerID: 00000000-0000-0000-000000000002  
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
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#accounts(name,createdby,createdonbehalfby,owninguser,createdby(fullname),createdonbehalfby(fullname),owninguser(fullname))/$entity",  
    "@odata.etag": "W/\"506868\"",  
    "name": "Sample Account created using impersonation",  
    "accountid": "00000000-0000-0000-000000000003",  
    "createdby": {  
        "@odata.etag": "W/\"506834\"",  
        "fullname": "Impersonated User",  
        "systemuserid": "00000000-0000-0000-000000000002",  
        "ownerid": "00000000-0000-0000-000000000002"  
    },  
    "createdonbehalfby": {  
        "@odata.etag": "W/\"320678\"",  
        "fullname": "Actual User",  
        "systemuserid": "00000000-0000-0000-000000000001",  
        "ownerid": "00000000-0000-0000-000000000001"  
    },  
    "owninguser": {  
        "@odata.etag": "W/\"506834\"",  
        "fullname": "Impersonated User",  
        "systemuserid": "00000000-0000-0000-000000000002",  
        "ownerid": "00000000-0000-0000-000000000002"  
    }  
}  
```  
  
### See also

[Impersonate another user](../impersonate-another-user.md)<br />
[Impersonate another user using the Organization service](../impersonate-another-user.md#impersonate-another-user-using-the-organization-service)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Create an entity using the Web API](create-entity-web-api.md)<br />
[Retrieve an entity using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete entities using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate entities using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)
