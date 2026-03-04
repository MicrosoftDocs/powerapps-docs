---
title: "Purview Label Info (purviewlabelinfo) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Purview Label Info (purviewlabelinfo) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Purview Label Info (purviewlabelinfo) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Purview Label Info (purviewlabelinfo) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /purviewlabelinfos<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /purviewlabelinfos(*purviewlabelinfoid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /purviewlabelinfos(*purviewlabelinfoid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /purviewlabelinfos<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /purviewlabelinfos(*purviewlabelinfoid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /purviewlabelinfos(*purviewlabelinfoid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /purviewlabelinfos(*purviewlabelinfoid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Purview Label Info (purviewlabelinfo) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Purview Label Info** |
| **DisplayCollectionName** | **PurviewLabelInfo** |
| **SchemaName** | `purviewlabelinfo` |
| **CollectionSchemaName** | `purviewlabelinfos` |
| **EntitySetName** | `purviewlabelinfos`|
| **LogicalName** | `purviewlabelinfo` |
| **LogicalCollectionName** | `purviewlabelinfos` |
| **PrimaryIdAttribute** | `purviewlabelinfoid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ApplicableTo](#BKMK_ApplicableTo)
- [ApplicationMode](#BKMK_ApplicationMode)
- [Color](#BKMK_Color)
- [ContentFormats](#BKMK_ContentFormats)
- [DefaultSubLabelId](#BKMK_DefaultSubLabelId)
- [Description](#BKMK_Description)
- [HasProtection](#BKMK_HasProtection)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsActive](#BKMK_IsActive)
- [IsApplicable](#BKMK_IsApplicable)
- [IsDataverseProtected](#BKMK_IsDataverseProtected)
- [IsDefault](#BKMK_IsDefault)
- [IsEnabled](#BKMK_IsEnabled)
- [IsEndpointProtectionEnabled](#BKMK_IsEndpointProtectionEnabled)
- [IsParent](#BKMK_IsParent)
- [IsSmimeEncryptEnabled](#BKMK_IsSmimeEncryptEnabled)
- [IsSmimeSignEnabled](#BKMK_IsSmimeSignEnabled)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ParentLabelId](#BKMK_ParentLabelId)
- [Priority](#BKMK_Priority)
- [purviewlabelinfoId](#BKMK_purviewlabelinfoId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Tooltip](#BKMK_Tooltip)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ApplicableTo"></a> ApplicableTo

|Property|Value|
|---|---|
|Description||
|DisplayName|**Applicable To**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicableto`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ApplicationMode"></a> ApplicationMode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Application Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicationmode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Color"></a> Color

|Property|Value|
|---|---|
|Description||
|DisplayName|**Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`color`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ContentFormats"></a> ContentFormats

|Property|Value|
|---|---|
|Description||
|DisplayName|**Content Formats**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contentformats`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_DefaultSubLabelId"></a> DefaultSubLabelId

|Property|Value|
|---|---|
|Description|**GUID of the Sub Label**|
|DisplayName|**Default Sub Label Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`defaultsublabelid`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the label Priority (sensitivity)**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|400|

### <a name="BKMK_HasProtection"></a> HasProtection

|Property|Value|
|---|---|
|Description||
|DisplayName|**Has Protection**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`hasprotection`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`purviewlabelinfo_hasprotection`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

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

### <a name="BKMK_IsActive"></a> IsActive

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is Active**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isactive`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`purviewlabelinfo_isactive`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_IsApplicable"></a> IsApplicable

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is Appliable**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isapplicable`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`purviewlabelinfo_isapplicable`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_IsDataverseProtected"></a> IsDataverseProtected

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is Dataverse Protected**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdataverseprotected`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`purviewlabelinfo_isdataverseprotected`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is Default**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdefault`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`purviewlabelinfo_isdefault`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_IsEnabled"></a> IsEnabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`purviewlabelinfo_isenabled`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_IsEndpointProtectionEnabled"></a> IsEndpointProtectionEnabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is Endpoint Protection Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isendpointprotectionenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`purviewlabelinfo_isendpointprotectionenabled`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_IsParent"></a> IsParent

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is Parent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isparent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`purviewlabelinfo_isparent`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_IsSmimeEncryptEnabled"></a> IsSmimeEncryptEnabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is SMIME Encrypt Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`issmimeencryptenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`purviewlabelinfo_issmimeencryptenabled`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_IsSmimeSignEnabled"></a> IsSmimeSignEnabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is SMIME Sign Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`issmimesignenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`purviewlabelinfo_issmimesignenabled`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
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
|MaxLength|100|

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

### <a name="BKMK_ParentLabelId"></a> ParentLabelId

|Property|Value|
|---|---|
|Description|**Unique identifier for Purview Label Info associated with Purview Label Info.**|
|DisplayName|**Parent Label Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentlabelid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|purviewlabelinfo|

### <a name="BKMK_Priority"></a> Priority

|Property|Value|
|---|---|
|Description||
|DisplayName|**Priority**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`priority`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_purviewlabelinfoId"></a> purviewlabelinfoId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**PurviewLabelInfo**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`purviewlabelinfoid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the PurviewLabelInfo**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`purviewlabelinfo_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the PurviewLabelInfo**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`purviewlabelinfo_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

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

### <a name="BKMK_Tooltip"></a> Tooltip

|Property|Value|
|---|---|
|Description||
|DisplayName|**Tooltip**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tooltip`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1500|

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
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

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

- [lk_purviewlabelinfo_createdby](#BKMK_lk_purviewlabelinfo_createdby)
- [lk_purviewlabelinfo_createdonbehalfby](#BKMK_lk_purviewlabelinfo_createdonbehalfby)
- [lk_purviewlabelinfo_modifiedby](#BKMK_lk_purviewlabelinfo_modifiedby)
- [lk_purviewlabelinfo_modifiedonbehalfby](#BKMK_lk_purviewlabelinfo_modifiedonbehalfby)
- [organization_purviewlabelinfo](#BKMK_organization_purviewlabelinfo)
- [purviewlabelinfo_purviewlabelinfo](#BKMK_purviewlabelinfo_purviewlabelinfo-many-to-one)

### <a name="BKMK_lk_purviewlabelinfo_createdby"></a> lk_purviewlabelinfo_createdby

One-To-Many Relationship: [systemuser lk_purviewlabelinfo_createdby](systemuser.md#BKMK_lk_purviewlabelinfo_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_purviewlabelinfo_createdonbehalfby"></a> lk_purviewlabelinfo_createdonbehalfby

One-To-Many Relationship: [systemuser lk_purviewlabelinfo_createdonbehalfby](systemuser.md#BKMK_lk_purviewlabelinfo_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_purviewlabelinfo_modifiedby"></a> lk_purviewlabelinfo_modifiedby

One-To-Many Relationship: [systemuser lk_purviewlabelinfo_modifiedby](systemuser.md#BKMK_lk_purviewlabelinfo_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_purviewlabelinfo_modifiedonbehalfby"></a> lk_purviewlabelinfo_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_purviewlabelinfo_modifiedonbehalfby](systemuser.md#BKMK_lk_purviewlabelinfo_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_purviewlabelinfo"></a> organization_purviewlabelinfo

One-To-Many Relationship: [organization organization_purviewlabelinfo](organization.md#BKMK_organization_purviewlabelinfo)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_purviewlabelinfo_purviewlabelinfo-many-to-one"></a> purviewlabelinfo_purviewlabelinfo

One-To-Many Relationship: [purviewlabelinfo purviewlabelinfo_purviewlabelinfo](#BKMK_purviewlabelinfo_purviewlabelinfo-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`purviewlabelinfo`|
|ReferencedAttribute|`purviewlabelinfoid`|
|ReferencingAttribute|`parentlabelid`|
|ReferencingEntityNavigationPropertyName|`ParentLabelId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [purviewlabelinfo_AsyncOperations](#BKMK_purviewlabelinfo_AsyncOperations)
- [purviewlabelinfo_BulkDeleteFailures](#BKMK_purviewlabelinfo_BulkDeleteFailures)
- [purviewlabelinfo_DuplicateBaseRecord](#BKMK_purviewlabelinfo_DuplicateBaseRecord)
- [purviewlabelinfo_DuplicateMatchingRecord](#BKMK_purviewlabelinfo_DuplicateMatchingRecord)
- [purviewlabelinfo_MailboxTrackingFolders](#BKMK_purviewlabelinfo_MailboxTrackingFolders)
- [purviewlabelinfo_PrincipalObjectAttributeAccesses](#BKMK_purviewlabelinfo_PrincipalObjectAttributeAccesses)
- [purviewlabelinfo_ProcessSession](#BKMK_purviewlabelinfo_ProcessSession)
- [purviewlabelinfo_purviewlabelinfo](#BKMK_purviewlabelinfo_purviewlabelinfo-one-to-many)
- [purviewlabelinfo_SyncErrors](#BKMK_purviewlabelinfo_SyncErrors)

### <a name="BKMK_purviewlabelinfo_AsyncOperations"></a> purviewlabelinfo_AsyncOperations

Many-To-One Relationship: [asyncoperation purviewlabelinfo_AsyncOperations](asyncoperation.md#BKMK_purviewlabelinfo_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`purviewlabelinfo_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_purviewlabelinfo_BulkDeleteFailures"></a> purviewlabelinfo_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure purviewlabelinfo_BulkDeleteFailures](bulkdeletefailure.md#BKMK_purviewlabelinfo_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`purviewlabelinfo_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_purviewlabelinfo_DuplicateBaseRecord"></a> purviewlabelinfo_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord purviewlabelinfo_DuplicateBaseRecord](duplicaterecord.md#BKMK_purviewlabelinfo_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`purviewlabelinfo_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_purviewlabelinfo_DuplicateMatchingRecord"></a> purviewlabelinfo_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord purviewlabelinfo_DuplicateMatchingRecord](duplicaterecord.md#BKMK_purviewlabelinfo_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`purviewlabelinfo_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_purviewlabelinfo_MailboxTrackingFolders"></a> purviewlabelinfo_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder purviewlabelinfo_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_purviewlabelinfo_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`purviewlabelinfo_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_purviewlabelinfo_PrincipalObjectAttributeAccesses"></a> purviewlabelinfo_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess purviewlabelinfo_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_purviewlabelinfo_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`purviewlabelinfo_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_purviewlabelinfo_ProcessSession"></a> purviewlabelinfo_ProcessSession

Many-To-One Relationship: [processsession purviewlabelinfo_ProcessSession](processsession.md#BKMK_purviewlabelinfo_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`purviewlabelinfo_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_purviewlabelinfo_purviewlabelinfo-one-to-many"></a> purviewlabelinfo_purviewlabelinfo

Many-To-One Relationship: [purviewlabelinfo purviewlabelinfo_purviewlabelinfo](#BKMK_purviewlabelinfo_purviewlabelinfo-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`purviewlabelinfo`|
|ReferencingAttribute|`parentlabelid`|
|ReferencedEntityNavigationPropertyName|`purviewlabelinfo_purviewlabelinfo`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_purviewlabelinfo_SyncErrors"></a> purviewlabelinfo_SyncErrors

Many-To-One Relationship: [syncerror purviewlabelinfo_SyncErrors](syncerror.md#BKMK_purviewlabelinfo_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`purviewlabelinfo_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

