---
title: Configure auditing
description: Learn how to programmatically configure auditing settings for the organization, tables, and columns in Microsoft Dataverse.
ms.date: 06/02/2023
ms.topic: overview
ms.subservice: dataverse-developer
author: paulliew
ms.author: paulliew
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
ms.custom: bap-template
---

# Configure auditing

Microsoft Dataverse auditing uses settings in the [Organization table](../reference/entities/organization.md) and definitions of individual tables and columns to determine what kind of audit history data to capture. Anyone can view the configuration, but you must have the System Administrator or System Customizer role to change the settings. [Changes made to the audit configuration](retrieve-audit-data.md#audit-change-events) are included in the audit history.

## Configure organization settings

Four properties in the [Organization table](../reference/entities/organization.md) control how auditing is enabled for an environment. The organization table contains a single row. The `organizationid` column is the primary key. Query the row directly to get the key value, or execute the `WhoAmI` message and take the value of the `WhoAmIResponse.OrganizationId` property.

The following table describes the organization table columns that control auditing behavior.

|Schema Name<br/>Logical Name<br/>Display Name|Type|Description|
|---------|---------|---------|
|`IsAuditEnabled`<br/>`isauditenabled`<br/>**Is Auditing Enabled**|Boolean|Whether auditing is enabled for the environment|
|`AuditRetentionPeriodV2`<br/>`auditretentionperiodv2`<br/>**Audit Retention Period Settings**|Integer|The number of days to retain audit log records<br/>The default value is 30. Valid values are between 1 and 365,000 days (~1,000 years). If the value is set to -1, the records are retained forever.<br/>[Administrator's guide: Start/stop auditing and set retention policy](/power-platform/admin/manage-dataverse-auditing#startstop-auditing-for-a-dataverse-environment-and-set-retention-policy)|
|`IsUserAccessAuditEnabled`<br/>`isuseraccessauditenabled`<br/>**Is User Access Auditing Enabled**|Boolean|Whether user access logging is enabled<br/>Auditing for the environment must be enabled for user access logging to be enabled.|
|`UserAccessAuditingInterval`<br/>`useraccessauditinginterval`<br/>**User Authentication Auditing Interval**|Integer|How often user access is logged, in hours<br/>The default value is 4.|

### Retrieve organization settings

Use the following queries to retrieve your organization settings.

#### [Web API](#tab/webapi)

**Request:**

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

**Response:**

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

Learn more about:

- [Retrieve a table row using the Web API](../webapi/retrieve-entity-using-web-api.md)
- [organization EntityType](xref:Microsoft.Dynamics.CRM.organization)

#### [SDK for .NET](#tab/sdk)

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

Learn more about:

- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)
- [WhoAmIRequest Class](xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest)
- [WhoAmIResponse Class](xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse)
- [IOrganizationService.Retrieve Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve%2A)

---

### Change organization settings

Change the column values in the organization table to change how auditing works for the environment. You must have the System Administrator or System Customizer role to change these settings.

You can use Web API or Dataverse SDK for .NET to change your organization settings:

- [Update and delete table rows using the Web API](../webapi/update-delete-entities-using-web-api.md)
- [Update and delete table rows using the Organization Service](../org-service/entity-operations-update-delete.md)

## Configure tables and columns

When auditing is enabled for the organization, any tables that are enabled for auditing write audit data for all columns that are enabled for auditing. The primary control is at the organization and then the table level.

Tables and columns each have a *managed property* named `IsAuditEnabled` that controls whether they're enabled for auditing.

|Item |Web API | SDK for .NET|
|---------|---------|---------|
|Table|<xref:Microsoft.Dynamics.CRM.EntityMetadata>.`IsAuditEnabled`|[EntityMetadata.IsAuditEnabled Property](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled)|
|Column|<xref:Microsoft.Dynamics.CRM.AttributeMetadata>.`IsAuditEnabled`|[AttributeMetadata.IsAuditEnabled Property](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsAuditEnabled)|

The `IsAuditEnabled` property is a managed property that's defined by the following types:

|Web API  |SDK for .NET|
|---------|---------|
|[BooleanManagedProperty ComplexType](xref:Microsoft.Dynamics.CRM.BooleanManagedProperty)|[BooleanManagedProperty Class](xref:Microsoft.Xrm.Sdk.BooleanManagedProperty)|

A `BooleanManagedProperty` has two important properties:

|Property|Description|
|---------|---------|
|`Value`|Determines whether the setting is enabled.|
|`CanBeChanged` |Determines whether the `Value` setting can be changed after the table or column is included in a managed solution.|

The publisher of a managed solution that adds a table may prevent people who install the solution from enabling auditing. Some Dataverse system tables can't be enabled or disabled for auditing because the `CanBeChanged` property is set to `false`. [Learn more about managed properties](/power-platform/alm/managed-properties-alm).

> [!NOTE]
> The `IsAuditEnabled` property is exposed in the designer as a simple boolean property with the label **Audit changes to its data** for tables or **Enable auditing** for columns. The `CanBeChanged` property can only be read or set programmatically.

### Detect which tables are enabled for auditing

Query the table definitions and look at the `IsAuditEnabled` property to determine which tables support auditing and which ones can be changed.

#### [Web API](#tab/webapi)

This query returns the `Logicalname` for all public tables that are enabled for auditing.

**Request:**

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

**Response:**

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

Learn more about:

- [EntityMetadata EntityType](xref:Microsoft.Dynamics.CRM.EntityMetadata)
- [Query table definitions using the Web API](../webapi/query-metadata-web-api.md)
- [Private tables](../entities.md#private-tables)

#### [SDK for .NET](#tab/sdk)

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
Learn more about:

- [Retrieve and detect changes to table definitions](../org-service/metadata-retrieve-detect-changes.md)
- [Private tables](../entities.md#private-tables)

---

### Detect which columns are enabled for auditing

Query the column definitions and look at the `IsAuditEnabled` property to determine which columns support auditing and which ones can be changed.

#### [Web API](#tab/webapi)

**Request:**

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

**Response:**

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

Learn more about: [Query table definitions using the Web API](../webapi/query-metadata-web-api.md)

#### [SDK for .NET](#tab/sdk)

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

Learn more about: [Query schema definitions](../query-schema-definitions.md)

---

## Enable or disable tables and columns for auditing

To change which tables and columns support auditing, update their `IsAuditEnabled.Value` property.

### Tables

|API|Property|More information|
|---------|---------|---------|
|Web API|<xref:Microsoft.Dynamics.CRM.EntityMetadata>.`IsAuditEnabled.Value`|[Update table definitions](../webapi/create-update-entity-definitions-using-web-api.md#update-table-definitions)|
|SDK for .NET|[EntityMetadata.IsAuditEnabled](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled).`Value`|[Retrieve and update a table](../org-service/metadata-retrieve-update-delete-entities.md#retrieve-and-update-a-table)|

### Columns

|API|Property|More information|
|---------|---------|---------|
|Web API|<xref:Microsoft.Dynamics.CRM.AttributeMetadata>.`IsAuditEnabled.Value`|[Update a column](../webapi/create-update-column-definitions-using-web-api.md#update-a-column)|
|SDK for .NET|[AttributeMetadata.IsAuditEnabled](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsAuditEnabled).`Value`|[Update a column](../org-service/metadata-attributemetadata.md#update-a-column)|

> [!IMPORTANT]
> Changes don't take effect until you publish the table customizations.

### Publish column changes

Use the `PublishXml` message to publish customizations for the table.
#### [Web API](#tab/webapi)

**Request:**

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

**Response:**

```http
HTTP/1.1 204 OK 
```

Learn more about:

- [PublishXml Action](xref:Microsoft.Dynamics.CRM.PublishXml)

#### [SDK for .NET](#tab/sdk)

The following example publishes the `account` table:

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

Learn more about:

- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)
- [PublishXmlRequest Class](xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest)

---

Learn more about:

- [Publish customizations](../../model-driven-apps/publish-customizations.md)
- [Publish request schema](../../model-driven-apps/publish-request-schema.md)

### See also

[Administrator's guide: Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing)  
[Administrator's guide: System Settings Auditing tab](/power-platform/admin/system-settings-dialog-box-auditing-tab)  
[Auditing overview](overview.md)  
[Retrieve the history of audited data changes](retrieve-audit-data.md)  
[Delete audit data](delete-audit-data.md)

[!INCLUDE [footer-include](../../../includes/footer-banner.md)]
