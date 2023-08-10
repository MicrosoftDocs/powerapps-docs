---
title: Do not use the OData v2.0 endpoint
description: Learn about the requirement to upgrade your code to use the Web API OData v4.0 endpoint rather than the deprecated OData v2.0 endpoint.
suite: powerapps
author: divkamath
ms.author: dikamath
ms.date: 04/12/2023
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
ms.custom: bap-template
---
# Do not use the OData v2.0 endpoint

**Category**: Supportability

**Impact potential**: High

## Symptoms

There are no immediate symptoms, but code that uses this endpoint will stop working when the deprecated endpoint is removed.

The original removal date was November 11, 2022. It was extended to April 30, 2023. We decided not to remove the service on April 30, 2023, to give people more time to transition their code to use the Web API. If you're still using this endpoint, you must prioritize transitioning your code to use the Web API so that you're prepared when the final removal date is announced. More information: [OData v2.0 Service removal date announcement](https://aka.ms/DataverseODataV2EndpointRemoval).

## Guidance

You should change any code that depends on the Organization Data Service (OData v2.0) to use the Dataverse Web API (OData v4.0) endpoint instead.

For model-driven apps, you should use the [Xrm.WebApi (client API reference)](../../clientapi/reference/xrm-webapi.md), which provides access to the Dataverse Web API for client-side extensions that use JavaScript web resources.

## Problematic patterns

The Organization Data Service uses this endpoint: `/XRMServices/2011/OrganizationData.svc`. You should look for any active code that uses this endpoint.

The Dynamics CRM SDK provided an example JavaScript library as a JavaScript web resource named `sample_/Scripts/SDK.REST.js`, which can be found [here](/previous-versions/dynamicscrm-2015/developers-guide/gg334427(v=crm.7)#sample_scriptssdkrestjs). The [Xrm.WebApi (client API reference)](../../clientapi/reference/xrm-webapi.md) provides similar functions to create, update, delete, and retrieve records.

PowerShell scripts that use [Invoke-WebRequest](/powershell/module/microsoft.powershell.utility/invoke-webrequest) also sometimes use the Organization Data Service endpoint.

## Additional information

The Organization Data Service is an OData v2.0 endpoint that was introduced with Dynamics CRM 2011. It was deprecated with Dynamics 365 Customer Engagement v8.0. Also known as the *OData endpoint* or *REST endpoint* when it was released, this endpoint only supports create, retrieve, update, and delete operations on tables.

Both the Dataverse Web API and Organization Data service are OData endpoints, but there are differences in how they are implemented. Do not expect that existing code will work with only minor changes.

Some of the major differences are described in the sections that follow.

### Resource names

Web API resource names for tables are based on the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.EntitySetName>. Organization Data Service names had `Set` appended to the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SchemaName>.

|Web API|Organization Data Service|
|---------|---------|
|accounts|AccountSet|
|contacts|ContactSet|
|tasks|TaskSet|

### Column names

Column names in the Web API are all lowercase and use the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName>. In the Organization Data Service, column names use the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName>.

### HTTP methods

The Organization Data Service uses `MERGE` or `PUT` rather than `PATCH` to update a record.

### Data format

The Organization Data Service supports both JSON and ATOM, an XML-based format usually used for RSS feeds. The Web API only supports JSON.

### Limits on number of records returned

The Organization Data Service will only return 50 records at a time and doesn't provide a way to specify max page size.

The Web API allows you to set a max page size and will return up to 5000 records. More information: [Page results](../../../data-platform/webapi/query-data-web-api.md#page-results)

### Legacy documentation

Organization Data Service documentation: [Microsoft Dynamics 2015 SDK: Use the OData endpoint with web resources](/previous-versions/dynamicscrm-2015/developers-guide/gg334279(v=crm.7)).

The following table connects related areas for the Organization Data Service and the Web API:


|Organization Data Service|Web API|
|---------|---------|
|[Query Microsoft Dynamics CRM 2015 data using the OData endpoint](/previous-versions/dynamicscrm-2015/developers-guide/gg334767(v=crm.7))<br />[OData system query options using the OData endpoint](/previous-versions/dynamicscrm-2015/developers-guide/gg309461(v=crm.7))|[Query data ](../../../data-platform/webapi/query-data-web-api.md)<br />[Web API properties](../../../data-platform/webapi/web-api-properties.md)|
|[Creating records](/previous-versions/dynamicscrm-2015/developers-guide/gg328090(v=crm.7)#creating-records)|[Create a table row](../../../data-platform/webapi/create-entity-web-api.md)|
|[Retrieving records](/previous-versions/dynamicscrm-2015/developers-guide/gg328090(v=crm.7)#retrieving-records)|[Retrieve a table row](../../../data-platform/webapi/retrieve-entity-using-web-api.md)|
|[Updating records](/previous-versions/dynamicscrm-2015/developers-guide/gg328090(v=crm.7)#updating-records)|[Basic update](../../../data-platform/webapi/update-delete-entities-using-web-api.md#basic-update)|
|[Deleting records](/previous-versions/dynamicscrm-2015/developers-guide/gg328090(v=crm.7)#deleting-records)|[Basic delete](../../../data-platform/webapi/update-delete-entities-using-web-api.md#basic-delete)|
|[Using Deep insert](/previous-versions/dynamicscrm-2015/developers-guide/gg309638(v=crm.7)#using-deep-insert)|[Create related table rows in one operation](../../../data-platform/webapi/create-entity-web-api.md#create-related-table-rows-in-one-operation)|
|[Updating individual properties](/previous-versions/dynamicscrm-2015/developers-guide/gg309638(v=crm.7)#updating-individual-properties)|[Update a single property value](../../../data-platform/webapi/update-delete-entities-using-web-api.md#update-a-single-property-value)|
|[Associating and disassociating records](/previous-versions/dynamicscrm-2015/developers-guide/gg309638(v=crm.7)#associating-and-disassociating-records)|[Associate and disassociate table rows](../../../data-platform/webapi/associate-disassociate-entities-using-web-api.md)|
|[OData endpoint HTTP status codes](/previous-versions/dynamicscrm-2015/developers-guide/gg334391(v=crm.7))|[Identify status codes](../../../data-platform/webapi/compose-http-requests-handle-errors.md#identify-status-codes)|

## Examples

This section highlights the differences between using the Organization Data Service and the Web API.

The Organization Data Service only supports create, retrieve, update, and delete operations on tables. The following examples illustrate the differences between the services to help you migrate to the Web API.

### Query records

These examples show the differences between the Organization Data Service and the Web API when you query records.

#### [Organization Data Service](#tab/odatav2)

The Organization Data Service has no way to manage paging other than using `$top `and `$skip`. The maximum page size is 50 records.

**Request:**

```http
GET  [Organization URI]/XRMServices/2011/OrganizationData.svc/AccountSet?$select=OwnershipCode,PrimaryContactId,OpenDeals_Date,Telephone1,NumberOfEmployees,Name,AccountNumber,DoNotPhone,IndustryCode&$filter=PrimaryContactId/Id ne null&$top=2 HTTP/1.1
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
Cache-Control: no-cache
Allow: OPTIONS,GET,HEAD,POST
Content-Type: application/json;charset=utf-8

{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": " [Organization URI]/xrmservices/2011/OrganizationData.svc/AccountSet(guid'7a4814f9-b0b8-ea11-a812-000d3a122b89')",
          "type": "Microsoft.Crm.Sdk.Data.Services.Account"
        },
        "OwnershipCode": {
          "__metadata": {
            "type": "Microsoft.Crm.Sdk.Data.Services.OptionSetValue"
          },
          "Value": 2
        },
        "PrimaryContactId": {
          "__metadata": {
            "type": "Microsoft.Crm.Sdk.Data.Services.EntityReference"
          },
          "Id": "dff27d1f-a61b-4bfe-a203-b2e5a36cda0e",
          "LogicalName": "contact",
          "Name": "Sam Smith",
          "RowVersion": null
        },
        "OpenDeals_Date": "/Date(1663715691000)/",
        "Telephone1": "555-1234",
        "NumberOfEmployees": 500,
        "Name": "Contoso, Ltd. (sample)",
        "AccountNumber": "1111",
        "DoNotPhone": false,
        "IndustryCode": {
          "__metadata": {
            "type": "Microsoft.Crm.Sdk.Data.Services.OptionSetValue"
          },
          "Value": 7
        }
      },
      {
        "__metadata": {
          "uri": " [Organization URI]/xrmservices/2011/OrganizationData.svc/AccountSet(guid'fed58509-4af3-ec11-bb3d-000d3a1a51c1')",
          "type": "Microsoft.Crm.Sdk.Data.Services.Account"
        },
        "OwnershipCode": {
          "__metadata": {
            "type": "Microsoft.Crm.Sdk.Data.Services.OptionSetValue"
          },
          "Value": null
        },
        "PrimaryContactId": {
          "__metadata": {
            "type": "Microsoft.Crm.Sdk.Data.Services.EntityReference"
          },
          "Id": "ffd58509-4af3-ec11-bb3d-000d3a1a51c1",
          "LogicalName": "contact",
          "Name": "Susie Curtis",
          "RowVersion": null
        },
        "OpenDeals_Date": "/Date(1663715691000)/",
        "Telephone1": null,
        "NumberOfEmployees": null,
        "Name": "Fourth Coffee",
        "AccountNumber": null,
        "DoNotPhone": false,
        "IndustryCode": {
          "__metadata": {
            "type": "Microsoft.Crm.Sdk.Data.Services.OptionSetValue"
          },
          "Value": null
        }
      }
    ]
  }
}
```

When more than 50 records are returned, use the `__next` property to access the next page.

```json
"__next": "https://[Organization URI]/XRMServices/2011/OrganizationData.svc/AccountSet?$select=OwnershipCode,PrimaryContactId,OpenDeals_Date,Telephone1,NumberOfEmployees,Name,AccountNumber,DoNotPhone,IndustryCode&$filter=PrimaryContactId/Id ne null&$skiptoken=1,'accountid','%7B22153355-851D-ED11-B83E-000D3A572421%7D','%7B7A4814F9-B0B8-EA11-A812-000D3A122B89%7D'"
```

#### [Web API](#tab/webapi)

The Web API `Prefer: odata.maxpagesize` request header gives you explicit control over paging.

**Request:**

```http
GET  [Organization URI]/api/data/v9.2/accounts?$select=ownershipcode,_primarycontactid_value,opendeals_date,telephone1,numberofemployees,name,accountnumber,donotphone,industrycode&$filter=_primarycontactid_value ne null&$count=true HTTP/1.1
Prefer: odata.include-annotations="*"
Prefer: odata.maxpagesize=2
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"
Preference-Applied: odata.maxpagesize=2

{
  "@odata.context": " [Organization URI]/api/data/v9.2/$metadata#accounts(ownershipcode,_primarycontactid_value,opendeals_date,telephone1,numberofemployees,name,accountnumber,donotphone,industrycode)",
  "@odata.count": 37,
  "@Microsoft.Dynamics.CRM.totalrecordcount": 37,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "73916662",
  "value": [
    {
      "@odata.etag": "W/\"73692809\"",
      "ownershipcode@OData.Community.Display.V1.FormattedValue": "Private",
      "ownershipcode": 2,
      "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Sam Smith",
      "_primarycontactid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "primarycontactid",
      "_primarycontactid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "contact",
      "_primarycontactid_value": "dff27d1f-a61b-4bfe-a203-b2e5a36cda0e",
      "opendeals_date@OData.Community.Display.V1.FormattedValue": "9/20/2022 4:14 PM",
      "opendeals_date": "2022-09-20T23:14:51Z",
      "telephone1": "555-1234",
      "numberofemployees@OData.Community.Display.V1.FormattedValue": "500",
      "numberofemployees": 500,
      "name": "Contoso, Ltd. (sample)",
      "accountnumber": "1111",
      "donotphone@OData.Community.Display.V1.FormattedValue": "Allow",
      "donotphone": false,
      "industrycode@OData.Community.Display.V1.FormattedValue": "Consulting",
      "industrycode": 7,
      "accountid": "7a4814f9-b0b8-ea11-a812-000d3a122b89"
    },
    {
      "@odata.etag": "W/\"68958376\"",
      "ownershipcode": null,
      "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Susie Curtis",
      "_primarycontactid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "primarycontactid",
      "_primarycontactid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "contact",
      "_primarycontactid_value": "ffd58509-4af3-ec11-bb3d-000d3a1a51c1",
      "opendeals_date@OData.Community.Display.V1.FormattedValue": "9/20/2022 4:14 PM",
      "opendeals_date": "2022-09-20T23:14:51Z",
      "telephone1": null,
      "numberofemployees": null,
      "name": "Fourth Coffee",
      "accountnumber": null,
      "donotphone@OData.Community.Display.V1.FormattedValue": "Allow",
      "donotphone": false,
      "industrycode": null,
      "accountid": "fed58509-4af3-ec11-bb3d-000d3a1a51c1"
    }
  ],
  "@odata.nextLink": " [Organization URI]/api/data/v9.2/accounts?$select=ownershipcode,_primarycontactid_value,opendeals_date,telephone1,numberofemployees,name,accountnumber,donotphone,industrycode&$filter=_primarycontactid_value%20ne%20null&$count=true&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257bFED58509-4AF3-EC11-BB3D-000D3A1A51C1%257d%2522%2520first%253d%2522%257b7A4814F9-B0B8-EA11-A812-000D3A122B89%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

Use the `@odata.nextLink` property to get a URL for the next page.

--- 


### Create records

These examples show the differences between the Organization Data Service and the Web API when you create records.

#### [Organization Data Service](#tab/odatav2)

**Request:**

```http
POST [Organization URI]/XRMServices/2011/OrganizationData.svc/AccountSet HTTP/1.1
Accept: application/json
Content-Type: application/json

{
  "OwnershipCode": {
    "Value": 2
  },
  "PrimaryContactId": {
    "Id": "dff27d1f-a61b-4bfe-a203-b2e5a36cda0e",
    "LogicalName": "contact"
  },
  "OpenDeals_Date": "12/25/2022",
  "CustomerSizeCode": {
    "Value": 1
  },
  "Telephone1": "555-1234",
  "NumberOfEmployees": 500,
  "Name": "Contoso, Ltd. (sample)",
  "AccountNumber": "12225",
  "DoNotPhone": true,
  "IndustryCode": {
    "Value": 7
  }
}
```

**Response:**

With the Organization Data Service, all properties are returned when a record is created.

```http
HTTP/1.1 201 Created
Content-Type: application/json;charset=utf-8
REQ_ID: a0c614be-50be-4c1e-9413-1c7ba459c5c9

{
  "d": {
    "__metadata": {
      "uri": "[Organization URI]/xrmservices/2011/OrganizationData.svc/AccountSet(guid'57d4d1af-7b38-ed11-9db0-002248296d7e')",
      "type": "Microsoft.Crm.Sdk.Data.Services.Account"
    },
    "AccountId": "57d4d1af-7b38-ed11-9db0-002248296d7e",

    <All properties are returned. Removed for brevity>

  }
}

```

#### [Web API](#tab/webapi)

The following example uses the `Prefer: return=representation` request header. This header defines a behavior similar to the Organization Data Service behavior of returning `201 Created` with the columns defined by the `$select` query option. Without it, the Web API returns `201 No Content` and the ID of the record that's created is included in the URL value of the `OData-EntityId` response header.

**Request:**

```http
POST  [Organization URI]/api/data/v9.2/accounts?$select=ownershipcode,_primarycontactid_value,opendeals_date,customersizecode,telephone1,numberofemployees,name,accountnumber,donotphone,industrycode HTTP/1.1
Prefer: odata.include-annotations="*"
Prefer: return=representation
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json

{
"ownershipcode": 2,
"primarycontactid@odata.bind":"/contacts(dff27d1f-a61b-4bfe-a203-b2e5a36cda0e)",
"opendeals_date": "2022-09-21T00:00:00Z",
"customersizecode": 1,
"telephone1":"555-1234",
"numberofemployees": 500,
"name":"Contoso, Ltd. (sample)",
"accountnumber": "12227",
"donotphone": true,
"industrycode": 7
}
```

**Response:**

```http
HTTP/1.1 201 Created
Content-Type: application/json; odata.metadata=minimal
Preference-Applied: return=representation
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": " [Organization URI]/api/data/v9.2/$metadata#accounts(ownershipcode,_primarycontactid_value,opendeals_date,customersizecode,telephone1,numberofemployees,name,accountnumber,donotphone,industrycode)/$entity",
  "@odata.etag": "W/\"73921446\"",
  "ownershipcode@OData.Community.Display.V1.FormattedValue": "Private",
  "ownershipcode": 2,
  "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Sam Smith",
  "_primarycontactid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "primarycontactid",
  "_primarycontactid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "contact",
  "_primarycontactid_value": "dff27d1f-a61b-4bfe-a203-b2e5a36cda0e",
  "opendeals_date@OData.Community.Display.V1.FormattedValue": "9/20/2022 5:52 PM",
  "opendeals_date": "2022-09-21T00:52:24Z",
  "customersizecode@OData.Community.Display.V1.FormattedValue": "Default Value",
  "customersizecode": 1,
  "telephone1": "555-1234",
  "numberofemployees@OData.Community.Display.V1.FormattedValue": "500",
  "numberofemployees": 500,
  "name": "Contoso, Ltd. (sample)",
  "accountnumber": "12227",
  "donotphone@OData.Community.Display.V1.FormattedValue": "Do Not Allow",
  "donotphone": true,
  "industrycode@OData.Community.Display.V1.FormattedValue": "Consulting",
  "industrycode": 7,
  "accountid": "b68d56a6-4739-ed11-9db0-002248296d7e"
}

```

Without the `Prefer: return=representation` request header, the response is like this:

**Response:**

```http
HTTP/1.1 204 No Content
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
OData-EntityId: https://[Organization URI]/api/data/v9.2/accounts(b68d56a6-4739-ed11-9db0-002248296d7e)
```

--- 

### Retrieve records

These examples show the differences between the Organization Data Service and the Web API when you retrieve records.

#### [Organization Data Service](#tab/odatav2)

**Request:**

```http
GET https://[Organization URI]/XRMServices/2011/OrganizationData.svc/AccountSet(guid'b68d56a6-4739-ed11-9db0-002248296d7e')?$select=OwnershipCode,PrimaryContactId,OpenDeals_Date,Telephone1,NumberOfEmployees,Name,AccountNumber,DoNotPhone,IndustryCode HTTP/1.1
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK

{
  "d": {
    "__metadata": {
      "uri": "https://[Organization URI]/xrmservices/2011/OrganizationData.svc/AccountSet(guid'b68d56a6-4739-ed11-9db0-002248296d7e')",
      "type": "Microsoft.Crm.Sdk.Data.Services.Account"
    },
    "OwnershipCode": {
      "__metadata": {
        "type": "Microsoft.Crm.Sdk.Data.Services.OptionSetValue"
      },
      "Value": 2
    },
    "PrimaryContactId": {
      "__metadata": {
        "type": "Microsoft.Crm.Sdk.Data.Services.EntityReference"
      },
      "Id": "dff27d1f-a61b-4bfe-a203-b2e5a36cda0e",
      "LogicalName": "contact",
      "Name": "Sam Smith",
      "RowVersion": null
    },
    "OpenDeals_Date": "/Date(1663784098000)/",
    "Telephone1": "555-1234",
    "NumberOfEmployees": 500,
    "Name": "Contoso, Ltd. (sample)",
    "AccountNumber": "12227",
    "DoNotPhone": true,
    "IndustryCode": {
      "__metadata": {
        "type": "Microsoft.Crm.Sdk.Data.Services.OptionSetValue"
      },
      "Value": 7
    }
  }
}

```

#### [Web API](#tab/webapi)

**Request:**

```http
GET https://[Organization URI]/api/data/v9.2/accounts(b68d56a6-4739-ed11-9db0-002248296d7e)?$select=ownershipcode,_primarycontactid_value,opendeals_date,customersizecode,telephone1,numberofemployees,name,accountnumber,donotphone,industrycode HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
ETag: W/"73921464"
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "https://[Organization URI]/api/data/v9.2/$metadata#accounts(ownershipcode,_primarycontactid_value,opendeals_date,customersizecode,telephone1,numberofemployees,name,accountnumber,donotphone,industrycode)/$entity",
  "@odata.etag": "W/\"73921464\"",
  "ownershipcode@OData.Community.Display.V1.FormattedValue": "Private",
  "ownershipcode": 2,
  "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Sam Smith",
  "_primarycontactid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "primarycontactid",
  "_primarycontactid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "contact",
  "_primarycontactid_value": "dff27d1f-a61b-4bfe-a203-b2e5a36cda0e",
  "opendeals_date@OData.Community.Display.V1.FormattedValue": "9/21/2022 11:14 AM",
  "opendeals_date": "2022-09-21T18:14:58Z",
  "customersizecode@OData.Community.Display.V1.FormattedValue": "Default Value",
  "customersizecode": 1,
  "telephone1": "555-1234",
  "numberofemployees@OData.Community.Display.V1.FormattedValue": "500",
  "numberofemployees": 500,
  "name": "Contoso, Ltd. (sample)",
  "accountnumber": "12227",
  "donotphone@OData.Community.Display.V1.FormattedValue": "Do Not Allow",
  "donotphone": true,
  "industrycode@OData.Community.Display.V1.FormattedValue": "Consulting",
  "industrycode": 7,
  "accountid": "b68d56a6-4739-ed11-9db0-002248296d7e"
}

```

--- 

### Update records

These examples show the differences between the Organization Data Service and the Web API when you update records.

#### [Organization Data Service](#tab/odatav2)

The Organization Data Service requires the `X-HTTP-Method: MERGE` request header to be applied with a `POST` request.

**Request:**

```http
POST https://[Organization URI]/XRMServices/2011/OrganizationData.svc/AccountSet(guid'b68d56a6-4739-ed11-9db0-002248296d7e') HTTP/1.1
Accept: application/json
X-HTTP-Method: MERGE
Content-Type: application/json

{
  "OwnershipCode": {
    "Value": 3
  },
  "PrimaryContactId": {
    "Id": "6db0be2e-d01c-ed11-b83e-000d3a572421"
  },
  "OpenDeals_Date": "12/26/2022",
  "Telephone1": "555-1235",
  "NumberOfEmployees": 501,
  "Name": "Contoso, Ltd.",
  "AccountNumber": "12228",
  "DoNotPhone": false,
  "IndustryCode": {
    "Value": 6
  }
}
```

**Response:**

```http
HTTP/1.1 204 No Content

```

#### [Web API](#tab/webapi)

**Request:**

```http
PATCH https://[Organization URI]/api/data/v9.2/accounts(b68d56a6-4739-ed11-9db0-002248296d7e) HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json

{
  "ownershipcode": 3,
  "primarycontactid@odata.bind": "/contacts(6db0be2e-d01c-ed11-b83e-000d3a572421)",
  "opendeals_date": "2022-12-26T00:00:00Z",
  "telephone1": "555-1235",
  "numberofemployees": 501,
  "name": "Contoso, Ltd.",
  "accountnumber": "12229",
  "donotphone": false,
  "industrycode": 6
}

```

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: https://[Organization URI]/api/data/v9.2/accounts(b68d56a6-4739-ed11-9db0-002248296d7e)
```

--- 

### Delete records

These examples show the differences between the Organization Data Service and the Web API when you delete records.

#### [Organization Data Service](#tab/odatav2)

**Request:**

```http
DELETE https://[Organization URI]/XRMServices/2011/OrganizationData.svc/AccountSet(guid'b68d56a6-4739-ed11-9db0-002248296d7e') HTTP/1.1
Accept: application/json
```

**Response:**

```http
HTTP/1.1 204 No Content
```

#### [Web API](#tab/webapi)

**Request:**

```http
DELETE https://[Organization URI]/api/data/v9.2/accounts(b68d56a6-4739-ed11-9db0-002248296d7e) HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

--- 

## See Also

[How to use Application Insights to identify usage of the OrganizationData.svc endpoint which is planned for retirement in November 2022 (Community Forum)](https://community.dynamics.com/forums/thread/details/?threadid=b43553cb-63d8-46f6-bee6-362ad0955e50)   
[How to use Solution Checker to identify usage of the OrganizationData.svc endpoint which is planned for retirement in November 2022 (Community Forum)](https://community.dynamics.com/forums/thread/details/?threadid=1156d54f-b665-4aac-b35a-644ed27d399b)   
[Use the Microsoft Dataverse Web API](../../../data-platform/webapi/overview.md)
