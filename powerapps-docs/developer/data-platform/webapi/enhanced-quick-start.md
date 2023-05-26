---
title: "Enhanced quick start (Microsoft Dataverse)| Microsoft Docs"
description: "An enhanced quick start building on the simple quick start using Dataverse Web API"
ms.date: 05/04/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Enhanced quick start

This article demonstrates how to refactor the code in the [Quick start](quick-start-console-app-csharp.md) article by adding reusable <xref:System.Net.Http.HttpClient> and error handling methods. Complete the steps in the [Quick start](quick-start-console-app-csharp.md) article to create a new Visual Studio project before you begin this article, or [download](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/C%23/QuickStart) the MSAL version of the complete Visual Studio project.

If you get stuck following this enhanced quick start, you can [download](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/C%23/EnhancedQuickStart) the completed solution.

## Enable passing credentials in a connection string

Putting user credentials inside your code isn't a good practice. How you capture user credentials depends on the type of client you're making. For this console application, we'll set the credentials within the App.config file because it's a convenient way to move the credentials out of code. It's also the method used in the [Web API Data operations Samples (C#)](web-api-samples-csharp.md), so if you understand this method, you can easily see how the other Web API samples work.

Enabling passing these credentials requires three steps:

1. [Add the System.Configuration.ConfigurationManager NuGet package to the Visual Studio project](#add-the-systemconfigurationconfigurationmanager-nuget-package-to-the-visual-studio-project)
1. [Add an application configuration file](#add-an-application-configuration-file)
1. [Add a `using` directive in Program.cs](#add-using-directive-to-programcs)

### Add the System.Configuration.ConfigurationManager NuGet package to the Visual Studio project

1. In **Solution Explorer**, right-click **Dependencies** and select **Manage NuGet Packages...** in the context menu.
1. Browse for the NuGet package named `System.Configuration.ConfigurationManager`, select it, and then choose **Install**.

:::image type="content" source="media/enhanced-quick-start-nuget-package-install-light-theme.png" alt-text="Install the System.Configuration.ConfigurationManager package" lightbox="media/enhanced-quick-start-nuget-package-install-light-theme.png":::

### Add an application configuration file

1. In **Solution Explorer**, right-click the project and select Add > New Item...
1. Select **Application Configuration File**.

   These steps creates a new file named `App.config` in your project.

1. In **Solution Explorer**, open the **App.config** file. It should look something like this:

   ```xml
   <?xml version="1.0" encoding="utf-8" ?>
   <configuration>
   </configuration>
   ```

1. Edit the `<configuration>` element to add the `connectionStrings` node as shown below:

   ```xml
   <?xml version="1.0" encoding="utf-8" ?>
      <configuration>
      <!--Online using Microsoft 365-->
      <add name="Connect"
            connectionString="Url=https://yourorg.api.crm.dynamics.com;Username=yourname@yourorg.onmicrosoft.com;Password=mypassword;" />
   </connectionStrings>
   </configuration>
   ```

This creates a connection string that can be referenced by name, in this case `Connect`, so that you can define more than one connection if you wish.

Edit the connection string `Url`, `Username` and `Password` values in the `connectionString` parameter to match what you need to connect to your Microsoft Dataverse test environment.

### Add using directive to Program.cs

At the top of your `Program.cs` file, add this `using` directive:

```csharp
using System.Configuration;
```

## Add helper code

In the [Quick start](quick-start-console-app-csharp.md) example, all the code is within the `Program.cs` file. We're going to move the code that deals with connecting and creating an <xref:System.Net.Http.HttpClient> into a separate file of helper methods.

These helpers are also used in the [SampleHelper.cs](https://github.com/Microsoft/PowerApps-Samples/blob/master/dataverse/webapi/C%23/SampleHelpers.cs) file used by the [Web API Data operations Samples (C#)](web-api-samples-csharp.md). If you understand these helpers, you'll understand how they're used in the samples.

1. In **Solution Explorer**, right-click your project and select **Add** > **Class...** (or press `Shift`+`Alt`+`C`) to open the **Add New Item** dialog.

1. Specify a name for your class file. To follow the pattern used by the [Web API Data operations Samples (C#)](web-api-samples-csharp.md), call it `SampleHelpers.cs`.

   > [!NOTE]
   > The name of the class will determine how you will reference these helper properties and methods within your main program. The remaining instructions will assume you named the class `SampleHelpers`.

1. Add the following code to your `SampleHelpers.cs` file.

   ```csharp

   using System;
   using System.Linq;
   using System.Net.Http;

   namespace EnhancedQuickStart
   {
   /// <summary>
   /// Shared code for common operations used by many Power Apps samples.
   /// </summary>
   class SampleHelpers
   {
         //These sample application registration values are available for all online instances.
         //You can use these while running sample code, but you should get your own for your own apps
         public static string clientId = "51f81489-12ee-4a9e-aaae-a2591f45987d";
         public static string redirectUrl = "app://58145B91-0C36-4500-8554-080854F2AC97";

         /// <summary>
         /// Method used to get a value from the connection string
         /// </summary>
         /// <param name="connectionString"></param>
         /// <param name="parameter"></param>
         /// <returns>The value from the connection string that matches the parameter key value</returns>
         public static string GetParameterValueFromConnectionString(string connectionString, string parameter)
         {
            try
            {
               return connectionString.Split(';').Where(s => s.Trim().StartsWith(parameter)).FirstOrDefault().Split('=')[1];
            }
            catch (Exception)
            {
               return string.Empty;
            }
         }

         /// <summary>
         /// Returns an HttpClient configured with an OAuthMessageHandler
         /// </summary>
         /// <param name="connectionString">The connection string to use.</param>
         /// <param name="clientId">The client id to use when authenticating.</param>
         /// <param name="redirectUrl">The redirect Url to use when authenticating</param>
         /// <param name="version">The version of Web API to use. Defaults to version 9.2 </param>
         /// <returns>An HttpClient you can use to perform authenticated operations with the Web API</returns>
         public static HttpClient GetHttpClient(string connectionString, string clientId, string redirectUrl, string version = "v9.2")
         {
            string url = GetParameterValueFromConnectionString(connectionString, "Url");
            string username = GetParameterValueFromConnectionString(connectionString, "Username");
            string password = GetParameterValueFromConnectionString(connectionString, "Password");
            try
            {
               HttpMessageHandler messageHandler = new OAuthMessageHandler(url, clientId, redirectUrl, username, password,
                              new HttpClientHandler());

               HttpClient httpClient = new HttpClient(messageHandler)
               {
                     BaseAddress = new Uri(string.Format("{0}/api/data/{1}/", url, version)),

                     Timeout = new TimeSpan(0, 2, 0)  //2 minutes
               };

               return httpClient;
            }
            catch (Exception)
            {
               throw;
            }
         }

         /// <summary> Displays exception information to the console. </summary>
         /// <param name="ex">The exception to output</param>
         public static void DisplayException(Exception ex)
         {
            Console.WriteLine("The application terminated with an error.");
            Console.WriteLine(ex.Message);
            while (ex.InnerException != null)
            {
               Console.WriteLine("\t* {0}", ex.InnerException.Message);
               ex = ex.InnerException;
            }
         }
   }
   }
   ```

1. Add an `OAuthMessageHandler` class in its own class file using the code provided below.

   This class ensures that the access token is refreshed each time an operation is performed. Each access token will expire after about an hour. This class implements a <xref:System.Net.Http.DelegatingHandler> that works with the Microsoft Authentication Library (MSAL) authentication context to call the correct `AcquireToken` variation every time an operation is performed so you don't need to explicitly manage token expiration.

   ```csharp
   using Microsoft.Identity.Client;
   using System.Net.Http;
   using System.Net.Http.Headers;
   using System.Security;
   using System.Threading.Tasks;

   namespace EnhancedQuickStart
   {
   /// <summary>
   /// Custom HTTP message handler that uses OAuth authentication through
   /// Microsoft Authentication Library (MSAL).
   /// </summary>
   class OAuthMessageHandler : DelegatingHandler
   {
         private AuthenticationHeaderValue authHeader;

         public OAuthMessageHandler(string serviceUrl, string clientId, string redirectUrl, string username, string password,
               HttpMessageHandler innerHandler)
            : base(innerHandler)
         {

            string apiVersion = "9.2";
            string webApiUrl = $"{serviceUrl}/api/data/v{apiVersion}/";

            //Build Microsoft.Identity.Client (MSAL) OAuth Token Request
            var authBuilder = PublicClientApplicationBuilder.Create(clientId)
                           .WithAuthority(AadAuthorityAudience.AzureAdMultipleOrgs)
                           .WithRedirectUri(redirectUrl)
                           .Build();
            var scope = serviceUrl + "//.default";
            string[] scopes = { scope };

            AuthenticationResult authBuilderResult;
            if (username != string.Empty && password != string.Empty)
            {
               //Make silent Microsoft.Identity.Client (MSAL) OAuth Token Request
               var securePassword = new SecureString();
               foreach (char ch in password) securePassword.AppendChar(ch);
               authBuilderResult = authBuilder.AcquireTokenByUsernamePassword(scopes, username, securePassword)
                           .ExecuteAsync().Result;
            }
            else
            {
               //Popup authentication dialog box to get token
               authBuilderResult = authBuilder.AcquireTokenInteractive(scopes)
                           .ExecuteAsync().Result;
            }

            //Note that an Azure AD access token has finite lifetime, default expiration is 60 minutes.
            authHeader = new AuthenticationHeaderValue("Bearer", authBuilderResult.AccessToken);
         }

         protected override Task<HttpResponseMessage> SendAsync(
                  HttpRequestMessage request, System.Threading.CancellationToken cancellationToken)
         {
            request.Headers.Authorization = authHeader;
            return base.SendAsync(request, cancellationToken);
         }
   }
   }
   ```

## Update Program.cs

Now that you have made the changes to [Enable passing credentials in a connection string](#enable-passing-credentials-in-a-connection-string) and [Add helper code](#add-helper-code), you can update the `Main` method in the `Program.cs` file to only contain the following:

```csharp
using Newtonsoft.Json.Linq;
using System;
using System.Configuration;
using System.Net.Http;

namespace EnhancedQuickStart
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                //Get configuration data from App.config connectionStrings
                string connectionString = ConfigurationManager.ConnectionStrings["Connect"].ConnectionString;

                using (HttpClient client = SampleHelpers.GetHttpClient(connectionString, SampleHelpers.clientId, SampleHelpers.redirectUrl))
                {
                    // Use the WhoAmI function
                    var response = client.GetAsync("WhoAmI").Result;

                    if (response.IsSuccessStatusCode)
                    {
                        //Get the response content and parse it.
                        JObject body = JObject.Parse(response.Content.ReadAsStringAsync().Result);
                        Guid userId = (Guid)body["UserId"];
                        Console.WriteLine("Your UserId is {0}", userId);
                    }
                    else
                    {
                        Console.WriteLine("The request failed with a status of '{0}'",
                                    response.ReasonPhrase);
                    }
                    Console.WriteLine("Press any key to exit.");
                    Console.ReadLine();
                }
            }
            catch (Exception ex)
            {
                SampleHelpers.DisplayException(ex);
                Console.WriteLine("Press any key to exit.");
                Console.ReadLine();
            }
        }
    }
}
```


This is less code and you have added error handling and the means to refresh the access token with every use of the `HttpClient`.

However, you'll see that `JObject` has red squiggly lines under it. If you try to build this project, it will fail.

The [Quick start](quick-start-console-app-csharp.md) used `System.Text.Json`, but this code uses NewtonSoft.

### Install NewtonSoft.Json

1. Right-click the `JObject` with the red squiggly lines under it and choose **Quick Actions and Refactorings...**.
1. Select **Install package 'Newtonsoft.Json'** > **Find and install latest version**.

## Run the program

Press F5 to run the program. Just like the [Quick start](quick-start-console-app-csharp.md) sample, the output should look like this:

```
Your UserId is 969effb0-98ae-478c-b547-53a2968c2e75
Press any key to exit.
```

## Create reusable methods

While we have reduced the total amount of code in the `Program.Main` method, you aren't going to write a program to just call one operation, and it isn't realistic to write so much code just to call a single operation.

This section shows how you can change this:

```csharp
var response = client.GetAsync("WhoAmI").Result;

if (response.IsSuccessStatusCode)
{
  //Get the response content and parse it.
  JObject body = JObject.Parse(response.Content.ReadAsStringAsync().Result);
  Guid userId = (Guid)body["UserId"];
  Console.WriteLine("Your UserId is {0}", userId);
}
else
{
  Console.WriteLine("The request failed with a status of '{0}'",
      response.ReasonPhrase);
}
```

to this:

```csharp
WhoAmIResponse response = WhoAmI(client);
      Console.WriteLine("Your system user ID is: {0}", response.UserId);
```

Before you begin, it would be a good idea to go out to the Web API Reference and review these articles:

- [WhoAmI Function](xref:Microsoft.Dynamics.CRM.WhoAmI)
- [WhoAmIResponse ComplexType](xref:Microsoft.Dynamics.CRM.WhoAmIResponse)

Notice how the [WhoAmI Function](xref:Microsoft.Dynamics.CRM.WhoAmI) returns a [WhoAmIResponse ComplexType](xref:Microsoft.Dynamics.CRM.WhoAmIResponse) and the [WhoAmIResponse ComplexType](xref:Microsoft.Dynamics.CRM.WhoAmIResponse) contains three `GUID` properties: `BusinessUnitId`, `UserId`, and `OrganizationId`;

The code we'll add is simply to model the function into a reusable method that accepts an `HttpClient` as a parameter.

> [!NOTE]
> Exactly how you do this is a matter of personal preference. This design is provided because of it's relative simplicity.

In your Visual Studio project, perform the following steps:

1. Edit the `Program` class to make it a partial class.

   At the top, change this:

   `class Program`

   To this:

   `partial class Program`

1. Create a new class file named `ProgramMethods.cs`

   In `ProgramMethods.cs`, change this:

   `class ProgramMethods`

   To this:

   `partial class Program`

   In this way, the `Program` class in `ProgramMethods.cs` file is just an extension of the original `Program` class in the `Program.cs` file.

1. Add the following using directives to the top of the ProgramMethods.cs file.

   ```csharp
   using Newtonsoft.Json.Linq;
   using System;
   using System.Net.Http;
   ```

1. Add the following method to the `Program` class in the ProgramMethods.cs file.

   ```csharp
   public static WhoAmIResponse WhoAmI(HttpClient client) {
     WhoAmIResponse returnValue = new WhoAmIResponse();
     //Send the WhoAmI request to the Web API using a GET request.
     HttpResponseMessage response = client.GetAsync("WhoAmI",
             HttpCompletionOption.ResponseHeadersRead).Result;
     if (response.IsSuccessStatusCode)
     {
         //Get the response content and parse it.
         JObject body = JObject.Parse(response.Content.ReadAsStringAsync().Result);
         returnValue.BusinessUnitId = (Guid)body["BusinessUnitId"];
         returnValue.UserId = (Guid)body["UserId"];
         returnValue.OrganizationId = (Guid)body["OrganizationId"];
     }
     else
     {
         throw new Exception(string.Format("The WhoAmI request failed with a status of '{0}'",
                 response.ReasonPhrase));
     }
     return returnValue;
   }
   ```

1. Add the following class outside of the `Program` class but within the namespace of the `ProgramMethods.cs` file.

   ```csharp
   public class WhoAmIResponse
   {
       public Guid BusinessUnitId { get; set; }
       public Guid UserId { get; set; }
       public Guid OrganizationId { get; set; }
   }
   ```

1. In the `Program.Main` method in the original Program.cs file:

   Replace this:

   ```csharp
   var response = client.GetAsync("WhoAmI").Result;

   if (response.IsSuccessStatusCode)
   {
     //Get the response content and parse it.
     JObject body = JObject.Parse(response.Content.ReadAsStringAsync().Result);
     Guid userId = (Guid)body["UserId"];
     Console.WriteLine("Your UserId is {0}", userId);
   }
   else
   {
     Console.WriteLine("The request failed with a status of '{0}'",
                 response.ReasonPhrase);
   }
   ```

   With this:

   ```csharp
   WhoAmIResponse response = WhoAmI(client);
   Console.WriteLine("Your system user ID is: {0}", response.UserId);
   ```

1. Press F5 to run the sample and you should get the same results as before.

## Troubleshooting

If you have any trouble running this sample, you can download all the Power Apps samples from the GitHub repository at [https://github.com/Microsoft/PowerApps-Samples](https://github.com/Microsoft/PowerApps-Samples).

> [!IMPORTANT]
> All the samples on the GitHub repo are configured to use a common App.config that is located at PowerApps-Samples:cds\App.config. When you set your connection string you must edit this file. When you do, you can run all the samples without setting your credentials again.

## Create a Template project

Before you leave this article, consider saving your project as a project template. You can then reuse that template for future learning projects and save yourself some time and effort in setting up new projects. To do this, while your project is open in Microsoft Visual Studio, in the **File** menu select **Export template**. Follow the [Export Template Wizard](/visualstudio/ide/how-to-create-project-templates) instructions to create the template.

## Next steps

Use the following resources to learn more:

> [!div class="nextstepaction"]
> [Perform operations using the Web API](perform-operations-web-api.md)
> [!div class="nextstepaction"]
> [Try Web API Data operations Samples (C#)](web-api-samples-csharp.md)
> [!div class="nextstepaction"]
> [Review Web API samples (C#) on GitHub](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/C%23-NETx)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
