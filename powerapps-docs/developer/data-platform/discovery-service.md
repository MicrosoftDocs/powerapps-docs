---
title: "Discover user organizations (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Your client application may connect to multiple Dataverse environments. Use the Global Discovery Service to find which environments the user of your application can access."
ms.date: 07/01/2022
ms.reviewer: pehecke
ms.topic: article
author: ImadYanni # GitHub ID
ms.subservice: dataverse-developer
ms.author: iyanni # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - PHecke
  - JimDaly
---

# Discover user organizations

Your client application may connect to multiple Dataverse environments. Use the Global Discovery Service to find which environments the user of your application can access.

In [Power Apps](https://make.powerapps.com) you can select from a list of environments available to you. The Global Discovery Service is the source of that data. Within your own app, you can provide a select control to allow users to choose which environment they want to use. Their choice will determine which environment your app must connect to.

With Dataverse, server and organization allocation may change as part of datacenter management and load balancing. Therefore, the Global Discovery Service provides a way to discover which server is serving an instance at a given time.

More information:

- [Choose an environment](../../maker/canvas-apps/intro-maker-portal.md#choose-an-environment)
- [Environments overview](/power-platform/admin/environments-overview)

## Global Discovery Service

The Global Discovery service, sometimes called GDS, is a set of OData v4.0 endpoints that are available for 5 different clouds.

> [!NOTE]
> While both the Dataverse Web API and the Global Discovery Service are OData v4.0 endpoints, they are separate endpoints with different behaviors.

The following table provides the location for each cloud.

|Cloud|URL and Description|
|---------|---------|
|Commercial|`https://globaldisco.crm.dynamics.com`<br />Used by private sector companies. This is the most commonly used cloud.|
|GCC|`https://globaldisco.crm9.dynamics.com`<br />Government Community Cloud. Used by public sector employees and contractors in the United States. |
|USG|`https://globaldisco.crm.microsoftdynamics.us`<br />Used by United States Federal government employees and contractors. Also known as GCC High.|
|DOD|`https://globaldisco.crm.appsplatform.us`<br />Used by Unites States Department of Defense employees and contractors.|
|China|`https://globaldisco.crm.dynamics.cn`<br />Used by companies in China to comply with regulatory requirements.|

More information:

- [Dynamics 365 US Government](/power-platform/admin/microsoft-dynamics-365-government)
- [Power Platform and Dynamics 365 apps - operated by 21Vianet in China](/power-platform/admin/about-microsoft-cloud-china)

## Authentication

The calling user must include a valid OAuth access token for the Global Discovery service.

### Use Postman to connect to the Global Discovery Service

You can use the same approach described for the Dataverse Web API here: [Set up a Postman environment](webapi/setup-postman-environment.md), but instead of the environment variables described in that topic, use the following to access the commercial cloud.

|Variable  |Initial Value  |
|---------|---------|
|`cloudUrl`|`https://globaldisco.crm.dynamics.com`|
|`globalDiscoUrl`|`{{cloudUrl}}/api/discovery/v2.0/`|
|`clientid`|`51f81489-12ee-4a9e-aaae-a2591f45987d`|
|`authurl`|`https://login.microsoftonline.com/common/oauth2/authorize?resource={{cloudUrl}}`|

Then, in the Postman **Authorization** tab, set or verify the following values:

|Field  |Value  |
|---------|---------|
|**Type**|OAuth 2.0|
|**Add authorization data to** |Request Headers|
|**Header Prefix**|Bearer|
|**Grant Type**|Implicit|
|**Callback URL**|`http://localhost`|
|**Auth URL**|`{{authurl}}`|
|**Client ID**|`{{clientid}}`|
|**Client Authentication**|Send as Basic Auth header|

Finally, use `{{globalDiscoUrl}}` as the **Request URL** and send a `GET` request.

More information: [YouTube: Get started using Postman with Microsoft Dataverse Web API](https://youtu.be/HpUj11yU0fY)

## Service Documents

To access the Global Discovery service for each cloud, append `/api/discovery/v2.0/` to the URL. Perform a `GET` request on this url to view the service document, which contains only a single EntitySet: `Instances`.

Append `$metadata` to the cloud URL and send a `GET` request to view the CSDL (Common Schema Definition Language) service document. This XML document provides details on the `Instance` entity and the alternate keys defined for it.

> [!NOTE]
> Unlike the Dataverse Web API, the Global Discovery service doesn't provide for retrieving a specific `Instance` using the `Id` or any of the alternate keys defined for it. GDS always returns an array of values.

## Instance EntitySet

The following table descripts the properties of the `Instance` EntitySet.

|Property|Type|Description|
|---------|---------|---------|
|`ApiUrl`|String|The location of web services client applications should use.|
|`DatacenterId`|String|The Id of the data center where the instance is located.|
|`DatacenterName`|String|The name of the data center where the instance is located. This value is typically null.|
|`EnvironmentId`|String|The EnvironmentId for the instance.|
|`FriendlyName`|String|A name for the instance that is displayed in powerapps.com and other client applications that allow selecting instances.|
|`Id`|Guid|The unique identifier for the instance.|
|`IsUserSysAdmin`|Boolean|Whether the calling user has the system administrator role for the environment.|
|`LastUpdated`|DateTimeOffset|When the environment was last updated. |
|`OrganizationType`|Int32|The type of the organization. Values correspond to the OrganizationType Enum|
|`Purpose`|String|Information for the purpose provided when the environment was created.|
|`Region`|String|A three letter code for region where the environment is located. |
|`SchemaType`|String|For internal use only.|
|`State`|Int32|Whether the organization is enabled (`0`) or eisabled (`1`).|
|`StatusMessage`|Int32|TODO: This is an integer value. What does it mean?|
|`TenantId`|Guid|The Id of the tenant associated to the instance|
|`TrialExpirationDate`|DateTimeOffset|The date when the trial period for the instance expires.|
|`UniqueName`|String|The Unique Name for the instance.|
|`UrlName`|String|The name used for the URL.|
|`Version`|String|The current version of the environment.|
|`Url`|String|The application url for the environment.|

You can use these property names with the OData $select query parameter to retrieve just the data you need. In most cases, all will need are the `FriendlyName` and `ApiUrl` properties. For example

**Request**

```http
GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances?$select=ApiUrl,FriendlyName HTTP/1.1
Authorization: Bearer < truncated for brevity>
```

**Response**

```http
HTTP/1.1 200 OK
Content-Length: 625
Content-Type: application/json; odata.metadata=minimal
odata-version: 4.0

{
  "@odata.context":"https://10.0.1.76:20193/api/discovery/v2.0/$metadata#Instances(ApiUrl,FriendlyName)","value":[
    {
      "ApiUrl":"https://yourorganization.api.crm2.dynamics.com",
      "FriendlyName":"Your Organization"
    }
  ]
}
```

## Filtering













The Discovery service is accessed through two different APIs:

- For the OData V4 RESTful API: [Discover the URL for your organization](webapi/discover-url-organization-web-api.md)
- For the discovery API available through the 2011 (SOAP) endpoint: [Use the Discovery service with the Microsoft.Xrm.Sdk.Discovery NameSpace](org-service/discovery-service.md)

> [!NOTE]
> The *regional* Discovery service was deprecated in March 2020 and removed in April 2021. More information: [Regional Discovery Service is deprecated](/power-platform/important-changes-coming#regional-discovery-service-is-deprecated).

### See Also

[Use the Microsoft Dataverse Web API](webapi/overview.md)<br />
[Modify your code to use global Discovery service](webapi/discovery-orgsdk-to-webapi.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
