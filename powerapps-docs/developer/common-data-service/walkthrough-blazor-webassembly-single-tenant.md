---
title: "Walkthrough: Create an ASP.NET Core Blazor WebAssembly App using Common Data Service | Microsoft Docs"
description: ""
keywords: ""
ms.date: 05/25/2020
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

# Walkthrough: Create an ASP.NET Core Blazor WebAssembly App using Common Data Service

Use the steps in this walkthrough to create a Blazor WebAssembly app that connects to the Common Data Service (CDS). The focus of this topic is to understand the necessary steps to authenticate a user with a specific CDS instance and retrieve data.

Blazor WebAssembly is one of two hosting models available for ASP.NET Core Blazor, the other is Blazor Server. For a complete description of the differences, see [ASP.NET Core Blazor hosting models](/aspnet/core/blazor/hosting-models).

This walkthrough depends on the instructions in the [Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory) topic. Because CDS uses Azure Active Directory (AAD) for authentication, this walkthrough will describe how to modify the basic app created using the app template provided so that it can connect to CDS.

## Goal

When you complete this walkthrough, you will have a Blazor WebAssembly app that displays data from the CDS Account entity which the authenticated user has access to.

:::image type="content" source="media/blazor-webassembly-walkthrough-goal.png" alt-text="todo":::


## Prerequisites

To complete this walkthrough you must have:

- Access to a Power Apps environment with a CDS database
- A CDS user with a security role that provides read access to the Account and Contact entities
- Application Administrator, Application Developer, Cloud Application Administrator, or Hybrid Identity Administrator role access to the AAD tenant that the CDS environment uses.
- Understanding of the C# programming language
- Understanding of ASP.NET Core Blazor is helpful but not required
- The latest version of Visual Studio 2019 with the **ASP.NET and web development** workload installed.


## Step 1: Verify Prerequisites and information about the database

Let’s make sure that your environment is configured properly, and you understand where to perform the actions in Step 2.

### Verify CDS database

1. Open https://make.powerapps.com/ 
1. Select **Solutions** in the navigation pane.

    :::image type="content" source="media/blazor-webassembly-walkthrough-maker-portal.png" alt-text="todo":::

1. If you don’t see a list of installed solutions, use the environment selector at the top to choose a different environment which has a database. Otherwise create a new environment.

### Get the CDS Web API URI

> [!NOTE]
> These instructions were valid when this content was written. The steps may change in the future.

1. When you have an environment with the database you want to connect to, select the **Settings** (Gear) icon and choose **Advanced settings**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-advanced-settings.png" alt-text="todo":::

1. The Dynamics 365 settings app will open. Select **Settings** > **Customizations**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-settings-customizations.png" alt-text="todo":::

1. Then select **Developer Resources**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-instance-web-api.png" alt-text="todo":::

1. Then copy the **Instance Web API Service Root URL**. You will need this in the [Step 3: Apply code changes](#step-3-apply-code-changes).

    :::image type="content" source="media/blazor-webassembly-walkthrough-navigate-admin-center.png" alt-text="todo":::

### Navigate to the Azure Active Directory portal

1. Return to https://make.powerapps.com/.
1. In the ‘waffle’ icon at the top left and select **Admin**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-navigate-admin-center.png" alt-text="todo":::

1. This will take you to the Microsoft 365 admin center. In the left navigation, click **Show all** and select **Azure Active Directory**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-navigate-AAD-from-admin-center.png" alt-text="todo":::

1. This will take you to the Azure Active Directory admin center. Expand the left navigation pane and select **Azure Active Directory**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-aad-admin-center.png" alt-text="todo":::

This takes you to the starting point for Step 2.

## Step 2: Create a Blazor WebAssembly standalone app using AAD for authentication

The [Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory) topic provides a complete set of instructions to create the app.

These steps will describe how to create an app registration in AAD and run a .NET Core CLI command to generate the scaffold for the basic app with support for AAD authentication.

> [!NOTE]
> At this time, you must use the .NET Core CLI command to generate the app. There is no template for this app when creating a project using Visual Studio.

The rest of the content in this section provides supplemental information to assist in completing the steps described in the [Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory) topic.

Registering the application involves completing a form. The default value for the Redirect URI includes a placeholder for the port value. You must replace the placeholder with a number value to complete the registration, for example, just add `1111` for now. You can provide the randomly generated port value later after you open the project in Visual Studio. See [Update callback URL](#update-callback-url).

:::image type="content" source="media/blazor-webassembly-walkthrough-register-application.png" alt-text="todo":::

This will generate two ID values that you will need to include in the .NET Core CLI command. The following placeholders will be used in the content. You must use the values generated by the application registration process.

- The Application (Client) Id : Placeholder: `11111111-1111-1111-1111-111111111111`
- Directory (Tenant) Id : Placeholder: `22222222-2222-2222-2222-222222222222`

> [!IMPORTANT]
> Follow the instructions in the topic to enable Access Tokens and ID tokens to enable the implicit grant and save your changes.

The .NET Core CLI command can be formatted this way and include a parameter to specify where the project should be created. You can run the command in an ordinary command window.

```dotnetcli
dotnet new blazorwasm^
 -au SingleOrg^
 --client-id "11111111-1111-1111-1111-111111111111"^
 --tenant-id "22222222-2222-2222-2222-222222222222"^
 -o "A:\Projects\Blazor-Standalone-AAD Example"
```

After you have run the command, navigate to the output folder and open the .csproj file using Visual Studio 2019.

:::image type="content" source="media/blazor-webassembly-walkthrough-application-files-folder.png" alt-text="todo":::

Within Visual Studio 2019 the project looks like this:

:::image type="content" source="media/blazor-webassembly-walkthrough-application-solution-explorer.png" alt-text="todo":::

The rest of the [Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory) topic describes the components of the app template.

### Update callback URL

The port setting used by Visual Studio is randomly generated. The callback URI in the application registration must be updated so that you can debug the app.

1. In Visual Studio, open the project properties and select **Debug**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-project-debug-settings.png" alt-text="todo":::

1. Under **Web Server Settings** copy the **Enable SSL** value that includes the random port assigned for debugging
1. Return to your app registration in AAD, In the **Authentication** section, change the **Redirect URI** to include this root Uri, then save your changes

    :::image type="content" source="media/blazor-webassembly-walkthrough-application-redirect-uri.png" alt-text="todo":::

### Verify that the app runs

Now that the Redirect URI has been updated; you should be able to press F5 in Visual Studio to run the app.

:::image type="content" source="media/blazor-webassembly-walkthrough-application-before-code-changes.png" alt-text="todo":::

At this point, all the capabilities of the app work whether you log-in or not. Only members of the AAD tenant can log in.

### Grant API permissions

To connect to CDS, you must configure permissions for the app to connect.

1. Return to your app registration in AAD, In the **API permissions** section, click **Add a permission**.

    :::image type="content" source="media/blazor-webassembly-walkthrough-add-permissions.png" alt-text="todo":::

1. In the **Request API permissions** area, select **APIs my organization uses** and search for *Common Data Service*.

    :::image type="content" source="media/blazor-webassembly-walkthrough-search-common-data-service-api.png" alt-text="todo":::

1. Select **Common Data Service**. 
1. Select the **user_impersonation** permission

    :::image type="content" source="media/blazor-webassembly-walkthrough-user-impersonation-permission.png" alt-text="todo":::

    > [!NOTE]
    > Dynamics CRM and Common Data Service refer to the same service.

1. Click **Add permissions**.
1. (Optional) For the **Configured permissions**, click **Grant Admin consent for [Your Azure Active Directory tenant name]**. In the screenshot below the tenant name is ‘Default Directory’. Yours may be different.

    :::image type="content" source="media/blazor-webassembly-walkthrough-grant-admin-consent.png" alt-text="todo":::

## Step 3: Apply code changes

Apply changes to the following files

### \wwwroot\appsettings.json

Update the file to include a new `CDSWebAPI` section that includes the root of the **Instance Web API Service Root URL** you copied in the [Get the CDS Web API URI](#get-the-cds-web-api-uri) step.

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

1. Comment out or remove the following line:

    ```csharp
    builder.Services.AddTransient(sp => new HttpClient { BaseAddress = new Uri(builder.HostEnvironment.BaseAddress) });
    ```
    > [!NOTE]
    > This line enables an HttpClient to access JSON data within the web site for the Weather Forecast functionality. Changes in this walkthrough will break this functionality

1. Add the following code to replace the line commented out in step 1. This code will read configuration information from appsettings.json and enable an HttpClient to use for CDS Data.

    ```csharp
    var CDSWebApiConfig = builder.Configuration.GetSection("CDSWebAPI");
    var resourceUrl = CDSWebApiConfig.GetSection("ResourceUrl").Value;
    var version = CDSWebApiConfig.GetSection("Version").Value;
    var timeoutSeconds = int.Parse(CDSWebApiConfig.GetSection("TimeoutSeconds").Value);

    builder.Services.AddTransient(sp => new HttpClient
    {
        BaseAddress = new Uri($"{resourceUrl}/api/data/{version}/"),
        Timeout = TimeSpan.FromSeconds(timeoutSeconds)

    }
    );
    ```

1. Add the following line within the section where MSAL authentication options are configured.

    ```csharp
    builder.Services.AddMsalAuthentication(options =>
    {
        builder.Configuration.Bind("AzureAd", options.ProviderOptions.Authentication);

        options.ProviderOptions.DefaultAccessTokenScopes.Add($"{resourceUrl}/user_impersonation");

    });
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
    @inject IAccessTokenProvider TokenProvider
    @inject HttpClient Http

    <AuthorizeView>
        <Authorized>
            <h3>Fetch Accounts</h3>

            @if (accounts == null)
            {
                <p><em>Loading...</em></p>
                <p>@message</p>
                @if (error != null)
                {
                    <h3>Error:</h3>
                    <table>
                        <tr>
                            <td>Status Code: </td>
                            <td>@error.statuscode</td>
                        </tr>
                        <tr>
                            <td>Reason: </td>
                            <td>@error.reason</td>
                        </tr>
                        <tr>
                            <td>Code: </td>
                            <td>@error.error.code</td>
                        </tr>
                        <tr>
                            <td>Message: </td>
                            <td>@error.error.message</td>
                        </tr>
                    </table>

                }
            }
            else
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
        </Authorized>
        <NotAuthorized>
            <h3>Authentication Failure!</h3>
            <p>You're not signed in.</p>
        </NotAuthorized>
    </AuthorizeView>


    @code {

        private AccountCollection accounts;

        private string message;

        private Error error;

        protected override async Task OnInitializedAsync()
        {

            var tokenResult = await TokenProvider.RequestAccessToken();

            if (tokenResult.TryGetToken(out var token))
            {
                var request = new HttpRequestMessage()
                {
                    Method = HttpMethod.Get,
                    RequestUri = new Uri($"{Http.BaseAddress}accounts?" +
                    $"$select=name,telephone1,address1_city&" +
                    $"$expand=primarycontactid($select=fullname,emailaddress1)")
                };
                request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token.Value);
                request.Headers.Add("OData-MaxVersion", "4.0");
                request.Headers.Add("OData-Version", "4.0");
                request.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                request.Headers.Add("Prefer", "odata.maxpagesize=10");

                var response = await Http.SendAsync(request);

                if (response.IsSuccessStatusCode)
                {

                    accounts = await response.Content.ReadFromJsonAsync<AccountCollection>();
                }
                else
                {

                    error = await response.Content.ReadFromJsonAsync<Error>();
                    error.statuscode = (int)response.StatusCode;
                    error.reason = response.ReasonPhrase;
                }

            }
            else
            {
                message = "There was a problem authenticating.";
            }

        }

        public class AccountCollection
        {
            public Account[] value { get; set; }
        }

        public class Account
        {

            public Guid accountid { get; set; }

            public string name { get; set; }

            public string telephone1 { get; set; }

            public string address1_city { get; set; }

            public Contact primarycontactid { get; set; }

        }

        public class Contact
        {

            public string fullname { get; set; }

            public string emailaddress1 { get; set; }
        }

        public class Error
        {
            public ErrorDetail error { get; set; }
            public int statuscode { get; set; }
            public string reason { get; set; }

        }

        public class ErrorDetail
        {
            public string code { get; set; }
            public string message { get; set; }

        }
    }
    ```
This code does the following:

1. Ensures that only authenticated users can view it
1. Defines a table to display Account data after it is retrieved.
1. Displays error information if there is an error retrieving the Account data
1. Requests an accesstoken and then uses that token with an HttpRequestMessage to retrieve data from CDS
1. Defines classes to enable strongly typed data when the JSON returned from the service is deserialized.

### \Shared\NavMenu.razor

Edit this file to remove the navigation option for Fetch Data and replace it with one to fetch Account data.

Replace this:

```html
<li class="nav-item px-3">
    <NavLink class="nav-link" href="fetchdata">
        <span class="oi oi-list-rich" aria-hidden="true"></span> Fetch data
    </NavLink>
</li>
```

With this:

```html
<li class="nav-item px-3">
    <NavLink class="nav-link" href="fetchaccounts">
        <span class="oi oi-list-rich" aria-hidden="true"></span> Fetch Accounts
    </NavLink>
</li>
```

## Step 4: Verify Behavior

In Visual Studio, press F5 to launch the app with the code changes.

1. Before logging in, navigate to **Fetch Accounts**. You should expect to see the notification failure.
1. Log-in as a user who has access to the CDS data.

    > [!NOTE]
    > If you did not grant admin consent in [Grant API permissions](#grant-api-permissions), users can expect to see a dialog like this:
    > 
    > :::image type="content" source="media/blazor-webassembly-walkthrough-request-consent-dialog.png" alt-text="todo":::

1. Navigate to **Fetch Accounts** and verify that the Account data is displayed as expected:

    :::image type="content" source="media/blazor-webassembly-walkthrough-goal.png" alt-text="todo":::

### See also

[Secure an ASP.NET Core Blazor WebAssembly standalone app with Azure Active Directory](/aspnet/core/security/blazor/webassembly/standalone-with-azure-active-directory)<br />
[Walkthrough: Register an app with Azure Active Directory](walkthrough-register-app-azure-active-directory.md)<br />
[Use OAuth with Common Data Service](authenticate-oauth.md)<br />
[Use the Common Data Service Web API](webapi/overview.md)