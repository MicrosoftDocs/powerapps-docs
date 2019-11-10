# Modify existing code using the Organization SDK for discovery to use Discovery Web API

The Discovery Service Web API can be used to discover instances for your users. If you currently use Organization Service SDK to discover your instances, you can follow the steps in this document to start consuming the Web API. 
A detailed description of the Web API can be found on the [Discovery Service Web API](/powerapps/developer/common-data-service/webapi/discover-url-organization-web-api) page.
 
If you currently use the Web API, it is recommended that you make sure to point to the global Discovery service endpoint (https://globaldisco.crm.dynamics.com) of the Discovery service.
The rest of this document describes the changes that might be needed to use the Web API
 
## Authentication
The Discovery Service Web API supports authentication with OAuth 2.0 access tokens. 
If your code uses WS-Trust SAML tokens, you will need to change code to acquire an OAuth 2.0 token from Azure AD, and pass it to the Discovery Service Web API call.
 
## OData API calls
The calls below are supported by the Web API. These follow the OData v4 standard and the Instances API replaces both RetrieveOrganizations and RetrieveOrganization based on the desired scenario and returns the same data.

-    Get all instances for the user in all regions.
```http  
GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances
```  
-    Get all instances for the user in a specific region.
```http  
GET  https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances(Region={region})
```
Response
```javascript 
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

-    Get a single instance by id
```http  
GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances(<guid>)
```  
-    Get a single instance by unique name
```http  
GET https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances(UniqueName='myorg')  
```  

Response
```javascript 
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

## Mapping of fields
The fields from the Organization Service SDK discovery APIs can be mapped as below to the Web API endpoint response properties. These are applicable to all above calls.

Organization Service response field |	Discovery Web API response field
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
The Organization Service SDK call GetUserIdByExternalId is not supported in the Web API.

## See Also
[Discovery Services](/powerapps/developer/common-data-service/discovery-service)

[Use the Common Data Service Web API](/powerapps/developer/common-data-service/webapi/discover-url-organization-web-api)
