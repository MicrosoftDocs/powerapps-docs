---
title: "Impersonate another user using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Impersonation is used to execute business logic(code) on behalf of another Microsoft Dataverse user to provide a desired feature or service using the appropriate role and object-based security of that impersonated user. Read how you can impersonate another user in Dataverse using the Web API"
ms.date: 04/06/2022
author: MsSQLGirl
ms.author: sriknair
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

<!-- TOD0: The higher level topic [Impersonate another user](../impersonate-another-user.md) should include all generic concepts.
This topic should only cover the Web API specific details -->

# Impersonate another user using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

There are times when your code needs to perform operations on behalf of another user. If the system account running your code has the necessary privileges, you can perform operations on behalf of other users.  
  
<a name="bkmk_Requirementsforimpersonation"></a>

## Requirements for impersonation

Impersonation is used to execute business logic (code) on behalf of another Microsoft Dataverse user to provide a desired feature or service using the appropriate role and object-based security of that impersonated user. Impersonation is necessary because the Dataverse Web services can be called by various clients and services on behalf of a Dataverse user, for example, in a workflow or custom ISV (Independent Software Vendor) solution. Impersonation involves two different user accounts: one user account (A) is used when executing code to perform some task on behalf of another user (B).  
  
User account (A) needs the `prvActOnBehalfOfAnotherUser` privilege, which is included in the Delegate security role. The actual set of privileges that is used to modify data is the intersection of the privileges that the Delegate role user possesses with that of the user who is being impersonated. In other words, user (A) is allowed to do something if and only if user (A) and the impersonated user (B) have the privilege necessary for the action.  
  
<a name="bkmk_Howtoimpersonateauser"></a>

## How to impersonate a user

There are two ways you can impersonate a user, both of which are made possible by passing in a header with the corresponding user ID.

1. **Preferred:** Impersonate a user based on their Microsoft Entra ID object ID by passing that value along with the header `CallerObjectId`.
1. **Legacy:** To impersonate a user based on their systemuserid, you can use `MSCRMCallerID` with the corresponding guid value.

 In this example, a new account entity is created on behalf of the user with a Microsoft Entra ID object ID `aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb`.
  
 **Request:**

```http 
POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1  
CallerObjectId: aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{"name":"Sample Account created using impersonation"}  
```  
  
 **Response:**

```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-000000000003)  
```  
  
<a name="bkmk_Determinetheactualuser"></a>

## Determine the actual user

When an operation such as creating an entity is performed using impersonation, you can find the user who actually performed the operation by querying the record including the `createdonbehalfby` single-valued navigation property. A corresponding `modifiedonbehalfby` single-valued navigation property is available for operations that update the entity.  
  
 **Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-000000000003)?$select=name&$expand=createdby($select=fullname),createdonbehalfby($select=fullname),owninguser($select=fullname) HTTP/1.1   
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
ETag: W/"506868"  
  
{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,createdby(fullname,azureactivedirectoryobjectid),createdonbehalfby(fullname,azureactivedirectoryobjectid),owninguser(fullname,azureactivedirectoryobjectid))/$entity",
  "@odata.etag": "W/\"2751197\"",
  "name": "Sample Account created using impersonation",
  "accountid": "00000000-0000-0000-000000000003",
  "createdby": {
    "@odata.etag": "W/\"2632435\"",
    "fullname": "Impersonated User",
    "azureactivedirectoryobjectid": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
    "systemuserid": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee",
    "ownerid": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee"
  },
  "createdonbehalfby": {
    "@odata.etag": "W/\"2632445\"",
    "fullname": "Actual User",
    "azureactivedirectoryobjectid": "bbbbbbbb-1111-2222-3333-cccccccccccc",
    "systemuserid": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
    "ownerid": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff"
  },
  "owninguser": {
    "@odata.etag": "W/\"2632435\"",
    "fullname": "Impersonated User",
    "azureactivedirectoryobjectid": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
    "systemuserid": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee",
    "ownerid": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee"
  }
}
```  
  
### See also

[Impersonate another user](../impersonate-another-user.md)<br />
[Impersonate another user using the SDK for .NET](../impersonate-another-user.md#impersonate-another-user-using-the-sdk-for-net)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query/overview.md)<br />
[Create a table row using the Web API](create-entity-web-api.md)<br />
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
