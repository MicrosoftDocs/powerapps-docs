---
title: "Global Discovery Service Sample (C#) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to access the global Discovery Service using the OData V4 RESTful API and the Dataverse.Client.ServiceClient" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 12/04/2024
author: ImadYanni
ms.author: iyanni
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Global Discovery Service (C#)

This Visual Studio solution contains two .NET 6.0 projects that demonstrate how to use the Global Discovery Service.

- `REST` project shows using the OData endpoint
- `ServiceClient` project shows using <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.DiscoverOnlineOrganizationsAsync%2A?text=Dataverse.Client.ServiceClient.DiscoverOnlineOrganizationsAsync Method>

## How to run this sample

The sample source code is available on Github at [PowerApps-Samples/cds/DiscoveryService/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/DiscoveryService).

To run the sample:

1. Download or clone the sample so that you have a local copy.
1. Open the solution file in Visual Studio.
1. Select which project will be the startup project, either `REST` or `ServiceClient`.
1. In Program.cs, edit the `Main` method to enter your user credentials:

   ```csharp
      string username = "yourUserName@yourOrgName.onmicrosoft.com";
      string password = "yourPassword";
   ```

1. Press F5 to build and run the sample.

Read the following important information about using username/password authentication in application code.
[!INCLUDE [cc-connection-string](includes/cc-connection-string.md)]

## What this sample does

Both the `REST` and `ServiceClient` samples do the same things:

1. Retrieve the list of environments available for your credentials.
1. List the environments so you can select one.
1. Execute a `WhoAmI` message to return the `SystemUser.UserId` value for your account in the selected environment.

## How this sample works

### REST

The `REST` project uses the MSAL libraries with an [HttpClient](/dotnet/api/system.net.http.httpclient) to use the Global Discovery OData endpoint without the use of any additional assemblies.

### ServiceClient

The `ServiceClient` project uses the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.DiscoverOnlineOrganizationsAsync%2A?text=Dataverse.Client.ServiceClient.DiscoverOnlineOrganizationsAsync Method> to use the Global Discovery OData endpoint.

### Demonstrates

Both projects use the same `Cloud` enum defined in Cloud.cs to represent the different clouds that may be used with the Global Discovery Service.

```csharp
using System.ComponentModel;

namespace PowerApps.Samples
{
    /// <summary>
    /// An enum for the known Clouds
    /// </summary>
    public enum Cloud
    {
        [Description("https://globaldisco.crm.dynamics.com")]
        Commercial,
        [Description("https://globaldisco.crm9.dynamics.com")]
        GCC,
        [Description("https://globaldisco.crm.microsoftdynamics.us")]
        USG,
        [Description("https://globaldisco.crm.appsplatform.us")]
        DOD,
        [Description("https://globaldisco.crm.dynamics.cn")]
        CHINA
    }
}
```

#### REST Project

The REST Project uses this `Instance` class in Instance.cs to deserialize the JSON returned from the Global Discovery service:

```csharp
namespace PowerApps.Samples
{
    /// <summary>
    /// Environment instance returned from the Discovery service.
    /// </summary>
    class Instance
    {
        public string? ApiUrl { get; set; }
        public Guid? DatacenterId { get; set; }
        public string? DatacenterName { get; set; }
        public string? EnvironmentId { get; set; }
        public string? FriendlyName { get; set; }
        public string? Id { get; set; }
        public bool IsUserSysAdmin { get; set; }
        public DateTime? LastUpdated { get; set; }
        public int OrganizationType { get; set; }
        public string? Purpose { get; set; }
        public string? Region { get; set; }
        public string? SchemaType { get; set; }
        public int? State { get; set; }
        public int? StatusMessage { get; set; }
        public string? TenantId { get; set; }
        public string? TrialExpirationDate { get; set; }
        public string? UniqueName { get; set; }
        public string? UrlName { get; set; }
        public string? Version { get; set; }
        public string? Url { get; set; }
    }
}
```

The `REST` Program.cs file contains the following:

```csharp
using Microsoft.Identity.Client;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.ComponentModel;
using System.Net;
using System.Net.Http.Headers;
using System.Security;

namespace PowerApps.Samples
{
    class Program
    {
        //These sample application registration values are available for all online instances.
        static readonly string clientId = "51f81489-12ee-4a9e-aaae-a2591f45987d";
        static readonly string redirectUrl = "http://localhost";

        //Establishes the MSAL app to manage caching access tokens
        private static IPublicClientApplication app = PublicClientApplicationBuilder.Create(clientId)
            .WithRedirectUri(redirectUrl)
            .WithAuthority("https://login.microsoftonline.com/organizations")
            .Build();

        static async Task Main()
        {
            string username = "yourUserName@yourOrgName.onmicrosoft.com";
            string password = "yourPassword";

            //Set the Cloud if you want to search other than Commercial.
            Cloud cloud = Cloud.Commercial;

            List<Instance> instances = await GetInstances(username, password, cloud);

            if (instances.Count.Equals(0))
            {
                Console.WriteLine("No valid environments returned for these credentials.");
                return;
            }

            Console.WriteLine("Type the number of the environments you want to use and press Enter.");

            int number = 0;

            //Display instances so they can be selected
            foreach (Instance instance in instances)
            {
                number++;

                //Get the Organization Service URL
                string apiUrl = instance.ApiUrl;
                string friendlyName = instance.FriendlyName;

                Console.WriteLine($"{number} Name: {instance.FriendlyName} URL: {apiUrl}");
            }

            string typedValue = string.Empty;

            try
            {
                //Capture the user's choice
                typedValue = Console.ReadLine();

                int selected = int.Parse(typedValue);

                if (selected <= number)
                {

                    Instance selectedInstance = instances[selected - 1];
                    Console.WriteLine($"You selected '{selectedInstance.FriendlyName}'");

                    //Use the selected instance to get the UserId
                    await ShowUserId(selectedInstance, username, password);

                }
                else
                {
                    throw new ArgumentOutOfRangeException("The selected value is not valid.");
                }
            }
            catch (ArgumentOutOfRangeException aex)
            {
                Console.WriteLine(aex.Message);
            }
            catch (Exception)
            {
                Console.WriteLine("Unable to process value: {0}", typedValue);
            }
        }


        /// <summary>
        /// Gets the instance data for the specified user and cloud.
        /// </summary>
        /// <param name="username">The user's username</param>
        /// <param name="password">The user's password</param>
        /// <param name="cloud">The Cloud enum value that corresponds to the region.</param>
        /// <returns>List of all the instances</returns>
        /// <exception cref="Exception"></exception>
        static async Task<List<Instance>> GetInstances(string username, string password, Cloud cloud)
        {
            try
            {
                //Get the Cloud URL from the Description Attribute applied for the Cloud enum member
                //i.e. Commercial is "https://globaldisco.crm.dynamics.com"
                var type = typeof(Cloud);
                var memInfo = type.GetMember(cloud.ToString());
                var attributes = memInfo[0].GetCustomAttributes(typeof(DescriptionAttribute), false);
                string baseUrl = ((DescriptionAttribute)attributes[0]).Description;

                HttpClient client = new();
                string token = await GetToken(baseUrl, username, password);
                client.DefaultRequestHeaders.Authorization =
                    new AuthenticationHeaderValue(scheme: "Bearer", parameter: token);
                client.Timeout = new TimeSpan(0, 2, 0);
                client.BaseAddress = new Uri(baseUrl);

                HttpResponseMessage response = await client
                    .GetAsync("/api/discovery/v2.0/Instances", HttpCompletionOption.ResponseHeadersRead);

                if (response.IsSuccessStatusCode)
                {
                    //Get the response content and parse it.
                    string result = await response.Content.ReadAsStringAsync();
                    JObject body = JObject.Parse(result);
                    JArray values = (JArray)body.GetValue("value");

                    if (!values.HasValues)
                    {
                        return new List<Instance>();
                    }

                    return JsonConvert.DeserializeObject<List<Instance>>(values.ToString());
                }
                else
                {
                    throw new Exception(response.ReasonPhrase);
                }
            }
            catch (Exception)
            {

                throw;
            }
        }

        /// <summary>
        /// Gets an access token using MSAL app.
        /// </summary>
        /// <param name="baseUrl">The Resource to authenticate to</param>
        /// <param name="username">The user's username</param>
        /// <param name="password">The user's password</param>
        /// <returns>An AccessToken</returns>
        /// <exception cref="Exception"></exception>
        internal static async Task<string> GetToken(string baseUrl, string username, string password)
        {
            try
            {
                List<string> scopes = new() { $"{baseUrl}//user_impersonation" };
                var accounts = await app.GetAccountsAsync();

                AuthenticationResult? result;
                if (accounts.Any())
                {
                    result = await app.AcquireTokenSilent(scopes, accounts.FirstOrDefault())
                                      .ExecuteAsync();
                }
                else
                {
                    try
                    {
                        SecureString securePassword = new NetworkCredential("", password).SecurePassword;

                        // Flow not recommended for production
                        result = await app.AcquireTokenByUsernamePassword(scopes.ToArray(), username, securePassword)
                            .ExecuteAsync();
                    }
                    catch (MsalUiRequiredException)
                    {

                        // When MFA is required
                        result = await app.AcquireTokenInteractive(scopes)
                                    .ExecuteAsync();

                    }
                    catch (Exception)
                    {
                        throw;
                    }
                }

                if (result != null && !string.IsNullOrEmpty(result.AccessToken))
                {
                    return result.AccessToken;
                }
                else
                {
                    throw new Exception("Failed to get accesstoken.");
                }
            }
            catch (Exception)
            {

                throw;
            }
        }

        /// <summary>
        /// Shows the user's UserId for selected instance.
        /// </summary>
        /// <param name="instance">A selected instance</param>
        /// <param name="username">The user's username</param>
        /// <param name="password">The user's password</param>
        /// <returns></returns>
        private static async Task ShowUserId(Instance instance, string username, string password)
        {
            try
            {
                HttpClient client = new();
                client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", await GetToken(instance.ApiUrl, username, password));
                client.Timeout = new TimeSpan(0, 2, 0);
                client.BaseAddress = new Uri(instance.ApiUrl);

                HttpResponseMessage response = await client.GetAsync("/api/data/v9.2/WhoAmI", HttpCompletionOption.ResponseHeadersRead);

                if (response.IsSuccessStatusCode)
                {
                    JObject content = JObject.Parse(await response.Content.ReadAsStringAsync());
                    string userId = content["UserId"].ToString();

                    Console.WriteLine($"Your UserId for {instance.FriendlyName} is: {userId}");
                }
                else
                {
                    Console.WriteLine($"Error calling WhoAmI: StatusCode {response.StatusCode} Reason: {response.ReasonPhrase}");
                }
            }
            catch (Exception)
            {

                throw;
            }
        }
    }
}
```

#### ServiceClient Project

The `ServiceClient` project Program.cs file contains the following:

```csharp
using Microsoft.Crm.Sdk.Messages;
using Microsoft.PowerPlatform.Dataverse.Client;
using Microsoft.PowerPlatform.Dataverse.Client.Auth;
using Microsoft.PowerPlatform.Dataverse.Client.Model;
using Microsoft.Xrm.Sdk.Discovery;
using System.ComponentModel;

namespace PowerApps.Samples
{
    class Program
    {
        //These sample application registration values are available for all online instances.
        public static string clientId = "51f81489-12ee-4a9e-aaae-a2591f45987d";
        public static string redirectUrl = "http://localhost";


        static async Task Main()
        {
            string username = "yourUserName@yourOrgName.onmicrosoft.com";
            string password = "yourPassword";

            //Set the Cloud if you want to search other than Commercial.
            Cloud cloud = Cloud.Commercial;

            //Get all environments for the selected data center.
            DiscoverOrganizationsResult orgs = await GetAllOrganizations(username, password, cloud);

            if (orgs.OrganizationDetailCollection.Count.Equals(0))
            {
                Console.WriteLine("No valid environments returned for these credentials.");
                return;
            }

            Console.WriteLine("Type the number of the environments you want to use and press Enter.");

            int number = 0;

            //Display organizations so they can be selected
            foreach (OrganizationDetail organization in orgs.OrganizationDetailCollection)
            {
                number++;

                //Get the Organization URL
                string webAppUrl = organization.Endpoints[EndpointType.WebApplication];

                Console.WriteLine($"{number} Name: {organization.FriendlyName} URL: {webAppUrl}");
            }

            string typedValue = string.Empty;
            try
            {
                typedValue = Console.ReadLine();

                int selected = int.Parse(typedValue);

                if (selected <= number)
                {
                    OrganizationDetail org = orgs.OrganizationDetailCollection[selected - 1];
                    Console.WriteLine($"You selected '{org.FriendlyName}'");

                    //Use the selected org with ServiceClient to get the UserId
                    ShowUserId(org, username, password);
                }
                else
                {
                    throw new ArgumentOutOfRangeException("The selected value is not valid.");
                }
            }
            catch (ArgumentOutOfRangeException aex)
            {
                Console.WriteLine(aex.Message);
            }
            catch (Exception)
            {
                Console.WriteLine("Unable to process value: {0}", typedValue);
            }
        }


        /// <summary>
        /// Gets organization data for the specified user and cloud
        /// </summary>
        /// <param name="username">The user's username</param>
        /// <param name="password">The user's password</param>
        /// <param name="cloud">The Cloud enum value that corresponds to the region.</param>
        /// <returns>A List of OrganizationDetail records</returns>
        public static async Task<DiscoverOrganizationsResult> GetAllOrganizations(string userName, string password, Cloud cloud)
        {
            try
            {
                //Get the Cloud URL from the Description Attribute applied for the Cloud member
                var type = typeof(Cloud);
                var memInfo = type.GetMember(cloud.ToString());
                var attributes = memInfo[0].GetCustomAttributes(typeof(DescriptionAttribute), false);
                string cloudRegionUrl = ((DescriptionAttribute)attributes[0]).Description;

                // Set up user credentials
                var creds = new System.ServiceModel.Description.ClientCredentials();
                creds.UserName.UserName = userName;
                creds.UserName.Password = password;

                try
                {
                    //Call DiscoverOnlineOrganizationsAsync
                    DiscoverOrganizationsResult organizationsResult = await ServiceClient.DiscoverOnlineOrganizationsAsync(
                           discoveryServiceUri: new Uri($"{cloudRegionUrl}/api/discovery/v2.0/Instances"),
                           clientCredentials: creds,
                           clientId: clientId,
                           redirectUri: new Uri(redirectUrl),
                           isOnPrem: false,
                           authority: "https://login.microsoftonline.com/organizations/",
                           promptBehavior: PromptBehavior.Auto);

                    return organizationsResult;
                }
                catch (Exception)
                {

                    throw;
                }
            }
            catch (Exception)
            {

                throw;
            }
        }

        /// <summary>
        /// Show the user's UserId for the selected organization
        /// </summary>
        /// <param name="org">The selected organization</param>
        /// <param name="username">The user's username</param>
        /// <param name="password">The user's password</param>
        private static void ShowUserId(OrganizationDetail org, string username, string password)
        {
            try
            {
                string conn = $@"AuthType=OAuth;
                         Url={org.Endpoints[EndpointType.OrganizationService]};
                         UserName={username};
                         Password={password};
                         ClientId={clientId};
                         RedirectUri={redirectUrl};
                         Prompt=Auto;
                         RequireNewInstance=True";
                ServiceClient svc = new(conn);

                if (svc.IsReady)
                {
                    try
                    {
                        var response = (WhoAmIResponse)svc.Execute(new WhoAmIRequest());

                        Console.WriteLine($"Your UserId for {org.FriendlyName} is: {response.UserId}");
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine(ex.Message);
                    }
                }
                else
                {
                    Console.WriteLine(svc.LastError);
                }
            }
            catch (Exception)
            {

                throw;
            }
        }
    }
}
```

### See Also

[Discover user organizations](discovery-service.md)<br />
[Sample: Blazor WebAssembly with Global Discovery](sample-blazor-web-assembly-global-discovery.md)

[!INCLUDE [footer-banner](../../includes/footer-banner.md)]
