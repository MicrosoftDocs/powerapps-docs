---
title: "App Action (appaction) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the App Action (appaction) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# App Action (appaction) table/entity reference (Microsoft Dataverse)

Contains Modern Command Information

## Messages

The following table lists the messages for the App Action (appaction) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /appactions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /appactions(*appactionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /appactions(*appactionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /appactions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /appactions(*appactionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /appactions(*appactionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /appactions(*appactionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the App Action (appaction) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the App Action (appaction) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **App Action** |
| **DisplayCollectionName** | **App Actions** |
| **SchemaName** | `appaction` |
| **CollectionSchemaName** | `appactions` |
| **EntitySetName** | `appactions`|
| **LogicalName** | `appaction` |
| **LogicalCollectionName** | `appactions` |
| **PrimaryIdAttribute** | `appactionid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

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
- [GroupTitle](#BKMK_GroupTitle)
- [Hidden](#BKMK_Hidden)
- [IconWebResourceId](#BKMK_IconWebResourceId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsDisabled](#BKMK_IsDisabled)
- [isGroupTitleHidden](#BKMK_isGroupTitleHidden)
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
- [Origin](#BKMK_Origin)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ParentAppActionId](#BKMK_ParentAppActionId)
- [Sequence](#BKMK_Sequence)
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
- [VisibilityType](#BKMK_VisibilityType)

### <a name="BKMK_appactionId"></a> appactionId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**App Action**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appactionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AppModuleId"></a> AppModuleId

|Property|Value|
|---|---|
|Description|**Unique identifier for AppModule associated with Modern Command**|
|DisplayName|**App Module Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`appmoduleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|appmodule|

### <a name="BKMK_ButtonAccessibilityText"></a> ButtonAccessibilityText

|Property|Value|
|---|---|
|Description||
|DisplayName|**Accessibility Text for Modern Command Button**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`buttonaccessibilitytext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|256|

### <a name="BKMK_ButtonLabelText"></a> ButtonLabelText

|Property|Value|
|---|---|
|Description|**Label Text renders for Modern Command Button**|
|DisplayName|**Button Label Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`buttonlabeltext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|256|

### <a name="BKMK_ButtonSequencePriority"></a> ButtonSequencePriority

|Property|Value|
|---|---|
|Description|**Order of the Modern Command Button (Depreciated)**|
|DisplayName|**Button Sequence Priority (Depreciated)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`buttonsequencepriority`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|0|
|Precision|10|
|SourceTypeMask|0|

### <a name="BKMK_ButtonTooltipDescription"></a> ButtonTooltipDescription

|Property|Value|
|---|---|
|Description|**Tooltip Description for Modern Command Button**|
|DisplayName|**Button Tooltip Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`buttontooltipdescription`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|500|

### <a name="BKMK_ButtonTooltipTitle"></a> ButtonTooltipTitle

|Property|Value|
|---|---|
|Description|**Tooltip Title for Modern Command Button**|
|DisplayName|**Button Tooltip Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`buttontooltiptitle`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|256|

### <a name="BKMK_ClientType"></a> ClientType

|Property|Value|
|---|---|
|Description|**Client Type associated with Modern Command**|
|DisplayName|**Client Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`clienttype`|
|RequiredLevel|None|
|Type|MultiSelectPicklist|
|DefaultFormValue||
|GlobalChoiceName|`appaction_clienttype`|

#### ClientType Choices/Options

|Value|Label|
|---|---|
|0|**Browser**|
|1|**Mobile**|
|2|**Mail App**|

### <a name="BKMK_Context"></a> Context

|Property|Value|
|---|---|
|Description|**Context scope associated with Modern Command**|
|DisplayName|**Context**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`context`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`appaction_context`|

#### Context Choices/Options

|Value|Label|
|---|---|
|0|**All**|
|1|**Entity**|

### <a name="BKMK_ContextEntity"></a> ContextEntity

|Property|Value|
|---|---|
|Description|**Context Entity associated with Modern Command**|
|DisplayName|**Context Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contextentity`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|entity|

### <a name="BKMK_ContextValue"></a> ContextValue

|Property|Value|
|---|---|
|Description|**Context Name associated with Modern Command**|
|DisplayName|**Context Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contextvalue`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|150|

### <a name="BKMK_FontIcon"></a> FontIcon

|Property|Value|
|---|---|
|Description|**Font Icon for Modern Command Button**|
|DisplayName|**Font Icon**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fonticon`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_GroupTitle"></a> GroupTitle

|Property|Value|
|---|---|
|Description|**Group Title for Modern Command Group Button**|
|DisplayName|**Group Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`grouptitle`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|256|

### <a name="BKMK_Hidden"></a> Hidden

|Property|Value|
|---|---|
|Description||
|DisplayName|**Hidden**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`hidden`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`appaction_hidden`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IconWebResourceId"></a> IconWebResourceId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Icon Webresource from Webresource entity which used by the associated Modern Command**|
|DisplayName|**Icon WebResource Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iconwebresourceid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|webresource|

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

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsDisabled"></a> IsDisabled

|Property|Value|
|---|---|
|Description|**Flag indicates the Modern Command Button is disabled for end user usage i.e. ribbon equivalent will be shown**|
|DisplayName|**IsDisabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdisabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`appaction_isdisabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_isGroupTitleHidden"></a> isGroupTitleHidden

|Property|Value|
|---|---|
|Description|**Flag indicates the Modern Command Group Button Title is hidden**|
|DisplayName|**isGroupTitleHidden**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isgrouptitlehidden`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`appaction_isgrouptitlehidden`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Location"></a> Location

|Property|Value|
|---|---|
|Description|**Location of the Command bar associated with the Modern Command.**|
|DisplayName|**Location**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`location`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`appaction_location`|

#### Location Choices/Options

|Value|Label|
|---|---|
|0|**Form**|
|1|**Main Grid**|
|2|**Sub Grid**|
|3|**Associated Grid**|
|4|**Quick Form**|
|5|**Global Header**|
|6|**Dashboard**|

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The name of the AppAction entity.**|
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
|MaxLength|256|

### <a name="BKMK_OnClickEventFormulaComponentLibrary"></a> OnClickEventFormulaComponentLibrary

|Property|Value|
|---|---|
|Description|**Name of the Component Library where FX Action stored.**|
|DisplayName|**On Click Event Formula Component Library**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onclickeventformulacomponentlibrary`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_OnClickEventFormulaComponentLibraryId"></a> OnClickEventFormulaComponentLibraryId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Component Library associated with Modern Command.**|
|DisplayName|**On Click Event Formula Component Library Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onclickeventformulacomponentlibraryid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|canvasapp|

### <a name="BKMK_OnClickEventFormulaComponentName"></a> OnClickEventFormulaComponentName

|Property|Value|
|---|---|
|Description|**Name of the Component for FX Modern Command.**|
|DisplayName|**On Click Event Formula Component Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onclickeventformulacomponentname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_OnClickEventFormulaFunctionName"></a> OnClickEventFormulaFunctionName

|Property|Value|
|---|---|
|Description|**Name of the Function for FX Modern Command.**|
|DisplayName|**On Click Event Formula Function Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onclickeventformulafunctionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_OnClickEventJavaScriptFunctionName"></a> OnClickEventJavaScriptFunctionName

|Property|Value|
|---|---|
|Description|**Name of the Function for JS Modern Command.**|
|DisplayName|**On Click Event JavaScript Function Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onclickeventjavascriptfunctionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

### <a name="BKMK_OnClickEventJavaScriptParameters"></a> OnClickEventJavaScriptParameters

|Property|Value|
|---|---|
|Description|**Parameters of the Function for JS Modern Command.**|
|DisplayName|**On Click Event JavaScript Parameters**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onclickeventjavascriptparameters`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_OnClickEventJavaScriptWebResourceId"></a> OnClickEventJavaScriptWebResourceId

|Property|Value|
|---|---|
|Description|**Unique identifier of the JavaScript WebResource from the Webresource entity which used by associated JS Modern Command.**|
|DisplayName|**On Click Event JavaScript WebResource Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onclickeventjavascriptwebresourceid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|webresource|

### <a name="BKMK_OnClickEventType"></a> OnClickEventType

|Property|Value|
|---|---|
|Description|**Type of Action associated with Modern Command.**|
|DisplayName|**On Click Event Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onclickeventtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`appaction_onclickeventtype`|

#### OnClickEventType Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Formula**|
|2|**JavaScript**|

### <a name="BKMK_Origin"></a> Origin

|Property|Value|
|---|---|
|Description|**Origin of App Action.**|
|DisplayName|**Origin**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`origin`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`appaction_origin`|

#### Origin Choices/Options

|Value|Label|
|---|---|
|0|**Default**|
|1|**Migrated**|
|2|**Enhanced Migrated**|

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

### <a name="BKMK_ParentAppActionId"></a> ParentAppActionId

|Property|Value|
|---|---|
|Description|**Unique identifier for Parent Modern Command associated with Modern Command.**|
|DisplayName|**Parent AppAction**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentappactionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|appaction|

### <a name="BKMK_Sequence"></a> Sequence

|Property|Value|
|---|---|
|Description|**Order of the Modern Command to be Displayed.**|
|DisplayName|**Sequence**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sequence`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|0|
|Precision|10|
|SourceTypeMask|0|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the App Action**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`appaction_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the App Action**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`appaction_statuscode`|

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

### <a name="BKMK_Type"></a> Type

|Property|Value|
|---|---|
|Description|**Type of Modern Command Button**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`appaction_type`|

#### Type Choices/Options

|Value|Label|
|---|---|
|0|**Standard Button**|
|1|**Dropdown Button**|
|2|**Split Button**|
|3|**Group**|

### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|---|---|
|Description|**Unique Name of the AppAction**|
|DisplayName|**Unique Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniquename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

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

### <a name="BKMK_VisibilityFormulaComponentLibrary"></a> VisibilityFormulaComponentLibrary

|Property|Value|
|---|---|
|Description|**Name of the Component Library where FX Visible Rule stored associated with Modern Command.**|
|DisplayName|**Visibility Formula Component Library**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`visibilityformulacomponentlibrary`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_VisibilityFormulaComponentLibraryId"></a> VisibilityFormulaComponentLibraryId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Component Library associated with Modern Command.**|
|DisplayName|**Visibility Formula Component Library Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`visibilityformulacomponentlibraryid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|canvasapp|

### <a name="BKMK_VisibilityFormulaComponentName"></a> VisibilityFormulaComponentName

|Property|Value|
|---|---|
|Description|**Name of the Component for FX Visible Rule associated with Modern Command.**|
|DisplayName|**Visibility Formula Component Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`visibilityformulacomponentname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_VisibilityFormulaFunctionName"></a> VisibilityFormulaFunctionName

|Property|Value|
|---|---|
|Description|**Name of the Function for FX Visible Rule assoicated with Modern Command.**|
|DisplayName|**Visibility Formula Function Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`visibilityformulafunctionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_VisibilityType"></a> VisibilityType

|Property|Value|
|---|---|
|Description|**Visibily Type of the Modern Command which should be either FX/Classic or None.**|
|DisplayName|**Visibility Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`visibilitytype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`appaction_visibilitytype`|

#### VisibilityType Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Formula**|
|2|**Classic Rules**|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
|DefaultFormValue||
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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
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
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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
|Description|**Version Number**|
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

- [appaction_appaction](#BKMK_appaction_appaction-many-to-one)
- [appmodule_appaction_appmoduleid](#BKMK_appmodule_appaction_appmoduleid)
- [canvasapp_appaction_onclickeventformulacomponentlibraryid](#BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid)
- [canvasapp_appaction_visibilityformulacomponentlibraryid](#BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid)
- [entity_appaction_ContextEntity](#BKMK_entity_appaction_ContextEntity)
- [lk_appaction_createdby](#BKMK_lk_appaction_createdby)
- [lk_appaction_createdonbehalfby](#BKMK_lk_appaction_createdonbehalfby)
- [lk_appaction_modifiedby](#BKMK_lk_appaction_modifiedby)
- [lk_appaction_modifiedonbehalfby](#BKMK_lk_appaction_modifiedonbehalfby)
- [organization_appaction](#BKMK_organization_appaction)
- [webresource_appaction_iconwebresourceid](#BKMK_webresource_appaction_iconwebresourceid)
- [webresource_appaction_onclickeventjavascriptwebresourceid](#BKMK_webresource_appaction_onclickeventjavascriptwebresourceid)

### <a name="BKMK_appaction_appaction-many-to-one"></a> appaction_appaction

One-To-Many Relationship: [appaction appaction_appaction](#BKMK_appaction_appaction-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`appaction`|
|ReferencedAttribute|`appactionid`|
|ReferencingAttribute|`parentappactionid`|
|ReferencingEntityNavigationPropertyName|`ParentAppActionId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appmodule_appaction_appmoduleid"></a> appmodule_appaction_appmoduleid

One-To-Many Relationship: [appmodule appmodule_appaction_appmoduleid](appmodule.md#BKMK_appmodule_appaction_appmoduleid)

|Property|Value|
|---|---|
|ReferencedEntity|`appmodule`|
|ReferencedAttribute|`appmoduleid`|
|ReferencingAttribute|`appmoduleid`|
|ReferencingEntityNavigationPropertyName|`AppModuleId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid"></a> canvasapp_appaction_onclickeventformulacomponentlibraryid

One-To-Many Relationship: [canvasapp canvasapp_appaction_onclickeventformulacomponentlibraryid](canvasapp.md#BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid)

|Property|Value|
|---|---|
|ReferencedEntity|`canvasapp`|
|ReferencedAttribute|`canvasappid`|
|ReferencingAttribute|`onclickeventformulacomponentlibraryid`|
|ReferencingEntityNavigationPropertyName|`OnClickEventFormulaComponentLibraryId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid"></a> canvasapp_appaction_visibilityformulacomponentlibraryid

One-To-Many Relationship: [canvasapp canvasapp_appaction_visibilityformulacomponentlibraryid](canvasapp.md#BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid)

|Property|Value|
|---|---|
|ReferencedEntity|`canvasapp`|
|ReferencedAttribute|`canvasappid`|
|ReferencingAttribute|`visibilityformulacomponentlibraryid`|
|ReferencingEntityNavigationPropertyName|`VisibilityFormulaComponentLibraryId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entity_appaction_ContextEntity"></a> entity_appaction_ContextEntity

One-To-Many Relationship: [entity entity_appaction_ContextEntity](entity.md#BKMK_entity_appaction_ContextEntity)

|Property|Value|
|---|---|
|ReferencedEntity|`entity`|
|ReferencedAttribute|`entityid`|
|ReferencingAttribute|`contextentity`|
|ReferencingEntityNavigationPropertyName|`ContextEntity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appaction_createdby"></a> lk_appaction_createdby

One-To-Many Relationship: [systemuser lk_appaction_createdby](systemuser.md#BKMK_lk_appaction_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appaction_createdonbehalfby"></a> lk_appaction_createdonbehalfby

One-To-Many Relationship: [systemuser lk_appaction_createdonbehalfby](systemuser.md#BKMK_lk_appaction_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appaction_modifiedby"></a> lk_appaction_modifiedby

One-To-Many Relationship: [systemuser lk_appaction_modifiedby](systemuser.md#BKMK_lk_appaction_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appaction_modifiedonbehalfby"></a> lk_appaction_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_appaction_modifiedonbehalfby](systemuser.md#BKMK_lk_appaction_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_appaction"></a> organization_appaction

One-To-Many Relationship: [organization organization_appaction](organization.md#BKMK_organization_appaction)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_webresource_appaction_iconwebresourceid"></a> webresource_appaction_iconwebresourceid

One-To-Many Relationship: [webresource webresource_appaction_iconwebresourceid](webresource.md#BKMK_webresource_appaction_iconwebresourceid)

|Property|Value|
|---|---|
|ReferencedEntity|`webresource`|
|ReferencedAttribute|`webresourceid`|
|ReferencingAttribute|`iconwebresourceid`|
|ReferencingEntityNavigationPropertyName|`IconWebResourceId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_webresource_appaction_onclickeventjavascriptwebresourceid"></a> webresource_appaction_onclickeventjavascriptwebresourceid

One-To-Many Relationship: [webresource webresource_appaction_onclickeventjavascriptwebresourceid](webresource.md#BKMK_webresource_appaction_onclickeventjavascriptwebresourceid)

|Property|Value|
|---|---|
|ReferencedEntity|`webresource`|
|ReferencedAttribute|`webresourceid`|
|ReferencingAttribute|`onclickeventjavascriptwebresourceid`|
|ReferencingEntityNavigationPropertyName|`OnClickEventJavaScriptWebResourceId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [appaction_appaction](#BKMK_appaction_appaction-one-to-many)
- [appaction_AsyncOperations](#BKMK_appaction_AsyncOperations)
- [appaction_BulkDeleteFailures](#BKMK_appaction_BulkDeleteFailures)
- [appaction_MailboxTrackingFolders](#BKMK_appaction_MailboxTrackingFolders)
- [appaction_PrincipalObjectAttributeAccesses](#BKMK_appaction_PrincipalObjectAttributeAccesses)
- [appaction_ProcessSession](#BKMK_appaction_ProcessSession)
- [appaction_SyncErrors](#BKMK_appaction_SyncErrors)

### <a name="BKMK_appaction_appaction-one-to-many"></a> appaction_appaction

Many-To-One Relationship: [appaction appaction_appaction](#BKMK_appaction_appaction-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`appaction`|
|ReferencingAttribute|`parentappactionid`|
|ReferencedEntityNavigationPropertyName|`appaction_appaction`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appaction_AsyncOperations"></a> appaction_AsyncOperations

Many-To-One Relationship: [asyncoperation appaction_AsyncOperations](asyncoperation.md#BKMK_appaction_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`appaction_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appaction_BulkDeleteFailures"></a> appaction_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure appaction_BulkDeleteFailures](bulkdeletefailure.md#BKMK_appaction_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`appaction_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appaction_MailboxTrackingFolders"></a> appaction_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder appaction_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_appaction_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`appaction_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appaction_PrincipalObjectAttributeAccesses"></a> appaction_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess appaction_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_appaction_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`appaction_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appaction_ProcessSession"></a> appaction_ProcessSession

Many-To-One Relationship: [processsession appaction_ProcessSession](processsession.md#BKMK_appaction_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`appaction_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appaction_SyncErrors"></a> appaction_SyncErrors

Many-To-One Relationship: [syncerror appaction_SyncErrors](syncerror.md#BKMK_appaction_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`appaction_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_appaction_appactionrule_classicrules"></a> appaction_appactionrule_classicrules

See [appactionrule appaction_appactionrule_classicrules Many-To-Many Relationship](appactionrule.md#BKMK_appaction_appactionrule_classicrules)

|Property|Value|
|---|---|
|IntersectEntityName|`appaction_appactionrule_classicrules`|
|IsCustomizable|False|
|SchemaName|`appaction_appactionrule_classicrules`|
|IntersectAttribute|`appactionid`|
|NavigationPropertyName|`appaction_appactionrule_classicrules`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.appaction?displayProperty=fullName>
