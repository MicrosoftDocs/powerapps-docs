---
title: "organizationdatasyncsubscription table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the organizationdatasyncsubscription table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# organizationdatasyncsubscription table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: OrganizationDataSyncSolution Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /organizationdatasyncsubscriptions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET /organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /organizationdatasyncsubscriptions<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH /organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|organizationdatasyncsubscriptions|
|DisplayCollectionName|OrganizationDataSyncSubscriptions|
|DisplayName|OrganizationDataSyncSubscription|
|EntitySetName|organizationdatasyncsubscriptions|
|IsBPFEntity|False|
|LogicalCollectionName|organizationdatasyncsubscriptions|
|LogicalName|organizationdatasyncsubscription|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|organizationdatasyncsubscriptionid|
|PrimaryNameAttribute|name|
|SchemaName|organizationdatasyncsubscription|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description||
|DisplayName|AadApplicationId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aadapplicationid|
|MaxLength|300|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_BlobPartitionBy"></a> BlobPartitionBy

|Property|Value|
|--------|-----|
|Description||
|DisplayName|BlobPartitionBy|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|blobpartitionby|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### BlobPartitionBy Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None||
|1|Day||
|2|Month||
|3|Year||



### <a name="BKMK_CanSyncAllMetadata"></a> CanSyncAllMetadata

|Property|Value|
|--------|-----|
|Description||
|DisplayName|CanSyncAllMetadata|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|cansyncallmetadata|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### CanSyncAllMetadata Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_DataEndpointPostingType"></a> DataEndpointPostingType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|DataEndpointPostingType|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|dataendpointpostingtype|
|RequiredLevel|None|
|Type|Picklist|

#### DataEndpointPostingType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|DefaultEndpoint||
|1|ServiceBusTopic||
|2|HTTPS||
|3|ServiceBusEventHub||



### <a name="BKMK_DataProcessingType"></a> DataProcessingType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|DataProcessingType|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|dataprocessingtype|
|RequiredLevel|None|
|Type|Picklist|

#### DataProcessingType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Unknown||
|1|Streaming||
|2|Batch||
|3|Mixed||
|4|NotificationOnly||



### <a name="BKMK_EndpointSettings"></a> EndpointSettings

|Property|Value|
|--------|-----|
|Description||
|DisplayName|EndpointSettings|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|endpointsettings|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_EntityFilters"></a> EntityFilters

|Property|Value|
|--------|-----|
|Description||
|DisplayName|EntityFilters|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|entityfilters|
|MaxLength|300000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_EntitySettings"></a> EntitySettings

|Property|Value|
|--------|-----|
|Description||
|DisplayName|EntitySettings|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|entitysettings|
|MaxLength|50000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_FullSyncOnly"></a> FullSyncOnly

|Property|Value|
|--------|-----|
|Description||
|DisplayName|FullSyncOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fullsynconly|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### FullSyncOnly Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsOutOfBoxSubscription"></a> IsOutOfBoxSubscription

|Property|Value|
|--------|-----|
|Description||
|DisplayName|IsOutOfBoxSubscription|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isoutofboxsubscription|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### IsOutOfBoxSubscription Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_MigrationState"></a> MigrationState

|Property|Value|
|--------|-----|
|Description||
|DisplayName|MigrationState|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|migrationstate|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### MigrationState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|DsfCloudService||
|1|DsfSdk||



### <a name="BKMK_name"></a> name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|200|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_NeedCopyAttachmentsToBlob"></a> NeedCopyAttachmentsToBlob

|Property|Value|
|--------|-----|
|Description||
|DisplayName|NeedCopyAttachmentsToBlob|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|needcopyattachmentstoblob|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### NeedCopyAttachmentsToBlob Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_NeedToCopyFilesToBlob"></a> NeedToCopyFilesToBlob

|Property|Value|
|--------|-----|
|Description||
|DisplayName|NeedToCopyFilesToBlob|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|needtocopyfilestoblob|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### NeedToCopyFilesToBlob Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_NewEntities"></a> NewEntities

|Property|Value|
|--------|-----|
|Description||
|DisplayName|NewEntities|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|newentities|
|MaxLength|50000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_NewFnoTables"></a> NewFnoTables

|Property|Value|
|--------|-----|
|Description||
|DisplayName|NewFnoTables|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|newfnotables|
|MaxLength|50000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_organizationdatasyncsubscriptionId"></a> organizationdatasyncsubscriptionId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|OrganizationDataSyncSubscription|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|organizationdatasyncsubscriptionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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


### <a name="BKMK_PartnerPrefix"></a> PartnerPrefix

|Property|Value|
|--------|-----|
|Description||
|DisplayName|PartnerPrefix|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|partnerprefix|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the OrganizationDataSyncSubscription|
|DisplayName|Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|3|Active|
|1|Inactive|0|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the OrganizationDataSyncSubscription|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|3|Uninitialized|0|
|4|Activated|0|
|5|Deactivated|1|



### <a name="BKMK_SubscribedToAllEntities"></a> SubscribedToAllEntities

|Property|Value|
|--------|-----|
|Description||
|DisplayName|SubscribedToAllEntities|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|subscribedtoallentities|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### SubscribedToAllEntities Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_SubscriptionEndpointStatus"></a> SubscriptionEndpointStatus

|Property|Value|
|--------|-----|
|Description||
|DisplayName|SubscriptionEndpointStatus|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|subscriptionendpointstatus|
|MaxValue|6|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_SubscriptionEntities"></a> SubscriptionEntities

|Property|Value|
|--------|-----|
|Description||
|DisplayName|subscriptionentities|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|subscriptionentities|
|MaxLength|50000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_SubscriptionFnoTables"></a> SubscriptionFnoTables

|Property|Value|
|--------|-----|
|Description||
|DisplayName|subscriptionfnotables|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|subscriptionfnotables|
|MaxLength|50000|
|RequiredLevel|None|
|Type|Memo|


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


### <a name="BKMK_UnsubscribedEntities"></a> UnsubscribedEntities

|Property|Value|
|--------|-----|
|Description||
|DisplayName|UnsubscribedEntities|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|unsubscribedentities|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_UnsubscribedFnoTables"></a> UnsubscribedFnoTables

|Property|Value|
|--------|-----|
|Description||
|DisplayName|UnsubscribedFnoTables|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|unsubscribedfnotables|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version number of OrganizationDataSyncSubscription.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [organizationdatasyncsubscription_SyncErrors](#BKMK_organizationdatasyncsubscription_SyncErrors)
- [organizationdatasyncsubscription_DuplicateMatchingRecord](#BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord)
- [organizationdatasyncsubscription_DuplicateBaseRecord](#BKMK_organizationdatasyncsubscription_DuplicateBaseRecord)
- [organizationdatasyncsubscription_AsyncOperations](#BKMK_organizationdatasyncsubscription_AsyncOperations)
- [organizationdatasyncsubscription_MailboxTrackingFolders](#BKMK_organizationdatasyncsubscription_MailboxTrackingFolders)
- [organizationdatasyncsubscription_ProcessSession](#BKMK_organizationdatasyncsubscription_ProcessSession)
- [organizationdatasyncsubscription_BulkDeleteFailures](#BKMK_organizationdatasyncsubscription_BulkDeleteFailures)
- [organizationdatasyncsubscription_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses)
- [subscription_subscriptionentity](#BKMK_subscription_subscriptionentity)
- [subscription_subscriptionentity_duplicate](#BKMK_subscription_subscriptionentity_duplicate)
- [subscription_subscriptionfnotable](#BKMK_subscription_subscriptionfnotable)
- [subscription_subscriptionfnotable_duplicate](#BKMK_subscription_subscriptionfnotable_duplicate)
- [organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid](#BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid)
- [organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid](#BKMK_organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid)


### <a name="BKMK_organizationdatasyncsubscription_SyncErrors"></a> organizationdatasyncsubscription_SyncErrors

**Added by**: System Solution Solution

Same as the [organizationdatasyncsubscription_SyncErrors](syncerror.md#BKMK_organizationdatasyncsubscription_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncsubscription_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord"></a> organizationdatasyncsubscription_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [organizationdatasyncsubscription_DuplicateMatchingRecord](duplicaterecord.md#BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncsubscription_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncsubscription_DuplicateBaseRecord"></a> organizationdatasyncsubscription_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [organizationdatasyncsubscription_DuplicateBaseRecord](duplicaterecord.md#BKMK_organizationdatasyncsubscription_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncsubscription_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncsubscription_AsyncOperations"></a> organizationdatasyncsubscription_AsyncOperations

**Added by**: System Solution Solution

Same as the [organizationdatasyncsubscription_AsyncOperations](asyncoperation.md#BKMK_organizationdatasyncsubscription_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncsubscription_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncsubscription_MailboxTrackingFolders"></a> organizationdatasyncsubscription_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [organizationdatasyncsubscription_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_organizationdatasyncsubscription_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncsubscription_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncsubscription_ProcessSession"></a> organizationdatasyncsubscription_ProcessSession

**Added by**: System Solution Solution

Same as the [organizationdatasyncsubscription_ProcessSession](processsession.md#BKMK_organizationdatasyncsubscription_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncsubscription_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncsubscription_BulkDeleteFailures"></a> organizationdatasyncsubscription_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [organizationdatasyncsubscription_BulkDeleteFailures](bulkdeletefailure.md#BKMK_organizationdatasyncsubscription_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncsubscription_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses"></a> organizationdatasyncsubscription_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [organizationdatasyncsubscription_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncsubscription_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_subscription_subscriptionentity"></a> subscription_subscriptionentity

Same as the [subscription_subscriptionentity](organizationdatasyncsubscriptionentity.md#BKMK_subscription_subscriptionentity) many-to-one relationship for the [organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscriptionentity|
|ReferencingAttribute|organizationdatasyncsubscriptioid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|subscription_subscriptionentity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_subscription_subscriptionentity_duplicate"></a> subscription_subscriptionentity_duplicate

Same as the [subscription_subscriptionentity_duplicate](organizationdatasyncsubscriptionentity.md#BKMK_subscription_subscriptionentity_duplicate) many-to-one relationship for the [organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscriptionentity|
|ReferencingAttribute|organizationdatasyncsubscription|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|subscription_subscriptionentity_duplicate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_subscription_subscriptionfnotable"></a> subscription_subscriptionfnotable

Same as the [subscription_subscriptionfnotable](organizationdatasyncsubscriptionfnotable.md#BKMK_subscription_subscriptionfnotable) many-to-one relationship for the [organizationdatasyncsubscriptionfnotable](organizationdatasyncsubscriptionfnotable.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscriptionfnotable|
|ReferencingAttribute|organizationdatasyncsubscriptioid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|subscription_subscriptionfnotable|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_subscription_subscriptionfnotable_duplicate"></a> subscription_subscriptionfnotable_duplicate

Same as the [subscription_subscriptionfnotable_duplicate](organizationdatasyncsubscriptionfnotable.md#BKMK_subscription_subscriptionfnotable_duplicate) many-to-one relationship for the [organizationdatasyncsubscriptionfnotable](organizationdatasyncsubscriptionfnotable.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscriptionfnotable|
|ReferencingAttribute|organizationdatasyncsubscription|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|subscription_subscriptionfnotable_duplicate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid"></a> organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid

**Added by**: DataSyncState Solution

Same as the [organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid](organizationdatasyncstate.md#BKMK_organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid) many-to-one relationship for the [organizationdatasyncstate](organizationdatasyncstate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncstate|
|ReferencingAttribute|organizationdatasyncsubscriptionid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncsubscription_organizationdatasyncstate_organizationdatasyncsubscriptionid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid"></a> organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid

**Added by**: DataSyncState Solution

Same as the [organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid](organizationdatasyncfnostate.md#BKMK_organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid) many-to-one relationship for the [organizationdatasyncfnostate](organizationdatasyncfnostate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncfnostate|
|ReferencingAttribute|organizationdatasyncsubscriptionid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|organizationdatasyncsubscription_organizationdatasyncfnostate_organizationdatasyncsubscriptionid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_organizationdatasyncsubscription_createdby](#BKMK_lk_organizationdatasyncsubscription_createdby)
- [lk_organizationdatasyncsubscription_createdonbehalfby](#BKMK_lk_organizationdatasyncsubscription_createdonbehalfby)
- [lk_organizationdatasyncsubscription_modifiedby](#BKMK_lk_organizationdatasyncsubscription_modifiedby)
- [lk_organizationdatasyncsubscription_modifiedonbehalfby](#BKMK_lk_organizationdatasyncsubscription_modifiedonbehalfby)
- [organization_organizationdatasyncsubscription](#BKMK_organization_organizationdatasyncsubscription)


### <a name="BKMK_lk_organizationdatasyncsubscription_createdby"></a> lk_organizationdatasyncsubscription_createdby

**Added by**: System Solution Solution

See the [lk_organizationdatasyncsubscription_createdby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_organizationdatasyncsubscription_createdonbehalfby"></a> lk_organizationdatasyncsubscription_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_organizationdatasyncsubscription_createdonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_organizationdatasyncsubscription_modifiedby"></a> lk_organizationdatasyncsubscription_modifiedby

**Added by**: System Solution Solution

See the [lk_organizationdatasyncsubscription_modifiedby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_organizationdatasyncsubscription_modifiedonbehalfby"></a> lk_organizationdatasyncsubscription_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_organizationdatasyncsubscription_modifiedonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_organization_organizationdatasyncsubscription"></a> organization_organizationdatasyncsubscription

**Added by**: System Solution Solution

See the [organization_organizationdatasyncsubscription](organization.md#BKMK_organization_organizationdatasyncsubscription) one-to-many relationship for the [organization](organization.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.organizationdatasyncsubscription?text=organizationdatasyncsubscription EntityType" />