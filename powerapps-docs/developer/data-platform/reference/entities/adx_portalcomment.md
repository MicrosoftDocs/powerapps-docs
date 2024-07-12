---
title: "Portal Comment (adx_portalcomment)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Portal Comment (adx_portalcomment)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Portal Comment (adx_portalcomment)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

An activity which is used to share information between the user and the customer on the portal.

**Added by**: Power Pages Runtime Core Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /adx_portalcomments(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /adx_portalcomments<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /adx_portalcomments(*activityid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Restore||Use <xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/>where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName> = Restore|
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /adx_portalcomments(*activityid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /adx_portalcomments<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /adx_portalcomments(*activityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /adx_portalcomments(*activityid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|adx_portalcomments|
|DisplayCollectionName|Portal Comments|
|DisplayName|Portal Comment|
|EntitySetName|adx_portalcomments|
|IsBPFEntity|False|
|LogicalCollectionName|adx_portalcomments|
|LogicalName|adx_portalcomment|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|activityid|
|PrimaryNameAttribute|subject|
|SchemaName|adx_portalcomment|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityAdditionalParams](#BKMK_ActivityAdditionalParams)
- [ActivityId](#BKMK_ActivityId)
- [ActualDurationMinutes](#BKMK_ActualDurationMinutes)
- [ActualEnd](#BKMK_ActualEnd)
- [ActualStart](#BKMK_ActualStart)
- [adx_PortalCommentDirectionCode](#BKMK_adx_PortalCommentDirectionCode)
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
- [OptionalAttendees](#BKMK_OptionalAttendees)
- [Organizer](#BKMK_Organizer)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Partners](#BKMK_Partners)
- [PriorityCode](#BKMK_PriorityCode)
- [ProcessId](#BKMK_ProcessId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
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
|--------|-----|
|Description|Additional information provided by the external application as JSON. For internal use only.|
|DisplayName|Activity Additional Parameters|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|activityadditionalparams|
|MaxLength|8192|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ActivityId"></a> ActivityId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the activity.|
|DisplayName|Activity|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|activityid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ActualDurationMinutes"></a> ActualDurationMinutes

|Property|Value|
|--------|-----|
|Description|Actual duration of the activity in minutes.|
|DisplayName|Actual Duration|
|Format|Duration|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualdurationminutes|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ActualEnd"></a> ActualEnd

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Actual end time of the activity.|
|DisplayName|Actual End|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualend|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ActualStart"></a> ActualStart

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Actual start time of the activity.|
|DisplayName|Actual Start|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|actualstart|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_adx_PortalCommentDirectionCode"></a> adx_PortalCommentDirectionCode

|Property|Value|
|--------|-----|
|Description|Specifies whether the WebActivity created by Portal User or Dynamics 365 User.|
|DisplayName|Direction|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|adx_portalcommentdirectioncode|
|RequiredLevel|None|
|Type|Picklist|

#### adx_PortalCommentDirectionCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Incoming||
|2|Outgoing||



### <a name="BKMK_BCC"></a> BCC

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Blind Carbon-copy (bcc) recipients of the activity.|
|DisplayName|BCC|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|bcc|
|RequiredLevel|None|
|Targets|account,contact,systemuser|
|Type|PartyList|


### <a name="BKMK_CC"></a> CC

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Carbon-copy (cc) recipients of the activity.|
|DisplayName|CC|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|cc|
|RequiredLevel|None|
|Targets|account,contact,systemuser|
|Type|PartyList|


### <a name="BKMK_Community"></a> Community

|Property|Value|
|--------|-----|
|Description|Shows how contact about the social activity originated, such as from Twitter or Facebook. This field is read-only.|
|DisplayName|Social Channel|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|community|
|RequiredLevel|None|
|Type|Picklist|

#### Community Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Other|Other default|
|1|Facebook|Facebook item.|
|2|Twitter|Twitter.|



### <a name="BKMK_Customers"></a> Customers

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Customer with which the activity is associated.|
|DisplayName|Customers|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|customers|
|RequiredLevel|None|
|Targets|account,contact|
|Type|PartyList|


### <a name="BKMK_DeliveryPriorityCode"></a> DeliveryPriorityCode

|Property|Value|
|--------|-----|
|Description|Priority of delivery of the activity to the email server.|
|DisplayName|Delivery Priority|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|deliveryprioritycode|
|RequiredLevel|None|
|Type|Picklist|

#### DeliveryPriorityCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Low||
|1|Normal||
|2|High||



### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the activity.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ExchangeItemId"></a> ExchangeItemId

|Property|Value|
|--------|-----|
|Description|The message id of activity which is returned from Exchange Server.|
|DisplayName|Exchange Item ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangeitemid|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExchangeWebLink"></a> ExchangeWebLink

|Property|Value|
|--------|-----|
|Description|Shows the web link of Activity of type email.|
|DisplayName|Exchange WebLink|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangeweblink|
|MaxLength|1250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_From"></a> From

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Person who the activity is from.|
|DisplayName|From|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|from|
|RequiredLevel|None|
|Targets|account,contact,systemuser|
|Type|PartyList|


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


### <a name="BKMK_IsBilled"></a> IsBilled

|Property|Value|
|--------|-----|
|Description|Information regarding whether the activity was billed as part of resolving a case.|
|DisplayName|Is Billed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isbilled|
|RequiredLevel|None|
|Type|Boolean|

#### IsBilled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_IsMapiPrivate"></a> IsMapiPrivate

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Private|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismapiprivate|
|RequiredLevel|None|
|Type|Boolean|

#### IsMapiPrivate Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_IsWorkflowCreated"></a> IsWorkflowCreated

|Property|Value|
|--------|-----|
|Description|Information regarding whether the activity was created from a workflow rule.|
|DisplayName|Is Workflow Created|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isworkflowcreated|
|RequiredLevel|None|
|Type|Boolean|

#### IsWorkflowCreated Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_LastOnHoldTime"></a> LastOnHoldTime

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Contains the date and time stamp of the last on hold time.|
|DisplayName|Last On Hold Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastonholdtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LeftVoiceMail"></a> LeftVoiceMail

|Property|Value|
|--------|-----|
|Description|Left the voice mail|
|DisplayName|Left Voice Mail|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|leftvoicemail|
|RequiredLevel|None|
|Type|Boolean|

#### LeftVoiceMail Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_OptionalAttendees"></a> OptionalAttendees

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|List of optional attendees for the activity.|
|DisplayName|Optional Attendees|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|optionalattendees|
|RequiredLevel|None|
|Targets|account,contact,knowledgearticle,queue,systemuser,unresolvedaddress|
|Type|PartyList|


### <a name="BKMK_Organizer"></a> Organizer

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Person who organized the activity.|
|DisplayName|Organizer|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|organizer|
|RequiredLevel|None|
|Targets|systemuser|
|Type|PartyList|


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
|Description|Unique identifier of the user or team who owns the activity.|
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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_Partners"></a> Partners

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Outsource vendor with which activity is associated.|
|DisplayName|Outsource Vendors|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|partners|
|RequiredLevel|None|
|Targets|account,contact|
|Type|PartyList|


### <a name="BKMK_PriorityCode"></a> PriorityCode

|Property|Value|
|--------|-----|
|Description|Priority of the activity.|
|DisplayName|Priority|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|prioritycode|
|RequiredLevel|None|
|Type|Picklist|

#### PriorityCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Low||
|1|Normal||
|2|High||



### <a name="BKMK_ProcessId"></a> ProcessId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Process.|
|DisplayName|Process|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the object with which the activity is associated.|
|DisplayName|Regarding|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|account,adx_invitation,contact,interactionforemail,knowledgearticle,knowledgebaserecord,mspp_adplacement,mspp_pollplacement,mspp_publishingstatetransitionrule,mspp_redirect,mspp_shortcut,mspp_website|
|Type|Lookup|


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidyominame|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_RequiredAttendees"></a> RequiredAttendees

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|List of required attendees for the activity.|
|DisplayName|Required Attendees|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|requiredattendees|
|RequiredLevel|None|
|Targets|account,contact,knowledgearticle,queue,systemuser,unresolvedaddress|
|Type|PartyList|


### <a name="BKMK_Resources"></a> Resources

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Users or facility/equipment that are required for the activity.|
|DisplayName|Resources|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|resources|
|RequiredLevel|None|
|Targets|systemuser|
|Type|PartyList|


### <a name="BKMK_ScheduledDurationMinutes"></a> ScheduledDurationMinutes

|Property|Value|
|--------|-----|
|Description|Scheduled duration of the activity, specified in minutes.|
|DisplayName|Scheduled Duration|
|Format|Duration|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|scheduleddurationminutes|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ScheduledEnd"></a> ScheduledEnd

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Scheduled end time of the activity.|
|DisplayName|Due Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|scheduledend|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ScheduledStart"></a> ScheduledStart

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Scheduled start time of the activity.|
|DisplayName|Start Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|scheduledstart|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_SLAId"></a> SLAId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Choose the service level agreement (SLA) that you want to apply to the case record.|
|DisplayName|SLA|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|slaid|
|RequiredLevel|None|
|Targets|sla|
|Type|Lookup|


### <a name="BKMK_SortDate"></a> SortDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time by which the activities are sorted.|
|DisplayName|Sort Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|sortdate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_StageId"></a> StageId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Stage.|
|DisplayName|Process Stage|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|stageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Status of the activity.|
|DisplayName|Activity Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Open|1|Open|
|1|Completed|2|Completed|
|2|Canceled|4|Canceled|
|3|Scheduled|5|Scheduled|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the activity.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Open|0|
|2|Sent|1|
|3|Received|1|
|4|Canceled|2|
|5|Scheduled|3|



### <a name="BKMK_Subject"></a> Subject

|Property|Value|
|--------|-----|
|Description|Subject associated with the activity.|
|DisplayName|Subject|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|subject|
|MaxLength|200|
|RequiredLevel|ApplicationRequired|
|Type|String|


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


### <a name="BKMK_To"></a> To

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Person who is the receiver of the activity.|
|DisplayName|To|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|to|
|RequiredLevel|None|
|Targets|account,contact,systemuser|
|Type|PartyList|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the currency associated with the activitypointer.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_TraversedPath"></a> TraversedPath

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Traversed Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|traversedpath|
|MaxLength|1250|
|RequiredLevel|None|
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

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ActivityTypeCode](#BKMK_ActivityTypeCode)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [DeliveryLastAttemptedOn](#BKMK_DeliveryLastAttemptedOn)
- [ExchangeRate](#BKMK_ExchangeRate)
- [InstanceTypeCode](#BKMK_InstanceTypeCode)
- [IsRegularActivity](#BKMK_IsRegularActivity)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OnHoldTime](#BKMK_OnHoldTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PostponeActivityProcessingUntil](#BKMK_PostponeActivityProcessingUntil)
- [SenderMailboxId](#BKMK_SenderMailboxId)
- [SenderMailboxIdName](#BKMK_SenderMailboxIdName)
- [SentOn](#BKMK_SentOn)
- [SeriesId](#BKMK_SeriesId)
- [SLAInvokedId](#BKMK_SLAInvokedId)
- [SLAInvokedIdName](#BKMK_SLAInvokedIdName)
- [SLAName](#BKMK_SLAName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ActivityTypeCode"></a> ActivityTypeCode

|Property|Value|
|--------|-----|
|Description|Type of activity.|
|DisplayName|Activity Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|activitytypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the activity.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the activity was created.|
|DisplayName|Date Created|
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
|Description|Unique identifier of the delegate user who created the activitypointer.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DeliveryLastAttemptedOn"></a> DeliveryLastAttemptedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the delivery of the activity was last attempted.|
|DisplayName|Date Delivery Last Attempted|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|deliverylastattemptedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the activitypointer with respect to the base currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_InstanceTypeCode"></a> InstanceTypeCode

|Property|Value|
|--------|-----|
|Description|Type of instance of a recurring series.|
|DisplayName|Recurring Instance Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|instancetypecode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### InstanceTypeCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Not Recurring||
|1|Recurring Master||
|2|Recurring Instance||
|3|Recurring Exception||
|4|Recurring Future Exception||



### <a name="BKMK_IsRegularActivity"></a> IsRegularActivity

|Property|Value|
|--------|-----|
|Description|Information regarding whether the activity is a regular activity type or event type.|
|DisplayName|Is Regular Activity|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isregularactivity|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsRegularActivity Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of user who last modified the activity.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when activity was last modified.|
|DisplayName|Last Updated|
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
|Description|Unique identifier of the delegate user who last modified the activitypointer.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OnHoldTime"></a> OnHoldTime

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Shows how long, in minutes, that the record was on hold.|
|DisplayName|On Hold Time (Minutes)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|onholdtime|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
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
|Description||
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
|Description|Unique identifier of the business unit that owns the activity.|
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
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team that owns the activity.|
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
|Description|Unique identifier of the user that owns the activity.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_PostponeActivityProcessingUntil"></a> PostponeActivityProcessingUntil

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Delay activity processing until|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postponeactivityprocessinguntil|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_SenderMailboxId"></a> SenderMailboxId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the mailbox associated with the sender of the email message.|
|DisplayName|Sender's Mailbox|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sendermailboxid|
|RequiredLevel|None|
|Targets|mailbox|
|Type|Lookup|


### <a name="BKMK_SenderMailboxIdName"></a> SenderMailboxIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sendermailboxidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SentOn"></a> SentOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the activity was sent.|
|DisplayName|Date Sent|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|senton|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_SeriesId"></a> SeriesId

|Property|Value|
|--------|-----|
|Description|Uniqueidentifier specifying the id of recurring series of an instance.|
|DisplayName|Series Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|seriesid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_SLAInvokedId"></a> SLAInvokedId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Last SLA that was applied to this case. This field is for internal use only.|
|DisplayName|Last SLA applied|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|slainvokedid|
|RequiredLevel|None|
|Targets|sla|
|Type|Lookup|


### <a name="BKMK_SLAInvokedIdName"></a> SLAInvokedIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|slainvokedidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SLAName"></a> SLAName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|slaname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version number of the activity.|
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

- [adx_portalcomment_activity_parties](#BKMK_adx_portalcomment_activity_parties)
- [adx_portalcomment_ActionCards](#BKMK_adx_portalcomment_ActionCards)
- [adx_portalcomment_SyncErrors](#BKMK_adx_portalcomment_SyncErrors)
- [adx_portalcomment_SharePointDocumentLocations](#BKMK_adx_portalcomment_SharePointDocumentLocations)
- [adx_portalcomment_AsyncOperations](#BKMK_adx_portalcomment_AsyncOperations)
- [adx_portalcomment_MailboxTrackingFolders](#BKMK_adx_portalcomment_MailboxTrackingFolders)
- [adx_portalcomment_ProcessSession](#BKMK_adx_portalcomment_ProcessSession)
- [adx_portalcomment_BulkDeleteFailures](#BKMK_adx_portalcomment_BulkDeleteFailures)
- [adx_portalcomment_PrincipalObjectAttributeAccesses](#BKMK_adx_portalcomment_PrincipalObjectAttributeAccesses)
- [adx_portalcomment_QueueItems](#BKMK_adx_portalcomment_QueueItems)
- [adx_portalcomment_Annotations](#BKMK_adx_portalcomment_Annotations)


### <a name="BKMK_adx_portalcomment_activity_parties"></a> adx_portalcomment_activity_parties

**Added by**: System Solution Solution

Same as the [adx_portalcomment_activity_parties](activityparty.md#BKMK_adx_portalcomment_activity_parties) many-to-one relationship for the [activityparty](activityparty.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityparty|
|ReferencingAttribute|activityid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_portalcomment_activity_parties|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_portalcomment_ActionCards"></a> adx_portalcomment_ActionCards

**Added by**: System Solution Solution

Same as the [adx_portalcomment_ActionCards](actioncard.md#BKMK_adx_portalcomment_ActionCards) many-to-one relationship for the [actioncard](actioncard.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncard|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_portalcomment_ActionCards|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_portalcomment_SyncErrors"></a> adx_portalcomment_SyncErrors

**Added by**: System Solution Solution

Same as the [adx_portalcomment_SyncErrors](syncerror.md#BKMK_adx_portalcomment_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_portalcomment_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_portalcomment_SharePointDocumentLocations"></a> adx_portalcomment_SharePointDocumentLocations

**Added by**: System Solution Solution

Same as the [adx_portalcomment_SharePointDocumentLocations](sharepointdocumentlocation.md#BKMK_adx_portalcomment_SharePointDocumentLocations) many-to-one relationship for the [sharepointdocumentlocation](sharepointdocumentlocation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_portalcomment_SharePointDocumentLocations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_portalcomment_AsyncOperations"></a> adx_portalcomment_AsyncOperations

**Added by**: System Solution Solution

Same as the [adx_portalcomment_AsyncOperations](asyncoperation.md#BKMK_adx_portalcomment_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_portalcomment_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_portalcomment_MailboxTrackingFolders"></a> adx_portalcomment_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [adx_portalcomment_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_adx_portalcomment_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_portalcomment_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_portalcomment_ProcessSession"></a> adx_portalcomment_ProcessSession

**Added by**: System Solution Solution

Same as the [adx_portalcomment_ProcessSession](processsession.md#BKMK_adx_portalcomment_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_portalcomment_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_portalcomment_BulkDeleteFailures"></a> adx_portalcomment_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [adx_portalcomment_BulkDeleteFailures](bulkdeletefailure.md#BKMK_adx_portalcomment_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_portalcomment_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_portalcomment_PrincipalObjectAttributeAccesses"></a> adx_portalcomment_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [adx_portalcomment_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_adx_portalcomment_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_portalcomment_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_portalcomment_QueueItems"></a> adx_portalcomment_QueueItems

**Added by**: System Solution Solution

Same as the [adx_portalcomment_QueueItems](queueitem.md#BKMK_adx_portalcomment_QueueItems) many-to-one relationship for the [queueitem](queueitem.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_portalcomment_QueueItems|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_portalcomment_Annotations"></a> adx_portalcomment_Annotations

**Added by**: System Solution Solution

Same as the [adx_portalcomment_Annotations](annotation.md#BKMK_adx_portalcomment_Annotations) many-to-one relationship for the [annotation](annotation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_portalcomment_Annotations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [interactionforemail_adx_portalcomments](#BKMK_interactionforemail_adx_portalcomments)
- [adx_invitation_adx_portalcomments](#BKMK_adx_invitation_adx_portalcomments)
- [knowledgebaserecord_adx_portalcomments](#BKMK_knowledgebaserecord_adx_portalcomments)
- [account_adx_portalcomments](#BKMK_account_adx_portalcomments)
- [adx_portalcomment_systemuser_createdby](#BKMK_adx_portalcomment_systemuser_createdby)
- [contact_adx_portalcomments](#BKMK_contact_adx_portalcomments)
- [adx_portalcomment_mailbox_sendermailboxid](#BKMK_adx_portalcomment_mailbox_sendermailboxid)
- [adx_portalcomment_transactioncurrency_transactioncurrencyid](#BKMK_adx_portalcomment_transactioncurrency_transactioncurrencyid)
- [adx_portalcomment_systemuser_owninguser](#BKMK_adx_portalcomment_systemuser_owninguser)
- [adx_portalcomment_sla_slaid](#BKMK_adx_portalcomment_sla_slaid)
- [adx_portalcomment_businessunit_owningbusinessunit](#BKMK_adx_portalcomment_businessunit_owningbusinessunit)
- [knowledgearticle_adx_portalcomments](#BKMK_knowledgearticle_adx_portalcomments)
- [adx_portalcomment_systemuser_modifiedonbehalfby](#BKMK_adx_portalcomment_systemuser_modifiedonbehalfby)
- [adx_portalcomment_systemuser_createdonbehalfby](#BKMK_adx_portalcomment_systemuser_createdonbehalfby)
- [adx_portalcomment_systemuser_modifiedby](#BKMK_adx_portalcomment_systemuser_modifiedby)
- [adx_portalcomment_team_owningteam](#BKMK_adx_portalcomment_team_owningteam)
- [adx_portalcomment_sla_slainvokedid](#BKMK_adx_portalcomment_sla_slainvokedid)
- [activity_pointer_adx_portalcomment](#BKMK_activity_pointer_adx_portalcomment)
- [processstage_adx_portalcomment](#BKMK_processstage_adx_portalcomment)
- [mspp_adplacement_adx_portalcomments](#BKMK_mspp_adplacement_adx_portalcomments)
- [mspp_pollplacement_adx_portalcomments](#BKMK_mspp_pollplacement_adx_portalcomments)
- [mspp_publishingstatetransitionrule_adx_portalcomments](#BKMK_mspp_publishingstatetransitionrule_adx_portalcomments)
- [mspp_redirect_adx_portalcomments](#BKMK_mspp_redirect_adx_portalcomments)
- [mspp_shortcut_adx_portalcomments](#BKMK_mspp_shortcut_adx_portalcomments)
- [mspp_website_adx_portalcomments](#BKMK_mspp_website_adx_portalcomments)


### <a name="BKMK_interactionforemail_adx_portalcomments"></a> interactionforemail_adx_portalcomments

**Added by**: System Solution Solution

See the [interactionforemail_adx_portalcomments](interactionforemail.md#BKMK_interactionforemail_adx_portalcomments) one-to-many relationship for the [interactionforemail](interactionforemail.md) table/entity.

### <a name="BKMK_adx_invitation_adx_portalcomments"></a> adx_invitation_adx_portalcomments

See the [adx_invitation_adx_portalcomments](adx_invitation.md#BKMK_adx_invitation_adx_portalcomments) one-to-many relationship for the [adx_invitation](adx_invitation.md) table/entity.

### <a name="BKMK_knowledgebaserecord_adx_portalcomments"></a> knowledgebaserecord_adx_portalcomments

**Added by**: System Solution Solution

See the [knowledgebaserecord_adx_portalcomments](knowledgebaserecord.md#BKMK_knowledgebaserecord_adx_portalcomments) one-to-many relationship for the [knowledgebaserecord](knowledgebaserecord.md) table/entity.

### <a name="BKMK_account_adx_portalcomments"></a> account_adx_portalcomments

**Added by**: System Solution Solution

See the [account_adx_portalcomments](account.md#BKMK_account_adx_portalcomments) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_adx_portalcomment_systemuser_createdby"></a> adx_portalcomment_systemuser_createdby

**Added by**: System Solution Solution

See the [adx_portalcomment_systemuser_createdby](systemuser.md#BKMK_adx_portalcomment_systemuser_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_contact_adx_portalcomments"></a> contact_adx_portalcomments

**Added by**: System Solution Solution

See the [contact_adx_portalcomments](contact.md#BKMK_contact_adx_portalcomments) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_adx_portalcomment_mailbox_sendermailboxid"></a> adx_portalcomment_mailbox_sendermailboxid

**Added by**: System Solution Solution

See the [adx_portalcomment_mailbox_sendermailboxid](mailbox.md#BKMK_adx_portalcomment_mailbox_sendermailboxid) one-to-many relationship for the [mailbox](mailbox.md) table/entity.

### <a name="BKMK_adx_portalcomment_transactioncurrency_transactioncurrencyid"></a> adx_portalcomment_transactioncurrency_transactioncurrencyid

**Added by**: System Solution Solution

See the [adx_portalcomment_transactioncurrency_transactioncurrencyid](transactioncurrency.md#BKMK_adx_portalcomment_transactioncurrency_transactioncurrencyid) one-to-many relationship for the [transactioncurrency](transactioncurrency.md) table/entity.

### <a name="BKMK_adx_portalcomment_systemuser_owninguser"></a> adx_portalcomment_systemuser_owninguser

**Added by**: System Solution Solution

See the [adx_portalcomment_systemuser_owninguser](systemuser.md#BKMK_adx_portalcomment_systemuser_owninguser) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_adx_portalcomment_sla_slaid"></a> adx_portalcomment_sla_slaid

**Added by**: System Solution Solution

See the [adx_portalcomment_sla_slaid](sla.md#BKMK_adx_portalcomment_sla_slaid) one-to-many relationship for the [sla](sla.md) table/entity.

### <a name="BKMK_adx_portalcomment_businessunit_owningbusinessunit"></a> adx_portalcomment_businessunit_owningbusinessunit

**Added by**: System Solution Solution

See the [adx_portalcomment_businessunit_owningbusinessunit](businessunit.md#BKMK_adx_portalcomment_businessunit_owningbusinessunit) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_knowledgearticle_adx_portalcomments"></a> knowledgearticle_adx_portalcomments

**Added by**: System Solution Solution

See the [knowledgearticle_adx_portalcomments](knowledgearticle.md#BKMK_knowledgearticle_adx_portalcomments) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_adx_portalcomment_systemuser_modifiedonbehalfby"></a> adx_portalcomment_systemuser_modifiedonbehalfby

**Added by**: System Solution Solution

See the [adx_portalcomment_systemuser_modifiedonbehalfby](systemuser.md#BKMK_adx_portalcomment_systemuser_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_adx_portalcomment_systemuser_createdonbehalfby"></a> adx_portalcomment_systemuser_createdonbehalfby

**Added by**: System Solution Solution

See the [adx_portalcomment_systemuser_createdonbehalfby](systemuser.md#BKMK_adx_portalcomment_systemuser_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_adx_portalcomment_systemuser_modifiedby"></a> adx_portalcomment_systemuser_modifiedby

**Added by**: System Solution Solution

See the [adx_portalcomment_systemuser_modifiedby](systemuser.md#BKMK_adx_portalcomment_systemuser_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_adx_portalcomment_team_owningteam"></a> adx_portalcomment_team_owningteam

**Added by**: System Solution Solution

See the [adx_portalcomment_team_owningteam](team.md#BKMK_adx_portalcomment_team_owningteam) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_adx_portalcomment_sla_slainvokedid"></a> adx_portalcomment_sla_slainvokedid

**Added by**: System Solution Solution

See the [adx_portalcomment_sla_slainvokedid](sla.md#BKMK_adx_portalcomment_sla_slainvokedid) one-to-many relationship for the [sla](sla.md) table/entity.

### <a name="BKMK_activity_pointer_adx_portalcomment"></a> activity_pointer_adx_portalcomment

**Added by**: System Solution Solution

See the [activity_pointer_adx_portalcomment](activitypointer.md#BKMK_activity_pointer_adx_portalcomment) one-to-many relationship for the [activitypointer](activitypointer.md) table/entity.

### <a name="BKMK_processstage_adx_portalcomment"></a> processstage_adx_portalcomment

**Added by**: System Solution Solution

See the [processstage_adx_portalcomment](processstage.md#BKMK_processstage_adx_portalcomment) one-to-many relationship for the [processstage](processstage.md) table/entity.

### <a name="BKMK_mspp_adplacement_adx_portalcomments"></a> mspp_adplacement_adx_portalcomments

**Added by**: Power Pages Apps Solution

See the [mspp_adplacement_adx_portalcomments](mspp_adplacement.md#BKMK_mspp_adplacement_adx_portalcomments) one-to-many relationship for the [mspp_adplacement](mspp_adplacement.md) table/entity.

### <a name="BKMK_mspp_pollplacement_adx_portalcomments"></a> mspp_pollplacement_adx_portalcomments

**Added by**: Power Pages Apps Solution

See the [mspp_pollplacement_adx_portalcomments](mspp_pollplacement.md#BKMK_mspp_pollplacement_adx_portalcomments) one-to-many relationship for the [mspp_pollplacement](mspp_pollplacement.md) table/entity.

### <a name="BKMK_mspp_publishingstatetransitionrule_adx_portalcomments"></a> mspp_publishingstatetransitionrule_adx_portalcomments

**Added by**: Power Pages Apps Solution

See the [mspp_publishingstatetransitionrule_adx_portalcomments](mspp_publishingstatetransitionrule.md#BKMK_mspp_publishingstatetransitionrule_adx_portalcomments) one-to-many relationship for the [mspp_publishingstatetransitionrule](mspp_publishingstatetransitionrule.md) table/entity.

### <a name="BKMK_mspp_redirect_adx_portalcomments"></a> mspp_redirect_adx_portalcomments

**Added by**: Power Pages Apps Solution

See the [mspp_redirect_adx_portalcomments](mspp_redirect.md#BKMK_mspp_redirect_adx_portalcomments) one-to-many relationship for the [mspp_redirect](mspp_redirect.md) table/entity.

### <a name="BKMK_mspp_shortcut_adx_portalcomments"></a> mspp_shortcut_adx_portalcomments

**Added by**: Power Pages Apps Solution

See the [mspp_shortcut_adx_portalcomments](mspp_shortcut.md#BKMK_mspp_shortcut_adx_portalcomments) one-to-many relationship for the [mspp_shortcut](mspp_shortcut.md) table/entity.

### <a name="BKMK_mspp_website_adx_portalcomments"></a> mspp_website_adx_portalcomments

**Added by**: Power Pages Apps Solution

See the [mspp_website_adx_portalcomments](mspp_website.md#BKMK_mspp_website_adx_portalcomments) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.adx_portalcomment?text=adx_portalcomment EntityType" />