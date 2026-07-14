---
title: "organizationdatasyncsubscription table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the organizationdatasyncsubscription table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# organizationdatasyncsubscription table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the organizationdatasyncsubscription table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /organizationdatasyncsubscriptions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /organizationdatasyncsubscriptions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the organizationdatasyncsubscription table.

|Property|Value|
| --- | --- |
| **DisplayName** | **OrganizationDataSyncSubscription** |
| **DisplayCollectionName** | **OrganizationDataSyncSubscriptions** |
| **SchemaName** | `organizationdatasyncsubscription` |
| **CollectionSchemaName** | `organizationdatasyncsubscriptions` |
| **EntitySetName** | `organizationdatasyncsubscriptions`|
| **LogicalName** | `organizationdatasyncsubscription` |
| **LogicalCollectionName** | `organizationdatasyncsubscriptions` |
| **PrimaryIdAttribute** | `organizationdatasyncsubscriptionid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AadApplicationId](#BKMK_AadApplicationId)
- [BlobPartitionBy](#BKMK_BlobPartitionBy)
- [CanSyncAllMetadata](#BKMK_CanSyncAllMetadata)
- [DataEndpointPostingType](#BKMK_DataEndpointPostingType)
- [DataProcessingType](#BKMK_DataProcessingType)
- [EndpointSettings](#BKMK_EndpointSettings)
- [EntityFilters](#BKMK_EntityFilters)
- [EntitySettings](#BKMK_EntitySettings)
- [FullSyncOnly](#BKMK_FullSyncOnly)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsOutOfBoxSubscription](#BKMK_IsOutOfBoxSubscription)
- [MigrationState](#BKMK_MigrationState)
- [name](#BKMK_name)
- [NeedCopyAttachmentsToBlob](#BKMK_NeedCopyAttachmentsToBlob)
- [NeedToCopyFilesToBlob](#BKMK_NeedToCopyFilesToBlob)
- [NewEntities](#BKMK_NewEntities)
- [NewFnoTables](#BKMK_NewFnoTables)
- [organizationdatasyncsubscriptionId](#BKMK_organizationdatasyncsubscriptionId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartnerPrefix](#BKMK_PartnerPrefix)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [SubscribedToAllEntities](#BKMK_SubscribedToAllEntities)
- [SubscriptionEndpointStatus](#BKMK_SubscriptionEndpointStatus)
- [SubscriptionEntities](#BKMK_SubscriptionEntities)
- [SubscriptionFnoTables](#BKMK_SubscriptionFnoTables)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UnsubscribedEntities](#BKMK_UnsubscribedEntities)
- [UnsubscribedFnoTables](#BKMK_UnsubscribedFnoTables)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AadApplicationId"></a> AadApplicationId

|Property|Value|
|---|---|
|Description||
|DisplayName|**AadApplicationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aadapplicationid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

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
|DefaultFormValue|0|
|GlobalChoiceName|`organizationdatasyncsubscription_blobpartitionby`|

#### BlobPartitionBy Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Day**|
|2|**Month**|
|3|**Year**|

### <a name="BKMK_CanSyncAllMetadata"></a> CanSyncAllMetadata

|Property|Value|
|---|---|
|Description||
|DisplayName|**CanSyncAllMetadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cansyncallmetadata`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`organizationdatasyncsubscription_cansyncallmetadata`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_DataEndpointPostingType"></a> DataEndpointPostingType

|Property|Value|
|---|---|
|Description||
|DisplayName|**DataEndpointPostingType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dataendpointpostingtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`organizationdatasyncsubscription_dataendpointpostingtype`|

#### DataEndpointPostingType Choices/Options

|Value|Label|
|---|---|
|0|**DefaultEndpoint**|
|1|**ServiceBusTopic**|
|2|**HTTPS**|
|3|**ServiceBusEventHub**|

### <a name="BKMK_DataProcessingType"></a> DataProcessingType

|Property|Value|
|---|---|
|Description||
|DisplayName|**DataProcessingType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dataprocessingtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`organizationdatasyncsubscription_dataprocessingtype`|

#### DataProcessingType Choices/Options

|Value|Label|
|---|---|
|0|**Unknown**|
|1|**Streaming**|
|2|**Batch**|
|3|**Mixed**|
|4|**NotificationOnly**|

### <a name="BKMK_EndpointSettings"></a> EndpointSettings

|Property|Value|
|---|---|
|Description||
|DisplayName|**EndpointSettings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`endpointsettings`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20000|

### <a name="BKMK_EntityFilters"></a> EntityFilters

|Property|Value|
|---|---|
|Description||
|DisplayName|**EntityFilters**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityfilters`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300000|

### <a name="BKMK_EntitySettings"></a> EntitySettings

|Property|Value|
|---|---|
|Description||
|DisplayName|**EntitySettings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitysettings`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50000|

### <a name="BKMK_FullSyncOnly"></a> FullSyncOnly

|Property|Value|
|---|---|
|Description||
|DisplayName|**FullSyncOnly**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fullsynconly`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`organizationdatasyncsubscription_fullsynconly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_IsOutOfBoxSubscription"></a> IsOutOfBoxSubscription

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsOutOfBoxSubscription**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isoutofboxsubscription`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`organizationdatasyncsubscription_isoutofboxsubscription`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MigrationState"></a> MigrationState

|Property|Value|
|---|---|
|Description||
|DisplayName|**MigrationState**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`migrationstate`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`organizationdatasyncsubscription_migrationstate`|

#### MigrationState Choices/Options

|Value|Label|
|---|---|
|0|**DsfCloudService**|
|1|**DsfSdk**|

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

### <a name="BKMK_NeedCopyAttachmentsToBlob"></a> NeedCopyAttachmentsToBlob

|Property|Value|
|---|---|
|Description||
|DisplayName|**NeedCopyAttachmentsToBlob**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`needcopyattachmentstoblob`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`organizationdatasyncsubscription_needcopyattachmentstoblob`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_NeedToCopyFilesToBlob"></a> NeedToCopyFilesToBlob

|Property|Value|
|---|---|
|Description||
|DisplayName|**NeedToCopyFilesToBlob**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`needtocopyfilestoblob`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`organizationdatasyncsubscription_needtocopyfilestoblob`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_NewEntities"></a> NewEntities

|Property|Value|
|---|---|
|Description||
|DisplayName|**NewEntities**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`newentities`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50000|

### <a name="BKMK_NewFnoTables"></a> NewFnoTables

|Property|Value|
|---|---|
|Description||
|DisplayName|**NewFnoTables**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`newfnotables`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50000|

### <a name="BKMK_organizationdatasyncsubscriptionId"></a> organizationdatasyncsubscriptionId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**OrganizationDataSyncSubscription**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationdatasyncsubscriptionid`|
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

### <a name="BKMK_PartnerPrefix"></a> PartnerPrefix

|Property|Value|
|---|---|
|Description||
|DisplayName|**PartnerPrefix**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`partnerprefix`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the OrganizationDataSyncSubscription**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`organizationdatasyncsubscription_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 3<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 0<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the OrganizationDataSyncSubscription**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`organizationdatasyncsubscription_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|3|Label: **Uninitialized**<br />State:0<br />TransitionData: None|
|4|Label: **Activated**<br />State:0<br />TransitionData: None|
|5|Label: **Deactivated**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SubscribedToAllEntities"></a> SubscribedToAllEntities

|Property|Value|
|---|---|
|Description||
|DisplayName|**SubscribedToAllEntities**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subscribedtoallentities`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`organizationdatasyncsubscription_subscribedtoallentities`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SubscriptionEndpointStatus"></a> SubscriptionEndpointStatus

|Property|Value|
|---|---|
|Description||
|DisplayName|**SubscriptionEndpointStatus**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subscriptionendpointstatus`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|6|
|MinValue|0|

### <a name="BKMK_SubscriptionEntities"></a> SubscriptionEntities

|Property|Value|
|---|---|
|Description||
|DisplayName|**subscriptionentities**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subscriptionentities`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300000|

### <a name="BKMK_SubscriptionFnoTables"></a> SubscriptionFnoTables

|Property|Value|
|---|---|
|Description||
|DisplayName|**subscriptionfnotables**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subscriptionfnotables`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300000|

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

### <a name="BKMK_UnsubscribedEntities"></a> UnsubscribedEntities

|Property|Value|
|---|---|
|Description||
|DisplayName|**UnsubscribedEntities**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`unsubscribedentities`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300000|

### <a name="BKMK_UnsubscribedFnoTables"></a> UnsubscribedFnoTables

|Property|Value|
|---|---|
|Description||
|DisplayName|**UnsubscribedFnoTables**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`unsubscribedfnotables`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300000|

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
|Description|**Version number of OrganizationDataSyncSubscription.**|
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

- [lk_organizationdatasyncsubscription_createdby](#BKMK_lk_organizationdatasyncsubscription_createdby)
- [lk_organizationdatasyncsubscription_createdonbehalfby](#BKMK_lk_organizationdatasyncsubscription_createdonbehalfby)
- [lk_organizationdatasyncsubscription_modifiedby](#BKMK_lk_organizationdatasyncsubscription_modifiedby)
- [lk_organizationdatasyncsubscription_modifiedonbehalfby](#BKMK_lk_organizationdatasyncsubscription_modifiedonbehalfby)
- [organization_organizationdatasyncsubscription](#BKMK_organization_organizationdatasyncsubscription)

### <a name="BKMK_lk_organizationdatasyncsubscription_createdby"></a> lk_organizationdatasyncsubscription_createdby

One-To-Many Relationship: [systemuser lk_organizationdatasyncsubscription_createdby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organizationdatasyncsubscription_createdonbehalfby"></a> lk_organizationdatasyncsubscription_createdonbehalfby

One-To-Many Relationship: [systemuser lk_organizationdatasyncsubscription_createdonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organizationdatasyncsubscription_modifiedby"></a> lk_organizationdatasyncsubscription_modifiedby

One-To-Many Relationship: [systemuser lk_organizationdatasyncsubscription_modifiedby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_organizationdatasyncsubscription_modifiedonbehalfby"></a> lk_organizationdatasyncsubscription_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_organizationdatasyncsubscription_modifiedonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_organizationdatasyncsubscription"></a> organization_organizationdatasyncsubscription

One-To-Many Relationship: [organization organization_organizationdatasyncsubscription](organization.md#BKMK_organization_organizationdatasyncsubscription)

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

- [organizationdatasyncsubscription_AsyncOperations](#BKMK_organizationdatasyncsubscription_AsyncOperations)
- [organizationdatasyncsubscription_BulkDeleteFailures](#BKMK_organizationdatasyncsubscription_BulkDeleteFailures)
- [organizationdatasyncsubscription_DuplicateBaseRecord](#BKMK_organizationdatasyncsubscription_DuplicateBaseRecord)
- [organizationdatasyncsubscription_DuplicateMatchingRecord](#BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord)
- [organizationdatasyncsubscription_MailboxTrackingFolders](#BKMK_organizationdatasyncsubscription_MailboxTrackingFolders)
- [organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid](#BKMK_organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid)
- [organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid](#BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid)
- [organizationdatasyncsubscription_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses)
- [organizationdatasyncsubscription_ProcessSession](#BKMK_organizationdatasyncsubscription_ProcessSession)
- [organizationdatasyncsubscription_SyncErrors](#BKMK_organizationdatasyncsubscription_SyncErrors)
- [subscription_subscriptionentity](#BKMK_subscription_subscriptionentity)
- [subscription_subscriptionentity_duplicate](#BKMK_subscription_subscriptionentity_duplicate)
- [subscription_subscriptionfnotable](#BKMK_subscription_subscriptionfnotable)
- [subscription_subscriptionfnotable_duplicate](#BKMK_subscription_subscriptionfnotable_duplicate)

### <a name="BKMK_organizationdatasyncsubscription_AsyncOperations"></a> organizationdatasyncsubscription_AsyncOperations

Many-To-One Relationship: [asyncoperation organizationdatasyncsubscription_AsyncOperations](asyncoperation.md#BKMK_organizationdatasyncsubscription_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscription_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscription_BulkDeleteFailures"></a> organizationdatasyncsubscription_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure organizationdatasyncsubscription_BulkDeleteFailures](bulkdeletefailure.md#BKMK_organizationdatasyncsubscription_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscription_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscription_DuplicateBaseRecord"></a> organizationdatasyncsubscription_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord organizationdatasyncsubscription_DuplicateBaseRecord](duplicaterecord.md#BKMK_organizationdatasyncsubscription_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscription_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord"></a> organizationdatasyncsubscription_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord organizationdatasyncsubscription_DuplicateMatchingRecord](duplicaterecord.md#BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscription_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscription_MailboxTrackingFolders"></a> organizationdatasyncsubscription_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder organizationdatasyncsubscription_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_organizationdatasyncsubscription_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscription_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid"></a> organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid

Many-To-One Relationship: [organizationdatasyncfnostate organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid](organizationdatasyncfnostate.md#BKMK_organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncfnostate`|
|ReferencingAttribute|`organizationdatasyncsubscriptionid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid"></a> organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid

Many-To-One Relationship: [organizationdatasyncstate organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid](organizationdatasyncstate.md#BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncstate`|
|ReferencingAttribute|`organizationdatasyncsubscriptionid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses"></a> organizationdatasyncsubscription_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess organizationdatasyncsubscription_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscription_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscription_ProcessSession"></a> organizationdatasyncsubscription_ProcessSession

Many-To-One Relationship: [processsession organizationdatasyncsubscription_ProcessSession](processsession.md#BKMK_organizationdatasyncsubscription_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscription_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_organizationdatasyncsubscription_SyncErrors"></a> organizationdatasyncsubscription_SyncErrors

Many-To-One Relationship: [syncerror organizationdatasyncsubscription_SyncErrors](syncerror.md#BKMK_organizationdatasyncsubscription_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`organizationdatasyncsubscription_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_subscription_subscriptionentity"></a> subscription_subscriptionentity

Many-To-One Relationship: [organizationdatasyncsubscriptionentity subscription_subscriptionentity](organizationdatasyncsubscriptionentity.md#BKMK_subscription_subscriptionentity)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncsubscriptionentity`|
|ReferencingAttribute|`organizationdatasyncsubscriptioid`|
|ReferencedEntityNavigationPropertyName|`subscription_subscriptionentity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_subscription_subscriptionentity_duplicate"></a> subscription_subscriptionentity_duplicate

Many-To-One Relationship: [organizationdatasyncsubscriptionentity subscription_subscriptionentity_duplicate](organizationdatasyncsubscriptionentity.md#BKMK_subscription_subscriptionentity_duplicate)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncsubscriptionentity`|
|ReferencingAttribute|`organizationdatasyncsubscription`|
|ReferencedEntityNavigationPropertyName|`subscription_subscriptionentity_duplicate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_subscription_subscriptionfnotable"></a> subscription_subscriptionfnotable

Many-To-One Relationship: [organizationdatasyncsubscriptionfnotable subscription_subscriptionfnotable](organizationdatasyncsubscriptionfnotable.md#BKMK_subscription_subscriptionfnotable)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencingAttribute|`organizationdatasyncsubscriptioid`|
|ReferencedEntityNavigationPropertyName|`subscription_subscriptionfnotable`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_subscription_subscriptionfnotable_duplicate"></a> subscription_subscriptionfnotable_duplicate

Many-To-One Relationship: [organizationdatasyncsubscriptionfnotable subscription_subscriptionfnotable_duplicate](organizationdatasyncsubscriptionfnotable.md#BKMK_subscription_subscriptionfnotable_duplicate)

|Property|Value|
|---|---|
|ReferencingEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencingAttribute|`organizationdatasyncsubscription`|
|ReferencedEntityNavigationPropertyName|`subscription_subscriptionfnotable_duplicate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.organizationdatasyncsubscription?displayProperty=fullName>
