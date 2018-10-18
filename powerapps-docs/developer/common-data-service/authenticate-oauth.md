---
title: "Use OAuth with Common Data Service for apps (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to authenticate using OAuth with Common Data Service for Apps" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 09/30/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Use OAuth with Common Data Service for apps

[OAuth 2.0](https://oauth.net/2/) is the industry-standard protocol for authorization. After people provide credentials to authenticate, OAuth determines whether they are authorized to access the resources.

Client applications must support the use of OAuth to access data using the Web API. OAuth enables two-factor authentication (2FA) or certificate-based authentication for server-to-server application scenarios.

OAuth requires an identity provider for authentication. For Common Data Service for Apps the identity provider is Azure Active Directory (AAD). To authenticate with AAD using a Microsoft work or school account, use the Azure Active Directory Authentication Libraries (ADAL).

> [!NOTE]
> This topic will introduce common concepts related to connecting to CDS for Apps using OAuth with the ADAL libraries. This content will focus on how a developer can connect to CDS for Apps but not on the inner workings of OAuth or the ADAL libraries. For complete information related to authentication see the Azure Active Directory documentation. [What is authentication?](/azure/active-directory/develop/authentication-scenarios) is a good place to start.
>
>Samples we provide are pre-configured with appropriate registration values so that you can run them without generating your own app registration. When you publish your own apps, you must use your own registration values.

## App Registration

When you connect using OAuth you must first register an application in your Azure AD tenant. How you should register your app depends on the type of app you want to make.

In all cases, start with basic steps to register an app described in the AAD topic: [Quickstart: Register an app with the Azure Active Directory v1.0 endpoint](/azure/active-directory/develop/quickstart-v1-add-azure-ad-app). For CDS for Apps specific instructions see [Walkthrough: Register an app with Azure Active Directory > Create an application registration](walkthrough-register-app-azure-active-directory.md#create-an-application-registration).

The decisions you will need to make in this step mostly depend on the Application Type choice.

### Types of app registration

When you register an app with Azure AD one of the decisions you must make is the Application type. There are two types of applications you can register:

|Application type|Description|
|--|--|
|Web app /API|**Web client**<br />A type of [client application](/azure/active-directory/develop/developer-glossary#client-application) that executes all code on a web server.<br /><br />**User-agent-based client**<br />A type of [client application](/azure/active-directory/develop/developer-glossary#client-application) that downloads code from a web server and executes within a user-agent (for instance, a web browser), such as a Single Page Application (SPA). 
|
|Native|A type of [client application](/azure/active-directory/develop/developer-glossary#client-application) that is installed natively on a device. |

When you select **Web app /API** you must provide a **Sign-On URL** which is the URL where Azure AD will send the authentication response, including a token if authentication was successful. While you develop an app, this is usually set to `http://localhost/appname:[port]` so you can develop and debug your app locally. When you publish your app, you need to change this value to the published URL of the app.

When you select **Native**, you must provide a Redirect URI. This is a unique identifier to which Azure AD will redirect the user-agent in an OAuth 2.0 request. This is typically a value formatted like so: `//app:<guid>`. 

### Giving access to CDS for Apps

If your app will be a client which allows the authenticated user to perform operations, you must configure the application to have the Access Dynamics 365 as organization users delegated permission.

For specific steps to do this, see [Walkthrough: Register an app with Azure Active Directory > Apply Permissions](walkthrough-register-app-azure-active-directory.md#apply-permissions).

<!-- TODO Verify this -->
If your app will use Server-to-Server (S2S) authentication, this step is not required. That configuration requires a specific system user and the operations will be performed by that user account rather than any user that must be authenticated.

### Enable Implicit Flow

If you are configuring an app for a Single Page Application (SPA) you must edit the Manifest to set the `oauth2AllowImplicitFlow` value to `true`. More information: [Walkthrough: Registering and configuring a SPA application with adal.js](walkthrough-registering-configuring-simplespa-application-adal-js.md)

### Use Client Secrets & Certificates

For server to server scenarios there will not be an interactive user account to authenticate. In these cases, you need to provide some means to confirm that the application is trusted. This is done using client secrets or certificates.

For apps that are registered with the **Web app /API** application type, you can configure secrets. These are set using the **Keys** area under **API Access** in the **Settings** for the app registration. 

For either application type, you can upload a certificate.

More information: [Connect as an app](#connect-as-an-app)

## Use ADAL Libraries to connect

Use one of the Microsoft-supported Azure Active Directory Authentication Libraries (ADAL) client libraries. [Azure Active Directory Authentication Libraries > Microsoft-supported Client Libraries](/azure/active-directory/develop/active-directory-authentication-libraries#microsoft-supported-client-libraries).

These libraries are available for various platforms as shown in the following table:

|Platform|Library|
|--|--|
|.NET Client, Windows Store, UWP, Xamarin |ADAL .NET v3|
|.NET Client, Windows Store, Windows Phone 8.1|ADAL .NET v2|
|JavaScript|ADAL.js|
|iOS, macOS|ADAL|
|Android|ADAL|
|Node.js|ADAL|
|Java|ADAL4J|
|Python|ADAL|

> [!NOTE]
> Currently, all our samples use the .NET Client libraries except for [Use OAuth with Cross-Origin Resource Sharing to connect a Single Page Application](oauth-cross-origin-resource-sharing-connect-single-page-application.md) which uses the JavaScript ADAL.js library.

## ADAL .NET Client library versions

There are two libraries that support .NET clients. The ADAL .NET v3 library is the latest but does not replace the ADAL .NET v2 library.

> [!IMPORTANT]
> If you are using Xrm.Tooling for .NET framework applications, you must use the ADAL .NET v2 library.

One of the significant differences between the .NET Client versions is that the v2 library provides support for passing user credentials. The v3 library requires that user credential information must be captured interactively using a browser pop-up.

If you are not using Xrm.Tooling you may use the ADAL .NET v2 or v3 client libraries with the Web API. For an example using the v3 client library see : [ADAL v3 WhoAmI sample](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/webapi/C%23/ADALV3WhoAmI/ADALV3WhoAmI).

## Use the AccessToken with your requests

The point of using the ADAL libraries is to get a token that you can include with your requests. 
This only requires a few lines of code, and just a few more lines to configure an HttpClient to execute a request.

The following is the minimum amount of code needed to execute a single Web Api request, but it is not the recommended approach:

```csharp
class SampleProgram
{
    private static string serviceUrl = "https://yourorg.crm.dynamics.com"; 
    private static string clientId = "51f81489-12ee-4a9e-aaae-a2591f45987d"; 
    private static string userName = "you@yourorg.onmicrosoft.com";
    private static string password = "yourpassword";

    static void Main(string[] args)
    {

        AuthenticationContext authContext = 
        new AuthenticationContext("https://login.microsoftonline.com/common", false);  
        UserCredential credential = new UserCredential(userName, password);
        AuthenticationResult result = authContext.AcquireToken(serviceUrl, clientId, credential);
        //The access token
        string accessToken = result.AccessToken;

        using (HttpClient client = new HttpClient()) {
        client.BaseAddress = new Uri(serviceUrl);
        client.Timeout = new TimeSpan(0, 2, 0);  //2 minutes  
        client.DefaultRequestHeaders.Add("OData-MaxVersion", "4.0");
        client.DefaultRequestHeaders.Add("OData-Version", "4.0");
        client.DefaultRequestHeaders.Accept.Add(
            new MediaTypeWithQualityHeaderValue("application/json"));
        HttpRequestMessage request = 
            new HttpRequestMessage(HttpMethod.Get, "/api/data/v9.0/WhoAmI");
        //Set the access token
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", accessToken);
        HttpResponseMessage response = client.SendAsync(request).Result;
        if (response.IsSuccessStatusCode)
        {
            //Get the response content and parse it.  
            JObject body = JObject.Parse(response.Content.ReadAsStringAsync().Result);
            Guid userId = (Guid)body["UserId"];
            Console.WriteLine("Your system user ID is: {0}", userId);
        }

    }
}
```

This simple approach does not represent a good pattern to follow because the `AccessToken` will expire in about an hour. ADAL libraries will cache the token for you and will refresh it each time the `AcquireToken` method is called.

The recommended approach is to implement a class derived from <xref:System.Net.Http.DelegatingHandler> which will be passed to the constructor of the <xref:System.Net.Http.HttpClient>. This handler will allow you to override the <xref:System.Net.Http.HttpClient>.<xref:System.Net.Http.HttpClient.SendAsync*> method so that ADAL will call the `AcquireToken` method with each request sent by the http client.

The following is an example of a custom class derived from <xref:System.Net.Http.DelegatingHandler>

```csharp
  /// <summary>  
  ///Custom HTTP message handler that uses OAuth authentication thru ADAL.  
  /// </summary>  
  class OAuthMessageHandler : DelegatingHandler
  {
    private UserCredential _credential;
    private AuthenticationContext _authContext = 
      new AuthenticationContext("https://login.microsoftonline.com/common", false);
    private string _clientId;
    private string _serviceUrl;

    public OAuthMessageHandler(string serviceUrl, string clientId, string userName, string password,
            HttpMessageHandler innerHandler)
        : base(innerHandler)
    {
      _credential = new UserCredential(userName, password);
      _clientId = clientId;
      _serviceUrl = serviceUrl;
    }

    protected override Task<HttpResponseMessage> SendAsync(
             HttpRequestMessage request, System.Threading.CancellationToken cancellationToken)
    {
      try
      {
        request.Headers.Authorization =
        new AuthenticationHeaderValue("Bearer", _authContext.AcquireToken(_serviceUrl, _clientId, _credential).AccessToken);
      }
      catch (Exception ex)
      {
        throw ex;
      }      
      return base.SendAsync(request, cancellationToken);
    }
  }
```

Using this `OAuthMessageHandler` class, the simple program shown above would look like this, with some additional error handling included:

```csharp
class SampleProgram
{
    private static string serviceUrl = "https://yourorg.crm.dynamics.com"; 
    private static string clientId = "51f81489-12ee-4a9e-aaae-a2591f45987d"; 
    private static string userName = "you@yourorg.onmicrosoft.com";
    private static string password = "yourpassword";

    static void Main(string[] args)
    {
       HttpMessageHandler messageHandler;

      try
      {
        messageHandler = new OAuthMessageHandler(serviceUrl, clientId, userName, password,
                         new HttpClientHandler());
        //Create an HTTP client to send a request message to the CRM Web service.  
        using (HttpClient client = new HttpClient(messageHandler))
        {
          //Specify the Web API address of the service and the period of time each request   
          // has to execute.  
          client.BaseAddress = new Uri(serviceUrl);
          client.Timeout = new TimeSpan(0, 2, 0);  //2 minutes
          client.DefaultRequestHeaders.Add("OData-MaxVersion", "4.0");
          client.DefaultRequestHeaders.Add("OData-Version", "4.0");
          client.DefaultRequestHeaders.Accept.Add(
              new MediaTypeWithQualityHeaderValue("application/json"));

          //Send the WhoAmI request to the Web API using a GET request.   
          var response = client.GetAsync("api/data/v9.0/WhoAmI",
                  HttpCompletionOption.ResponseHeadersRead).Result;
          if (response.IsSuccessStatusCode)
          {
            //Get the response content and parse it.  
            JObject body = JObject.Parse(response.Content.ReadAsStringAsync().Result);
            Guid userId = (Guid)body["UserId"];
            Console.WriteLine("Your system user ID is: {0}", userId);
          }
          else
          {
            throw new Exception(response.ReasonPhrase);
          }
        }
      }
      catch (Exception ex)
      {
        DisplayException(ex);
      }
    }

    /// <summary> Displays exception information to the console. </summary>  
    /// <param name="ex">The exception to output</param>  
    private static void DisplayException(Exception ex)
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
```

Even though this example uses <xref:System.Net.Http.HttpClient>.<xref:System.Net.Http.HttpClient.GetAsync*> rather than the overridden <xref:System.Net.Http.HttpClient.SendAsync*>, it will apply for any of the <xref:System.Net.Http.HttpClient> methods that send a request.


## Connect as an app

<!-- TODO provide some examples -->

### See also

[Authentication with Common Data Service for Apps web services](authentication.md)<br />
[Authentication with .NET Framework applications](authenticate-dot-net-framework.md)