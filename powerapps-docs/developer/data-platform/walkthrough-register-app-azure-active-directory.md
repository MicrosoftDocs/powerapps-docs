---
title: "Tutorial: Register an app with Microsoft Entra ID (Microsoft Dataverse) | Microsoft Docs"
description: "Describes how to register an application with Microsoft Entra ID for authentication with Microsoft Dataverse web services."
keywords: ""
ms.date: 02/24/2025
ms.topic: tutorial
ms.assetid: 86c4a8a8-7401-6d75-7979-3b04b506eb0c
author: "paulliew" 
ms.subservice: dataverse-developer
ms.author: "paulliew"
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
---

# Tutorial: Register an app with Microsoft Entra ID

This tutorial describes how to register an application (desktop, mobile, or Web) with Microsoft Entra ID. App registration is required before an application can authenticate with Microsoft Dataverse and access business data.

## About app registration and authentication

There are several authentication flows that Dataverse supports: username/password, client secret, certificate, and managed identity. App registration and authentication is slightly different for each of these flows. This article covers the username/password and client secret authentication flows. Certificate flows are planned to be documented in a future article.

Read the following important information about using username/password authentication in application code.
[!INCLUDE [cc-connection-string](includes/cc-connection-string.md)]

For an app to authenticate with Dataverse and gain access to business data, you must first register the app in Microsoft Entra ID. That app registration is then used during the authentication process.

The included instructions in this article are specific to app registration in Microsoft Entra ID for Dataverse access. For general Microsoft Entra ID app registration information, see [Application registration in Microsoft Entra ID](/azure/active-directory/develop/active-directory-integrating-applications).

### Public and confidential clients

There are two types of clients that you can use to authenticate with Dataverse: public and confidential. These clients are represented by the <xref:Microsoft.Identity.Client.PublicClientApplicationBuilder> and <xref:Microsoft.Identity.Client.ConfidentialClientApplicationBuilder> classes. You can instance these classes in your app directly, for example if your app is using the Dataverse Web API, or you can use the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> class. The `ServiceClient` class handles instantiation of these clients internally based on the configuration values in the passed [connection string parameters](xrm-tooling/use-connection-strings-xrm-tooling-connect.md#connection-string-parameters).

> [!NOTE]
> The confidential client is used with a client secret or certificate and is often referred to as Service Principle, Application User, or server-to-server (S2S) authentication.

## Prerequisites  

- A Microsoft Entra subscription for application registration. A trial account will work.

If you don't have an Azure tenant (account) or you do have one but your Microsoft 365 subscription with Dataverse isn't available in your Azure subscription, follow the instructions in the article [Set up Microsoft Entra ID access for your Developer Site](/office/developer-program/microsoft-365-developer-program) to associate the two accounts.
  
## Public client app registration

To create an app registration for a username/password authentication flow, and for use with a public client or `ServiceClient` connection string, follow these steps.
  
1. Sign in to the Microsoft Azure [portal](https://portal.azure.com/#home) using an account with administrator permission. You must use an account in the same Microsoft 365 subscription (tenant) as you intend to register an app with. On the **Home** page of the portal under **Azure services**, select **Microsoft Entra ID**.

    Alternately, you can also access the Azure portal through the Microsoft 365 [admin center](https://admin.microsoft.com/adminportal) by first choosing the **All admin centers** item in the left navigation pane, select **Microsoft Entra**, and then select **Go to Microsoft Entra ID**. Next, in the left navigation pane of the Microsoft Entra admin center, expand the  **Applications** node.
  
2. In the left navigation pane, select **App registrations** and then select **+ New registration** on the **App registrations** page.

3. On the **App registrations** page, enter your application's registration information as described in the table.

    | Form input element | Description |
    | --- | --- |
    | Name | Enter a meaningful application name that is displayed to users. |
    | Supported account types | Select the **Accounts in \<any or this> organizational directory** option. |

4. Select **Register** to create the application registration. The app registration overview page is shown. Remain on that page.

    :::image type="content" source="media/app-registration-overview-page.png" alt-text="App registration overview." lightbox="media/app-registration-overview-page.png":::

5. On the **Overview** page under **Essentials**, select the **Add a Redirect URI** link. Set the redirect URI by first selecting **Add a platform**, enter a URI value, and then select **Configure**.

    You must supply a redirect URI value described as follows. For a .NET Framework built desktop or mobile app, use a URI value of "app://\<Application (client) ID>". This ID value is displayed on the **Overview** page of the registered app. For a .NET Core built desktop or mobile app that uses [MSAL](/entra/identity-platform/msal-overview) for authentication, use a URI value of "<http://localhost>". For a Web API app, use any valid web address though the address does not have to actually exist.

6. On the **Overview** page of your newly created app, hover the cursor over the **Application (client) ID** value, and select the copy to clipboard icon to copy the ID value. Record the value somewhere. You need to specify this value later in your application's authentication code or app.config file where appropriate.

7. In the left navigation panel, select **API permissions** and then select **Add a permission**.

8. Select the **APIs my organization uses** tab, and then in the search field, enter "Dataverse" to search for the Dataverse entry. Select the Dataverse item in the search results list.

9. On the **Request API permissions** page,  select **Delegated permissions**. Next, select (check) the **user_impersonation** option

10. Select **Grant admin consent for \<name>** even though it looks like it is already checked. Next, on the popup, select **Yes** to grant consent. If you do not approve consent here, your app will receive a consent error at run-time.
    > [!NOTE]
    > If the **Grant admin consent for \<name>** is ghosted (non-selectable), you do not have permission to set this value.
    > More information: [Admin consent button](/entra/identity-platform/quickstart-configure-app-access-web-apis#admin-consent-button), [User and admin consent in Microsoft Entra ID](/entra/identity/enterprise-apps/user-admin-consent-overview)

12. Select **Add permissions**.

13. (Optional) On the **Authentication** page under **Advanced settings** and **Allow public client flows**, select **Yes** and then **Save**. See the description in the next paragraphs for more information.

During authentication, if the client app does not supply a password for a username/password flow, the app user will be prompted for logon credentials in a browser window.

If you intend to supply a password for client authentication, then you must explicitly set **Enable the following mobile and desktop flows** to **Yes**. This requirement is in place to discourage providing a password in code, App.config, etc. as this method is less secure.

You've completed the public client app registration in Microsoft Entra ID.

## Confidential client app registration

To create an app registration for a client secret or certificate authentication flow, and for use with a confidential client or `ServiceClient` connection string, follow the steps in the next two sections. You'll be creating a Microsoft Entra ID app registration and a new app user in the Power Platform admin center.

### Create the app registration

App registration is much simpler for the confidential client compared to the public client. You need only provide an app registration name and set the tenant (account type) scope.

1. Sign in to the Microsoft Azure [portal](https://portal.azure.com/#home) using an account with administrator permission. You must use an account in the same Microsoft 365 subscription (tenant) as you intend to register an app with. On the **Home** page of the portal under **Azure services**, select **Microsoft Entra ID**.

    Alternately, you can also access the Azure portal through the Microsoft 365 [admin center](https://admin.microsoft.com/adminportal) by first choosing the **All admin centers** item in the left navigation pane, select **Microsoft Entra**, and then select **Go to Microsoft Entra ID**. Next, in the left navigation pane of the Microsoft Entra admin center, expand the  **Applications** node.
  
2. In the left navigation pane, select **App registrations** and then select **+ New registration** on the **App registrations** page.

3. On the **App registrations** page, enter your application's registration information as described in the table.

    | Form input element | Description |
    | --- | --- |
    | Name | Enter a meaningful application name that is displayed to users. |
    | Supported account types | Select the **Accounts in \<any or this> organizational directory** option. |

4. Select **Register** to create the application registration. The app registration overview page is shown.

5. Add a client secret by selecting the **Certificates & secrets** link in the left navigation pane. More information: [Add a client secret](/entra/identity-platform/quickstart-register-app#add-a-client-secret)

> [!IMPORTANT]
> After adding a client secret, save a copy of the secret value for later use. Do not navigate away from the client secret page until after you have copied the secret value (not the ID) as you'll not have access to the secret value again.

### Create a new app user

Follow these steps to create an app user and bind it to your app registration.

1. Log into the Power Platform [admin center](https://admin.powerplatform.microsoft.com) using an account in the same tenant as your app registration.

2. Select **Environments** in the left navigation pane, and then select the target environment in the list to display the environment information.

3. Select the **S2S** link on the right side of the page.

4. Select **New app user**.

5. On the **Create a new app user** slide-out, select **+ Add app**.

6. Start typing the name of your app registration in the search field, and then select (check) it within the results list. Next, select **Add**.

7. Back on the **Create a new app user** slide-out, select the target **Business unit** from the drop-down and add a security role for the app user (also known as a service principle).

8. Select **Save** and then **Create**. You should see your new application user in the displayed list of application users.

## Use an app registration in code

To view code that uses an app registration, see the [Get Started](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/GetStarted#get-started-using-the-dataverse-sdk-for-net) SDK samples, and the [QuickStart](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/QuickStart) Web API sample.

Here is the confidential client code from the SDK samples. The client ID and secret are obtained from the Entra ID app registration once completed.

```csharp
class Program
{
    // TODO Enter your Dataverse environment's URL, ClientId, and Secret.
    static string url = "https://<myorg>.crm.dynamics.com";

    static string connectionString = $@"
    AuthType = ClientSecret;
    Url = {url};
    ClientId = 66667777-aaaa-8888-bbbb-9999cccc0000;
    Secret = aaaaaaaa-6b6b-7c7c-8d8d-999999999999";

    static void Main()
    {
        // ServiceClient class implements IOrganizationService interface
        IOrganizationService service = new ServiceClient(connectionString);

        var response = (WhoAmIResponse)service.Execute(new WhoAmIRequest());

        Console.WriteLine($"Application ID is {response.UserId}.");

        // Pause the console so it does not close.
        Console.WriteLine("Press the <Enter> key to exit.");
        Console.ReadLine();
    }
}
```

For the complete code sample, refer to the links mentioned previously.

### See also

[Authenticate Users with Dataverse Web Services](authentication.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
