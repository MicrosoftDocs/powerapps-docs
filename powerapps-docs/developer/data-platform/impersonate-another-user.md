---
title: "Impersonate another user (Microsoft Dataverse) | Microsoft Docs"
description: "Use impersonation to execute business logic on behalf of another Microsoft Dataverse user." 
ms.date: 08/20/2026
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

To impersonate a user, add a request header named `CallerObjectId` with a GUID value equal to the impersonated user's Microsoft Entra ID object identifier before sending the request to the web service. The user's Microsoft Entra ID object identifier is included in the [SystemUser.AzureActiveDirectoryObjectId](reference/entities/systemuser.md#BKMK_AzureActiveDirectoryObjectId).

More information: [Impersonate another user using the Web API](webapi/impersonate-another-user-web-api.md).


## Impersonate another user by using the SDK for .NET

To impersonate another user, set the `CallerId` property to the Guid value of the impersonated user. The following classes that implement <xref:Microsoft.Xrm.Sdk.IOrganizationService> include this property.

- <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.CallerId>
- <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy>.<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy.CallerId>
- <xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient>.<xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient.CallerId>

## Impersonate another user by using plug-ins

You can register a plug-in containing code to specify the user that the operations should use.
More information: [Impersonate a user](impersonate-a-user.md).


### See also

[Build web applications using Server-to-Server (S2S) authentication](build-web-applications-server-server-s2s-authentication.md)<br />
[Impersonate another user using the Web API](webapi/impersonate-another-user-web-api.md)<br />
[Write a plug-in](write-plug-in.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
