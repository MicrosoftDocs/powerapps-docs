---
title: "AIPluginOperation table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the AIPluginOperation table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# AIPluginOperation table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

AIPluginOperations component

**Added by**: AIPlatformExtensionsCore Solution Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /aipluginoperations(*aipluginoperationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST /aipluginoperations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /aipluginoperations(*aipluginoperationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET /aipluginoperations(*aipluginoperationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /aipluginoperations<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RetrieveUnpublished|<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
|RetrieveUnpublishedMultiple|<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH /aipluginoperations(*aipluginoperationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /aipluginoperations(*aipluginoperationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|AIPluginOperations|
|DisplayCollectionName|AIPluginOperations|
|DisplayName|AIPluginOperation|
|EntitySetName|aipluginoperations|
|IsBPFEntity|False|
|LogicalCollectionName|aipluginoperations|
|LogicalName|aipluginoperation|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|aipluginoperationid|
|PrimaryNameAttribute|name|
|SchemaName|AIPluginOperation|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AIPlugin](#BKMK_AIPlugin)
- [AIPluginOperationExportKey](#BKMK_AIPluginOperationExportKey)
- [AIPluginOperationId](#BKMK_AIPluginOperationId)
- [AIPluginOperationResponseTemplate](#BKMK_AIPluginOperationResponseTemplate)
- [CustomAPI](#BKMK_CustomAPI)
- [Description](#BKMK_Description)
- [DVFileSearch](#BKMK_DVFileSearch)
- [DVTableSearch](#BKMK_DVTableSearch)
- [Entity](#BKMK_Entity)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsConsequential](#BKMK_IsConsequential)
- [IsCustomizable](#BKMK_IsCustomizable)
- [msdyn_AIModel](#BKMK_msdyn_AIModel)
- [Name](#BKMK_Name)
- [OperationId](#BKMK_OperationId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ReferencedOperationId](#BKMK_ReferencedOperationId)
- [ResponseSemantics](#BKMK_ResponseSemantics)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [Workflow](#BKMK_Workflow)


### <a name="BKMK_AIPlugin"></a> AIPlugin

|Property|Value|
|--------|-----|
|Description||
|DisplayName|AIPlugin|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|aiplugin|
|RequiredLevel|SystemRequired|
|Targets|aiplugin|
|Type|Lookup|


### <a name="BKMK_AIPluginOperationExportKey"></a> AIPluginOperationExportKey

|Property|Value|
|--------|-----|
|Description||
|DisplayName|AI Plugin Operation Export Key|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aipluginoperationexportkey|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AIPluginOperationId"></a> AIPluginOperationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|AIPluginOperation|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|aipluginoperationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_AIPluginOperationResponseTemplate"></a> AIPluginOperationResponseTemplate

|Property|Value|
|--------|-----|
|Description||
|DisplayName|AIPluginOperationResponseTemplate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aipluginoperationresponsetemplate|
|RequiredLevel|None|
|Targets|aipluginoperationresponsetemplate|
|Type|Lookup|


### <a name="BKMK_CustomAPI"></a> CustomAPI

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Custom API|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|customapi|
|RequiredLevel|None|
|Targets|customapi|
|Type|Lookup|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Operation Description|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|4000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_DVFileSearch"></a> DVFileSearch

|Property|Value|
|--------|-----|
|Description||
|DisplayName|DVFileSearch|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|dvfilesearch|
|RequiredLevel|None|
|Targets|dvfilesearch|
|Type|Lookup|


### <a name="BKMK_DVTableSearch"></a> DVTableSearch

|Property|Value|
|--------|-----|
|Description||
|DisplayName|DVTableSearch|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|dvtablesearch|
|RequiredLevel|None|
|Targets|dvtablesearch|
|Type|Lookup|


### <a name="BKMK_Entity"></a> Entity

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Entity|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|entity|
|RequiredLevel|None|
|Targets|entity|
|Type|Lookup|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Added by**: Basic Solution Solution

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


### <a name="BKMK_IsConsequential"></a> IsConsequential

|Property|Value|
|--------|-----|
|Description|Defines if the AIPluginOperation is consequential.|
|DisplayName|Is Consequential|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isconsequential|
|RequiredLevel|None|
|Type|Boolean|

#### IsConsequential Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_msdyn_AIModel"></a> msdyn_AIModel

**Added by**: AISolution Solution

|Property|Value|
|--------|-----|
|Description|Lookup to AI Model|
|DisplayName|AIModel|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_aimodel|
|RequiredLevel|None|
|Targets|msdyn_aimodel|
|Type|Lookup|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_OperationId"></a> OperationId

|Property|Value|
|--------|-----|
|Description|OperationId on the swagger file|
|DisplayName|OperationId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|operationid|
|MaxLength|100|
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


### <a name="BKMK_ReferencedOperationId"></a> ReferencedOperationId

|Property|Value|
|--------|-----|
|Description|ReferencedOperationId Description|
|DisplayName|ReferencedOperationId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|referencedoperationid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ResponseSemantics"></a> ResponseSemantics

|Property|Value|
|--------|-----|
|Description|ResponseSemantics for the AI Plugin Operation|
|DisplayName|ResponseSemantics|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|responsesemantics|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the AIPluginOperation|
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
|Description|Reason for the status of the AIPluginOperation|
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


### <a name="BKMK_Workflow"></a> Workflow

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Process|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|workflow|
|RequiredLevel|None|
|Targets|workflow|
|Type|Lookup|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AIPluginName](#BKMK_AIPluginName)
- [AIPluginOperationResponseTemplateName](#BKMK_AIPluginOperationResponseTemplateName)
- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomAPIName](#BKMK_CustomAPIName)
- [DVFileSearchName](#BKMK_DVFileSearchName)
- [DVTableSearchName](#BKMK_DVTableSearchName)
- [EntityName](#BKMK_EntityName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [msdyn_AIModelName](#BKMK_msdyn_AIModelName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)
- [WorkflowName](#BKMK_WorkflowName)


### <a name="BKMK_AIPluginName"></a> AIPluginName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|aipluginname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AIPluginOperationResponseTemplateName"></a> AIPluginOperationResponseTemplateName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|aipluginoperationresponsetemplatename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_CustomAPIName"></a> CustomAPIName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|customapiname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DVFileSearchName"></a> DVFileSearchName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|dvfilesearchname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DVTableSearchName"></a> DVTableSearchName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|dvtablesearchname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityName"></a> EntityName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_msdyn_AIModelName"></a> msdyn_AIModelName

**Added by**: AISolution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_aimodelname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunitname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


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


### <a name="BKMK_WorkflowName"></a> WorkflowName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|workflowname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [aipluginoperation_SyncErrors](#BKMK_aipluginoperation_SyncErrors)
- [aipluginoperation_AsyncOperations](#BKMK_aipluginoperation_AsyncOperations)
- [aipluginoperation_MailboxTrackingFolders](#BKMK_aipluginoperation_MailboxTrackingFolders)
- [aipluginoperation_ProcessSession](#BKMK_aipluginoperation_ProcessSession)
- [aipluginoperation_BulkDeleteFailures](#BKMK_aipluginoperation_BulkDeleteFailures)
- [aipluginoperation_PrincipalObjectAttributeAccesses](#BKMK_aipluginoperation_PrincipalObjectAttributeAccesses)
- [AIPluginOperationParameter_AIPluginO](#BKMK_AIPluginOperationParameter_AIPluginO)
- [msdyn_knowledgeassetconfiguration_aipluginoperationid](#BKMK_msdyn_knowledgeassetconfiguration_aipluginoperationid)
- [fabricaiskill_aipluginoperationid](#BKMK_fabricaiskill_aipluginoperationid)


### <a name="BKMK_aipluginoperation_SyncErrors"></a> aipluginoperation_SyncErrors

**Added by**: System Solution Solution

Same as the [aipluginoperation_SyncErrors](syncerror.md#BKMK_aipluginoperation_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|aipluginoperation_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_aipluginoperation_AsyncOperations"></a> aipluginoperation_AsyncOperations

**Added by**: System Solution Solution

Same as the [aipluginoperation_AsyncOperations](asyncoperation.md#BKMK_aipluginoperation_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|aipluginoperation_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_aipluginoperation_MailboxTrackingFolders"></a> aipluginoperation_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [aipluginoperation_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_aipluginoperation_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|aipluginoperation_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_aipluginoperation_ProcessSession"></a> aipluginoperation_ProcessSession

**Added by**: System Solution Solution

Same as the [aipluginoperation_ProcessSession](processsession.md#BKMK_aipluginoperation_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|aipluginoperation_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_aipluginoperation_BulkDeleteFailures"></a> aipluginoperation_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [aipluginoperation_BulkDeleteFailures](bulkdeletefailure.md#BKMK_aipluginoperation_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|aipluginoperation_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_aipluginoperation_PrincipalObjectAttributeAccesses"></a> aipluginoperation_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [aipluginoperation_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_aipluginoperation_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|aipluginoperation_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_AIPluginOperationParameter_AIPluginO"></a> AIPluginOperationParameter_AIPluginO

Same as the [AIPluginOperationParameter_AIPluginO](aipluginoperationparameter.md#BKMK_AIPluginOperationParameter_AIPluginO) many-to-one relationship for the [aipluginoperationparameter](aipluginoperationparameter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|aipluginoperationparameter|
|ReferencingAttribute|aipluginoperation|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|AIPluginOperationParameter_AIPluginO|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_msdyn_knowledgeassetconfiguration_aipluginoperationid"></a> msdyn_knowledgeassetconfiguration_aipluginoperationid

**Added by**: Insights App Platform Base Solution

Same as the [msdyn_knowledgeassetconfiguration_aipluginoperationid](msdyn_knowledgeassetconfiguration.md#BKMK_msdyn_knowledgeassetconfiguration_aipluginoperationid) many-to-one relationship for the [msdyn_knowledgeassetconfiguration](msdyn_knowledgeassetconfiguration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgeassetconfiguration|
|ReferencingAttribute|msdyn_aipluginoperationid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgeassetconfiguration_aipluginoperationid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_fabricaiskill_aipluginoperationid"></a> fabricaiskill_aipluginoperationid

**Added by**: Insights App Platform Base Solution

Same as the [fabricaiskill_aipluginoperationid](fabricaiskill.md#BKMK_fabricaiskill_aipluginoperationid) many-to-one relationship for the [fabricaiskill](fabricaiskill.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|fabricaiskill|
|ReferencingAttribute|aipluginoperationid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|fabricaiskill_aipluginoperationid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_aipluginoperation_createdby](#BKMK_lk_aipluginoperation_createdby)
- [lk_aipluginoperation_createdonbehalfby](#BKMK_lk_aipluginoperation_createdonbehalfby)
- [lk_aipluginoperation_modifiedby](#BKMK_lk_aipluginoperation_modifiedby)
- [lk_aipluginoperation_modifiedonbehalfby](#BKMK_lk_aipluginoperation_modifiedonbehalfby)
- [user_aipluginoperation](#BKMK_user_aipluginoperation)
- [team_aipluginoperation](#BKMK_team_aipluginoperation)
- [business_unit_aipluginoperation](#BKMK_business_unit_aipluginoperation)
- [AIPluginOperation_AIPlugin_AIPlugin](#BKMK_AIPluginOperation_AIPlugin_AIPlugin)
- [AIPluginOperation_CustomAPI_CustomAPI](#BKMK_AIPluginOperation_CustomAPI_CustomAPI)
- [AIPluginOperation_DVFileSearch_DVFileSear](#BKMK_AIPluginOperation_DVFileSearch_DVFileSear)
- [AIPluginOperation_DVTableSearch_DVTableSe](#BKMK_AIPluginOperation_DVTableSearch_DVTableSe)
- [AIPluginOperation_Entity_Entity](#BKMK_AIPluginOperation_Entity_Entity)
- [AIPluginOperation_Workflow_Workflow](#BKMK_AIPluginOperation_Workflow_Workflow)
- [operationresponsetemplate_aipluginoperation](#BKMK_operationresponsetemplate_aipluginoperation)
- [msdyn_AIPluginOperation_AIModel](#BKMK_msdyn_AIPluginOperation_AIModel)


### <a name="BKMK_lk_aipluginoperation_createdby"></a> lk_aipluginoperation_createdby

**Added by**: System Solution Solution

See the [lk_aipluginoperation_createdby](systemuser.md#BKMK_lk_aipluginoperation_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_aipluginoperation_createdonbehalfby"></a> lk_aipluginoperation_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_aipluginoperation_createdonbehalfby](systemuser.md#BKMK_lk_aipluginoperation_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_aipluginoperation_modifiedby"></a> lk_aipluginoperation_modifiedby

**Added by**: System Solution Solution

See the [lk_aipluginoperation_modifiedby](systemuser.md#BKMK_lk_aipluginoperation_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_aipluginoperation_modifiedonbehalfby"></a> lk_aipluginoperation_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_aipluginoperation_modifiedonbehalfby](systemuser.md#BKMK_lk_aipluginoperation_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_aipluginoperation"></a> user_aipluginoperation

**Added by**: System Solution Solution

See the [user_aipluginoperation](systemuser.md#BKMK_user_aipluginoperation) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_aipluginoperation"></a> team_aipluginoperation

**Added by**: System Solution Solution

See the [team_aipluginoperation](team.md#BKMK_team_aipluginoperation) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_aipluginoperation"></a> business_unit_aipluginoperation

**Added by**: System Solution Solution

See the [business_unit_aipluginoperation](businessunit.md#BKMK_business_unit_aipluginoperation) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_AIPluginOperation_AIPlugin_AIPlugin"></a> AIPluginOperation_AIPlugin_AIPlugin

See the [AIPluginOperation_AIPlugin_AIPlugin](aiplugin.md#BKMK_AIPluginOperation_AIPlugin_AIPlugin) one-to-many relationship for the [aiplugin](aiplugin.md) table/entity.

### <a name="BKMK_AIPluginOperation_CustomAPI_CustomAPI"></a> AIPluginOperation_CustomAPI_CustomAPI

**Added by**: Custom API Framework Solution

See the [AIPluginOperation_CustomAPI_CustomAPI](customapi.md#BKMK_AIPluginOperation_CustomAPI_CustomAPI) one-to-many relationship for the [customapi](customapi.md) table/entity.

### <a name="BKMK_AIPluginOperation_DVFileSearch_DVFileSear"></a> AIPluginOperation_DVFileSearch_DVFileSear

**Added by**: AIPlatformExtensionsComponents Solution Solution

See the [AIPluginOperation_DVFileSearch_DVFileSear](dvfilesearch.md#BKMK_AIPluginOperation_DVFileSearch_DVFileSear) one-to-many relationship for the [dvfilesearch](dvfilesearch.md) table/entity.

### <a name="BKMK_AIPluginOperation_DVTableSearch_DVTableSe"></a> AIPluginOperation_DVTableSearch_DVTableSe

**Added by**: AIPlatformExtensionsComponents Solution Solution

See the [AIPluginOperation_DVTableSearch_DVTableSe](dvtablesearch.md#BKMK_AIPluginOperation_DVTableSearch_DVTableSe) one-to-many relationship for the [dvtablesearch](dvtablesearch.md) table/entity.

### <a name="BKMK_AIPluginOperation_Entity_Entity"></a> AIPluginOperation_Entity_Entity

**Added by**: System Solution Solution

See the [AIPluginOperation_Entity_Entity](entity.md#BKMK_AIPluginOperation_Entity_Entity) one-to-many relationship for the [entity](entity.md) table/entity.

### <a name="BKMK_AIPluginOperation_Workflow_Workflow"></a> AIPluginOperation_Workflow_Workflow

**Added by**: System Solution Solution

See the [AIPluginOperation_Workflow_Workflow](workflow.md#BKMK_AIPluginOperation_Workflow_Workflow) one-to-many relationship for the [workflow](workflow.md) table/entity.

### <a name="BKMK_operationresponsetemplate_aipluginoperation"></a> operationresponsetemplate_aipluginoperation

See the [operationresponsetemplate_aipluginoperation](aipluginoperationresponsetemplate.md#BKMK_operationresponsetemplate_aipluginoperation) one-to-many relationship for the [aipluginoperationresponsetemplate](aipluginoperationresponsetemplate.md) table/entity.

### <a name="BKMK_msdyn_AIPluginOperation_AIModel"></a> msdyn_AIPluginOperation_AIModel

**Added by**: AISolution Solution

See the [msdyn_AIPluginOperation_AIModel](msdyn_aimodel.md#BKMK_msdyn_AIPluginOperation_AIModel) one-to-many relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the AIPluginOperation table is the first table in the relationship. Listed by **SchemaName**.


### <a name="BKMK_botcomponent_aipluginoperation"></a> botcomponent_aipluginoperation

See the [botcomponent_aipluginoperation](botcomponent.md#BKMK_botcomponent_aipluginoperation) many-to-many relationship for the [botcomponent](botcomponent.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.aipluginoperation?text=aipluginoperation EntityType" />