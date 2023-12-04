---
title: "Tutorial: Register an app with Microsoft Entra ID (Microsoft Dataverse) | Microsoft Docs"
description: "Describes how to register an application with Microsoft Entra ID for authentication with Microsoft Dataverse web services."
keywords: ""
ms.date: 12/04/2023
ms.topic: article
ms.assetid: 86c4a8a8-7401-6d75-7979-3b04b506eb0c
author: "paulliew" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "paulliew" # MSFT alias of Microsoft employees only
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
---

# Tutorial: Register an app with Microsoft Entra ID

This tutorial describes how to register an application with Microsoft Entra ID that accesses Microsoft Dataverse business data. After registering an external client application, a user with a Power Apps user account can to connect to their Dataverse environment and access business data.

The included instructions in this article are specific to Dataverse app registration in Entra ID. For the latest Entra ID information, see [Application registration in Microsoft Entra ID](/azure/active-directory/develop/active-directory-integrating-applications).

## About app registration

App registration in Microsoft Entra ID is typically done by ISVs who want to develop external client applications to read and write data in Dataverse. Registering an app in Microsoft Entra ID provides you with **Application ID** and **Redirect URI** values that ISVs can use in their client application's authentication code. When end users use the ISV's application for the *first time* to connect to their Dataverse environment by providing their Dataverse credentials, a consent form is presented to the end user. After consenting to use their Dataverse account with the ISV's application, end users can connect to Dataverse environment from the external application. The consent form is not displayed again to other users after the first user who has already consented to use the ISV's app. Apps registered in Microsoft Entra ID can be multi-tenant, which implies that other Dataverse users from other tenant can connect to their environment using the ISV's app.

App registration can also be done by an application developer or individual user who is building a client application to connect to and read/write data in Dataverse. Use the **Application ID** and **Redirect URI** values from your registered app in your client application's authentication code to connect to a Dataverse environment from your client application, and perform the required operations. Note that if the app is registered in the same tenant as your Dataverse environment, you won't be presented with a consent form when connecting from your client application to your Dataverse environment.

> [!IMPORTANT]
> Power Apps also provides you with a Server-to-Server (S2S) authentication option to connect to Dataverse environment from external applications and services using the special application user account. Using S2S authentication is a common way that apps registered on Microsoft AppSource use to access the data of their subscribers. More information: [Build web applications using Server-to-Server (S2S) authentication](build-web-applications-server-server-s2s-authentication.md).

## Prerequisites  

- A Microsoft Entra subscription for application registration. A trial account will also work.

If you don't have an Azure tenant (account) or you do have one but your Microsoft 365 subscription with Dataverse is not available in your Azure subscription, follow the instructions in the topic [Set up Microsoft Entra ID access for your Developer Site](/office/developer-program/microsoft-365-developer-program) to associate the two accounts.

If you don't have an account, you can sign up for one by using a credit card. However, the account is free for application registration and your credit card won't be charged if you only follow the procedures called out in this topic to register one or more apps. More information: [Microsoft Entra ID Pricing Details](https://azure.microsoft.com/pricing/details/active-directory/)  
  
## Create an application registration

To create an application registration, follow these steps.
  
1. Sign in to the Microsoft Azure [portal](https://portal.azure.com/#home) using an account with administrator permission. You must use an account in the same Microsoft 365 subscription (tenant) as you intend to register an app with. On the **Home** page of the portal under **Azure services** select **Microsoft Entra ID**.

    Alternately, you can also access the Azure portal through the Microsoft 365 [Admin center](https://admin.microsoft.com/adminportal) by first choosing the **All admin centers** item in the left navigation pane, select **Microsoft Entra**, and then select **Go to Microsoft Entra ID**. Next, in the left navigation pane of the Microsoft Entra admin center, expand the  **Applications** node. 
  
2. In the left navigation pane select **App registrations** and then select **+ New registration** on the **App registrations** page.

3. On the **App registrations** page, enter your application's registration information as described below.

    | Form input element | Description |
    | --- | --- |
    | Name | Enter a meaningful application name that will be displayed to users. |
    | Supported account types | Select the **Accounts in any organizational directory** option. |
    | Redirect URI | This field is optional when using client secret or certificate authentication. For basic username/password authentication, supply a redirect URI. The redirect URI value must be a valid value, however the specified URI is not required to exist.|

4. Select **Register** to create the application registration. The app registration overview page is shown. Remain on that page.

    :::image type="content" source="media/app-registration-overview-page.png" alt-text="App registration overview." lightbox="media/app-registration-overview-page.png":::

5. On the **Overview** page of your newly created app, hover the cursor over the **Application (client) ID** value, and select the copy to clipboard icon to copy the ID value. Record the value somewhere. You'll need to specify this value later in your application's authentication code or app.config file where appropriate.
  
6. Select **Manifest** in the left navigation panel. In the manifest editor, set the `allowPublicClient` property to `true` and select **Save**.

    ```JSON
    {
    "id": "219db142-b8e2-4645-9434-44a4516b8968",
    "acceptMappedClaims": null,
    "accessTokenAcceptedVersion": null,
    "addIns": [],
    "allowPublicClient": true,
    "appId": "4bfce595-7819-423c-b0bd-a053ff97fb99",
    "appRoles": [],
    "oauth2AllowUrlPathMatching": false,
    ```

7. In the left navigation panel, select **API permissions** and then select **Add a permission**.

8. Select the **APIs my organization uses** tab, and then in the search field, enter "Dataverse" to search for the Dataverse entry. Select the Dataverse item in the search results list.

9. On the **Request API permissions** page,  select **Delegated permissions**. Next, select (check) the **user_impersonation** option, and then select **Add permissions**.

    > [!NOTE]
    > For a server-to-server (S2S) scenario, you do not need to check the user_impersonation option. More information: [Use multi-tenant server-to-server authentication](use-multi-tenant-server-server-authentication.md)

This completes the basic app registration in Microsoft Entra ID.

### Add a certificate or secret

 If you want to add a certificate or client secret to your app registration, simply select **Certificates & secrets** in the left navigation panel and add those items.

More information: [Add a certificate](/entra/identity-platform/quickstart-register-app#add-a-certificate), [Add a secret](/entra/identity-platform/quickstart-register-app#add-a-client-secret)

## Use app registration in code

To view code that uses an app registration, see the [Get Started](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23-NETCore/GetStarted#get-started-using-the-dataverse-sdk-for-net) SDK samples, and the [QuickStart](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/C%23-NETx/QuickStart) Web API sample.

### See also

[Authenticate Users with Dataverse Web Services](authentication.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
