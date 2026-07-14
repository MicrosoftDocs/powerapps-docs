---
title: "System Chart (SavedQueryVisualization) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the System Chart (SavedQueryVisualization) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# System Chart (SavedQueryVisualization) table/entity reference (Microsoft Dataverse)

System chart attached to an entity.

## Messages

The following table lists the messages for the System Chart (SavedQueryVisualization) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /savedqueryvisualizations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /savedqueryvisualizations(*savedqueryvisualizationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /savedqueryvisualizations(*savedqueryvisualizationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /savedqueryvisualizations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveUnpublished`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `Update`<br />Event: False |`PATCH` /savedqueryvisualizations(*savedqueryvisualizationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /savedqueryvisualizations(*savedqueryvisualizationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the System Chart (SavedQueryVisualization) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **System Chart** |
| **DisplayCollectionName** | **System Charts** |
| **SchemaName** | `SavedQueryVisualization` |
| **CollectionSchemaName** | `SavedQueryVisualizations` |
| **EntitySetName** | `savedqueryvisualizations`|
| **LogicalName** | `savedqueryvisualization` |
| **LogicalCollectionName** | `savedqueryvisualizations` |
| **PrimaryIdAttribute** | `savedqueryvisualizationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CanBeDeleted](#BKMK_CanBeDeleted)
- [ChartType](#BKMK_ChartType)
- [DataDescription](#BKMK_DataDescription)
- [Description](#BKMK_Description)
- [EnableCrossPartition](#BKMK_EnableCrossPartition)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsDefault](#BKMK_IsDefault)
- [Name](#BKMK_Name)
- [PresentationDescription](#BKMK_PresentationDescription)
- [PrimaryEntityTypeCode](#BKMK_PrimaryEntityTypeCode)
- [SavedQueryVisualizationId](#BKMK_SavedQueryVisualizationId)
- [Type](#BKMK_Type)
- [WebResourceId](#BKMK_WebResourceId)

### <a name="BKMK_CanBeDeleted"></a> CanBeDeleted

|Property|Value|
|---|---|
|Description|**Tells whether the saved query visualization can be deleted.**|
|DisplayName|**Can Be Deleted**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbedeleted`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_ChartType"></a> ChartType

|Property|Value|
|---|---|
|Description|**Indicates the library used to render the visualization.**|
|DisplayName|**Chart Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`charttype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`savedqueryvisualization_charttype`|

#### ChartType Choices/Options

|Value|Label|
|---|---|
|0|**ASP.NET Charts**|
|1|**Power BI**|

### <a name="BKMK_DataDescription"></a> DataDescription

|Property|Value|
|---|---|
|Description|**XML string used to define the underlying data for the system chart.**|
|DisplayName|**Data XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`datadescription`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the system chart.**|
|DisplayName|**Description**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|2000|

### <a name="BKMK_EnableCrossPartition"></a> EnableCrossPartition

|Property|Value|
|---|---|
|Description|**Tells whether the chart can retrieve data from all cluster partitions.**|
|DisplayName|**Default**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablecrosspartition`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`savedqueryvisualization_enablecrosspartition`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the form is introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|---|---|
|Description|**Indicates whether the system chart is the default chart for the entity.**|
|DisplayName|**Default Chart**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdefault`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`savedqueryvisualization_isdefault`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the system chart.**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|100|

### <a name="BKMK_PresentationDescription"></a> PresentationDescription

|Property|Value|
|---|---|
|Description|**XML string used to define the presentation properties of the system chart.**|
|DisplayName|**Presentation XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`presentationdescription`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_PrimaryEntityTypeCode"></a> PrimaryEntityTypeCode

|Property|Value|
|---|---|
|Description|**Type of entity with which the system chart is attached.**|
|DisplayName|**Primary Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`primaryentitytypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_SavedQueryVisualizationId"></a> SavedQueryVisualizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the system chart.**|
|DisplayName|**System Chart**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`savedqueryvisualizationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Type"></a> Type

|Property|Value|
|---|---|
|Description|**Specifies where the chart will be used, 0 for data centric as well as interaction centric and 1 for just interaction centric**|
|DisplayName|**Form Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`chart_usage`|

#### Type Choices/Options

|Value|Label|
|---|---|
|0|**for data centric as well as interaction centric**|
|1|**just for interaction centric**|

### <a name="BKMK_WebResourceId"></a> WebResourceId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Web resource that will be displayed in the system chart.**|
|DisplayName|**Web Resource**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`webresourceid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|webresource|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SavedQueryVisualizationIdUnique](#BKMK_SavedQueryVisualizationIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the system chart.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the system chart was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the system chart.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the system chart.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the system chart was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who last modified the system chart.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the system chart.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SavedQueryVisualizationIdUnique"></a> SavedQueryVisualizationIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**System Chart**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`savedqueryvisualizationidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the system chart.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_savedqueryvisualizationbase_createdby](#BKMK_lk_savedqueryvisualizationbase_createdby)
- [lk_savedqueryvisualizationbase_createdonbehalfby](#BKMK_lk_savedqueryvisualizationbase_createdonbehalfby)
- [lk_savedqueryvisualizationbase_modifiedby](#BKMK_lk_savedqueryvisualizationbase_modifiedby)
- [lk_savedqueryvisualizationbase_modifiedonbehalfby](#BKMK_lk_savedqueryvisualizationbase_modifiedonbehalfby)
- [organization_saved_query_visualizations](#BKMK_organization_saved_query_visualizations)
- [webresource_savedqueryvisualizations](#BKMK_webresource_savedqueryvisualizations)

### <a name="BKMK_lk_savedqueryvisualizationbase_createdby"></a> lk_savedqueryvisualizationbase_createdby

One-To-Many Relationship: [systemuser lk_savedqueryvisualizationbase_createdby](systemuser.md#BKMK_lk_savedqueryvisualizationbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_savedqueryvisualizationbase_createdonbehalfby"></a> lk_savedqueryvisualizationbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_savedqueryvisualizationbase_createdonbehalfby](systemuser.md#BKMK_lk_savedqueryvisualizationbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_savedqueryvisualizationbase_modifiedby"></a> lk_savedqueryvisualizationbase_modifiedby

One-To-Many Relationship: [systemuser lk_savedqueryvisualizationbase_modifiedby](systemuser.md#BKMK_lk_savedqueryvisualizationbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_savedqueryvisualizationbase_modifiedonbehalfby"></a> lk_savedqueryvisualizationbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_savedqueryvisualizationbase_modifiedonbehalfby](systemuser.md#BKMK_lk_savedqueryvisualizationbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_saved_query_visualizations"></a> organization_saved_query_visualizations

One-To-Many Relationship: [organization organization_saved_query_visualizations](organization.md#BKMK_organization_saved_query_visualizations)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_webresource_savedqueryvisualizations"></a> webresource_savedqueryvisualizations

One-To-Many Relationship: [webresource webresource_savedqueryvisualizations](webresource.md#BKMK_webresource_savedqueryvisualizations)

|Property|Value|
|---|---|
|ReferencedEntity|`webresource`|
|ReferencedAttribute|`webresourceid`|
|ReferencingAttribute|`webresourceid`|
|ReferencingEntityNavigationPropertyName|`webresourceid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_SavedQueryVisualization_SyncErrors"></a> SavedQueryVisualization_SyncErrors

Many-To-One Relationship: [syncerror SavedQueryVisualization_SyncErrors](syncerror.md#BKMK_SavedQueryVisualization_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SavedQueryVisualization_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.savedqueryvisualization?displayProperty=fullName>
