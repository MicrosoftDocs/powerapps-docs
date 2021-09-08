---
title: "Impersonate another user (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use impersonation to execute business logic on behalf of another Microsoft Dataverse user." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/12/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Impersonate another user

Use impersonation to execute business logic on behalf of another Microsoft Dataverse user to provide a desired feature or service using the appropriate role and object-based security of that impersonated user.

This is necessary because the Dataverse web services can be called by various clients and services on behalf of a Dataverse user.

Impersonation involves two different user accounts:

|Impersonator|Impersonated user|
|--|--|
|User account used when executing code|User account that the task is being performed on behalf of.|

## Required privileges

The *impersonator* needs the privilege **Act on Behalf of Another User** (`prvActOnBehalfOfAnotherUser`), which is included in the **Delegate** security role or can be enabled for any security role.

> [!NOTE]
> Remember that users can be associated with more than one security role. Assigning the **Delegate** security role to a user will grant them the `prvActOnBehalfOfAnotherUser` privilege as well as the privileges provided by any other security roles associated with the user account.

The actual set of privileges that is used to modify data is the intersection of the privileges that the *impersonator* user possesses with that of the *impersonated user*. 

In other words, the *impersonator* is allowed to do something *if and only if* the *impersonator* and the *impersonated user* have the privilege necessary for the action.

## Impersonation with Server-to-Server authentication

If you are creating a web client application that requires a user account that can act on behalf of a subscribing user, you can use the special *application user* account so that you do not need to use a paid Dataverse user license.

More information: [Build web applications using Server-to-Server (S2S) authentication](build-web-applications-server-server-s2s-authentication.md).

## Impersonate another user using the Web API

To impersonate a user, add a request header named `CallerObjectId` with a GUID value equal to the impersonated user's Azure Active Directory (AAD) object id before sending the request to the web service. The user's AAD object id is included in the [SystemUser.AzureActiveDirectoryObjectId](reference/entities/systemuser.md#BKMK_AzureActiveDirectoryObjectId).

More information: [Impersonate another user using the Web API](webapi/impersonate-another-user-web-api.md).


## Impersonate another user using the Organization service

To impersonate another user, set the `CallerId` property to the Guid value of the impersonated user. The following classes that implement <xref:Microsoft.Xrm.Sdk.IOrganizationService> include this property.

- <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.CallerId>
- <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy>.<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy.CallerId>
- <xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient>.<xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient.CallerId>

## Impersonate another user using plug-ins

You can register a plug-in you can specify a user that the operations should use. Within the code of a plug-in you can override this setting.
More information: [Impersonate a user](impersonate-a-user.md).


### See also

[Build web applications using Server-to-Server (S2S) authentication](build-web-applications-server-server-s2s-authentication.md)<br />
[Impersonate another user using the Web API](webapi/impersonate-another-user-web-api.md)<br />
[Write a plug-in](write-plug-in.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]