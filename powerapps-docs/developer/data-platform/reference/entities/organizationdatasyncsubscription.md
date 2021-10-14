---
title: "organizationdatasyncsubscription table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the organizationdatasyncsubscription table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# organizationdatasyncsubscription table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: OrganizationDataSyncSolution Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/organizationdatasyncsubscriptions<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref href="Microsoft.Dynamics.CRM.IsValidStateTransition?text=IsValidStateTransition Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/organizationdatasyncsubscriptions<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH [*org URI*]/api/data/v9.0/organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/organizationdatasyncsubscriptions(*organizationdatasyncsubscriptionid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

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
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsOutOfBoxSubscription](#BKMK_IsOutOfBoxSubscription)
- [name](#BKMK_name)
- [NeedCopyAttachmentsToBlob](#BKMK_NeedCopyAttachmentsToBlob)
- [organizationdatasyncsubscriptionId](#BKMK_organizationdatasyncsubscriptionId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartnerPrefix](#BKMK_PartnerPrefix)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [SubscriptionEndpointStatus](#BKMK_SubscriptionEndpointStatus)
- [SubscriptionEntities](#BKMK_SubscriptionEntities)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
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
|MaxLength|150|
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
|1|Yes|
|0|No|

**DefaultValue**: False



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
|MaxLength|5000|
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
|MaxLength|10000|
|RequiredLevel|None|
|Type|Memo|


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
|1|Yes|
|0|No|

**DefaultValue**: False



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
|MaxLength|100|
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
|1|Yes|
|0|No|

**DefaultValue**: False



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
|MaxLength|50|
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
|MaxLength|5000|
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


### <a name="BKMK_organizationdatasyncsubscription_SyncErrors"></a> organizationdatasyncsubscription_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [organizationdatasyncsubscription_SyncErrors](syncerror.md#BKMK_organizationdatasyncsubscription_SyncErrors) Many-To-One relationship.

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

Same as duplicaterecord table [organizationdatasyncsubscription_DuplicateMatchingRecord](duplicaterecord.md#BKMK_organizationdatasyncsubscription_DuplicateMatchingRecord) Many-To-One relationship.

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

Same as duplicaterecord table [organizationdatasyncsubscription_DuplicateBaseRecord](duplicaterecord.md#BKMK_organizationdatasyncsubscription_DuplicateBaseRecord) Many-To-One relationship.

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

Same as asyncoperation table [organizationdatasyncsubscription_AsyncOperations](asyncoperation.md#BKMK_organizationdatasyncsubscription_AsyncOperations) Many-To-One relationship.

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

Same as mailboxtrackingfolder table [organizationdatasyncsubscription_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_organizationdatasyncsubscription_MailboxTrackingFolders) Many-To-One relationship.

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

Same as processsession table [organizationdatasyncsubscription_ProcessSession](processsession.md#BKMK_organizationdatasyncsubscription_ProcessSession) Many-To-One relationship.

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

Same as bulkdeletefailure table [organizationdatasyncsubscription_BulkDeleteFailures](bulkdeletefailure.md#BKMK_organizationdatasyncsubscription_BulkDeleteFailures) Many-To-One relationship.

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

Same as principalobjectattributeaccess table [organizationdatasyncsubscription_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses) Many-To-One relationship.

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

Same as organizationdatasyncsubscriptionentity table [subscription_subscriptionentity](organizationdatasyncsubscriptionentity.md#BKMK_subscription_subscriptionentity) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organizationdatasyncsubscriptionentity|
|ReferencingAttribute|organizationdatasyncsubscriptioid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|subscription_subscriptionentity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

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

See systemuser Table [lk_organizationdatasyncsubscription_createdby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_createdby) One-To-Many relationship.

### <a name="BKMK_lk_organizationdatasyncsubscription_createdonbehalfby"></a> lk_organizationdatasyncsubscription_createdonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_organizationdatasyncsubscription_createdonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_organizationdatasyncsubscription_modifiedby"></a> lk_organizationdatasyncsubscription_modifiedby

**Added by**: System Solution Solution

See systemuser Table [lk_organizationdatasyncsubscription_modifiedby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_organizationdatasyncsubscription_modifiedonbehalfby"></a> lk_organizationdatasyncsubscription_modifiedonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_organizationdatasyncsubscription_modifiedonbehalfby](systemuser.md#BKMK_lk_organizationdatasyncsubscription_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_organizationdatasyncsubscription"></a> organization_organizationdatasyncsubscription

**Added by**: System Solution Solution

See organization Table [organization_organizationdatasyncsubscription](organization.md#BKMK_organization_organizationdatasyncsubscription) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.organizationdatasyncsubscription?text=organizationdatasyncsubscription EntityType" />