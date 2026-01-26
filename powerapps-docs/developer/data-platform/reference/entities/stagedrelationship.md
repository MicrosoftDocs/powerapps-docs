---
title: "Staged relationship (StagedRelationship) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Staged relationship (StagedRelationship) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Staged relationship (StagedRelationship) table/entity reference (Microsoft Dataverse)

Stores staged replationship metadata to be processed asynchronous.

## Messages

The following table lists the messages for the Staged relationship (StagedRelationship) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /stagedrelationships<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /stagedrelationships(*stagedrelationshipid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /stagedrelationships(*stagedrelationshipid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /stagedrelationships<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /stagedrelationships(*stagedrelationshipid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /stagedrelationships(*stagedrelationshipid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Staged relationship (StagedRelationship) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Staged relationship** |
| **DisplayCollectionName** | **Staged relationships** |
| **SchemaName** | `StagedRelationship` |
| **CollectionSchemaName** | `StagedRelationships` |
| **EntitySetName** | `stagedrelationships`|
| **LogicalName** | `stagedrelationship` |
| **LogicalCollectionName** | `stagedrelationships` |
| **PrimaryIdAttribute** | `stagedrelationshipid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CascadeArchive](#BKMK_CascadeArchive)
- [CascadeAssign](#BKMK_CascadeAssign)
- [CascadeDelete](#BKMK_CascadeDelete)
- [CascadeLinkMask](#BKMK_CascadeLinkMask)
- [CascadeMerge](#BKMK_CascadeMerge)
- [CascadeReparent](#BKMK_CascadeReparent)
- [CascadeRollupView](#BKMK_CascadeRollupView)
- [CascadeShare](#BKMK_CascadeShare)
- [CascadeUnShare](#BKMK_CascadeUnShare)
- [ComponentState](#BKMK_ComponentState)
- [EntityKeyId](#BKMK_EntityKeyId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomRelationship](#BKMK_IsCustomRelationship)
- [IsLogical](#BKMK_IsLogical)
- [IsRelationshipAttributeDenormalized](#BKMK_IsRelationshipAttributeDenormalized)
- [IsValidForAdvancedFind](#BKMK_IsValidForAdvancedFind)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OverwriteTime](#BKMK_OverwriteTime)
- [RecordId](#BKMK_RecordId)
- [ReferencedAttributeId](#BKMK_ReferencedAttributeId)
- [ReferencedEntityId](#BKMK_ReferencedEntityId)
- [ReferencingAttributeId](#BKMK_ReferencingAttributeId)
- [ReferencingEntityId](#BKMK_ReferencingEntityId)
- [RelationshipRowId](#BKMK_RelationshipRowId)
- [RelationshipType](#BKMK_RelationshipType)
- [SolutionId](#BKMK_SolutionId)
- [StagedRelationshipId](#BKMK_StagedRelationshipId)
- [StagingExecutionContextId](#BKMK_StagingExecutionContextId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_CascadeArchive"></a> CascadeArchive

|Property|Value|
|---|---|
|Description|**Cascade archive behavior.**|
|DisplayName|**Cascade Archive**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cascadearchive`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_CascadeAssign"></a> CascadeAssign

|Property|Value|
|---|---|
|Description|**Cascade assign behavior.**|
|DisplayName|**Cascade Assign**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cascadeassign`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_CascadeDelete"></a> CascadeDelete

|Property|Value|
|---|---|
|Description|**Cascade delete behavior.**|
|DisplayName|**Cascade Delete**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cascadedelete`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_CascadeLinkMask"></a> CascadeLinkMask

|Property|Value|
|---|---|
|Description|**Cascade link mask value.**|
|DisplayName|**Cascade Link Mask**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cascadelinkmask`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_CascadeMerge"></a> CascadeMerge

|Property|Value|
|---|---|
|Description|**Cascade merge behavior.**|
|DisplayName|**Cascade Merge**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cascademerge`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_CascadeReparent"></a> CascadeReparent

|Property|Value|
|---|---|
|Description|**Cascade reparent behavior.**|
|DisplayName|**Cascade Reparent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cascadereparent`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_CascadeRollupView"></a> CascadeRollupView

|Property|Value|
|---|---|
|Description|**Cascade rollup view behavior.**|
|DisplayName|**Cascade Rollup View**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cascaderollupview`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_CascadeShare"></a> CascadeShare

|Property|Value|
|---|---|
|Description|**Cascade share behavior.**|
|DisplayName|**Cascade Share**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cascadeshare`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_CascadeUnShare"></a> CascadeUnShare

|Property|Value|
|---|---|
|Description|**Cascade unshare behavior.**|
|DisplayName|**Cascade UnShare**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cascadeunshare`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**Solution component state of relationship.**|
|DisplayName|**Component State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_EntityKeyId"></a> EntityKeyId

|Property|Value|
|---|---|
|Description|**Identifier of the entity key.**|
|DisplayName|**Entity Key Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitykeyid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsCustomRelationship"></a> IsCustomRelationship

|Property|Value|
|---|---|
|Description|**Indicates if the relationship is custom.**|
|DisplayName|**Is Custom Relationship**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iscustomrelationship`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_stagedrelationship_iscustomrelationship`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_IsLogical"></a> IsLogical

|Property|Value|
|---|---|
|Description|**Indicates if the relationship is logical.**|
|DisplayName|**Is Logical**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`islogical`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_stagedrelationship_islogical`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_IsRelationshipAttributeDenormalized"></a> IsRelationshipAttributeDenormalized

|Property|Value|
|---|---|
|Description|**Indicates if the relationship attribute is denormalized.**|
|DisplayName|**Is Relationship Attribute Denormalized**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isrelationshipattributedenormalized`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_stagedrelationship_isrelationshipattributedenormalized`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_IsValidForAdvancedFind"></a> IsValidForAdvancedFind

|Property|Value|
|---|---|
|Description|**Indicates if the relationship is valid for advanced find.**|
|DisplayName|**Is Valid For Advanced Find**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isvalidforadvancedfind`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_stagedrelationship_isvalidforadvancedfind`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the relationship.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**Overwrite time of the solution component relationship.**|
|DisplayName|**Overwrite Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_RecordId"></a> RecordId

|Property|Value|
|---|---|
|Description|**Record identifier.**|
|DisplayName|**Record Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordid`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_ReferencedAttributeId"></a> ReferencedAttributeId

|Property|Value|
|---|---|
|Description|**Identifier of the referenced attribute.**|
|DisplayName|**Referenced Attribute Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`referencedattributeid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ReferencedEntityId"></a> ReferencedEntityId

|Property|Value|
|---|---|
|Description|**Identifier of the referenced entity.**|
|DisplayName|**Referenced Entity Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`referencedentityid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ReferencingAttributeId"></a> ReferencingAttributeId

|Property|Value|
|---|---|
|Description|**Identifier of the referencing attribute.**|
|DisplayName|**Referencing Attribute Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`referencingattributeid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ReferencingEntityId"></a> ReferencingEntityId

|Property|Value|
|---|---|
|Description|**Identifier of the referencing entity.**|
|DisplayName|**Referencing Entity Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`referencingentityid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RelationshipRowId"></a> RelationshipRowId

|Property|Value|
|---|---|
|Description|**Identifier of the relationship row.**|
|DisplayName|**Relationship Row Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`relationshiprowid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RelationshipType"></a> RelationshipType

|Property|Value|
|---|---|
|Description|**Type of the relationship.**|
|DisplayName|**Relationship Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`relationshiptype`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Identifier of the solution that contains relationship.**|
|DisplayName|**Solution Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_StagedRelationshipId"></a> StagedRelationshipId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances.**|
|DisplayName|**Staged Relationship**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stagedrelationshipid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_StagingExecutionContextId"></a> StagingExecutionContextId

|Property|Value|
|---|---|
|Description|**A unique identifier used to tie together all objects staged within the same transaction.**|
|DisplayName|**Staging Execution Context Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stagingexecutioncontextid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the staged relationship.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`stagedrelationship_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the staged relationship.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`stagedrelationship_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**Identifier of the supporting solution.**|
|DisplayName|**Supporting Solution Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
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
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**The version in which this relationship was introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
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
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
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

- [lk_stagedrelationship_createdby](#BKMK_lk_stagedrelationship_createdby)
- [lk_stagedrelationship_createdonbehalfby](#BKMK_lk_stagedrelationship_createdonbehalfby)
- [lk_stagedrelationship_modifiedby](#BKMK_lk_stagedrelationship_modifiedby)
- [lk_stagedrelationship_modifiedonbehalfby](#BKMK_lk_stagedrelationship_modifiedonbehalfby)

### <a name="BKMK_lk_stagedrelationship_createdby"></a> lk_stagedrelationship_createdby

One-To-Many Relationship: [systemuser lk_stagedrelationship_createdby](systemuser.md#BKMK_lk_stagedrelationship_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedrelationship_createdonbehalfby"></a> lk_stagedrelationship_createdonbehalfby

One-To-Many Relationship: [systemuser lk_stagedrelationship_createdonbehalfby](systemuser.md#BKMK_lk_stagedrelationship_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedrelationship_modifiedby"></a> lk_stagedrelationship_modifiedby

One-To-Many Relationship: [systemuser lk_stagedrelationship_modifiedby](systemuser.md#BKMK_lk_stagedrelationship_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedrelationship_modifiedonbehalfby"></a> lk_stagedrelationship_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_stagedrelationship_modifiedonbehalfby](systemuser.md#BKMK_lk_stagedrelationship_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [stagedrelationship_AsyncOperations](#BKMK_stagedrelationship_AsyncOperations)
- [stagedrelationship_BulkDeleteFailures](#BKMK_stagedrelationship_BulkDeleteFailures)
- [stagedrelationship_MailboxTrackingFolders](#BKMK_stagedrelationship_MailboxTrackingFolders)
- [stagedrelationship_PrincipalObjectAttributeAccesses](#BKMK_stagedrelationship_PrincipalObjectAttributeAccesses)
- [stagedrelationship_ProcessSession](#BKMK_stagedrelationship_ProcessSession)
- [stagedrelationship_SyncErrors](#BKMK_stagedrelationship_SyncErrors)

### <a name="BKMK_stagedrelationship_AsyncOperations"></a> stagedrelationship_AsyncOperations

Many-To-One Relationship: [asyncoperation stagedrelationship_AsyncOperations](asyncoperation.md#BKMK_stagedrelationship_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedrelationship_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedrelationship_BulkDeleteFailures"></a> stagedrelationship_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure stagedrelationship_BulkDeleteFailures](bulkdeletefailure.md#BKMK_stagedrelationship_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedrelationship_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedrelationship_MailboxTrackingFolders"></a> stagedrelationship_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder stagedrelationship_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_stagedrelationship_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedrelationship_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedrelationship_PrincipalObjectAttributeAccesses"></a> stagedrelationship_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess stagedrelationship_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_stagedrelationship_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`stagedrelationship_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedrelationship_ProcessSession"></a> stagedrelationship_ProcessSession

Many-To-One Relationship: [processsession stagedrelationship_ProcessSession](processsession.md#BKMK_stagedrelationship_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedrelationship_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedrelationship_SyncErrors"></a> stagedrelationship_SyncErrors

Many-To-One Relationship: [syncerror stagedrelationship_SyncErrors](syncerror.md#BKMK_stagedrelationship_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedrelationship_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

