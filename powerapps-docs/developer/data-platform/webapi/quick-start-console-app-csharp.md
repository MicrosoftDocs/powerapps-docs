---
title: "Quick Start: Web API sample (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "Walks you through creating a program to authenticate with the Microsoft Dataverse Server and then call a Web API function."
ms.custom: intro-internal
ms.date: 09/28/2021
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
ms.reviewer: "pehecke"
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Quick Start: Web API sample (C#)

In this quick start you will create a simple console application to connect to your target Microsoft Dataverse environment and invoke the Web API `WhoAmI` function. This function retrieves information about the logged on Dataverse user. Once you understand the basic functionality described here, you can move onto other Web API operations such as create, retrieve, update, and deletion of Dataverse table rows.

This program will authenticate and use an <xref:System.Net.Http.HttpClient> to send a `GET` request to the <xref href="Microsoft.Dynamics.CRM.WhoAmI?text=WhoAmI Function" /> the response will be a <xref href="Microsoft.Dynamics.CRM.WhoAmIResponse?text=WhoAmIResponse ComplexType" />. The program will then display the `UserId` property value obtained from the response.

> [!NOTE]
> This is a very simple example to show how to get connected with a minimum of code. The [Enhanced quick start](enhanced-quick-start.md) will build upon this sample to apply better design patterns.

You can find the complete Visual Studio solution for this project in the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repo under cds/webapi/C#/QuickStart.

## Prerequisites

 - Visual Studio 2019
 - Internet connection
 - Valid user account for a Dataverse environment
 - Url to the Dataverse environment you want to connect with
 - Basic understanding of the Visual C# language

> [!NOTE]
> To authenticate you must have an app registered in Azure Active Directory (AD). This quick start example provides an app registration `clientid` value you can use for the purpose of running sample code published by Microsoft. However, for your own custom applications you must register your apps with AD. More information: [Walkthrough: Register an app with Azure Active Directory](../walkthrough-register-app-azure-active-directory.md)

## Create Visual Studio project

1. Launch Visual Studio and select **Create a new project**.

1. Create a new Console App (.NET Framework) project.

    :::image type="content" source="media/quickstart-new-project.png" alt-text="New console app project":::

1. Configure the project to use .NET Framework 4.6.2.

    :::image type="content" source="media/quickstart-configure-project.png" alt-text="Configure the project":::

1. In **Solution Explorer**, right-click the project you created and select **Manage NuGet Packages** in the context menu. We will now bring in required assemblies for our project.

1. Browse for the  `Microsoft.IdentityModel.Clients.ActiveDirectory` NuGet package, select it, and then choose **Install**.

    :::image type="content" source="media/quickstart-nuget-package-install.png" alt-text="Install the Active Directory Nuget package" lightbox="media/quickstart-nuget-package-install.png":::

    > [!NOTE]
    > You will be prompted to preview and **OK** the assembly additions, and **Accept** the license agreements, for the installed packages and their contents.

    To use the Microsoft Authentication Library (MSAL) instead of Azure Active Directory Authentication Library (ADAL), browse for an install the `Microsoft.Identity.Client` package.

1. Browse for the `Newtonsoft.Json` NuGet package and install the latest version.

    :::image type="content" source="media/quickstart-nuget-package-json.png" alt-text="Install the JSON package" lightbox="media/quickstart-nuget-package-json.png":::

## Edit Program.cs

Follow these next steps to add code for the main program.

1. Replace the entire contents of Program.cs with the following code. If you used a different name for your project than WebAPIQuickStart, you will need to change to namespace name in the new code to match your project name.

#### [C#/ADAL](#tab/adal)

```csharp
using Microsoft.IdentityModel.Clients.ActiveDirectory;
using Newtonsoft.Json.Linq;
using System;
using System.Net.Http;
using System.Net.Http.Headers;

namespace WebAPIQuickStart
{
    class Program
    {
        static void Main()
        {
            // TODO Specify the Dataverse environment URL to connect with.
            string resource = "https://<env-name>.<region>.dynamics.com";

            // Azure Active Directory app registration shared by all Power App samples.
            // For your custom apps, you will need to register them with Azure AD yourself.
            // See https://docs.microsoft.com/powerapps/developer/data-platform/walkthrough-register-app-azure-active-directory
            var clientId = "51f81489-12ee-4a9e-aaae-a2591f45987d";
            var redirectUri = new Uri("app://58145B91-0C36-4500-8554-080854F2AC97");

            #region Authentication

            // The authentication context used to acquire the web service access token
            var authContext = new AuthenticationContext(
                "https://login.microsoftonline.com/common", false);

            // Get the web service access token. Its lifetime is about one hour after
            // which it must be refreshed. For this simple sample, no refresh is needed.
            // See https://docs.microsoft.com/powerapps/developer/data-platform/authenticate-oauth
            var token = authContext.AcquireTokenAsync(
                resource, clientId, redirectUri,
                new PlatformParameters(
                    PromptBehavior.SelectAccount   // Prompt the user for a logon account.
                ),
                UserIdentifier.AnyUser
            ).Result;
            #endregion Authentication

            #region Client configuration

            var client = new HttpClient
            {
                // See https://docs.microsoft.com/en-us/powerapps/developer/data-platform/webapi/compose-http-requests-handle-errors#web-api-url-and-versions
                BaseAddress = new Uri(resource + "/api/data/v9.2/"),
                Timeout = new TimeSpan(0, 2, 0)    // Standard two minute timeout on web service calls.
            };

            // Default headers for each Web API call.
            // See https://docs.microsoft.com/powerapps/developer/data-platform/webapi/compose-http-requests-handle-errors#http-headers
            HttpRequestHeaders headers = client.DefaultRequestHeaders;
            headers.Authorization = new AuthenticationHeaderValue("Bearer", token.AccessToken);
            headers.Add("OData-MaxVersion", "4.0");
            headers.Add("OData-Version", "4.0");
            headers.Accept.Add(
                new MediaTypeWithQualityHeaderValue("application/json"));
            #endregion Client configuration

            #region Web API call

            // Invoke the Web API 'WhoAmI' unbound function.
            // See https://docs.microsoft.com/powerapps/developer/data-platform/webapi/compose-http-requests-handle-errors
            // See https://docs.microsoft.com/powerapps/developer/data-platform/webapi/use-web-api-functions#unbound-functions
            var response = client.GetAsync("WhoAmI").Result;

            if (response.IsSuccessStatusCode)
            {
                // Parse the JSON formatted service response to obtain the user ID.  
                JObject body = JObject.Parse(
                    response.Content.ReadAsStringAsync().Result);
                Guid userId = (Guid)body["UserId"];

                Console.WriteLine("Your user ID is {0}", userId);
            }
            else
            {
                Console.WriteLine("Web API call failed");
                Console.WriteLine("Reason: " + response.ReasonPhrase);
            }
            #endregion Web API call

            // Pause program execution.
            Console.ReadKey();
        }
    }
}
```

#### [C#/MSAL](#tab/msal)

```csharp
using Microsoft.Identity.Client;
using Newtonsoft.Json.Linq;
using System;
using System.Net.Http;
using System.Net.Http.Headers;

namespace PowerApps.Samples
{
    class Program
    {
        static void Main()
        {
            // TODO Specify the Dataverse environment name to connect with.
            string resource = "https://<env-name>.api.<region>.dynamics.com";

            // Azure Active Directory app registration shared by all Power App samples.
            // For your custom apps, you will need to register them with Azure AD yourself.
            // See https://docs.microsoft.com/powerapps/developer/data-platform/walkthrough-register-app-azure-active-directory
            var clientId = "51f81489-12ee-4a9e-aaae-a2591f45987d";
            var redirectUri = "app://58145B91-0C36-4500-8554-080854F2AC97";

            #region Authentication

            var authBuilder = PublicClientApplicationBuilder.Create(clientId)
                             .WithAuthority(AadAuthorityAudience.AzureAdMultipleOrgs)
                             .WithRedirectUri(redirectUri)
                             .Build();
            var scope = resource + "/.default";
            string[] scopes = { scope };

            AuthenticationResult token = 
                authBuilder.AcquireTokenInteractive(scopes).ExecuteAsync().Result;
            #endregion Authentication

            #region Client configuration

            var client = new HttpClient
            {
                // See https://docs.microsoft.com/powerapps/developer/data-platform/webapi/compose-http-requests-handle-errors#web-api-url-and-versions
                BaseAddress = new Uri(resource + "/api/data/v9.2/"),
                Timeout = new TimeSpan(0, 2, 0)    // Standard two minute timeout on web service calls.
            };

            // Default headers for each Web API call.
            // See https://docs.microsoft.com/powerapps/developer/data-platform/webapi/compose-http-requests-handle-errors#http-headers
            HttpRequestHeaders headers = client.DefaultRequestHeaders;
            headers.Authorization = new AuthenticationHeaderValue("Bearer", token.AccessToken);
            headers.Add("OData-MaxVersion", "4.0");
            headers.Add("OData-Version", "4.0");
            headers.Accept.Add(
                new MediaTypeWithQualityHeaderValue("application/json"));
            #endregion Client configuration

            #region Web API call

            // Invoke the Web API 'WhoAmI' unbound function.
            // See https://docs.microsoft.com/powerapps/developer/data-platform/webapi/compose-http-requests-handle-errors
            // See https://docs.microsoft.com/powerapps/developer/data-platform/webapi/use-web-api-functions#unbound-functions
            var response = client.GetAsync("WhoAmI").Result;

            if (response.IsSuccessStatusCode)
            {
                // Parse the JSON formatted service response to obtain the user ID.  
                JObject body = JObject.Parse(
                    response.Content.ReadAsStringAsync().Result);
                Guid userId = (Guid)body["UserId"];

                Console.WriteLine("Your user ID is {0}", userId);
            }
            else
            {
                Console.WriteLine("Web API call failed");
                Console.WriteLine("Reason: " + response.ReasonPhrase);
            }
            #endregion Web API call

            // Pause program execution by waiting for a key press.
            Console.ReadKey();
        }
    }
}
```

---

2. Right below the TODO comment in the above code, replace the `resource` value with the actual URL of your Dataverse test environment. To find the URL value for your test environment, follow these steps:

    1. Navigate your browser to [Power Apps](https://make.powerapps.com).
    1. Select the environments icon (to the right of the search field), and choose a test environment.
    1. Select the settings icon ![Settings button.](media/settings-icon.png) and choose **Developer resources**.
    1. Copy the Web API endpoint URL from "https:" through ".com" leaving off the /api/data/v9.x.
    1. Replace the resource string value in the program code with that endpoint URL value. For example:<p/>
        `string resource = "https://contoso.api.crm.dynamics.com";`

## Run the program

1. Press F5 to build and run the program. The output should look something like this:

    `Your user ID is 969effb0-98ae-478c-b547-53a2968c2e75`

2. With the console window active, press any key to terminate the program.

### Congratulations!

You have successfully connected to the Web API.

The quick start sample shows a simple approach to create a Visual Studio project without any exception handling or method to refresh the access token.

This is enough to verify you can connect, but it doesn't necessarily represent a good pattern for building an app.

The [Enhanced quick start](enhanced-quick-start.md) topic shows how to implement exception handling methods, basic authentication method using connection string, a re-usable method to refresh the access token, and introduces how to build re-usable methods to perform data operations.

## Next steps

Learn how to structure your code for a better design.

> [!div class="nextstepaction"]
> [Enhanced quick start](enhanced-quick-start.md)<br/>

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
