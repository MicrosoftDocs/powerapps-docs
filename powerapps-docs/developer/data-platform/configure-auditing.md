---
title: "Configure auditing (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Explains how to configure programatically configure auditing settins for the organization, tables and columns." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 05/10/2022
ms.reviewer: jdaly
ms.topic: overview
author: Bluebear7 # GitHub ID
ms.subservice: dataverse-developer
ms.author: munzinge # MSFT alias of Microsoft employees only
manager: mayadu # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---

# Configure auditing 

Auditing uses settings in the [Organization table](reference/entities/organization.md) as well as settings for each table and column to determine what kind of audit history data to capture. 

Anyone can read this data, but you must have the System Administrator or System Customizer roles to change these settings.

## Configure organization settings

The [Organization table](reference/entities/organization.md) contains properties that control how auditing is enabled for an environment. The organization table contains a single row. The `organizationid` column value is the primary key. You can get this value by querying the row directly or you may already have it by previously executing the `WhoAmI` message. The response from the WhoAmI message contains the `OrganizationId` value.

The following table describes the organization table columns that control auditing behavior.


|Schema Name<br />Logical Name |Type  |Description  |
|---------|---------|---------|
|`IsAuditEnabled`<br />`isauditenabled`|Boolean|Whether auditing is enabled for the environment.|
|`AuditRetentionPeriodV2`<br />`auditretentionperiodv2`|Integer|The number of days to retain audit log records. The default value is 30. Valid values are between 1 and 365,000 days (~1000 years) or if the value is set to -1, the records will be retained forever.<br />More information: [Microsoft Power Platform admin: Start/stop auditing and set retention policy](/power-platform/admin/audit-data-user-activity#startstop-auditing-and-set-retention-policy)|
|`IsUserAccessAuditEnabled`<br />`isuseraccessauditenabled`|Boolean|Whether user access logging is enabled. Auditing for the environment must also be enabled for user access logging to be enabled.<br />More information: [Microsoft Power Platform admin: TODO topic about User Access Auditing](/power-platform/admin/audit-data-user-activity)|
|`UserAccessAuditingInterval`<br />`useraccessauditinginterval`|Integer|The interval how often user access is logged in hours. Default value is 4.|

You can retrieve these values using the following queries:

# [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/organizations(<organizationid value>)?$select=isauditenabled,auditretentionperiodv2,isuseraccessauditenabled,useraccessauditinginterval
```

**Response**

```http
HTTP/1.1 200 OK

{
    "@odata.context": "https://crmue.api.crm.dynamics.com/api/data/v9.2/$metadata#organizations(isauditenabled,auditretentionperiodv2,isuseraccessauditenabled,useraccessauditinginterval)/$entity",
    "@odata.etag": "W/\"67037845\"",
    "isauditenabled": true,
    "auditretentionperiodv2": 30,
    "isuseraccessauditenabled": true,
    "useraccessauditinginterval": 4,
    "organizationid": "<organizationid value>"
}
```
More information: [Retrieve a table row using the Web API](webapi/retrieve-entity-using-web-api.md)

# [Organization Service](#tab/orgservice)

```csharp
using (var svc = new CrmServiceClient(conn))
{
    WhoAmIResponse whoAmIResponse = (WhoAmIResponse)svc.Execute(new WhoAmIRequest());

    Entity organization = svc.Retrieve(
        entityName: "organization",
        id: whoAmIResponse.OrganizationId,
        columnSet: new ColumnSet(
        "isauditenabled",
        "auditretentionperiodv2",
        "isuseraccessauditenabled",
        "useraccessauditinginterval"
        )
      );

    Console.WriteLine($"isauditenabled: {organization["isauditenabled"]}");
    Console.WriteLine($"auditretentionperiodv2: {organization["auditretentionperiodv2"]}");
    Console.WriteLine($"isuseraccessauditenabled: {organization["isuseraccessauditenabled"]}");
    Console.WriteLine($"useraccessauditinginterval: {organization["useraccessauditinginterval"]}");
}
```

More information:

- <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient?displayProperty=fullName>
- <xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest?displayProperty=fullName>
- <xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse?displayProperty=fullName>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve?displayProperty=fullName>

---

Update the column properties in the table above to control how auditing works for the environment.

You can set these column values using Web API or Organization Service. More information: 
- [Update and delete table rows using the Web API](webapi/update-delete-entities-using-web-api.md)
- [Update and delete table rows using the Organization Service](org-service/entity-operations-update-delete.md)

## Configure tables and columns

Tables and columns each have a *managed property* named `IsAuditEnabled` that controls whether they are enabled for auditing.

|Item |Web API | Organization Service|
|---------|---------|---------|
|Table|<xref:Microsoft.Dynamics.CRM.EntityMetadata>.`IsAuditEnabled`|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled>|
|Column|<xref:Microsoft.Dynamics.CRM.AttributeMetadata>.`IsAuditEnabled`|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsAuditEnabled>|

The `IsAuditEnabled` property is a managed property that is defined with the following types:

|Web API  |Organization Service|
|---------|---------|
|<xref:Microsoft.Dynamics.CRM.BooleanManagedProperty?displayProperty=fullName>|<xref:Microsoft.Xrm.Sdk.BooleanManagedProperty?displayProperty=fullName>|

A managed property has two important properties:

|Property|Description|
|---------|---------|
|`Value`|Determines whether the setting is enabled.|
|`CanBeChanged` |Determines whether the `Value` setting can be changed after the table or column is included in a managed solution.|

The publisher of the solution that adds a table  may block people installing their managed solution from enabling auditing. Some Dataverse system tables cannot be enabled or disabled for auditing because the `CanBeChanged` property is set to `false`. More information: [Managed properties](/power-platform/alm/managed-properties-alm)




