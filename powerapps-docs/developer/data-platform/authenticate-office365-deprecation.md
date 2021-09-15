---
title: "Use Office365 authentication with Microsoft Dataverse (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes deprecation of the WS-Trust security protocol and the code changes required in applications that use Office365 authentication."
ms.custom: ""
ms.date: 08/29/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "phecke" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Use Office365 authentication with Microsoft Dataverse

Use of the WS-Trust authentication security protocol when connecting to Microsoft Dataverse is no longer recommended and has been deprecated; see the [announcement](/power-platform/important-changes-coming#deprecation-of-office365-authentication-type-and-organizationserviceproxy-class-for-connecting-to-dataverse).

Additionally, the WS-Trust protocol does not support modern forms of multi-factor authentication and Azure AD Conditional Access controls to customer data.

This change impacts custom client applications that use “Office365” authentication and the
[Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy](/dotnet/api/microsoft.xrm.sdk.client.organizationserviceproxy) or
[Microsoft.Xrm.Tooling.Connector.CrmServiceClient](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient)
classes. If your applications use this type of authentication protocol and API,
continue reading below to learn more about the recommended authentication
changes to be made to your application’s code.

## How do I know if my code or application is using WS-Trust?

First and most importantly, this change **only** impacts client applications that
connect to the Microsoft Dataverse. It does not impact custom plug-ins,
workflow activities, or on-premises/IFD service connections.

- If your code employs user account and password credentials for authentication with Dataverse or an application, you are likely using the WS-Trust security protocol. Some examples are shown below, though this list is not fully inclusive.

  - When using the [CrmServiceClient](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient) class with a connection string:

    `connectionString="AuthType=Office365; Username=jsmith\@contoso.onmicrosoft.com;Password=passcode;Url=https://contoso.crm.dynamics.com"`

  - When using [OrganizationServiceProxy](/dotnet/api/microsoft.xrm.sdk.client.organizationserviceproxy) class constructors:

```csharp
using (OrganizationServiceProxy organizationServiceProxy =
    new OrganizationServiceProxy(serviceManagement, clientCredentials)
{ ... }
```

- If you are using the `OrganizationServiceProxy` class at all in your code, you are using WS-Trust.

- If you are using [CrmServiceClient](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient).`OrganizationServiceProxy` in your code, you are using WS-Trust.

## What should I do to fix my application code if affected?

There are very straight forward ways to modify your application’s code to use
the recommended connection interface for authentication with Dataverse.

- If your code uses an [Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy](/dotnet/api/microsoft.xrm.sdk.client.organizationserviceproxy) instance:

  If you are passing the `OrganizationServiceProxy` instance around to various methods, or returning the instance from a method, replace all occurrences of the type `OrganizationServiceProxy` with the [IOrganizationService](/dotnet/api/microsoft.xrm.sdk.iorganizationservice?view=dynamics-general-ce-9) interface. This interface exposes all the core methods used to communicate with Dataverse.

  When invoking the constructor, it is recommend you add the NuGet package [Microsoft.CrmSdk.XrmTooling.CoreAssembly](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/) to your project and replace all use of `OrganizationServiceProxy` class constructors with [CrmServiceClient](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient) class constructors. You will need to alter your coding pattern here, however, for simplicity `CrmServiceClient` supports connection strings in addition to complex constructors and the ability to provide external authentication handlers. `CrmServiceClient` implements `IOrganizationService`, therefore your new authentication code will be portable to the rest of your application code. You can find examples on the use of `CrmServiceClient` in the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23) repository.

- If your code is using [CrmServiceClient](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient) with the “Office365” authentication type:

    An example of this is a connections string that looks like this:

    `connectionString = "AuthType=Office365;Username=jsmith@contoso.onmicrosoft.com;Password=passcode;Url=https://contoso.crm.dynamics.com"`

    Similarly, you could also use a `CrmServiceClient` constructor and pass in `AuthType.Office365`.

    You have two options for dealing with this.<p/>

    - Switch over to using an OAuth based connection string. Such connection string looks like this:

        `connectionString = "AuthType=OAuth;Username=jsmith@contoso.onmicrosoft.com;
    Password=passcode;Url=https://contosotest.crm.dynamics.com;AppId=51f81489-12ee-4a9e-aaae-a2591f45987d;
    RedirectUri=app://58145B91-0C36-4500-8554-080854F2AC97;LoginPrompt=Auto"`

        This will be your fastest way to update the code. Note that LoginPrompt can be set to “never” to simulate the way that the Office365 behavior worked.

        The AppId and RedirectUri provided above are examples of working application registration values. These values work everywhere our online services are deployed. However, they are provided here as examples and you are encouraged to create your own application registration in Azure Active Directory (Azure AD) for applications running in your tenant.<p/>

    - When we announce it, update to the latest [Microsoft.CrmSdk.XrmTooling.CoreAssembly](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/) NuGet package that includes auto redirect support. This library will redirect an authentication type of Office365 to OAuth and use the example AppId and Redirect URI automatically. This capability is planned for the 9.2.x version of the Microsoft.CrmSdk.XrmTooling.CoreAssembly package.

- If you are accessing the [CrmServiceClient](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient).`OrganizationServiceProxy` property:

     Remove all use of that property in your code. `CrmServiceClient` implements `IOrganizationService` and exposes everything that is settable for the organization service proxy.

> [!IMPORTANT]
> Regarding not being able to login using User ID/Password even if using OAuth: if your tenant and user is configured in Azure Active Directory for conditional access and/or Multi-Factor Authentication is required, you will not be able to use user ID/password flows in a non-interactive form at all. For those situations, you must use a Service Principal user to authenticate with Dataverse.<p/>
To do this, you must first register the application user (Service Principal) in Azure Active Directory. You can find out how to do this [here](/azure/active-directory/develop/howto-create-service-principal-portal). During application registration you will need to create that user in Dataverse and grant permissions. Those permissions can either be granted directly or indirectly by adding the application user to a team which has been granted permissions in Dataverse. You can find more information on how to set up an application user to authenticate with Dataverse [here](./use-single-tenant-server-server-authentication.md).

## Need help?

We will be monitoring the Power Apps ALM and ProDev community [forums](https://powerusers.microsoft.com/t5/Power-Apps-Component-Framework/bd-p/pa_component_framework). Please take a look there to get help on how to solve various issues or post a
question.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
