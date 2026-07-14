---
title: "CopilotExampleQuestion table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the CopilotExampleQuestion table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# CopilotExampleQuestion table/entity reference (Microsoft Dataverse)

CopilotExampleQuestions Component

## Messages

The following table lists the messages for the CopilotExampleQuestion table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /copilotexamplequestions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /copilotexamplequestions(*copilotexamplequestionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /copilotexamplequestions(*copilotexamplequestionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /copilotexamplequestions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /copilotexamplequestions(*copilotexamplequestionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /copilotexamplequestions(*copilotexamplequestionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /copilotexamplequestions(*copilotexamplequestionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the CopilotExampleQuestion table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the CopilotExampleQuestion table.

|Property|Value|
| --- | --- |
| **DisplayName** | **CopilotExampleQuestion** |
| **DisplayCollectionName** | **CopilotExampleQuestions** |
| **SchemaName** | `CopilotExampleQuestion` |
| **CollectionSchemaName** | `CopilotExampleQuestions` |
| **EntitySetName** | `copilotexamplequestions`|
| **LogicalName** | `copilotexamplequestion` |
| **LogicalCollectionName** | `copilotexamplequestions` |
| **PrimaryIdAttribute** | `copilotexamplequestionid` |
| **PrimaryNameAttribute** |`question` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AppContext](#BKMK_AppContext)
- [Comment](#BKMK_Comment)
- [CopilotExampleQuestionId](#BKMK_CopilotExampleQuestionId)
- [CustomDimension](#BKMK_CustomDimension)
- [CustomField](#BKMK_CustomField)
- [DynamicKnowledge](#BKMK_DynamicKnowledge)
- [EntityScope](#BKMK_EntityScope)
- [EntityScopeColumn](#BKMK_EntityScopeColumn)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [Knowledge](#BKMK_Knowledge)
- [knowledgetype](#BKMK_knowledgetype)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [Question](#BKMK_Question)
- [Rephrase](#BKMK_Rephrase)
- [Skill](#BKMK_Skill)
- [SkillId](#BKMK_SkillId)
- [SQLCorrectness](#BKMK_SQLCorrectness)
- [StandardSQL](#BKMK_StandardSQL)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AppContext"></a> AppContext

|Property|Value|
|---|---|
|Description|**AppContext for distinguishing between apps within the organization.**|
|DisplayName|**AppContext**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`appcontext`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20000|

### <a name="BKMK_Comment"></a> Comment

|Property|Value|
|---|---|
|Description|**Explanation of the question.**|
|DisplayName|**Comment**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`comment`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|20000|

### <a name="BKMK_CopilotExampleQuestionId"></a> CopilotExampleQuestionId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Copilot Example Question**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`copilotexamplequestionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_CustomDimension"></a> CustomDimension

|Property|Value|
|---|---|
|Description|**CustomDimension.**|
|DisplayName|**CustomDimension**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customdimension`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20000|

### <a name="BKMK_CustomField"></a> CustomField

|Property|Value|
|---|---|
|Description|**CustomField.**|
|DisplayName|**CustomField**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customfield`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20000|

### <a name="BKMK_DynamicKnowledge"></a> DynamicKnowledge

|Property|Value|
|---|---|
|Description|**DynamicKnowledge.**|
|DisplayName|**DynamicKnowledge**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dynamicknowledge`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|20000|

### <a name="BKMK_EntityScope"></a> EntityScope

|Property|Value|
|---|---|
|Description|**EntityScope that can be used to extract results. Format: \[entityscopeA\], \[entityscopeB\]**|
|DisplayName|**EntityScope**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityscope`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20000|

### <a name="BKMK_EntityScopeColumn"></a> EntityScopeColumn

|Property|Value|
|---|---|
|Description|**EntityScopeColumn within the EntityScope specified above.Format: \[EntityScopeA\].\[EntityScopeColumnA1\], \[EntityScopeB\].\[EntityScopeColumnB2\]**|
|DisplayName|**EntityScopeColumn**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityscopecolumn`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20000|

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

### <a name="BKMK_Knowledge"></a> Knowledge

|Property|Value|
|---|---|
|Description|**The information and understanding that the model has acquired through its training data.**|
|DisplayName|**Knowledge**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`knowledge`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|20000|

### <a name="BKMK_knowledgetype"></a> knowledgetype

|Property|Value|
|---|---|
|Description|**Knowledge Type: Example Question, Dynamic Knowledge.**|
|DisplayName|**Knowledge Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`knowledgetype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`copilotexamplequestiontknowledgetype`|

#### knowledgetype Choices/Options

|Value|Label|
|---|---|
|0|**Example Question**|
|1|**Example Knowledge**|

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

### <a name="BKMK_Question"></a> Question

|Property|Value|
|---|---|
|Description||
|DisplayName|**Question**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`question`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|300|

### <a name="BKMK_Rephrase"></a> Rephrase

|Property|Value|
|---|---|
|Description|**Rephrase generated by NL2SQ.**|
|DisplayName|**Rephrase**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rephrase`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|20000|

### <a name="BKMK_Skill"></a> Skill

|Property|Value|
|---|---|
|Description|**skill name for distinguishing between apps within the organization.**|
|DisplayName|**Skill**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`skill`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20000|

### <a name="BKMK_SkillId"></a> SkillId

|Property|Value|
|---|---|
|Description||
|DisplayName|**SkillId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`skillid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|dvtablesearch|

### <a name="BKMK_SQLCorrectness"></a> SQLCorrectness

|Property|Value|
|---|---|
|Description|**Feedback by the maker after they validate the standard sql.**|
|DisplayName|**SQLCorrectness**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sqlcorrectness`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`makerfewshotsqlcorrectness`|

#### SQLCorrectness Choices/Options

|Value|Label|
|---|---|
|0|**Pending Validation**|
|1|**Valid**|
|2|**Invalid**|
|3|**NotSure**|

### <a name="BKMK_StandardSQL"></a> StandardSQL

|Property|Value|
|---|---|
|Description|**Updated by the NL2SQ service/ Maker. This is for the maker to validate.**|
|DisplayName|**Standard SQL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`standardsql`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20000|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the CopilotExampleQuestion**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`copilotexamplequestion_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the CopilotExampleQuestion**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`copilotexamplequestion_statuscode`|

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
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
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

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier for the business unit that owns the record**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

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

- [CopilotExampleQuestion_DVTableSearch](#BKMK_CopilotExampleQuestion_DVTableSearch)
- [lk_copilotexamplequestion_createdby](#BKMK_lk_copilotexamplequestion_createdby)
- [lk_copilotexamplequestion_createdonbehalfby](#BKMK_lk_copilotexamplequestion_createdonbehalfby)
- [lk_copilotexamplequestion_modifiedby](#BKMK_lk_copilotexamplequestion_modifiedby)
- [lk_copilotexamplequestion_modifiedonbehalfby](#BKMK_lk_copilotexamplequestion_modifiedonbehalfby)
- [organization_copilotexamplequestion](#BKMK_organization_copilotexamplequestion)

### <a name="BKMK_CopilotExampleQuestion_DVTableSearch"></a> CopilotExampleQuestion_DVTableSearch

One-To-Many Relationship: [dvtablesearch CopilotExampleQuestion_DVTableSearch](dvtablesearch.md#BKMK_CopilotExampleQuestion_DVTableSearch)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearch`|
|ReferencedAttribute|`dvtablesearchid`|
|ReferencingAttribute|`skillid`|
|ReferencingEntityNavigationPropertyName|`skillid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_copilotexamplequestion_createdby"></a> lk_copilotexamplequestion_createdby

One-To-Many Relationship: [systemuser lk_copilotexamplequestion_createdby](systemuser.md#BKMK_lk_copilotexamplequestion_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_copilotexamplequestion_createdonbehalfby"></a> lk_copilotexamplequestion_createdonbehalfby

One-To-Many Relationship: [systemuser lk_copilotexamplequestion_createdonbehalfby](systemuser.md#BKMK_lk_copilotexamplequestion_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_copilotexamplequestion_modifiedby"></a> lk_copilotexamplequestion_modifiedby

One-To-Many Relationship: [systemuser lk_copilotexamplequestion_modifiedby](systemuser.md#BKMK_lk_copilotexamplequestion_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_copilotexamplequestion_modifiedonbehalfby"></a> lk_copilotexamplequestion_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_copilotexamplequestion_modifiedonbehalfby](systemuser.md#BKMK_lk_copilotexamplequestion_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_copilotexamplequestion"></a> organization_copilotexamplequestion

One-To-Many Relationship: [organization organization_copilotexamplequestion](organization.md#BKMK_organization_copilotexamplequestion)

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

- [copilotexamplequestion_AsyncOperations](#BKMK_copilotexamplequestion_AsyncOperations)
- [copilotexamplequestion_BulkDeleteFailures](#BKMK_copilotexamplequestion_BulkDeleteFailures)
- [copilotexamplequestion_MailboxTrackingFolders](#BKMK_copilotexamplequestion_MailboxTrackingFolders)
- [copilotexamplequestion_PrincipalObjectAttributeAccesses](#BKMK_copilotexamplequestion_PrincipalObjectAttributeAccesses)
- [copilotexamplequestion_ProcessSession](#BKMK_copilotexamplequestion_ProcessSession)
- [copilotexamplequestion_SyncErrors](#BKMK_copilotexamplequestion_SyncErrors)

### <a name="BKMK_copilotexamplequestion_AsyncOperations"></a> copilotexamplequestion_AsyncOperations

Many-To-One Relationship: [asyncoperation copilotexamplequestion_AsyncOperations](asyncoperation.md#BKMK_copilotexamplequestion_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`copilotexamplequestion_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_copilotexamplequestion_BulkDeleteFailures"></a> copilotexamplequestion_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure copilotexamplequestion_BulkDeleteFailures](bulkdeletefailure.md#BKMK_copilotexamplequestion_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`copilotexamplequestion_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_copilotexamplequestion_MailboxTrackingFolders"></a> copilotexamplequestion_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder copilotexamplequestion_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_copilotexamplequestion_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`copilotexamplequestion_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_copilotexamplequestion_PrincipalObjectAttributeAccesses"></a> copilotexamplequestion_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess copilotexamplequestion_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_copilotexamplequestion_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`copilotexamplequestion_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_copilotexamplequestion_ProcessSession"></a> copilotexamplequestion_ProcessSession

Many-To-One Relationship: [processsession copilotexamplequestion_ProcessSession](processsession.md#BKMK_copilotexamplequestion_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`copilotexamplequestion_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_copilotexamplequestion_SyncErrors"></a> copilotexamplequestion_SyncErrors

Many-To-One Relationship: [syncerror copilotexamplequestion_SyncErrors](syncerror.md#BKMK_copilotexamplequestion_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`copilotexamplequestion_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.copilotexamplequestion?displayProperty=fullName>
