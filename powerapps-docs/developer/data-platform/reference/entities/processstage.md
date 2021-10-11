---
title: "ProcessStage table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the ProcessStage table/entity."
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

# ProcessStage table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Stage associated with a process.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/processstages<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/processstages(*processstageid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/processstages(*processstageid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveActivePath|<xref href="Microsoft.Dynamics.CRM.RetrieveActivePath?text=RetrieveActivePath Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveActivePathRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/processstages<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|ProcessStages|
|DisplayCollectionName|Process Stages|
|DisplayName|Process Stage|
|EntitySetName|processstages|
|IsBPFEntity|False|
|LogicalCollectionName|processstages|
|LogicalName|processstage|
|OwnershipType|None|
|PrimaryIdAttribute|processstageid|
|PrimaryNameAttribute|stagename|
|SchemaName|ProcessStage|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Connector](#BKMK_Connector)
- [IsTrigger](#BKMK_IsTrigger)
- [OperationId](#BKMK_OperationId)
- [OperationKind](#BKMK_OperationKind)
- [OperationType](#BKMK_OperationType)
- [PrimaryEntityTypeCode](#BKMK_PrimaryEntityTypeCode)
- [ProcessId](#BKMK_ProcessId)
- [ProcessStageId](#BKMK_ProcessStageId)
- [StageCategory](#BKMK_StageCategory)
- [StageName](#BKMK_StageName)


### <a name="BKMK_Connector"></a> Connector

**Added by**: Power Automate Extensions core package Solution

|Property|Value|
|--------|-----|
|Description|The connector associated with the stage.|
|DisplayName|Connector|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|connector|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsTrigger"></a> IsTrigger

**Added by**: Power Automate Extensions core package Solution

|Property|Value|
|--------|-----|
|Description|Whether the stage is a trigger|
|DisplayName|Is Trigger|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|istrigger|
|RequiredLevel|None|
|Type|Boolean|

#### IsTrigger Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_OperationId"></a> OperationId

**Added by**: Power Automate Extensions core package Solution

|Property|Value|
|--------|-----|
|Description|The operation id of the stage|
|DisplayName|Operation Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|operationid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OperationKind"></a> OperationKind

**Added by**: Power Automate Extensions core package Solution

|Property|Value|
|--------|-----|
|Description|The operation kind|
|DisplayName|Operation Kind|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|operationkind|
|RequiredLevel|None|
|Type|Picklist|

#### OperationKind Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|473330000|Http||
|473330001|PowerApp||
|473330002|PowerAppV2||
|473330003|Button||
|473330004|ApiConnection||
|473330005|Alert||
|473330006|EventGrid||
|473330007|CurrentTime||
|473330008|ConvertTimeZone||
|473330009|GetFutureTime||
|473330010|GetPastTime||
|473330011|AddToTime||
|473330012|SubtractFromTime||
|473330013|AzureMonitorAlert||
|473330014|SecurityCenterAlert||
|473330015|JsonToJson||
|473330016|JsonToText||
|473330017|XmlToJson||
|473330018|XmlToText||
|473330019|Geofence||
|473330020|ODataOpenApiConnection||
|473330021|IndexOf||
|473330022|Substring||
|473330023|VirtualAgent||
|473330024|FormatNumber||



### <a name="BKMK_OperationType"></a> OperationType

**Added by**: Power Automate Extensions core package Solution

|Property|Value|
|--------|-----|
|Description|The type of the operation|
|DisplayName|Operation Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|operationtype|
|RequiredLevel|None|
|Type|Picklist|

#### OperationType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|473330000|Http||
|473330001|ApiApp||
|473330002|Recurrence||
|473330003|Workflow||
|473330004|Flow||
|473330005|Wait||
|473330006|ApiConnection||
|473330007|OpenApiConnection||
|473330008|Manual||
|473330009|ApiConnectionWebhook||
|473330010|OpenApiConnectionWebhook||
|473330011|Response||
|473330012|HttpWebhook||
|473330013|Compose||
|473330014|Query||
|473330015|Function||
|473330016|ApiManagement||
|473330017|XmlValidation||
|473330018|FlatFileEncoding||
|473330019|Scope||
|473330020|Request||
|473330021|If||
|473330022|Foreach||
|473330023|Until||
|473330024|Xslt||
|473330025|FlatFileDecoding||
|473330026|Terminate||
|473330027|IntegrationAccountArtifactLookup||
|473330028|Switch||
|473330029|ParseJson||
|473330030|Table||
|473330031|Join||
|473330032|Select||
|473330033|InitializeVariable||
|473330034|IncrementVariable||
|473330035|DecrementVariable||
|473330036|SetVariable||
|473330037|AppendToArrayVariable||
|473330038|AppendToStringVariable||
|473330039|Batch||
|473330040|SendToBatch||
|473330041|SlidingWindow||
|473330042|Expression||
|473330043|Liquid||
|473330044|JavascriptCode||
|473330045|As2Decode||
|473330046|As2Encode||
|473330047|RosettaNetEncode||
|473330048|RosettaNetDecode||
|473330049|RosettaNetWaitForResponse||
|473330050|ApiConnectionNotification||
|473330051|Changeset||
|473330052|SwiftEncode||



### <a name="BKMK_PrimaryEntityTypeCode"></a> PrimaryEntityTypeCode

|Property|Value|
|--------|-----|
|Description|Primary entity associated with the stage.|
|DisplayName|Primary Entity|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|primaryentitytypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the process.|
|DisplayName|Process|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|processid|
|RequiredLevel|SystemRequired|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_ProcessStageId"></a> ProcessStageId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the process stage record.|
|DisplayName|Process Stage|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|processstageid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_StageCategory"></a> StageCategory

|Property|Value|
|--------|-----|
|Description|Select the category of the sales process.|
|DisplayName|Stage Category|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|stagecategory|
|RequiredLevel|None|
|Type|Picklist|

#### StageCategory Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Qualify||
|1|Develop||
|2|Propose||
|3|Close||
|4|Identify||
|5|Research||
|6|Resolve||
|7|Approval||



### <a name="BKMK_StageName"></a> StageName

|Property|Value|
|--------|-----|
|Description|Type a name for the process stage.|
|DisplayName|Process Stage Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|stagename|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ClientData](#BKMK_ClientData)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [ProcessIdName](#BKMK_ProcessIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ClientData"></a> ClientData

|Property|Value|
|--------|-----|
|Description|Step metadata for process stage|
|DisplayName|Client Data|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|clientdata|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.|
|DisplayName|Owner|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|ApplicationRequired|
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
|Description|Select the business unit that owns the record.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ProcessIdName"></a> ProcessIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the process stage.|
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

- [processstage_knowledgearticle](#BKMK_processstage_knowledgearticle)
- [processstage_contact](#BKMK_processstage_contact)
- [processstage_teams](#BKMK_processstage_teams)
- [ProcessStage_SyncErrors](#BKMK_ProcessStage_SyncErrors)
- [processstage_recurringappointmentmasters](#BKMK_processstage_recurringappointmentmasters)
- [processstage_letters](#BKMK_processstage_letters)
- [processstage_faxes](#BKMK_processstage_faxes)
- [processstage_tasks](#BKMK_processstage_tasks)
- [processstage_account](#BKMK_processstage_account)
- [lk_translationprocess_activestageid](#BKMK_lk_translationprocess_activestageid)
- [processstage_systemusers](#BKMK_processstage_systemusers)
- [lk_newprocess_activestageid](#BKMK_lk_newprocess_activestageid)
- [processstage_emails](#BKMK_processstage_emails)
- [processstage_appointments](#BKMK_processstage_appointments)
- [processstage_phonecalls](#BKMK_processstage_phonecalls)
- [lk_expiredprocess_activestageid](#BKMK_lk_expiredprocess_activestageid)
- [processstage_processstageparameter](#BKMK_processstage_processstageparameter)


### <a name="BKMK_processstage_knowledgearticle"></a> processstage_knowledgearticle

Same as knowledgearticle table [processstage_knowledgearticle](knowledgearticle.md#BKMK_processstage_knowledgearticle) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_knowledgearticle|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processstage_contact"></a> processstage_contact

Same as contact table [processstage_contact](contact.md#BKMK_processstage_contact) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_contact|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processstage_teams"></a> processstage_teams

Same as team table [processstage_teams](team.md#BKMK_processstage_teams) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|team|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_teams|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_ProcessStage_SyncErrors"></a> ProcessStage_SyncErrors

Same as syncerror table [ProcessStage_SyncErrors](syncerror.md#BKMK_ProcessStage_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|ProcessStage_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_processstage_recurringappointmentmasters"></a> processstage_recurringappointmentmasters

Same as recurringappointmentmaster table [processstage_recurringappointmentmasters](recurringappointmentmaster.md#BKMK_processstage_recurringappointmentmasters) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_recurringappointmentmasters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processstage_letters"></a> processstage_letters

Same as letter table [processstage_letters](letter.md#BKMK_processstage_letters) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_letters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processstage_faxes"></a> processstage_faxes

Same as fax table [processstage_faxes](fax.md#BKMK_processstage_faxes) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_faxes|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processstage_tasks"></a> processstage_tasks

Same as task table [processstage_tasks](task.md#BKMK_processstage_tasks) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_tasks|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processstage_account"></a> processstage_account

Same as account table [processstage_account](account.md#BKMK_processstage_account) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_account|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_translationprocess_activestageid"></a> lk_translationprocess_activestageid

Same as translationprocess table [lk_translationprocess_activestageid](translationprocess.md#BKMK_lk_translationprocess_activestageid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|translationprocess|
|ReferencingAttribute|activestageid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|processstage_translationprocess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processstage_systemusers"></a> processstage_systemusers

Same as systemuser table [processstage_systemusers](systemuser.md#BKMK_processstage_systemusers) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_systemusers|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_newprocess_activestageid"></a> lk_newprocess_activestageid

Same as newprocess table [lk_newprocess_activestageid](newprocess.md#BKMK_lk_newprocess_activestageid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|newprocess|
|ReferencingAttribute|activestageid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|processstage_newprocess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processstage_emails"></a> processstage_emails

Same as email table [processstage_emails](email.md#BKMK_processstage_emails) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_emails|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processstage_appointments"></a> processstage_appointments

Same as appointment table [processstage_appointments](appointment.md#BKMK_processstage_appointments) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_appointments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processstage_phonecalls"></a> processstage_phonecalls

Same as phonecall table [processstage_phonecalls](phonecall.md#BKMK_processstage_phonecalls) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|stageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_phonecalls|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_expiredprocess_activestageid"></a> lk_expiredprocess_activestageid

Same as expiredprocess table [lk_expiredprocess_activestageid](expiredprocess.md#BKMK_lk_expiredprocess_activestageid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|expiredprocess|
|ReferencingAttribute|activestageid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|processstage_expiredprocess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processstage_processstageparameter"></a> processstage_processstageparameter

**Added by**: Power Automate Extensions core package Solution

Same as processstageparameter table [processstage_processstageparameter](processstageparameter.md#BKMK_processstage_processstageparameter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processstageparameter|
|ReferencingAttribute|processstageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processstage_processstageparameter|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.


### <a name="BKMK_process_processstage"></a> process_processstage

See workflow Table [process_processstage](workflow.md#BKMK_process_processstage) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.processstage?text=processstage EntityType" />