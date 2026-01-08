---
title: "Use OAuth authentication with Microsoft Dataverse (Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to authenticate applications with Microsoft Dataverse using OAuth." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: has-adal-ref
ms.date: 01/07/2026
ms.reviewer: pehecke
ms.topic: how-to
author: ritesp # GitHub ID
ms.subservice: dataverse-developer
ms.author: ritesp # MSFT alias of Microsoft employees only
search.audienceType:
  - developer
contributors:
 - JimDaly
---

# Use OAuth authentication with Microsoft Dataverse

[OAuth 2.0](https://oauth.net/2/) is the industry-standard protocol for authorization. After application users provide credentials to authenticate, OAuth determines whether they're authorized to access the resources.

Client applications must support the use of OAuth to access data using the Web API. OAuth enables two-factor authentication (2FA) or certificate-based authentication for server-to-server application scenarios.

OAuth requires an identity provider for authentication. For Dataverse, the identity provider is Microsoft Entra ID. To authenticate using a Microsoft work or school account, use the [Microsoft Authentication Library](/azure/active-directory/develop/msal-overview#languages-and-frameworks) (MSAL).

> [!NOTE]
> This topic will introduce common concepts related to connecting to Dataverse using OAuth with authentication libraries. This content will focus on how a developer can connect to Dataverse but not on the inner workings of OAuth or the libraries. For complete information related to authentication see the Microsoft Entra ID documentation. [What is authentication?](/azure/active-directory/develop/authentication-scenarios) is a good place to start.
>
> Samples we provide are pre-configured with appropriate registration values so that you can run them without generating your own app registration. When you publish your own apps, you must use your own registration values.

## App Registration

When you connect using OAuth, you must first register an application in your Microsoft Entra ID tenant. How you should register your app depends on the type of app you want to make.

In all cases, start with basic steps to register an app described in the article: [Quickstart: Register an application with the Microsoft identity platform](/azure/active-directory/develop/quickstart-register-app). For Dataverse specific instructions see [Walkthrough: Register an app with Microsoft Entra ID](walkthrough-register-app-azure-active-directory.md).

The decisions you need to make in this step mostly depend on the Application Type choice (see below).

### Types of app registration

When you register an app with Microsoft Entra ID one of the decisions, you must make is the application type. There are two types of applications you can register:

| Application type | Description|
|------------------|------------|
| Web app /API | **Web client**<br />A type of [client application](/azure/active-directory/develop/developer-glossary#client-application) that executes all code on a web server.<br /><br />**User-agent-based client**<br />A type of [client application](/azure/active-directory/develop/developer-glossary#client-application) that downloads code from a web server and executes within a user-agent (for instance, a web browser), such as a Single Page Application (SPA). |
|Native|A type of [client application](/azure/active-directory/develop/developer-glossary#client-application) that is installed natively on a device. |

When you select **Web app /API** you must provide a **Sign-On URL** which is the URL where Microsoft Entra ID sends the authentication response, including a token if authentication was successful. While you develop an app, this URL is usually set to `https://localhost/appname:[port]` so you can develop and debug your app locally. When you publish your app, you need to change this value to the published URL of the app.

When you select **Native**, you must provide a Redirect URI. This URL is a unique identifier to which Microsoft Entra ID will redirect the user-agent in an OAuth 2.0 request. This URL is typically a value formatted like so: `app://<guid>`.

### Giving access to Dataverse

If your app is a client that allows the authenticated user to perform operations, you must configure the application to have the Access Dynamics 365 as organization users delegated permission.

For specific steps to set permissions, see [Register an app with Microsoft Entra ID](walkthrough-register-app-azure-active-directory.md).

If your app uses Server-to-Server (S2S) authentication, this step isn't required. That configuration requires a specific system user and the operations are performed by that user account rather than any user that must be authenticated.

### Use Client Secrets & Certificates

For server-to-server scenarios there won't be an interactive user account to authenticate. In these cases, you need to provide some means to confirm that the application is trusted. This is done using client secrets or certificates.

For apps that are registered with the **Web app /API** application type, you can configure secrets. These are set using the **Keys** area under **API Access** in the **Settings** for the app registration.

For either application type, you can upload a certificate.

More information: [Connect as an app](#connect-as-an-app)

## Use authentication libraries to connect

Use one of the Microsoft-supported Microsoft Entra ID authentication client libraries to connect to Dataverse such as [Microsoft Authentication Library (MSAL)](/azure/active-directory/develop/reference-v2-libraries). That library is available for various platforms as described in the provided links.

> [!NOTE]
> Azure Active Directory Authentication Library (ADAL) is no longer actively receiving updates and is scheduled to be supported only until June, 2022. MSAL is the recommended authentication library to use for projects.

For a code sample that demonstrates use of MSAL libraries for authentication with Dataverse see [QuickStart sample](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp/QuickStart).

### .NET client libraries

Dataverse supports application authentication with the Web API endpoint using the OAuth 2.0 protocol. For your custom .NET applications, use MSAL for application authentication with the Web API endpoint.

Dataverse SDK for .NET includes client classes [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) and [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) to handle authentication. The `CrmServiceClient` class currently uses ADAL for authentication while `ServiceClient` uses MSAL. Writing your application code to use these clients removes the need to manage authentication directly. Both clients work with the SDK and Web API endpoints.

## Use the AccessToken with your requests

The point of using the authentication libraries is to get an access token that you can include with your requests. Getting the token only requires a few lines of code, and just a few more lines to configure an [HttpClient](xref:System.Net.Http.HttpClient) to execute a request.

> [!IMPORTANT]
> As demonstrated in the sample code of this article, use a "\<environment-url>/user_impersonation" scope for a public client. For a confidential client, use a scope of "\<environment-url>/.default".

### Simple example

The following is the minimum amount of code needed to execute a single Web API request, but it isn't the recommended approach. Note that this code uses the MSAL library and is taken from the [QuickStart](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp/QuickStart) sample.

```csharp
string resource = "https://contoso.api.crm.dynamics.com";
var clientId = "51f81489-12ee-4a9e-aaae-a2591f45987d";
var redirectUri = "http://localhost"; // Loopback for the interactive login.

// MSAL authentication
var authBuilder = PublicClientApplicationBuilder.Create(clientId)
    .WithAuthority(AadAuthorityAudience.AzureAdMultipleOrgs)
    .WithRedirectUri(redirectUri)
    .Build();
var scope = resource + "/user_impersonation";
string[] scopes = { scope };

AuthenticationResult token =
    authBuilder.AcquireTokenInteractive(scopes).ExecuteAsync().Result;

// Set up the HTTP client
var client = new HttpClient
{
    BaseAddress = new Uri(resource + "/api/data/v9.2/"),
    Timeout = new TimeSpan(0, 2, 0)  // Standard two minute timeout.
};

HttpRequestHeaders headers = client.DefaultRequestHeaders;
headers.Authorization = new AuthenticationHeaderValue("Bearer", token.AccessToken);
headers.Add("OData-MaxVersion", "4.0");
headers.Add("OData-Version", "4.0");
headers.Accept.Add(
    new MediaTypeWithQualityHeaderValue("application/json"));

// Web API call
var response = client.GetAsync("WhoAmI").Result;
```

This simple approach does not represent a good pattern to follow because the `token` will expire in about an hour. MSAL libraries will cache the token for you and will refresh it each time the `AcquireTokenInteractive` method is called. However in this simple example, the token is only acquired once.

### Example demonstrating a delegating message handler

The recommended approach is to implement a class derived from <xref:System.Net.Http.DelegatingHandler> which will be passed to the constructor of the <xref:System.Net.Http.HttpClient>. This handler will allow you to override the <xref:System.Net.Http.HttpClient>.<xref:System.Net.Http.HttpClient.SendAsync*> method so that the access token will be refreshed by the `AcquireToken*` method calls with each request sent by the Http client.

The following is an example of a custom class derived from <xref:System.Net.Http.DelegatingHandler>. This code is taken from the [Enhanced QuickStart](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp/EnhancedQuickStart) sample which uses the MSAL authentication library.

```csharp
class OAuthMessageHandler : DelegatingHandler
{
    private AuthenticationHeaderValue authHeader;
    public OAuthMessageHandler(string serviceUrl, string clientId, string redirectUrl, string username, string password,
            HttpMessageHandler innerHandler)
        : base(innerHandler)
    {
        string apiVersion = "9.2";
        string webApiUrl = $"{serviceUrl}/api/data/v{apiVersion}/";
        var authBuilder = PublicClientApplicationBuilder.Create(clientId)
                        .WithAuthority(AadAuthorityAudience.AzureAdMultipleOrgs)
                        .WithRedirectUri(redirectUrl)
                        .Build();
        var scope = serviceUrl + "/user_impersonation";
        string[] scopes = { scope };
        // First try to get an authentication token from the cache using a hint.
        AuthenticationResult authBuilderResult=null;
        try
        {
            authBuilderResult = authBuilder.AcquireTokenSilent(scopes, username)
               .ExecuteAsync().Result;
        }
        catch (Exception ex)
        {
            System.Diagnostics.Debug.WriteLine(
                $"Error acquiring auth token from cache:{System.Environment.NewLine}{ex}");
            // Token cache request failed, so request a new token.
            try
            {
                if (username != string.Empty && password != string.Empty)
                {
                    // Request a token based on username/password credentials.
                    authBuilderResult = authBuilder.AcquireTokenByUsernamePassword(scopes, username, password)
                                .ExecuteAsync().Result;
                }
                else
                {
                    // Prompt the user for credentials and get the token.
                    authBuilderResult = authBuilder.AcquireTokenInteractive(scopes)
                                .ExecuteAsync().Result;
                }
            }
            catch (Exception msalex)
            {
                System.Diagnostics.Debug.WriteLine(
                    $"Error acquiring auth token with user credentials:{System.Environment.NewLine}{msalex}");
                throw;
            }
        }
        //Note that an Microsoft Entra ID access token has finite lifetime, default expiration is 60 minutes.
        authHeader = new AuthenticationHeaderValue("Bearer", authBuilderResult.AccessToken);
    }

    protected override Task<HttpResponseMessage> SendAsync(
              HttpRequestMessage request, System.Threading.CancellationToken cancellationToken)
    {
        request.Headers.Authorization = authHeader;
        return base.SendAsync(request, cancellationToken);
    }
}
```

Using this `OAuthMessageHandler` class, the simple `Main` method would look like this.

```csharp
class Program
{
    static void Main(string[] args)
    {
        try
        {
            //Get configuration data from App.config connectionStrings
            string connectionString = ConfigurationManager.ConnectionStrings["Connect"].ConnectionString;

            using (HttpClient client = SampleHelpers.GetHttpClient(connectionString, SampleHelpers.clientId,
                SampleHelpers.redirectUrl))
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
```

Read the following important information about using a connection string or username/password authentication in application code.
[!INCLUDE [cc-connection-string](includes/cc-connection-string.md)]

The configuration string values have been moved into an App.config file connection string, and the Http client is configured in the `GetHttpClient` method.

```csharp
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
```

See the [Enhanced QuickStart](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp/EnhancedQuickStart) sample for the complete code.

Even though this example uses <xref:System.Net.Http.HttpClient>.<xref:System.Net.Http.HttpClient.GetAsync*> rather than the overridden <xref:System.Net.Http.HttpClient.SendAsync*>, it will apply for any of the <xref:System.Net.Http.HttpClient> methods that send a request.

## Connect as an app

Some apps you will create are not intended to be run interactively by a user. For example, you may want to make a web client application that can perform operations on Dataverse data, or a console application that performs a scheduled task of some kind.

While you could achieve these scenarios using credentials for an ordinary user, that user account would need to use a paid license. This isn't the recommended approach.

In these cases you can create a special application user which is bound to an Microsoft Entra ID registered application and use either a key secret configured for the app or upload a [X.509](https://www.itu.int/rec/T-REC-X.509/en) certificate. Another benefit of this approach is that it doesn't consume a paid license.

### Requirements to connect as an app

To connect as an app you will need:

- A registered app
- A Dataverse user bound to the registered app
- Connect using either the application secret or a certificate thumbprint

#### Register your app

When registering an app you follow many of the same steps described in [Walkthrough: Register an app with Microsoft Entra ID](walkthrough-register-app-azure-active-directory.md), with the following exceptions:

- You do not need to grant the **Access Dynamics 365 as organization users** permission.

  This application will be bound to a specific user account.

- You must configure a secret for the app registration OR upload a public key certificate.

You can create or view credentials in your app registration under **Manage** > **Certificates & secrets**.

To add a certificate (public key):

1. In the **Certificates** tab, select **Upload certificate**.
2. Select the file you'd like to upload. It must be one of the following file types: .cer, .pem, .crt.
3. Provide a description.
4. Select **Add**.

To add an client secret (application password):

1. In the **Client secrets** tab, add a description for your client secret.
2. Select an expiration time period.
3. Select **Add**.

> [!IMPORTANT]
> After you save the configuration changes, a secret value is displayed. Be sure to copy the secret value for use in your client application code, as that value is not accessible once you leave the page.

More information: [Add credentials](/entra/identity-platform/quickstart-register-app?tabs=certificate#add-credentials)

#### Dataverse user account bound to the registered app

The first thing you must do is create a custom security role that will define what access and privileges this account will have within the Dataverse organization. More information: [Create or configure a custom security role](/power-platform/admin/database-security#create-or-configure-a-custom-security-role)

After you have created the custom security role, you must create the user account which will use it.

<!-- Almost exactly the same intructions below can be found in powerapps-docs\developer\data-platform\use-multi-tenant-server-server-authentication.md -->

#### Manually create a Dataverse application user

The procedure to create an application user can be found in the Administer Power Platform article: [Create an application user](/power-platform/admin/manage-application-users#create-an-application-user).

After creating an application user, associate the application user with the custom security role you created.

#### Connect using the application secret

If you are connecting using a client secret and using the <xref:Microsoft.Xrm.Tooling.Connector>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> you can use code like the following:

```csharp
string SecretID = "00000000-0000-0000-0000-000000000000";
string AppID = "00001111-aaaa-2222-bbbb-3333cccc4444";
string InstanceUri = "https://yourorg.crm.dynamics.com";

string ConnectionStr = $@"AuthType=ClientSecret;
                        SkipDiscovery=true;url={InstanceUri};
                        Secret={SecretID};
                        ClientId={AppID};
                        RequireNewInstance=true";
using (ServiceClient svc = new ServiceClient(ConnectionStr))
{
    if (svc.IsReady)
    {
    //your code goes here
    }

}
```

#### Connect using a certificate thumbprint

If you are connecting using a certificate and using the <xref:Microsoft.Xrm.Tooling.Connector>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> you can use code like the following:

```csharp
string CertThumbPrintId = "DC6C689022C905EA5F812B51F1574ED10F256FF6";
string AppID = "00001111-aaaa-2222-bbbb-3333cccc4444";
string InstanceUri = "https://yourorg.crm.dynamics.com";

string ConnectionStr = $@"AuthType=Certificate;
                        SkipDiscovery=true;url={InstanceUri};
                        thumbprint={CertThumbPrintId};
                        ClientId={AppID};
                        RequireNewInstance=true";
using (ServiceClient svc = new ServiceClient(ConnectionStr))
{
    if (svc.IsReady)
    {
    //your code goes here
    }

}
```

### See also

[Authentication with Microsoft Dataverse web services](authentication.md)<br />
[Authenticating .NET Framework applications](authenticate-dot-net-framework.md)<br/>
[Overview of the Microsoft Authentication Library](/azure/active-directory/develop/msal-overview)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
