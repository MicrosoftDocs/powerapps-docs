---
title: "Enhanced quick start (Microsoft Dataverse)| Microsoft Docs"
description: "Create a new project in Visual Studio to build a console application that uses Microsoft Dataverse Web API"
ms.custom: intro-internal
ms.date: 02/02/2019
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 08377156-32c7-492a-8e66-50a47a330dc6
caps.latest.revision: 14
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Enhanced quick start

This topic demonstrates how to re-factor the code in [Quick start](quick-start-console-app-csharp.md) topic by adding re-usable <xref:System.Net.Http.HttpClient> and error handling methods. Complete the steps in the [Quick start](quick-start-console-app-csharp.md) topic to create a new Visual Studio project before you begin this topic.

## Enable passing credentials in a connection string

Putting user credentials inside your code the way that the [Quick start](quick-start-console-app-csharp.md) example did is not a good practice. 

How you capture user credentials depends on the type of client you are making. For this console application we will set the credentials within the `App.config` because it is a convenient way to move the credentials out of code. It is also the method used in the [Web API Data operations Samples (C#)](web-api-samples-csharp.md), so if you understand this method, you can easily see how the various samples work.

Enabling this requires three steps:

1. [Add Reference to System.Configuration to the Visual Studio project](#add-reference-to-systemconfiguration-to-the-visual-studio-project)
1. [Edit the application configuration file](#edit-the-application-configuration-file)
1. [Add using directive to Program.cs](#add-using-directive-to-programcs)


### Add Reference to System.Configuration to the Visual Studio project

1. In **Solution Explorer**, right click **References** and select **Add Reference...** .
1. In the **Reference Manager** dialog search for `System.Configuration` and select the checkbox to add this reference to your project.
1. Click **OK** to close the **Reference Manager** dialog.
  
### Edit the application configuration file

In **Solution Explorer**, open the **App.config** file. It should look something like this:

```xml
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
    <startup> 
        <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.6.2" />
    </startup>
</configuration>
```

Edit the `<configuration>` element to add a the `connectionStrings` node as shown below:

```xml
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
    <startup> 
        <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.6.2" />
    </startup>
  <connectionStrings>
    <!--Online using Microsoft 365-->
    <add name="Connect"
         connectionString="Url=https://yourorg.api.crm.dynamics.com;Username=yourname@yourorg.onmicrosoft.com;Password=mypassword;" />
  </connectionStrings>
</configuration>
```

This creates a connection string that can be referenced by name, in this case `Connect`, so that you can define more than one connection if you wish.

Edit the connection string `Url`, `Username` and `Password` values in the `connectionString` to match what you need to connect to your Microsoft Dataverse environment.

### Add using directive to Program.cs

At the top of your Program.cs file, add this using directive:

```csharp
using System.Configuration;
```

## Add helper code

In the [Quick start](quick-start-console-app-csharp.md) example, all the code is within the `program.cs` file. We are going to move the code that deals with connecting and creating an <xref:System.Net.Http.HttpClient> into a separate file of helper methods. 

These helpers are also used in the [SampleHelper.cs](https://github.com/Microsoft/PowerApps-Samples/blob/master/cds/webapi/C%23/SampleHelpers.cs) used by the [Web API Data operations Samples (C#)](web-api-samples-csharp.md). If you understand these helpers, you will understand how they are used in the samples.

1. In **Solution Explorer**, right click your project and select **Add** > **Class...** (or press `Shift`+`Alt`+`C`) to open the **Add New Item** dialog.
1. Specify a name for your class. To follow the pattern used by the [Web API Data operations Samples (C#)](web-api-samples-csharp.md), call it `SampleHelpers.cs`. 

    > [!NOTE]
    > The name of the class will determine how you will reference these helper properties and methods within your `Program.cs`. The remaining instructions will expect you named it `SampleHelpers`, so remember if you named it something else.

1. Add the following `using` directives:

    ```csharp
    using Microsoft.IdentityModel.Clients.ActiveDirectory;
    using System;
    using System.Linq;
    using System.Net.Http;
    using System.Net.Http.Headers;
    using System.Threading.Tasks;
    ```

1. Add the following properties and methods to your `SampleHelper` class:

    ```csharp
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
    /// <param name="version">The version of Web API to use. Defaults to version 9.1 </param>
    /// <returns>An HttpClient you can use to perform authenticated operations with the Web API</returns>
    public static HttpClient GetHttpClient(string connectionString, string clientId, string redirectUrl, string version = "v9.1")
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
    ```

1. Add the `OAuthMessageHandler` class within the namespace of your `SampleHelpers.cs` file.

    > [!NOTE]
    > Do not add this within the `SampleHelpers` class itself.

    This class ensures that the access token is refreshed each time an operation is performed. Each access token will expire after about an hour. This class implements a <xref:System.Net.Http.DelegatingHandler> that will work with the Azure Active Directory Authentication Library (ADAL) authentication context to call the `AcquireToken` method every time an operation is performed so you don't need to explicitly manage token expiration.

    ```csharp
    /// <summary>
    ///Custom HTTP message handler that uses OAuth authentication through ADAL.
    /// </summary>
    class OAuthMessageHandler : DelegatingHandler
    {
      private AuthenticationHeaderValue authHeader;

      public OAuthMessageHandler(string serviceUrl, string clientId, string redirectUrl, string username, string password,
              HttpMessageHandler innerHandler)
          : base(innerHandler)
      {
        // Obtain the Azure Active Directory Authentication Library (ADAL) authentication context.
        AuthenticationParameters ap = AuthenticationParameters.CreateFromResourceUrlAsync(
                new Uri(serviceUrl + "/api/data/")).Result;
        AuthenticationContext authContext = new AuthenticationContext(ap.Authority, false);
        //Note that an Azure AD access token has finite lifetime, default expiration is 60 minutes.
        AuthenticationResult authResult;
        if (username != string.Empty && password != string.Empty)
        {

          UserCredential cred = new UserCredential(username, password);
          authResult = authContext.AcquireToken(serviceUrl, clientId, cred);
        }
        else
        {
          authResult = authContext.AcquireToken(serviceUrl, clientId, new Uri(redirectUrl), PromptBehavior.Auto);
        }

        authHeader = new AuthenticationHeaderValue("Bearer", authResult.AccessToken);
      }

      protected override Task<HttpResponseMessage> SendAsync(
                HttpRequestMessage request, System.Threading.CancellationToken cancellationToken)
      {
        request.Headers.Authorization = authHeader;
        return base.SendAsync(request, cancellationToken);
      }
    }
    ```

## Update Program.cs

Now that you have made the changes to [Enable passing credentials in a connection string](#enable-passing-credentials-in-a-connection-string) and [Add helper code](#add-helper-code), you can update the `Main` method in your `Program.cs` to only contain the following:

```csharp
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
```

This is less code and you have added error handling and the means to refresh the access token with every use of the `HttpClient`.

Press F5 to run the program. Just like the [Quick start](quick-start-console-app-csharp.md) sample, the output should look like this:

```
Your UserId is 969effb0-98ae-478c-b547-53a2968c2e75
Press any key to exit.
```

## Create re-usable methods

While we have reduced the total amount of code in the `Program.cs` `main` method, you aren't going to write a program to just call one operation, and it isn't realistic to write so much code just to call a single operation.

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

Before you begin, it would be a good idea to go out to the Web API Reference and review these topics:
- <xref href="Microsoft.Dynamics.CRM.WhoAmI?text=WhoAmI Function" /> 
- <xref href="Microsoft.Dynamics.CRM.WhoAmIResponse?text=WhoAmIResponse ComplexType" />

Notice how the <xref href="Microsoft.Dynamics.CRM.WhoAmI?text=WhoAmI Function" /> returns a <xref href="Microsoft.Dynamics.CRM.WhoAmIResponse?text=WhoAmIResponse ComplexType" /> and the <xref href="Microsoft.Dynamics.CRM.WhoAmIResponse?text=WhoAmIResponse ComplexType" /> contains three `GUID` properties: `BusinessUnitId`, `UserId`, and `OrganizationId`;

The code we will add is simply to model these into a re-usable method that accepts an `HttpClient` as a parameter.

> [!NOTE]
> Exactly how you do this is a matter of personal preference. This design is provided because of it's relative simplicity.

In your Visual Studio project perform the following steps:

1. Edit the `Program` class to make it a partial class.

    At the top, change this:

    `class Program`

    To this:

    `partial class Program`

1. Create a new class named `ProgramMethods.cs`

    In `ProgramMethods.cs`, change this:

    `class ProgramMethods`

    To this:

    `partial class Program`

    In this way the `Program` class in `ProgramMethods.cs` file is just an extension of the original `Program` class in the `Program.cs` file. 

1. Add the following using directives to the top of the `ProgramMethods.cs` file.

    ```csharp
    using Newtonsoft.Json.Linq;
    using System;
    using System.Net.Http;
    ```

1. Add the following method to the `Program` class in the `ProgramMethods.cs` file.

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

1. In the `Program` `main` method in the original `Program.cs` file:

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

Before you leave this topic, consider saving your project as a project template. You can then reuse that template for future learning projects and save yourself some time and effort in setting up new projects. To do this, while your project is open in Microsoft Visual Studio, in the **File** menu select **Export template**. Follow the [Export Template Wizard](/visualstudio/ide/how-to-create-project-templates) instructions to create the template.  
  
## Next steps

Use the following resources to learn more:

> [!div class="nextstepaction"]
> [Perform operations using the Web API](perform-operations-web-api.md)<br /><br />
> [Try Web API Data operations Samples (C#)](web-api-samples-csharp.md)<br /><br />
> [Review Web API samples (C#) on GitHub](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/webapi/C%23)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]