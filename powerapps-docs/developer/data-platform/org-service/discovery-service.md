---
title: "Use the Discovery Service with the SDK Assemblies (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes how to use the Discovery Service with the APIs available in the Microsoft Dataverse SDK assemblies." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.date: 1/16/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Use the Discovery Service with the SDK Assemblies

> [!IMPORTANT]
> Effective March 2, 2020, the *regional* Discovery Service will be [deprecated](/power-platform/important-changes-coming#regional-discovery-service-is-deprecated).
>
> For information on how to transition to use the *global* Discovery Service, see [Modify your code to use global Discovery Service](../webapi/discovery-orgsdk-to-webapi.md).

[!INCLUDE [cc-discovery-service-description](../includes/cc-discovery-service-description.md)]

To access the Discovery Service using SDK assembly APIs, add a reference to the `Microsoft.Xrm.Sdk.dll` assembly in your Visual Studio project, and then add a `using` statement to access the <xref:Microsoft.Xrm.Sdk.Discovery> namespace.

The <xref:Microsoft.Xrm.Sdk.WebServiceClient.DiscoveryWebProxyClient> implements the <xref:Microsoft.Xrm.Sdk.Discovery.IDiscoveryService> interface.

The <xref:Microsoft.Xrm.Sdk.Discovery.IDiscoveryService> interface provides <xref:Microsoft.Xrm.Sdk.Discovery.IDiscoveryService.Execute(Microsoft.Xrm.Sdk.Discovery.DiscoveryRequest)> method you will use to pass a instance of the abstract <xref:Microsoft.Xrm.Sdk.Discovery.DiscoveryRequest> class.

## Regional Discovery services

When you instantiate the <xref:Microsoft.Xrm.Sdk.WebServiceClient.DiscoveryWebProxyClient> you will need to provide a URL for a regional data center using one of the following values.

[!INCLUDE [regional-discovery-services](../../../includes/regional-discovery-services.md)]

> [!NOTE]
> If you do not know the user's region, you need to loop through the available regions until you get results. A single global Discovery Service is also available. More information: [Discover the URL for your organization](../webapi/discover-url-organization-web-api.md)

## Discovery service messages

There are three messages that you can use which all inherit from the abstract <xref:Microsoft.Xrm.Sdk.Discovery.DiscoveryRequest> class.

 The following table lists the messages that are supported with <xref:Microsoft.Xrm.Sdk.Discovery.IDiscoveryService.Execute(Microsoft.Xrm.Sdk.Discovery.DiscoveryRequest)> method.  
  
|Message|Description|  
|-------------|-----------------|  
|<xref:Microsoft.Xrm.Sdk.Discovery.RetrieveUserIdByExternalIdRequest>|Retrieves the logged-on user's ID in Microsoft Dataverse|  
|<xref:Microsoft.Xrm.Sdk.Discovery.RetrieveOrganizationRequest>|Retrieves information about a single organization.|  
|<xref:Microsoft.Xrm.Sdk.Discovery.RetrieveOrganizationsRequest>|Retrieves information about all organizations to which the user belongs.|  

## Example

The following code for a console application uses the <xref:Microsoft.Xrm.Sdk.Discovery.RetrieveOrganizationsRequest> message to retrieve all the organizations for a user.

```csharp
using System;
using System.Linq;
using Microsoft.Xrm.Sdk.Discovery;
using Microsoft.IdentityModel.Clients.ActiveDirectory;
using Microsoft.Xrm.Sdk.WebServiceClient;

namespace DiscoveryServiceSample
{
    class Program
    {
        //These sample application registration values are available for all online instances.
        // this sample requires ADAL.net 5.2 or later
        public static string clientId = "51f81489-12ee-4a9e-aaae-a2591f45987d";

        static OrganizationDetailCollection GetOrganizationDetails(DiscoveryWebProxyClient svc)
        {

            var request = new RetrieveOrganizationsRequest()
            {
                AccessType = EndpointAccessType.Default,
                Release = OrganizationRelease.Current
            };
            try
            {
                var response = (RetrieveOrganizationsResponse)svc.Execute(request);
                return response.Details;
            }
            catch (Exception)
            {
                throw;
            }
        }
        static void Main(string[] args)
        {
            string authority = @"https://login.microsoftonline.com/common";
            string northAmericaResourceUrl = "https://disco.crm.dynamics.com";
            string discoveryUrl = $"{northAmericaResourceUrl}/XRMServices/2011/Discovery.svc/web";
            Uri discoveryUri = new Uri(discoveryUrl);

            AuthenticationContext authContext = new AuthenticationContext(authority, false);
            string username = "you@yourorg.onmicrosoft.com";
            string password = "yourPassword"; 

            AuthenticationResult authResult = null;
            if (username != string.Empty && password != string.Empty)
            {
                UserPasswordCredential cred = new UserPasswordCredential(username, password);
                authResult = authContext.AcquireTokenAsync(northAmericaResourceUrl, clientId, cred).Result;
            }

           
            using (var svc = new DiscoveryWebProxyClient(discoveryUri))
            {
                svc.HeaderToken = authResult.AccessToken;

                OrganizationDetailCollection details = GetOrganizationDetails(svc);

                details.ToList().ForEach(x =>
                {
                    Console.WriteLine("Organization Name: {0}", x.FriendlyName);
                    Console.WriteLine("Unique Name: {0}", x.UniqueName);
                    Console.WriteLine("Endpoints:");
                    foreach (var endpoint in x.Endpoints)
                    {
                        Console.WriteLine("  Name: {0}", endpoint.Key);
                        Console.WriteLine("  URL: {0}", endpoint.Value);
                    }
                    Console.WriteLine();
                });
            };
            Console.ReadLine();
        }
    }
}

```

The results may look like this for a user with access to two instances:

```
Organization Name: Organization A
Unique Name: orga
Endpoints:
  Name: WebApplication
  URL: https://orgaservice.crm.dynamics.com/
  Name: OrganizationService
  URL: https://orgaservice.api.crm.dynamics.com/XRMServices/2011/Organization.svc
  Name: OrganizationDataService
  URL: https://orgaservice.api.crm.dynamics.com/XRMServices/2011/OrganizationData.svc

Organization Name: Organization B
Unique Name: orgb
Endpoints:
  Name: WebApplication
  URL: https://orgbservice.crm.dynamics.com/
  Name: OrganizationService
  URL: https://orgbservice.api.crm.dynamics.com/XRMServices/2011/Organization.svc
  Name: OrganizationDataService
  URL: https://orgbservice.api.crm.dynamics.com/XRMServices/2011/OrganizationData.svc
```

> [!NOTE]
> The `OrganizationDataService` is the deprecated Organization Data Service, not the Web API. This service does not include a URL for the Web API.


### See also

[Discovery Services](../discovery-service.md)<br />
[Discover the URL for your organization](../webapi/discover-url-organization-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]