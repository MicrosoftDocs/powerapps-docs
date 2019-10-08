---
title: "Discover the URL for your organization using the Web API (Common Data Service)| Microsoft Docs"
description: "Learn how you can use the Web API to discover at runtime the organizations, or instances that the logged-on user belongs to"
ms.custom: ""
ms.date: 04/22/2019
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 2db13b4e-0e7c-4f25-b7be-70a612fb96e2
caps.latest.revision: 18
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "susikka"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Discover the URL for your organization using the Web API

[!INCLUDE [cc-discovery-service-description](../includes/cc-discovery-service-description.md)]

With the Web API discovery service, you can use standard `$filter` and `$select` parameters to a Web API service request to customize the returned list of instance data.
<!-- TODO should only talk about the global discovery service -->

## Global discovery service

In addition to datacenter specific Discovery services, that are available on the 2011 (SOAP) endpoint and through the Web API, there is also a Web API only Global Discovery service that spans all operational datacenters. For more information about the Discovery service on the 2011 endpoint see [Discovery Service](../org-service/discovery-service.md)

> [!NOTE]
> It is recommended that users switch from the legacy regional discovery service (`https://disco.crm.dynamics.com`) to global discovery service (`https://globaldisco.crm.dynamics.com`).
> 
> For Dynamics 365 US Government users, the global discovery service is available for the **GCC** and **GCC High** users, and the URL is different from the regular global discovery service URL. More information: [Dynamics 365 Government URLs](https://docs.microsoft.com/dynamics365/customer-engagement/admin/government/microsoft-dynamics-365-government#dynamics-365-us-government-urls).

  
## Information provided by the Discovery service 
 
 Organization information is stored in the `Instance` entity of the Discovery service.  To see the kind of information contained in that entity, send an HTTP GET request to the service for one of your instances.  
  
```http  
GET https://globaldisco.crm.dynamics.com/api/discovery/v1.0/Instances(UniqueName='myorg')  
```  
  
In the above example, the global Discovery service of Common Data Service is used to obtain the organization information of the instance with a unique name of "myorg". More details about this request is expanded upon later in this topic.  

 

  
### Scope of the returned information

For the global Discovery service, the `Instances` entity set, returns the set of instances that the user has access to across all geographies, when no filters are applied.   The returned data has a scope as described below.  
  
-   Includes all instances in the commercial cloud where the user is provisioned and enabled, except sovereign clouds instances are not returned
-   Does not  include instances where the user's account is disabled
-   Does not include instances where users have been filtered out based on an instance security group
-   Does not include instances where the user has access as a result of being a delegated administrator
-   If the calling user has access to no instances, the response simply returns an empty list

## How to access the Discovery services

In general, the Web API address of the Discovery service has the following format: `<service base address>/api/discovery/`.  The addresses for  each deployment type are identified below. You can easily  find the Web API addresses and version number for your deployment in the Common Data Service web application by navigating to **Settings > Customization > Developer Resources**  
  
### Common Data Service Discovery services  

The service base address of the global Discovery service is : `https://globaldisco.crm.dynamics.com/`. This results in the service address of `https://globaldisco.crm.dynamics.com/api/discovery/`.  
  
## Using the Discovery service  

An entity set named `Instances` is used to obtain instance information. You can use `$select` and `$filter` with the Instances entity set to filter the returned data. You can also use `$metadata` to obtain the metadata document of the service.  
  
### Authentication

Common Data Service Web API instances of the Discovery service require authentication with OAuth access tokens.

When the Discovery service is configured for OAuth authentication, a request sent  to the service Web API without an access token triggers a bearer challenge with the authority of the “common” endpoint and the resource ID of the service.
### CORS support

The Discovery service Web API supports the CORS standard for cross-origin access as does the Web API.  For more information about CORS support see [Use OAuth with Cross-Origin Resource Sharing  to connect a Single Page Application](../oauth-cross-origin-resource-sharing-connect-single-page-application.md).  
  
### Examples  
  
-   Get the details of a specific instance. If you leave out the GUID, all instances that the authenticated user has access to are returned.  
  
    ```http      
    GET https://globaldisco.crm.dynamics.com/api/discovery/v1.0/Instances(<guid>)
    GET https://disco.crm.dynamics.com/api/discovery/v9.0/Instances(<guid>)  
    ```  
  
-   You can use the UniqueName attribute as an alternate key.  
  
    ```http  
    GET https://globaldisco.crm.dynamics.com/api/discovery/v1.0/Instances(UniqueName='myorg')  
    ```  
  
-   Retrieve a list of available instances, filtered by production type.  
  
    ```http  
    GET https://globaldisco.crm.dynamics.com/api/discovery/v1.0/Instances?$select=DisplayName,Description&$filter=Type+eq+0   
    ```  
  
-   Retrieve a specific instance's ID property value.  
  
    ```http  
    GET https://disco.crm.dynamics.com/api/discovery/v9.0/Instances(UniqueName='myorg')/Id/$value  
    ```

## See also

[Web API Global Discovery Service sample (C#)](samples/global-discovery-service-csharp.md)

