---
title: "Quick Start Sample: Retrieve Microsoft Dataverse environements using Online Management API| MicrosoftDocs"
description: "The C# sample demonstrates how to authenticate to the Online Management API and then retrieve all Microsoft Dataverse environments from your Microsoft 365 tenant."
ms.date: 10/01/2019
ms.service: powerapps
ms.topic: conceptual
ms.assetid: 63600a55-a1f0-491f-83f6-b3252566d27e
author: KumarVivek
ms.author: kvivek
manager: annbe
search.audienceType: 
  - developer
search.app: 
  - PowerApps
---
# Quick Start Sample: Retrieve Microsoft Dataverse environments using Online Management API 

> [!NOTE]
> Effective August 26, 2020, the Online Management API is [deprecated](/power-platform/important-changes-coming##online-management-api-powershell-module-and-rest-api-are-deprecated).

The C# sample demonstrates how to authenticate to the Online Management API and then retrieve all Dataverse environments from your Microsoft 365 tenant.

The sample uses the authentication [helper code](sample-authentication-helper.md) to easily authenticate to Online Management API using the OAuth 2.0 protocol and pass in the access token in header of your request.

## What this sample does?

The sample performs the following tasks:

1. Uses the **ConnectToAPI** method to connect to the Online Management API.

    a. Calls the **DiscoverAuthority** method in the authentication helper code, and passes in the service URL to get the authority information.

    b. Uses an HttpClient instance to connect to Online Management API service.

    c. Specifies the API service base address and the max period of execution time.
1. Uses the **RetrieveInstancesAsync** method to execute a http request to retrieve all Customer Engagement instances in your Microsoft 365 tenant, and then displays the response.

## Run this sample
Before you can run this sample, make sure that you have:
- One of the admin roles in your Microsoft 365 tenant. See [Microsoft 365 Admin roles](get-started-online-management-api.md#microsoft-365-admin-roles)
- Visual Studio 2015 or later; Internet connectivity is required to download/restore assemblies in the NuGet package.
- .NET Framework 4.6.2

To run the sample:
1. [Download](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/online-management-api) the sample, and extract it.
2. Double-click the Visual Studio solution file (.sln) under the C# folder at the extracted location to open the solution in Visual Studio.
3. In the **Programs.cs** file, specify a different service URL if the region is not North America. For a list of service URL values for worldwide regions, see [Service URL](get-started-online-management-api.md#service-url).
    ```csharp
    //TODO: Change this value if your Microsoft 365 tenant is in a different region than North America

    private static string _serviceUrl = "https://admin.services.crm.dynamics.com";
    ```
4. In the **HelperCode** > **AuthenticationHelper.cs** file, update the values of the `_clientId` and `_redirectURL` values appropriately.

    ```csharp
    // TODO: Substitute your app registration values here.
    // These values are obtained on registering your application with the 
    // Azure Active Directory.
    private static string _clientId = "<GUID>";    //e.g. "e5cf0024-a66a-4f16-85ce-99ba97a24bb2"
    private static string _redirectUrl = "<Url>";  //e.g. "app://e5cf0024-a66a-4f16-85ce-99ba97a24bb2"
    ```
5. Save changes, and then start debugging by pressing F5 or select **Debug** > **Start Debugging**.

## Code sample listing 

Here is the complete sample code:

```csharp
using Microsoft.Crm.Sdk.Samples.HelperCode;
using System;
using System.Net.Http;
using System.Threading.Tasks;


namespace Microsoft.Crm.Sdk.Samples
{
    /// <summary>
    /// This sample retrieves Customer Engagement instances
    /// in your Microsoft 365 tenant.
    /// </summary>    

    class RetrieveInstances
    {
        private HttpClient httpClient;

        //TODO: Change this value if your Microsoft 365 tenant is in a different region than North America
        private static string _serviceUrl = "https://admin.services.crm.dynamics.com";

        private void ConnectToAPI()
        {
            Console.WriteLine("Connecting to the Online Management API service...");

            // Discover authority for the Online Management API service
            var authority = Authentication.DiscoverAuthority(_serviceUrl);

            // Authenticate to the Online Management API service by 
            // passing in the discovered authority 
            Authentication auth = new Authentication(authority.Result.ToString());            

            // Use an HttpClient object to connect to Online Management API service.           
            httpClient = new HttpClient(auth.ClientHandler, true);

            // Specify the API service base address and the max period of execution time 
            httpClient.BaseAddress = new Uri(_serviceUrl);
            httpClient.Timeout = new TimeSpan(0, 2, 0);            
        }

        public async Task RetrieveInstancesAsync()
        {
            HttpRequestMessage myRequest = new HttpRequestMessage(HttpMethod.Get, "/api/v1.1/instances");
            HttpResponseMessage myResponse = await httpClient.SendAsync(myRequest);

            if (myResponse.IsSuccessStatusCode)
            {
                var result = myResponse.Content.ReadAsStringAsync().Result;
                Console.WriteLine("Your instances retrieved from Microsoft 365 tenant: \n{0}", result);
            }
            else
            {
                Console.WriteLine("The request failed with a status of '{0}'",
                       myResponse.ReasonPhrase);
            }
        }

        static public void Main(string[] args)
        {
            RetrieveInstances app = new RetrieveInstances();
            try
            {
                // Connect to the Online Management API. 
                app.ConnectToAPI();

                // Run your request
                Task.WaitAll(Task.Run(async () => await app.RetrieveInstancesAsync()));
            }
            catch (System.Exception ex) { DisplayException(ex); }
            finally
            {
                if (app.httpClient != null)
                { app.httpClient.Dispose(); }
                Console.WriteLine("Press <Enter> to exit the program.");
                Console.ReadLine();
            }
        }

        /// <summary> Helper method to display exceptions </summary> 
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
}
```

### Related Topics  

[Get started with Online Management API](get-started-online-management-api.md)

[Operations supported by Online Management API](operations-supported.md)

[Online Management API Reference](/rest/api/admin.services.crm.dynamics.com)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]