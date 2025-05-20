---
title: "System Job (AsyncOperation) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the System Job (AsyncOperation) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# System Job (AsyncOperation) table/entity reference (Microsoft Dataverse)

Process whose execution can proceed independently or in the background.

## Messages

The following table lists the messages for the System Job (AsyncOperation) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /asyncoperations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /asyncoperations(*asyncoperationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /asyncoperations(*asyncoperationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /asyncoperations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `Update`<br />Event: False |`PATCH` /asyncoperations(*asyncoperationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /asyncoperations(*asyncoperationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the System Job (AsyncOperation) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **System Job** |
| **DisplayCollectionName** | **System Jobs** |
| **SchemaName** | `AsyncOperation` |
| **CollectionSchemaName** | `AsyncOperations` |
| **EntitySetName** | `asyncoperations`|
| **LogicalName** | `asyncoperation` |
| **LogicalCollectionName** | `asyncoperations` |
| **PrimaryIdAttribute** | `asyncoperationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncOperationId](#BKMK_AsyncOperationId)
- [BreadcrumbId](#BKMK_BreadcrumbId)
- [CallerOrigin](#BKMK_CallerOrigin)
- [CorrelationId](#BKMK_CorrelationId)
- [CorrelationUpdatedTime](#BKMK_CorrelationUpdatedTime)
- [Data](#BKMK_Data)
- [DependencyToken](#BKMK_DependencyToken)
- [Depth](#BKMK_Depth)
- [ExpanderStartTime](#BKMK_ExpanderStartTime)
- [FriendlyMessage](#BKMK_FriendlyMessage)
- [HostId](#BKMK_HostId)
- [MessageName](#BKMK_MessageName)
- [Name](#BKMK_Name)
- [OperationType](#BKMK_OperationType)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningExtensionId](#BKMK_OwningExtensionId)
- [OwningExtensionTypeCode](#BKMK_OwningExtensionTypeCode)
- [ParentPluginExecutionId](#BKMK_ParentPluginExecutionId)
- [PostponeUntil](#BKMK_PostponeUntil)
- [PrimaryEntityType](#BKMK_PrimaryEntityType)
- [RecurrencePattern](#BKMK_RecurrencePattern)
- [RecurrenceStartTime](#BKMK_RecurrenceStartTime)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [RequestId](#BKMK_RequestId)
- [RetainJobHistory](#BKMK_RetainJobHistory)
- [RootExecutionContext](#BKMK_RootExecutionContext)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [WorkflowActivationId](#BKMK_WorkflowActivationId)
- [Workload](#BKMK_Workload)

### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the system job.**|
|DisplayName|**System Job**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`asyncoperationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_BreadcrumbId"></a> BreadcrumbId

|Property|Value|
|---|---|
|Description|**The breadcrumb record ID.**|
|DisplayName|**Breadcrumb ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`breadcrumbid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_CallerOrigin"></a> CallerOrigin

|Property|Value|
|---|---|
|Description|**The origin of the caller.**|
|DisplayName|**Caller Origin**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`callerorigin`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_CorrelationId"></a> CorrelationId

|Property|Value|
|---|---|
|Description|**Unique identifier used to correlate between multiple SDK requests and system jobs.**|
|DisplayName|**Correlation Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`correlationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_CorrelationUpdatedTime"></a> CorrelationUpdatedTime

|Property|Value|
|---|---|
|Description|**Last time the correlation depth was updated.**|
|DisplayName|**Correlation Updated Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`correlationupdatedtime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_Data"></a> Data

|Property|Value|
|---|---|
|Description|**Unstructured data associated with the system job.**|
|DisplayName|**Data**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`data`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_DependencyToken"></a> DependencyToken

|Property|Value|
|---|---|
|Description|**Execution of all operations with the same dependency token is serialized.**|
|DisplayName|**Dependency Token**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependencytoken`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_Depth"></a> Depth

|Property|Value|
|---|---|
|Description|**Number of SDK calls made since the first call.**|
|DisplayName|**Depth**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`depth`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ExpanderStartTime"></a> ExpanderStartTime

|Property|Value|
|---|---|
|Description|**The datetime when the Expander pipeline started.**|
|DisplayName|**Expander Start Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`expanderstarttime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_FriendlyMessage"></a> FriendlyMessage

|Property|Value|
|---|---|
|Description|**Message provided by the system job.**|
|DisplayName|**Friendly message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`friendlymessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_HostId"></a> HostId

|Property|Value|
|---|---|
|Description|**Unique identifier of the host that owns this system job.**|
|DisplayName|**Host**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`hostid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_MessageName"></a> MessageName

|Property|Value|
|---|---|
|Description|**Name of the message that started this system job.**|
|DisplayName|**Message Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`messagename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the system job.**|
|DisplayName|**System Job Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_OperationType"></a> OperationType

|Property|Value|
|---|---|
|Description|**Type of the system job.**|
|DisplayName|**System Job Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operationtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`asyncoperation_operationtype`|

#### OperationType Choices/Options

|Value|Label|
|---|---|
|1|**System Event**|
|2|**Bulk Email**|
|3|**Import File Parse**|
|4|**Transform Parse Data**|
|5|**Import**|
|6|**Activity Propagation**|
|7|**Duplicate Detection Rule Publish**|
|8|**Bulk Duplicate Detection**|
|9|**SQM Data Collection**|
|10|**Workflow**|
|11|**Quick Campaign**|
|12|**Matchcode Update**|
|13|**Bulk Delete**|
|14|**Deletion Service**|
|15|**Index Management**|
|16|**Collect Organization Statistics**|
|17|**Import Subprocess**|
|18|**Calculate Organization Storage Size**|
|19|**Collect Organization Database Statistics**|
|20|**Collection Organization Size Statistics**|
|21|**Database Tuning**|
|22|**Calculate Organization Maximum Storage Size**|
|23|**Bulk Delete Subprocess**|
|24|**Update Statistic Intervals**|
|25|**Organization Full Text Catalog Index**|
|26|**Database log backup**|
|27|**Update Contract States**|
|28|**DBCC SHRINKDATABASE maintenance job**|
|29|**DBCC SHRINKFILE maintenance job**|
|30|**Reindex all indices maintenance job**|
|31|**Storage Limit Notification**|
|32|**Cleanup inactive workflow assemblies**|
|35|**Recurring Series Expansion**|
|38|**Import Sample Data**|
|40|**Goal Roll Up**|
|41|**Audit Partition Creation**|
|42|**Check For Language Pack Updates**|
|43|**Provision Language Pack**|
|44|**Update Organization Database**|
|45|**Update Solution**|
|46|**Regenerate Entity Row Count Snapshot Data**|
|47|**Regenerate Read Share Snapshot Data**|
|49|**Post to Yammer**|
|50|**Outgoing Activity**|
|51|**Incoming Email Processing**|
|52|**Mailbox Test Access**|
|53|**Encryption Health Check**|
|54|**Execute Async Request**|
|56|**Update Entitlement States**|
|57|**Calculate Rollup Field**|
|58|**Mass Calculate Rollup Field**|
|59|**Import Translation**|
|62|**Convert Date And Time Behavior**|
|63|**EntityKey Index Creation**|
|65|**Update Knowledge Article States**|
|68|**Resource Booking Sync**|
|69|**Relationship Assistant Cards**|
|71|**Cleanup Solution Components**|
|72|**App Module Metadata Operation**|
|73|**ALM Anomaly Detection Operation**|
|75|**Flow Notification**|
|76|**Ribbon Client Metadata Operation**|
|79|**CallbackRegistration Expander Operation**|
|85|**Migrate notes to attachments job**|
|86|**Migrate article content to file storage**|
|87|**Updated Deactived On for Resolved Cases job**|
|88|**Cascade Reparent DB Async Operation**|
|89|**Cascade Merge Async Operation**|
|90|**CascadeAssign**|
|91|**CascadeDelete**|
|92|**Event Expander Operation**|
|93|**Import Solution Metadata**|
|94|**Bulk Delete File Attachment**|
|95|**Refresh Business Unit for Records Owned By Principal**|
|96|**Revoke Inherited Access**|
|98|**Create Or Refresh Virtual Entity**|
|100|**Cascade FlowSession Permissions Async Operation**|
|101|**Update Modern Flow Async Operation**|
|102|**AsyncArchive Async Operation**|
|103|**Cancel Async Operations (System)**|
|104|**Process Table For RecycleBin**|
|105|**Cascade Assign All Async Operation**|
|106|**Background Team Service Async Operation**|
|187|**Async Restore Job**|
|201|**Provision language for user**|
|202|**Export Solution Async Operation**|
|203|**Import Solution Async Operation**|
|204|**PublishAll Async Operation**|
|207|**DeleteAndPromote Async Operation**|
|208|**UninstallSolution Async Operation**|
|209|**ProvisionLanguage Async Operation**|
|210|**ImportTranslation Async Operation**|
|211|**StageAndUpgrade Async Operation**|
|239|**Denormalization Async Operation**|
|250|**Refresh Runtime Integration Components Async Operation**|
|300|**Bulk Archive Operation**|
|301|**Archive Execution Async Operation**|
|302|**FinOps Deployment Async Operation**|
|304|**Purge Archived Content Operation**|
|305|**Register Offering Async Operation**|
|306|**Execute DataProcessing Configuration**|
|307|**Sync Synapse Tables Schema**|
|308|**FinOps DB Sync Async Operation**|
|309|**FinOps Unit Test Async Operation**|
|320|**Catalog Service Generate Package Async Operation**|
|321|**Catalog Service Submit Approval Request Async Operation**|
|322|**Catalog Service Install Request Async Operation**|
|330|**TDS endpoint provisioning new TVF functions and grant permission Async Operation**|
|332|**FinOps Deploy Custom Package Async Operation**|
|333|**Deletes related Elastic Table records when a SQL record is deleted**|
|334|**Deletes related Elastic or SQL Table records when an Elastic Table record is deleted**|
|335|**Catalog service asyc operation to poll for a solution checker request**|
|336|**Catalog service asyc operation to submit a solution checker request**|
|337|**Solution service async operation to install solution after app updates**|
|12801|**Cascade Grant or Revoke Access Version Tracking Async Operation**|
|190690091|**AI Builder Training Events**|
|190690092|**AI Builder Prediction Events**|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the system job.**|
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

### <a name="BKMK_OwningExtensionId"></a> OwningExtensionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the owning extension with which the system job is associated.**|
|DisplayName|**Owning Extension**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningextensionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sdkmessageprocessingstep|

### <a name="BKMK_OwningExtensionTypeCode"></a> OwningExtensionTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningextensiontypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_ParentPluginExecutionId"></a> ParentPluginExecutionId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentpluginexecutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_PostponeUntil"></a> PostponeUntil

|Property|Value|
|---|---|
|Description|**Indicates whether the system job should run only after the specified date and time.**|
|DisplayName|**Postpone Until**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`postponeuntil`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PrimaryEntityType"></a> PrimaryEntityType

|Property|Value|
|---|---|
|Description|**Type of entity with which the system job is primarily associated.**|
|DisplayName|**Primary Entity Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`primaryentitytype`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_RecurrencePattern"></a> RecurrencePattern

|Property|Value|
|---|---|
|Description|**Pattern of the system job's recurrence.**|
|DisplayName|**Recurrence Pattern**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recurrencepattern`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_RecurrenceStartTime"></a> RecurrenceStartTime

|Property|Value|
|---|---|
|Description|**Starting time in UTC for the recurrence pattern.**|
|DisplayName|**Recurrence Start**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recurrencestarttime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the object with which the system job is associated.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, activityfileattachment, activitymimeattachment, activitypointer, adx_externalidentity, adx_invitation, adx_inviteredemption, adx_portalcomment, adx_setting, adx_webformsession, aicopilot, aiinsightcard, aiplugin, aipluginauth, aipluginconversationstarter, aipluginconversationstartermapping, aipluginexternalschema, aipluginexternalschemaproperty, aiplugingovernance, aiplugingovernanceext, aiplugininstance, aipluginoperation, aipluginoperationparameter, aipluginoperationresponsetemplate, aiplugintitle, aipluginusersetting, aiskillconfig, annotation, annualfiscalcalendar, appaction, appactionmigration, appactionrule, appelement, application, applicationuser, appmodulecomponentedge, appmodulecomponentnode, appointment, approvalprocess, approvalstageapproval, approvalstagecondition, approvalstageorder, appsetting, appusersetting, archivecleanupinfo, archivecleanupoperation, attributeimageconfig, attributemap, attributemaskingrule, attributepicklistvalue, bot, botcomponent, botcomponentcollection, bulkarchiveconfig, bulkarchivefailuredetail, bulkarchiveoperation, bulkarchiveoperationdetail, businessprocess, businessunit, businessunitnewsarticle, calendar, canvasappextendedmetadata, card, cascadegrantrevokeaccessrecordstracker, cascadegrantrevokeaccessversiontracker, catalog, catalogassignment, certificatecredential, channelaccessprofile, channelaccessprofilerule, chat, comment, connection, connectioninstance, connectionreference, connectionrole, connector, contact, conversationtranscript, convertrule, copilotexamplequestion, copilotglossaryterm, copilotsynonyms, credential, customapi, customapirequestparameter, customapiresponseproperty, customeraddress, customerrelationship, datalakefolder, datalakefolderpermission, datalakeworkspace, datalakeworkspacepermission, dataprocessingconfiguration, delegatedauthorization, deleteditemreference, desktopflowbinary, desktopflowmodule, displaystring, dvfilesearch, dvfilesearchattribute, dvfilesearchentity, dvtablesearch, dvtablesearchattribute, dvtablesearchentity, email, emailaddressconfiguration, emailserverprofile, enablearchivalrequest, entityanalyticsconfig, entityclusterconfig, entityimageconfig, entityindex, entitymap, entityrecordfilter, environmentvariabledefinition, environmentvariablevalue, exportedexcel, exportsolutionupload, externalparty, externalpartyitem, fabricaiskill, fax, featurecontrolsetting, federatedknowledgecitation, federatedknowledgeconfiguration, federatedknowledgeentityconfiguration, federatedknowledgemetadatarefresh, fixedmonthlyfiscalcalendar, flowcapacityassignment, flowcredentialapplication, flowevent, flowmachine, flowmachinegroup, flowmachineimage, flowmachineimageversion, flowmachinenetwork, flowsession, fxexpression, goal, goalrollupquery, governanceconfiguration, holidaywrapper, import, importdata, importfile, importlog, importmap, indexattributes, interactionforemail, internalcatalogassignment, isvconfig, kbarticle, kbarticlecomment, kbarticletemplate, keyvaultreference, knowledgearticle, knowledgebaserecord, letter, mailbox, mailmergetemplate, mainfewshot, makerfewshot, managedidentity, maskingrule, metadataforarchival, metric, mobileofflineprofileextension, monthlyfiscalcalendar, msdynce_botcontent, msdyn_aibdataset, msdyn_aibdatasetfile, msdyn_aibdatasetrecord, msdyn_aibdatasetscontainer, msdyn_aibfeedbackloop, msdyn_aibfile, msdyn_aibfileattacheddata, msdyn_aiconfiguration, msdyn_aidataprocessingevent, msdyn_aievaluationconfiguration, msdyn_aievaluationrun, msdyn_aievent, msdyn_aifptrainingdocument, msdyn_aimodel, msdyn_aimodelcatalog, msdyn_aiodimage, msdyn_aiodlabel, msdyn_aiodtrainingboundingbox, msdyn_aiodtrainingimage, msdyn_aitemplate, msdyn_aitestcase, msdyn_aitestcasedocument, msdyn_aitestcaseinput, msdyn_aitestrun, msdyn_aitestrunbatch, msdyn_analysiscomponent, msdyn_analysisjob, msdyn_analysisoverride, msdyn_analysisresult, msdyn_analysisresultdetail, msdyn_appinsightsmetadata, msdyn_copilotinteractions, msdyn_customcontrolextendedsettings, msdyn_dataflow, msdyn_dataflowconnectionreference, msdyn_dataflowrefreshhistory, msdyn_dataflowtemplate, msdyn_dataflow_datalakefolder, msdyn_dataworkspace, msdyn_dmsrequest, msdyn_dmsrequeststatus, msdyn_dmssyncrequest, msdyn_dmssyncstatus, msdyn_entitylinkchatconfiguration, msdyn_entityrefreshhistory, msdyn_favoriteknowledgearticle, msdyn_federatedarticle, msdyn_federatedarticleincident, msdyn_fileupload, msdyn_flow_actionapprovalmodel, msdyn_flow_approval, msdyn_flow_approvalrequest, msdyn_flow_approvalresponse, msdyn_flow_approvalstep, msdyn_flow_awaitallactionapprovalmodel, msdyn_flow_awaitallapprovalmodel, msdyn_flow_basicapprovalmodel, msdyn_flow_flowapproval, msdyn_formmapping, msdyn_function, msdyn_helppage, msdyn_insightsstorevirtualentity, msdyn_integratedsearchprovider, msdyn_kalanguagesetting, msdyn_kbattachment, msdyn_kmfederatedsearchconfig, msdyn_kmpersonalizationsetting, msdyn_knowledgearticleimage, msdyn_knowledgearticletemplate, msdyn_knowledgeassetconfiguration, msdyn_knowledgeconfiguration, msdyn_knowledgeinteractioninsight, msdyn_knowledgemanagementsetting, msdyn_knowledgepersonalfilter, msdyn_knowledgesearchfilter, msdyn_knowledgesearchinsight, msdyn_mobileapp, msdyn_modulerundetail, msdyn_plan, msdyn_planartifact, msdyn_planattachment, msdyn_pmanalysishistory, msdyn_pmbusinessruleautomationconfig, msdyn_pmcalendar, msdyn_pmcalendarversion, msdyn_pminferredtask, msdyn_pmprocessextendedmetadataversion, msdyn_pmprocesstemplate, msdyn_pmprocessusersettings, msdyn_pmprocessversion, msdyn_pmrecording, msdyn_pmsimulation, msdyn_pmtemplate, msdyn_pmview, msdyn_qna, msdyn_richtextfile, msdyn_salesforcestructuredobject, msdyn_salesforcestructuredqnaconfig, msdyn_schedule, msdyn_serviceconfiguration, msdyn_slakpi, msdyn_solutionhealthrule, msdyn_solutionhealthruleargument, msdyn_solutionhealthruleset, msdyn_tour, msdyn_virtualtablecolumncandidate, msdyn_workflowactionstatus, msgraphresourcetosubscription, mspcat_catalogsubmissionfiles, mspcat_packagestore, organization, organizationdatasyncfnostate, organizationdatasyncstate, organizationdatasyncsubscription, organizationdatasyncsubscriptionentity, organizationdatasyncsubscriptionfnotable, organizationsetting, package, packagehistory, pdfsetting, phonecall, plannerbusinessscenario, plannersyncaction, plugin, pluginpackage, position, post, postfollow, powerbidataset, powerbidatasetapdx, powerbimashupparameter, powerbireport, powerbireportapdx, powerfxrule, powerpagecomponent, powerpagesite, powerpagesitelanguage, powerpagesitepublished, powerpagesmanagedidentity, powerpagesscanreport, privilege, privilegecheckerlog, privilegecheckerrun, privilegesremovalsetting, processorregistration, processstageparameter, provisionlanguageforuser, quarterlyfiscalcalendar, queue, queueitem, reconciliationentityinfo, reconciliationentitystepinfo, reconciliationinfo, recordfilter, recurringappointmentmaster, recyclebinconfig, relationshipattribute, relationshiprole, relationshiprolemap, report, reportparameter, retaineddataexcel, retentioncleanupinfo, retentioncleanupoperation, retentionconfig, retentionfailuredetail, retentionoperation, retentionoperationdetail, retentionsuccessdetail, revokeinheritedaccessrecordstracker, role, roleeditorlayout, rollupfield, routingrule, routingruleitem, savedquery, savingrule, searchattributesettings, searchcustomanalyzer, searchrelationshipsettings, semiannualfiscalcalendar, serviceplan, serviceplancustomcontrol, serviceplanmapping, settingdefinition, sharedlinksetting, sharedobject, sharedworkspace, sharedworkspacepool, sharepointdocumentlocation, sharepointmanagedidentity, sharepointsite, sideloadedaiplugin, signalregistration, similarityrule, sla, socialactivity, socialprofile, solutioncomponentattributeconfiguration, solutioncomponentbatchconfiguration, solutioncomponentconfiguration, solutioncomponentrelationshipconfiguration, stagedentity, stagedentityattribute, stagedmetadataasyncoperation, stagesolutionupload, subject, supportusertable, synapsedatabase, synapselinkexternaltablestate, synapselinkprofile, synapselinkprofileentity, synapselinkprofileentitystate, synapselinkschedule, systemform, systemuser, systemuserauthorizationchangetracker, tag, taggedflowsession, taggedprocess, task, tdsmetadata, team, teammobileofflineprofilemembership, template, territory, theme, traitregistration, transactioncurrency, unstructuredfilesearchentity, unstructuredfilesearchrecord, userform, usermapping, usermobileofflineprofilemembership, userquery, userrating, viewasexamplequestion, virtualentitymetadata, workflowbinary, workflowmetadata, workqueue, workqueueitem|

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

### <a name="BKMK_RequestId"></a> RequestId

|Property|Value|
|---|---|
|Description|**Unique identifier of the request that generated the system job.**|
|DisplayName|**Request**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requestid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RetainJobHistory"></a> RetainJobHistory

|Property|Value|
|---|---|
|Description|**Retain job history.**|
|DisplayName|**Retain Job History**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`retainjobhistory`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`asyncoperation_retainjobhistory`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_RootExecutionContext"></a> RootExecutionContext

|Property|Value|
|---|---|
|Description|**Root execution context of the job that trigerred async job.**|
|DisplayName|**RootExecutionContext**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rootexecutioncontext`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the system job.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`asyncoperation_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Ready**<br />DefaultStatus: 0<br />InvariantName: `Ready`|
|1|Label: **Suspended**<br />DefaultStatus: 10<br />InvariantName: `Suspended`|
|2|Label: **Locked**<br />DefaultStatus: 20<br />InvariantName: `Locked`|
|3|Label: **Completed**<br />DefaultStatus: 30<br />InvariantName: `Completed`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the system job.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`asyncoperation_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Waiting For Resources**<br />State:0<br />TransitionData: None|
|10|Label: **Waiting**<br />State:1<br />TransitionData: None|
|20|Label: **In Progress**<br />State:2<br />TransitionData: None|
|21|Label: **Pausing**<br />State:2<br />TransitionData: None|
|22|Label: **Canceling**<br />State:2<br />TransitionData: None|
|30|Label: **Succeeded**<br />State:3<br />TransitionData: None|
|31|Label: **Failed**<br />State:3<br />TransitionData: None|
|32|Label: **Canceled**<br />State:3<br />TransitionData: None|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
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
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_WorkflowActivationId"></a> WorkflowActivationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the workflow activation related to the system job.**|
|DisplayName|**Workflow Activation Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workflowactivationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_Workload"></a> Workload

|Property|Value|
|---|---|
|Description|**The workload name.**|
|DisplayName|**Workload**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`workload`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CompletedOn](#BKMK_CompletedOn)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [DataBlobId](#BKMK_DataBlobId)
- [DataBlobId_Name](#BKMK_DataBlobId_Name)
- [ErrorCode](#BKMK_ErrorCode)
- [ExecutionTimeSpan](#BKMK_ExecutionTimeSpan)
- [IsWaitingForEvent](#BKMK_IsWaitingForEvent)
- [Message](#BKMK_Message)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [RetryCount](#BKMK_RetryCount)
- [Sequence](#BKMK_Sequence)
- [StartedOn](#BKMK_StartedOn)
- [Subtype](#BKMK_Subtype)
- [WorkflowIsBlocked](#BKMK_WorkflowIsBlocked)
- [WorkflowStageName](#BKMK_WorkflowStageName)
- [WorkflowState](#BKMK_WorkflowState)

### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|---|---|
|Description|**Date and time when the system job was completed.**|
|DisplayName|**Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`completedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the system job.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the system job was created.**|
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
|Description|**Unique identifier of the delegate user who created the asyncoperation.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_DataBlobId"></a> DataBlobId

|Property|Value|
|---|---|
|Description|**File Id for the blob url used for file storage.**|
|DisplayName|**Data File Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`datablobid`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|128000|

### <a name="BKMK_DataBlobId_Name"></a> DataBlobId_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`datablobid_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ErrorCode"></a> ErrorCode

|Property|Value|
|---|---|
|Description|**Error code returned from a canceled system job.**|
|DisplayName|**Error Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errorcode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ExecutionTimeSpan"></a> ExecutionTimeSpan

|Property|Value|
|---|---|
|Description|**Time that the system job has taken to execute.**|
|DisplayName|**ExecutionTimeSpan**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`executiontimespan`|
|RequiredLevel|SystemRequired|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_IsWaitingForEvent"></a> IsWaitingForEvent

|Property|Value|
|---|---|
|Description|**Indicates that the system job is waiting for an event.**|
|DisplayName|**Waiting for Event**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iswaitingforevent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`asyncoperation_iswaitingforevent`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Message"></a> Message

|Property|Value|
|---|---|
|Description|**Message related to the system job.**|
|DisplayName|**Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`message`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the system job.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the system job was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the asyncoperation.**|
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
|MaxLength|160|

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
|MaxLength|160|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit that owns the system job.**|
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
|Description|**Unique identifier of the team who owns the record.**|
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
|Description|**Unique identifier of the user who owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_RetryCount"></a> RetryCount

|Property|Value|
|---|---|
|Description|**Number of times to retry the system job.**|
|DisplayName|**Retry Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`retrycount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_Sequence"></a> Sequence

|Property|Value|
|---|---|
|Description|**Order in which operations were submitted.**|
|DisplayName|**Sequence**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sequence`|
|RequiredLevel|SystemRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_StartedOn"></a> StartedOn

|Property|Value|
|---|---|
|Description|**Date and time when the system job was started.**|
|DisplayName|**Started On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`startedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_Subtype"></a> Subtype

|Property|Value|
|---|---|
|Description|**The Subtype of the Async Job**|
|DisplayName|**Subtype**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subtype`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|255|
|MinValue|0|

### <a name="BKMK_WorkflowIsBlocked"></a> WorkflowIsBlocked

|Property|Value|
|---|---|
|Description|**Indicates whether the workflow instance was blocked when it was persisted.**|
|DisplayName|**Workflow Is Blocked**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`workflowisblocked`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`asyncoperation_workflowisblocked`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_WorkflowStageName"></a> WorkflowStageName

|Property|Value|
|---|---|
|Description|**Name of a workflow stage.**|
|DisplayName|**Workflow Stage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`workflowstagename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_WorkflowState"></a> WorkflowState

|Property|Value|
|---|---|
|Description|**State of the workflow job.**|
|DisplayName|**Workflow State**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`workflowstate`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [Account_AsyncOperations](#BKMK_Account_AsyncOperations)
- [activityfileattachment_AsyncOperations](#BKMK_activityfileattachment_AsyncOperations)
- [ActivityMimeAttachment_AsyncOperations](#BKMK_ActivityMimeAttachment_AsyncOperations)
- [ActivityPointer_AsyncOperations](#BKMK_ActivityPointer_AsyncOperations)
- [adx_externalidentity_AsyncOperations](#BKMK_adx_externalidentity_AsyncOperations)
- [adx_invitation_AsyncOperations](#BKMK_adx_invitation_AsyncOperations)
- [adx_inviteredemption_AsyncOperations](#BKMK_adx_inviteredemption_AsyncOperations)
- [adx_portalcomment_AsyncOperations](#BKMK_adx_portalcomment_AsyncOperations)
- [adx_setting_AsyncOperations](#BKMK_adx_setting_AsyncOperations)
- [adx_webformsession_AsyncOperations](#BKMK_adx_webformsession_AsyncOperations)
- [aicopilot_AsyncOperations](#BKMK_aicopilot_AsyncOperations)
- [aiplugin_AsyncOperations](#BKMK_aiplugin_AsyncOperations)
- [aipluginauth_AsyncOperations](#BKMK_aipluginauth_AsyncOperations)
- [aipluginconversationstarter_AsyncOperations](#BKMK_aipluginconversationstarter_AsyncOperations)
- [aipluginconversationstartermapping_AsyncOperations](#BKMK_aipluginconversationstartermapping_AsyncOperations)
- [aipluginexternalschema_AsyncOperations](#BKMK_aipluginexternalschema_AsyncOperations)
- [aipluginexternalschemaproperty_AsyncOperations](#BKMK_aipluginexternalschemaproperty_AsyncOperations)
- [aiplugingovernance_AsyncOperations](#BKMK_aiplugingovernance_AsyncOperations)
- [aiplugingovernanceext_AsyncOperations](#BKMK_aiplugingovernanceext_AsyncOperations)
- [aiplugininstance_AsyncOperations](#BKMK_aiplugininstance_AsyncOperations)
- [aipluginoperation_AsyncOperations](#BKMK_aipluginoperation_AsyncOperations)
- [aipluginoperationparameter_AsyncOperations](#BKMK_aipluginoperationparameter_AsyncOperations)
- [aipluginoperationresponsetemplate_AsyncOperations](#BKMK_aipluginoperationresponsetemplate_AsyncOperations)
- [aiplugintitle_AsyncOperations](#BKMK_aiplugintitle_AsyncOperations)
- [aipluginusersetting_AsyncOperations](#BKMK_aipluginusersetting_AsyncOperations)
- [Annotation_AsyncOperations](#BKMK_Annotation_AsyncOperations)
- [AnnualFiscalCalendar_AsyncOperations](#BKMK_AnnualFiscalCalendar_AsyncOperations)
- [appaction_AsyncOperations](#BKMK_appaction_AsyncOperations)
- [appactionmigration_AsyncOperations](#BKMK_appactionmigration_AsyncOperations)
- [appactionrule_AsyncOperations](#BKMK_appactionrule_AsyncOperations)
- [application_AsyncOperations](#BKMK_application_AsyncOperations)
- [applicationuser_AsyncOperations](#BKMK_applicationuser_AsyncOperations)
- [Appointment_AsyncOperations](#BKMK_Appointment_AsyncOperations)
- [approvalprocess_AsyncOperations](#BKMK_approvalprocess_AsyncOperations)
- [approvalstageapproval_AsyncOperations](#BKMK_approvalstageapproval_AsyncOperations)
- [approvalstagecondition_AsyncOperations](#BKMK_approvalstagecondition_AsyncOperations)
- [approvalstageorder_AsyncOperations](#BKMK_approvalstageorder_AsyncOperations)
- [attributeimageconfig_AsyncOperations](#BKMK_attributeimageconfig_AsyncOperations)
- [attributemaskingrule_AsyncOperations](#BKMK_attributemaskingrule_AsyncOperations)
- [attributepicklistvalue_AsyncOperations](#BKMK_attributepicklistvalue_AsyncOperations)
- [bot_AsyncOperations](#BKMK_bot_AsyncOperations)
- [botcomponent_AsyncOperations](#BKMK_botcomponent_AsyncOperations)
- [botcomponentcollection_AsyncOperations](#BKMK_botcomponentcollection_AsyncOperations)
- [business_unit_asyncoperation](#BKMK_business_unit_asyncoperation)
- [businessprocess_AsyncOperations](#BKMK_businessprocess_AsyncOperations)
- [BusinessUnit_AsyncOperations](#BKMK_BusinessUnit_AsyncOperations)
- [BusinessUnitNewsArticle_AsyncOperations](#BKMK_BusinessUnitNewsArticle_AsyncOperations)
- [Calendar_AsyncOperations](#BKMK_Calendar_AsyncOperations)
- [card_AsyncOperations](#BKMK_card_AsyncOperations)
- [catalog_AsyncOperations](#BKMK_catalog_AsyncOperations)
- [catalogassignment_AsyncOperations](#BKMK_catalogassignment_AsyncOperations)
- [certificatecredential_AsyncOperations](#BKMK_certificatecredential_AsyncOperations)
- [chat_AsyncOperations](#BKMK_chat_AsyncOperations)
- [Connection_AsyncOperations](#BKMK_Connection_AsyncOperations)
- [Connection_Role_AsyncOperations](#BKMK_Connection_Role_AsyncOperations)
- [connectioninstance_AsyncOperations](#BKMK_connectioninstance_AsyncOperations)
- [connectionreference_AsyncOperations](#BKMK_connectionreference_AsyncOperations)
- [connector_AsyncOperations](#BKMK_connector_AsyncOperations)
- [Contact_AsyncOperations](#BKMK_Contact_AsyncOperations)
- [conversationtranscript_AsyncOperations](#BKMK_conversationtranscript_AsyncOperations)
- [copilotexamplequestion_AsyncOperations](#BKMK_copilotexamplequestion_AsyncOperations)
- [copilotglossaryterm_AsyncOperations](#BKMK_copilotglossaryterm_AsyncOperations)
- [copilotsynonyms_AsyncOperations](#BKMK_copilotsynonyms_AsyncOperations)
- [credential_AsyncOperations](#BKMK_credential_AsyncOperations)
- [customapi_AsyncOperations](#BKMK_customapi_AsyncOperations)
- [customapirequestparameter_AsyncOperations](#BKMK_customapirequestparameter_AsyncOperations)
- [customapiresponseproperty_AsyncOperations](#BKMK_customapiresponseproperty_AsyncOperations)
- [CustomerAddress_AsyncOperations](#BKMK_CustomerAddress_AsyncOperations)
- [datalakefolder_AsyncOperations](#BKMK_datalakefolder_AsyncOperations)
- [datalakefolderpermission_AsyncOperations](#BKMK_datalakefolderpermission_AsyncOperations)
- [datalakeworkspace_AsyncOperations](#BKMK_datalakeworkspace_AsyncOperations)
- [datalakeworkspacepermission_AsyncOperations](#BKMK_datalakeworkspacepermission_AsyncOperations)
- [dataprocessingconfiguration_AsyncOperations](#BKMK_dataprocessingconfiguration_AsyncOperations)
- [delegatedauthorization_AsyncOperations](#BKMK_delegatedauthorization_AsyncOperations)
- [desktopflowbinary_AsyncOperations](#BKMK_desktopflowbinary_AsyncOperations)
- [desktopflowmodule_AsyncOperations](#BKMK_desktopflowmodule_AsyncOperations)
- [DisplayString_AsyncOperations](#BKMK_DisplayString_AsyncOperations)
- [dvfilesearch_AsyncOperations](#BKMK_dvfilesearch_AsyncOperations)
- [dvfilesearchattribute_AsyncOperations](#BKMK_dvfilesearchattribute_AsyncOperations)
- [dvfilesearchentity_AsyncOperations](#BKMK_dvfilesearchentity_AsyncOperations)
- [dvtablesearch_AsyncOperations](#BKMK_dvtablesearch_AsyncOperations)
- [dvtablesearchattribute_AsyncOperations](#BKMK_dvtablesearchattribute_AsyncOperations)
- [dvtablesearchentity_AsyncOperations](#BKMK_dvtablesearchentity_AsyncOperations)
- [Email_AsyncOperations](#BKMK_Email_AsyncOperations)
- [emailaddressconfiguration_AsyncOperations](#BKMK_emailaddressconfiguration_AsyncOperations)
- [emailserverprofile_asyncoperations](#BKMK_emailserverprofile_asyncoperations)
- [entityanalyticsconfig_AsyncOperations](#BKMK_entityanalyticsconfig_AsyncOperations)
- [entityclusterconfig_AsyncOperations](#BKMK_entityclusterconfig_AsyncOperations)
- [entityimageconfig_AsyncOperations](#BKMK_entityimageconfig_AsyncOperations)
- [entityindex_AsyncOperations](#BKMK_entityindex_AsyncOperations)
- [entityrecordfilter_AsyncOperations](#BKMK_entityrecordfilter_AsyncOperations)
- [environmentvariabledefinition_AsyncOperations](#BKMK_environmentvariabledefinition_AsyncOperations)
- [environmentvariablevalue_AsyncOperations](#BKMK_environmentvariablevalue_AsyncOperations)
- [exportedexcel_AsyncOperations](#BKMK_exportedexcel_AsyncOperations)
- [exportsolutionupload_AsyncOperations](#BKMK_exportsolutionupload_AsyncOperations)
- [fabricaiskill_AsyncOperations](#BKMK_fabricaiskill_AsyncOperations)
- [Fax_AsyncOperations](#BKMK_Fax_AsyncOperations)
- [featurecontrolsetting_AsyncOperations](#BKMK_featurecontrolsetting_AsyncOperations)
- [federatedknowledgeconfiguration_AsyncOperations](#BKMK_federatedknowledgeconfiguration_AsyncOperations)
- [federatedknowledgeentityconfiguration_AsyncOperations](#BKMK_federatedknowledgeentityconfiguration_AsyncOperations)
- [FileAttachment_AsyncOperation_DataBlobId](#BKMK_FileAttachment_AsyncOperation_DataBlobId)
- [FixedMonthlyFiscalCalendar_AsyncOperations](#BKMK_FixedMonthlyFiscalCalendar_AsyncOperations)
- [flowcapacityassignment_AsyncOperations](#BKMK_flowcapacityassignment_AsyncOperations)
- [flowcredentialapplication_AsyncOperations](#BKMK_flowcredentialapplication_AsyncOperations)
- [flowevent_AsyncOperations](#BKMK_flowevent_AsyncOperations)
- [flowmachine_AsyncOperations](#BKMK_flowmachine_AsyncOperations)
- [flowmachinegroup_AsyncOperations](#BKMK_flowmachinegroup_AsyncOperations)
- [flowmachineimage_AsyncOperations](#BKMK_flowmachineimage_AsyncOperations)
- [flowmachineimageversion_AsyncOperations](#BKMK_flowmachineimageversion_AsyncOperations)
- [flowmachinenetwork_AsyncOperations](#BKMK_flowmachinenetwork_AsyncOperations)
- [flowsession_AsyncOperations](#BKMK_flowsession_AsyncOperations)
- [fxexpression_AsyncOperations](#BKMK_fxexpression_AsyncOperations)
- [Goal_AsyncOperations](#BKMK_Goal_AsyncOperations)
- [goalrollupquery_AsyncOperations](#BKMK_goalrollupquery_AsyncOperations)
- [governanceconfiguration_AsyncOperations](#BKMK_governanceconfiguration_AsyncOperations)
- [Import_AsyncOperations](#BKMK_Import_AsyncOperations)
- [ImportData_AsyncOperations](#BKMK_ImportData_AsyncOperations)
- [ImportFile_AsyncOperations](#BKMK_ImportFile_AsyncOperations)
- [ImportLog_AsyncOperations](#BKMK_ImportLog_AsyncOperations)
- [ImportMap_AsyncOperations](#BKMK_ImportMap_AsyncOperations)
- [indexattributes_AsyncOperations](#BKMK_indexattributes_AsyncOperations)
- [interactionforemail_AsyncOperations](#BKMK_interactionforemail_AsyncOperations)
- [KbArticle_AsyncOperations](#BKMK_KbArticle_AsyncOperations)
- [KbArticleComment_AsyncOperations](#BKMK_KbArticleComment_AsyncOperations)
- [KbArticleTemplate_AsyncOperations](#BKMK_KbArticleTemplate_AsyncOperations)
- [keyvaultreference_AsyncOperations](#BKMK_keyvaultreference_AsyncOperations)
- [knowledgearticle_AsyncOperations](#BKMK_knowledgearticle_AsyncOperations)
- [KnowledgeBaseRecord_AsyncOperations](#BKMK_KnowledgeBaseRecord_AsyncOperations)
- [Letter_AsyncOperations](#BKMK_Letter_AsyncOperations)
- [lk_asyncoperation_createdby](#BKMK_lk_asyncoperation_createdby)
- [lk_asyncoperation_createdonbehalfby](#BKMK_lk_asyncoperation_createdonbehalfby)
- [lk_asyncoperation_modifiedby](#BKMK_lk_asyncoperation_modifiedby)
- [lk_asyncoperation_modifiedonbehalfby](#BKMK_lk_asyncoperation_modifiedonbehalfby)
- [lk_asyncoperation_workflowactivationid](#BKMK_lk_asyncoperation_workflowactivationid)
- [mailbox_asyncoperations](#BKMK_mailbox_asyncoperations)
- [MailMergeTemplate_AsyncOperations](#BKMK_MailMergeTemplate_AsyncOperations)
- [mainfewshot_AsyncOperations](#BKMK_mainfewshot_AsyncOperations)
- [makerfewshot_AsyncOperations](#BKMK_makerfewshot_AsyncOperations)
- [managedidentity_AsyncOperations](#BKMK_managedidentity_AsyncOperations)
- [maskingrule_AsyncOperations](#BKMK_maskingrule_AsyncOperations)
- [metadataforarchival_AsyncOperations](#BKMK_metadataforarchival_AsyncOperations)
- [metric_AsyncOperations](#BKMK_metric_AsyncOperations)
- [mobileofflineprofileextension_AsyncOperations](#BKMK_mobileofflineprofileextension_AsyncOperations)
- [MonthlyFiscalCalendar_AsyncOperations](#BKMK_MonthlyFiscalCalendar_AsyncOperations)
- [msdyn_aibdataset_AsyncOperations](#BKMK_msdyn_aibdataset_AsyncOperations)
- [msdyn_aibdatasetfile_AsyncOperations](#BKMK_msdyn_aibdatasetfile_AsyncOperations)
- [msdyn_aibdatasetrecord_AsyncOperations](#BKMK_msdyn_aibdatasetrecord_AsyncOperations)
- [msdyn_aibdatasetscontainer_AsyncOperations](#BKMK_msdyn_aibdatasetscontainer_AsyncOperations)
- [msdyn_aibfeedbackloop_AsyncOperations](#BKMK_msdyn_aibfeedbackloop_AsyncOperations)
- [msdyn_aibfile_AsyncOperations](#BKMK_msdyn_aibfile_AsyncOperations)
- [msdyn_aibfileattacheddata_AsyncOperations](#BKMK_msdyn_aibfileattacheddata_AsyncOperations)
- [msdyn_aiconfiguration_AsyncOperations](#BKMK_msdyn_aiconfiguration_AsyncOperations)
- [msdyn_aidataprocessingevent_AsyncOperations](#BKMK_msdyn_aidataprocessingevent_AsyncOperations)
- [msdyn_aievaluationconfiguration_AsyncOperations](#BKMK_msdyn_aievaluationconfiguration_AsyncOperations)
- [msdyn_aievaluationrun_AsyncOperations](#BKMK_msdyn_aievaluationrun_AsyncOperations)
- [msdyn_aievent_AsyncOperations](#BKMK_msdyn_aievent_AsyncOperations)
- [msdyn_aifptrainingdocument_AsyncOperations](#BKMK_msdyn_aifptrainingdocument_AsyncOperations)
- [msdyn_aimodel_AsyncOperations](#BKMK_msdyn_aimodel_AsyncOperations)
- [msdyn_aimodelcatalog_AsyncOperations](#BKMK_msdyn_aimodelcatalog_AsyncOperations)
- [msdyn_aiodimage_AsyncOperations](#BKMK_msdyn_aiodimage_AsyncOperations)
- [msdyn_aiodlabel_AsyncOperations](#BKMK_msdyn_aiodlabel_AsyncOperations)
- [msdyn_aiodtrainingboundingbox_AsyncOperations](#BKMK_msdyn_aiodtrainingboundingbox_AsyncOperations)
- [msdyn_aiodtrainingimage_AsyncOperations](#BKMK_msdyn_aiodtrainingimage_AsyncOperations)
- [msdyn_aitemplate_AsyncOperations](#BKMK_msdyn_aitemplate_AsyncOperations)
- [msdyn_aitestcase_AsyncOperations](#BKMK_msdyn_aitestcase_AsyncOperations)
- [msdyn_aitestcasedocument_AsyncOperations](#BKMK_msdyn_aitestcasedocument_AsyncOperations)
- [msdyn_aitestcaseinput_AsyncOperations](#BKMK_msdyn_aitestcaseinput_AsyncOperations)
- [msdyn_aitestrun_AsyncOperations](#BKMK_msdyn_aitestrun_AsyncOperations)
- [msdyn_aitestrunbatch_AsyncOperations](#BKMK_msdyn_aitestrunbatch_AsyncOperations)
- [msdyn_analysiscomponent_AsyncOperations](#BKMK_msdyn_analysiscomponent_AsyncOperations)
- [msdyn_analysisjob_AsyncOperations](#BKMK_msdyn_analysisjob_AsyncOperations)
- [msdyn_analysisoverride_AsyncOperations](#BKMK_msdyn_analysisoverride_AsyncOperations)
- [msdyn_analysisresult_AsyncOperations](#BKMK_msdyn_analysisresult_AsyncOperations)
- [msdyn_analysisresultdetail_AsyncOperations](#BKMK_msdyn_analysisresultdetail_AsyncOperations)
- [msdyn_appinsightsmetadata_AsyncOperations](#BKMK_msdyn_appinsightsmetadata_AsyncOperations)
- [msdyn_copilotinteractions_AsyncOperations](#BKMK_msdyn_copilotinteractions_AsyncOperations)
- [msdyn_customcontrolextendedsettings_AsyncOperations](#BKMK_msdyn_customcontrolextendedsettings_AsyncOperations)
- [msdyn_dataflow_AsyncOperations](#BKMK_msdyn_dataflow_AsyncOperations)
- [msdyn_dataflow_datalakefolder_AsyncOperations](#BKMK_msdyn_dataflow_datalakefolder_AsyncOperations)
- [msdyn_dataflowconnectionreference_AsyncOperations](#BKMK_msdyn_dataflowconnectionreference_AsyncOperations)
- [msdyn_dataflowrefreshhistory_AsyncOperations](#BKMK_msdyn_dataflowrefreshhistory_AsyncOperations)
- [msdyn_dataflowtemplate_AsyncOperations](#BKMK_msdyn_dataflowtemplate_AsyncOperations)
- [msdyn_dmsrequest_AsyncOperations](#BKMK_msdyn_dmsrequest_AsyncOperations)
- [msdyn_dmsrequeststatus_AsyncOperations](#BKMK_msdyn_dmsrequeststatus_AsyncOperations)
- [msdyn_dmssyncrequest_AsyncOperations](#BKMK_msdyn_dmssyncrequest_AsyncOperations)
- [msdyn_dmssyncstatus_AsyncOperations](#BKMK_msdyn_dmssyncstatus_AsyncOperations)
- [msdyn_entitylinkchatconfiguration_AsyncOperations](#BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations)
- [msdyn_entityrefreshhistory_AsyncOperations](#BKMK_msdyn_entityrefreshhistory_AsyncOperations)
- [msdyn_favoriteknowledgearticle_AsyncOperations](#BKMK_msdyn_favoriteknowledgearticle_AsyncOperations)
- [msdyn_federatedarticle_AsyncOperations](#BKMK_msdyn_federatedarticle_AsyncOperations)
- [msdyn_federatedarticleincident_AsyncOperations](#BKMK_msdyn_federatedarticleincident_AsyncOperations)
- [msdyn_fileupload_AsyncOperations](#BKMK_msdyn_fileupload_AsyncOperations)
- [msdyn_flow_actionapprovalmodel_AsyncOperations](#BKMK_msdyn_flow_actionapprovalmodel_AsyncOperations)
- [msdyn_flow_approval_AsyncOperations](#BKMK_msdyn_flow_approval_AsyncOperations)
- [msdyn_flow_approvalrequest_AsyncOperations](#BKMK_msdyn_flow_approvalrequest_AsyncOperations)
- [msdyn_flow_approvalresponse_AsyncOperations](#BKMK_msdyn_flow_approvalresponse_AsyncOperations)
- [msdyn_flow_approvalstep_AsyncOperations](#BKMK_msdyn_flow_approvalstep_AsyncOperations)
- [msdyn_flow_awaitallactionapprovalmodel_AsyncOperations](#BKMK_msdyn_flow_awaitallactionapprovalmodel_AsyncOperations)
- [msdyn_flow_awaitallapprovalmodel_AsyncOperations](#BKMK_msdyn_flow_awaitallapprovalmodel_AsyncOperations)
- [msdyn_flow_basicapprovalmodel_AsyncOperations](#BKMK_msdyn_flow_basicapprovalmodel_AsyncOperations)
- [msdyn_flow_flowapproval_AsyncOperations](#BKMK_msdyn_flow_flowapproval_AsyncOperations)
- [msdyn_formmapping_AsyncOperations](#BKMK_msdyn_formmapping_AsyncOperations)
- [msdyn_function_AsyncOperations](#BKMK_msdyn_function_AsyncOperations)
- [msdyn_helppage_AsyncOperations](#BKMK_msdyn_helppage_AsyncOperations)
- [msdyn_insightsstorevirtualentity_AsyncOperations](#BKMK_msdyn_insightsstorevirtualentity_AsyncOperations)
- [msdyn_integratedsearchprovider_AsyncOperations](#BKMK_msdyn_integratedsearchprovider_AsyncOperations)
- [msdyn_kalanguagesetting_AsyncOperations](#BKMK_msdyn_kalanguagesetting_AsyncOperations)
- [msdyn_kbattachment_AsyncOperations](#BKMK_msdyn_kbattachment_AsyncOperations)
- [msdyn_kmfederatedsearchconfig_AsyncOperations](#BKMK_msdyn_kmfederatedsearchconfig_AsyncOperations)
- [msdyn_kmpersonalizationsetting_AsyncOperations](#BKMK_msdyn_kmpersonalizationsetting_AsyncOperations)
- [msdyn_knowledgearticleimage_AsyncOperations](#BKMK_msdyn_knowledgearticleimage_AsyncOperations)
- [msdyn_knowledgearticletemplate_AsyncOperations](#BKMK_msdyn_knowledgearticletemplate_AsyncOperations)
- [msdyn_knowledgeassetconfiguration_AsyncOperations](#BKMK_msdyn_knowledgeassetconfiguration_AsyncOperations)
- [msdyn_knowledgeconfiguration_AsyncOperations](#BKMK_msdyn_knowledgeconfiguration_AsyncOperations)
- [msdyn_knowledgeinteractioninsight_AsyncOperations](#BKMK_msdyn_knowledgeinteractioninsight_AsyncOperations)
- [msdyn_knowledgemanagementsetting_AsyncOperations](#BKMK_msdyn_knowledgemanagementsetting_AsyncOperations)
- [msdyn_knowledgepersonalfilter_AsyncOperations](#BKMK_msdyn_knowledgepersonalfilter_AsyncOperations)
- [msdyn_knowledgesearchfilter_AsyncOperations](#BKMK_msdyn_knowledgesearchfilter_AsyncOperations)
- [msdyn_knowledgesearchinsight_AsyncOperations](#BKMK_msdyn_knowledgesearchinsight_AsyncOperations)
- [msdyn_mobileapp_AsyncOperations](#BKMK_msdyn_mobileapp_AsyncOperations)
- [msdyn_modulerundetail_AsyncOperations](#BKMK_msdyn_modulerundetail_AsyncOperations)
- [msdyn_pmanalysishistory_AsyncOperations](#BKMK_msdyn_pmanalysishistory_AsyncOperations)
- [msdyn_pmbusinessruleautomationconfig_AsyncOperations](#BKMK_msdyn_pmbusinessruleautomationconfig_AsyncOperations)
- [msdyn_pmcalendar_AsyncOperations](#BKMK_msdyn_pmcalendar_AsyncOperations)
- [msdyn_pmcalendarversion_AsyncOperations](#BKMK_msdyn_pmcalendarversion_AsyncOperations)
- [msdyn_pminferredtask_AsyncOperations](#BKMK_msdyn_pminferredtask_AsyncOperations)
- [msdyn_pmprocessextendedmetadataversion_AsyncOperations](#BKMK_msdyn_pmprocessextendedmetadataversion_AsyncOperations)
- [msdyn_pmprocesstemplate_AsyncOperations](#BKMK_msdyn_pmprocesstemplate_AsyncOperations)
- [msdyn_pmprocessusersettings_AsyncOperations](#BKMK_msdyn_pmprocessusersettings_AsyncOperations)
- [msdyn_pmprocessversion_AsyncOperations](#BKMK_msdyn_pmprocessversion_AsyncOperations)
- [msdyn_pmrecording_AsyncOperations](#BKMK_msdyn_pmrecording_AsyncOperations)
- [msdyn_pmsimulation_AsyncOperations](#BKMK_msdyn_pmsimulation_AsyncOperations)
- [msdyn_pmtemplate_AsyncOperations](#BKMK_msdyn_pmtemplate_AsyncOperations)
- [msdyn_pmview_AsyncOperations](#BKMK_msdyn_pmview_AsyncOperations)
- [msdyn_qna_AsyncOperations](#BKMK_msdyn_qna_AsyncOperations)
- [msdyn_richtextfile_AsyncOperations](#BKMK_msdyn_richtextfile_AsyncOperations)
- [msdyn_salesforcestructuredobject_AsyncOperations](#BKMK_msdyn_salesforcestructuredobject_AsyncOperations)
- [msdyn_salesforcestructuredqnaconfig_AsyncOperations](#BKMK_msdyn_salesforcestructuredqnaconfig_AsyncOperations)
- [msdyn_schedule_AsyncOperations](#BKMK_msdyn_schedule_AsyncOperations)
- [msdyn_serviceconfiguration_AsyncOperations](#BKMK_msdyn_serviceconfiguration_AsyncOperations)
- [msdyn_slakpi_AsyncOperations](#BKMK_msdyn_slakpi_AsyncOperations)
- [msdyn_solutionhealthrule_AsyncOperations](#BKMK_msdyn_solutionhealthrule_AsyncOperations)
- [msdyn_solutionhealthruleargument_AsyncOperations](#BKMK_msdyn_solutionhealthruleargument_AsyncOperations)
- [msdyn_solutionhealthruleset_AsyncOperations](#BKMK_msdyn_solutionhealthruleset_AsyncOperations)
- [msdyn_tour_AsyncOperations](#BKMK_msdyn_tour_AsyncOperations)
- [msdyn_virtualtablecolumncandidate_AsyncOperations](#BKMK_msdyn_virtualtablecolumncandidate_AsyncOperations)
- [msdyn_workflowactionstatus_AsyncOperations](#BKMK_msdyn_workflowactionstatus_AsyncOperations)
- [msdynce_botcontent_AsyncOperations](#BKMK_msdynce_botcontent_AsyncOperations)
- [msgraphresourcetosubscription_AsyncOperations](#BKMK_msgraphresourcetosubscription_AsyncOperations)
- [mspcat_catalogsubmissionfiles_AsyncOperations](#BKMK_mspcat_catalogsubmissionfiles_AsyncOperations)
- [mspcat_packagestore_AsyncOperations](#BKMK_mspcat_packagestore_AsyncOperations)
- [Organization_AsyncOperations](#BKMK_Organization_AsyncOperations)
- [organizationdatasyncfnostate_AsyncOperations](#BKMK_organizationdatasyncfnostate_AsyncOperations)
- [organizationdatasyncstate_AsyncOperations](#BKMK_organizationdatasyncstate_AsyncOperations)
- [organizationdatasyncsubscription_AsyncOperations](#BKMK_organizationdatasyncsubscription_AsyncOperations)
- [organizationdatasyncsubscriptionentity_AsyncOperations](#BKMK_organizationdatasyncsubscriptionentity_AsyncOperations)
- [organizationdatasyncsubscriptionfnotable_AsyncOperations](#BKMK_organizationdatasyncsubscriptionfnotable_AsyncOperations)
- [owner_asyncoperations](#BKMK_owner_asyncoperations)
- [package_AsyncOperations](#BKMK_package_AsyncOperations)
- [packagehistory_AsyncOperations](#BKMK_packagehistory_AsyncOperations)
- [PhoneCall_AsyncOperations](#BKMK_PhoneCall_AsyncOperations)
- [plannerbusinessscenario_AsyncOperations](#BKMK_plannerbusinessscenario_AsyncOperations)
- [plannersyncaction_AsyncOperations](#BKMK_plannersyncaction_AsyncOperations)
- [plugin_AsyncOperations](#BKMK_plugin_AsyncOperations)
- [pluginpackage_AsyncOperations](#BKMK_pluginpackage_AsyncOperations)
- [position_AsyncOperations](#BKMK_position_AsyncOperations)
- [post_AsyncOperations](#BKMK_post_AsyncOperations)
- [PostFollow_AsyncOperations](#BKMK_PostFollow_AsyncOperations)
- [powerbidataset_AsyncOperations](#BKMK_powerbidataset_AsyncOperations)
- [powerbidatasetapdx_AsyncOperations](#BKMK_powerbidatasetapdx_AsyncOperations)
- [powerbimashupparameter_AsyncOperations](#BKMK_powerbimashupparameter_AsyncOperations)
- [powerbireport_AsyncOperations](#BKMK_powerbireport_AsyncOperations)
- [powerbireportapdx_AsyncOperations](#BKMK_powerbireportapdx_AsyncOperations)
- [powerfxrule_AsyncOperations](#BKMK_powerfxrule_AsyncOperations)
- [powerpagecomponent_AsyncOperations](#BKMK_powerpagecomponent_AsyncOperations)
- [powerpagesite_AsyncOperations](#BKMK_powerpagesite_AsyncOperations)
- [powerpagesitelanguage_AsyncOperations](#BKMK_powerpagesitelanguage_AsyncOperations)
- [powerpagesitepublished_AsyncOperations](#BKMK_powerpagesitepublished_AsyncOperations)
- [powerpagesmanagedidentity_AsyncOperations](#BKMK_powerpagesmanagedidentity_AsyncOperations)
- [powerpagesscanreport_AsyncOperations](#BKMK_powerpagesscanreport_AsyncOperations)
- [Privilege_AsyncOperations](#BKMK_Privilege_AsyncOperations)
- [privilegecheckerlog_AsyncOperations](#BKMK_privilegecheckerlog_AsyncOperations)
- [privilegecheckerrun_AsyncOperations](#BKMK_privilegecheckerrun_AsyncOperations)
- [privilegesremovalsetting_AsyncOperations](#BKMK_privilegesremovalsetting_AsyncOperations)
- [processstageparameter_AsyncOperations](#BKMK_processstageparameter_AsyncOperations)
- [provisionlanguageforuser_AsyncOperations](#BKMK_provisionlanguageforuser_AsyncOperations)
- [QuarterlyFiscalCalendar_AsyncOperations](#BKMK_QuarterlyFiscalCalendar_AsyncOperations)
- [Queue_AsyncOperations](#BKMK_Queue_AsyncOperations)
- [QueueItem_AsyncOperations](#BKMK_QueueItem_AsyncOperations)
- [recordfilter_AsyncOperations](#BKMK_recordfilter_AsyncOperations)
- [RecurringAppointmentMaster_AsyncOperations](#BKMK_RecurringAppointmentMaster_AsyncOperations)
- [recyclebinconfig_AsyncOperations](#BKMK_recyclebinconfig_AsyncOperations)
- [relationshipattribute_AsyncOperations](#BKMK_relationshipattribute_AsyncOperations)
- [Report_AsyncOperations](#BKMK_Report_AsyncOperations)
- [reportparameter_AsyncOperations](#BKMK_reportparameter_AsyncOperations)
- [retaineddataexcel_AsyncOperations](#BKMK_retaineddataexcel_AsyncOperations)
- [retentionconfig_AsyncOperations](#BKMK_retentionconfig_AsyncOperations)
- [retentionfailuredetail_AsyncOperations](#BKMK_retentionfailuredetail_AsyncOperations)
- [retentionoperation_AsyncOperations](#BKMK_retentionoperation_AsyncOperations)
- [retentionoperationdetail_AsyncOperations](#BKMK_retentionoperationdetail_AsyncOperations)
- [retentionsuccessdetail_AsyncOperations](#BKMK_retentionsuccessdetail_AsyncOperations)
- [Role_AsyncOperations](#BKMK_Role_AsyncOperations)
- [roleeditorlayout_AsyncOperations](#BKMK_roleeditorlayout_AsyncOperations)
- [rollupfield_AsyncOperations](#BKMK_rollupfield_AsyncOperations)
- [SavedQuery_AsyncOperations](#BKMK_SavedQuery_AsyncOperations)
- [savingrule_AsyncOperations](#BKMK_savingrule_AsyncOperations)
- [SdkMessageProcessingStep_AsyncOperations](#BKMK_SdkMessageProcessingStep_AsyncOperations)
- [searchattributesettings_AsyncOperations](#BKMK_searchattributesettings_AsyncOperations)
- [searchcustomanalyzer_AsyncOperations](#BKMK_searchcustomanalyzer_AsyncOperations)
- [searchrelationshipsettings_AsyncOperations](#BKMK_searchrelationshipsettings_AsyncOperations)
- [SemiAnnualFiscalCalendar_AsyncOperations](#BKMK_SemiAnnualFiscalCalendar_AsyncOperations)
- [serviceplan_AsyncOperations](#BKMK_serviceplan_AsyncOperations)
- [serviceplanmapping_AsyncOperations](#BKMK_serviceplanmapping_AsyncOperations)
- [sharedlinksetting_AsyncOperations](#BKMK_sharedlinksetting_AsyncOperations)
- [sharedobject_AsyncOperations](#BKMK_sharedobject_AsyncOperations)
- [sharedworkspace_AsyncOperations](#BKMK_sharedworkspace_AsyncOperations)
- [sharedworkspacepool_AsyncOperations](#BKMK_sharedworkspacepool_AsyncOperations)
- [SharePointDocumentLocation_AsyncOperations](#BKMK_SharePointDocumentLocation_AsyncOperations)
- [sharepointmanagedidentity_AsyncOperations](#BKMK_sharepointmanagedidentity_AsyncOperations)
- [SharePointSite_AsyncOperations](#BKMK_SharePointSite_AsyncOperations)
- [sideloadedaiplugin_AsyncOperations](#BKMK_sideloadedaiplugin_AsyncOperations)
- [similarityrule_AsyncOperations](#BKMK_similarityrule_AsyncOperations)
- [slabase_AsyncOperations](#BKMK_slabase_AsyncOperations)
- [SocialActivity_AsyncOperations](#BKMK_SocialActivity_AsyncOperations)
- [SocialProfile_AsyncOperations](#BKMK_SocialProfile_AsyncOperations)
- [solutioncomponentattributeconfiguration_AsyncOperations](#BKMK_solutioncomponentattributeconfiguration_AsyncOperations)
- [solutioncomponentbatchconfiguration_AsyncOperations](#BKMK_solutioncomponentbatchconfiguration_AsyncOperations)
- [solutioncomponentconfiguration_AsyncOperations](#BKMK_solutioncomponentconfiguration_AsyncOperations)
- [solutioncomponentrelationshipconfiguration_AsyncOperations](#BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations)
- [stagedentity_AsyncOperations](#BKMK_stagedentity_AsyncOperations)
- [stagedentityattribute_AsyncOperations](#BKMK_stagedentityattribute_AsyncOperations)
- [stagedmetadataasyncoperation_AsyncOperations](#BKMK_stagedmetadataasyncoperation_AsyncOperations)
- [stagesolutionupload_AsyncOperations](#BKMK_stagesolutionupload_AsyncOperations)
- [Subject_AsyncOperations](#BKMK_Subject_AsyncOperations)
- [supportusertable_AsyncOperations](#BKMK_supportusertable_AsyncOperations)
- [synapsedatabase_AsyncOperations](#BKMK_synapsedatabase_AsyncOperations)
- [synapselinkexternaltablestate_AsyncOperations](#BKMK_synapselinkexternaltablestate_AsyncOperations)
- [synapselinkprofile_AsyncOperations](#BKMK_synapselinkprofile_AsyncOperations)
- [synapselinkprofileentity_AsyncOperations](#BKMK_synapselinkprofileentity_AsyncOperations)
- [synapselinkprofileentitystate_AsyncOperations](#BKMK_synapselinkprofileentitystate_AsyncOperations)
- [synapselinkschedule_AsyncOperations](#BKMK_synapselinkschedule_AsyncOperations)
- [system_user_asyncoperation](#BKMK_system_user_asyncoperation)
- [SystemForm_AsyncOperations](#BKMK_SystemForm_AsyncOperations)
- [SystemUser_AsyncOperations](#BKMK_SystemUser_AsyncOperations)
- [systemuserauthorizationchangetracker_AsyncOperations](#BKMK_systemuserauthorizationchangetracker_AsyncOperations)
- [tag_AsyncOperations](#BKMK_tag_AsyncOperations)
- [taggedflowsession_AsyncOperations](#BKMK_taggedflowsession_AsyncOperations)
- [taggedprocess_AsyncOperations](#BKMK_taggedprocess_AsyncOperations)
- [Task_AsyncOperations](#BKMK_Task_AsyncOperations)
- [team_asyncoperation](#BKMK_team_asyncoperation)
- [Team_AsyncOperations](#BKMK_Team_AsyncOperations)
- [teammobileofflineprofilemembership_AsyncOperations](#BKMK_teammobileofflineprofilemembership_AsyncOperations)
- [Template_AsyncOperations](#BKMK_Template_AsyncOperations)
- [Territory_AsyncOperations](#BKMK_Territory_AsyncOperations)
- [theme_AsyncOperations](#BKMK_theme_AsyncOperations)
- [TransactionCurrency_AsyncOperations](#BKMK_TransactionCurrency_AsyncOperations)
- [unstructuredfilesearchentity_AsyncOperations](#BKMK_unstructuredfilesearchentity_AsyncOperations)
- [unstructuredfilesearchrecord_AsyncOperations](#BKMK_unstructuredfilesearchrecord_AsyncOperations)
- [UserForm_AsyncOperations](#BKMK_UserForm_AsyncOperations)
- [usermapping_AsyncOperations](#BKMK_usermapping_AsyncOperations)
- [usermobileofflineprofilemembership_AsyncOperations](#BKMK_usermobileofflineprofilemembership_AsyncOperations)
- [UserQuery_AsyncOperations](#BKMK_UserQuery_AsyncOperations)
- [userrating_AsyncOperations](#BKMK_userrating_AsyncOperations)
- [viewasexamplequestion_AsyncOperations](#BKMK_viewasexamplequestion_AsyncOperations)
- [virtualentitymetadata_AsyncOperations](#BKMK_virtualentitymetadata_AsyncOperations)
- [workflowbinary_AsyncOperations](#BKMK_workflowbinary_AsyncOperations)
- [workflowmetadata_AsyncOperations](#BKMK_workflowmetadata_AsyncOperations)
- [workqueue_AsyncOperations](#BKMK_workqueue_AsyncOperations)
- [workqueueitem_AsyncOperations](#BKMK_workqueueitem_AsyncOperations)

### <a name="BKMK_Account_AsyncOperations"></a> Account_AsyncOperations

One-To-Many Relationship: [account Account_AsyncOperations](account.md#BKMK_Account_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activityfileattachment_AsyncOperations"></a> activityfileattachment_AsyncOperations

One-To-Many Relationship: [activityfileattachment activityfileattachment_AsyncOperations](activityfileattachment.md#BKMK_activityfileattachment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`activityfileattachment`|
|ReferencedAttribute|`activityfileattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_activityfileattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ActivityMimeAttachment_AsyncOperations"></a> ActivityMimeAttachment_AsyncOperations

One-To-Many Relationship: [activitymimeattachment ActivityMimeAttachment_AsyncOperations](activitymimeattachment.md#BKMK_ActivityMimeAttachment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`activitymimeattachment`|
|ReferencedAttribute|`activitymimeattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_activitymimeattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ActivityPointer_AsyncOperations"></a> ActivityPointer_AsyncOperations

One-To-Many Relationship: [activitypointer ActivityPointer_AsyncOperations](activitypointer.md#BKMK_ActivityPointer_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_externalidentity_AsyncOperations"></a> adx_externalidentity_AsyncOperations

One-To-Many Relationship: [adx_externalidentity adx_externalidentity_AsyncOperations](adx_externalidentity.md#BKMK_adx_externalidentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_externalidentity`|
|ReferencedAttribute|`adx_externalidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_externalidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_AsyncOperations"></a> adx_invitation_AsyncOperations

One-To-Many Relationship: [adx_invitation adx_invitation_AsyncOperations](adx_invitation.md#BKMK_adx_invitation_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_invitation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_AsyncOperations"></a> adx_inviteredemption_AsyncOperations

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_AsyncOperations](adx_inviteredemption.md#BKMK_adx_inviteredemption_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_portalcomment_AsyncOperations"></a> adx_portalcomment_AsyncOperations

One-To-Many Relationship: [adx_portalcomment adx_portalcomment_AsyncOperations](adx_portalcomment.md#BKMK_adx_portalcomment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_portalcomment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_portalcomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_setting_AsyncOperations"></a> adx_setting_AsyncOperations

One-To-Many Relationship: [adx_setting adx_setting_AsyncOperations](adx_setting.md#BKMK_adx_setting_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_setting`|
|ReferencedAttribute|`adx_settingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_setting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_webformsession_AsyncOperations"></a> adx_webformsession_AsyncOperations

One-To-Many Relationship: [adx_webformsession adx_webformsession_AsyncOperations](adx_webformsession.md#BKMK_adx_webformsession_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_webformsession`|
|ReferencedAttribute|`adx_webformsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_webformsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aicopilot_AsyncOperations"></a> aicopilot_AsyncOperations

One-To-Many Relationship: [aicopilot aicopilot_AsyncOperations](aicopilot.md#BKMK_aicopilot_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aicopilot`|
|ReferencedAttribute|`aicopilotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aicopilot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugin_AsyncOperations"></a> aiplugin_AsyncOperations

One-To-Many Relationship: [aiplugin aiplugin_AsyncOperations](aiplugin.md#BKMK_aiplugin_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugin`|
|ReferencedAttribute|`aipluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginauth_AsyncOperations"></a> aipluginauth_AsyncOperations

One-To-Many Relationship: [aipluginauth aipluginauth_AsyncOperations](aipluginauth.md#BKMK_aipluginauth_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginauth`|
|ReferencedAttribute|`aipluginauthid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginauth`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstarter_AsyncOperations"></a> aipluginconversationstarter_AsyncOperations

One-To-Many Relationship: [aipluginconversationstarter aipluginconversationstarter_AsyncOperations](aipluginconversationstarter.md#BKMK_aipluginconversationstarter_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstarter`|
|ReferencedAttribute|`aipluginconversationstarterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginconversationstarter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstartermapping_AsyncOperations"></a> aipluginconversationstartermapping_AsyncOperations

One-To-Many Relationship: [aipluginconversationstartermapping aipluginconversationstartermapping_AsyncOperations](aipluginconversationstartermapping.md#BKMK_aipluginconversationstartermapping_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstartermapping`|
|ReferencedAttribute|`aipluginconversationstartermappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginconversationstartermapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschema_AsyncOperations"></a> aipluginexternalschema_AsyncOperations

One-To-Many Relationship: [aipluginexternalschema aipluginexternalschema_AsyncOperations](aipluginexternalschema.md#BKMK_aipluginexternalschema_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschema`|
|ReferencedAttribute|`aipluginexternalschemaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginexternalschema`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschemaproperty_AsyncOperations"></a> aipluginexternalschemaproperty_AsyncOperations

One-To-Many Relationship: [aipluginexternalschemaproperty aipluginexternalschemaproperty_AsyncOperations](aipluginexternalschemaproperty.md#BKMK_aipluginexternalschemaproperty_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschemaproperty`|
|ReferencedAttribute|`aipluginexternalschemapropertyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginexternalschemaproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernance_AsyncOperations"></a> aiplugingovernance_AsyncOperations

One-To-Many Relationship: [aiplugingovernance aiplugingovernance_AsyncOperations](aiplugingovernance.md#BKMK_aiplugingovernance_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernance`|
|ReferencedAttribute|`aiplugingovernanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugingovernance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernanceext_AsyncOperations"></a> aiplugingovernanceext_AsyncOperations

One-To-Many Relationship: [aiplugingovernanceext aiplugingovernanceext_AsyncOperations](aiplugingovernanceext.md#BKMK_aiplugingovernanceext_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernanceext`|
|ReferencedAttribute|`aiplugingovernanceextid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugingovernanceext`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugininstance_AsyncOperations"></a> aiplugininstance_AsyncOperations

One-To-Many Relationship: [aiplugininstance aiplugininstance_AsyncOperations](aiplugininstance.md#BKMK_aiplugininstance_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugininstance`|
|ReferencedAttribute|`aiplugininstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugininstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperation_AsyncOperations"></a> aipluginoperation_AsyncOperations

One-To-Many Relationship: [aipluginoperation aipluginoperation_AsyncOperations](aipluginoperation.md#BKMK_aipluginoperation_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperation`|
|ReferencedAttribute|`aipluginoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationparameter_AsyncOperations"></a> aipluginoperationparameter_AsyncOperations

One-To-Many Relationship: [aipluginoperationparameter aipluginoperationparameter_AsyncOperations](aipluginoperationparameter.md#BKMK_aipluginoperationparameter_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationparameter`|
|ReferencedAttribute|`aipluginoperationparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperationparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationresponsetemplate_AsyncOperations"></a> aipluginoperationresponsetemplate_AsyncOperations

One-To-Many Relationship: [aipluginoperationresponsetemplate aipluginoperationresponsetemplate_AsyncOperations](aipluginoperationresponsetemplate.md#BKMK_aipluginoperationresponsetemplate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationresponsetemplate`|
|ReferencedAttribute|`aipluginoperationresponsetemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperationresponsetemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugintitle_AsyncOperations"></a> aiplugintitle_AsyncOperations

One-To-Many Relationship: [aiplugintitle aiplugintitle_AsyncOperations](aiplugintitle.md#BKMK_aiplugintitle_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugintitle`|
|ReferencedAttribute|`aiplugintitleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugintitle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginusersetting_AsyncOperations"></a> aipluginusersetting_AsyncOperations

One-To-Many Relationship: [aipluginusersetting aipluginusersetting_AsyncOperations](aipluginusersetting.md#BKMK_aipluginusersetting_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginusersetting`|
|ReferencedAttribute|`aipluginusersettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginusersetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Annotation_AsyncOperations"></a> Annotation_AsyncOperations

One-To-Many Relationship: [annotation Annotation_AsyncOperations](annotation.md#BKMK_Annotation_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`annotation`|
|ReferencedAttribute|`annotationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_annotation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_AnnualFiscalCalendar_AsyncOperations"></a> AnnualFiscalCalendar_AsyncOperations

One-To-Many Relationship: [annualfiscalcalendar AnnualFiscalCalendar_AsyncOperations](annualfiscalcalendar.md#BKMK_AnnualFiscalCalendar_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`annualfiscalcalendar`|
|ReferencedAttribute|`userfiscalcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_annualfiscalcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appaction_AsyncOperations"></a> appaction_AsyncOperations

One-To-Many Relationship: [appaction appaction_AsyncOperations](appaction.md#BKMK_appaction_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`appaction`|
|ReferencedAttribute|`appactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionmigration_AsyncOperations"></a> appactionmigration_AsyncOperations

One-To-Many Relationship: [appactionmigration appactionmigration_AsyncOperations](appactionmigration.md#BKMK_appactionmigration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionmigration`|
|ReferencedAttribute|`appactionmigrationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appactionmigration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionrule_AsyncOperations"></a> appactionrule_AsyncOperations

One-To-Many Relationship: [appactionrule appactionrule_AsyncOperations](appactionrule.md#BKMK_appactionrule_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionrule`|
|ReferencedAttribute|`appactionruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appactionrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_application_AsyncOperations"></a> application_AsyncOperations

One-To-Many Relationship: [application application_AsyncOperations](application.md#BKMK_application_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`application`|
|ReferencedAttribute|`applicationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_application`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_applicationuser_AsyncOperations"></a> applicationuser_AsyncOperations

One-To-Many Relationship: [applicationuser applicationuser_AsyncOperations](applicationuser.md#BKMK_applicationuser_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`applicationuser`|
|ReferencedAttribute|`applicationuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_applicationuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Appointment_AsyncOperations"></a> Appointment_AsyncOperations

One-To-Many Relationship: [appointment Appointment_AsyncOperations](appointment.md#BKMK_Appointment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalprocess_AsyncOperations"></a> approvalprocess_AsyncOperations

One-To-Many Relationship: [approvalprocess approvalprocess_AsyncOperations](approvalprocess.md#BKMK_approvalprocess_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalprocess`|
|ReferencedAttribute|`approvalprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageapproval_AsyncOperations"></a> approvalstageapproval_AsyncOperations

One-To-Many Relationship: [approvalstageapproval approvalstageapproval_AsyncOperations](approvalstageapproval.md#BKMK_approvalstageapproval_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageapproval`|
|ReferencedAttribute|`approvalstageapprovalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstagecondition_AsyncOperations"></a> approvalstagecondition_AsyncOperations

One-To-Many Relationship: [approvalstagecondition approvalstagecondition_AsyncOperations](approvalstagecondition.md#BKMK_approvalstagecondition_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstagecondition`|
|ReferencedAttribute|`approvalstageconditionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstagecondition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_AsyncOperations"></a> approvalstageorder_AsyncOperations

One-To-Many Relationship: [approvalstageorder approvalstageorder_AsyncOperations](approvalstageorder.md#BKMK_approvalstageorder_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageorder`|
|ReferencedAttribute|`approvalstageorderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageorder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributeimageconfig_AsyncOperations"></a> attributeimageconfig_AsyncOperations

One-To-Many Relationship: [attributeimageconfig attributeimageconfig_AsyncOperations](attributeimageconfig.md#BKMK_attributeimageconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`attributeimageconfig`|
|ReferencedAttribute|`attributeimageconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributeimageconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributemaskingrule_AsyncOperations"></a> attributemaskingrule_AsyncOperations

One-To-Many Relationship: [attributemaskingrule attributemaskingrule_AsyncOperations](attributemaskingrule.md#BKMK_attributemaskingrule_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`attributemaskingrule`|
|ReferencedAttribute|`attributemaskingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributemaskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributepicklistvalue_AsyncOperations"></a> attributepicklistvalue_AsyncOperations

One-To-Many Relationship: [attributepicklistvalue attributepicklistvalue_AsyncOperations](attributepicklistvalue.md#BKMK_attributepicklistvalue_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`attributepicklistvalue`|
|ReferencedAttribute|`attributepicklistvalueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributepicklistvalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_bot_AsyncOperations"></a> bot_AsyncOperations

One-To-Many Relationship: [bot bot_AsyncOperations](bot.md#BKMK_bot_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`bot`|
|ReferencedAttribute|`botid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_bot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponent_AsyncOperations"></a> botcomponent_AsyncOperations

One-To-Many Relationship: [botcomponent botcomponent_AsyncOperations](botcomponent.md#BKMK_botcomponent_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponent`|
|ReferencedAttribute|`botcomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_botcomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponentcollection_AsyncOperations"></a> botcomponentcollection_AsyncOperations

One-To-Many Relationship: [botcomponentcollection botcomponentcollection_AsyncOperations](botcomponentcollection.md#BKMK_botcomponentcollection_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponentcollection`|
|ReferencedAttribute|`botcomponentcollectionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_botcomponentcollection`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_business_unit_asyncoperation"></a> business_unit_asyncoperation

One-To-Many Relationship: [businessunit business_unit_asyncoperation](businessunit.md#BKMK_business_unit_asyncoperation)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_businessprocess_AsyncOperations"></a> businessprocess_AsyncOperations

One-To-Many Relationship: [businessprocess businessprocess_AsyncOperations](businessprocess.md#BKMK_businessprocess_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`businessprocess`|
|ReferencedAttribute|`businessprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_BusinessUnit_AsyncOperations"></a> BusinessUnit_AsyncOperations

One-To-Many Relationship: [businessunit BusinessUnit_AsyncOperations](businessunit.md#BKMK_BusinessUnit_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_BusinessUnitNewsArticle_AsyncOperations"></a> BusinessUnitNewsArticle_AsyncOperations

One-To-Many Relationship: [businessunitnewsarticle BusinessUnitNewsArticle_AsyncOperations](businessunitnewsarticle.md#BKMK_BusinessUnitNewsArticle_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunitnewsarticle`|
|ReferencedAttribute|`businessunitnewsarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessunitnewsarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Calendar_AsyncOperations"></a> Calendar_AsyncOperations

One-To-Many Relationship: [calendar Calendar_AsyncOperations](calendar.md#BKMK_Calendar_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`calendar`|
|ReferencedAttribute|`calendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_calendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_card_AsyncOperations"></a> card_AsyncOperations

One-To-Many Relationship: [card card_AsyncOperations](card.md#BKMK_card_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`card`|
|ReferencedAttribute|`cardid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_card`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalog_AsyncOperations"></a> catalog_AsyncOperations

One-To-Many Relationship: [catalog catalog_AsyncOperations](catalog.md#BKMK_catalog_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`catalog`|
|ReferencedAttribute|`catalogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_catalog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalogassignment_AsyncOperations"></a> catalogassignment_AsyncOperations

One-To-Many Relationship: [catalogassignment catalogassignment_AsyncOperations](catalogassignment.md#BKMK_catalogassignment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`catalogassignment`|
|ReferencedAttribute|`catalogassignmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_catalogassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_certificatecredential_AsyncOperations"></a> certificatecredential_AsyncOperations

One-To-Many Relationship: [certificatecredential certificatecredential_AsyncOperations](certificatecredential.md#BKMK_certificatecredential_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`certificatecredential`|
|ReferencedAttribute|`certificatecredentialid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_certificatecredential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_chat_AsyncOperations"></a> chat_AsyncOperations

One-To-Many Relationship: [chat chat_AsyncOperations](chat.md#BKMK_chat_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`chat`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_chat`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Connection_AsyncOperations"></a> Connection_AsyncOperations

One-To-Many Relationship: [connection Connection_AsyncOperations](connection.md#BKMK_Connection_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`connection`|
|ReferencedAttribute|`connectionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connection`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Connection_Role_AsyncOperations"></a> Connection_Role_AsyncOperations

One-To-Many Relationship: [connectionrole Connection_Role_AsyncOperations](connectionrole.md#BKMK_Connection_Role_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionrole`|
|ReferencedAttribute|`connectionroleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectionrole`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectioninstance_AsyncOperations"></a> connectioninstance_AsyncOperations

One-To-Many Relationship: [connectioninstance connectioninstance_AsyncOperations](connectioninstance.md#BKMK_connectioninstance_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`connectioninstance`|
|ReferencedAttribute|`connectioninstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectioninstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectionreference_AsyncOperations"></a> connectionreference_AsyncOperations

One-To-Many Relationship: [connectionreference connectionreference_AsyncOperations](connectionreference.md#BKMK_connectionreference_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionreference`|
|ReferencedAttribute|`connectionreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connector_AsyncOperations"></a> connector_AsyncOperations

One-To-Many Relationship: [connector connector_AsyncOperations](connector.md#BKMK_connector_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`connector`|
|ReferencedAttribute|`connectorid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connector`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_AsyncOperations"></a> Contact_AsyncOperations

One-To-Many Relationship: [contact Contact_AsyncOperations](contact.md#BKMK_Contact_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_conversationtranscript_AsyncOperations"></a> conversationtranscript_AsyncOperations

One-To-Many Relationship: [conversationtranscript conversationtranscript_AsyncOperations](conversationtranscript.md#BKMK_conversationtranscript_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`conversationtranscript`|
|ReferencedAttribute|`conversationtranscriptid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_conversationtranscript`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotexamplequestion_AsyncOperations"></a> copilotexamplequestion_AsyncOperations

One-To-Many Relationship: [copilotexamplequestion copilotexamplequestion_AsyncOperations](copilotexamplequestion.md#BKMK_copilotexamplequestion_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotexamplequestion`|
|ReferencedAttribute|`copilotexamplequestionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotglossaryterm_AsyncOperations"></a> copilotglossaryterm_AsyncOperations

One-To-Many Relationship: [copilotglossaryterm copilotglossaryterm_AsyncOperations](copilotglossaryterm.md#BKMK_copilotglossaryterm_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotglossaryterm`|
|ReferencedAttribute|`copilotglossarytermid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotglossaryterm`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotsynonyms_AsyncOperations"></a> copilotsynonyms_AsyncOperations

One-To-Many Relationship: [copilotsynonyms copilotsynonyms_AsyncOperations](copilotsynonyms.md#BKMK_copilotsynonyms_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotsynonyms`|
|ReferencedAttribute|`copilotsynonymsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotsynonyms`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_credential_AsyncOperations"></a> credential_AsyncOperations

One-To-Many Relationship: [credential credential_AsyncOperations](credential.md#BKMK_credential_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`credential`|
|ReferencedAttribute|`credentialid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_credential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapi_AsyncOperations"></a> customapi_AsyncOperations

One-To-Many Relationship: [customapi customapi_AsyncOperations](customapi.md#BKMK_customapi_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`customapi`|
|ReferencedAttribute|`customapiid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapirequestparameter_AsyncOperations"></a> customapirequestparameter_AsyncOperations

One-To-Many Relationship: [customapirequestparameter customapirequestparameter_AsyncOperations](customapirequestparameter.md#BKMK_customapirequestparameter_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`customapirequestparameter`|
|ReferencedAttribute|`customapirequestparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapirequestparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapiresponseproperty_AsyncOperations"></a> customapiresponseproperty_AsyncOperations

One-To-Many Relationship: [customapiresponseproperty customapiresponseproperty_AsyncOperations](customapiresponseproperty.md#BKMK_customapiresponseproperty_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`customapiresponseproperty`|
|ReferencedAttribute|`customapiresponsepropertyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapiresponseproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_CustomerAddress_AsyncOperations"></a> CustomerAddress_AsyncOperations

One-To-Many Relationship: [customeraddress CustomerAddress_AsyncOperations](customeraddress.md#BKMK_CustomerAddress_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`customeraddress`|
|ReferencedAttribute|`customeraddressid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customeraddress`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolder_AsyncOperations"></a> datalakefolder_AsyncOperations

One-To-Many Relationship: [datalakefolder datalakefolder_AsyncOperations](datalakefolder.md#BKMK_datalakefolder_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolder`|
|ReferencedAttribute|`datalakefolderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolderpermission_AsyncOperations"></a> datalakefolderpermission_AsyncOperations

One-To-Many Relationship: [datalakefolderpermission datalakefolderpermission_AsyncOperations](datalakefolderpermission.md#BKMK_datalakefolderpermission_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolderpermission`|
|ReferencedAttribute|`datalakefolderpermissionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakefolderpermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspace_AsyncOperations"></a> datalakeworkspace_AsyncOperations

One-To-Many Relationship: [datalakeworkspace datalakeworkspace_AsyncOperations](datalakeworkspace.md#BKMK_datalakeworkspace_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspace`|
|ReferencedAttribute|`datalakeworkspaceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakeworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspacepermission_AsyncOperations"></a> datalakeworkspacepermission_AsyncOperations

One-To-Many Relationship: [datalakeworkspacepermission datalakeworkspacepermission_AsyncOperations](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspacepermission`|
|ReferencedAttribute|`datalakeworkspacepermissionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakeworkspacepermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dataprocessingconfiguration_AsyncOperations"></a> dataprocessingconfiguration_AsyncOperations

One-To-Many Relationship: [dataprocessingconfiguration dataprocessingconfiguration_AsyncOperations](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`dataprocessingconfiguration`|
|ReferencedAttribute|`dataprocessingconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dataprocessingconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_delegatedauthorization_AsyncOperations"></a> delegatedauthorization_AsyncOperations

One-To-Many Relationship: [delegatedauthorization delegatedauthorization_AsyncOperations](delegatedauthorization.md#BKMK_delegatedauthorization_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`delegatedauthorization`|
|ReferencedAttribute|`delegatedauthorizationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_delegatedauthorization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowbinary_AsyncOperations"></a> desktopflowbinary_AsyncOperations

One-To-Many Relationship: [desktopflowbinary desktopflowbinary_AsyncOperations](desktopflowbinary.md#BKMK_desktopflowbinary_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowbinary`|
|ReferencedAttribute|`desktopflowbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_desktopflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowmodule_AsyncOperations"></a> desktopflowmodule_AsyncOperations

One-To-Many Relationship: [desktopflowmodule desktopflowmodule_AsyncOperations](desktopflowmodule.md#BKMK_desktopflowmodule_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowmodule`|
|ReferencedAttribute|`desktopflowmoduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_desktopflowmodule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_DisplayString_AsyncOperations"></a> DisplayString_AsyncOperations

One-To-Many Relationship: [displaystring DisplayString_AsyncOperations](displaystring.md#BKMK_DisplayString_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`displaystring`|
|ReferencedAttribute|`displaystringid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_displaystring`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearch_AsyncOperations"></a> dvfilesearch_AsyncOperations

One-To-Many Relationship: [dvfilesearch dvfilesearch_AsyncOperations](dvfilesearch.md#BKMK_dvfilesearch_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearch`|
|ReferencedAttribute|`dvfilesearchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchattribute_AsyncOperations"></a> dvfilesearchattribute_AsyncOperations

One-To-Many Relationship: [dvfilesearchattribute dvfilesearchattribute_AsyncOperations](dvfilesearchattribute.md#BKMK_dvfilesearchattribute_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchattribute`|
|ReferencedAttribute|`dvfilesearchattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchentity_AsyncOperations"></a> dvfilesearchentity_AsyncOperations

One-To-Many Relationship: [dvfilesearchentity dvfilesearchentity_AsyncOperations](dvfilesearchentity.md#BKMK_dvfilesearchentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchentity`|
|ReferencedAttribute|`dvfilesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearch_AsyncOperations"></a> dvtablesearch_AsyncOperations

One-To-Many Relationship: [dvtablesearch dvtablesearch_AsyncOperations](dvtablesearch.md#BKMK_dvtablesearch_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearch`|
|ReferencedAttribute|`dvtablesearchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchattribute_AsyncOperations"></a> dvtablesearchattribute_AsyncOperations

One-To-Many Relationship: [dvtablesearchattribute dvtablesearchattribute_AsyncOperations](dvtablesearchattribute.md#BKMK_dvtablesearchattribute_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchattribute`|
|ReferencedAttribute|`dvtablesearchattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchentity_AsyncOperations"></a> dvtablesearchentity_AsyncOperations

One-To-Many Relationship: [dvtablesearchentity dvtablesearchentity_AsyncOperations](dvtablesearchentity.md#BKMK_dvtablesearchentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchentity`|
|ReferencedAttribute|`dvtablesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Email_AsyncOperations"></a> Email_AsyncOperations

One-To-Many Relationship: [email Email_AsyncOperations](email.md#BKMK_Email_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_emailaddressconfiguration_AsyncOperations"></a> emailaddressconfiguration_AsyncOperations

One-To-Many Relationship: [emailaddressconfiguration emailaddressconfiguration_AsyncOperations](emailaddressconfiguration.md#BKMK_emailaddressconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`emailaddressconfiguration`|
|ReferencedAttribute|`emailaddressconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_emailaddressconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_emailserverprofile_asyncoperations"></a> emailserverprofile_asyncoperations

One-To-Many Relationship: [emailserverprofile emailserverprofile_asyncoperations](emailserverprofile.md#BKMK_emailserverprofile_asyncoperations)

|Property|Value|
|---|---|
|ReferencedEntity|`emailserverprofile`|
|ReferencedAttribute|`emailserverprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_emailserverprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityanalyticsconfig_AsyncOperations"></a> entityanalyticsconfig_AsyncOperations

One-To-Many Relationship: [entityanalyticsconfig entityanalyticsconfig_AsyncOperations](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`entityanalyticsconfig`|
|ReferencedAttribute|`entityanalyticsconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityanalyticsconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityclusterconfig_AsyncOperations"></a> entityclusterconfig_AsyncOperations

One-To-Many Relationship: [entityclusterconfig entityclusterconfig_AsyncOperations](entityclusterconfig.md#BKMK_entityclusterconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`entityclusterconfig`|
|ReferencedAttribute|`entityclusterconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityclusterconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityimageconfig_AsyncOperations"></a> entityimageconfig_AsyncOperations

One-To-Many Relationship: [entityimageconfig entityimageconfig_AsyncOperations](entityimageconfig.md#BKMK_entityimageconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`entityimageconfig`|
|ReferencedAttribute|`entityimageconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityimageconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityindex_AsyncOperations"></a> entityindex_AsyncOperations

One-To-Many Relationship: [entityindex entityindex_AsyncOperations](entityindex.md#BKMK_entityindex_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`entityindex`|
|ReferencedAttribute|`indexid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityindex`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityrecordfilter_AsyncOperations"></a> entityrecordfilter_AsyncOperations

One-To-Many Relationship: [entityrecordfilter entityrecordfilter_AsyncOperations](entityrecordfilter.md#BKMK_entityrecordfilter_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`entityrecordfilter`|
|ReferencedAttribute|`entityrecordfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityrecordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_AsyncOperations"></a> environmentvariabledefinition_AsyncOperations

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_AsyncOperations](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_environmentvariabledefinition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariablevalue_AsyncOperations"></a> environmentvariablevalue_AsyncOperations

One-To-Many Relationship: [environmentvariablevalue environmentvariablevalue_AsyncOperations](environmentvariablevalue.md#BKMK_environmentvariablevalue_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariablevalue`|
|ReferencedAttribute|`environmentvariablevalueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_environmentvariablevalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportedexcel_AsyncOperations"></a> exportedexcel_AsyncOperations

One-To-Many Relationship: [exportedexcel exportedexcel_AsyncOperations](exportedexcel.md#BKMK_exportedexcel_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`exportedexcel`|
|ReferencedAttribute|`exportedexcelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_exportedexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportsolutionupload_AsyncOperations"></a> exportsolutionupload_AsyncOperations

One-To-Many Relationship: [exportsolutionupload exportsolutionupload_AsyncOperations](exportsolutionupload.md#BKMK_exportsolutionupload_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`exportsolutionupload`|
|ReferencedAttribute|`exportsolutionuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_exportsolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fabricaiskill_AsyncOperations"></a> fabricaiskill_AsyncOperations

One-To-Many Relationship: [fabricaiskill fabricaiskill_AsyncOperations](fabricaiskill.md#BKMK_fabricaiskill_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`fabricaiskill`|
|ReferencedAttribute|`fabricaiskillid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fabricaiskill`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Fax_AsyncOperations"></a> Fax_AsyncOperations

One-To-Many Relationship: [fax Fax_AsyncOperations](fax.md#BKMK_Fax_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fax`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_featurecontrolsetting_AsyncOperations"></a> featurecontrolsetting_AsyncOperations

One-To-Many Relationship: [featurecontrolsetting featurecontrolsetting_AsyncOperations](featurecontrolsetting.md#BKMK_featurecontrolsetting_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`featurecontrolsetting`|
|ReferencedAttribute|`featurecontrolsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_featurecontrolsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeconfiguration_AsyncOperations"></a> federatedknowledgeconfiguration_AsyncOperations

One-To-Many Relationship: [federatedknowledgeconfiguration federatedknowledgeconfiguration_AsyncOperations](federatedknowledgeconfiguration.md#BKMK_federatedknowledgeconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeconfiguration`|
|ReferencedAttribute|`federatedknowledgeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_federatedknowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeentityconfiguration_AsyncOperations"></a> federatedknowledgeentityconfiguration_AsyncOperations

One-To-Many Relationship: [federatedknowledgeentityconfiguration federatedknowledgeentityconfiguration_AsyncOperations](federatedknowledgeentityconfiguration.md#BKMK_federatedknowledgeentityconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeentityconfiguration`|
|ReferencedAttribute|`federatedknowledgeentityconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_federatedknowledgeentityconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_AsyncOperation_DataBlobId"></a> FileAttachment_AsyncOperation_DataBlobId

One-To-Many Relationship: [fileattachment FileAttachment_AsyncOperation_DataBlobId](fileattachment.md#BKMK_FileAttachment_AsyncOperation_DataBlobId)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`datablobid`|
|ReferencingEntityNavigationPropertyName|`datablobid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FixedMonthlyFiscalCalendar_AsyncOperations"></a> FixedMonthlyFiscalCalendar_AsyncOperations

One-To-Many Relationship: [fixedmonthlyfiscalcalendar FixedMonthlyFiscalCalendar_AsyncOperations](fixedmonthlyfiscalcalendar.md#BKMK_FixedMonthlyFiscalCalendar_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`fixedmonthlyfiscalcalendar`|
|ReferencedAttribute|`userfiscalcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fixedmonthlyfiscalcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcapacityassignment_AsyncOperations"></a> flowcapacityassignment_AsyncOperations

One-To-Many Relationship: [flowcapacityassignment flowcapacityassignment_AsyncOperations](flowcapacityassignment.md#BKMK_flowcapacityassignment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcapacityassignment`|
|ReferencedAttribute|`flowcapacityassignmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowcapacityassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcredentialapplication_AsyncOperations"></a> flowcredentialapplication_AsyncOperations

One-To-Many Relationship: [flowcredentialapplication flowcredentialapplication_AsyncOperations](flowcredentialapplication.md#BKMK_flowcredentialapplication_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcredentialapplication`|
|ReferencedAttribute|`flowcredentialapplicationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowcredentialapplication`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowevent_AsyncOperations"></a> flowevent_AsyncOperations

One-To-Many Relationship: [flowevent flowevent_AsyncOperations](flowevent.md#BKMK_flowevent_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`flowevent`|
|ReferencedAttribute|`floweventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachine_AsyncOperations"></a> flowmachine_AsyncOperations

One-To-Many Relationship: [flowmachine flowmachine_AsyncOperations](flowmachine.md#BKMK_flowmachine_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachine`|
|ReferencedAttribute|`flowmachineid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachine`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_AsyncOperations"></a> flowmachinegroup_AsyncOperations

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_AsyncOperations](flowmachinegroup.md#BKMK_flowmachinegroup_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachinegroup`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimage_AsyncOperations"></a> flowmachineimage_AsyncOperations

One-To-Many Relationship: [flowmachineimage flowmachineimage_AsyncOperations](flowmachineimage.md#BKMK_flowmachineimage_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimage`|
|ReferencedAttribute|`flowmachineimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachineimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimageversion_AsyncOperations"></a> flowmachineimageversion_AsyncOperations

One-To-Many Relationship: [flowmachineimageversion flowmachineimageversion_AsyncOperations](flowmachineimageversion.md#BKMK_flowmachineimageversion_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimageversion`|
|ReferencedAttribute|`flowmachineimageversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachineimageversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinenetwork_AsyncOperations"></a> flowmachinenetwork_AsyncOperations

One-To-Many Relationship: [flowmachinenetwork flowmachinenetwork_AsyncOperations](flowmachinenetwork.md#BKMK_flowmachinenetwork_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinenetwork`|
|ReferencedAttribute|`flowmachinenetworkid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachinenetwork`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsession_AsyncOperations"></a> flowsession_AsyncOperations

One-To-Many Relationship: [flowsession flowsession_AsyncOperations](flowsession.md#BKMK_flowsession_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsession`|
|ReferencedAttribute|`flowsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fxexpression_AsyncOperations"></a> fxexpression_AsyncOperations

One-To-Many Relationship: [fxexpression fxexpression_AsyncOperations](fxexpression.md#BKMK_fxexpression_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`fxexpression`|
|ReferencedAttribute|`fxexpressionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fxexpression`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Goal_AsyncOperations"></a> Goal_AsyncOperations

One-To-Many Relationship: [goal Goal_AsyncOperations](goal.md#BKMK_Goal_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`goal`|
|ReferencedAttribute|`goalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_goal`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goalrollupquery_AsyncOperations"></a> goalrollupquery_AsyncOperations

One-To-Many Relationship: [goalrollupquery goalrollupquery_AsyncOperations](goalrollupquery.md#BKMK_goalrollupquery_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_goalrollupquery`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_governanceconfiguration_AsyncOperations"></a> governanceconfiguration_AsyncOperations

One-To-Many Relationship: [governanceconfiguration governanceconfiguration_AsyncOperations](governanceconfiguration.md#BKMK_governanceconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`governanceconfiguration`|
|ReferencedAttribute|`governanceconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_governanceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Import_AsyncOperations"></a> Import_AsyncOperations

One-To-Many Relationship: [import Import_AsyncOperations](import.md#BKMK_Import_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`import`|
|ReferencedAttribute|`importid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_import`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportData_AsyncOperations"></a> ImportData_AsyncOperations

One-To-Many Relationship: [importdata ImportData_AsyncOperations](importdata.md#BKMK_ImportData_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`importdata`|
|ReferencedAttribute|`importdataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_importdata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportFile_AsyncOperations"></a> ImportFile_AsyncOperations

One-To-Many Relationship: [importfile ImportFile_AsyncOperations](importfile.md#BKMK_ImportFile_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`importfile`|
|ReferencedAttribute|`importfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_importfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportLog_AsyncOperations"></a> ImportLog_AsyncOperations

One-To-Many Relationship: [importlog ImportLog_AsyncOperations](importlog.md#BKMK_ImportLog_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`importlog`|
|ReferencedAttribute|`importlogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_importlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportMap_AsyncOperations"></a> ImportMap_AsyncOperations

One-To-Many Relationship: [importmap ImportMap_AsyncOperations](importmap.md#BKMK_ImportMap_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`importmap`|
|ReferencedAttribute|`importmapid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_importmap`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_indexattributes_AsyncOperations"></a> indexattributes_AsyncOperations

One-To-Many Relationship: [indexattributes indexattributes_AsyncOperations](indexattributes.md#BKMK_indexattributes_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`indexattributes`|
|ReferencedAttribute|`indexattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_indexattributes`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_interactionforemail_AsyncOperations"></a> interactionforemail_AsyncOperations

One-To-Many Relationship: [interactionforemail interactionforemail_AsyncOperations](interactionforemail.md#BKMK_interactionforemail_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`interactionforemail`|
|ReferencedAttribute|`interactionforemailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_new_interactionforemail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticle_AsyncOperations"></a> KbArticle_AsyncOperations

One-To-Many Relationship: [kbarticle KbArticle_AsyncOperations](kbarticle.md#BKMK_KbArticle_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticle`|
|ReferencedAttribute|`kbarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_kbarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticleComment_AsyncOperations"></a> KbArticleComment_AsyncOperations

One-To-Many Relationship: [kbarticlecomment KbArticleComment_AsyncOperations](kbarticlecomment.md#BKMK_KbArticleComment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticlecomment`|
|ReferencedAttribute|`kbarticlecommentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_kbarticlecomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KbArticleTemplate_AsyncOperations"></a> KbArticleTemplate_AsyncOperations

One-To-Many Relationship: [kbarticletemplate KbArticleTemplate_AsyncOperations](kbarticletemplate.md#BKMK_KbArticleTemplate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticletemplate`|
|ReferencedAttribute|`kbarticletemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_kbarticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_keyvaultreference_AsyncOperations"></a> keyvaultreference_AsyncOperations

One-To-Many Relationship: [keyvaultreference keyvaultreference_AsyncOperations](keyvaultreference.md#BKMK_keyvaultreference_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`keyvaultreference`|
|ReferencedAttribute|`keyvaultreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_keyvaultreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_AsyncOperations"></a> knowledgearticle_AsyncOperations

One-To-Many Relationship: [knowledgearticle knowledgearticle_AsyncOperations](knowledgearticle.md#BKMK_knowledgearticle_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KnowledgeBaseRecord_AsyncOperations"></a> KnowledgeBaseRecord_AsyncOperations

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_AsyncOperations](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgebaserecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Letter_AsyncOperations"></a> Letter_AsyncOperations

One-To-Many Relationship: [letter Letter_AsyncOperations](letter.md#BKMK_Letter_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_letter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_asyncoperation_createdby"></a> lk_asyncoperation_createdby

One-To-Many Relationship: [systemuser lk_asyncoperation_createdby](systemuser.md#BKMK_lk_asyncoperation_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_asyncoperation_createdonbehalfby"></a> lk_asyncoperation_createdonbehalfby

One-To-Many Relationship: [systemuser lk_asyncoperation_createdonbehalfby](systemuser.md#BKMK_lk_asyncoperation_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_asyncoperation_modifiedby"></a> lk_asyncoperation_modifiedby

One-To-Many Relationship: [systemuser lk_asyncoperation_modifiedby](systemuser.md#BKMK_lk_asyncoperation_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_asyncoperation_modifiedonbehalfby"></a> lk_asyncoperation_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_asyncoperation_modifiedonbehalfby](systemuser.md#BKMK_lk_asyncoperation_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_asyncoperation_workflowactivationid"></a> lk_asyncoperation_workflowactivationid

One-To-Many Relationship: [workflow lk_asyncoperation_workflowactivationid](workflow.md#BKMK_lk_asyncoperation_workflowactivationid)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`workflowactivationid`|
|ReferencingEntityNavigationPropertyName|`workflowactivationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mailbox_asyncoperations"></a> mailbox_asyncoperations

One-To-Many Relationship: [mailbox mailbox_asyncoperations](mailbox.md#BKMK_mailbox_asyncoperations)

|Property|Value|
|---|---|
|ReferencedEntity|`mailbox`|
|ReferencedAttribute|`mailboxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mailbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_MailMergeTemplate_AsyncOperations"></a> MailMergeTemplate_AsyncOperations

One-To-Many Relationship: [mailmergetemplate MailMergeTemplate_AsyncOperations](mailmergetemplate.md#BKMK_MailMergeTemplate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`mailmergetemplate`|
|ReferencedAttribute|`mailmergetemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mailmergetemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mainfewshot_AsyncOperations"></a> mainfewshot_AsyncOperations

One-To-Many Relationship: [mainfewshot mainfewshot_AsyncOperations](mainfewshot.md#BKMK_mainfewshot_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`mainfewshot`|
|ReferencedAttribute|`mainfewshotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mainfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_makerfewshot_AsyncOperations"></a> makerfewshot_AsyncOperations

One-To-Many Relationship: [makerfewshot makerfewshot_AsyncOperations](makerfewshot.md#BKMK_makerfewshot_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`makerfewshot`|
|ReferencedAttribute|`makerfewshotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_makerfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_AsyncOperations"></a> managedidentity_AsyncOperations

One-To-Many Relationship: [managedidentity managedidentity_AsyncOperations](managedidentity.md#BKMK_managedidentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_managedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_maskingrule_AsyncOperations"></a> maskingrule_AsyncOperations

One-To-Many Relationship: [maskingrule maskingrule_AsyncOperations](maskingrule.md#BKMK_maskingrule_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`maskingrule`|
|ReferencedAttribute|`maskingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_maskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_metadataforarchival_AsyncOperations"></a> metadataforarchival_AsyncOperations

One-To-Many Relationship: [metadataforarchival metadataforarchival_AsyncOperations](metadataforarchival.md#BKMK_metadataforarchival_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`metadataforarchival`|
|ReferencedAttribute|`metadataforarchivalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_metadataforarchival`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_metric_AsyncOperations"></a> metric_AsyncOperations

One-To-Many Relationship: [metric metric_AsyncOperations](metric.md#BKMK_metric_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`metric`|
|ReferencedAttribute|`metricid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_metric`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mobileofflineprofileextension_AsyncOperations"></a> mobileofflineprofileextension_AsyncOperations

One-To-Many Relationship: [mobileofflineprofileextension mobileofflineprofileextension_AsyncOperations](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofileextension`|
|ReferencedAttribute|`mobileofflineprofileextensionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mobileofflineprofileextension`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_MonthlyFiscalCalendar_AsyncOperations"></a> MonthlyFiscalCalendar_AsyncOperations

One-To-Many Relationship: [monthlyfiscalcalendar MonthlyFiscalCalendar_AsyncOperations](monthlyfiscalcalendar.md#BKMK_MonthlyFiscalCalendar_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`monthlyfiscalcalendar`|
|ReferencedAttribute|`userfiscalcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_monthlyfiscalcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdataset_AsyncOperations"></a> msdyn_aibdataset_AsyncOperations

One-To-Many Relationship: [msdyn_aibdataset msdyn_aibdataset_AsyncOperations](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdataset`|
|ReferencedAttribute|`msdyn_aibdatasetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetfile_AsyncOperations"></a> msdyn_aibdatasetfile_AsyncOperations

One-To-Many Relationship: [msdyn_aibdatasetfile msdyn_aibdatasetfile_AsyncOperations](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetfile`|
|ReferencedAttribute|`msdyn_aibdatasetfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetrecord_AsyncOperations"></a> msdyn_aibdatasetrecord_AsyncOperations

One-To-Many Relationship: [msdyn_aibdatasetrecord msdyn_aibdatasetrecord_AsyncOperations](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetrecord`|
|ReferencedAttribute|`msdyn_aibdatasetrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetscontainer_AsyncOperations"></a> msdyn_aibdatasetscontainer_AsyncOperations

One-To-Many Relationship: [msdyn_aibdatasetscontainer msdyn_aibdatasetscontainer_AsyncOperations](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetscontainer`|
|ReferencedAttribute|`msdyn_aibdatasetscontainerid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetscontainer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfeedbackloop_AsyncOperations"></a> msdyn_aibfeedbackloop_AsyncOperations

One-To-Many Relationship: [msdyn_aibfeedbackloop msdyn_aibfeedbackloop_AsyncOperations](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfeedbackloop`|
|ReferencedAttribute|`msdyn_aibfeedbackloopid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfeedbackloop`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfile_AsyncOperations"></a> msdyn_aibfile_AsyncOperations

One-To-Many Relationship: [msdyn_aibfile msdyn_aibfile_AsyncOperations](msdyn_aibfile.md#BKMK_msdyn_aibfile_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfile`|
|ReferencedAttribute|`msdyn_aibfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfileattacheddata_AsyncOperations"></a> msdyn_aibfileattacheddata_AsyncOperations

One-To-Many Relationship: [msdyn_aibfileattacheddata msdyn_aibfileattacheddata_AsyncOperations](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfileattacheddata`|
|ReferencedAttribute|`msdyn_aibfileattacheddataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfileattacheddata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiconfiguration_AsyncOperations"></a> msdyn_aiconfiguration_AsyncOperations

One-To-Many Relationship: [msdyn_aiconfiguration msdyn_aiconfiguration_AsyncOperations](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfiguration`|
|ReferencedAttribute|`msdyn_aiconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aidataprocessingevent_AsyncOperations"></a> msdyn_aidataprocessingevent_AsyncOperations

One-To-Many Relationship: [msdyn_aidataprocessingevent msdyn_aidataprocessingevent_AsyncOperations](msdyn_aidataprocessingevent.md#BKMK_msdyn_aidataprocessingevent_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aidataprocessingevent`|
|ReferencedAttribute|`msdyn_aidataprocessingeventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aidataprocessingevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationconfiguration_AsyncOperations"></a> msdyn_aievaluationconfiguration_AsyncOperations

One-To-Many Relationship: [msdyn_aievaluationconfiguration msdyn_aievaluationconfiguration_AsyncOperations](msdyn_aievaluationconfiguration.md#BKMK_msdyn_aievaluationconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationconfiguration`|
|ReferencedAttribute|`msdyn_aievaluationconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievaluationconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationrun_AsyncOperations"></a> msdyn_aievaluationrun_AsyncOperations

One-To-Many Relationship: [msdyn_aievaluationrun msdyn_aievaluationrun_AsyncOperations](msdyn_aievaluationrun.md#BKMK_msdyn_aievaluationrun_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationrun`|
|ReferencedAttribute|`msdyn_aievaluationrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievaluationrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievent_AsyncOperations"></a> msdyn_aievent_AsyncOperations

One-To-Many Relationship: [msdyn_aievent msdyn_aievent_AsyncOperations](msdyn_aievent.md#BKMK_msdyn_aievent_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievent`|
|ReferencedAttribute|`msdyn_aieventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aifptrainingdocument_AsyncOperations"></a> msdyn_aifptrainingdocument_AsyncOperations

One-To-Many Relationship: [msdyn_aifptrainingdocument msdyn_aifptrainingdocument_AsyncOperations](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aifptrainingdocument`|
|ReferencedAttribute|`msdyn_aifptrainingdocumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aifptrainingdocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aimodel_AsyncOperations"></a> msdyn_aimodel_AsyncOperations

One-To-Many Relationship: [msdyn_aimodel msdyn_aimodel_AsyncOperations](msdyn_aimodel.md#BKMK_msdyn_aimodel_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aimodel`|
|ReferencedAttribute|`msdyn_aimodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aimodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aimodelcatalog_AsyncOperations"></a> msdyn_aimodelcatalog_AsyncOperations

One-To-Many Relationship: [msdyn_aimodelcatalog msdyn_aimodelcatalog_AsyncOperations](msdyn_aimodelcatalog.md#BKMK_msdyn_aimodelcatalog_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aimodelcatalog`|
|ReferencedAttribute|`msdyn_aimodelcatalogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aimodelcatalog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodimage_AsyncOperations"></a> msdyn_aiodimage_AsyncOperations

One-To-Many Relationship: [msdyn_aiodimage msdyn_aiodimage_AsyncOperations](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodimage`|
|ReferencedAttribute|`msdyn_aiodimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodlabel_AsyncOperations"></a> msdyn_aiodlabel_AsyncOperations

One-To-Many Relationship: [msdyn_aiodlabel msdyn_aiodlabel_AsyncOperations](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodlabel`|
|ReferencedAttribute|`msdyn_aiodlabelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodlabel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingboundingbox_AsyncOperations"></a> msdyn_aiodtrainingboundingbox_AsyncOperations

One-To-Many Relationship: [msdyn_aiodtrainingboundingbox msdyn_aiodtrainingboundingbox_AsyncOperations](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencedAttribute|`msdyn_aiodtrainingboundingboxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodtrainingboundingbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingimage_AsyncOperations"></a> msdyn_aiodtrainingimage_AsyncOperations

One-To-Many Relationship: [msdyn_aiodtrainingimage msdyn_aiodtrainingimage_AsyncOperations](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingimage`|
|ReferencedAttribute|`msdyn_aiodtrainingimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodtrainingimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitemplate_AsyncOperations"></a> msdyn_aitemplate_AsyncOperations

One-To-Many Relationship: [msdyn_aitemplate msdyn_aitemplate_AsyncOperations](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitemplate`|
|ReferencedAttribute|`msdyn_aitemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcase_AsyncOperations"></a> msdyn_aitestcase_AsyncOperations

One-To-Many Relationship: [msdyn_aitestcase msdyn_aitestcase_AsyncOperations](msdyn_aitestcase.md#BKMK_msdyn_aitestcase_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcase`|
|ReferencedAttribute|`msdyn_aitestcaseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcasedocument_AsyncOperations"></a> msdyn_aitestcasedocument_AsyncOperations

One-To-Many Relationship: [msdyn_aitestcasedocument msdyn_aitestcasedocument_AsyncOperations](msdyn_aitestcasedocument.md#BKMK_msdyn_aitestcasedocument_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcasedocument`|
|ReferencedAttribute|`msdyn_aitestcasedocumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcasedocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcaseinput_AsyncOperations"></a> msdyn_aitestcaseinput_AsyncOperations

One-To-Many Relationship: [msdyn_aitestcaseinput msdyn_aitestcaseinput_AsyncOperations](msdyn_aitestcaseinput.md#BKMK_msdyn_aitestcaseinput_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcaseinput`|
|ReferencedAttribute|`msdyn_aitestcaseinputid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcaseinput`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrun_AsyncOperations"></a> msdyn_aitestrun_AsyncOperations

One-To-Many Relationship: [msdyn_aitestrun msdyn_aitestrun_AsyncOperations](msdyn_aitestrun.md#BKMK_msdyn_aitestrun_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrun`|
|ReferencedAttribute|`msdyn_aitestrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrunbatch_AsyncOperations"></a> msdyn_aitestrunbatch_AsyncOperations

One-To-Many Relationship: [msdyn_aitestrunbatch msdyn_aitestrunbatch_AsyncOperations](msdyn_aitestrunbatch.md#BKMK_msdyn_aitestrunbatch_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrunbatch`|
|ReferencedAttribute|`msdyn_aitestrunbatchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestrunbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysiscomponent_AsyncOperations"></a> msdyn_analysiscomponent_AsyncOperations

One-To-Many Relationship: [msdyn_analysiscomponent msdyn_analysiscomponent_AsyncOperations](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysiscomponent`|
|ReferencedAttribute|`msdyn_analysiscomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysiscomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_AsyncOperations"></a> msdyn_analysisjob_AsyncOperations

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_AsyncOperations](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisjob`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisoverride_AsyncOperations"></a> msdyn_analysisoverride_AsyncOperations

One-To-Many Relationship: [msdyn_analysisoverride msdyn_analysisoverride_AsyncOperations](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisoverride`|
|ReferencedAttribute|`msdyn_analysisoverrideid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisoverride`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresult_AsyncOperations"></a> msdyn_analysisresult_AsyncOperations

One-To-Many Relationship: [msdyn_analysisresult msdyn_analysisresult_AsyncOperations](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresult`|
|ReferencedAttribute|`msdyn_analysisresultid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisresult`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresultdetail_AsyncOperations"></a> msdyn_analysisresultdetail_AsyncOperations

One-To-Many Relationship: [msdyn_analysisresultdetail msdyn_analysisresultdetail_AsyncOperations](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresultdetail`|
|ReferencedAttribute|`msdyn_analysisresultdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisresultdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_appinsightsmetadata_AsyncOperations"></a> msdyn_appinsightsmetadata_AsyncOperations

One-To-Many Relationship: [msdyn_appinsightsmetadata msdyn_appinsightsmetadata_AsyncOperations](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_appinsightsmetadata`|
|ReferencedAttribute|`msdyn_appinsightsmetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_appinsightsmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_copilotinteractions_AsyncOperations"></a> msdyn_copilotinteractions_AsyncOperations

One-To-Many Relationship: [msdyn_copilotinteractions msdyn_copilotinteractions_AsyncOperations](msdyn_copilotinteractions.md#BKMK_msdyn_copilotinteractions_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_copilotinteractions`|
|ReferencedAttribute|`msdyn_copilotinteractionsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_copilotinteractions`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_AsyncOperations"></a> msdyn_customcontrolextendedsettings_AsyncOperations

One-To-Many Relationship: [msdyn_customcontrolextendedsettings msdyn_customcontrolextendedsettings_AsyncOperations](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_customcontrolextendedsettings`|
|ReferencedAttribute|`msdyn_customcontrolextendedsettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_customcontrolextendedsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_AsyncOperations"></a> msdyn_dataflow_AsyncOperations

One-To-Many Relationship: [msdyn_dataflow msdyn_dataflow_AsyncOperations](msdyn_dataflow.md#BKMK_msdyn_dataflow_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow`|
|ReferencedAttribute|`msdyn_dataflowid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_datalakefolder_AsyncOperations"></a> msdyn_dataflow_datalakefolder_AsyncOperations

One-To-Many Relationship: [msdyn_dataflow_datalakefolder msdyn_dataflow_datalakefolder_AsyncOperations](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow_datalakefolder`|
|ReferencedAttribute|`msdyn_dataflow_datalakefolderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflow_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowconnectionreference_AsyncOperations"></a> msdyn_dataflowconnectionreference_AsyncOperations

One-To-Many Relationship: [msdyn_dataflowconnectionreference msdyn_dataflowconnectionreference_AsyncOperations](msdyn_dataflowconnectionreference.md#BKMK_msdyn_dataflowconnectionreference_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowconnectionreference`|
|ReferencedAttribute|`msdyn_dataflowconnectionreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowconnectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowrefreshhistory_AsyncOperations"></a> msdyn_dataflowrefreshhistory_AsyncOperations

One-To-Many Relationship: [msdyn_dataflowrefreshhistory msdyn_dataflowrefreshhistory_AsyncOperations](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowrefreshhistory`|
|ReferencedAttribute|`msdyn_dataflowrefreshhistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowtemplate_AsyncOperations"></a> msdyn_dataflowtemplate_AsyncOperations

One-To-Many Relationship: [msdyn_dataflowtemplate msdyn_dataflowtemplate_AsyncOperations](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowtemplate`|
|ReferencedAttribute|`msdyn_dataflowtemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequest_AsyncOperations"></a> msdyn_dmsrequest_AsyncOperations

One-To-Many Relationship: [msdyn_dmsrequest msdyn_dmsrequest_AsyncOperations](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequest`|
|ReferencedAttribute|`msdyn_dmsrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmsrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequeststatus_AsyncOperations"></a> msdyn_dmsrequeststatus_AsyncOperations

One-To-Many Relationship: [msdyn_dmsrequeststatus msdyn_dmsrequeststatus_AsyncOperations](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequeststatus`|
|ReferencedAttribute|`msdyn_dmsrequeststatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmsrequeststatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncrequest_AsyncOperations"></a> msdyn_dmssyncrequest_AsyncOperations

One-To-Many Relationship: [msdyn_dmssyncrequest msdyn_dmssyncrequest_AsyncOperations](msdyn_dmssyncrequest.md#BKMK_msdyn_dmssyncrequest_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncrequest`|
|ReferencedAttribute|`msdyn_dmssyncrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmssyncrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncstatus_AsyncOperations"></a> msdyn_dmssyncstatus_AsyncOperations

One-To-Many Relationship: [msdyn_dmssyncstatus msdyn_dmssyncstatus_AsyncOperations](msdyn_dmssyncstatus.md#BKMK_msdyn_dmssyncstatus_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncstatus`|
|ReferencedAttribute|`msdyn_dmssyncstatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmssyncstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations"></a> msdyn_entitylinkchatconfiguration_AsyncOperations

One-To-Many Relationship: [msdyn_entitylinkchatconfiguration msdyn_entitylinkchatconfiguration_AsyncOperations](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencedAttribute|`msdyn_entitylinkchatconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_entitylinkchatconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entityrefreshhistory_AsyncOperations"></a> msdyn_entityrefreshhistory_AsyncOperations

One-To-Many Relationship: [msdyn_entityrefreshhistory msdyn_entityrefreshhistory_AsyncOperations](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entityrefreshhistory`|
|ReferencedAttribute|`msdyn_entityrefreshhistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_entityrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_favoriteknowledgearticle_AsyncOperations"></a> msdyn_favoriteknowledgearticle_AsyncOperations

One-To-Many Relationship: [msdyn_favoriteknowledgearticle msdyn_favoriteknowledgearticle_AsyncOperations](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_favoriteknowledgearticle`|
|ReferencedAttribute|`msdyn_favoriteknowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_favoriteknowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticle_AsyncOperations"></a> msdyn_federatedarticle_AsyncOperations

One-To-Many Relationship: [msdyn_federatedarticle msdyn_federatedarticle_AsyncOperations](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticle`|
|ReferencedAttribute|`msdyn_federatedarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_federatedarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticleincident_AsyncOperations"></a> msdyn_federatedarticleincident_AsyncOperations

One-To-Many Relationship: [msdyn_federatedarticleincident msdyn_federatedarticleincident_AsyncOperations](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticleincident`|
|ReferencedAttribute|`msdyn_federatedarticleincidentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_federatedarticleincident`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_fileupload_AsyncOperations"></a> msdyn_fileupload_AsyncOperations

One-To-Many Relationship: [msdyn_fileupload msdyn_fileupload_AsyncOperations](msdyn_fileupload.md#BKMK_msdyn_fileupload_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_fileupload`|
|ReferencedAttribute|`msdyn_fileuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_fileupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_actionapprovalmodel_AsyncOperations"></a> msdyn_flow_actionapprovalmodel_AsyncOperations

One-To-Many Relationship: [msdyn_flow_actionapprovalmodel msdyn_flow_actionapprovalmodel_AsyncOperations](msdyn_flow_actionapprovalmodel.md#BKMK_msdyn_flow_actionapprovalmodel_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_actionapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_actionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approval_AsyncOperations"></a> msdyn_flow_approval_AsyncOperations

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approval_AsyncOperations](msdyn_flow_approval.md#BKMK_msdyn_flow_approval_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrequest_AsyncOperations"></a> msdyn_flow_approvalrequest_AsyncOperations

One-To-Many Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrequest_AsyncOperations](msdyn_flow_approvalrequest.md#BKMK_msdyn_flow_approvalrequest_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalrequest`|
|ReferencedAttribute|`msdyn_flow_approvalrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalresponse_AsyncOperations"></a> msdyn_flow_approvalresponse_AsyncOperations

One-To-Many Relationship: [msdyn_flow_approvalresponse msdyn_flow_approvalresponse_AsyncOperations](msdyn_flow_approvalresponse.md#BKMK_msdyn_flow_approvalresponse_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalresponse`|
|ReferencedAttribute|`msdyn_flow_approvalresponseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalresponse`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalstep_AsyncOperations"></a> msdyn_flow_approvalstep_AsyncOperations

One-To-Many Relationship: [msdyn_flow_approvalstep msdyn_flow_approvalstep_AsyncOperations](msdyn_flow_approvalstep.md#BKMK_msdyn_flow_approvalstep_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalstep`|
|ReferencedAttribute|`msdyn_flow_approvalstepid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallactionapprovalmodel_AsyncOperations"></a> msdyn_flow_awaitallactionapprovalmodel_AsyncOperations

One-To-Many Relationship: [msdyn_flow_awaitallactionapprovalmodel msdyn_flow_awaitallactionapprovalmodel_AsyncOperations](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_msdyn_flow_awaitallactionapprovalmodel_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallactionapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_awaitallactionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallapprovalmodel_AsyncOperations"></a> msdyn_flow_awaitallapprovalmodel_AsyncOperations

One-To-Many Relationship: [msdyn_flow_awaitallapprovalmodel msdyn_flow_awaitallapprovalmodel_AsyncOperations](msdyn_flow_awaitallapprovalmodel.md#BKMK_msdyn_flow_awaitallapprovalmodel_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_awaitallapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_basicapprovalmodel_AsyncOperations"></a> msdyn_flow_basicapprovalmodel_AsyncOperations

One-To-Many Relationship: [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodel_AsyncOperations](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodel_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_basicapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_basicapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_flowapproval_AsyncOperations"></a> msdyn_flow_flowapproval_AsyncOperations

One-To-Many Relationship: [msdyn_flow_flowapproval msdyn_flow_flowapproval_AsyncOperations](msdyn_flow_flowapproval.md#BKMK_msdyn_flow_flowapproval_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_flowapproval`|
|ReferencedAttribute|`msdyn_flow_flowapprovalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_flowapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_formmapping_AsyncOperations"></a> msdyn_formmapping_AsyncOperations

One-To-Many Relationship: [msdyn_formmapping msdyn_formmapping_AsyncOperations](msdyn_formmapping.md#BKMK_msdyn_formmapping_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_formmapping`|
|ReferencedAttribute|`msdyn_formmappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_formmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_function_AsyncOperations"></a> msdyn_function_AsyncOperations

One-To-Many Relationship: [msdyn_function msdyn_function_AsyncOperations](msdyn_function.md#BKMK_msdyn_function_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_function`|
|ReferencedAttribute|`msdyn_functionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_function`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_helppage_AsyncOperations"></a> msdyn_helppage_AsyncOperations

One-To-Many Relationship: [msdyn_helppage msdyn_helppage_AsyncOperations](msdyn_helppage.md#BKMK_msdyn_helppage_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_helppage`|
|ReferencedAttribute|`msdyn_helppageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_helppage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_insightsstorevirtualentity_AsyncOperations"></a> msdyn_insightsstorevirtualentity_AsyncOperations

One-To-Many Relationship: [msdyn_insightsstorevirtualentity msdyn_insightsstorevirtualentity_AsyncOperations](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_insightsstorevirtualentity`|
|ReferencedAttribute|`msdyn_insightsstorevirtualentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_insightsstorevirtualentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_integratedsearchprovider_AsyncOperations"></a> msdyn_integratedsearchprovider_AsyncOperations

One-To-Many Relationship: [msdyn_integratedsearchprovider msdyn_integratedsearchprovider_AsyncOperations](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_integratedsearchprovider`|
|ReferencedAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_integratedsearchprovider`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kalanguagesetting_AsyncOperations"></a> msdyn_kalanguagesetting_AsyncOperations

One-To-Many Relationship: [msdyn_kalanguagesetting msdyn_kalanguagesetting_AsyncOperations](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kalanguagesetting`|
|ReferencedAttribute|`msdyn_kalanguagesettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kalanguagesetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kbattachment_AsyncOperations"></a> msdyn_kbattachment_AsyncOperations

One-To-Many Relationship: [msdyn_kbattachment msdyn_kbattachment_AsyncOperations](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kbattachment`|
|ReferencedAttribute|`msdyn_kbattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kbattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_AsyncOperations"></a> msdyn_kmfederatedsearchconfig_AsyncOperations

One-To-Many Relationship: [msdyn_kmfederatedsearchconfig msdyn_kmfederatedsearchconfig_AsyncOperations](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencedAttribute|`msdyn_kmfederatedsearchconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kmfederatedsearchconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmpersonalizationsetting_AsyncOperations"></a> msdyn_kmpersonalizationsetting_AsyncOperations

One-To-Many Relationship: [msdyn_kmpersonalizationsetting msdyn_kmpersonalizationsetting_AsyncOperations](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmpersonalizationsetting`|
|ReferencedAttribute|`msdyn_kmpersonalizationsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kmpersonalizationsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticleimage_AsyncOperations"></a> msdyn_knowledgearticleimage_AsyncOperations

One-To-Many Relationship: [msdyn_knowledgearticleimage msdyn_knowledgearticleimage_AsyncOperations](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticleimage`|
|ReferencedAttribute|`msdyn_knowledgearticleimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgearticleimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticletemplate_AsyncOperations"></a> msdyn_knowledgearticletemplate_AsyncOperations

One-To-Many Relationship: [msdyn_knowledgearticletemplate msdyn_knowledgearticletemplate_AsyncOperations](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticletemplate`|
|ReferencedAttribute|`msdyn_knowledgearticletemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgearticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeassetconfiguration_AsyncOperations"></a> msdyn_knowledgeassetconfiguration_AsyncOperations

One-To-Many Relationship: [msdyn_knowledgeassetconfiguration msdyn_knowledgeassetconfiguration_AsyncOperations](msdyn_knowledgeassetconfiguration.md#BKMK_msdyn_knowledgeassetconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeassetconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeassetconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeassetconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeconfiguration_AsyncOperations"></a> msdyn_knowledgeconfiguration_AsyncOperations

One-To-Many Relationship: [msdyn_knowledgeconfiguration msdyn_knowledgeconfiguration_AsyncOperations](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeinteractioninsight_AsyncOperations"></a> msdyn_knowledgeinteractioninsight_AsyncOperations

One-To-Many Relationship: [msdyn_knowledgeinteractioninsight msdyn_knowledgeinteractioninsight_AsyncOperations](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencedAttribute|`msdyn_knowledgeinteractioninsightid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeinteractioninsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgemanagementsetting_AsyncOperations"></a> msdyn_knowledgemanagementsetting_AsyncOperations

One-To-Many Relationship: [msdyn_knowledgemanagementsetting msdyn_knowledgemanagementsetting_AsyncOperations](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgemanagementsetting`|
|ReferencedAttribute|`msdyn_knowledgemanagementsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgemanagementsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgepersonalfilter_AsyncOperations"></a> msdyn_knowledgepersonalfilter_AsyncOperations

One-To-Many Relationship: [msdyn_knowledgepersonalfilter msdyn_knowledgepersonalfilter_AsyncOperations](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgepersonalfilter`|
|ReferencedAttribute|`msdyn_knowledgepersonalfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgepersonalfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchfilter_AsyncOperations"></a> msdyn_knowledgesearchfilter_AsyncOperations

One-To-Many Relationship: [msdyn_knowledgesearchfilter msdyn_knowledgesearchfilter_AsyncOperations](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchfilter`|
|ReferencedAttribute|`msdyn_knowledgesearchfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgesearchfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchinsight_AsyncOperations"></a> msdyn_knowledgesearchinsight_AsyncOperations

One-To-Many Relationship: [msdyn_knowledgesearchinsight msdyn_knowledgesearchinsight_AsyncOperations](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchinsight`|
|ReferencedAttribute|`msdyn_knowledgesearchinsightid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgesearchinsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_mobileapp_AsyncOperations"></a> msdyn_mobileapp_AsyncOperations

One-To-Many Relationship: [msdyn_mobileapp msdyn_mobileapp_AsyncOperations](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_mobileapp`|
|ReferencedAttribute|`msdyn_mobileappid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_mobileapp`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_modulerundetail_AsyncOperations"></a> msdyn_modulerundetail_AsyncOperations

One-To-Many Relationship: [msdyn_modulerundetail msdyn_modulerundetail_AsyncOperations](msdyn_modulerundetail.md#BKMK_msdyn_modulerundetail_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_modulerundetail`|
|ReferencedAttribute|`msdyn_modulerundetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_modulerundetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmanalysishistory_AsyncOperations"></a> msdyn_pmanalysishistory_AsyncOperations

One-To-Many Relationship: [msdyn_pmanalysishistory msdyn_pmanalysishistory_AsyncOperations](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmanalysishistory`|
|ReferencedAttribute|`msdyn_pmanalysishistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmanalysishistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmbusinessruleautomationconfig_AsyncOperations"></a> msdyn_pmbusinessruleautomationconfig_AsyncOperations

One-To-Many Relationship: [msdyn_pmbusinessruleautomationconfig msdyn_pmbusinessruleautomationconfig_AsyncOperations](msdyn_pmbusinessruleautomationconfig.md#BKMK_msdyn_pmbusinessruleautomationconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencedAttribute|`msdyn_pmbusinessruleautomationconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmbusinessruleautomationconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendar_AsyncOperations"></a> msdyn_pmcalendar_AsyncOperations

One-To-Many Relationship: [msdyn_pmcalendar msdyn_pmcalendar_AsyncOperations](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendar`|
|ReferencedAttribute|`msdyn_pmcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendarversion_AsyncOperations"></a> msdyn_pmcalendarversion_AsyncOperations

One-To-Many Relationship: [msdyn_pmcalendarversion msdyn_pmcalendarversion_AsyncOperations](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendarversion`|
|ReferencedAttribute|`msdyn_pmcalendarversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmcalendarversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pminferredtask_AsyncOperations"></a> msdyn_pminferredtask_AsyncOperations

One-To-Many Relationship: [msdyn_pminferredtask msdyn_pminferredtask_AsyncOperations](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pminferredtask`|
|ReferencedAttribute|`msdyn_pminferredtaskid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pminferredtask`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_AsyncOperations"></a> msdyn_pmprocessextendedmetadataversion_AsyncOperations

One-To-Many Relationship: [msdyn_pmprocessextendedmetadataversion msdyn_pmprocessextendedmetadataversion_AsyncOperations](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessextendedmetadataversion`|
|ReferencedAttribute|`msdyn_pmprocessextendedmetadataversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessextendedmetadataversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocesstemplate_AsyncOperations"></a> msdyn_pmprocesstemplate_AsyncOperations

One-To-Many Relationship: [msdyn_pmprocesstemplate msdyn_pmprocesstemplate_AsyncOperations](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocesstemplate`|
|ReferencedAttribute|`msdyn_pmprocesstemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocesstemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessusersettings_AsyncOperations"></a> msdyn_pmprocessusersettings_AsyncOperations

One-To-Many Relationship: [msdyn_pmprocessusersettings msdyn_pmprocessusersettings_AsyncOperations](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessusersettings`|
|ReferencedAttribute|`msdyn_pmprocessusersettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessusersettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessversion_AsyncOperations"></a> msdyn_pmprocessversion_AsyncOperations

One-To-Many Relationship: [msdyn_pmprocessversion msdyn_pmprocessversion_AsyncOperations](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessversion`|
|ReferencedAttribute|`msdyn_pmprocessversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmrecording_AsyncOperations"></a> msdyn_pmrecording_AsyncOperations

One-To-Many Relationship: [msdyn_pmrecording msdyn_pmrecording_AsyncOperations](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmrecording`|
|ReferencedAttribute|`msdyn_pmrecordingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmrecording`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmsimulation_AsyncOperations"></a> msdyn_pmsimulation_AsyncOperations

One-To-Many Relationship: [msdyn_pmsimulation msdyn_pmsimulation_AsyncOperations](msdyn_pmsimulation.md#BKMK_msdyn_pmsimulation_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmsimulation`|
|ReferencedAttribute|`msdyn_pmsimulationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmsimulation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtemplate_AsyncOperations"></a> msdyn_pmtemplate_AsyncOperations

One-To-Many Relationship: [msdyn_pmtemplate msdyn_pmtemplate_AsyncOperations](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtemplate`|
|ReferencedAttribute|`msdyn_pmtemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmview_AsyncOperations"></a> msdyn_pmview_AsyncOperations

One-To-Many Relationship: [msdyn_pmview msdyn_pmview_AsyncOperations](msdyn_pmview.md#BKMK_msdyn_pmview_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmview`|
|ReferencedAttribute|`msdyn_pmviewid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmview`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_qna_AsyncOperations"></a> msdyn_qna_AsyncOperations

One-To-Many Relationship: [msdyn_qna msdyn_qna_AsyncOperations](msdyn_qna.md#BKMK_msdyn_qna_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_qna`|
|ReferencedAttribute|`msdyn_qnaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_qna`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_richtextfile_AsyncOperations"></a> msdyn_richtextfile_AsyncOperations

One-To-Many Relationship: [msdyn_richtextfile msdyn_richtextfile_AsyncOperations](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_richtextfile`|
|ReferencedAttribute|`msdyn_richtextfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_richtextfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredobject_AsyncOperations"></a> msdyn_salesforcestructuredobject_AsyncOperations

One-To-Many Relationship: [msdyn_salesforcestructuredobject msdyn_salesforcestructuredobject_AsyncOperations](msdyn_salesforcestructuredobject.md#BKMK_msdyn_salesforcestructuredobject_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredobject`|
|ReferencedAttribute|`msdyn_salesforcestructuredobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_salesforcestructuredobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredqnaconfig_AsyncOperations"></a> msdyn_salesforcestructuredqnaconfig_AsyncOperations

One-To-Many Relationship: [msdyn_salesforcestructuredqnaconfig msdyn_salesforcestructuredqnaconfig_AsyncOperations](msdyn_salesforcestructuredqnaconfig.md#BKMK_msdyn_salesforcestructuredqnaconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredqnaconfig`|
|ReferencedAttribute|`msdyn_salesforcestructuredqnaconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_salesforcestructuredqnaconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_schedule_AsyncOperations"></a> msdyn_schedule_AsyncOperations

One-To-Many Relationship: [msdyn_schedule msdyn_schedule_AsyncOperations](msdyn_schedule.md#BKMK_msdyn_schedule_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_schedule`|
|ReferencedAttribute|`msdyn_scheduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_schedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_serviceconfiguration_AsyncOperations"></a> msdyn_serviceconfiguration_AsyncOperations

One-To-Many Relationship: [msdyn_serviceconfiguration msdyn_serviceconfiguration_AsyncOperations](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_serviceconfiguration`|
|ReferencedAttribute|`msdyn_serviceconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_serviceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_slakpi_AsyncOperations"></a> msdyn_slakpi_AsyncOperations

One-To-Many Relationship: [msdyn_slakpi msdyn_slakpi_AsyncOperations](msdyn_slakpi.md#BKMK_msdyn_slakpi_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_slakpi`|
|ReferencedAttribute|`msdyn_slakpiid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_slakpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthrule_AsyncOperations"></a> msdyn_solutionhealthrule_AsyncOperations

One-To-Many Relationship: [msdyn_solutionhealthrule msdyn_solutionhealthrule_AsyncOperations](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthrule`|
|ReferencedAttribute|`msdyn_solutionhealthruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleargument_AsyncOperations"></a> msdyn_solutionhealthruleargument_AsyncOperations

One-To-Many Relationship: [msdyn_solutionhealthruleargument msdyn_solutionhealthruleargument_AsyncOperations](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleargument`|
|ReferencedAttribute|`msdyn_solutionhealthruleargumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthruleargument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleset_AsyncOperations"></a> msdyn_solutionhealthruleset_AsyncOperations

One-To-Many Relationship: [msdyn_solutionhealthruleset msdyn_solutionhealthruleset_AsyncOperations](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleset`|
|ReferencedAttribute|`msdyn_solutionhealthrulesetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthruleset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_tour_AsyncOperations"></a> msdyn_tour_AsyncOperations

One-To-Many Relationship: [msdyn_tour msdyn_tour_AsyncOperations](msdyn_tour.md#BKMK_msdyn_tour_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_tour`|
|ReferencedAttribute|`msdyn_tourid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_tour`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_virtualtablecolumncandidate_AsyncOperations"></a> msdyn_virtualtablecolumncandidate_AsyncOperations

One-To-Many Relationship: [msdyn_virtualtablecolumncandidate msdyn_virtualtablecolumncandidate_AsyncOperations](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencedAttribute|`msdyn_virtualtablecolumncandidateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_virtualtablecolumncandidate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_workflowactionstatus_AsyncOperations"></a> msdyn_workflowactionstatus_AsyncOperations

One-To-Many Relationship: [msdyn_workflowactionstatus msdyn_workflowactionstatus_AsyncOperations](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_workflowactionstatus`|
|ReferencedAttribute|`msdyn_workflowactionstatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_workflowactionstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdynce_botcontent_AsyncOperations"></a> msdynce_botcontent_AsyncOperations

One-To-Many Relationship: [msdynce_botcontent msdynce_botcontent_AsyncOperations](msdynce_botcontent.md#BKMK_msdynce_botcontent_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msdynce_botcontent`|
|ReferencedAttribute|`msdynce_botcontentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdynce_botcontent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msgraphresourcetosubscription_AsyncOperations"></a> msgraphresourcetosubscription_AsyncOperations

One-To-Many Relationship: [msgraphresourcetosubscription msgraphresourcetosubscription_AsyncOperations](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`msgraphresourcetosubscription`|
|ReferencedAttribute|`msgraphresourcetosubscriptionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msgraphresourcetosubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_AsyncOperations"></a> mspcat_catalogsubmissionfiles_AsyncOperations

One-To-Many Relationship: [mspcat_catalogsubmissionfiles mspcat_catalogsubmissionfiles_AsyncOperations](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_catalogsubmissionfiles`|
|ReferencedAttribute|`mspcat_catalogsubmissionfilesid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspcat_catalogsubmissionfiles`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_packagestore_AsyncOperations"></a> mspcat_packagestore_AsyncOperations

One-To-Many Relationship: [mspcat_packagestore mspcat_packagestore_AsyncOperations](mspcat_packagestore.md#BKMK_mspcat_packagestore_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_packagestore`|
|ReferencedAttribute|`mspcat_packagestoreid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspcat_packagestore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Organization_AsyncOperations"></a> Organization_AsyncOperations

One-To-Many Relationship: [organization Organization_AsyncOperations](organization.md#BKMK_Organization_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncfnostate_AsyncOperations"></a> organizationdatasyncfnostate_AsyncOperations

One-To-Many Relationship: [organizationdatasyncfnostate organizationdatasyncfnostate_AsyncOperations](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncfnostate`|
|ReferencedAttribute|`organizationdatasyncfnostateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncfnostate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncstate_AsyncOperations"></a> organizationdatasyncstate_AsyncOperations

One-To-Many Relationship: [organizationdatasyncstate organizationdatasyncstate_AsyncOperations](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncstate`|
|ReferencedAttribute|`organizationdatasyncstateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncstate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscription_AsyncOperations"></a> organizationdatasyncsubscription_AsyncOperations

One-To-Many Relationship: [organizationdatasyncsubscription organizationdatasyncsubscription_AsyncOperations](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionentity_AsyncOperations"></a> organizationdatasyncsubscriptionentity_AsyncOperations

One-To-Many Relationship: [organizationdatasyncsubscriptionentity organizationdatasyncsubscriptionentity_AsyncOperations](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionentity`|
|ReferencedAttribute|`organizationdatasyncsubscriptionentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscriptionentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_AsyncOperations"></a> organizationdatasyncsubscriptionfnotable_AsyncOperations

One-To-Many Relationship: [organizationdatasyncsubscriptionfnotable organizationdatasyncsubscriptionfnotable_AsyncOperations](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencedAttribute|`organizationdatasyncsubscriptionfnotableid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscriptionfnotable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_asyncoperations"></a> owner_asyncoperations

One-To-Many Relationship: [owner owner_asyncoperations](owner.md#BKMK_owner_asyncoperations)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_package_AsyncOperations"></a> package_AsyncOperations

One-To-Many Relationship: [package package_AsyncOperations](package.md#BKMK_package_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`package`|
|ReferencedAttribute|`packageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_package`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_packagehistory_AsyncOperations"></a> packagehistory_AsyncOperations

One-To-Many Relationship: [packagehistory packagehistory_AsyncOperations](packagehistory.md#BKMK_packagehistory_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`packagehistory`|
|ReferencedAttribute|`packagehistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_packagehistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_PhoneCall_AsyncOperations"></a> PhoneCall_AsyncOperations

One-To-Many Relationship: [phonecall PhoneCall_AsyncOperations](phonecall.md#BKMK_PhoneCall_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannerbusinessscenario_AsyncOperations"></a> plannerbusinessscenario_AsyncOperations

One-To-Many Relationship: [plannerbusinessscenario plannerbusinessscenario_AsyncOperations](plannerbusinessscenario.md#BKMK_plannerbusinessscenario_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`plannerbusinessscenario`|
|ReferencedAttribute|`plannerbusinessscenarioid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plannerbusinessscenario`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannersyncaction_AsyncOperations"></a> plannersyncaction_AsyncOperations

One-To-Many Relationship: [plannersyncaction plannersyncaction_AsyncOperations](plannersyncaction.md#BKMK_plannersyncaction_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`plannersyncaction`|
|ReferencedAttribute|`plannersyncactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plannersyncaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plugin_AsyncOperations"></a> plugin_AsyncOperations

One-To-Many Relationship: [plugin plugin_AsyncOperations](plugin.md#BKMK_plugin_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`plugin`|
|ReferencedAttribute|`pluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_pluginpackage_AsyncOperations"></a> pluginpackage_AsyncOperations

One-To-Many Relationship: [pluginpackage pluginpackage_AsyncOperations](pluginpackage.md#BKMK_pluginpackage_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`pluginpackage`|
|ReferencedAttribute|`pluginpackageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_pluginpackage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_position_AsyncOperations"></a> position_AsyncOperations

One-To-Many Relationship: [position position_AsyncOperations](position.md#BKMK_position_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`position`|
|ReferencedAttribute|`positionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_position`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_post_AsyncOperations"></a> post_AsyncOperations

One-To-Many Relationship: [post post_AsyncOperations](post.md#BKMK_post_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`post`|
|ReferencedAttribute|`postid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_post`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_PostFollow_AsyncOperations"></a> PostFollow_AsyncOperations

One-To-Many Relationship: [postfollow PostFollow_AsyncOperations](postfollow.md#BKMK_PostFollow_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`postfollow`|
|ReferencedAttribute|`postfollowid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_postfollow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidataset_AsyncOperations"></a> powerbidataset_AsyncOperations

One-To-Many Relationship: [powerbidataset powerbidataset_AsyncOperations](powerbidataset.md#BKMK_powerbidataset_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidataset`|
|ReferencedAttribute|`powerbidatasetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbidataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidatasetapdx_AsyncOperations"></a> powerbidatasetapdx_AsyncOperations

One-To-Many Relationship: [powerbidatasetapdx powerbidatasetapdx_AsyncOperations](powerbidatasetapdx.md#BKMK_powerbidatasetapdx_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidatasetapdx`|
|ReferencedAttribute|`powerbidatasetapdxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbidatasetapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbimashupparameter_AsyncOperations"></a> powerbimashupparameter_AsyncOperations

One-To-Many Relationship: [powerbimashupparameter powerbimashupparameter_AsyncOperations](powerbimashupparameter.md#BKMK_powerbimashupparameter_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbimashupparameter`|
|ReferencedAttribute|`powerbimashupparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbimashupparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireport_AsyncOperations"></a> powerbireport_AsyncOperations

One-To-Many Relationship: [powerbireport powerbireport_AsyncOperations](powerbireport.md#BKMK_powerbireport_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireport`|
|ReferencedAttribute|`powerbireportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbireport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireportapdx_AsyncOperations"></a> powerbireportapdx_AsyncOperations

One-To-Many Relationship: [powerbireportapdx powerbireportapdx_AsyncOperations](powerbireportapdx.md#BKMK_powerbireportapdx_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireportapdx`|
|ReferencedAttribute|`powerbireportapdxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbireportapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerfxrule_AsyncOperations"></a> powerfxrule_AsyncOperations

One-To-Many Relationship: [powerfxrule powerfxrule_AsyncOperations](powerfxrule.md#BKMK_powerfxrule_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerfxrule`|
|ReferencedAttribute|`powerfxruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerfxrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagecomponent_AsyncOperations"></a> powerpagecomponent_AsyncOperations

One-To-Many Relationship: [powerpagecomponent powerpagecomponent_AsyncOperations](powerpagecomponent.md#BKMK_powerpagecomponent_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagecomponent`|
|ReferencedAttribute|`powerpagecomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagecomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesite_AsyncOperations"></a> powerpagesite_AsyncOperations

One-To-Many Relationship: [powerpagesite powerpagesite_AsyncOperations](powerpagesite.md#BKMK_powerpagesite_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesite`|
|ReferencedAttribute|`powerpagesiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitelanguage_AsyncOperations"></a> powerpagesitelanguage_AsyncOperations

One-To-Many Relationship: [powerpagesitelanguage powerpagesitelanguage_AsyncOperations](powerpagesitelanguage.md#BKMK_powerpagesitelanguage_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitelanguage`|
|ReferencedAttribute|`powerpagesitelanguageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesitelanguage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitepublished_AsyncOperations"></a> powerpagesitepublished_AsyncOperations

One-To-Many Relationship: [powerpagesitepublished powerpagesitepublished_AsyncOperations](powerpagesitepublished.md#BKMK_powerpagesitepublished_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitepublished`|
|ReferencedAttribute|`powerpagesitepublishedid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesitepublished`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesmanagedidentity_AsyncOperations"></a> powerpagesmanagedidentity_AsyncOperations

One-To-Many Relationship: [powerpagesmanagedidentity powerpagesmanagedidentity_AsyncOperations](powerpagesmanagedidentity.md#BKMK_powerpagesmanagedidentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesmanagedidentity`|
|ReferencedAttribute|`powerpagesmanagedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesscanreport_AsyncOperations"></a> powerpagesscanreport_AsyncOperations

One-To-Many Relationship: [powerpagesscanreport powerpagesscanreport_AsyncOperations](powerpagesscanreport.md#BKMK_powerpagesscanreport_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesscanreport`|
|ReferencedAttribute|`powerpagesscanreportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesscanreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Privilege_AsyncOperations"></a> Privilege_AsyncOperations

One-To-Many Relationship: [privilege Privilege_AsyncOperations](privilege.md#BKMK_Privilege_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`privilege`|
|ReferencedAttribute|`privilegeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilege`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerlog_AsyncOperations"></a> privilegecheckerlog_AsyncOperations

One-To-Many Relationship: [privilegecheckerlog privilegecheckerlog_AsyncOperations](privilegecheckerlog.md#BKMK_privilegecheckerlog_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerlog`|
|ReferencedAttribute|`privilegecheckerlogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegecheckerlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerrun_AsyncOperations"></a> privilegecheckerrun_AsyncOperations

One-To-Many Relationship: [privilegecheckerrun privilegecheckerrun_AsyncOperations](privilegecheckerrun.md#BKMK_privilegecheckerrun_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerrun`|
|ReferencedAttribute|`privilegecheckerrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegecheckerrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegesremovalsetting_AsyncOperations"></a> privilegesremovalsetting_AsyncOperations

One-To-Many Relationship: [privilegesremovalsetting privilegesremovalsetting_AsyncOperations](privilegesremovalsetting.md#BKMK_privilegesremovalsetting_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegesremovalsetting`|
|ReferencedAttribute|`privilegesremovalsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegesremovalsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstageparameter_AsyncOperations"></a> processstageparameter_AsyncOperations

One-To-Many Relationship: [processstageparameter processstageparameter_AsyncOperations](processstageparameter.md#BKMK_processstageparameter_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`processstageparameter`|
|ReferencedAttribute|`processstageparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_processstageparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_provisionlanguageforuser_AsyncOperations"></a> provisionlanguageforuser_AsyncOperations

One-To-Many Relationship: [provisionlanguageforuser provisionlanguageforuser_AsyncOperations](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`provisionlanguageforuser`|
|ReferencedAttribute|`provisionlanguageforuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_provisionlanguageforuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_QuarterlyFiscalCalendar_AsyncOperations"></a> QuarterlyFiscalCalendar_AsyncOperations

One-To-Many Relationship: [quarterlyfiscalcalendar QuarterlyFiscalCalendar_AsyncOperations](quarterlyfiscalcalendar.md#BKMK_QuarterlyFiscalCalendar_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`quarterlyfiscalcalendar`|
|ReferencedAttribute|`userfiscalcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_quarterlyfiscalcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Queue_AsyncOperations"></a> Queue_AsyncOperations

One-To-Many Relationship: [queue Queue_AsyncOperations](queue.md#BKMK_Queue_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_queue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_QueueItem_AsyncOperations"></a> QueueItem_AsyncOperations

One-To-Many Relationship: [queueitem QueueItem_AsyncOperations](queueitem.md#BKMK_QueueItem_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`queueitem`|
|ReferencedAttribute|`queueitemid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_queueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recordfilter_AsyncOperations"></a> recordfilter_AsyncOperations

One-To-Many Relationship: [recordfilter recordfilter_AsyncOperations](recordfilter.md#BKMK_recordfilter_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`recordfilter`|
|ReferencedAttribute|`recordfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_RecurringAppointmentMaster_AsyncOperations"></a> RecurringAppointmentMaster_AsyncOperations

One-To-Many Relationship: [recurringappointmentmaster RecurringAppointmentMaster_AsyncOperations](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recyclebinconfig_AsyncOperations"></a> recyclebinconfig_AsyncOperations

One-To-Many Relationship: [recyclebinconfig recyclebinconfig_AsyncOperations](recyclebinconfig.md#BKMK_recyclebinconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`recyclebinconfig`|
|ReferencedAttribute|`recyclebinconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recyclebinconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_relationshipattribute_AsyncOperations"></a> relationshipattribute_AsyncOperations

One-To-Many Relationship: [relationshipattribute relationshipattribute_AsyncOperations](relationshipattribute.md#BKMK_relationshipattribute_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`relationshipattribute`|
|ReferencedAttribute|`relationshipattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_relationshipattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Report_AsyncOperations"></a> Report_AsyncOperations

One-To-Many Relationship: [report Report_AsyncOperations](report.md#BKMK_Report_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`report`|
|ReferencedAttribute|`reportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_report`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_reportparameter_AsyncOperations"></a> reportparameter_AsyncOperations

One-To-Many Relationship: [reportparameter reportparameter_AsyncOperations](reportparameter.md#BKMK_reportparameter_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`reportparameter`|
|ReferencedAttribute|`reportparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_reportparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retaineddataexcel_AsyncOperations"></a> retaineddataexcel_AsyncOperations

One-To-Many Relationship: [retaineddataexcel retaineddataexcel_AsyncOperations](retaineddataexcel.md#BKMK_retaineddataexcel_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`retaineddataexcel`|
|ReferencedAttribute|`retaineddataexcelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retaineddataexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionconfig_AsyncOperations"></a> retentionconfig_AsyncOperations

One-To-Many Relationship: [retentionconfig retentionconfig_AsyncOperations](retentionconfig.md#BKMK_retentionconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionconfig`|
|ReferencedAttribute|`retentionconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionfailuredetail_AsyncOperations"></a> retentionfailuredetail_AsyncOperations

One-To-Many Relationship: [retentionfailuredetail retentionfailuredetail_AsyncOperations](retentionfailuredetail.md#BKMK_retentionfailuredetail_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionfailuredetail`|
|ReferencedAttribute|`retentionfailuredetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionfailuredetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperation_AsyncOperations"></a> retentionoperation_AsyncOperations

One-To-Many Relationship: [retentionoperation retentionoperation_AsyncOperations](retentionoperation.md#BKMK_retentionoperation_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperation`|
|ReferencedAttribute|`retentionoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperationdetail_AsyncOperations"></a> retentionoperationdetail_AsyncOperations

One-To-Many Relationship: [retentionoperationdetail retentionoperationdetail_AsyncOperations](retentionoperationdetail.md#BKMK_retentionoperationdetail_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperationdetail`|
|ReferencedAttribute|`retentionoperationdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionoperationdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionsuccessdetail_AsyncOperations"></a> retentionsuccessdetail_AsyncOperations

One-To-Many Relationship: [retentionsuccessdetail retentionsuccessdetail_AsyncOperations](retentionsuccessdetail.md#BKMK_retentionsuccessdetail_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionsuccessdetail`|
|ReferencedAttribute|`retentionsuccessdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionsuccessdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Role_AsyncOperations"></a> Role_AsyncOperations

One-To-Many Relationship: [role Role_AsyncOperations](role.md#BKMK_Role_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`role`|
|ReferencedAttribute|`roleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_role`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_roleeditorlayout_AsyncOperations"></a> roleeditorlayout_AsyncOperations

One-To-Many Relationship: [roleeditorlayout roleeditorlayout_AsyncOperations](roleeditorlayout.md#BKMK_roleeditorlayout_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`roleeditorlayout`|
|ReferencedAttribute|`roleeditorlayoutid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_roleeditorlayout`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_rollupfield_AsyncOperations"></a> rollupfield_AsyncOperations

One-To-Many Relationship: [rollupfield rollupfield_AsyncOperations](rollupfield.md#BKMK_rollupfield_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`rollupfield`|
|ReferencedAttribute|`rollupfieldid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_rollupfield`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SavedQuery_AsyncOperations"></a> SavedQuery_AsyncOperations

One-To-Many Relationship: [savedquery SavedQuery_AsyncOperations](savedquery.md#BKMK_SavedQuery_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`savedquery`|
|ReferencedAttribute|`savedqueryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_savedquery`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_savingrule_AsyncOperations"></a> savingrule_AsyncOperations

One-To-Many Relationship: [savingrule savingrule_AsyncOperations](savingrule.md#BKMK_savingrule_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`savingrule`|
|ReferencedAttribute|`savingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_savingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SdkMessageProcessingStep_AsyncOperations"></a> SdkMessageProcessingStep_AsyncOperations

One-To-Many Relationship: [sdkmessageprocessingstep SdkMessageProcessingStep_AsyncOperations](sdkmessageprocessingstep.md#BKMK_SdkMessageProcessingStep_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`sdkmessageprocessingstep`|
|ReferencedAttribute|`sdkmessageprocessingstepid`|
|ReferencingAttribute|`owningextensionid`|
|ReferencingEntityNavigationPropertyName|`owningextensionid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchattributesettings_AsyncOperations"></a> searchattributesettings_AsyncOperations

One-To-Many Relationship: [searchattributesettings searchattributesettings_AsyncOperations](searchattributesettings.md#BKMK_searchattributesettings_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`searchattributesettings`|
|ReferencedAttribute|`searchattributesettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchattributesettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchcustomanalyzer_AsyncOperations"></a> searchcustomanalyzer_AsyncOperations

One-To-Many Relationship: [searchcustomanalyzer searchcustomanalyzer_AsyncOperations](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`searchcustomanalyzer`|
|ReferencedAttribute|`searchcustomanalyzerid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchcustomanalyzer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchrelationshipsettings_AsyncOperations"></a> searchrelationshipsettings_AsyncOperations

One-To-Many Relationship: [searchrelationshipsettings searchrelationshipsettings_AsyncOperations](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`searchrelationshipsettings`|
|ReferencedAttribute|`searchrelationshipsettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchrelationshipsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SemiAnnualFiscalCalendar_AsyncOperations"></a> SemiAnnualFiscalCalendar_AsyncOperations

One-To-Many Relationship: [semiannualfiscalcalendar SemiAnnualFiscalCalendar_AsyncOperations](semiannualfiscalcalendar.md#BKMK_SemiAnnualFiscalCalendar_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`semiannualfiscalcalendar`|
|ReferencedAttribute|`userfiscalcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_semiannualfiscalcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplan_AsyncOperations"></a> serviceplan_AsyncOperations

One-To-Many Relationship: [serviceplan serviceplan_AsyncOperations](serviceplan.md#BKMK_serviceplan_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplan`|
|ReferencedAttribute|`serviceplanid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_serviceplan`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplanmapping_AsyncOperations"></a> serviceplanmapping_AsyncOperations

One-To-Many Relationship: [serviceplanmapping serviceplanmapping_AsyncOperations](serviceplanmapping.md#BKMK_serviceplanmapping_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplanmapping`|
|ReferencedAttribute|`serviceplanmappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_serviceplanmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedlinksetting_AsyncOperations"></a> sharedlinksetting_AsyncOperations

One-To-Many Relationship: [sharedlinksetting sharedlinksetting_AsyncOperations](sharedlinksetting.md#BKMK_sharedlinksetting_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedlinksetting`|
|ReferencedAttribute|`sharedlinksettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedlinksetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedobject_AsyncOperations"></a> sharedobject_AsyncOperations

One-To-Many Relationship: [sharedobject sharedobject_AsyncOperations](sharedobject.md#BKMK_sharedobject_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedobject`|
|ReferencedAttribute|`sharedobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspace_AsyncOperations"></a> sharedworkspace_AsyncOperations

One-To-Many Relationship: [sharedworkspace sharedworkspace_AsyncOperations](sharedworkspace.md#BKMK_sharedworkspace_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspace`|
|ReferencedAttribute|`sharedworkspaceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspacepool_AsyncOperations"></a> sharedworkspacepool_AsyncOperations

One-To-Many Relationship: [sharedworkspacepool sharedworkspacepool_AsyncOperations](sharedworkspacepool.md#BKMK_sharedworkspacepool_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspacepool`|
|ReferencedAttribute|`sharedworkspacepoolid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedworkspacepool`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SharePointDocumentLocation_AsyncOperations"></a> SharePointDocumentLocation_AsyncOperations

One-To-Many Relationship: [sharepointdocumentlocation SharePointDocumentLocation_AsyncOperations](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointdocumentlocation`|
|ReferencedAttribute|`sharepointdocumentlocationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharepointdocumentlocation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharepointmanagedidentity_AsyncOperations"></a> sharepointmanagedidentity_AsyncOperations

One-To-Many Relationship: [sharepointmanagedidentity sharepointmanagedidentity_AsyncOperations](sharepointmanagedidentity.md#BKMK_sharepointmanagedidentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointmanagedidentity`|
|ReferencedAttribute|`sharepointmanagedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharepointmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SharePointSite_AsyncOperations"></a> SharePointSite_AsyncOperations

One-To-Many Relationship: [sharepointsite SharePointSite_AsyncOperations](sharepointsite.md#BKMK_SharePointSite_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointsite`|
|ReferencedAttribute|`sharepointsiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharepointsite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sideloadedaiplugin_AsyncOperations"></a> sideloadedaiplugin_AsyncOperations

One-To-Many Relationship: [sideloadedaiplugin sideloadedaiplugin_AsyncOperations](sideloadedaiplugin.md#BKMK_sideloadedaiplugin_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`sideloadedaiplugin`|
|ReferencedAttribute|`sideloadedaipluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sideloadedaiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_similarityrule_AsyncOperations"></a> similarityrule_AsyncOperations

One-To-Many Relationship: [similarityrule similarityrule_AsyncOperations](similarityrule.md#BKMK_similarityrule_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`similarityrule`|
|ReferencedAttribute|`similarityruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_similarityrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slabase_AsyncOperations"></a> slabase_AsyncOperations

One-To-Many Relationship: [sla slabase_AsyncOperations](sla.md#BKMK_slabase_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sla`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SocialActivity_AsyncOperations"></a> SocialActivity_AsyncOperations

One-To-Many Relationship: [socialactivity SocialActivity_AsyncOperations](socialactivity.md#BKMK_SocialActivity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_socialactivity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SocialProfile_AsyncOperations"></a> SocialProfile_AsyncOperations

One-To-Many Relationship: [socialprofile SocialProfile_AsyncOperations](socialprofile.md#BKMK_SocialProfile_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`socialprofile`|
|ReferencedAttribute|`socialprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_socialprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentattributeconfiguration_AsyncOperations"></a> solutioncomponentattributeconfiguration_AsyncOperations

One-To-Many Relationship: [solutioncomponentattributeconfiguration solutioncomponentattributeconfiguration_AsyncOperations](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentattributeconfiguration`|
|ReferencedAttribute|`solutioncomponentattributeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentattributeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentbatchconfiguration_AsyncOperations"></a> solutioncomponentbatchconfiguration_AsyncOperations

One-To-Many Relationship: [solutioncomponentbatchconfiguration solutioncomponentbatchconfiguration_AsyncOperations](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentbatchconfiguration`|
|ReferencedAttribute|`solutioncomponentbatchconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentbatchconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentconfiguration_AsyncOperations"></a> solutioncomponentconfiguration_AsyncOperations

One-To-Many Relationship: [solutioncomponentconfiguration solutioncomponentconfiguration_AsyncOperations](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentconfiguration`|
|ReferencedAttribute|`solutioncomponentconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations"></a> solutioncomponentrelationshipconfiguration_AsyncOperations

One-To-Many Relationship: [solutioncomponentrelationshipconfiguration solutioncomponentrelationshipconfiguration_AsyncOperations](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentrelationshipconfiguration`|
|ReferencedAttribute|`solutioncomponentrelationshipconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentrelationshipconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentity_AsyncOperations"></a> stagedentity_AsyncOperations

One-To-Many Relationship: [stagedentity stagedentity_AsyncOperations](stagedentity.md#BKMK_stagedentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentity`|
|ReferencedAttribute|`stagedentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentityattribute_AsyncOperations"></a> stagedentityattribute_AsyncOperations

One-To-Many Relationship: [stagedentityattribute stagedentityattribute_AsyncOperations](stagedentityattribute.md#BKMK_stagedentityattribute_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentityattribute`|
|ReferencedAttribute|`stagedentityattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedentityattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedmetadataasyncoperation_AsyncOperations"></a> stagedmetadataasyncoperation_AsyncOperations

One-To-Many Relationship: [stagedmetadataasyncoperation stagedmetadataasyncoperation_AsyncOperations](stagedmetadataasyncoperation.md#BKMK_stagedmetadataasyncoperation_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedmetadataasyncoperation`|
|ReferencedAttribute|`stagedmetadataasyncoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedmetadataasyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagesolutionupload_AsyncOperations"></a> stagesolutionupload_AsyncOperations

One-To-Many Relationship: [stagesolutionupload stagesolutionupload_AsyncOperations](stagesolutionupload.md#BKMK_stagesolutionupload_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`stagesolutionupload`|
|ReferencedAttribute|`stagesolutionuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagesolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Subject_AsyncOperations"></a> Subject_AsyncOperations

One-To-Many Relationship: [subject Subject_AsyncOperations](subject.md#BKMK_Subject_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`subject`|
|ReferencedAttribute|`subjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_subject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_supportusertable_AsyncOperations"></a> supportusertable_AsyncOperations

One-To-Many Relationship: [supportusertable supportusertable_AsyncOperations](supportusertable.md#BKMK_supportusertable_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`supportusertable`|
|ReferencedAttribute|`supportusertableid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_supportusertable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapsedatabase_AsyncOperations"></a> synapsedatabase_AsyncOperations

One-To-Many Relationship: [synapsedatabase synapsedatabase_AsyncOperations](synapsedatabase.md#BKMK_synapsedatabase_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`synapsedatabase`|
|ReferencedAttribute|`synapsedatabaseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapsedatabase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkexternaltablestate_AsyncOperations"></a> synapselinkexternaltablestate_AsyncOperations

One-To-Many Relationship: [synapselinkexternaltablestate synapselinkexternaltablestate_AsyncOperations](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkexternaltablestate`|
|ReferencedAttribute|`synapselinkexternaltablestateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkexternaltablestate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofile_AsyncOperations"></a> synapselinkprofile_AsyncOperations

One-To-Many Relationship: [synapselinkprofile synapselinkprofile_AsyncOperations](synapselinkprofile.md#BKMK_synapselinkprofile_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofile`|
|ReferencedAttribute|`synapselinkprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentity_AsyncOperations"></a> synapselinkprofileentity_AsyncOperations

One-To-Many Relationship: [synapselinkprofileentity synapselinkprofileentity_AsyncOperations](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentity`|
|ReferencedAttribute|`synapselinkprofileentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofileentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentitystate_AsyncOperations"></a> synapselinkprofileentitystate_AsyncOperations

One-To-Many Relationship: [synapselinkprofileentitystate synapselinkprofileentitystate_AsyncOperations](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentitystate`|
|ReferencedAttribute|`synapselinkprofileentitystateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofileentitystate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkschedule_AsyncOperations"></a> synapselinkschedule_AsyncOperations

One-To-Many Relationship: [synapselinkschedule synapselinkschedule_AsyncOperations](synapselinkschedule.md#BKMK_synapselinkschedule_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkschedule`|
|ReferencedAttribute|`synapselinkscheduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkschedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_system_user_asyncoperation"></a> system_user_asyncoperation

One-To-Many Relationship: [systemuser system_user_asyncoperation](systemuser.md#BKMK_system_user_asyncoperation)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemForm_AsyncOperations"></a> SystemForm_AsyncOperations

One-To-Many Relationship: [systemform SystemForm_AsyncOperations](systemform.md#BKMK_SystemForm_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`systemform`|
|ReferencedAttribute|`formid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemform`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemUser_AsyncOperations"></a> SystemUser_AsyncOperations

One-To-Many Relationship: [systemuser SystemUser_AsyncOperations](systemuser.md#BKMK_SystemUser_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuserauthorizationchangetracker_AsyncOperations"></a> systemuserauthorizationchangetracker_AsyncOperations

One-To-Many Relationship: [systemuserauthorizationchangetracker systemuserauthorizationchangetracker_AsyncOperations](systemuserauthorizationchangetracker.md#BKMK_systemuserauthorizationchangetracker_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuserauthorizationchangetracker`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemuserauthorizationchangetracker`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_tag_AsyncOperations"></a> tag_AsyncOperations

One-To-Many Relationship: [tag tag_AsyncOperations](tag.md#BKMK_tag_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`tag`|
|ReferencedAttribute|`tagid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_tag`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedflowsession_AsyncOperations"></a> taggedflowsession_AsyncOperations

One-To-Many Relationship: [taggedflowsession taggedflowsession_AsyncOperations](taggedflowsession.md#BKMK_taggedflowsession_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedflowsession`|
|ReferencedAttribute|`taggedflowsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_taggedflowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedprocess_AsyncOperations"></a> taggedprocess_AsyncOperations

One-To-Many Relationship: [taggedprocess taggedprocess_AsyncOperations](taggedprocess.md#BKMK_taggedprocess_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedprocess`|
|ReferencedAttribute|`taggedprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_taggedprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Task_AsyncOperations"></a> Task_AsyncOperations

One-To-Many Relationship: [task Task_AsyncOperations](task.md#BKMK_Task_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_asyncoperation"></a> team_asyncoperation

One-To-Many Relationship: [team team_asyncoperation](team.md#BKMK_team_asyncoperation)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Team_AsyncOperations"></a> Team_AsyncOperations

One-To-Many Relationship: [team Team_AsyncOperations](team.md#BKMK_Team_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_teammobileofflineprofilemembership_AsyncOperations"></a> teammobileofflineprofilemembership_AsyncOperations

One-To-Many Relationship: [teammobileofflineprofilemembership teammobileofflineprofilemembership_AsyncOperations](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`teammobileofflineprofilemembership`|
|ReferencedAttribute|`teammobileofflineprofilemembershipid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_teammobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Template_AsyncOperations"></a> Template_AsyncOperations

One-To-Many Relationship: [template Template_AsyncOperations](template.md#BKMK_Template_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`template`|
|ReferencedAttribute|`templateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_template`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Territory_AsyncOperations"></a> Territory_AsyncOperations

One-To-Many Relationship: [territory Territory_AsyncOperations](territory.md#BKMK_Territory_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`territory`|
|ReferencedAttribute|`territoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_territory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_theme_AsyncOperations"></a> theme_AsyncOperations

One-To-Many Relationship: [theme theme_AsyncOperations](theme.md#BKMK_theme_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`theme`|
|ReferencedAttribute|`themeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_theme`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_AsyncOperations"></a> TransactionCurrency_AsyncOperations

One-To-Many Relationship: [transactioncurrency TransactionCurrency_AsyncOperations](transactioncurrency.md#BKMK_TransactionCurrency_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_transactioncurrency`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchentity_AsyncOperations"></a> unstructuredfilesearchentity_AsyncOperations

One-To-Many Relationship: [unstructuredfilesearchentity unstructuredfilesearchentity_AsyncOperations](unstructuredfilesearchentity.md#BKMK_unstructuredfilesearchentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchentity`|
|ReferencedAttribute|`unstructuredfilesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_unstructuredfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchrecord_AsyncOperations"></a> unstructuredfilesearchrecord_AsyncOperations

One-To-Many Relationship: [unstructuredfilesearchrecord unstructuredfilesearchrecord_AsyncOperations](unstructuredfilesearchrecord.md#BKMK_unstructuredfilesearchrecord_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchrecord`|
|ReferencedAttribute|`unstructuredfilesearchrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_unstructuredfilesearchrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_UserForm_AsyncOperations"></a> UserForm_AsyncOperations

One-To-Many Relationship: [userform UserForm_AsyncOperations](userform.md#BKMK_UserForm_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`userform`|
|ReferencedAttribute|`userformid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_userform`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_usermapping_AsyncOperations"></a> usermapping_AsyncOperations

One-To-Many Relationship: [usermapping usermapping_AsyncOperations](usermapping.md#BKMK_usermapping_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`usermapping`|
|ReferencedAttribute|`usermappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_usermapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_usermobileofflineprofilemembership_AsyncOperations"></a> usermobileofflineprofilemembership_AsyncOperations

One-To-Many Relationship: [usermobileofflineprofilemembership usermobileofflineprofilemembership_AsyncOperations](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`usermobileofflineprofilemembership`|
|ReferencedAttribute|`usermobileofflineprofilemembershipid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_usermobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_UserQuery_AsyncOperations"></a> UserQuery_AsyncOperations

One-To-Many Relationship: [userquery UserQuery_AsyncOperations](userquery.md#BKMK_UserQuery_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`userquery`|
|ReferencedAttribute|`userqueryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_userquery`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_userrating_AsyncOperations"></a> userrating_AsyncOperations

One-To-Many Relationship: [userrating userrating_AsyncOperations](userrating.md#BKMK_userrating_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`userrating`|
|ReferencedAttribute|`userratingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_userrating`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_viewasexamplequestion_AsyncOperations"></a> viewasexamplequestion_AsyncOperations

One-To-Many Relationship: [viewasexamplequestion viewasexamplequestion_AsyncOperations](viewasexamplequestion.md#BKMK_viewasexamplequestion_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`viewasexamplequestion`|
|ReferencedAttribute|`viewasexamplequestionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_viewasexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_virtualentitymetadata_AsyncOperations"></a> virtualentitymetadata_AsyncOperations

One-To-Many Relationship: [virtualentitymetadata virtualentitymetadata_AsyncOperations](virtualentitymetadata.md#BKMK_virtualentitymetadata_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`virtualentitymetadata`|
|ReferencedAttribute|`virtualentitymetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_virtualentitymetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowbinary_AsyncOperations"></a> workflowbinary_AsyncOperations

One-To-Many Relationship: [workflowbinary workflowbinary_AsyncOperations](workflowbinary.md#BKMK_workflowbinary_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowbinary`|
|ReferencedAttribute|`workflowbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowmetadata_AsyncOperations"></a> workflowmetadata_AsyncOperations

One-To-Many Relationship: [workflowmetadata workflowmetadata_AsyncOperations](workflowmetadata.md#BKMK_workflowmetadata_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowmetadata`|
|ReferencedAttribute|`workflowmetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workflowmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueue_AsyncOperations"></a> workqueue_AsyncOperations

One-To-Many Relationship: [workqueue workqueue_AsyncOperations](workqueue.md#BKMK_workqueue_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueue`|
|ReferencedAttribute|`workqueueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workqueue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueueitem_AsyncOperations"></a> workqueueitem_AsyncOperations

One-To-Many Relationship: [workqueueitem workqueueitem_AsyncOperations](workqueueitem.md#BKMK_workqueueitem_AsyncOperations)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueueitem`|
|ReferencedAttribute|`workqueueitemid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workqueueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [AsyncOperation_BulkDeleteOperation](#BKMK_AsyncOperation_BulkDeleteOperation)
- [AsyncOperation_DuplicateBaseRecord](#BKMK_AsyncOperation_DuplicateBaseRecord)
- [AsyncOperation_Emails](#BKMK_AsyncOperation_Emails)
- [asyncoperation_FileAttachments](#BKMK_asyncoperation_FileAttachments)
- [AsyncOperation_MailboxTrackingFolder](#BKMK_AsyncOperation_MailboxTrackingFolder)
- [AsyncOperation_SocialActivities](#BKMK_AsyncOperation_SocialActivities)
- [lk_workflowlog_asyncoperation_childworkflow](#BKMK_lk_workflowlog_asyncoperation_childworkflow)
- [lk_workflowlog_asyncoperations](#BKMK_lk_workflowlog_asyncoperations)

### <a name="BKMK_AsyncOperation_BulkDeleteOperation"></a> AsyncOperation_BulkDeleteOperation

Many-To-One Relationship: [bulkdeleteoperation AsyncOperation_BulkDeleteOperation](bulkdeleteoperation.md#BKMK_AsyncOperation_BulkDeleteOperation)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeleteoperation`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencedEntityNavigationPropertyName|`AsyncOperation_BulkDeleteOperation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_AsyncOperation_DuplicateBaseRecord"></a> AsyncOperation_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord AsyncOperation_DuplicateBaseRecord](duplicaterecord.md#BKMK_AsyncOperation_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencedEntityNavigationPropertyName|`AsyncOperation_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_AsyncOperation_Emails"></a> AsyncOperation_Emails

Many-To-One Relationship: [email AsyncOperation_Emails](email.md#BKMK_AsyncOperation_Emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`AsyncOperation_Emails`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_asyncoperation_FileAttachments"></a> asyncoperation_FileAttachments

Many-To-One Relationship: [fileattachment asyncoperation_FileAttachments](fileattachment.md#BKMK_asyncoperation_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`asyncoperation_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_AsyncOperation_MailboxTrackingFolder"></a> AsyncOperation_MailboxTrackingFolder

Many-To-One Relationship: [mailboxtrackingfolder AsyncOperation_MailboxTrackingFolder](mailboxtrackingfolder.md#BKMK_AsyncOperation_MailboxTrackingFolder)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`AsyncOperation_MailboxTrackingFolder`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_AsyncOperation_SocialActivities"></a> AsyncOperation_SocialActivities

Many-To-One Relationship: [socialactivity AsyncOperation_SocialActivities](socialactivity.md#BKMK_AsyncOperation_SocialActivities)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`AsyncOperation_SocialActivities`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_workflowlog_asyncoperation_childworkflow"></a> lk_workflowlog_asyncoperation_childworkflow

Many-To-One Relationship: [workflowlog lk_workflowlog_asyncoperation_childworkflow](workflowlog.md#BKMK_lk_workflowlog_asyncoperation_childworkflow)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowlog`|
|ReferencingAttribute|`childworkflowinstanceid`|
|ReferencedEntityNavigationPropertyName|`lk_workflowlog_asyncoperation_childworkflow`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_workflowlog_asyncoperations"></a> lk_workflowlog_asyncoperations

Many-To-One Relationship: [workflowlog lk_workflowlog_asyncoperations](workflowlog.md#BKMK_lk_workflowlog_asyncoperations)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowlog`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencedEntityNavigationPropertyName|`lk_workflowlog_asyncoperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.asyncoperation?displayProperty=fullName>
