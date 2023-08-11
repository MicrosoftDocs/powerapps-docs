---
title: "Mailbox Auto Tracking Folder (MailboxTrackingFolder)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Mailbox Auto Tracking Folder (MailboxTrackingFolder)  table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Mailbox Auto Tracking Folder (MailboxTrackingFolder)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Stores data about what folders for a mailbox are auto tracked


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /mailboxtrackingfolders<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /mailboxtrackingfolders(*mailboxtrackingfolderid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /mailboxtrackingfolders(*mailboxtrackingfolderid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /mailboxtrackingfolders<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH /mailboxtrackingfolders(*mailboxtrackingfolderid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|MailboxTrackingFolders|
|DisplayCollectionName|Mailbox Auto Tracking Folders|
|DisplayName|Mailbox Auto Tracking Folder|
|EntitySetName|mailboxtrackingfolders|
|IsBPFEntity|False|
|LogicalCollectionName|mailboxtrackingfolders|
|LogicalName|mailboxtrackingfolder|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|mailboxtrackingfolderid|
|PrimaryNameAttribute||
|SchemaName|MailboxTrackingFolder|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ExchangeFolderId](#BKMK_ExchangeFolderId)
- [ExchangeFolderName](#BKMK_ExchangeFolderName)
- [FolderOnboardingStatus](#BKMK_FolderOnboardingStatus)
- [MailboxId](#BKMK_MailboxId)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)


### <a name="BKMK_ExchangeFolderId"></a> ExchangeFolderId

|Property|Value|
|--------|-----|
|Description|Folder Id for a folder in Exchange|
|DisplayName|Exchange Folder Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangefolderid|
|MaxLength|120|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExchangeFolderName"></a> ExchangeFolderName

|Property|Value|
|--------|-----|
|Description|Exchange Folder Name|
|DisplayName|Exchange Folder Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|exchangefoldername|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FolderOnboardingStatus"></a> FolderOnboardingStatus

|Property|Value|
|--------|-----|
|Description|Information to indicate whether the folder has been on boarded for auto tracking|
|DisplayName|Folder on boarding Status|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|folderonboardingstatus|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_MailboxId"></a> MailboxId

|Property|Value|
|--------|-----|
|Description|Mailbox id associated with this record.|
|DisplayName|MailboxId|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mailboxid|
|RequiredLevel|SystemRequired|
|Targets|mailbox|
|Type|Lookup|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.|
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


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|The regarding object such as Account, Contact, Lead etc. that the folder relates to.|
|DisplayName|Regarding Object Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|account,activityfileattachment,appaction,appactionmigration,appactionrule,appelement,applicationuser,appmodulecomponentedge,appmodulecomponentnode,appsetting,appusersetting,archivecleanupinfo,archivecleanupoperation,asyncoperation,attributeimageconfig,bot,botcomponent,bulkarchiveconfig,bulkarchivefailuredetail,bulkarchiveoperation,bulkarchiveoperationdetail,canvasappextendedmetadata,card,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalog,catalogassignment,chat,comment,connectioninstance,connectionreference,connector,contact,conversationtranscript,customapi,customapirequestparameter,customapiresponseproperty,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,dataprocessingconfiguration,delegatedauthorization,desktopflowbinary,desktopflowmodule,enablearchivalrequest,entityanalyticsconfig,entityimageconfig,entityindex,entityrecordfilter,environmentvariabledefinition,environmentvariablevalue,exportedexcel,exportsolutionupload,featurecontrolsetting,flowmachine,flowmachinegroup,flowmachineimage,flowmachineimageversion,flowmachinenetwork,flowsession,fxexpression,holidaywrapper,indexattributes,internalcatalogassignment,keyvaultreference,managedidentity,metadataforarchival,mobileofflineprofileextension,msdynce_botcontent,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfeedbackloop,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiconfiguration,msdyn_aievent,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_aitemplate,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisoverride,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_appinsightsmetadata,msdyn_customcontrolextendedsettings,msdyn_dataflow,msdyn_dataflowrefreshhistory,msdyn_dataflowtemplate,msdyn_dataflow_datalakefolder,msdyn_dmsrequest,msdyn_dmsrequeststatus,msdyn_entitylinkchatconfiguration,msdyn_entityrefreshhistory,msdyn_favoriteknowledgearticle,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_fileupload,msdyn_helppage,msdyn_insightsstorevirtualentity,msdyn_integratedsearchprovider,msdyn_kalanguagesetting,msdyn_kbattachment,msdyn_kmfederatedsearchconfig,msdyn_kmpersonalizationsetting,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeconfiguration,msdyn_knowledgeinteractioninsight,msdyn_knowledgemanagementsetting,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_mobileapp,msdyn_pmanalysishistory,msdyn_pmcalendar,msdyn_pmcalendarversion,msdyn_pminferredtask,msdyn_pmprocessextendedmetadataversion,msdyn_pmprocesstemplate,msdyn_pmprocessusersettings,msdyn_pmprocessversion,msdyn_pmrecording,msdyn_pmtemplate,msdyn_pmview,msdyn_richtextfile,msdyn_schedule,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,msdyn_tour,msdyn_virtualtablecolumncandidate,msdyn_workflowactionstatus,msgraphresourcetosubscription,mspcat_catalogsubmissionfiles,mspcat_packagestore,organizationdatasyncfnostate,organizationdatasyncstate,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,organizationdatasyncsubscriptionfnotable,organizationsetting,package,pdfsetting,pluginpackage,powerbidataset,powerbimashupparameter,powerbireport,powerfxrule,privilegesremovalsetting,processstageparameter,provisionlanguageforuser,reconciliationentityinfo,reconciliationinfo,recordfilter,relationshipattribute,retaineddataexcel,retentioncleanupinfo,retentioncleanupoperation,retentionconfig,retentionfailuredetail,retentionoperation,retentionoperationdetail,revokeinheritedaccessrecordstracker,roleeditorlayout,searchattributesettings,searchcustomanalyzer,searchrelationshipsettings,serviceplan,serviceplanmapping,settingdefinition,sharedlinksetting,sharedobject,sharedworkspace,sharedworkspacepool,solutioncomponentattributeconfiguration,solutioncomponentbatchconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagedentity,stagedentityattribute,stagesolutionupload,supportusertable,synapsedatabase,synapselinkexternaltablestate,synapselinkprofile,synapselinkprofileentity,synapselinkprofileentitystate,synapselinkschedule,systemuserauthorizationchangetracker,tdsmetadata,teammobileofflineprofilemembership,territory,usermobileofflineprofilemembership,userrating,virtualentitymetadata,workflowbinary,workqueue,workqueueitem|
|Type|Lookup|


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

|Property|Value|
|--------|-----|
|Description|Regarding Object Name|
|DisplayName|Regarding Object Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Information that indicates the type of regarding object associated with the folder|
|DisplayName|Regarding Object Type Code|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [MailboxTrackingFolderId](#BKMK_MailboxTrackingFolderId)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|False|
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
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the entry was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
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
|MaxLength|160|
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
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_MailboxTrackingFolderId"></a> MailboxTrackingFolderId

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mailboxtrackingfolderid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|False|
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
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the entry was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the record.|
|DisplayName|Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit that owns the folder mapping.|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the folder mapping.|
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
|Targets||
|Type|Lookup|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the mailbox tracking folder.|
|DisplayName|Version number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_mailboxtrackingfolder_modifiedby](#BKMK_lk_mailboxtrackingfolder_modifiedby)
- [lk_mailboxtrackingfolder_createdby](#BKMK_lk_mailboxtrackingfolder_createdby)
- [Account_MailboxTrackingFolder](#BKMK_Account_MailboxTrackingFolder)
- [team_mailboxtrackingfolder](#BKMK_team_mailboxtrackingfolder)
- [Contact_MailboxTrackingFolder](#BKMK_Contact_MailboxTrackingFolder)
- [lk_mailboxtrackingfolder_createdonbehalfby](#BKMK_lk_mailboxtrackingfolder_createdonbehalfby)
- [lk_mailboxtrackingfolder_modifiedonbehalfby](#BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby)
- [Organization_MailboxTrackingFolder](#BKMK_Organization_MailboxTrackingFolder)
- [Mailbox_MailboxTrackingFolder](#BKMK_Mailbox_MailboxTrackingFolder)
- [businessunit_mailboxtrackingfolder](#BKMK_businessunit_mailboxtrackingfolder)
- [AsyncOperation_MailboxTrackingFolder](#BKMK_AsyncOperation_MailboxTrackingFolder)
- [solutioncomponentattributeconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentattributeconfiguration_MailboxTrackingFolders)
- [solutioncomponentbatchconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentbatchconfiguration_MailboxTrackingFolders)
- [solutioncomponentconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentconfiguration_MailboxTrackingFolders)
- [solutioncomponentrelationshipconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders)
- [package_MailboxTrackingFolders](#BKMK_package_MailboxTrackingFolders)
- [stagesolutionupload_MailboxTrackingFolders](#BKMK_stagesolutionupload_MailboxTrackingFolders)
- [exportsolutionupload_MailboxTrackingFolders](#BKMK_exportsolutionupload_MailboxTrackingFolders)
- [featurecontrolsetting_MailboxTrackingFolders](#BKMK_featurecontrolsetting_MailboxTrackingFolders)
- [attributeimageconfig_MailboxTrackingFolders](#BKMK_attributeimageconfig_MailboxTrackingFolders)
- [entityimageconfig_MailboxTrackingFolders](#BKMK_entityimageconfig_MailboxTrackingFolders)
- [relationshipattribute_MailboxTrackingFolders](#BKMK_relationshipattribute_MailboxTrackingFolders)
- [stagedentity_MailboxTrackingFolders](#BKMK_stagedentity_MailboxTrackingFolders)
- [stagedentityattribute_MailboxTrackingFolders](#BKMK_stagedentityattribute_MailboxTrackingFolders)
- [catalog_MailboxTrackingFolders](#BKMK_catalog_MailboxTrackingFolders)
- [catalogassignment_MailboxTrackingFolders](#BKMK_catalogassignment_MailboxTrackingFolders)
- [customapi_MailboxTrackingFolders](#BKMK_customapi_MailboxTrackingFolders)
- [customapirequestparameter_MailboxTrackingFolders](#BKMK_customapirequestparameter_MailboxTrackingFolders)
- [customapiresponseproperty_MailboxTrackingFolders](#BKMK_customapiresponseproperty_MailboxTrackingFolders)
- [provisionlanguageforuser_MailboxTrackingFolders](#BKMK_provisionlanguageforuser_MailboxTrackingFolders)
- [sharedobject_MailboxTrackingFolders](#BKMK_sharedobject_MailboxTrackingFolders)
- [sharedworkspace_MailboxTrackingFolders](#BKMK_sharedworkspace_MailboxTrackingFolders)
- [sharedworkspacepool_MailboxTrackingFolders](#BKMK_sharedworkspacepool_MailboxTrackingFolders)
- [entityanalyticsconfig_MailboxTrackingFolders](#BKMK_entityanalyticsconfig_MailboxTrackingFolders)
- [datalakefolder_MailboxTrackingFolders](#BKMK_datalakefolder_MailboxTrackingFolders)
- [datalakefolderpermission_MailboxTrackingFolders](#BKMK_datalakefolderpermission_MailboxTrackingFolders)
- [datalakeworkspace_MailboxTrackingFolders](#BKMK_datalakeworkspace_MailboxTrackingFolders)
- [datalakeworkspacepermission_MailboxTrackingFolders](#BKMK_datalakeworkspacepermission_MailboxTrackingFolders)
- [dataprocessingconfiguration_MailboxTrackingFolders](#BKMK_dataprocessingconfiguration_MailboxTrackingFolders)
- [exportedexcel_MailboxTrackingFolders](#BKMK_exportedexcel_MailboxTrackingFolders)
- [retaineddataexcel_MailboxTrackingFolders](#BKMK_retaineddataexcel_MailboxTrackingFolders)
- [synapsedatabase_MailboxTrackingFolders](#BKMK_synapsedatabase_MailboxTrackingFolders)
- [synapselinkexternaltablestate_MailboxTrackingFolders](#BKMK_synapselinkexternaltablestate_MailboxTrackingFolders)
- [synapselinkprofile_MailboxTrackingFolders](#BKMK_synapselinkprofile_MailboxTrackingFolders)
- [synapselinkprofileentity_MailboxTrackingFolders](#BKMK_synapselinkprofileentity_MailboxTrackingFolders)
- [synapselinkprofileentitystate_MailboxTrackingFolders](#BKMK_synapselinkprofileentitystate_MailboxTrackingFolders)
- [synapselinkschedule_MailboxTrackingFolders](#BKMK_synapselinkschedule_MailboxTrackingFolders)
- [msdyn_dataflow_MailboxTrackingFolders](#BKMK_msdyn_dataflow_MailboxTrackingFolders)
- [msdyn_dataflowrefreshhistory_MailboxTrackingFolders](#BKMK_msdyn_dataflowrefreshhistory_MailboxTrackingFolders)
- [msdyn_entityrefreshhistory_MailboxTrackingFolders](#BKMK_msdyn_entityrefreshhistory_MailboxTrackingFolders)
- [sharedlinksetting_MailboxTrackingFolders](#BKMK_sharedlinksetting_MailboxTrackingFolders)
- [entityrecordfilter_MailboxTrackingFolders](#BKMK_entityrecordfilter_MailboxTrackingFolders)
- [recordfilter_MailboxTrackingFolders](#BKMK_recordfilter_MailboxTrackingFolders)
- [delegatedauthorization_MailboxTrackingFolders](#BKMK_delegatedauthorization_MailboxTrackingFolders)
- [serviceplan_MailboxTrackingFolders](#BKMK_serviceplan_MailboxTrackingFolders)
- [serviceplanmapping_MailboxTrackingFolders](#BKMK_serviceplanmapping_MailboxTrackingFolders)
- [applicationuser_MailboxTrackingFolders](#BKMK_applicationuser_MailboxTrackingFolders)
- [connector_MailboxTrackingFolders](#BKMK_connector_MailboxTrackingFolders)
- [environmentvariabledefinition_MailboxTrackingFolders](#BKMK_environmentvariabledefinition_MailboxTrackingFolders)
- [environmentvariablevalue_MailboxTrackingFolders](#BKMK_environmentvariablevalue_MailboxTrackingFolders)
- [workflowbinary_MailboxTrackingFolders](#BKMK_workflowbinary_MailboxTrackingFolders)
- [desktopflowmodule_MailboxTrackingFolders](#BKMK_desktopflowmodule_MailboxTrackingFolders)
- [flowmachine_MailboxTrackingFolders](#BKMK_flowmachine_MailboxTrackingFolders)
- [flowmachinegroup_MailboxTrackingFolders](#BKMK_flowmachinegroup_MailboxTrackingFolders)
- [flowmachineimage_MailboxTrackingFolders](#BKMK_flowmachineimage_MailboxTrackingFolders)
- [flowmachineimageversion_MailboxTrackingFolders](#BKMK_flowmachineimageversion_MailboxTrackingFolders)
- [flowmachinenetwork_MailboxTrackingFolders](#BKMK_flowmachinenetwork_MailboxTrackingFolders)
- [processstageparameter_MailboxTrackingFolders](#BKMK_processstageparameter_MailboxTrackingFolders)
- [workqueue_MailboxTrackingFolders](#BKMK_workqueue_MailboxTrackingFolders)
- [workqueueitem_MailboxTrackingFolders](#BKMK_workqueueitem_MailboxTrackingFolders)
- [desktopflowbinary_MailboxTrackingFolders](#BKMK_desktopflowbinary_MailboxTrackingFolders)
- [flowsession_MailboxTrackingFolders](#BKMK_flowsession_MailboxTrackingFolders)
- [connectionreference_MailboxTrackingFolders](#BKMK_connectionreference_MailboxTrackingFolders)
- [connectioninstance_MailboxTrackingFolders](#BKMK_connectioninstance_MailboxTrackingFolders)
- [msdyn_helppage_MailboxTrackingFolders](#BKMK_msdyn_helppage_MailboxTrackingFolders)
- [msdyn_tour_MailboxTrackingFolders](#BKMK_msdyn_tour_MailboxTrackingFolders)
- [msdynce_botcontent_MailboxTrackingFolders](#BKMK_msdynce_botcontent_MailboxTrackingFolders)
- [conversationtranscript_MailboxTrackingFolders](#BKMK_conversationtranscript_MailboxTrackingFolders)
- [bot_MailboxTrackingFolders](#BKMK_bot_MailboxTrackingFolders)
- [botcomponent_MailboxTrackingFolders](#BKMK_botcomponent_MailboxTrackingFolders)
- [territory_MailboxTrackingFolders](#BKMK_territory_MailboxTrackingFolders)
- [activityfileattachment_MailboxTrackingFolders](#BKMK_activityfileattachment_MailboxTrackingFolders)
- [chat_MailboxTrackingFolders](#BKMK_chat_MailboxTrackingFolders)
- [msdyn_serviceconfiguration_MailboxTrackingFolders](#BKMK_msdyn_serviceconfiguration_MailboxTrackingFolders)
- [msdyn_slakpi_MailboxTrackingFolders](#BKMK_msdyn_slakpi_MailboxTrackingFolders)
- [msdyn_knowledgemanagementsetting_MailboxTrackingFolders](#BKMK_msdyn_knowledgemanagementsetting_MailboxTrackingFolders)
- [msdyn_federatedarticle_MailboxTrackingFolders](#BKMK_msdyn_federatedarticle_MailboxTrackingFolders)
- [msdyn_federatedarticleincident_MailboxTrackingFolders](#BKMK_msdyn_federatedarticleincident_MailboxTrackingFolders)
- [msdyn_integratedsearchprovider_MailboxTrackingFolders](#BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders)
- [msdyn_kmfederatedsearchconfig_MailboxTrackingFolders](#BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders)
- [msdyn_knowledgearticleimage_MailboxTrackingFolders](#BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders)
- [msdyn_knowledgeconfiguration_MailboxTrackingFolders](#BKMK_msdyn_knowledgeconfiguration_MailboxTrackingFolders)
- [msdyn_knowledgeinteractioninsight_MailboxTrackingFolders](#BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders)
- [msdyn_knowledgesearchinsight_MailboxTrackingFolders](#BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders)
- [msdyn_favoriteknowledgearticle_MailboxTrackingFolders](#BKMK_msdyn_favoriteknowledgearticle_MailboxTrackingFolders)
- [msdyn_kalanguagesetting_MailboxTrackingFolders](#BKMK_msdyn_kalanguagesetting_MailboxTrackingFolders)
- [msdyn_kbattachment_MailboxTrackingFolders](#BKMK_msdyn_kbattachment_MailboxTrackingFolders)
- [msdyn_kmpersonalizationsetting_MailboxTrackingFolders](#BKMK_msdyn_kmpersonalizationsetting_MailboxTrackingFolders)
- [msdyn_knowledgearticletemplate_MailboxTrackingFolders](#BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders)
- [msdyn_knowledgepersonalfilter_MailboxTrackingFolders](#BKMK_msdyn_knowledgepersonalfilter_MailboxTrackingFolders)
- [msdyn_knowledgesearchfilter_MailboxTrackingFolders](#BKMK_msdyn_knowledgesearchfilter_MailboxTrackingFolders)
- [pluginpackage_MailboxTrackingFolders](#BKMK_pluginpackage_MailboxTrackingFolders)
- [fxexpression_MailboxTrackingFolders](#BKMK_fxexpression_MailboxTrackingFolders)
- [powerfxrule_MailboxTrackingFolders](#BKMK_powerfxrule_MailboxTrackingFolders)
- [keyvaultreference_MailboxTrackingFolders](#BKMK_keyvaultreference_MailboxTrackingFolders)
- [managedidentity_MailboxTrackingFolders](#BKMK_managedidentity_MailboxTrackingFolders)
- [msgraphresourcetosubscription_MailboxTrackingFolders](#BKMK_msgraphresourcetosubscription_MailboxTrackingFolders)
- [virtualentitymetadata_MailboxTrackingFolders](#BKMK_virtualentitymetadata_MailboxTrackingFolders)
- [mobileofflineprofileextension_MailboxTrackingFolders](#BKMK_mobileofflineprofileextension_MailboxTrackingFolders)
- [teammobileofflineprofilemembership_MailboxTrackingFolders](#BKMK_teammobileofflineprofilemembership_MailboxTrackingFolders)
- [usermobileofflineprofilemembership_MailboxTrackingFolders](#BKMK_usermobileofflineprofilemembership_MailboxTrackingFolders)
- [organizationdatasyncsubscription_MailboxTrackingFolders](#BKMK_organizationdatasyncsubscription_MailboxTrackingFolders)
- [organizationdatasyncsubscriptionentity_MailboxTrackingFolders](#BKMK_organizationdatasyncsubscriptionentity_MailboxTrackingFolders)
- [organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders](#BKMK_organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders)
- [organizationdatasyncfnostate_MailboxTrackingFolders](#BKMK_organizationdatasyncfnostate_MailboxTrackingFolders)
- [organizationdatasyncstate_MailboxTrackingFolders](#BKMK_organizationdatasyncstate_MailboxTrackingFolders)
- [metadataforarchival_MailboxTrackingFolders](#BKMK_metadataforarchival_MailboxTrackingFolders)
- [retentionconfig_MailboxTrackingFolders](#BKMK_retentionconfig_MailboxTrackingFolders)
- [retentionfailuredetail_MailboxTrackingFolders](#BKMK_retentionfailuredetail_MailboxTrackingFolders)
- [retentionoperation_MailboxTrackingFolders](#BKMK_retentionoperation_MailboxTrackingFolders)
- [retentionoperationdetail_MailboxTrackingFolders](#BKMK_retentionoperationdetail_MailboxTrackingFolders)
- [msdyn_appinsightsmetadata_MailboxTrackingFolders](#BKMK_msdyn_appinsightsmetadata_MailboxTrackingFolders)
- [msdyn_dataflowtemplate_MailboxTrackingFolders](#BKMK_msdyn_dataflowtemplate_MailboxTrackingFolders)
- [msdyn_workflowactionstatus_MailboxTrackingFolders](#BKMK_msdyn_workflowactionstatus_MailboxTrackingFolders)
- [userrating_MailboxTrackingFolders](#BKMK_userrating_MailboxTrackingFolders)
- [msdyn_mobileapp_MailboxTrackingFolders](#BKMK_msdyn_mobileapp_MailboxTrackingFolders)
- [msdyn_insightsstorevirtualentity_MailboxTrackingFolders](#BKMK_msdyn_insightsstorevirtualentity_MailboxTrackingFolders)
- [roleeditorlayout_MailboxTrackingFolders](#BKMK_roleeditorlayout_MailboxTrackingFolders)
- [appaction_MailboxTrackingFolders](#BKMK_appaction_MailboxTrackingFolders)
- [appactionmigration_MailboxTrackingFolders](#BKMK_appactionmigration_MailboxTrackingFolders)
- [appactionrule_MailboxTrackingFolders](#BKMK_appactionrule_MailboxTrackingFolders)
- [card_MailboxTrackingFolders](#BKMK_card_MailboxTrackingFolders)
- [msdyn_entitylinkchatconfiguration_MailboxTrackingFolders](#BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders)
- [msdyn_richtextfile_MailboxTrackingFolders](#BKMK_msdyn_richtextfile_MailboxTrackingFolders)
- [msdyn_customcontrolextendedsettings_MailboxTrackingFolders](#BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders)
- [searchrelationshipsettings_MailboxTrackingFolders](#BKMK_searchrelationshipsettings_MailboxTrackingFolders)
- [msdyn_virtualtablecolumncandidate_MailboxTrackingFolders](#BKMK_msdyn_virtualtablecolumncandidate_MailboxTrackingFolders)
- [msdyn_aiconfiguration_MailboxTrackingFolders](#BKMK_msdyn_aiconfiguration_MailboxTrackingFolders)
- [msdyn_aievent_MailboxTrackingFolders](#BKMK_msdyn_aievent_MailboxTrackingFolders)
- [msdyn_aimodel_MailboxTrackingFolders](#BKMK_msdyn_aimodel_MailboxTrackingFolders)
- [msdyn_aitemplate_MailboxTrackingFolders](#BKMK_msdyn_aitemplate_MailboxTrackingFolders)
- [msdyn_aibfeedbackloop_MailboxTrackingFolders](#BKMK_msdyn_aibfeedbackloop_MailboxTrackingFolders)
- [msdyn_aifptrainingdocument_MailboxTrackingFolders](#BKMK_msdyn_aifptrainingdocument_MailboxTrackingFolders)
- [msdyn_aiodimage_MailboxTrackingFolders](#BKMK_msdyn_aiodimage_MailboxTrackingFolders)
- [msdyn_aiodlabel_MailboxTrackingFolders](#BKMK_msdyn_aiodlabel_MailboxTrackingFolders)
- [msdyn_aiodtrainingboundingbox_MailboxTrackingFolders](#BKMK_msdyn_aiodtrainingboundingbox_MailboxTrackingFolders)
- [msdyn_aiodtrainingimage_MailboxTrackingFolders](#BKMK_msdyn_aiodtrainingimage_MailboxTrackingFolders)
- [msdyn_aibdataset_MailboxTrackingFolders](#BKMK_msdyn_aibdataset_MailboxTrackingFolders)
- [msdyn_aibdatasetfile_MailboxTrackingFolders](#BKMK_msdyn_aibdatasetfile_MailboxTrackingFolders)
- [msdyn_aibdatasetrecord_MailboxTrackingFolders](#BKMK_msdyn_aibdatasetrecord_MailboxTrackingFolders)
- [msdyn_aibdatasetscontainer_MailboxTrackingFolders](#BKMK_msdyn_aibdatasetscontainer_MailboxTrackingFolders)
- [msdyn_aibfile_MailboxTrackingFolders](#BKMK_msdyn_aibfile_MailboxTrackingFolders)
- [msdyn_aibfileattacheddata_MailboxTrackingFolders](#BKMK_msdyn_aibfileattacheddata_MailboxTrackingFolders)
- [msdyn_pmanalysishistory_MailboxTrackingFolders](#BKMK_msdyn_pmanalysishistory_MailboxTrackingFolders)
- [msdyn_pmcalendar_MailboxTrackingFolders](#BKMK_msdyn_pmcalendar_MailboxTrackingFolders)
- [msdyn_pmcalendarversion_MailboxTrackingFolders](#BKMK_msdyn_pmcalendarversion_MailboxTrackingFolders)
- [msdyn_pminferredtask_MailboxTrackingFolders](#BKMK_msdyn_pminferredtask_MailboxTrackingFolders)
- [msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders](#BKMK_msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders)
- [msdyn_pmprocesstemplate_MailboxTrackingFolders](#BKMK_msdyn_pmprocesstemplate_MailboxTrackingFolders)
- [msdyn_pmprocessusersettings_MailboxTrackingFolders](#BKMK_msdyn_pmprocessusersettings_MailboxTrackingFolders)
- [msdyn_pmprocessversion_MailboxTrackingFolders](#BKMK_msdyn_pmprocessversion_MailboxTrackingFolders)
- [msdyn_pmrecording_MailboxTrackingFolders](#BKMK_msdyn_pmrecording_MailboxTrackingFolders)
- [msdyn_pmtemplate_MailboxTrackingFolders](#BKMK_msdyn_pmtemplate_MailboxTrackingFolders)
- [msdyn_pmview_MailboxTrackingFolders](#BKMK_msdyn_pmview_MailboxTrackingFolders)
- [msdyn_analysiscomponent_MailboxTrackingFolders](#BKMK_msdyn_analysiscomponent_MailboxTrackingFolders)
- [msdyn_analysisjob_MailboxTrackingFolders](#BKMK_msdyn_analysisjob_MailboxTrackingFolders)
- [msdyn_analysisoverride_MailboxTrackingFolders](#BKMK_msdyn_analysisoverride_MailboxTrackingFolders)
- [msdyn_analysisresult_MailboxTrackingFolders](#BKMK_msdyn_analysisresult_MailboxTrackingFolders)
- [msdyn_analysisresultdetail_MailboxTrackingFolders](#BKMK_msdyn_analysisresultdetail_MailboxTrackingFolders)
- [msdyn_solutionhealthrule_MailboxTrackingFolders](#BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders)
- [msdyn_solutionhealthruleargument_MailboxTrackingFolders](#BKMK_msdyn_solutionhealthruleargument_MailboxTrackingFolders)
- [msdyn_solutionhealthruleset_MailboxTrackingFolders](#BKMK_msdyn_solutionhealthruleset_MailboxTrackingFolders)
- [powerbidataset_MailboxTrackingFolders](#BKMK_powerbidataset_MailboxTrackingFolders)
- [powerbimashupparameter_MailboxTrackingFolders](#BKMK_powerbimashupparameter_MailboxTrackingFolders)
- [powerbireport_MailboxTrackingFolders](#BKMK_powerbireport_MailboxTrackingFolders)
- [msdyn_fileupload_MailboxTrackingFolders](#BKMK_msdyn_fileupload_MailboxTrackingFolders)
- [mspcat_catalogsubmissionfiles_MailboxTrackingFolders](#BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders)
- [mspcat_packagestore_MailboxTrackingFolders](#BKMK_mspcat_packagestore_MailboxTrackingFolders)
- [msdyn_schedule_MailboxTrackingFolders](#BKMK_msdyn_schedule_MailboxTrackingFolders)
- [msdyn_dataflow_datalakefolder_MailboxTrackingFolders](#BKMK_msdyn_dataflow_datalakefolder_MailboxTrackingFolders)
- [msdyn_dmsrequest_MailboxTrackingFolders](#BKMK_msdyn_dmsrequest_MailboxTrackingFolders)
- [msdyn_dmsrequeststatus_MailboxTrackingFolders](#BKMK_msdyn_dmsrequeststatus_MailboxTrackingFolders)
- [searchattributesettings_MailboxTrackingFolders](#BKMK_searchattributesettings_MailboxTrackingFolders)
- [searchcustomanalyzer_MailboxTrackingFolders](#BKMK_searchcustomanalyzer_MailboxTrackingFolders)


### <a name="BKMK_lk_mailboxtrackingfolder_modifiedby"></a> lk_mailboxtrackingfolder_modifiedby

See the [lk_mailboxtrackingfolder_modifiedby](systemuser.md#BKMK_lk_mailboxtrackingfolder_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_mailboxtrackingfolder_createdby"></a> lk_mailboxtrackingfolder_createdby

See the [lk_mailboxtrackingfolder_createdby](systemuser.md#BKMK_lk_mailboxtrackingfolder_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Account_MailboxTrackingFolder"></a> Account_MailboxTrackingFolder

See the [Account_MailboxTrackingFolder](account.md#BKMK_Account_MailboxTrackingFolder) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_team_mailboxtrackingfolder"></a> team_mailboxtrackingfolder

See the [team_mailboxtrackingfolder](team.md#BKMK_team_mailboxtrackingfolder) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_Contact_MailboxTrackingFolder"></a> Contact_MailboxTrackingFolder

See the [Contact_MailboxTrackingFolder](contact.md#BKMK_Contact_MailboxTrackingFolder) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_lk_mailboxtrackingfolder_createdonbehalfby"></a> lk_mailboxtrackingfolder_createdonbehalfby

See the [lk_mailboxtrackingfolder_createdonbehalfby](systemuser.md#BKMK_lk_mailboxtrackingfolder_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby"></a> lk_mailboxtrackingfolder_modifiedonbehalfby

See the [lk_mailboxtrackingfolder_modifiedonbehalfby](systemuser.md#BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Organization_MailboxTrackingFolder"></a> Organization_MailboxTrackingFolder

See the [Organization_MailboxTrackingFolder](organization.md#BKMK_Organization_MailboxTrackingFolder) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_Mailbox_MailboxTrackingFolder"></a> Mailbox_MailboxTrackingFolder

See the [Mailbox_MailboxTrackingFolder](mailbox.md#BKMK_Mailbox_MailboxTrackingFolder) one-to-many relationship for the [mailbox](mailbox.md) table/entity.

### <a name="BKMK_businessunit_mailboxtrackingfolder"></a> businessunit_mailboxtrackingfolder

See the [businessunit_mailboxtrackingfolder](businessunit.md#BKMK_businessunit_mailboxtrackingfolder) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_AsyncOperation_MailboxTrackingFolder"></a> AsyncOperation_MailboxTrackingFolder

See the [AsyncOperation_MailboxTrackingFolder](asyncoperation.md#BKMK_AsyncOperation_MailboxTrackingFolder) one-to-many relationship for the [asyncoperation](asyncoperation.md) table/entity.

### <a name="BKMK_solutioncomponentattributeconfiguration_MailboxTrackingFolders"></a> solutioncomponentattributeconfiguration_MailboxTrackingFolders

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentattributeconfiguration_MailboxTrackingFolders](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_MailboxTrackingFolders) one-to-many relationship for the [solutioncomponentattributeconfiguration](solutioncomponentattributeconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentbatchconfiguration_MailboxTrackingFolders"></a> solutioncomponentbatchconfiguration_MailboxTrackingFolders

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentbatchconfiguration_MailboxTrackingFolders](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_MailboxTrackingFolders) one-to-many relationship for the [solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentconfiguration_MailboxTrackingFolders"></a> solutioncomponentconfiguration_MailboxTrackingFolders

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentconfiguration_MailboxTrackingFolders](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_MailboxTrackingFolders) one-to-many relationship for the [solutioncomponentconfiguration](solutioncomponentconfiguration.md) table/entity.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders"></a> solutioncomponentrelationshipconfiguration_MailboxTrackingFolders

**Added by**: Solution Component Configuration Solution

See the [solutioncomponentrelationshipconfiguration_MailboxTrackingFolders](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders) one-to-many relationship for the [solutioncomponentrelationshipconfiguration](solutioncomponentrelationshipconfiguration.md) table/entity.

### <a name="BKMK_package_MailboxTrackingFolders"></a> package_MailboxTrackingFolders

**Added by**: msdyn_SolutionPackageMapping Solution

See the [package_MailboxTrackingFolders](package.md#BKMK_package_MailboxTrackingFolders) one-to-many relationship for the [package](package.md) table/entity.

### <a name="BKMK_stagesolutionupload_MailboxTrackingFolders"></a> stagesolutionupload_MailboxTrackingFolders

**Added by**: StageSolutionUpload Solution

See the [stagesolutionupload_MailboxTrackingFolders](stagesolutionupload.md#BKMK_stagesolutionupload_MailboxTrackingFolders) one-to-many relationship for the [stagesolutionupload](stagesolutionupload.md) table/entity.

### <a name="BKMK_exportsolutionupload_MailboxTrackingFolders"></a> exportsolutionupload_MailboxTrackingFolders

**Added by**: ExportSolutionUpload Solution

See the [exportsolutionupload_MailboxTrackingFolders](exportsolutionupload.md#BKMK_exportsolutionupload_MailboxTrackingFolders) one-to-many relationship for the [exportsolutionupload](exportsolutionupload.md) table/entity.

### <a name="BKMK_featurecontrolsetting_MailboxTrackingFolders"></a> featurecontrolsetting_MailboxTrackingFolders

**Added by**: msdyn_FeatureControlSetting Solution

See the [featurecontrolsetting_MailboxTrackingFolders](featurecontrolsetting.md#BKMK_featurecontrolsetting_MailboxTrackingFolders) one-to-many relationship for the [featurecontrolsetting](featurecontrolsetting.md) table/entity.

### <a name="BKMK_attributeimageconfig_MailboxTrackingFolders"></a> attributeimageconfig_MailboxTrackingFolders

**Added by**: Image Configuration Solution

See the [attributeimageconfig_MailboxTrackingFolders](attributeimageconfig.md#BKMK_attributeimageconfig_MailboxTrackingFolders) one-to-many relationship for the [attributeimageconfig](attributeimageconfig.md) table/entity.

### <a name="BKMK_entityimageconfig_MailboxTrackingFolders"></a> entityimageconfig_MailboxTrackingFolders

**Added by**: Image Configuration Solution

See the [entityimageconfig_MailboxTrackingFolders](entityimageconfig.md#BKMK_entityimageconfig_MailboxTrackingFolders) one-to-many relationship for the [entityimageconfig](entityimageconfig.md) table/entity.

### <a name="BKMK_relationshipattribute_MailboxTrackingFolders"></a> relationshipattribute_MailboxTrackingFolders

**Added by**: Metadata Extension Solution

See the [relationshipattribute_MailboxTrackingFolders](relationshipattribute.md#BKMK_relationshipattribute_MailboxTrackingFolders) one-to-many relationship for the [relationshipattribute](relationshipattribute.md) table/entity.

### <a name="BKMK_stagedentity_MailboxTrackingFolders"></a> stagedentity_MailboxTrackingFolders

**Added by**: Metadata Extension Solution

See the [stagedentity_MailboxTrackingFolders](stagedentity.md#BKMK_stagedentity_MailboxTrackingFolders) one-to-many relationship for the [stagedentity](stagedentity.md) table/entity.

### <a name="BKMK_stagedentityattribute_MailboxTrackingFolders"></a> stagedentityattribute_MailboxTrackingFolders

**Added by**: Metadata Extension Solution

See the [stagedentityattribute_MailboxTrackingFolders](stagedentityattribute.md#BKMK_stagedentityattribute_MailboxTrackingFolders) one-to-many relationship for the [stagedentityattribute](stagedentityattribute.md) table/entity.

### <a name="BKMK_catalog_MailboxTrackingFolders"></a> catalog_MailboxTrackingFolders

**Added by**: CatalogFramework Solution

See the [catalog_MailboxTrackingFolders](catalog.md#BKMK_catalog_MailboxTrackingFolders) one-to-many relationship for the [catalog](catalog.md) table/entity.

### <a name="BKMK_catalogassignment_MailboxTrackingFolders"></a> catalogassignment_MailboxTrackingFolders

**Added by**: CatalogFramework Solution

See the [catalogassignment_MailboxTrackingFolders](catalogassignment.md#BKMK_catalogassignment_MailboxTrackingFolders) one-to-many relationship for the [catalogassignment](catalogassignment.md) table/entity.

### <a name="BKMK_customapi_MailboxTrackingFolders"></a> customapi_MailboxTrackingFolders

**Added by**: Custom API Framework Solution

See the [customapi_MailboxTrackingFolders](customapi.md#BKMK_customapi_MailboxTrackingFolders) one-to-many relationship for the [customapi](customapi.md) table/entity.

### <a name="BKMK_customapirequestparameter_MailboxTrackingFolders"></a> customapirequestparameter_MailboxTrackingFolders

**Added by**: Custom API Framework Solution

See the [customapirequestparameter_MailboxTrackingFolders](customapirequestparameter.md#BKMK_customapirequestparameter_MailboxTrackingFolders) one-to-many relationship for the [customapirequestparameter](customapirequestparameter.md) table/entity.

### <a name="BKMK_customapiresponseproperty_MailboxTrackingFolders"></a> customapiresponseproperty_MailboxTrackingFolders

**Added by**: Custom API Framework Solution

See the [customapiresponseproperty_MailboxTrackingFolders](customapiresponseproperty.md#BKMK_customapiresponseproperty_MailboxTrackingFolders) one-to-many relationship for the [customapiresponseproperty](customapiresponseproperty.md) table/entity.

### <a name="BKMK_provisionlanguageforuser_MailboxTrackingFolders"></a> provisionlanguageforuser_MailboxTrackingFolders

**Added by**: msft_LocalizationExtension Solution

See the [provisionlanguageforuser_MailboxTrackingFolders](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_MailboxTrackingFolders) one-to-many relationship for the [provisionlanguageforuser](provisionlanguageforuser.md) table/entity.

### <a name="BKMK_sharedobject_MailboxTrackingFolders"></a> sharedobject_MailboxTrackingFolders

**Added by**: Real-time Collaboration App Solution

See the [sharedobject_MailboxTrackingFolders](sharedobject.md#BKMK_sharedobject_MailboxTrackingFolders) one-to-many relationship for the [sharedobject](sharedobject.md) table/entity.

### <a name="BKMK_sharedworkspace_MailboxTrackingFolders"></a> sharedworkspace_MailboxTrackingFolders

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspace_MailboxTrackingFolders](sharedworkspace.md#BKMK_sharedworkspace_MailboxTrackingFolders) one-to-many relationship for the [sharedworkspace](sharedworkspace.md) table/entity.

### <a name="BKMK_sharedworkspacepool_MailboxTrackingFolders"></a> sharedworkspacepool_MailboxTrackingFolders

**Added by**: Real-time Collaboration App Solution

See the [sharedworkspacepool_MailboxTrackingFolders](sharedworkspacepool.md#BKMK_sharedworkspacepool_MailboxTrackingFolders) one-to-many relationship for the [sharedworkspacepool](sharedworkspacepool.md) table/entity.

### <a name="BKMK_entityanalyticsconfig_MailboxTrackingFolders"></a> entityanalyticsconfig_MailboxTrackingFolders

**Added by**: Advanced Analytics Infrastructure Solution

See the [entityanalyticsconfig_MailboxTrackingFolders](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_MailboxTrackingFolders) one-to-many relationship for the [entityanalyticsconfig](entityanalyticsconfig.md) table/entity.

### <a name="BKMK_datalakefolder_MailboxTrackingFolders"></a> datalakefolder_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See the [datalakefolder_MailboxTrackingFolders](datalakefolder.md#BKMK_datalakefolder_MailboxTrackingFolders) one-to-many relationship for the [datalakefolder](datalakefolder.md) table/entity.

### <a name="BKMK_datalakefolderpermission_MailboxTrackingFolders"></a> datalakefolderpermission_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See the [datalakefolderpermission_MailboxTrackingFolders](datalakefolderpermission.md#BKMK_datalakefolderpermission_MailboxTrackingFolders) one-to-many relationship for the [datalakefolderpermission](datalakefolderpermission.md) table/entity.

### <a name="BKMK_datalakeworkspace_MailboxTrackingFolders"></a> datalakeworkspace_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See the [datalakeworkspace_MailboxTrackingFolders](datalakeworkspace.md#BKMK_datalakeworkspace_MailboxTrackingFolders) one-to-many relationship for the [datalakeworkspace](datalakeworkspace.md) table/entity.

### <a name="BKMK_datalakeworkspacepermission_MailboxTrackingFolders"></a> datalakeworkspacepermission_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See the [datalakeworkspacepermission_MailboxTrackingFolders](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_MailboxTrackingFolders) one-to-many relationship for the [datalakeworkspacepermission](datalakeworkspacepermission.md) table/entity.

### <a name="BKMK_dataprocessingconfiguration_MailboxTrackingFolders"></a> dataprocessingconfiguration_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See the [dataprocessingconfiguration_MailboxTrackingFolders](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_MailboxTrackingFolders) one-to-many relationship for the [dataprocessingconfiguration](dataprocessingconfiguration.md) table/entity.

### <a name="BKMK_exportedexcel_MailboxTrackingFolders"></a> exportedexcel_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See the [exportedexcel_MailboxTrackingFolders](exportedexcel.md#BKMK_exportedexcel_MailboxTrackingFolders) one-to-many relationship for the [exportedexcel](exportedexcel.md) table/entity.

### <a name="BKMK_retaineddataexcel_MailboxTrackingFolders"></a> retaineddataexcel_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See the [retaineddataexcel_MailboxTrackingFolders](retaineddataexcel.md#BKMK_retaineddataexcel_MailboxTrackingFolders) one-to-many relationship for the [retaineddataexcel](retaineddataexcel.md) table/entity.

### <a name="BKMK_synapsedatabase_MailboxTrackingFolders"></a> synapsedatabase_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See the [synapsedatabase_MailboxTrackingFolders](synapsedatabase.md#BKMK_synapsedatabase_MailboxTrackingFolders) one-to-many relationship for the [synapsedatabase](synapsedatabase.md) table/entity.

### <a name="BKMK_synapselinkexternaltablestate_MailboxTrackingFolders"></a> synapselinkexternaltablestate_MailboxTrackingFolders

**Added by**: Synapse Link Solution

See the [synapselinkexternaltablestate_MailboxTrackingFolders](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_MailboxTrackingFolders) one-to-many relationship for the [synapselinkexternaltablestate](synapselinkexternaltablestate.md) table/entity.

### <a name="BKMK_synapselinkprofile_MailboxTrackingFolders"></a> synapselinkprofile_MailboxTrackingFolders

**Added by**: Synapse Link Solution

See the [synapselinkprofile_MailboxTrackingFolders](synapselinkprofile.md#BKMK_synapselinkprofile_MailboxTrackingFolders) one-to-many relationship for the [synapselinkprofile](synapselinkprofile.md) table/entity.

### <a name="BKMK_synapselinkprofileentity_MailboxTrackingFolders"></a> synapselinkprofileentity_MailboxTrackingFolders

**Added by**: Synapse Link Solution

See the [synapselinkprofileentity_MailboxTrackingFolders](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_MailboxTrackingFolders) one-to-many relationship for the [synapselinkprofileentity](synapselinkprofileentity.md) table/entity.

### <a name="BKMK_synapselinkprofileentitystate_MailboxTrackingFolders"></a> synapselinkprofileentitystate_MailboxTrackingFolders

**Added by**: Synapse Link Solution

See the [synapselinkprofileentitystate_MailboxTrackingFolders](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_MailboxTrackingFolders) one-to-many relationship for the [synapselinkprofileentitystate](synapselinkprofileentitystate.md) table/entity.

### <a name="BKMK_synapselinkschedule_MailboxTrackingFolders"></a> synapselinkschedule_MailboxTrackingFolders

**Added by**: Synapse Link Solution

See the [synapselinkschedule_MailboxTrackingFolders](synapselinkschedule.md#BKMK_synapselinkschedule_MailboxTrackingFolders) one-to-many relationship for the [synapselinkschedule](synapselinkschedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_MailboxTrackingFolders"></a> msdyn_dataflow_MailboxTrackingFolders

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflow_MailboxTrackingFolders](msdyn_dataflow.md#BKMK_msdyn_dataflow_MailboxTrackingFolders) one-to-many relationship for the [msdyn_dataflow](msdyn_dataflow.md) table/entity.

### <a name="BKMK_msdyn_dataflowrefreshhistory_MailboxTrackingFolders"></a> msdyn_dataflowrefreshhistory_MailboxTrackingFolders

**Added by**: Dataflow Solution Solution

See the [msdyn_dataflowrefreshhistory_MailboxTrackingFolders](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_MailboxTrackingFolders) one-to-many relationship for the [msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md) table/entity.

### <a name="BKMK_msdyn_entityrefreshhistory_MailboxTrackingFolders"></a> msdyn_entityrefreshhistory_MailboxTrackingFolders

**Added by**: Dataflow Solution Solution

See the [msdyn_entityrefreshhistory_MailboxTrackingFolders](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_MailboxTrackingFolders) one-to-many relationship for the [msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md) table/entity.

### <a name="BKMK_sharedlinksetting_MailboxTrackingFolders"></a> sharedlinksetting_MailboxTrackingFolders

**Added by**: Access Team Solution

See the [sharedlinksetting_MailboxTrackingFolders](sharedlinksetting.md#BKMK_sharedlinksetting_MailboxTrackingFolders) one-to-many relationship for the [sharedlinksetting](sharedlinksetting.md) table/entity.

### <a name="BKMK_entityrecordfilter_MailboxTrackingFolders"></a> entityrecordfilter_MailboxTrackingFolders

**Added by**: AuthorizationCore Solution

See the [entityrecordfilter_MailboxTrackingFolders](entityrecordfilter.md#BKMK_entityrecordfilter_MailboxTrackingFolders) one-to-many relationship for the [entityrecordfilter](entityrecordfilter.md) table/entity.

### <a name="BKMK_recordfilter_MailboxTrackingFolders"></a> recordfilter_MailboxTrackingFolders

**Added by**: AuthorizationCore Solution

See the [recordfilter_MailboxTrackingFolders](recordfilter.md#BKMK_recordfilter_MailboxTrackingFolders) one-to-many relationship for the [recordfilter](recordfilter.md) table/entity.

### <a name="BKMK_delegatedauthorization_MailboxTrackingFolders"></a> delegatedauthorization_MailboxTrackingFolders

**Added by**: Delegated Authorization Solution

See the [delegatedauthorization_MailboxTrackingFolders](delegatedauthorization.md#BKMK_delegatedauthorization_MailboxTrackingFolders) one-to-many relationship for the [delegatedauthorization](delegatedauthorization.md) table/entity.

### <a name="BKMK_serviceplan_MailboxTrackingFolders"></a> serviceplan_MailboxTrackingFolders

**Added by**: License Enforcement Solution

See the [serviceplan_MailboxTrackingFolders](serviceplan.md#BKMK_serviceplan_MailboxTrackingFolders) one-to-many relationship for the [serviceplan](serviceplan.md) table/entity.

### <a name="BKMK_serviceplanmapping_MailboxTrackingFolders"></a> serviceplanmapping_MailboxTrackingFolders

**Added by**: License Enforcement Solution

See the [serviceplanmapping_MailboxTrackingFolders](serviceplanmapping.md#BKMK_serviceplanmapping_MailboxTrackingFolders) one-to-many relationship for the [serviceplanmapping](serviceplanmapping.md) table/entity.

### <a name="BKMK_applicationuser_MailboxTrackingFolders"></a> applicationuser_MailboxTrackingFolders

**Added by**: ApplicationUserSolution Solution

See the [applicationuser_MailboxTrackingFolders](applicationuser.md#BKMK_applicationuser_MailboxTrackingFolders) one-to-many relationship for the [applicationuser](applicationuser.md) table/entity.

### <a name="BKMK_connector_MailboxTrackingFolders"></a> connector_MailboxTrackingFolders

**Added by**: Power Connector Solution Solution

See the [connector_MailboxTrackingFolders](connector.md#BKMK_connector_MailboxTrackingFolders) one-to-many relationship for the [connector](connector.md) table/entity.

### <a name="BKMK_environmentvariabledefinition_MailboxTrackingFolders"></a> environmentvariabledefinition_MailboxTrackingFolders

**Added by**: Environment Variables Solution

See the [environmentvariabledefinition_MailboxTrackingFolders](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_MailboxTrackingFolders) one-to-many relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.

### <a name="BKMK_environmentvariablevalue_MailboxTrackingFolders"></a> environmentvariablevalue_MailboxTrackingFolders

**Added by**: Environment Variables Solution

See the [environmentvariablevalue_MailboxTrackingFolders](environmentvariablevalue.md#BKMK_environmentvariablevalue_MailboxTrackingFolders) one-to-many relationship for the [environmentvariablevalue](environmentvariablevalue.md) table/entity.

### <a name="BKMK_workflowbinary_MailboxTrackingFolders"></a> workflowbinary_MailboxTrackingFolders

**Added by**: Power Automate Extensions Workflow Binary package Solution

See the [workflowbinary_MailboxTrackingFolders](workflowbinary.md#BKMK_workflowbinary_MailboxTrackingFolders) one-to-many relationship for the [workflowbinary](workflowbinary.md) table/entity.

### <a name="BKMK_desktopflowmodule_MailboxTrackingFolders"></a> desktopflowmodule_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowmodule_MailboxTrackingFolders](desktopflowmodule.md#BKMK_desktopflowmodule_MailboxTrackingFolders) one-to-many relationship for the [desktopflowmodule](desktopflowmodule.md) table/entity.

### <a name="BKMK_flowmachine_MailboxTrackingFolders"></a> flowmachine_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See the [flowmachine_MailboxTrackingFolders](flowmachine.md#BKMK_flowmachine_MailboxTrackingFolders) one-to-many relationship for the [flowmachine](flowmachine.md) table/entity.

### <a name="BKMK_flowmachinegroup_MailboxTrackingFolders"></a> flowmachinegroup_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinegroup_MailboxTrackingFolders](flowmachinegroup.md#BKMK_flowmachinegroup_MailboxTrackingFolders) one-to-many relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

### <a name="BKMK_flowmachineimage_MailboxTrackingFolders"></a> flowmachineimage_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimage_MailboxTrackingFolders](flowmachineimage.md#BKMK_flowmachineimage_MailboxTrackingFolders) one-to-many relationship for the [flowmachineimage](flowmachineimage.md) table/entity.

### <a name="BKMK_flowmachineimageversion_MailboxTrackingFolders"></a> flowmachineimageversion_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See the [flowmachineimageversion_MailboxTrackingFolders](flowmachineimageversion.md#BKMK_flowmachineimageversion_MailboxTrackingFolders) one-to-many relationship for the [flowmachineimageversion](flowmachineimageversion.md) table/entity.

### <a name="BKMK_flowmachinenetwork_MailboxTrackingFolders"></a> flowmachinenetwork_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See the [flowmachinenetwork_MailboxTrackingFolders](flowmachinenetwork.md#BKMK_flowmachinenetwork_MailboxTrackingFolders) one-to-many relationship for the [flowmachinenetwork](flowmachinenetwork.md) table/entity.

### <a name="BKMK_processstageparameter_MailboxTrackingFolders"></a> processstageparameter_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See the [processstageparameter_MailboxTrackingFolders](processstageparameter.md#BKMK_processstageparameter_MailboxTrackingFolders) one-to-many relationship for the [processstageparameter](processstageparameter.md) table/entity.

### <a name="BKMK_workqueue_MailboxTrackingFolders"></a> workqueue_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See the [workqueue_MailboxTrackingFolders](workqueue.md#BKMK_workqueue_MailboxTrackingFolders) one-to-many relationship for the [workqueue](workqueue.md) table/entity.

### <a name="BKMK_workqueueitem_MailboxTrackingFolders"></a> workqueueitem_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See the [workqueueitem_MailboxTrackingFolders](workqueueitem.md#BKMK_workqueueitem_MailboxTrackingFolders) one-to-many relationship for the [workqueueitem](workqueueitem.md) table/entity.

### <a name="BKMK_desktopflowbinary_MailboxTrackingFolders"></a> desktopflowbinary_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See the [desktopflowbinary_MailboxTrackingFolders](desktopflowbinary.md#BKMK_desktopflowbinary_MailboxTrackingFolders) one-to-many relationship for the [desktopflowbinary](desktopflowbinary.md) table/entity.

### <a name="BKMK_flowsession_MailboxTrackingFolders"></a> flowsession_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See the [flowsession_MailboxTrackingFolders](flowsession.md#BKMK_flowsession_MailboxTrackingFolders) one-to-many relationship for the [flowsession](flowsession.md) table/entity.

### <a name="BKMK_connectionreference_MailboxTrackingFolders"></a> connectionreference_MailboxTrackingFolders

**Added by**: Power Platform Connection References Solution

See the [connectionreference_MailboxTrackingFolders](connectionreference.md#BKMK_connectionreference_MailboxTrackingFolders) one-to-many relationship for the [connectionreference](connectionreference.md) table/entity.

### <a name="BKMK_connectioninstance_MailboxTrackingFolders"></a> connectioninstance_MailboxTrackingFolders

**Added by**: Connection Instance Solution Solution

See the [connectioninstance_MailboxTrackingFolders](connectioninstance.md#BKMK_connectioninstance_MailboxTrackingFolders) one-to-many relationship for the [connectioninstance](connectioninstance.md) table/entity.

### <a name="BKMK_msdyn_helppage_MailboxTrackingFolders"></a> msdyn_helppage_MailboxTrackingFolders

**Added by**: Contextual Help Solution

See the [msdyn_helppage_MailboxTrackingFolders](msdyn_helppage.md#BKMK_msdyn_helppage_MailboxTrackingFolders) one-to-many relationship for the [msdyn_helppage](msdyn_helppage.md) table/entity.

### <a name="BKMK_msdyn_tour_MailboxTrackingFolders"></a> msdyn_tour_MailboxTrackingFolders

**Added by**: Contextual Help Solution

See the [msdyn_tour_MailboxTrackingFolders](msdyn_tour.md#BKMK_msdyn_tour_MailboxTrackingFolders) one-to-many relationship for the [msdyn_tour](msdyn_tour.md) table/entity.

### <a name="BKMK_msdynce_botcontent_MailboxTrackingFolders"></a> msdynce_botcontent_MailboxTrackingFolders

**Added by**: Customer Care Intelligence Bots Solution

See the [msdynce_botcontent_MailboxTrackingFolders](msdynce_botcontent.md#BKMK_msdynce_botcontent_MailboxTrackingFolders) one-to-many relationship for the [msdynce_botcontent](msdynce_botcontent.md) table/entity.

### <a name="BKMK_conversationtranscript_MailboxTrackingFolders"></a> conversationtranscript_MailboxTrackingFolders

**Added by**: Power Virtual Agents Common Solution

See the [conversationtranscript_MailboxTrackingFolders](conversationtranscript.md#BKMK_conversationtranscript_MailboxTrackingFolders) one-to-many relationship for the [conversationtranscript](conversationtranscript.md) table/entity.

### <a name="BKMK_bot_MailboxTrackingFolders"></a> bot_MailboxTrackingFolders

**Added by**: Power Virtual Agents Solution

See the [bot_MailboxTrackingFolders](bot.md#BKMK_bot_MailboxTrackingFolders) one-to-many relationship for the [bot](bot.md) table/entity.

### <a name="BKMK_botcomponent_MailboxTrackingFolders"></a> botcomponent_MailboxTrackingFolders

**Added by**: Power Virtual Agents Solution

See the [botcomponent_MailboxTrackingFolders](botcomponent.md#BKMK_botcomponent_MailboxTrackingFolders) one-to-many relationship for the [botcomponent](botcomponent.md) table/entity.

### <a name="BKMK_territory_MailboxTrackingFolders"></a> territory_MailboxTrackingFolders

**Added by**: Application Common Solution

See the [territory_MailboxTrackingFolders](territory.md#BKMK_territory_MailboxTrackingFolders) one-to-many relationship for the [territory](territory.md) table/entity.

### <a name="BKMK_activityfileattachment_MailboxTrackingFolders"></a> activityfileattachment_MailboxTrackingFolders

**Added by**: Activities Patch Solution

See the [activityfileattachment_MailboxTrackingFolders](activityfileattachment.md#BKMK_activityfileattachment_MailboxTrackingFolders) one-to-many relationship for the [activityfileattachment](activityfileattachment.md) table/entity.

### <a name="BKMK_chat_MailboxTrackingFolders"></a> chat_MailboxTrackingFolders

**Added by**: Activities Patch Solution

See the [chat_MailboxTrackingFolders](chat.md#BKMK_chat_MailboxTrackingFolders) one-to-many relationship for the [chat](chat.md) table/entity.

### <a name="BKMK_msdyn_serviceconfiguration_MailboxTrackingFolders"></a> msdyn_serviceconfiguration_MailboxTrackingFolders

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_serviceconfiguration_MailboxTrackingFolders](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_MailboxTrackingFolders) one-to-many relationship for the [msdyn_serviceconfiguration](msdyn_serviceconfiguration.md) table/entity.

### <a name="BKMK_msdyn_slakpi_MailboxTrackingFolders"></a> msdyn_slakpi_MailboxTrackingFolders

**Added by**: Service Level Agreement (SLA) Extension Solution

See the [msdyn_slakpi_MailboxTrackingFolders](msdyn_slakpi.md#BKMK_msdyn_slakpi_MailboxTrackingFolders) one-to-many relationship for the [msdyn_slakpi](msdyn_slakpi.md) table/entity.

### <a name="BKMK_msdyn_knowledgemanagementsetting_MailboxTrackingFolders"></a> msdyn_knowledgemanagementsetting_MailboxTrackingFolders

**Added by**: Knowledge Management Patch Solution

See the [msdyn_knowledgemanagementsetting_MailboxTrackingFolders](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_MailboxTrackingFolders) one-to-many relationship for the [msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md) table/entity.

### <a name="BKMK_msdyn_federatedarticle_MailboxTrackingFolders"></a> msdyn_federatedarticle_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticle_MailboxTrackingFolders](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_MailboxTrackingFolders) one-to-many relationship for the [msdyn_federatedarticle](msdyn_federatedarticle.md) table/entity.

### <a name="BKMK_msdyn_federatedarticleincident_MailboxTrackingFolders"></a> msdyn_federatedarticleincident_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_federatedarticleincident_MailboxTrackingFolders](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_MailboxTrackingFolders) one-to-many relationship for the [msdyn_federatedarticleincident](msdyn_federatedarticleincident.md) table/entity.

### <a name="BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders"></a> msdyn_integratedsearchprovider_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_integratedsearchprovider_MailboxTrackingFolders](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders) one-to-many relationship for the [msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md) table/entity.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders"></a> msdyn_kmfederatedsearchconfig_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_kmfederatedsearchconfig_MailboxTrackingFolders](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders) one-to-many relationship for the [msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders"></a> msdyn_knowledgearticleimage_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgearticleimage_MailboxTrackingFolders](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders) one-to-many relationship for the [msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md) table/entity.

### <a name="BKMK_msdyn_knowledgeconfiguration_MailboxTrackingFolders"></a> msdyn_knowledgeconfiguration_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeconfiguration_MailboxTrackingFolders](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_MailboxTrackingFolders) one-to-many relationship for the [msdyn_knowledgeconfiguration](msdyn_knowledgeconfiguration.md) table/entity.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders"></a> msdyn_knowledgeinteractioninsight_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgeinteractioninsight_MailboxTrackingFolders](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders) one-to-many relationship for the [msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders"></a> msdyn_knowledgesearchinsight_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See the [msdyn_knowledgesearchinsight_MailboxTrackingFolders](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders) one-to-many relationship for the [msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md) table/entity.

### <a name="BKMK_msdyn_favoriteknowledgearticle_MailboxTrackingFolders"></a> msdyn_favoriteknowledgearticle_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See the [msdyn_favoriteknowledgearticle_MailboxTrackingFolders](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_MailboxTrackingFolders) one-to-many relationship for the [msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md) table/entity.

### <a name="BKMK_msdyn_kalanguagesetting_MailboxTrackingFolders"></a> msdyn_kalanguagesetting_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See the [msdyn_kalanguagesetting_MailboxTrackingFolders](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_MailboxTrackingFolders) one-to-many relationship for the [msdyn_kalanguagesetting](msdyn_kalanguagesetting.md) table/entity.

### <a name="BKMK_msdyn_kbattachment_MailboxTrackingFolders"></a> msdyn_kbattachment_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See the [msdyn_kbattachment_MailboxTrackingFolders](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_MailboxTrackingFolders) one-to-many relationship for the [msdyn_kbattachment](msdyn_kbattachment.md) table/entity.

### <a name="BKMK_msdyn_kmpersonalizationsetting_MailboxTrackingFolders"></a> msdyn_kmpersonalizationsetting_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See the [msdyn_kmpersonalizationsetting_MailboxTrackingFolders](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_MailboxTrackingFolders) one-to-many relationship for the [msdyn_kmpersonalizationsetting](msdyn_kmpersonalizationsetting.md) table/entity.

### <a name="BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders"></a> msdyn_knowledgearticletemplate_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgearticletemplate_MailboxTrackingFolders](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders) one-to-many relationship for the [msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md) table/entity.

### <a name="BKMK_msdyn_knowledgepersonalfilter_MailboxTrackingFolders"></a> msdyn_knowledgepersonalfilter_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgepersonalfilter_MailboxTrackingFolders](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_MailboxTrackingFolders) one-to-many relationship for the [msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md) table/entity.

### <a name="BKMK_msdyn_knowledgesearchfilter_MailboxTrackingFolders"></a> msdyn_knowledgesearchfilter_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See the [msdyn_knowledgesearchfilter_MailboxTrackingFolders](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_MailboxTrackingFolders) one-to-many relationship for the [msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md) table/entity.

### <a name="BKMK_pluginpackage_MailboxTrackingFolders"></a> pluginpackage_MailboxTrackingFolders

**Added by**: Plugin Infrastructure Extension Solution

See the [pluginpackage_MailboxTrackingFolders](pluginpackage.md#BKMK_pluginpackage_MailboxTrackingFolders) one-to-many relationship for the [pluginpackage](pluginpackage.md) table/entity.

### <a name="BKMK_fxexpression_MailboxTrackingFolders"></a> fxexpression_MailboxTrackingFolders

**Added by**: msft_PowerfxRuleSolution Solution

See the [fxexpression_MailboxTrackingFolders](fxexpression.md#BKMK_fxexpression_MailboxTrackingFolders) one-to-many relationship for the [fxexpression](fxexpression.md) table/entity.

### <a name="BKMK_powerfxrule_MailboxTrackingFolders"></a> powerfxrule_MailboxTrackingFolders

**Added by**: msft_PowerfxRuleSolution Solution

See the [powerfxrule_MailboxTrackingFolders](powerfxrule.md#BKMK_powerfxrule_MailboxTrackingFolders) one-to-many relationship for the [powerfxrule](powerfxrule.md) table/entity.

### <a name="BKMK_keyvaultreference_MailboxTrackingFolders"></a> keyvaultreference_MailboxTrackingFolders

**Added by**: ManagedIdentityExtensions Solution

See the [keyvaultreference_MailboxTrackingFolders](keyvaultreference.md#BKMK_keyvaultreference_MailboxTrackingFolders) one-to-many relationship for the [keyvaultreference](keyvaultreference.md) table/entity.

### <a name="BKMK_managedidentity_MailboxTrackingFolders"></a> managedidentity_MailboxTrackingFolders

**Added by**: ManagedIdentityExtensions Solution

See the [managedidentity_MailboxTrackingFolders](managedidentity.md#BKMK_managedidentity_MailboxTrackingFolders) one-to-many relationship for the [managedidentity](managedidentity.md) table/entity.

### <a name="BKMK_msgraphresourcetosubscription_MailboxTrackingFolders"></a> msgraphresourcetosubscription_MailboxTrackingFolders

**Added by**: msft_ActivitiesInfra_Extensions Solution

See the [msgraphresourcetosubscription_MailboxTrackingFolders](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_MailboxTrackingFolders) one-to-many relationship for the [msgraphresourcetosubscription](msgraphresourcetosubscription.md) table/entity.

### <a name="BKMK_virtualentitymetadata_MailboxTrackingFolders"></a> virtualentitymetadata_MailboxTrackingFolders

**Added by**: RuntimeIntegration Solution

See the [virtualentitymetadata_MailboxTrackingFolders](virtualentitymetadata.md#BKMK_virtualentitymetadata_MailboxTrackingFolders) one-to-many relationship for the [virtualentitymetadata](virtualentitymetadata.md) table/entity.

### <a name="BKMK_mobileofflineprofileextension_MailboxTrackingFolders"></a> mobileofflineprofileextension_MailboxTrackingFolders

**Added by**: MobileOfflineProfileExtensionSolution Solution

See the [mobileofflineprofileextension_MailboxTrackingFolders](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_MailboxTrackingFolders) one-to-many relationship for the [mobileofflineprofileextension](mobileofflineprofileextension.md) table/entity.

### <a name="BKMK_teammobileofflineprofilemembership_MailboxTrackingFolders"></a> teammobileofflineprofilemembership_MailboxTrackingFolders

**Added by**: MobileOfflineMembership Solution

See the [teammobileofflineprofilemembership_MailboxTrackingFolders](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_MailboxTrackingFolders) one-to-many relationship for the [teammobileofflineprofilemembership](teammobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_usermobileofflineprofilemembership_MailboxTrackingFolders"></a> usermobileofflineprofilemembership_MailboxTrackingFolders

**Added by**: MobileOfflineMembership Solution

See the [usermobileofflineprofilemembership_MailboxTrackingFolders](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_MailboxTrackingFolders) one-to-many relationship for the [usermobileofflineprofilemembership](usermobileofflineprofilemembership.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscription_MailboxTrackingFolders"></a> organizationdatasyncsubscription_MailboxTrackingFolders

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscription_MailboxTrackingFolders](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_MailboxTrackingFolders) one-to-many relationship for the [organizationdatasyncsubscription](organizationdatasyncsubscription.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionentity_MailboxTrackingFolders"></a> organizationdatasyncsubscriptionentity_MailboxTrackingFolders

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionentity_MailboxTrackingFolders](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_MailboxTrackingFolders) one-to-many relationship for the [organizationdatasyncsubscriptionentity](organizationdatasyncsubscriptionentity.md) table/entity.

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders"></a> organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders

**Added by**: OrganizationDataSyncSolution Solution

See the [organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_MailboxTrackingFolders) one-to-many relationship for the [organizationdatasyncsubscriptionfnotable](organizationdatasyncsubscriptionfnotable.md) table/entity.

### <a name="BKMK_organizationdatasyncfnostate_MailboxTrackingFolders"></a> organizationdatasyncfnostate_MailboxTrackingFolders

**Added by**: DataSyncState Solution

See the [organizationdatasyncfnostate_MailboxTrackingFolders](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_MailboxTrackingFolders) one-to-many relationship for the [organizationdatasyncfnostate](organizationdatasyncfnostate.md) table/entity.

### <a name="BKMK_organizationdatasyncstate_MailboxTrackingFolders"></a> organizationdatasyncstate_MailboxTrackingFolders

**Added by**: DataSyncState Solution

See the [organizationdatasyncstate_MailboxTrackingFolders](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_MailboxTrackingFolders) one-to-many relationship for the [organizationdatasyncstate](organizationdatasyncstate.md) table/entity.

### <a name="BKMK_metadataforarchival_MailboxTrackingFolders"></a> metadataforarchival_MailboxTrackingFolders

**Added by**: Retention Base Components Solution

See the [metadataforarchival_MailboxTrackingFolders](metadataforarchival.md#BKMK_metadataforarchival_MailboxTrackingFolders) one-to-many relationship for the [metadataforarchival](metadataforarchival.md) table/entity.

### <a name="BKMK_retentionconfig_MailboxTrackingFolders"></a> retentionconfig_MailboxTrackingFolders

**Added by**: Retention Base Components Solution

See the [retentionconfig_MailboxTrackingFolders](retentionconfig.md#BKMK_retentionconfig_MailboxTrackingFolders) one-to-many relationship for the [retentionconfig](retentionconfig.md) table/entity.

### <a name="BKMK_retentionfailuredetail_MailboxTrackingFolders"></a> retentionfailuredetail_MailboxTrackingFolders

**Added by**: Retention Base Components Solution

See the [retentionfailuredetail_MailboxTrackingFolders](retentionfailuredetail.md#BKMK_retentionfailuredetail_MailboxTrackingFolders) one-to-many relationship for the [retentionfailuredetail](retentionfailuredetail.md) table/entity.

### <a name="BKMK_retentionoperation_MailboxTrackingFolders"></a> retentionoperation_MailboxTrackingFolders

**Added by**: Retention Base Components Solution

See the [retentionoperation_MailboxTrackingFolders](retentionoperation.md#BKMK_retentionoperation_MailboxTrackingFolders) one-to-many relationship for the [retentionoperation](retentionoperation.md) table/entity.

### <a name="BKMK_retentionoperationdetail_MailboxTrackingFolders"></a> retentionoperationdetail_MailboxTrackingFolders

**Added by**: Retention Base Components Solution

See the [retentionoperationdetail_MailboxTrackingFolders](retentionoperationdetail.md#BKMK_retentionoperationdetail_MailboxTrackingFolders) one-to-many relationship for the [retentionoperationdetail](retentionoperationdetail.md) table/entity.

### <a name="BKMK_msdyn_appinsightsmetadata_MailboxTrackingFolders"></a> msdyn_appinsightsmetadata_MailboxTrackingFolders

**Added by**: Insights App Platform Solution

See the [msdyn_appinsightsmetadata_MailboxTrackingFolders](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_MailboxTrackingFolders) one-to-many relationship for the [msdyn_appinsightsmetadata](msdyn_appinsightsmetadata.md) table/entity.

### <a name="BKMK_msdyn_dataflowtemplate_MailboxTrackingFolders"></a> msdyn_dataflowtemplate_MailboxTrackingFolders

**Added by**: Insights App Platform Solution

See the [msdyn_dataflowtemplate_MailboxTrackingFolders](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_MailboxTrackingFolders) one-to-many relationship for the [msdyn_dataflowtemplate](msdyn_dataflowtemplate.md) table/entity.

### <a name="BKMK_msdyn_workflowactionstatus_MailboxTrackingFolders"></a> msdyn_workflowactionstatus_MailboxTrackingFolders

**Added by**: Insights App Platform Solution

See the [msdyn_workflowactionstatus_MailboxTrackingFolders](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_MailboxTrackingFolders) one-to-many relationship for the [msdyn_workflowactionstatus](msdyn_workflowactionstatus.md) table/entity.

### <a name="BKMK_userrating_MailboxTrackingFolders"></a> userrating_MailboxTrackingFolders

**Added by**: User Rating Solution

See the [userrating_MailboxTrackingFolders](userrating.md#BKMK_userrating_MailboxTrackingFolders) one-to-many relationship for the [userrating](userrating.md) table/entity.

### <a name="BKMK_msdyn_mobileapp_MailboxTrackingFolders"></a> msdyn_mobileapp_MailboxTrackingFolders

**Added by**: Mobile Apps Solution Solution

See the [msdyn_mobileapp_MailboxTrackingFolders](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_MailboxTrackingFolders) one-to-many relationship for the [msdyn_mobileapp](msdyn_mobileapp.md) table/entity.

### <a name="BKMK_msdyn_insightsstorevirtualentity_MailboxTrackingFolders"></a> msdyn_insightsstorevirtualentity_MailboxTrackingFolders

**Added by**: Insights Store Data Provider Solution

See the [msdyn_insightsstorevirtualentity_MailboxTrackingFolders](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_MailboxTrackingFolders) one-to-many relationship for the [msdyn_insightsstorevirtualentity](msdyn_insightsstorevirtualentity.md) table/entity.

### <a name="BKMK_roleeditorlayout_MailboxTrackingFolders"></a> roleeditorlayout_MailboxTrackingFolders

**Added by**: Role Editor Solution

See the [roleeditorlayout_MailboxTrackingFolders](roleeditorlayout.md#BKMK_roleeditorlayout_MailboxTrackingFolders) one-to-many relationship for the [roleeditorlayout](roleeditorlayout.md) table/entity.

### <a name="BKMK_appaction_MailboxTrackingFolders"></a> appaction_MailboxTrackingFolders

**Added by**: Power Apps Actions Solution

See the [appaction_MailboxTrackingFolders](appaction.md#BKMK_appaction_MailboxTrackingFolders) one-to-many relationship for the [appaction](appaction.md) table/entity.

### <a name="BKMK_appactionmigration_MailboxTrackingFolders"></a> appactionmigration_MailboxTrackingFolders

**Added by**: Power Apps Actions Solution

See the [appactionmigration_MailboxTrackingFolders](appactionmigration.md#BKMK_appactionmigration_MailboxTrackingFolders) one-to-many relationship for the [appactionmigration](appactionmigration.md) table/entity.

### <a name="BKMK_appactionrule_MailboxTrackingFolders"></a> appactionrule_MailboxTrackingFolders

**Added by**: Power Apps Actions Solution

See the [appactionrule_MailboxTrackingFolders](appactionrule.md#BKMK_appactionrule_MailboxTrackingFolders) one-to-many relationship for the [appactionrule](appactionrule.md) table/entity.

### <a name="BKMK_card_MailboxTrackingFolders"></a> card_MailboxTrackingFolders

**Added by**: Power Apps cards Solution

See the [card_MailboxTrackingFolders](card.md#BKMK_card_MailboxTrackingFolders) one-to-many relationship for the [card](card.md) table/entity.

### <a name="BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders"></a> msdyn_entitylinkchatconfiguration_MailboxTrackingFolders

**Added by**: Teams Chat Settings Solution Solution

See the [msdyn_entitylinkchatconfiguration_MailboxTrackingFolders](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_MailboxTrackingFolders) one-to-many relationship for the [msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md) table/entity.

### <a name="BKMK_msdyn_richtextfile_MailboxTrackingFolders"></a> msdyn_richtextfile_MailboxTrackingFolders

**Added by**: Rich Text Editor Solution

See the [msdyn_richtextfile_MailboxTrackingFolders](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_MailboxTrackingFolders) one-to-many relationship for the [msdyn_richtextfile](msdyn_richtextfile.md) table/entity.

### <a name="BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders"></a> msdyn_customcontrolextendedsettings_MailboxTrackingFolders

**Added by**: User Experiences Extended Settings Solution

See the [msdyn_customcontrolextendedsettings_MailboxTrackingFolders](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_MailboxTrackingFolders) one-to-many relationship for the [msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md) table/entity.

### <a name="BKMK_searchrelationshipsettings_MailboxTrackingFolders"></a> searchrelationshipsettings_MailboxTrackingFolders

**Added by**: msdyn_RelevanceSearch Solution

See the [searchrelationshipsettings_MailboxTrackingFolders](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_MailboxTrackingFolders) one-to-many relationship for the [searchrelationshipsettings](searchrelationshipsettings.md) table/entity.

### <a name="BKMK_msdyn_virtualtablecolumncandidate_MailboxTrackingFolders"></a> msdyn_virtualtablecolumncandidate_MailboxTrackingFolders

**Added by**: Virtual Connector Provider Solution

See the [msdyn_virtualtablecolumncandidate_MailboxTrackingFolders](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_MailboxTrackingFolders) one-to-many relationship for the [msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md) table/entity.

### <a name="BKMK_msdyn_aiconfiguration_MailboxTrackingFolders"></a> msdyn_aiconfiguration_MailboxTrackingFolders

**Added by**: AISolution Solution

See the [msdyn_aiconfiguration_MailboxTrackingFolders](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aiconfiguration](msdyn_aiconfiguration.md) table/entity.

### <a name="BKMK_msdyn_aievent_MailboxTrackingFolders"></a> msdyn_aievent_MailboxTrackingFolders

**Added by**: AISolution Solution

See the [msdyn_aievent_MailboxTrackingFolders](msdyn_aievent.md#BKMK_msdyn_aievent_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aievent](msdyn_aievent.md) table/entity.

### <a name="BKMK_msdyn_aimodel_MailboxTrackingFolders"></a> msdyn_aimodel_MailboxTrackingFolders

**Added by**: AISolution Solution

See the [msdyn_aimodel_MailboxTrackingFolders](msdyn_aimodel.md#BKMK_msdyn_aimodel_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.

### <a name="BKMK_msdyn_aitemplate_MailboxTrackingFolders"></a> msdyn_aitemplate_MailboxTrackingFolders

**Added by**: AISolution Solution

See the [msdyn_aitemplate_MailboxTrackingFolders](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aitemplate](msdyn_aitemplate.md) table/entity.

### <a name="BKMK_msdyn_aibfeedbackloop_MailboxTrackingFolders"></a> msdyn_aibfeedbackloop_MailboxTrackingFolders

**Added by**: AISolutionFullAdditions Solution

See the [msdyn_aibfeedbackloop_MailboxTrackingFolders](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md) table/entity.

### <a name="BKMK_msdyn_aifptrainingdocument_MailboxTrackingFolders"></a> msdyn_aifptrainingdocument_MailboxTrackingFolders

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aifptrainingdocument_MailboxTrackingFolders](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md) table/entity.

### <a name="BKMK_msdyn_aiodimage_MailboxTrackingFolders"></a> msdyn_aiodimage_MailboxTrackingFolders

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodimage_MailboxTrackingFolders](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aiodimage](msdyn_aiodimage.md) table/entity.

### <a name="BKMK_msdyn_aiodlabel_MailboxTrackingFolders"></a> msdyn_aiodlabel_MailboxTrackingFolders

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodlabel_MailboxTrackingFolders](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aiodlabel](msdyn_aiodlabel.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_MailboxTrackingFolders"></a> msdyn_aiodtrainingboundingbox_MailboxTrackingFolders

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingboundingbox_MailboxTrackingFolders](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md) table/entity.

### <a name="BKMK_msdyn_aiodtrainingimage_MailboxTrackingFolders"></a> msdyn_aiodtrainingimage_MailboxTrackingFolders

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodtrainingimage_MailboxTrackingFolders](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) table/entity.

### <a name="BKMK_msdyn_aibdataset_MailboxTrackingFolders"></a> msdyn_aibdataset_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdataset_MailboxTrackingFolders](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aibdataset](msdyn_aibdataset.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetfile_MailboxTrackingFolders"></a> msdyn_aibdatasetfile_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetfile_MailboxTrackingFolders](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aibdatasetfile](msdyn_aibdatasetfile.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetrecord_MailboxTrackingFolders"></a> msdyn_aibdatasetrecord_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetrecord_MailboxTrackingFolders](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md) table/entity.

### <a name="BKMK_msdyn_aibdatasetscontainer_MailboxTrackingFolders"></a> msdyn_aibdatasetscontainer_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See the [msdyn_aibdatasetscontainer_MailboxTrackingFolders](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md) table/entity.

### <a name="BKMK_msdyn_aibfile_MailboxTrackingFolders"></a> msdyn_aibfile_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfile_MailboxTrackingFolders](msdyn_aibfile.md#BKMK_msdyn_aibfile_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aibfile](msdyn_aibfile.md) table/entity.

### <a name="BKMK_msdyn_aibfileattacheddata_MailboxTrackingFolders"></a> msdyn_aibfileattacheddata_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See the [msdyn_aibfileattacheddata_MailboxTrackingFolders](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_MailboxTrackingFolders) one-to-many relationship for the [msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md) table/entity.

### <a name="BKMK_msdyn_pmanalysishistory_MailboxTrackingFolders"></a> msdyn_pmanalysishistory_MailboxTrackingFolders

**Added by**: Process Mining Solution

See the [msdyn_pmanalysishistory_MailboxTrackingFolders](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_MailboxTrackingFolders) one-to-many relationship for the [msdyn_pmanalysishistory](msdyn_pmanalysishistory.md) table/entity.

### <a name="BKMK_msdyn_pmcalendar_MailboxTrackingFolders"></a> msdyn_pmcalendar_MailboxTrackingFolders

**Added by**: Process Mining Solution

See the [msdyn_pmcalendar_MailboxTrackingFolders](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_MailboxTrackingFolders) one-to-many relationship for the [msdyn_pmcalendar](msdyn_pmcalendar.md) table/entity.

### <a name="BKMK_msdyn_pmcalendarversion_MailboxTrackingFolders"></a> msdyn_pmcalendarversion_MailboxTrackingFolders

**Added by**: Process Mining Solution

See the [msdyn_pmcalendarversion_MailboxTrackingFolders](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_MailboxTrackingFolders) one-to-many relationship for the [msdyn_pmcalendarversion](msdyn_pmcalendarversion.md) table/entity.

### <a name="BKMK_msdyn_pminferredtask_MailboxTrackingFolders"></a> msdyn_pminferredtask_MailboxTrackingFolders

**Added by**: Process Mining Solution

See the [msdyn_pminferredtask_MailboxTrackingFolders](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_MailboxTrackingFolders) one-to-many relationship for the [msdyn_pminferredtask](msdyn_pminferredtask.md) table/entity.

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders"></a> msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders

**Added by**: Process Mining Solution

See the [msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_MailboxTrackingFolders) one-to-many relationship for the [msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md) table/entity.

### <a name="BKMK_msdyn_pmprocesstemplate_MailboxTrackingFolders"></a> msdyn_pmprocesstemplate_MailboxTrackingFolders

**Added by**: Process Mining Solution

See the [msdyn_pmprocesstemplate_MailboxTrackingFolders](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_MailboxTrackingFolders) one-to-many relationship for the [msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md) table/entity.

### <a name="BKMK_msdyn_pmprocessusersettings_MailboxTrackingFolders"></a> msdyn_pmprocessusersettings_MailboxTrackingFolders

**Added by**: Process Mining Solution

See the [msdyn_pmprocessusersettings_MailboxTrackingFolders](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_MailboxTrackingFolders) one-to-many relationship for the [msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md) table/entity.

### <a name="BKMK_msdyn_pmprocessversion_MailboxTrackingFolders"></a> msdyn_pmprocessversion_MailboxTrackingFolders

**Added by**: Process Mining Solution

See the [msdyn_pmprocessversion_MailboxTrackingFolders](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_MailboxTrackingFolders) one-to-many relationship for the [msdyn_pmprocessversion](msdyn_pmprocessversion.md) table/entity.

### <a name="BKMK_msdyn_pmrecording_MailboxTrackingFolders"></a> msdyn_pmrecording_MailboxTrackingFolders

**Added by**: Process Mining Solution

See the [msdyn_pmrecording_MailboxTrackingFolders](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_MailboxTrackingFolders) one-to-many relationship for the [msdyn_pmrecording](msdyn_pmrecording.md) table/entity.

### <a name="BKMK_msdyn_pmtemplate_MailboxTrackingFolders"></a> msdyn_pmtemplate_MailboxTrackingFolders

**Added by**: Process Mining Solution

See the [msdyn_pmtemplate_MailboxTrackingFolders](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_MailboxTrackingFolders) one-to-many relationship for the [msdyn_pmtemplate](msdyn_pmtemplate.md) table/entity.

### <a name="BKMK_msdyn_pmview_MailboxTrackingFolders"></a> msdyn_pmview_MailboxTrackingFolders

**Added by**: Process Mining Solution

See the [msdyn_pmview_MailboxTrackingFolders](msdyn_pmview.md#BKMK_msdyn_pmview_MailboxTrackingFolders) one-to-many relationship for the [msdyn_pmview](msdyn_pmview.md) table/entity.

### <a name="BKMK_msdyn_analysiscomponent_MailboxTrackingFolders"></a> msdyn_analysiscomponent_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See the [msdyn_analysiscomponent_MailboxTrackingFolders](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_MailboxTrackingFolders) one-to-many relationship for the [msdyn_analysiscomponent](msdyn_analysiscomponent.md) table/entity.

### <a name="BKMK_msdyn_analysisjob_MailboxTrackingFolders"></a> msdyn_analysisjob_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisjob_MailboxTrackingFolders](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_MailboxTrackingFolders) one-to-many relationship for the [msdyn_analysisjob](msdyn_analysisjob.md) table/entity.

### <a name="BKMK_msdyn_analysisoverride_MailboxTrackingFolders"></a> msdyn_analysisoverride_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisoverride_MailboxTrackingFolders](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_MailboxTrackingFolders) one-to-many relationship for the [msdyn_analysisoverride](msdyn_analysisoverride.md) table/entity.

### <a name="BKMK_msdyn_analysisresult_MailboxTrackingFolders"></a> msdyn_analysisresult_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresult_MailboxTrackingFolders](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_MailboxTrackingFolders) one-to-many relationship for the [msdyn_analysisresult](msdyn_analysisresult.md) table/entity.

### <a name="BKMK_msdyn_analysisresultdetail_MailboxTrackingFolders"></a> msdyn_analysisresultdetail_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See the [msdyn_analysisresultdetail_MailboxTrackingFolders](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_MailboxTrackingFolders) one-to-many relationship for the [msdyn_analysisresultdetail](msdyn_analysisresultdetail.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders"></a> msdyn_solutionhealthrule_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthrule_MailboxTrackingFolders](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders) one-to-many relationship for the [msdyn_solutionhealthrule](msdyn_solutionhealthrule.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleargument_MailboxTrackingFolders"></a> msdyn_solutionhealthruleargument_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleargument_MailboxTrackingFolders](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_MailboxTrackingFolders) one-to-many relationship for the [msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md) table/entity.

### <a name="BKMK_msdyn_solutionhealthruleset_MailboxTrackingFolders"></a> msdyn_solutionhealthruleset_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See the [msdyn_solutionhealthruleset_MailboxTrackingFolders](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_MailboxTrackingFolders) one-to-many relationship for the [msdyn_solutionhealthruleset](msdyn_solutionhealthruleset.md) table/entity.

### <a name="BKMK_powerbidataset_MailboxTrackingFolders"></a> powerbidataset_MailboxTrackingFolders

**Added by**: Power BI Entities Solution

See the [powerbidataset_MailboxTrackingFolders](powerbidataset.md#BKMK_powerbidataset_MailboxTrackingFolders) one-to-many relationship for the [powerbidataset](powerbidataset.md) table/entity.

### <a name="BKMK_powerbimashupparameter_MailboxTrackingFolders"></a> powerbimashupparameter_MailboxTrackingFolders

**Added by**: Power BI Entities Solution

See the [powerbimashupparameter_MailboxTrackingFolders](powerbimashupparameter.md#BKMK_powerbimashupparameter_MailboxTrackingFolders) one-to-many relationship for the [powerbimashupparameter](powerbimashupparameter.md) table/entity.

### <a name="BKMK_powerbireport_MailboxTrackingFolders"></a> powerbireport_MailboxTrackingFolders

**Added by**: Power BI Entities Solution

See the [powerbireport_MailboxTrackingFolders](powerbireport.md#BKMK_powerbireport_MailboxTrackingFolders) one-to-many relationship for the [powerbireport](powerbireport.md) table/entity.

### <a name="BKMK_msdyn_fileupload_MailboxTrackingFolders"></a> msdyn_fileupload_MailboxTrackingFolders

**Added by**: Smart Data Import Base Solution

See the [msdyn_fileupload_MailboxTrackingFolders](msdyn_fileupload.md#BKMK_msdyn_fileupload_MailboxTrackingFolders) one-to-many relationship for the [msdyn_fileupload](msdyn_fileupload.md) table/entity.

### <a name="BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders"></a> mspcat_catalogsubmissionfiles_MailboxTrackingFolders

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_catalogsubmissionfiles_MailboxTrackingFolders](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_MailboxTrackingFolders) one-to-many relationship for the [mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md) table/entity.

### <a name="BKMK_mspcat_packagestore_MailboxTrackingFolders"></a> mspcat_packagestore_MailboxTrackingFolders

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_packagestore_MailboxTrackingFolders](mspcat_packagestore.md#BKMK_mspcat_packagestore_MailboxTrackingFolders) one-to-many relationship for the [mspcat_packagestore](mspcat_packagestore.md) table/entity.

### <a name="BKMK_msdyn_schedule_MailboxTrackingFolders"></a> msdyn_schedule_MailboxTrackingFolders

**Added by**: Insights App Platform Solution

See the [msdyn_schedule_MailboxTrackingFolders](msdyn_schedule.md#BKMK_msdyn_schedule_MailboxTrackingFolders) one-to-many relationship for the [msdyn_schedule](msdyn_schedule.md) table/entity.

### <a name="BKMK_msdyn_dataflow_datalakefolder_MailboxTrackingFolders"></a> msdyn_dataflow_datalakefolder_MailboxTrackingFolders

**Added by**: Insights App Platform Solution

See the [msdyn_dataflow_datalakefolder_MailboxTrackingFolders](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_MailboxTrackingFolders) one-to-many relationship for the [msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md) table/entity.

### <a name="BKMK_msdyn_dmsrequest_MailboxTrackingFolders"></a> msdyn_dmsrequest_MailboxTrackingFolders

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequest_MailboxTrackingFolders](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_MailboxTrackingFolders) one-to-many relationship for the [msdyn_dmsrequest](msdyn_dmsrequest.md) table/entity.

### <a name="BKMK_msdyn_dmsrequeststatus_MailboxTrackingFolders"></a> msdyn_dmsrequeststatus_MailboxTrackingFolders

**Added by**: Insights App Platform Solution

See the [msdyn_dmsrequeststatus_MailboxTrackingFolders](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_MailboxTrackingFolders) one-to-many relationship for the [msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md) table/entity.

### <a name="BKMK_searchattributesettings_MailboxTrackingFolders"></a> searchattributesettings_MailboxTrackingFolders

**Added by**: msdyn_RelevanceSearch Solution

See the [searchattributesettings_MailboxTrackingFolders](searchattributesettings.md#BKMK_searchattributesettings_MailboxTrackingFolders) one-to-many relationship for the [searchattributesettings](searchattributesettings.md) table/entity.

### <a name="BKMK_searchcustomanalyzer_MailboxTrackingFolders"></a> searchcustomanalyzer_MailboxTrackingFolders

**Added by**: msdyn_RelevanceSearch Solution

See the [searchcustomanalyzer_MailboxTrackingFolders](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_MailboxTrackingFolders) one-to-many relationship for the [searchcustomanalyzer](searchcustomanalyzer.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mailboxtrackingfolder?text=mailboxtrackingfolder EntityType" />