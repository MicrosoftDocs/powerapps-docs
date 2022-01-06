---
title: "appaction table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the appaction table/entity."
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

# appaction table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Apps Actions Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/appactions<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/appactions(*appactionid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref href="Microsoft.Dynamics.CRM.IsValidStateTransition?text=IsValidStateTransition Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/appactions(*appactionid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/appactions<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH [*org URI*]/api/data/v9.0/appactions(*appactionid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/appactions(*appactionid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|appactions|
|DisplayCollectionName|App Actions|
|DisplayName|App Action|
|EntitySetName|appactions|
|IsBPFEntity|False|
|LogicalCollectionName|appactions|
|LogicalName|appaction|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|appactionid|
|PrimaryNameAttribute|name|
|SchemaName|appaction|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [appactionId](#BKMK_appactionId)
- [AppModuleId](#BKMK_AppModuleId)
- [ButtonAccessibilityText](#BKMK_ButtonAccessibilityText)
- [ButtonLabelText](#BKMK_ButtonLabelText)
- [ButtonSequencePriority](#BKMK_ButtonSequencePriority)
- [ButtonTooltipDescription](#BKMK_ButtonTooltipDescription)
- [ButtonTooltipTitle](#BKMK_ButtonTooltipTitle)
- [ClientType](#BKMK_ClientType)
- [Context](#BKMK_Context)
- [ContextEntity](#BKMK_ContextEntity)
- [ContextValue](#BKMK_ContextValue)
- [FontIcon](#BKMK_FontIcon)
- [Hidden](#BKMK_Hidden)
- [IconWebResourceId](#BKMK_IconWebResourceId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [Location](#BKMK_Location)
- [name](#BKMK_name)
- [OnClickEventFormulaComponentLibrary](#BKMK_OnClickEventFormulaComponentLibrary)
- [OnClickEventFormulaComponentLibraryId](#BKMK_OnClickEventFormulaComponentLibraryId)
- [OnClickEventFormulaComponentName](#BKMK_OnClickEventFormulaComponentName)
- [OnClickEventFormulaFunctionName](#BKMK_OnClickEventFormulaFunctionName)
- [OnClickEventJavaScriptFunctionName](#BKMK_OnClickEventJavaScriptFunctionName)
- [OnClickEventJavaScriptParameters](#BKMK_OnClickEventJavaScriptParameters)
- [OnClickEventJavaScriptWebResourceId](#BKMK_OnClickEventJavaScriptWebResourceId)
- [OnClickEventType](#BKMK_OnClickEventType)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Type](#BKMK_Type)
- [UniqueName](#BKMK_UniqueName)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [VisibilityFormulaComponentLibrary](#BKMK_VisibilityFormulaComponentLibrary)
- [VisibilityFormulaComponentLibraryId](#BKMK_VisibilityFormulaComponentLibraryId)
- [VisibilityFormulaComponentName](#BKMK_VisibilityFormulaComponentName)
- [VisibilityFormulaFunctionName](#BKMK_VisibilityFormulaFunctionName)


### <a name="BKMK_appactionId"></a> appactionId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|App Action|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|appactionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_AppModuleId"></a> AppModuleId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|App Module Id|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|appmoduleid|
|RequiredLevel|None|
|Targets|appmodule|
|Type|Lookup|


### <a name="BKMK_ButtonAccessibilityText"></a> ButtonAccessibilityText

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Button Accessibility Text|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|buttonaccessibilitytext|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ButtonLabelText"></a> ButtonLabelText

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Button Label Text|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|buttonlabeltext|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ButtonSequencePriority"></a> ButtonSequencePriority

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Button Sequence Priority|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|buttonsequencepriority|
|MaxValue|100000000000|
|MinValue|0|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_ButtonTooltipDescription"></a> ButtonTooltipDescription

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Button Tooltip Description|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|buttontooltipdescription|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ButtonTooltipTitle"></a> ButtonTooltipTitle

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Button Tooltip Title|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|buttontooltiptitle|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ClientType"></a> ClientType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Client Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|clienttype|
|RequiredLevel|None|
|Type|MultiSelectPicklist|

#### ClientType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Browser||
|1|Mobile||
|2|Mail App||



### <a name="BKMK_Context"></a> Context

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Context|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|context|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### Context Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|All||
|1|Entity||



### <a name="BKMK_ContextEntity"></a> ContextEntity

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Context Entity|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|contextentity|
|RequiredLevel|None|
|Targets|entity|
|Type|Lookup|


### <a name="BKMK_ContextValue"></a> ContextValue

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Context Value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|contextvalue|
|MaxLength|150|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FontIcon"></a> FontIcon

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Font Icon|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fonticon|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Hidden"></a> Hidden

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Hidden|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|hidden|
|RequiredLevel|None|
|Type|Boolean|

#### Hidden Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IconWebResourceId"></a> IconWebResourceId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Icon WebResource Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|iconwebresourceid|
|RequiredLevel|None|
|Targets|webresource|
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


### <a name="BKMK_Location"></a> Location

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Location|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|location|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### Location Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Form||
|1|Main Grid||
|2|Sub Grid||
|3|Associated Grid||
|4|Quick Form||
|5|Global Header||
|6|Dashboard||



### <a name="BKMK_name"></a> name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OnClickEventFormulaComponentLibrary"></a> OnClickEventFormulaComponentLibrary

|Property|Value|
|--------|-----|
|Description||
|DisplayName|On Click Event Formula Component Library|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onclickeventformulacomponentlibrary|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnClickEventFormulaComponentLibraryId"></a> OnClickEventFormulaComponentLibraryId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|On Click Event Formula Component Library Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onclickeventformulacomponentlibraryid|
|RequiredLevel|None|
|Targets|canvasapp|
|Type|Lookup|


### <a name="BKMK_OnClickEventFormulaComponentName"></a> OnClickEventFormulaComponentName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|On Click Event Formula Component Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onclickeventformulacomponentname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnClickEventFormulaFunctionName"></a> OnClickEventFormulaFunctionName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|On Click Event Formula Function Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onclickeventformulafunctionname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnClickEventJavaScriptFunctionName"></a> OnClickEventJavaScriptFunctionName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|On Click Event JavaScript Function Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onclickeventjavascriptfunctionname|
|MaxLength|300|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnClickEventJavaScriptParameters"></a> OnClickEventJavaScriptParameters

|Property|Value|
|--------|-----|
|Description||
|DisplayName|On Click Event JavaScript Parameters|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onclickeventjavascriptparameters|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnClickEventJavaScriptWebResourceId"></a> OnClickEventJavaScriptWebResourceId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|On Click Event JavaScript WebResource Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onclickeventjavascriptwebresourceid|
|RequiredLevel|None|
|Targets|webresource|
|Type|Lookup|


### <a name="BKMK_OnClickEventType"></a> OnClickEventType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|On Click Event Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onclickeventtype|
|RequiredLevel|None|
|Type|Picklist|

#### OnClickEventType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None||
|1|Formula||
|2|JavaScript||



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


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the App Action|
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
|Description|Reason for the status of the App Action|
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


### <a name="BKMK_Type"></a> Type

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|type|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### Type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Standard Button||
|1|Dropdown Button||
|2|Split Button||



### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|uniquename|
|MaxLength|300|
|RequiredLevel|SystemRequired|
|Type|String|


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


### <a name="BKMK_VisibilityFormulaComponentLibrary"></a> VisibilityFormulaComponentLibrary

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Visibility Formula Component Library|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|visibilityformulacomponentlibrary|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VisibilityFormulaComponentLibraryId"></a> VisibilityFormulaComponentLibraryId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Visibility Formula Component Library Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|visibilityformulacomponentlibraryid|
|RequiredLevel|None|
|Targets|canvasapp|
|Type|Lookup|


### <a name="BKMK_VisibilityFormulaComponentName"></a> VisibilityFormulaComponentName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Visibility Formula Component Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|visibilityformulacomponentname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VisibilityFormulaFunctionName"></a> VisibilityFormulaFunctionName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Visibility Formula Function Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|visibilityformulafunctionname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AppModuleIdName](#BKMK_AppModuleIdName)
- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [ContextEntityName](#BKMK_ContextEntityName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IconWebResourceIdName](#BKMK_IconWebResourceIdName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OnClickEventFormulaComponentLibraryIdName](#BKMK_OnClickEventFormulaComponentLibraryIdName)
- [OnClickEventJavaScriptWebResourceIdName](#BKMK_OnClickEventJavaScriptWebResourceIdName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)
- [VisibilityFormulaComponentLibraryIdName](#BKMK_VisibilityFormulaComponentLibraryIdName)


### <a name="BKMK_AppModuleIdName"></a> AppModuleIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appmoduleidname|
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



### <a name="BKMK_ContextEntityName"></a> ContextEntityName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|contextentityname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_IconWebResourceIdName"></a> IconWebResourceIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iconwebresourceidname|
|MaxLength|256|
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
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



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


### <a name="BKMK_OnClickEventFormulaComponentLibraryIdName"></a> OnClickEventFormulaComponentLibraryIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|onclickeventformulacomponentlibraryidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnClickEventJavaScriptWebResourceIdName"></a> OnClickEventJavaScriptWebResourceIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|onclickeventjavascriptwebresourceidname|
|MaxLength|256|
|RequiredLevel|None|
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


### <a name="BKMK_VisibilityFormulaComponentLibraryIdName"></a> VisibilityFormulaComponentLibraryIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|visibilityformulacomponentlibraryidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [appaction_SyncErrors](#BKMK_appaction_SyncErrors)
- [appaction_AsyncOperations](#BKMK_appaction_AsyncOperations)
- [appaction_MailboxTrackingFolders](#BKMK_appaction_MailboxTrackingFolders)
- [appaction_ProcessSession](#BKMK_appaction_ProcessSession)
- [appaction_BulkDeleteFailures](#BKMK_appaction_BulkDeleteFailures)
- [appaction_PrincipalObjectAttributeAccesses](#BKMK_appaction_PrincipalObjectAttributeAccesses)


### <a name="BKMK_appaction_SyncErrors"></a> appaction_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [appaction_SyncErrors](syncerror.md#BKMK_appaction_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appaction_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appaction_AsyncOperations"></a> appaction_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [appaction_AsyncOperations](asyncoperation.md#BKMK_appaction_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appaction_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appaction_MailboxTrackingFolders"></a> appaction_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [appaction_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_appaction_MailboxTrackingFolders) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appaction_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appaction_ProcessSession"></a> appaction_ProcessSession

**Added by**: System Solution Solution

Same as processsession table [appaction_ProcessSession](processsession.md#BKMK_appaction_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appaction_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appaction_BulkDeleteFailures"></a> appaction_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [appaction_BulkDeleteFailures](bulkdeletefailure.md#BKMK_appaction_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appaction_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appaction_PrincipalObjectAttributeAccesses"></a> appaction_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [appaction_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_appaction_PrincipalObjectAttributeAccesses) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appaction_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_appaction_createdby](#BKMK_lk_appaction_createdby)
- [lk_appaction_createdonbehalfby](#BKMK_lk_appaction_createdonbehalfby)
- [lk_appaction_modifiedby](#BKMK_lk_appaction_modifiedby)
- [lk_appaction_modifiedonbehalfby](#BKMK_lk_appaction_modifiedonbehalfby)
- [organization_appaction](#BKMK_organization_appaction)
- [appmodule_appaction_appmoduleid](#BKMK_appmodule_appaction_appmoduleid)
- [canvasapp_appaction_onclickeventformulacomponentlibraryid](#BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid)
- [canvasapp_appaction_visibilityformulacomponentlibraryid](#BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid)
- [entity_appaction_ContextEntity](#BKMK_entity_appaction_ContextEntity)
- [webresource_appaction_iconwebresourceid](#BKMK_webresource_appaction_iconwebresourceid)
- [webresource_appaction_onclickeventjavascriptwebresourceid](#BKMK_webresource_appaction_onclickeventjavascriptwebresourceid)


### <a name="BKMK_lk_appaction_createdby"></a> lk_appaction_createdby

**Added by**: System Solution Solution

See systemuser Table [lk_appaction_createdby](systemuser.md#BKMK_lk_appaction_createdby) One-To-Many relationship.

### <a name="BKMK_lk_appaction_createdonbehalfby"></a> lk_appaction_createdonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_appaction_createdonbehalfby](systemuser.md#BKMK_lk_appaction_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_appaction_modifiedby"></a> lk_appaction_modifiedby

**Added by**: System Solution Solution

See systemuser Table [lk_appaction_modifiedby](systemuser.md#BKMK_lk_appaction_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_appaction_modifiedonbehalfby"></a> lk_appaction_modifiedonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_appaction_modifiedonbehalfby](systemuser.md#BKMK_lk_appaction_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_appaction"></a> organization_appaction

**Added by**: System Solution Solution

See organization Table [organization_appaction](organization.md#BKMK_organization_appaction) One-To-Many relationship.

### <a name="BKMK_appmodule_appaction_appmoduleid"></a> appmodule_appaction_appmoduleid

**Added by**: System Solution Solution

See appmodule Table [appmodule_appaction_appmoduleid](appmodule.md#BKMK_appmodule_appaction_appmoduleid) One-To-Many relationship.

### <a name="BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid"></a> canvasapp_appaction_onclickeventformulacomponentlibraryid

**Added by**: System Solution Solution

See canvasapp Table [canvasapp_appaction_onclickeventformulacomponentlibraryid](canvasapp.md#BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid) One-To-Many relationship.

### <a name="BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid"></a> canvasapp_appaction_visibilityformulacomponentlibraryid

**Added by**: System Solution Solution

See canvasapp Table [canvasapp_appaction_visibilityformulacomponentlibraryid](canvasapp.md#BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid) One-To-Many relationship.

### <a name="BKMK_entity_appaction_ContextEntity"></a> entity_appaction_ContextEntity

**Added by**: System Solution Solution

See entity Table [entity_appaction_ContextEntity](entity.md#BKMK_entity_appaction_ContextEntity) One-To-Many relationship.

### <a name="BKMK_webresource_appaction_iconwebresourceid"></a> webresource_appaction_iconwebresourceid

**Added by**: System Solution Solution

See webresource Table [webresource_appaction_iconwebresourceid](webresource.md#BKMK_webresource_appaction_iconwebresourceid) One-To-Many relationship.

### <a name="BKMK_webresource_appaction_onclickeventjavascriptwebresourceid"></a> webresource_appaction_onclickeventjavascriptwebresourceid

**Added by**: System Solution Solution

See webresource Table [webresource_appaction_onclickeventjavascriptwebresourceid](webresource.md#BKMK_webresource_appaction_onclickeventjavascriptwebresourceid) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.appaction?text=appaction EntityType" />