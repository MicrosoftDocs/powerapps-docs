---
title: "Customer Voice alert (msfp_alert) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Customer Voice alert (msfp_alert) table/entity with Microsoft Dataverse."
ms.date: 01/06/2025
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Customer Voice alert (msfp_alert) table/entity reference



## Messages

The following table lists the messages for the Customer Voice alert (msfp_alert) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msfp_alerts(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Create`<br />Event: True |`POST` /msfp_alerts<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msfp_alerts(*activityid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /msfp_alerts(*activityid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msfp_alerts<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msfp_alerts(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msfp_alerts(*activityid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msfp_alerts(*activityid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Customer Voice alert (msfp_alert) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Customer Voice alert (msfp_alert) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Customer Voice alert** |
| **DisplayCollectionName** | **Customer Voice alert** |
| **SchemaName** | `msfp_alert` |
| **CollectionSchemaName** | `msfp_alerts` |
| **EntitySetName** | `msfp_alerts`|
| **LogicalName** | `msfp_alert` |
| **LogicalCollectionName** | `msfp_alerts` |
| **PrimaryIdAttribute** | `activityid` |
| **PrimaryNameAttribute** |`subject` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityAdditionalParams](#BKMK_ActivityAdditionalParams)
- [ActivityId](#BKMK_ActivityId)
- [ActualDurationMinutes](#BKMK_ActualDurationMinutes)
- [ActualEnd](#BKMK_ActualEnd)
- [ActualStart](#BKMK_ActualStart)
- [BCC](#BKMK_BCC)
- [CC](#BKMK_CC)
- [Community](#BKMK_Community)
- [Customers](#BKMK_Customers)
- [DeliveryPriorityCode](#BKMK_DeliveryPriorityCode)
- [Description](#BKMK_Description)
- [ExchangeItemId](#BKMK_ExchangeItemId)
- [ExchangeWebLink](#BKMK_ExchangeWebLink)
- [From](#BKMK_From)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsBilled](#BKMK_IsBilled)
- [IsMapiPrivate](#BKMK_IsMapiPrivate)
- [IsWorkflowCreated](#BKMK_IsWorkflowCreated)
- [LastOnHoldTime](#BKMK_LastOnHoldTime)
- [LeftVoiceMail](#BKMK_LeftVoiceMail)
- [msfp_alertrule](#BKMK_msfp_alertrule)
- [msfp_assigneeemail](#BKMK_msfp_assigneeemail)
- [msfp_assigneename](#BKMK_msfp_assigneename)
- [msfp_customeremail](#BKMK_msfp_customeremail)
- [msfp_customername](#BKMK_msfp_customername)
- [msfp_notes](#BKMK_msfp_notes)
- [msfp_project](#BKMK_msfp_project)
- [msfp_questions](#BKMK_msfp_questions)
- [msfp_reason](#BKMK_msfp_reason)
- [msfp_resolutiondetail](#BKMK_msfp_resolutiondetail)
- [msfp_resolutionsentiment](#BKMK_msfp_resolutionsentiment)
- [msfp_resolveremail](#BKMK_msfp_resolveremail)
- [msfp_resolvername](#BKMK_msfp_resolvername)
- [msfp_satisfactionmetric](#BKMK_msfp_satisfactionmetric)
- [msfp_survey](#BKMK_msfp_survey)
- [msfp_surveyresponse](#BKMK_msfp_surveyresponse)
- [OptionalAttendees](#BKMK_OptionalAttendees)
- [Organizer](#BKMK_Organizer)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Partners](#BKMK_Partners)
- [PriorityCode](#BKMK_PriorityCode)
- [ProcessId](#BKMK_ProcessId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [RequiredAttendees](#BKMK_RequiredAttendees)
- [Resources](#BKMK_Resources)
- [ScheduledDurationMinutes](#BKMK_ScheduledDurationMinutes)
- [ScheduledEnd](#BKMK_ScheduledEnd)
- [ScheduledStart](#BKMK_ScheduledStart)
- [SLAId](#BKMK_SLAId)
- [SortDate](#BKMK_SortDate)
- [StageId](#BKMK_StageId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [Subject](#BKMK_Subject)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [To](#BKMK_To)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ActivityAdditionalParams"></a> ActivityAdditionalParams

|Property|Value|
|---|---|
|Description|**Additional information provided by the external application as JSON. For internal use only.**|
|DisplayName|**Activity Additional Parameters**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`activityadditionalparams`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8192|

### <a name="BKMK_ActivityId"></a> ActivityId

|Property|Value|
|---|---|
|Description|**Unique identifier of the activity.**|
|DisplayName|**Activity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activityid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ActualDurationMinutes"></a> ActualDurationMinutes

|Property|Value|
|---|---|
|Description|**Actual duration of the activity in minutes.**|
|DisplayName|**Actual Duration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualdurationminutes`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ActualEnd"></a> ActualEnd

|Property|Value|
|---|---|
|Description|**Actual end time of the activity.**|
|DisplayName|**Actual End**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualend`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ActualStart"></a> ActualStart

|Property|Value|
|---|---|
|Description|**Actual start time of the activity.**|
|DisplayName|**Actual Start**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actualstart`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_BCC"></a> BCC

|Property|Value|
|---|---|
|Description|**Blind Carbon-copy (bcc) recipients of the activity.**|
|DisplayName|**BCC**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`bcc`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, systemuser|

### <a name="BKMK_CC"></a> CC

|Property|Value|
|---|---|
|Description|**Carbon-copy (cc) recipients of the activity.**|
|DisplayName|**CC**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cc`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, systemuser|

### <a name="BKMK_Community"></a> Community

|Property|Value|
|---|---|
|Description|**Shows how contact about the social activity originated, such as from Twitter or Facebook. This field is read-only.**|
|DisplayName|**Social Channel**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`community`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`socialprofile_community`|

#### Community Choices/Options

|Value|Label|
|---|---|
|0|**Other**|
|1|**Facebook**|
|2|**Twitter**|

### <a name="BKMK_Customers"></a> Customers

|Property|Value|
|---|---|
|Description|**Customer with which the activity is associated.**|
|DisplayName|**Customers**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customers`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact|

### <a name="BKMK_DeliveryPriorityCode"></a> DeliveryPriorityCode

|Property|Value|
|---|---|
|Description|**Priority of delivery of the activity to the email server.**|
|DisplayName|**Delivery Priority**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deliveryprioritycode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`activitypointer_deliveryprioritycode`|

#### DeliveryPriorityCode Choices/Options

|Value|Label|
|---|---|
|0|**Low**|
|1|**Normal**|
|2|**High**|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the activity.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_ExchangeItemId"></a> ExchangeItemId

|Property|Value|
|---|---|
|Description|**The message id of activity which is returned from Exchange Server.**|
|DisplayName|**Exchange Item ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangeitemid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ExchangeWebLink"></a> ExchangeWebLink

|Property|Value|
|---|---|
|Description|**Shows the web link of Activity of type email.**|
|DisplayName|**Exchange WebLink**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangeweblink`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|

### <a name="BKMK_From"></a> From

|Property|Value|
|---|---|
|Description|**Person who the activity is from.**|
|DisplayName|**From**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`from`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, systemuser|

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

### <a name="BKMK_IsBilled"></a> IsBilled

|Property|Value|
|---|---|
|Description|**Information regarding whether the activity was billed as part of resolving a case.**|
|DisplayName|**Is Billed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isbilled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msfp_alert_isbilled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMapiPrivate"></a> IsMapiPrivate

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Private**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismapiprivate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msfp_alert_ismapiprivate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsWorkflowCreated"></a> IsWorkflowCreated

|Property|Value|
|---|---|
|Description|**Information regarding whether the activity was created from a workflow rule.**|
|DisplayName|**Is Workflow Created**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isworkflowcreated`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msfp_alert_isworkflowcreated`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_LastOnHoldTime"></a> LastOnHoldTime

|Property|Value|
|---|---|
|Description|**Contains the date and time stamp of the last on hold time.**|
|DisplayName|**Last On Hold Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastonholdtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_LeftVoiceMail"></a> LeftVoiceMail

|Property|Value|
|---|---|
|Description|**Left the voice mail**|
|DisplayName|**Left Voice Mail**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`leftvoicemail`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msfp_alert_leftvoicemail`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msfp_alertrule"></a> msfp_alertrule

|Property|Value|
|---|---|
|Description|**Rule associated with this alert.**|
|DisplayName|**Alert rule**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_alertrule`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msfp_alertrule|

### <a name="BKMK_msfp_assigneeemail"></a> msfp_assigneeemail

|Property|Value|
|---|---|
|Description|**Email address of the assignee of the alert.**|
|DisplayName|**Assignee email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_assigneeemail`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_assigneename"></a> msfp_assigneename

|Property|Value|
|---|---|
|Description|**Name of the assignee of the alert.**|
|DisplayName|**Assignee name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_assigneename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_customeremail"></a> msfp_customeremail

|Property|Value|
|---|---|
|Description||
|DisplayName|**Customer email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_customeremail`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msfp_customername"></a> msfp_customername

|Property|Value|
|---|---|
|Description||
|DisplayName|**Customer name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_customername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msfp_notes"></a> msfp_notes

|Property|Value|
|---|---|
|Description|**Additional detail for the alert.**|
|DisplayName|**Notes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_notes`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msfp_project"></a> msfp_project

|Property|Value|
|---|---|
|Description|**Project to which the alert belongs.**|
|DisplayName|**Project**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_project`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msfp_project|

### <a name="BKMK_msfp_questions"></a> msfp_questions

|Property|Value|
|---|---|
|Description|**Questions associated with the alert.**|
|DisplayName|**Questions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_questions`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msfp_reason"></a> msfp_reason

|Property|Value|
|---|---|
|Description|**Reason for creating the alert.**|
|DisplayName|**Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_reason`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msfp_resolutiondetail"></a> msfp_resolutiondetail

|Property|Value|
|---|---|
|Description|**Detail on how the alert was resolved.**|
|DisplayName|**Resolution detail**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_resolutiondetail`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_msfp_resolutionsentiment"></a> msfp_resolutionsentiment

|Property|Value|
|---|---|
|Description|**Sentiment while resolving the alert.**|
|DisplayName|**Resolution sentiment**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_resolutionsentiment`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msfp_resolveremail"></a> msfp_resolveremail

|Property|Value|
|---|---|
|Description|**Email address of the user who resolved the alert.**|
|DisplayName|**Resolver email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_resolveremail`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msfp_resolvername"></a> msfp_resolvername

|Property|Value|
|---|---|
|Description|**Name of the user who resolved the alert.**|
|DisplayName|**Resolver name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_resolvername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msfp_satisfactionmetric"></a> msfp_satisfactionmetric

|Property|Value|
|---|---|
|Description|**Satisfaction metric associated with the alert.**|
|DisplayName|**Satisfaction metric**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_satisfactionmetric`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msfp_satisfactionmetric|

### <a name="BKMK_msfp_survey"></a> msfp_survey

|Property|Value|
|---|---|
|Description|**Survey associated with the alert.**|
|DisplayName|**Survey**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_survey`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msfp_survey|

### <a name="BKMK_msfp_surveyresponse"></a> msfp_surveyresponse

|Property|Value|
|---|---|
|Description|**Survey response associated with the alert.**|
|DisplayName|**Survey Response**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_surveyresponse`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msfp_surveyresponse|

### <a name="BKMK_OptionalAttendees"></a> OptionalAttendees

|Property|Value|
|---|---|
|Description|**List of optional attendees for the activity.**|
|DisplayName|**Optional Attendees**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`optionalattendees`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, knowledgearticle, queue, systemuser, unresolvedaddress|

### <a name="BKMK_Organizer"></a> Organizer

|Property|Value|
|---|---|
|Description|**Person who organized the activity.**|
|DisplayName|**Organizer**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`organizer`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|systemuser|

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
|Description|**Unique identifier of the user or team who owns the activity.**|
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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_Partners"></a> Partners

|Property|Value|
|---|---|
|Description|**Outsource vendor with which activity is associated.**|
|DisplayName|**Outsource Vendors**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`partners`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact|

### <a name="BKMK_PriorityCode"></a> PriorityCode

|Property|Value|
|---|---|
|Description|**Priority of the activity.**|
|DisplayName|**Priority**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`prioritycode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`msfp_alert_prioritycode`|

#### PriorityCode Choices/Options

|Value|Label|
|---|---|
|0|**Low**|
|1|**Normal**|
|2|**High**|

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Process.**|
|DisplayName|**Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the object with which the activity is associated.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, adx_invitation, contact, interactionforemail, knowledgearticle, knowledgebaserecord, mspp_adplacement, mspp_pollplacement, mspp_publishingstatetransitionrule, mspp_redirect, mspp_shortcut, mspp_website|

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_RequiredAttendees"></a> RequiredAttendees

|Property|Value|
|---|---|
|Description|**List of required attendees for the activity.**|
|DisplayName|**Required Attendees**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`requiredattendees`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, knowledgearticle, queue, systemuser, unresolvedaddress|

### <a name="BKMK_Resources"></a> Resources

|Property|Value|
|---|---|
|Description|**Users or facility/equipment that are required for the activity.**|
|DisplayName|**Resources**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`resources`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|systemuser|

### <a name="BKMK_ScheduledDurationMinutes"></a> ScheduledDurationMinutes

|Property|Value|
|---|---|
|Description|**Scheduled duration of the activity, specified in minutes.**|
|DisplayName|**Scheduled Duration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`scheduleddurationminutes`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

|Property|Value|
|---|---|
|Description|**Scheduled end time of the activity.**|
|DisplayName|**Due Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`scheduledend`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ScheduledStart"></a> ScheduledStart

|Property|Value|
|---|---|
|Description|**Scheduled start time of the activity.**|
|DisplayName|**Start Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`scheduledstart`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|---|---|
|Description|**Choose the service level agreement (SLA) that you want to apply to the case record.**|
|DisplayName|**SLA**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`slaid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sla|

### <a name="BKMK_SortDate"></a> SortDate

|Property|Value|
|---|---|
|Description|**Shows the date and time by which the activities are sorted.**|
|DisplayName|**Sort Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sortdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Stage.**|
|DisplayName|**(Deprecated) Process Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the activity.**|
|DisplayName|**Activity Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`msfp_alert_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Open**<br />DefaultStatus: 1<br />InvariantName: `Open`|
|1|Label: **Completed**<br />DefaultStatus: 2<br />InvariantName: `Completed`|
|2|Label: **Canceled**<br />DefaultStatus: 3<br />InvariantName: `Canceled`|
|3|Label: **Scheduled**<br />DefaultStatus: 4<br />InvariantName: `Scheduled`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the activity.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`msfp_alert_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Open**<br />State:0<br />TransitionData: None|
|2|Label: **Completed**<br />State:1<br />TransitionData: None|
|3|Label: **Canceled**<br />State:2<br />TransitionData: None|
|4|Label: **Scheduled**<br />State:3<br />TransitionData: None|

### <a name="BKMK_Subject"></a> Subject

|Property|Value|
|---|---|
|Description|**Subject associated with the activity.**|
|DisplayName|**Subject**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subject`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|400|

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

### <a name="BKMK_To"></a> To

|Property|Value|
|---|---|
|Description|**Person who is the receiver of the activity.**|
|DisplayName|**To**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`to`|
|RequiredLevel|None|
|Type|PartyList|
|Targets|account, contact, systemuser|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the currency associated with the activitypointer.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**(Deprecated) Traversed Path**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`traversedpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|

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

- [ActivityTypeCode](#BKMK_ActivityTypeCode)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [DeliveryLastAttemptedOn](#BKMK_DeliveryLastAttemptedOn)
- [ExchangeRate](#BKMK_ExchangeRate)
- [InstanceTypeCode](#BKMK_InstanceTypeCode)
- [IsRegularActivity](#BKMK_IsRegularActivity)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OnHoldTime](#BKMK_OnHoldTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PostponeActivityProcessingUntil](#BKMK_PostponeActivityProcessingUntil)
- [SenderMailboxId](#BKMK_SenderMailboxId)
- [SentOn](#BKMK_SentOn)
- [SeriesId](#BKMK_SeriesId)
- [SLAInvokedId](#BKMK_SLAInvokedId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ActivityTypeCode"></a> ActivityTypeCode

|Property|Value|
|---|---|
|Description|**Type of activity.**|
|DisplayName|**Activity Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activitytypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the activity.**|
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
|Description|**Date and time when the activity was created.**|
|DisplayName|**Date Created**|
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
|Description|**Unique identifier of the delegate user who created the activitypointer.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_DeliveryLastAttemptedOn"></a> DeliveryLastAttemptedOn

|Property|Value|
|---|---|
|Description|**Date and time when the delivery of the activity was last attempted.**|
|DisplayName|**Date Delivery Last Attempted**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deliverylastattemptedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the activitypointer with respect to the base currency.**|
|DisplayName|**Exchange Rate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

### <a name="BKMK_InstanceTypeCode"></a> InstanceTypeCode

|Property|Value|
|---|---|
|Description|**Type of instance of a recurring series.**|
|DisplayName|**Recurring Instance Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`instancetypecode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`msfp_alert_instancetypecode`|

#### InstanceTypeCode Choices/Options

|Value|Label|
|---|---|
|0|**Not Recurring**|
|1|**Recurring Master**|
|2|**Recurring Instance**|
|3|**Recurring Exception**|
|4|**Recurring Future Exception**|

### <a name="BKMK_IsRegularActivity"></a> IsRegularActivity

|Property|Value|
|---|---|
|Description|**Information regarding whether the activity is a regular activity type or event type.**|
|DisplayName|**Is Regular Activity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isregularactivity`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`activitypointer_isregularactivity`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of user who last modified the activity.**|
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
|Description|**Date and time when activity was last modified.**|
|DisplayName|**Last Updated**|
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
|Description|**Unique identifier of the delegate user who last modified the activitypointer.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OnHoldTime"></a> OnHoldTime

|Property|Value|
|---|---|
|Description|**Shows how long, in minutes, that the record was on hold.**|
|DisplayName|**On Hold Time (Minutes)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`onholdtime`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description||
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
|Description||
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
|Description|**Unique identifier of the business unit that owns the activity.**|
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
|Description|**Unique identifier of the team that owns the activity.**|
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
|Description|**Unique identifier of the user that owns the activity.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_PostponeActivityProcessingUntil"></a> PostponeActivityProcessingUntil

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Delay activity processing until**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`postponeactivityprocessinguntil`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SenderMailboxId"></a> SenderMailboxId

|Property|Value|
|---|---|
|Description|**Unique identifier of the mailbox associated with the sender of the email message.**|
|DisplayName|**Sender's Mailbox**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sendermailboxid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mailbox|

### <a name="BKMK_SentOn"></a> SentOn

|Property|Value|
|---|---|
|Description|**Date and time when the activity was sent.**|
|DisplayName|**Date Sent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`senton`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SeriesId"></a> SeriesId

|Property|Value|
|---|---|
|Description|**Uniqueidentifier specifying the id of recurring series of an instance.**|
|DisplayName|**Series Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`seriesid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_SLAInvokedId"></a> SLAInvokedId

|Property|Value|
|---|---|
|Description|**Last SLA that was applied to this case. This field is for internal use only.**|
|DisplayName|**Last SLA applied**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`slainvokedid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sla|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the activity.**|
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

- [account_msfp_alerts](#BKMK_account_msfp_alerts)
- [activity_pointer_msfp_alert](#BKMK_activity_pointer_msfp_alert)
- [adx_invitation_msfp_alerts](#BKMK_adx_invitation_msfp_alerts)
- [contact_msfp_alerts](#BKMK_contact_msfp_alerts)
- [interactionforemail_msfp_alerts](#BKMK_interactionforemail_msfp_alerts)
- [knowledgearticle_msfp_alerts](#BKMK_knowledgearticle_msfp_alerts)
- [knowledgebaserecord_msfp_alerts](#BKMK_knowledgebaserecord_msfp_alerts)
- [msfp_alert_businessunit_owningbusinessunit](#BKMK_msfp_alert_businessunit_owningbusinessunit)
- [msfp_alert_mailbox_sendermailboxid](#BKMK_msfp_alert_mailbox_sendermailboxid)
- [msfp_alert_owner_ownerid](#BKMK_msfp_alert_owner_ownerid)
- [msfp_alert_sla_slaid](#BKMK_msfp_alert_sla_slaid)
- [msfp_alert_sla_slainvokedid](#BKMK_msfp_alert_sla_slainvokedid)
- [msfp_alert_systemuser_createdby](#BKMK_msfp_alert_systemuser_createdby)
- [msfp_alert_systemuser_createdonbehalfby](#BKMK_msfp_alert_systemuser_createdonbehalfby)
- [msfp_alert_systemuser_modifiedby](#BKMK_msfp_alert_systemuser_modifiedby)
- [msfp_alert_systemuser_modifiedonbehalfby](#BKMK_msfp_alert_systemuser_modifiedonbehalfby)
- [msfp_alert_systemuser_owninguser](#BKMK_msfp_alert_systemuser_owninguser)
- [msfp_alert_team_owningteam](#BKMK_msfp_alert_team_owningteam)
- [msfp_alert_transactioncurrency_transactioncurrencyid](#BKMK_msfp_alert_transactioncurrency_transactioncurrencyid)
- [msfp_msfp_alertrule_msfp_alert_alertrule](#BKMK_msfp_msfp_alertrule_msfp_alert_alertrule)
- [msfp_msfp_project_msfp_alert_project](#BKMK_msfp_msfp_project_msfp_alert_project)
- [msfp_msfp_satisfactionmetric_msfp_alert](#BKMK_msfp_msfp_satisfactionmetric_msfp_alert)
- [msfp_msfp_survey_msfp_alert_survey](#BKMK_msfp_msfp_survey_msfp_alert_survey)
- [msfp_msfp_surveyresponse_msfp_alert_surveyresponse](#BKMK_msfp_msfp_surveyresponse_msfp_alert_surveyresponse)
- [mspp_adplacement_msfp_alerts](#BKMK_mspp_adplacement_msfp_alerts)
- [mspp_pollplacement_msfp_alerts](#BKMK_mspp_pollplacement_msfp_alerts)
- [mspp_publishingstatetransitionrule_msfp_alerts](#BKMK_mspp_publishingstatetransitionrule_msfp_alerts)
- [mspp_redirect_msfp_alerts](#BKMK_mspp_redirect_msfp_alerts)
- [mspp_shortcut_msfp_alerts](#BKMK_mspp_shortcut_msfp_alerts)
- [mspp_website_msfp_alerts](#BKMK_mspp_website_msfp_alerts)

### <a name="BKMK_account_msfp_alerts"></a> account_msfp_alerts

One-To-Many Relationship: [account account_msfp_alerts](account.md#BKMK_account_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_account_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_activity_pointer_msfp_alert"></a> activity_pointer_msfp_alert

One-To-Many Relationship: [activitypointer activity_pointer_msfp_alert](activitypointer.md#BKMK_activity_pointer_msfp_alert)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`activityid`|
|ReferencingEntityNavigationPropertyName|`activityid_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_msfp_alerts"></a> adx_invitation_msfp_alerts

One-To-Many Relationship: [adx_invitation adx_invitation_msfp_alerts](adx_invitation.md#BKMK_adx_invitation_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_invitation_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_contact_msfp_alerts"></a> contact_msfp_alerts

One-To-Many Relationship: [contact contact_msfp_alerts](contact.md#BKMK_contact_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_contact_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_interactionforemail_msfp_alerts"></a> interactionforemail_msfp_alerts

One-To-Many Relationship: [interactionforemail interactionforemail_msfp_alerts](interactionforemail.md#BKMK_interactionforemail_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`interactionforemail`|
|ReferencedAttribute|`interactionforemailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_new_interactionforemail_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_knowledgearticle_msfp_alerts"></a> knowledgearticle_msfp_alerts

One-To-Many Relationship: [knowledgearticle knowledgearticle_msfp_alerts](knowledgearticle.md#BKMK_knowledgearticle_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgearticle_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_knowledgebaserecord_msfp_alerts"></a> knowledgebaserecord_msfp_alerts

One-To-Many Relationship: [knowledgebaserecord knowledgebaserecord_msfp_alerts](knowledgebaserecord.md#BKMK_knowledgebaserecord_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgebaserecord_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_businessunit_owningbusinessunit"></a> msfp_alert_businessunit_owningbusinessunit

One-To-Many Relationship: [businessunit msfp_alert_businessunit_owningbusinessunit](businessunit.md#BKMK_msfp_alert_businessunit_owningbusinessunit)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_mailbox_sendermailboxid"></a> msfp_alert_mailbox_sendermailboxid

One-To-Many Relationship: [mailbox msfp_alert_mailbox_sendermailboxid](mailbox.md#BKMK_msfp_alert_mailbox_sendermailboxid)

|Property|Value|
|---|---|
|ReferencedEntity|`mailbox`|
|ReferencedAttribute|`mailboxid`|
|ReferencingAttribute|`sendermailboxid`|
|ReferencingEntityNavigationPropertyName|`sendermailboxid_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_owner_ownerid"></a> msfp_alert_owner_ownerid

One-To-Many Relationship: [owner msfp_alert_owner_ownerid](owner.md#BKMK_msfp_alert_owner_ownerid)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_sla_slaid"></a> msfp_alert_sla_slaid

One-To-Many Relationship: [sla msfp_alert_sla_slaid](sla.md#BKMK_msfp_alert_sla_slaid)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`slaid`|
|ReferencingEntityNavigationPropertyName|`sla_activitypointer_sla_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_sla_slainvokedid"></a> msfp_alert_sla_slainvokedid

One-To-Many Relationship: [sla msfp_alert_sla_slainvokedid](sla.md#BKMK_msfp_alert_sla_slainvokedid)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`slainvokedid`|
|ReferencingEntityNavigationPropertyName|`slainvokedid_activitypointer_sla_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_systemuser_createdby"></a> msfp_alert_systemuser_createdby

One-To-Many Relationship: [systemuser msfp_alert_systemuser_createdby](systemuser.md#BKMK_msfp_alert_systemuser_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_systemuser_createdonbehalfby"></a> msfp_alert_systemuser_createdonbehalfby

One-To-Many Relationship: [systemuser msfp_alert_systemuser_createdonbehalfby](systemuser.md#BKMK_msfp_alert_systemuser_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_systemuser_modifiedby"></a> msfp_alert_systemuser_modifiedby

One-To-Many Relationship: [systemuser msfp_alert_systemuser_modifiedby](systemuser.md#BKMK_msfp_alert_systemuser_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_systemuser_modifiedonbehalfby"></a> msfp_alert_systemuser_modifiedonbehalfby

One-To-Many Relationship: [systemuser msfp_alert_systemuser_modifiedonbehalfby](systemuser.md#BKMK_msfp_alert_systemuser_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_systemuser_owninguser"></a> msfp_alert_systemuser_owninguser

One-To-Many Relationship: [systemuser msfp_alert_systemuser_owninguser](systemuser.md#BKMK_msfp_alert_systemuser_owninguser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_team_owningteam"></a> msfp_alert_team_owningteam

One-To-Many Relationship: [team msfp_alert_team_owningteam](team.md#BKMK_msfp_alert_team_owningteam)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_alert_transactioncurrency_transactioncurrencyid"></a> msfp_alert_transactioncurrency_transactioncurrencyid

One-To-Many Relationship: [transactioncurrency msfp_alert_transactioncurrency_transactioncurrencyid](transactioncurrency.md#BKMK_msfp_alert_transactioncurrency_transactioncurrencyid)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_msfp_alertrule_msfp_alert_alertrule"></a> msfp_msfp_alertrule_msfp_alert_alertrule

One-To-Many Relationship: [msfp_alertrule msfp_msfp_alertrule_msfp_alert_alertrule](msfp_alertrule.md#BKMK_msfp_msfp_alertrule_msfp_alert_alertrule)

|Property|Value|
|---|---|
|ReferencedEntity|`msfp_alertrule`|
|ReferencedAttribute|`msfp_alertruleid`|
|ReferencingAttribute|`msfp_alertrule`|
|ReferencingEntityNavigationPropertyName|`msfp_alertrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_msfp_project_msfp_alert_project"></a> msfp_msfp_project_msfp_alert_project

One-To-Many Relationship: [msfp_project msfp_msfp_project_msfp_alert_project](msfp_project.md#BKMK_msfp_msfp_project_msfp_alert_project)

|Property|Value|
|---|---|
|ReferencedEntity|`msfp_project`|
|ReferencedAttribute|`msfp_projectid`|
|ReferencingAttribute|`msfp_project`|
|ReferencingEntityNavigationPropertyName|`msfp_project`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_msfp_satisfactionmetric_msfp_alert"></a> msfp_msfp_satisfactionmetric_msfp_alert

One-To-Many Relationship: [msfp_satisfactionmetric msfp_msfp_satisfactionmetric_msfp_alert](msfp_satisfactionmetric.md#BKMK_msfp_msfp_satisfactionmetric_msfp_alert)

|Property|Value|
|---|---|
|ReferencedEntity|`msfp_satisfactionmetric`|
|ReferencedAttribute|`msfp_satisfactionmetricid`|
|ReferencingAttribute|`msfp_satisfactionmetric`|
|ReferencingEntityNavigationPropertyName|`msfp_satisfactionmetric`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_msfp_survey_msfp_alert_survey"></a> msfp_msfp_survey_msfp_alert_survey

One-To-Many Relationship: [msfp_survey msfp_msfp_survey_msfp_alert_survey](msfp_survey.md#BKMK_msfp_msfp_survey_msfp_alert_survey)

|Property|Value|
|---|---|
|ReferencedEntity|`msfp_survey`|
|ReferencedAttribute|`msfp_surveyid`|
|ReferencingAttribute|`msfp_survey`|
|ReferencingEntityNavigationPropertyName|`msfp_survey`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_msfp_surveyresponse_msfp_alert_surveyresponse"></a> msfp_msfp_surveyresponse_msfp_alert_surveyresponse

One-To-Many Relationship: [msfp_surveyresponse msfp_msfp_surveyresponse_msfp_alert_surveyresponse](msfp_surveyresponse.md#BKMK_msfp_msfp_surveyresponse_msfp_alert_surveyresponse)

|Property|Value|
|---|---|
|ReferencedEntity|`msfp_surveyresponse`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`msfp_surveyresponse`|
|ReferencingEntityNavigationPropertyName|`msfp_surveyresponse`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_adplacement_msfp_alerts"></a> mspp_adplacement_msfp_alerts

One-To-Many Relationship: [mspp_adplacement mspp_adplacement_msfp_alerts](mspp_adplacement.md#BKMK_mspp_adplacement_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_adplacement`|
|ReferencedAttribute|`mspp_adplacementid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_adplacement_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_pollplacement_msfp_alerts"></a> mspp_pollplacement_msfp_alerts

One-To-Many Relationship: [mspp_pollplacement mspp_pollplacement_msfp_alerts](mspp_pollplacement.md#BKMK_mspp_pollplacement_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_pollplacement`|
|ReferencedAttribute|`mspp_pollplacementid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_pollplacement_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_publishingstatetransitionrule_msfp_alerts"></a> mspp_publishingstatetransitionrule_msfp_alerts

One-To-Many Relationship: [mspp_publishingstatetransitionrule mspp_publishingstatetransitionrule_msfp_alerts](mspp_publishingstatetransitionrule.md#BKMK_mspp_publishingstatetransitionrule_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstatetransitionrule`|
|ReferencedAttribute|`mspp_publishingstatetransitionruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_publishingstatetransitionrule_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_redirect_msfp_alerts"></a> mspp_redirect_msfp_alerts

One-To-Many Relationship: [mspp_redirect mspp_redirect_msfp_alerts](mspp_redirect.md#BKMK_mspp_redirect_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_redirect`|
|ReferencedAttribute|`mspp_redirectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_redirect_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_shortcut_msfp_alerts"></a> mspp_shortcut_msfp_alerts

One-To-Many Relationship: [mspp_shortcut mspp_shortcut_msfp_alerts](mspp_shortcut.md#BKMK_mspp_shortcut_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_shortcut`|
|ReferencedAttribute|`mspp_shortcutid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_shortcut_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_msfp_alerts"></a> mspp_website_msfp_alerts

One-To-Many Relationship: [mspp_website mspp_website_msfp_alerts](mspp_website.md#BKMK_mspp_website_msfp_alerts)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspp_website_msfp_alert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [msfp_alert_ActionCards](#BKMK_msfp_alert_ActionCards)
- [msfp_alert_activity_parties](#BKMK_msfp_alert_activity_parties)
- [msfp_alert_Annotations](#BKMK_msfp_alert_Annotations)
- [msfp_alert_AsyncOperations](#BKMK_msfp_alert_AsyncOperations)
- [msfp_alert_BulkDeleteFailures](#BKMK_msfp_alert_BulkDeleteFailures)
- [msfp_alert_connections1](#BKMK_msfp_alert_connections1)
- [msfp_alert_connections2](#BKMK_msfp_alert_connections2)
- [msfp_alert_DuplicateBaseRecord](#BKMK_msfp_alert_DuplicateBaseRecord)
- [msfp_alert_DuplicateMatchingRecord](#BKMK_msfp_alert_DuplicateMatchingRecord)
- [msfp_alert_Feedback](#BKMK_msfp_alert_Feedback)
- [msfp_alert_MailboxTrackingFolders](#BKMK_msfp_alert_MailboxTrackingFolders)
- [msfp_alert_PrincipalObjectAttributeAccesses](#BKMK_msfp_alert_PrincipalObjectAttributeAccesses)
- [msfp_alert_ProcessSession](#BKMK_msfp_alert_ProcessSession)
- [msfp_alert_QueueItems](#BKMK_msfp_alert_QueueItems)
- [msfp_alert_SyncErrors](#BKMK_msfp_alert_SyncErrors)

### <a name="BKMK_msfp_alert_ActionCards"></a> msfp_alert_ActionCards

Many-To-One Relationship: [actioncard msfp_alert_ActionCards](actioncard.md#BKMK_msfp_alert_ActionCards)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncard`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_ActionCards`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_activity_parties"></a> msfp_alert_activity_parties

Many-To-One Relationship: [activityparty msfp_alert_activity_parties](activityparty.md#BKMK_msfp_alert_activity_parties)

|Property|Value|
|---|---|
|ReferencingEntity|`activityparty`|
|ReferencingAttribute|`activityid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_activity_parties`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_Annotations"></a> msfp_alert_Annotations

Many-To-One Relationship: [annotation msfp_alert_Annotations](annotation.md#BKMK_msfp_alert_Annotations)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_Annotations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_AsyncOperations"></a> msfp_alert_AsyncOperations

Many-To-One Relationship: [asyncoperation msfp_alert_AsyncOperations](asyncoperation.md#BKMK_msfp_alert_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_BulkDeleteFailures"></a> msfp_alert_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msfp_alert_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msfp_alert_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_connections1"></a> msfp_alert_connections1

Many-To-One Relationship: [connection msfp_alert_connections1](connection.md#BKMK_msfp_alert_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_connections2"></a> msfp_alert_connections2

Many-To-One Relationship: [connection msfp_alert_connections2](connection.md#BKMK_msfp_alert_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_DuplicateBaseRecord"></a> msfp_alert_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msfp_alert_DuplicateBaseRecord](duplicaterecord.md#BKMK_msfp_alert_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_DuplicateMatchingRecord"></a> msfp_alert_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msfp_alert_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msfp_alert_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_Feedback"></a> msfp_alert_Feedback

Many-To-One Relationship: [feedback msfp_alert_Feedback](feedback.md#BKMK_msfp_alert_Feedback)

|Property|Value|
|---|---|
|ReferencingEntity|`feedback`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_Feedback`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 150<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_MailboxTrackingFolders"></a> msfp_alert_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msfp_alert_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msfp_alert_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_PrincipalObjectAttributeAccesses"></a> msfp_alert_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msfp_alert_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msfp_alert_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_ProcessSession"></a> msfp_alert_ProcessSession

Many-To-One Relationship: [processsession msfp_alert_ProcessSession](processsession.md#BKMK_msfp_alert_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_QueueItems"></a> msfp_alert_QueueItems

Many-To-One Relationship: [queueitem msfp_alert_QueueItems](queueitem.md#BKMK_msfp_alert_QueueItems)

|Property|Value|
|---|---|
|ReferencingEntity|`queueitem`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_QueueItems`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_alert_SyncErrors"></a> msfp_alert_SyncErrors

Many-To-One Relationship: [syncerror msfp_alert_SyncErrors](syncerror.md#BKMK_msfp_alert_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_alert_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

