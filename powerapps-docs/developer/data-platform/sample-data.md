---
title: "Add and remove sample data (Microsoft Dataverse) | Microsoft Learn" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to install or uninstall sample data using the Web API or SDK for .NET." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 09/28/2022
ms.reviewer: pehecke
ms.topic: how-to
author: JimDaly # GitHub ID
ms.subservice: dataverse-developer
ms.author: jdaly # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---

# Add and remove sample data

> [!NOTE]
> You can add or remove sample data without writing code. More information: [Administrators Guide: Add or remove sample data](/power-platform/admin/add-remove-sample-data)

You install and uninstall sample data programmatically using the `InstallSampleData` and  `UninstallSampleData` messages:

|Web API Action |SDK for .NET Class|
|--|--|
|<xref:Microsoft.Dynamics.CRM.InstallSampleData?text=InstallSampleData Action> |<xref:Microsoft.Crm.Sdk.Messages.InstallSampleDataRequest?text=InstallSampleDataRequest Class>|
|<xref:Microsoft.Dynamics.CRM.UninstallSampleData?text=UninstallSampleData Action>|<xref:Microsoft.Crm.Sdk.Messages.UninstallSampleDataRequest?text=UninstallSampleDataRequest Class>|

## Install sample data

Install a pre-defined set of sample data.

#### [SDK for .NET](#tab/sdk)

Using the <xref:Microsoft.Crm.Sdk.Messages.InstallSampleDataRequest?text=InstallSampleDataRequest Class>.

```csharp
static void InstallSampleData(IOrganizationService service)
{
    var request = new InstallSampleDataRequest();
    service.Execute(request);
}
```

More information:

- [IOrganizationService Interface](org-service/iorganizationservice-interface.md)
- [Use messages with the SDK for .NET](org-service/use-messages.md)

> [!NOTE]
> The <xref:Microsoft.Crm.Sdk.Messages.InstallSampleDataResponse?text=InstallSampleDataResponse Class> returned by this operation doesn't include any properties to examine.

#### [Web API](#tab/webapi)

Using the <xref:Microsoft.Dynamics.CRM.InstallSampleData?text=InstallSampleData Action>.

### Request

```http
POST [Organization URI]/api/data/v9.2/InstallSampleData HTTP/1.1
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

More information: [Use Web API actions](webapi/use-web-api-actions.md)

---

## Uninstall sample data

Remove a pre-defined set of sample data.

#### [SDK for .NET](#tab/sdk)

Using the <xref:Microsoft.Crm.Sdk.Messages.UninstallSampleDataRequest?text=UninstallSampleDataRequest Class>

```csharp
static void UninstallSampleData(IOrganizationService service)
{
    var request = new UninstallSampleDataRequest();
    service.Execute(request);
}
```

More information:

- [IOrganizationService Interface](org-service/iorganizationservice-interface.md)
- [Use messages with the SDK for .NET](org-service/use-messages.md)

> [!NOTE]
> The <xref:Microsoft.Crm.Sdk.Messages.UninstallSampleDataResponse?text=UninstallSampleDataResponse Class> returned by this operation doesn't include any properties to examine.

#### [Web API](#tab/webapi)

Using the <xref:Microsoft.Dynamics.CRM.UninstallSampleData?text=UninstallSampleData Action>.

### Request

```http
POST [Organization URI]/api/data/v9.2/UninstallSampleData HTTP/1.1
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

More information: [Use Web API actions](webapi/use-web-api-actions.md)

---

### See Also

[Administrators Guide: Add or remove sample data](/power-platform/admin/add-remove-sample-data)<br />
[Import data](import-data.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
