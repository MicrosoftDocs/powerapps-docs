---
title: "SLA table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the SLA table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# SLA table/entity reference (Microsoft Dataverse)

Contains information about the tracked service-level KPIs for cases that belong to different customers.

## Messages

The following table lists the messages for the SLA table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /slas(*slaid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /slas<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /slas(*slaid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /slas(*slaid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /slas<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /slas(*slaid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /slas(*slaid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /slas(*slaid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the SLA table.

|Property|Value|
| --- | --- |
| **DisplayName** | **SLA** |
| **DisplayCollectionName** | **SLAs** |
| **SchemaName** | `SLA` |
| **CollectionSchemaName** | `SLAs` |
| **EntitySetName** | `slas`|
| **LogicalName** | `sla` |
| **LogicalCollectionName** | `slas` |
| **PrimaryIdAttribute** | `slaid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AllowPauseResume](#BKMK_AllowPauseResume)
- [ApplicableFrom](#BKMK_ApplicableFrom)
- [ApplicableFromPickList](#BKMK_ApplicableFromPickList)
- [BusinessHoursId](#BKMK_BusinessHoursId)
- [ChangedAttributeList](#BKMK_ChangedAttributeList)
- [Description](#BKMK_Description)
- [IsDefault](#BKMK_IsDefault)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PrimaryEntityOTC](#BKMK_PrimaryEntityOTC)
- [SLAId](#BKMK_SLAId)
- [SLAType](#BKMK_SLAType)
- [slaversion](#BKMK_slaversion)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [WorkflowId](#BKMK_WorkflowId)

### <a name="BKMK_AllowPauseResume"></a> AllowPauseResume

|Property|Value|
|---|---|
|Description|**Select whether this SLA will allow pausing and resuming during the time calculation.**|
|DisplayName|**Allow Pause and Resume**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`allowpauseresume`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`sla_allowpauseresume`|
|DefaultValue|False|
|True Label|Allow|
|False Label|Do Not Allow|

### <a name="BKMK_ApplicableFrom"></a> ApplicableFrom

|Property|Value|
|---|---|
|Description|**Select the field that specifies the date and time from which the SLA items will be calculated for the case record. For example, if you select the Case Created On field, SLA calculation will begin from the time the case is created.**|
|DisplayName|**Applicable From**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicablefrom`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ApplicableFromPickList"></a> ApplicableFromPickList

|Property|Value|
|---|---|
|Description|**Select the field that specifies the date and time from which the SLA items will be calculated. For example, if you select the Case Created On field, SLA calculation will begin from the time the case is created.**|
|DisplayName|**Applicable From**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicablefrompicklist`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`slabase_applicablefrom`|

#### ApplicableFromPickList Choices/Options

|Value|Label|
|---|---|
|1|**No**|
|2|**Yes**|

### <a name="BKMK_BusinessHoursId"></a> BusinessHoursId

|Property|Value|
|---|---|
|Description|**Choose the business hours for calculating SLA item timelines.**|
|DisplayName|**Business Hours**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`businesshoursid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|calendar|

### <a name="BKMK_ChangedAttributeList"></a> ChangedAttributeList

|Property|Value|
|---|---|
|Description|**Type additional information to describe the SLA**|
|DisplayName|**ChangedAttributeList**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`changedattributelist`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type additional information to describe the SLA**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|---|---|
|Description|**Tells whether this SLA is the default one.**|
|DisplayName|**Is Default**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdefault`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sla_isdefault`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Type a descriptive name of the service level agreement (SLA).**|
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
|MaxLength|100|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user or team who owns the SLA. This field is updated every time the item is assigned to a different user.**|
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

### <a name="BKMK_PrimaryEntityOTC"></a> PrimaryEntityOTC

|Property|Value|
|---|---|
|Description|**Shows the primary entity that the SLA has been created for.**|
|DisplayName|**Primary Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`primaryentityotc`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SLA.**|
|DisplayName|**SLA**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`slaid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SLAType"></a> SLAType

|Property|Value|
|---|---|
|Description|**Select the type of service level agreement (SLA).**|
|DisplayName|**SLA Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`slatype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sla_slatype`|

#### SLAType Choices/Options

|Value|Label|
|---|---|
|0|**Standard**|
|1|**Enhanced**|

### <a name="BKMK_slaversion"></a> slaversion

|Property|Value|
|---|---|
|Description||
|DisplayName|**Record version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`slaversion`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`sla_slaversion`|

#### slaversion Choices/Options

|Value|Label|
|---|---|
|100000000|**Version WC**|
|100000001|**Version UC**|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the Service Level Agreement (SLA) is active or inactive.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`sla_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Draft**<br />DefaultStatus: 1<br />InvariantName: `Draft`|
|1|Label: **Active**<br />DefaultStatus: 2<br />InvariantName: `Active`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the status of the service level agreement (SLA).**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|1|
|GlobalChoiceName|`sla_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Draft**<br />State:0<br />TransitionData: None|
|2|Label: **Active**<br />State:1<br />TransitionData: None|

### <a name="BKMK_WorkflowId"></a> WorkflowId

|Property|Value|
|---|---|
|Description|**Workflow associated with the SLA.**|
|DisplayName|**Workflow ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workflowid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [SLAIdUnique](#BKMK_SLAIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [VersionNumber](#BKMK_VersionNumber)

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
|DefaultFormValue|-1|
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
|Description|**Shows who created the record.**|
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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate between the currency associated with the SLA record and the base currency.**|
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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**For internal use only.**|
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
|Description|**Shows who last updated the record.**|
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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Choose the entity type that the SLA is defined.**|
|DisplayName|**Object Type Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`sla_objecttypecode`|

#### ObjectTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Account**|
|2|**Contact**|
|5|**Note**|
|6|**Business Unit Map**|
|7|**Owner**|
|8|**User**|
|9|**Team**|
|10|**Business Unit**|
|14|**System User Principal**|
|29|**Subscription**|
|30|**Filter Template**|
|31|**Privilege Object Type Code**|
|33|**Subscription Synchronization Information**|
|35|**Tracking information for deleted entities**|
|36|**Client update**|
|37|**Subscription Manually Tracked Object**|
|42|**SystemUser BusinessUnit Entity Map**|
|44|**Field Sharing**|
|45|**Subscription Statistic Offline**|
|46|**Subscription Statistic Outlook**|
|47|**Subscription Sync Entry Offline**|
|48|**Subscription Sync Entry Outlook**|
|50|**Position**|
|51|**System User Manager Map**|
|52|**User Search Facet**|
|54|**Global Search Configuration**|
|55|**FileAttachment**|
|60|**SystemUserAuthorizationChangeTracker**|
|72|**Record Filter**|
|73|**EntityRecordFilter**|
|74|**Secured Masking Rule**|
|75|**Privilege Checker Run**|
|76|**Privilege Checker Log**|
|78|**Virtual Entity Data Provider**|
|85|**Virtual Entity Data Source**|
|92|**Team template**|
|99|**Social Profile**|
|101|**Service Plan**|
|103|**Privileges Removal Setting**|
|126|**Indexed Article**|
|127|**Article**|
|129|**Subject**|
|132|**Announcement**|
|135|**Activity Party**|
|150|**User Settings**|
|300|**Canvas App**|
|301|**Callback Registration**|
|372|**Connector**|
|373|**Connection Instance**|
|380|**Environment Variable Definition**|
|381|**Environment Variable Value**|
|400|**AI Template**|
|401|**AI Model**|
|402|**AI Configuration**|
|418|**Dataflow**|
|430|**Entity Analytics Config**|
|431|**Image Attribute Configuration**|
|432|**Entity Image Configuration**|
|950|**New Process**|
|951|**Translation Process**|
|955|**Expired Process**|
|1001|**Attachment**|
|1002|**Attachment**|
|1003|**Internal Address**|
|1007|**Image Descriptor**|
|1016|**Article Template**|
|1019|**Organization**|
|1021|**Organization UI**|
|1023|**Privilege**|
|1030|**System Form**|
|1031|**User Dashboard**|
|1036|**Security Role**|
|1037|**Role Template**|
|1039|**View**|
|1043|**String Map**|
|1071|**Address**|
|1072|**Subscription Clients**|
|1075|**Status Map**|
|1082|**Article Comment**|
|1086|**User Fiscal Calendar**|
|1094|**Authorization Server**|
|1095|**Partner Application**|
|1111|**System Chart**|
|1112|**User Chart**|
|1113|**Ribbon Tab To Command Mapping**|
|1115|**Ribbon Context Group**|
|1116|**Ribbon Command**|
|1117|**Ribbon Rule**|
|1120|**Application Ribbons**|
|1130|**Ribbon Difference**|
|1140|**Replication Backlog**|
|1189|**Document Suggestions**|
|1190|**SuggestionCardTemplate**|
|1200|**Field Security Profile**|
|1201|**Field Permission**|
|1203|**Team Profiles**|
|1204|**Application**|
|1234|**Channel Property Group**|
|1236|**Channel Property**|
|1300|**SocialInsightsConfiguration**|
|1309|**Saved Organization Insights Configuration**|
|1400|**Sync Attribute Mapping Profile**|
|1401|**Sync Attribute Mapping**|
|1403|**Team Sync-Attribute Mapping Profiles**|
|1404|**Principal Sync Attribute Map**|
|2000|**Annual Fiscal Calendar**|
|2001|**Semiannual Fiscal Calendar**|
|2002|**Quarterly Fiscal Calendar**|
|2003|**Monthly Fiscal Calendar**|
|2004|**Fixed Monthly Fiscal Calendar**|
|2010|**Email Template**|
|2012|**Unresolved Address**|
|2013|**Territory**|
|2015|**Theme**|
|2016|**User Mapping**|
|2020|**Queue**|
|2023|**QueueItemCount**|
|2024|**QueueMemberCount**|
|2027|**License**|
|2029|**Queue Item**|
|2500|**User Entity UI Settings**|
|2501|**User Entity Instance Data**|
|3000|**Integration Status**|
|3005|**Channel Access Profile**|
|3008|**External Party**|
|3231|**Connection Role**|
|3233|**Connection Role Object Type Code**|
|3234|**Connection**|
|4003|**Calendar**|
|4004|**Calendar Rule**|
|4011|**Inter Process Lock**|
|4023|**Email Hash**|
|4101|**Display String Map**|
|4102|**Display String**|
|4110|**Notification**|
|4120|**Exchange Sync Id Mapping**|
|4200|**Activity**|
|4201|**Appointment**|
|4202|**Email**|
|4204|**Fax**|
|4207|**Letter**|
|4210|**Phone Call**|
|4212|**Task**|
|4216|**Social Activity**|
|4220|**UntrackedEmail**|
|4230|**Saved View**|
|4231|**Metadata Difference**|
|4232|**Business Data Localized Label**|
|4250|**Recurrence Rule**|
|4251|**Recurring Appointment**|
|4299|**Email Search**|
|4410|**Data Import**|
|4411|**Data Map**|
|4412|**Import Source File**|
|4413|**Import Data**|
|4414|**Duplicate Detection Rule**|
|4415|**Duplicate Record**|
|4416|**Duplicate Rule Condition**|
|4417|**Column Mapping**|
|4418|**List Value Mapping**|
|4419|**Lookup Mapping**|
|4420|**Owner Mapping**|
|4423|**Import Log**|
|4424|**Bulk Delete Operation**|
|4425|**Bulk Delete Failure**|
|4426|**Transformation Mapping**|
|4427|**Transformation Parameter Mapping**|
|4428|**Import Entity Mapping**|
|4450|**Data Performance Dashboard**|
|4490|**Office Document**|
|4500|**Relationship Role**|
|4501|**Relationship Role Map**|
|4502|**Customer Relationship**|
|4567|**Auditing**|
|4579|**Ribbon Client Metadata.**|
|4600|**Entity Map**|
|4601|**Attribute Map**|
|4602|**Plug-in Type**|
|4603|**Plug-in Type Statistic**|
|4605|**Plug-in Assembly**|
|4606|**Sdk Message**|
|4607|**Sdk Message Filter**|
|4608|**Sdk Message Processing Step**|
|4609|**Sdk Message Request**|
|4610|**Sdk Message Response**|
|4611|**Sdk Message Response Field**|
|4613|**Sdk Message Pair**|
|4614|**Sdk Message Request Field**|
|4615|**Sdk Message Processing Step Image**|
|4616|**Sdk Message Processing Step Secure Configuration**|
|4618|**Service Endpoint**|
|4619|**Plug-in Trace Log**|
|4700|**System Job**|
|4702|**Workflow Wait Subscription**|
|4703|**Process**|
|4704|**Process Dependency**|
|4705|**ISV Config**|
|4706|**Process Log**|
|4707|**Application File**|
|4708|**Organization Statistic**|
|4709|**Site Map**|
|4710|**Process Session**|
|4711|**Expander Event**|
|4712|**Process Trigger**|
|4720|**Flow Session**|
|4724|**Process Stage**|
|4725|**Business Process Flow Instance**|
|4800|**Web Wizard**|
|4802|**Wizard Page**|
|4803|**Web Wizard Access Privilege**|
|4810|**Time Zone Definition**|
|4811|**Time Zone Rule**|
|4812|**Time Zone Localized Name**|
|5000|**Recently Used**|
|5004|**NL2SQ Registration Information**|
|5006|**Event Expander Breadcrumb**|
|7000|**System Application Metadata**|
|7001|**User Application Metadata**|
|7100|**Solution**|
|7101|**Publisher**|
|7102|**Publisher Address**|
|7103|**Solution Component**|
|7104|**Solution Component Definition**|
|7105|**Dependency**|
|7106|**Dependency Node**|
|7107|**Invalid Dependency**|
|7108|**Dependency Feature**|
|7200|**RuntimeDependency**|
|7755|**ElasticFileAttachment**|
|8000|**Post**|
|8001|**Post Role**|
|8002|**Post Regarding**|
|8003|**Follow**|
|8005|**Comment**|
|8006|**Like**|
|8040|**ACIViewMapper**|
|8050|**Trace**|
|8051|**Trace Association**|
|8052|**Trace Regarding**|
|8181|**Routing Rule Set**|
|8199|**Rule Item**|
|8700|**AppModule Metadata**|
|8701|**AppModule Metadata Dependency**|
|8702|**AppModule Metadata Async Operation**|
|8840|**Hierarchy Rule**|
|9006|**Model-driven App**|
|9007|**App Module Component**|
|9009|**App Module Roles**|
|9011|**App Config Master**|
|9012|**App Configuration**|
|9013|**App Configuration Instance**|
|9100|**Report**|
|9101|**Report Related Entity**|
|9102|**Report Related Category**|
|9103|**Report Visibility**|
|9104|**Report Link**|
|9105|**Currency**|
|9106|**Mail Merge Template**|
|9107|**Import Job**|
|9201|**LocalConfigStore**|
|9300|**Record Creation and Update Rule**|
|9301|**Record Creation and Update Rule Item**|
|9333|**Web Resource**|
|9400|**Channel Access Profile Rule**|
|9401|**Channel Access Profile Rule Item**|
|9502|**SharePoint Site**|
|9507|**Sharepoint Document**|
|9508|**Document Location**|
|9509|**SharePoint Data**|
|9510|**Rollup Properties**|
|9511|**Rollup Job**|
|9600|**Goal**|
|9602|**Rollup Query**|
|9603|**Goal Metric**|
|9604|**Rollup Field**|
|9605|**Email Server Profile**|
|9606|**Mailbox**|
|9607|**Mailbox Statistics**|
|9608|**Mailbox Auto Tracking Folder**|
|9609|**Mailbox Tracking Category**|
|9650|**Process Configuration**|
|9690|**Organization Insights Notification**|
|9699|**Organization Insights Metric**|
|9750|**SLA**|
|9751|**SLA Item**|
|9752|**SLA KPI Instance**|
|9753|**Custom Control**|
|9754|**Custom Control Resource**|
|9755|**Custom Control Default Config**|
|9800|**Entity**|
|9808|**Attribute**|
|9809|**OptionSet**|
|9810|**Entity Key**|
|9811|**Entity Relationship**|
|9812|**Managed Property**|
|9813|**Relationship Entity**|
|9814|**Relationship Attribute**|
|9815|**Entity Index**|
|9816|**Index Attribute**|
|9817|**Option Set Value**|
|9820|**Secured Masking Column**|
|9866|**Mobile Offline Profile**|
|9867|**Mobile Offline Profile Item**|
|9868|**Mobile Offline Profile Item Association**|
|9869|**Sync Error**|
|9870|**Offline Command Definition**|
|9875|**Language Provisioning State**|
|9880|**Ribbon Metadata To Process**|
|9890|**SolutionHistoryData**|
|9900|**Navigation Setting**|
|9910|**MultiEntitySearch**|
|9912|**Multi Select Option Value**|
|9919|**Hierarchy Security Configuration**|
|9930|**Knowledge Base Record**|
|9932|**Time Stamp Date Mapping**|
|9936|**Azure Service Connection**|
|9940|**Document Template**|
|9941|**Personal Document Template**|
|9945|**Text Analytics Entity Mapping**|
|9947|**Knowledge Search Model**|
|9949|**Advanced Similarity Rule**|
|9950|**Office Graph Document**|
|9951|**Similarity Rule**|
|9953|**Knowledge Article**|
|9955|**Knowledge Article Views**|
|9957|**Language**|
|9958|**Feedback**|
|9959|**Category**|
|9960|**Knowledge Article Category**|
|9961|**DelveActionHub**|
|9962|**Action Card**|
|9968|**ActionCardUserState**|
|9973|**Action Card User Settings**|
|9983|**Action Card Type**|
|9986|**Interaction for Email**|
|9987|**External Party Item**|
|9996|**HolidayWrapper**|
|9997|**Email Signature**|
|10000|**Solution Component Attribute Configuration**|
|10001|**Solution Component Batch Configuration**|
|10002|**Solution Component Configuration**|
|10003|**Solution Component Relationship Configuration**|
|10004|**Solution History**|
|10005|**Solution History Data Source**|
|10006|**Component Layer**|
|10007|**Component Layer Data Source**|
|10008|**Package**|
|10009|**Package History**|
|10011|**StageSolutionUpload**|
|10012|**ExportSolutionUpload**|
|10013|**FeatureControlSetting**|
|10014|**Solution Component Summary**|
|10015|**Solution Component Count Summary**|
|10016|**Solution Component Data Source**|
|10017|**Solution Component Count Data Source**|
|10018|**Microsoft Entra ID**|
|10019|**Staged attribute lookup value**|
|10020|**Staged attribute picklist value**|
|10021|**Staged Entity**|
|10022|**Staged Entity Attribute**|
|10023|**Staged entity relationship**|
|10024|**Staged entity relationship relationships**|
|10025|**Staged entity relationship role**|
|10026|**Staged Metadata Async Operation**|
|10027|**Staged optionset**|
|10028|**Staged relationship**|
|10029|**Staged relationship**|
|10030|**Staged relationship**|
|10031|**Key Vault Reference**|
|10032|**Managed Identity**|
|10033|**Catalog**|
|10034|**Catalog Assignment**|
|10035|**Internal Catalog Assignment**|
|10036|**Custom API**|
|10037|**Custom API Request Parameter**|
|10038|**Custom API Response Property**|
|10039|**Plugin Package**|
|10040|**Sensitivity Label**|
|10041|**NonRelational Data Source**|
|10042|**ProvisionLanguageForUser**|
|10043|**Purview Label Info**|
|10044|**Purview Label Sync Cache**|
|10045|**Sensitivity Label Attribute Mapping**|
|10046|**Shared Object**|
|10047|**Shared Workspace**|
|10048|**Shared Workspace Access Token**|
|10049|**Shared Workspace Pool**|
|10050|**Data Lake Folder**|
|10051|**Data Lake Folder Permission**|
|10052|**Data Lake Workspace**|
|10053|**Data Lake Workspace Permission**|
|10054|**Data Processing configuration**|
|10055|**Exported Excel**|
|10056|**RetainedData Excel**|
|10057|**Synapse Database**|
|10058|**Synapse Link External Table State**|
|10059|**Synapse Link Profile**|
|10060|**Synapse Link Profile Entity**|
|10061|**Synapse Link Profile Entity State**|
|10062|**Synapse Link Schedule**|
|10063|**Component Changeset Payload**|
|10064|**Component Changeset Version**|
|10065|**Component Version**|
|10066|**Component Version Data Source**|
|10067|**Component Version (Internal)**|
|10068|**Git Branch**|
|10069|**Git Configuration Retrieval Data Source**|
|10070|**Git Organization**|
|10071|**Git Project**|
|10072|**Git Repository**|
|10073|**Git Solution**|
|10074|**Source Control Branch Configuration**|
|10075|**Source Control Component**|
|10076|**Source Control Component Payload**|
|10077|**Source Control Configuration**|
|10078|**Staged Source Control Component**|
|10079|**DataflowRefreshHistory**|
|10080|**EntityRefreshHistory**|
|10081|**Shared Link Setting**|
|10082|**DelegatedAuthorization**|
|10084|**CascadeGrantRevokeAccessRecordsTracker**|
|10085|**CascadeGrantRevokeAccessVersionTracker**|
|10086|**RevokeInheritedAccessRecordsTracker**|
|10087|**TdsMetadata**|
|10088|**Model-Driven App Element**|
|10089|**Model-Driven App Component Node's Edge**|
|10090|**Model-Driven App Component Node**|
|10091|**Model-Driven App Setting**|
|10092|**Model-Driven App User Setting**|
|10093|**Organization Setting**|
|10094|**Setting Definition**|
|10095|**CanvasApp Extended Metadata**|
|10096|**Service Plan Mapping**|
|10097|**Service Plan Custom Control**|
|10099|**ApplicationUser**|
|10102|**OData v4 Data Source**|
|10103|**Workflow Binary**|
|10104|**Business Process**|
|10105|**Credential**|
|10106|**Desktop Flow Module**|
|10107|**Flow Capacity Assignment**|
|10108|**Flow Credential Application**|
|10109|**Flow Event**|
|10110|**Flow Machine**|
|10111|**Flow Machine Group**|
|10112|**Flow Machine Image**|
|10113|**Flow Machine Image Version**|
|10114|**Flow Machine Network**|
|10115|**Flow Session Binary**|
|10116|**ProcessStageParameter**|
|10117|**Saving Rule**|
|10118|**Tag**|
|10119|**Tagged Flow Session**|
|10120|**Tagged Process**|
|10121|**Workflow Metadata**|
|10122|**Work Queue**|
|10123|**Work Queue Item**|
|10124|**Desktop Flow Binary**|
|10125|**Flow Aggregation**|
|10126|**Flow Log**|
|10127|**Flow Run**|
|10128|**Approval Process**|
|10129|**Approval Stage Approval**|
|10130|**Approval Stage Condition**|
|10131|**Approval Stage Intelligent**|
|10132|**Approval Stage Order**|
|10133|**Action Approval Model**|
|10134|**Approval**|
|10135|**Approval Request**|
|10136|**Approval Response**|
|10137|**Approval Step**|
|10138|**Await All Action Approval Model**|
|10139|**Await All Approval Model**|
|10140|**Basic Approval Model Data**|
|10141|**Flow Approval**|
|10150|**Connection Reference**|
|10151|**Knowledge Source Consumer**|
|10152|**Knowledge Source Profile**|
|10153|**UnstructuredFileSearchEntity**|
|10154|**UnstructuredFileSearchRecord**|
|10155|**DVFileSearch**|
|10156|**DVFileSearchAttribute**|
|10157|**DVFileSearchEntity**|
|10158|**DVTableSearch**|
|10159|**DVTableSearchAttribute**|
|10160|**DVTableSearchEntity**|
|10161|**AICopilot**|
|10162|**AIPluginAuth**|
|10163|**AI Plugin Conversation Starter**|
|10164|**AI Plugin Conversation Starter Mapping**|
|10165|**AI Plugin Governance**|
|10166|**AI Plugin Governance Extended**|
|10167|**AIPluginOperationResponseTemplate**|
|10168|**AIPluginTitle**|
|10169|**SideloadedAIPlugin**|
|10170|**AIPlugin**|
|10171|**AIPluginExternalSchema**|
|10172|**AIPluginExternalSchemaProperty**|
|10173|**AIPluginInstance**|
|10174|**AIPluginOperation**|
|10175|**AIPluginOperationParameter**|
|10176|**AIPluginUserSetting**|
|10178|**AI Configuration Search**|
|10179|**Data Processing Event**|
|10180|**AI Document Template**|
|10181|**AI Event**|
|10182|**AI Model Catalog**|
|10184|**AI Builder Feedback Loop**|
|10185|**AI Form Processing Document**|
|10186|**AI Object Detection Image**|
|10187|**AI Object Detection Label**|
|10188|**AI Object Detection Bounding Box**|
|10189|**AI Object Detection Image Mapping**|
|10191|**AI Builder Dataset**|
|10192|**AI Builder Dataset File**|
|10193|**AI Builder Dataset Record**|
|10194|**AI Builder Datasets Container**|
|10195|**AI Builder File**|
|10196|**AI Builder File Attached Data**|
|10197|**AI Evaluation Configuration**|
|10198|**AI Evaluation Metric**|
|10199|**AI Evaluation Run**|
|10200|**AI Optimization**|
|10201|**AI Optimization Private Data**|
|10202|**AI Test Case**|
|10203|**AI Test Case Document**|
|10204|**AI Test Case Input**|
|10205|**AI Test Run**|
|10206|**AI Test Run Batch**|
|10207|**Help Page**|
|10208|**Tour**|
|10209|**BotContent**|
|10210|**ConversationTranscript**|
|10211|**Copilot**|
|10212|**Copilot component**|
|10213|**Copilot component collection**|
|10224|**Comment**|
|10225|**Governance Configuration**|
|10226|**Fabric AISkill**|
|10227|**App Insights Metadata**|
|10228|**Dataflow Connection Reference**|
|10229|**Schedule**|
|10230|**Dataflow Template**|
|10231|**Dataflow DatalakeFolder**|
|10232|**Data Movement Service Request**|
|10233|**Data Movement Service Request Status**|
|10234|**DMS Sync Request**|
|10235|**DMS Sync Status**|
|10236|**Knowledge Asset Configuration**|
|10237|**Module Run Detail**|
|10238|**QnA**|
|10239|**Salesforce Structured Object**|
|10240|**Salesforce Structured QnA Config**|
|10241|**Workflow Action Status**|
|10242|**Allowed MCP Client**|
|10243|**FederatedKnowledgeCitation**|
|10244|**FederatedKnowledgeConfiguration**|
|10245|**FederatedKnowledgeEntityConfiguration**|
|10246|**FederatedKnowledgeMetadataRefresh**|
|10247|**IntelligentMemory**|
|10248|**Knowledge FAQ**|
|10249|**Form Mapping**|
|10250|**Copilot Interactions**|
|10251|**PDF Setting**|
|10252|**Activity File Attachment**|
|10253|**Teams chat**|
|10254|**Service Configuration**|
|10255|**SLA KPI**|
|10256|**Integrated search provider**|
|10257|**Knowledge Management Setting**|
|10258|**Knowledge Federated Article**|
|10259|**Knowledge Federated Article Incident**|
|10260|**Search provider**|
|10261|**Knowledge Article Image**|
|10262|**Knowledge Configuration**|
|10263|**Knowledge Interaction Insight**|
|10264|**Knowledge Search Insight**|
|10265|**Favorite knowledge article**|
|10266|**Knowledge article language setting**|
|10267|**Knowledge Article Attachment**|
|10268|**Knowledge personalization**|
|10269|**Knowledge Article Template**|
|10270|**Knowledge search personal filter config**|
|10271|**Knowledge search filter**|
|10273|**msdyn\_historicalcaseharvestbatch**|
|10274|**msdyn\_historicalcaseharvestrun**|
|10275|**Interim Update Knowledge Article**|
|10276|**Knowledge Article Custom Entity**|
|10277|**Knowledge Harvest Job Record**|
|10278|**Attribute Cluster Config**|
|10279|**Entity Cluster Configuration**|
|10280|**SupportUserTable**|
|10281|**FxExpression**|
|10282|**Function**|
|10283|**Plug-in**|
|10284|**PowerfxRule**|
|10285|**Planner Business Scenario**|
|10286|**Planner Sync Action**|
|10287|**Email Address Configuration**|
|10288|**Ms Graph Resource To Subscription**|
|10289|**Virtual Entity  Metadata**|
|10290|**Background Operation**|
|10291|**Report Parameter**|
|10292|**MobileOfflineProfileExtension**|
|10293|**MobileOfflineProfileItemFilter**|
|10294|**TeamMobileOfflineProfileMembership**|
|10295|**UserMobileOfflineProfileMembership**|
|10296|**OrganizationDataSyncSubscription**|
|10297|**OrganizationDataSyncSubscriptionEntity**|
|10298|**OrganizationDataSyncSubscriptionFnoTable**|
|10299|**OrganizationDataSyncFnoState**|
|10300|**OrganizationDataSyncState**|
|10301|**ArchiveCleanupInfo**|
|10302|**ArchiveCleanupOperation**|
|10303|**BulkArchiveConfig**|
|10304|**BulkArchiveFailureDetail**|
|10305|**BulkArchiveOperation**|
|10306|**BulkArchiveOperationDetail**|
|10307|**EnableArchivalRequest**|
|10308|**MetadataForArchival**|
|10309|**ReconciliationEntityInfo**|
|10310|**ReconciliationEntityStepInfo**|
|10311|**ReconciliationInfo**|
|10312|**RetentionCleanupInfo**|
|10313|**RetentionCleanupOperation**|
|10314|**RetentionConfig**|
|10315|**RetentionFailureDetail**|
|10316|**RetentionOperation**|
|10317|**RetentionOperationDetail**|
|10318|**RetentionSuccessDetail**|
|10319|**CertificateCredential**|
|10320|**Notification**|
|10321|**User Rating**|
|10322|**Mobile App**|
|10323|**Insights Store Data Source**|
|10324|**Insights Store Virtual Entity**|
|10325|**RoleEditorLayout**|
|10326|**Deleted Record Reference**|
|10327|**Restore Deleted Records Configuration**|
|10328|**App Action**|
|10329|**App Action Migration**|
|10330|**App Action Rule**|
|10333|**Card**|
|10334|**Card State Item**|
|10337|**Entity link chat configuration**|
|10338|**SharePoint Managed Identity**|
|10339|**AI Insight Card**|
|10340|**AI Skill Config**|
|10341|**Suggested Action**|
|10342|**Suggested Action Criteria**|
|10343|**Data Workspace**|
|10344|**Plan**|
|10345|**Plan Artifact**|
|10346|**Plan Attachment**|
|10347|**UX Agent Component**|
|10348|**UX Agent Component Revision**|
|10349|**UX Agent Project**|
|10350|**UX Agent Project File**|
|10351|**Agent Conversation Message**|
|10352|**Agent Conversation Message File**|
|10353|**Rich Text Attachment**|
|10354|**Custom Control Extended Setting**|
|10355|**Timeline Pin**|
|10356|**Virtual Connector Data Source**|
|10357|**Virtual Table Column Candidate**|
|10359|**PM Analysis History**|
|10360|**PM Business Rule Automation Config**|
|10361|**PM Calendar**|
|10362|**PM Calendar Version**|
|10363|**PM Inferred Task**|
|10364|**PM Process Extended Metadata Version**|
|10365|**PM Process Template**|
|10366|**PM Process User Settings**|
|10367|**PM Process Version**|
|10368|**PM Recording**|
|10369|**PM Simulation**|
|10370|**PM Tab**|
|10371|**PM Template**|
|10372|**PM View**|
|10373|**Analysis Component**|
|10374|**Analysis Job**|
|10375|**Analysis Override**|
|10376|**Analysis Result**|
|10377|**Analysis Result Detail**|
|10378|**Solution Health Rule**|
|10379|**Solution Health Rule Argument**|
|10380|**Solution Health Rule Set**|
|10381|**Power BI Dataset**|
|10382|**powerbidatasetapdx**|
|10383|**Power BI Mashup Parameter**|
|10384|**Power BI Report**|
|10385|**powerbireportapdx**|
|10386|**File Upload**|
|10387|**AppEntitySearchView**|
|10388|**MainFewShot**|
|10389|**MakerFewShot**|
|10390|**SearchAttributeSettings**|
|10391|**SearchCustomAnalyzer**|
|10392|**SearchRelationshipSettings**|
|10393|**SearchResultsCache**|
|10394|**Search Telemetry**|
|10395|**TextDataRecordsIndexingStatus**|
|10396|**ViewAsExampleQuestion**|
|10397|**CopilotExampleQuestion**|
|10398|**CopilotGlossaryTerm**|
|10399|**CopilotSynonyms**|
|10400|**Site Component**|
|10401|**Site**|
|10402|**Site Language**|
|10403|**Power Pages Site Published**|
|10404|**Site Source File**|
|10407|**External Identity**|
|10408|**Invitation**|
|10409|**Invite Redemption**|
|10410|**Portal Comment**|
|10411|**Setting**|
|10412|**Multistep Form Session**|
|10416|**Ad Placement**|
|10417|**Column Permission**|
|10418|**Column Permission Profile**|
|10419|**Content Snippet**|
|10420|**Basic Form**|
|10421|**Basic Form Metadata**|
|10422|**List**|
|10423|**Table Permission**|
|10424|**Page Template**|
|10425|**Poll Placement**|
|10426|**Power Pages Core Entity DS**|
|10427|**Publishing State**|
|10428|**Publishing State Transition Rule**|
|10429|**Redirect**|
|10430|**Shortcut**|
|10431|**Site Marker**|
|10432|**Site Setting**|
|10433|**Web File**|
|10434|**Multistep Form**|
|10435|**Multistep Form Metadata**|
|10436|**Form Step**|
|10437|**Web Link**|
|10438|**Web Link Set**|
|10439|**Web Page**|
|10440|**Web Page Access Control Rule**|
|10441|**Web Role**|
|10442|**Website**|
|10443|**Website Access**|
|10444|**Website Language**|
|10445|**Web Template**|
|10452|**Power Pages Scan Report**|
|10453|**PowerPagesDDOSAlert**|
|10454|**Power Pages Log**|
|10455|**PowerPagesManagedIdentity**|
|10456|**Power Pages Site AI Feedback**|
|10462|**Catalog Submission Files**|
|10463|**Package Submission Store**|
|10464|**indexedtrait**|
|10465|**processor registration**|
|10466|**signal**|
|10467|**signal registration**|
|10468|**trait**|
|10469|**trait registration**|

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
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

### <a name="BKMK_SLAIdUnique"></a> SLAIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`slaidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the currency associated with the SLA record.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the SLA.**|
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

- [business_unit_slabase](#BKMK_business_unit_slabase)
- [lk_slabase_createdby](#BKMK_lk_slabase_createdby)
- [lk_slabase_createdonbehalfby](#BKMK_lk_slabase_createdonbehalfby)
- [lk_slabase_modifiedby](#BKMK_lk_slabase_modifiedby)
- [lk_slabase_modifiedonbehalfby](#BKMK_lk_slabase_modifiedonbehalfby)
- [owner_slas](#BKMK_owner_slas)
- [slabase_businesshoursid](#BKMK_slabase_businesshoursid)
- [slabase_workflowid](#BKMK_slabase_workflowid)
- [team_slaBase](#BKMK_team_slaBase)
- [TransactionCurrency_SLA](#BKMK_TransactionCurrency_SLA)
- [user_slabase](#BKMK_user_slabase)

### <a name="BKMK_business_unit_slabase"></a> business_unit_slabase

One-To-Many Relationship: [businessunit business_unit_slabase](businessunit.md#BKMK_business_unit_slabase)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slabase_createdby"></a> lk_slabase_createdby

One-To-Many Relationship: [systemuser lk_slabase_createdby](systemuser.md#BKMK_lk_slabase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slabase_createdonbehalfby"></a> lk_slabase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_slabase_createdonbehalfby](systemuser.md#BKMK_lk_slabase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slabase_modifiedby"></a> lk_slabase_modifiedby

One-To-Many Relationship: [systemuser lk_slabase_modifiedby](systemuser.md#BKMK_lk_slabase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slabase_modifiedonbehalfby"></a> lk_slabase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_slabase_modifiedonbehalfby](systemuser.md#BKMK_lk_slabase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_slas"></a> owner_slas

One-To-Many Relationship: [owner owner_slas](owner.md#BKMK_owner_slas)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slabase_businesshoursid"></a> slabase_businesshoursid

One-To-Many Relationship: [calendar slabase_businesshoursid](calendar.md#BKMK_slabase_businesshoursid)

|Property|Value|
|---|---|
|ReferencedEntity|`calendar`|
|ReferencedAttribute|`calendarid`|
|ReferencingAttribute|`businesshoursid`|
|ReferencingEntityNavigationPropertyName|`businesshoursid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slabase_workflowid"></a> slabase_workflowid

One-To-Many Relationship: [workflow slabase_workflowid](workflow.md#BKMK_slabase_workflowid)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`workflowid`|
|ReferencingEntityNavigationPropertyName|`workflowid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_slaBase"></a> team_slaBase

One-To-Many Relationship: [team team_slaBase](team.md#BKMK_team_slaBase)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_SLA"></a> TransactionCurrency_SLA

One-To-Many Relationship: [transactioncurrency TransactionCurrency_SLA](transactioncurrency.md#BKMK_TransactionCurrency_SLA)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_slabase"></a> user_slabase

One-To-Many Relationship: [systemuser user_slabase](systemuser.md#BKMK_user_slabase)

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

- [adx_inviteredemption_sla_slaid](#BKMK_adx_inviteredemption_sla_slaid)
- [adx_inviteredemption_sla_slainvokedid](#BKMK_adx_inviteredemption_sla_slainvokedid)
- [adx_portalcomment_sla_slaid](#BKMK_adx_portalcomment_sla_slaid)
- [adx_portalcomment_sla_slainvokedid](#BKMK_adx_portalcomment_sla_slainvokedid)
- [chat_sla_slaid](#BKMK_chat_sla_slaid)
- [chat_sla_slainvokedid](#BKMK_chat_sla_slainvokedid)
- [manualsla_account](#BKMK_manualsla_account)
- [manualsla_activitypointer](#BKMK_manualsla_activitypointer)
- [manualsla_appointment](#BKMK_manualsla_appointment)
- [manualsla_contact](#BKMK_manualsla_contact)
- [manualsla_email](#BKMK_manualsla_email)
- [manualsla_fax](#BKMK_manualsla_fax)
- [manualsla_letter](#BKMK_manualsla_letter)
- [manualsla_phonecall](#BKMK_manualsla_phonecall)
- [manualsla_socialactivity](#BKMK_manualsla_socialactivity)
- [manualsla_task](#BKMK_manualsla_task)
- [sla_account](#BKMK_sla_account)
- [sla_activitypointer](#BKMK_sla_activitypointer)
- [sla_Annotation](#BKMK_sla_Annotation)
- [sla_appointment](#BKMK_sla_appointment)
- [sla_contact](#BKMK_sla_contact)
- [sla_email](#BKMK_sla_email)
- [sla_fax](#BKMK_sla_fax)
- [sla_letter](#BKMK_sla_letter)
- [sla_phonecall](#BKMK_sla_phonecall)
- [sla_slaitem_slaId](#BKMK_sla_slaitem_slaId)
- [sla_socialactivity](#BKMK_sla_socialactivity)
- [SLA_SyncErrors](#BKMK_SLA_SyncErrors)
- [sla_task](#BKMK_sla_task)
- [slabase_AsyncOperations](#BKMK_slabase_AsyncOperations)
- [slabase_BulkDeleteFailures](#BKMK_slabase_BulkDeleteFailures)
- [slabase_ProcessSessions](#BKMK_slabase_ProcessSessions)

### <a name="BKMK_adx_inviteredemption_sla_slaid"></a> adx_inviteredemption_sla_slaid

Many-To-One Relationship: [adx_inviteredemption adx_inviteredemption_sla_slaid](adx_inviteredemption.md#BKMK_adx_inviteredemption_sla_slaid)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`adx_inviteredemption_sla_slaid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10001<br />QueryApi: null<br />ViewId: `7f15e2bb-305a-468f-9af7-be865755a984`|

### <a name="BKMK_adx_inviteredemption_sla_slainvokedid"></a> adx_inviteredemption_sla_slainvokedid

Many-To-One Relationship: [adx_inviteredemption adx_inviteredemption_sla_slainvokedid](adx_inviteredemption.md#BKMK_adx_inviteredemption_sla_slainvokedid)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`adx_inviteredemption_sla_slainvokedid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_portalcomment_sla_slaid"></a> adx_portalcomment_sla_slaid

Many-To-One Relationship: [adx_portalcomment adx_portalcomment_sla_slaid](adx_portalcomment.md#BKMK_adx_portalcomment_sla_slaid)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`adx_portalcomment_sla_slaid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10001<br />QueryApi: null<br />ViewId: `7f15e2bb-305a-468f-9af7-be865755a984`|

### <a name="BKMK_adx_portalcomment_sla_slainvokedid"></a> adx_portalcomment_sla_slainvokedid

Many-To-One Relationship: [adx_portalcomment adx_portalcomment_sla_slainvokedid](adx_portalcomment.md#BKMK_adx_portalcomment_sla_slainvokedid)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`adx_portalcomment_sla_slainvokedid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_chat_sla_slaid"></a> chat_sla_slaid

Many-To-One Relationship: [chat chat_sla_slaid](chat.md#BKMK_chat_sla_slaid)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`chat_sla_slaid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10001<br />QueryApi: null<br />ViewId: `7f15e2bb-305a-468f-9af7-be865755a984`|

### <a name="BKMK_chat_sla_slainvokedid"></a> chat_sla_slainvokedid

Many-To-One Relationship: [chat chat_sla_slainvokedid](chat.md#BKMK_chat_sla_slainvokedid)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`chat_sla_slainvokedid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_manualsla_account"></a> manualsla_account

Many-To-One Relationship: [account manualsla_account](account.md#BKMK_manualsla_account)

|Property|Value|
|---|---|
|ReferencingEntity|`account`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`manualsla_account`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-00aa-000010001200`|

### <a name="BKMK_manualsla_activitypointer"></a> manualsla_activitypointer

Many-To-One Relationship: [activitypointer manualsla_activitypointer](activitypointer.md#BKMK_manualsla_activitypointer)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`manualsla_activitypointer`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10001<br />QueryApi: null<br />ViewId: `7f15e2bb-305a-468f-9af7-be865755a984`|

### <a name="BKMK_manualsla_appointment"></a> manualsla_appointment

Many-To-One Relationship: [appointment manualsla_appointment](appointment.md#BKMK_manualsla_appointment)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`manualsla_appointment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `d0479533-05a4-4bd3-affc-5767379a344d`|

### <a name="BKMK_manualsla_contact"></a> manualsla_contact

Many-To-One Relationship: [contact manualsla_contact](contact.md#BKMK_manualsla_contact)

|Property|Value|
|---|---|
|ReferencingEntity|`contact`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`manualsla_contact`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-00aa-000010001210`|

### <a name="BKMK_manualsla_email"></a> manualsla_email

Many-To-One Relationship: [email manualsla_email](email.md#BKMK_manualsla_email)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`manualsla_email`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `f26e11d0-0ef8-4dff-a7e2-1f5e091fedb0`|

### <a name="BKMK_manualsla_fax"></a> manualsla_fax

Many-To-One Relationship: [fax manualsla_fax](fax.md#BKMK_manualsla_fax)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`manualsla_fax`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10001<br />QueryApi: null<br />ViewId: `cff5d26b-966b-40e4-ad06-b9c65d1b8978`|

### <a name="BKMK_manualsla_letter"></a> manualsla_letter

Many-To-One Relationship: [letter manualsla_letter](letter.md#BKMK_manualsla_letter)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`manualsla_letter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10001<br />QueryApi: null<br />ViewId: `e6be0f51-5892-4a70-86d1-4611fc5b2b5e`|

### <a name="BKMK_manualsla_phonecall"></a> manualsla_phonecall

Many-To-One Relationship: [phonecall manualsla_phonecall](phonecall.md#BKMK_manualsla_phonecall)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`manualsla_phonecall`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10001<br />QueryApi: null<br />ViewId: `04f1599c-09e1-40d5-a493-b25165f2c3c3`|

### <a name="BKMK_manualsla_socialactivity"></a> manualsla_socialactivity

Many-To-One Relationship: [socialactivity manualsla_socialactivity](socialactivity.md#BKMK_manualsla_socialactivity)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`manualsla_socialactivity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10001<br />QueryApi: null<br />ViewId: `ae2b791c-8210-49d3-ba16-3110af6864a4`|

### <a name="BKMK_manualsla_task"></a> manualsla_task

Many-To-One Relationship: [task manualsla_task](task.md#BKMK_manualsla_task)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`manualsla_task`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10001<br />QueryApi: null<br />ViewId: `bd9e5b3b-94ae-4c4a-9e79-2e7aefee4f5e`|

### <a name="BKMK_sla_account"></a> sla_account

Many-To-One Relationship: [account sla_account](account.md#BKMK_sla_account)

|Property|Value|
|---|---|
|ReferencingEntity|`account`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`sla_account`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sla_activitypointer"></a> sla_activitypointer

Many-To-One Relationship: [activitypointer sla_activitypointer](activitypointer.md#BKMK_sla_activitypointer)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`sla_activitypointer`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sla_Annotation"></a> sla_Annotation

Many-To-One Relationship: [annotation sla_Annotation](annotation.md#BKMK_sla_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`sla_Annotation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sla_appointment"></a> sla_appointment

Many-To-One Relationship: [appointment sla_appointment](appointment.md#BKMK_sla_appointment)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`sla_appointment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sla_contact"></a> sla_contact

Many-To-One Relationship: [contact sla_contact](contact.md#BKMK_sla_contact)

|Property|Value|
|---|---|
|ReferencingEntity|`contact`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`sla_contact`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sla_email"></a> sla_email

Many-To-One Relationship: [email sla_email](email.md#BKMK_sla_email)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`sla_email`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sla_fax"></a> sla_fax

Many-To-One Relationship: [fax sla_fax](fax.md#BKMK_sla_fax)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`sla_fax`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sla_letter"></a> sla_letter

Many-To-One Relationship: [letter sla_letter](letter.md#BKMK_sla_letter)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`sla_letter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sla_phonecall"></a> sla_phonecall

Many-To-One Relationship: [phonecall sla_phonecall](phonecall.md#BKMK_sla_phonecall)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`sla_phonecall`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sla_slaitem_slaId"></a> sla_slaitem_slaId

Many-To-One Relationship: [slaitem sla_slaitem_slaId](slaitem.md#BKMK_sla_slaitem_slaId)

|Property|Value|
|---|---|
|ReferencingEntity|`slaitem`|
|ReferencingAttribute|`slaid`|
|ReferencedEntityNavigationPropertyName|`sla_slaitem_slaId`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sla_socialactivity"></a> sla_socialactivity

Many-To-One Relationship: [socialactivity sla_socialactivity](socialactivity.md#BKMK_sla_socialactivity)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`sla_socialactivity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SLA_SyncErrors"></a> SLA_SyncErrors

Many-To-One Relationship: [syncerror SLA_SyncErrors](syncerror.md#BKMK_SLA_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SLA_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sla_task"></a> sla_task

Many-To-One Relationship: [task sla_task](task.md#BKMK_sla_task)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`slainvokedid`|
|ReferencedEntityNavigationPropertyName|`sla_task`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_slabase_AsyncOperations"></a> slabase_AsyncOperations

Many-To-One Relationship: [asyncoperation slabase_AsyncOperations](asyncoperation.md#BKMK_slabase_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`slabase_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_slabase_BulkDeleteFailures"></a> slabase_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure slabase_BulkDeleteFailures](bulkdeletefailure.md#BKMK_slabase_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`slabase_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_slabase_ProcessSessions"></a> slabase_ProcessSessions

Many-To-One Relationship: [processsession slabase_ProcessSessions](processsession.md#BKMK_slabase_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`slabase_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sla?displayProperty=fullName>
