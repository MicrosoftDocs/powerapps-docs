---
title: "Quickstart: Blazor Server Web API sample (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to authenticate with a Microsoft Dataverse from a Blazor Server application and then call a basic WhoAmI Web API function."
ms.date: 12/20/2022
ms.topic: article
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
ms.reviewer: pehecke
search.audienceType: 
  - developer
---
# Quickstart: Blazor Server Web API sample (C#)

In this quickstart, you create a Blazor Server application to connect to your Microsoft Dataverse environment using the Web API.

You authenticate and use <xref:System.Net.Http.HttpClient> to send a `GET` request containing the [WhoAmI Function](xref:Microsoft.Dynamics.CRM.WhoAmI). The response is a [WhoAmIResponse ComplexType ](xref:Microsoft.Dynamics.CRM.WhoAmIResponse). After call completion, the `WhoAmIResponse` properties are displayed.

> [!NOTE]
> This is a very simple example to show how to get connected with a minimum of code.

## Prerequisites

- Visual Studio 2022 with the **ASP.NET and web development** workload.
- [.NET 7.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/7.0).
- Familiarity with the Microsoft Azure portal.
- Internet connection.
- Valid user account for a Dataverse instance.
- Administrator access to grant application registrations.
- URL to the Dataverse environment you want to connect with.
- Basic understanding of the Visual C# language.


> [!NOTE]
> To authenticate you must have an app registered in Azure Active Directory. The registration will happen automatically as part of the template creation, but will require additional updates in the Azure portal.

## Create a Visual Studio project

1. Open Visual Studio 2022 and select **Create a new project**.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-1.png" alt-text="Open Visual Studio 2022":::

1. In the **Create a new project** dialog, search for *Blazor Server App*. Select the template and select **Next**.

    :::image type="content" source="../media/quick-start-blazor-server-app-csharp-2.png" alt-text="Create a new project":::

1. In the **Configure your new project** dialog, set the **Project name**, and **Location**. Then select **Next**.

    :::image type="content" source="../media/quick-start-blazor-server-app-csharp-2.5.png" alt-text="Enter project name and location":::

   In this example, we'll use **DataverseWebApiBlazorServerQuickStart** as the **Project name**.

1. In the **Additional information** dialog, specify **Framework** and **Authentication type**.

   In this example, the Framework is **.NET 7.0 (Standard Term Support)**.

   > [!IMPORTANT]
   > Set the **Authentication type** to **Microsoft identity platform**.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-3.png" alt-text="Set the Authentication type to Microsoft identity platform":::

1. Select **Create** to create the project.
1. The project template opens a **Required components** dialog. Select **Next**.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-4.png" alt-text="Required components":::

1. In the **Microsoft identity platform** dialog, make sure that the selected Azure account has permissions to manage applications in Azure AD and the selected tenant is the one associated with your Power Platform environment.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-5.png" alt-text="Microsoft identity platform dialog":::

1. Select **Create new**.
1. In the **Register an application** dialog, set the **Display name** and select **Register** to close the dialog.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-6.png" alt-text="Register an application":::

   In this example, we're using the name *Dataverse Web Api Blazor Server Quick Start*. We'll search for the application using this name in a later step.

1. Select **Next**.

    > [!NOTE]
    > You don't need to do anything in this step.

   This step provides capabilities to connect to Microsoft Graph or another API, but connecting to another API isn't necessary for this quickstart.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-6.5.png" alt-text="Additional settings step.":::

1. Select **Next**. This step summarizes the changes that are made to the project.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-6.6.png" alt-text="Summary of changes":::

1. Select **Finish**.

   The **Dependency configuration progress** dialog shows the automated steps performed by the template to register the application.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-7.png" alt-text="Dependency configuration progress":::

1. Select **Close** to close the dialog.

## Configure the application in Active Directory

The Visual Studio template created a registered application using the information you provided. Connecting to Dataverse requires more permissions.

1. From the [Power Platform admin center](https://admin.powerplatform.microsoft.com/home), select the **Azure Active Directory** admin center.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-8.png" alt-text="Azure Active Directory admin center from the Power Platform admin center":::

1. In the **Microsoft Entra admin center**, search for the application created by name within **App Registrations**.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-9.png" alt-text="Search for the application registration":::

1. Open the application and select **API permissions**. Select **Add a permission**.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-10.png" alt-text="API permissions":::

1. In the **Request API permissions** fly-out, select the **APIs my organization uses** tab and search for *Dataverse*.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-11.png" alt-text="search for Dataverse in APIs my organization uses":::

1. Select **Dataverse**, and **Dynamics CRM API** opens.
1. Select the `user_impersonation` delegated permission and select **Add permissions**.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-12.png" alt-text="Add the user_impersonation delegated privilege":::

1. Select **Certificates & secrets** and select **New client secret**.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-13.png" alt-text="Certificates & secrets":::

1. In the **Add a client secret** fly-out, enter a **Description** and **Expires** duration, then select **Add**.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-14.png" alt-text="Add a client secret":::

   > [!IMPORTANT]
   > Copy the secret now. You can't access it after you leave this page.

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-15.png" alt-text="Copy the client secret":::

1. In Visual Studio, within your Blazor Server app project, open `appsettings.json` and add an entry for `ClientSecret` with the secret value. The contents of the `appsettings.json` file should look like this:
    
    ```json
    {
    "AzureAd": {
        "Instance": "https://login.microsoftonline.com/",
        "Domain": "<your org>.onmicrosoft.com",
        "TenantId": "<your tenantid>",
        "ClientId": "<your clientid>",
        "CallbackPath": "/signin-oidc",
        "ClientSecret": "<your secret>"
    },
    "Logging": {
        "LogLevel": {
        "Default": "Information",
        "Microsoft.AspNetCore": "Warning"
        }
    },
    "AllowedHosts": "*"
    }
    ```

## Edit the app

To enable calls to Dataverse, you must edit three files in the application:

- appsettings.json
- Program.cs
- Pages/FetchData.razor

### appsettings.json

There are several places in the other files that require a reference to the base uri used to access the Dataverse Web API. Adding this data to the `appsettings.json` allows you to set this data in one place.

Add the following below `"AllowedHosts": "*"` where `<your org>` represents the base url to access the Dataverse Web API. If you aren't sure what this is, see [Web API URL and versions](compose-http-requests-handle-errors.md#web-api-url-and-versions).

```json
  "AllowedHosts": "*",
  "DataverseConfig": {
    "BaseUri": "https://<your org>.api.crm.dynamics.com/"
  }
```

> [!NOTE]
> Make sure to :
> 
> - Add the comma after `"AllowedHosts": "*"` so that the JSON is valid.
> - End the `BaseUri` value with "`/`".

### Program.cs

1. To access the value of the Web API base URI in the settings, add the line below commented with `// Get BaseUri from appsettings.json`  in the `Main` method below the line: <br />`var builder = WebApplication.CreateBuilder(args);`

   ```csharp
   public static void Main(string[] args)
   {
     var builder = WebApplication.CreateBuilder(args);

     // Get BaseUri from appsettings.json
     string dataverseBaseUri = builder.Configuration.GetSection("DataverseConfig").GetValue<string>("BaseUri");
   ```

1. Add the following two lines below the line: <br />`.AddMicrosoftIdentityWebApp(builder.Configuration.GetSection("AzureAd"))`

   ```csharp
   // Add services to the container.
   builder.Services.AddAuthentication(OpenIdConnectDefaults.AuthenticationScheme)
     .AddMicrosoftIdentityWebApp(builder.Configuration.GetSection("AzureAd"))
       .EnableTokenAcquisitionToCallDownstreamApi(new string[] { $"{dataverseBaseUri}user_impersonation" })
       .AddInMemoryTokenCaches();
   ```
 
   - The [MicrosoftIdentityWebApiAuthenticationBuilder.EnableTokenAcquisitionToCallDownstreamApi Method](/dotnet/api/microsoft.identity.web.microsoftidentitywebapiauthenticationbuilder.enabletokenacquisitiontocalldownstreamapi) adds support for the web app to acquire tokens to call an API. By passing the `user_impersonation` scope, the user can consent to the capability to use the Dataverse Web API.
   - [AddInMemoryTokenCaches Method](xref:Microsoft.Identity.Web.MicrosoftIdentityAppCallsWebApiAuthenticationBuilder.AddInMemoryTokenCaches%2A) Enables caching the token issued for requests.


### Pages/FetchData.razor

The default `Pages/FetchData.razor` component retrieves some weather forecast data. We're going to replace this completely.

Copy the following code and replace all the code in `Pages/FetchData.razor`:

```razor
@page "/fetchdata"
@using Microsoft.Identity.Client;
@using Microsoft.Identity.Web
@using System.Text.Json;
@inject MicrosoftIdentityConsentAndConditionalAccessHandler ConsentHandler
@inject IHttpClientFactory HttpClientFactory
@inject Microsoft.Identity.Web.ITokenAcquisition TokenAcquisitionService
@inject IConfiguration configuration;

<PageTitle>WhoAmI</PageTitle>

<h1>WhoAmI</h1>

<p>This component demonstrates fetching data from Dataverse.</p>

@if (WhoIAm == null)
{
    <p><em>Loading...</em></p>
}
else
{
    <table class="table">
        <thead>
            <tr>
                <th>Property</th>
                <th>Value</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>BusinessUnitId</td>
                <td>@WhoIAm.BusinessUnitId</td>
            </tr>
            <tr>
                <td>OrganizationId</td>
                <td>@WhoIAm.OrganizationId</td>
            </tr>
            <tr>
                <td>UserId</td>
                <td>@WhoIAm.UserId</td>
            </tr>
        </tbody>
    </table>
}

@code {
    private WhoAmIResponse WhoIAm;
    private HttpClient _httpClient;

    protected override async Task OnInitializedAsync()
    {
        string baseUrl = configuration["DataverseConfig:BaseUri"];

        // Get the HttpClient
        _httpClient = HttpClientFactory.CreateClient();
        
        // Get the token
        var token = string.Empty;
        try
        {
            token = await TokenAcquisitionService.GetAccessTokenForUserAsync(new string[] { $"{baseUrl}user_impersonation" });
        }
        // Microsoft Identity Web specific exception class for use in Blazor or Razor pages to process the user challenge. 
        // Handles the MsalUiRequiredException.
        catch (MicrosoftIdentityWebChallengeUserException ex)
        {
            ConsentHandler.HandleException(ex);
        }
        catch (Exception)
        {
            throw new Exception("Error getting access token.");
        }

        // Set the auth token
        _httpClient.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", token);

        // Send the request
        var dataRequest = await _httpClient.GetAsync($"{baseUrl}api/data/v9.2/WhoAmI");

        if (dataRequest.IsSuccessStatusCode)
        {
            var jsonString = System.Text.Json.JsonDocument.Parse(await dataRequest.Content.ReadAsStreamAsync());
            WhoIAm = JsonSerializer.Deserialize<WhoAmIResponse>(jsonString);
        }
        else
        {
            throw new Exception("Error sending request.");
        }
    }

    // Used with System.Text.Json.JsonSerializer.Deserialize to deserialize response body
    public class WhoAmIResponse
    {
        public Guid BusinessUnitId { get; set; }
        public Guid OrganizationId { get; set; }
        public Guid UserId { get; set; }
    }

}
```

## Run the program

The application is now ready.

1. Press F5 to run the program. The first time the program runs you should see this consent dialog:

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-15.5.png" alt-text="Consent dialog":::

1. Select **Accept**.
1. Select **Fetch data**.

   The output should look like this:

   :::image type="content" source="../media/quick-start-blazor-server-app-csharp-16.png" alt-text="final result":::

**Congratulations!** You have successfully connected to the Web API.

This quickstart shows a simple approach to create a Blazor Server web application that connects to data in Dataverse.

Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"]
> [Web API types and operations](web-api-types-operations.md)



### See Also

[Tutorial: Create an ASP.NET Core Blazor WebAssembly App using Dataverse](../walkthrough-blazor-webassembly-single-tenant.md)<br />
[Tutorial: Create a Blazor Server app that uses the Microsoft identity platform for authentication](/azure/active-directory/develop/tutorial-blazor-server)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
