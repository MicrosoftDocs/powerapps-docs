---
title: "msdyn_DataflowTemplate table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the msdyn_DataflowTemplate table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# msdyn_DataflowTemplate table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

An entity to store information about dataflow templates

**Added by**: Insights App Platform Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /msdyn_dataflowtemplates(*msdyn_dataflowtemplateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /msdyn_dataflowtemplates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msdyn_dataflowtemplates(*msdyn_dataflowtemplateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /msdyn_dataflowtemplates(*msdyn_dataflowtemplateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /msdyn_dataflowtemplates<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /msdyn_dataflowtemplates(*msdyn_dataflowtemplateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /msdyn_dataflowtemplates(*msdyn_dataflowtemplateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_DataflowTemplates|
|DisplayCollectionName|Dataflow Templates|
|DisplayName|Dataflow Template|
|EntitySetName|msdyn_dataflowtemplates|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_dataflowtemplates|
|LogicalName|msdyn_dataflowtemplate|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_dataflowtemplateid|
|PrimaryNameAttribute|msdyn_uniquename|
|SchemaName|msdyn_DataflowTemplate|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [msdyn_Category](#BKMK_msdyn_Category)
- [msdyn_Configuration](#BKMK_msdyn_Configuration)
- [msdyn_DataflowTemplateId](#BKMK_msdyn_DataflowTemplateId)
- [msdyn_Description](#BKMK_msdyn_Description)
- [msdyn_HelpLink](#BKMK_msdyn_HelpLink)
- [msdyn_IsDisabled](#BKMK_msdyn_IsDisabled)
- [msdyn_MashupDocument](#BKMK_msdyn_MashupDocument)
- [msdyn_TemplateIcon](#BKMK_msdyn_TemplateIcon)
- [msdyn_TemplateName](#BKMK_msdyn_TemplateName)
- [msdyn_TemplateState](#BKMK_msdyn_TemplateState)
- [msdyn_TemplateVersion](#BKMK_msdyn_TemplateVersion)
- [msdyn_UniqueName](#BKMK_msdyn_UniqueName)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


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


### <a name="BKMK_msdyn_Category"></a> msdyn_Category

|Property|Value|
|--------|-----|
|Description|Template category|
|DisplayName|Category|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_category|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_Configuration"></a> msdyn_Configuration

|Property|Value|
|--------|-----|
|Description|The template configuration|
|DisplayName|Template Configuration|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_configuration|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_DataflowTemplateId"></a> msdyn_DataflowTemplateId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Dataflow Template|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_dataflowtemplateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_Description"></a> msdyn_Description

|Property|Value|
|--------|-----|
|Description|Description of template|
|DisplayName|Description|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_description|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_HelpLink"></a> msdyn_HelpLink

|Property|Value|
|--------|-----|
|Description|URL to help document|
|DisplayName|Help Link|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_helplink|
|MaxLength|2100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_IsDisabled"></a> msdyn_IsDisabled

|Property|Value|
|--------|-----|
|Description|Indicates if template is disabled|
|DisplayName|Is Disabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isdisabled|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_IsDisabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|True||
|0|False||

**DefaultValue**: 0



### <a name="BKMK_msdyn_MashupDocument"></a> msdyn_MashupDocument

|Property|Value|
|--------|-----|
|Description|The mashup document|
|DisplayName|Mashup Document|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_mashupdocument|
|MaxLength|1048576|
|RequiredLevel|SystemRequired|
|Type|Memo|


### <a name="BKMK_msdyn_TemplateIcon"></a> msdyn_TemplateIcon

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|The dataflow template icon|
|DisplayName|Template Icon|
|IsPrimaryImage|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_templateicon|
|MaxHeight|144|
|MaxWidth|144|
|RequiredLevel|None|
|Type|Image|


### <a name="BKMK_msdyn_TemplateName"></a> msdyn_TemplateName

|Property|Value|
|--------|-----|
|Description|The template name|
|DisplayName|Template Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_templatename|
|MaxLength|400|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_msdyn_TemplateState"></a> msdyn_TemplateState

|Property|Value|
|--------|-----|
|Description|The template state|
|DisplayName|Template State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_templatestate|
|RequiredLevel|None|
|Type|Picklist|

#### msdyn_TemplateState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|100000000|Draft||
|100000001|Active||
|100000002|Published||
|100000003|Deprecated||



### <a name="BKMK_msdyn_TemplateVersion"></a> msdyn_TemplateVersion

|Property|Value|
|--------|-----|
|Description|The template version|
|DisplayName|Template Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_templateversion|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_UniqueName"></a> msdyn_UniqueName

|Property|Value|
|--------|-----|
|Description|The unique name of the dataflow template|
|DisplayName|Template Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_uniquename|
|MaxLength|400|
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


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Dataflow Template|
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
|Description|Reason for the status of the Dataflow Template|
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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [msdyn_TemplateIcon_Timestamp](#BKMK_msdyn_TemplateIcon_Timestamp)
- [msdyn_TemplateIcon_URL](#BKMK_msdyn_TemplateIcon_URL)
- [msdyn_TemplateIconId](#BKMK_msdyn_TemplateIconId)
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


### <a name="BKMK_msdyn_TemplateIcon_Timestamp"></a> msdyn_TemplateIcon_Timestamp

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_templateicon_timestamp|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_msdyn_TemplateIcon_URL"></a> msdyn_TemplateIcon_URL

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_templateicon_url|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_TemplateIconId"></a> msdyn_TemplateIconId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_templateiconid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [msdyn_dataflowtemplate_SyncErrors](#BKMK_msdyn_dataflowtemplate_SyncErrors)
- [msdyn_dataflowtemplate_AsyncOperations](#BKMK_msdyn_dataflowtemplate_AsyncOperations)
- [msdyn_dataflowtemplate_MailboxTrackingFolders](#BKMK_msdyn_dataflowtemplate_MailboxTrackingFolders)
- [msdyn_dataflowtemplate_ProcessSession](#BKMK_msdyn_dataflowtemplate_ProcessSession)
- [msdyn_dataflowtemplate_BulkDeleteFailures](#BKMK_msdyn_dataflowtemplate_BulkDeleteFailures)
- [msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses)


### <a name="BKMK_msdyn_dataflowtemplate_SyncErrors"></a> msdyn_dataflowtemplate_SyncErrors

**Added by**: System Solution Solution

Same as the [msdyn_dataflowtemplate_SyncErrors](syncerror.md#BKMK_msdyn_dataflowtemplate_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_dataflowtemplate_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_dataflowtemplate_AsyncOperations"></a> msdyn_dataflowtemplate_AsyncOperations

**Added by**: System Solution Solution

Same as the [msdyn_dataflowtemplate_AsyncOperations](asyncoperation.md#BKMK_msdyn_dataflowtemplate_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_dataflowtemplate_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_dataflowtemplate_MailboxTrackingFolders"></a> msdyn_dataflowtemplate_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msdyn_dataflowtemplate_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_dataflowtemplate_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_dataflowtemplate_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_dataflowtemplate_ProcessSession"></a> msdyn_dataflowtemplate_ProcessSession

**Added by**: System Solution Solution

Same as the [msdyn_dataflowtemplate_ProcessSession](processsession.md#BKMK_msdyn_dataflowtemplate_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_dataflowtemplate_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_dataflowtemplate_BulkDeleteFailures"></a> msdyn_dataflowtemplate_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msdyn_dataflowtemplate_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_dataflowtemplate_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_dataflowtemplate_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses"></a> msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_dataflowtemplate_createdby](#BKMK_lk_msdyn_dataflowtemplate_createdby)
- [lk_msdyn_dataflowtemplate_createdonbehalfby](#BKMK_lk_msdyn_dataflowtemplate_createdonbehalfby)
- [lk_msdyn_dataflowtemplate_modifiedby](#BKMK_lk_msdyn_dataflowtemplate_modifiedby)
- [lk_msdyn_dataflowtemplate_modifiedonbehalfby](#BKMK_lk_msdyn_dataflowtemplate_modifiedonbehalfby)
- [user_msdyn_dataflowtemplate](#BKMK_user_msdyn_dataflowtemplate)
- [team_msdyn_dataflowtemplate](#BKMK_team_msdyn_dataflowtemplate)
- [business_unit_msdyn_dataflowtemplate](#BKMK_business_unit_msdyn_dataflowtemplate)


### <a name="BKMK_lk_msdyn_dataflowtemplate_createdby"></a> lk_msdyn_dataflowtemplate_createdby

**Added by**: System Solution Solution

See the [lk_msdyn_dataflowtemplate_createdby](systemuser.md#BKMK_lk_msdyn_dataflowtemplate_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_dataflowtemplate_createdonbehalfby"></a> lk_msdyn_dataflowtemplate_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_dataflowtemplate_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_dataflowtemplate_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_dataflowtemplate_modifiedby"></a> lk_msdyn_dataflowtemplate_modifiedby

**Added by**: System Solution Solution

See the [lk_msdyn_dataflowtemplate_modifiedby](systemuser.md#BKMK_lk_msdyn_dataflowtemplate_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_dataflowtemplate_modifiedonbehalfby"></a> lk_msdyn_dataflowtemplate_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_dataflowtemplate_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_dataflowtemplate_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_msdyn_dataflowtemplate"></a> user_msdyn_dataflowtemplate

**Added by**: System Solution Solution

See the [user_msdyn_dataflowtemplate](systemuser.md#BKMK_user_msdyn_dataflowtemplate) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_msdyn_dataflowtemplate"></a> team_msdyn_dataflowtemplate

**Added by**: System Solution Solution

See the [team_msdyn_dataflowtemplate](team.md#BKMK_team_msdyn_dataflowtemplate) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_msdyn_dataflowtemplate"></a> business_unit_msdyn_dataflowtemplate

**Added by**: System Solution Solution

See the [business_unit_msdyn_dataflowtemplate](businessunit.md#BKMK_business_unit_msdyn_dataflowtemplate) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msdyn_dataflowtemplate?text=msdyn_dataflowtemplate EntityType" />