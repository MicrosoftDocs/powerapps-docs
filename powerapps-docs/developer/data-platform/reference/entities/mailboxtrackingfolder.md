---
title: "Mailbox Auto Tracking Folder (MailboxTrackingFolder) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Mailbox Auto Tracking Folder (MailboxTrackingFolder) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Mailbox Auto Tracking Folder (MailboxTrackingFolder) table/entity reference (Microsoft Dataverse)

Stores data about what folders for a mailbox are auto tracked

## Messages

The following table lists the messages for the Mailbox Auto Tracking Folder (MailboxTrackingFolder) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /mailboxtrackingfolders<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /mailboxtrackingfolders(*mailboxtrackingfolderid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /mailboxtrackingfolders(*mailboxtrackingfolderid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /mailboxtrackingfolders<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /mailboxtrackingfolders(*mailboxtrackingfolderid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /mailboxtrackingfolders(*mailboxtrackingfolderid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Mailbox Auto Tracking Folder (MailboxTrackingFolder) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Mailbox Auto Tracking Folder** |
| **DisplayCollectionName** | **Mailbox Auto Tracking Folders** |
| **SchemaName** | `MailboxTrackingFolder` |
| **CollectionSchemaName** | `MailboxTrackingFolders` |
| **EntitySetName** | `mailboxtrackingfolders`|
| **LogicalName** | `mailboxtrackingfolder` |
| **LogicalCollectionName** | `mailboxtrackingfolders` |
| **PrimaryIdAttribute** | `mailboxtrackingfolderid` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ExchangeFolderId](#BKMK_ExchangeFolderId)
- [ExchangeFolderName](#BKMK_ExchangeFolderName)
- [FolderOnboardingStatus](#BKMK_FolderOnboardingStatus)
- [MailboxId](#BKMK_MailboxId)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)

### <a name="BKMK_ExchangeFolderId"></a> ExchangeFolderId

|Property|Value|
|---|---|
|Description|**Folder Id for a folder in Exchange**|
|DisplayName|**Exchange Folder Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangefolderid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|120|

### <a name="BKMK_ExchangeFolderName"></a> ExchangeFolderName

|Property|Value|
|---|---|
|Description|**Exchange Folder Name**|
|DisplayName|**Exchange Folder Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangefoldername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_FolderOnboardingStatus"></a> FolderOnboardingStatus

|Property|Value|
|---|---|
|Description|**Information to indicate whether the folder has been on boarded for auto tracking**|
|DisplayName|**Folder on boarding Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`folderonboardingstatus`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MailboxId"></a> MailboxId

|Property|Value|
|---|---|
|Description|**Mailbox id associated with this record.**|
|DisplayName|**MailboxId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mailboxid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|mailbox|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.**|
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

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**The regarding object such as Account, Contact, Lead etc. that the folder relates to.**|
|DisplayName|**Regarding Object Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, activityfileattachment, adx_externalidentity, adx_invitation, adx_inviteredemption, adx_portalcomment, adx_setting, adx_webformsession, aicopilot, aiinsightcard, aiplugin, aipluginauth, aipluginconversationstarter, aipluginconversationstartermapping, aipluginexternalschema, aipluginexternalschemaproperty, aiplugingovernance, aiplugingovernanceext, aiplugininstance, aipluginoperation, aipluginoperationparameter, aipluginoperationresponsetemplate, aiplugintitle, aipluginusersetting, aiskillconfig, appaction, appactionmigration, appactionrule, appelement, application, applicationuser, appmodulecomponentedge, appmodulecomponentnode, approvalprocess, approvalstageapproval, approvalstagecondition, approvalstageorder, appsetting, appusersetting, archivecleanupinfo, archivecleanupoperation, asyncoperation, attributeimageconfig, attributemaskingrule, attributepicklistvalue, bot, botcomponent, botcomponentcollection, bulkarchiveconfig, bulkarchivefailuredetail, bulkarchiveoperation, bulkarchiveoperationdetail, businessprocess, canvasappextendedmetadata, card, cascadegrantrevokeaccessrecordstracker, cascadegrantrevokeaccessversiontracker, catalog, catalogassignment, certificatecredential, chat, comment, connectioninstance, connectionreference, connector, contact, conversationtranscript, copilotexamplequestion, copilotglossaryterm, copilotsynonyms, credential, customapi, customapirequestparameter, customapiresponseproperty, datalakefolder, datalakefolderpermission, datalakeworkspace, datalakeworkspacepermission, dataprocessingconfiguration, delegatedauthorization, deleteditemreference, desktopflowbinary, desktopflowmodule, dvfilesearch, dvfilesearchattribute, dvfilesearchentity, dvtablesearch, dvtablesearchattribute, dvtablesearchentity, emailaddressconfiguration, enablearchivalrequest, entityanalyticsconfig, entityclusterconfig, entityimageconfig, entityindex, entityrecordfilter, environmentvariabledefinition, environmentvariablevalue, exportedexcel, exportsolutionupload, fabricaiskill, featurecontrolsetting, federatedknowledgecitation, federatedknowledgeconfiguration, federatedknowledgeentityconfiguration, federatedknowledgemetadatarefresh, flowcapacityassignment, flowcredentialapplication, flowevent, flowmachine, flowmachinegroup, flowmachineimage, flowmachineimageversion, flowmachinenetwork, flowsession, fxexpression, governanceconfiguration, holidaywrapper, indexattributes, internalcatalogassignment, keyvaultreference, mainfewshot, makerfewshot, managedidentity, maskingrule, metadataforarchival, mobileofflineprofileextension, msdynce_botcontent, msdyn_aibdataset, msdyn_aibdatasetfile, msdyn_aibdatasetrecord, msdyn_aibdatasetscontainer, msdyn_aibfeedbackloop, msdyn_aibfile, msdyn_aibfileattacheddata, msdyn_aiconfiguration, msdyn_aidataprocessingevent, msdyn_aievaluationconfiguration, msdyn_aievaluationrun, msdyn_aievent, msdyn_aifptrainingdocument, msdyn_aimodel, msdyn_aimodelcatalog, msdyn_aiodimage, msdyn_aiodlabel, msdyn_aiodtrainingboundingbox, msdyn_aiodtrainingimage, msdyn_aitemplate, msdyn_aitestcase, msdyn_aitestcasedocument, msdyn_aitestcaseinput, msdyn_aitestrun, msdyn_aitestrunbatch, msdyn_analysiscomponent, msdyn_analysisjob, msdyn_analysisoverride, msdyn_analysisresult, msdyn_analysisresultdetail, msdyn_appinsightsmetadata, msdyn_copilotinteractions, msdyn_customcontrolextendedsettings, msdyn_dataflow, msdyn_dataflowconnectionreference, msdyn_dataflowrefreshhistory, msdyn_dataflowtemplate, msdyn_dataflow_datalakefolder, msdyn_dataworkspace, msdyn_dmsrequest, msdyn_dmsrequeststatus, msdyn_dmssyncrequest, msdyn_dmssyncstatus, msdyn_entitylinkchatconfiguration, msdyn_entityrefreshhistory, msdyn_favoriteknowledgearticle, msdyn_federatedarticle, msdyn_federatedarticleincident, msdyn_fileupload, msdyn_flow_actionapprovalmodel, msdyn_flow_approval, msdyn_flow_approvalrequest, msdyn_flow_approvalresponse, msdyn_flow_approvalstep, msdyn_flow_awaitallactionapprovalmodel, msdyn_flow_awaitallapprovalmodel, msdyn_flow_basicapprovalmodel, msdyn_flow_flowapproval, msdyn_formmapping, msdyn_function, msdyn_helppage, msdyn_insightsstorevirtualentity, msdyn_integratedsearchprovider, msdyn_kalanguagesetting, msdyn_kbattachment, msdyn_kmfederatedsearchconfig, msdyn_kmpersonalizationsetting, msdyn_knowledgearticleimage, msdyn_knowledgearticletemplate, msdyn_knowledgeassetconfiguration, msdyn_knowledgeconfiguration, msdyn_knowledgeinteractioninsight, msdyn_knowledgemanagementsetting, msdyn_knowledgepersonalfilter, msdyn_knowledgesearchfilter, msdyn_knowledgesearchinsight, msdyn_mobileapp, msdyn_modulerundetail, msdyn_plan, msdyn_planartifact, msdyn_planattachment, msdyn_pmanalysishistory, msdyn_pmbusinessruleautomationconfig, msdyn_pmcalendar, msdyn_pmcalendarversion, msdyn_pminferredtask, msdyn_pmprocessextendedmetadataversion, msdyn_pmprocesstemplate, msdyn_pmprocessusersettings, msdyn_pmprocessversion, msdyn_pmrecording, msdyn_pmsimulation, msdyn_pmtemplate, msdyn_pmview, msdyn_qna, msdyn_richtextfile, msdyn_salesforcestructuredobject, msdyn_salesforcestructuredqnaconfig, msdyn_schedule, msdyn_serviceconfiguration, msdyn_slakpi, msdyn_solutionhealthrule, msdyn_solutionhealthruleargument, msdyn_solutionhealthruleset, msdyn_tour, msdyn_virtualtablecolumncandidate, msdyn_workflowactionstatus, msgraphresourcetosubscription, mspcat_catalogsubmissionfiles, mspcat_packagestore, organizationdatasyncfnostate, organizationdatasyncstate, organizationdatasyncsubscription, organizationdatasyncsubscriptionentity, organizationdatasyncsubscriptionfnotable, organizationsetting, package, packagehistory, pdfsetting, plannerbusinessscenario, plannersyncaction, plugin, pluginpackage, powerbidataset, powerbidatasetapdx, powerbimashupparameter, powerbireport, powerbireportapdx, powerfxrule, powerpagecomponent, powerpagesite, powerpagesitelanguage, powerpagesitepublished, powerpagesmanagedidentity, powerpagesscanreport, privilegecheckerlog, privilegecheckerrun, privilegesremovalsetting, processorregistration, processstageparameter, provisionlanguageforuser, reconciliationentityinfo, reconciliationentitystepinfo, reconciliationinfo, recordfilter, recyclebinconfig, relationshipattribute, reportparameter, retaineddataexcel, retentioncleanupinfo, retentioncleanupoperation, retentionconfig, retentionfailuredetail, retentionoperation, retentionoperationdetail, retentionsuccessdetail, revokeinheritedaccessrecordstracker, roleeditorlayout, savingrule, searchattributesettings, searchcustomanalyzer, searchrelationshipsettings, serviceplan, serviceplancustomcontrol, serviceplanmapping, settingdefinition, sharedlinksetting, sharedobject, sharedworkspace, sharedworkspacepool, sharepointmanagedidentity, sideloadedaiplugin, signalregistration, solutioncomponentattributeconfiguration, solutioncomponentbatchconfiguration, solutioncomponentconfiguration, solutioncomponentrelationshipconfiguration, stagedentity, stagedentityattribute, stagedmetadataasyncoperation, stagesolutionupload, supportusertable, synapsedatabase, synapselinkexternaltablestate, synapselinkprofile, synapselinkprofileentity, synapselinkprofileentitystate, synapselinkschedule, systemuserauthorizationchangetracker, tag, taggedflowsession, taggedprocess, tdsmetadata, teammobileofflineprofilemembership, territory, traitregistration, unstructuredfilesearchentity, unstructuredfilesearchrecord, usermobileofflineprofilemembership, userrating, viewasexamplequestion, virtualentitymetadata, workflowbinary, workflowmetadata, workqueue, workqueueitem|

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description|**Information that indicates the type of regarding object associated with the folder**|
|DisplayName|**Regarding Object Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [MailboxTrackingFolderId](#BKMK_MailboxTrackingFolderId)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the entry was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
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

### <a name="BKMK_MailboxTrackingFolderId"></a> MailboxTrackingFolderId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mailboxtrackingfolderid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the entry was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the record.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit that owns the folder mapping.**|
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
|Description|**Unique identifier of the team who owns the folder mapping.**|
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
|Targets||

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the mailbox tracking folder.**|
|DisplayName|**Version number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [Account_MailboxTrackingFolder](#BKMK_Account_MailboxTrackingFolder)
- [activityfileattachment_MailboxTrackingFolders](#BKMK_activityfileattachment_MailboxTrackingFolders)
- [adx_externalidentity_MailboxTrackingFolders](#BKMK_adx_externalidentity_MailboxTrackingFolders)
- [adx_invitation_MailboxTrackingFolders](#BKMK_adx_invitation_MailboxTrackingFolders)
- [adx_inviteredemption_MailboxTrackingFolders](#BKMK_adx_inviteredemption_MailboxTrackingFolders)
- [adx_portalcomment_MailboxTrackingFolders](#BKMK_adx_portalcomment_MailboxTrackingFolders)
- [adx_setting_MailboxTrackingFolders](#BKMK_adx_setting_MailboxTrackingFolders)
- [adx_webformsession_MailboxTrackingFolders](#BKMK_adx_webformsession_MailboxTrackingFolders)
- [aicopilot_MailboxTrackingFolders](#BKMK_aicopilot_MailboxTrackingFolders)
- [aiplugin_MailboxTrackingFolders](#BKMK_aiplugin_MailboxTrackingFolders)
- [aipluginauth_MailboxTrackingFolders](#BKMK_aipluginauth_MailboxTrackingFolders)
- [aipluginconversationstarter_MailboxTrackingFolders](#BKMK_aipluginconversationstarter_MailboxTrackingFolders)
- [aipluginconversationstartermapping_MailboxTrackingFolders](#BKMK_aipluginconversationstartermapping_MailboxTrackingFolders)
- [aipluginexternalschema_MailboxTrackingFolders](#BKMK_aipluginexternalschema_MailboxTrackingFolders)
- [aipluginexternalschemaproperty_MailboxTrackingFolders](#BKMK_aipluginexternalschemaproperty_MailboxTrackingFolders)
- [aiplugingovernance_MailboxTrackingFolders](#BKMK_aiplugingovernance_MailboxTrackingFolders)
- [aiplugingovernanceext_MailboxTrackingFolders](#BKMK_aiplugingovernanceext_MailboxTrackingFolders)
- [aiplugininstance_MailboxTrackingFolders](#BKMK_aiplugininstance_MailboxTrackingFolders)
- [aipluginoperation_MailboxTrackingFolders](#BKMK_aipluginoperation_MailboxTrackingFolders)
- [aipluginoperationparameter_MailboxTrackingFolders](#BKMK_aipluginoperationparameter_MailboxTrackingFolders)
- [aipluginoperationresponsetemplate_MailboxTrackingFolders](#BKMK_aipluginoperationresponsetemplate_MailboxTrackingFolders)
- [aiplugintitle_MailboxTrackingFolders](#BKMK_aiplugintitle_MailboxTrackingFolders)
- [aipluginusersetting_MailboxTrackingFolders](#BKMK_aipluginusersetting_MailboxTrackingFolders)
- [appaction_MailboxTrackingFolders](#BKMK_appaction_MailboxTrackingFolders)
- [appactionmigration_MailboxTrackingFolders](#BKMK_appactionmigration_MailboxTrackingFolders)
- [appactionrule_MailboxTrackingFolders](#BKMK_appactionrule_MailboxTrackingFolders)
- [application_MailboxTrackingFolders](#BKMK_application_MailboxTrackingFolders)
- [applicationuser_MailboxTrackingFolders](#BKMK_applicationuser_MailboxTrackingFolders)
- [approvalprocess_MailboxTrackingFolders](#BKMK_approvalprocess_MailboxTrackingFolders)
- [approvalstageapproval_MailboxTrackingFolders](#BKMK_approvalstageapproval_MailboxTrackingFolders)
- [approvalstagecondition_MailboxTrackingFolders](#BKMK_approvalstagecondition_MailboxTrackingFolders)
- [approvalstageorder_MailboxTrackingFolders](#BKMK_approvalstageorder_MailboxTrackingFolders)
- [AsyncOperation_MailboxTrackingFolder](#BKMK_AsyncOperation_MailboxTrackingFolder)
- [attributeimageconfig_MailboxTrackingFolders](#BKMK_attributeimageconfig_MailboxTrackingFolders)
- [attributemaskingrule_MailboxTrackingFolders](#BKMK_attributemaskingrule_MailboxTrackingFolders)
- [attributepicklistvalue_MailboxTrackingFolders](#BKMK_attributepicklistvalue_MailboxTrackingFolders)
- [bot_MailboxTrackingFolders](#BKMK_bot_MailboxTrackingFolders)
- [botcomponent_MailboxTrackingFolders](#BKMK_botcomponent_MailboxTrackingFolders)
- [botcomponentcollection_MailboxTrackingFolders](#BKMK_botcomponentcollection_MailboxTrackingFolders)
- [businessprocess_MailboxTrackingFolders](#BKMK_businessprocess_MailboxTrackingFolders)
- [businessunit_mailboxtrackingfolder](#BKMK_businessunit_mailboxtrackingfolder)
- [card_MailboxTrackingFolders](#BKMK_card_MailboxTrackingFolders)
- [catalog_MailboxTrackingFolders](#BKMK_catalog_MailboxTrackingFolders)
- [catalogassignment_MailboxTrackingFolders](#BKMK_catalogassignment_MailboxTrackingFolders)
- [certificatecredential_MailboxTrackingFolders](#BKMK_certificatecredential_MailboxTrackingFolders)
- [chat_MailboxTrackingFolders](#BKMK_chat_MailboxTrackingFolders)
- [connectioninstance_MailboxTrackingFolders](#BKMK_connectioninstance_MailboxTrackingFolders)
- [connectionreference_MailboxTrackingFolders](#BKMK_connectionreference_MailboxTrackingFolders)
- [connector_MailboxTrackingFolders](#BKMK_connector_MailboxTrackingFolders)
- [Contact_MailboxTrackingFolder](#BKMK_Contact_MailboxTrackingFolder)
- [conversationtranscript_MailboxTrackingFolders](#BKMK_conversationtranscript_MailboxTrackingFolders)
- [copilotexamplequestion_MailboxTrackingFolders](#BKMK_copilotexamplequestion_MailboxTrackingFolders)
- [copilotglossaryterm_MailboxTrackingFolders](#BKMK_copilotglossaryterm_MailboxTrackingFolders)
- [copilotsynonyms_MailboxTrackingFolders](#BKMK_copilotsynonyms_MailboxTrackingFolders)
- [credential_MailboxTrackingFolders](#BKMK_credential_MailboxTrackingFolders)
- [customapi_MailboxTrackingFolders](#BKMK_customapi_MailboxTrackingFolders)
- [customapirequestparameter_MailboxTrackingFolders](#BKMK_customapirequestparameter_MailboxTrackingFolders)
- [customapiresponseproperty_MailboxTrackingFolders](#BKMK_customapiresponseproperty_MailboxTrackingFolders)
- [datalakefolder_MailboxTrackingFolders](#BKMK_datalakefolder_MailboxTrackingFolders)
- [datalakefolderpermission_MailboxTrackingFolders](#BKMK_datalakefolderpermission_MailboxTrackingFolders)
- [datalakeworkspace_MailboxTrackingFolders](#BKMK_datalakeworkspace_MailboxTrackingFolders)
- [datalakeworkspacepermission_MailboxTrackingFolders](#BKMK_datalakeworkspacepermission_MailboxTrackingFolders)
- [dataprocessingconfiguration_MailboxTrackingFolders](#BKMK_dataprocessingconfiguration_MailboxTrackingFolders)
- [delegatedauthorization_MailboxTrackingFolders](#BKMK_delegatedauthorization_MailboxTrackingFolders)
- [desktopflowbinary_MailboxTrackingFolders](#BKMK_desktopflowbinary_MailboxTrackingFolders)
- [desktopflowmodule_MailboxTrackingFolders](#BKMK_desktopflowmodule_MailboxTrackingFolders)
- [dvfilesearch_MailboxTrackingFolders](#BKMK_dvfilesearch_MailboxTrackingFolders)
- [dvfilesearchattribute_MailboxTrackingFolders](#BKMK_dvfilesearchattribute_MailboxTrackingFolders)
- [dvfilesearchentity_MailboxTrackingFolders](#BKMK_dvfilesearchentity_MailboxTrackingFolders)
- [dvtablesearch_MailboxTrackingFolders](#BKMK_dvtablesearch_MailboxTrackingFolders)
- [dvtablesearchattribute_MailboxTrackingFolders](#BKMK_dvtablesearchattribute_MailboxTrackingFolders)
- [dvtablesearchentity_MailboxTrackingFolders](#BKMK_dvtablesearchentity_MailboxTrackingFolders)
- [emailaddressconfiguration_MailboxTrackingFolders](#BKMK_emailaddressconfiguration_MailboxTrackingFolders)
- [entityanalyticsconfig_MailboxTrackingFolders](#BKMK_entityanalyticsconfig_MailboxTrackingFolders)
- [entityclusterconfig_MailboxTrackingFolders](#BKMK_entityclusterconfig_MailboxTrackingFolders)
- [entityimageconfig_MailboxTrackingFolders](#BKMK_entityimageconfig_MailboxTrackingFolders)
- [entityindex_MailboxTrackingFolders](#BKMK_entityindex_MailboxTrackingFolders)
- [entityrecordfilter_MailboxTrackingFolders](#BKMK_entityrecordfilter_MailboxTrackingFolders)
- [environmentvariabledefinition_MailboxTrackingFolders](#BKMK_environmentvariabledefinition_MailboxTrackingFolders)
- [environmentvariablevalue_MailboxTrackingFolders](#BKMK_environmentvariablevalue_MailboxTrackingFolders)
- [exportedexcel_MailboxTrackingFolders](#BKMK_exportedexcel_MailboxTrackingFolders)
- [exportsolutionupload_MailboxTrackingFolders](#BKMK_exportsolutionupload_MailboxTrackingFolders)
- [fabricaiskill_MailboxTrackingFolders](#BKMK_fabricaiskill_MailboxTrackingFolders)
- [featurecontrolsetting_MailboxTrackingFolders](#BKMK_featurecontrolsetting_MailboxTrackingFolders)
- [federatedknowledgeconfiguration_MailboxTrackingFolders](#BKMK_federatedknowledgeconfiguration_MailboxTrackingFolders)
- [federatedknowledgeentityconfiguration_MailboxTrackingFolders](#BKMK_federatedknowledgeentityconfiguration_MailboxTrackingFolders)
- [flowcapacityassignment_MailboxTrackingFolders](#BKMK_flowcapacityassignment_MailboxTrackingFolders)
- [flowcredentialapplication_MailboxTrackingFolders](#BKMK_flowcredentialapplication_MailboxTrackingFolders)
- [flowevent_MailboxTrackingFolders](#BKMK_flowevent_MailboxTrackingFolders)
- [flowmachine_MailboxTrackingFolders](#BKMK_flowmachine_MailboxTrackingFolders)
- [flowmachinegroup_MailboxTrackingFolders](#BKMK_flowmachinegroup_MailboxTrackingFolders)
- [flowmachineimage_MailboxTrackingFolders](#BKMK_flowmachineimage_MailboxTrackingFolders)
- [flowmachineimageversion_MailboxTrackingFolders](#BKMK_flowmachineimageversion_MailboxTrackingFolders)
- [flowmachinenetwork_MailboxTrackingFolders](#BKMK_flowmachinenetwork_MailboxTrackingFolders)
- [flowsession_MailboxTrackingFolders](#BKMK_flowsession_MailboxTrackingFolders)
- [fxexpression_MailboxTrackingFolders](#BKMK_fxexpression_MailboxTrackingFolders)
- [governanceconfiguration_MailboxTrackingFolders](#BKMK_governanceconfiguration_MailboxTrackingFolders)
- [indexattributes_MailboxTrackingFolders](#BKMK_indexattributes_MailboxTrackingFolders)
- [keyvaultreference_MailboxTrackingFolders](#BKMK_keyvaultreference_MailboxTrackingFolders)
- [lk_mailboxtrackingfolder_createdby](#BKMK_lk_mailboxtrackingfolder_createdby)
- [lk_mailboxtrackingfolder_createdonbehalfby](#BKMK_lk_mailboxtrackingfolder_createdonbehalfby)
- [lk_mailboxtrackingfolder_modifiedby](#BKMK_lk_mailboxtrackingfolder_modifiedby)
- [lk_mailboxtrackingfolder_modifiedonbehalfby](#BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby)
- [Mailbox_MailboxTrackingFolder](#BKMK_Mailbox_MailboxTrackingFolder)
- [mainfewshot_MailboxTrackingFolders](#BKMK_mainfewshot_MailboxTrackingFolders)
- [makerfewshot_MailboxTrackingFolders](#BKMK_makerfewshot_MailboxTrackingFolders)
- [managedidentity_MailboxTrackingFolders](#BKMK_managedidentity_MailboxTrackingFolders)
- [maskingrule_MailboxTrackingFolders](#BKMK_maskingrule_MailboxTrackingFolders)
- [metadataforarchival_MailboxTrackingFolders](#BKMK_metadataforarchival_MailboxTrackingFolders)
- [mobileofflineprofileextension_MailboxTrackingFolders](#BKMK_mobileofflineprofileextension_MailboxTrackingFolders)
- [msdyn_aibdataset_MailboxTrackingFolders](#BKMK_msdyn_aibdataset_MailboxTrackingFolders)
- [msdyn_aibdatasetfile_MailboxTrackingFolders](#BKMK_msdyn_aibdatasetfile_MailboxTrackingFolders)
- [msdyn_aibdatasetrecord_MailboxTrackingFolders](#BKMK_msdyn_aibdatasetrecord_MailboxTrackingFolders)
- [msdyn_aibdatasetscontainer_MailboxTrackingFolders](#BKMK_msdyn_aibdatasetscontainer_MailboxTrackingFolders)
- [msdyn_aibfeedbackloop_MailboxTrackingFolders](#BKMK_msdyn_aibfeedbackloop_MailboxTrackingFolders)
- [msdyn_aibfile_MailboxTrackingFolders](#BKMK_msdyn_aibfile_MailboxTrackingFolders)
- [msdyn_aibfileattacheddata_MailboxTrackingFolders](#BKMK_msdyn_aibfileattacheddata_MailboxTrackingFolders)
- [msdyn_aiconfiguration_MailboxTrackingFolders](#BKMK_msdyn_aiconfiguration_MailboxTrackingFolders)
- [msdyn_aidataprocessingevent_MailboxTrackingFolders](#BKMK_msdyn_aidataprocessingevent_MailboxTrackingFolders)
- [msdyn_aievaluationconfiguration_MailboxTrackingFolders](#BKMK_msdyn_aievaluationconfiguration_MailboxTrackingFolders)
- [msdyn_aievaluationrun_MailboxTrackingFolders](#BKMK_msdyn_aievaluationrun_MailboxTrackingFolders)
- [msdyn_aievent_MailboxTrackingFolders](#BKMK_msdyn_aievent_MailboxTrackingFolders)
- [msdyn_aifptrainingdocument_MailboxTrackingFolders](#BKMK_msdyn_aifptrainingdocument_MailboxTrackingFolders)
- [msdyn_aimodel_MailboxTrackingFolders](#BKMK_msdyn_aimodel_MailboxTrackingFolders)
- [msdyn_aiodimage_MailboxTrackingFolders](#BKMK_msdyn_aiodimage_MailboxTrackingFolders)
- [msdyn_aiodlabel_MailboxTrackingFolders](#BKMK_msdyn_aiodlabel_MailboxTrackingFolders)
- [msdyn_aiodtrainingboundingbox_MailboxTrackingFolders](#BKMK_msdyn_aiodtrainingboundingbox_MailboxTrackingFolders)
- [msdyn_aiodtrainingimage_MailboxTrackingFolders](#BKMK_msdyn_aiodtrainingimage_MailboxTrackingFolders)
- [msdyn_aitemplate_MailboxTrackingFolders](#BKMK_msdyn_aitemplate_MailboxTrackingFolders)
- [msdyn_aitestcase_MailboxTrackingFolders](#BKMK_msdyn_aitestcase_MailboxTrackingFolders)
- [msdyn_aitestcasedocument_MailboxTrackingFolders](#BKMK_msdyn_aitestcasedocument_MailboxTrackingFolders)
- [msdyn_aitestcaseinput_MailboxTrackingFolders](#BKMK_msdyn_aitestcaseinput_MailboxTrackingFolders)
- [msdyn_aitestrun_MailboxTrackingFolders](#BKMK_msdyn_aitestrun_MailboxTrackingFolders)
- [msdyn_aitestrunbatch_MailboxTrackingFolders](#BKMK_msdyn_aitestrunbatch_MailboxTrackingFolders)
- [msdyn_analysiscomponent_MailboxTrackingFolders](#BKMK_msdyn_analysiscomponent_MailboxTrackingFolders)
- [msdyn_analysisjob_MailboxTrackingFolders](#BKMK_msdyn_analysisjob_MailboxTrackingFolders)
- [msdyn_analysisoverride_MailboxTrackingFolders](#BKMK_msdyn_analysisoverride_MailboxTrackingFolders)
- [msdyn_analysisresult_MailboxTrackingFolders](#BKMK_msdyn_analysisresult_MailboxTrackingFolders)
- [msdyn_analysisresultdetail_MailboxTrackingFolders](#BKMK_msdyn_analysisresultdetail_MailboxTrackingFolders)
- [msdyn_appinsightsmetadata_MailboxTrackingFolders](#BKMK_msdyn_appinsightsmetadata_MailboxTrackingFolders)
- [msdyn_copilotinteractions_MailboxTrackingFolders](#BKMK_msdyn_copilotinteractions_MailboxTrackingFolders)
- [msdyn_customcontrolextendedsettings_MailboxTrackingFolders](#BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders)
- [msdyn_dataflow_datalakefolder_MailboxTrackingFolders](#BKMK_msdyn_dataflow_datalakefolder_MailboxTrackingFolders)
- [msdyn_dataflow_MailboxTrackingFolders](#BKMK_msdyn_dataflow_MailboxTrackingFolders)
- [msdyn_dataflowconnectionreference_MailboxTrackingFolders](#BKMK_msdyn_dataflowconnectionreference_MailboxTrackingFolders)
- [msdyn_dataflowrefreshhistory_MailboxTrackingFolders](#BKMK_msdyn_dataflowrefreshhistory_MailboxTrackingFolders)
- [msdyn_dataflowtemplate_MailboxTrackingFolders](#BKMK_msdyn_dataflowtemplate_MailboxTrackingFolders)
- [msdyn_dmsrequest_MailboxTrackingFolders](#BKMK_msdyn_dmsrequest_MailboxTrackingFolders)
- [msdyn_dmsrequeststatus_MailboxTrackingFolders](#BKMK_msdyn_dmsrequeststatus_MailboxTrackingFolders)
- [msdyn_dmssyncrequest_MailboxTrackingFolders](#BKMK_msdyn_dmssyncrequest_MailboxTrackingFolders)
- [msdyn_dmssyncstatus_MailboxTrackingFolders](#BKMK_msdyn_dmssyncstatus_MailboxTrackingFolders)
- [msdyn_entitylinkchatconfiguration_MailboxTrackingFolders](#BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders)
- [msdyn_entityrefreshhistory_MailboxTrackingFolders](#BKMK_msdyn_entityrefreshhistory_MailboxTrackingFolders)
- [msdyn_favoriteknowledgearticle_MailboxTrackingFolders](#BKMK_msdyn_favoriteknowledgearticle_MailboxTrackingFolders)
- [msdyn_federatedarticle_MailboxTrackingFolders](#BKMK_msdyn_federatedarticle_MailboxTrackingFolders)
- [msdyn_federatedarticleincident_MailboxTrackingFolders](#BKMK_msdyn_federatedarticleincident_MailboxTrackingFolders)
- [msdyn_fileupload_MailboxTrackingFolders](#BKMK_msdyn_fileupload_MailboxTrackingFolders)
- [msdyn_flow_actionapprovalmodel_MailboxTrackingFolders](#BKMK_msdyn_flow_actionapprovalmodel_MailboxTrackingFolders)
- [msdyn_flow_approval_MailboxTrackingFolders](#BKMK_msdyn_flow_approval_MailboxTrackingFolders)
- [msdyn_flow_approvalrequest_MailboxTrackingFolders](#BKMK_msdyn_flow_approvalrequest_MailboxTrackingFolders)
- [msdyn_flow_approvalresponse_MailboxTrackingFolders](#BKMK_msdyn_flow_approvalresponse_MailboxTrackingFolders)
- [msdyn_flow_approvalstep_MailboxTrackingFolders](#BKMK_msdyn_flow_approvalstep_MailboxTrackingFolders)
- [msdyn_flow_awaitallactionapprovalmodel_MailboxTrackingFolders](#BKMK_msdyn_flow_awaitallactionapprovalmodel_MailboxTrackingFolders)
- [msdyn_flow_awaitallapprovalmodel_MailboxTrackingFolders](#BKMK_msdyn_flow_awaitallapprovalmodel_MailboxTrackingFolders)
- [msdyn_flow_basicapprovalmodel_MailboxTrackingFolders](#BKMK_msdyn_flow_basicapprovalmodel_MailboxTrackingFolders)
- [msdyn_flow_flowapproval_MailboxTrackingFolders](#BKMK_msdyn_flow_flowapproval_MailboxTrackingFolders)
- [msdyn_formmapping_MailboxTrackingFolders](#BKMK_msdyn_formmapping_MailboxTrackingFolders)
- [msdyn_function_MailboxTrackingFolders](#BKMK_msdyn_function_MailboxTrackingFolders)
- [msdyn_helppage_MailboxTrackingFolders](#BKMK_msdyn_helppage_MailboxTrackingFolders)
- [msdyn_insightsstorevirtualentity_MailboxTrackingFolders](#BKMK_msdyn_insightsstorevirtualentity_MailboxTrackingFolders)
- [msdyn_integratedsearchprovider_MailboxTrackingFolders](#BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders)
- [msdyn_kalanguagesetting_MailboxTrackingFolders](#BKMK_msdyn_kalanguagesetting_MailboxTrackingFolders)
- [msdyn_kbattachment_MailboxTrackingFolders](#BKMK_msdyn_kbattachment_MailboxTrackingFolders)
- [msdyn_kmfederatedsearchconfig_MailboxTrackingFolders](#BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders)
- [msdyn_kmpersonalizationsetting_MailboxTrackingFolders](#BKMK_msdyn_kmpersonalizationsetting_MailboxTrackingFolders)
- [msdyn_knowledgearticleimage_MailboxTrackingFolders](#BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders)
- [msdyn_knowledgearticletemplate_MailboxTrackingFolders](#BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders)
- [msdyn_knowledgeassetconfiguration_MailboxTrackingFolders](#BKMK_msdyn_knowledgeassetconfiguration_MailboxTrackingFolders)
- [msdyn_knowledgeconfiguration_MailboxTrackingFolders](#BKMK_msdyn_knowledgeconfiguration_MailboxTrackingFolders)
- [msdyn_knowledgeinteractioninsight_MailboxTrackingFolders](#BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders)
- [msdyn_knowledgemanagementsetting_MailboxTrackingFolders](#BKMK_msdyn_knowledgemanagementsetting_MailboxTrackingFolders)
- [msdyn_knowledgepersonalfilter_MailboxTrackingFolders](#BKMK_msdyn_knowledgepersonalfilter_MailboxTrackingFolders)
- [msdyn_knowledgesearchfilter_MailboxTrackingFolders](#BKMK_msdyn_knowledgesearchfilter_MailboxTrackingFolders)
- [msdyn_knowledgesearchinsight_MailboxTrackingFolders](#BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders)
- [msdyn_mobileapp_MailboxTrackingFolders](#BKMK_msdyn_mobileapp_MailboxTrackingFolders)
- [msdyn_modulerundetail_MailboxTrackingFolders](#BKMK_msdyn_modulerundetail_MailboxTrackingFolders)
- [msdyn_pmanalysishistory_MailboxTrackingFolders](#BKMK_msdyn_pmanalysishistory_MailboxTrackingFolders)
- [msdyn_pmbusinessruleautomationconfig_MailboxTrackingFolders](#BKMK_msdyn_pmbusinessruleautomationconfig_MailboxTrackingFolders)
- [msdyn_pmcalendar_MailboxTrackingFolders](#BKMK_msdyn_pmcalendar_MailboxTrackingFolders)
- [msdyn_pmcalendarversion_MailboxTrackingFolders](#BKMK_msdyn_pmcalendarversion_MailboxTrackingFolders)
- [msdyn_pminferredtask_MailboxTrackingFolders](#BKMK_msdyn_pminferredtask_MailboxTrackingFolders)
- [msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders](#BKMK_msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders)
- [msdyn_pmprocesstemplate_MailboxTrackingFolders](#BKMK_msdyn_pmprocesstemplate_MailboxTrackingFolders)
- [msdyn_pmprocessusersettings_MailboxTrackingFolders](#BKMK_msdyn_pmprocessusersettings_MailboxTrackingFolders)
- [msdyn_pmprocessversion_MailboxTrackingFolders](#BKMK_msdyn_pmprocessversion_MailboxTrackingFolders)
- [msdyn_pmrecording_MailboxTrackingFolders](#BKMK_msdyn_pmrecording_MailboxTrackingFolders)
- [msdyn_pmsimulation_MailboxTrackingFolders](#BKMK_msdyn_pmsimulation_MailboxTrackingFolders)
- [msdyn_pmtemplate_MailboxTrackingFolders](#BKMK_msdyn_pmtemplate_MailboxTrackingFolders)
- [msdyn_pmview_MailboxTrackingFolders](#BKMK_msdyn_pmview_MailboxTrackingFolders)
- [msdyn_qna_MailboxTrackingFolders](#BKMK_msdyn_qna_MailboxTrackingFolders)
- [msdyn_richtextfile_MailboxTrackingFolders](#BKMK_msdyn_richtextfile_MailboxTrackingFolders)
- [msdyn_salesforcestructuredobject_MailboxTrackingFolders](#BKMK_msdyn_salesforcestructuredobject_MailboxTrackingFolders)
- [msdyn_salesforcestructuredqnaconfig_MailboxTrackingFolders](#BKMK_msdyn_salesforcestructuredqnaconfig_MailboxTrackingFolders)
- [msdyn_schedule_MailboxTrackingFolders](#BKMK_msdyn_schedule_MailboxTrackingFolders)
- [msdyn_serviceconfiguration_MailboxTrackingFolders](#BKMK_msdyn_serviceconfiguration_MailboxTrackingFolders)
- [msdyn_slakpi_MailboxTrackingFolders](#BKMK_msdyn_slakpi_MailboxTrackingFolders)
- [msdyn_solutionhealthrule_MailboxTrackingFolders](#BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders)
- [msdyn_solutionhealthruleargument_MailboxTrackingFolders](#BKMK_msdyn_solutionhealthruleargument_MailboxTrackingFolders)
- [msdyn_solutionhealthruleset_MailboxTrackingFolders](#BKMK_msdyn_solutionhealthruleset_MailboxTrackingFolders)
- [msdyn_tour_MailboxTrackingFolders](#BKMK_msdyn_tour_MailboxTrackingFolders)
- [msdyn_virtualtablecolumncandidate_MailboxTrackingFolders](#BKMK_msdyn_virtualtablecolumncandidate_MailboxTrackingFolders)
- [msdyn_workflowactionstatus_MailboxTrackingFolders](#BKMK_msdyn_workflowactionstatus_MailboxTrackingFolders)
- [msdynce_botcontent_MailboxTrackingFolders](#BKMK_msdynce_botcontent_MailboxTrackingFolders)
- [msgraphresourcetosubscription_MailboxTrackingFolders](#BKMK_msgraphresourcetosubscription_MailboxTrackingFolders)
- [mspcat_catalogsubmissionfiles_MailboxTrackingFolders](#BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders)
- [mspcat_packagestore_MailboxTrackingFolders](#BKMK_mspcat_packagestore_MailboxTrackingFolders)
- [Organization_MailboxTrackingFolder](#BKMK_Organization_MailboxTrackingFolder)
- [organizationdatasyncfnostate_MailboxTrackingFolders](#BKMK_organizationdatasyncfnostate_MailboxTrackingFolders)
- [organizationdatasyncstate_MailboxTrackingFolders](#BKMK_organizationdatasyncstate_MailboxTrackingFolders)
- [organizationdatasyncsubscription_MailboxTrackingFolders](#BKMK_organizationdatasyncsubscription_MailboxTrackingFolders)
- [organizationdatasyncsubscriptionentity_MailboxTrackingFolders](#BKMK_organizationdatasyncsubscriptionentity_MailboxTrackingFolders)
- [organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders](#BKMK_organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders)
- [owner_mailboxtrackingfolder](#BKMK_owner_mailboxtrackingfolder)
- [package_MailboxTrackingFolders](#BKMK_package_MailboxTrackingFolders)
- [packagehistory_MailboxTrackingFolders](#BKMK_packagehistory_MailboxTrackingFolders)
- [plannerbusinessscenario_MailboxTrackingFolders](#BKMK_plannerbusinessscenario_MailboxTrackingFolders)
- [plannersyncaction_MailboxTrackingFolders](#BKMK_plannersyncaction_MailboxTrackingFolders)
- [plugin_MailboxTrackingFolders](#BKMK_plugin_MailboxTrackingFolders)
- [pluginpackage_MailboxTrackingFolders](#BKMK_pluginpackage_MailboxTrackingFolders)
- [powerbidataset_MailboxTrackingFolders](#BKMK_powerbidataset_MailboxTrackingFolders)
- [powerbidatasetapdx_MailboxTrackingFolders](#BKMK_powerbidatasetapdx_MailboxTrackingFolders)
- [powerbimashupparameter_MailboxTrackingFolders](#BKMK_powerbimashupparameter_MailboxTrackingFolders)
- [powerbireport_MailboxTrackingFolders](#BKMK_powerbireport_MailboxTrackingFolders)
- [powerbireportapdx_MailboxTrackingFolders](#BKMK_powerbireportapdx_MailboxTrackingFolders)
- [powerfxrule_MailboxTrackingFolders](#BKMK_powerfxrule_MailboxTrackingFolders)
- [powerpagecomponent_MailboxTrackingFolders](#BKMK_powerpagecomponent_MailboxTrackingFolders)
- [powerpagesite_MailboxTrackingFolders](#BKMK_powerpagesite_MailboxTrackingFolders)
- [powerpagesitelanguage_MailboxTrackingFolders](#BKMK_powerpagesitelanguage_MailboxTrackingFolders)
- [powerpagesitepublished_MailboxTrackingFolders](#BKMK_powerpagesitepublished_MailboxTrackingFolders)
- [powerpagesmanagedidentity_MailboxTrackingFolders](#BKMK_powerpagesmanagedidentity_MailboxTrackingFolders)
- [powerpagesscanreport_MailboxTrackingFolders](#BKMK_powerpagesscanreport_MailboxTrackingFolders)
- [privilegecheckerlog_MailboxTrackingFolders](#BKMK_privilegecheckerlog_MailboxTrackingFolders)
- [privilegecheckerrun_MailboxTrackingFolders](#BKMK_privilegecheckerrun_MailboxTrackingFolders)
- [privilegesremovalsetting_MailboxTrackingFolders](#BKMK_privilegesremovalsetting_MailboxTrackingFolders)
- [processstageparameter_MailboxTrackingFolders](#BKMK_processstageparameter_MailboxTrackingFolders)
- [provisionlanguageforuser_MailboxTrackingFolders](#BKMK_provisionlanguageforuser_MailboxTrackingFolders)
- [recordfilter_MailboxTrackingFolders](#BKMK_recordfilter_MailboxTrackingFolders)
- [recyclebinconfig_MailboxTrackingFolders](#BKMK_recyclebinconfig_MailboxTrackingFolders)
- [relationshipattribute_MailboxTrackingFolders](#BKMK_relationshipattribute_MailboxTrackingFolders)
- [reportparameter_MailboxTrackingFolders](#BKMK_reportparameter_MailboxTrackingFolders)
- [retaineddataexcel_MailboxTrackingFolders](#BKMK_retaineddataexcel_MailboxTrackingFolders)
- [retentionconfig_MailboxTrackingFolders](#BKMK_retentionconfig_MailboxTrackingFolders)
- [retentionfailuredetail_MailboxTrackingFolders](#BKMK_retentionfailuredetail_MailboxTrackingFolders)
- [retentionoperation_MailboxTrackingFolders](#BKMK_retentionoperation_MailboxTrackingFolders)
- [retentionoperationdetail_MailboxTrackingFolders](#BKMK_retentionoperationdetail_MailboxTrackingFolders)
- [retentionsuccessdetail_MailboxTrackingFolders](#BKMK_retentionsuccessdetail_MailboxTrackingFolders)
- [roleeditorlayout_MailboxTrackingFolders](#BKMK_roleeditorlayout_MailboxTrackingFolders)
- [savingrule_MailboxTrackingFolders](#BKMK_savingrule_MailboxTrackingFolders)
- [searchattributesettings_MailboxTrackingFolders](#BKMK_searchattributesettings_MailboxTrackingFolders)
- [searchcustomanalyzer_MailboxTrackingFolders](#BKMK_searchcustomanalyzer_MailboxTrackingFolders)
- [searchrelationshipsettings_MailboxTrackingFolders](#BKMK_searchrelationshipsettings_MailboxTrackingFolders)
- [serviceplan_MailboxTrackingFolders](#BKMK_serviceplan_MailboxTrackingFolders)
- [serviceplanmapping_MailboxTrackingFolders](#BKMK_serviceplanmapping_MailboxTrackingFolders)
- [sharedlinksetting_MailboxTrackingFolders](#BKMK_sharedlinksetting_MailboxTrackingFolders)
- [sharedobject_MailboxTrackingFolders](#BKMK_sharedobject_MailboxTrackingFolders)
- [sharedworkspace_MailboxTrackingFolders](#BKMK_sharedworkspace_MailboxTrackingFolders)
- [sharedworkspacepool_MailboxTrackingFolders](#BKMK_sharedworkspacepool_MailboxTrackingFolders)
- [sharepointmanagedidentity_MailboxTrackingFolders](#BKMK_sharepointmanagedidentity_MailboxTrackingFolders)
- [sideloadedaiplugin_MailboxTrackingFolders](#BKMK_sideloadedaiplugin_MailboxTrackingFolders)
- [solutioncomponentattributeconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentattributeconfiguration_MailboxTrackingFolders)
- [solutioncomponentbatchconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentbatchconfiguration_MailboxTrackingFolders)
- [solutioncomponentconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentconfiguration_MailboxTrackingFolders)
- [solutioncomponentrelationshipconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders)
- [stagedentity_MailboxTrackingFolders](#BKMK_stagedentity_MailboxTrackingFolders)
- [stagedentityattribute_MailboxTrackingFolders](#BKMK_stagedentityattribute_MailboxTrackingFolders)
- [stagedmetadataasyncoperation_MailboxTrackingFolders](#BKMK_stagedmetadataasyncoperation_MailboxTrackingFolders)
- [stagesolutionupload_MailboxTrackingFolders](#BKMK_stagesolutionupload_MailboxTrackingFolders)
- [supportusertable_MailboxTrackingFolders](#BKMK_supportusertable_MailboxTrackingFolders)
- [synapsedatabase_MailboxTrackingFolders](#BKMK_synapsedatabase_MailboxTrackingFolders)
- [synapselinkexternaltablestate_MailboxTrackingFolders](#BKMK_synapselinkexternaltablestate_MailboxTrackingFolders)
- [synapselinkprofile_MailboxTrackingFolders](#BKMK_synapselinkprofile_MailboxTrackingFolders)
- [synapselinkprofileentity_MailboxTrackingFolders](#BKMK_synapselinkprofileentity_MailboxTrackingFolders)
- [synapselinkprofileentitystate_MailboxTrackingFolders](#BKMK_synapselinkprofileentitystate_MailboxTrackingFolders)
- [synapselinkschedule_MailboxTrackingFolders](#BKMK_synapselinkschedule_MailboxTrackingFolders)
- [systemuserauthorizationchangetracker_MailboxTrackingFolders](#BKMK_systemuserauthorizationchangetracker_MailboxTrackingFolders)
- [tag_MailboxTrackingFolders](#BKMK_tag_MailboxTrackingFolders)
- [taggedflowsession_MailboxTrackingFolders](#BKMK_taggedflowsession_MailboxTrackingFolders)
- [taggedprocess_MailboxTrackingFolders](#BKMK_taggedprocess_MailboxTrackingFolders)
- [team_mailboxtrackingfolder](#BKMK_team_mailboxtrackingfolder)
- [teammobileofflineprofilemembership_MailboxTrackingFolders](#BKMK_teammobileofflineprofilemembership_MailboxTrackingFolders)
- [territory_MailboxTrackingFolders](#BKMK_territory_MailboxTrackingFolders)
- [unstructuredfilesearchentity_MailboxTrackingFolders](#BKMK_unstructuredfilesearchentity_MailboxTrackingFolders)
- [unstructuredfilesearchrecord_MailboxTrackingFolders](#BKMK_unstructuredfilesearchrecord_MailboxTrackingFolders)
- [usermobileofflineprofilemembership_MailboxTrackingFolders](#BKMK_usermobileofflineprofilemembership_MailboxTrackingFolders)
- [userrating_MailboxTrackingFolders](#BKMK_userrating_MailboxTrackingFolders)
- [viewasexamplequestion_MailboxTrackingFolders](#BKMK_viewasexamplequestion_MailboxTrackingFolders)
- [virtualentitymetadata_MailboxTrackingFolders](#BKMK_virtualentitymetadata_MailboxTrackingFolders)
- [workflowbinary_MailboxTrackingFolders](#BKMK_workflowbinary_MailboxTrackingFolders)
- [workflowmetadata_MailboxTrackingFolders](#BKMK_workflowmetadata_MailboxTrackingFolders)
- [workqueue_MailboxTrackingFolders](#BKMK_workqueue_MailboxTrackingFolders)
- [workqueueitem_MailboxTrackingFolders](#BKMK_workqueueitem_MailboxTrackingFolders)

### <a name="BKMK_Account_MailboxTrackingFolder"></a> Account_MailboxTrackingFolder

One-To-Many Relationship: [account Account_MailboxTrackingFolder](account.md#BKMK_Account_MailboxTrackingFolder)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_activityfileattachment_MailboxTrackingFolders"></a> activityfileattachment_MailboxTrackingFolders

One-To-Many Relationship: [activityfileattachment activityfileattachment_MailboxTrackingFolders](activityfileattachment.md#BKMK_activityfileattachment_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`activityfileattachment`|
|ReferencedAttribute|`activityfileattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_activityfileattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_externalidentity_MailboxTrackingFolders"></a> adx_externalidentity_MailboxTrackingFolders

One-To-Many Relationship: [adx_externalidentity adx_externalidentity_MailboxTrackingFolders](adx_externalidentity.md#BKMK_adx_externalidentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_externalidentity`|
|ReferencedAttribute|`adx_externalidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_externalidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_MailboxTrackingFolders"></a> adx_invitation_MailboxTrackingFolders

One-To-Many Relationship: [adx_invitation adx_invitation_MailboxTrackingFolders](adx_invitation.md#BKMK_adx_invitation_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_invitation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_MailboxTrackingFolders"></a> adx_inviteredemption_MailboxTrackingFolders

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_MailboxTrackingFolders](adx_inviteredemption.md#BKMK_adx_inviteredemption_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_portalcomment_MailboxTrackingFolders"></a> adx_portalcomment_MailboxTrackingFolders

One-To-Many Relationship: [adx_portalcomment adx_portalcomment_MailboxTrackingFolders](adx_portalcomment.md#BKMK_adx_portalcomment_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_portalcomment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_portalcomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_setting_MailboxTrackingFolders"></a> adx_setting_MailboxTrackingFolders

One-To-Many Relationship: [adx_setting adx_setting_MailboxTrackingFolders](adx_setting.md#BKMK_adx_setting_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_setting`|
|ReferencedAttribute|`adx_settingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_setting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_webformsession_MailboxTrackingFolders"></a> adx_webformsession_MailboxTrackingFolders

One-To-Many Relationship: [adx_webformsession adx_webformsession_MailboxTrackingFolders](adx_webformsession.md#BKMK_adx_webformsession_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_webformsession`|
|ReferencedAttribute|`adx_webformsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_adx_webformsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aicopilot_MailboxTrackingFolders"></a> aicopilot_MailboxTrackingFolders

One-To-Many Relationship: [aicopilot aicopilot_MailboxTrackingFolders](aicopilot.md#BKMK_aicopilot_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aicopilot`|
|ReferencedAttribute|`aicopilotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aicopilot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugin_MailboxTrackingFolders"></a> aiplugin_MailboxTrackingFolders

One-To-Many Relationship: [aiplugin aiplugin_MailboxTrackingFolders](aiplugin.md#BKMK_aiplugin_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugin`|
|ReferencedAttribute|`aipluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginauth_MailboxTrackingFolders"></a> aipluginauth_MailboxTrackingFolders

One-To-Many Relationship: [aipluginauth aipluginauth_MailboxTrackingFolders](aipluginauth.md#BKMK_aipluginauth_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginauth`|
|ReferencedAttribute|`aipluginauthid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginauth`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstarter_MailboxTrackingFolders"></a> aipluginconversationstarter_MailboxTrackingFolders

One-To-Many Relationship: [aipluginconversationstarter aipluginconversationstarter_MailboxTrackingFolders](aipluginconversationstarter.md#BKMK_aipluginconversationstarter_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstarter`|
|ReferencedAttribute|`aipluginconversationstarterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginconversationstarter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstartermapping_MailboxTrackingFolders"></a> aipluginconversationstartermapping_MailboxTrackingFolders

One-To-Many Relationship: [aipluginconversationstartermapping aipluginconversationstartermapping_MailboxTrackingFolders](aipluginconversationstartermapping.md#BKMK_aipluginconversationstartermapping_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstartermapping`|
|ReferencedAttribute|`aipluginconversationstartermappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginconversationstartermapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschema_MailboxTrackingFolders"></a> aipluginexternalschema_MailboxTrackingFolders

One-To-Many Relationship: [aipluginexternalschema aipluginexternalschema_MailboxTrackingFolders](aipluginexternalschema.md#BKMK_aipluginexternalschema_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschema`|
|ReferencedAttribute|`aipluginexternalschemaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginexternalschema`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschemaproperty_MailboxTrackingFolders"></a> aipluginexternalschemaproperty_MailboxTrackingFolders

One-To-Many Relationship: [aipluginexternalschemaproperty aipluginexternalschemaproperty_MailboxTrackingFolders](aipluginexternalschemaproperty.md#BKMK_aipluginexternalschemaproperty_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschemaproperty`|
|ReferencedAttribute|`aipluginexternalschemapropertyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginexternalschemaproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernance_MailboxTrackingFolders"></a> aiplugingovernance_MailboxTrackingFolders

One-To-Many Relationship: [aiplugingovernance aiplugingovernance_MailboxTrackingFolders](aiplugingovernance.md#BKMK_aiplugingovernance_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernance`|
|ReferencedAttribute|`aiplugingovernanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugingovernance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernanceext_MailboxTrackingFolders"></a> aiplugingovernanceext_MailboxTrackingFolders

One-To-Many Relationship: [aiplugingovernanceext aiplugingovernanceext_MailboxTrackingFolders](aiplugingovernanceext.md#BKMK_aiplugingovernanceext_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernanceext`|
|ReferencedAttribute|`aiplugingovernanceextid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugingovernanceext`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugininstance_MailboxTrackingFolders"></a> aiplugininstance_MailboxTrackingFolders

One-To-Many Relationship: [aiplugininstance aiplugininstance_MailboxTrackingFolders](aiplugininstance.md#BKMK_aiplugininstance_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugininstance`|
|ReferencedAttribute|`aiplugininstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugininstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperation_MailboxTrackingFolders"></a> aipluginoperation_MailboxTrackingFolders

One-To-Many Relationship: [aipluginoperation aipluginoperation_MailboxTrackingFolders](aipluginoperation.md#BKMK_aipluginoperation_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperation`|
|ReferencedAttribute|`aipluginoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationparameter_MailboxTrackingFolders"></a> aipluginoperationparameter_MailboxTrackingFolders

One-To-Many Relationship: [aipluginoperationparameter aipluginoperationparameter_MailboxTrackingFolders](aipluginoperationparameter.md#BKMK_aipluginoperationparameter_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationparameter`|
|ReferencedAttribute|`aipluginoperationparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperationparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationresponsetemplate_MailboxTrackingFolders"></a> aipluginoperationresponsetemplate_MailboxTrackingFolders

One-To-Many Relationship: [aipluginoperationresponsetemplate aipluginoperationresponsetemplate_MailboxTrackingFolders](aipluginoperationresponsetemplate.md#BKMK_aipluginoperationresponsetemplate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationresponsetemplate`|
|ReferencedAttribute|`aipluginoperationresponsetemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginoperationresponsetemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugintitle_MailboxTrackingFolders"></a> aiplugintitle_MailboxTrackingFolders

One-To-Many Relationship: [aiplugintitle aiplugintitle_MailboxTrackingFolders](aiplugintitle.md#BKMK_aiplugintitle_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugintitle`|
|ReferencedAttribute|`aiplugintitleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aiplugintitle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginusersetting_MailboxTrackingFolders"></a> aipluginusersetting_MailboxTrackingFolders

One-To-Many Relationship: [aipluginusersetting aipluginusersetting_MailboxTrackingFolders](aipluginusersetting.md#BKMK_aipluginusersetting_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginusersetting`|
|ReferencedAttribute|`aipluginusersettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_aipluginusersetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appaction_MailboxTrackingFolders"></a> appaction_MailboxTrackingFolders

One-To-Many Relationship: [appaction appaction_MailboxTrackingFolders](appaction.md#BKMK_appaction_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`appaction`|
|ReferencedAttribute|`appactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionmigration_MailboxTrackingFolders"></a> appactionmigration_MailboxTrackingFolders

One-To-Many Relationship: [appactionmigration appactionmigration_MailboxTrackingFolders](appactionmigration.md#BKMK_appactionmigration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionmigration`|
|ReferencedAttribute|`appactionmigrationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appactionmigration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionrule_MailboxTrackingFolders"></a> appactionrule_MailboxTrackingFolders

One-To-Many Relationship: [appactionrule appactionrule_MailboxTrackingFolders](appactionrule.md#BKMK_appactionrule_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionrule`|
|ReferencedAttribute|`appactionruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_appactionrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_application_MailboxTrackingFolders"></a> application_MailboxTrackingFolders

One-To-Many Relationship: [application application_MailboxTrackingFolders](application.md#BKMK_application_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`application`|
|ReferencedAttribute|`applicationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_application`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_applicationuser_MailboxTrackingFolders"></a> applicationuser_MailboxTrackingFolders

One-To-Many Relationship: [applicationuser applicationuser_MailboxTrackingFolders](applicationuser.md#BKMK_applicationuser_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`applicationuser`|
|ReferencedAttribute|`applicationuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_applicationuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalprocess_MailboxTrackingFolders"></a> approvalprocess_MailboxTrackingFolders

One-To-Many Relationship: [approvalprocess approvalprocess_MailboxTrackingFolders](approvalprocess.md#BKMK_approvalprocess_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalprocess`|
|ReferencedAttribute|`approvalprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageapproval_MailboxTrackingFolders"></a> approvalstageapproval_MailboxTrackingFolders

One-To-Many Relationship: [approvalstageapproval approvalstageapproval_MailboxTrackingFolders](approvalstageapproval.md#BKMK_approvalstageapproval_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageapproval`|
|ReferencedAttribute|`approvalstageapprovalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstagecondition_MailboxTrackingFolders"></a> approvalstagecondition_MailboxTrackingFolders

One-To-Many Relationship: [approvalstagecondition approvalstagecondition_MailboxTrackingFolders](approvalstagecondition.md#BKMK_approvalstagecondition_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstagecondition`|
|ReferencedAttribute|`approvalstageconditionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstagecondition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_MailboxTrackingFolders"></a> approvalstageorder_MailboxTrackingFolders

One-To-Many Relationship: [approvalstageorder approvalstageorder_MailboxTrackingFolders](approvalstageorder.md#BKMK_approvalstageorder_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageorder`|
|ReferencedAttribute|`approvalstageorderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_approvalstageorder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_AsyncOperation_MailboxTrackingFolder"></a> AsyncOperation_MailboxTrackingFolder

One-To-Many Relationship: [asyncoperation AsyncOperation_MailboxTrackingFolder](asyncoperation.md#BKMK_AsyncOperation_MailboxTrackingFolder)

|Property|Value|
|---|---|
|ReferencedEntity|`asyncoperation`|
|ReferencedAttribute|`asyncoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_asyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_attributeimageconfig_MailboxTrackingFolders"></a> attributeimageconfig_MailboxTrackingFolders

One-To-Many Relationship: [attributeimageconfig attributeimageconfig_MailboxTrackingFolders](attributeimageconfig.md#BKMK_attributeimageconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`attributeimageconfig`|
|ReferencedAttribute|`attributeimageconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributeimageconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributemaskingrule_MailboxTrackingFolders"></a> attributemaskingrule_MailboxTrackingFolders

One-To-Many Relationship: [attributemaskingrule attributemaskingrule_MailboxTrackingFolders](attributemaskingrule.md#BKMK_attributemaskingrule_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`attributemaskingrule`|
|ReferencedAttribute|`attributemaskingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributemaskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributepicklistvalue_MailboxTrackingFolders"></a> attributepicklistvalue_MailboxTrackingFolders

One-To-Many Relationship: [attributepicklistvalue attributepicklistvalue_MailboxTrackingFolders](attributepicklistvalue.md#BKMK_attributepicklistvalue_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`attributepicklistvalue`|
|ReferencedAttribute|`attributepicklistvalueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_attributepicklistvalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_bot_MailboxTrackingFolders"></a> bot_MailboxTrackingFolders

One-To-Many Relationship: [bot bot_MailboxTrackingFolders](bot.md#BKMK_bot_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`bot`|
|ReferencedAttribute|`botid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_bot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponent_MailboxTrackingFolders"></a> botcomponent_MailboxTrackingFolders

One-To-Many Relationship: [botcomponent botcomponent_MailboxTrackingFolders](botcomponent.md#BKMK_botcomponent_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponent`|
|ReferencedAttribute|`botcomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_botcomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponentcollection_MailboxTrackingFolders"></a> botcomponentcollection_MailboxTrackingFolders

One-To-Many Relationship: [botcomponentcollection botcomponentcollection_MailboxTrackingFolders](botcomponentcollection.md#BKMK_botcomponentcollection_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponentcollection`|
|ReferencedAttribute|`botcomponentcollectionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_botcomponentcollection`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_businessprocess_MailboxTrackingFolders"></a> businessprocess_MailboxTrackingFolders

One-To-Many Relationship: [businessprocess businessprocess_MailboxTrackingFolders](businessprocess.md#BKMK_businessprocess_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`businessprocess`|
|ReferencedAttribute|`businessprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_businessprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_businessunit_mailboxtrackingfolder"></a> businessunit_mailboxtrackingfolder

One-To-Many Relationship: [businessunit businessunit_mailboxtrackingfolder](businessunit.md#BKMK_businessunit_mailboxtrackingfolder)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_card_MailboxTrackingFolders"></a> card_MailboxTrackingFolders

One-To-Many Relationship: [card card_MailboxTrackingFolders](card.md#BKMK_card_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`card`|
|ReferencedAttribute|`cardid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_card`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalog_MailboxTrackingFolders"></a> catalog_MailboxTrackingFolders

One-To-Many Relationship: [catalog catalog_MailboxTrackingFolders](catalog.md#BKMK_catalog_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`catalog`|
|ReferencedAttribute|`catalogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_catalog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalogassignment_MailboxTrackingFolders"></a> catalogassignment_MailboxTrackingFolders

One-To-Many Relationship: [catalogassignment catalogassignment_MailboxTrackingFolders](catalogassignment.md#BKMK_catalogassignment_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`catalogassignment`|
|ReferencedAttribute|`catalogassignmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_catalogassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_certificatecredential_MailboxTrackingFolders"></a> certificatecredential_MailboxTrackingFolders

One-To-Many Relationship: [certificatecredential certificatecredential_MailboxTrackingFolders](certificatecredential.md#BKMK_certificatecredential_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`certificatecredential`|
|ReferencedAttribute|`certificatecredentialid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_certificatecredential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_chat_MailboxTrackingFolders"></a> chat_MailboxTrackingFolders

One-To-Many Relationship: [chat chat_MailboxTrackingFolders](chat.md#BKMK_chat_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`chat`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_chat`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectioninstance_MailboxTrackingFolders"></a> connectioninstance_MailboxTrackingFolders

One-To-Many Relationship: [connectioninstance connectioninstance_MailboxTrackingFolders](connectioninstance.md#BKMK_connectioninstance_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`connectioninstance`|
|ReferencedAttribute|`connectioninstanceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectioninstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectionreference_MailboxTrackingFolders"></a> connectionreference_MailboxTrackingFolders

One-To-Many Relationship: [connectionreference connectionreference_MailboxTrackingFolders](connectionreference.md#BKMK_connectionreference_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionreference`|
|ReferencedAttribute|`connectionreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connector_MailboxTrackingFolders"></a> connector_MailboxTrackingFolders

One-To-Many Relationship: [connector connector_MailboxTrackingFolders](connector.md#BKMK_connector_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`connector`|
|ReferencedAttribute|`connectorid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_connector`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_MailboxTrackingFolder"></a> Contact_MailboxTrackingFolder

One-To-Many Relationship: [contact Contact_MailboxTrackingFolder](contact.md#BKMK_Contact_MailboxTrackingFolder)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_conversationtranscript_MailboxTrackingFolders"></a> conversationtranscript_MailboxTrackingFolders

One-To-Many Relationship: [conversationtranscript conversationtranscript_MailboxTrackingFolders](conversationtranscript.md#BKMK_conversationtranscript_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`conversationtranscript`|
|ReferencedAttribute|`conversationtranscriptid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_conversationtranscript`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotexamplequestion_MailboxTrackingFolders"></a> copilotexamplequestion_MailboxTrackingFolders

One-To-Many Relationship: [copilotexamplequestion copilotexamplequestion_MailboxTrackingFolders](copilotexamplequestion.md#BKMK_copilotexamplequestion_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotexamplequestion`|
|ReferencedAttribute|`copilotexamplequestionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotglossaryterm_MailboxTrackingFolders"></a> copilotglossaryterm_MailboxTrackingFolders

One-To-Many Relationship: [copilotglossaryterm copilotglossaryterm_MailboxTrackingFolders](copilotglossaryterm.md#BKMK_copilotglossaryterm_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotglossaryterm`|
|ReferencedAttribute|`copilotglossarytermid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotglossaryterm`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotsynonyms_MailboxTrackingFolders"></a> copilotsynonyms_MailboxTrackingFolders

One-To-Many Relationship: [copilotsynonyms copilotsynonyms_MailboxTrackingFolders](copilotsynonyms.md#BKMK_copilotsynonyms_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotsynonyms`|
|ReferencedAttribute|`copilotsynonymsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_copilotsynonyms`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_credential_MailboxTrackingFolders"></a> credential_MailboxTrackingFolders

One-To-Many Relationship: [credential credential_MailboxTrackingFolders](credential.md#BKMK_credential_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`credential`|
|ReferencedAttribute|`credentialid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_credential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapi_MailboxTrackingFolders"></a> customapi_MailboxTrackingFolders

One-To-Many Relationship: [customapi customapi_MailboxTrackingFolders](customapi.md#BKMK_customapi_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`customapi`|
|ReferencedAttribute|`customapiid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapirequestparameter_MailboxTrackingFolders"></a> customapirequestparameter_MailboxTrackingFolders

One-To-Many Relationship: [customapirequestparameter customapirequestparameter_MailboxTrackingFolders](customapirequestparameter.md#BKMK_customapirequestparameter_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`customapirequestparameter`|
|ReferencedAttribute|`customapirequestparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapirequestparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapiresponseproperty_MailboxTrackingFolders"></a> customapiresponseproperty_MailboxTrackingFolders

One-To-Many Relationship: [customapiresponseproperty customapiresponseproperty_MailboxTrackingFolders](customapiresponseproperty.md#BKMK_customapiresponseproperty_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`customapiresponseproperty`|
|ReferencedAttribute|`customapiresponsepropertyid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_customapiresponseproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolder_MailboxTrackingFolders"></a> datalakefolder_MailboxTrackingFolders

One-To-Many Relationship: [datalakefolder datalakefolder_MailboxTrackingFolders](datalakefolder.md#BKMK_datalakefolder_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolder`|
|ReferencedAttribute|`datalakefolderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolderpermission_MailboxTrackingFolders"></a> datalakefolderpermission_MailboxTrackingFolders

One-To-Many Relationship: [datalakefolderpermission datalakefolderpermission_MailboxTrackingFolders](datalakefolderpermission.md#BKMK_datalakefolderpermission_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolderpermission`|
|ReferencedAttribute|`datalakefolderpermissionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakefolderpermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspace_MailboxTrackingFolders"></a> datalakeworkspace_MailboxTrackingFolders

One-To-Many Relationship: [datalakeworkspace datalakeworkspace_MailboxTrackingFolders](datalakeworkspace.md#BKMK_datalakeworkspace_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspace`|
|ReferencedAttribute|`datalakeworkspaceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakeworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspacepermission_MailboxTrackingFolders"></a> datalakeworkspacepermission_MailboxTrackingFolders

One-To-Many Relationship: [datalakeworkspacepermission datalakeworkspacepermission_MailboxTrackingFolders](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspacepermission`|
|ReferencedAttribute|`datalakeworkspacepermissionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_datalakeworkspacepermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dataprocessingconfiguration_MailboxTrackingFolders"></a> dataprocessingconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [dataprocessingconfiguration dataprocessingconfiguration_MailboxTrackingFolders](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`dataprocessingconfiguration`|
|ReferencedAttribute|`dataprocessingconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dataprocessingconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_delegatedauthorization_MailboxTrackingFolders"></a> delegatedauthorization_MailboxTrackingFolders

One-To-Many Relationship: [delegatedauthorization delegatedauthorization_MailboxTrackingFolders](delegatedauthorization.md#BKMK_delegatedauthorization_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`delegatedauthorization`|
|ReferencedAttribute|`delegatedauthorizationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_delegatedauthorization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowbinary_MailboxTrackingFolders"></a> desktopflowbinary_MailboxTrackingFolders

One-To-Many Relationship: [desktopflowbinary desktopflowbinary_MailboxTrackingFolders](desktopflowbinary.md#BKMK_desktopflowbinary_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowbinary`|
|ReferencedAttribute|`desktopflowbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_desktopflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowmodule_MailboxTrackingFolders"></a> desktopflowmodule_MailboxTrackingFolders

One-To-Many Relationship: [desktopflowmodule desktopflowmodule_MailboxTrackingFolders](desktopflowmodule.md#BKMK_desktopflowmodule_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowmodule`|
|ReferencedAttribute|`desktopflowmoduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_desktopflowmodule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearch_MailboxTrackingFolders"></a> dvfilesearch_MailboxTrackingFolders

One-To-Many Relationship: [dvfilesearch dvfilesearch_MailboxTrackingFolders](dvfilesearch.md#BKMK_dvfilesearch_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearch`|
|ReferencedAttribute|`dvfilesearchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchattribute_MailboxTrackingFolders"></a> dvfilesearchattribute_MailboxTrackingFolders

One-To-Many Relationship: [dvfilesearchattribute dvfilesearchattribute_MailboxTrackingFolders](dvfilesearchattribute.md#BKMK_dvfilesearchattribute_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchattribute`|
|ReferencedAttribute|`dvfilesearchattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchentity_MailboxTrackingFolders"></a> dvfilesearchentity_MailboxTrackingFolders

One-To-Many Relationship: [dvfilesearchentity dvfilesearchentity_MailboxTrackingFolders](dvfilesearchentity.md#BKMK_dvfilesearchentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchentity`|
|ReferencedAttribute|`dvfilesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearch_MailboxTrackingFolders"></a> dvtablesearch_MailboxTrackingFolders

One-To-Many Relationship: [dvtablesearch dvtablesearch_MailboxTrackingFolders](dvtablesearch.md#BKMK_dvtablesearch_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearch`|
|ReferencedAttribute|`dvtablesearchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchattribute_MailboxTrackingFolders"></a> dvtablesearchattribute_MailboxTrackingFolders

One-To-Many Relationship: [dvtablesearchattribute dvtablesearchattribute_MailboxTrackingFolders](dvtablesearchattribute.md#BKMK_dvtablesearchattribute_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchattribute`|
|ReferencedAttribute|`dvtablesearchattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchentity_MailboxTrackingFolders"></a> dvtablesearchentity_MailboxTrackingFolders

One-To-Many Relationship: [dvtablesearchentity dvtablesearchentity_MailboxTrackingFolders](dvtablesearchentity.md#BKMK_dvtablesearchentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchentity`|
|ReferencedAttribute|`dvtablesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_dvtablesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_emailaddressconfiguration_MailboxTrackingFolders"></a> emailaddressconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [emailaddressconfiguration emailaddressconfiguration_MailboxTrackingFolders](emailaddressconfiguration.md#BKMK_emailaddressconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`emailaddressconfiguration`|
|ReferencedAttribute|`emailaddressconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_emailaddressconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityanalyticsconfig_MailboxTrackingFolders"></a> entityanalyticsconfig_MailboxTrackingFolders

One-To-Many Relationship: [entityanalyticsconfig entityanalyticsconfig_MailboxTrackingFolders](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`entityanalyticsconfig`|
|ReferencedAttribute|`entityanalyticsconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityanalyticsconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityclusterconfig_MailboxTrackingFolders"></a> entityclusterconfig_MailboxTrackingFolders

One-To-Many Relationship: [entityclusterconfig entityclusterconfig_MailboxTrackingFolders](entityclusterconfig.md#BKMK_entityclusterconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`entityclusterconfig`|
|ReferencedAttribute|`entityclusterconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityclusterconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityimageconfig_MailboxTrackingFolders"></a> entityimageconfig_MailboxTrackingFolders

One-To-Many Relationship: [entityimageconfig entityimageconfig_MailboxTrackingFolders](entityimageconfig.md#BKMK_entityimageconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`entityimageconfig`|
|ReferencedAttribute|`entityimageconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityimageconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityindex_MailboxTrackingFolders"></a> entityindex_MailboxTrackingFolders

One-To-Many Relationship: [entityindex entityindex_MailboxTrackingFolders](entityindex.md#BKMK_entityindex_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`entityindex`|
|ReferencedAttribute|`indexid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityindex`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityrecordfilter_MailboxTrackingFolders"></a> entityrecordfilter_MailboxTrackingFolders

One-To-Many Relationship: [entityrecordfilter entityrecordfilter_MailboxTrackingFolders](entityrecordfilter.md#BKMK_entityrecordfilter_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`entityrecordfilter`|
|ReferencedAttribute|`entityrecordfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_entityrecordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_MailboxTrackingFolders"></a> environmentvariabledefinition_MailboxTrackingFolders

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_MailboxTrackingFolders](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_environmentvariabledefinition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariablevalue_MailboxTrackingFolders"></a> environmentvariablevalue_MailboxTrackingFolders

One-To-Many Relationship: [environmentvariablevalue environmentvariablevalue_MailboxTrackingFolders](environmentvariablevalue.md#BKMK_environmentvariablevalue_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariablevalue`|
|ReferencedAttribute|`environmentvariablevalueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_environmentvariablevalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportedexcel_MailboxTrackingFolders"></a> exportedexcel_MailboxTrackingFolders

One-To-Many Relationship: [exportedexcel exportedexcel_MailboxTrackingFolders](exportedexcel.md#BKMK_exportedexcel_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`exportedexcel`|
|ReferencedAttribute|`exportedexcelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_exportedexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportsolutionupload_MailboxTrackingFolders"></a> exportsolutionupload_MailboxTrackingFolders

One-To-Many Relationship: [exportsolutionupload exportsolutionupload_MailboxTrackingFolders](exportsolutionupload.md#BKMK_exportsolutionupload_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`exportsolutionupload`|
|ReferencedAttribute|`exportsolutionuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_exportsolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fabricaiskill_MailboxTrackingFolders"></a> fabricaiskill_MailboxTrackingFolders

One-To-Many Relationship: [fabricaiskill fabricaiskill_MailboxTrackingFolders](fabricaiskill.md#BKMK_fabricaiskill_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`fabricaiskill`|
|ReferencedAttribute|`fabricaiskillid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fabricaiskill`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_featurecontrolsetting_MailboxTrackingFolders"></a> featurecontrolsetting_MailboxTrackingFolders

One-To-Many Relationship: [featurecontrolsetting featurecontrolsetting_MailboxTrackingFolders](featurecontrolsetting.md#BKMK_featurecontrolsetting_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`featurecontrolsetting`|
|ReferencedAttribute|`featurecontrolsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_featurecontrolsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeconfiguration_MailboxTrackingFolders"></a> federatedknowledgeconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [federatedknowledgeconfiguration federatedknowledgeconfiguration_MailboxTrackingFolders](federatedknowledgeconfiguration.md#BKMK_federatedknowledgeconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeconfiguration`|
|ReferencedAttribute|`federatedknowledgeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_federatedknowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeentityconfiguration_MailboxTrackingFolders"></a> federatedknowledgeentityconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [federatedknowledgeentityconfiguration federatedknowledgeentityconfiguration_MailboxTrackingFolders](federatedknowledgeentityconfiguration.md#BKMK_federatedknowledgeentityconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeentityconfiguration`|
|ReferencedAttribute|`federatedknowledgeentityconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_federatedknowledgeentityconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcapacityassignment_MailboxTrackingFolders"></a> flowcapacityassignment_MailboxTrackingFolders

One-To-Many Relationship: [flowcapacityassignment flowcapacityassignment_MailboxTrackingFolders](flowcapacityassignment.md#BKMK_flowcapacityassignment_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcapacityassignment`|
|ReferencedAttribute|`flowcapacityassignmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowcapacityassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcredentialapplication_MailboxTrackingFolders"></a> flowcredentialapplication_MailboxTrackingFolders

One-To-Many Relationship: [flowcredentialapplication flowcredentialapplication_MailboxTrackingFolders](flowcredentialapplication.md#BKMK_flowcredentialapplication_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcredentialapplication`|
|ReferencedAttribute|`flowcredentialapplicationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowcredentialapplication`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowevent_MailboxTrackingFolders"></a> flowevent_MailboxTrackingFolders

One-To-Many Relationship: [flowevent flowevent_MailboxTrackingFolders](flowevent.md#BKMK_flowevent_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`flowevent`|
|ReferencedAttribute|`floweventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachine_MailboxTrackingFolders"></a> flowmachine_MailboxTrackingFolders

One-To-Many Relationship: [flowmachine flowmachine_MailboxTrackingFolders](flowmachine.md#BKMK_flowmachine_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachine`|
|ReferencedAttribute|`flowmachineid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachine`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_MailboxTrackingFolders"></a> flowmachinegroup_MailboxTrackingFolders

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_MailboxTrackingFolders](flowmachinegroup.md#BKMK_flowmachinegroup_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachinegroup`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimage_MailboxTrackingFolders"></a> flowmachineimage_MailboxTrackingFolders

One-To-Many Relationship: [flowmachineimage flowmachineimage_MailboxTrackingFolders](flowmachineimage.md#BKMK_flowmachineimage_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimage`|
|ReferencedAttribute|`flowmachineimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachineimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimageversion_MailboxTrackingFolders"></a> flowmachineimageversion_MailboxTrackingFolders

One-To-Many Relationship: [flowmachineimageversion flowmachineimageversion_MailboxTrackingFolders](flowmachineimageversion.md#BKMK_flowmachineimageversion_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimageversion`|
|ReferencedAttribute|`flowmachineimageversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachineimageversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinenetwork_MailboxTrackingFolders"></a> flowmachinenetwork_MailboxTrackingFolders

One-To-Many Relationship: [flowmachinenetwork flowmachinenetwork_MailboxTrackingFolders](flowmachinenetwork.md#BKMK_flowmachinenetwork_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinenetwork`|
|ReferencedAttribute|`flowmachinenetworkid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowmachinenetwork`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsession_MailboxTrackingFolders"></a> flowsession_MailboxTrackingFolders

One-To-Many Relationship: [flowsession flowsession_MailboxTrackingFolders](flowsession.md#BKMK_flowsession_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsession`|
|ReferencedAttribute|`flowsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_flowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fxexpression_MailboxTrackingFolders"></a> fxexpression_MailboxTrackingFolders

One-To-Many Relationship: [fxexpression fxexpression_MailboxTrackingFolders](fxexpression.md#BKMK_fxexpression_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`fxexpression`|
|ReferencedAttribute|`fxexpressionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_fxexpression`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_governanceconfiguration_MailboxTrackingFolders"></a> governanceconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [governanceconfiguration governanceconfiguration_MailboxTrackingFolders](governanceconfiguration.md#BKMK_governanceconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`governanceconfiguration`|
|ReferencedAttribute|`governanceconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_governanceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_indexattributes_MailboxTrackingFolders"></a> indexattributes_MailboxTrackingFolders

One-To-Many Relationship: [indexattributes indexattributes_MailboxTrackingFolders](indexattributes.md#BKMK_indexattributes_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`indexattributes`|
|ReferencedAttribute|`indexattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_indexattributes`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_keyvaultreference_MailboxTrackingFolders"></a> keyvaultreference_MailboxTrackingFolders

One-To-Many Relationship: [keyvaultreference keyvaultreference_MailboxTrackingFolders](keyvaultreference.md#BKMK_keyvaultreference_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`keyvaultreference`|
|ReferencedAttribute|`keyvaultreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_keyvaultreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mailboxtrackingfolder_createdby"></a> lk_mailboxtrackingfolder_createdby

One-To-Many Relationship: [systemuser lk_mailboxtrackingfolder_createdby](systemuser.md#BKMK_lk_mailboxtrackingfolder_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mailboxtrackingfolder_createdonbehalfby"></a> lk_mailboxtrackingfolder_createdonbehalfby

One-To-Many Relationship: [systemuser lk_mailboxtrackingfolder_createdonbehalfby](systemuser.md#BKMK_lk_mailboxtrackingfolder_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mailboxtrackingfolder_modifiedby"></a> lk_mailboxtrackingfolder_modifiedby

One-To-Many Relationship: [systemuser lk_mailboxtrackingfolder_modifiedby](systemuser.md#BKMK_lk_mailboxtrackingfolder_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby"></a> lk_mailboxtrackingfolder_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_mailboxtrackingfolder_modifiedonbehalfby](systemuser.md#BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Mailbox_MailboxTrackingFolder"></a> Mailbox_MailboxTrackingFolder

One-To-Many Relationship: [mailbox Mailbox_MailboxTrackingFolder](mailbox.md#BKMK_Mailbox_MailboxTrackingFolder)

|Property|Value|
|---|---|
|ReferencedEntity|`mailbox`|
|ReferencedAttribute|`mailboxid`|
|ReferencingAttribute|`mailboxid`|
|ReferencingEntityNavigationPropertyName|`mailboxid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mainfewshot_MailboxTrackingFolders"></a> mainfewshot_MailboxTrackingFolders

One-To-Many Relationship: [mainfewshot mainfewshot_MailboxTrackingFolders](mainfewshot.md#BKMK_mainfewshot_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`mainfewshot`|
|ReferencedAttribute|`mainfewshotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mainfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_makerfewshot_MailboxTrackingFolders"></a> makerfewshot_MailboxTrackingFolders

One-To-Many Relationship: [makerfewshot makerfewshot_MailboxTrackingFolders](makerfewshot.md#BKMK_makerfewshot_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`makerfewshot`|
|ReferencedAttribute|`makerfewshotid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_makerfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_MailboxTrackingFolders"></a> managedidentity_MailboxTrackingFolders

One-To-Many Relationship: [managedidentity managedidentity_MailboxTrackingFolders](managedidentity.md#BKMK_managedidentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_managedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_maskingrule_MailboxTrackingFolders"></a> maskingrule_MailboxTrackingFolders

One-To-Many Relationship: [maskingrule maskingrule_MailboxTrackingFolders](maskingrule.md#BKMK_maskingrule_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`maskingrule`|
|ReferencedAttribute|`maskingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_maskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_metadataforarchival_MailboxTrackingFolders"></a> metadataforarchival_MailboxTrackingFolders

One-To-Many Relationship: [metadataforarchival metadataforarchival_MailboxTrackingFolders](metadataforarchival.md#BKMK_metadataforarchival_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`metadataforarchival`|
|ReferencedAttribute|`metadataforarchivalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_metadataforarchival`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mobileofflineprofileextension_MailboxTrackingFolders"></a> mobileofflineprofileextension_MailboxTrackingFolders

One-To-Many Relationship: [mobileofflineprofileextension mobileofflineprofileextension_MailboxTrackingFolders](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofileextension`|
|ReferencedAttribute|`mobileofflineprofileextensionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mobileofflineprofileextension`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdataset_MailboxTrackingFolders"></a> msdyn_aibdataset_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aibdataset msdyn_aibdataset_MailboxTrackingFolders](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdataset`|
|ReferencedAttribute|`msdyn_aibdatasetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetfile_MailboxTrackingFolders"></a> msdyn_aibdatasetfile_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aibdatasetfile msdyn_aibdatasetfile_MailboxTrackingFolders](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetfile`|
|ReferencedAttribute|`msdyn_aibdatasetfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetrecord_MailboxTrackingFolders"></a> msdyn_aibdatasetrecord_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aibdatasetrecord msdyn_aibdatasetrecord_MailboxTrackingFolders](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetrecord`|
|ReferencedAttribute|`msdyn_aibdatasetrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetscontainer_MailboxTrackingFolders"></a> msdyn_aibdatasetscontainer_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aibdatasetscontainer msdyn_aibdatasetscontainer_MailboxTrackingFolders](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetscontainer`|
|ReferencedAttribute|`msdyn_aibdatasetscontainerid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibdatasetscontainer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfeedbackloop_MailboxTrackingFolders"></a> msdyn_aibfeedbackloop_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aibfeedbackloop msdyn_aibfeedbackloop_MailboxTrackingFolders](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfeedbackloop`|
|ReferencedAttribute|`msdyn_aibfeedbackloopid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfeedbackloop`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfile_MailboxTrackingFolders"></a> msdyn_aibfile_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aibfile msdyn_aibfile_MailboxTrackingFolders](msdyn_aibfile.md#BKMK_msdyn_aibfile_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfile`|
|ReferencedAttribute|`msdyn_aibfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfileattacheddata_MailboxTrackingFolders"></a> msdyn_aibfileattacheddata_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aibfileattacheddata msdyn_aibfileattacheddata_MailboxTrackingFolders](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfileattacheddata`|
|ReferencedAttribute|`msdyn_aibfileattacheddataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aibfileattacheddata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiconfiguration_MailboxTrackingFolders"></a> msdyn_aiconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aiconfiguration msdyn_aiconfiguration_MailboxTrackingFolders](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfiguration`|
|ReferencedAttribute|`msdyn_aiconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aidataprocessingevent_MailboxTrackingFolders"></a> msdyn_aidataprocessingevent_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aidataprocessingevent msdyn_aidataprocessingevent_MailboxTrackingFolders](msdyn_aidataprocessingevent.md#BKMK_msdyn_aidataprocessingevent_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aidataprocessingevent`|
|ReferencedAttribute|`msdyn_aidataprocessingeventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aidataprocessingevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationconfiguration_MailboxTrackingFolders"></a> msdyn_aievaluationconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aievaluationconfiguration msdyn_aievaluationconfiguration_MailboxTrackingFolders](msdyn_aievaluationconfiguration.md#BKMK_msdyn_aievaluationconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationconfiguration`|
|ReferencedAttribute|`msdyn_aievaluationconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievaluationconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationrun_MailboxTrackingFolders"></a> msdyn_aievaluationrun_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aievaluationrun msdyn_aievaluationrun_MailboxTrackingFolders](msdyn_aievaluationrun.md#BKMK_msdyn_aievaluationrun_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationrun`|
|ReferencedAttribute|`msdyn_aievaluationrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievaluationrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievent_MailboxTrackingFolders"></a> msdyn_aievent_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aievent msdyn_aievent_MailboxTrackingFolders](msdyn_aievent.md#BKMK_msdyn_aievent_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievent`|
|ReferencedAttribute|`msdyn_aieventid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aievent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aifptrainingdocument_MailboxTrackingFolders"></a> msdyn_aifptrainingdocument_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aifptrainingdocument msdyn_aifptrainingdocument_MailboxTrackingFolders](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aifptrainingdocument`|
|ReferencedAttribute|`msdyn_aifptrainingdocumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aifptrainingdocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aimodel_MailboxTrackingFolders"></a> msdyn_aimodel_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aimodel msdyn_aimodel_MailboxTrackingFolders](msdyn_aimodel.md#BKMK_msdyn_aimodel_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aimodel`|
|ReferencedAttribute|`msdyn_aimodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aimodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodimage_MailboxTrackingFolders"></a> msdyn_aiodimage_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aiodimage msdyn_aiodimage_MailboxTrackingFolders](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodimage`|
|ReferencedAttribute|`msdyn_aiodimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodlabel_MailboxTrackingFolders"></a> msdyn_aiodlabel_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aiodlabel msdyn_aiodlabel_MailboxTrackingFolders](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodlabel`|
|ReferencedAttribute|`msdyn_aiodlabelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodlabel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingboundingbox_MailboxTrackingFolders"></a> msdyn_aiodtrainingboundingbox_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aiodtrainingboundingbox msdyn_aiodtrainingboundingbox_MailboxTrackingFolders](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencedAttribute|`msdyn_aiodtrainingboundingboxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodtrainingboundingbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingimage_MailboxTrackingFolders"></a> msdyn_aiodtrainingimage_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aiodtrainingimage msdyn_aiodtrainingimage_MailboxTrackingFolders](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingimage`|
|ReferencedAttribute|`msdyn_aiodtrainingimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aiodtrainingimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitemplate_MailboxTrackingFolders"></a> msdyn_aitemplate_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aitemplate msdyn_aitemplate_MailboxTrackingFolders](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitemplate`|
|ReferencedAttribute|`msdyn_aitemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcase_MailboxTrackingFolders"></a> msdyn_aitestcase_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aitestcase msdyn_aitestcase_MailboxTrackingFolders](msdyn_aitestcase.md#BKMK_msdyn_aitestcase_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcase`|
|ReferencedAttribute|`msdyn_aitestcaseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcasedocument_MailboxTrackingFolders"></a> msdyn_aitestcasedocument_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aitestcasedocument msdyn_aitestcasedocument_MailboxTrackingFolders](msdyn_aitestcasedocument.md#BKMK_msdyn_aitestcasedocument_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcasedocument`|
|ReferencedAttribute|`msdyn_aitestcasedocumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcasedocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcaseinput_MailboxTrackingFolders"></a> msdyn_aitestcaseinput_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aitestcaseinput msdyn_aitestcaseinput_MailboxTrackingFolders](msdyn_aitestcaseinput.md#BKMK_msdyn_aitestcaseinput_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcaseinput`|
|ReferencedAttribute|`msdyn_aitestcaseinputid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestcaseinput`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrun_MailboxTrackingFolders"></a> msdyn_aitestrun_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aitestrun msdyn_aitestrun_MailboxTrackingFolders](msdyn_aitestrun.md#BKMK_msdyn_aitestrun_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrun`|
|ReferencedAttribute|`msdyn_aitestrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrunbatch_MailboxTrackingFolders"></a> msdyn_aitestrunbatch_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_aitestrunbatch msdyn_aitestrunbatch_MailboxTrackingFolders](msdyn_aitestrunbatch.md#BKMK_msdyn_aitestrunbatch_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrunbatch`|
|ReferencedAttribute|`msdyn_aitestrunbatchid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_aitestrunbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysiscomponent_MailboxTrackingFolders"></a> msdyn_analysiscomponent_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_analysiscomponent msdyn_analysiscomponent_MailboxTrackingFolders](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysiscomponent`|
|ReferencedAttribute|`msdyn_analysiscomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysiscomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_MailboxTrackingFolders"></a> msdyn_analysisjob_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_MailboxTrackingFolders](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisjob`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisoverride_MailboxTrackingFolders"></a> msdyn_analysisoverride_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_analysisoverride msdyn_analysisoverride_MailboxTrackingFolders](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisoverride`|
|ReferencedAttribute|`msdyn_analysisoverrideid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisoverride`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresult_MailboxTrackingFolders"></a> msdyn_analysisresult_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_analysisresult msdyn_analysisresult_MailboxTrackingFolders](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresult`|
|ReferencedAttribute|`msdyn_analysisresultid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisresult`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresultdetail_MailboxTrackingFolders"></a> msdyn_analysisresultdetail_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_analysisresultdetail msdyn_analysisresultdetail_MailboxTrackingFolders](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresultdetail`|
|ReferencedAttribute|`msdyn_analysisresultdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_analysisresultdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_appinsightsmetadata_MailboxTrackingFolders"></a> msdyn_appinsightsmetadata_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_appinsightsmetadata msdyn_appinsightsmetadata_MailboxTrackingFolders](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_appinsightsmetadata`|
|ReferencedAttribute|`msdyn_appinsightsmetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_appinsightsmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_copilotinteractions_MailboxTrackingFolders"></a> msdyn_copilotinteractions_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_copilotinteractions msdyn_copilotinteractions_MailboxTrackingFolders](msdyn_copilotinteractions.md#BKMK_msdyn_copilotinteractions_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_copilotinteractions`|
|ReferencedAttribute|`msdyn_copilotinteractionsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_copilotinteractions`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders"></a> msdyn_customcontrolextendedsettings_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_customcontrolextendedsettings msdyn_customcontrolextendedsettings_MailboxTrackingFolders](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_customcontrolextendedsettings`|
|ReferencedAttribute|`msdyn_customcontrolextendedsettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_customcontrolextendedsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_datalakefolder_MailboxTrackingFolders"></a> msdyn_dataflow_datalakefolder_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_dataflow_datalakefolder msdyn_dataflow_datalakefolder_MailboxTrackingFolders](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow_datalakefolder`|
|ReferencedAttribute|`msdyn_dataflow_datalakefolderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflow_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_MailboxTrackingFolders"></a> msdyn_dataflow_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_dataflow msdyn_dataflow_MailboxTrackingFolders](msdyn_dataflow.md#BKMK_msdyn_dataflow_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow`|
|ReferencedAttribute|`msdyn_dataflowid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowconnectionreference_MailboxTrackingFolders"></a> msdyn_dataflowconnectionreference_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_dataflowconnectionreference msdyn_dataflowconnectionreference_MailboxTrackingFolders](msdyn_dataflowconnectionreference.md#BKMK_msdyn_dataflowconnectionreference_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowconnectionreference`|
|ReferencedAttribute|`msdyn_dataflowconnectionreferenceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowconnectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowrefreshhistory_MailboxTrackingFolders"></a> msdyn_dataflowrefreshhistory_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_dataflowrefreshhistory msdyn_dataflowrefreshhistory_MailboxTrackingFolders](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowrefreshhistory`|
|ReferencedAttribute|`msdyn_dataflowrefreshhistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowtemplate_MailboxTrackingFolders"></a> msdyn_dataflowtemplate_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_dataflowtemplate msdyn_dataflowtemplate_MailboxTrackingFolders](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowtemplate`|
|ReferencedAttribute|`msdyn_dataflowtemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dataflowtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequest_MailboxTrackingFolders"></a> msdyn_dmsrequest_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_dmsrequest msdyn_dmsrequest_MailboxTrackingFolders](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequest`|
|ReferencedAttribute|`msdyn_dmsrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmsrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequeststatus_MailboxTrackingFolders"></a> msdyn_dmsrequeststatus_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_dmsrequeststatus msdyn_dmsrequeststatus_MailboxTrackingFolders](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequeststatus`|
|ReferencedAttribute|`msdyn_dmsrequeststatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmsrequeststatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncrequest_MailboxTrackingFolders"></a> msdyn_dmssyncrequest_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_dmssyncrequest msdyn_dmssyncrequest_MailboxTrackingFolders](msdyn_dmssyncrequest.md#BKMK_msdyn_dmssyncrequest_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncrequest`|
|ReferencedAttribute|`msdyn_dmssyncrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmssyncrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncstatus_MailboxTrackingFolders"></a> msdyn_dmssyncstatus_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_dmssyncstatus msdyn_dmssyncstatus_MailboxTrackingFolders](msdyn_dmssyncstatus.md#BKMK_msdyn_dmssyncstatus_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncstatus`|
|ReferencedAttribute|`msdyn_dmssyncstatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_dmssyncstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders"></a> msdyn_entitylinkchatconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_entitylinkchatconfiguration msdyn_entitylinkchatconfiguration_MailboxTrackingFolders](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencedAttribute|`msdyn_entitylinkchatconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_entitylinkchatconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entityrefreshhistory_MailboxTrackingFolders"></a> msdyn_entityrefreshhistory_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_entityrefreshhistory msdyn_entityrefreshhistory_MailboxTrackingFolders](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entityrefreshhistory`|
|ReferencedAttribute|`msdyn_entityrefreshhistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_entityrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_favoriteknowledgearticle_MailboxTrackingFolders"></a> msdyn_favoriteknowledgearticle_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_favoriteknowledgearticle msdyn_favoriteknowledgearticle_MailboxTrackingFolders](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_favoriteknowledgearticle`|
|ReferencedAttribute|`msdyn_favoriteknowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_favoriteknowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticle_MailboxTrackingFolders"></a> msdyn_federatedarticle_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_federatedarticle msdyn_federatedarticle_MailboxTrackingFolders](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticle`|
|ReferencedAttribute|`msdyn_federatedarticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_federatedarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticleincident_MailboxTrackingFolders"></a> msdyn_federatedarticleincident_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_federatedarticleincident msdyn_federatedarticleincident_MailboxTrackingFolders](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticleincident`|
|ReferencedAttribute|`msdyn_federatedarticleincidentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_federatedarticleincident`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_fileupload_MailboxTrackingFolders"></a> msdyn_fileupload_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_fileupload msdyn_fileupload_MailboxTrackingFolders](msdyn_fileupload.md#BKMK_msdyn_fileupload_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_fileupload`|
|ReferencedAttribute|`msdyn_fileuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_fileupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_actionapprovalmodel_MailboxTrackingFolders"></a> msdyn_flow_actionapprovalmodel_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_flow_actionapprovalmodel msdyn_flow_actionapprovalmodel_MailboxTrackingFolders](msdyn_flow_actionapprovalmodel.md#BKMK_msdyn_flow_actionapprovalmodel_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_actionapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_actionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approval_MailboxTrackingFolders"></a> msdyn_flow_approval_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approval_MailboxTrackingFolders](msdyn_flow_approval.md#BKMK_msdyn_flow_approval_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrequest_MailboxTrackingFolders"></a> msdyn_flow_approvalrequest_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrequest_MailboxTrackingFolders](msdyn_flow_approvalrequest.md#BKMK_msdyn_flow_approvalrequest_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalrequest`|
|ReferencedAttribute|`msdyn_flow_approvalrequestid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalresponse_MailboxTrackingFolders"></a> msdyn_flow_approvalresponse_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_flow_approvalresponse msdyn_flow_approvalresponse_MailboxTrackingFolders](msdyn_flow_approvalresponse.md#BKMK_msdyn_flow_approvalresponse_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalresponse`|
|ReferencedAttribute|`msdyn_flow_approvalresponseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalresponse`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalstep_MailboxTrackingFolders"></a> msdyn_flow_approvalstep_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_flow_approvalstep msdyn_flow_approvalstep_MailboxTrackingFolders](msdyn_flow_approvalstep.md#BKMK_msdyn_flow_approvalstep_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalstep`|
|ReferencedAttribute|`msdyn_flow_approvalstepid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_approvalstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallactionapprovalmodel_MailboxTrackingFolders"></a> msdyn_flow_awaitallactionapprovalmodel_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_flow_awaitallactionapprovalmodel msdyn_flow_awaitallactionapprovalmodel_MailboxTrackingFolders](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_msdyn_flow_awaitallactionapprovalmodel_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallactionapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_awaitallactionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallapprovalmodel_MailboxTrackingFolders"></a> msdyn_flow_awaitallapprovalmodel_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_flow_awaitallapprovalmodel msdyn_flow_awaitallapprovalmodel_MailboxTrackingFolders](msdyn_flow_awaitallapprovalmodel.md#BKMK_msdyn_flow_awaitallapprovalmodel_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_awaitallapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_basicapprovalmodel_MailboxTrackingFolders"></a> msdyn_flow_basicapprovalmodel_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodel_MailboxTrackingFolders](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodel_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_basicapprovalmodelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_basicapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_flowapproval_MailboxTrackingFolders"></a> msdyn_flow_flowapproval_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_flow_flowapproval msdyn_flow_flowapproval_MailboxTrackingFolders](msdyn_flow_flowapproval.md#BKMK_msdyn_flow_flowapproval_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_flowapproval`|
|ReferencedAttribute|`msdyn_flow_flowapprovalid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_flow_flowapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_formmapping_MailboxTrackingFolders"></a> msdyn_formmapping_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_formmapping msdyn_formmapping_MailboxTrackingFolders](msdyn_formmapping.md#BKMK_msdyn_formmapping_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_formmapping`|
|ReferencedAttribute|`msdyn_formmappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_formmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_function_MailboxTrackingFolders"></a> msdyn_function_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_function msdyn_function_MailboxTrackingFolders](msdyn_function.md#BKMK_msdyn_function_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_function`|
|ReferencedAttribute|`msdyn_functionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_function`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_helppage_MailboxTrackingFolders"></a> msdyn_helppage_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_helppage msdyn_helppage_MailboxTrackingFolders](msdyn_helppage.md#BKMK_msdyn_helppage_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_helppage`|
|ReferencedAttribute|`msdyn_helppageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_helppage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_insightsstorevirtualentity_MailboxTrackingFolders"></a> msdyn_insightsstorevirtualentity_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_insightsstorevirtualentity msdyn_insightsstorevirtualentity_MailboxTrackingFolders](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_insightsstorevirtualentity`|
|ReferencedAttribute|`msdyn_insightsstorevirtualentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_insightsstorevirtualentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders"></a> msdyn_integratedsearchprovider_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_integratedsearchprovider msdyn_integratedsearchprovider_MailboxTrackingFolders](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_integratedsearchprovider`|
|ReferencedAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_integratedsearchprovider`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kalanguagesetting_MailboxTrackingFolders"></a> msdyn_kalanguagesetting_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_kalanguagesetting msdyn_kalanguagesetting_MailboxTrackingFolders](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kalanguagesetting`|
|ReferencedAttribute|`msdyn_kalanguagesettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kalanguagesetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kbattachment_MailboxTrackingFolders"></a> msdyn_kbattachment_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_kbattachment msdyn_kbattachment_MailboxTrackingFolders](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kbattachment`|
|ReferencedAttribute|`msdyn_kbattachmentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kbattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders"></a> msdyn_kmfederatedsearchconfig_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_kmfederatedsearchconfig msdyn_kmfederatedsearchconfig_MailboxTrackingFolders](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencedAttribute|`msdyn_kmfederatedsearchconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kmfederatedsearchconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmpersonalizationsetting_MailboxTrackingFolders"></a> msdyn_kmpersonalizationsetting_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_kmpersonalizationsetting msdyn_kmpersonalizationsetting_MailboxTrackingFolders](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmpersonalizationsetting`|
|ReferencedAttribute|`msdyn_kmpersonalizationsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_kmpersonalizationsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders"></a> msdyn_knowledgearticleimage_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_knowledgearticleimage msdyn_knowledgearticleimage_MailboxTrackingFolders](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticleimage`|
|ReferencedAttribute|`msdyn_knowledgearticleimageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgearticleimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders"></a> msdyn_knowledgearticletemplate_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_knowledgearticletemplate msdyn_knowledgearticletemplate_MailboxTrackingFolders](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticletemplate`|
|ReferencedAttribute|`msdyn_knowledgearticletemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgearticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeassetconfiguration_MailboxTrackingFolders"></a> msdyn_knowledgeassetconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_knowledgeassetconfiguration msdyn_knowledgeassetconfiguration_MailboxTrackingFolders](msdyn_knowledgeassetconfiguration.md#BKMK_msdyn_knowledgeassetconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeassetconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeassetconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeassetconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeconfiguration_MailboxTrackingFolders"></a> msdyn_knowledgeconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_knowledgeconfiguration msdyn_knowledgeconfiguration_MailboxTrackingFolders](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders"></a> msdyn_knowledgeinteractioninsight_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_knowledgeinteractioninsight msdyn_knowledgeinteractioninsight_MailboxTrackingFolders](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencedAttribute|`msdyn_knowledgeinteractioninsightid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgeinteractioninsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgemanagementsetting_MailboxTrackingFolders"></a> msdyn_knowledgemanagementsetting_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_knowledgemanagementsetting msdyn_knowledgemanagementsetting_MailboxTrackingFolders](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgemanagementsetting`|
|ReferencedAttribute|`msdyn_knowledgemanagementsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgemanagementsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgepersonalfilter_MailboxTrackingFolders"></a> msdyn_knowledgepersonalfilter_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_knowledgepersonalfilter msdyn_knowledgepersonalfilter_MailboxTrackingFolders](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgepersonalfilter`|
|ReferencedAttribute|`msdyn_knowledgepersonalfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgepersonalfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchfilter_MailboxTrackingFolders"></a> msdyn_knowledgesearchfilter_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_knowledgesearchfilter msdyn_knowledgesearchfilter_MailboxTrackingFolders](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchfilter`|
|ReferencedAttribute|`msdyn_knowledgesearchfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgesearchfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders"></a> msdyn_knowledgesearchinsight_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_knowledgesearchinsight msdyn_knowledgesearchinsight_MailboxTrackingFolders](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchinsight`|
|ReferencedAttribute|`msdyn_knowledgesearchinsightid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_knowledgesearchinsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_mobileapp_MailboxTrackingFolders"></a> msdyn_mobileapp_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_mobileapp msdyn_mobileapp_MailboxTrackingFolders](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_mobileapp`|
|ReferencedAttribute|`msdyn_mobileappid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_mobileapp`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_modulerundetail_MailboxTrackingFolders"></a> msdyn_modulerundetail_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_modulerundetail msdyn_modulerundetail_MailboxTrackingFolders](msdyn_modulerundetail.md#BKMK_msdyn_modulerundetail_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_modulerundetail`|
|ReferencedAttribute|`msdyn_modulerundetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_modulerundetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmanalysishistory_MailboxTrackingFolders"></a> msdyn_pmanalysishistory_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmanalysishistory msdyn_pmanalysishistory_MailboxTrackingFolders](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmanalysishistory`|
|ReferencedAttribute|`msdyn_pmanalysishistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmanalysishistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmbusinessruleautomationconfig_MailboxTrackingFolders"></a> msdyn_pmbusinessruleautomationconfig_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmbusinessruleautomationconfig msdyn_pmbusinessruleautomationconfig_MailboxTrackingFolders](msdyn_pmbusinessruleautomationconfig.md#BKMK_msdyn_pmbusinessruleautomationconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencedAttribute|`msdyn_pmbusinessruleautomationconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmbusinessruleautomationconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendar_MailboxTrackingFolders"></a> msdyn_pmcalendar_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmcalendar msdyn_pmcalendar_MailboxTrackingFolders](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendar`|
|ReferencedAttribute|`msdyn_pmcalendarid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendarversion_MailboxTrackingFolders"></a> msdyn_pmcalendarversion_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmcalendarversion msdyn_pmcalendarversion_MailboxTrackingFolders](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendarversion`|
|ReferencedAttribute|`msdyn_pmcalendarversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmcalendarversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pminferredtask_MailboxTrackingFolders"></a> msdyn_pminferredtask_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pminferredtask msdyn_pminferredtask_MailboxTrackingFolders](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pminferredtask`|
|ReferencedAttribute|`msdyn_pminferredtaskid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pminferredtask`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders"></a> msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmprocessextendedmetadataversion msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessextendedmetadataversion`|
|ReferencedAttribute|`msdyn_pmprocessextendedmetadataversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessextendedmetadataversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocesstemplate_MailboxTrackingFolders"></a> msdyn_pmprocesstemplate_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmprocesstemplate msdyn_pmprocesstemplate_MailboxTrackingFolders](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocesstemplate`|
|ReferencedAttribute|`msdyn_pmprocesstemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocesstemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessusersettings_MailboxTrackingFolders"></a> msdyn_pmprocessusersettings_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmprocessusersettings msdyn_pmprocessusersettings_MailboxTrackingFolders](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessusersettings`|
|ReferencedAttribute|`msdyn_pmprocessusersettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessusersettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessversion_MailboxTrackingFolders"></a> msdyn_pmprocessversion_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmprocessversion msdyn_pmprocessversion_MailboxTrackingFolders](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessversion`|
|ReferencedAttribute|`msdyn_pmprocessversionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmprocessversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmrecording_MailboxTrackingFolders"></a> msdyn_pmrecording_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmrecording msdyn_pmrecording_MailboxTrackingFolders](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmrecording`|
|ReferencedAttribute|`msdyn_pmrecordingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmrecording`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmsimulation_MailboxTrackingFolders"></a> msdyn_pmsimulation_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmsimulation msdyn_pmsimulation_MailboxTrackingFolders](msdyn_pmsimulation.md#BKMK_msdyn_pmsimulation_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmsimulation`|
|ReferencedAttribute|`msdyn_pmsimulationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmsimulation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtemplate_MailboxTrackingFolders"></a> msdyn_pmtemplate_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmtemplate msdyn_pmtemplate_MailboxTrackingFolders](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtemplate`|
|ReferencedAttribute|`msdyn_pmtemplateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmview_MailboxTrackingFolders"></a> msdyn_pmview_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_pmview msdyn_pmview_MailboxTrackingFolders](msdyn_pmview.md#BKMK_msdyn_pmview_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmview`|
|ReferencedAttribute|`msdyn_pmviewid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_pmview`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_qna_MailboxTrackingFolders"></a> msdyn_qna_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_qna msdyn_qna_MailboxTrackingFolders](msdyn_qna.md#BKMK_msdyn_qna_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_qna`|
|ReferencedAttribute|`msdyn_qnaid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_qna`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_richtextfile_MailboxTrackingFolders"></a> msdyn_richtextfile_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_richtextfile msdyn_richtextfile_MailboxTrackingFolders](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_richtextfile`|
|ReferencedAttribute|`msdyn_richtextfileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_richtextfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredobject_MailboxTrackingFolders"></a> msdyn_salesforcestructuredobject_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_salesforcestructuredobject msdyn_salesforcestructuredobject_MailboxTrackingFolders](msdyn_salesforcestructuredobject.md#BKMK_msdyn_salesforcestructuredobject_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredobject`|
|ReferencedAttribute|`msdyn_salesforcestructuredobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_salesforcestructuredobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredqnaconfig_MailboxTrackingFolders"></a> msdyn_salesforcestructuredqnaconfig_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_salesforcestructuredqnaconfig msdyn_salesforcestructuredqnaconfig_MailboxTrackingFolders](msdyn_salesforcestructuredqnaconfig.md#BKMK_msdyn_salesforcestructuredqnaconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredqnaconfig`|
|ReferencedAttribute|`msdyn_salesforcestructuredqnaconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_salesforcestructuredqnaconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_schedule_MailboxTrackingFolders"></a> msdyn_schedule_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_schedule msdyn_schedule_MailboxTrackingFolders](msdyn_schedule.md#BKMK_msdyn_schedule_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_schedule`|
|ReferencedAttribute|`msdyn_scheduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_schedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_serviceconfiguration_MailboxTrackingFolders"></a> msdyn_serviceconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_serviceconfiguration msdyn_serviceconfiguration_MailboxTrackingFolders](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_serviceconfiguration`|
|ReferencedAttribute|`msdyn_serviceconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_serviceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_slakpi_MailboxTrackingFolders"></a> msdyn_slakpi_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_slakpi msdyn_slakpi_MailboxTrackingFolders](msdyn_slakpi.md#BKMK_msdyn_slakpi_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_slakpi`|
|ReferencedAttribute|`msdyn_slakpiid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_slakpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders"></a> msdyn_solutionhealthrule_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_solutionhealthrule msdyn_solutionhealthrule_MailboxTrackingFolders](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthrule`|
|ReferencedAttribute|`msdyn_solutionhealthruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleargument_MailboxTrackingFolders"></a> msdyn_solutionhealthruleargument_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_solutionhealthruleargument msdyn_solutionhealthruleargument_MailboxTrackingFolders](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleargument`|
|ReferencedAttribute|`msdyn_solutionhealthruleargumentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthruleargument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleset_MailboxTrackingFolders"></a> msdyn_solutionhealthruleset_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_solutionhealthruleset msdyn_solutionhealthruleset_MailboxTrackingFolders](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleset`|
|ReferencedAttribute|`msdyn_solutionhealthrulesetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_solutionhealthruleset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_tour_MailboxTrackingFolders"></a> msdyn_tour_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_tour msdyn_tour_MailboxTrackingFolders](msdyn_tour.md#BKMK_msdyn_tour_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_tour`|
|ReferencedAttribute|`msdyn_tourid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_tour`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_virtualtablecolumncandidate_MailboxTrackingFolders"></a> msdyn_virtualtablecolumncandidate_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_virtualtablecolumncandidate msdyn_virtualtablecolumncandidate_MailboxTrackingFolders](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencedAttribute|`msdyn_virtualtablecolumncandidateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_virtualtablecolumncandidate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_workflowactionstatus_MailboxTrackingFolders"></a> msdyn_workflowactionstatus_MailboxTrackingFolders

One-To-Many Relationship: [msdyn_workflowactionstatus msdyn_workflowactionstatus_MailboxTrackingFolders](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_workflowactionstatus`|
|ReferencedAttribute|`msdyn_workflowactionstatusid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdyn_workflowactionstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdynce_botcontent_MailboxTrackingFolders"></a> msdynce_botcontent_MailboxTrackingFolders

One-To-Many Relationship: [msdynce_botcontent msdynce_botcontent_MailboxTrackingFolders](msdynce_botcontent.md#BKMK_msdynce_botcontent_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msdynce_botcontent`|
|ReferencedAttribute|`msdynce_botcontentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msdynce_botcontent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msgraphresourcetosubscription_MailboxTrackingFolders"></a> msgraphresourcetosubscription_MailboxTrackingFolders

One-To-Many Relationship: [msgraphresourcetosubscription msgraphresourcetosubscription_MailboxTrackingFolders](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`msgraphresourcetosubscription`|
|ReferencedAttribute|`msgraphresourcetosubscriptionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_msgraphresourcetosubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders"></a> mspcat_catalogsubmissionfiles_MailboxTrackingFolders

One-To-Many Relationship: [mspcat_catalogsubmissionfiles mspcat_catalogsubmissionfiles_MailboxTrackingFolders](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_catalogsubmissionfiles`|
|ReferencedAttribute|`mspcat_catalogsubmissionfilesid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspcat_catalogsubmissionfiles`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_packagestore_MailboxTrackingFolders"></a> mspcat_packagestore_MailboxTrackingFolders

One-To-Many Relationship: [mspcat_packagestore mspcat_packagestore_MailboxTrackingFolders](mspcat_packagestore.md#BKMK_mspcat_packagestore_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_packagestore`|
|ReferencedAttribute|`mspcat_packagestoreid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_mspcat_packagestore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Organization_MailboxTrackingFolder"></a> Organization_MailboxTrackingFolder

One-To-Many Relationship: [organization Organization_MailboxTrackingFolder](organization.md#BKMK_Organization_MailboxTrackingFolder)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncfnostate_MailboxTrackingFolders"></a> organizationdatasyncfnostate_MailboxTrackingFolders

One-To-Many Relationship: [organizationdatasyncfnostate organizationdatasyncfnostate_MailboxTrackingFolders](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncfnostate`|
|ReferencedAttribute|`organizationdatasyncfnostateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncfnostate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncstate_MailboxTrackingFolders"></a> organizationdatasyncstate_MailboxTrackingFolders

One-To-Many Relationship: [organizationdatasyncstate organizationdatasyncstate_MailboxTrackingFolders](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncstate`|
|ReferencedAttribute|`organizationdatasyncstateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncstate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscription_MailboxTrackingFolders"></a> organizationdatasyncsubscription_MailboxTrackingFolders

One-To-Many Relationship: [organizationdatasyncsubscription organizationdatasyncsubscription_MailboxTrackingFolders](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionentity_MailboxTrackingFolders"></a> organizationdatasyncsubscriptionentity_MailboxTrackingFolders

One-To-Many Relationship: [organizationdatasyncsubscriptionentity organizationdatasyncsubscriptionentity_MailboxTrackingFolders](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionentity`|
|ReferencedAttribute|`organizationdatasyncsubscriptionentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscriptionentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders"></a> organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders

One-To-Many Relationship: [organizationdatasyncsubscriptionfnotable organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencedAttribute|`organizationdatasyncsubscriptionfnotableid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_organizationdatasyncsubscriptionfnotable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_mailboxtrackingfolder"></a> owner_mailboxtrackingfolder

One-To-Many Relationship: [owner owner_mailboxtrackingfolder](owner.md#BKMK_owner_mailboxtrackingfolder)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_package_MailboxTrackingFolders"></a> package_MailboxTrackingFolders

One-To-Many Relationship: [package package_MailboxTrackingFolders](package.md#BKMK_package_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`package`|
|ReferencedAttribute|`packageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_package`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_packagehistory_MailboxTrackingFolders"></a> packagehistory_MailboxTrackingFolders

One-To-Many Relationship: [packagehistory packagehistory_MailboxTrackingFolders](packagehistory.md#BKMK_packagehistory_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`packagehistory`|
|ReferencedAttribute|`packagehistoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_packagehistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannerbusinessscenario_MailboxTrackingFolders"></a> plannerbusinessscenario_MailboxTrackingFolders

One-To-Many Relationship: [plannerbusinessscenario plannerbusinessscenario_MailboxTrackingFolders](plannerbusinessscenario.md#BKMK_plannerbusinessscenario_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`plannerbusinessscenario`|
|ReferencedAttribute|`plannerbusinessscenarioid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plannerbusinessscenario`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannersyncaction_MailboxTrackingFolders"></a> plannersyncaction_MailboxTrackingFolders

One-To-Many Relationship: [plannersyncaction plannersyncaction_MailboxTrackingFolders](plannersyncaction.md#BKMK_plannersyncaction_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`plannersyncaction`|
|ReferencedAttribute|`plannersyncactionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plannersyncaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plugin_MailboxTrackingFolders"></a> plugin_MailboxTrackingFolders

One-To-Many Relationship: [plugin plugin_MailboxTrackingFolders](plugin.md#BKMK_plugin_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`plugin`|
|ReferencedAttribute|`pluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_plugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_pluginpackage_MailboxTrackingFolders"></a> pluginpackage_MailboxTrackingFolders

One-To-Many Relationship: [pluginpackage pluginpackage_MailboxTrackingFolders](pluginpackage.md#BKMK_pluginpackage_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`pluginpackage`|
|ReferencedAttribute|`pluginpackageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_pluginpackage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidataset_MailboxTrackingFolders"></a> powerbidataset_MailboxTrackingFolders

One-To-Many Relationship: [powerbidataset powerbidataset_MailboxTrackingFolders](powerbidataset.md#BKMK_powerbidataset_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidataset`|
|ReferencedAttribute|`powerbidatasetid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbidataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidatasetapdx_MailboxTrackingFolders"></a> powerbidatasetapdx_MailboxTrackingFolders

One-To-Many Relationship: [powerbidatasetapdx powerbidatasetapdx_MailboxTrackingFolders](powerbidatasetapdx.md#BKMK_powerbidatasetapdx_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidatasetapdx`|
|ReferencedAttribute|`powerbidatasetapdxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbidatasetapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbimashupparameter_MailboxTrackingFolders"></a> powerbimashupparameter_MailboxTrackingFolders

One-To-Many Relationship: [powerbimashupparameter powerbimashupparameter_MailboxTrackingFolders](powerbimashupparameter.md#BKMK_powerbimashupparameter_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbimashupparameter`|
|ReferencedAttribute|`powerbimashupparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbimashupparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireport_MailboxTrackingFolders"></a> powerbireport_MailboxTrackingFolders

One-To-Many Relationship: [powerbireport powerbireport_MailboxTrackingFolders](powerbireport.md#BKMK_powerbireport_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireport`|
|ReferencedAttribute|`powerbireportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbireport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireportapdx_MailboxTrackingFolders"></a> powerbireportapdx_MailboxTrackingFolders

One-To-Many Relationship: [powerbireportapdx powerbireportapdx_MailboxTrackingFolders](powerbireportapdx.md#BKMK_powerbireportapdx_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireportapdx`|
|ReferencedAttribute|`powerbireportapdxid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerbireportapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerfxrule_MailboxTrackingFolders"></a> powerfxrule_MailboxTrackingFolders

One-To-Many Relationship: [powerfxrule powerfxrule_MailboxTrackingFolders](powerfxrule.md#BKMK_powerfxrule_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerfxrule`|
|ReferencedAttribute|`powerfxruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerfxrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagecomponent_MailboxTrackingFolders"></a> powerpagecomponent_MailboxTrackingFolders

One-To-Many Relationship: [powerpagecomponent powerpagecomponent_MailboxTrackingFolders](powerpagecomponent.md#BKMK_powerpagecomponent_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagecomponent`|
|ReferencedAttribute|`powerpagecomponentid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagecomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesite_MailboxTrackingFolders"></a> powerpagesite_MailboxTrackingFolders

One-To-Many Relationship: [powerpagesite powerpagesite_MailboxTrackingFolders](powerpagesite.md#BKMK_powerpagesite_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesite`|
|ReferencedAttribute|`powerpagesiteid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitelanguage_MailboxTrackingFolders"></a> powerpagesitelanguage_MailboxTrackingFolders

One-To-Many Relationship: [powerpagesitelanguage powerpagesitelanguage_MailboxTrackingFolders](powerpagesitelanguage.md#BKMK_powerpagesitelanguage_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitelanguage`|
|ReferencedAttribute|`powerpagesitelanguageid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesitelanguage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitepublished_MailboxTrackingFolders"></a> powerpagesitepublished_MailboxTrackingFolders

One-To-Many Relationship: [powerpagesitepublished powerpagesitepublished_MailboxTrackingFolders](powerpagesitepublished.md#BKMK_powerpagesitepublished_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitepublished`|
|ReferencedAttribute|`powerpagesitepublishedid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesitepublished`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesmanagedidentity_MailboxTrackingFolders"></a> powerpagesmanagedidentity_MailboxTrackingFolders

One-To-Many Relationship: [powerpagesmanagedidentity powerpagesmanagedidentity_MailboxTrackingFolders](powerpagesmanagedidentity.md#BKMK_powerpagesmanagedidentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesmanagedidentity`|
|ReferencedAttribute|`powerpagesmanagedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesscanreport_MailboxTrackingFolders"></a> powerpagesscanreport_MailboxTrackingFolders

One-To-Many Relationship: [powerpagesscanreport powerpagesscanreport_MailboxTrackingFolders](powerpagesscanreport.md#BKMK_powerpagesscanreport_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesscanreport`|
|ReferencedAttribute|`powerpagesscanreportid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_powerpagesscanreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerlog_MailboxTrackingFolders"></a> privilegecheckerlog_MailboxTrackingFolders

One-To-Many Relationship: [privilegecheckerlog privilegecheckerlog_MailboxTrackingFolders](privilegecheckerlog.md#BKMK_privilegecheckerlog_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerlog`|
|ReferencedAttribute|`privilegecheckerlogid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegecheckerlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerrun_MailboxTrackingFolders"></a> privilegecheckerrun_MailboxTrackingFolders

One-To-Many Relationship: [privilegecheckerrun privilegecheckerrun_MailboxTrackingFolders](privilegecheckerrun.md#BKMK_privilegecheckerrun_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerrun`|
|ReferencedAttribute|`privilegecheckerrunid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegecheckerrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegesremovalsetting_MailboxTrackingFolders"></a> privilegesremovalsetting_MailboxTrackingFolders

One-To-Many Relationship: [privilegesremovalsetting privilegesremovalsetting_MailboxTrackingFolders](privilegesremovalsetting.md#BKMK_privilegesremovalsetting_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegesremovalsetting`|
|ReferencedAttribute|`privilegesremovalsettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_privilegesremovalsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstageparameter_MailboxTrackingFolders"></a> processstageparameter_MailboxTrackingFolders

One-To-Many Relationship: [processstageparameter processstageparameter_MailboxTrackingFolders](processstageparameter.md#BKMK_processstageparameter_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`processstageparameter`|
|ReferencedAttribute|`processstageparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_processstageparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_provisionlanguageforuser_MailboxTrackingFolders"></a> provisionlanguageforuser_MailboxTrackingFolders

One-To-Many Relationship: [provisionlanguageforuser provisionlanguageforuser_MailboxTrackingFolders](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`provisionlanguageforuser`|
|ReferencedAttribute|`provisionlanguageforuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_provisionlanguageforuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recordfilter_MailboxTrackingFolders"></a> recordfilter_MailboxTrackingFolders

One-To-Many Relationship: [recordfilter recordfilter_MailboxTrackingFolders](recordfilter.md#BKMK_recordfilter_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`recordfilter`|
|ReferencedAttribute|`recordfilterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recyclebinconfig_MailboxTrackingFolders"></a> recyclebinconfig_MailboxTrackingFolders

One-To-Many Relationship: [recyclebinconfig recyclebinconfig_MailboxTrackingFolders](recyclebinconfig.md#BKMK_recyclebinconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`recyclebinconfig`|
|ReferencedAttribute|`recyclebinconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_recyclebinconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_relationshipattribute_MailboxTrackingFolders"></a> relationshipattribute_MailboxTrackingFolders

One-To-Many Relationship: [relationshipattribute relationshipattribute_MailboxTrackingFolders](relationshipattribute.md#BKMK_relationshipattribute_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`relationshipattribute`|
|ReferencedAttribute|`relationshipattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_relationshipattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_reportparameter_MailboxTrackingFolders"></a> reportparameter_MailboxTrackingFolders

One-To-Many Relationship: [reportparameter reportparameter_MailboxTrackingFolders](reportparameter.md#BKMK_reportparameter_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`reportparameter`|
|ReferencedAttribute|`reportparameterid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_reportparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retaineddataexcel_MailboxTrackingFolders"></a> retaineddataexcel_MailboxTrackingFolders

One-To-Many Relationship: [retaineddataexcel retaineddataexcel_MailboxTrackingFolders](retaineddataexcel.md#BKMK_retaineddataexcel_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`retaineddataexcel`|
|ReferencedAttribute|`retaineddataexcelid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retaineddataexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionconfig_MailboxTrackingFolders"></a> retentionconfig_MailboxTrackingFolders

One-To-Many Relationship: [retentionconfig retentionconfig_MailboxTrackingFolders](retentionconfig.md#BKMK_retentionconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionconfig`|
|ReferencedAttribute|`retentionconfigid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionfailuredetail_MailboxTrackingFolders"></a> retentionfailuredetail_MailboxTrackingFolders

One-To-Many Relationship: [retentionfailuredetail retentionfailuredetail_MailboxTrackingFolders](retentionfailuredetail.md#BKMK_retentionfailuredetail_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionfailuredetail`|
|ReferencedAttribute|`retentionfailuredetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionfailuredetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperation_MailboxTrackingFolders"></a> retentionoperation_MailboxTrackingFolders

One-To-Many Relationship: [retentionoperation retentionoperation_MailboxTrackingFolders](retentionoperation.md#BKMK_retentionoperation_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperation`|
|ReferencedAttribute|`retentionoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperationdetail_MailboxTrackingFolders"></a> retentionoperationdetail_MailboxTrackingFolders

One-To-Many Relationship: [retentionoperationdetail retentionoperationdetail_MailboxTrackingFolders](retentionoperationdetail.md#BKMK_retentionoperationdetail_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperationdetail`|
|ReferencedAttribute|`retentionoperationdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionoperationdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionsuccessdetail_MailboxTrackingFolders"></a> retentionsuccessdetail_MailboxTrackingFolders

One-To-Many Relationship: [retentionsuccessdetail retentionsuccessdetail_MailboxTrackingFolders](retentionsuccessdetail.md#BKMK_retentionsuccessdetail_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionsuccessdetail`|
|ReferencedAttribute|`retentionsuccessdetailid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_retentionsuccessdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_roleeditorlayout_MailboxTrackingFolders"></a> roleeditorlayout_MailboxTrackingFolders

One-To-Many Relationship: [roleeditorlayout roleeditorlayout_MailboxTrackingFolders](roleeditorlayout.md#BKMK_roleeditorlayout_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`roleeditorlayout`|
|ReferencedAttribute|`roleeditorlayoutid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_roleeditorlayout`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_savingrule_MailboxTrackingFolders"></a> savingrule_MailboxTrackingFolders

One-To-Many Relationship: [savingrule savingrule_MailboxTrackingFolders](savingrule.md#BKMK_savingrule_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`savingrule`|
|ReferencedAttribute|`savingruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_savingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchattributesettings_MailboxTrackingFolders"></a> searchattributesettings_MailboxTrackingFolders

One-To-Many Relationship: [searchattributesettings searchattributesettings_MailboxTrackingFolders](searchattributesettings.md#BKMK_searchattributesettings_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`searchattributesettings`|
|ReferencedAttribute|`searchattributesettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchattributesettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchcustomanalyzer_MailboxTrackingFolders"></a> searchcustomanalyzer_MailboxTrackingFolders

One-To-Many Relationship: [searchcustomanalyzer searchcustomanalyzer_MailboxTrackingFolders](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`searchcustomanalyzer`|
|ReferencedAttribute|`searchcustomanalyzerid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchcustomanalyzer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchrelationshipsettings_MailboxTrackingFolders"></a> searchrelationshipsettings_MailboxTrackingFolders

One-To-Many Relationship: [searchrelationshipsettings searchrelationshipsettings_MailboxTrackingFolders](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`searchrelationshipsettings`|
|ReferencedAttribute|`searchrelationshipsettingsid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_searchrelationshipsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplan_MailboxTrackingFolders"></a> serviceplan_MailboxTrackingFolders

One-To-Many Relationship: [serviceplan serviceplan_MailboxTrackingFolders](serviceplan.md#BKMK_serviceplan_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplan`|
|ReferencedAttribute|`serviceplanid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_serviceplan`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplanmapping_MailboxTrackingFolders"></a> serviceplanmapping_MailboxTrackingFolders

One-To-Many Relationship: [serviceplanmapping serviceplanmapping_MailboxTrackingFolders](serviceplanmapping.md#BKMK_serviceplanmapping_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplanmapping`|
|ReferencedAttribute|`serviceplanmappingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_serviceplanmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedlinksetting_MailboxTrackingFolders"></a> sharedlinksetting_MailboxTrackingFolders

One-To-Many Relationship: [sharedlinksetting sharedlinksetting_MailboxTrackingFolders](sharedlinksetting.md#BKMK_sharedlinksetting_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedlinksetting`|
|ReferencedAttribute|`sharedlinksettingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedlinksetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedobject_MailboxTrackingFolders"></a> sharedobject_MailboxTrackingFolders

One-To-Many Relationship: [sharedobject sharedobject_MailboxTrackingFolders](sharedobject.md#BKMK_sharedobject_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedobject`|
|ReferencedAttribute|`sharedobjectid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspace_MailboxTrackingFolders"></a> sharedworkspace_MailboxTrackingFolders

One-To-Many Relationship: [sharedworkspace sharedworkspace_MailboxTrackingFolders](sharedworkspace.md#BKMK_sharedworkspace_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspace`|
|ReferencedAttribute|`sharedworkspaceid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspacepool_MailboxTrackingFolders"></a> sharedworkspacepool_MailboxTrackingFolders

One-To-Many Relationship: [sharedworkspacepool sharedworkspacepool_MailboxTrackingFolders](sharedworkspacepool.md#BKMK_sharedworkspacepool_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspacepool`|
|ReferencedAttribute|`sharedworkspacepoolid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharedworkspacepool`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharepointmanagedidentity_MailboxTrackingFolders"></a> sharepointmanagedidentity_MailboxTrackingFolders

One-To-Many Relationship: [sharepointmanagedidentity sharepointmanagedidentity_MailboxTrackingFolders](sharepointmanagedidentity.md#BKMK_sharepointmanagedidentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointmanagedidentity`|
|ReferencedAttribute|`sharepointmanagedidentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sharepointmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sideloadedaiplugin_MailboxTrackingFolders"></a> sideloadedaiplugin_MailboxTrackingFolders

One-To-Many Relationship: [sideloadedaiplugin sideloadedaiplugin_MailboxTrackingFolders](sideloadedaiplugin.md#BKMK_sideloadedaiplugin_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`sideloadedaiplugin`|
|ReferencedAttribute|`sideloadedaipluginid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_sideloadedaiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentattributeconfiguration_MailboxTrackingFolders"></a> solutioncomponentattributeconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [solutioncomponentattributeconfiguration solutioncomponentattributeconfiguration_MailboxTrackingFolders](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentattributeconfiguration`|
|ReferencedAttribute|`solutioncomponentattributeconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentattributeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentbatchconfiguration_MailboxTrackingFolders"></a> solutioncomponentbatchconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [solutioncomponentbatchconfiguration solutioncomponentbatchconfiguration_MailboxTrackingFolders](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentbatchconfiguration`|
|ReferencedAttribute|`solutioncomponentbatchconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentbatchconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentconfiguration_MailboxTrackingFolders"></a> solutioncomponentconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [solutioncomponentconfiguration solutioncomponentconfiguration_MailboxTrackingFolders](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentconfiguration`|
|ReferencedAttribute|`solutioncomponentconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders"></a> solutioncomponentrelationshipconfiguration_MailboxTrackingFolders

One-To-Many Relationship: [solutioncomponentrelationshipconfiguration solutioncomponentrelationshipconfiguration_MailboxTrackingFolders](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentrelationshipconfiguration`|
|ReferencedAttribute|`solutioncomponentrelationshipconfigurationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_solutioncomponentrelationshipconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentity_MailboxTrackingFolders"></a> stagedentity_MailboxTrackingFolders

One-To-Many Relationship: [stagedentity stagedentity_MailboxTrackingFolders](stagedentity.md#BKMK_stagedentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentity`|
|ReferencedAttribute|`stagedentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentityattribute_MailboxTrackingFolders"></a> stagedentityattribute_MailboxTrackingFolders

One-To-Many Relationship: [stagedentityattribute stagedentityattribute_MailboxTrackingFolders](stagedentityattribute.md#BKMK_stagedentityattribute_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentityattribute`|
|ReferencedAttribute|`stagedentityattributeid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedentityattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedmetadataasyncoperation_MailboxTrackingFolders"></a> stagedmetadataasyncoperation_MailboxTrackingFolders

One-To-Many Relationship: [stagedmetadataasyncoperation stagedmetadataasyncoperation_MailboxTrackingFolders](stagedmetadataasyncoperation.md#BKMK_stagedmetadataasyncoperation_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedmetadataasyncoperation`|
|ReferencedAttribute|`stagedmetadataasyncoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagedmetadataasyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagesolutionupload_MailboxTrackingFolders"></a> stagesolutionupload_MailboxTrackingFolders

One-To-Many Relationship: [stagesolutionupload stagesolutionupload_MailboxTrackingFolders](stagesolutionupload.md#BKMK_stagesolutionupload_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`stagesolutionupload`|
|ReferencedAttribute|`stagesolutionuploadid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_stagesolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_supportusertable_MailboxTrackingFolders"></a> supportusertable_MailboxTrackingFolders

One-To-Many Relationship: [supportusertable supportusertable_MailboxTrackingFolders](supportusertable.md#BKMK_supportusertable_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`supportusertable`|
|ReferencedAttribute|`supportusertableid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_supportusertable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapsedatabase_MailboxTrackingFolders"></a> synapsedatabase_MailboxTrackingFolders

One-To-Many Relationship: [synapsedatabase synapsedatabase_MailboxTrackingFolders](synapsedatabase.md#BKMK_synapsedatabase_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`synapsedatabase`|
|ReferencedAttribute|`synapsedatabaseid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapsedatabase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkexternaltablestate_MailboxTrackingFolders"></a> synapselinkexternaltablestate_MailboxTrackingFolders

One-To-Many Relationship: [synapselinkexternaltablestate synapselinkexternaltablestate_MailboxTrackingFolders](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkexternaltablestate`|
|ReferencedAttribute|`synapselinkexternaltablestateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkexternaltablestate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofile_MailboxTrackingFolders"></a> synapselinkprofile_MailboxTrackingFolders

One-To-Many Relationship: [synapselinkprofile synapselinkprofile_MailboxTrackingFolders](synapselinkprofile.md#BKMK_synapselinkprofile_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofile`|
|ReferencedAttribute|`synapselinkprofileid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentity_MailboxTrackingFolders"></a> synapselinkprofileentity_MailboxTrackingFolders

One-To-Many Relationship: [synapselinkprofileentity synapselinkprofileentity_MailboxTrackingFolders](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentity`|
|ReferencedAttribute|`synapselinkprofileentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofileentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentitystate_MailboxTrackingFolders"></a> synapselinkprofileentitystate_MailboxTrackingFolders

One-To-Many Relationship: [synapselinkprofileentitystate synapselinkprofileentitystate_MailboxTrackingFolders](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentitystate`|
|ReferencedAttribute|`synapselinkprofileentitystateid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkprofileentitystate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkschedule_MailboxTrackingFolders"></a> synapselinkschedule_MailboxTrackingFolders

One-To-Many Relationship: [synapselinkschedule synapselinkschedule_MailboxTrackingFolders](synapselinkschedule.md#BKMK_synapselinkschedule_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkschedule`|
|ReferencedAttribute|`synapselinkscheduleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_synapselinkschedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuserauthorizationchangetracker_MailboxTrackingFolders"></a> systemuserauthorizationchangetracker_MailboxTrackingFolders

One-To-Many Relationship: [systemuserauthorizationchangetracker systemuserauthorizationchangetracker_MailboxTrackingFolders](systemuserauthorizationchangetracker.md#BKMK_systemuserauthorizationchangetracker_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuserauthorizationchangetracker`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_systemuserauthorizationchangetracker`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_tag_MailboxTrackingFolders"></a> tag_MailboxTrackingFolders

One-To-Many Relationship: [tag tag_MailboxTrackingFolders](tag.md#BKMK_tag_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`tag`|
|ReferencedAttribute|`tagid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_tag`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedflowsession_MailboxTrackingFolders"></a> taggedflowsession_MailboxTrackingFolders

One-To-Many Relationship: [taggedflowsession taggedflowsession_MailboxTrackingFolders](taggedflowsession.md#BKMK_taggedflowsession_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedflowsession`|
|ReferencedAttribute|`taggedflowsessionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_taggedflowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedprocess_MailboxTrackingFolders"></a> taggedprocess_MailboxTrackingFolders

One-To-Many Relationship: [taggedprocess taggedprocess_MailboxTrackingFolders](taggedprocess.md#BKMK_taggedprocess_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedprocess`|
|ReferencedAttribute|`taggedprocessid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_taggedprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_mailboxtrackingfolder"></a> team_mailboxtrackingfolder

One-To-Many Relationship: [team team_mailboxtrackingfolder](team.md#BKMK_team_mailboxtrackingfolder)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_teammobileofflineprofilemembership_MailboxTrackingFolders"></a> teammobileofflineprofilemembership_MailboxTrackingFolders

One-To-Many Relationship: [teammobileofflineprofilemembership teammobileofflineprofilemembership_MailboxTrackingFolders](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`teammobileofflineprofilemembership`|
|ReferencedAttribute|`teammobileofflineprofilemembershipid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_teammobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_territory_MailboxTrackingFolders"></a> territory_MailboxTrackingFolders

One-To-Many Relationship: [territory territory_MailboxTrackingFolders](territory.md#BKMK_territory_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`territory`|
|ReferencedAttribute|`territoryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_territory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchentity_MailboxTrackingFolders"></a> unstructuredfilesearchentity_MailboxTrackingFolders

One-To-Many Relationship: [unstructuredfilesearchentity unstructuredfilesearchentity_MailboxTrackingFolders](unstructuredfilesearchentity.md#BKMK_unstructuredfilesearchentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchentity`|
|ReferencedAttribute|`unstructuredfilesearchentityid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_unstructuredfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchrecord_MailboxTrackingFolders"></a> unstructuredfilesearchrecord_MailboxTrackingFolders

One-To-Many Relationship: [unstructuredfilesearchrecord unstructuredfilesearchrecord_MailboxTrackingFolders](unstructuredfilesearchrecord.md#BKMK_unstructuredfilesearchrecord_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchrecord`|
|ReferencedAttribute|`unstructuredfilesearchrecordid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_unstructuredfilesearchrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_usermobileofflineprofilemembership_MailboxTrackingFolders"></a> usermobileofflineprofilemembership_MailboxTrackingFolders

One-To-Many Relationship: [usermobileofflineprofilemembership usermobileofflineprofilemembership_MailboxTrackingFolders](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`usermobileofflineprofilemembership`|
|ReferencedAttribute|`usermobileofflineprofilemembershipid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_usermobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_userrating_MailboxTrackingFolders"></a> userrating_MailboxTrackingFolders

One-To-Many Relationship: [userrating userrating_MailboxTrackingFolders](userrating.md#BKMK_userrating_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`userrating`|
|ReferencedAttribute|`userratingid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_userrating`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_viewasexamplequestion_MailboxTrackingFolders"></a> viewasexamplequestion_MailboxTrackingFolders

One-To-Many Relationship: [viewasexamplequestion viewasexamplequestion_MailboxTrackingFolders](viewasexamplequestion.md#BKMK_viewasexamplequestion_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`viewasexamplequestion`|
|ReferencedAttribute|`viewasexamplequestionid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_viewasexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_virtualentitymetadata_MailboxTrackingFolders"></a> virtualentitymetadata_MailboxTrackingFolders

One-To-Many Relationship: [virtualentitymetadata virtualentitymetadata_MailboxTrackingFolders](virtualentitymetadata.md#BKMK_virtualentitymetadata_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`virtualentitymetadata`|
|ReferencedAttribute|`virtualentitymetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_virtualentitymetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowbinary_MailboxTrackingFolders"></a> workflowbinary_MailboxTrackingFolders

One-To-Many Relationship: [workflowbinary workflowbinary_MailboxTrackingFolders](workflowbinary.md#BKMK_workflowbinary_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowbinary`|
|ReferencedAttribute|`workflowbinaryid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowmetadata_MailboxTrackingFolders"></a> workflowmetadata_MailboxTrackingFolders

One-To-Many Relationship: [workflowmetadata workflowmetadata_MailboxTrackingFolders](workflowmetadata.md#BKMK_workflowmetadata_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowmetadata`|
|ReferencedAttribute|`workflowmetadataid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workflowmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueue_MailboxTrackingFolders"></a> workqueue_MailboxTrackingFolders

One-To-Many Relationship: [workqueue workqueue_MailboxTrackingFolders](workqueue.md#BKMK_workqueue_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueue`|
|ReferencedAttribute|`workqueueid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workqueue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueueitem_MailboxTrackingFolders"></a> workqueueitem_MailboxTrackingFolders

One-To-Many Relationship: [workqueueitem workqueueitem_MailboxTrackingFolders](workqueueitem.md#BKMK_workqueueitem_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueueitem`|
|ReferencedAttribute|`workqueueitemid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_workqueueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mailboxtrackingfolder?displayProperty=fullName>
