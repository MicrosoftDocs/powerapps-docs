---
title: Web API Functions and Actions Sample
description: This collection of code samples demonstrates how to perform bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API. These samples are implemented using client-side JavaScript and C#.
ms.date: 09/02/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API Functions and Actions Sample

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This group of samples demonstrate how to perform bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API. This sample is implemented as a separate project for the following languages:  
  
- [Functions and Actions Sample (C#)](samples/webapiservice-functions-and-actions.md)
- [Functions and Actions Sample (Client-side JavaScript)](samples/functions-actions-client-side-javascript.md)
  
This article explains the structure and content of the sample at a higher, language-neutral level. Review the linked sample articles above for language-specific implementation details about how to perform the operations described in this article.  
  
<a name="bkmk_demonstrates"></a>  
 
## Demonstrates  

This sample is divided into the following principal sections, containing Web API functions and actions operations that are discussed in greater detail in the associated conceptual articles.  
  
|Article section|Associated article(s)|  
|-------------------|---------------------------|
|[Section 1: Unbound Function WhoAmI](#section-1-unbound-function-whoami)|<xref:Microsoft.Dynamics.CRM.WhoAmI?text=WhoAmI Function><br />[Unbound functions](use-web-api-functions.md#unbound-functions)|
|[Section 2: Unbound Function FormatAddress](#section-2-unbound-function-formataddress)|<xref:Microsoft.Dynamics.CRM.FormatAddress?text=FormatAddress Function><br />[Passing parameters to a function](use-web-api-functions.md#passing-parameters-to-a-function)|
|[Section 3: Unbound Function InitializeFrom](#section-3-unbound-function-initializefrom)|<xref:Microsoft.Dynamics.CRM.InitializeFrom?text=InitializeFrom Function><br />[Create a record from another record](create-entity-web-api.md#create-a-record-from-another-record)<br />[Map table columns](../../../maker/data-platform/map-entity-fields.md)<br />[Customize table and column mappings](../customize-entity-attribute-mappings.md)|
|[Section 4: Unbound Function RetrieveCurrentOrganization](#section-4-unbound-function-retrievecurrentorganization)|<xref:Microsoft.Dynamics.CRM.RetrieveCurrentOrganization?text=RetrieveCurrentOrganization Function><br />|
|[Section 6: Bound Function IsSystemAdmin custom API](#section-6-bound-function-issystemadmin-custom-api)|[Bound Functions](web-api-functions.md#bound-functions)<br />[Use Bound functions](use-web-api-functions.md#bound-functions)<br />[Sample: IsSystemAdmin custom API](../org-service/samples/issystemadmin-customapi-sample-plugin.md)<br />[Create and use custom APIs](../custom-api.md)|
|[Section 7: Unbound Action GrantAccess](#section-7-unbound-action-grantaccess)|<xref:Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action><br />[Sharing and assigning](../security-sharing-assigning.md)<br /><xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function>|
|[Section 8: Bound Actions AddPrivilegesRole](#section-8-bound-action-addprivilegesrole)|[Bound actions](web-api-actions.md#bound-actions)<br />[Use Bound actions](use-web-api-actions.md#bound-actions)<br /><xref:Microsoft.Dynamics.CRM.AddPrivilegesRole?text=AddPrivilegesRole Action><br />[Security Role (Role)  table/entity reference](../reference/entities/role.md)|
|[Section 9: Delete sample records](#section-9-delete-sample-records)|[Basic delete](update-delete-entities-using-web-api.md#basic-delete)<br />[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)|
  
The following sections contain a brief discussion of the Dataverse Web API operations performed, along with the corresponding HTTP messages and associated console output.  

## Section 1: Unbound Function WhoAmI

[WhoAmI Function](xref:Microsoft.Dynamics.CRM.WhoAmI) is a simple and commonly used unbound function.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/WhoAmI HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",
  "BusinessUnitId": "cca3985e-c618-ea11-a811-000d3a33f066",
  "UserId": "2138bd90-ec19-ea11-a811-000d3a334e11",
  "OrganizationId": "f2c9290b-0806-4d48-bf9c-3814d4286755"
}
```

**Console output:**

```
WhoAmI tells us:
WhoAmIResponse.BusinessUnitId:cca3985e-c618-ea11-a811-000d3a33f066
WhoAmIResponse.UserId:2138bd90-ec19-ea11-a811-000d3a334e11
WhoAmIResponse.OrganizationId:f2c9290b-0806-4d48-bf9c-3814d4286755
```

The `BusinessUnitId` value retrieved here will be used in [Section 8: Bound Action AddPrivilegesRole](#section-8-bound-action-addprivilegesrole).

## Section 2: Unbound Function FormatAddress

[FormatAddress function](xref:Microsoft.Dynamics.CRM.FormatAddress) is an unbound function that requires parameters to be set. It returns a string that represents an address according to country/regional format specific requirements.

In this example, the parameters are set using query string parameter values.

1. A request for an address in the United States:

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/FormatAddress(Line1=@p1,City=@p2,StateOrProvince=@p3,PostalCode=@p4,Country=@p5)?@p1='123%20Maple%20St.'&@p2='Seattle'&@p3='WA'&@p4='98007'&@p5='USA' HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.FormatAddressResponse",
   "Address": "123 Maple St.\r\nSeattle, WA 98007\r\nUSA"
   }
   ```

   **Console output:**

   ```
   USA Formatted Address:
   123 Maple St.
   Seattle, WA 98007
   USA
   ```

1. A request for an address in Japan.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/FormatAddress(Line1=@p1,City=@p2,StateOrProvince=@p3,PostalCode=@p4,Country=@p5)?@p1='1-2-3%20Sakura'&@p2='Nagoya'&@p3='Aichi'&@p4='455-2345'&@p5='JAPAN' HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.FormatAddressResponse",
   "Address": "455-2345\r\nAichi\r\nNagoya\r\n1-2-3 Sakura\r\nJAPAN"
   }
   ```

   **Console output:**

   ```
   JAPAN Formatted Address:
   455-2345
   Aichi
   Nagoya
   1-2-3 Sakura
   JAPAN
   ```

## Section 3: Unbound Function InitializeFrom

[InitializeFrom function](xref:Microsoft.Dynamics.CRM.InitializeFrom) is an unbound function that requires parameters. This function returns the data for a new record to create in the context of an existing record. Depending on the configuration data to control what data is copied over, the record data returned includes data copied from the original record.

More information:

- [Create a record from another record](create-entity-web-api.md#create-a-record-from-another-record)
- [Map table columns](../../../maker/data-platform/map-entity-fields.md)
- [Customize table and column mappings](../customize-entity-attribute-mappings.md)

1. Create a record to be the original record:

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/accounts HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "accountcategorycode": 1,
   "address1_addresstypecode": 3,
   "address1_city": "Redmond",
   "address1_country": "USA",
   "address1_line1": "123 Maple St.",
   "address1_name": "Corporate Headquarters",
   "address1_postalcode": "98000",
   "address1_shippingmethodcode": 4,
   "address1_stateorprovince": "WA",
   "address1_telephone1": "555-1234",
   "customertypecode": 3,
   "description": "Contoso is a business consulting company.",
   "emailaddress1": "info@contoso.com",
   "industrycode": 7,
   "name": "Contoso Consulting",
   "numberofemployees": 150,
   "ownershipcode": 2,
   "preferredcontactmethodcode": 2,
   "telephone1": "(425) 555-1234"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/accounts(98d463e4-6d29-ed11-9db1-00224804f8e2)
   ```

1. Use `InitializeFrom` to get the data for a new record from the original record.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/InitializeFrom(EntityMoniker=@p1,TargetEntityName=@p2,TargetFieldType=@p3)?@p1={'@odata.id':'accounts(98d463e4-6d29-ed11-9db1-00224804f8e2)'}&@p2='account'&@p3=Microsoft.Dynamics.CRM.TargetFieldType'ValidForCreate' HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   Preference-Applied: return=representation
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts/$entity",
   "@odata.type": "#Microsoft.Dynamics.CRM.account",
   "parentaccountid@odata.bind": "accounts(98d463e4-6d29-ed11-9db1-00224804f8e2)"
   }
   ```

   **Console output:**

   ```
   New data based on original record:
   {
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts/$entity",
   "@odata.type": "#Microsoft.Dynamics.CRM.account",
   "parentaccountid@odata.bind": "accounts(98d463e4-6d29-ed11-9db1-00224804f8e2)"
   }
   ```

   > [!NOTE]
   > If there are no columns mapped for this relationship, only the minimum column values are included as shown above. In this case, only the `parentaccountid` lookup to associate the new record with the original.

   If all the available columns are mapped for this relationship, the value returned includes more data from the original record, for example:

   ```json
   {
      "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts/$entity",
      "@odata.type": "#Microsoft.Dynamics.CRM.account",
      "territorycode": 1,
      "address2_freighttermscode": 1,
      "address2_shippingmethodcode": 1,
      "address1_telephone1": "555-1234",
      "accountclassificationcode": 1,
      "creditonhold": false,
      "donotbulkemail": false,
      "donotsendmm": false,
      "emailaddress1": "info@contoso.com",
      "address1_line1": "123 Maple St.",
      "customertypecode": 3,
      "ownershipcode": 2,
      "businesstypecode": 1,
      "donotpostalmail": false,
      "donotbulkpostalmail": false,
      "name": "Contoso Consulting",
      "address1_city": "Redmond",
      "description": "Contoso is a business consulting company.",
      "donotemail": false,
      "address2_addresstypecode": 1,
      "donotphone": false,
      "statuscode": 1,
      "address1_name": "Corporate Headquarters",
      "followemail": true,
      "preferredcontactmethodcode": 2,
      "numberofemployees": 150,
      "industrycode": 7,
      "telephone1": "(425) 555-1234",
      "address1_shippingmethodcode": 4,
      "donotfax": false,
      "address1_addresstypecode": 3,
      "customersizecode": 1,
      "marketingonly": false,
      "accountratingcode": 1,
      "shippingmethodcode": 1,
      "address1_country": "USA",
      "participatesinworkflow": false,
      "accountcategorycode": 1,
      "address1_postalcode": "98000",
      "address1_stateorprovince": "WA",
      "parentaccountid@odata.bind": "accounts(fe9873ac-2f1b-ed11-b83e-00224837179f)"
   }     
   ```

1. Create a new record using the data returned with `InitializeFrom`.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/accounts HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts/$entity",
   "@odata.type": "#Microsoft.Dynamics.CRM.account",
   "parentaccountid@odata.bind": "accounts(98d463e4-6d29-ed11-9db1-00224804f8e2)",
   "name": "Contoso Consulting Chicago Branch",
   "address1_city": "Chicago",
   "address1_line1": "456 Elm St.",
   "address1_name": "Chicago Branch Office",
   "address1_postalcode": "60007",
   "address1_stateorprovince": "IL",
   "address1_telephone1": "(312) 555-3456",
   "numberofemployees": 12
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/accounts(9ad463e4-6d29-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   New Record:
   {
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts/$entity",
   "@odata.type": "#Microsoft.Dynamics.CRM.account",
   "parentaccountid@odata.bind": "accounts(98d463e4-6d29-ed11-9db1-00224804f8e2)",
   "name": "Contoso Consulting Chicago Branch",
   "address1_city": "Chicago",
   "address1_line1": "456 Elm St.",
   "address1_name": "Chicago Branch Office",
   "address1_postalcode": "60007",
   "address1_stateorprovince": "IL",
   "address1_telephone1": "(312) 555-3456",
   "numberofemployees": 12
   }
   ```

## Section 4: Unbound Function RetrieveCurrentOrganization

[RetrieveCurrentOrganization function](xref:Microsoft.Dynamics.CRM.RetrieveCurrentOrganization) returns information about the current organization. It requires an [EndpointAccessType enum type](xref:Microsoft.Dynamics.CRM.EndpointAccessType) value as a parameter.

`RetrieveCurrentOrganization` returns a [RetrieveCurrentOrganizationResponse complex type](xref:Microsoft.Dynamics.CRM.RetrieveCurrentOrganizationResponse) which includes a `Detail` property that is an [OrganizationDetail complex type](xref:Microsoft.Dynamics.CRM.OrganizationDetail), which has complex properties that use the [EndpointCollection complex type](xref:Microsoft.Dynamics.CRM.EndpointCollection), [EndpointType enum type](xref:Microsoft.Dynamics.CRM.EndpointType) and [OrganizationState enum type](xref:Microsoft.Dynamics.CRM.OrganizationState)

> [!NOTE]
> Notice how the `AccessType` [EndpointAccessType enum type](xref:Microsoft.Dynamics.CRM.EndpointAccessType) parameter value is passed in the URL. The fully qualified name with the selected member name is required.


**Request:**

```http
GET [Organization Uri]/api/data/v9.2/RetrieveCurrentOrganization(AccessType=@p1)?@p1=Microsoft.Dynamics.CRM.EndpointAccessType'Default' HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveCurrentOrganizationResponse",
  "Detail": {
    "OrganizationId": "f2c9290b-0806-4d48-bf9c-3814d4286755",
    "FriendlyName": "[Organization Name]",
    "OrganizationVersion": "9.2.22074.168",
    "EnvironmentId": "Default-f6976b02-5a42-4e90-ac3d-8bf516ce0859",
    "DatacenterId": "695014e1-bafd-4d7e-9d3d-2261d4aaf780",
    "Geo": "NA",
    "TenantId": "f6976b02-5a42-4e90-ac3d-8bf516ce0859",
    "UrlName": "org619726b5",
    "UniqueName": "org0335df44",
    "State": "Enabled",
    "Endpoints": {
      "Count": 3,
      "IsReadOnly": false,
      "Keys": [
        "WebApplication",
        "OrganizationService",
        "OrganizationDataService"
      ],
      "Values": [
        "[Organization URI]/",
        "[Organization URI]/XRMServices/2011/Organization.svc",
        "[Organization URI]/XRMServices/2011/OrganizationData.svc"
      ]
    }
  }
}
```

**Console output:**

```
Data returned with RetrieveCurrentOrganizationResponse:
{
  "OrganizationId": "f2c9290b-0806-4d48-bf9c-3814d4286755",
  "FriendlyName": "[Organization Name]",
  "OrganizationVersion": "9.2.22074.168",
  "EnvironmentId": "Default-f6976b02-5a42-4e90-ac3d-8bf516ce0859",
  "DatacenterId": "695014e1-bafd-4d7e-9d3d-2261d4aaf780",
  "Geo": "NA",
  "TenantId": "f6976b02-5a42-4e90-ac3d-8bf516ce0859",
  "UrlName": "org619726b5",
  "UniqueName": "org0335df44",
  "Endpoints": {
    "Count": 3,
    "IsReadOnly": false,
    "Keys": [
      "WebApplication",
      "OrganizationService",
      "OrganizationDataService"
    ],
    "Values": [
      "[Organization URI]/",
      "[Organization URI]/XRMServices/2011/Organization.svc",
      "[Organization URI]/XRMServices/2011/OrganizationData.svc"
    ]
  },
  "State": "Enabled"
}
```

## Section 5: Unbound Function RetrieveTotalRecordCount

[RetrieveTotalRecordCount function](xref:Microsoft.Dynamics.CRM.RetrieveTotalRecordCount) returns data on the total number of records for specific entities. The data retrieved is from a snapshot within last 24 hours, so it isn't an exact count at a given moment in time.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/RetrieveTotalRecordCount(EntityNames=@p1)?@p1=["account","contact"] HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveTotalRecordCountResponse",
  "EntityRecordCountCollection": {
    "Count": 2,
    "IsReadOnly": false,
    "Keys": [
      "account",
      "contact"
    ],
    "Values": [
      19,
      3
    ]
  }
}
```

**Console output:**

```
The number of records for each table according to RetrieveTotalRecordCount:
        account:19
        contact:3
```

## Section 6: Bound Function IsSystemAdmin custom API

To demonstrate a bound function, this sample imports a custom message defined within a solution before running this portion of the sample.

The sample uses the `sample_IsSystemAdmin` custom message that is defined using a [custom API](../custom-api.md). You can find details about this custom api here: [Sample: IsSystemAdmin custom API](../org-service/samples/issystemadmin-customapi-sample-plugin.md).

> [!NOTE]
> When using a bound function or action, you must include the fully qualified name, which includes `Microsoft.Dynamics.CRM.`+ &lt;function or action name&gt; in the url.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/systemusers(ce31e691-f559-ec11-8f8f-000d3a308de4)/Microsoft.Dynamics.CRM.sample_IsSystemAdmin HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.sample_IsSystemAdminResponse",
  "HasRole": false
}
```

This sample retrieves 10 user records and test each one to determine whether each user has the System Administrator security role.

**Console output:**

The actual names depend on the people in your environment.

```
Top 10 users and whether they have System Administrator role.
        Gediminas Matulis does not have the System Administrator role.
        Gaby Frost does not have the System Administrator role.
        Henrikas Martinkus does not have the System Administrator role.
        Alain Davignon HAS the System Administrator role.
        Isobel Macintyre HAS the System Administrator role.
        Ale Laukaitiene HAS the System Administrator role.
        Rudabeh Yekta HAS the System Administrator role.
        Grazina Januliene HAS the System Administrator role.
        Pranciskus Sukys HAS the System Administrator role.
        Asha Sawant HAS the System Administrator role.
```

For another example of a bound function, see the use of the [RetrievePrincipalAccess function](xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess) in the next example.

## Section 7: Unbound Action GrantAccess

[GrantAccess action](xref:Microsoft.Dynamics.CRM.GrantAccess) is an unbound action allows people to share specific privileges to other users in their environment.

The sample code demonstrates the following operations:

1. Create a record to share.
1. Find an enabled user other than the current user.
1. Use [RetrievePrincipalAccess function](xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess) to determine what access rights the user has for the record created.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/systemusers(ce31e691-f559-ec11-8f8f-000d3a308de4)/Microsoft.Dynamics.CRM.RetrievePrincipalAccess(Target=@p1)?@p1={'@odata.id':'accounts(659876fd-6d29-ed11-9db1-00224804f8e2)'} HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrievePrincipalAccessResponse",
   "AccessRights": "ShareAccess"
   }
   ```

   **Console output:**

   ```
   Testing user: Gediminas Matulis
   Current users access: ShareAccess
   ```

1. If the user doesn't have <xref:Microsoft.Dynamics.CRM.AccessRights?text=AccessRights>.`DeleteAccess`, grant the user this access using the `GrantAccess` action.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/GrantAccess HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "Target": {
      "accountid": "659876fd-6d29-ed11-9db1-00224804f8e2",
      "@odata.type": "Microsoft.Dynamics.CRM.account"
   },
   "PrincipalAccess": {
      "AccessMask": "DeleteAccess",
      "Principal": {
         "systemuserid": "ce31e691-f559-ec11-8f8f-000d3a308de4",
         "@odata.type": "Microsoft.Dynamics.CRM.systemuser"
      }
    }
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```

1. Once `DeleteAccess` has been granted, the same call to <xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function> shows that they now have access to delete this record:

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/systemusers(ce31e691-f559-ec11-8f8f-000d3a308de4)/Microsoft.Dynamics.CRM.RetrievePrincipalAccess(Target=@p1)?@p1={'@odata.id':'accounts(659876fd-6d29-ed11-9db1-00224804f8e2)'} HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrievePrincipalAccessResponse",
   "AccessRights": "DeleteAccess, ShareAccess"
   }
   ```

   **Console output:**

   ```
   Gediminas Matulis was granted DeleteAccess
   ```

## Section 8: Bound Action AddPrivilegesRole

[AddPrivilegesRole action](xref:Microsoft.Dynamics.CRM.AddPrivilegesRole) is an action bound to the [role entity type](xref:Microsoft.Dynamics.CRM.role). It's the way to add privileges to a security role.

The sample code performs the following operations:

1. Create a security role. The role must be associated with a business unit. The business unit id value was retrieved in [Section 1: Unbound Function WhoAmI](#section-1-unbound-function-whoami).
   
   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/roles HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "businessunitid@odata.bind": "businessunits(cca3985e-c618-ea11-a811-000d3a33f066)",
   "name": "Test Role"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/roles(669876fd-6d29-ed11-9db1-00224804f8e2)
   ```

1. Retrieve the role, expanding the `roleprivileges_association` collection-valued navigation property to include the privileges included with the role.
   
   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/roles(669876fd-6d29-ed11-9db1-00224804f8e2)?$select=roleid&$expand=roleprivileges_association($select=name) HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   ETag: W/"13278232"
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#roles(roleid,roleprivileges_association(name))/$entity",
   "@odata.etag": "W/\"13278232\"",
   "roleid": "669876fd-6d29-ed11-9db1-00224804f8e2",
   "roleprivileges_association": [
      {
         "@odata.etag": "W/\"142279\"",
         "name": "prvReadSharePointData",
         "privilegeid": "fecbd29c-df64-4ede-a611-47226b402c22"
      },
      {
         "@odata.etag": "W/\"142304\"",
         "name": "prvReadSdkMessage",
         "privilegeid": "94c3ac2c-eb23-41cb-a903-4e2e49e910b4"
      },
      {
         "@odata.etag": "W/\"142421\"",
         "name": "prvWriteSharePointData",
         "privilegeid": "cfdd12cf-090b-4599-8302-771962d2350a"
      },
      {
         "@odata.etag": "W/\"142477\"",
         "name": "prvReadSdkMessageProcessingStepImage",
         "privilegeid": "122e085f-8c52-47e8-8415-875dee1c961e"
      },
      {
         "@odata.etag": "W/\"142695\"",
         "name": "prvReadSdkMessageProcessingStep",
         "privilegeid": "db10a828-ec49-4035-8b7e-c58efaf169ec"
      },
      {
         "@odata.etag": "W/\"142713\"",
         "name": "prvReadPluginAssembly",
         "privilegeid": "f5b50296-a212-488a-be92-cbcca8971717"
      },
      {
         "@odata.etag": "W/\"142735\"",
         "name": "prvCreateSharePointData",
         "privilegeid": "5eb85025-363b-46ea-a77e-ce24159cd231"
      },
      {
         "@odata.etag": "W/\"142740\"",
         "name": "prvReadPluginType",
         "privilegeid": "9365005c-4703-473b-8d3c-d073cfd8670c"
      },
      {
         "@odata.etag": "W/\"142761\"",
         "name": "prvReadSharePointDocument",
         "privilegeid": "d71fc8d0-99bc-430e-abd7-d95c64f11e9c"
      }
   ]
   }
   ```

1. Show the number of privileges created by default for the new role.
   
   **Console output:**

   ```
   Number of privileges in new role: 9
         prvReadSharePointData
         prvReadSdkMessage
         prvWriteSharePointData
         prvReadSdkMessageProcessingStepImage
         prvReadSdkMessageProcessingStep
         prvReadPluginAssembly
         prvCreateSharePointData
         prvReadPluginType
         prvReadSharePointDocument
   ```

1. Retrieve the definition of the `prvCreateAccount` and `prvReadAccount` privileges from <xref:Microsoft.Dynamics.CRM.privilege?text=privilege EntityType>.
   
   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/privileges?$select=name&$filter=name eq 'prvCreateAccount' or name eq 'prvReadAccount' HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#privileges(name)",
   "value": [
      {
         "@odata.etag": "W/\"142189\"",
         "name": "prvReadAccount",
         "privilegeid": "886b280c-6396-4d56-a0a3-2c1b0a50ceb0"
      },
      {
         "@odata.etag": "W/\"142359\"",
         "name": "prvCreateAccount",
         "privilegeid": "d26fe964-230b-42dd-ad93-5cc879de411e"
      }
    ]
   }
   ```

1. Prepare a list of <xref:Microsoft.Dynamics.CRM.RolePrivilege?text=RolePrivilege ComplexType> instances for the `prvCreateAccount` and `prvReadAccount` privileges with the `Depth` property set to <xref:Microsoft.Dynamics.CRM.PrivilegeDepth?text=PrivilegeDepth>.'Basic'.
1. Pass the list as the `AddPrivilegesRole.Privileges` parameter.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/roles(669876fd-6d29-ed11-9db1-00224804f8e2)/Microsoft.Dynamics.CRM.AddPrivilegesRole HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "Privileges": [
      {
         "Depth": "Basic",
         "PrivilegeId": "886b280c-6396-4d56-a0a3-2c1b0a50ceb0",
         "BusinessUnitId": "cca3985e-c618-ea11-a811-000d3a33f066",
         "PrivilegeName": "prvReadAccount"
      },
      {
         "Depth": "Basic",
         "PrivilegeId": "d26fe964-230b-42dd-ad93-5cc879de411e",
         "BusinessUnitId": "cca3985e-c618-ea11-a811-000d3a33f066",
         "PrivilegeName": "prvCreateAccount"
      }
    ]
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```

1. Retrieve the privileges associated with the role again to confirm that they have been added.
   
   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/roles(669876fd-6d29-ed11-9db1-00224804f8e2)?$select=roleid&$expand=roleprivileges_association($select=name) HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   ETag: W/"13278248"
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#roles(roleid,roleprivileges_association(name))/$entity",
   "@odata.etag": "W/\"13278248\"",
   "roleid": "669876fd-6d29-ed11-9db1-00224804f8e2",
   "roleprivileges_association": [
      {
         "@odata.etag": "W/\"142189\"",
         "name": "prvReadAccount",
         "privilegeid": "886b280c-6396-4d56-a0a3-2c1b0a50ceb0"
      },
      {
         "@odata.etag": "W/\"142279\"",
         "name": "prvReadSharePointData",
         "privilegeid": "fecbd29c-df64-4ede-a611-47226b402c22"
      },
      {
         "@odata.etag": "W/\"142304\"",
         "name": "prvReadSdkMessage",
         "privilegeid": "94c3ac2c-eb23-41cb-a903-4e2e49e910b4"
      },
      {
         "@odata.etag": "W/\"142359\"",
         "name": "prvCreateAccount",
         "privilegeid": "d26fe964-230b-42dd-ad93-5cc879de411e"
      },
      {
         "@odata.etag": "W/\"142421\"",
         "name": "prvWriteSharePointData",
         "privilegeid": "cfdd12cf-090b-4599-8302-771962d2350a"
      },
      {
         "@odata.etag": "W/\"142477\"",
         "name": "prvReadSdkMessageProcessingStepImage",
         "privilegeid": "122e085f-8c52-47e8-8415-875dee1c961e"
      },
      {
         "@odata.etag": "W/\"142695\"",
         "name": "prvReadSdkMessageProcessingStep",
         "privilegeid": "db10a828-ec49-4035-8b7e-c58efaf169ec"
      },
      {
         "@odata.etag": "W/\"142713\"",
         "name": "prvReadPluginAssembly",
         "privilegeid": "f5b50296-a212-488a-be92-cbcca8971717"
      },
      {
         "@odata.etag": "W/\"142735\"",
         "name": "prvCreateSharePointData",
         "privilegeid": "5eb85025-363b-46ea-a77e-ce24159cd231"
      },
      {
         "@odata.etag": "W/\"142740\"",
         "name": "prvReadPluginType",
         "privilegeid": "9365005c-4703-473b-8d3c-d073cfd8670c"
      },
      {
         "@odata.etag": "W/\"142761\"",
         "name": "prvReadSharePointDocument",
         "privilegeid": "d71fc8d0-99bc-430e-abd7-d95c64f11e9c"
      }
   ]
   }
   ```

   **Console output:**

   ```
   Number of privileges after: 11
         prvReadAccount
         prvReadSharePointData
         prvReadSdkMessage
         prvCreateAccount
         prvWriteSharePointData
         prvReadSdkMessageProcessingStepImage
         prvReadSdkMessageProcessingStep
         prvReadPluginAssembly
         prvCreateSharePointData
         prvReadPluginType
         prvReadSharePointDocument
   ```

## Section 9: Delete sample records

Each record created in this sample was added to a list to be deleted at the end. These records are deleted using a `$batch` request.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/$batch HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

--batch_d6010246-cd97-429f-bc05-cf20054cfe8a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/accounts(98d463e4-6d29-ed11-9db1-00224804f8e2) HTTP/1.1


--batch_d6010246-cd97-429f-bc05-cf20054cfe8a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/accounts(9ad463e4-6d29-ed11-9db1-00224804f8e2) HTTP/1.1


--batch_d6010246-cd97-429f-bc05-cf20054cfe8a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 122

DELETE /api/data/v9.2/solutions(b37bc86a-4c3a-41be-b35d-ddfd129276c5) HTTP/1.1


--batch_d6010246-cd97-429f-bc05-cf20054cfe8a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/accounts(659876fd-6d29-ed11-9db1-00224804f8e2) HTTP/1.1


--batch_d6010246-cd97-429f-bc05-cf20054cfe8a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 118

DELETE /api/data/v9.2/roles(669876fd-6d29-ed11-9db1-00224804f8e2) HTTP/1.1


--batch_d6010246-cd97-429f-bc05-cf20054cfe8a--

```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_cb852192-c300-4ed7-a54f-dc5fc7ee27c3
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_cb852192-c300-4ed7-a54f-dc5fc7ee27c3
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_cb852192-c300-4ed7-a54f-dc5fc7ee27c3
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_cb852192-c300-4ed7-a54f-dc5fc7ee27c3
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_cb852192-c300-4ed7-a54f-dc5fc7ee27c3
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_cb852192-c300-4ed7-a54f-dc5fc7ee27c3--

```

**Console output:**

```
Deleting created records.
```

### See also  

[Use the Dataverse Web API](overview.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Web API Functions and Actions Sample (C#)](samples/webapiservice-functions-and-actions.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
