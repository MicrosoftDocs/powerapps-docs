---
title: "Do not use the OData v2.0 endpoint | MicrosoftDocs"
description: "Describes the requirement to upgrade code to use Web API OData v4.0 endpoint rather than the deprecated OData v2.0 endpoint."
suite: powerapps
author: divka78
ms.author: dikamath
ms.date: 09/19/2022
ms.reviewer: jdaly
ms.topic: article
ms.subservice: mda-developer
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
---
# Do not use the OData v2.0 endpoint

**Category**: Supportability

**Impact potential**: High

## Symptoms

There are no immediate symptoms, but code using this endpoint will stop working when the deprecated endpoint is removed.

We plan to remove this endpoint on November 11, 2022. [OData v2.0 Service removal date announcement](https://aka.ms/DataverseODataV2EndpointRemoval)

## Guidance

You should change any code that depends on the Organization Data Service (OData v2.0) to use the Dataverse Web API (OData v4.0) endpoint instead.

For model-driven apps, you should use the [Xrm.WebApi (Client API reference)](../../clientapi/reference/xrm-webapi.md), which provides access to the Dataverse Web API for client-side extensions using JavaScript web resources.

## Problematic patterns

The Organization Data Service uses this endpoint: `/XRMServices/2011/OrganizationData.svc`. You should look for any active code using this endpoint.

The Dynamics CRM SDK provided an example JavaScript library as a JavaScript Web Resource named `sample_/Scripts/SDK.REST.js`, which can be found [here](/previous-versions/dynamicscrm-2015/developers-guide/gg334427(v=crm.7)#sample_scriptssdkrestjs). The [Xrm.WebApi (Client API reference)](../../clientapi/reference/xrm-webapi.md) provides similar functions to create, update, delete, and retrieve records.

The Organization Data Service endpoint is also sometimes used by PowerShell scripts using [Invoke-WebRequest](/powershell/module/microsoft.powershell.utility/invoke-webrequest).

## Additional information

Organization Data Service is an OData v2.0 endpoint introduced with Dynamics CRM 2011. It was deprecated with Dynamics 365 Customer Engagement v8.0. Also known as the *OData endpoint* or *REST endpoint* when it was released, this endpoint only provides the ability to perform create, retrieve, update, and delete operations on tables.

> [!NOTE]
> Both are OData endpoints, but there are differences in how they are implemented. Do not expect that existing code will work with only minor changes.

Some of the major differences are described below.

### Resource names

Web API resource names for tables are based on the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.EntitySetName>. Organization Data Service names had `Set` appended to the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SchemaName>. For example:

|Web API  |Organization Data Service  |
|---------|---------|
|accounts|AccountSet|
|contacts|ContactSet|
|tasks|TaskSet|

### Column names

Column Names in Web API are all lower case using the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName>. With the Organization Data Service, column names use the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName>.

### HTTP methods

Organization Data Service uses `MERGE` or `PUT` rather than `PATCH`.

### Data format

Organization Data Service supports both JSON and ATOM. ATOM is an XML-based format usually used for RSS feeds. Web API only supports JSON.

### Limits on number of records returned

Organization Data Service will only return 50 records at a time and doesn't provide a way to specify max page size.

Web API allows to set a max page size and will return up to 5000 records. More information: [Limits on number of table rows (entities) returned](../../../data-platform/webapi/query-data-web-api.md#limits-on-number-of-table-rows-entities-returned).

### Legacy documentation

Documentation describing the Organization Data Service is available here: [Microsoft Dynamics 2015 SDK: Use the OData endpoint with web resources](/previous-versions/dynamicscrm-2015/developers-guide/gg334279(v=crm.7)).

The following table connects related areas for the Organization Data Service and the Web API:


|Organization Data Service|Web API|
|---------|---------|
|[Query Microsoft Dynamics CRM 2015 data using the OData endpoint](/previous-versions/dynamicscrm-2015/developers-guide/gg334767(v=crm.7))<br />[OData system query options using the OData endpoint](/previous-versions/dynamicscrm-2015/developers-guide/gg309461(v=crm.7))|[Query data ](../../../data-platform/webapi/query-data-web-api.md)<br /> [Web API Properties](../../../data-platform/webapi/web-api-properties.md)|
|[Creating records](/previous-versions/dynamicscrm-2015/developers-guide/gg328090(v=crm.7)#creating-records)|[Create a table row](../../../data-platform/webapi/create-entity-web-api.md)|
|[Retrieving records](/previous-versions/dynamicscrm-2015/developers-guide/gg328090(v=crm.7)#retrieving-records)|[Retrieve a table row](../../../data-platform/webapi/retrieve-entity-using-web-api.md)|
|[Updating records](/previous-versions/dynamicscrm-2015/developers-guide/gg328090(v=crm.7)#updating-records)|[Basic update](../../../data-platform/webapi/update-delete-entities-using-web-api.md#basic-update)|
|[Deleting records](/previous-versions/dynamicscrm-2015/developers-guide/gg328090(v=crm.7)#deleting-records)|[Basic delete](../../../data-platform/webapi/update-delete-entities-using-web-api.md#basic-delete)|
|[Using Deep insert](/previous-versions/dynamicscrm-2015/developers-guide/gg309638(v=crm.7)#using-deep-insert)|[Create related table rows in one operation](../../../data-platform/webapi/create-entity-web-api.md#create-related-table-rows-in-one-operation)|
|[Updating individual properties](/previous-versions/dynamicscrm-2015/developers-guide/gg309638(v=crm.7)#updating-individual-properties)|[Update a single property value](../../../data-platform/webapi/update-delete-entities-using-web-api.md#update-a-single-property-value)|
|[Associating and disassociating records](/previous-versions/dynamicscrm-2015/developers-guide/gg309638(v=crm.7)#associating-and-disassociating-records)|[Associate and disassociate table rows](../../../data-platform/webapi/associate-disassociate-entities-using-web-api.md)|
|[OData endpoint Http status codes](/previous-versions/dynamicscrm-2015/developers-guide/gg334391(v=crm.7))|[Identify status codes](../../../data-platform/webapi/compose-http-requests-handle-errors.md#identify-status-codes)|

## Examples

This section highlights the differences between using the Organization Data Service and the Web API.

### Create records

These examples show the differences between the Organization Data Service and the Web API when creating records.

#### [Organization Data Service](#tab/odatav2)

**Request**

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
    "LogicalName": "contact",
    "Name": "Sam Smith"
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

**Response**

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
    <All properties are returned>
  }
}

```

#### [Web API](#tab/webapi)

**Request**

```http

```

**Response**

```http


```

--- 

### Retrieve records

These examples show the differences between the Organization Data Service and the Web API when retrieving records.

#### [Organization Data Service](#tab/odatav2)

**Request**

```http

```

**Response**

```http


```

#### [Web API](#tab/webapi)

**Request**

```http

```

**Response**

```http


```

--- 

### Update records

These examples show the differences between the Organization Data Service and the Web API when updating records.

#### [Organization Data Service](#tab/odatav2)

**Request**

```http

```

**Response**

```http


```

#### [Web API](#tab/webapi)

**Request**

```http

```

**Response**

```http


```

--- 

### Delete records

These examples show the differences between the Organization Data Service and the Web API when deleting records.

#### [Organization Data Service](#tab/odatav2)

**Request**

```http

```

**Response**

```http


```

#### [Web API](#tab/webapi)

**Request**

```http

```

**Response**

```http


```

--- 

## See Also

[How to use Application Insights to identify usage of the OrganizationData.svc endpoint which is planned for retirement in November 2022 (Community Forum)](https://community.dynamics.com/365/f/dynamics-365-general-forum/459370/how-to-use-application-insights-to-identify-usage-of-the-organizationdata-svc-endpoint-which-is-planned-for-retirement-in-november-2022)  
[How to use Solution Checker to identify usage of the OrganizationData.svc endpoint which is planned for retirement in November 2022 (Community Forum)](https://community.dynamics.com/365/f/dynamics-365-general-forum/459368/how-to-use-solution-checker-to-identify-usage-of-the-organizationdata-svc-endpoint-which-is-planned-for-retirement-in-november-2022)  
[Use the Microsoft Dataverse Web API](../../../data-platform/webapi/overview.md)
