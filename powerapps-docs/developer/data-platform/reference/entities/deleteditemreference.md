---
title: "Deleted Record Reference (DeletedItemReference) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Deleted Record Reference (DeletedItemReference) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType: 
  - developer
---

# Deleted Record Reference (DeletedItemReference) table/entity reference (Microsoft Dataverse)

Deleted Record Reference

## Messages

The following table lists the messages for the Deleted Record Reference (DeletedItemReference) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /deleteditemreferences<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /deleteditemreferences(*deleteditemreferenceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: False |`GET` /deleteditemreferences(*deleteditemreferenceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /deleteditemreferences<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /deleteditemreferences(*deleteditemreferenceid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /deleteditemreferences(*deleteditemreferenceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /deleteditemreferences(*deleteditemreferenceid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Deleted Record Reference (DeletedItemReference) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Deleted Record Reference (DeletedItemReference) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Deleted Record Reference** |
| **DisplayCollectionName** | **Deleted Record References** |
| **SchemaName** | `DeletedItemReference` |
| **CollectionSchemaName** | `DeletedItemReferences` |
| **EntitySetName** | `deleteditemreferences`|
| **LogicalName** | `deleteditemreference` |
| **LogicalCollectionName** | `deleteditemreferences` |
| **PrimaryIdAttribute** | `deleteditemreferenceid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DeletedItemReferenceId](#BKMK_DeletedItemReferenceId)
- [DeletedObject](#BKMK_DeletedObject)
- [deletedobjectIdType](#BKMK_deletedobjectIdType)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_DeletedItemReferenceId"></a> DeletedItemReferenceId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Deleted Record Reference**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`deleteditemreferenceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_DeletedObject"></a> DeletedObject

|Property|Value|
|---|---|
|Description|**Deleted Object**|
|DisplayName|**Deleted Object**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deletedobject`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|account, aciviewmapper, actioncard, actioncardusersettings, actioncarduserstate, activitymimeattachment, activityparty, activitypointer, adx_externalidentity, adx_invitation, adx_invitation_invitecontacts, adx_invitation_mspp_webrole_powerpagecomponent, adx_invitation_redeemedcontacts, adx_inviteredemption, adx_kbarticle_kbarticle, adx_portalcomment, adx_setting, adx_webformsession, agentconversationmessage, agentconversationmessagefile, agentfeeditem, agenthubgoal, agenthubinsight, agenthubmetric, agentrule, aipluginauth, aiplugingovernance, aiplugingovernanceext, aipluginusersetting, annotation, appconfigmaster, applicationfile, appmodulecomponentedge, appmodulecomponentnode, approvalstageapproval, approvalstagecondition, approvalstageintelligent, approvalstageorder, appusersetting, archivecleanupinfo, archivecleanupoperation, athenareconciliationinfo, attachment, audit, authorizationserver, azureserviceconnection, bulkarchivefailuredetail, bulkarchiveoperation, bulkarchiveoperationdetail, businessunitnewsarticle, calendarrule, canvasappextendedmetadata, cardtype, category, certificatecredential, chat, clientupdate, comment, connection, contact, conversationtranscript, customeraddress, customerrelationship, dataperformance, delegatedauthorization, delveactionhub, documentindex, documenttemplate, email, emailsearch, emailserverprofile, emailsignature, exportsolutionupload, externalparty, externalpartyitem, fax, federatedknowledgecitation, federatedknowledgemetadatarefresh, feedback, fileattachment, filtertemplate, flowcapacityassignment, flowevent, flowsession, flowsessionbinary, flowtestsession, flowtrigger, flowtriggerinstance, githubappconfig, goalrollupquery, governanceconfiguration, holidaywrapper, imagedescriptor, importdata, integrationstatus, internaladdress, interprocesslock, isvconfig, kbarticle, kbarticlecomment, knowledgearticle, knowledgearticlescategories, knowledgearticleviews, knowledgebaserecord, knowledgefaq, knowledgesourceconsumer, knowledgesourceprofile, languagelocale, languageprovisioningstate, letter, license, localconfigstore, mailbox, mailboxstatistics, mailboxtrackingcategory, makerfewshot, metadatadifference, metric, mobileofflineprofileextension, mos3management, msdynce_botcontent, msdyn_aibdataset, msdyn_aibdatasetfile, msdyn_aibdatasetrecord, msdyn_aibdatasetscontainer, msdyn_aibfeedbackloop, msdyn_aibfile, msdyn_aibfileattacheddata, msdyn_aidataprocessingevent, msdyn_aievaluationrun, msdyn_aievent, msdyn_aifptrainingdocument, msdyn_aiodimage, msdyn_aiodlabel, msdyn_aiodlabel_msdyn_aiconfiguration, msdyn_aiodtrainingboundingbox, msdyn_aiodtrainingimage, msdyn_aioptimization, msdyn_aioptimizationprivatedata, msdyn_aitestrun, msdyn_aitestrunbatch, msdyn_analysiscomponent, msdyn_analysisjob, msdyn_analysisoverride, msdyn_analysisresult, msdyn_analysisresultdetail, msdyn_bulkharvestrunlog, msdyn_connectordatasource_environmentva, msdyn_copilotinteractions, msdyn_customcontrolextendedsettings, msdyn_dataflowrefreshhistory, msdyn_dmssyncrequest, msdyn_dmssyncstatus, msdyn_entityrefreshhistory, msdyn_favoriteknowledgearticle, msdyn_federatedarticle, msdyn_federatedarticleincident, msdyn_fileupload, msdyn_flow_actionapprovalmodel, msdyn_flow_actionapprovalmodel_systemuser, msdyn_flow_actionapprovalmodel_team, msdyn_flow_approval, msdyn_flow_approvalrequest, msdyn_flow_approvalresponse, msdyn_flow_approvalstep, msdyn_flow_awaitallactionapprovalmodel, msdyn_flow_awaitallactionapprovalmodel_team, msdyn_flow_awaitallactionapprovalmodel_user, msdyn_flow_awaitallapprovalmodel, msdyn_flow_awaitallmodel_systemuser, msdyn_flow_awaitallmodel_team, msdyn_flow_basicapprovalmodel, msdyn_flow_basicapprovalmodel_systemuser, msdyn_flow_basicapprovalmodel_team, msdyn_flow_flowapproval, msdyn_harvesteligibilitycondition, msdyn_harvestworkitem, msdyn_historicalcaseharvestbatch, msdyn_historicalcaseharvestrun, msdyn_historicalcaseharvestrunlog, msdyn_integratedsearchprovider, msdyn_interimupdateknowledgearticle, msdyn_kalanguagesetting, msdyn_kbattachment, msdyn_kmfederatedsearchconfig, msdyn_kmpersonalizationsetting, msdyn_knowledgearticlecustomentity, msdyn_knowledgearticleimage, msdyn_knowledgearticletemplate, msdyn_knowledgeconfiguration, msdyn_knowledgeharvestjobrecord, msdyn_knowledgeinteractioninsight, msdyn_knowledgepersonalfilter, msdyn_knowledgesearchinsight, msdyn_msdyn_kbattachment_knowledgearticle, msdyn_powerappswrapbuild, msdyn_qna, msdyn_richtextfile, msdyn_serviceconfiguration, msdyn_solutionhealthrule, msdyn_solutionhealthruleargument, msdyn_solutionhealthruleset, msdyn_virtualtablecolumncandidate, msgraphresourcetosubscription, mspcat_catalogsubmissionfiles, mspcat_packagestore, mspp_accesscontrolrule_publishingstate, mspp_columnpermissionprofile_webrole, mspp_entitypermission_webrole, mspp_publishingstatetransitionrule_webrole, mspp_webpageaccesscontrolrule_webrole, mspp_websiteaccess_webrole, multientitysearch, multientitysearchentities, multiselectattributeoptionvalues, notification, officedocument, officegraphdocument, offlinecommanddefinition, organizationdatasyncfnostate, organizationdatasyncstate, organizationdatasyncsubscription, organizationdatasyncsubscriptionentity, organizationdatasyncsubscriptionfnotable, organizationstatistic, orginsightsmetric, orginsightsnotification, owner, package, packagehistory, package_solution, partnerapplication, pdfsetting, personaldocumenttemplate, phonecall, plannerbusinessscenario, plannersyncaction, plugintypestatistic, post, postcomment, postfollow, postlike, postregarding, postrole, powerpagecomponent_mspp_webrole_account, powerpagecomponent_mspp_webrole_contact, powerpagecomponent_webrole_systemuser, powerpagesddosalert, powerpagesitepublished, powerpagesmanagedidentity, powerpagesscanreport, powerpagesusermapping, principalobjectaccess, principalobjectattributeaccess, principalsyncattributemap, privilegecheckerlog, privilegecheckerrun, processorregistration, processstageparameter, provisionlanguageforuser, purviewlabelinfo, purviewlabelsynccache, queueitem, recommendeddocument, reconciliationentityinfo, reconciliationentitystepinfo, reconciliationinfo, recordcountsnapshot, recurrencerule, recyclebinconfig, relationshiprole, relationshiprolemap, replicationbacklog, reportlink, retentioncleanupinfo, retentioncleanupoperation, retentionfailuredetail, retentionoperation, retentionoperationdetail, retentionsuccessdetail, ribbonclientmetadata, rollupfield, rollupjob, savedorginsightsconfiguration, sa_suggestedaction, sa_suggestedactioncriteria, sdkmessageprocessingstepsecureconfig, searchattributesettings, searchcustomanalyzer, searchrelationshipsettings, sharedobject, sharedworkspace, sharedworkspacepool, sharepointdata, sharepointdocument, sharepointdocumentlocation, sideloadedaiplugin, signalregistration, socialactivity, socialinsightsconfiguration, socialprofile, sourcecontroloperationtracking, sqlencryptionaudit, stagedattributelookupvalue, stagedattributepicklistvalue, stagedentity, stagedentityattribute, stagedentityrelationship, stagedentityrelationshiprelationships, stagedentityrelationshiprole, stagedmetadataasyncoperation, stagedoptionset, stagedrelationship, stagedrelationshipextracondition, stagedviewattribute, stagesolutionupload, subject, subscriptionmanuallytrackedobject, subscriptionstatisticsoutlook, subscriptionsyncentryoutlook, subscriptionsyncinfo, suggestioncardtemplate, supportusertable, synapselinkexternaltablestate, synapselinkprofileentitystate, syncattributemapping, syncattributemappingprofile, systemapplicationmetadata, systemuserlicenses, systemusersyncmappingprofiles, task, team, teammembership, teamsyncattributemappingprofiles, territory, theme, timestampdatemapping, timezonedefinition, timezonelocalizedname, timezonerule, toolinggateway, toolinggatewaymcpserver, traceassociation, traitregistration, transactioncurrency, unresolvedaddress, untrackedemail, userapplicationmetadata, userentityinstancedata, userfiscalcalendar, usermapping, userrating, usersearchfacet, usersettings, uxagentcomponent, uxagentcomponentrevision, viewasexamplequestion, wizardaccessprivilege, wizardpage, workflowwaitsubscription|

### <a name="BKMK_deletedobjectIdType"></a> deletedobjectIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`deletedobjectidtype`|
|RequiredLevel|None|
|Type|EntityName|

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

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The Display name of the deleted record.**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Deleted On**|
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

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Regarding Object**|
|DisplayName|**RegardingObjectId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|asyncoperation|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Deleted Record Reference**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`deleteditemreference_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Deleted Record Reference**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`deleteditemreference_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [DeletedLogicalNames](#BKMK_DeletedLogicalNames)
- [DeletedLogicalNames_Name](#BKMK_DeletedLogicalNames_Name)
- [DeletedRecords](#BKMK_DeletedRecords)
- [DeletedRecords_Name](#BKMK_DeletedRecords_Name)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [ProcessedRecords](#BKMK_ProcessedRecords)
- [TotalRecords](#BKMK_TotalRecords)
- [ValidForRestore](#BKMK_ValidForRestore)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who deleted the record.**|
|DisplayName|**Deleted By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was deleted.**|
|DisplayName|**Deleted On**|
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
|Description|**Unique identifier of the delegate user who deleted the record.**|
|DisplayName|**Deleted By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_DeletedLogicalNames"></a> DeletedLogicalNames

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Deleted Logical Names**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deletedlogicalnames`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_DeletedLogicalNames_Name"></a> DeletedLogicalNames_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`deletedlogicalnames_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_DeletedRecords"></a> DeletedRecords

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Deleted Records**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deletedrecords`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_DeletedRecords_Name"></a> DeletedRecords_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`deletedrecords_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
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
|Description|**Date and time when the record was modified.**|
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
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_ProcessedRecords"></a> ProcessedRecords

|Property|Value|
|---|---|
|Description|**Number of Processed Records**|
|DisplayName|**Processed Records**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processedrecords`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_TotalRecords"></a> TotalRecords

|Property|Value|
|---|---|
|Description|**Total impacted Records**|
|DisplayName|**Total Records**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`totalrecords`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ValidForRestore"></a> ValidForRestore

|Property|Value|
|---|---|
|Description|**If true this record can be restored.**|
|DisplayName|**Valid for restore**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`validforrestore`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`_deleteditemreference_validforrestore`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
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

- [account_DeletedItemReferences](#BKMK_account_DeletedItemReferences)
- [aciviewmapper_DeletedItemReferences](#BKMK_aciviewmapper_DeletedItemReferences)
- [actioncard_DeletedItemReferences](#BKMK_actioncard_DeletedItemReferences)
- [actioncarduserstate_DeletedItemReferences](#BKMK_actioncarduserstate_DeletedItemReferences)
- [activitymimeattachment_DeletedItemReferences](#BKMK_activitymimeattachment_DeletedItemReferences)
- [activityparty_DeletedItemReferences](#BKMK_activityparty_DeletedItemReferences)
- [activitypointer_DeletedItemReferences](#BKMK_activitypointer_DeletedItemReferences)
- [adx_externalidentity_DeletedItemReferences](#BKMK_adx_externalidentity_DeletedItemReferences)
- [adx_invitation_DeletedItemReferences](#BKMK_adx_invitation_DeletedItemReferences)
- [adx_inviteredemption_DeletedItemReferences](#BKMK_adx_inviteredemption_DeletedItemReferences)
- [adx_portalcomment_DeletedItemReferences](#BKMK_adx_portalcomment_DeletedItemReferences)
- [adx_setting_DeletedItemReferences](#BKMK_adx_setting_DeletedItemReferences)
- [adx_webformsession_DeletedItemReferences](#BKMK_adx_webformsession_DeletedItemReferences)
- [agentrule_DeletedItemReferences](#BKMK_agentrule_DeletedItemReferences)
- [aipluginauth_DeletedItemReferences](#BKMK_aipluginauth_DeletedItemReferences)
- [aiplugingovernance_DeletedItemReferences](#BKMK_aiplugingovernance_DeletedItemReferences)
- [aiplugingovernanceext_DeletedItemReferences](#BKMK_aiplugingovernanceext_DeletedItemReferences)
- [aipluginusersetting_DeletedItemReferences](#BKMK_aipluginusersetting_DeletedItemReferences)
- [annotation_DeletedItemReferences](#BKMK_annotation_DeletedItemReferences)
- [appconfigmaster_DeletedItemReferences](#BKMK_appconfigmaster_DeletedItemReferences)
- [approvalstageapproval_DeletedItemReferences](#BKMK_approvalstageapproval_DeletedItemReferences)
- [approvalstagecondition_DeletedItemReferences](#BKMK_approvalstagecondition_DeletedItemReferences)
- [approvalstageintelligent_DeletedItemReferences](#BKMK_approvalstageintelligent_DeletedItemReferences)
- [approvalstageorder_DeletedItemReferences](#BKMK_approvalstageorder_DeletedItemReferences)
- [AsyncOperation_DeletedItemReference_RegardingObjectId](#BKMK_AsyncOperation_DeletedItemReference_RegardingObjectId)
- [athenareconciliationinfo_DeletedItemReferences](#BKMK_athenareconciliationinfo_DeletedItemReferences)
- [attachment_DeletedItemReferences](#BKMK_attachment_DeletedItemReferences)
- [audit_DeletedItemReferences](#BKMK_audit_DeletedItemReferences)
- [businessunitnewsarticle_DeletedItemReferences](#BKMK_businessunitnewsarticle_DeletedItemReferences)
- [calendarrule_DeletedItemReferences](#BKMK_calendarrule_DeletedItemReferences)
- [category_DeletedItemReferences](#BKMK_category_DeletedItemReferences)
- [certificatecredential_DeletedItemReferences](#BKMK_certificatecredential_DeletedItemReferences)
- [chat_DeletedItemReferences](#BKMK_chat_DeletedItemReferences)
- [connection_DeletedItemReferences](#BKMK_connection_DeletedItemReferences)
- [contact_DeletedItemReferences](#BKMK_contact_DeletedItemReferences)
- [conversationtranscript_DeletedItemReferences](#BKMK_conversationtranscript_DeletedItemReferences)
- [customeraddress_DeletedItemReferences](#BKMK_customeraddress_DeletedItemReferences)
- [dataperformance_DeletedItemReferences](#BKMK_dataperformance_DeletedItemReferences)
- [delegatedauthorization_DeletedItemReferences](#BKMK_delegatedauthorization_DeletedItemReferences)
- [documenttemplate_DeletedItemReferences](#BKMK_documenttemplate_DeletedItemReferences)
- [email_DeletedItemReferences](#BKMK_email_DeletedItemReferences)
- [emailserverprofile_DeletedItemReferences](#BKMK_emailserverprofile_DeletedItemReferences)
- [exportsolutionupload_DeletedItemReferences](#BKMK_exportsolutionupload_DeletedItemReferences)
- [fax_DeletedItemReferences](#BKMK_fax_DeletedItemReferences)
- [feedback_DeletedItemReferences](#BKMK_feedback_DeletedItemReferences)
- [FileAttachment_DeletedItemReference_DeletedLogicalNames](#BKMK_FileAttachment_DeletedItemReference_DeletedLogicalNames)
- [FileAttachment_DeletedItemReference_DeletedRecords](#BKMK_FileAttachment_DeletedItemReference_DeletedRecords)
- [fileattachment_DeletedItemReferences](#BKMK_fileattachment_DeletedItemReferences)
- [flowcapacityassignment_DeletedItemReferences](#BKMK_flowcapacityassignment_DeletedItemReferences)
- [flowevent_DeletedItemReferences](#BKMK_flowevent_DeletedItemReferences)
- [flowsession_DeletedItemReferences](#BKMK_flowsession_DeletedItemReferences)
- [flowsessionbinary_DeletedItemReferences](#BKMK_flowsessionbinary_DeletedItemReferences)
- [flowtestsession_DeletedItemReferences](#BKMK_flowtestsession_DeletedItemReferences)
- [flowtrigger_DeletedItemReferences](#BKMK_flowtrigger_DeletedItemReferences)
- [flowtriggerinstance_DeletedItemReferences](#BKMK_flowtriggerinstance_DeletedItemReferences)
- [githubappconfig_DeletedItemReferences](#BKMK_githubappconfig_DeletedItemReferences)
- [goalrollupquery_DeletedItemReferences](#BKMK_goalrollupquery_DeletedItemReferences)
- [governanceconfiguration_DeletedItemReferences](#BKMK_governanceconfiguration_DeletedItemReferences)
- [importdata_DeletedItemReferences](#BKMK_importdata_DeletedItemReferences)
- [kbarticle_DeletedItemReferences](#BKMK_kbarticle_DeletedItemReferences)
- [kbarticlecomment_DeletedItemReferences](#BKMK_kbarticlecomment_DeletedItemReferences)
- [knowledgearticle_DeletedItemReferences](#BKMK_knowledgearticle_DeletedItemReferences)
- [knowledgearticleviews_DeletedItemReferences](#BKMK_knowledgearticleviews_DeletedItemReferences)
- [knowledgebaserecord_DeletedItemReferences](#BKMK_knowledgebaserecord_DeletedItemReferences)
- [knowledgefaq_DeletedItemReferences](#BKMK_knowledgefaq_DeletedItemReferences)
- [languagelocale_DeletedItemReferences](#BKMK_languagelocale_DeletedItemReferences)
- [languageprovisioningstate_DeletedItemReferences](#BKMK_languageprovisioningstate_DeletedItemReferences)
- [letter_DeletedItemReferences](#BKMK_letter_DeletedItemReferences)
- [lk_deleteditemreference_createdby](#BKMK_lk_deleteditemreference_createdby)
- [lk_deleteditemreference_createdonbehalfby](#BKMK_lk_deleteditemreference_createdonbehalfby)
- [lk_deleteditemreference_modifiedby](#BKMK_lk_deleteditemreference_modifiedby)
- [lk_deleteditemreference_modifiedonbehalfby](#BKMK_lk_deleteditemreference_modifiedonbehalfby)
- [mailbox_DeletedItemReferences](#BKMK_mailbox_DeletedItemReferences)
- [makerfewshot_DeletedItemReferences](#BKMK_makerfewshot_DeletedItemReferences)
- [metric_DeletedItemReferences](#BKMK_metric_DeletedItemReferences)
- [mobileofflineprofileextension_DeletedItemReferences](#BKMK_mobileofflineprofileextension_DeletedItemReferences)
- [mos3management_DeletedItemReferences](#BKMK_mos3management_DeletedItemReferences)
- [msdyn_aibdataset_DeletedItemReferences](#BKMK_msdyn_aibdataset_DeletedItemReferences)
- [msdyn_aibdatasetfile_DeletedItemReferences](#BKMK_msdyn_aibdatasetfile_DeletedItemReferences)
- [msdyn_aibdatasetrecord_DeletedItemReferences](#BKMK_msdyn_aibdatasetrecord_DeletedItemReferences)
- [msdyn_aibdatasetscontainer_DeletedItemReferences](#BKMK_msdyn_aibdatasetscontainer_DeletedItemReferences)
- [msdyn_aibfeedbackloop_DeletedItemReferences](#BKMK_msdyn_aibfeedbackloop_DeletedItemReferences)
- [msdyn_aibfile_DeletedItemReferences](#BKMK_msdyn_aibfile_DeletedItemReferences)
- [msdyn_aibfileattacheddata_DeletedItemReferences](#BKMK_msdyn_aibfileattacheddata_DeletedItemReferences)
- [msdyn_aidataprocessingevent_DeletedItemReferences](#BKMK_msdyn_aidataprocessingevent_DeletedItemReferences)
- [msdyn_aievaluationrun_DeletedItemReferences](#BKMK_msdyn_aievaluationrun_DeletedItemReferences)
- [msdyn_aievent_DeletedItemReferences](#BKMK_msdyn_aievent_DeletedItemReferences)
- [msdyn_aifptrainingdocument_DeletedItemReferences](#BKMK_msdyn_aifptrainingdocument_DeletedItemReferences)
- [msdyn_aiodimage_DeletedItemReferences](#BKMK_msdyn_aiodimage_DeletedItemReferences)
- [msdyn_aiodlabel_DeletedItemReferences](#BKMK_msdyn_aiodlabel_DeletedItemReferences)
- [msdyn_aiodtrainingboundingbox_DeletedItemReferences](#BKMK_msdyn_aiodtrainingboundingbox_DeletedItemReferences)
- [msdyn_aiodtrainingimage_DeletedItemReferences](#BKMK_msdyn_aiodtrainingimage_DeletedItemReferences)
- [msdyn_aitestrun_DeletedItemReferences](#BKMK_msdyn_aitestrun_DeletedItemReferences)
- [msdyn_aitestrunbatch_DeletedItemReferences](#BKMK_msdyn_aitestrunbatch_DeletedItemReferences)
- [msdyn_analysiscomponent_DeletedItemReferences](#BKMK_msdyn_analysiscomponent_DeletedItemReferences)
- [msdyn_analysisjob_DeletedItemReferences](#BKMK_msdyn_analysisjob_DeletedItemReferences)
- [msdyn_analysisoverride_DeletedItemReferences](#BKMK_msdyn_analysisoverride_DeletedItemReferences)
- [msdyn_analysisresult_DeletedItemReferences](#BKMK_msdyn_analysisresult_DeletedItemReferences)
- [msdyn_analysisresultdetail_DeletedItemReferences](#BKMK_msdyn_analysisresultdetail_DeletedItemReferences)
- [msdyn_bulkharvestrunlog_DeletedItemReferences](#BKMK_msdyn_bulkharvestrunlog_DeletedItemReferences)
- [msdyn_copilotinteractions_DeletedItemReferences](#BKMK_msdyn_copilotinteractions_DeletedItemReferences)
- [msdyn_customcontrolextendedsettings_DeletedItemReferences](#BKMK_msdyn_customcontrolextendedsettings_DeletedItemReferences)
- [msdyn_dataflowrefreshhistory_DeletedItemReferences](#BKMK_msdyn_dataflowrefreshhistory_DeletedItemReferences)
- [msdyn_dmssyncrequest_DeletedItemReferences](#BKMK_msdyn_dmssyncrequest_DeletedItemReferences)
- [msdyn_dmssyncstatus_DeletedItemReferences](#BKMK_msdyn_dmssyncstatus_DeletedItemReferences)
- [msdyn_entityrefreshhistory_DeletedItemReferences](#BKMK_msdyn_entityrefreshhistory_DeletedItemReferences)
- [msdyn_favoriteknowledgearticle_DeletedItemReferences](#BKMK_msdyn_favoriteknowledgearticle_DeletedItemReferences)
- [msdyn_federatedarticle_DeletedItemReferences](#BKMK_msdyn_federatedarticle_DeletedItemReferences)
- [msdyn_federatedarticleincident_DeletedItemReferences](#BKMK_msdyn_federatedarticleincident_DeletedItemReferences)
- [msdyn_fileupload_DeletedItemReferences](#BKMK_msdyn_fileupload_DeletedItemReferences)
- [msdyn_flow_actionapprovalmodel_DeletedItemReferences](#BKMK_msdyn_flow_actionapprovalmodel_DeletedItemReferences)
- [msdyn_flow_approval_DeletedItemReferences](#BKMK_msdyn_flow_approval_DeletedItemReferences)
- [msdyn_flow_approvalrequest_DeletedItemReferences](#BKMK_msdyn_flow_approvalrequest_DeletedItemReferences)
- [msdyn_flow_approvalresponse_DeletedItemReferences](#BKMK_msdyn_flow_approvalresponse_DeletedItemReferences)
- [msdyn_flow_approvalstep_DeletedItemReferences](#BKMK_msdyn_flow_approvalstep_DeletedItemReferences)
- [msdyn_flow_awaitallactionapprovalmodel_DeletedItemReferences](#BKMK_msdyn_flow_awaitallactionapprovalmodel_DeletedItemReferences)
- [msdyn_flow_awaitallapprovalmodel_DeletedItemReferences](#BKMK_msdyn_flow_awaitallapprovalmodel_DeletedItemReferences)
- [msdyn_flow_basicapprovalmodel_DeletedItemReferences](#BKMK_msdyn_flow_basicapprovalmodel_DeletedItemReferences)
- [msdyn_flow_flowapproval_DeletedItemReferences](#BKMK_msdyn_flow_flowapproval_DeletedItemReferences)
- [msdyn_harvesteligibilitycondition_DeletedItemReferences](#BKMK_msdyn_harvesteligibilitycondition_DeletedItemReferences)
- [msdyn_harvestworkitem_DeletedItemReferences](#BKMK_msdyn_harvestworkitem_DeletedItemReferences)
- [msdyn_historicalcaseharvestbatch_DeletedItemReferences](#BKMK_msdyn_historicalcaseharvestbatch_DeletedItemReferences)
- [msdyn_historicalcaseharvestrun_DeletedItemReferences](#BKMK_msdyn_historicalcaseharvestrun_DeletedItemReferences)
- [msdyn_historicalcaseharvestrunlog_DeletedItemReferences](#BKMK_msdyn_historicalcaseharvestrunlog_DeletedItemReferences)
- [msdyn_integratedsearchprovider_DeletedItemReferences](#BKMK_msdyn_integratedsearchprovider_DeletedItemReferences)
- [msdyn_kalanguagesetting_DeletedItemReferences](#BKMK_msdyn_kalanguagesetting_DeletedItemReferences)
- [msdyn_kbattachment_DeletedItemReferences](#BKMK_msdyn_kbattachment_DeletedItemReferences)
- [msdyn_kmfederatedsearchconfig_DeletedItemReferences](#BKMK_msdyn_kmfederatedsearchconfig_DeletedItemReferences)
- [msdyn_kmpersonalizationsetting_DeletedItemReferences](#BKMK_msdyn_kmpersonalizationsetting_DeletedItemReferences)
- [msdyn_knowledgearticleimage_DeletedItemReferences](#BKMK_msdyn_knowledgearticleimage_DeletedItemReferences)
- [msdyn_knowledgearticletemplate_DeletedItemReferences](#BKMK_msdyn_knowledgearticletemplate_DeletedItemReferences)
- [msdyn_knowledgeconfiguration_DeletedItemReferences](#BKMK_msdyn_knowledgeconfiguration_DeletedItemReferences)
- [msdyn_knowledgeharvestjobrecord_DeletedItemReferences](#BKMK_msdyn_knowledgeharvestjobrecord_DeletedItemReferences)
- [msdyn_knowledgeinteractioninsight_DeletedItemReferences](#BKMK_msdyn_knowledgeinteractioninsight_DeletedItemReferences)
- [msdyn_knowledgepersonalfilter_DeletedItemReferences](#BKMK_msdyn_knowledgepersonalfilter_DeletedItemReferences)
- [msdyn_knowledgesearchinsight_DeletedItemReferences](#BKMK_msdyn_knowledgesearchinsight_DeletedItemReferences)
- [msdyn_powerappswrapbuild_DeletedItemReferences](#BKMK_msdyn_powerappswrapbuild_DeletedItemReferences)
- [msdyn_qna_DeletedItemReferences](#BKMK_msdyn_qna_DeletedItemReferences)
- [msdyn_richtextfile_DeletedItemReferences](#BKMK_msdyn_richtextfile_DeletedItemReferences)
- [msdyn_serviceconfiguration_DeletedItemReferences](#BKMK_msdyn_serviceconfiguration_DeletedItemReferences)
- [msdyn_solutionhealthrule_DeletedItemReferences](#BKMK_msdyn_solutionhealthrule_DeletedItemReferences)
- [msdyn_solutionhealthruleargument_DeletedItemReferences](#BKMK_msdyn_solutionhealthruleargument_DeletedItemReferences)
- [msdyn_solutionhealthruleset_DeletedItemReferences](#BKMK_msdyn_solutionhealthruleset_DeletedItemReferences)
- [msdyn_virtualtablecolumncandidate_DeletedItemReferences](#BKMK_msdyn_virtualtablecolumncandidate_DeletedItemReferences)
- [msdynce_botcontent_DeletedItemReferences](#BKMK_msdynce_botcontent_DeletedItemReferences)
- [msgraphresourcetosubscription_DeletedItemReferences](#BKMK_msgraphresourcetosubscription_DeletedItemReferences)
- [mspcat_catalogsubmissionfiles_DeletedItemReferences](#BKMK_mspcat_catalogsubmissionfiles_DeletedItemReferences)
- [mspcat_packagestore_DeletedItemReferences](#BKMK_mspcat_packagestore_DeletedItemReferences)
- [officegraphdocument_DeletedItemReferences](#BKMK_officegraphdocument_DeletedItemReferences)
- [organization_deleteditemreference](#BKMK_organization_deleteditemreference)
- [organizationdatasyncfnostate_DeletedItemReferences](#BKMK_organizationdatasyncfnostate_DeletedItemReferences)
- [organizationdatasyncstate_DeletedItemReferences](#BKMK_organizationdatasyncstate_DeletedItemReferences)
- [organizationdatasyncsubscription_DeletedItemReferences](#BKMK_organizationdatasyncsubscription_DeletedItemReferences)
- [organizationdatasyncsubscriptionentity_DeletedItemReferences](#BKMK_organizationdatasyncsubscriptionentity_DeletedItemReferences)
- [organizationdatasyncsubscriptionfnotable_DeletedItemReferences](#BKMK_organizationdatasyncsubscriptionfnotable_DeletedItemReferences)
- [owner_DeletedItemReferences](#BKMK_owner_DeletedItemReferences)
- [package_DeletedItemReferences](#BKMK_package_DeletedItemReferences)
- [packagehistory_DeletedItemReferences](#BKMK_packagehistory_DeletedItemReferences)
- [personaldocumenttemplate_DeletedItemReferences](#BKMK_personaldocumenttemplate_DeletedItemReferences)
- [phonecall_DeletedItemReferences](#BKMK_phonecall_DeletedItemReferences)
- [plannerbusinessscenario_DeletedItemReferences](#BKMK_plannerbusinessscenario_DeletedItemReferences)
- [plannersyncaction_DeletedItemReferences](#BKMK_plannersyncaction_DeletedItemReferences)
- [plugintypestatistic_DeletedItemReferences](#BKMK_plugintypestatistic_DeletedItemReferences)
- [post_DeletedItemReferences](#BKMK_post_DeletedItemReferences)
- [postcomment_DeletedItemReferences](#BKMK_postcomment_DeletedItemReferences)
- [postfollow_DeletedItemReferences](#BKMK_postfollow_DeletedItemReferences)
- [postlike_DeletedItemReferences](#BKMK_postlike_DeletedItemReferences)
- [postregarding_DeletedItemReferences](#BKMK_postregarding_DeletedItemReferences)
- [powerpagesddosalert_DeletedItemReferences](#BKMK_powerpagesddosalert_DeletedItemReferences)
- [powerpagesitepublished_DeletedItemReferences](#BKMK_powerpagesitepublished_DeletedItemReferences)
- [powerpagesmanagedidentity_DeletedItemReferences](#BKMK_powerpagesmanagedidentity_DeletedItemReferences)
- [powerpagesscanreport_DeletedItemReferences](#BKMK_powerpagesscanreport_DeletedItemReferences)
- [powerpagesusermapping_DeletedItemReferences](#BKMK_powerpagesusermapping_DeletedItemReferences)
- [principalobjectaccess_DeletedItemReferences](#BKMK_principalobjectaccess_DeletedItemReferences)
- [principalobjectattributeaccess_DeletedItemReferences](#BKMK_principalobjectattributeaccess_DeletedItemReferences)
- [privilegecheckerlog_DeletedItemReferences](#BKMK_privilegecheckerlog_DeletedItemReferences)
- [privilegecheckerrun_DeletedItemReferences](#BKMK_privilegecheckerrun_DeletedItemReferences)
- [processstageparameter_DeletedItemReferences](#BKMK_processstageparameter_DeletedItemReferences)
- [provisionlanguageforuser_DeletedItemReferences](#BKMK_provisionlanguageforuser_DeletedItemReferences)
- [purviewlabelinfo_DeletedItemReferences](#BKMK_purviewlabelinfo_DeletedItemReferences)
- [queueitem_DeletedItemReferences](#BKMK_queueitem_DeletedItemReferences)
- [recommendeddocument_DeletedItemReferences](#BKMK_recommendeddocument_DeletedItemReferences)
- [recurrencerule_DeletedItemReferences](#BKMK_recurrencerule_DeletedItemReferences)
- [RecycleBinConfig_DeletedItemReference_DeletedObject](#BKMK_RecycleBinConfig_DeletedItemReference_DeletedObject)
- [retentionfailuredetail_DeletedItemReferences](#BKMK_retentionfailuredetail_DeletedItemReferences)
- [retentionoperation_DeletedItemReferences](#BKMK_retentionoperation_DeletedItemReferences)
- [retentionoperationdetail_DeletedItemReferences](#BKMK_retentionoperationdetail_DeletedItemReferences)
- [retentionsuccessdetail_DeletedItemReferences](#BKMK_retentionsuccessdetail_DeletedItemReferences)
- [rollupfield_DeletedItemReferences](#BKMK_rollupfield_DeletedItemReferences)
- [sa_suggestedaction_DeletedItemReferences](#BKMK_sa_suggestedaction_DeletedItemReferences)
- [sa_suggestedactioncriteria_DeletedItemReferences](#BKMK_sa_suggestedactioncriteria_DeletedItemReferences)
- [sdkmessageprocessingstepsecureconfig_DeletedItemReferences](#BKMK_sdkmessageprocessingstepsecureconfig_DeletedItemReferences)
- [searchattributesettings_DeletedItemReferences](#BKMK_searchattributesettings_DeletedItemReferences)
- [searchcustomanalyzer_DeletedItemReferences](#BKMK_searchcustomanalyzer_DeletedItemReferences)
- [searchrelationshipsettings_DeletedItemReferences](#BKMK_searchrelationshipsettings_DeletedItemReferences)
- [sharedobject_DeletedItemReferences](#BKMK_sharedobject_DeletedItemReferences)
- [sharedworkspace_DeletedItemReferences](#BKMK_sharedworkspace_DeletedItemReferences)
- [sharedworkspacepool_DeletedItemReferences](#BKMK_sharedworkspacepool_DeletedItemReferences)
- [sharepointdocumentlocation_DeletedItemReferences](#BKMK_sharepointdocumentlocation_DeletedItemReferences)
- [sideloadedaiplugin_DeletedItemReferences](#BKMK_sideloadedaiplugin_DeletedItemReferences)
- [socialactivity_DeletedItemReferences](#BKMK_socialactivity_DeletedItemReferences)
- [socialprofile_DeletedItemReferences](#BKMK_socialprofile_DeletedItemReferences)
- [sourcecontroloperationtracking_DeletedItemReferences](#BKMK_sourcecontroloperationtracking_DeletedItemReferences)
- [stagedentity_DeletedItemReferences](#BKMK_stagedentity_DeletedItemReferences)
- [stagedentityattribute_DeletedItemReferences](#BKMK_stagedentityattribute_DeletedItemReferences)
- [stagedmetadataasyncoperation_DeletedItemReferences](#BKMK_stagedmetadataasyncoperation_DeletedItemReferences)
- [stagesolutionupload_DeletedItemReferences](#BKMK_stagesolutionupload_DeletedItemReferences)
- [subject_DeletedItemReferences](#BKMK_subject_DeletedItemReferences)
- [subscriptionmanuallytrackedobject_DeletedItemReferences](#BKMK_subscriptionmanuallytrackedobject_DeletedItemReferences)
- [subscriptionstatisticsoutlook_DeletedItemReferences](#BKMK_subscriptionstatisticsoutlook_DeletedItemReferences)
- [subscriptionsyncentryoutlook_DeletedItemReferences](#BKMK_subscriptionsyncentryoutlook_DeletedItemReferences)
- [supportusertable_DeletedItemReferences](#BKMK_supportusertable_DeletedItemReferences)
- [synapselinkexternaltablestate_DeletedItemReferences](#BKMK_synapselinkexternaltablestate_DeletedItemReferences)
- [synapselinkprofileentitystate_DeletedItemReferences](#BKMK_synapselinkprofileentitystate_DeletedItemReferences)
- [task_DeletedItemReferences](#BKMK_task_DeletedItemReferences)
- [team_DeletedItemReferences](#BKMK_team_DeletedItemReferences)
- [territory_DeletedItemReferences](#BKMK_territory_DeletedItemReferences)
- [theme_DeletedItemReferences](#BKMK_theme_DeletedItemReferences)
- [timestampdatemapping_DeletedItemReferences](#BKMK_timestampdatemapping_DeletedItemReferences)
- [timezonedefinition_DeletedItemReferences](#BKMK_timezonedefinition_DeletedItemReferences)
- [timezonelocalizedname_DeletedItemReferences](#BKMK_timezonelocalizedname_DeletedItemReferences)
- [timezonerule_DeletedItemReferences](#BKMK_timezonerule_DeletedItemReferences)
- [transactioncurrency_DeletedItemReferences](#BKMK_transactioncurrency_DeletedItemReferences)
- [usermapping_DeletedItemReferences](#BKMK_usermapping_DeletedItemReferences)
- [userrating_DeletedItemReferences](#BKMK_userrating_DeletedItemReferences)
- [usersettings_DeletedItemReferences](#BKMK_usersettings_DeletedItemReferences)
- [viewasexamplequestion_DeletedItemReferences](#BKMK_viewasexamplequestion_DeletedItemReferences)

### <a name="BKMK_account_DeletedItemReferences"></a> account_DeletedItemReferences

One-To-Many Relationship: [account account_DeletedItemReferences](account.md#BKMK_account_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aciviewmapper_DeletedItemReferences"></a> aciviewmapper_DeletedItemReferences

One-To-Many Relationship: [aciviewmapper aciviewmapper_DeletedItemReferences](aciviewmapper.md#BKMK_aciviewmapper_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`aciviewmapper`|
|ReferencedAttribute|`aciviewmapperid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_aciviewmapper`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_actioncard_DeletedItemReferences"></a> actioncard_DeletedItemReferences

One-To-Many Relationship: [actioncard actioncard_DeletedItemReferences](actioncard.md#BKMK_actioncard_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`actioncard`|
|ReferencedAttribute|`actioncardid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_actioncard`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_actioncarduserstate_DeletedItemReferences"></a> actioncarduserstate_DeletedItemReferences

One-To-Many Relationship: [actioncarduserstate actioncarduserstate_DeletedItemReferences](actioncarduserstate.md#BKMK_actioncarduserstate_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`actioncarduserstate`|
|ReferencedAttribute|`actioncarduserstateid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_actioncarduserstate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activitymimeattachment_DeletedItemReferences"></a> activitymimeattachment_DeletedItemReferences

One-To-Many Relationship: [activitymimeattachment activitymimeattachment_DeletedItemReferences](activitymimeattachment.md#BKMK_activitymimeattachment_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`activitymimeattachment`|
|ReferencedAttribute|`activitymimeattachmentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_activitymimeattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activityparty_DeletedItemReferences"></a> activityparty_DeletedItemReferences

One-To-Many Relationship: [activityparty activityparty_DeletedItemReferences](activityparty.md#BKMK_activityparty_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`activityparty`|
|ReferencedAttribute|`activitypartyid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_activityparty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activitypointer_DeletedItemReferences"></a> activitypointer_DeletedItemReferences

One-To-Many Relationship: [activitypointer activitypointer_DeletedItemReferences](activitypointer.md#BKMK_activitypointer_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_externalidentity_DeletedItemReferences"></a> adx_externalidentity_DeletedItemReferences

One-To-Many Relationship: [adx_externalidentity adx_externalidentity_DeletedItemReferences](adx_externalidentity.md#BKMK_adx_externalidentity_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_externalidentity`|
|ReferencedAttribute|`adx_externalidentityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_adx_externalidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_DeletedItemReferences"></a> adx_invitation_DeletedItemReferences

One-To-Many Relationship: [adx_invitation adx_invitation_DeletedItemReferences](adx_invitation.md#BKMK_adx_invitation_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_adx_invitation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_DeletedItemReferences"></a> adx_inviteredemption_DeletedItemReferences

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_DeletedItemReferences](adx_inviteredemption.md#BKMK_adx_inviteredemption_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_portalcomment_DeletedItemReferences"></a> adx_portalcomment_DeletedItemReferences

One-To-Many Relationship: [adx_portalcomment adx_portalcomment_DeletedItemReferences](adx_portalcomment.md#BKMK_adx_portalcomment_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_portalcomment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_adx_portalcomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_setting_DeletedItemReferences"></a> adx_setting_DeletedItemReferences

One-To-Many Relationship: [adx_setting adx_setting_DeletedItemReferences](adx_setting.md#BKMK_adx_setting_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_setting`|
|ReferencedAttribute|`adx_settingid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_adx_setting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_webformsession_DeletedItemReferences"></a> adx_webformsession_DeletedItemReferences

One-To-Many Relationship: [adx_webformsession adx_webformsession_DeletedItemReferences](adx_webformsession.md#BKMK_adx_webformsession_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_webformsession`|
|ReferencedAttribute|`adx_webformsessionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_adx_webformsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_agentrule_DeletedItemReferences"></a> agentrule_DeletedItemReferences

One-To-Many Relationship: [agentrule agentrule_DeletedItemReferences](agentrule.md#BKMK_agentrule_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`agentrule`|
|ReferencedAttribute|`agentruleid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_agentrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginauth_DeletedItemReferences"></a> aipluginauth_DeletedItemReferences

One-To-Many Relationship: [aipluginauth aipluginauth_DeletedItemReferences](aipluginauth.md#BKMK_aipluginauth_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginauth`|
|ReferencedAttribute|`aipluginauthid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_aipluginauth`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernance_DeletedItemReferences"></a> aiplugingovernance_DeletedItemReferences

One-To-Many Relationship: [aiplugingovernance aiplugingovernance_DeletedItemReferences](aiplugingovernance.md#BKMK_aiplugingovernance_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernance`|
|ReferencedAttribute|`aiplugingovernanceid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_aiplugingovernance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernanceext_DeletedItemReferences"></a> aiplugingovernanceext_DeletedItemReferences

One-To-Many Relationship: [aiplugingovernanceext aiplugingovernanceext_DeletedItemReferences](aiplugingovernanceext.md#BKMK_aiplugingovernanceext_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernanceext`|
|ReferencedAttribute|`aiplugingovernanceextid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_aiplugingovernanceext`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginusersetting_DeletedItemReferences"></a> aipluginusersetting_DeletedItemReferences

One-To-Many Relationship: [aipluginusersetting aipluginusersetting_DeletedItemReferences](aipluginusersetting.md#BKMK_aipluginusersetting_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginusersetting`|
|ReferencedAttribute|`aipluginusersettingid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_aipluginusersetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_annotation_DeletedItemReferences"></a> annotation_DeletedItemReferences

One-To-Many Relationship: [annotation annotation_DeletedItemReferences](annotation.md#BKMK_annotation_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`annotation`|
|ReferencedAttribute|`annotationid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_annotation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appconfigmaster_DeletedItemReferences"></a> appconfigmaster_DeletedItemReferences

One-To-Many Relationship: [appconfigmaster appconfigmaster_DeletedItemReferences](appconfigmaster.md#BKMK_appconfigmaster_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`appconfigmaster`|
|ReferencedAttribute|`appconfigmasterid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_appconfigmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageapproval_DeletedItemReferences"></a> approvalstageapproval_DeletedItemReferences

One-To-Many Relationship: [approvalstageapproval approvalstageapproval_DeletedItemReferences](approvalstageapproval.md#BKMK_approvalstageapproval_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageapproval`|
|ReferencedAttribute|`approvalstageapprovalid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_approvalstageapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstagecondition_DeletedItemReferences"></a> approvalstagecondition_DeletedItemReferences

One-To-Many Relationship: [approvalstagecondition approvalstagecondition_DeletedItemReferences](approvalstagecondition.md#BKMK_approvalstagecondition_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstagecondition`|
|ReferencedAttribute|`approvalstageconditionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_approvalstagecondition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageintelligent_DeletedItemReferences"></a> approvalstageintelligent_DeletedItemReferences

One-To-Many Relationship: [approvalstageintelligent approvalstageintelligent_DeletedItemReferences](approvalstageintelligent.md#BKMK_approvalstageintelligent_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageintelligent`|
|ReferencedAttribute|`approvalstageintelligentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_approvalstageintelligent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_DeletedItemReferences"></a> approvalstageorder_DeletedItemReferences

One-To-Many Relationship: [approvalstageorder approvalstageorder_DeletedItemReferences](approvalstageorder.md#BKMK_approvalstageorder_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageorder`|
|ReferencedAttribute|`approvalstageorderid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_approvalstageorder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_AsyncOperation_DeletedItemReference_RegardingObjectId"></a> AsyncOperation_DeletedItemReference_RegardingObjectId

One-To-Many Relationship: [asyncoperation AsyncOperation_DeletedItemReference_RegardingObjectId](asyncoperation.md#BKMK_AsyncOperation_DeletedItemReference_RegardingObjectId)

|Property|Value|
|---|---|
|ReferencedEntity|`asyncoperation`|
|ReferencedAttribute|`asyncoperationid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`RegardingObjectId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_athenareconciliationinfo_DeletedItemReferences"></a> athenareconciliationinfo_DeletedItemReferences

One-To-Many Relationship: [athenareconciliationinfo athenareconciliationinfo_DeletedItemReferences](athenareconciliationinfo.md#BKMK_athenareconciliationinfo_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`athenareconciliationinfo`|
|ReferencedAttribute|`athenareconciliationinfoid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_athenareconciliationinfo`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attachment_DeletedItemReferences"></a> attachment_DeletedItemReferences

One-To-Many Relationship: [attachment attachment_DeletedItemReferences](attachment.md#BKMK_attachment_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`attachment`|
|ReferencedAttribute|`attachmentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_attachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_audit_DeletedItemReferences"></a> audit_DeletedItemReferences

One-To-Many Relationship: [audit audit_DeletedItemReferences](audit.md#BKMK_audit_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`audit`|
|ReferencedAttribute|`auditid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_audit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_businessunitnewsarticle_DeletedItemReferences"></a> businessunitnewsarticle_DeletedItemReferences

One-To-Many Relationship: [businessunitnewsarticle businessunitnewsarticle_DeletedItemReferences](businessunitnewsarticle.md#BKMK_businessunitnewsarticle_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunitnewsarticle`|
|ReferencedAttribute|`businessunitnewsarticleid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_businessunitnewsarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_calendarrule_DeletedItemReferences"></a> calendarrule_DeletedItemReferences

One-To-Many Relationship: [calendarrule calendarrule_DeletedItemReferences](calendarrule.md#BKMK_calendarrule_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`calendarrule`|
|ReferencedAttribute|`calendarruleid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_calendarrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_category_DeletedItemReferences"></a> category_DeletedItemReferences

One-To-Many Relationship: [category category_DeletedItemReferences](category.md#BKMK_category_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`category`|
|ReferencedAttribute|`categoryid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_category`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_certificatecredential_DeletedItemReferences"></a> certificatecredential_DeletedItemReferences

One-To-Many Relationship: [certificatecredential certificatecredential_DeletedItemReferences](certificatecredential.md#BKMK_certificatecredential_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`certificatecredential`|
|ReferencedAttribute|`certificatecredentialid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_certificatecredential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_chat_DeletedItemReferences"></a> chat_DeletedItemReferences

One-To-Many Relationship: [chat chat_DeletedItemReferences](chat.md#BKMK_chat_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`chat`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_chat`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connection_DeletedItemReferences"></a> connection_DeletedItemReferences

One-To-Many Relationship: [connection connection_DeletedItemReferences](connection.md#BKMK_connection_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`connection`|
|ReferencedAttribute|`connectionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_connection`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_contact_DeletedItemReferences"></a> contact_DeletedItemReferences

One-To-Many Relationship: [contact contact_DeletedItemReferences](contact.md#BKMK_contact_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_conversationtranscript_DeletedItemReferences"></a> conversationtranscript_DeletedItemReferences

One-To-Many Relationship: [conversationtranscript conversationtranscript_DeletedItemReferences](conversationtranscript.md#BKMK_conversationtranscript_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`conversationtranscript`|
|ReferencedAttribute|`conversationtranscriptid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_conversationtranscript`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customeraddress_DeletedItemReferences"></a> customeraddress_DeletedItemReferences

One-To-Many Relationship: [customeraddress customeraddress_DeletedItemReferences](customeraddress.md#BKMK_customeraddress_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`customeraddress`|
|ReferencedAttribute|`customeraddressid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_customeraddress`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dataperformance_DeletedItemReferences"></a> dataperformance_DeletedItemReferences

One-To-Many Relationship: [dataperformance dataperformance_DeletedItemReferences](dataperformance.md#BKMK_dataperformance_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`dataperformance`|
|ReferencedAttribute|`dataperformanceid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_dataperformance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_delegatedauthorization_DeletedItemReferences"></a> delegatedauthorization_DeletedItemReferences

One-To-Many Relationship: [delegatedauthorization delegatedauthorization_DeletedItemReferences](delegatedauthorization.md#BKMK_delegatedauthorization_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`delegatedauthorization`|
|ReferencedAttribute|`delegatedauthorizationid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_delegatedauthorization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_documenttemplate_DeletedItemReferences"></a> documenttemplate_DeletedItemReferences

One-To-Many Relationship: [documenttemplate documenttemplate_DeletedItemReferences](documenttemplate.md#BKMK_documenttemplate_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`documenttemplate`|
|ReferencedAttribute|`documenttemplateid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_documenttemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_DeletedItemReferences"></a> email_DeletedItemReferences

One-To-Many Relationship: [email email_DeletedItemReferences](email.md#BKMK_email_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_emailserverprofile_DeletedItemReferences"></a> emailserverprofile_DeletedItemReferences

One-To-Many Relationship: [emailserverprofile emailserverprofile_DeletedItemReferences](emailserverprofile.md#BKMK_emailserverprofile_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`emailserverprofile`|
|ReferencedAttribute|`emailserverprofileid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_emailserverprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportsolutionupload_DeletedItemReferences"></a> exportsolutionupload_DeletedItemReferences

One-To-Many Relationship: [exportsolutionupload exportsolutionupload_DeletedItemReferences](exportsolutionupload.md#BKMK_exportsolutionupload_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`exportsolutionupload`|
|ReferencedAttribute|`exportsolutionuploadid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_exportsolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fax_DeletedItemReferences"></a> fax_DeletedItemReferences

One-To-Many Relationship: [fax fax_DeletedItemReferences](fax.md#BKMK_fax_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_fax`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_feedback_DeletedItemReferences"></a> feedback_DeletedItemReferences

One-To-Many Relationship: [feedback feedback_DeletedItemReferences](feedback.md#BKMK_feedback_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`feedback`|
|ReferencedAttribute|`feedbackid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_feedback`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_DeletedItemReference_DeletedLogicalNames"></a> FileAttachment_DeletedItemReference_DeletedLogicalNames

One-To-Many Relationship: [fileattachment FileAttachment_DeletedItemReference_DeletedLogicalNames](fileattachment.md#BKMK_FileAttachment_DeletedItemReference_DeletedLogicalNames)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`deletedlogicalnames`|
|ReferencingEntityNavigationPropertyName|`DeletedLogicalNames`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_DeletedItemReference_DeletedRecords"></a> FileAttachment_DeletedItemReference_DeletedRecords

One-To-Many Relationship: [fileattachment FileAttachment_DeletedItemReference_DeletedRecords](fileattachment.md#BKMK_FileAttachment_DeletedItemReference_DeletedRecords)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`deletedrecords`|
|ReferencingEntityNavigationPropertyName|`DeletedRecords`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fileattachment_DeletedItemReferences"></a> fileattachment_DeletedItemReferences

One-To-Many Relationship: [fileattachment fileattachment_DeletedItemReferences](fileattachment.md#BKMK_fileattachment_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_fileattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcapacityassignment_DeletedItemReferences"></a> flowcapacityassignment_DeletedItemReferences

One-To-Many Relationship: [flowcapacityassignment flowcapacityassignment_DeletedItemReferences](flowcapacityassignment.md#BKMK_flowcapacityassignment_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcapacityassignment`|
|ReferencedAttribute|`flowcapacityassignmentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_flowcapacityassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowevent_DeletedItemReferences"></a> flowevent_DeletedItemReferences

One-To-Many Relationship: [flowevent flowevent_DeletedItemReferences](flowevent.md#BKMK_flowevent_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`flowevent`|
|ReferencedAttribute|`floweventid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_flowevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsession_DeletedItemReferences"></a> flowsession_DeletedItemReferences

One-To-Many Relationship: [flowsession flowsession_DeletedItemReferences](flowsession.md#BKMK_flowsession_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsession`|
|ReferencedAttribute|`flowsessionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_flowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsessionbinary_DeletedItemReferences"></a> flowsessionbinary_DeletedItemReferences

One-To-Many Relationship: [flowsessionbinary flowsessionbinary_DeletedItemReferences](flowsessionbinary.md#BKMK_flowsessionbinary_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsessionbinary`|
|ReferencedAttribute|`flowsessionbinaryid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_flowsessionbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowtestsession_DeletedItemReferences"></a> flowtestsession_DeletedItemReferences

One-To-Many Relationship: [flowtestsession flowtestsession_DeletedItemReferences](flowtestsession.md#BKMK_flowtestsession_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`flowtestsession`|
|ReferencedAttribute|`flowtestsessionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_flowtestsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowtrigger_DeletedItemReferences"></a> flowtrigger_DeletedItemReferences

One-To-Many Relationship: [flowtrigger flowtrigger_DeletedItemReferences](flowtrigger.md#BKMK_flowtrigger_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`flowtrigger`|
|ReferencedAttribute|`flowtriggerid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_flowtrigger`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowtriggerinstance_DeletedItemReferences"></a> flowtriggerinstance_DeletedItemReferences

One-To-Many Relationship: [flowtriggerinstance flowtriggerinstance_DeletedItemReferences](flowtriggerinstance.md#BKMK_flowtriggerinstance_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`flowtriggerinstance`|
|ReferencedAttribute|`flowtriggerinstanceid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_flowtriggerinstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_githubappconfig_DeletedItemReferences"></a> githubappconfig_DeletedItemReferences

One-To-Many Relationship: [githubappconfig githubappconfig_DeletedItemReferences](githubappconfig.md#BKMK_githubappconfig_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`githubappconfig`|
|ReferencedAttribute|`githubappconfigid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_githubappconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goalrollupquery_DeletedItemReferences"></a> goalrollupquery_DeletedItemReferences

One-To-Many Relationship: [goalrollupquery goalrollupquery_DeletedItemReferences](goalrollupquery.md#BKMK_goalrollupquery_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`goalrollupquery`|
|ReferencedAttribute|`goalrollupqueryid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_goalrollupquery`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_governanceconfiguration_DeletedItemReferences"></a> governanceconfiguration_DeletedItemReferences

One-To-Many Relationship: [governanceconfiguration governanceconfiguration_DeletedItemReferences](governanceconfiguration.md#BKMK_governanceconfiguration_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`governanceconfiguration`|
|ReferencedAttribute|`governanceconfigurationid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_governanceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_importdata_DeletedItemReferences"></a> importdata_DeletedItemReferences

One-To-Many Relationship: [importdata importdata_DeletedItemReferences](importdata.md#BKMK_importdata_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`importdata`|
|ReferencedAttribute|`importdataid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_importdata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_kbarticle_DeletedItemReferences"></a> kbarticle_DeletedItemReferences

One-To-Many Relationship: [kbarticle kbarticle_DeletedItemReferences](kbarticle.md#BKMK_kbarticle_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticle`|
|ReferencedAttribute|`kbarticleid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_kbarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_kbarticlecomment_DeletedItemReferences"></a> kbarticlecomment_DeletedItemReferences

One-To-Many Relationship: [kbarticlecomment kbarticlecomment_DeletedItemReferences](kbarticlecomment.md#BKMK_kbarticlecomment_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticlecomment`|
|ReferencedAttribute|`kbarticlecommentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_kbarticlecomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_DeletedItemReferences"></a> knowledgearticle_DeletedItemReferences

One-To-Many Relationship: [knowledgearticle knowledgearticle_DeletedItemReferences](knowledgearticle.md#BKMK_knowledgearticle_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticleviews_DeletedItemReferences"></a> knowledgearticleviews_DeletedItemReferences

One-To-Many Relationship: [knowledgearticleviews knowledgearticleviews_DeletedItemReferences](knowledgearticleviews.md#BKMK_knowledgearticleviews_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticleviews`|
|ReferencedAttribute|`knowledgearticleviewsid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_knowledgearticleviews`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgebaserecord_DeletedItemReferences"></a> knowledgebaserecord_DeletedItemReferences

One-To-Many Relationship: [knowledgebaserecord knowledgebaserecord_DeletedItemReferences](knowledgebaserecord.md#BKMK_knowledgebaserecord_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_knowledgebaserecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgefaq_DeletedItemReferences"></a> knowledgefaq_DeletedItemReferences

One-To-Many Relationship: [knowledgefaq knowledgefaq_DeletedItemReferences](knowledgefaq.md#BKMK_knowledgefaq_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgefaq`|
|ReferencedAttribute|`knowledgefaqid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_knowledgefaq`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_languagelocale_DeletedItemReferences"></a> languagelocale_DeletedItemReferences

One-To-Many Relationship: [languagelocale languagelocale_DeletedItemReferences](languagelocale.md#BKMK_languagelocale_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`languagelocale`|
|ReferencedAttribute|`languagelocaleid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_languagelocale`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_languageprovisioningstate_DeletedItemReferences"></a> languageprovisioningstate_DeletedItemReferences

One-To-Many Relationship: [languageprovisioningstate languageprovisioningstate_DeletedItemReferences](languageprovisioningstate.md#BKMK_languageprovisioningstate_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`languageprovisioningstate`|
|ReferencedAttribute|`languageprovisioningstateid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_languageprovisioningstate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_letter_DeletedItemReferences"></a> letter_DeletedItemReferences

One-To-Many Relationship: [letter letter_DeletedItemReferences](letter.md#BKMK_letter_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_letter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_deleteditemreference_createdby"></a> lk_deleteditemreference_createdby

One-To-Many Relationship: [systemuser lk_deleteditemreference_createdby](systemuser.md#BKMK_lk_deleteditemreference_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_deleteditemreference_createdonbehalfby"></a> lk_deleteditemreference_createdonbehalfby

One-To-Many Relationship: [systemuser lk_deleteditemreference_createdonbehalfby](systemuser.md#BKMK_lk_deleteditemreference_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_deleteditemreference_modifiedby"></a> lk_deleteditemreference_modifiedby

One-To-Many Relationship: [systemuser lk_deleteditemreference_modifiedby](systemuser.md#BKMK_lk_deleteditemreference_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_deleteditemreference_modifiedonbehalfby"></a> lk_deleteditemreference_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_deleteditemreference_modifiedonbehalfby](systemuser.md#BKMK_lk_deleteditemreference_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mailbox_DeletedItemReferences"></a> mailbox_DeletedItemReferences

One-To-Many Relationship: [mailbox mailbox_DeletedItemReferences](mailbox.md#BKMK_mailbox_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`mailbox`|
|ReferencedAttribute|`mailboxid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_mailbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_makerfewshot_DeletedItemReferences"></a> makerfewshot_DeletedItemReferences

One-To-Many Relationship: [makerfewshot makerfewshot_DeletedItemReferences](makerfewshot.md#BKMK_makerfewshot_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`makerfewshot`|
|ReferencedAttribute|`makerfewshotid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_makerfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_metric_DeletedItemReferences"></a> metric_DeletedItemReferences

One-To-Many Relationship: [metric metric_DeletedItemReferences](metric.md#BKMK_metric_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`metric`|
|ReferencedAttribute|`metricid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_metric`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mobileofflineprofileextension_DeletedItemReferences"></a> mobileofflineprofileextension_DeletedItemReferences

One-To-Many Relationship: [mobileofflineprofileextension mobileofflineprofileextension_DeletedItemReferences](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofileextension`|
|ReferencedAttribute|`mobileofflineprofileextensionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_mobileofflineprofileextension`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mos3management_DeletedItemReferences"></a> mos3management_DeletedItemReferences

One-To-Many Relationship: [mos3management mos3management_DeletedItemReferences](mos3management.md#BKMK_mos3management_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`mos3management`|
|ReferencedAttribute|`mos3managementid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_mos3management`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdataset_DeletedItemReferences"></a> msdyn_aibdataset_DeletedItemReferences

One-To-Many Relationship: [msdyn_aibdataset msdyn_aibdataset_DeletedItemReferences](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdataset`|
|ReferencedAttribute|`msdyn_aibdatasetid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aibdataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetfile_DeletedItemReferences"></a> msdyn_aibdatasetfile_DeletedItemReferences

One-To-Many Relationship: [msdyn_aibdatasetfile msdyn_aibdatasetfile_DeletedItemReferences](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetfile`|
|ReferencedAttribute|`msdyn_aibdatasetfileid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aibdatasetfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetrecord_DeletedItemReferences"></a> msdyn_aibdatasetrecord_DeletedItemReferences

One-To-Many Relationship: [msdyn_aibdatasetrecord msdyn_aibdatasetrecord_DeletedItemReferences](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetrecord`|
|ReferencedAttribute|`msdyn_aibdatasetrecordid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aibdatasetrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetscontainer_DeletedItemReferences"></a> msdyn_aibdatasetscontainer_DeletedItemReferences

One-To-Many Relationship: [msdyn_aibdatasetscontainer msdyn_aibdatasetscontainer_DeletedItemReferences](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetscontainer`|
|ReferencedAttribute|`msdyn_aibdatasetscontainerid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aibdatasetscontainer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfeedbackloop_DeletedItemReferences"></a> msdyn_aibfeedbackloop_DeletedItemReferences

One-To-Many Relationship: [msdyn_aibfeedbackloop msdyn_aibfeedbackloop_DeletedItemReferences](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfeedbackloop`|
|ReferencedAttribute|`msdyn_aibfeedbackloopid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aibfeedbackloop`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfile_DeletedItemReferences"></a> msdyn_aibfile_DeletedItemReferences

One-To-Many Relationship: [msdyn_aibfile msdyn_aibfile_DeletedItemReferences](msdyn_aibfile.md#BKMK_msdyn_aibfile_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfile`|
|ReferencedAttribute|`msdyn_aibfileid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aibfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfileattacheddata_DeletedItemReferences"></a> msdyn_aibfileattacheddata_DeletedItemReferences

One-To-Many Relationship: [msdyn_aibfileattacheddata msdyn_aibfileattacheddata_DeletedItemReferences](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfileattacheddata`|
|ReferencedAttribute|`msdyn_aibfileattacheddataid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aibfileattacheddata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aidataprocessingevent_DeletedItemReferences"></a> msdyn_aidataprocessingevent_DeletedItemReferences

One-To-Many Relationship: [msdyn_aidataprocessingevent msdyn_aidataprocessingevent_DeletedItemReferences](msdyn_aidataprocessingevent.md#BKMK_msdyn_aidataprocessingevent_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aidataprocessingevent`|
|ReferencedAttribute|`msdyn_aidataprocessingeventid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aidataprocessingevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationrun_DeletedItemReferences"></a> msdyn_aievaluationrun_DeletedItemReferences

One-To-Many Relationship: [msdyn_aievaluationrun msdyn_aievaluationrun_DeletedItemReferences](msdyn_aievaluationrun.md#BKMK_msdyn_aievaluationrun_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationrun`|
|ReferencedAttribute|`msdyn_aievaluationrunid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aievaluationrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievent_DeletedItemReferences"></a> msdyn_aievent_DeletedItemReferences

One-To-Many Relationship: [msdyn_aievent msdyn_aievent_DeletedItemReferences](msdyn_aievent.md#BKMK_msdyn_aievent_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievent`|
|ReferencedAttribute|`msdyn_aieventid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aievent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aifptrainingdocument_DeletedItemReferences"></a> msdyn_aifptrainingdocument_DeletedItemReferences

One-To-Many Relationship: [msdyn_aifptrainingdocument msdyn_aifptrainingdocument_DeletedItemReferences](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aifptrainingdocument`|
|ReferencedAttribute|`msdyn_aifptrainingdocumentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aifptrainingdocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodimage_DeletedItemReferences"></a> msdyn_aiodimage_DeletedItemReferences

One-To-Many Relationship: [msdyn_aiodimage msdyn_aiodimage_DeletedItemReferences](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodimage`|
|ReferencedAttribute|`msdyn_aiodimageid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aiodimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodlabel_DeletedItemReferences"></a> msdyn_aiodlabel_DeletedItemReferences

One-To-Many Relationship: [msdyn_aiodlabel msdyn_aiodlabel_DeletedItemReferences](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodlabel`|
|ReferencedAttribute|`msdyn_aiodlabelid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aiodlabel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingboundingbox_DeletedItemReferences"></a> msdyn_aiodtrainingboundingbox_DeletedItemReferences

One-To-Many Relationship: [msdyn_aiodtrainingboundingbox msdyn_aiodtrainingboundingbox_DeletedItemReferences](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencedAttribute|`msdyn_aiodtrainingboundingboxid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aiodtrainingboundingbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingimage_DeletedItemReferences"></a> msdyn_aiodtrainingimage_DeletedItemReferences

One-To-Many Relationship: [msdyn_aiodtrainingimage msdyn_aiodtrainingimage_DeletedItemReferences](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingimage`|
|ReferencedAttribute|`msdyn_aiodtrainingimageid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aiodtrainingimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrun_DeletedItemReferences"></a> msdyn_aitestrun_DeletedItemReferences

One-To-Many Relationship: [msdyn_aitestrun msdyn_aitestrun_DeletedItemReferences](msdyn_aitestrun.md#BKMK_msdyn_aitestrun_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrun`|
|ReferencedAttribute|`msdyn_aitestrunid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aitestrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrunbatch_DeletedItemReferences"></a> msdyn_aitestrunbatch_DeletedItemReferences

One-To-Many Relationship: [msdyn_aitestrunbatch msdyn_aitestrunbatch_DeletedItemReferences](msdyn_aitestrunbatch.md#BKMK_msdyn_aitestrunbatch_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrunbatch`|
|ReferencedAttribute|`msdyn_aitestrunbatchid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_aitestrunbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysiscomponent_DeletedItemReferences"></a> msdyn_analysiscomponent_DeletedItemReferences

One-To-Many Relationship: [msdyn_analysiscomponent msdyn_analysiscomponent_DeletedItemReferences](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysiscomponent`|
|ReferencedAttribute|`msdyn_analysiscomponentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_analysiscomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_DeletedItemReferences"></a> msdyn_analysisjob_DeletedItemReferences

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_DeletedItemReferences](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_analysisjob`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisoverride_DeletedItemReferences"></a> msdyn_analysisoverride_DeletedItemReferences

One-To-Many Relationship: [msdyn_analysisoverride msdyn_analysisoverride_DeletedItemReferences](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisoverride`|
|ReferencedAttribute|`msdyn_analysisoverrideid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_analysisoverride`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresult_DeletedItemReferences"></a> msdyn_analysisresult_DeletedItemReferences

One-To-Many Relationship: [msdyn_analysisresult msdyn_analysisresult_DeletedItemReferences](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresult`|
|ReferencedAttribute|`msdyn_analysisresultid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_analysisresult`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresultdetail_DeletedItemReferences"></a> msdyn_analysisresultdetail_DeletedItemReferences

One-To-Many Relationship: [msdyn_analysisresultdetail msdyn_analysisresultdetail_DeletedItemReferences](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresultdetail`|
|ReferencedAttribute|`msdyn_analysisresultdetailid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_analysisresultdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_bulkharvestrunlog_DeletedItemReferences"></a> msdyn_bulkharvestrunlog_DeletedItemReferences

One-To-Many Relationship: [msdyn_bulkharvestrunlog msdyn_bulkharvestrunlog_DeletedItemReferences](msdyn_bulkharvestrunlog.md#BKMK_msdyn_bulkharvestrunlog_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_bulkharvestrunlog`|
|ReferencedAttribute|`msdyn_bulkharvestrunlogid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_bulkharvestrunlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_copilotinteractions_DeletedItemReferences"></a> msdyn_copilotinteractions_DeletedItemReferences

One-To-Many Relationship: [msdyn_copilotinteractions msdyn_copilotinteractions_DeletedItemReferences](msdyn_copilotinteractions.md#BKMK_msdyn_copilotinteractions_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_copilotinteractions`|
|ReferencedAttribute|`msdyn_copilotinteractionsid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_copilotinteractions`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_DeletedItemReferences"></a> msdyn_customcontrolextendedsettings_DeletedItemReferences

One-To-Many Relationship: [msdyn_customcontrolextendedsettings msdyn_customcontrolextendedsettings_DeletedItemReferences](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_customcontrolextendedsettings`|
|ReferencedAttribute|`msdyn_customcontrolextendedsettingsid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_customcontrolextendedsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowrefreshhistory_DeletedItemReferences"></a> msdyn_dataflowrefreshhistory_DeletedItemReferences

One-To-Many Relationship: [msdyn_dataflowrefreshhistory msdyn_dataflowrefreshhistory_DeletedItemReferences](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowrefreshhistory`|
|ReferencedAttribute|`msdyn_dataflowrefreshhistoryid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_dataflowrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncrequest_DeletedItemReferences"></a> msdyn_dmssyncrequest_DeletedItemReferences

One-To-Many Relationship: [msdyn_dmssyncrequest msdyn_dmssyncrequest_DeletedItemReferences](msdyn_dmssyncrequest.md#BKMK_msdyn_dmssyncrequest_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncrequest`|
|ReferencedAttribute|`msdyn_dmssyncrequestid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_dmssyncrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncstatus_DeletedItemReferences"></a> msdyn_dmssyncstatus_DeletedItemReferences

One-To-Many Relationship: [msdyn_dmssyncstatus msdyn_dmssyncstatus_DeletedItemReferences](msdyn_dmssyncstatus.md#BKMK_msdyn_dmssyncstatus_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncstatus`|
|ReferencedAttribute|`msdyn_dmssyncstatusid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_dmssyncstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entityrefreshhistory_DeletedItemReferences"></a> msdyn_entityrefreshhistory_DeletedItemReferences

One-To-Many Relationship: [msdyn_entityrefreshhistory msdyn_entityrefreshhistory_DeletedItemReferences](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entityrefreshhistory`|
|ReferencedAttribute|`msdyn_entityrefreshhistoryid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_entityrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_favoriteknowledgearticle_DeletedItemReferences"></a> msdyn_favoriteknowledgearticle_DeletedItemReferences

One-To-Many Relationship: [msdyn_favoriteknowledgearticle msdyn_favoriteknowledgearticle_DeletedItemReferences](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_favoriteknowledgearticle`|
|ReferencedAttribute|`msdyn_favoriteknowledgearticleid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_favoriteknowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticle_DeletedItemReferences"></a> msdyn_federatedarticle_DeletedItemReferences

One-To-Many Relationship: [msdyn_federatedarticle msdyn_federatedarticle_DeletedItemReferences](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticle`|
|ReferencedAttribute|`msdyn_federatedarticleid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_federatedarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticleincident_DeletedItemReferences"></a> msdyn_federatedarticleincident_DeletedItemReferences

One-To-Many Relationship: [msdyn_federatedarticleincident msdyn_federatedarticleincident_DeletedItemReferences](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticleincident`|
|ReferencedAttribute|`msdyn_federatedarticleincidentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_federatedarticleincident`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_fileupload_DeletedItemReferences"></a> msdyn_fileupload_DeletedItemReferences

One-To-Many Relationship: [msdyn_fileupload msdyn_fileupload_DeletedItemReferences](msdyn_fileupload.md#BKMK_msdyn_fileupload_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_fileupload`|
|ReferencedAttribute|`msdyn_fileuploadid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_fileupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_actionapprovalmodel_DeletedItemReferences"></a> msdyn_flow_actionapprovalmodel_DeletedItemReferences

One-To-Many Relationship: [msdyn_flow_actionapprovalmodel msdyn_flow_actionapprovalmodel_DeletedItemReferences](msdyn_flow_actionapprovalmodel.md#BKMK_msdyn_flow_actionapprovalmodel_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_actionapprovalmodelid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_flow_actionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approval_DeletedItemReferences"></a> msdyn_flow_approval_DeletedItemReferences

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approval_DeletedItemReferences](msdyn_flow_approval.md#BKMK_msdyn_flow_approval_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_flow_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrequest_DeletedItemReferences"></a> msdyn_flow_approvalrequest_DeletedItemReferences

One-To-Many Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrequest_DeletedItemReferences](msdyn_flow_approvalrequest.md#BKMK_msdyn_flow_approvalrequest_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalrequest`|
|ReferencedAttribute|`msdyn_flow_approvalrequestid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_flow_approvalrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalresponse_DeletedItemReferences"></a> msdyn_flow_approvalresponse_DeletedItemReferences

One-To-Many Relationship: [msdyn_flow_approvalresponse msdyn_flow_approvalresponse_DeletedItemReferences](msdyn_flow_approvalresponse.md#BKMK_msdyn_flow_approvalresponse_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalresponse`|
|ReferencedAttribute|`msdyn_flow_approvalresponseid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_flow_approvalresponse`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalstep_DeletedItemReferences"></a> msdyn_flow_approvalstep_DeletedItemReferences

One-To-Many Relationship: [msdyn_flow_approvalstep msdyn_flow_approvalstep_DeletedItemReferences](msdyn_flow_approvalstep.md#BKMK_msdyn_flow_approvalstep_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalstep`|
|ReferencedAttribute|`msdyn_flow_approvalstepid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_flow_approvalstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallactionapprovalmodel_DeletedItemReferences"></a> msdyn_flow_awaitallactionapprovalmodel_DeletedItemReferences

One-To-Many Relationship: [msdyn_flow_awaitallactionapprovalmodel msdyn_flow_awaitallactionapprovalmodel_DeletedItemReferences](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_msdyn_flow_awaitallactionapprovalmodel_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallactionapprovalmodelid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_flow_awaitallactionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallapprovalmodel_DeletedItemReferences"></a> msdyn_flow_awaitallapprovalmodel_DeletedItemReferences

One-To-Many Relationship: [msdyn_flow_awaitallapprovalmodel msdyn_flow_awaitallapprovalmodel_DeletedItemReferences](msdyn_flow_awaitallapprovalmodel.md#BKMK_msdyn_flow_awaitallapprovalmodel_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallapprovalmodelid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_flow_awaitallapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_basicapprovalmodel_DeletedItemReferences"></a> msdyn_flow_basicapprovalmodel_DeletedItemReferences

One-To-Many Relationship: [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodel_DeletedItemReferences](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodel_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_basicapprovalmodelid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_flow_basicapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_flowapproval_DeletedItemReferences"></a> msdyn_flow_flowapproval_DeletedItemReferences

One-To-Many Relationship: [msdyn_flow_flowapproval msdyn_flow_flowapproval_DeletedItemReferences](msdyn_flow_flowapproval.md#BKMK_msdyn_flow_flowapproval_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_flowapproval`|
|ReferencedAttribute|`msdyn_flow_flowapprovalid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_flow_flowapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_harvesteligibilitycondition_DeletedItemReferences"></a> msdyn_harvesteligibilitycondition_DeletedItemReferences

One-To-Many Relationship: [msdyn_harvesteligibilitycondition msdyn_harvesteligibilitycondition_DeletedItemReferences](msdyn_harvesteligibilitycondition.md#BKMK_msdyn_harvesteligibilitycondition_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_harvesteligibilitycondition`|
|ReferencedAttribute|`msdyn_harvesteligibilityconditionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_harvesteligibilitycondition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_harvestworkitem_DeletedItemReferences"></a> msdyn_harvestworkitem_DeletedItemReferences

One-To-Many Relationship: [msdyn_harvestworkitem msdyn_harvestworkitem_DeletedItemReferences](msdyn_harvestworkitem.md#BKMK_msdyn_harvestworkitem_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_harvestworkitem`|
|ReferencedAttribute|`msdyn_harvestworkitemid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_harvestworkitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_historicalcaseharvestbatch_DeletedItemReferences"></a> msdyn_historicalcaseharvestbatch_DeletedItemReferences

One-To-Many Relationship: [msdyn_historicalcaseharvestbatch msdyn_historicalcaseharvestbatch_DeletedItemReferences](msdyn_historicalcaseharvestbatch.md#BKMK_msdyn_historicalcaseharvestbatch_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_historicalcaseharvestbatch`|
|ReferencedAttribute|`msdyn_historicalcaseharvestbatchid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_historicalcaseharvestbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_historicalcaseharvestrun_DeletedItemReferences"></a> msdyn_historicalcaseharvestrun_DeletedItemReferences

One-To-Many Relationship: [msdyn_historicalcaseharvestrun msdyn_historicalcaseharvestrun_DeletedItemReferences](msdyn_historicalcaseharvestrun.md#BKMK_msdyn_historicalcaseharvestrun_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_historicalcaseharvestrun`|
|ReferencedAttribute|`msdyn_historicalcaseharvestrunid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_historicalcaseharvestrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_historicalcaseharvestrunlog_DeletedItemReferences"></a> msdyn_historicalcaseharvestrunlog_DeletedItemReferences

One-To-Many Relationship: [msdyn_historicalcaseharvestrunlog msdyn_historicalcaseharvestrunlog_DeletedItemReferences](msdyn_historicalcaseharvestrunlog.md#BKMK_msdyn_historicalcaseharvestrunlog_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_historicalcaseharvestrunlog`|
|ReferencedAttribute|`msdyn_historicalcaseharvestrunlogid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_historicalcaseharvestrunlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_integratedsearchprovider_DeletedItemReferences"></a> msdyn_integratedsearchprovider_DeletedItemReferences

One-To-Many Relationship: [msdyn_integratedsearchprovider msdyn_integratedsearchprovider_DeletedItemReferences](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_integratedsearchprovider`|
|ReferencedAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_integratedsearchprovider`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kalanguagesetting_DeletedItemReferences"></a> msdyn_kalanguagesetting_DeletedItemReferences

One-To-Many Relationship: [msdyn_kalanguagesetting msdyn_kalanguagesetting_DeletedItemReferences](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kalanguagesetting`|
|ReferencedAttribute|`msdyn_kalanguagesettingid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_kalanguagesetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kbattachment_DeletedItemReferences"></a> msdyn_kbattachment_DeletedItemReferences

One-To-Many Relationship: [msdyn_kbattachment msdyn_kbattachment_DeletedItemReferences](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kbattachment`|
|ReferencedAttribute|`msdyn_kbattachmentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_kbattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_DeletedItemReferences"></a> msdyn_kmfederatedsearchconfig_DeletedItemReferences

One-To-Many Relationship: [msdyn_kmfederatedsearchconfig msdyn_kmfederatedsearchconfig_DeletedItemReferences](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencedAttribute|`msdyn_kmfederatedsearchconfigid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_kmfederatedsearchconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmpersonalizationsetting_DeletedItemReferences"></a> msdyn_kmpersonalizationsetting_DeletedItemReferences

One-To-Many Relationship: [msdyn_kmpersonalizationsetting msdyn_kmpersonalizationsetting_DeletedItemReferences](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmpersonalizationsetting`|
|ReferencedAttribute|`msdyn_kmpersonalizationsettingid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_kmpersonalizationsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticleimage_DeletedItemReferences"></a> msdyn_knowledgearticleimage_DeletedItemReferences

One-To-Many Relationship: [msdyn_knowledgearticleimage msdyn_knowledgearticleimage_DeletedItemReferences](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticleimage`|
|ReferencedAttribute|`msdyn_knowledgearticleimageid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_knowledgearticleimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticletemplate_DeletedItemReferences"></a> msdyn_knowledgearticletemplate_DeletedItemReferences

One-To-Many Relationship: [msdyn_knowledgearticletemplate msdyn_knowledgearticletemplate_DeletedItemReferences](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticletemplate`|
|ReferencedAttribute|`msdyn_knowledgearticletemplateid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_knowledgearticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeconfiguration_DeletedItemReferences"></a> msdyn_knowledgeconfiguration_DeletedItemReferences

One-To-Many Relationship: [msdyn_knowledgeconfiguration msdyn_knowledgeconfiguration_DeletedItemReferences](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeconfigurationid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_knowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeharvestjobrecord_DeletedItemReferences"></a> msdyn_knowledgeharvestjobrecord_DeletedItemReferences

One-To-Many Relationship: [msdyn_knowledgeharvestjobrecord msdyn_knowledgeharvestjobrecord_DeletedItemReferences](msdyn_knowledgeharvestjobrecord.md#BKMK_msdyn_knowledgeharvestjobrecord_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeharvestjobrecord`|
|ReferencedAttribute|`msdyn_knowledgeharvestjobrecordid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_knowledgeharvestjobrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeinteractioninsight_DeletedItemReferences"></a> msdyn_knowledgeinteractioninsight_DeletedItemReferences

One-To-Many Relationship: [msdyn_knowledgeinteractioninsight msdyn_knowledgeinteractioninsight_DeletedItemReferences](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencedAttribute|`msdyn_knowledgeinteractioninsightid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_knowledgeinteractioninsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgepersonalfilter_DeletedItemReferences"></a> msdyn_knowledgepersonalfilter_DeletedItemReferences

One-To-Many Relationship: [msdyn_knowledgepersonalfilter msdyn_knowledgepersonalfilter_DeletedItemReferences](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgepersonalfilter`|
|ReferencedAttribute|`msdyn_knowledgepersonalfilterid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_knowledgepersonalfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchinsight_DeletedItemReferences"></a> msdyn_knowledgesearchinsight_DeletedItemReferences

One-To-Many Relationship: [msdyn_knowledgesearchinsight msdyn_knowledgesearchinsight_DeletedItemReferences](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchinsight`|
|ReferencedAttribute|`msdyn_knowledgesearchinsightid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_knowledgesearchinsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_powerappswrapbuild_DeletedItemReferences"></a> msdyn_powerappswrapbuild_DeletedItemReferences

One-To-Many Relationship: [msdyn_powerappswrapbuild msdyn_powerappswrapbuild_DeletedItemReferences](msdyn_powerappswrapbuild.md#BKMK_msdyn_powerappswrapbuild_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_powerappswrapbuild`|
|ReferencedAttribute|`msdyn_powerappswrapbuildid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_powerappswrapbuild`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_qna_DeletedItemReferences"></a> msdyn_qna_DeletedItemReferences

One-To-Many Relationship: [msdyn_qna msdyn_qna_DeletedItemReferences](msdyn_qna.md#BKMK_msdyn_qna_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_qna`|
|ReferencedAttribute|`msdyn_qnaid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_qna`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_richtextfile_DeletedItemReferences"></a> msdyn_richtextfile_DeletedItemReferences

One-To-Many Relationship: [msdyn_richtextfile msdyn_richtextfile_DeletedItemReferences](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_richtextfile`|
|ReferencedAttribute|`msdyn_richtextfileid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_richtextfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_serviceconfiguration_DeletedItemReferences"></a> msdyn_serviceconfiguration_DeletedItemReferences

One-To-Many Relationship: [msdyn_serviceconfiguration msdyn_serviceconfiguration_DeletedItemReferences](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_serviceconfiguration`|
|ReferencedAttribute|`msdyn_serviceconfigurationid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_serviceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthrule_DeletedItemReferences"></a> msdyn_solutionhealthrule_DeletedItemReferences

One-To-Many Relationship: [msdyn_solutionhealthrule msdyn_solutionhealthrule_DeletedItemReferences](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthrule`|
|ReferencedAttribute|`msdyn_solutionhealthruleid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_solutionhealthrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleargument_DeletedItemReferences"></a> msdyn_solutionhealthruleargument_DeletedItemReferences

One-To-Many Relationship: [msdyn_solutionhealthruleargument msdyn_solutionhealthruleargument_DeletedItemReferences](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleargument`|
|ReferencedAttribute|`msdyn_solutionhealthruleargumentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_solutionhealthruleargument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleset_DeletedItemReferences"></a> msdyn_solutionhealthruleset_DeletedItemReferences

One-To-Many Relationship: [msdyn_solutionhealthruleset msdyn_solutionhealthruleset_DeletedItemReferences](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleset`|
|ReferencedAttribute|`msdyn_solutionhealthrulesetid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_solutionhealthruleset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_virtualtablecolumncandidate_DeletedItemReferences"></a> msdyn_virtualtablecolumncandidate_DeletedItemReferences

One-To-Many Relationship: [msdyn_virtualtablecolumncandidate msdyn_virtualtablecolumncandidate_DeletedItemReferences](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencedAttribute|`msdyn_virtualtablecolumncandidateid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdyn_virtualtablecolumncandidate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdynce_botcontent_DeletedItemReferences"></a> msdynce_botcontent_DeletedItemReferences

One-To-Many Relationship: [msdynce_botcontent msdynce_botcontent_DeletedItemReferences](msdynce_botcontent.md#BKMK_msdynce_botcontent_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msdynce_botcontent`|
|ReferencedAttribute|`msdynce_botcontentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msdynce_botcontent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msgraphresourcetosubscription_DeletedItemReferences"></a> msgraphresourcetosubscription_DeletedItemReferences

One-To-Many Relationship: [msgraphresourcetosubscription msgraphresourcetosubscription_DeletedItemReferences](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`msgraphresourcetosubscription`|
|ReferencedAttribute|`msgraphresourcetosubscriptionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_msgraphresourcetosubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_DeletedItemReferences"></a> mspcat_catalogsubmissionfiles_DeletedItemReferences

One-To-Many Relationship: [mspcat_catalogsubmissionfiles mspcat_catalogsubmissionfiles_DeletedItemReferences](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_catalogsubmissionfiles`|
|ReferencedAttribute|`mspcat_catalogsubmissionfilesid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_mspcat_catalogsubmissionfiles`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_packagestore_DeletedItemReferences"></a> mspcat_packagestore_DeletedItemReferences

One-To-Many Relationship: [mspcat_packagestore mspcat_packagestore_DeletedItemReferences](mspcat_packagestore.md#BKMK_mspcat_packagestore_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_packagestore`|
|ReferencedAttribute|`mspcat_packagestoreid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_mspcat_packagestore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_officegraphdocument_DeletedItemReferences"></a> officegraphdocument_DeletedItemReferences

One-To-Many Relationship: [officegraphdocument officegraphdocument_DeletedItemReferences](officegraphdocument.md#BKMK_officegraphdocument_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`officegraphdocument`|
|ReferencedAttribute|`officegraphdocumentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_officegraphdocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_deleteditemreference"></a> organization_deleteditemreference

One-To-Many Relationship: [organization organization_deleteditemreference](organization.md#BKMK_organization_deleteditemreference)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncfnostate_DeletedItemReferences"></a> organizationdatasyncfnostate_DeletedItemReferences

One-To-Many Relationship: [organizationdatasyncfnostate organizationdatasyncfnostate_DeletedItemReferences](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncfnostate`|
|ReferencedAttribute|`organizationdatasyncfnostateid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_organizationdatasyncfnostate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncstate_DeletedItemReferences"></a> organizationdatasyncstate_DeletedItemReferences

One-To-Many Relationship: [organizationdatasyncstate organizationdatasyncstate_DeletedItemReferences](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncstate`|
|ReferencedAttribute|`organizationdatasyncstateid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_organizationdatasyncstate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscription_DeletedItemReferences"></a> organizationdatasyncsubscription_DeletedItemReferences

One-To-Many Relationship: [organizationdatasyncsubscription organizationdatasyncsubscription_DeletedItemReferences](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_organizationdatasyncsubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionentity_DeletedItemReferences"></a> organizationdatasyncsubscriptionentity_DeletedItemReferences

One-To-Many Relationship: [organizationdatasyncsubscriptionentity organizationdatasyncsubscriptionentity_DeletedItemReferences](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionentity`|
|ReferencedAttribute|`organizationdatasyncsubscriptionentityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_organizationdatasyncsubscriptionentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_DeletedItemReferences"></a> organizationdatasyncsubscriptionfnotable_DeletedItemReferences

One-To-Many Relationship: [organizationdatasyncsubscriptionfnotable organizationdatasyncsubscriptionfnotable_DeletedItemReferences](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencedAttribute|`organizationdatasyncsubscriptionfnotableid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_organizationdatasyncsubscriptionfnotable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_DeletedItemReferences"></a> owner_DeletedItemReferences

One-To-Many Relationship: [owner owner_DeletedItemReferences](owner.md#BKMK_owner_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_owner`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_package_DeletedItemReferences"></a> package_DeletedItemReferences

One-To-Many Relationship: [package package_DeletedItemReferences](package.md#BKMK_package_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`package`|
|ReferencedAttribute|`packageid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_package`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_packagehistory_DeletedItemReferences"></a> packagehistory_DeletedItemReferences

One-To-Many Relationship: [packagehistory packagehistory_DeletedItemReferences](packagehistory.md#BKMK_packagehistory_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`packagehistory`|
|ReferencedAttribute|`packagehistoryid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_packagehistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_personaldocumenttemplate_DeletedItemReferences"></a> personaldocumenttemplate_DeletedItemReferences

One-To-Many Relationship: [personaldocumenttemplate personaldocumenttemplate_DeletedItemReferences](personaldocumenttemplate.md#BKMK_personaldocumenttemplate_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`personaldocumenttemplate`|
|ReferencedAttribute|`personaldocumenttemplateid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_personaldocumenttemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_phonecall_DeletedItemReferences"></a> phonecall_DeletedItemReferences

One-To-Many Relationship: [phonecall phonecall_DeletedItemReferences](phonecall.md#BKMK_phonecall_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannerbusinessscenario_DeletedItemReferences"></a> plannerbusinessscenario_DeletedItemReferences

One-To-Many Relationship: [plannerbusinessscenario plannerbusinessscenario_DeletedItemReferences](plannerbusinessscenario.md#BKMK_plannerbusinessscenario_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`plannerbusinessscenario`|
|ReferencedAttribute|`plannerbusinessscenarioid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_plannerbusinessscenario`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannersyncaction_DeletedItemReferences"></a> plannersyncaction_DeletedItemReferences

One-To-Many Relationship: [plannersyncaction plannersyncaction_DeletedItemReferences](plannersyncaction.md#BKMK_plannersyncaction_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`plannersyncaction`|
|ReferencedAttribute|`plannersyncactionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_plannersyncaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plugintypestatistic_DeletedItemReferences"></a> plugintypestatistic_DeletedItemReferences

One-To-Many Relationship: [plugintypestatistic plugintypestatistic_DeletedItemReferences](plugintypestatistic.md#BKMK_plugintypestatistic_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`plugintypestatistic`|
|ReferencedAttribute|`plugintypestatisticid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_plugintypestatistic`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_post_DeletedItemReferences"></a> post_DeletedItemReferences

One-To-Many Relationship: [post post_DeletedItemReferences](post.md#BKMK_post_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`post`|
|ReferencedAttribute|`postid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_post`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_postcomment_DeletedItemReferences"></a> postcomment_DeletedItemReferences

One-To-Many Relationship: [postcomment postcomment_DeletedItemReferences](postcomment.md#BKMK_postcomment_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`postcomment`|
|ReferencedAttribute|`postcommentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_postcomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_postfollow_DeletedItemReferences"></a> postfollow_DeletedItemReferences

One-To-Many Relationship: [postfollow postfollow_DeletedItemReferences](postfollow.md#BKMK_postfollow_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`postfollow`|
|ReferencedAttribute|`postfollowid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_postfollow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_postlike_DeletedItemReferences"></a> postlike_DeletedItemReferences

One-To-Many Relationship: [postlike postlike_DeletedItemReferences](postlike.md#BKMK_postlike_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`postlike`|
|ReferencedAttribute|`postlikeid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_postlike`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_postregarding_DeletedItemReferences"></a> postregarding_DeletedItemReferences

One-To-Many Relationship: [postregarding postregarding_DeletedItemReferences](postregarding.md#BKMK_postregarding_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`postregarding`|
|ReferencedAttribute|`postregardingid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_postregarding`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesddosalert_DeletedItemReferences"></a> powerpagesddosalert_DeletedItemReferences

One-To-Many Relationship: [powerpagesddosalert powerpagesddosalert_DeletedItemReferences](powerpagesddosalert.md#BKMK_powerpagesddosalert_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesddosalert`|
|ReferencedAttribute|`powerpagesddosalertid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_powerpagesddosalert`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitepublished_DeletedItemReferences"></a> powerpagesitepublished_DeletedItemReferences

One-To-Many Relationship: [powerpagesitepublished powerpagesitepublished_DeletedItemReferences](powerpagesitepublished.md#BKMK_powerpagesitepublished_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitepublished`|
|ReferencedAttribute|`powerpagesitepublishedid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_powerpagesitepublished`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesmanagedidentity_DeletedItemReferences"></a> powerpagesmanagedidentity_DeletedItemReferences

One-To-Many Relationship: [powerpagesmanagedidentity powerpagesmanagedidentity_DeletedItemReferences](powerpagesmanagedidentity.md#BKMK_powerpagesmanagedidentity_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesmanagedidentity`|
|ReferencedAttribute|`powerpagesmanagedidentityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_powerpagesmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesscanreport_DeletedItemReferences"></a> powerpagesscanreport_DeletedItemReferences

One-To-Many Relationship: [powerpagesscanreport powerpagesscanreport_DeletedItemReferences](powerpagesscanreport.md#BKMK_powerpagesscanreport_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesscanreport`|
|ReferencedAttribute|`powerpagesscanreportid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_powerpagesscanreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesusermapping_DeletedItemReferences"></a> powerpagesusermapping_DeletedItemReferences

One-To-Many Relationship: [powerpagesusermapping powerpagesusermapping_DeletedItemReferences](powerpagesusermapping.md#BKMK_powerpagesusermapping_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesusermapping`|
|ReferencedAttribute|`powerpagesusermappingid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_powerpagesusermapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_principalobjectaccess_DeletedItemReferences"></a> principalobjectaccess_DeletedItemReferences

One-To-Many Relationship: [principalobjectaccess principalobjectaccess_DeletedItemReferences](principalobjectaccess.md#BKMK_principalobjectaccess_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`principalobjectaccess`|
|ReferencedAttribute|`principalobjectaccessid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_principalobjectaccess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_principalobjectattributeaccess_DeletedItemReferences"></a> principalobjectattributeaccess_DeletedItemReferences

One-To-Many Relationship: [principalobjectattributeaccess principalobjectattributeaccess_DeletedItemReferences](principalobjectattributeaccess.md#BKMK_principalobjectattributeaccess_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`principalobjectattributeaccess`|
|ReferencedAttribute|`principalobjectattributeaccessid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_principalobjectattributeaccess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerlog_DeletedItemReferences"></a> privilegecheckerlog_DeletedItemReferences

One-To-Many Relationship: [privilegecheckerlog privilegecheckerlog_DeletedItemReferences](privilegecheckerlog.md#BKMK_privilegecheckerlog_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerlog`|
|ReferencedAttribute|`privilegecheckerlogid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_privilegecheckerlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerrun_DeletedItemReferences"></a> privilegecheckerrun_DeletedItemReferences

One-To-Many Relationship: [privilegecheckerrun privilegecheckerrun_DeletedItemReferences](privilegecheckerrun.md#BKMK_privilegecheckerrun_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerrun`|
|ReferencedAttribute|`privilegecheckerrunid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_privilegecheckerrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstageparameter_DeletedItemReferences"></a> processstageparameter_DeletedItemReferences

One-To-Many Relationship: [processstageparameter processstageparameter_DeletedItemReferences](processstageparameter.md#BKMK_processstageparameter_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`processstageparameter`|
|ReferencedAttribute|`processstageparameterid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_processstageparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_provisionlanguageforuser_DeletedItemReferences"></a> provisionlanguageforuser_DeletedItemReferences

One-To-Many Relationship: [provisionlanguageforuser provisionlanguageforuser_DeletedItemReferences](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`provisionlanguageforuser`|
|ReferencedAttribute|`provisionlanguageforuserid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_provisionlanguageforuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_purviewlabelinfo_DeletedItemReferences"></a> purviewlabelinfo_DeletedItemReferences

One-To-Many Relationship: [purviewlabelinfo purviewlabelinfo_DeletedItemReferences](purviewlabelinfo.md#BKMK_purviewlabelinfo_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`purviewlabelinfo`|
|ReferencedAttribute|`purviewlabelinfoid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_purviewlabelinfo`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_queueitem_DeletedItemReferences"></a> queueitem_DeletedItemReferences

One-To-Many Relationship: [queueitem queueitem_DeletedItemReferences](queueitem.md#BKMK_queueitem_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`queueitem`|
|ReferencedAttribute|`queueitemid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_queueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recommendeddocument_DeletedItemReferences"></a> recommendeddocument_DeletedItemReferences

One-To-Many Relationship: [recommendeddocument recommendeddocument_DeletedItemReferences](recommendeddocument.md#BKMK_recommendeddocument_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`recommendeddocument`|
|ReferencedAttribute|`recommendeddocumentid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_recommendeddocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recurrencerule_DeletedItemReferences"></a> recurrencerule_DeletedItemReferences

One-To-Many Relationship: [recurrencerule recurrencerule_DeletedItemReferences](recurrencerule.md#BKMK_recurrencerule_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`recurrencerule`|
|ReferencedAttribute|`ruleid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_recurrencerule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_RecycleBinConfig_DeletedItemReference_DeletedObject"></a> RecycleBinConfig_DeletedItemReference_DeletedObject

One-To-Many Relationship: [recyclebinconfig RecycleBinConfig_DeletedItemReference_DeletedObject](recyclebinconfig.md#BKMK_RecycleBinConfig_DeletedItemReference_DeletedObject)

|Property|Value|
|---|---|
|ReferencedEntity|`recyclebinconfig`|
|ReferencedAttribute|`recyclebinconfigid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`DeletedObject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionfailuredetail_DeletedItemReferences"></a> retentionfailuredetail_DeletedItemReferences

One-To-Many Relationship: [retentionfailuredetail retentionfailuredetail_DeletedItemReferences](retentionfailuredetail.md#BKMK_retentionfailuredetail_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionfailuredetail`|
|ReferencedAttribute|`retentionfailuredetailid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_retentionfailuredetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperation_DeletedItemReferences"></a> retentionoperation_DeletedItemReferences

One-To-Many Relationship: [retentionoperation retentionoperation_DeletedItemReferences](retentionoperation.md#BKMK_retentionoperation_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperation`|
|ReferencedAttribute|`retentionoperationid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_retentionoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperationdetail_DeletedItemReferences"></a> retentionoperationdetail_DeletedItemReferences

One-To-Many Relationship: [retentionoperationdetail retentionoperationdetail_DeletedItemReferences](retentionoperationdetail.md#BKMK_retentionoperationdetail_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperationdetail`|
|ReferencedAttribute|`retentionoperationdetailid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_retentionoperationdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionsuccessdetail_DeletedItemReferences"></a> retentionsuccessdetail_DeletedItemReferences

One-To-Many Relationship: [retentionsuccessdetail retentionsuccessdetail_DeletedItemReferences](retentionsuccessdetail.md#BKMK_retentionsuccessdetail_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionsuccessdetail`|
|ReferencedAttribute|`retentionsuccessdetailid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_retentionsuccessdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_rollupfield_DeletedItemReferences"></a> rollupfield_DeletedItemReferences

One-To-Many Relationship: [rollupfield rollupfield_DeletedItemReferences](rollupfield.md#BKMK_rollupfield_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`rollupfield`|
|ReferencedAttribute|`rollupfieldid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_rollupfield`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sa_suggestedaction_DeletedItemReferences"></a> sa_suggestedaction_DeletedItemReferences

One-To-Many Relationship: [sa_suggestedaction sa_suggestedaction_DeletedItemReferences](sa_suggestedaction.md#BKMK_sa_suggestedaction_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`sa_suggestedaction`|
|ReferencedAttribute|`sa_suggestedactionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_sa_suggestedaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sa_suggestedactioncriteria_DeletedItemReferences"></a> sa_suggestedactioncriteria_DeletedItemReferences

One-To-Many Relationship: [sa_suggestedactioncriteria sa_suggestedactioncriteria_DeletedItemReferences](sa_suggestedactioncriteria.md#BKMK_sa_suggestedactioncriteria_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`sa_suggestedactioncriteria`|
|ReferencedAttribute|`sa_suggestedactioncriteriaid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_sa_suggestedactioncriteria`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sdkmessageprocessingstepsecureconfig_DeletedItemReferences"></a> sdkmessageprocessingstepsecureconfig_DeletedItemReferences

One-To-Many Relationship: [sdkmessageprocessingstepsecureconfig sdkmessageprocessingstepsecureconfig_DeletedItemReferences](sdkmessageprocessingstepsecureconfig.md#BKMK_sdkmessageprocessingstepsecureconfig_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`sdkmessageprocessingstepsecureconfig`|
|ReferencedAttribute|`sdkmessageprocessingstepsecureconfigid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_sdkmessageprocessingstepsecureconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchattributesettings_DeletedItemReferences"></a> searchattributesettings_DeletedItemReferences

One-To-Many Relationship: [searchattributesettings searchattributesettings_DeletedItemReferences](searchattributesettings.md#BKMK_searchattributesettings_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`searchattributesettings`|
|ReferencedAttribute|`searchattributesettingsid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_searchattributesettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchcustomanalyzer_DeletedItemReferences"></a> searchcustomanalyzer_DeletedItemReferences

One-To-Many Relationship: [searchcustomanalyzer searchcustomanalyzer_DeletedItemReferences](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`searchcustomanalyzer`|
|ReferencedAttribute|`searchcustomanalyzerid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_searchcustomanalyzer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchrelationshipsettings_DeletedItemReferences"></a> searchrelationshipsettings_DeletedItemReferences

One-To-Many Relationship: [searchrelationshipsettings searchrelationshipsettings_DeletedItemReferences](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`searchrelationshipsettings`|
|ReferencedAttribute|`searchrelationshipsettingsid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_searchrelationshipsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedobject_DeletedItemReferences"></a> sharedobject_DeletedItemReferences

One-To-Many Relationship: [sharedobject sharedobject_DeletedItemReferences](sharedobject.md#BKMK_sharedobject_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedobject`|
|ReferencedAttribute|`sharedobjectid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_sharedobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspace_DeletedItemReferences"></a> sharedworkspace_DeletedItemReferences

One-To-Many Relationship: [sharedworkspace sharedworkspace_DeletedItemReferences](sharedworkspace.md#BKMK_sharedworkspace_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspace`|
|ReferencedAttribute|`sharedworkspaceid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_sharedworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspacepool_DeletedItemReferences"></a> sharedworkspacepool_DeletedItemReferences

One-To-Many Relationship: [sharedworkspacepool sharedworkspacepool_DeletedItemReferences](sharedworkspacepool.md#BKMK_sharedworkspacepool_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspacepool`|
|ReferencedAttribute|`sharedworkspacepoolid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_sharedworkspacepool`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharepointdocumentlocation_DeletedItemReferences"></a> sharepointdocumentlocation_DeletedItemReferences

One-To-Many Relationship: [sharepointdocumentlocation sharepointdocumentlocation_DeletedItemReferences](sharepointdocumentlocation.md#BKMK_sharepointdocumentlocation_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointdocumentlocation`|
|ReferencedAttribute|`sharepointdocumentlocationid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_sharepointdocumentlocation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sideloadedaiplugin_DeletedItemReferences"></a> sideloadedaiplugin_DeletedItemReferences

One-To-Many Relationship: [sideloadedaiplugin sideloadedaiplugin_DeletedItemReferences](sideloadedaiplugin.md#BKMK_sideloadedaiplugin_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`sideloadedaiplugin`|
|ReferencedAttribute|`sideloadedaipluginid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_sideloadedaiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_socialactivity_DeletedItemReferences"></a> socialactivity_DeletedItemReferences

One-To-Many Relationship: [socialactivity socialactivity_DeletedItemReferences](socialactivity.md#BKMK_socialactivity_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_socialactivity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_socialprofile_DeletedItemReferences"></a> socialprofile_DeletedItemReferences

One-To-Many Relationship: [socialprofile socialprofile_DeletedItemReferences](socialprofile.md#BKMK_socialprofile_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`socialprofile`|
|ReferencedAttribute|`socialprofileid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_socialprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sourcecontroloperationtracking_DeletedItemReferences"></a> sourcecontroloperationtracking_DeletedItemReferences

One-To-Many Relationship: [sourcecontroloperationtracking sourcecontroloperationtracking_DeletedItemReferences](sourcecontroloperationtracking.md#BKMK_sourcecontroloperationtracking_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`sourcecontroloperationtracking`|
|ReferencedAttribute|`sourcecontroloperationtrackingid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_sourcecontroloperationtracking`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentity_DeletedItemReferences"></a> stagedentity_DeletedItemReferences

One-To-Many Relationship: [stagedentity stagedentity_DeletedItemReferences](stagedentity.md#BKMK_stagedentity_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentity`|
|ReferencedAttribute|`stagedentityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_stagedentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentityattribute_DeletedItemReferences"></a> stagedentityattribute_DeletedItemReferences

One-To-Many Relationship: [stagedentityattribute stagedentityattribute_DeletedItemReferences](stagedentityattribute.md#BKMK_stagedentityattribute_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentityattribute`|
|ReferencedAttribute|`stagedentityattributeid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_stagedentityattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedmetadataasyncoperation_DeletedItemReferences"></a> stagedmetadataasyncoperation_DeletedItemReferences

One-To-Many Relationship: [stagedmetadataasyncoperation stagedmetadataasyncoperation_DeletedItemReferences](stagedmetadataasyncoperation.md#BKMK_stagedmetadataasyncoperation_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedmetadataasyncoperation`|
|ReferencedAttribute|`stagedmetadataasyncoperationid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_stagedmetadataasyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagesolutionupload_DeletedItemReferences"></a> stagesolutionupload_DeletedItemReferences

One-To-Many Relationship: [stagesolutionupload stagesolutionupload_DeletedItemReferences](stagesolutionupload.md#BKMK_stagesolutionupload_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`stagesolutionupload`|
|ReferencedAttribute|`stagesolutionuploadid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_stagesolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_subject_DeletedItemReferences"></a> subject_DeletedItemReferences

One-To-Many Relationship: [subject subject_DeletedItemReferences](subject.md#BKMK_subject_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`subject`|
|ReferencedAttribute|`subjectid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_subject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_subscriptionmanuallytrackedobject_DeletedItemReferences"></a> subscriptionmanuallytrackedobject_DeletedItemReferences

One-To-Many Relationship: [subscriptionmanuallytrackedobject subscriptionmanuallytrackedobject_DeletedItemReferences](subscriptionmanuallytrackedobject.md#BKMK_subscriptionmanuallytrackedobject_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`subscriptionmanuallytrackedobject`|
|ReferencedAttribute|`subscriptionmanuallytrackedobjectid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_subscriptionmanuallytrackedobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_subscriptionstatisticsoutlook_DeletedItemReferences"></a> subscriptionstatisticsoutlook_DeletedItemReferences

One-To-Many Relationship: [subscriptionstatisticsoutlook subscriptionstatisticsoutlook_DeletedItemReferences](subscriptionstatisticsoutlook.md#BKMK_subscriptionstatisticsoutlook_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`subscriptionstatisticsoutlook`|
|ReferencedAttribute|`subscriptionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_subscriptionstatisticsoutlook`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_subscriptionsyncentryoutlook_DeletedItemReferences"></a> subscriptionsyncentryoutlook_DeletedItemReferences

One-To-Many Relationship: [subscriptionsyncentryoutlook subscriptionsyncentryoutlook_DeletedItemReferences](subscriptionsyncentryoutlook.md#BKMK_subscriptionsyncentryoutlook_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`subscriptionsyncentryoutlook`|
|ReferencedAttribute|`subscriptionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_subscriptionsyncentryoutlook`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_supportusertable_DeletedItemReferences"></a> supportusertable_DeletedItemReferences

One-To-Many Relationship: [supportusertable supportusertable_DeletedItemReferences](supportusertable.md#BKMK_supportusertable_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`supportusertable`|
|ReferencedAttribute|`supportusertableid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_supportusertable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkexternaltablestate_DeletedItemReferences"></a> synapselinkexternaltablestate_DeletedItemReferences

One-To-Many Relationship: [synapselinkexternaltablestate synapselinkexternaltablestate_DeletedItemReferences](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkexternaltablestate`|
|ReferencedAttribute|`synapselinkexternaltablestateid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_synapselinkexternaltablestate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentitystate_DeletedItemReferences"></a> synapselinkprofileentitystate_DeletedItemReferences

One-To-Many Relationship: [synapselinkprofileentitystate synapselinkprofileentitystate_DeletedItemReferences](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentitystate`|
|ReferencedAttribute|`synapselinkprofileentitystateid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_synapselinkprofileentitystate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_task_DeletedItemReferences"></a> task_DeletedItemReferences

One-To-Many Relationship: [task task_DeletedItemReferences](task.md#BKMK_task_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_DeletedItemReferences"></a> team_DeletedItemReferences

One-To-Many Relationship: [team team_DeletedItemReferences](team.md#BKMK_team_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_territory_DeletedItemReferences"></a> territory_DeletedItemReferences

One-To-Many Relationship: [territory territory_DeletedItemReferences](territory.md#BKMK_territory_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`territory`|
|ReferencedAttribute|`territoryid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_territory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_theme_DeletedItemReferences"></a> theme_DeletedItemReferences

One-To-Many Relationship: [theme theme_DeletedItemReferences](theme.md#BKMK_theme_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`theme`|
|ReferencedAttribute|`themeid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_theme`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_timestampdatemapping_DeletedItemReferences"></a> timestampdatemapping_DeletedItemReferences

One-To-Many Relationship: [timestampdatemapping timestampdatemapping_DeletedItemReferences](timestampdatemapping.md#BKMK_timestampdatemapping_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`timestampdatemapping`|
|ReferencedAttribute|`timestampdatemappingid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_timestampdatemapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_timezonedefinition_DeletedItemReferences"></a> timezonedefinition_DeletedItemReferences

One-To-Many Relationship: [timezonedefinition timezonedefinition_DeletedItemReferences](timezonedefinition.md#BKMK_timezonedefinition_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`timezonedefinition`|
|ReferencedAttribute|`timezonedefinitionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_timezonedefinition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_timezonelocalizedname_DeletedItemReferences"></a> timezonelocalizedname_DeletedItemReferences

One-To-Many Relationship: [timezonelocalizedname timezonelocalizedname_DeletedItemReferences](timezonelocalizedname.md#BKMK_timezonelocalizedname_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`timezonelocalizedname`|
|ReferencedAttribute|`timezonelocalizednameid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_timezonelocalizedname`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_timezonerule_DeletedItemReferences"></a> timezonerule_DeletedItemReferences

One-To-Many Relationship: [timezonerule timezonerule_DeletedItemReferences](timezonerule.md#BKMK_timezonerule_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`timezonerule`|
|ReferencedAttribute|`timezoneruleid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_timezonerule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_transactioncurrency_DeletedItemReferences"></a> transactioncurrency_DeletedItemReferences

One-To-Many Relationship: [transactioncurrency transactioncurrency_DeletedItemReferences](transactioncurrency.md#BKMK_transactioncurrency_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_transactioncurrency`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_usermapping_DeletedItemReferences"></a> usermapping_DeletedItemReferences

One-To-Many Relationship: [usermapping usermapping_DeletedItemReferences](usermapping.md#BKMK_usermapping_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`usermapping`|
|ReferencedAttribute|`usermappingid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_usermapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_userrating_DeletedItemReferences"></a> userrating_DeletedItemReferences

One-To-Many Relationship: [userrating userrating_DeletedItemReferences](userrating.md#BKMK_userrating_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`userrating`|
|ReferencedAttribute|`userratingid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_userrating`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_usersettings_DeletedItemReferences"></a> usersettings_DeletedItemReferences

One-To-Many Relationship: [usersettings usersettings_DeletedItemReferences](usersettings.md#BKMK_usersettings_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`usersettings`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_usersettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_viewasexamplequestion_DeletedItemReferences"></a> viewasexamplequestion_DeletedItemReferences

One-To-Many Relationship: [viewasexamplequestion viewasexamplequestion_DeletedItemReferences](viewasexamplequestion.md#BKMK_viewasexamplequestion_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencedEntity|`viewasexamplequestion`|
|ReferencedAttribute|`viewasexamplequestionid`|
|ReferencingAttribute|`deletedobject`|
|ReferencingEntityNavigationPropertyName|`deletedobject_viewasexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [deleteditemreference_AsyncOperations](#BKMK_deleteditemreference_AsyncOperations)
- [deleteditemreference_BulkDeleteFailures](#BKMK_deleteditemreference_BulkDeleteFailures)
- [deleteditemreference_DuplicateBaseRecord](#BKMK_deleteditemreference_DuplicateBaseRecord)
- [deleteditemreference_DuplicateMatchingRecord](#BKMK_deleteditemreference_DuplicateMatchingRecord)
- [deleteditemreference_FileAttachments](#BKMK_deleteditemreference_FileAttachments)
- [deleteditemreference_MailboxTrackingFolders](#BKMK_deleteditemreference_MailboxTrackingFolders)
- [deleteditemreference_PrincipalObjectAttributeAccesses](#BKMK_deleteditemreference_PrincipalObjectAttributeAccesses)
- [deleteditemreference_ProcessSession](#BKMK_deleteditemreference_ProcessSession)
- [deleteditemreference_SyncErrors](#BKMK_deleteditemreference_SyncErrors)

### <a name="BKMK_deleteditemreference_AsyncOperations"></a> deleteditemreference_AsyncOperations

Many-To-One Relationship: [asyncoperation deleteditemreference_AsyncOperations](asyncoperation.md#BKMK_deleteditemreference_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`deleteditemreference_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_deleteditemreference_BulkDeleteFailures"></a> deleteditemreference_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure deleteditemreference_BulkDeleteFailures](bulkdeletefailure.md#BKMK_deleteditemreference_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`deleteditemreference_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_deleteditemreference_DuplicateBaseRecord"></a> deleteditemreference_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord deleteditemreference_DuplicateBaseRecord](duplicaterecord.md#BKMK_deleteditemreference_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`deleteditemreference_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_deleteditemreference_DuplicateMatchingRecord"></a> deleteditemreference_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord deleteditemreference_DuplicateMatchingRecord](duplicaterecord.md#BKMK_deleteditemreference_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`deleteditemreference_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_deleteditemreference_FileAttachments"></a> deleteditemreference_FileAttachments

Many-To-One Relationship: [fileattachment deleteditemreference_FileAttachments](fileattachment.md#BKMK_deleteditemreference_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`deleteditemreference_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_deleteditemreference_MailboxTrackingFolders"></a> deleteditemreference_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder deleteditemreference_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_deleteditemreference_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`deleteditemreference_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_deleteditemreference_PrincipalObjectAttributeAccesses"></a> deleteditemreference_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess deleteditemreference_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_deleteditemreference_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`deleteditemreference_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_deleteditemreference_ProcessSession"></a> deleteditemreference_ProcessSession

Many-To-One Relationship: [processsession deleteditemreference_ProcessSession](processsession.md#BKMK_deleteditemreference_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`deleteditemreference_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_deleteditemreference_SyncErrors"></a> deleteditemreference_SyncErrors

Many-To-One Relationship: [syncerror deleteditemreference_SyncErrors](syncerror.md#BKMK_deleteditemreference_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`deleteditemreference_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

