---
title: "Discover user organizations (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Your client application may connect to multiple Dataverse environments. Use the Global Discovery Service to find which environments the user of your application can access."
ms.date: 07/18/2022
ms.reviewer: pehecke
ms.topic: article
author: ImadYanni # GitHub ID
ms.subservice: dataverse-developer
ms.author: iyanni # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
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

The following table provides the GDS location for each cloud.

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

### Limitations

The Global Discovery Service does not return information where:

- The user's account is disabled.
- Users have been filtered out based on an instance security group.
- The user has access as a result of being a delegated administrator.

If the calling user has access to no instances, the response simply returns an empty list.

## Authentication

The calling user must aquire an OAuth 2.0 token from Azure Active Directory (AD), and then add that token in the Authorization header of the API calls. More information: [Use OAuth authentication with Microsoft Dataverse](authenticate-oauth.md).

### CORS support

The Discovery Service supports the CORS standard for cross-origin access. For more information about CORS support see [Use OAuth with Cross-Origin Resource Sharing to connect a Single-Page Application](oauth-cross-origin-resource-sharing-connect-single-page-application.md).

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

Use `{{globalDiscoUrl}}` as the **Request URL** and in the **Authorization** tab, click **Get New Access Token**.

You should now be able to query the Global Discovery Service using Postman.

More information: [YouTube: Get started using Postman with Microsoft Dataverse Web API](https://youtu.be/HpUj11yU0fY)

## Service Documents

To access the Global Discovery service for each cloud, append `/api/discovery/v2.0/` to the URL. Perform a `GET` request on this url to view the service document, which contains only a single EntitySet: `Instances`.

Append `$metadata` to the cloud URL and send a `GET` request to view the CSDL (Common Schema Definition Language) service document. This XML document provides details on the `Instance` entity and the alternate keys defined for it.

## Instance EntitySet

The following table describes the properties of the `Instance` Entity from the $metadata CDSL Service document.

|Property|Type|Description|
|---------|---------|---------|
|`ApiUrl`|String|The location of web services client applications should use.|
|`DatacenterId`|String|The Id of the data center where the instance is located.|
|`DatacenterName`|String|The name of the data center where the instance is located. This value is typically null.|
|`EnvironmentId`|String|The EnvironmentId for the instance.|
|`FriendlyName`|String|A name for the instance that is displayed in powerapps.com and other client applications that allow selecting instances.|
|`Id`|Guid|The OrganizationId for the environment.|
|`IsUserSysAdmin`|Boolean|Whether the calling user has the system administrator role for the environment.|
|`LastUpdated`|DateTimeOffset|When the environment was last updated. |
|`OrganizationType`|Int32|The type of the organization. Values correspond to the <xref:Microsoft.Dynamics.CRM.OrganizationType?text=OrganizationType EnumType>|
|`Purpose`|String|Information for the purpose provided when the environment was created.|
|`Region`|String|A 2-3 letter code for region where the environment is located. |
|`SchemaType`|String|For internal use only.|
|`State`|Int32|Whether the organization is `0`:enabled  or `1`:disabled.|
|`StatusMessage`|Int32|One of the following values: <br /> `0`:`InstanceLocked`<br /> `1`:`PendingServiceInstanceMove`<br /> `2`:`InstanceFailed`<br /> `3`:`Provisioning` <br /> `4`:`InActiveOrganizationStatus`<br /> `5`:`NewInstance`<br /> `6`:`InstancePickerReady`   |
|`TenantId`|Guid|The Id of the tenant associated to the instance|
|`TrialExpirationDate`|DateTimeOffset|The date when the trial period for the instance expires.|
|`UniqueName`|String|The Unique Name for the instance.|
|`UrlName`|String|The name used for the URL.|
|`Version`|String|The current version of the environment.|
|`Url`|String|The application url for the environment.|

You can use these property names with the OData `$select` query parameter to retrieve just the data you need. In most cases, all you will need are the `FriendlyName` and `ApiUrl` properties. For example:

**Request:**

```http
GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances?$select=ApiUrl,FriendlyName HTTP/1.1
Authorization: Bearer <truncated for brevity>
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Length: 625
Content-Type: application/json; odata.metadata=minimal
odata-version: 4.0

{
  "@odata.context":"https://10.0.1.76:20193/api/discovery/v2.0/$metadata#Instances(ApiUrl,FriendlyName)",
  "value":[
    {
      "ApiUrl":"https://yourorganization.api.crm.dynamics.com",
      "FriendlyName":"Your Organization"
    }
  ]
}
```

Use the `FriendlyName` property for your application UI so the user will recognize the name of the environment. Use the `ApiUrl` to connect to Dataverse.

The rest of the properties are primarily for filtering.

## Filtering

There are two ways you can filter the instances returned:

- Using key values
- Use OData `$filter` query options

### Use one of the key values

You can use the `Id` or `UniqueName` value to filter the list to return a only the specified instance.

> [!NOTE]
> Unlike the Dataverse Web API, the Global Discovery Service doesn't provide for retrieving a specific `Instance` using the `Id` or any of the alternate keys defined for it. GDS always returns an array of values.

Both of these queries will an array with a single item:

```http
GET https://globaldisco.crm.dynamics.com/Instances(6bcbf6bf-1f2a-4ab9-9901-2605b314d72d)?$select=ApiUrl,FriendlyName,Id,UniqueName
```

```http
GET https://globaldisco.crm.dynamics.com/Instances(UniqueName='unq6bcbf6bf1f2a4ab999012605b314d')?$select=ApiUrl,FriendlyName,Id,UniqueName
```

You can also use any of the following alternate key values: `Region`, `State`, `Version` to filter on specific values. For example, use the query below to return only those instances where the Region is `NA` representing North America.

```http
GET https://globaldisco.crm.dynamics.com/Instances(Region='NA')?$select=FriendlyName,Region,State,Version,ApiUrl
```

### Use OData $filter query options

You can use OData `$filter` query options as well with any of the properties that apply, including the alternate key properties.

You can use the following comparison, logical and grouping operators:

|Operator|Description|Example|  
|--------------|-----------------|-------------|  
|**Comparison Operators**|||  
|`eq`|Equal|`$filter=IsUserSysAdmin eq true`|  
|`ne`|Not Equal|`$filter=IsUserSysAdmin ne true`|  
|`gt`|Greater than|`$filter=TrialExpirationDate gt 2022-07-14T00:00:00Z`|  
|`ge`|Greater than or equal|`$filter=TrialExpirationDate ge 2022-07-14T00:00:00Z`|  
|`lt`|Less than|`$filter=TrialExpirationDate lt 2022-07-14T00:00:00Z`|  
|`le`|Less than or equal|`$filter=TrialExpirationDate le 2022-07-14T00:00:00Z`|  
|**Logical Operators**|||  
|`and`|Logical and|`$filter=TrialExpirationDate gt 2022-07-14T00:00:00Z and IsUserSysAdmin eq true`|  
|`or`|Logical or|`$filter=TrialExpirationDate gt 2022-07-14T00:00:00Z or IsUserSysAdmin eq true`|  
|`not`|Logical negation|`$filter=not contains(Purpose,'test')`|  
|**Grouping Operators**|||  
|`( )`|Precedence grouping|`(contains(Purpose,'sample') or contains(Purpose,'test')) and TrialExpirationDate gt 2022-07-14T00:00:00Z`|  


You can use the following string query functions:
 
|Function|Example|  
|--------------|-------------|  
|`contains`|`$filter=contains(Purpose,'test')`|  
|`endswith`|`$filter=endswith(FriendlyName,'Inc.')`|  
|`startswith`|`$filter=startswith(FriendlyName,'A')`|  

> [!NOTE]
> Unlike the Dataverse Web API, Global Discovery Service search strings are case sensitive.

## Use Dataverse ServiceClient

For .NET applications you can use <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient?text=Dataverse.Client.ServiceClient>.<xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.DiscoverOnlineOrganizationsAsync%2A?text=DiscoverOnlineOrganizationsAsync Method> to call the Global Discovery Services.

```csharp
 // Set up user credentials
var creds = new System.ServiceModel.Description.ClientCredentials();
creds.UserName.UserName = userName;
creds.UserName.Password = password;

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
```

While the `DiscoverOnlineOrganizationsAsync` method uses the same OData endpoint and enables that it be passed in the `discoveryServiceUri` parameter, it does not return data in the shape of an *Instance*. Data is returned as an <xref:Microsoft.PowerPlatform.Dataverse.Client.Model.DiscoverOrganizationsResult?text=DiscoverOrganizationsResult Class> that includes a <xref:Microsoft.PowerPlatform.Dataverse.Client.Model.DiscoverOrganizationsResult.OrganizationDetailCollection?text=OrganizationDetailCollection Property> which contains a collection of <xref:Microsoft.Xrm.Sdk.Discovery.OrganizationDetail?text=OrganizationDetail Class> instances. This class contains the same information as the `Instance` types returned by the OData service.

> [!NOTE]
> While the `DiscoverOnlineOrganizationsAsync.discoveryServiceUri` parameter accepts a URL to the Global Discovery Service, any `$select` or `$filter` query options used will be ignored. The `DiscoverOnlineOrganizationsAsync.discoveryServiceUri` parameter is optional and if not provided will default to the Commercial cloud.

## Use CrmServiceClient

For .NET Framework applications you can continue to use the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.DiscoverGlobalOrganizations%2A?text=CrmServiceClient.DiscoverGlobalOrganizations Method> to call the Global Discovery Service.

```csharp
  // Set up user credentials
  var creds = new System.ServiceModel.Description.ClientCredentials();
  creds.UserName.UserName = userName;
  creds.UserName.Password = password;

  // Call to get organizations from global discovery
  var organizations = CrmServiceClient.DiscoverGlobalOrganizations(
        discoveryServiceUri:new Uri($"{cloudRegionUrl}/api/discovery/v2.0/Instances"), 
        clientCredentials: creds, 
        user: null, 
        clientId: clientId,
        redirectUri: new Uri(redirectUrl), 
        tokenCachePath: "",
        isOnPrem: false,
        authority: string.Empty, 
        promptBehavior: PromptBehavior.Auto);

  return organizations.ToList();
```

Like the `ServiceClient.DiscoverOnlineOrganizationsAsync` method, the `CrmServiceClient.DiscoverGlobalOrganizations` method also does not return data as an *Instance*. It returns a <xref:Microsoft.Xrm.Sdk.Discovery.OrganizationDetailCollection?text=OrganizationDetailCollection> which contains a collection of <xref:Microsoft.Xrm.Sdk.Discovery.OrganizationDetail?text=OrganizationDetail Class> instances that contains the same information as the `Instance` types returned by the OData service.

### See Also

[Sample: Global Discovery Service Sample (C#)](sample-global-discovery-service-csharp.md)<br />
[Sample: Access the Discovery service using CrmServiceClient](sample-discovery-service-crmserviceclient.md)<br />
[Sample: Blazor WebAssembly with Global Discovery](sample-blazor-web-assembly-global-discovery.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
