---
title: "Add and remove sample data (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to install or uninstall sample data using the Web API or Organization service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/26/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Add and remove sample data

You can install and uninstall sample data programmatically for an organization using the `InstallSampleData` and  `UninstallSampleData` messages:

|Web API Action |Organization Service Class|
|--|--|
|<xref href="Microsoft.Dynamics.CRM.InstallSampleData?text=InstallSampleData Action" /> |<xref:Microsoft.Crm.Sdk.Messages.InstallSampleDataRequest>|
|<xref href="Microsoft.Dynamics.CRM.UninstallSampleData?text=UninstallSampleData Action" />|<xref:Microsoft.Crm.Sdk.Messages.UninstallSampleDataRequest>|

## Using the Web API

Install sample data using the <xref href="Microsoft.Dynamics.CRM.InstallSampleData?text=InstallSampleData Action" />.

### Request

```http
POST [Organization URI]/api/data/v9.0/InstallSampleData HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
```
### Response

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

Uninstall sample data using the <xref href="Microsoft.Dynamics.CRM.UninstallSampleData?text=UninstallSampleData Action" />.

### Request

```http
POST [Organization URI]/api/data/v9.0/UninstallSampleData HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
```
### Response

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

## Using the Organization Service

Install sample data using the <xref:Microsoft.Crm.Sdk.Messages.InstallSampleDataRequest>

```csharp
var request = new InstallSampleDataRequest();
service.Execute(request);
```

Uninstall sample data using the <xref:Microsoft.Crm.Sdk.Messages.UninstallSampleDataRequest>

```csharp
var request = new UninstallSampleDataRequest();
service.Execute(request);
```

> [!NOTE]
> Neither the <xref:Microsoft.Crm.Sdk.Messages.InstallSampleDataResponse> or <xref:Microsoft.Crm.Sdk.Messages.UninstallSampleDataResponse> classes returned by these operations include any properties to examine.

### See Also

[Import data](import-data.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]