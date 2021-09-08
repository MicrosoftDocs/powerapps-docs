---
title: "SocialActivity table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SocialActivity table/entity."
ms.date: 05/20/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# SocialActivity table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

For internal use only.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/socialactivities(*activityid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/socialactivities<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/socialactivities(*activityid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/socialactivities(*activityid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/socialactivities<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/socialactivities(*activityid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/socialactivities(*activityid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SocialActivities|
|DisplayCollectionName|Social Activities|
|DisplayName|Social Activity|
|EntitySetName|socialactivities|
|IsBPFEntity|False|
|LogicalCollectionName|socialactivities|
|LogicalName|socialactivity|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|activityid|
|PrimaryNameAttribute|subject|
|SchemaName|SocialActivity|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityAdditionalParams](#BKMK_ActivityAdditionalParams)
- [ActivityId](#BKMK_ActivityId)
- [ActualDurationMinutes](#BKMK_ActualDurationMinutes)
- [ActualEnd](#BKMK_ActualEnd)
- [ActualStart](#BKMK_ActualStart)
- [Community](#BKMK_Community)
- [Description](#BKMK_Description)
- [DirectionCode](#BKMK_DirectionCode)
- [From](#BKMK_From)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [InResponseTo](#BKMK_InResponseTo)
- [IsBilled](#BKMK_IsBilled)
- [IsWorkflowCreated](#BKMK_IsWorkflowCreated)
- [LastOnHoldTime](#BKMK_LastOnHoldTime)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PostAuthor](#BKMK_PostAuthor)
- [PostAuthorAccount](#BKMK_PostAuthorAccount)
- [PostAuthorAccountType](#BKMK_PostAuthorAccountType)
- [PostAuthorType](#BKMK_PostAuthorType)
- [PostedOn](#BKMK_PostedOn)
- [PostFromProfileId](#BKMK_PostFromProfileId)
- [PostId](#BKMK_PostId)
- [PostMessageType](#BKMK_PostMessageType)
- [PostToProfileId](#BKMK_PostToProfileId)
- [PostURL](#BKMK_PostURL)
- [PriorityCode](#BKMK_PriorityCode)
- [ProcessId](#BKMK_ProcessId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [Resources](#BKMK_Resources)
- [ScheduledDurationMinutes](#BKMK_ScheduledDurationMinutes)
- [ScheduledEnd](#BKMK_ScheduledEnd)
- [ScheduledStart](#BKMK_ScheduledStart)
- [SentimentValue](#BKMK_SentimentValue)
- [SLAId](#BKMK_SLAId)
- [SocialAdditionalParams](#BKMK_SocialAdditionalParams)
- [SortDate](#BKMK_SortDate)
- [StageId](#BKMK_StageId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [Subject](#BKMK_Subject)
- [ThreadId](#BKMK_ThreadId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [To](#BKMK_To)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_ActivityAdditionalParams"></a> ActivityAdditionalParams

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Additional Parameters|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|activityadditionalparams|
|MaxLength|8192|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ActivityId"></a> ActivityId

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

|Value|Label|
|-----|-----|
|0|Other|
|1|Facebook|
|2|Twitter|



### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Shows information about the social post content. This field is read-only.|
|DisplayName|Post Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_DirectionCode"></a> DirectionCode

|Property|Value|
|--------|-----|
|Description|Select the direction of the post as incoming or outbound.|
|DisplayName|Direction|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|directioncode|
|RequiredLevel|None|
|Type|Boolean|

#### DirectionCode Choices/Options

|Value|Label|
|-----|-----|
|1|Outgoing|
|0|Incoming|

**DefaultValue**: False



### <a name="BKMK_From"></a> From

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


### <a name="BKMK_InResponseTo"></a> InResponseTo

|Property|Value|
|--------|-----|
|Description|Unique identifier for the responses to a post. For internal use only.|
|DisplayName|In Response To|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|inresponseto|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


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

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



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

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_LastOnHoldTime"></a> LastOnHoldTime

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

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_PostAuthor"></a> PostAuthor

|Property|Value|
|--------|-----|
|Description|Shows the contact or account that authored the post.|
|DisplayName|Post Author|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|postauthor|
|RequiredLevel|None|
|Targets|account,contact|
|Type|Customer|


### <a name="BKMK_PostAuthorAccount"></a> PostAuthorAccount

|Property|Value|
|--------|-----|
|Description|Shows the parent account of the author of the post.|
|DisplayName|Post Author Account|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|postauthoraccount|
|RequiredLevel|ApplicationRequired|
|Targets|account,contact|
|Type|Customer|


### <a name="BKMK_PostAuthorAccountType"></a> PostAuthorAccountType

|Property|Value|
|--------|-----|
|Description|Select the parent account or parent contact for the post author|
|DisplayName|Post author parent|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postauthoraccounttype|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_PostAuthorType"></a> PostAuthorType

|Property|Value|
|--------|-----|
|Description|Select the parent account or parent contact for the social profile of the social activity|
|DisplayName|Post Author Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postauthortype|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_PostedOn"></a> PostedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|postedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_PostFromProfileId"></a> PostFromProfileId

|Property|Value|
|--------|-----|
|Description|Shows the author of the post on the corresponding social channel.|
|DisplayName|Posted By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|postfromprofileid|
|RequiredLevel|None|
|Targets|socialprofile|
|Type|Lookup|


### <a name="BKMK_PostId"></a> PostId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the post. For internal use only.|
|DisplayName|Post ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|postid|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PostMessageType"></a> PostMessageType

|Property|Value|
|--------|-----|
|Description|Shows if the social post originated as a private or public message.|
|DisplayName|Received As|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postmessagetype|
|RequiredLevel|None|
|Type|Picklist|

#### PostMessageType Choices/Options

|Value|Label|
|-----|-----|
|0|Public Message|
|1|Private Message|



### <a name="BKMK_PostToProfileId"></a> PostToProfileId

|Property|Value|
|--------|-----|
|Description|Shows the recipients of the social post.|
|DisplayName|Posted To|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|posttoprofileid|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PostURL"></a> PostURL

|Property|Value|
|--------|-----|
|Description|Shows the URL of the post.|
|DisplayName|Post URL|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|posturl|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PriorityCode"></a> PriorityCode

|Property|Value|
|--------|-----|
|Description|Shows the priority so that preferred customers or critical issues are handled quickly.|
|DisplayName|Priority|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|prioritycode|
|RequiredLevel|None|
|Type|Picklist|

#### PriorityCode Choices/Options

|Value|Label|
|-----|-----|
|0|Low|
|1|Normal|
|2|High|



### <a name="BKMK_ProcessId"></a> ProcessId

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

|Property|Value|
|--------|-----|
|Description|Shows the record that the social activity relates to.|
|DisplayName|Regarding|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|account,asyncoperation,contact,knowledgearticle,knowledgebaserecord|
|Type|Lookup|


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

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

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_Resources"></a> Resources

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


### <a name="BKMK_SentimentValue"></a> SentimentValue

|Property|Value|
|--------|-----|
|Description|Value derived after assessing words commonly associated with a negative, neutral, or positive sentiment that occurs in a social post. Sentiment information can also be reported as numeric values.|
|DisplayName|Sentiment Value|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|sentimentvalue|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|--------|-----|
|Description|Choose the service level agreement (SLA) that you want to apply to the Social Activity record.|
|DisplayName|SLA|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|slaid|
|RequiredLevel|None|
|Targets|sla|
|Type|Lookup|


### <a name="BKMK_SocialAdditionalParams"></a> SocialAdditionalParams

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Social Additional Parameters|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|socialadditionalparams|
|MaxLength|8192|
|RequiredLevel|None|
|Type|Memo|


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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Stage.|
|DisplayName|(Deprecated) Process Stage|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|stageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows whether the social activity completed. This field is read-only.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Open|4|Open|
|1|Completed|3|Completed|
|2|Canceled|5|Canceled|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Shows whether the social activity is completed, failed, or processing. This field is read-only.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Completed|1|
|2|Failed|1|
|3|Processing|1|
|4|Open|0|
|5|Canceled|2|



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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ThreadId"></a> ThreadId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the social conversation. For internal use only.|
|DisplayName|Thread ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|threadid|
|MaxLength|160|
|RequiredLevel|None|
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

|Property|Value|
|--------|-----|
|Description|Choose the local currency for the record to make sure budgets are reported in the correct currency.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|(Deprecated) Traversed Path|
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
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsRegularActivity](#BKMK_IsRegularActivity)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OnHoldTime](#BKMK_OnHoldTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PostAuthorAccountName](#BKMK_PostAuthorAccountName)
- [PostAuthorAccountYomiName](#BKMK_PostAuthorAccountYomiName)
- [PostAuthorName](#BKMK_PostAuthorName)
- [PostAuthorYomiName](#BKMK_PostAuthorYomiName)
- [PostFromProfileIdName](#BKMK_PostFromProfileIdName)
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


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the activity was created.|
|DisplayName|Created Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.0000000001|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


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

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Last Updated|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit that owns the activity.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who owns the Activity.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_PostAuthorAccountName"></a> PostAuthorAccountName

|Property|Value|
|--------|-----|
|Description|Select the parent account or parent contact for post author.|
|DisplayName|Post author parent|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postauthoraccountname|
|MaxLength|160|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_PostAuthorAccountYomiName"></a> PostAuthorAccountYomiName

|Property|Value|
|--------|-----|
|Description|Select the parent account or parent contact for the post author|
|DisplayName|Post author parent|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postauthoraccountyominame|
|MaxLength|450|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_PostAuthorName"></a> PostAuthorName

|Property|Value|
|--------|-----|
|Description|Account or contact associated with the social profile or author of the post.|
|DisplayName|Post Author Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postauthorname|
|MaxLength|160|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_PostAuthorYomiName"></a> PostAuthorYomiName

|Property|Value|
|--------|-----|
|Description|Parent account or parent contact for the social profile of the social activity|
|DisplayName|Post Author Yomi Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postauthoryominame|
|MaxLength|450|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_PostFromProfileIdName"></a> PostFromProfileIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|postedbyname|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_SLAInvokedId"></a> SLAInvokedId

|Property|Value|
|--------|-----|
|Description|Last SLA that was applied to this Social Activity. This field is for internal use only.|
|DisplayName|Last SLA applied|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|slainvokedid|
|RequiredLevel|None|
|Targets|sla|
|Type|Lookup|


### <a name="BKMK_SLAInvokedIdName"></a> SLAInvokedIdName

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

|Property|Value|
|--------|-----|
|Description|Version number of the social activity.|
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

- [socialactivity_principalobjectattributeaccess](#BKMK_socialactivity_principalobjectattributeaccess)
- [socialactivity_activity_parties](#BKMK_socialactivity_activity_parties)
- [SocialActivity_BulkDeleteFailures](#BKMK_SocialActivity_BulkDeleteFailures)
- [SocialActivity_QueueItem](#BKMK_SocialActivity_QueueItem)
- [SocialActivity_SyncErrors](#BKMK_SocialActivity_SyncErrors)
- [slakpiinstance_socialactivity](#BKMK_slakpiinstance_socialactivity)
- [SocialActivity_DuplicateBaseRecord](#BKMK_SocialActivity_DuplicateBaseRecord)
- [SocialActivity_AsyncOperations](#BKMK_SocialActivity_AsyncOperations)
- [SocialActivity_ProcessSessions](#BKMK_SocialActivity_ProcessSessions)
- [SocialActivity_DuplicateMatchingRecord](#BKMK_SocialActivity_DuplicateMatchingRecord)
- [socialactivity_connections1](#BKMK_socialactivity_connections1)
- [SocialActivity_Annotation](#BKMK_SocialActivity_Annotation)
- [socialactivity_connections2](#BKMK_socialactivity_connections2)


### <a name="BKMK_socialactivity_principalobjectattributeaccess"></a> socialactivity_principalobjectattributeaccess

Same as principalobjectattributeaccess table [socialactivity_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_socialactivity_principalobjectattributeaccess) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|socialactivity_principalobjectattributeaccess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_socialactivity_activity_parties"></a> socialactivity_activity_parties

Same as activityparty table [socialactivity_activity_parties](activityparty.md#BKMK_socialactivity_activity_parties) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityparty|
|ReferencingAttribute|activityid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|socialactivity_activity_parties|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SocialActivity_BulkDeleteFailures"></a> SocialActivity_BulkDeleteFailures

Same as bulkdeletefailure table [SocialActivity_BulkDeleteFailures](bulkdeletefailure.md#BKMK_SocialActivity_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SocialActivity_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SocialActivity_QueueItem"></a> SocialActivity_QueueItem

Same as queueitem table [SocialActivity_QueueItem](queueitem.md#BKMK_SocialActivity_QueueItem) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|SocialActivity_QueueItem|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SocialActivity_SyncErrors"></a> SocialActivity_SyncErrors

Same as syncerror table [SocialActivity_SyncErrors](syncerror.md#BKMK_SocialActivity_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|SocialActivity_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_slakpiinstance_socialactivity"></a> slakpiinstance_socialactivity

Same as slakpiinstance table [slakpiinstance_socialactivity](slakpiinstance.md#BKMK_slakpiinstance_socialactivity) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slakpiinstance|
|ReferencingAttribute|regarding|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|slakpiinstance_socialactivity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SocialActivity_DuplicateBaseRecord"></a> SocialActivity_DuplicateBaseRecord

Same as duplicaterecord table [SocialActivity_DuplicateBaseRecord](duplicaterecord.md#BKMK_SocialActivity_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SocialActivity_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SocialActivity_AsyncOperations"></a> SocialActivity_AsyncOperations

Same as asyncoperation table [SocialActivity_AsyncOperations](asyncoperation.md#BKMK_SocialActivity_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SocialActivity_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SocialActivity_ProcessSessions"></a> SocialActivity_ProcessSessions

Same as processsession table [SocialActivity_ProcessSessions](processsession.md#BKMK_SocialActivity_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SocialActivity_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SocialActivity_DuplicateMatchingRecord"></a> SocialActivity_DuplicateMatchingRecord

Same as duplicaterecord table [SocialActivity_DuplicateMatchingRecord](duplicaterecord.md#BKMK_SocialActivity_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SocialActivity_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_socialactivity_connections1"></a> socialactivity_connections1

Same as connection table [socialactivity_connections1](connection.md#BKMK_socialactivity_connections1) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|socialactivity_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SocialActivity_Annotation"></a> SocialActivity_Annotation

Same as annotation table [SocialActivity_Annotation](annotation.md#BKMK_SocialActivity_Annotation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|SocialActivity_Annotation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_socialactivity_connections2"></a> socialactivity_connections2

Same as connection table [socialactivity_connections2](connection.md#BKMK_socialactivity_connections2) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|socialactivity_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [KnowledgeBaseRecord_SocialActivities](#BKMK_KnowledgeBaseRecord_SocialActivities)
- [socialactivity_postauthoraccount_contacts](#BKMK_socialactivity_postauthoraccount_contacts)
- [KnowledgeArticle_SocialActivities](#BKMK_KnowledgeArticle_SocialActivities)
- [activity_pointer_socialactivity](#BKMK_activity_pointer_socialactivity)
- [SocialActivity_PostAuthorAccount_accounts](#BKMK_SocialActivity_PostAuthorAccount_accounts)
- [lk_socialactivity_createdby](#BKMK_lk_socialactivity_createdby)
- [Account_SocialActivities](#BKMK_Account_SocialActivities)
- [transactioncurrency_socialactivity](#BKMK_transactioncurrency_socialactivity)
- [sla_socialactivity](#BKMK_sla_socialactivity)
- [user_socialactivity](#BKMK_user_socialactivity)
- [business_unit_socialactivity](#BKMK_business_unit_socialactivity)
- [socialactivity_postauthor_contacts](#BKMK_socialactivity_postauthor_contacts)
- [team_socialactivity](#BKMK_team_socialactivity)
- [manualsla_socialactivity](#BKMK_manualsla_socialactivity)
- [SocialActivity_PostAuthor_accounts](#BKMK_SocialActivity_PostAuthor_accounts)
- [Socialprofile_SocialActivities](#BKMK_Socialprofile_SocialActivities)
- [AsyncOperation_SocialActivities](#BKMK_AsyncOperation_SocialActivities)
- [lk_socialactivity_modifiedby](#BKMK_lk_socialactivity_modifiedby)
- [lk_socialactivitybase_createdonbehalfby](#BKMK_lk_socialactivitybase_createdonbehalfby)
- [lk_socialactivitybase_modifiedonbehalfby](#BKMK_lk_socialactivitybase_modifiedonbehalfby)
- [Contact_SocialActivities](#BKMK_Contact_SocialActivities)


### <a name="BKMK_KnowledgeBaseRecord_SocialActivities"></a> KnowledgeBaseRecord_SocialActivities

See knowledgebaserecord Table [KnowledgeBaseRecord_SocialActivities](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_SocialActivities) One-To-Many relationship.

### <a name="BKMK_socialactivity_postauthoraccount_contacts"></a> socialactivity_postauthoraccount_contacts

See contact Table [socialactivity_postauthoraccount_contacts](contact.md#BKMK_socialactivity_postauthoraccount_contacts) One-To-Many relationship.

### <a name="BKMK_KnowledgeArticle_SocialActivities"></a> KnowledgeArticle_SocialActivities

See knowledgearticle Table [KnowledgeArticle_SocialActivities](knowledgearticle.md#BKMK_KnowledgeArticle_SocialActivities) One-To-Many relationship.

### <a name="BKMK_activity_pointer_socialactivity"></a> activity_pointer_socialactivity

See activitypointer Table [activity_pointer_socialactivity](activitypointer.md#BKMK_activity_pointer_socialactivity) One-To-Many relationship.

### <a name="BKMK_SocialActivity_PostAuthorAccount_accounts"></a> SocialActivity_PostAuthorAccount_accounts

See account Table [SocialActivity_PostAuthorAccount_accounts](account.md#BKMK_SocialActivity_PostAuthorAccount_accounts) One-To-Many relationship.

### <a name="BKMK_lk_socialactivity_createdby"></a> lk_socialactivity_createdby

See systemuser Table [lk_socialactivity_createdby](systemuser.md#BKMK_lk_socialactivity_createdby) One-To-Many relationship.

### <a name="BKMK_Account_SocialActivities"></a> Account_SocialActivities

See account Table [Account_SocialActivities](account.md#BKMK_Account_SocialActivities) One-To-Many relationship.

### <a name="BKMK_transactioncurrency_socialactivity"></a> transactioncurrency_socialactivity

See transactioncurrency Table [transactioncurrency_socialactivity](transactioncurrency.md#BKMK_transactioncurrency_socialactivity) One-To-Many relationship.

### <a name="BKMK_sla_socialactivity"></a> sla_socialactivity

See sla Table [sla_socialactivity](sla.md#BKMK_sla_socialactivity) One-To-Many relationship.

### <a name="BKMK_user_socialactivity"></a> user_socialactivity

See systemuser Table [user_socialactivity](systemuser.md#BKMK_user_socialactivity) One-To-Many relationship.

### <a name="BKMK_business_unit_socialactivity"></a> business_unit_socialactivity

See businessunit Table [business_unit_socialactivity](businessunit.md#BKMK_business_unit_socialactivity) One-To-Many relationship.

### <a name="BKMK_socialactivity_postauthor_contacts"></a> socialactivity_postauthor_contacts

See contact Table [socialactivity_postauthor_contacts](contact.md#BKMK_socialactivity_postauthor_contacts) One-To-Many relationship.

### <a name="BKMK_team_socialactivity"></a> team_socialactivity

See team Table [team_socialactivity](team.md#BKMK_team_socialactivity) One-To-Many relationship.

### <a name="BKMK_manualsla_socialactivity"></a> manualsla_socialactivity

See sla Table [manualsla_socialactivity](sla.md#BKMK_manualsla_socialactivity) One-To-Many relationship.

### <a name="BKMK_SocialActivity_PostAuthor_accounts"></a> SocialActivity_PostAuthor_accounts

See account Table [SocialActivity_PostAuthor_accounts](account.md#BKMK_SocialActivity_PostAuthor_accounts) One-To-Many relationship.

### <a name="BKMK_Socialprofile_SocialActivities"></a> Socialprofile_SocialActivities

See socialprofile Table [Socialprofile_SocialActivities](socialprofile.md#BKMK_Socialprofile_SocialActivities) One-To-Many relationship.

### <a name="BKMK_AsyncOperation_SocialActivities"></a> AsyncOperation_SocialActivities

See asyncoperation Table [AsyncOperation_SocialActivities](asyncoperation.md#BKMK_AsyncOperation_SocialActivities) One-To-Many relationship.

### <a name="BKMK_lk_socialactivity_modifiedby"></a> lk_socialactivity_modifiedby

See systemuser Table [lk_socialactivity_modifiedby](systemuser.md#BKMK_lk_socialactivity_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_socialactivitybase_createdonbehalfby"></a> lk_socialactivitybase_createdonbehalfby

See systemuser Table [lk_socialactivitybase_createdonbehalfby](systemuser.md#BKMK_lk_socialactivitybase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_socialactivitybase_modifiedonbehalfby"></a> lk_socialactivitybase_modifiedonbehalfby

See systemuser Table [lk_socialactivitybase_modifiedonbehalfby](systemuser.md#BKMK_lk_socialactivitybase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_Contact_SocialActivities"></a> Contact_SocialActivities

See contact Table [Contact_SocialActivities](contact.md#BKMK_Contact_SocialActivities) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.socialactivity?text=socialactivity EntityType" />