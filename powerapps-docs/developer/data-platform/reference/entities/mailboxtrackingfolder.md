---
title: "Mailbox Auto Tracking Folder (MailboxTrackingFolder) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Mailbox Auto Tracking Folder (MailboxTrackingFolder) table/entity."
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

# Mailbox Auto Tracking Folder (MailboxTrackingFolder) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Stores data about what folders for a mailbox are auto tracked


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/mailboxtrackingfolders<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/mailboxtrackingfolders(*mailboxtrackingfolderid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/mailboxtrackingfolders(*mailboxtrackingfolderid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/mailboxtrackingfolders<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/mailboxtrackingfolders(*mailboxtrackingfolderid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

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
|Targets|account,activityfileattachment,appaction,appelement,applicationuser,appmodulecomponentedge,appmodulecomponentnode,appsetting,appusersetting,asyncoperation,attributeimageconfig,bot,botcomponent,canvasappextendedmetadata,cascadegrantrevokeaccessrecordstracker,cascadegrantrevokeaccessversiontracker,catalog,catalogassignment,comment,connectionreference,connector,contact,conversationtranscript,customapi,customapirequestparameter,customapiresponseproperty,datalakefolder,datalakefolderpermission,datalakeworkspace,datalakeworkspacepermission,entityanalyticsconfig,entityimageconfig,entityindex,environmentvariabledefinition,environmentvariablevalue,exportsolutionupload,featurecontrolsetting,flowmachine,flowmachinegroup,flowsession,holidaywrapper,indexattributes,internalcatalogassignment,keyvaultreference,managedidentity,msdynce_botcontent,msdyn_aibdataset,msdyn_aibdatasetfile,msdyn_aibdatasetrecord,msdyn_aibdatasetscontainer,msdyn_aibfile,msdyn_aibfileattacheddata,msdyn_aiconfiguration,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,msdyn_aiodlabel,msdyn_aiodtrainingboundingbox,msdyn_aiodtrainingimage,msdyn_aitemplate,msdyn_analysiscomponent,msdyn_analysisjob,msdyn_analysisresult,msdyn_analysisresultdetail,msdyn_dataflow,msdyn_federatedarticle,msdyn_federatedarticleincident,msdyn_helppage,msdyn_kalanguagesetting,msdyn_kbattachment,msdyn_kmfederatedsearchconfig,msdyn_kmpersonalizationsetting,msdyn_knowledgearticleimage,msdyn_knowledgearticletemplate,msdyn_knowledgeinteractioninsight,msdyn_knowledgepersonalfilter,msdyn_knowledgesearchfilter,msdyn_knowledgesearchinsight,msdyn_pminferredtask,msdyn_pmrecording,msdyn_richtextfile,msdyn_serviceconfiguration,msdyn_slakpi,msdyn_solutionhealthrule,msdyn_solutionhealthruleargument,msdyn_solutionhealthruleset,msdyn_tour,organizationdatasyncsubscription,organizationdatasyncsubscriptionentity,organizationsetting,package,pdfsetting,pluginpackage,processstageparameter,provisionlanguageforuser,relationshipattribute,revokeinheritedaccessrecordstracker,serviceplan,serviceplanmapping,settingdefinition,solutioncomponentattributeconfiguration,solutioncomponentbatchconfiguration,solutioncomponentconfiguration,solutioncomponentrelationshipconfiguration,stagesolutionupload,systemuserauthorizationchangetracker,teammobileofflineprofilemembership,territory,usermobileofflineprofilemembership,virtualentitymetadata,workflowbinary|
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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


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
- [catalog_MailboxTrackingFolders](#BKMK_catalog_MailboxTrackingFolders)
- [catalogassignment_MailboxTrackingFolders](#BKMK_catalogassignment_MailboxTrackingFolders)
- [customapi_MailboxTrackingFolders](#BKMK_customapi_MailboxTrackingFolders)
- [customapirequestparameter_MailboxTrackingFolders](#BKMK_customapirequestparameter_MailboxTrackingFolders)
- [customapiresponseproperty_MailboxTrackingFolders](#BKMK_customapiresponseproperty_MailboxTrackingFolders)
- [provisionlanguageforuser_MailboxTrackingFolders](#BKMK_provisionlanguageforuser_MailboxTrackingFolders)
- [entityanalyticsconfig_MailboxTrackingFolders](#BKMK_entityanalyticsconfig_MailboxTrackingFolders)
- [datalakefolder_MailboxTrackingFolders](#BKMK_datalakefolder_MailboxTrackingFolders)
- [datalakefolderpermission_MailboxTrackingFolders](#BKMK_datalakefolderpermission_MailboxTrackingFolders)
- [datalakeworkspace_MailboxTrackingFolders](#BKMK_datalakeworkspace_MailboxTrackingFolders)
- [datalakeworkspacepermission_MailboxTrackingFolders](#BKMK_datalakeworkspacepermission_MailboxTrackingFolders)
- [msdyn_dataflow_MailboxTrackingFolders](#BKMK_msdyn_dataflow_MailboxTrackingFolders)
- [serviceplan_MailboxTrackingFolders](#BKMK_serviceplan_MailboxTrackingFolders)
- [serviceplanmapping_MailboxTrackingFolders](#BKMK_serviceplanmapping_MailboxTrackingFolders)
- [applicationuser_MailboxTrackingFolders](#BKMK_applicationuser_MailboxTrackingFolders)
- [connector_MailboxTrackingFolders](#BKMK_connector_MailboxTrackingFolders)
- [environmentvariabledefinition_MailboxTrackingFolders](#BKMK_environmentvariabledefinition_MailboxTrackingFolders)
- [environmentvariablevalue_MailboxTrackingFolders](#BKMK_environmentvariablevalue_MailboxTrackingFolders)
- [flowmachine_MailboxTrackingFolders](#BKMK_flowmachine_MailboxTrackingFolders)
- [flowmachinegroup_MailboxTrackingFolders](#BKMK_flowmachinegroup_MailboxTrackingFolders)
- [processstageparameter_MailboxTrackingFolders](#BKMK_processstageparameter_MailboxTrackingFolders)
- [flowsession_MailboxTrackingFolders](#BKMK_flowsession_MailboxTrackingFolders)
- [workflowbinary_MailboxTrackingFolders](#BKMK_workflowbinary_MailboxTrackingFolders)
- [connectionreference_MailboxTrackingFolders](#BKMK_connectionreference_MailboxTrackingFolders)
- [msdyn_aiconfiguration_MailboxTrackingFolders](#BKMK_msdyn_aiconfiguration_MailboxTrackingFolders)
- [msdyn_aimodel_MailboxTrackingFolders](#BKMK_msdyn_aimodel_MailboxTrackingFolders)
- [msdyn_aitemplate_MailboxTrackingFolders](#BKMK_msdyn_aitemplate_MailboxTrackingFolders)
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
- [msdyn_helppage_MailboxTrackingFolders](#BKMK_msdyn_helppage_MailboxTrackingFolders)
- [msdyn_tour_MailboxTrackingFolders](#BKMK_msdyn_tour_MailboxTrackingFolders)
- [msdynce_botcontent_MailboxTrackingFolders](#BKMK_msdynce_botcontent_MailboxTrackingFolders)
- [conversationtranscript_MailboxTrackingFolders](#BKMK_conversationtranscript_MailboxTrackingFolders)
- [bot_MailboxTrackingFolders](#BKMK_bot_MailboxTrackingFolders)
- [botcomponent_MailboxTrackingFolders](#BKMK_botcomponent_MailboxTrackingFolders)
- [territory_MailboxTrackingFolders](#BKMK_territory_MailboxTrackingFolders)
- [activityfileattachment_MailboxTrackingFolders](#BKMK_activityfileattachment_MailboxTrackingFolders)
- [msdyn_serviceconfiguration_MailboxTrackingFolders](#BKMK_msdyn_serviceconfiguration_MailboxTrackingFolders)
- [msdyn_slakpi_MailboxTrackingFolders](#BKMK_msdyn_slakpi_MailboxTrackingFolders)
- [msdyn_federatedarticle_MailboxTrackingFolders](#BKMK_msdyn_federatedarticle_MailboxTrackingFolders)
- [msdyn_federatedarticleincident_MailboxTrackingFolders](#BKMK_msdyn_federatedarticleincident_MailboxTrackingFolders)
- [msdyn_kmfederatedsearchconfig_MailboxTrackingFolders](#BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders)
- [msdyn_knowledgearticleimage_MailboxTrackingFolders](#BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders)
- [msdyn_knowledgeinteractioninsight_MailboxTrackingFolders](#BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders)
- [msdyn_knowledgesearchinsight_MailboxTrackingFolders](#BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders)
- [msdyn_kalanguagesetting_MailboxTrackingFolders](#BKMK_msdyn_kalanguagesetting_MailboxTrackingFolders)
- [msdyn_kbattachment_MailboxTrackingFolders](#BKMK_msdyn_kbattachment_MailboxTrackingFolders)
- [msdyn_kmpersonalizationsetting_MailboxTrackingFolders](#BKMK_msdyn_kmpersonalizationsetting_MailboxTrackingFolders)
- [msdyn_knowledgearticletemplate_MailboxTrackingFolders](#BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders)
- [msdyn_knowledgepersonalfilter_MailboxTrackingFolders](#BKMK_msdyn_knowledgepersonalfilter_MailboxTrackingFolders)
- [msdyn_knowledgesearchfilter_MailboxTrackingFolders](#BKMK_msdyn_knowledgesearchfilter_MailboxTrackingFolders)
- [pluginpackage_MailboxTrackingFolders](#BKMK_pluginpackage_MailboxTrackingFolders)
- [keyvaultreference_MailboxTrackingFolders](#BKMK_keyvaultreference_MailboxTrackingFolders)
- [managedidentity_MailboxTrackingFolders](#BKMK_managedidentity_MailboxTrackingFolders)
- [virtualentitymetadata_MailboxTrackingFolders](#BKMK_virtualentitymetadata_MailboxTrackingFolders)
- [organizationdatasyncsubscription_MailboxTrackingFolders](#BKMK_organizationdatasyncsubscription_MailboxTrackingFolders)
- [organizationdatasyncsubscriptionentity_MailboxTrackingFolders](#BKMK_organizationdatasyncsubscriptionentity_MailboxTrackingFolders)
- [appaction_MailboxTrackingFolders](#BKMK_appaction_MailboxTrackingFolders)
- [msdyn_richtextfile_MailboxTrackingFolders](#BKMK_msdyn_richtextfile_MailboxTrackingFolders)
- [msdyn_pminferredtask_MailboxTrackingFolders](#BKMK_msdyn_pminferredtask_MailboxTrackingFolders)
- [msdyn_pmrecording_MailboxTrackingFolders](#BKMK_msdyn_pmrecording_MailboxTrackingFolders)
- [msdyn_analysiscomponent_MailboxTrackingFolders](#BKMK_msdyn_analysiscomponent_MailboxTrackingFolders)
- [msdyn_analysisjob_MailboxTrackingFolders](#BKMK_msdyn_analysisjob_MailboxTrackingFolders)
- [msdyn_analysisresult_MailboxTrackingFolders](#BKMK_msdyn_analysisresult_MailboxTrackingFolders)
- [msdyn_analysisresultdetail_MailboxTrackingFolders](#BKMK_msdyn_analysisresultdetail_MailboxTrackingFolders)
- [msdyn_solutionhealthrule_MailboxTrackingFolders](#BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders)
- [msdyn_solutionhealthruleargument_MailboxTrackingFolders](#BKMK_msdyn_solutionhealthruleargument_MailboxTrackingFolders)
- [msdyn_solutionhealthruleset_MailboxTrackingFolders](#BKMK_msdyn_solutionhealthruleset_MailboxTrackingFolders)


### <a name="BKMK_lk_mailboxtrackingfolder_modifiedby"></a> lk_mailboxtrackingfolder_modifiedby

See systemuser Table [lk_mailboxtrackingfolder_modifiedby](systemuser.md#BKMK_lk_mailboxtrackingfolder_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_mailboxtrackingfolder_createdby"></a> lk_mailboxtrackingfolder_createdby

See systemuser Table [lk_mailboxtrackingfolder_createdby](systemuser.md#BKMK_lk_mailboxtrackingfolder_createdby) One-To-Many relationship.

### <a name="BKMK_Account_MailboxTrackingFolder"></a> Account_MailboxTrackingFolder

See account Table [Account_MailboxTrackingFolder](account.md#BKMK_Account_MailboxTrackingFolder) One-To-Many relationship.

### <a name="BKMK_team_mailboxtrackingfolder"></a> team_mailboxtrackingfolder

See team Table [team_mailboxtrackingfolder](team.md#BKMK_team_mailboxtrackingfolder) One-To-Many relationship.

### <a name="BKMK_Contact_MailboxTrackingFolder"></a> Contact_MailboxTrackingFolder

See contact Table [Contact_MailboxTrackingFolder](contact.md#BKMK_Contact_MailboxTrackingFolder) One-To-Many relationship.

### <a name="BKMK_lk_mailboxtrackingfolder_createdonbehalfby"></a> lk_mailboxtrackingfolder_createdonbehalfby

See systemuser Table [lk_mailboxtrackingfolder_createdonbehalfby](systemuser.md#BKMK_lk_mailboxtrackingfolder_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby"></a> lk_mailboxtrackingfolder_modifiedonbehalfby

See systemuser Table [lk_mailboxtrackingfolder_modifiedonbehalfby](systemuser.md#BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_Organization_MailboxTrackingFolder"></a> Organization_MailboxTrackingFolder

See organization Table [Organization_MailboxTrackingFolder](organization.md#BKMK_Organization_MailboxTrackingFolder) One-To-Many relationship.

### <a name="BKMK_Mailbox_MailboxTrackingFolder"></a> Mailbox_MailboxTrackingFolder

See mailbox Table [Mailbox_MailboxTrackingFolder](mailbox.md#BKMK_Mailbox_MailboxTrackingFolder) One-To-Many relationship.

### <a name="BKMK_businessunit_mailboxtrackingfolder"></a> businessunit_mailboxtrackingfolder

See businessunit Table [businessunit_mailboxtrackingfolder](businessunit.md#BKMK_businessunit_mailboxtrackingfolder) One-To-Many relationship.

### <a name="BKMK_AsyncOperation_MailboxTrackingFolder"></a> AsyncOperation_MailboxTrackingFolder

See asyncoperation Table [AsyncOperation_MailboxTrackingFolder](asyncoperation.md#BKMK_AsyncOperation_MailboxTrackingFolder) One-To-Many relationship.

### <a name="BKMK_solutioncomponentattributeconfiguration_MailboxTrackingFolders"></a> solutioncomponentattributeconfiguration_MailboxTrackingFolders

**Added by**: Solution Component Configuration Solution

See solutioncomponentattributeconfiguration Table [solutioncomponentattributeconfiguration_MailboxTrackingFolders](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_solutioncomponentbatchconfiguration_MailboxTrackingFolders"></a> solutioncomponentbatchconfiguration_MailboxTrackingFolders

**Added by**: Solution Component Configuration Solution

See solutioncomponentbatchconfiguration Table [solutioncomponentbatchconfiguration_MailboxTrackingFolders](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_solutioncomponentconfiguration_MailboxTrackingFolders"></a> solutioncomponentconfiguration_MailboxTrackingFolders

**Added by**: Solution Component Configuration Solution

See solutioncomponentconfiguration Table [solutioncomponentconfiguration_MailboxTrackingFolders](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders"></a> solutioncomponentrelationshipconfiguration_MailboxTrackingFolders

**Added by**: Solution Component Configuration Solution

See solutioncomponentrelationshipconfiguration Table [solutioncomponentrelationshipconfiguration_MailboxTrackingFolders](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_package_MailboxTrackingFolders"></a> package_MailboxTrackingFolders

**Added by**: msdyn_SolutionPackageMapping Solution

See package Table [package_MailboxTrackingFolders](package.md#BKMK_package_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_stagesolutionupload_MailboxTrackingFolders"></a> stagesolutionupload_MailboxTrackingFolders

**Added by**: StageSolutionUpload Solution

See stagesolutionupload Table [stagesolutionupload_MailboxTrackingFolders](stagesolutionupload.md#BKMK_stagesolutionupload_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_exportsolutionupload_MailboxTrackingFolders"></a> exportsolutionupload_MailboxTrackingFolders

**Added by**: ExportSolutionUpload Solution

See exportsolutionupload Table [exportsolutionupload_MailboxTrackingFolders](exportsolutionupload.md#BKMK_exportsolutionupload_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_featurecontrolsetting_MailboxTrackingFolders"></a> featurecontrolsetting_MailboxTrackingFolders

**Added by**: msdyn_FeatureControlSetting Solution

See featurecontrolsetting Table [featurecontrolsetting_MailboxTrackingFolders](featurecontrolsetting.md#BKMK_featurecontrolsetting_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_attributeimageconfig_MailboxTrackingFolders"></a> attributeimageconfig_MailboxTrackingFolders

**Added by**: Image Configuration Solution

See attributeimageconfig Table [attributeimageconfig_MailboxTrackingFolders](attributeimageconfig.md#BKMK_attributeimageconfig_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_entityimageconfig_MailboxTrackingFolders"></a> entityimageconfig_MailboxTrackingFolders

**Added by**: Image Configuration Solution

See entityimageconfig Table [entityimageconfig_MailboxTrackingFolders](entityimageconfig.md#BKMK_entityimageconfig_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_relationshipattribute_MailboxTrackingFolders"></a> relationshipattribute_MailboxTrackingFolders

**Added by**: Metadata Extension Solution

See relationshipattribute Table [relationshipattribute_MailboxTrackingFolders](relationshipattribute.md#BKMK_relationshipattribute_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_catalog_MailboxTrackingFolders"></a> catalog_MailboxTrackingFolders

**Added by**: CatalogFramework Solution

See catalog Table [catalog_MailboxTrackingFolders](catalog.md#BKMK_catalog_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_catalogassignment_MailboxTrackingFolders"></a> catalogassignment_MailboxTrackingFolders

**Added by**: CatalogFramework Solution

See catalogassignment Table [catalogassignment_MailboxTrackingFolders](catalogassignment.md#BKMK_catalogassignment_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_customapi_MailboxTrackingFolders"></a> customapi_MailboxTrackingFolders

**Added by**: Custom API Framework Solution

See customapi Table [customapi_MailboxTrackingFolders](customapi.md#BKMK_customapi_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_customapirequestparameter_MailboxTrackingFolders"></a> customapirequestparameter_MailboxTrackingFolders

**Added by**: Custom API Framework Solution

See customapirequestparameter Table [customapirequestparameter_MailboxTrackingFolders](customapirequestparameter.md#BKMK_customapirequestparameter_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_customapiresponseproperty_MailboxTrackingFolders"></a> customapiresponseproperty_MailboxTrackingFolders

**Added by**: Custom API Framework Solution

See customapiresponseproperty Table [customapiresponseproperty_MailboxTrackingFolders](customapiresponseproperty.md#BKMK_customapiresponseproperty_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_provisionlanguageforuser_MailboxTrackingFolders"></a> provisionlanguageforuser_MailboxTrackingFolders

**Added by**: msft_LocalizationExtension Solution

See provisionlanguageforuser Table [provisionlanguageforuser_MailboxTrackingFolders](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_entityanalyticsconfig_MailboxTrackingFolders"></a> entityanalyticsconfig_MailboxTrackingFolders

**Added by**: Advanced Analytics Infrastructure Solution

See entityanalyticsconfig Table [entityanalyticsconfig_MailboxTrackingFolders](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_datalakefolder_MailboxTrackingFolders"></a> datalakefolder_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See datalakefolder Table [datalakefolder_MailboxTrackingFolders](datalakefolder.md#BKMK_datalakefolder_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_datalakefolderpermission_MailboxTrackingFolders"></a> datalakefolderpermission_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See datalakefolderpermission Table [datalakefolderpermission_MailboxTrackingFolders](datalakefolderpermission.md#BKMK_datalakefolderpermission_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_datalakeworkspace_MailboxTrackingFolders"></a> datalakeworkspace_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See datalakeworkspace Table [datalakeworkspace_MailboxTrackingFolders](datalakeworkspace.md#BKMK_datalakeworkspace_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_datalakeworkspacepermission_MailboxTrackingFolders"></a> datalakeworkspacepermission_MailboxTrackingFolders

**Added by**: Data lake workspaces Solution

See datalakeworkspacepermission Table [datalakeworkspacepermission_MailboxTrackingFolders](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_dataflow_MailboxTrackingFolders"></a> msdyn_dataflow_MailboxTrackingFolders

**Added by**: Dataflow Solution Solution

See msdyn_dataflow Table [msdyn_dataflow_MailboxTrackingFolders](msdyn_dataflow.md#BKMK_msdyn_dataflow_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_serviceplan_MailboxTrackingFolders"></a> serviceplan_MailboxTrackingFolders

**Added by**: License Enforcement Solution

See serviceplan Table [serviceplan_MailboxTrackingFolders](serviceplan.md#BKMK_serviceplan_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_serviceplanmapping_MailboxTrackingFolders"></a> serviceplanmapping_MailboxTrackingFolders

**Added by**: License Enforcement Solution

See serviceplanmapping Table [serviceplanmapping_MailboxTrackingFolders](serviceplanmapping.md#BKMK_serviceplanmapping_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_applicationuser_MailboxTrackingFolders"></a> applicationuser_MailboxTrackingFolders

**Added by**: ApplicationUserSolution Solution

See applicationuser Table [applicationuser_MailboxTrackingFolders](applicationuser.md#BKMK_applicationuser_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_connector_MailboxTrackingFolders"></a> connector_MailboxTrackingFolders

**Added by**: Power Connector Solution Solution

See connector Table [connector_MailboxTrackingFolders](connector.md#BKMK_connector_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_environmentvariabledefinition_MailboxTrackingFolders"></a> environmentvariabledefinition_MailboxTrackingFolders

**Added by**: Environment Variables Solution

See environmentvariabledefinition Table [environmentvariabledefinition_MailboxTrackingFolders](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_environmentvariablevalue_MailboxTrackingFolders"></a> environmentvariablevalue_MailboxTrackingFolders

**Added by**: Environment Variables Solution

See environmentvariablevalue Table [environmentvariablevalue_MailboxTrackingFolders](environmentvariablevalue.md#BKMK_environmentvariablevalue_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_flowmachine_MailboxTrackingFolders"></a> flowmachine_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See flowmachine Table [flowmachine_MailboxTrackingFolders](flowmachine.md#BKMK_flowmachine_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_flowmachinegroup_MailboxTrackingFolders"></a> flowmachinegroup_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See flowmachinegroup Table [flowmachinegroup_MailboxTrackingFolders](flowmachinegroup.md#BKMK_flowmachinegroup_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_processstageparameter_MailboxTrackingFolders"></a> processstageparameter_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See processstageparameter Table [processstageparameter_MailboxTrackingFolders](processstageparameter.md#BKMK_processstageparameter_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_flowsession_MailboxTrackingFolders"></a> flowsession_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See flowsession Table [flowsession_MailboxTrackingFolders](flowsession.md#BKMK_flowsession_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_workflowbinary_MailboxTrackingFolders"></a> workflowbinary_MailboxTrackingFolders

**Added by**: Power Automate Extensions core package Solution

See workflowbinary Table [workflowbinary_MailboxTrackingFolders](workflowbinary.md#BKMK_workflowbinary_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_connectionreference_MailboxTrackingFolders"></a> connectionreference_MailboxTrackingFolders

**Added by**: Power Platform Connection References Solution

See connectionreference Table [connectionreference_MailboxTrackingFolders](connectionreference.md#BKMK_connectionreference_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aiconfiguration_MailboxTrackingFolders"></a> msdyn_aiconfiguration_MailboxTrackingFolders

**Added by**: AISolution Solution

See msdyn_aiconfiguration Table [msdyn_aiconfiguration_MailboxTrackingFolders](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aimodel_MailboxTrackingFolders"></a> msdyn_aimodel_MailboxTrackingFolders

**Added by**: AISolution Solution

See msdyn_aimodel Table [msdyn_aimodel_MailboxTrackingFolders](msdyn_aimodel.md#BKMK_msdyn_aimodel_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aitemplate_MailboxTrackingFolders"></a> msdyn_aitemplate_MailboxTrackingFolders

**Added by**: AISolution Solution

See msdyn_aitemplate Table [msdyn_aitemplate_MailboxTrackingFolders](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aifptrainingdocument_MailboxTrackingFolders"></a> msdyn_aifptrainingdocument_MailboxTrackingFolders

**Added by**: AI Solution deprecated templates Solution

See msdyn_aifptrainingdocument Table [msdyn_aifptrainingdocument_MailboxTrackingFolders](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodimage_MailboxTrackingFolders"></a> msdyn_aiodimage_MailboxTrackingFolders

**Added by**: AI Solution deprecated templates Solution

See msdyn_aiodimage Table [msdyn_aiodimage_MailboxTrackingFolders](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodlabel_MailboxTrackingFolders"></a> msdyn_aiodlabel_MailboxTrackingFolders

**Added by**: AI Solution deprecated templates Solution

See msdyn_aiodlabel Table [msdyn_aiodlabel_MailboxTrackingFolders](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingboundingbox_MailboxTrackingFolders"></a> msdyn_aiodtrainingboundingbox_MailboxTrackingFolders

**Added by**: AI Solution deprecated templates Solution

See msdyn_aiodtrainingboundingbox Table [msdyn_aiodtrainingboundingbox_MailboxTrackingFolders](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aiodtrainingimage_MailboxTrackingFolders"></a> msdyn_aiodtrainingimage_MailboxTrackingFolders

**Added by**: AI Solution deprecated templates Solution

See msdyn_aiodtrainingimage Table [msdyn_aiodtrainingimage_MailboxTrackingFolders](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdataset_MailboxTrackingFolders"></a> msdyn_aibdataset_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See msdyn_aibdataset Table [msdyn_aibdataset_MailboxTrackingFolders](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetfile_MailboxTrackingFolders"></a> msdyn_aibdatasetfile_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetfile Table [msdyn_aibdatasetfile_MailboxTrackingFolders](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetrecord_MailboxTrackingFolders"></a> msdyn_aibdatasetrecord_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetrecord Table [msdyn_aibdatasetrecord_MailboxTrackingFolders](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aibdatasetscontainer_MailboxTrackingFolders"></a> msdyn_aibdatasetscontainer_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See msdyn_aibdatasetscontainer Table [msdyn_aibdatasetscontainer_MailboxTrackingFolders](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfile_MailboxTrackingFolders"></a> msdyn_aibfile_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See msdyn_aibfile Table [msdyn_aibfile_MailboxTrackingFolders](msdyn_aibfile.md#BKMK_msdyn_aibfile_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfileattacheddata_MailboxTrackingFolders"></a> msdyn_aibfileattacheddata_MailboxTrackingFolders

**Added by**: AI Solution default templates Solution

See msdyn_aibfileattacheddata Table [msdyn_aibfileattacheddata_MailboxTrackingFolders](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_helppage_MailboxTrackingFolders"></a> msdyn_helppage_MailboxTrackingFolders

**Added by**: Contextual Help Solution

See msdyn_helppage Table [msdyn_helppage_MailboxTrackingFolders](msdyn_helppage.md#BKMK_msdyn_helppage_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_tour_MailboxTrackingFolders"></a> msdyn_tour_MailboxTrackingFolders

**Added by**: Contextual Help Solution

See msdyn_tour Table [msdyn_tour_MailboxTrackingFolders](msdyn_tour.md#BKMK_msdyn_tour_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdynce_botcontent_MailboxTrackingFolders"></a> msdynce_botcontent_MailboxTrackingFolders

**Added by**: Customer Care Intelligence Bots Solution

See msdynce_botcontent Table [msdynce_botcontent_MailboxTrackingFolders](msdynce_botcontent.md#BKMK_msdynce_botcontent_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_conversationtranscript_MailboxTrackingFolders"></a> conversationtranscript_MailboxTrackingFolders

**Added by**: Power Virtual Agents Common Solution

See conversationtranscript Table [conversationtranscript_MailboxTrackingFolders](conversationtranscript.md#BKMK_conversationtranscript_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_bot_MailboxTrackingFolders"></a> bot_MailboxTrackingFolders

**Added by**: Power Virtual Agents Solution

See bot Table [bot_MailboxTrackingFolders](bot.md#BKMK_bot_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_botcomponent_MailboxTrackingFolders"></a> botcomponent_MailboxTrackingFolders

**Added by**: Power Virtual Agents Solution

See botcomponent Table [botcomponent_MailboxTrackingFolders](botcomponent.md#BKMK_botcomponent_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_territory_MailboxTrackingFolders"></a> territory_MailboxTrackingFolders

**Added by**: Application Common Solution

See territory Table [territory_MailboxTrackingFolders](territory.md#BKMK_territory_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_activityfileattachment_MailboxTrackingFolders"></a> activityfileattachment_MailboxTrackingFolders

**Added by**: Activities Patch Solution

See activityfileattachment Table [activityfileattachment_MailboxTrackingFolders](activityfileattachment.md#BKMK_activityfileattachment_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_serviceconfiguration_MailboxTrackingFolders"></a> msdyn_serviceconfiguration_MailboxTrackingFolders

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_serviceconfiguration Table [msdyn_serviceconfiguration_MailboxTrackingFolders](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_slakpi_MailboxTrackingFolders"></a> msdyn_slakpi_MailboxTrackingFolders

**Added by**: Service Level Agreement (SLA) Extension Solution

See msdyn_slakpi Table [msdyn_slakpi_MailboxTrackingFolders](msdyn_slakpi.md#BKMK_msdyn_slakpi_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticle_MailboxTrackingFolders"></a> msdyn_federatedarticle_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticle Table [msdyn_federatedarticle_MailboxTrackingFolders](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_federatedarticleincident_MailboxTrackingFolders"></a> msdyn_federatedarticleincident_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See msdyn_federatedarticleincident Table [msdyn_federatedarticleincident_MailboxTrackingFolders](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders"></a> msdyn_kmfederatedsearchconfig_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See msdyn_kmfederatedsearchconfig Table [msdyn_kmfederatedsearchconfig_MailboxTrackingFolders](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders"></a> msdyn_knowledgearticleimage_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgearticleimage Table [msdyn_knowledgearticleimage_MailboxTrackingFolders](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders"></a> msdyn_knowledgeinteractioninsight_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgeinteractioninsight Table [msdyn_knowledgeinteractioninsight_MailboxTrackingFolders](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders"></a> msdyn_knowledgesearchinsight_MailboxTrackingFolders

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgesearchinsight Table [msdyn_knowledgesearchinsight_MailboxTrackingFolders](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_kalanguagesetting_MailboxTrackingFolders"></a> msdyn_kalanguagesetting_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See msdyn_kalanguagesetting Table [msdyn_kalanguagesetting_MailboxTrackingFolders](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_kbattachment_MailboxTrackingFolders"></a> msdyn_kbattachment_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See msdyn_kbattachment Table [msdyn_kbattachment_MailboxTrackingFolders](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_kmpersonalizationsetting_MailboxTrackingFolders"></a> msdyn_kmpersonalizationsetting_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See msdyn_kmpersonalizationsetting Table [msdyn_kmpersonalizationsetting_MailboxTrackingFolders](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders"></a> msdyn_knowledgearticletemplate_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgearticletemplate Table [msdyn_knowledgearticletemplate_MailboxTrackingFolders](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgepersonalfilter_MailboxTrackingFolders"></a> msdyn_knowledgepersonalfilter_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgepersonalfilter Table [msdyn_knowledgepersonalfilter_MailboxTrackingFolders](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgesearchfilter_MailboxTrackingFolders"></a> msdyn_knowledgesearchfilter_MailboxTrackingFolders

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgesearchfilter Table [msdyn_knowledgesearchfilter_MailboxTrackingFolders](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_pluginpackage_MailboxTrackingFolders"></a> pluginpackage_MailboxTrackingFolders

**Added by**: Plugin Infrastructure Extension Solution

See pluginpackage Table [pluginpackage_MailboxTrackingFolders](pluginpackage.md#BKMK_pluginpackage_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_keyvaultreference_MailboxTrackingFolders"></a> keyvaultreference_MailboxTrackingFolders

**Added by**: ManagedIdentityExtensions Solution

See keyvaultreference Table [keyvaultreference_MailboxTrackingFolders](keyvaultreference.md#BKMK_keyvaultreference_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_managedidentity_MailboxTrackingFolders"></a> managedidentity_MailboxTrackingFolders

**Added by**: ManagedIdentityExtensions Solution

See managedidentity Table [managedidentity_MailboxTrackingFolders](managedidentity.md#BKMK_managedidentity_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_virtualentitymetadata_MailboxTrackingFolders"></a> virtualentitymetadata_MailboxTrackingFolders

**Added by**: RuntimeIntegration Solution

See virtualentitymetadata Table [virtualentitymetadata_MailboxTrackingFolders](virtualentitymetadata.md#BKMK_virtualentitymetadata_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscription_MailboxTrackingFolders"></a> organizationdatasyncsubscription_MailboxTrackingFolders

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscription Table [organizationdatasyncsubscription_MailboxTrackingFolders](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_organizationdatasyncsubscriptionentity_MailboxTrackingFolders"></a> organizationdatasyncsubscriptionentity_MailboxTrackingFolders

**Added by**: OrganizationDataSyncSolution Solution

See organizationdatasyncsubscriptionentity Table [organizationdatasyncsubscriptionentity_MailboxTrackingFolders](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_appaction_MailboxTrackingFolders"></a> appaction_MailboxTrackingFolders

**Added by**: Power Apps Actions Solution

See appaction Table [appaction_MailboxTrackingFolders](appaction.md#BKMK_appaction_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_richtextfile_MailboxTrackingFolders"></a> msdyn_richtextfile_MailboxTrackingFolders

**Added by**: Rich Text Editor Solution

See msdyn_richtextfile Table [msdyn_richtextfile_MailboxTrackingFolders](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_pminferredtask_MailboxTrackingFolders"></a> msdyn_pminferredtask_MailboxTrackingFolders

**Added by**: Process Mining Solution

See msdyn_pminferredtask Table [msdyn_pminferredtask_MailboxTrackingFolders](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_pmrecording_MailboxTrackingFolders"></a> msdyn_pmrecording_MailboxTrackingFolders

**Added by**: Process Mining Solution

See msdyn_pmrecording Table [msdyn_pmrecording_MailboxTrackingFolders](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_analysiscomponent_MailboxTrackingFolders"></a> msdyn_analysiscomponent_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See msdyn_analysiscomponent Table [msdyn_analysiscomponent_MailboxTrackingFolders](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisjob_MailboxTrackingFolders"></a> msdyn_analysisjob_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See msdyn_analysisjob Table [msdyn_analysisjob_MailboxTrackingFolders](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresult_MailboxTrackingFolders"></a> msdyn_analysisresult_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See msdyn_analysisresult Table [msdyn_analysisresult_MailboxTrackingFolders](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_analysisresultdetail_MailboxTrackingFolders"></a> msdyn_analysisresultdetail_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See msdyn_analysisresultdetail Table [msdyn_analysisresultdetail_MailboxTrackingFolders](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders"></a> msdyn_solutionhealthrule_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthrule Table [msdyn_solutionhealthrule_MailboxTrackingFolders](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleargument_MailboxTrackingFolders"></a> msdyn_solutionhealthruleargument_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleargument Table [msdyn_solutionhealthruleargument_MailboxTrackingFolders](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_MailboxTrackingFolders) One-To-Many relationship.

### <a name="BKMK_msdyn_solutionhealthruleset_MailboxTrackingFolders"></a> msdyn_solutionhealthruleset_MailboxTrackingFolders

**Added by**: Power Apps Checker Solution

See msdyn_solutionhealthruleset Table [msdyn_solutionhealthruleset_MailboxTrackingFolders](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_MailboxTrackingFolders) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.mailboxtrackingfolder?text=mailboxtrackingfolder EntityType" />