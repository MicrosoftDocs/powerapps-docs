---
title: "Tutorial: Register an app with Microsoft Entra ID (Microsoft Dataverse) | Microsoft Docs"
description: "Describes how to register an application with Microsoft Entra ID for authentication with Microsoft Dataverse web services."
keywords: ""
ms.date: 11/28/2023
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

This tutorial describes how to register an application with Microsoft Entra ID, which enables a user with a Power Apps user account to connect to their Microsoft Dataverse environment from external client applications using OAuth authentication.

> [!IMPORTANT]
> Power Apps also provides you with a Server-to-Server (S2S) authentication option to connect to Dataverse environment from external applications and services using the special application user account. Using S2S authentication is a common way that apps registered on Microsoft AppSource use to access the data of their subscribers. More information: [Build web applications using Server-to-Server (S2S) authentication](build-web-applications-server-server-s2s-authentication.md).

App registration in Microsoft Entra ID is typically done by ISVs who want to develop external client applications to read and write data in Dataverse. Registering an app in Microsoft Entra ID provides you with **Application ID** and **Redirect URI** values that ISVs can use in their client application's authentication code. When end users use the ISV's application for the *first time* to connect to their Dataverse environment by providing their Dataverse credentials, a consent form is presented to the end user. After consenting to use their Dataverse account with the ISV's application, end users can connect to Dataverse environment from the external application. The consent form is not displayed again to other users after the first user who has already consented to use the ISV's app. Apps registered in Microsoft Entra ID can be multi-tenant, which implies that other Dataverse users from other tenant can connect to their environment using the ISV's app.

App registration can also be done by an application developer or individual user who is building a client application to connect to and read/write data in Dataverse. Use the **Application ID** and **Redirect URI** values from your registered app in your client application's authentication code to connect to a Dataverse environment from your client application, and perform the required operations. Note that if the app is registered in the same tenant as your Dataverse environment, you won't be presented with a consent form when connecting from your client application to your Dataverse environment.

## Prerequisites  

- An Microsoft Entra subscription for application registration. A trial account will also work.  
  
## Create an application registration
  
1. Sign in to the Microsoft Azure [portal](https://portal.azure.com/#home) using an account with administrator permission. You must use an account in the same Microsoft 365 subscription (tenant) as you intend to register an app with. On the **Home** page of the portal under **Azure services** select **Microsoft Entra ID**.

    Alternately, you can also access the Azure portal through the Microsoft 365 [Admin center](https://admin.microsoft.com/adminportal) by first choosing the **All admin centers** item in the left navigation pane, select **Microsoft Entra**, and then select **Go to Microsoft Entra ID**. Next, in the left navigation pane of the Microsoft Entra admin center, expand the  **Applications** node.
  
   > [!NOTE]
   > If you don't have an Azure tenant (account) or you do have one but your Microsoft 365 subscription with Dataverse is not available in your Azure subscription, following the instructions in the topic [Set up Microsoft Entra ID access for your Developer Site](/office/developer-program/microsoft-365-developer-program) to associate the two accounts.
   >
   > If you don't have an account, you can sign up for one by using a credit card. However, the account is free for application registration and your credit card won't be charged if you only follow the procedures called out in this topic to register one or more apps. More information: [Microsoft Entra ID Pricing Details](https://azure.microsoft.com/pricing/details/active-directory/)  
  
2. In the left navigation pane select **App registrations** and then select **+ New registration** on the **App registrations** page.

3. On the **App registrations** page, enter your application's registration information as described below.

    | Form input element | Description |
    | --- | --- |
    | Name | Enter a meaningful application name that will be displayed to users. |
    | Supported account types | Select the **Accounts in any organizational directory** option. |
    | Redirect URI | This field is optional when using client secret or certificate authentication. For basic username/password authentication, supply a redirect URI. The redirect URI value must be a valid value, however the specified URI is not required to exist.|

4. Select **Register** to create the application registration. The app registration overview page is shown. Remain on that page.

    :::image type="content" source="media/app-registration-overview-page.png" alt-text="App registration overview.":::

5. Set the **Application ID URI** value by first selecting **Add an Application ID URI** and then **+ Add a scope**. Set the URI value to your target environment (organization) base address.

6. On the **Overview** page of your newly created app, hover the cursor over the **Application (client) ID** value, and select the copy to clipboard icon to copy the ID value. Record the value somewhere. You'll need to specify this value later in your application's authentication code or app.config file where appropriate.
  
6. Select **Manifest** tab, in the manifest editor, set the *allowPublicClient** property to **true** and click on **Save**.
   
    ![App registration Manifest.](media/app-registration-manifest-page.png "App registration Manifest")

7. Select **API permissions** tab, click on **Add a permission**. 

    ![Add app permission.](media/azure-api-permissions-page.png "Add app permission")

8. Search for and choose **Dataverse** under the **APIs my organization uses** tab. If "Dataverse" is not found, then search for "Common Data Service".
    
    ![Select API.](media/app-registration-select-api-page.png "Select API")    
    > [!TIP]
    > If you are presented with more than one **Common Data Service** item in the search list, choose any one of them. In the next step the service name and URL will be shown. At that point you can go back to the API search and choose a different Dataverse list item if needed.
    
9.  Click on **Delegated permissions** and check the options and click on **Add permissions**. 
    
    ![Delegate Permissions.](media/app-registration-delegate-permissions-page.png "Delegate Permission")
    > [!NOTE]
    > A future revision of the form in step #8 will replace the Dynamics CRM logo and icon with Dataverse.

This completes the registration of your application in Microsoft Entra ID.

## Additional configuration options

If your application will support server-to-server connections, see [Use Multi-Tenant Server-to-server authentication](use-multi-tenant-server-server-authentication.md)
  
### See also

[Application registration in Microsoft Entra ID](/azure/active-directory/develop/active-directory-integrating-applications)<br />
[Authenticate Users with Dataverse Web Services](authentication.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
