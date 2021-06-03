---
title: "Modify your code to use global Discovery Service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Update your application code to make Discovery Service calls using a modern RESTful API."
ms.custom: ""
ms.date: 1/16/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "bpevans" # GitHub ID
ms.author: "bevans" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType:
  - developer
search.app:
  - PowerApps
  - D365CE
---

# Modify your code to use global Discovery Service

The Discovery Service APIs can be used by your application to discover business organization instances (environments) that the application user has access to. If your application currently uses the Organization Service API on the 2011 SOAP endpoint to discover organization instances, you can follow the steps in this topic and convert your application to access organization details using the OData V4 RESTful API with the global Discovery Service URL. If your application accesses the Discovery Service using the regional Discovery Service URL, you will need to change the application code from using the regional URL to the global Discovery Service URL.

A detailed description of using the Discovery Service with the RESTful API can be found on the [Discover the URL for your organization](./discover-url-organization-web-api.md) page.

> [!IMPORTANT]
> When accessing the Discovery Service, it is strongly recommended that your application use the *global* Discovery Service endpoint (https://globaldisco.crm.dynamics.com) and not the *regional* Discovery Service endpoint, which will be [deprecated](/power-platform/important-changes-coming#regional-discovery-service-is-deprecated) on March 2, 2020. The global Discovery Service is only available when using the RESTful API.

The rest of this document describes the changes that may be needed to call the Discovery Service using the RESTful API.

## Authentication
Accessing the Discovery Service using the RESTful API requires authentication with an OAuth 2.0 access token.
If your application code uses WS-Trust SAML tokens for authentication, you need to change your application code to acquire an OAuth 2.0 token from Azure Active Directory (AD), and then add that token in the Authorization header of the Discovery Service API calls. More information: [Use OAuth with Microsoft Dataverse](../authenticate-oauth.md).

## OData API calls
The example HTTP requests shown below are supported by the Discovery Service RESTful API. These examples use the Instances API to return the same organization data as the <xref:Microsoft.Xrm.Sdk.Discovery.RetrieveOrganizationsRequest> and <xref:Microsoft.Xrm.Sdk.Discovery.RetrieveOrganizationRequest> message requests of the Organization Service API.

-    Get all instances for the user in all regions.
```http  
GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances
```  
-    Get all instances for the user in a specific region.
```http  
GET  https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances(Region={region})
```
Response
```JSON
{
  "value":[
    {
      "Id":"<GUID>",
      "UniqueName":"myorg",
      "UrlName":"orgurlname",
      "FriendlyName":"My Org",
      "State":0,
      "Version":"<Version>",
      "Url":"https://orgurlname.crm.dynamics.com",
      "ApiUrl":"https://orgurlname.api.crm.dynamics.com"
    }
  ]
}
```

-    Get a single instance by ID
```http  
GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances(<guid>)
```  
-    Get a single instance by unique name
```http  
GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances(UniqueName='myorg')  
```  

Response
```JSON
{
  "Id":"<GUID>",
  "UniqueName":"myorg",
  "UrlName":"orgurlname",
  "FriendlyName":"My Org",
  "State":0,
  "Version":"<Version>",
  "Url":"https://orgurlname.crm.dynamics.com",
  "ApiUrl":"https://orgurlname.api.crm.dynamics.com"
}
```

## Mapping of columns

The table shown below shows the column mapping in the responses returned from the Discovery Service when using the two APIs. These are applicable to all above example calls.

Response field (SOAP endpoint) |	Response field (OData V4 RESTful endpoint)
------------------------------------|---------------------------------
Endpoints[WebApplication] |	Url
Endpoints[OrganizationService]	| {ApiUrl}/XRMServices/2011/Organization.svc
Endpoints[OrganizationDataService] |{ApiUrl}//XRMServices/2011/OrganizationData.svc
FriendlyName|FriendlyName
OrganizationId|Id
OrganizationVersion|Version
State | State<br/><ul><li>0: Enabled</li><li>1: Disabled</li><ul>
UniqueName|UniqueName
UrlName|UrlName

## Deprecated API call
The Organization Service API message GetUserIdByExternalId is not supported in the RESTful API.

## See Also

[Discovery Services](../discovery-service.md)  
[Use the Dataverse Web API](./discover-url-organization-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]