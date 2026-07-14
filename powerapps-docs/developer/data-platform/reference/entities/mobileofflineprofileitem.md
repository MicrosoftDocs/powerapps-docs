---
title: "Mobile Offline Profile Item (MobileOfflineProfileItem) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Mobile Offline Profile Item (MobileOfflineProfileItem) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Mobile Offline Profile Item (MobileOfflineProfileItem) table/entity reference (Microsoft Dataverse)

Information on entity availability to mobile devices in offline mode for a mobile offline profile item.

## Messages

The following table lists the messages for the Mobile Offline Profile Item (MobileOfflineProfileItem) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /mobileofflineprofileitems<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /mobileofflineprofileitems(*mobileofflineprofileitemid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /mobileofflineprofileitems(*mobileofflineprofileitemid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /mobileofflineprofileitems<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveUnpublished`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `Update`<br />Event: False |`PATCH` /mobileofflineprofileitems(*mobileofflineprofileitemid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /mobileofflineprofileitems(*mobileofflineprofileitemid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Mobile Offline Profile Item (MobileOfflineProfileItem) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Mobile Offline Profile Item** |
| **DisplayCollectionName** | **Mobile Offline Profile Item** |
| **SchemaName** | `MobileOfflineProfileItem` |
| **CollectionSchemaName** | `MobileOfflineProfileItems` |
| **EntitySetName** | `mobileofflineprofileitems`|
| **LogicalName** | `mobileofflineprofileitem` |
| **LogicalCollectionName** | `mobileofflineprofileitems` |
| **PrimaryIdAttribute** | `mobileofflineprofileitemid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CanBeFollowed](#BKMK_CanBeFollowed)
- [GetRelatedEntityRecords](#BKMK_GetRelatedEntityRecords)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsVisibleInGrid](#BKMK_IsVisibleInGrid)
- [MobileOfflineProfileItemId](#BKMK_MobileOfflineProfileItemId)
- [Name](#BKMK_Name)
- [ProcessId](#BKMK_ProcessId)
- [ProfileItemEntityFilter](#BKMK_ProfileItemEntityFilter)
- [ProfileItemRule](#BKMK_ProfileItemRule)
- [RecordDistributionCriteria](#BKMK_RecordDistributionCriteria)
- [RecordsOwnedByMe](#BKMK_RecordsOwnedByMe)
- [RecordsOwnedByMyBusinessUnit](#BKMK_RecordsOwnedByMyBusinessUnit)
- [RecordsOwnedByMyTeam](#BKMK_RecordsOwnedByMyTeam)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RelationshipData](#BKMK_RelationshipData)
- [SelectedColumns](#BKMK_SelectedColumns)
- [SelectedEntityTypeCode](#BKMK_SelectedEntityTypeCode)
- [StageId](#BKMK_StageId)
- [SyncIntervalInMinutes](#BKMK_SyncIntervalInMinutes)
- [TraversedPath](#BKMK_TraversedPath)
- [ViewQuery](#BKMK_ViewQuery)

### <a name="BKMK_CanBeFollowed"></a> CanBeFollowed

|Property|Value|
|---|---|
|Description|**Specifies whether records of this entity can be followed.**|
|DisplayName|**Allow Entity to Follow Relationship**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`canbefollowed`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mobileofflineprofileitem_canbefollowed`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_GetRelatedEntityRecords"></a> GetRelatedEntityRecords

|Property|Value|
|---|---|
|Description|**Specify whether records related to this entity will be made available for offline access.**|
|DisplayName|**Get Related Entities**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`getrelatedentityrecords`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mobileofflineprofileitem_getrelatedentityrecords`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the Mobile offline Profile Item is introduced.**|
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

### <a name="BKMK_IsVisibleInGrid"></a> IsVisibleInGrid

|Property|Value|
|---|---|
|Description|**Information about whether the mobile offline profile item is visible in the Profile Item subgrid.**|
|DisplayName|**Is Visible In Grid**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isvisibleingrid`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`mobileofflineprofileitem_isvisibleingrid`|
|DefaultValue|True|
|True Label|True|
|False Label|False|

### <a name="BKMK_MobileOfflineProfileItemId"></a> MobileOfflineProfileItemId

|Property|Value|
|---|---|
|Description|**Unique identifier of the mobile offline profile item.**|
|DisplayName|**Mobile Offline Profile Item**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mobileofflineprofileitemid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Enter the name of the mobile offline profile item.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**Shows the ID of the process.**|
|DisplayName|**Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ProfileItemEntityFilter"></a> ProfileItemEntityFilter

|Property|Value|
|---|---|
|Description|**Profile item entity filter criteria**|
|DisplayName|**Profile item entity filter**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`profileitementityfilter`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ProfileItemRule"></a> ProfileItemRule

|Property|Value|
|---|---|
|Description|**Saved Query associated with the Mobile offline profile item rule.**|
|DisplayName|**View to sync data to device**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`profileitemrule`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|savedquery|

### <a name="BKMK_RecordDistributionCriteria"></a> RecordDistributionCriteria

|Property|Value|
|---|---|
|Description|**Specify data download filter for selected entity**|
|DisplayName|**Data Download Filter**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recorddistributioncriteria`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`mobileofflineprofileitem_recorddistributioncriteria`|

#### RecordDistributionCriteria Choices/Options

|Value|Label|
|---|---|
|0|**Download related data only**|
|1|**All records**|
|2|**Other data filter**|
|3|**Custom data filter**|

### <a name="BKMK_RecordsOwnedByMe"></a> RecordsOwnedByMe

|Property|Value|
|---|---|
|Description|**Download my records**|
|DisplayName|**Download my records**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordsownedbyme`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mobileofflineprofileitem_recordsownedbyme`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_RecordsOwnedByMyBusinessUnit"></a> RecordsOwnedByMyBusinessUnit

|Property|Value|
|---|---|
|Description|**Download my business unit's records**|
|DisplayName|**Download my business unit's records**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordsownedbymybusinessunit`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mobileofflineprofileitem_recordsownedbymybusinessunit`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_RecordsOwnedByMyTeam"></a> RecordsOwnedByMyTeam

|Property|Value|
|---|---|
|Description|**Download my team's records**|
|DisplayName|**Download my team's records**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordsownedbymyteam`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mobileofflineprofileitem_recordsownedbymyteam`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Items contained with a particular Profile.**|
|DisplayName|**Regarding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|mobileofflineprofile|

### <a name="BKMK_RelationshipData"></a> RelationshipData

|Property|Value|
|---|---|
|Description|**Internal Use Only**|
|DisplayName|**Internal Use Only**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`relationshipdata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_SelectedColumns"></a> SelectedColumns

|Property|Value|
|---|---|
|Description|**Selected attributes of an entity to enable for offline sync**|
|DisplayName|**SelectedColumns**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`selectedcolumns`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_SelectedEntityTypeCode"></a> SelectedEntityTypeCode

|Property|Value|
|---|---|
|Description|**Mobile offline enabled entity**|
|DisplayName|**Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`selectedentitytypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|---|---|
|Description|**Shows the ID of the stage.**|
|DisplayName|**(Deprecated) Process Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_SyncIntervalInMinutes"></a> SyncIntervalInMinutes

|Property|Value|
|---|---|
|Description|**How often to sync data offline.**|
|DisplayName|**SyncIntervalInMinutes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`syncintervalinminutes`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1440|
|MinValue|5|

### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**(Deprecated) Traversed Path**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`traversedpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|

### <a name="BKMK_ViewQuery"></a> ViewQuery

|Property|Value|
|---|---|
|Description|**Contains converted sql of the referenced view.**|
|DisplayName|**View Query**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`viewquery`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EntityObjectTypeCode](#BKMK_EntityObjectTypeCode)
- [IsManaged](#BKMK_IsManaged)
- [IsValidated](#BKMK_IsValidated)
- [MobileOfflineProfileItemIdUnique](#BKMK_MobileOfflineProfileItemIdUnique)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PublishedOn](#BKMK_PublishedOn)
- [SelectedEntityMetadata](#BKMK_SelectedEntityMetadata)
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
|Description|**Shows who created the record.**|
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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_EntityObjectTypeCode"></a> EntityObjectTypeCode

|Property|Value|
|---|---|
|Description|**Internal Use Only**|
|DisplayName|**Internal Use Only**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityobjecttypecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**For internal use only.**|
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

### <a name="BKMK_IsValidated"></a> IsValidated

|Property|Value|
|---|---|
|Description|**Information about whether profile item is validated or not**|
|DisplayName|**Is Valid For Mobile Offline**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isvalidated`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`mobileofflineprofile_isvalidated`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MobileOfflineProfileItemIdUnique"></a> MobileOfflineProfileItemIdUnique

|Property|Value|
|---|---|
|Description|**For Internal Use Only**|
|DisplayName|**Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mobileofflineprofileitemidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who updated the record on behalf of another user.**|
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
|Description|**Unique identifier of the organization associated with the Mobile Offline Profile Item.**|
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

### <a name="BKMK_PublishedOn"></a> PublishedOn

|Property|Value|
|---|---|
|Description|**Displays the last published date time.**|
|DisplayName|**Published On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publishedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SelectedEntityMetadata"></a> SelectedEntityMetadata

|Property|Value|
|---|---|
|Description|**Internal Use Only**|
|DisplayName|**Internal Use Only**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`selectedentitymetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

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
|Description|**Version number of the Mobile Offline Profile Item.**|
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

- [lk_MobileOfflineProfileItem_createdby](#BKMK_lk_MobileOfflineProfileItem_createdby)
- [lk_mobileofflineprofileitem_createdonbehalfby](#BKMK_lk_mobileofflineprofileitem_createdonbehalfby)
- [lk_mobileofflineprofileitem_modifiedby](#BKMK_lk_mobileofflineprofileitem_modifiedby)
- [lk_mobileofflineprofileitem_modifiedonbehalfby](#BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby)
- [lk_mobileofflineprofileitem_savedquery](#BKMK_lk_mobileofflineprofileitem_savedquery)
- [MobileOfflineProfile_MobileOfflineProfileItem](#BKMK_MobileOfflineProfile_MobileOfflineProfileItem)
- [MobileOfflineProfileItem_organization](#BKMK_MobileOfflineProfileItem_organization)

### <a name="BKMK_lk_MobileOfflineProfileItem_createdby"></a> lk_MobileOfflineProfileItem_createdby

One-To-Many Relationship: [systemuser lk_MobileOfflineProfileItem_createdby](systemuser.md#BKMK_lk_MobileOfflineProfileItem_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mobileofflineprofileitem_createdonbehalfby"></a> lk_mobileofflineprofileitem_createdonbehalfby

One-To-Many Relationship: [systemuser lk_mobileofflineprofileitem_createdonbehalfby](systemuser.md#BKMK_lk_mobileofflineprofileitem_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mobileofflineprofileitem_modifiedby"></a> lk_mobileofflineprofileitem_modifiedby

One-To-Many Relationship: [systemuser lk_mobileofflineprofileitem_modifiedby](systemuser.md#BKMK_lk_mobileofflineprofileitem_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby"></a> lk_mobileofflineprofileitem_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_mobileofflineprofileitem_modifiedonbehalfby](systemuser.md#BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mobileofflineprofileitem_savedquery"></a> lk_mobileofflineprofileitem_savedquery

One-To-Many Relationship: [savedquery lk_mobileofflineprofileitem_savedquery](savedquery.md#BKMK_lk_mobileofflineprofileitem_savedquery)

|Property|Value|
|---|---|
|ReferencedEntity|`savedquery`|
|ReferencedAttribute|`savedqueryid`|
|ReferencingAttribute|`profileitemrule`|
|ReferencingEntityNavigationPropertyName|`profileitemrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_MobileOfflineProfile_MobileOfflineProfileItem"></a> MobileOfflineProfile_MobileOfflineProfileItem

One-To-Many Relationship: [mobileofflineprofile MobileOfflineProfile_MobileOfflineProfileItem](mobileofflineprofile.md#BKMK_MobileOfflineProfile_MobileOfflineProfileItem)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofile`|
|ReferencedAttribute|`mobileofflineprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_MobileOfflineProfileItem_organization"></a> MobileOfflineProfileItem_organization

One-To-Many Relationship: [organization MobileOfflineProfileItem_organization](organization.md#BKMK_MobileOfflineProfileItem_organization)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_MobileOfflineProfileItem_MobileOfflineProfileItemAssociation"></a> MobileOfflineProfileItem_MobileOfflineProfileItemAssociation

Many-To-One Relationship: [mobileofflineprofileitemassociation MobileOfflineProfileItem_MobileOfflineProfileItemAssociation](mobileofflineprofileitemassociation.md#BKMK_MobileOfflineProfileItem_MobileOfflineProfileItemAssociation)

|Property|Value|
|---|---|
|ReferencingEntity|`mobileofflineprofileitemassociation`|
|ReferencingAttribute|`mobileofflineprofileitemid`|
|ReferencedEntityNavigationPropertyName|`MobileOfflineProfileItem_MobileOfflineProfileItemAssociation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mobileofflineprofileitem?displayProperty=fullName>
