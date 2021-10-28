---
title: "Do not use the OData v2.0 endpoint | MicrosoftDocs"
description: "Describes the requirement to upgrade code to use Web API OData v4.0 endpoint rather than the deprecated OData v2.0 endpoint."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: sunilg
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/28/2021
ms.subservice: mda-developer
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Do not use the OData v2.0 endpoint

**Category**: Supportability

**Impact potential**: High

## Symptoms

There are no immediate symptoms, but code using this endpoint will stop working when the deprecated endpoint is removed.

There will be announcements before this endpoint is removed.

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

## See Also

[Use the Microsoft Dataverse Web API](../../../data-platform/webapi/overview.md)