---
title: "Tutorial: Create an ASP.NET Core Blazor WebAssembly app using Microsoft Dataverse | Microsoft Docs"
description: "Learn how to create an ASP.NET Core Blazor WebAssembly application that connects to Microsoft Dataverse web services and retrieves business data."
keywords: ""
ms.date: 03/23/2021
ms.service: powerapps
ms.topic: article
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: ryjones # MSFT alias of manager or PM counterpart
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Tutorial: Create an ASP.NET Core Blazor WebAssembly app using Microsoft Dataverse

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Use the steps in this tutorial to create a Blazor WebAssembly app that connects to the Dataverse. The focus of this topic is to understand the necessary steps to authenticate a user with a specific Dataverse instance and retrieve data.

Blazor WebAssembly is one of two hosting models available for ASP.NET Core Blazor, the other is Blazor Server. For a complete description of the differences, see [ASP.NET Core Blazor hosting models](/aspnet/core/blazor/hosting-models).

This tutorial depends on the instructions in the [Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory) topic. Because Dataverse uses Azure Active Directory (Azure AD) for authentication, this tutorial will describe how to modify the basic app created using the app template provided so that it can connect to Dataverse.

## Goal

When you complete this tutorial, you will have a Blazor WebAssembly app that displays data from the Dataverse Account table that the authenticated user has access to.

:::image type="content" source="media/blazor-webassembly-walkthrough-goal.png" alt-text="Represents the goal of this tutorial.":::


## Prerequisites

To complete this tutorial, you must have:

- Access to a [Dataverse environment with a database](/power-platform/admin/create-environment#create-an-environment-with-a-database)
- A Dataverse user with a security role that provides read access to the Account and Contact tables
- Understanding of the C# programming language
- Understanding of ASP.NET Core Blazor is helpful but not required
- The latest version of Visual Studio 2019 with the **ASP.NET and web development** workload installed.

## Step 1: Verify prerequisites and information about the database

Let’s make sure that your environment is configured properly, and you understand where to perform the actions in Step 2.

### Verify Dataverse database

1. Sign in to [Power Apps](https://make.powerapps.com/).
1. Select **Solutions** in the navigation pane.

    :::image type="content" source="media/blazor-webassembly-walkthrough-maker-portal.png" alt-text="The maker portal showing an environment without a Dataverse database.":::

1. If you don’t see a list of installed solutions, use the environment selector at the top to choose a different environment that has a database. Otherwise create a new environment.

### Get the Dataverse Web API URI

You will need the Instance Web API Service Root URL. This is found on the Developer Resources page of your Dataverse environment.

Follow the instructions found in [View or download developer resources](view-download-developer-resources.md) to copy the Url. 

It will look something like this: `https://yourorgname.api.crm.dynamics.com/api/data/v9.1/`

### Navigate to the Azure Active Directory portal

1. Sign in to [Power Apps](https://make.powerapps.com).
1. In the ‘waffle’ icon at the top left and select **Admin**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-navigate-admin-center.png" alt-text="Navigating to the Microsoft 365 admin center.":::

1. This will take you to the Microsoft 365 admin center. In the left navigation, click **Show all** and select **Azure Active Directory**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-navigate-AAD-from-admin-center.png" alt-text="Navigating to the Azure Active Directory Admin center.":::

1. This will take you to the Azure Active Directory admin center. Expand the left navigation pane and select **Azure Active Directory**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-aad-admin-center.png" alt-text="Navigating to the Azure Active Directory page.":::

This takes you to the starting point for Step 2.

## Step 2: Create a Blazor WebAssembly standalone app using Azure AD for authentication

The [Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory) topic provides a complete set of instructions to create the app.

These steps will describe how to create an app registration in Azure AD and run a .NET Core CLI command to generate the scaffold for the basic app with support for Azure AD authentication.

> [!NOTE]
> At this time, you must use the .NET Core CLI command to generate the app. There is no template for this specific type of app when creating a project using Visual Studio.

Go to [Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory) and follow the instructions there to generate the basic app template. 

> [!NOTE]
> The rest of the content in this section provides supplemental information to assist in completing the steps described in the [Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory) topic. 
> 
> You may want to review this as you complete those steps, but it is not required. When you are done, come back here and start with [Step 3 Grant API permissions](#step-3-grant-api-permissions).

Registering the application involves completing a form. The default value for the Redirect URI includes a placeholder for the port value. You must replace the placeholder with a number value to complete the registration, for example, just add `1111` for now. You can provide the randomly generated port value later after you open the project in Visual Studio. See [Update callback URL](#update-callback-url).

:::image type="content" source="media/blazor-webassembly-walkthrough-register-application.png" alt-text="The form to register an application in Azure Active Directory.":::

This will generate two ID values that you will need to include in the .NET Core CLI command. The following placeholders will be used in the content. You must use the values generated by the application registration process.

- The Application (Client) Id : Placeholder: `11111111-1111-1111-1111-111111111111`
- Directory (Tenant) Id : Placeholder: `22222222-2222-2222-2222-222222222222`

> [!IMPORTANT]
> Follow the instructions in the [Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory) topic to enable Access Tokens and ID tokens to enable the implicit grant and save your changes.

The .NET Core CLI command can be formatted this way and include a parameter to specify where the project should be created. You can run the command in an ordinary command window.

```dotnetcli
dotnet new blazorwasm^
 -au SingleOrg^
 --client-id "11111111-1111-1111-1111-111111111111"^
 --tenant-id "22222222-2222-2222-2222-222222222222"^
 -o "A:\Projects\Blazor-Standalone-AAD Example"
```

After you have run the command, navigate to the output folder and open the .csproj file using Visual Studio 2019.

:::image type="content" source="media/blazor-webassembly-walkthrough-application-files-folder.png" alt-text="The files generated by the template viewed in windows explorer.":::

Within Visual Studio 2019 the project looks like this:

:::image type="content" source="media/blazor-webassembly-walkthrough-application-solution-explorer.png" alt-text="The project generated by the template viewedin the Visual Studio solution explorer":::

The rest of the [Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory) topic describes the components of the app template.

### Update callback URL

The port setting used by Visual Studio is randomly generated. The callback URI in the application registration must be updated so that you can debug the app.

1. In Visual Studio, open the project properties and select **Debug**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-project-debug-settings.png" alt-text="The Visual Studio project Debug page.":::

1. Under **Web Server Settings** copy the **Enable SSL** value that includes the random port assigned for debugging
1. Return to your app registration in Azure AD, In the **Authentication** section, change the **Redirect URI** to include this root Uri, then save your changes

    :::image type="content" source="media/blazor-webassembly-walkthrough-application-redirect-uri.png" alt-text="The registered application Authentication information.":::

### Verify that the app runs

Now that the Redirect URI has been updated; you should be able to press F5 in Visual Studio to run the app.

:::image type="content" source="media/blazor-webassembly-walkthrough-application-before-code-changes.png" alt-text="The default behavior of the Blazor WebAssembly app before changes are made.":::

At this point, all the capabilities of the app work whether you log-in or not. Only members of the Azure AD tenant can log in.

## Step 3: Grant API permissions

To connect to Dataverse, you must configure permissions for the app to connect.

1. Return to your app registration in Azure AD, In the **API permissions** section, click **Add a permission**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-add-permissions.png" alt-text="The registered application API Permissions settings page.":::

1. In the **Request API permissions** area, select **APIs my organization uses** and search for *Common Data Service*.

    :::image type="content" source="media/blazor-webassembly-walkthrough-search-common-data-service-api.png" alt-text="Searching for the Dataverse permissions.":::

1. Select **Common Data Service**. 
1. Select the **user_impersonation** permission

    :::image type="content" source="media/blazor-webassembly-walkthrough-user-impersonation-permission.png" alt-text="Adding the Dataverse user_impersonation permission.":::

    > [!NOTE]
    > Dynamics CRM and Dataverse refer to the same service.

1. Click **Add permissions**.
1. (Optional) For the **Configured permissions**, click **Grant Admin consent for [Your Azure Active Directory tenant name]**. In the screenshot below the tenant name is ‘Default Directory’. Yours may be different.

    :::image type="content" source="media/blazor-webassembly-walkthrough-grant-admin-consent.png" alt-text="The button showing the optional button to grant admin consent for the registered application.":::

## Step 4: Apply code changes

Apply changes to the following files to enable displaying Dataverse data in the application.

### \wwwroot\appsettings.json

You will find that this file already has configuration information generated by the template with information about the application registered in Azure AD. It will look like this:

```json
{
  "AzureAd": {
    "Authority": "https://login.microsoftonline.com/22222222-2222-2222-2222-222222222222",
    "ClientId": "11111111-1111-1111-1111-111111111111",
    "ValidateAuthority": true
  }
}
```

Update the file to include a new `CDSWebAPI` section that includes the root of the **Instance Web API Service Root URL** you copied in the [Get the Dataverse Web API URI](#get-the-dataverse-web-api-uri) step.

> [!NOTE]
> You don’t need the full URL, just the root.

```json
{
  "AzureAd": {
    "Authority": "https://login.microsoftonline.com/22222222-2222-2222-2222-222222222222",
    "ClientId": "11111111-1111-1111-1111-111111111111",
    "ValidateAuthority": true
  },
  "CDSWebAPI": {
    "ResourceUrl": "https://yourorg.api.crm.dynamics.com",
    "Version": "v9.1",
    "TimeoutSeconds": 30
  }
}
```

### Program.cs

1. Install the `Microsoft.Extensions.Http` NuGet package.
    1. In the solution explorer, right-click the project and select **Manage NuGet Packages...**.
    1. Select **Browse** and search for `Microsoft.Extensions.Http`.
    1. Install the latest version of the package.

    :::image type="content" source="media/blazor-webassembly-walkthrough-install-microsoft.extensions.http-nuget-package.png" alt-text="Install the required NuGet package":::

1. Add the following code below the line that starts with `builder.Services.AddTransient(sp => new HttpClient...`

    ```csharp
    // Get configuration data about the Web API set in wwwroot/appsettings.json
    var CDSWebApiConfig = builder.Configuration.GetSection("CDSWebAPI");
    var resourceUrl = CDSWebApiConfig.GetSection("ResourceUrl").Value;
    var version = CDSWebApiConfig.GetSection("Version").Value;
    var timeoutSeconds = int.Parse(CDSWebApiConfig.GetSection("TimeoutSeconds").Value);

    // Create an named definition of an HttpClient that can be created in a component page
    builder.Services.AddHttpClient("CDSClient", client =>
    {
        // See https://docs.microsoft.com/powerapps/developer/data-platform/webapi/compose-http-requests-handle-errors
        client.BaseAddress = new Uri($"{resourceUrl}/api/data/{version}/");
        client.Timeout = TimeSpan.FromSeconds(timeoutSeconds);
        client.DefaultRequestHeaders.Add("OData-Version", "4.0");
        client.DefaultRequestHeaders.Add("OData-MaxVersion", "4.0");
    });
    ```

1. Add the following code below the line that starts with `builder.Configuration.Bind("AzureAd" ...`

    ```csharp
    // Add access to Dataverse to the scope of the access token when the user signs in
    options.ProviderOptions.DefaultAccessTokenScopes.Add($"{resourceUrl}/user_impersonation");
    ```

### Add \Pages\FetchAccounts.razor

This is a new page that will display the account information.

1. In solution explorer, right click **Pages** and select **Add** > **Razor Component…** from the context menu and name it `FetchAccounts.razor`.
1. Replace the code in the file with the following:

    ```cshtml
    @page "/fetchaccounts"
    @using Microsoft.AspNetCore.Components.WebAssembly.Authentication
    @using System.Net.Http.Headers
    @using System.Net.Http.Json
    @using Microsoft.Extensions.Logging;
    @using System.Text.Json.Serialization;
    @inject IAccessTokenProvider TokenProvider
    @inject IHttpClientFactory ClientFactory
    @inject ILogger<FetchAccounts> logger;

    <AuthorizeView>
        @*Only show the list if the user is signed in and authorized*@
        <Authorized>
            <h3>Fetch Accounts</h3>

            @if (accounts != null)
            {
                <table class="table">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Main Phone</th>
                            <th>City</th>
                            <th>Primary Contact</th>
                            <th>Email (Primary Contact)</th>
                        </tr>
                    </thead>
                    <tbody>
                        @foreach (Account account in accounts.value)
                        {
                            <tr id="@account.accountid">
                                <td>
                                    @((account.name != null)
                                    ? account.name
                                    : string.Empty)
                                </td>
                                <td>
                                    @((account.telephone1 != null)
                                    ? account.telephone1
                                    : string.Empty)
                                </td>
                                <td>
                                    @((account.address1_city != null)
                                    ? account.address1_city
                                    : string.Empty)
                                </td>
                                <td>
                                    @((account.primarycontactid != null)
                                    ? (account.primarycontactid.fullname != null
                                        ? account.primarycontactid.fullname
                                        : string.Empty)
                                    : string.Empty)
                                </td>
                                <td>
                                    @((account.primarycontactid != null)
                                    ? (account.primarycontactid.emailaddress1 !=null
                                        ? account.primarycontactid.emailaddress1
                                        : string.Empty)
                                    : string.Empty)
                                </td>
                            </tr>
                        }
                    </tbody>
                </table>
            }
            else
            {
                <p><em>@message</em></p>
            }
        </Authorized>
        <NotAuthorized>
            <h3>Authentication Failure!</h3>
            <p>You're not signed in.</p>
        </NotAuthorized>
    </AuthorizeView>


    @code {

        //The collection of Account records to display
        private AccountCollection accounts;

        //An informational message
        private string message = "Loading...";

        //Contains data about an error returned from the Web API
        private Error error;

        // Method invoked when the component is ready to start, having received its initial parameters from its parent in the render tree.
        // Override this method if you will perform an asynchronous operation and want the component to refresh when that operation is completed.
        protected override async Task OnInitializedAsync()
        {
            // Tries to get an access token for the current user with the default set of permissions.
            var tokenResult = await TokenProvider.RequestAccessToken();

            // If the token request was successful
            if (tokenResult.TryGetToken(out var token))
            {
                //Creates an HttpClient based on the named definition found in Program.Main
                var client = ClientFactory.CreateClient("CDSClient");

                //Prepare the request to get the data
                var request = new HttpRequestMessage()
                {
                    Method = HttpMethod.Get,
                    RequestUri = new Uri($"{client.BaseAddress}accounts?" +
                    "$select=name,telephone1,address1_city&" +
                    "$expand=primarycontactid($select=fullname,emailaddress1)")
                };
                //Add the access token
                request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token.Value);
                //Specify a JSON result is expected
                request.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                //Limit the number of results to 10
                request.Headers.Add("Prefer", "odata.maxpagesize=10");

                //Send the request
                var response = await client.SendAsync(request);

                if (response.IsSuccessStatusCode)
                {
                    //Parse the JSON returned into a strongly typed AccountCollection
                    accounts = await response.Content.ReadFromJsonAsync<AccountCollection>();
                }
                else
                {
                    //Parse the JSON returned into a strongly typed Error
                    error = await response.Content.ReadFromJsonAsync<Error>();
                    error.statuscode = (int)response.StatusCode;
                    error.reason = response.ReasonPhrase;
                    //Display a message to the user
                    message = "An error occurred.";
                    //Log the details so they can be seen in the browser console
                    logger.LogError($"{error.detail.message}");

                }

            }
            else
            {
                // Notify user that the token request was not successful
                message = "There was a problem authenticating.";
            }

        }


        // The result will be a JSON object with an array of entities set to the value property
        public class AccountCollection
        {
            public Account[] value { get; set; }
        }

        //Just the properties of the Account EntityType used for this sample
        // See https://docs.microsoft.com/dynamics365/customer-engagement/web-api/account
        public class Account
        {

            public Guid accountid { get; set; }

            public string name { get; set; }

            public string telephone1 { get; set; }

            public string address1_city { get; set; }

            public Contact primarycontactid { get; set; }

        }

        //Just the properties of the Contact EntityType that are expanded from the Account entity
        // See https://docs.microsoft.com/dynamics365/customer-engagement/web-api/contact
        public class Contact
        {

            public string fullname { get; set; }

            public string emailaddress1 { get; set; }
        }

        // Contains the error data returned by the Web API and the HttpMessageResponse
        public class Error
        {
            [JsonPropertyName("error")]
            public ErrorDetail detail { get; set; }
            public int statuscode { get; set; }
            public string reason { get; set; }

        }

        //Contains data from the Web API
        //See https://docs.microsoft.com/powerapps/developer/data-platform/webapi/compose-http-requests-handle-errors#parse-errors-from-the-response
        public class ErrorDetail
        {
            public string code { get; set; }
            public string message { get; set; }

        }
    }
    ```

This code does the following:

1. Ensures that only authenticated users can view the page with data.
1. Defines a table to display Account data after it is retrieved.
1. Requests an accesstoken and then uses that token with an HttpRequestMessage to retrieve data from Dataverse.
1. Defines classes to enable strongly typed data when the JSON returned from the service is deserialized.

### \Shared\NavMenu.razor

Edit this file to add the fetchaccounts razor component page.

Add this node where ever you like within the `<ul class="nav flex-column">` element.

```html
<li class="nav-item px-3">
    <NavLink class="nav-link" href="fetchaccounts">
        <span class="oi oi-list-rich" aria-hidden="true"></span> Fetch Accounts
    </NavLink>
</li>
```

## Step 5: Verify it works

In Visual Studio, press F5 to launch the app with the code changes.

1. Before logging in, navigate to **Fetch Accounts**. You should expect to see the failure notification.
1. Log-in as a user who has access to the Dataverse data.

    > [!NOTE]
    > If you did not grant admin consent in [Step 3: Grant API permissions](#step-3-grant-api-permissions), users can expect to see a dialog like this:
    > 
    > :::image type="content" source="media/blazor-webassembly-walkthrough-request-consent-dialog.png" alt-text="The dialog to prompt the user to grant consent to the application.":::
    >
    > You must click **Accept** to continue.

1. Navigate to **Fetch Accounts** and verify that the Account data is displayed as expected:

    :::image type="content" source="media/blazor-webassembly-walkthrough-goal.png" alt-text="The final expected behavior for successfully completing the walkthrough.":::

### See also

[Use the global Discovery service from a Blazor WebAssembly](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/webapi/C%23/BlazorCDS)  
[Quickstart: Blazor Server Web API sample (C#)](./webapi/quick-start-blazor-server-app.md)  
[Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory)<br />
[Walkthrough: Register an app with Azure Active Directory](walkthrough-register-app-azure-active-directory.md)<br />
[Use OAuth with Dataverse](authenticate-oauth.md)<br />
[Use the Dataverse Web API](webapi/overview.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]