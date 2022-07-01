---
title: "Discover the URL for your organization (Microsoft Dataverse)| Microsoft Docs"
description: "Use the Discovery Service to find the organizations (instances) that the logged-on user belongs to"
ms.date: 04/06/2022
author: ImadYanni
ms.author: iyanni
ms.reviewer: jdaly
manager: sporter
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
  - phecke
---
# Discover the URL for your organization

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can create a client for a specific Microsoft Dataverse environment and not provide the user any options about which environment they can connect with. Only valid users for that specific environment can use your client.

If you want people using your client to be able to connect to any Dataverse environment they have access to you could prompt them to enter the URL for their environment, but this is not recommended. Each user may have access to multiple Dataverse environments. Users may not know or remember the URL for their environment. Expecting people to enter this URL is bound to frustrate users. 

Instead, your client should provide a list of each of the available environments based on the user's credentials. If there is more than one environment available, your application should prompt the user to choose which environment they want to connect with.

With Dataverse, server and organization allocation may change as part of datacenter management and load balancing. Therefore, a discovery service provides a way to discover which server is serving an instance at a given time.

When accessing the Discovery Service using the OData V4 RESTful API, you can add standard `$filter` and `$select` parameters to the service request to customize the returned list of instance data.

> [!IMPORTANT]
> - Effective March 2, 2020, the *regional* Discovery Service will be [deprecated](/power-platform/important-changes-coming#regional-discovery-service-is-deprecated). Applications must use the global Discovery Service that is documented in this topic.  
> - For Dynamics 365 US Government users, a *global* Discovery Service endpoint is available for the **GCC** and **GCC High** users, and the URL is different from the regular global Discovery Service URL. More information: [Dynamics 365 Government URLs](/dynamics365/customer-engagement/admin/government/microsoft-dynamics-365-government#dynamics-365-us-government-urls).

## Information provided by the Discovery Service 

Organization information is stored in the `Instance` table of the Discovery Service.  To see the kind of information contained in that table, send an HTTP GET request to the service for one of your instances.  
  
```http  
GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances(UniqueName='myorg')  
```

In the above example, the global Discovery Service is used to obtain the organization information of the instance with a unique name of "myorg". More details about this request is provided later in this topic.  

### Scope of the returned information

For the global Discovery Service, the `Instances` entity set, returns the set of instances (environments) that the user has access to across all geographies, when no filters are applied.   The returned data has a scope as described below.  
  
-   Includes all instances in the commercial cloud where the user is provisioned and enabled, except sovereign clouds instances are not returned
-   Does not  include instances where the user's account is disabled
-   Does not include instances where users have been filtered out based on an instance security group
-   Does not include instances where the user has access as a result of being a delegated administrator
-   If the calling user has access to no instances, the response simply returns an empty list

## How to access the Discovery Service

In general, the Web address of the Discovery Service has the following format: `<service base address>/api/discovery/`.  You can easily find the Web address and version number for your deployment in the Microsoft Dataverse Web application by navigating to **Settings > Customization > Developer Resources**  
  
### Dataverse Discovery services  

The service base address of the global Discovery Service is : `https://globaldisco.crm.dynamics.com/`. This results in the service address of `https://globaldisco.crm.dynamics.com/api/discovery/`.  
  
## Using the Discovery service  

An entity set named `Instances` is used to obtain instance information. You can use `$select` and `$filter` with the Instances entity set to filter the returned data. You can also use `$metadata` to obtain the metadata document of the service.  
  
### Authentication

Accessing the Discovery Service requires authentication with an OAuth access token.

When the Discovery Service is configured for OAuth authentication, a request sent to the service without an access token triggers a bearer challenge with the authority of the "common" endpoint and the resource ID of the service.

### CORS support

The Discovery Service supports the CORS standard for cross-origin access. For more information about CORS support see [Use OAuth with Cross-Origin Resource Sharing  to connect a Single Page Application](../oauth-cross-origin-resource-sharing-connect-single-page-application.md).  
  
### Examples  
  
-   Get the details of a specific instance. If you leave out the GUID, all instances that the authenticated user has access to are returned.  
  
    ```http      
    GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances(<guid>)
    ```  
  
-   You can use the UniqueName column as an alternate key.  
  
    ```http  
    GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances(UniqueName='myorg')  
    ```  
  
-   Retrieve a list of available instances, filtered by production type.  
  
    ```http  
    GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances?$select=DisplayName,Description&$filter=Type+eq+0   
    ```  
  
## See also

[Discovery Service sample (C#)](samples/global-discovery-service-csharp.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]