---
title: "Customer Voice survey question (msfp_question) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Customer Voice survey question (msfp_question) table/entity with Microsoft Dataverse."
ms.date: 01/06/2025
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Customer Voice survey question (msfp_question) table/entity reference

Question in a survey to collect feedback.

## Messages

The following table lists the messages for the Customer Voice survey question (msfp_question) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msfp_questions(*msfp_questionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Create`<br />Event: True |`POST` /msfp_questions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msfp_questions(*msfp_questionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msfp_questions(*msfp_questionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msfp_questions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msfp_questions(*msfp_questionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msfp_questions(*msfp_questionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msfp_questions(*msfp_questionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Customer Voice survey question (msfp_question) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Customer Voice survey question (msfp_question) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Customer Voice survey question** |
| **DisplayCollectionName** | **Customer Voice survey  questions** |
| **SchemaName** | `msfp_question` |
| **CollectionSchemaName** | `msfp_questions` |
| **EntitySetName** | `msfp_questions`|
| **LogicalName** | `msfp_question` |
| **LogicalCollectionName** | `msfp_questions` |
| **PrimaryIdAttribute** | `msfp_questionid` |
| **PrimaryNameAttribute** |`msfp_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msfp_choicetype](#BKMK_msfp_choicetype)
- [msfp_correctanswer](#BKMK_msfp_correctanswer)
- [msfp_imageproperties](#BKMK_msfp_imageproperties)
- [msfp_Maximumrating](#BKMK_msfp_Maximumrating)
- [msfp_multiline](#BKMK_msfp_multiline)
- [msfp_name](#BKMK_msfp_name)
- [msfp_order](#BKMK_msfp_order)
- [msfp_otherproperties](#BKMK_msfp_otherproperties)
- [msfp_PermanentID](#BKMK_msfp_PermanentID)
- [msfp_questionchoices](#BKMK_msfp_questionchoices)
- [msfp_questionId](#BKMK_msfp_questionId)
- [msfp_questiontext](#BKMK_msfp_questiontext)
- [msfp_questiontype](#BKMK_msfp_questiontype)
- [msfp_responserequired](#BKMK_msfp_responserequired)
- [msfp_sequence](#BKMK_msfp_sequence)
- [msfp_sourceparentquestionidentifier](#BKMK_msfp_sourceparentquestionidentifier)
- [msfp_Sourcequestionidentifier](#BKMK_msfp_Sourcequestionidentifier)
- [msfp_sourcesurveyidentifier](#BKMK_msfp_sourcesurveyidentifier)
- [msfp_subtitle](#BKMK_msfp_subtitle)
- [msfp_Survey](#BKMK_msfp_Survey)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

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

### <a name="BKMK_msfp_choicetype"></a> msfp_choicetype

|Property|Value|
|---|---|
|Description|**Shows whether the question accepts single line or multiple lines of response.**|
|DisplayName|**Choice question type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_choicetype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msfp_question_msfp_choicetype`|

#### msfp_choicetype Choices/Options

|Value|Label|
|---|---|
|647390000|**Single choice**|
|647390001|**Multi choice**|
|647390002|**none**|

### <a name="BKMK_msfp_correctanswer"></a> msfp_correctanswer

|Property|Value|
|---|---|
|Description|**Stores the correct answer in case of quizzes.**|
|DisplayName|**Correct answer**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_correctanswer`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000000|

### <a name="BKMK_msfp_imageproperties"></a> msfp_imageproperties

|Property|Value|
|---|---|
|Description|**Question image properties in JSON format.**|
|DisplayName|**Image Properties**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_imageproperties`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000000|

### <a name="BKMK_msfp_Maximumrating"></a> msfp_Maximumrating

|Property|Value|
|---|---|
|Description|**Stores maximum rating of rating question type**|
|DisplayName|**Maximum rating**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_maximumrating`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msfp_multiline"></a> msfp_multiline

|Property|Value|
|---|---|
|Description|**Shows if the text question is multiple lines or not**|
|DisplayName|**Multiple lines**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_multiline`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msfp_question_msfp_multiline`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msfp_name"></a> msfp_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msfp_order"></a> msfp_order

|Property|Value|
|---|---|
|Description|**Order of the question in the survey.**|
|DisplayName|**Order**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_order`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|10|
|SourceTypeMask|0|

### <a name="BKMK_msfp_otherproperties"></a> msfp_otherproperties

|Property|Value|
|---|---|
|Description|**Stores other question properties in JSON format.**|
|DisplayName|**Other properties**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_otherproperties`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000000|

### <a name="BKMK_msfp_PermanentID"></a> msfp_PermanentID

|Property|Value|
|---|---|
|Description|**Permanent ID is auto-generated for a new survey question. For a copied survey, the ID is carried over from the original survey question.**|
|DisplayName|**Permanent ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_permanentid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msfp_questionchoices"></a> msfp_questionchoices

|Property|Value|
|---|---|
|Description|**Stores the list of answer options**|
|DisplayName|**Question choices**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_questionchoices`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000000|

### <a name="BKMK_msfp_questionId"></a> msfp_questionId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Question**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_questionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msfp_questiontext"></a> msfp_questiontext

|Property|Value|
|---|---|
|Description|**Text of the question in the survey.**|
|DisplayName|**Question text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_questiontext`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_msfp_questiontype"></a> msfp_questiontype

|Property|Value|
|---|---|
|Description|**Stores the type of question to display.**|
|DisplayName|**Question type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_questiontype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msfp_question_msfp_questiontype`|

#### msfp_questiontype Choices/Options

|Value|Label|
|---|---|
|647390000|**Choice**|
|647390001|**Text**|
|647390002|**Rating**|
|647390003|**Date**|
|647390004|**Ranking**|
|647390005|**MatrixChoiceGroup**|
|647390006|**MatrixChoice**|
|647390007|**NPS**|
|647390008|**File Upload**|
|647390009|**Number**|
|647390010|**Date and time**|
|647390011|**Drop-down**|

### <a name="BKMK_msfp_responserequired"></a> msfp_responserequired

|Property|Value|
|---|---|
|Description|**Shows if the question is mandatory.**|
|DisplayName|**Response required**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_responserequired`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msfp_question_msfp_responserequired`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msfp_sequence"></a> msfp_sequence

|Property|Value|
|---|---|
|Description|**Order of the question in the survey.**|
|DisplayName|**Sequence**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_sequence`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msfp_sourceparentquestionidentifier"></a> msfp_sourceparentquestionidentifier

|Property|Value|
|---|---|
|Description|**Unique identifier for the parent question in the source application.**|
|DisplayName|**Source parent question identifier**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_sourceparentquestionidentifier`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_msfp_Sourcequestionidentifier"></a> msfp_Sourcequestionidentifier

|Property|Value|
|---|---|
|Description|**Unique identifier for the question in the source application.**|
|DisplayName|**Source question identifier**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_sourcequestionidentifier`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msfp_sourcesurveyidentifier"></a> msfp_sourcesurveyidentifier

|Property|Value|
|---|---|
|Description|**Unique identifier for the survey in the source application.**|
|DisplayName|**Source survey identifier**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_sourcesurveyidentifier`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msfp_subtitle"></a> msfp_subtitle

|Property|Value|
|---|---|
|Description|**Stores subtitle of a question.**|
|DisplayName|**Subtitle**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_subtitle`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50000|

### <a name="BKMK_msfp_Survey"></a> msfp_Survey

|Property|Value|
|---|---|
|Description|**Unique identifier of the survey to which the question belongs.**|
|DisplayName|**Survey**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_survey`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msfp_survey|

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

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Owner Id**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Question**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msfp_question_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Question**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msfp_question_statuscode`|

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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
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

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description|**Yomi name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier for the team that owns the record.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

- [business_unit_msfp_question](#BKMK_business_unit_msfp_question)
- [lk_msfp_question_createdby](#BKMK_lk_msfp_question_createdby)
- [lk_msfp_question_createdonbehalfby](#BKMK_lk_msfp_question_createdonbehalfby)
- [lk_msfp_question_modifiedby](#BKMK_lk_msfp_question_modifiedby)
- [lk_msfp_question_modifiedonbehalfby](#BKMK_lk_msfp_question_modifiedonbehalfby)
- [msfp_msfp_survey_msfp_question_Survey](#BKMK_msfp_msfp_survey_msfp_question_Survey)
- [owner_msfp_question](#BKMK_owner_msfp_question)
- [team_msfp_question](#BKMK_team_msfp_question)
- [user_msfp_question](#BKMK_user_msfp_question)

### <a name="BKMK_business_unit_msfp_question"></a> business_unit_msfp_question

One-To-Many Relationship: [businessunit business_unit_msfp_question](businessunit.md#BKMK_business_unit_msfp_question)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_question_createdby"></a> lk_msfp_question_createdby

One-To-Many Relationship: [systemuser lk_msfp_question_createdby](systemuser.md#BKMK_lk_msfp_question_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_question_createdonbehalfby"></a> lk_msfp_question_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msfp_question_createdonbehalfby](systemuser.md#BKMK_lk_msfp_question_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_question_modifiedby"></a> lk_msfp_question_modifiedby

One-To-Many Relationship: [systemuser lk_msfp_question_modifiedby](systemuser.md#BKMK_lk_msfp_question_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_question_modifiedonbehalfby"></a> lk_msfp_question_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msfp_question_modifiedonbehalfby](systemuser.md#BKMK_lk_msfp_question_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_msfp_survey_msfp_question_Survey"></a> msfp_msfp_survey_msfp_question_Survey

One-To-Many Relationship: [msfp_survey msfp_msfp_survey_msfp_question_Survey](msfp_survey.md#BKMK_msfp_msfp_survey_msfp_question_Survey)

|Property|Value|
|---|---|
|ReferencedEntity|`msfp_survey`|
|ReferencedAttribute|`msfp_surveyid`|
|ReferencingAttribute|`msfp_survey`|
|ReferencingEntityNavigationPropertyName|`msfp_Survey`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_owner_msfp_question"></a> owner_msfp_question

One-To-Many Relationship: [owner owner_msfp_question](owner.md#BKMK_owner_msfp_question)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msfp_question"></a> team_msfp_question

One-To-Many Relationship: [team team_msfp_question](team.md#BKMK_team_msfp_question)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msfp_question"></a> user_msfp_question

One-To-Many Relationship: [systemuser user_msfp_question](systemuser.md#BKMK_user_msfp_question)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [msfp_msfp_question_msfp_fileresponse_question](#BKMK_msfp_msfp_question_msfp_fileresponse_question)
- [msfp_msfp_question_msfp_questionresponse_questionid](#BKMK_msfp_msfp_question_msfp_questionresponse_questionid)
- [msfp_question_Annotations](#BKMK_msfp_question_Annotations)
- [msfp_question_AsyncOperations](#BKMK_msfp_question_AsyncOperations)
- [msfp_question_BulkDeleteFailures](#BKMK_msfp_question_BulkDeleteFailures)
- [msfp_question_MailboxTrackingFolders](#BKMK_msfp_question_MailboxTrackingFolders)
- [msfp_question_PrincipalObjectAttributeAccesses](#BKMK_msfp_question_PrincipalObjectAttributeAccesses)
- [msfp_question_ProcessSession](#BKMK_msfp_question_ProcessSession)
- [msfp_question_SyncErrors](#BKMK_msfp_question_SyncErrors)

### <a name="BKMK_msfp_msfp_question_msfp_fileresponse_question"></a> msfp_msfp_question_msfp_fileresponse_question

Many-To-One Relationship: [msfp_fileresponse msfp_msfp_question_msfp_fileresponse_question](msfp_fileresponse.md#BKMK_msfp_msfp_question_msfp_fileresponse_question)

|Property|Value|
|---|---|
|ReferencingEntity|`msfp_fileresponse`|
|ReferencingAttribute|`msfp_question`|
|ReferencedEntityNavigationPropertyName|`msfp_msfp_question_msfp_fileresponse_question`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_msfp_question_msfp_questionresponse_questionid"></a> msfp_msfp_question_msfp_questionresponse_questionid

Many-To-One Relationship: [msfp_questionresponse msfp_msfp_question_msfp_questionresponse_questionid](msfp_questionresponse.md#BKMK_msfp_msfp_question_msfp_questionresponse_questionid)

|Property|Value|
|---|---|
|ReferencingEntity|`msfp_questionresponse`|
|ReferencingAttribute|`msfp_questionid`|
|ReferencedEntityNavigationPropertyName|`msfp_msfp_question_msfp_questionresponse_questionid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_question_Annotations"></a> msfp_question_Annotations

Many-To-One Relationship: [annotation msfp_question_Annotations](annotation.md#BKMK_msfp_question_Annotations)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msfp_question_Annotations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_question_AsyncOperations"></a> msfp_question_AsyncOperations

Many-To-One Relationship: [asyncoperation msfp_question_AsyncOperations](asyncoperation.md#BKMK_msfp_question_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_question_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_question_BulkDeleteFailures"></a> msfp_question_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msfp_question_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msfp_question_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_question_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_question_MailboxTrackingFolders"></a> msfp_question_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msfp_question_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msfp_question_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_question_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_question_PrincipalObjectAttributeAccesses"></a> msfp_question_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msfp_question_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msfp_question_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msfp_question_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_question_ProcessSession"></a> msfp_question_ProcessSession

Many-To-One Relationship: [processsession msfp_question_ProcessSession](processsession.md#BKMK_msfp_question_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_question_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_question_SyncErrors"></a> msfp_question_SyncErrors

Many-To-One Relationship: [syncerror msfp_question_SyncErrors](syncerror.md#BKMK_msfp_question_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_question_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

