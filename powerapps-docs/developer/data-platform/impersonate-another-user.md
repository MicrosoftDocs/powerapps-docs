---
title: "Impersonate another user (Microsoft Dataverse) | Microsoft Docs"
description: "Use impersonation to execute business logic on behalf of another Microsoft Dataverse user." 
ms.date: 10/29/2026
ai-usage: ai-assisted
ms.reviewer: pehecke
ms.topic: article
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---
# Impersonate another user

Use impersonation to execute business logic on behalf of another Microsoft Dataverse user. By using the appropriate role and object-based security of the impersonated user, you can provide a desired feature or service.

Various clients and services can use impersonation to call the Dataverse web services on behalf of a Dataverse user.

Impersonation involves two different user accounts:

|Impersonator|Impersonated user|
|--|--|
|User account used when executing code|User account that the task is being performed on behalf of.|

<a name="bkmk_Requirementsforimpersonation"></a>
<a name="requirements-for-impersonation"></a>

## Required privileges

The *impersonator* needs the **Act on Behalf of Another User** privilege (`prvActOnBehalfOfAnotherUser`). This privilege is included in the **Delegate** security role or can be enabled for any security role.

> [!NOTE]
> Users can be associated with more than one security role. Assigning the **Delegate** security role to a user grants the `prvActOnBehalfOfAnotherUser` privilege as well as the privileges provided by any other security roles associated with the user account.

The actual set of privileges used to modify data is the intersection of the privileges that the *impersonator* user possesses with that of the *impersonated user*. 

In other words, the *impersonator* is allowed to do something *if and only if* the *impersonator* and the *impersonated user* have the privilege necessary for the action.

### Direct assignment required

You must assign the **Act on Behalf of Another User** privilege (`prvActOnBehalfOfAnotherUser`) or a role containing that privilege directly to users. Users can't inherit this privilege through a Team. This direct assignment is required because of the sensitive nature of the privilege.

## Impersonation with Server-to-Server authentication

If you're creating a web client application that requires a user account that can act on behalf of a subscribing user, use the special *application user* account so that you don't need to use a paid Dataverse user license.

More information: [Build web applications using Server-to-Server (S2S) authentication](build-web-applications-server-server-s2s-authentication.md).

## Impersonate another user by using the Web API

You can impersonate a user by passing a request header with the corresponding user ID before sending the request to the web service.

<a name="bkmk_Howtoimpersonateauser"></a>

### How to impersonate a user

Use one of these headers:

1. **Preferred:** Set `CallerObjectId` to the impersonated user's Microsoft Entra ID object ID. This value is stored in [SystemUser.AzureActiveDirectoryObjectId](reference/entities/systemuser.md#BKMK_AzureActiveDirectoryObjectId).
2. **Legacy:** Set `MSCRMCallerID` to the impersonated user's [SystemUser.SystemUserId](reference/entities/systemuser.md#BKMK_SystemUserId) GUID value.

The following example creates an account row on behalf of the user with the Microsoft Entra ID object ID `aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb`.

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
OData-EntityId: [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000003)
```

<a name="bkmk_Determinetheactualuser"></a>

### Determine the actual user

When you create a row by using impersonation, query the `createdonbehalfby` single-valued navigation property to find the user who actually performed the operation. For updates, use the corresponding `modifiedonbehalfby` single-valued navigation property.

The following example retrieves the account created in the previous example. The `createdby` and `owninguser` properties identify the impersonated user, while `createdonbehalfby` identifies the actual user.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000003)?$select=name&$expand=createdby($select=fullname,azureactivedirectoryobjectid),createdonbehalfby($select=fullname,azureactivedirectoryobjectid),owninguser($select=fullname,azureactivedirectoryobjectid) HTTP/1.1
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
ETag: W/"2751197"

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,createdby(fullname,azureactivedirectoryobjectid),createdonbehalfby(fullname,azureactivedirectoryobjectid),owninguser(fullname,azureactivedirectoryobjectid))/$entity",
  "@odata.etag": "W/\"2751197\"",
  "name": "Sample Account created using impersonation",
  "accountid": "00000000-0000-0000-0000-000000000003",
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

## Impersonate another user by using the SDK for .NET

To impersonate another user, set the `CallerId` property to the Guid value of the impersonated user. The following classes that implement <xref:Microsoft.Xrm.Sdk.IOrganizationService> include this property.

- <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.CallerId>
- <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy>.<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy.CallerId>
- <xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient>.<xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient.CallerId>

## Impersonate another user by using plug-ins

You can register a plug-in containing code to specify the user that the operations should use.
More information: [Impersonate a user](impersonate-a-user.md).


## See also

[Build web applications using Server-to-Server (S2S) authentication](build-web-applications-server-server-s2s-authentication.md)<br />
[Perform operations using the Web API](webapi/perform-operations-web-api.md)<br />
[Write a plug-in](write-plug-in.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
