---
title: "OrgInsightsMetric Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the OrgInsightsMetric entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# OrgInsightsMetric Entity Reference

Stores data regarding organization insights metric

## Entity Properties

**DisplayName**: Organization Insights Metric<br />
**DisplayCollectionName**: Organization Insights Metric<br />
**SchemaName**: OrgInsightsMetric<br />
**CollectionSchemaName**: OrgInsightsMetrics<br />
**LogicalName**: orginsightsmetric<br />
**LogicalCollectionName**: orginsightsmetrics<br />
**EntitySetName**: orginsightsmetrics<br />
**PrimaryIdAttribute**: orginsightsmetricid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [InternalName](#BKMK_InternalName)
- [MetricType](#BKMK_MetricType)
- [Name](#BKMK_Name)
- [OrgInsightsMetricId](#BKMK_OrgInsightsMetricId)


### <a name="BKMK_InternalName"></a> InternalName

**Description**: Name of the metric which is used for retrieving the data<br />
**DisplayName**: Name of the metric that is used for retrieving the data<br />
**LogicalName**: internalname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_MetricType"></a> MetricType

**Description**: Type of the metric<br />
**DisplayName**: Metric Type<br />
**LogicalName**: metrictype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Time Series
- **Value**: 2 **Label**: Category



### <a name="BKMK_Name"></a> Name

**Description**: Legend Name used while displaying the metric<br />
**DisplayName**: Legend Name used wile displaying the metric<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 160


### <a name="BKMK_OrgInsightsMetricId"></a> OrgInsightsMetricId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: orginsightsmetricid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedOn](#BKMK_CreatedOn)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the organization insights metric was created<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the record<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: organizationidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.


### <a name="BKMK_organization_orginsightsmetric"></a> organization_orginsightsmetric

See organization Entity [organization_orginsightsmetric](organization.md#BKMK_organization_orginsightsmetric) One-To-Many relationship.
orginsightsmetric

