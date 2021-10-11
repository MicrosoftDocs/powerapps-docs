---
title: "msdyn_knowledgesearchinsight table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_knowledgesearchinsight table/entity."
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

# msdyn_knowledgesearchinsight table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Knowledge Search Insight

**Added by**: Knowledge Management Online Features Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/msdyn_knowledgesearchinsights(*msdyn_knowledgesearchinsightid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_knowledgesearchinsights<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_knowledgesearchinsights(*msdyn_knowledgesearchinsightid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref href="Microsoft.Dynamics.CRM.IsValidStateTransition?text=IsValidStateTransition Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_knowledgesearchinsights(*msdyn_knowledgesearchinsightid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_knowledgesearchinsights<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/msdyn_knowledgesearchinsights(*msdyn_knowledgesearchinsightid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_knowledgesearchinsights(*msdyn_knowledgesearchinsightid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_knowledgesearchinsights|
|DisplayCollectionName|Knowledge Search Insights|
|DisplayName|Knowledge Search Insight|
|EntitySetName|msdyn_knowledgesearchinsights|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_knowledgesearchinsights|
|LogicalName|msdyn_knowledgesearchinsight|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_knowledgesearchinsightid|
|PrimaryNameAttribute|msdyn_searchterm|
|SchemaName|msdyn_knowledgesearchinsight|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_ApplicationName](#BKMK_msdyn_ApplicationName)
- [msdyn_CorrelationId](#BKMK_msdyn_CorrelationId)
- [msdyn_CustomControlId](#BKMK_msdyn_CustomControlId)
- [msdyn_EntityRecordId](#BKMK_msdyn_EntityRecordId)
- [msdyn_EntityType](#BKMK_msdyn_EntityType)
- [msdyn_Filters](#BKMK_msdyn_Filters)
- [msdyn_InitiatedBy](#BKMK_msdyn_InitiatedBy)
- [msdyn_knowledgesearchinsightId](#BKMK_msdyn_knowledgesearchinsightId)
- [msdyn_ResponseTime](#BKMK_msdyn_ResponseTime)
- [msdyn_ResultCount](#BKMK_msdyn_ResultCount)
- [msdyn_SearchProviderId](#BKMK_msdyn_SearchProviderId)
- [msdyn_SearchProviderName](#BKMK_msdyn_SearchProviderName)
- [msdyn_SearchTerm](#BKMK_msdyn_SearchTerm)
- [msdyn_SearchType](#BKMK_msdyn_SearchType)
- [msdyn_SortBy](#BKMK_msdyn_SortBy)
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


### <a name="BKMK_msdyn_ApplicationName"></a> msdyn_ApplicationName

|Property|Value|
|--------|-----|
|Description|The name of the application where the knowledge search is performed.|
|DisplayName|Application name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_applicationname|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_CorrelationId"></a> msdyn_CorrelationId

|Property|Value|
|--------|-----|
|Description|Designed for federation search. Used to correlate the search that triggered different search records from different search providers.|
|DisplayName|Correlation ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_correlationid|
|MaxLength|36|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_CustomControlId"></a> msdyn_CustomControlId

|Property|Value|
|--------|-----|
|Description|The ID of control knowledge search where the search is performed.|
|DisplayName|Custom Control ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_customcontrolid|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_EntityRecordId"></a> msdyn_EntityRecordId

|Property|Value|
|--------|-----|
|Description|Entity Record ID of the Entity Type|
|DisplayName|Entity Record ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_entityrecordid|
|MaxLength|36|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_EntityType"></a> msdyn_EntityType

|Property|Value|
|--------|-----|
|Description|Which kind of entity context the knowledge search performed|
|DisplayName|Entity type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_entitytype|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_Filters"></a> msdyn_Filters

|Property|Value|
|--------|-----|
|Description|The filters selected when performing the search.|
|DisplayName|Filters|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_filters|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_InitiatedBy"></a> msdyn_InitiatedBy

|Property|Value|
|--------|-----|
|Description|Whether the search is initiated by the system automatically or manually initiated by the user.|
|DisplayName|Initiated by|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_initiatedby|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_knowledgesearchinsightId"></a> msdyn_knowledgesearchinsightId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Knowledge Search Insight ID|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_knowledgesearchinsightid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_ResponseTime"></a> msdyn_ResponseTime

|Property|Value|
|--------|-----|
|Description|The time to return search results.|
|DisplayName|Response time|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_responsetime|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_ResultCount"></a> msdyn_ResultCount

|Property|Value|
|--------|-----|
|Description|The total count of knowledge articles returned|
|DisplayName|Result count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_resultcount|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_msdyn_SearchProviderId"></a> msdyn_SearchProviderId

|Property|Value|
|--------|-----|
|Description|Designed for federation search. The ID of the federated search provider.|
|DisplayName|Search Provider ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_searchproviderid|
|MaxLength|36|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_SearchProviderName"></a> msdyn_SearchProviderName

|Property|Value|
|--------|-----|
|Description|Designed for federation search. The name of the federated search provider.|
|DisplayName|Search provider name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_searchprovidername|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_SearchTerm"></a> msdyn_SearchTerm

|Property|Value|
|--------|-----|
|Description|The string typed in the search field|
|DisplayName|Search term|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_searchterm|
|MaxLength|256|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_SearchType"></a> msdyn_SearchType

|Property|Value|
|--------|-----|
|Description|The type of search run, like full text search, relevance search, etc.|
|DisplayName|Search type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_searchtype|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_SortBy"></a> msdyn_SortBy

|Property|Value|
|--------|-----|
|Description|The sort selected when performing the search.|
|DisplayName|Sort by|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_sortby|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_TimeStamp"></a> msdyn_TimeStamp

|Property|Value|
|--------|-----|
|DateTimeBehavior|TimeZoneIndependent|
|Description|Date and time when the search is performed|
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
|Description|Status of the Knowledge Search Insight|
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
|Description|Reason for the status of the Knowledge Search Insight|
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

- [msdyn_knowledgesearchinsight_SyncErrors](#BKMK_msdyn_knowledgesearchinsight_SyncErrors)
- [msdyn_knowledgesearchinsight_DuplicateMatchingRecord](#BKMK_msdyn_knowledgesearchinsight_DuplicateMatchingRecord)
- [msdyn_knowledgesearchinsight_DuplicateBaseRecord](#BKMK_msdyn_knowledgesearchinsight_DuplicateBaseRecord)
- [msdyn_knowledgesearchinsight_AsyncOperations](#BKMK_msdyn_knowledgesearchinsight_AsyncOperations)
- [msdyn_knowledgesearchinsight_MailboxTrackingFolders](#BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders)
- [msdyn_knowledgesearchinsight_ProcessSession](#BKMK_msdyn_knowledgesearchinsight_ProcessSession)
- [msdyn_knowledgesearchinsight_BulkDeleteFailures](#BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures)
- [msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses)


### <a name="BKMK_msdyn_knowledgesearchinsight_SyncErrors"></a> msdyn_knowledgesearchinsight_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [msdyn_knowledgesearchinsight_SyncErrors](syncerror.md#BKMK_msdyn_knowledgesearchinsight_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgesearchinsight_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgesearchinsight_DuplicateMatchingRecord"></a> msdyn_knowledgesearchinsight_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [msdyn_knowledgesearchinsight_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_knowledgesearchinsight_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgesearchinsight_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgesearchinsight_DuplicateBaseRecord"></a> msdyn_knowledgesearchinsight_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [msdyn_knowledgesearchinsight_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_knowledgesearchinsight_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgesearchinsight_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgesearchinsight_AsyncOperations"></a> msdyn_knowledgesearchinsight_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [msdyn_knowledgesearchinsight_AsyncOperations](asyncoperation.md#BKMK_msdyn_knowledgesearchinsight_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgesearchinsight_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders"></a> msdyn_knowledgesearchinsight_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [msdyn_knowledgesearchinsight_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgesearchinsight_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgesearchinsight_ProcessSession"></a> msdyn_knowledgesearchinsight_ProcessSession

**Added by**: System Solution Solution

Same as processsession table [msdyn_knowledgesearchinsight_ProcessSession](processsession.md#BKMK_msdyn_knowledgesearchinsight_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgesearchinsight_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures"></a> msdyn_knowledgesearchinsight_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [msdyn_knowledgesearchinsight_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_knowledgesearchinsight_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgesearchinsight_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_knowledgesearchinsight_createdby](#BKMK_lk_msdyn_knowledgesearchinsight_createdby)
- [lk_msdyn_knowledgesearchinsight_createdonbehalfby](#BKMK_lk_msdyn_knowledgesearchinsight_createdonbehalfby)
- [lk_msdyn_knowledgesearchinsight_modifiedby](#BKMK_lk_msdyn_knowledgesearchinsight_modifiedby)
- [lk_msdyn_knowledgesearchinsight_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgesearchinsight_modifiedonbehalfby)
- [user_msdyn_knowledgesearchinsight](#BKMK_user_msdyn_knowledgesearchinsight)
- [team_msdyn_knowledgesearchinsight](#BKMK_team_msdyn_knowledgesearchinsight)
- [business_unit_msdyn_knowledgesearchinsight](#BKMK_business_unit_msdyn_knowledgesearchinsight)


### <a name="BKMK_lk_msdyn_knowledgesearchinsight_createdby"></a> lk_msdyn_knowledgesearchinsight_createdby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgesearchinsight_createdby](systemuser.md#BKMK_lk_msdyn_knowledgesearchinsight_createdby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_knowledgesearchinsight_createdonbehalfby"></a> lk_msdyn_knowledgesearchinsight_createdonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgesearchinsight_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgesearchinsight_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_knowledgesearchinsight_modifiedby"></a> lk_msdyn_knowledgesearchinsight_modifiedby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgesearchinsight_modifiedby](systemuser.md#BKMK_lk_msdyn_knowledgesearchinsight_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_knowledgesearchinsight_modifiedonbehalfby"></a> lk_msdyn_knowledgesearchinsight_modifiedonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgesearchinsight_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgesearchinsight_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_msdyn_knowledgesearchinsight"></a> user_msdyn_knowledgesearchinsight

**Added by**: System Solution Solution

See systemuser Table [user_msdyn_knowledgesearchinsight](systemuser.md#BKMK_user_msdyn_knowledgesearchinsight) One-To-Many relationship.

### <a name="BKMK_team_msdyn_knowledgesearchinsight"></a> team_msdyn_knowledgesearchinsight

**Added by**: System Solution Solution

See team Table [team_msdyn_knowledgesearchinsight](team.md#BKMK_team_msdyn_knowledgesearchinsight) One-To-Many relationship.

### <a name="BKMK_business_unit_msdyn_knowledgesearchinsight"></a> business_unit_msdyn_knowledgesearchinsight

**Added by**: System Solution Solution

See businessunit Table [business_unit_msdyn_knowledgesearchinsight](businessunit.md#BKMK_business_unit_msdyn_knowledgesearchinsight) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_knowledgesearchinsight?text=msdyn_knowledgesearchinsight EntityType" />