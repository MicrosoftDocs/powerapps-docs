---
title: "organizationdatasyncsubscriptionfnotable table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the organizationdatasyncsubscriptionfnotable table/entity with Microsoft Dataverse."
ms.date: 11/09/2024
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# organizationdatasyncsubscriptionfnotable table/entity reference



## Messages

The following table lists the messages for the organizationdatasyncsubscriptionfnotable table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /organizationdatasyncsubscriptionfnotables<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /organizationdatasyncsubscriptionfnotables(*organizationdatasyncsubscriptionfnotableid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /organizationdatasyncsubscriptionfnotables(*organizationdatasyncsubscriptionfnotableid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /organizationdatasyncsubscriptionfnotables<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /organizationdatasyncsubscriptionfnotables(*organizationdatasyncsubscriptionfnotableid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /organizationdatasyncsubscriptionfnotables(*organizationdatasyncsubscriptionfnotableid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /organizationdatasyncsubscriptionfnotables(*organizationdatasyncsubscriptionfnotableid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the organizationdatasyncsubscriptionfnotable table.

|Property|Value|
| --- | --- |
| **DisplayName** | **OrganizationDataSyncSubscriptionFnoTable** |
| **DisplayCollectionName** | **OrganizationDataSyncSubscriptionFnoTables** |
| **SchemaName** | `organizationdatasyncsubscriptionfnotable` |
| **CollectionSchemaName** | `organizationdatasyncsubscriptionfnotables` |
| **EntitySetName** | `organizationdatasyncsubscriptionfnotables`|
| **LogicalName** | `organizationdatasyncsubscriptionfnotable` |
| **LogicalCollectionName** | `organizationdatasyncsubscriptionfnotables` |
| **PrimaryIdAttribute** | `organizationdatasyncsubscriptionfnotableid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [BlobPartitionBy](#BKMK_BlobPartitionBy)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [InheritsFromOtc](#BKMK_InheritsFromOtc)
- [IsActivity](#BKMK_IsActivity)
- [name](#BKMK_name)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OrganizationDataSyncSubscriptioId](#BKMK_OrganizationDataSyncSubscriptioId)
- [OrganizationDataSyncSubscription](#BKMK_OrganizationDataSyncSubscription)
- [organizationdatasyncsubscriptionfnotableId](#BKMK_organizationdatasyncsubscriptionfnotableId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_BlobPartitionBy"></a> BlobPartitionBy

|Property|Value|
|---|---|
|Description||
|DisplayName|**BlobPartitionBy**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`blobpartitionby`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`organizationdatasyncsubscriptionfnotable_blobpartitionby`|

#### BlobPartitionBy Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Day**|
|2|**Month**|
|3|**Year**|

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

### <a name="BKMK_InheritsFromOtc"></a> InheritsFromOtc

|Property|Value|
|---|---|
|Description||
|DisplayName|**InheritsFromOtc**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`inheritsfromotc`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_IsActivity"></a> IsActivity

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsActivity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isactivity`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`organizationdatasyncsubscriptionfnotable_isactivity`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_name"></a> name

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
|MaxLength|200|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName|**ObjectTypeCode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_OrganizationDataSyncSubscriptioId"></a> OrganizationDataSyncSubscriptioId

|Property|Value|
|---|---|
|Description|**Unique identifier for OrganizationDataSyncSubscription associated with OrganizationDataSyncSubscriptionFnoTable.**|
|DisplayName|**OrganizationDataSyncSubscription**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`organizationdatasyncsubscriptioid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|organizationdatasyncsubscription|

### <a name="BKMK_OrganizationDataSyncSubscription"></a> OrganizationDataSyncSubscription

|Property|Value|
|---|---|
|Description|**Unique identifier for OrganizationDataSyncSubscription associated with OrganizationDataSyncSubscriptionFnoTable.**|
|DisplayName|**OrganizationDataSyncSubscription**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`organizationdatasyncsubscription`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|organizationdatasyncsubscription|

### <a name="BKMK_organizationdatasyncsubscriptionfnotableId"></a> organizationdatasyncsubscriptionfnotableId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**OrganizationDataSyncSubscriptionFnoTable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationdatasyncsubscriptionfnotableid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the OrganizationDataSyncSubscriptionFnoTable**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`organizationdatasyncsubscriptionfnotable_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the OrganizationDataSyncSubscriptionFnoTable**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`organizationdatasyncsubscriptionfnotable_statuscode`|

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
|Description|**Version number of OrganizationDataSyncSubscriptionFnoTable.**|
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

- [lk_organizationdatasyncsubscriptionfnotable_createdby](#BKMK_lk_organizationdatasyncsubscriptionfnotable_createdby)
- [lk_organizationdatasyncsubscriptionfnotable_createdonbehalfby](#BKMK_lk_organizationdatasyncsubscriptionfnotable_createdonbehalfby)
- [lk_organizationdatasyncsubscriptionfnotable_modifiedby](#BKMK_lk_organizationdatasyncsubscriptionfnotable_modifiedby)
- [lk_organizationdatasyncsubscriptionfnotable_modifiedonbehalfby](#BKMK_lk_organizationdatasyncsubscriptionfnotable_modifiedonbehalfby)
- [organization_organizationdatasyncsubscriptionfnotable](#BKMK_organization_organizationdatasyncsubscriptionfnotable)
- [subscription_subscriptionfnotable](#BKMK_subscription_subscriptionfnotable)
- [subscription_subscriptionfnotable_duplicate](#BKMK_subscription_subscriptionfnotable_duplicate)

### <a name="BKMK_lk_organizationdatasyncsubscriptionfnotable_createdby"></a> lk_organizationdatasyncsubscriptionfnotable_createdby

One-To-Many Relationship: [systemuser lk_organizationdatasyncsubscriptionfnotable_createdby](systemuser.md#BKMK_lk_organizationdatasyncsubscriptionfnotable_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organizationdatasyncsubscriptionfnotable_createdonbehalfby"></a> lk_organizationdatasyncsubscriptionfnotable_createdonbehalfby

One-To-Many Relationship: [systemuser lk_organizationdatasyncsubscriptionfnotable_createdonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncsubscriptionfnotable_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organizationdatasyncsubscriptionfnotable_modifiedby"></a> lk_organizationdatasyncsubscriptionfnotable_modifiedby

One-To-Many Relationship: [systemuser lk_organizationdatasyncsubscriptionfnotable_modifiedby](systemuser.md#BKMK_lk_organizationdatasyncsubscriptionfnotable_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organizationdatasyncsubscriptionfnotable_modifiedonbehalfby"></a> lk_organizationdatasyncsubscriptionfnotable_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_organizationdatasyncsubscriptionfnotable_modifiedonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncsubscriptionfnotable_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_organizationdatasyncsubscriptionfnotable"></a> organization_organizationdatasyncsubscriptionfnotable

One-To-Many Relationship: [organization organization_organizationdatasyncsubscriptionfnotable](organization.md#BKMK_organization_organizationdatasyncsubscriptionfnotable)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_subscription_subscriptionfnotable"></a> subscription_subscriptionfnotable

One-To-Many Relationship: [organizationdatasyncsubscription subscription_subscriptionfnotable](organizationdatasyncsubscription.md#BKMK_subscription_subscriptionfnotable)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`organizationdatasyncsubscriptioid`|
|ReferencingEntityNavigationPropertyName|`organizationdatasyncsubscriptionId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_subscription_subscriptionfnotable_duplicate"></a> subscription_subscriptionfnotable_duplicate

One-To-Many Relationship: [organizationdatasyncsubscription subscription_subscriptionfnotable_duplicate](organizationdatasyncsubscription.md#BKMK_subscription_subscriptionfnotable_duplicate)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`organizationdatasyncsubscription`|
|ReferencingEntityNavigationPropertyName|`organizationdatasyncsubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [organizationdatasyncsubscriptionfnotable_AsyncOperations](#BKMK_organizationdatasyncsubscriptionfnotable_AsyncOperations)
- [organizationdatasyncsubscriptionfnotable_BulkDeleteFailures](#BKMK_organizationdatasyncsubscriptionfnotable_BulkDeleteFailures)
- [organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord](#BKMK_organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord)
- [organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord](#BKMK_organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord)
- [organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders](#BKMK_organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders)
- [organizationdatasyncsubscriptionfnotable_organizationdatasyncfnostate_entityname](#BKMK_organizationdatasyncsubscriptionfnotable_organizationdatasyncfnostate_entityname)
- [organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses)
- [organizationdatasyncsubscriptionfnotable_ProcessSession](#BKMK_organizationdatasyncsubscriptionfnotable_ProcessSession)
- [organizationdatasyncsubscriptionfnotable_SyncErrors](#BKMK_organizationdatasyncsubscriptionfnotable_SyncErrors)

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_AsyncOperations"></a> organizationdatasyncsubscriptionfnotable_AsyncOperations

Many-To-One Relationship: [asyncoperation organizationdatasyncsubscriptionfnotable_AsyncOperations](asyncoperation.md#BKMK_organizationdatasyncsubscriptionfnotable_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscriptionfnotable_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_BulkDeleteFailures"></a> organizationdatasyncsubscriptionfnotable_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure organizationdatasyncsubscriptionfnotable_BulkDeleteFailures](bulkdeletefailure.md#BKMK_organizationdatasyncsubscriptionfnotable_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscriptionfnotable_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord"></a> organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord](duplicaterecord.md#BKMK_organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscriptionfnotable_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord"></a> organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord](duplicaterecord.md#BKMK_organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscriptionfnotable_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders"></a> organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_organizationdatasyncfnostate_entityname"></a> organizationdatasyncsubscriptionfnotable_organizationdatasyncfnostate_entityname

Many-To-One Relationship: [organizationdatasyncfnostate organizationdatasyncsubscriptionfnotable_organizationdatasyncfnostate_entityname](organizationdatasyncfnostate.md#BKMK_organizationdatasyncsubscriptionfnotable_organizationdatasyncfnostate_entityname)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncfnostate`|
|ReferencingAttribute|`entityname`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscriptionfnotable_organizationdatasyncfnostate_entityname`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses"></a> organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_ProcessSession"></a> organizationdatasyncsubscriptionfnotable_ProcessSession

Many-To-One Relationship: [processsession organizationdatasyncsubscriptionfnotable_ProcessSession](processsession.md#BKMK_organizationdatasyncsubscriptionfnotable_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscriptionfnotable_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_SyncErrors"></a> organizationdatasyncsubscriptionfnotable_SyncErrors

Many-To-One Relationship: [syncerror organizationdatasyncsubscriptionfnotable_SyncErrors](syncerror.md#BKMK_organizationdatasyncsubscriptionfnotable_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscriptionfnotable_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.organizationdatasyncsubscriptionfnotable?displayProperty=fullName>
