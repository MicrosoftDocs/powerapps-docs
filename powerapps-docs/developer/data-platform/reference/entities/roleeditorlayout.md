---
title: "RoleEditorLayout table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the RoleEditorLayout table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# RoleEditorLayout table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Role Editor Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /roleeditorlayouts<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /roleeditorlayouts(*roleeditorlayoutid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /roleeditorlayouts(*roleeditorlayoutid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /roleeditorlayouts<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /roleeditorlayouts(*roleeditorlayoutid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /roleeditorlayouts(*roleeditorlayoutid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|RoleEditorLayouts|
|DisplayCollectionName|RoleEditorLayouts|
|DisplayName|RoleEditorLayout|
|EntitySetName|roleeditorlayouts|
|IsBPFEntity|False|
|LogicalCollectionName|roleeditorlayouts|
|LogicalName|roleeditorlayout|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|roleeditorlayoutid|
|PrimaryNameAttribute|name|
|SchemaName|RoleEditorLayout|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DisplayName](#BKMK_DisplayName)
- [EntityLogicalName](#BKMK_EntityLogicalName)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsPrivacyRelated](#BKMK_IsPrivacyRelated)
- [ItemType](#BKMK_ItemType)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PrivilegeName](#BKMK_PrivilegeName)
- [RoleEditorLayoutHierarchyId](#BKMK_RoleEditorLayoutHierarchyId)
- [RoleEditorLayoutId](#BKMK_RoleEditorLayoutId)
- [TabOrder](#BKMK_TabOrder)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|--------|-----|
|Description|Display name used for tabs, sections and miscellaneous privileges.|
|DisplayName|DisplayName|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|displayname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityLogicalName"></a> EntityLogicalName

|Property|Value|
|--------|-----|
|Description|For ItemType Entity: the logicalname of the entity.|
|DisplayName|EntityLogicalName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|entitylogicalname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_IsPrivacyRelated"></a> IsPrivacyRelated

|Property|Value|
|--------|-----|
|Description|Whether this is a privacy related miscellaneous privilege.|
|DisplayName|IsPrivacyRelated|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isprivacyrelated|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsPrivacyRelated Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_ItemType"></a> ItemType

|Property|Value|
|--------|-----|
|Description|The type of role editor layout item.|
|DisplayName|ItemType|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|itemtype|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### ItemType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Root||
|2|Tab||
|3|Miscellaneous Section||
|4|Entity||
|5|Privilege||



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|The name of the role editor layout item.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|name|
|MaxLength|128|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_PrivilegeName"></a> PrivilegeName

|Property|Value|
|--------|-----|
|Description|For ItemType Privilege: Name of the privilege|
|DisplayName|PrivilegeName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|privilegename|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RoleEditorLayoutHierarchyId"></a> RoleEditorLayoutHierarchyId

|Property|Value|
|--------|-----|
|Description|Unique identifier for RoleEditorLayout associated with RoleEditorLayout.|
|DisplayName|RoleEditorLayoutHierarchy|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|roleeditorlayouthierarchyid|
|RequiredLevel|None|
|Targets|roleeditorlayout|
|Type|Lookup|


### <a name="BKMK_RoleEditorLayoutId"></a> RoleEditorLayoutId

|Property|Value|
|--------|-----|
|Description|Unique identifier for role editor layout instances|
|DisplayName|Role Editor Layout|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|roleeditorlayoutid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_TabOrder"></a> TabOrder

|Property|Value|
|--------|-----|
|Description|For ItemType Tab: the order of which this tab is for the UI.|
|DisplayName|TabOrder|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|taborder|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
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
- [RoleEditorLayoutHierarchyIdName](#BKMK_RoleEditorLayoutHierarchyIdName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)


### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Row id unique|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ComponentState"></a> ComponentState

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_IsManaged"></a> IsManaged

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|Indicates whether the solution component is part of a managed solution.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed||
|0|Unmanaged||

**DefaultValue**: 0



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_RoleEditorLayoutHierarchyIdName"></a> RoleEditorLayoutHierarchyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|roleeditorlayouthierarchyidname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SolutionId"></a> SolutionId

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [roleeditorlayout_SyncErrors](#BKMK_roleeditorlayout_SyncErrors)
- [roleeditorlayout_DuplicateMatchingRecord](#BKMK_roleeditorlayout_DuplicateMatchingRecord)
- [roleeditorlayout_DuplicateBaseRecord](#BKMK_roleeditorlayout_DuplicateBaseRecord)
- [roleeditorlayout_AsyncOperations](#BKMK_roleeditorlayout_AsyncOperations)
- [roleeditorlayout_MailboxTrackingFolders](#BKMK_roleeditorlayout_MailboxTrackingFolders)
- [roleeditorlayout_ProcessSession](#BKMK_roleeditorlayout_ProcessSession)
- [roleeditorlayout_BulkDeleteFailures](#BKMK_roleeditorlayout_BulkDeleteFailures)
- [roleeditorlayout_PrincipalObjectAttributeAccesses](#BKMK_roleeditorlayout_PrincipalObjectAttributeAccesses)
- [roleeditorlayout_roleeditorlayout](#BKMK_roleeditorlayout_roleeditorlayout)


### <a name="BKMK_roleeditorlayout_SyncErrors"></a> roleeditorlayout_SyncErrors

**Added by**: System Solution Solution

Same as the [roleeditorlayout_SyncErrors](syncerror.md#BKMK_roleeditorlayout_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|roleeditorlayout_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_roleeditorlayout_DuplicateMatchingRecord"></a> roleeditorlayout_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [roleeditorlayout_DuplicateMatchingRecord](duplicaterecord.md#BKMK_roleeditorlayout_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|roleeditorlayout_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_roleeditorlayout_DuplicateBaseRecord"></a> roleeditorlayout_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [roleeditorlayout_DuplicateBaseRecord](duplicaterecord.md#BKMK_roleeditorlayout_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|roleeditorlayout_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_roleeditorlayout_AsyncOperations"></a> roleeditorlayout_AsyncOperations

**Added by**: System Solution Solution

Same as the [roleeditorlayout_AsyncOperations](asyncoperation.md#BKMK_roleeditorlayout_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|roleeditorlayout_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_roleeditorlayout_MailboxTrackingFolders"></a> roleeditorlayout_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [roleeditorlayout_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_roleeditorlayout_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|roleeditorlayout_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_roleeditorlayout_ProcessSession"></a> roleeditorlayout_ProcessSession

**Added by**: System Solution Solution

Same as the [roleeditorlayout_ProcessSession](processsession.md#BKMK_roleeditorlayout_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|roleeditorlayout_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_roleeditorlayout_BulkDeleteFailures"></a> roleeditorlayout_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [roleeditorlayout_BulkDeleteFailures](bulkdeletefailure.md#BKMK_roleeditorlayout_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|roleeditorlayout_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_roleeditorlayout_PrincipalObjectAttributeAccesses"></a> roleeditorlayout_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [roleeditorlayout_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_roleeditorlayout_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|roleeditorlayout_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_roleeditorlayout_roleeditorlayout"></a> roleeditorlayout_roleeditorlayout

Same as the [roleeditorlayout_roleeditorlayout](roleeditorlayout.md#BKMK_roleeditorlayout_roleeditorlayout) many-to-one relationship for the [roleeditorlayout](roleeditorlayout.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|roleeditorlayout|
|ReferencingAttribute|roleeditorlayouthierarchyid|
|IsHierarchical|True|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|roleeditorlayout_roleeditorlayout|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [roleeditorlayout_roleeditorlayout](#BKMK_roleeditorlayout_roleeditorlayout)
- [organization_roleeditorlayout](#BKMK_organization_roleeditorlayout)


### <a name="BKMK_roleeditorlayout_roleeditorlayout"></a> roleeditorlayout_roleeditorlayout

See the [roleeditorlayout_roleeditorlayout](roleeditorlayout.md#BKMK_roleeditorlayout_roleeditorlayout) one-to-many relationship for the [roleeditorlayout](roleeditorlayout.md) table/entity.

### <a name="BKMK_organization_roleeditorlayout"></a> organization_roleeditorlayout

**Added by**: System Solution Solution

See the [organization_roleeditorlayout](organization.md#BKMK_organization_roleeditorlayout) one-to-many relationship for the [organization](organization.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.roleeditorlayout?text=roleeditorlayout EntityType" />