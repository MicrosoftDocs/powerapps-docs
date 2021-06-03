---
title: "SLA table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SLA table/entity."
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

# SLA table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Contains information about the tracked service-level KPIs for cases that belong to different customers.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/slas(*slaid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/slas<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/slas(*slaid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/slas(*slaid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/slas<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/slas(*slaid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/slas(*slaid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SLAs|
|DisplayCollectionName|SLAs|
|DisplayName|SLA|
|EntitySetName|slas|
|IsBPFEntity|False|
|LogicalCollectionName|slas|
|LogicalName|sla|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|slaid|
|PrimaryNameAttribute|name|
|SchemaName|SLA|

<a name="writable-attributes"></a>

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
- [WorkflowIdName](#BKMK_WorkflowIdName)


### <a name="BKMK_AllowPauseResume"></a> AllowPauseResume

|Property|Value|
|--------|-----|
|Description|Select whether this SLA will allow pausing and resuming during the time calculation.|
|DisplayName|Allow Pause and Resume|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|allowpauseresume|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### AllowPauseResume Choices/Options

|Value|Label|
|-----|-----|
|1|Allow|
|0|Do Not Allow|

**DefaultValue**: False



### <a name="BKMK_ApplicableFrom"></a> ApplicableFrom

|Property|Value|
|--------|-----|
|Description|Select the field that specifies the date and time from which the SLA items will be calculated for the case record. For example, if you select the Case Created On field, SLA calculation will begin from the time the case is created. |
|DisplayName|Applicable From|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|applicablefrom|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ApplicableFromPickList"></a> ApplicableFromPickList

|Property|Value|
|--------|-----|
|Description|Select the field that specifies the date and time from which the SLA items will be calculated. For example, if you select the Case Created On field, SLA calculation will begin from the time the case is created.|
|DisplayName|Applicable From|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|applicablefrompicklist|
|RequiredLevel|None|
|Type|Picklist|

#### ApplicableFromPickList Choices/Options

|Value|Label|
|-----|-----|
|1|No|
|2|Yes|



### <a name="BKMK_BusinessHoursId"></a> BusinessHoursId

|Property|Value|
|--------|-----|
|Description|Choose the business hours for calculating SLA item timelines.|
|DisplayName|Business Hours|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|businesshoursid|
|RequiredLevel|None|
|Targets|calendar|
|Type|Lookup|


### <a name="BKMK_ChangedAttributeList"></a> ChangedAttributeList

|Property|Value|
|--------|-----|
|Description|Type additional information to describe the SLA|
|DisplayName|ChangedAttributeList|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|changedattributelist|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Type additional information to describe the SLA|
|DisplayName|Description|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|--------|-----|
|Description|Tells whether this SLA is the default one.|
|DisplayName|Is Default|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isdefault|
|RequiredLevel|None|
|Type|Boolean|

#### IsDefault Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Type a descriptive name of the service level agreement (SLA).|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Enter the user or team who owns the SLA. This field is updated every time the item is assigned to a different user.|
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


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
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
|Description|Unique identifier for the team that owns the record.|
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
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_PrimaryEntityOTC"></a> PrimaryEntityOTC

|Property|Value|
|--------|-----|
|Description|Shows the primary entity that the SLA has been created for.|
|DisplayName|Primary Entity|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|primaryentityotc|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the SLA.|
|DisplayName|SLA|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|slaid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SLAType"></a> SLAType

|Property|Value|
|--------|-----|
|Description|Select the type of service level agreement (SLA).|
|DisplayName|SLA Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|slatype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### SLAType Choices/Options

|Value|Label|
|-----|-----|
|0|Standard|
|1|Enhanced|



### <a name="BKMK_slaversion"></a> slaversion

**Added by**: Service Level Agreement (SLA) Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Record version|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|slaversion|
|RequiredLevel|None|
|Type|Picklist|

#### slaversion Choices/Options

|Value|Label|
|-----|-----|
|100000000|Version WC|
|100000001|Version UC|



### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows whether the Service Level Agreement (SLA) is active or inactive.|
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
|0|Draft|1|Draft|
|1|Active|2|Active|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Select the status of the service level agreement (SLA).|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Draft|0|
|2|Active|1|



### <a name="BKMK_WorkflowId"></a> WorkflowId

|Property|Value|
|--------|-----|
|Description|Workflow associated with the SLA.|
|DisplayName|Workflow ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|workflowid|
|RequiredLevel|None|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_WorkflowIdName"></a> WorkflowIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|workflowidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [BusinessHoursIdName](#BKMK_BusinessHoursIdName)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [SLAIdUnique](#BKMK_SLAIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_BusinessHoursIdName"></a> BusinessHoursIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businesshoursidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ComponentState"></a> ComponentState

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

|Value|Label|
|-----|-----|
|0|Published|
|1|Unpublished|
|2|Deleted|
|3|Deleted Unpublished|



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

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
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record on behalf of another user.|
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
|Description|Exchange rate between the currency associated with the SLA record and the base currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.0000000001|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|
|-----|-----|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

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
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record on behalf of another user.|
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


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Choose the entity type that the SLA is defined.|
|DisplayName|Object Type Code|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|objecttypecode|
|RequiredLevel|None|
|Type|Picklist|

#### ObjectTypeCode Choices/Options

|Value|Label|
|-----|-----|
|1|Account|
|2|Contact|
|5|Note|
|6|Business Unit Map|
|7|Owner|
|8|User|
|9|Team|
|10|Business Unit|
|14|System User Principal|
|29|Subscription|
|30|Filter Template|
|31|Privilege Object Type Code|
|33|Subscription Synchronization Information|
|35|Tracking information for deleted entities|
|36|Client update|
|37|Subscription Manually Tracked Object|
|42|SystemUser BusinessUnit Entity Map|
|44|Field Sharing|
|45|Subscription Statistic Offline|
|46|Subscription Statistic Outlook|
|47|Subscription Sync Entry Offline|
|48|Subscription Sync Entry Outlook|
|50|Position|
|51|System User Manager Map|
|52|User Search Facet|
|54|Global Search Configuration|
|55|FileAttachment|
|60|SystemUserAuthorizationChangeTracker|
|78|Virtual Entity Data Provider|
|85|Virtual Entity Data Source|
|92|Team template|
|99|Social Profile|
|101|Service Plan|
|126|Indexed Article|
|127|Article|
|129|Subject|
|132|Announcement|
|135|Activity Party|
|150|User Settings|
|300|Canvas App|
|301|Callback Registration|
|372|Connector|
|380|Environment Variable Definition|
|381|Environment Variable Value|
|400|AI Template|
|401|AI Model|
|402|AI Configuration|
|418|Dataflow|
|430|Entity Analytics Config|
|431|Image Attribute Configuration|
|432|Entity Image Configuration|
|950|New Process|
|951|Translation Process|
|955|Expired Process|
|1001|Attachment|
|1002|Attachment|
|1003|Internal Address|
|1007|Image Descriptor|
|1016|Article Template|
|1019|Organization|
|1021|Organization UI|
|1023|Privilege|
|1030|System Form|
|1031|User Dashboard|
|1036|Security Role|
|1037|Role Template|
|1039|View|
|1043|String Map|
|1071|Address|
|1072|Subscription Clients|
|1075|Status Map|
|1082|Article Comment|
|1086|User Fiscal Calendar|
|1094|Authorization Server|
|1095|Partner Application|
|1111|System Chart|
|1112|User Chart|
|1113|Ribbon Tab To Command Mapping|
|1115|Ribbon Context Group|
|1116|Ribbon Command|
|1117|Ribbon Rule|
|1120|Application Ribbons|
|1130|Ribbon Difference|
|1140|Replication Backlog|
|1189|Document Suggestions|
|1190|SuggestionCardTemplate|
|1200|Field Security Profile|
|1201|Field Permission|
|1203|Team Profiles|
|1234|Channel Property Group|
|1236|Channel Property|
|1300|SocialInsightsConfiguration|
|1309|Saved Organization Insights Configuration|
|1400|Sync Attribute Mapping Profile|
|1401|Sync Attribute Mapping|
|1403|Team Sync-Attribute Mapping Profiles|
|1404|Principal Sync Attribute Map|
|2000|Annual Fiscal Calendar|
|2001|Semiannual Fiscal Calendar|
|2002|Quarterly Fiscal Calendar|
|2003|Monthly Fiscal Calendar|
|2004|Fixed Monthly Fiscal Calendar|
|2010|Email Template|
|2012|Unresolved Address|
|2013|Territory|
|2015|Theme|
|2016|User Mapping|
|2020|Queue|
|2023|QueueItemCount|
|2024|QueueMemberCount|
|2027|License|
|2029|Queue Item|
|2500|User Entity UI Settings|
|2501|User Entity Instance Data|
|3000|Integration Status|
|3005|Channel Access Profile|
|3008|External Party|
|3231|Connection Role|
|3233|Connection Role Object Type Code|
|3234|Connection|
|4003|Calendar|
|4004|Calendar Rule|
|4011|Inter Process Lock|
|4023|Email Hash|
|4101|Display String Map|
|4102|Display String|
|4110|Notification|
|4120|Exchange Sync Id Mapping|
|4200|Activity|
|4201|Appointment|
|4202|Email|
|4204|Fax|
|4207|Letter|
|4210|Phone Call|
|4212|Task|
|4216|Social Activity|
|4220|UntrackedEmail|
|4230|Saved View|
|4231|Metadata Difference|
|4232|Business Data Localized Label|
|4250|Recurrence Rule|
|4251|Recurring Appointment|
|4299|Email Search|
|4410|Data Import|
|4411|Data Map|
|4412|Import Source File|
|4413|Import Data|
|4414|Duplicate Detection Rule|
|4415|Duplicate Record|
|4416|Duplicate Rule Condition|
|4417|Column Mapping|
|4418|List Value Mapping|
|4419|Lookup Mapping|
|4420|Owner Mapping|
|4423|Import Log|
|4424|Bulk Delete Operation|
|4425|Bulk Delete Failure|
|4426|Transformation Mapping|
|4427|Transformation Parameter Mapping|
|4428|Import Entity Mapping|
|4450|Data Performance Dashboard|
|4490|Office Document|
|4500|Relationship Role|
|4501|Relationship Role Map|
|4502|Customer Relationship|
|4567|Auditing|
|4579|Ribbon Client Metadata.|
|4600|Entity Map|
|4601|Attribute Map|
|4602|Plug-in Type|
|4603|Plug-in Type Statistic|
|4605|Plug-in Assembly|
|4606|Sdk Message|
|4607|Sdk Message Filter|
|4608|Sdk Message Processing Step|
|4609|Sdk Message Request|
|4610|Sdk Message Response|
|4611|Sdk Message Response Field|
|4613|Sdk Message Pair|
|4614|Sdk Message Request Field|
|4615|Sdk Message Processing Step Image|
|4616|Sdk Message Processing Step Secure Configuration|
|4618|Service Endpoint|
|4619|Plug-in Trace Log|
|4700|System Job|
|4702|Workflow Wait Subscription|
|4703|Process|
|4704|Process Dependency|
|4705|ISV Config|
|4706|Process Log|
|4707|Application File|
|4708|Organization Statistic|
|4709|Site Map|
|4710|Process Session|
|4711|Expander Event|
|4712|Process Trigger|
|4720|Flow Session|
|4724|Process Stage|
|4725|Business Process Flow Instance|
|4800|Web Wizard|
|4802|Wizard Page|
|4803|Web Wizard Access Privilege|
|4810|Time Zone Definition|
|4811|Time Zone Rule|
|4812|Time Zone Localized Name|
|7000|System Application Metadata|
|7001|User Application Metadata|
|7100|Solution|
|7101|Publisher|
|7102|Publisher Address|
|7103|Solution Component|
|7104|Solution Component Definition|
|7105|Dependency|
|7106|Dependency Node|
|7107|Invalid Dependency|
|7108|Dependency Feature|
|7200|RuntimeDependency|
|8000|Post|
|8001|Post Role|
|8002|Post Regarding|
|8003|Follow|
|8005|Comment|
|8006|Like|
|8040|ACIViewMapper|
|8050|Trace|
|8051|Trace Association|
|8052|Trace Regarding|
|8181|Routing Rule Set|
|8199|Rule Item|
|8700|AppModule Metadata|
|8701|AppModule Metadata Dependency|
|8702|AppModule Metadata Async Operation|
|8840|Hierarchy Rule|
|9006|Model-driven App|
|9007|App Module Component|
|9009|App Module Roles|
|9011|App Config Master|
|9012|App Configuration|
|9013|App Configuration Instance|
|9100|Report|
|9101|Report Related Entity|
|9102|Report Related Category|
|9103|Report Visibility|
|9104|Report Link|
|9105|Currency|
|9106|Mail Merge Template|
|9107|Import Job|
|9201|LocalConfigStore|
|9300|Record Creation and Update Rule|
|9301|Record Creation and Update Rule Item|
|9333|Web Resource|
|9400|Channel Access Profile Rule|
|9401|Channel Access Profile Rule Item|
|9502|SharePoint Site|
|9507|Sharepoint Document|
|9508|Document Location|
|9509|SharePoint Data|
|9510|Rollup Properties|
|9511|Rollup Job|
|9600|Goal|
|9602|Rollup Query|
|9603|Goal Metric|
|9604|Rollup Field|
|9605|Email Server Profile|
|9606|Mailbox|
|9607|Mailbox Statistics|
|9608|Mailbox Auto Tracking Folder|
|9609|Mailbox Tracking Category|
|9650|Process Configuration|
|9690|Organization Insights Notification|
|9699|Organization Insights Metric|
|9750|SLA|
|9751|SLA Item|
|9752|SLA KPI Instance|
|9753|Custom Control|
|9754|Custom Control Resource|
|9755|Custom Control Default Config|
|9800|Entity|
|9808|Attribute|
|9809|OptionSet|
|9810|Entity Key|
|9811|Entity Relationship|
|9812|Managed Property|
|9813|Relationship Entity|
|9814|Relationship Attribute|
|9866|Mobile Offline Profile|
|9867|Mobile Offline Profile Item|
|9868|Mobile Offline Profile Item Association|
|9869|Sync Error|
|9870|Offline Command Definition|
|9875|Language Provisioning State|
|9880|Ribbon Metadata To Process|
|9890|SolutionHistoryData|
|9900|Navigation Setting|
|9910|MultiEntitySearch|
|9912|Multi Select Option Value|
|9919|Hierarchy Security Configuration|
|9930|Knowledge Base Record|
|9932|Time Stamp Date Mapping|
|9936|Azure Service Connection|
|9940|Document Template|
|9941|Personal Document Template|
|9945|Text Analytics Entity Mapping|
|9947|Knowledge Search Model|
|9949|Advanced Similarity Rule|
|9950|Office Graph Document|
|9951|Similarity Rule|
|9953|Knowledge Article|
|9955|Knowledge Article Views|
|9957|Language|
|9958|Feedback|
|9959|Category|
|9960|Knowledge Article Category|
|9961|DelveActionHub|
|9962|Action Card|
|9968|ActionCardUserState|
|9973|Action Card User Settings|
|9983|Action Card Type|
|9986|Interaction for Email|
|9987|External Party Item|
|9996|HolidayWrapper|
|9997|Email Signature|
|10000|Solution Component Attribute Configuration|
|10001|Solution Component Configuration|
|10002|Solution Component Relationship Configuration|
|10003|Solution History|
|10004|Solution History Data Source|
|10005|Component Layer|
|10006|Component Layer Data Source|
|10007|Package|
|10009|StageSolutionUpload|
|10010|ExportSolutionUpload|
|10011|Solution Component Summary|
|10012|Solution Component Data Source|
|10013|ProvisionLanguageForUser|
|10014|Data Lake Folder|
|10015|Data Lake Folder Permission|
|10016|Data Lake Workspace|
|10017|Data Lake Workspace Permission|
|10018|CascadeGrantRevokeAccessRecordsTracker|
|10019|CascadeGrantRevokeAccessVersionTracker|
|10021|ApplicationUser|
|10024|Model-Driven App Element|
|10025|Model-Driven App Component Node's Edge|
|10026|Model-Driven App Component Node|
|10027|Model-Driven App Setting|
|10028|Model-Driven App User Setting|
|10029|Organization Setting|
|10030|Setting Definition|
|10031|CanvasApp Extended Metadata|
|10032|OData v4 Data Source|
|10033|Flow Machine|
|10034|Flow Machine Group|
|10035|ProcessStageParameter|
|10036|Workflow Binary|
|10037|Connection Reference|
|10038|Help Page|
|10039|BotContent|
|10040|ConversationTranscript|
|10041|Chatbot|
|10042|Chatbot subcomponent|
|10048|PDF Setting|
|10049|Activity File Attachment|
|10050|Service Configuration|
|10051|SLA KPI|
|10052|Knowledge Federated Article|
|10053|Knowledge FederatedArticle Incident|
|10054|Search provider|
|10055|Knowledge Article Image|
|10056|Knowledge Interaction Insight|
|10057|Knowledge Search Insight|
|10058|Knowledge article language setting|
|10059|Knowledge personalization|
|10060|Knowledge Article Template|
|10061|Knowledge search personal filter config|
|10062|Knowledge search filter|
|10063|KeyVaultReference|
|10064|ManagedIdentity|
|10065|Catalog|
|10066|Catalog Assignment|
|10067|Internal Catalog Assignment|
|10068|Custom API|
|10069|Custom API Request Parameter|
|10070|Custom API Response Property|
|10071|TeamMobileOfflineProfileMembership|
|10072|UserMobileOfflineProfileMembership|
|10073|OrganizationDataSyncSubscription|
|10074|OrganizationDataSyncSubscriptionEntity|
|10075|Notification|
|10076|Rich Text Attachment|
|10077|NonRelational Data Source|
|10078|Search Telemetry|
|10079|AI Builder Dataset|
|10080|AI Builder Dataset File|
|10081|AI Builder Dataset Record|
|10082|AI Builder Datasets Container|
|10083|AI Builder File|
|10084|AI Builder File Attached Data|
|10085|AI Form Processing Document|
|10086|AI Object Detection Image|
|10087|AI Object Detection Label|
|10088|AI Object Detection Bounding Box|
|10089|AI Object Detection Image Mapping|
|10091|PM Inferred Task|
|10092|PM Recording|
|10093|Analysis Component|
|10094|Analysis Job|
|10095|Analysis Result|
|10096|Analysis Result Detail|
|10097|Solution Health Rule|
|10098|Solution Health Rule Argument|
|10099|Solution Health Rule Set|
|90001|RevokeInheritedAccessRecordsTracker|



### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


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


### <a name="BKMK_SLAIdUnique"></a> SLAIdUnique

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Unique Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|slaidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SolutionId"></a> SolutionId

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

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the currency associated with the SLA record.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


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
|Description|Version number of the SLA.|
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

- [sla_socialactivity](#BKMK_sla_socialactivity)
- [manualsla_contact](#BKMK_manualsla_contact)
- [slabase_BulkDeleteFailures](#BKMK_slabase_BulkDeleteFailures)
- [manualsla_fax](#BKMK_manualsla_fax)
- [manualsla_activitypointer](#BKMK_manualsla_activitypointer)
- [slabase_AsyncOperations](#BKMK_slabase_AsyncOperations)
- [sla_Annotation](#BKMK_sla_Annotation)
- [sla_task](#BKMK_sla_task)
- [sla_activitypointer](#BKMK_sla_activitypointer)
- [manualsla_task](#BKMK_manualsla_task)
- [manualsla_account](#BKMK_manualsla_account)
- [sla_letter](#BKMK_sla_letter)
- [manualsla_phonecall](#BKMK_manualsla_phonecall)
- [sla_email](#BKMK_sla_email)
- [sla_appointment](#BKMK_sla_appointment)
- [sla_slaitem_slaId](#BKMK_sla_slaitem_slaId)
- [sla_account](#BKMK_sla_account)
- [SLA_SyncErrors](#BKMK_SLA_SyncErrors)
- [manualsla_letter](#BKMK_manualsla_letter)
- [manualsla_appointment](#BKMK_manualsla_appointment)
- [manualsla_socialactivity](#BKMK_manualsla_socialactivity)
- [sla_fax](#BKMK_sla_fax)
- [sla_contact](#BKMK_sla_contact)
- [slabase_ProcessSessions](#BKMK_slabase_ProcessSessions)
- [sla_phonecall](#BKMK_sla_phonecall)
- [manualsla_email](#BKMK_manualsla_email)


### <a name="BKMK_sla_socialactivity"></a> sla_socialactivity

Same as socialactivity table [sla_socialactivity](socialactivity.md#BKMK_sla_socialactivity) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|slainvokedid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_socialactivity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_manualsla_contact"></a> manualsla_contact

Same as contact table [manualsla_contact](contact.md#BKMK_manualsla_contact) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|slaid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|manualsla_contact|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_slabase_BulkDeleteFailures"></a> slabase_BulkDeleteFailures

Same as bulkdeletefailure table [slabase_BulkDeleteFailures](bulkdeletefailure.md#BKMK_slabase_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|slabase_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_manualsla_fax"></a> manualsla_fax

Same as fax table [manualsla_fax](fax.md#BKMK_manualsla_fax) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|slaid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|manualsla_fax|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10001|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_manualsla_activitypointer"></a> manualsla_activitypointer

Same as activitypointer table [manualsla_activitypointer](activitypointer.md#BKMK_manualsla_activitypointer) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|slaid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|manualsla_activitypointer|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10001|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_slabase_AsyncOperations"></a> slabase_AsyncOperations

Same as asyncoperation table [slabase_AsyncOperations](asyncoperation.md#BKMK_slabase_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|slabase_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_sla_Annotation"></a> sla_Annotation

Same as annotation table [sla_Annotation](annotation.md#BKMK_sla_Annotation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_Annotation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_sla_task"></a> sla_task

Same as task table [sla_task](task.md#BKMK_sla_task) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|slainvokedid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_task|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_sla_activitypointer"></a> sla_activitypointer

Same as activitypointer table [sla_activitypointer](activitypointer.md#BKMK_sla_activitypointer) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|slainvokedid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_activitypointer|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_manualsla_task"></a> manualsla_task

Same as task table [manualsla_task](task.md#BKMK_manualsla_task) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|slaid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|manualsla_task|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10001|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_manualsla_account"></a> manualsla_account

Same as account table [manualsla_account](account.md#BKMK_manualsla_account) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|slaid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|manualsla_account|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_sla_letter"></a> sla_letter

Same as letter table [sla_letter](letter.md#BKMK_sla_letter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|slainvokedid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_letter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_manualsla_phonecall"></a> manualsla_phonecall

Same as phonecall table [manualsla_phonecall](phonecall.md#BKMK_manualsla_phonecall) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|slaid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|manualsla_phonecall|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10001|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_sla_email"></a> sla_email

Same as email table [sla_email](email.md#BKMK_sla_email) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|slainvokedid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_email|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_sla_appointment"></a> sla_appointment

Same as appointment table [sla_appointment](appointment.md#BKMK_sla_appointment) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|slainvokedid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_appointment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_sla_slaitem_slaId"></a> sla_slaitem_slaId

Same as slaitem table [sla_slaitem_slaId](slaitem.md#BKMK_sla_slaitem_slaId) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slaitem|
|ReferencingAttribute|slaid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_slaitem_slaId|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_sla_account"></a> sla_account

Same as account table [sla_account](account.md#BKMK_sla_account) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|slainvokedid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_account|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SLA_SyncErrors"></a> SLA_SyncErrors

Same as syncerror table [SLA_SyncErrors](syncerror.md#BKMK_SLA_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|SLA_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_manualsla_letter"></a> manualsla_letter

Same as letter table [manualsla_letter](letter.md#BKMK_manualsla_letter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|slaid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|manualsla_letter|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10001|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_manualsla_appointment"></a> manualsla_appointment

Same as appointment table [manualsla_appointment](appointment.md#BKMK_manualsla_appointment) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|slaid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|manualsla_appointment|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_manualsla_socialactivity"></a> manualsla_socialactivity

Same as socialactivity table [manualsla_socialactivity](socialactivity.md#BKMK_manualsla_socialactivity) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|slaid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|manualsla_socialactivity|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10001|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_sla_fax"></a> sla_fax

Same as fax table [sla_fax](fax.md#BKMK_sla_fax) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|slainvokedid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_fax|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_sla_contact"></a> sla_contact

Same as contact table [sla_contact](contact.md#BKMK_sla_contact) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|slainvokedid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_contact|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_slabase_ProcessSessions"></a> slabase_ProcessSessions

Same as processsession table [slabase_ProcessSessions](processsession.md#BKMK_slabase_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|slabase_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_sla_phonecall"></a> sla_phonecall

Same as phonecall table [sla_phonecall](phonecall.md#BKMK_sla_phonecall) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|slainvokedid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sla_phonecall|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_manualsla_email"></a> manualsla_email

Same as email table [manualsla_email](email.md#BKMK_manualsla_email) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|slaid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|manualsla_email|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [slabase_workflowid](#BKMK_slabase_workflowid)
- [lk_slabase_modifiedonbehalfby](#BKMK_lk_slabase_modifiedonbehalfby)
- [lk_slabase_createdonbehalfby](#BKMK_lk_slabase_createdonbehalfby)
- [lk_slabase_createdby](#BKMK_lk_slabase_createdby)
- [team_slaBase](#BKMK_team_slaBase)
- [TransactionCurrency_SLA](#BKMK_TransactionCurrency_SLA)
- [lk_slabase_modifiedby](#BKMK_lk_slabase_modifiedby)
- [user_slabase](#BKMK_user_slabase)
- [business_unit_slabase](#BKMK_business_unit_slabase)
- [slabase_businesshoursid](#BKMK_slabase_businesshoursid)


### <a name="BKMK_slabase_workflowid"></a> slabase_workflowid

See workflow Table [slabase_workflowid](workflow.md#BKMK_slabase_workflowid) One-To-Many relationship.

### <a name="BKMK_lk_slabase_modifiedonbehalfby"></a> lk_slabase_modifiedonbehalfby

See systemuser Table [lk_slabase_modifiedonbehalfby](systemuser.md#BKMK_lk_slabase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_slabase_createdonbehalfby"></a> lk_slabase_createdonbehalfby

See systemuser Table [lk_slabase_createdonbehalfby](systemuser.md#BKMK_lk_slabase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_slabase_createdby"></a> lk_slabase_createdby

See systemuser Table [lk_slabase_createdby](systemuser.md#BKMK_lk_slabase_createdby) One-To-Many relationship.

### <a name="BKMK_team_slaBase"></a> team_slaBase

See team Table [team_slaBase](team.md#BKMK_team_slaBase) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_SLA"></a> TransactionCurrency_SLA

See transactioncurrency Table [TransactionCurrency_SLA](transactioncurrency.md#BKMK_TransactionCurrency_SLA) One-To-Many relationship.

### <a name="BKMK_lk_slabase_modifiedby"></a> lk_slabase_modifiedby

See systemuser Table [lk_slabase_modifiedby](systemuser.md#BKMK_lk_slabase_modifiedby) One-To-Many relationship.

### <a name="BKMK_user_slabase"></a> user_slabase

See systemuser Table [user_slabase](systemuser.md#BKMK_user_slabase) One-To-Many relationship.

### <a name="BKMK_business_unit_slabase"></a> business_unit_slabase

See businessunit Table [business_unit_slabase](businessunit.md#BKMK_business_unit_slabase) One-To-Many relationship.

### <a name="BKMK_slabase_businesshoursid"></a> slabase_businesshoursid

See calendar Table [slabase_businesshoursid](calendar.md#BKMK_slabase_businesshoursid) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.sla?text=sla EntityType" />