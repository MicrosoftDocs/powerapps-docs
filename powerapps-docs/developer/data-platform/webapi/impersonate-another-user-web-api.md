---
title: "Impersonate another user using the Microsoft Dataverse Web API"
description: "Learn how to impersonate another user in Microsoft Dataverse using the Web API. Execute business logic on behalf of another user with appropriate role and object-based security. Includes code examples and requirements."
ms.date: 03/27/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

<!-- 

TODO: This content should be incorporated into a single higher level article [Impersonate another user](../impersonate-another-user.md). There should be just one article, not three.

-->

# Impersonate another user by using the Web API

Sometimes your code needs to perform operations on behalf of another user. If the system account running your code has the necessary privileges, it can perform operations on behalf of other users.  
  
<a name="bkmk_Requirementsforimpersonation"></a>

## Requirements for impersonation

Use impersonation to execute business logic (code) on behalf of another Microsoft Dataverse user to provide a desired feature or service by using the appropriate role and object-based security of the impersonated user. The Dataverse Web services can be called by various clients and services on behalf of a Dataverse user, for example, in a workflow or custom ISV (Independent Software Vendor) solution. Impersonation involves two different user accounts: one user account (A) is used when executing code to perform some task on behalf of another user (B).  
  
User account (A) needs the `prvActOnBehalfOfAnotherUser` privilege, which the Delegate security role includes. The actual set of privileges that is used to modify data is the intersection of the privileges that the Delegate role user possesses with that of the user who is being impersonated. In other words, user (A) is allowed to do something if and only if user (A) and the impersonated user (B) have the privilege necessary for the action.  
  
<a name="bkmk_Howtoimpersonateauser"></a>

## How to impersonate a user

You can impersonate a user in two ways. Both methods work by passing a header with the corresponding user ID.

1. **Preferred:** Impersonate a user based on their Microsoft Entra ID object ID by passing that value along with the header `CallerObjectId`.
1. **Legacy:** To impersonate a user based on their systemuserid, use `MSCRMCallerID` with the corresponding GUID value.

 In this example, you create a new account entity on behalf of the user with a Microsoft Entra ID object ID `aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb`.
  
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

When you perform an operation such as creating an entity by using impersonation, you can find the user who actually performed the operation by querying the record including the `createdonbehalfby` single-valued navigation property. A corresponding `modifiedonbehalfby` single-valued navigation property is available for operations that update the entity.  
  
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

[Impersonate another user](../impersonate-another-user.md)   
[Impersonate another user using the SDK for .NET](../impersonate-another-user.md#impersonate-another-user-using-the-sdk-for-net)   
[Perform operations using the Web API](perform-operations-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
