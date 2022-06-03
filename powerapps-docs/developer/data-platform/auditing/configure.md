---
title: "Configure auditing (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Explains how to configure programatically configure auditing settins for the organization, tables and columns." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 06/03/2022
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

Auditing uses settings in the [Organization table](../reference/entities/organization.md) and definitions of individual tables and columns to determine what kind of audit history data to capture.

Anyone can read this configuration data, but you must have the System Administrator or System Customizer roles to change these settings.

Changes made to audit configuration are included in the auditing history. More information: [Audit change events](retrieve-audit-data.md#audit-change-events)

## Configure organization settings

Four properties in the [Organization table](../reference/entities/organization.md) control how auditing is enabled for an environment. The `organization` table contains a single row. The `organizationid` column is the primary key. You can get the key value by querying the row directly or you may already have it cached by previously executing the `WhoAmI` message. The `WhoAmIResponse.OrganizationId` property returns the primary key value for the single row in the `organization` table.

The following table describes the `organization` table columns that control auditing behavior.

|Schema Name<br />Logical Name<br />Display Name|Type|Description  |
|---------|---------|---------|
|`IsAuditEnabled`<br />`isauditenabled`<br />**Is Auditing Enabled**|Boolean|Whether auditing is enabled for the environment.|
|`AuditRetentionPeriodV2`<br />`auditretentionperiodv2`<br />**Audit Retention Period Settings**|Integer|The number of days to retain audit log records.<br />The default value is 30. Valid values are between 1 and 365,000 days (~1000 years) or if the value is set to -1, the records will be retained forever.<br />More information: [Microsoft Power Platform admin: Start/stop auditing and set retention policy](/power-platform/admin/audit-data-user-activity#startstop-auditing-and-set-retention-policy)|
|`IsUserAccessAuditEnabled`<br />`isuseraccessauditenabled`<br />**Is User Access Auditing Enabled**|Boolean|Whether user access logging is enabled.<br />Auditing for the environment must also be enabled for user access logging to be enabled.<br />More information: [Microsoft Power Platform admin: Audit data and user activity for security and compliance](/power-platform/admin/audit-data-user-activity)|
|`UserAccessAuditingInterval`<br />`useraccessauditinginterval`<br />**User Authentication Auditing Interval**|Integer|The interval how often user access is logged in hours. Default value is 4.|

### Retrieve organization settings

You can retrieve these values using the following queries:

# [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/organizations?$select=
isauditenabled,
auditretentionperiodv2,
isuseraccessauditenabled,
useraccessauditinginterval HTTP/1.1

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
```

**Response**

```http
HTTP/1.1 200 OK

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#organizations(isauditenabled,auditretentionperiodv2,isuseraccessauditenabled,useraccessauditinginterval)",
    "value": [
        {
            "@odata.etag": "W/\"67404512\"",
            "isauditenabled": true,
            "auditretentionperiodv2": 30,
            "isuseraccessauditenabled": true,
            "useraccessauditinginterval": 4,
            "organizationid": "<organizationid value>"
        }
    ]
}
```

More information:

- <xref:Microsoft.Dynamics.CRM.organization?text=organization EntityType>
- [Retrieve a table row using the Web API](../webapi/retrieve-entity-using-web-api.md)

# [SDK for .NET](#tab/sdk)

```csharp
/// <summary>
/// Shows Auditing Configuration properties
/// </summary>
/// <param name="svc">The IOrganizationService instance to use.</param>
static void ShowAuditingConfig(IOrganizationService svc)
{
    WhoAmIResponse whoAmIResponse = 
        (WhoAmIResponse)svc.Execute(new WhoAmIRequest());

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

    Console.WriteLine($"isauditenabled: " +
        $"{organization["isauditenabled"]}");
    Console.WriteLine($"auditretentionperiodv2: " +
        $"{organization["auditretentionperiodv2"]}");
    Console.WriteLine($"isuseraccessauditenabled: " +
        $"{organization["isuseraccessauditenabled"]}");
    Console.WriteLine($"useraccessauditinginterval: " +
        $"{organization["useraccessauditinginterval"]}");
}
```

More information:

- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*?text=IOrganizationService.Execute Method>
- <xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest?text=WhoAmIRequest Class>
- <xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse?text=WhoAmIResponse Class>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*?text=IOrganizationService.Retrieve Method>

---

### Change organization settings

Update the column properties in the table above to change how auditing works for the environment. You must have the System Administrator or System Customizer roles to change these settings.

You can set these column values using Web API or Dataverse SDK for .NET. More information:

- [Update and delete table rows using the Web API](../webapi/update-delete-entities-using-web-api.md)
- [Update and delete table rows using the Organization Service](../org-service/entity-operations-update-delete.md)

## Configure tables and columns

When auditing is configured for the organization, any tables configured for auditing will write auditing data for all of the columns that are enabled for auditing. By default, all columns that can participate in auditing are enabled. The primary control is at the organization and then table level.

Tables and columns each have a *managed property* named `IsAuditEnabled` that controls whether they are enabled for auditing.

|Item |Web API | SDK for .NET|
|---------|---------|---------|
|Table|<xref:Microsoft.Dynamics.CRM.EntityMetadata>.`IsAuditEnabled`|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled?text=EntityMetadata.IsAuditEnabled Property>|
|Column|<xref:Microsoft.Dynamics.CRM.AttributeMetadata>.`IsAuditEnabled`|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsAuditEnabled?text=AttributeMetadata.IsAuditEnabled Property>|

The `IsAuditEnabled` property is a managed property that is defined by the following types:

|Web API  |SDK for .NET|
|---------|---------|
|<xref:Microsoft.Dynamics.CRM.BooleanManagedProperty?text=BooleanManagedProperty ComplexType>|<xref:Microsoft.Xrm.Sdk.BooleanManagedProperty?text=BooleanManagedProperty Class>|

A `BooleanManagedProperty` has two important properties:

|Property|Description|
|---------|---------|
|`Value`|Determines whether the setting is enabled.|
|`CanBeChanged` |Determines whether the `Value` setting can be changed after the table or column is included in a managed solution.|

The publisher of the solution that adds a table  may block people who install their managed solution from enabling auditing. Some Dataverse system tables cannot be enabled or disabled for auditing because the `CanBeChanged` property is set to `false`. More information: [Managed properties](/power-platform/alm/managed-properties-alm)

> [!NOTE]
> At the time of this writing, the `IsAuditEnabled` property is exposed in the designer like a simple boolean property with the label **Audit changes to its data** for tables or **Enable auditing** for columns. The `CanBeChanged` property can only be read or set programmatically.

### Detect which tables are enabled for auditing

Query the table definitions to detect which tables currently support auditing and which ones can be changed by looking at the `IsAuditEnabled` property.

# [Web API](#tab/webapi)

This query returns the `Logicalname` for all public tables that are enabled for auditing:

**Request**

```http
GET [Organization URI]/api/data/v9.2/EntityDefinitions?$select=
LogicalName,
IsAuditEnabled
&$filter=IsAuditEnabled/Value eq true 
and IsPrivate eq false

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
```

**Response**

```http
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#EntityDefinitions(LogicalName,IsAuditEnabled)",
    "value": [
        {
            "LogicalName": "account",
            "MetadataId": "70816501-edb9-4740-a16c-6a5efbc05d84",
            "IsAuditEnabled": {
                "Value": true,
                "CanBeChanged": true,
                "ManagedPropertyLogicalName": "canmodifyauditsettings"
            }
        },
    < list truncated for brevity >
    ]
}
```

More information:

- [Query table definitions using the Web API](../webapi/query-metadata-web-api.md)
- <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType>
- [Private tables](../entities.md#private-tables)

# [SDK for .NET](#tab/sdk)

```csharp
/// <summary>
/// Lists the tables that can be enabled for auditing and 
/// the tables that cannot be enabled for auditing.
/// </summary>
/// <param name="svc">The IOrganizationService instance to use.</param>
static void ShowTableAuditConfigurations(IOrganizationService svc)
{
    //Define properties to return
    MetadataPropertiesExpression EntityProperties =
        new MetadataPropertiesExpression()
        {
            AllProperties = false
        };
    EntityProperties.PropertyNames
        .AddRange(new string[] { "IsAuditEnabled" });

    //Define filter to apply
    MetadataFilterExpression EntityFilter =
        new MetadataFilterExpression(LogicalOperator.And);
    EntityFilter.Conditions
        .Add(new MetadataConditionExpression(
            "IsPrivate",
            MetadataConditionOperator.Equals,
            false));

    RetrieveMetadataChangesRequest request =
        new RetrieveMetadataChangesRequest()
        {
            Query = new EntityQueryExpression()
            {
                Criteria = EntityFilter,
                Properties = EntityProperties
            }
        };

    RetrieveMetadataChangesResponse response =
        (RetrieveMetadataChangesResponse)svc.Execute(request);

    Console.WriteLine("These tables can be enabled for auditing:");
    response.EntityMetadata.ToList().ForEach(x =>
    {
        if (x.IsAuditEnabled.CanBeChanged && !x.IsAuditEnabled.Value)
        {
            Console.WriteLine($"{x.LogicalName}");
        }
    });

    Console.WriteLine("\nThese tables cannot be enabled for auditing:");
    response.EntityMetadata.ToList().ForEach(x =>
    {
        if (!x.IsAuditEnabled.CanBeChanged && !x.IsAuditEnabled.Value)
        {
            Console.WriteLine($"{x.LogicalName}");
        }
    });
}
```

More information:

- [Retrieve and detect changes to table definitions](../org-service/metadata-retrieve-detect-changes.md)
- [Private tables](../entities.md#private-tables)

---

### Detect which columns are enabled for auditing

Query the column definitions to detect which table columns currently support auditing and which ones can be changed by looking at the `IsAuditEnabled` property.


# [Web API](#tab/webapi)

This returns all the columns enabled for auditing for the `account` table.

**Request**

```http
GET [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='account')/Attributes?$select=
LogicalName,
IsAuditEnabled
&$filter=IsAuditEnabled/Value eq true

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
```

**Response**

```http
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#EntityDefinitions('account')/Attributes(LogicalName,IsAuditEnabled)",
    "value": [
        {
            "@odata.type": "#Microsoft.Dynamics.CRM.StringAttributeMetadata",
            "LogicalName": "emailaddress3",
            "MetadataId": "97fb4aae-ea5d-427f-9b2b-9a6b9754286e",
            "IsAuditEnabled": {
                "Value": true,
                "CanBeChanged": true,
                "ManagedPropertyLogicalName": "canmodifyauditsettings"
            }
        },
    < list truncated for brevity >
    ]
}
```

More information: [Query table definitions using the Web API](../webapi/query-metadata-web-api.md)

# [SDK for .NET](#tab/sdk)

```csharp
/// <summary>
/// Lists the columns of a table that can be enabled for auditing and 
/// the columns that cannot be enabled for auditing.
/// </summary>
/// <param name="svc">The IOrganizationService instance to use.</param>
/// <param name="tableLogicalName">The logical name of the table.</param>
static void ShowColumnAuditConfigurations(
IOrganizationService svc,
string tableLogicalName)
{

//Define properties to return
MetadataPropertiesExpression EntityProperties =
    new MetadataPropertiesExpression()
    {
        AllProperties = false
    };
EntityProperties.PropertyNames
    .AddRange(new string[] { "Attributes" });

//Define filter to apply
MetadataFilterExpression EntityFilter =
    new MetadataFilterExpression(LogicalOperator.And);
EntityFilter.Conditions.Add(
    new MetadataConditionExpression(
        "LogicalName",
        MetadataConditionOperator.Equals,
        tableLogicalName));

//Define properties to return
MetadataPropertiesExpression AttributeProperties =
    new MetadataPropertiesExpression()
    {
        AllProperties = false
    };
AttributeProperties.PropertyNames
    .AddRange(new string[] {
        "LogicalName",
        "IsAuditEnabled" });


RetrieveMetadataChangesRequest request =
    new RetrieveMetadataChangesRequest()
    {
        Query = new EntityQueryExpression()
        {
            Criteria = EntityFilter,
            Properties = EntityProperties,
            AttributeQuery = new AttributeQueryExpression
            {
                Criteria = null,
                Properties = AttributeProperties
            }

        }
    };

RetrieveMetadataChangesResponse response =
    (RetrieveMetadataChangesResponse)svc.Execute(request);

response.EntityMetadata.ToList().ForEach(x =>
{
    Console.WriteLine("These columns can be enabled for auditing:");
    x.Attributes.ToList().ForEach(y =>
    {
        if (y.IsAuditEnabled.CanBeChanged && !y.IsAuditEnabled.Value)
        {
            Console.WriteLine($"{y.LogicalName}");
        }
    });

    Console.WriteLine("\nThese columns cannot be enabled for auditing:");
    x.Attributes.ToList().ForEach(y =>
    {
        if (!y.IsAuditEnabled.CanBeChanged && !y.IsAuditEnabled.Value)
        {
            Console.WriteLine($"{y.LogicalName}");
        }
    });
});
}
```

More information: [Retrieve and detect changes to table definitions](../org-service/metadata-retrieve-detect-changes.md)

---

## Enable or disable tables and columns for auditing

If you want to change which tables or columns support auditing, you must update the respective `IsAuditEnabled.Value` property.

### Tables

|API|Property|More information|
|---------|---------|---------|
|Web API|<xref:Microsoft.Dynamics.CRM.EntityMetadata>.`IsAuditEnabled.Value`|[Update table definitions](../webapi/create-update-entity-definitions-using-web-api.md#update-table-definitions)|
|SDK for .NET|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled?text=EntityMetadata.IsAuditEnabled>.`Value`|[Retrieve and update a table](../org-service/metadata-retrieve-update-delete-entities.md#retrieve-and-update-a-table)|

### Columns

|API|Property|More information|
|---------|---------|---------|
|Web API|<xref:Microsoft.Dynamics.CRM.AttributeMetadata>.`IsAuditEnabled.Value`|[Update a column](../webapi/create-update-entity-definitions-using-web-api.md#update-a-column)|
|SDK for .NET|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsAuditEnabled?text=AttributeMetadata.IsAuditEnabled>.`Value`|[Update a column](../org-service/metadata-attributemetadata.md#update-a-column)|


> [!IMPORTANT]
> After you change the value for columns you must publish customizations for the table.
> Changes will not take effect until the table customizations are published.

### Publish column changes

Use the `PublishXml` message to publish customizations for the table.

# [Web API](#tab/webapi)

This example publishes the `account` table.

**Request**

```http
POST [Organization URI]/api/data/v9.2/PublishXml HTTP/1.1

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null

{
    "ParameterXml": "<importexportxml><entities><entity>account</entity></entities></importexportxml>"
}
```

**Response**

```http
HTTP/1.1 204 OK 
```

More information:

- [Use Web API actions](../webapi/use-web-api-actions.md)
- <xref:Microsoft.Dynamics.CRM.PublishXml?text=PublishXml Action>

# [SDK for .NET](#tab/sdk)

This example publishes the `account` table.

```csharp
PublishXmlRequest request = new PublishXmlRequest()
{
    ParameterXml = @"<importexportxml>
                        <entities>
                            <entity>account</entity>
                        </entities>
                    </importexportxml>"
};
svc.Execute(request);
```

More information:

 - <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*?text=IOrganizationService.Execute Method>
 - <xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest?text=PublishXmlRequest Class>
 - [Publish customizations](../../model-driven-apps/publish-customizations.md)
 - [Publish request schema](../../model-driven-apps/publish-request-schema.md)

---


### See also

[Administrators Guide: Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing)<br />
[Auditing overview](overview.md)<br />
[Retrieve the history of audited data changes](retrieve-audit-data.md)<br />
[Delete audit data](delete-audit-data.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]