---
title: "SavedOrgInsightsConfiguration Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SavedOrgInsightsConfiguration entity."

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
---
# SavedOrgInsightsConfiguration Entity Reference

Saved configuration for the organization insights

## Entity Properties

**DisplayName**: Saved Organization Insights Configuration<br />
**DisplayCollectionName**: Saved Organization Insights Configurations<br />
**SchemaName**: SavedOrgInsightsConfiguration<br />
**CollectionSchemaName**: SavedOrgInsightsConfigurations<br />
**LogicalName**: savedorginsightsconfiguration<br />
**LogicalCollectionName**: savedorginsightsconfigurations<br />
**EntitySetName**: savedorginsightsconfigurations<br />
**PrimaryIdAttribute**: savedorginsightsconfigurationid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Description](#BKMK_Description)
- [IsDefault](#BKMK_IsDefault)
- [IsDrilldown](#BKMK_IsDrilldown)
- [Lookback](#BKMK_Lookback)
- [MetricType](#BKMK_MetricType)
- [Name](#BKMK_Name)
- [Parameters](#BKMK_Parameters)
- [PlotOption](#BKMK_PlotOption)
- [SavedOrgInsightsConfigurationId](#BKMK_SavedOrgInsightsConfigurationId)


### <a name="BKMK_Description"></a> Description

**Description**: Description of the saved organization insights configuration<br />
**DisplayName**: Description of the saved organization insights configuration<br />
**LogicalName**: description<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 1000


### <a name="BKMK_IsDefault"></a> IsDefault

**Description**: Indicates whether this saved organization insights configuration is the default config<br />
**DisplayName**: Default Configuration<br />
**LogicalName**: isdefault<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsDrilldown"></a> IsDrilldown

**Description**: Indicates whether this configuration indicates a drilldown chart<br />
**DisplayName**: Is Drilldown<br />
**LogicalName**: isdrilldown<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Lookback"></a> Lookback

**Description**: Lookback period<br />
**DisplayName**: Lookback<br />
**LogicalName**: lookback<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: 2H
- **Value**: 2 **Label**: 48H
- **Value**: 3 **Label**: 7D
- **Value**: 4 **Label**: 30D



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

**Description**: Display name<br />
**DisplayName**: Display name for the saved organization insights configuration<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 1000


### <a name="BKMK_Parameters"></a> Parameters

**Description**: Parameters needed for data retrieval<br />
**DisplayName**: Parameters needed for data retrieval<br />
**LogicalName**: parameters<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1000


### <a name="BKMK_PlotOption"></a> PlotOption

**Description**: Plot Option<br />
**DisplayName**: Plot Option<br />
**LogicalName**: plotoption<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Line
- **Value**: 2 **Label**: Column
- **Value**: 3 **Label**: Area
- **Value**: 4 **Label**: Pie
- **Value**: 5 **Label**: Bar
- **Value**: 6 **Label**: Donut
- **Value**: 7 **Label**: Infocard
- **Value**: 8 **Label**: List
- **Value**: 9 **Label**: DoubleDonut
- **Value**: 10 **Label**: LinearGauge
- **Value**: 11 **Label**: Bubble



### <a name="BKMK_SavedOrgInsightsConfigurationId"></a> SavedOrgInsightsConfigurationId

**Description**: Shows the ID of the Saved Organization Insights Configuration<br />
**DisplayName**: SavedOrgInsightsConfigurationId<br />
**LogicalName**: savedorginsightsconfigurationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [JsonData](#BKMK_JsonData)
- [JsonDataEndTime](#BKMK_JsonDataEndTime)
- [JsonDataStartTime](#BKMK_JsonDataStartTime)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the record<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the record was created<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the record<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_JsonData"></a> JsonData

**Description**: Metrics Data in Json format for those metrics defined in parameters<br />
**DisplayName**: Metrics Data in Json format for the metrics defined in parameters<br />
**LogicalName**: jsondata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_JsonDataEndTime"></a> JsonDataEndTime

**Description**: End Time<br />
**DisplayName**: End Time<br />
**LogicalName**: jsondataendtime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_JsonDataStartTime"></a> JsonDataStartTime

**Description**: Start Time<br />
**DisplayName**: Start Time<br />
**LogicalName**: jsondatastarttime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who modified the record<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the record was modified<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the record<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the solution<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
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

- [lk_savedorginsightsconfiguration_modifiedby](#BKMK_lk_savedorginsightsconfiguration_modifiedby)
- [lk_savedorginsightsconfiguration_modifiedonbehalfby](#BKMK_lk_savedorginsightsconfiguration_modifiedonbehalfby)
- [organization_savedorginsightsconfiguration](#BKMK_organization_savedorginsightsconfiguration)
- [lk_savedorginsightsconfiguration_createdby](#BKMK_lk_savedorginsightsconfiguration_createdby)
- [lk_savedorginsightsconfiguration_createdonbehalfby](#BKMK_lk_savedorginsightsconfiguration_createdonbehalfby)


### <a name="BKMK_lk_savedorginsightsconfiguration_modifiedby"></a> lk_savedorginsightsconfiguration_modifiedby

See systemuser Entity [lk_savedorginsightsconfiguration_modifiedby](systemuser.md#BKMK_lk_savedorginsightsconfiguration_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_savedorginsightsconfiguration_modifiedonbehalfby"></a> lk_savedorginsightsconfiguration_modifiedonbehalfby

See systemuser Entity [lk_savedorginsightsconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_savedorginsightsconfiguration_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_savedorginsightsconfiguration"></a> organization_savedorginsightsconfiguration

See organization Entity [organization_savedorginsightsconfiguration](organization.md#BKMK_organization_savedorginsightsconfiguration) One-To-Many relationship.

### <a name="BKMK_lk_savedorginsightsconfiguration_createdby"></a> lk_savedorginsightsconfiguration_createdby

See systemuser Entity [lk_savedorginsightsconfiguration_createdby](systemuser.md#BKMK_lk_savedorginsightsconfiguration_createdby) One-To-Many relationship.

### <a name="BKMK_lk_savedorginsightsconfiguration_createdonbehalfby"></a> lk_savedorginsightsconfiguration_createdonbehalfby

See systemuser Entity [lk_savedorginsightsconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_savedorginsightsconfiguration_createdonbehalfby) One-To-Many relationship.
savedorginsightsconfiguration

