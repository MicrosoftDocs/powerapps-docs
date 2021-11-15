---
title: "msdyn_knowledgeinteractioninsight table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_knowledgeinteractioninsight table/entity."
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

# msdyn_knowledgeinteractioninsight table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Knowledge Interaction Insight

**Added by**: Knowledge Management Online Features Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/msdyn_knowledgeinteractioninsights(*msdyn_knowledgeinteractioninsightid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_knowledgeinteractioninsights<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_knowledgeinteractioninsights(*msdyn_knowledgeinteractioninsightid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref href="Microsoft.Dynamics.CRM.IsValidStateTransition?text=IsValidStateTransition Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_knowledgeinteractioninsights(*msdyn_knowledgeinteractioninsightid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_knowledgeinteractioninsights<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/msdyn_knowledgeinteractioninsights(*msdyn_knowledgeinteractioninsightid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_knowledgeinteractioninsights(*msdyn_knowledgeinteractioninsightid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_knowledgeinteractioninsights|
|DisplayCollectionName|Knowledge Interaction Insights|
|DisplayName|Knowledge Interaction Insight|
|EntitySetName|msdyn_knowledgeinteractioninsights|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_knowledgeinteractioninsights|
|LogicalName|msdyn_knowledgeinteractioninsight|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_knowledgeinteractioninsightid|
|PrimaryNameAttribute|msdyn_interactiontype|
|SchemaName|msdyn_knowledgeinteractioninsight|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_ArticleRank](#BKMK_msdyn_ArticleRank)
- [msdyn_ArticleRecordId](#BKMK_msdyn_ArticleRecordId)
- [msdyn_ArticleRelevance](#BKMK_msdyn_ArticleRelevance)
- [msdyn_InteractionContext](#BKMK_msdyn_InteractionContext)
- [msdyn_InteractionType](#BKMK_msdyn_InteractionType)
- [msdyn_knowledgeinteractioninsightId](#BKMK_msdyn_knowledgeinteractioninsightId)
- [msdyn_KnowledgeOperationId](#BKMK_msdyn_KnowledgeOperationId)
- [msdyn_KnowledgeOperationType](#BKMK_msdyn_KnowledgeOperationType)
- [msdyn_TimeStamp](#BKMK_msdyn_TimeStamp)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


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


### <a name="BKMK_msdyn_ArticleRank"></a> msdyn_ArticleRank

|Property|Value|
|--------|-----|
|Description|The position of the article in the returned article list|
|DisplayName|Article rank|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_articlerank|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_msdyn_ArticleRecordId"></a> msdyn_ArticleRecordId

|Property|Value|
|--------|-----|
|Description|The ID of the knowledge article record|
|DisplayName|Article Record ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_articlerecordid|
|MaxLength|36|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_ArticleRelevance"></a> msdyn_ArticleRelevance

|Property|Value|
|--------|-----|
|Description|Relevance score for the knowledge article returned by the search engine|
|DisplayName|Article relevance|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_articlerelevance|
|MaxValue|1000000000|
|MinValue|-1000000000|
|Precision|2|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_msdyn_InteractionContext"></a> msdyn_InteractionContext

|Property|Value|
|--------|-----|
|Description|Context of custom interactions|
|DisplayName|Interaction context|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_interactioncontext|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_InteractionType"></a> msdyn_InteractionType

|Property|Value|
|--------|-----|
|Description|The type of interaction with the customer|
|DisplayName|Interaction type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_interactiontype|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_knowledgeinteractioninsightId"></a> msdyn_knowledgeinteractioninsightId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Knowledge Interaction Insight ID|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_knowledgeinteractioninsightid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_KnowledgeOperationId"></a> msdyn_KnowledgeOperationId

|Property|Value|
|--------|-----|
|Description|The related Record ID of the knowledge operation entity|
|DisplayName|Knowledge Operation ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_knowledgeoperationid|
|MaxLength|36|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_KnowledgeOperationType"></a> msdyn_KnowledgeOperationType

|Property|Value|
|--------|-----|
|Description|The operation type performed, such as search or recommendation|
|DisplayName|Knowledge Operation Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_knowledgeoperationtype|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_TimeStamp"></a> msdyn_TimeStamp

|Property|Value|
|--------|-----|
|DateTimeBehavior|TimeZoneIndependent|
|Description|Date and time of the interaction.|
|DisplayName|Time stamp|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_timestamp|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|


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


### <a name="BKMK_OwnerId"></a> OwnerId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Knowledge Interaction Insight|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Knowledge Interaction Insight|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



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
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Yomi name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version Number|
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

- [msdyn_knowledgeinteractioninsight_SyncErrors](#BKMK_msdyn_knowledgeinteractioninsight_SyncErrors)
- [msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord](#BKMK_msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord)
- [msdyn_knowledgeinteractioninsight_DuplicateBaseRecord](#BKMK_msdyn_knowledgeinteractioninsight_DuplicateBaseRecord)
- [msdyn_knowledgeinteractioninsight_AsyncOperations](#BKMK_msdyn_knowledgeinteractioninsight_AsyncOperations)
- [msdyn_knowledgeinteractioninsight_MailboxTrackingFolders](#BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders)
- [msdyn_knowledgeinteractioninsight_ProcessSession](#BKMK_msdyn_knowledgeinteractioninsight_ProcessSession)
- [msdyn_knowledgeinteractioninsight_BulkDeleteFailures](#BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures)
- [msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses)


### <a name="BKMK_msdyn_knowledgeinteractioninsight_SyncErrors"></a> msdyn_knowledgeinteractioninsight_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [msdyn_knowledgeinteractioninsight_SyncErrors](syncerror.md#BKMK_msdyn_knowledgeinteractioninsight_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgeinteractioninsight_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord"></a> msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgeinteractioninsight_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgeinteractioninsight_DuplicateBaseRecord"></a> msdyn_knowledgeinteractioninsight_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [msdyn_knowledgeinteractioninsight_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_knowledgeinteractioninsight_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgeinteractioninsight_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgeinteractioninsight_AsyncOperations"></a> msdyn_knowledgeinteractioninsight_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [msdyn_knowledgeinteractioninsight_AsyncOperations](asyncoperation.md#BKMK_msdyn_knowledgeinteractioninsight_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgeinteractioninsight_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders"></a> msdyn_knowledgeinteractioninsight_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [msdyn_knowledgeinteractioninsight_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgeinteractioninsight_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgeinteractioninsight_ProcessSession"></a> msdyn_knowledgeinteractioninsight_ProcessSession

**Added by**: System Solution Solution

Same as processsession table [msdyn_knowledgeinteractioninsight_ProcessSession](processsession.md#BKMK_msdyn_knowledgeinteractioninsight_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgeinteractioninsight_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures"></a> msdyn_knowledgeinteractioninsight_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [msdyn_knowledgeinteractioninsight_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_knowledgeinteractioninsight_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgeinteractioninsight_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_knowledgeinteractioninsight_createdby](#BKMK_lk_msdyn_knowledgeinteractioninsight_createdby)
- [lk_msdyn_knowledgeinteractioninsight_createdonbehalfby](#BKMK_lk_msdyn_knowledgeinteractioninsight_createdonbehalfby)
- [lk_msdyn_knowledgeinteractioninsight_modifiedby](#BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedby)
- [lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby)
- [user_msdyn_knowledgeinteractioninsight](#BKMK_user_msdyn_knowledgeinteractioninsight)
- [team_msdyn_knowledgeinteractioninsight](#BKMK_team_msdyn_knowledgeinteractioninsight)
- [business_unit_msdyn_knowledgeinteractioninsight](#BKMK_business_unit_msdyn_knowledgeinteractioninsight)


### <a name="BKMK_lk_msdyn_knowledgeinteractioninsight_createdby"></a> lk_msdyn_knowledgeinteractioninsight_createdby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgeinteractioninsight_createdby](systemuser.md#BKMK_lk_msdyn_knowledgeinteractioninsight_createdby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_knowledgeinteractioninsight_createdonbehalfby"></a> lk_msdyn_knowledgeinteractioninsight_createdonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgeinteractioninsight_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgeinteractioninsight_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedby"></a> lk_msdyn_knowledgeinteractioninsight_modifiedby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgeinteractioninsight_modifiedby](systemuser.md#BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby"></a> lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgeinteractioninsight_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_msdyn_knowledgeinteractioninsight"></a> user_msdyn_knowledgeinteractioninsight

**Added by**: System Solution Solution

See systemuser Table [user_msdyn_knowledgeinteractioninsight](systemuser.md#BKMK_user_msdyn_knowledgeinteractioninsight) One-To-Many relationship.

### <a name="BKMK_team_msdyn_knowledgeinteractioninsight"></a> team_msdyn_knowledgeinteractioninsight

**Added by**: System Solution Solution

See team Table [team_msdyn_knowledgeinteractioninsight](team.md#BKMK_team_msdyn_knowledgeinteractioninsight) One-To-Many relationship.

### <a name="BKMK_business_unit_msdyn_knowledgeinteractioninsight"></a> business_unit_msdyn_knowledgeinteractioninsight

**Added by**: System Solution Solution

See businessunit Table [business_unit_msdyn_knowledgeinteractioninsight](businessunit.md#BKMK_business_unit_msdyn_knowledgeinteractioninsight) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_knowledgeinteractioninsight?text=msdyn_knowledgeinteractioninsight EntityType" />