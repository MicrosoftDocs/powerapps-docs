---
title: "Field Sharing (PrincipalObjectAttributeAccess) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Field Sharing (PrincipalObjectAttributeAccess) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Field Sharing (PrincipalObjectAttributeAccess) table/entity reference (Microsoft Dataverse)

Defines CRM security principals (users and teams) access rights to secured field for an entity instance.

## Messages

The following table lists the messages for the Field Sharing (PrincipalObjectAttributeAccess) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /principalobjectattributeaccessset<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /principalobjectattributeaccessset(*principalobjectattributeaccessid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /principalobjectattributeaccessset(*principalobjectattributeaccessid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /principalobjectattributeaccessset<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /principalobjectattributeaccessset(*principalobjectattributeaccessid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /principalobjectattributeaccessset(*principalobjectattributeaccessid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Field Sharing (PrincipalObjectAttributeAccess) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Field Sharing** |
| **DisplayCollectionName** | **Field Sharing** |
| **SchemaName** | `PrincipalObjectAttributeAccess` |
| **CollectionSchemaName** | `PrincipalObjectAttributeAccesses` |
| **EntitySetName** | `principalobjectattributeaccessset`|
| **LogicalName** | `principalobjectattributeaccess` |
| **LogicalCollectionName** | `principalobjectattributeaccesses` |
| **PrimaryIdAttribute** | `principalobjectattributeaccessid` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeId](#BKMK_AttributeId)
- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [PrincipalId](#BKMK_PrincipalId)
- [PrincipalIdType](#BKMK_PrincipalIdType)
- [PrincipalObjectAttributeAccessId](#BKMK_PrincipalObjectAttributeAccessId)
- [ReadAccess](#BKMK_ReadAccess)
- [UpdateAccess](#BKMK_UpdateAccess)

### <a name="BKMK_AttributeId"></a> AttributeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the shared secured field**|
|DisplayName|**Secured field**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attributeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the entity instance with shared secured field**|
|DisplayName|**Entity instance**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|account, activityfileattachment, adx_externalidentity, adx_invitation, adx_inviteredemption, adx_portalcomment, adx_setting, adx_webformsession, aicopilot, aiinsightcard, aiplugin, aipluginauth, aipluginconversationstarter, aipluginconversationstartermapping, aipluginexternalschema, aipluginexternalschemaproperty, aiplugingovernance, aiplugingovernanceext, aiplugininstance, aipluginoperation, aipluginoperationparameter, aipluginoperationresponsetemplate, aiplugintitle, aipluginusersetting, aiskillconfig, appaction, appactionmigration, appactionrule, appelement, application, applicationuser, appmodulecomponentedge, appmodulecomponentnode, appointment, approvalprocess, approvalstageapproval, approvalstagecondition, approvalstageorder, appsetting, appusersetting, archivecleanupinfo, archivecleanupoperation, attributeimageconfig, attributemaskingrule, attributepicklistvalue, bot, botcomponent, botcomponentcollection, bulkarchiveconfig, bulkarchivefailuredetail, bulkarchiveoperation, bulkarchiveoperationdetail, businessprocess, businessunit, canvasappextendedmetadata, card, cascadegrantrevokeaccessrecordstracker, cascadegrantrevokeaccessversiontracker, catalog, catalogassignment, certificatecredential, channelaccessprofile, chat, comment, connection, connectioninstance, connectionreference, connector, contact, conversationtranscript, copilotexamplequestion, copilotglossaryterm, copilotsynonyms, credential, customapi, customapirequestparameter, customapiresponseproperty, customeraddress, datalakefolder, datalakefolderpermission, datalakeworkspace, datalakeworkspacepermission, dataprocessingconfiguration, delegatedauthorization, deleteditemreference, desktopflowbinary, desktopflowmodule, dvfilesearch, dvfilesearchattribute, dvfilesearchentity, dvtablesearch, dvtablesearchattribute, dvtablesearchentity, email, emailaddressconfiguration, enablearchivalrequest, entityanalyticsconfig, entityclusterconfig, entityimageconfig, entityindex, entityrecordfilter, environmentvariabledefinition, environmentvariablevalue, exportedexcel, exportsolutionupload, fabricaiskill, fax, featurecontrolsetting, federatedknowledgecitation, federatedknowledgeconfiguration, federatedknowledgeentityconfiguration, federatedknowledgemetadatarefresh, feedback, flowcapacityassignment, flowcredentialapplication, flowevent, flowmachine, flowmachinegroup, flowmachineimage, flowmachineimageversion, flowmachinenetwork, flowsession, fxexpression, goal, governanceconfiguration, holidaywrapper, indexattributes, internalcatalogassignment, kbarticle, keyvaultreference, knowledgearticle, knowledgearticleviews, knowledgebaserecord, letter, mailmergetemplate, mainfewshot, makerfewshot, managedidentity, maskingrule, metadataforarchival, mobileofflineprofileextension, msdynce_botcontent, msdyn_aibdataset, msdyn_aibdatasetfile, msdyn_aibdatasetrecord, msdyn_aibdatasetscontainer, msdyn_aibfeedbackloop, msdyn_aibfile, msdyn_aibfileattacheddata, msdyn_aiconfiguration, msdyn_aidataprocessingevent, msdyn_aievaluationconfiguration, msdyn_aievaluationrun, msdyn_aievent, msdyn_aifptrainingdocument, msdyn_aimodel, msdyn_aimodelcatalog, msdyn_aiodimage, msdyn_aiodlabel, msdyn_aiodtrainingboundingbox, msdyn_aiodtrainingimage, msdyn_aitemplate, msdyn_aitestcase, msdyn_aitestcasedocument, msdyn_aitestcaseinput, msdyn_aitestrun, msdyn_aitestrunbatch, msdyn_analysiscomponent, msdyn_analysisjob, msdyn_analysisoverride, msdyn_analysisresult, msdyn_analysisresultdetail, msdyn_appinsightsmetadata, msdyn_copilotinteractions, msdyn_customcontrolextendedsettings, msdyn_dataflow, msdyn_dataflowconnectionreference, msdyn_dataflowrefreshhistory, msdyn_dataflowtemplate, msdyn_dataflow_datalakefolder, msdyn_dataworkspace, msdyn_dmsrequest, msdyn_dmsrequeststatus, msdyn_dmssyncrequest, msdyn_dmssyncstatus, msdyn_entitylinkchatconfiguration, msdyn_entityrefreshhistory, msdyn_favoriteknowledgearticle, msdyn_federatedarticle, msdyn_federatedarticleincident, msdyn_fileupload, msdyn_flow_actionapprovalmodel, msdyn_flow_approval, msdyn_flow_approvalrequest, msdyn_flow_approvalresponse, msdyn_flow_approvalstep, msdyn_flow_awaitallactionapprovalmodel, msdyn_flow_awaitallapprovalmodel, msdyn_flow_basicapprovalmodel, msdyn_flow_flowapproval, msdyn_formmapping, msdyn_function, msdyn_helppage, msdyn_insightsstorevirtualentity, msdyn_integratedsearchprovider, msdyn_kalanguagesetting, msdyn_kbattachment, msdyn_kmfederatedsearchconfig, msdyn_kmpersonalizationsetting, msdyn_knowledgearticleimage, msdyn_knowledgearticletemplate, msdyn_knowledgeassetconfiguration, msdyn_knowledgeconfiguration, msdyn_knowledgeinteractioninsight, msdyn_knowledgemanagementsetting, msdyn_knowledgepersonalfilter, msdyn_knowledgesearchfilter, msdyn_knowledgesearchinsight, msdyn_mobileapp, msdyn_modulerundetail, msdyn_plan, msdyn_planartifact, msdyn_planattachment, msdyn_pmanalysishistory, msdyn_pmbusinessruleautomationconfig, msdyn_pmcalendar, msdyn_pmcalendarversion, msdyn_pminferredtask, msdyn_pmprocessextendedmetadataversion, msdyn_pmprocesstemplate, msdyn_pmprocessusersettings, msdyn_pmprocessversion, msdyn_pmrecording, msdyn_pmsimulation, msdyn_pmtemplate, msdyn_pmview, msdyn_qna, msdyn_richtextfile, msdyn_salesforcestructuredobject, msdyn_salesforcestructuredqnaconfig, msdyn_schedule, msdyn_serviceconfiguration, msdyn_slakpi, msdyn_solutionhealthrule, msdyn_solutionhealthruleargument, msdyn_solutionhealthruleset, msdyn_tour, msdyn_virtualtablecolumncandidate, msdyn_workflowactionstatus, msgraphresourcetosubscription, mspcat_catalogsubmissionfiles, mspcat_packagestore, organizationdatasyncfnostate, organizationdatasyncstate, organizationdatasyncsubscription, organizationdatasyncsubscriptionentity, organizationdatasyncsubscriptionfnotable, organizationsetting, package, packagehistory, pdfsetting, phonecall, plannerbusinessscenario, plannersyncaction, plugin, pluginpackage, position, powerbidataset, powerbidatasetapdx, powerbimashupparameter, powerbireport, powerbireportapdx, powerfxrule, powerpagecomponent, powerpagesite, powerpagesitelanguage, powerpagesitepublished, powerpagesmanagedidentity, powerpagesscanreport, privilegecheckerlog, privilegecheckerrun, privilegesremovalsetting, processorregistration, processstageparameter, provisionlanguageforuser, queue, queueitem, reconciliationentityinfo, reconciliationentitystepinfo, reconciliationinfo, recordfilter, recurringappointmentmaster, recyclebinconfig, relationshipattribute, reportcategory, reportparameter, retaineddataexcel, retentioncleanupinfo, retentioncleanupoperation, retentionconfig, retentionfailuredetail, retentionoperation, retentionoperationdetail, retentionsuccessdetail, revokeinheritedaccessrecordstracker, roleeditorlayout, savingrule, searchattributesettings, searchcustomanalyzer, searchrelationshipsettings, serviceplan, serviceplancustomcontrol, serviceplanmapping, settingdefinition, sharedlinksetting, sharedobject, sharedworkspace, sharedworkspacepool, sharepointdocumentlocation, sharepointmanagedidentity, sharepointsite, sideloadedaiplugin, signalregistration, socialactivity, socialprofile, solutioncomponentattributeconfiguration, solutioncomponentbatchconfiguration, solutioncomponentconfiguration, solutioncomponentrelationshipconfiguration, stagedentity, stagedentityattribute, stagedmetadataasyncoperation, stagesolutionupload, supportusertable, synapsedatabase, synapselinkexternaltablestate, synapselinkprofile, synapselinkprofileentity, synapselinkprofileentitystate, synapselinkschedule, systemuser, systemuserauthorizationchangetracker, tag, taggedflowsession, taggedprocess, task, tdsmetadata, team, teammobileofflineprofilemembership, territory, traitregistration, unstructuredfilesearchentity, unstructuredfilesearchrecord, usermobileofflineprofilemembership, userrating, viewasexamplequestion, virtualentitymetadata, workflowbinary, workflowmetadata, workqueue, workqueueitem|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Type of the record with shared secured field**|
|DisplayName|**Entity object type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_PrincipalId"></a> PrincipalId

|Property|Value|
|---|---|
|Description|**Unique identifier of the principal to which secured field is shared**|
|DisplayName|**Principal**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`principalid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|systemuser, team|

### <a name="BKMK_PrincipalIdType"></a> PrincipalIdType

|Property|Value|
|---|---|
|Description|**Type of the principal to which secured field is shared**|
|DisplayName|**Principal type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`principalidtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_PrincipalObjectAttributeAccessId"></a> PrincipalObjectAttributeAccessId

|Property|Value|
|---|---|
|Description|**Unique identifier of the shared secured field instance**|
|DisplayName|**Shared secured field**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`principalobjectattributeaccessid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ReadAccess"></a> ReadAccess

|Property|Value|
|---|---|
|Description|**Read permission for secured field instance**|
|DisplayName|**Read permission**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`readaccess`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`principalobjectattributeaccess_readaccess`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UpdateAccess"></a> UpdateAccess

|Property|Value|
|---|---|
|Description|**Update permission for secured field instance**|
|DisplayName|**Update permission**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`updateaccess`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`principalobjectattributeaccess_updateaccess`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [OrganizationId](#BKMK_OrganizationId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated organization.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [account_principalobjectattributeaccess](#BKMK_account_principalobjectattributeaccess)
- [activityfileattachment_PrincipalObjectAttributeAccesses](#BKMK_activityfileattachment_PrincipalObjectAttributeAccesses)
- [adx_externalidentity_PrincipalObjectAttributeAccesses](#BKMK_adx_externalidentity_PrincipalObjectAttributeAccesses)
- [adx_invitation_PrincipalObjectAttributeAccesses](#BKMK_adx_invitation_PrincipalObjectAttributeAccesses)
- [adx_inviteredemption_PrincipalObjectAttributeAccesses](#BKMK_adx_inviteredemption_PrincipalObjectAttributeAccesses)
- [adx_portalcomment_PrincipalObjectAttributeAccesses](#BKMK_adx_portalcomment_PrincipalObjectAttributeAccesses)
- [adx_setting_PrincipalObjectAttributeAccesses](#BKMK_adx_setting_PrincipalObjectAttributeAccesses)
- [adx_webformsession_PrincipalObjectAttributeAccesses](#BKMK_adx_webformsession_PrincipalObjectAttributeAccesses)
- [aicopilot_PrincipalObjectAttributeAccesses](#BKMK_aicopilot_PrincipalObjectAttributeAccesses)
- [aiplugin_PrincipalObjectAttributeAccesses](#BKMK_aiplugin_PrincipalObjectAttributeAccesses)
- [aipluginauth_PrincipalObjectAttributeAccesses](#BKMK_aipluginauth_PrincipalObjectAttributeAccesses)
- [aipluginconversationstarter_PrincipalObjectAttributeAccesses](#BKMK_aipluginconversationstarter_PrincipalObjectAttributeAccesses)
- [aipluginconversationstartermapping_PrincipalObjectAttributeAccesses](#BKMK_aipluginconversationstartermapping_PrincipalObjectAttributeAccesses)
- [aipluginexternalschema_PrincipalObjectAttributeAccesses](#BKMK_aipluginexternalschema_PrincipalObjectAttributeAccesses)
- [aipluginexternalschemaproperty_PrincipalObjectAttributeAccesses](#BKMK_aipluginexternalschemaproperty_PrincipalObjectAttributeAccesses)
- [aiplugingovernance_PrincipalObjectAttributeAccesses](#BKMK_aiplugingovernance_PrincipalObjectAttributeAccesses)
- [aiplugingovernanceext_PrincipalObjectAttributeAccesses](#BKMK_aiplugingovernanceext_PrincipalObjectAttributeAccesses)
- [aiplugininstance_PrincipalObjectAttributeAccesses](#BKMK_aiplugininstance_PrincipalObjectAttributeAccesses)
- [aipluginoperation_PrincipalObjectAttributeAccesses](#BKMK_aipluginoperation_PrincipalObjectAttributeAccesses)
- [aipluginoperationparameter_PrincipalObjectAttributeAccesses](#BKMK_aipluginoperationparameter_PrincipalObjectAttributeAccesses)
- [aipluginoperationresponsetemplate_PrincipalObjectAttributeAccesses](#BKMK_aipluginoperationresponsetemplate_PrincipalObjectAttributeAccesses)
- [aiplugintitle_PrincipalObjectAttributeAccesses](#BKMK_aiplugintitle_PrincipalObjectAttributeAccesses)
- [aipluginusersetting_PrincipalObjectAttributeAccesses](#BKMK_aipluginusersetting_PrincipalObjectAttributeAccesses)
- [appaction_PrincipalObjectAttributeAccesses](#BKMK_appaction_PrincipalObjectAttributeAccesses)
- [appactionmigration_PrincipalObjectAttributeAccesses](#BKMK_appactionmigration_PrincipalObjectAttributeAccesses)
- [appactionrule_PrincipalObjectAttributeAccesses](#BKMK_appactionrule_PrincipalObjectAttributeAccesses)
- [application_PrincipalObjectAttributeAccesses](#BKMK_application_PrincipalObjectAttributeAccesses)
- [applicationuser_PrincipalObjectAttributeAccesses](#BKMK_applicationuser_PrincipalObjectAttributeAccesses)
- [appointment_principalobjectattributeaccess](#BKMK_appointment_principalobjectattributeaccess)
- [approvalprocess_PrincipalObjectAttributeAccesses](#BKMK_approvalprocess_PrincipalObjectAttributeAccesses)
- [approvalstageapproval_PrincipalObjectAttributeAccesses](#BKMK_approvalstageapproval_PrincipalObjectAttributeAccesses)
- [approvalstagecondition_PrincipalObjectAttributeAccesses](#BKMK_approvalstagecondition_PrincipalObjectAttributeAccesses)
- [approvalstageorder_PrincipalObjectAttributeAccesses](#BKMK_approvalstageorder_PrincipalObjectAttributeAccesses)
- [attributeimageconfig_PrincipalObjectAttributeAccesses](#BKMK_attributeimageconfig_PrincipalObjectAttributeAccesses)
- [attributemaskingrule_PrincipalObjectAttributeAccesses](#BKMK_attributemaskingrule_PrincipalObjectAttributeAccesses)
- [attributepicklistvalue_PrincipalObjectAttributeAccesses](#BKMK_attributepicklistvalue_PrincipalObjectAttributeAccesses)
- [bot_PrincipalObjectAttributeAccesses](#BKMK_bot_PrincipalObjectAttributeAccesses)
- [botcomponent_PrincipalObjectAttributeAccesses](#BKMK_botcomponent_PrincipalObjectAttributeAccesses)
- [botcomponentcollection_PrincipalObjectAttributeAccesses](#BKMK_botcomponentcollection_PrincipalObjectAttributeAccesses)
- [businessprocess_PrincipalObjectAttributeAccesses](#BKMK_businessprocess_PrincipalObjectAttributeAccesses)
- [businessunit_principalobjectattributeaccess](#BKMK_businessunit_principalobjectattributeaccess)
- [card_PrincipalObjectAttributeAccesses](#BKMK_card_PrincipalObjectAttributeAccesses)
- [catalog_PrincipalObjectAttributeAccesses](#BKMK_catalog_PrincipalObjectAttributeAccesses)
- [catalogassignment_PrincipalObjectAttributeAccesses](#BKMK_catalogassignment_PrincipalObjectAttributeAccesses)
- [certificatecredential_PrincipalObjectAttributeAccesses](#BKMK_certificatecredential_PrincipalObjectAttributeAccesses)
- [chat_PrincipalObjectAttributeAccesses](#BKMK_chat_PrincipalObjectAttributeAccesses)
- [connection_principalobjectattributeaccess](#BKMK_connection_principalobjectattributeaccess)
- [connectioninstance_PrincipalObjectAttributeAccesses](#BKMK_connectioninstance_PrincipalObjectAttributeAccesses)
- [connectionreference_PrincipalObjectAttributeAccesses](#BKMK_connectionreference_PrincipalObjectAttributeAccesses)
- [connector_PrincipalObjectAttributeAccesses](#BKMK_connector_PrincipalObjectAttributeAccesses)
- [contact_principalobjectattributeaccess](#BKMK_contact_principalobjectattributeaccess)
- [conversationtranscript_PrincipalObjectAttributeAccesses](#BKMK_conversationtranscript_PrincipalObjectAttributeAccesses)
- [copilotexamplequestion_PrincipalObjectAttributeAccesses](#BKMK_copilotexamplequestion_PrincipalObjectAttributeAccesses)
- [copilotglossaryterm_PrincipalObjectAttributeAccesses](#BKMK_copilotglossaryterm_PrincipalObjectAttributeAccesses)
- [copilotsynonyms_PrincipalObjectAttributeAccesses](#BKMK_copilotsynonyms_PrincipalObjectAttributeAccesses)
- [credential_PrincipalObjectAttributeAccesses](#BKMK_credential_PrincipalObjectAttributeAccesses)
- [customapi_PrincipalObjectAttributeAccesses](#BKMK_customapi_PrincipalObjectAttributeAccesses)
- [customapirequestparameter_PrincipalObjectAttributeAccesses](#BKMK_customapirequestparameter_PrincipalObjectAttributeAccesses)
- [customapiresponseproperty_PrincipalObjectAttributeAccesses](#BKMK_customapiresponseproperty_PrincipalObjectAttributeAccesses)
- [customeraddress_principalobjectattributeaccess](#BKMK_customeraddress_principalobjectattributeaccess)
- [datalakefolder_PrincipalObjectAttributeAccesses](#BKMK_datalakefolder_PrincipalObjectAttributeAccesses)
- [datalakefolderpermission_PrincipalObjectAttributeAccesses](#BKMK_datalakefolderpermission_PrincipalObjectAttributeAccesses)
- [datalakeworkspace_PrincipalObjectAttributeAccesses](#BKMK_datalakeworkspace_PrincipalObjectAttributeAccesses)
- [datalakeworkspacepermission_PrincipalObjectAttributeAccesses](#BKMK_datalakeworkspacepermission_PrincipalObjectAttributeAccesses)
- [dataprocessingconfiguration_PrincipalObjectAttributeAccesses](#BKMK_dataprocessingconfiguration_PrincipalObjectAttributeAccesses)
- [delegatedauthorization_PrincipalObjectAttributeAccesses](#BKMK_delegatedauthorization_PrincipalObjectAttributeAccesses)
- [desktopflowbinary_PrincipalObjectAttributeAccesses](#BKMK_desktopflowbinary_PrincipalObjectAttributeAccesses)
- [desktopflowmodule_PrincipalObjectAttributeAccesses](#BKMK_desktopflowmodule_PrincipalObjectAttributeAccesses)
- [dvfilesearch_PrincipalObjectAttributeAccesses](#BKMK_dvfilesearch_PrincipalObjectAttributeAccesses)
- [dvfilesearchattribute_PrincipalObjectAttributeAccesses](#BKMK_dvfilesearchattribute_PrincipalObjectAttributeAccesses)
- [dvfilesearchentity_PrincipalObjectAttributeAccesses](#BKMK_dvfilesearchentity_PrincipalObjectAttributeAccesses)
- [dvtablesearch_PrincipalObjectAttributeAccesses](#BKMK_dvtablesearch_PrincipalObjectAttributeAccesses)
- [dvtablesearchattribute_PrincipalObjectAttributeAccesses](#BKMK_dvtablesearchattribute_PrincipalObjectAttributeAccesses)
- [dvtablesearchentity_PrincipalObjectAttributeAccesses](#BKMK_dvtablesearchentity_PrincipalObjectAttributeAccesses)
- [email_principalobjectattributeaccess](#BKMK_email_principalobjectattributeaccess)
- [emailaddressconfiguration_PrincipalObjectAttributeAccesses](#BKMK_emailaddressconfiguration_PrincipalObjectAttributeAccesses)
- [entityanalyticsconfig_PrincipalObjectAttributeAccesses](#BKMK_entityanalyticsconfig_PrincipalObjectAttributeAccesses)
- [entityclusterconfig_PrincipalObjectAttributeAccesses](#BKMK_entityclusterconfig_PrincipalObjectAttributeAccesses)
- [entityimageconfig_PrincipalObjectAttributeAccesses](#BKMK_entityimageconfig_PrincipalObjectAttributeAccesses)
- [entityindex_PrincipalObjectAttributeAccesses](#BKMK_entityindex_PrincipalObjectAttributeAccesses)
- [entityrecordfilter_PrincipalObjectAttributeAccesses](#BKMK_entityrecordfilter_PrincipalObjectAttributeAccesses)
- [environmentvariabledefinition_PrincipalObjectAttributeAccesses](#BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses)
- [environmentvariablevalue_PrincipalObjectAttributeAccesses](#BKMK_environmentvariablevalue_PrincipalObjectAttributeAccesses)
- [exportedexcel_PrincipalObjectAttributeAccesses](#BKMK_exportedexcel_PrincipalObjectAttributeAccesses)
- [exportsolutionupload_PrincipalObjectAttributeAccesses](#BKMK_exportsolutionupload_PrincipalObjectAttributeAccesses)
- [fabricaiskill_PrincipalObjectAttributeAccesses](#BKMK_fabricaiskill_PrincipalObjectAttributeAccesses)
- [fax_principalobjectattributeaccess](#BKMK_fax_principalobjectattributeaccess)
- [featurecontrolsetting_PrincipalObjectAttributeAccesses](#BKMK_featurecontrolsetting_PrincipalObjectAttributeAccesses)
- [federatedknowledgeconfiguration_PrincipalObjectAttributeAccesses](#BKMK_federatedknowledgeconfiguration_PrincipalObjectAttributeAccesses)
- [federatedknowledgeentityconfiguration_PrincipalObjectAttributeAccesses](#BKMK_federatedknowledgeentityconfiguration_PrincipalObjectAttributeAccesses)
- [feedback_principalobjectattributeaccess](#BKMK_feedback_principalobjectattributeaccess)
- [flowcapacityassignment_PrincipalObjectAttributeAccesses](#BKMK_flowcapacityassignment_PrincipalObjectAttributeAccesses)
- [flowcredentialapplication_PrincipalObjectAttributeAccesses](#BKMK_flowcredentialapplication_PrincipalObjectAttributeAccesses)
- [flowevent_PrincipalObjectAttributeAccesses](#BKMK_flowevent_PrincipalObjectAttributeAccesses)
- [flowmachine_PrincipalObjectAttributeAccesses](#BKMK_flowmachine_PrincipalObjectAttributeAccesses)
- [flowmachinegroup_PrincipalObjectAttributeAccesses](#BKMK_flowmachinegroup_PrincipalObjectAttributeAccesses)
- [flowmachineimage_PrincipalObjectAttributeAccesses](#BKMK_flowmachineimage_PrincipalObjectAttributeAccesses)
- [flowmachineimageversion_PrincipalObjectAttributeAccesses](#BKMK_flowmachineimageversion_PrincipalObjectAttributeAccesses)
- [flowmachinenetwork_PrincipalObjectAttributeAccesses](#BKMK_flowmachinenetwork_PrincipalObjectAttributeAccesses)
- [flowsession_PrincipalObjectAttributeAccesses](#BKMK_flowsession_PrincipalObjectAttributeAccesses)
- [fxexpression_PrincipalObjectAttributeAccesses](#BKMK_fxexpression_PrincipalObjectAttributeAccesses)
- [goal_principalobjectattributeaccess](#BKMK_goal_principalobjectattributeaccess)
- [governanceconfiguration_PrincipalObjectAttributeAccesses](#BKMK_governanceconfiguration_PrincipalObjectAttributeAccesses)
- [indexattributes_PrincipalObjectAttributeAccesses](#BKMK_indexattributes_PrincipalObjectAttributeAccesses)
- [kbarticle_principalobjectattributeaccess](#BKMK_kbarticle_principalobjectattributeaccess)
- [keyvaultreference_PrincipalObjectAttributeAccesses](#BKMK_keyvaultreference_PrincipalObjectAttributeAccesses)
- [knowledgearticle_PrincipalObjectAttributeAccess](#BKMK_knowledgearticle_PrincipalObjectAttributeAccess)
- [knowledgearticleview_principalobjectattributeaccess](#BKMK_knowledgearticleview_principalobjectattributeaccess)
- [KnowledgeBaseRecord_PrincipalObjectAttributeAccess](#BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess)
- [letter_principalobjectattributeaccess](#BKMK_letter_principalobjectattributeaccess)
- [lk_principalobjectattributeaccess_organizationid](#BKMK_lk_principalobjectattributeaccess_organizationid)
- [mailmergetemplate_principalobjectattributeaccess](#BKMK_mailmergetemplate_principalobjectattributeaccess)
- [mainfewshot_PrincipalObjectAttributeAccesses](#BKMK_mainfewshot_PrincipalObjectAttributeAccesses)
- [makerfewshot_PrincipalObjectAttributeAccesses](#BKMK_makerfewshot_PrincipalObjectAttributeAccesses)
- [managedidentity_PrincipalObjectAttributeAccesses](#BKMK_managedidentity_PrincipalObjectAttributeAccesses)
- [maskingrule_PrincipalObjectAttributeAccesses](#BKMK_maskingrule_PrincipalObjectAttributeAccesses)
- [metadataforarchival_PrincipalObjectAttributeAccesses](#BKMK_metadataforarchival_PrincipalObjectAttributeAccesses)
- [mobileofflineprofileextension_PrincipalObjectAttributeAccesses](#BKMK_mobileofflineprofileextension_PrincipalObjectAttributeAccesses)
- [msdyn_aibdataset_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibdataset_PrincipalObjectAttributeAccesses)
- [msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses)
- [msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses)
- [msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses)
- [msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses)
- [msdyn_aibfile_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibfile_PrincipalObjectAttributeAccesses)
- [msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses)
- [msdyn_aiconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses)
- [msdyn_aievaluationconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aievaluationconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_aievaluationrun_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aievaluationrun_PrincipalObjectAttributeAccesses)
- [msdyn_aievent_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aievent_PrincipalObjectAttributeAccesses)
- [msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses)
- [msdyn_aimodel_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aimodel_PrincipalObjectAttributeAccesses)
- [msdyn_aimodelcatalog_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aimodelcatalog_PrincipalObjectAttributeAccesses)
- [msdyn_aiodimage_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiodimage_PrincipalObjectAttributeAccesses)
- [msdyn_aiodlabel_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiodlabel_PrincipalObjectAttributeAccesses)
- [msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses)
- [msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses)
- [msdyn_aitemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aitemplate_PrincipalObjectAttributeAccesses)
- [msdyn_aitestcase_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aitestcase_PrincipalObjectAttributeAccesses)
- [msdyn_aitestcasedocument_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aitestcasedocument_PrincipalObjectAttributeAccesses)
- [msdyn_aitestcaseinput_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aitestcaseinput_PrincipalObjectAttributeAccesses)
- [msdyn_aitestrun_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aitestrun_PrincipalObjectAttributeAccesses)
- [msdyn_aitestrunbatch_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aitestrunbatch_PrincipalObjectAttributeAccesses)
- [msdyn_analysiscomponent_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses)
- [msdyn_analysisjob_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses)
- [msdyn_analysisoverride_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysisoverride_PrincipalObjectAttributeAccesses)
- [msdyn_analysisresult_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysisresult_PrincipalObjectAttributeAccesses)
- [msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses)
- [msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses](#BKMK_msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses)
- [msdyn_copilotinteractions_PrincipalObjectAttributeAccesses](#BKMK_msdyn_copilotinteractions_PrincipalObjectAttributeAccesses)
- [msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses](#BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses)
- [msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses)
- [msdyn_dataflow_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dataflow_PrincipalObjectAttributeAccesses)
- [msdyn_dataflowconnectionreference_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dataflowconnectionreference_PrincipalObjectAttributeAccesses)
- [msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses)
- [msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses)
- [msdyn_dmsrequest_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dmsrequest_PrincipalObjectAttributeAccesses)
- [msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses)
- [msdyn_dmssyncrequest_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dmssyncrequest_PrincipalObjectAttributeAccesses)
- [msdyn_dmssyncstatus_PrincipalObjectAttributeAccesses](#BKMK_msdyn_dmssyncstatus_PrincipalObjectAttributeAccesses)
- [msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses](#BKMK_msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses)
- [msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses](#BKMK_msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses)
- [msdyn_federatedarticle_PrincipalObjectAttributeAccesses](#BKMK_msdyn_federatedarticle_PrincipalObjectAttributeAccesses)
- [msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses](#BKMK_msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses)
- [msdyn_fileupload_PrincipalObjectAttributeAccesses](#BKMK_msdyn_fileupload_PrincipalObjectAttributeAccesses)
- [msdyn_flow_actionapprovalmodel_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_actionapprovalmodel_PrincipalObjectAttributeAccesses)
- [msdyn_flow_approval_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_approval_PrincipalObjectAttributeAccesses)
- [msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses)
- [msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses)
- [msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses)
- [msdyn_flow_awaitallactionapprovalmodel_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_awaitallactionapprovalmodel_PrincipalObjectAttributeAccesses)
- [msdyn_flow_awaitallapprovalmodel_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_awaitallapprovalmodel_PrincipalObjectAttributeAccesses)
- [msdyn_flow_basicapprovalmodel_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_basicapprovalmodel_PrincipalObjectAttributeAccesses)
- [msdyn_flow_flowapproval_PrincipalObjectAttributeAccesses](#BKMK_msdyn_flow_flowapproval_PrincipalObjectAttributeAccesses)
- [msdyn_formmapping_PrincipalObjectAttributeAccesses](#BKMK_msdyn_formmapping_PrincipalObjectAttributeAccesses)
- [msdyn_function_PrincipalObjectAttributeAccesses](#BKMK_msdyn_function_PrincipalObjectAttributeAccesses)
- [msdyn_helppage_PrincipalObjectAttributeAccesses](#BKMK_msdyn_helppage_PrincipalObjectAttributeAccesses)
- [msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses](#BKMK_msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses)
- [msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses](#BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses)
- [msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses](#BKMK_msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses)
- [msdyn_kbattachment_PrincipalObjectAttributeAccesses](#BKMK_msdyn_kbattachment_PrincipalObjectAttributeAccesses)
- [msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses](#BKMK_msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses)
- [msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses](#BKMK_msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgeassetconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgeassetconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses)
- [msdyn_mobileapp_PrincipalObjectAttributeAccesses](#BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses)
- [msdyn_modulerundetail_PrincipalObjectAttributeAccesses](#BKMK_msdyn_modulerundetail_PrincipalObjectAttributeAccesses)
- [msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses)
- [msdyn_pmbusinessruleautomationconfig_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmbusinessruleautomationconfig_PrincipalObjectAttributeAccesses)
- [msdyn_pmcalendar_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmcalendar_PrincipalObjectAttributeAccesses)
- [msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses)
- [msdyn_pminferredtask_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pminferredtask_PrincipalObjectAttributeAccesses)
- [msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses)
- [msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses)
- [msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses)
- [msdyn_pmprocessversion_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmprocessversion_PrincipalObjectAttributeAccesses)
- [msdyn_pmrecording_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmrecording_PrincipalObjectAttributeAccesses)
- [msdyn_pmsimulation_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmsimulation_PrincipalObjectAttributeAccesses)
- [msdyn_pmtemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmtemplate_PrincipalObjectAttributeAccesses)
- [msdyn_pmview_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pmview_PrincipalObjectAttributeAccesses)
- [msdyn_qna_PrincipalObjectAttributeAccesses](#BKMK_msdyn_qna_PrincipalObjectAttributeAccesses)
- [msdyn_richtextfile_PrincipalObjectAttributeAccesses](#BKMK_msdyn_richtextfile_PrincipalObjectAttributeAccesses)
- [msdyn_salesforcestructuredobject_PrincipalObjectAttributeAccesses](#BKMK_msdyn_salesforcestructuredobject_PrincipalObjectAttributeAccesses)
- [msdyn_salesforcestructuredqnaconfig_PrincipalObjectAttributeAccesses](#BKMK_msdyn_salesforcestructuredqnaconfig_PrincipalObjectAttributeAccesses)
- [msdyn_schedule_PrincipalObjectAttributeAccesses](#BKMK_msdyn_schedule_PrincipalObjectAttributeAccesses)
- [msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_slakpi_PrincipalObjectAttributeAccesses](#BKMK_msdyn_slakpi_PrincipalObjectAttributeAccesses)
- [msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses](#BKMK_msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses)
- [msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses](#BKMK_msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses)
- [msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses](#BKMK_msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses)
- [msdyn_tour_PrincipalObjectAttributeAccesses](#BKMK_msdyn_tour_PrincipalObjectAttributeAccesses)
- [msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses)
- [msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses](#BKMK_msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses)
- [msdynce_botcontent_PrincipalObjectAttributeAccesses](#BKMK_msdynce_botcontent_PrincipalObjectAttributeAccesses)
- [msgraphresourcetosubscription_PrincipalObjectAttributeAccesses](#BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses)
- [mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses](#BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses)
- [mspcat_packagestore_PrincipalObjectAttributeAccesses](#BKMK_mspcat_packagestore_PrincipalObjectAttributeAccesses)
- [organizationdatasyncfnostate_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncfnostate_PrincipalObjectAttributeAccesses)
- [organizationdatasyncstate_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses)
- [organizationdatasyncsubscription_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses)
- [organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses)
- [organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses](#BKMK_organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses)
- [package_PrincipalObjectAttributeAccesses](#BKMK_package_PrincipalObjectAttributeAccesses)
- [packagehistory_PrincipalObjectAttributeAccesses](#BKMK_packagehistory_PrincipalObjectAttributeAccesses)
- [phonecall_principalobjectattributeaccess](#BKMK_phonecall_principalobjectattributeaccess)
- [plannerbusinessscenario_PrincipalObjectAttributeAccesses](#BKMK_plannerbusinessscenario_PrincipalObjectAttributeAccesses)
- [plannersyncaction_PrincipalObjectAttributeAccesses](#BKMK_plannersyncaction_PrincipalObjectAttributeAccesses)
- [plugin_PrincipalObjectAttributeAccesses](#BKMK_plugin_PrincipalObjectAttributeAccesses)
- [pluginpackage_PrincipalObjectAttributeAccesses](#BKMK_pluginpackage_PrincipalObjectAttributeAccesses)
- [position_principalobjectattributeaccess](#BKMK_position_principalobjectattributeaccess)
- [powerbidataset_PrincipalObjectAttributeAccesses](#BKMK_powerbidataset_PrincipalObjectAttributeAccesses)
- [powerbidatasetapdx_PrincipalObjectAttributeAccesses](#BKMK_powerbidatasetapdx_PrincipalObjectAttributeAccesses)
- [powerbimashupparameter_PrincipalObjectAttributeAccesses](#BKMK_powerbimashupparameter_PrincipalObjectAttributeAccesses)
- [powerbireport_PrincipalObjectAttributeAccesses](#BKMK_powerbireport_PrincipalObjectAttributeAccesses)
- [powerbireportapdx_PrincipalObjectAttributeAccesses](#BKMK_powerbireportapdx_PrincipalObjectAttributeAccesses)
- [powerfxrule_PrincipalObjectAttributeAccesses](#BKMK_powerfxrule_PrincipalObjectAttributeAccesses)
- [powerpagecomponent_PrincipalObjectAttributeAccesses](#BKMK_powerpagecomponent_PrincipalObjectAttributeAccesses)
- [powerpagesite_PrincipalObjectAttributeAccesses](#BKMK_powerpagesite_PrincipalObjectAttributeAccesses)
- [powerpagesitelanguage_PrincipalObjectAttributeAccesses](#BKMK_powerpagesitelanguage_PrincipalObjectAttributeAccesses)
- [powerpagesitepublished_PrincipalObjectAttributeAccesses](#BKMK_powerpagesitepublished_PrincipalObjectAttributeAccesses)
- [powerpagesmanagedidentity_PrincipalObjectAttributeAccesses](#BKMK_powerpagesmanagedidentity_PrincipalObjectAttributeAccesses)
- [powerpagesscanreport_PrincipalObjectAttributeAccesses](#BKMK_powerpagesscanreport_PrincipalObjectAttributeAccesses)
- [privilegecheckerlog_PrincipalObjectAttributeAccesses](#BKMK_privilegecheckerlog_PrincipalObjectAttributeAccesses)
- [privilegecheckerrun_PrincipalObjectAttributeAccesses](#BKMK_privilegecheckerrun_PrincipalObjectAttributeAccesses)
- [privilegesremovalsetting_PrincipalObjectAttributeAccesses](#BKMK_privilegesremovalsetting_PrincipalObjectAttributeAccesses)
- [processstageparameter_PrincipalObjectAttributeAccesses](#BKMK_processstageparameter_PrincipalObjectAttributeAccesses)
- [provisionlanguageforuser_PrincipalObjectAttributeAccesses](#BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses)
- [queue_principalobjectattributeaccess](#BKMK_queue_principalobjectattributeaccess)
- [queueitem_principalobjectattributeaccess](#BKMK_queueitem_principalobjectattributeaccess)
- [recordfilter_PrincipalObjectAttributeAccesses](#BKMK_recordfilter_PrincipalObjectAttributeAccesses)
- [recurringappointmentmaster_principalobjectattributeaccess](#BKMK_recurringappointmentmaster_principalobjectattributeaccess)
- [recyclebinconfig_PrincipalObjectAttributeAccesses](#BKMK_recyclebinconfig_PrincipalObjectAttributeAccesses)
- [relationshipattribute_PrincipalObjectAttributeAccesses](#BKMK_relationshipattribute_PrincipalObjectAttributeAccesses)
- [reportcategory_principalobjectattributeaccess](#BKMK_reportcategory_principalobjectattributeaccess)
- [reportparameter_PrincipalObjectAttributeAccesses](#BKMK_reportparameter_PrincipalObjectAttributeAccesses)
- [retaineddataexcel_PrincipalObjectAttributeAccesses](#BKMK_retaineddataexcel_PrincipalObjectAttributeAccesses)
- [retentionconfig_PrincipalObjectAttributeAccesses](#BKMK_retentionconfig_PrincipalObjectAttributeAccesses)
- [retentionfailuredetail_PrincipalObjectAttributeAccesses](#BKMK_retentionfailuredetail_PrincipalObjectAttributeAccesses)
- [retentionoperation_PrincipalObjectAttributeAccesses](#BKMK_retentionoperation_PrincipalObjectAttributeAccesses)
- [retentionoperationdetail_PrincipalObjectAttributeAccesses](#BKMK_retentionoperationdetail_PrincipalObjectAttributeAccesses)
- [retentionsuccessdetail_PrincipalObjectAttributeAccesses](#BKMK_retentionsuccessdetail_PrincipalObjectAttributeAccesses)
- [roleeditorlayout_PrincipalObjectAttributeAccesses](#BKMK_roleeditorlayout_PrincipalObjectAttributeAccesses)
- [savingrule_PrincipalObjectAttributeAccesses](#BKMK_savingrule_PrincipalObjectAttributeAccesses)
- [searchattributesettings_PrincipalObjectAttributeAccesses](#BKMK_searchattributesettings_PrincipalObjectAttributeAccesses)
- [searchcustomanalyzer_PrincipalObjectAttributeAccesses](#BKMK_searchcustomanalyzer_PrincipalObjectAttributeAccesses)
- [searchrelationshipsettings_PrincipalObjectAttributeAccesses](#BKMK_searchrelationshipsettings_PrincipalObjectAttributeAccesses)
- [serviceplan_PrincipalObjectAttributeAccesses](#BKMK_serviceplan_PrincipalObjectAttributeAccesses)
- [serviceplanmapping_PrincipalObjectAttributeAccesses](#BKMK_serviceplanmapping_PrincipalObjectAttributeAccesses)
- [sharedlinksetting_PrincipalObjectAttributeAccesses](#BKMK_sharedlinksetting_PrincipalObjectAttributeAccesses)
- [sharedobject_PrincipalObjectAttributeAccesses](#BKMK_sharedobject_PrincipalObjectAttributeAccesses)
- [sharedworkspace_PrincipalObjectAttributeAccesses](#BKMK_sharedworkspace_PrincipalObjectAttributeAccesses)
- [sharedworkspacepool_PrincipalObjectAttributeAccesses](#BKMK_sharedworkspacepool_PrincipalObjectAttributeAccesses)
- [sharepointdocumentlocation_principalobjectattributeaccess](#BKMK_sharepointdocumentlocation_principalobjectattributeaccess)
- [sharepointmanagedidentity_PrincipalObjectAttributeAccesses](#BKMK_sharepointmanagedidentity_PrincipalObjectAttributeAccesses)
- [sharepointsite_principalobjectattributeaccess](#BKMK_sharepointsite_principalobjectattributeaccess)
- [sideloadedaiplugin_PrincipalObjectAttributeAccesses](#BKMK_sideloadedaiplugin_PrincipalObjectAttributeAccesses)
- [socialactivity_principalobjectattributeaccess](#BKMK_socialactivity_principalobjectattributeaccess)
- [socialprofile_principalobjectattributeaccess](#BKMK_socialprofile_principalobjectattributeaccess)
- [solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses)
- [solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses)
- [solutioncomponentconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses)
- [solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses)
- [stagedentity_PrincipalObjectAttributeAccesses](#BKMK_stagedentity_PrincipalObjectAttributeAccesses)
- [stagedentityattribute_PrincipalObjectAttributeAccesses](#BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses)
- [stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses](#BKMK_stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses)
- [stagesolutionupload_PrincipalObjectAttributeAccesses](#BKMK_stagesolutionupload_PrincipalObjectAttributeAccesses)
- [supportusertable_PrincipalObjectAttributeAccesses](#BKMK_supportusertable_PrincipalObjectAttributeAccesses)
- [synapsedatabase_PrincipalObjectAttributeAccesses](#BKMK_synapsedatabase_PrincipalObjectAttributeAccesses)
- [synapselinkexternaltablestate_PrincipalObjectAttributeAccesses](#BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses)
- [synapselinkprofile_PrincipalObjectAttributeAccesses](#BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses)
- [synapselinkprofileentity_PrincipalObjectAttributeAccesses](#BKMK_synapselinkprofileentity_PrincipalObjectAttributeAccesses)
- [synapselinkprofileentitystate_PrincipalObjectAttributeAccesses](#BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses)
- [synapselinkschedule_PrincipalObjectAttributeAccesses](#BKMK_synapselinkschedule_PrincipalObjectAttributeAccesses)
- [systemuser_principalobjectattributeaccess](#BKMK_systemuser_principalobjectattributeaccess)
- [systemuser_principalobjectattributeaccess_principalid](#BKMK_systemuser_principalobjectattributeaccess_principalid)
- [systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses](#BKMK_systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses)
- [tag_PrincipalObjectAttributeAccesses](#BKMK_tag_PrincipalObjectAttributeAccesses)
- [taggedflowsession_PrincipalObjectAttributeAccesses](#BKMK_taggedflowsession_PrincipalObjectAttributeAccesses)
- [taggedprocess_PrincipalObjectAttributeAccesses](#BKMK_taggedprocess_PrincipalObjectAttributeAccesses)
- [task_principalobjectattributeaccess](#BKMK_task_principalobjectattributeaccess)
- [team_principalobjectattributeaccess](#BKMK_team_principalobjectattributeaccess)
- [team_principalobjectattributeaccess_principalid](#BKMK_team_principalobjectattributeaccess_principalid)
- [teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses](#BKMK_teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses)
- [territory_principalobjectattributeaccess](#BKMK_territory_principalobjectattributeaccess)
- [unstructuredfilesearchentity_PrincipalObjectAttributeAccesses](#BKMK_unstructuredfilesearchentity_PrincipalObjectAttributeAccesses)
- [unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses](#BKMK_unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses)
- [usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses](#BKMK_usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses)
- [userrating_PrincipalObjectAttributeAccesses](#BKMK_userrating_PrincipalObjectAttributeAccesses)
- [viewasexamplequestion_PrincipalObjectAttributeAccesses](#BKMK_viewasexamplequestion_PrincipalObjectAttributeAccesses)
- [virtualentitymetadata_PrincipalObjectAttributeAccesses](#BKMK_virtualentitymetadata_PrincipalObjectAttributeAccesses)
- [workflowbinary_PrincipalObjectAttributeAccesses](#BKMK_workflowbinary_PrincipalObjectAttributeAccesses)
- [workflowmetadata_PrincipalObjectAttributeAccesses](#BKMK_workflowmetadata_PrincipalObjectAttributeAccesses)
- [workqueue_PrincipalObjectAttributeAccesses](#BKMK_workqueue_PrincipalObjectAttributeAccesses)
- [workqueueitem_PrincipalObjectAttributeAccesses](#BKMK_workqueueitem_PrincipalObjectAttributeAccesses)

### <a name="BKMK_account_principalobjectattributeaccess"></a> account_principalobjectattributeaccess

One-To-Many Relationship: [account account_principalobjectattributeaccess](account.md#BKMK_account_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activityfileattachment_PrincipalObjectAttributeAccesses"></a> activityfileattachment_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [activityfileattachment activityfileattachment_PrincipalObjectAttributeAccesses](activityfileattachment.md#BKMK_activityfileattachment_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`activityfileattachment`|
|ReferencedAttribute|`activityfileattachmentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_activityfileattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_externalidentity_PrincipalObjectAttributeAccesses"></a> adx_externalidentity_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [adx_externalidentity adx_externalidentity_PrincipalObjectAttributeAccesses](adx_externalidentity.md#BKMK_adx_externalidentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_externalidentity`|
|ReferencedAttribute|`adx_externalidentityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_adx_externalidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_PrincipalObjectAttributeAccesses"></a> adx_invitation_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [adx_invitation adx_invitation_PrincipalObjectAttributeAccesses](adx_invitation.md#BKMK_adx_invitation_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_invitation`|
|ReferencedAttribute|`adx_invitationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_adx_invitation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_inviteredemption_PrincipalObjectAttributeAccesses"></a> adx_inviteredemption_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [adx_inviteredemption adx_inviteredemption_PrincipalObjectAttributeAccesses](adx_inviteredemption.md#BKMK_adx_inviteredemption_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_inviteredemption`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_adx_inviteredemption`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_portalcomment_PrincipalObjectAttributeAccesses"></a> adx_portalcomment_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [adx_portalcomment adx_portalcomment_PrincipalObjectAttributeAccesses](adx_portalcomment.md#BKMK_adx_portalcomment_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_portalcomment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_adx_portalcomment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_setting_PrincipalObjectAttributeAccesses"></a> adx_setting_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [adx_setting adx_setting_PrincipalObjectAttributeAccesses](adx_setting.md#BKMK_adx_setting_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_setting`|
|ReferencedAttribute|`adx_settingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_adx_setting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_webformsession_PrincipalObjectAttributeAccesses"></a> adx_webformsession_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [adx_webformsession adx_webformsession_PrincipalObjectAttributeAccesses](adx_webformsession.md#BKMK_adx_webformsession_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`adx_webformsession`|
|ReferencedAttribute|`adx_webformsessionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_adx_webformsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aicopilot_PrincipalObjectAttributeAccesses"></a> aicopilot_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aicopilot aicopilot_PrincipalObjectAttributeAccesses](aicopilot.md#BKMK_aicopilot_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aicopilot`|
|ReferencedAttribute|`aicopilotid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aicopilot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugin_PrincipalObjectAttributeAccesses"></a> aiplugin_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aiplugin aiplugin_PrincipalObjectAttributeAccesses](aiplugin.md#BKMK_aiplugin_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugin`|
|ReferencedAttribute|`aipluginid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginauth_PrincipalObjectAttributeAccesses"></a> aipluginauth_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aipluginauth aipluginauth_PrincipalObjectAttributeAccesses](aipluginauth.md#BKMK_aipluginauth_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginauth`|
|ReferencedAttribute|`aipluginauthid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aipluginauth`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstarter_PrincipalObjectAttributeAccesses"></a> aipluginconversationstarter_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aipluginconversationstarter aipluginconversationstarter_PrincipalObjectAttributeAccesses](aipluginconversationstarter.md#BKMK_aipluginconversationstarter_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstarter`|
|ReferencedAttribute|`aipluginconversationstarterid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aipluginconversationstarter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginconversationstartermapping_PrincipalObjectAttributeAccesses"></a> aipluginconversationstartermapping_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aipluginconversationstartermapping aipluginconversationstartermapping_PrincipalObjectAttributeAccesses](aipluginconversationstartermapping.md#BKMK_aipluginconversationstartermapping_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginconversationstartermapping`|
|ReferencedAttribute|`aipluginconversationstartermappingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aipluginconversationstartermapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschema_PrincipalObjectAttributeAccesses"></a> aipluginexternalschema_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aipluginexternalschema aipluginexternalschema_PrincipalObjectAttributeAccesses](aipluginexternalschema.md#BKMK_aipluginexternalschema_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschema`|
|ReferencedAttribute|`aipluginexternalschemaid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aipluginexternalschema`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginexternalschemaproperty_PrincipalObjectAttributeAccesses"></a> aipluginexternalschemaproperty_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aipluginexternalschemaproperty aipluginexternalschemaproperty_PrincipalObjectAttributeAccesses](aipluginexternalschemaproperty.md#BKMK_aipluginexternalschemaproperty_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginexternalschemaproperty`|
|ReferencedAttribute|`aipluginexternalschemapropertyid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aipluginexternalschemaproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernance_PrincipalObjectAttributeAccesses"></a> aiplugingovernance_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aiplugingovernance aiplugingovernance_PrincipalObjectAttributeAccesses](aiplugingovernance.md#BKMK_aiplugingovernance_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernance`|
|ReferencedAttribute|`aiplugingovernanceid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aiplugingovernance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugingovernanceext_PrincipalObjectAttributeAccesses"></a> aiplugingovernanceext_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aiplugingovernanceext aiplugingovernanceext_PrincipalObjectAttributeAccesses](aiplugingovernanceext.md#BKMK_aiplugingovernanceext_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugingovernanceext`|
|ReferencedAttribute|`aiplugingovernanceextid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aiplugingovernanceext`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugininstance_PrincipalObjectAttributeAccesses"></a> aiplugininstance_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aiplugininstance aiplugininstance_PrincipalObjectAttributeAccesses](aiplugininstance.md#BKMK_aiplugininstance_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugininstance`|
|ReferencedAttribute|`aiplugininstanceid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aiplugininstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperation_PrincipalObjectAttributeAccesses"></a> aipluginoperation_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aipluginoperation aipluginoperation_PrincipalObjectAttributeAccesses](aipluginoperation.md#BKMK_aipluginoperation_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperation`|
|ReferencedAttribute|`aipluginoperationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aipluginoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationparameter_PrincipalObjectAttributeAccesses"></a> aipluginoperationparameter_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aipluginoperationparameter aipluginoperationparameter_PrincipalObjectAttributeAccesses](aipluginoperationparameter.md#BKMK_aipluginoperationparameter_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationparameter`|
|ReferencedAttribute|`aipluginoperationparameterid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aipluginoperationparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginoperationresponsetemplate_PrincipalObjectAttributeAccesses"></a> aipluginoperationresponsetemplate_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aipluginoperationresponsetemplate aipluginoperationresponsetemplate_PrincipalObjectAttributeAccesses](aipluginoperationresponsetemplate.md#BKMK_aipluginoperationresponsetemplate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginoperationresponsetemplate`|
|ReferencedAttribute|`aipluginoperationresponsetemplateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aipluginoperationresponsetemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aiplugintitle_PrincipalObjectAttributeAccesses"></a> aiplugintitle_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aiplugintitle aiplugintitle_PrincipalObjectAttributeAccesses](aiplugintitle.md#BKMK_aiplugintitle_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aiplugintitle`|
|ReferencedAttribute|`aiplugintitleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aiplugintitle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_aipluginusersetting_PrincipalObjectAttributeAccesses"></a> aipluginusersetting_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [aipluginusersetting aipluginusersetting_PrincipalObjectAttributeAccesses](aipluginusersetting.md#BKMK_aipluginusersetting_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`aipluginusersetting`|
|ReferencedAttribute|`aipluginusersettingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_aipluginusersetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appaction_PrincipalObjectAttributeAccesses"></a> appaction_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [appaction appaction_PrincipalObjectAttributeAccesses](appaction.md#BKMK_appaction_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`appaction`|
|ReferencedAttribute|`appactionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_appaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionmigration_PrincipalObjectAttributeAccesses"></a> appactionmigration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [appactionmigration appactionmigration_PrincipalObjectAttributeAccesses](appactionmigration.md#BKMK_appactionmigration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionmigration`|
|ReferencedAttribute|`appactionmigrationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_appactionmigration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appactionrule_PrincipalObjectAttributeAccesses"></a> appactionrule_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [appactionrule appactionrule_PrincipalObjectAttributeAccesses](appactionrule.md#BKMK_appactionrule_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`appactionrule`|
|ReferencedAttribute|`appactionruleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_appactionrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_application_PrincipalObjectAttributeAccesses"></a> application_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [application application_PrincipalObjectAttributeAccesses](application.md#BKMK_application_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`application`|
|ReferencedAttribute|`applicationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_application`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_applicationuser_PrincipalObjectAttributeAccesses"></a> applicationuser_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [applicationuser applicationuser_PrincipalObjectAttributeAccesses](applicationuser.md#BKMK_applicationuser_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`applicationuser`|
|ReferencedAttribute|`applicationuserid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_applicationuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appointment_principalobjectattributeaccess"></a> appointment_principalobjectattributeaccess

One-To-Many Relationship: [appointment appointment_principalobjectattributeaccess](appointment.md#BKMK_appointment_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalprocess_PrincipalObjectAttributeAccesses"></a> approvalprocess_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [approvalprocess approvalprocess_PrincipalObjectAttributeAccesses](approvalprocess.md#BKMK_approvalprocess_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalprocess`|
|ReferencedAttribute|`approvalprocessid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_approvalprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageapproval_PrincipalObjectAttributeAccesses"></a> approvalstageapproval_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [approvalstageapproval approvalstageapproval_PrincipalObjectAttributeAccesses](approvalstageapproval.md#BKMK_approvalstageapproval_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageapproval`|
|ReferencedAttribute|`approvalstageapprovalid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_approvalstageapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstagecondition_PrincipalObjectAttributeAccesses"></a> approvalstagecondition_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [approvalstagecondition approvalstagecondition_PrincipalObjectAttributeAccesses](approvalstagecondition.md#BKMK_approvalstagecondition_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstagecondition`|
|ReferencedAttribute|`approvalstageconditionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_approvalstagecondition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_approvalstageorder_PrincipalObjectAttributeAccesses"></a> approvalstageorder_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [approvalstageorder approvalstageorder_PrincipalObjectAttributeAccesses](approvalstageorder.md#BKMK_approvalstageorder_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`approvalstageorder`|
|ReferencedAttribute|`approvalstageorderid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_approvalstageorder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributeimageconfig_PrincipalObjectAttributeAccesses"></a> attributeimageconfig_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [attributeimageconfig attributeimageconfig_PrincipalObjectAttributeAccesses](attributeimageconfig.md#BKMK_attributeimageconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`attributeimageconfig`|
|ReferencedAttribute|`attributeimageconfigid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_attributeimageconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributemaskingrule_PrincipalObjectAttributeAccesses"></a> attributemaskingrule_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [attributemaskingrule attributemaskingrule_PrincipalObjectAttributeAccesses](attributemaskingrule.md#BKMK_attributemaskingrule_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`attributemaskingrule`|
|ReferencedAttribute|`attributemaskingruleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_attributemaskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attributepicklistvalue_PrincipalObjectAttributeAccesses"></a> attributepicklistvalue_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [attributepicklistvalue attributepicklistvalue_PrincipalObjectAttributeAccesses](attributepicklistvalue.md#BKMK_attributepicklistvalue_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`attributepicklistvalue`|
|ReferencedAttribute|`attributepicklistvalueid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_attributepicklistvalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_bot_PrincipalObjectAttributeAccesses"></a> bot_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [bot bot_PrincipalObjectAttributeAccesses](bot.md#BKMK_bot_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`bot`|
|ReferencedAttribute|`botid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_bot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponent_PrincipalObjectAttributeAccesses"></a> botcomponent_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [botcomponent botcomponent_PrincipalObjectAttributeAccesses](botcomponent.md#BKMK_botcomponent_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponent`|
|ReferencedAttribute|`botcomponentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_botcomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponentcollection_PrincipalObjectAttributeAccesses"></a> botcomponentcollection_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [botcomponentcollection botcomponentcollection_PrincipalObjectAttributeAccesses](botcomponentcollection.md#BKMK_botcomponentcollection_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponentcollection`|
|ReferencedAttribute|`botcomponentcollectionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_botcomponentcollection`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_businessprocess_PrincipalObjectAttributeAccesses"></a> businessprocess_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [businessprocess businessprocess_PrincipalObjectAttributeAccesses](businessprocess.md#BKMK_businessprocess_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`businessprocess`|
|ReferencedAttribute|`businessprocessid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_businessprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_businessunit_principalobjectattributeaccess"></a> businessunit_principalobjectattributeaccess

One-To-Many Relationship: [businessunit businessunit_principalobjectattributeaccess](businessunit.md#BKMK_businessunit_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_businessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_card_PrincipalObjectAttributeAccesses"></a> card_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [card card_PrincipalObjectAttributeAccesses](card.md#BKMK_card_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`card`|
|ReferencedAttribute|`cardid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_card`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalog_PrincipalObjectAttributeAccesses"></a> catalog_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [catalog catalog_PrincipalObjectAttributeAccesses](catalog.md#BKMK_catalog_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`catalog`|
|ReferencedAttribute|`catalogid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_catalog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_catalogassignment_PrincipalObjectAttributeAccesses"></a> catalogassignment_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [catalogassignment catalogassignment_PrincipalObjectAttributeAccesses](catalogassignment.md#BKMK_catalogassignment_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`catalogassignment`|
|ReferencedAttribute|`catalogassignmentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_catalogassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_certificatecredential_PrincipalObjectAttributeAccesses"></a> certificatecredential_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [certificatecredential certificatecredential_PrincipalObjectAttributeAccesses](certificatecredential.md#BKMK_certificatecredential_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`certificatecredential`|
|ReferencedAttribute|`certificatecredentialid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_certificatecredential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_chat_PrincipalObjectAttributeAccesses"></a> chat_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [chat chat_PrincipalObjectAttributeAccesses](chat.md#BKMK_chat_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`chat`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_chat`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connection_principalobjectattributeaccess"></a> connection_principalobjectattributeaccess

One-To-Many Relationship: [connection connection_principalobjectattributeaccess](connection.md#BKMK_connection_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`connection`|
|ReferencedAttribute|`connectionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_connection`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectioninstance_PrincipalObjectAttributeAccesses"></a> connectioninstance_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [connectioninstance connectioninstance_PrincipalObjectAttributeAccesses](connectioninstance.md#BKMK_connectioninstance_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`connectioninstance`|
|ReferencedAttribute|`connectioninstanceid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_connectioninstance`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connectionreference_PrincipalObjectAttributeAccesses"></a> connectionreference_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [connectionreference connectionreference_PrincipalObjectAttributeAccesses](connectionreference.md#BKMK_connectionreference_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionreference`|
|ReferencedAttribute|`connectionreferenceid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_connectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_connector_PrincipalObjectAttributeAccesses"></a> connector_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [connector connector_PrincipalObjectAttributeAccesses](connector.md#BKMK_connector_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`connector`|
|ReferencedAttribute|`connectorid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_connector`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_contact_principalobjectattributeaccess"></a> contact_principalobjectattributeaccess

One-To-Many Relationship: [contact contact_principalobjectattributeaccess](contact.md#BKMK_contact_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_conversationtranscript_PrincipalObjectAttributeAccesses"></a> conversationtranscript_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [conversationtranscript conversationtranscript_PrincipalObjectAttributeAccesses](conversationtranscript.md#BKMK_conversationtranscript_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`conversationtranscript`|
|ReferencedAttribute|`conversationtranscriptid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_conversationtranscript`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotexamplequestion_PrincipalObjectAttributeAccesses"></a> copilotexamplequestion_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [copilotexamplequestion copilotexamplequestion_PrincipalObjectAttributeAccesses](copilotexamplequestion.md#BKMK_copilotexamplequestion_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotexamplequestion`|
|ReferencedAttribute|`copilotexamplequestionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_copilotexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotglossaryterm_PrincipalObjectAttributeAccesses"></a> copilotglossaryterm_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [copilotglossaryterm copilotglossaryterm_PrincipalObjectAttributeAccesses](copilotglossaryterm.md#BKMK_copilotglossaryterm_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotglossaryterm`|
|ReferencedAttribute|`copilotglossarytermid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_copilotglossaryterm`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_copilotsynonyms_PrincipalObjectAttributeAccesses"></a> copilotsynonyms_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [copilotsynonyms copilotsynonyms_PrincipalObjectAttributeAccesses](copilotsynonyms.md#BKMK_copilotsynonyms_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`copilotsynonyms`|
|ReferencedAttribute|`copilotsynonymsid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_copilotsynonyms`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_credential_PrincipalObjectAttributeAccesses"></a> credential_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [credential credential_PrincipalObjectAttributeAccesses](credential.md#BKMK_credential_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`credential`|
|ReferencedAttribute|`credentialid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_credential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapi_PrincipalObjectAttributeAccesses"></a> customapi_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [customapi customapi_PrincipalObjectAttributeAccesses](customapi.md#BKMK_customapi_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`customapi`|
|ReferencedAttribute|`customapiid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_customapi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapirequestparameter_PrincipalObjectAttributeAccesses"></a> customapirequestparameter_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [customapirequestparameter customapirequestparameter_PrincipalObjectAttributeAccesses](customapirequestparameter.md#BKMK_customapirequestparameter_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`customapirequestparameter`|
|ReferencedAttribute|`customapirequestparameterid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_customapirequestparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customapiresponseproperty_PrincipalObjectAttributeAccesses"></a> customapiresponseproperty_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [customapiresponseproperty customapiresponseproperty_PrincipalObjectAttributeAccesses](customapiresponseproperty.md#BKMK_customapiresponseproperty_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`customapiresponseproperty`|
|ReferencedAttribute|`customapiresponsepropertyid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_customapiresponseproperty`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_customeraddress_principalobjectattributeaccess"></a> customeraddress_principalobjectattributeaccess

One-To-Many Relationship: [customeraddress customeraddress_principalobjectattributeaccess](customeraddress.md#BKMK_customeraddress_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`customeraddress`|
|ReferencedAttribute|`customeraddressid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_customeraddress`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolder_PrincipalObjectAttributeAccesses"></a> datalakefolder_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [datalakefolder datalakefolder_PrincipalObjectAttributeAccesses](datalakefolder.md#BKMK_datalakefolder_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolder`|
|ReferencedAttribute|`datalakefolderid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolderpermission_PrincipalObjectAttributeAccesses"></a> datalakefolderpermission_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [datalakefolderpermission datalakefolderpermission_PrincipalObjectAttributeAccesses](datalakefolderpermission.md#BKMK_datalakefolderpermission_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolderpermission`|
|ReferencedAttribute|`datalakefolderpermissionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_datalakefolderpermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspace_PrincipalObjectAttributeAccesses"></a> datalakeworkspace_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [datalakeworkspace datalakeworkspace_PrincipalObjectAttributeAccesses](datalakeworkspace.md#BKMK_datalakeworkspace_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspace`|
|ReferencedAttribute|`datalakeworkspaceid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_datalakeworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakeworkspacepermission_PrincipalObjectAttributeAccesses"></a> datalakeworkspacepermission_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [datalakeworkspacepermission datalakeworkspacepermission_PrincipalObjectAttributeAccesses](datalakeworkspacepermission.md#BKMK_datalakeworkspacepermission_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakeworkspacepermission`|
|ReferencedAttribute|`datalakeworkspacepermissionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_datalakeworkspacepermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dataprocessingconfiguration_PrincipalObjectAttributeAccesses"></a> dataprocessingconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [dataprocessingconfiguration dataprocessingconfiguration_PrincipalObjectAttributeAccesses](dataprocessingconfiguration.md#BKMK_dataprocessingconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`dataprocessingconfiguration`|
|ReferencedAttribute|`dataprocessingconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_dataprocessingconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_delegatedauthorization_PrincipalObjectAttributeAccesses"></a> delegatedauthorization_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [delegatedauthorization delegatedauthorization_PrincipalObjectAttributeAccesses](delegatedauthorization.md#BKMK_delegatedauthorization_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`delegatedauthorization`|
|ReferencedAttribute|`delegatedauthorizationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_delegatedauthorization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowbinary_PrincipalObjectAttributeAccesses"></a> desktopflowbinary_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [desktopflowbinary desktopflowbinary_PrincipalObjectAttributeAccesses](desktopflowbinary.md#BKMK_desktopflowbinary_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowbinary`|
|ReferencedAttribute|`desktopflowbinaryid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_desktopflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowmodule_PrincipalObjectAttributeAccesses"></a> desktopflowmodule_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [desktopflowmodule desktopflowmodule_PrincipalObjectAttributeAccesses](desktopflowmodule.md#BKMK_desktopflowmodule_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowmodule`|
|ReferencedAttribute|`desktopflowmoduleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_desktopflowmodule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearch_PrincipalObjectAttributeAccesses"></a> dvfilesearch_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [dvfilesearch dvfilesearch_PrincipalObjectAttributeAccesses](dvfilesearch.md#BKMK_dvfilesearch_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearch`|
|ReferencedAttribute|`dvfilesearchid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_dvfilesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchattribute_PrincipalObjectAttributeAccesses"></a> dvfilesearchattribute_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [dvfilesearchattribute dvfilesearchattribute_PrincipalObjectAttributeAccesses](dvfilesearchattribute.md#BKMK_dvfilesearchattribute_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchattribute`|
|ReferencedAttribute|`dvfilesearchattributeid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_dvfilesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvfilesearchentity_PrincipalObjectAttributeAccesses"></a> dvfilesearchentity_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [dvfilesearchentity dvfilesearchentity_PrincipalObjectAttributeAccesses](dvfilesearchentity.md#BKMK_dvfilesearchentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`dvfilesearchentity`|
|ReferencedAttribute|`dvfilesearchentityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_dvfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearch_PrincipalObjectAttributeAccesses"></a> dvtablesearch_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [dvtablesearch dvtablesearch_PrincipalObjectAttributeAccesses](dvtablesearch.md#BKMK_dvtablesearch_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearch`|
|ReferencedAttribute|`dvtablesearchid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_dvtablesearch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchattribute_PrincipalObjectAttributeAccesses"></a> dvtablesearchattribute_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [dvtablesearchattribute dvtablesearchattribute_PrincipalObjectAttributeAccesses](dvtablesearchattribute.md#BKMK_dvtablesearchattribute_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchattribute`|
|ReferencedAttribute|`dvtablesearchattributeid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_dvtablesearchattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_dvtablesearchentity_PrincipalObjectAttributeAccesses"></a> dvtablesearchentity_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [dvtablesearchentity dvtablesearchentity_PrincipalObjectAttributeAccesses](dvtablesearchentity.md#BKMK_dvtablesearchentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`dvtablesearchentity`|
|ReferencedAttribute|`dvtablesearchentityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_dvtablesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_principalobjectattributeaccess"></a> email_principalobjectattributeaccess

One-To-Many Relationship: [email email_principalobjectattributeaccess](email.md#BKMK_email_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_emailaddressconfiguration_PrincipalObjectAttributeAccesses"></a> emailaddressconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [emailaddressconfiguration emailaddressconfiguration_PrincipalObjectAttributeAccesses](emailaddressconfiguration.md#BKMK_emailaddressconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`emailaddressconfiguration`|
|ReferencedAttribute|`emailaddressconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_emailaddressconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityanalyticsconfig_PrincipalObjectAttributeAccesses"></a> entityanalyticsconfig_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [entityanalyticsconfig entityanalyticsconfig_PrincipalObjectAttributeAccesses](entityanalyticsconfig.md#BKMK_entityanalyticsconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`entityanalyticsconfig`|
|ReferencedAttribute|`entityanalyticsconfigid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_entityanalyticsconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityclusterconfig_PrincipalObjectAttributeAccesses"></a> entityclusterconfig_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [entityclusterconfig entityclusterconfig_PrincipalObjectAttributeAccesses](entityclusterconfig.md#BKMK_entityclusterconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`entityclusterconfig`|
|ReferencedAttribute|`entityclusterconfigid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_entityclusterconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityimageconfig_PrincipalObjectAttributeAccesses"></a> entityimageconfig_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [entityimageconfig entityimageconfig_PrincipalObjectAttributeAccesses](entityimageconfig.md#BKMK_entityimageconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`entityimageconfig`|
|ReferencedAttribute|`entityimageconfigid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_entityimageconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityindex_PrincipalObjectAttributeAccesses"></a> entityindex_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [entityindex entityindex_PrincipalObjectAttributeAccesses](entityindex.md#BKMK_entityindex_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`entityindex`|
|ReferencedAttribute|`indexid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_entityindex`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entityrecordfilter_PrincipalObjectAttributeAccesses"></a> entityrecordfilter_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [entityrecordfilter entityrecordfilter_PrincipalObjectAttributeAccesses](entityrecordfilter.md#BKMK_entityrecordfilter_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`entityrecordfilter`|
|ReferencedAttribute|`entityrecordfilterid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_entityrecordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses"></a> environmentvariabledefinition_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_PrincipalObjectAttributeAccesses](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_environmentvariabledefinition`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariablevalue_PrincipalObjectAttributeAccesses"></a> environmentvariablevalue_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [environmentvariablevalue environmentvariablevalue_PrincipalObjectAttributeAccesses](environmentvariablevalue.md#BKMK_environmentvariablevalue_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariablevalue`|
|ReferencedAttribute|`environmentvariablevalueid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_environmentvariablevalue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportedexcel_PrincipalObjectAttributeAccesses"></a> exportedexcel_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [exportedexcel exportedexcel_PrincipalObjectAttributeAccesses](exportedexcel.md#BKMK_exportedexcel_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`exportedexcel`|
|ReferencedAttribute|`exportedexcelid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_exportedexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportsolutionupload_PrincipalObjectAttributeAccesses"></a> exportsolutionupload_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [exportsolutionupload exportsolutionupload_PrincipalObjectAttributeAccesses](exportsolutionupload.md#BKMK_exportsolutionupload_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`exportsolutionupload`|
|ReferencedAttribute|`exportsolutionuploadid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_exportsolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fabricaiskill_PrincipalObjectAttributeAccesses"></a> fabricaiskill_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [fabricaiskill fabricaiskill_PrincipalObjectAttributeAccesses](fabricaiskill.md#BKMK_fabricaiskill_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`fabricaiskill`|
|ReferencedAttribute|`fabricaiskillid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_fabricaiskill`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fax_principalobjectattributeaccess"></a> fax_principalobjectattributeaccess

One-To-Many Relationship: [fax fax_principalobjectattributeaccess](fax.md#BKMK_fax_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_fax`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_featurecontrolsetting_PrincipalObjectAttributeAccesses"></a> featurecontrolsetting_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [featurecontrolsetting featurecontrolsetting_PrincipalObjectAttributeAccesses](featurecontrolsetting.md#BKMK_featurecontrolsetting_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`featurecontrolsetting`|
|ReferencedAttribute|`featurecontrolsettingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_featurecontrolsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeconfiguration_PrincipalObjectAttributeAccesses"></a> federatedknowledgeconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [federatedknowledgeconfiguration federatedknowledgeconfiguration_PrincipalObjectAttributeAccesses](federatedknowledgeconfiguration.md#BKMK_federatedknowledgeconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeconfiguration`|
|ReferencedAttribute|`federatedknowledgeconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_federatedknowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_federatedknowledgeentityconfiguration_PrincipalObjectAttributeAccesses"></a> federatedknowledgeentityconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [federatedknowledgeentityconfiguration federatedknowledgeentityconfiguration_PrincipalObjectAttributeAccesses](federatedknowledgeentityconfiguration.md#BKMK_federatedknowledgeentityconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`federatedknowledgeentityconfiguration`|
|ReferencedAttribute|`federatedknowledgeentityconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_federatedknowledgeentityconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_feedback_principalobjectattributeaccess"></a> feedback_principalobjectattributeaccess

One-To-Many Relationship: [feedback feedback_principalobjectattributeaccess](feedback.md#BKMK_feedback_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`feedback`|
|ReferencedAttribute|`feedbackid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_feedback`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcapacityassignment_PrincipalObjectAttributeAccesses"></a> flowcapacityassignment_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [flowcapacityassignment flowcapacityassignment_PrincipalObjectAttributeAccesses](flowcapacityassignment.md#BKMK_flowcapacityassignment_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcapacityassignment`|
|ReferencedAttribute|`flowcapacityassignmentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_flowcapacityassignment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowcredentialapplication_PrincipalObjectAttributeAccesses"></a> flowcredentialapplication_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [flowcredentialapplication flowcredentialapplication_PrincipalObjectAttributeAccesses](flowcredentialapplication.md#BKMK_flowcredentialapplication_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`flowcredentialapplication`|
|ReferencedAttribute|`flowcredentialapplicationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_flowcredentialapplication`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowevent_PrincipalObjectAttributeAccesses"></a> flowevent_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [flowevent flowevent_PrincipalObjectAttributeAccesses](flowevent.md#BKMK_flowevent_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`flowevent`|
|ReferencedAttribute|`floweventid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_flowevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachine_PrincipalObjectAttributeAccesses"></a> flowmachine_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [flowmachine flowmachine_PrincipalObjectAttributeAccesses](flowmachine.md#BKMK_flowmachine_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachine`|
|ReferencedAttribute|`flowmachineid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_flowmachine`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_PrincipalObjectAttributeAccesses"></a> flowmachinegroup_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_PrincipalObjectAttributeAccesses](flowmachinegroup.md#BKMK_flowmachinegroup_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_flowmachinegroup`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimage_PrincipalObjectAttributeAccesses"></a> flowmachineimage_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [flowmachineimage flowmachineimage_PrincipalObjectAttributeAccesses](flowmachineimage.md#BKMK_flowmachineimage_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimage`|
|ReferencedAttribute|`flowmachineimageid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_flowmachineimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimageversion_PrincipalObjectAttributeAccesses"></a> flowmachineimageversion_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [flowmachineimageversion flowmachineimageversion_PrincipalObjectAttributeAccesses](flowmachineimageversion.md#BKMK_flowmachineimageversion_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimageversion`|
|ReferencedAttribute|`flowmachineimageversionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_flowmachineimageversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinenetwork_PrincipalObjectAttributeAccesses"></a> flowmachinenetwork_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [flowmachinenetwork flowmachinenetwork_PrincipalObjectAttributeAccesses](flowmachinenetwork.md#BKMK_flowmachinenetwork_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinenetwork`|
|ReferencedAttribute|`flowmachinenetworkid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_flowmachinenetwork`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsession_PrincipalObjectAttributeAccesses"></a> flowsession_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [flowsession flowsession_PrincipalObjectAttributeAccesses](flowsession.md#BKMK_flowsession_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsession`|
|ReferencedAttribute|`flowsessionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_flowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fxexpression_PrincipalObjectAttributeAccesses"></a> fxexpression_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [fxexpression fxexpression_PrincipalObjectAttributeAccesses](fxexpression.md#BKMK_fxexpression_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`fxexpression`|
|ReferencedAttribute|`fxexpressionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_fxexpression`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_goal_principalobjectattributeaccess"></a> goal_principalobjectattributeaccess

One-To-Many Relationship: [goal goal_principalobjectattributeaccess](goal.md#BKMK_goal_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`goal`|
|ReferencedAttribute|`goalid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_goal`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_governanceconfiguration_PrincipalObjectAttributeAccesses"></a> governanceconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [governanceconfiguration governanceconfiguration_PrincipalObjectAttributeAccesses](governanceconfiguration.md#BKMK_governanceconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`governanceconfiguration`|
|ReferencedAttribute|`governanceconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_governanceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_indexattributes_PrincipalObjectAttributeAccesses"></a> indexattributes_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [indexattributes indexattributes_PrincipalObjectAttributeAccesses](indexattributes.md#BKMK_indexattributes_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`indexattributes`|
|ReferencedAttribute|`indexattributeid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_indexattributes`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_kbarticle_principalobjectattributeaccess"></a> kbarticle_principalobjectattributeaccess

One-To-Many Relationship: [kbarticle kbarticle_principalobjectattributeaccess](kbarticle.md#BKMK_kbarticle_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`kbarticle`|
|ReferencedAttribute|`kbarticleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_kbarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_keyvaultreference_PrincipalObjectAttributeAccesses"></a> keyvaultreference_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [keyvaultreference keyvaultreference_PrincipalObjectAttributeAccesses](keyvaultreference.md#BKMK_keyvaultreference_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`keyvaultreference`|
|ReferencedAttribute|`keyvaultreferenceid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_keyvaultreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_PrincipalObjectAttributeAccess"></a> knowledgearticle_PrincipalObjectAttributeAccess

One-To-Many Relationship: [knowledgearticle knowledgearticle_PrincipalObjectAttributeAccess](knowledgearticle.md#BKMK_knowledgearticle_PrincipalObjectAttributeAccess)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticleview_principalobjectattributeaccess"></a> knowledgearticleview_principalobjectattributeaccess

One-To-Many Relationship: [knowledgearticleviews knowledgearticleview_principalobjectattributeaccess](knowledgearticleviews.md#BKMK_knowledgearticleview_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticleviews`|
|ReferencedAttribute|`knowledgearticleviewsid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_knowledgearticleviews`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess"></a> KnowledgeBaseRecord_PrincipalObjectAttributeAccess

One-To-Many Relationship: [knowledgebaserecord KnowledgeBaseRecord_PrincipalObjectAttributeAccess](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgebaserecord`|
|ReferencedAttribute|`knowledgebaserecordid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_knowledgebaserecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_letter_principalobjectattributeaccess"></a> letter_principalobjectattributeaccess

One-To-Many Relationship: [letter letter_principalobjectattributeaccess](letter.md#BKMK_letter_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_letter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_principalobjectattributeaccess_organizationid"></a> lk_principalobjectattributeaccess_organizationid

One-To-Many Relationship: [organization lk_principalobjectattributeaccess_organizationid](organization.md#BKMK_lk_principalobjectattributeaccess_organizationid)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mailmergetemplate_principalobjectattributeaccess"></a> mailmergetemplate_principalobjectattributeaccess

One-To-Many Relationship: [mailmergetemplate mailmergetemplate_principalobjectattributeaccess](mailmergetemplate.md#BKMK_mailmergetemplate_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`mailmergetemplate`|
|ReferencedAttribute|`mailmergetemplateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_mailmergetemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mainfewshot_PrincipalObjectAttributeAccesses"></a> mainfewshot_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [mainfewshot mainfewshot_PrincipalObjectAttributeAccesses](mainfewshot.md#BKMK_mainfewshot_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`mainfewshot`|
|ReferencedAttribute|`mainfewshotid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_mainfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_makerfewshot_PrincipalObjectAttributeAccesses"></a> makerfewshot_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [makerfewshot makerfewshot_PrincipalObjectAttributeAccesses](makerfewshot.md#BKMK_makerfewshot_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`makerfewshot`|
|ReferencedAttribute|`makerfewshotid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_makerfewshot`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_PrincipalObjectAttributeAccesses"></a> managedidentity_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [managedidentity managedidentity_PrincipalObjectAttributeAccesses](managedidentity.md#BKMK_managedidentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_managedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_maskingrule_PrincipalObjectAttributeAccesses"></a> maskingrule_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [maskingrule maskingrule_PrincipalObjectAttributeAccesses](maskingrule.md#BKMK_maskingrule_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`maskingrule`|
|ReferencedAttribute|`maskingruleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_maskingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_metadataforarchival_PrincipalObjectAttributeAccesses"></a> metadataforarchival_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [metadataforarchival metadataforarchival_PrincipalObjectAttributeAccesses](metadataforarchival.md#BKMK_metadataforarchival_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`metadataforarchival`|
|ReferencedAttribute|`metadataforarchivalid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_metadataforarchival`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mobileofflineprofileextension_PrincipalObjectAttributeAccesses"></a> mobileofflineprofileextension_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [mobileofflineprofileextension mobileofflineprofileextension_PrincipalObjectAttributeAccesses](mobileofflineprofileextension.md#BKMK_mobileofflineprofileextension_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofileextension`|
|ReferencedAttribute|`mobileofflineprofileextensionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_mobileofflineprofileextension`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdataset_PrincipalObjectAttributeAccesses"></a> msdyn_aibdataset_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aibdataset msdyn_aibdataset_PrincipalObjectAttributeAccesses](msdyn_aibdataset.md#BKMK_msdyn_aibdataset_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdataset`|
|ReferencedAttribute|`msdyn_aibdatasetid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aibdataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses"></a> msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aibdatasetfile msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses](msdyn_aibdatasetfile.md#BKMK_msdyn_aibdatasetfile_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetfile`|
|ReferencedAttribute|`msdyn_aibdatasetfileid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aibdatasetfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses"></a> msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aibdatasetrecord msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses](msdyn_aibdatasetrecord.md#BKMK_msdyn_aibdatasetrecord_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetrecord`|
|ReferencedAttribute|`msdyn_aibdatasetrecordid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aibdatasetrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses"></a> msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aibdatasetscontainer msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses](msdyn_aibdatasetscontainer.md#BKMK_msdyn_aibdatasetscontainer_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibdatasetscontainer`|
|ReferencedAttribute|`msdyn_aibdatasetscontainerid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aibdatasetscontainer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses"></a> msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aibfeedbackloop msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfeedbackloop`|
|ReferencedAttribute|`msdyn_aibfeedbackloopid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aibfeedbackloop`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfile_PrincipalObjectAttributeAccesses"></a> msdyn_aibfile_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aibfile msdyn_aibfile_PrincipalObjectAttributeAccesses](msdyn_aibfile.md#BKMK_msdyn_aibfile_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfile`|
|ReferencedAttribute|`msdyn_aibfileid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aibfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses"></a> msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aibfileattacheddata msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses](msdyn_aibfileattacheddata.md#BKMK_msdyn_aibfileattacheddata_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfileattacheddata`|
|ReferencedAttribute|`msdyn_aibfileattacheddataid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aibfileattacheddata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_aiconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aiconfiguration msdyn_aiconfiguration_PrincipalObjectAttributeAccesses](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfiguration`|
|ReferencedAttribute|`msdyn_aiconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aiconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses"></a> msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aidataprocessingevent msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses](msdyn_aidataprocessingevent.md#BKMK_msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aidataprocessingevent`|
|ReferencedAttribute|`msdyn_aidataprocessingeventid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aidataprocessingevent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_aievaluationconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aievaluationconfiguration msdyn_aievaluationconfiguration_PrincipalObjectAttributeAccesses](msdyn_aievaluationconfiguration.md#BKMK_msdyn_aievaluationconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationconfiguration`|
|ReferencedAttribute|`msdyn_aievaluationconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aievaluationconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationrun_PrincipalObjectAttributeAccesses"></a> msdyn_aievaluationrun_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aievaluationrun msdyn_aievaluationrun_PrincipalObjectAttributeAccesses](msdyn_aievaluationrun.md#BKMK_msdyn_aievaluationrun_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationrun`|
|ReferencedAttribute|`msdyn_aievaluationrunid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aievaluationrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievent_PrincipalObjectAttributeAccesses"></a> msdyn_aievent_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aievent msdyn_aievent_PrincipalObjectAttributeAccesses](msdyn_aievent.md#BKMK_msdyn_aievent_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievent`|
|ReferencedAttribute|`msdyn_aieventid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aievent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses"></a> msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aifptrainingdocument msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aifptrainingdocument`|
|ReferencedAttribute|`msdyn_aifptrainingdocumentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aifptrainingdocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aimodel_PrincipalObjectAttributeAccesses"></a> msdyn_aimodel_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aimodel msdyn_aimodel_PrincipalObjectAttributeAccesses](msdyn_aimodel.md#BKMK_msdyn_aimodel_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aimodel`|
|ReferencedAttribute|`msdyn_aimodelid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aimodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aimodelcatalog_PrincipalObjectAttributeAccesses"></a> msdyn_aimodelcatalog_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aimodelcatalog msdyn_aimodelcatalog_PrincipalObjectAttributeAccesses](msdyn_aimodelcatalog.md#BKMK_msdyn_aimodelcatalog_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aimodelcatalog`|
|ReferencedAttribute|`msdyn_aimodelcatalogid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aimodelcatalog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodimage_PrincipalObjectAttributeAccesses"></a> msdyn_aiodimage_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aiodimage msdyn_aiodimage_PrincipalObjectAttributeAccesses](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodimage`|
|ReferencedAttribute|`msdyn_aiodimageid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aiodimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodlabel_PrincipalObjectAttributeAccesses"></a> msdyn_aiodlabel_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aiodlabel msdyn_aiodlabel_PrincipalObjectAttributeAccesses](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodlabel`|
|ReferencedAttribute|`msdyn_aiodlabelid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aiodlabel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses"></a> msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aiodtrainingboundingbox msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingboundingbox_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencedAttribute|`msdyn_aiodtrainingboundingboxid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aiodtrainingboundingbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses"></a> msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aiodtrainingimage msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodtrainingimage`|
|ReferencedAttribute|`msdyn_aiodtrainingimageid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aiodtrainingimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitemplate_PrincipalObjectAttributeAccesses"></a> msdyn_aitemplate_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aitemplate msdyn_aitemplate_PrincipalObjectAttributeAccesses](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitemplate`|
|ReferencedAttribute|`msdyn_aitemplateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aitemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcase_PrincipalObjectAttributeAccesses"></a> msdyn_aitestcase_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aitestcase msdyn_aitestcase_PrincipalObjectAttributeAccesses](msdyn_aitestcase.md#BKMK_msdyn_aitestcase_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcase`|
|ReferencedAttribute|`msdyn_aitestcaseid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aitestcase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcasedocument_PrincipalObjectAttributeAccesses"></a> msdyn_aitestcasedocument_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aitestcasedocument msdyn_aitestcasedocument_PrincipalObjectAttributeAccesses](msdyn_aitestcasedocument.md#BKMK_msdyn_aitestcasedocument_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcasedocument`|
|ReferencedAttribute|`msdyn_aitestcasedocumentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aitestcasedocument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestcaseinput_PrincipalObjectAttributeAccesses"></a> msdyn_aitestcaseinput_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aitestcaseinput msdyn_aitestcaseinput_PrincipalObjectAttributeAccesses](msdyn_aitestcaseinput.md#BKMK_msdyn_aitestcaseinput_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestcaseinput`|
|ReferencedAttribute|`msdyn_aitestcaseinputid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aitestcaseinput`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrun_PrincipalObjectAttributeAccesses"></a> msdyn_aitestrun_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aitestrun msdyn_aitestrun_PrincipalObjectAttributeAccesses](msdyn_aitestrun.md#BKMK_msdyn_aitestrun_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrun`|
|ReferencedAttribute|`msdyn_aitestrunid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aitestrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitestrunbatch_PrincipalObjectAttributeAccesses"></a> msdyn_aitestrunbatch_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_aitestrunbatch msdyn_aitestrunbatch_PrincipalObjectAttributeAccesses](msdyn_aitestrunbatch.md#BKMK_msdyn_aitestrunbatch_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitestrunbatch`|
|ReferencedAttribute|`msdyn_aitestrunbatchid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aitestrunbatch`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses"></a> msdyn_analysiscomponent_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_analysiscomponent msdyn_analysiscomponent_PrincipalObjectAttributeAccesses](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysiscomponent`|
|ReferencedAttribute|`msdyn_analysiscomponentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_analysiscomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses"></a> msdyn_analysisjob_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_PrincipalObjectAttributeAccesses](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_analysisjob`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisoverride_PrincipalObjectAttributeAccesses"></a> msdyn_analysisoverride_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_analysisoverride msdyn_analysisoverride_PrincipalObjectAttributeAccesses](msdyn_analysisoverride.md#BKMK_msdyn_analysisoverride_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisoverride`|
|ReferencedAttribute|`msdyn_analysisoverrideid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_analysisoverride`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresult_PrincipalObjectAttributeAccesses"></a> msdyn_analysisresult_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_analysisresult msdyn_analysisresult_PrincipalObjectAttributeAccesses](msdyn_analysisresult.md#BKMK_msdyn_analysisresult_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresult`|
|ReferencedAttribute|`msdyn_analysisresultid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_analysisresult`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses"></a> msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_analysisresultdetail msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses](msdyn_analysisresultdetail.md#BKMK_msdyn_analysisresultdetail_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisresultdetail`|
|ReferencedAttribute|`msdyn_analysisresultdetailid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_analysisresultdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses"></a> msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_appinsightsmetadata msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses](msdyn_appinsightsmetadata.md#BKMK_msdyn_appinsightsmetadata_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_appinsightsmetadata`|
|ReferencedAttribute|`msdyn_appinsightsmetadataid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_appinsightsmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_copilotinteractions_PrincipalObjectAttributeAccesses"></a> msdyn_copilotinteractions_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_copilotinteractions msdyn_copilotinteractions_PrincipalObjectAttributeAccesses](msdyn_copilotinteractions.md#BKMK_msdyn_copilotinteractions_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_copilotinteractions`|
|ReferencedAttribute|`msdyn_copilotinteractionsid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_copilotinteractions`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses"></a> msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_customcontrolextendedsettings msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses](msdyn_customcontrolextendedsettings.md#BKMK_msdyn_customcontrolextendedsettings_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_customcontrolextendedsettings`|
|ReferencedAttribute|`msdyn_customcontrolextendedsettingsid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_customcontrolextendedsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses"></a> msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_dataflow_datalakefolder msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow_datalakefolder`|
|ReferencedAttribute|`msdyn_dataflow_datalakefolderid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_dataflow_datalakefolder`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflow_PrincipalObjectAttributeAccesses"></a> msdyn_dataflow_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_dataflow msdyn_dataflow_PrincipalObjectAttributeAccesses](msdyn_dataflow.md#BKMK_msdyn_dataflow_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflow`|
|ReferencedAttribute|`msdyn_dataflowid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_dataflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowconnectionreference_PrincipalObjectAttributeAccesses"></a> msdyn_dataflowconnectionreference_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_dataflowconnectionreference msdyn_dataflowconnectionreference_PrincipalObjectAttributeAccesses](msdyn_dataflowconnectionreference.md#BKMK_msdyn_dataflowconnectionreference_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowconnectionreference`|
|ReferencedAttribute|`msdyn_dataflowconnectionreferenceid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_dataflowconnectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses"></a> msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_dataflowrefreshhistory msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_dataflowrefreshhistory_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowrefreshhistory`|
|ReferencedAttribute|`msdyn_dataflowrefreshhistoryid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_dataflowrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses"></a> msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_dataflowtemplate msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses](msdyn_dataflowtemplate.md#BKMK_msdyn_dataflowtemplate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowtemplate`|
|ReferencedAttribute|`msdyn_dataflowtemplateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_dataflowtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequest_PrincipalObjectAttributeAccesses"></a> msdyn_dmsrequest_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_dmsrequest msdyn_dmsrequest_PrincipalObjectAttributeAccesses](msdyn_dmsrequest.md#BKMK_msdyn_dmsrequest_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequest`|
|ReferencedAttribute|`msdyn_dmsrequestid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_dmsrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses"></a> msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_dmsrequeststatus msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses](msdyn_dmsrequeststatus.md#BKMK_msdyn_dmsrequeststatus_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmsrequeststatus`|
|ReferencedAttribute|`msdyn_dmsrequeststatusid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_dmsrequeststatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncrequest_PrincipalObjectAttributeAccesses"></a> msdyn_dmssyncrequest_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_dmssyncrequest msdyn_dmssyncrequest_PrincipalObjectAttributeAccesses](msdyn_dmssyncrequest.md#BKMK_msdyn_dmssyncrequest_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncrequest`|
|ReferencedAttribute|`msdyn_dmssyncrequestid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_dmssyncrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_dmssyncstatus_PrincipalObjectAttributeAccesses"></a> msdyn_dmssyncstatus_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_dmssyncstatus msdyn_dmssyncstatus_PrincipalObjectAttributeAccesses](msdyn_dmssyncstatus.md#BKMK_msdyn_dmssyncstatus_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dmssyncstatus`|
|ReferencedAttribute|`msdyn_dmssyncstatusid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_dmssyncstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_entitylinkchatconfiguration msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses](msdyn_entitylinkchatconfiguration.md#BKMK_msdyn_entitylinkchatconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencedAttribute|`msdyn_entitylinkchatconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_entitylinkchatconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses"></a> msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_entityrefreshhistory msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses](msdyn_entityrefreshhistory.md#BKMK_msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_entityrefreshhistory`|
|ReferencedAttribute|`msdyn_entityrefreshhistoryid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_entityrefreshhistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses"></a> msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_favoriteknowledgearticle msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses](msdyn_favoriteknowledgearticle.md#BKMK_msdyn_favoriteknowledgearticle_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_favoriteknowledgearticle`|
|ReferencedAttribute|`msdyn_favoriteknowledgearticleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_favoriteknowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticle_PrincipalObjectAttributeAccesses"></a> msdyn_federatedarticle_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_federatedarticle msdyn_federatedarticle_PrincipalObjectAttributeAccesses](msdyn_federatedarticle.md#BKMK_msdyn_federatedarticle_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticle`|
|ReferencedAttribute|`msdyn_federatedarticleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_federatedarticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses"></a> msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_federatedarticleincident msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses](msdyn_federatedarticleincident.md#BKMK_msdyn_federatedarticleincident_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_federatedarticleincident`|
|ReferencedAttribute|`msdyn_federatedarticleincidentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_federatedarticleincident`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_fileupload_PrincipalObjectAttributeAccesses"></a> msdyn_fileupload_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_fileupload msdyn_fileupload_PrincipalObjectAttributeAccesses](msdyn_fileupload.md#BKMK_msdyn_fileupload_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_fileupload`|
|ReferencedAttribute|`msdyn_fileuploadid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_fileupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_actionapprovalmodel_PrincipalObjectAttributeAccesses"></a> msdyn_flow_actionapprovalmodel_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_flow_actionapprovalmodel msdyn_flow_actionapprovalmodel_PrincipalObjectAttributeAccesses](msdyn_flow_actionapprovalmodel.md#BKMK_msdyn_flow_actionapprovalmodel_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_actionapprovalmodelid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_flow_actionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approval_PrincipalObjectAttributeAccesses"></a> msdyn_flow_approval_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_flow_approval msdyn_flow_approval_PrincipalObjectAttributeAccesses](msdyn_flow_approval.md#BKMK_msdyn_flow_approval_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approval`|
|ReferencedAttribute|`msdyn_flow_approvalid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_flow_approval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses"></a> msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_flow_approvalrequest msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses](msdyn_flow_approvalrequest.md#BKMK_msdyn_flow_approvalrequest_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalrequest`|
|ReferencedAttribute|`msdyn_flow_approvalrequestid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_flow_approvalrequest`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses"></a> msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_flow_approvalresponse msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses](msdyn_flow_approvalresponse.md#BKMK_msdyn_flow_approvalresponse_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalresponse`|
|ReferencedAttribute|`msdyn_flow_approvalresponseid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_flow_approvalresponse`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses"></a> msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_flow_approvalstep msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses](msdyn_flow_approvalstep.md#BKMK_msdyn_flow_approvalstep_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_approvalstep`|
|ReferencedAttribute|`msdyn_flow_approvalstepid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_flow_approvalstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallactionapprovalmodel_PrincipalObjectAttributeAccesses"></a> msdyn_flow_awaitallactionapprovalmodel_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_flow_awaitallactionapprovalmodel msdyn_flow_awaitallactionapprovalmodel_PrincipalObjectAttributeAccesses](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_msdyn_flow_awaitallactionapprovalmodel_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallactionapprovalmodelid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_flow_awaitallactionapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_awaitallapprovalmodel_PrincipalObjectAttributeAccesses"></a> msdyn_flow_awaitallapprovalmodel_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_flow_awaitallapprovalmodel msdyn_flow_awaitallapprovalmodel_PrincipalObjectAttributeAccesses](msdyn_flow_awaitallapprovalmodel.md#BKMK_msdyn_flow_awaitallapprovalmodel_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_awaitallapprovalmodelid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_flow_awaitallapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_basicapprovalmodel_PrincipalObjectAttributeAccesses"></a> msdyn_flow_basicapprovalmodel_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodel_PrincipalObjectAttributeAccesses](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodel_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencedAttribute|`msdyn_flow_basicapprovalmodelid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_flow_basicapprovalmodel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_flow_flowapproval_PrincipalObjectAttributeAccesses"></a> msdyn_flow_flowapproval_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_flow_flowapproval msdyn_flow_flowapproval_PrincipalObjectAttributeAccesses](msdyn_flow_flowapproval.md#BKMK_msdyn_flow_flowapproval_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_flow_flowapproval`|
|ReferencedAttribute|`msdyn_flow_flowapprovalid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_flow_flowapproval`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_formmapping_PrincipalObjectAttributeAccesses"></a> msdyn_formmapping_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_formmapping msdyn_formmapping_PrincipalObjectAttributeAccesses](msdyn_formmapping.md#BKMK_msdyn_formmapping_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_formmapping`|
|ReferencedAttribute|`msdyn_formmappingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_formmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_function_PrincipalObjectAttributeAccesses"></a> msdyn_function_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_function msdyn_function_PrincipalObjectAttributeAccesses](msdyn_function.md#BKMK_msdyn_function_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_function`|
|ReferencedAttribute|`msdyn_functionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_function`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_helppage_PrincipalObjectAttributeAccesses"></a> msdyn_helppage_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_helppage msdyn_helppage_PrincipalObjectAttributeAccesses](msdyn_helppage.md#BKMK_msdyn_helppage_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_helppage`|
|ReferencedAttribute|`msdyn_helppageid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_helppage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses"></a> msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_insightsstorevirtualentity msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses](msdyn_insightsstorevirtualentity.md#BKMK_msdyn_insightsstorevirtualentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_insightsstorevirtualentity`|
|ReferencedAttribute|`msdyn_insightsstorevirtualentityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_insightsstorevirtualentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses"></a> msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_integratedsearchprovider msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_integratedsearchprovider`|
|ReferencedAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_integratedsearchprovider`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses"></a> msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_kalanguagesetting msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses](msdyn_kalanguagesetting.md#BKMK_msdyn_kalanguagesetting_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kalanguagesetting`|
|ReferencedAttribute|`msdyn_kalanguagesettingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_kalanguagesetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kbattachment_PrincipalObjectAttributeAccesses"></a> msdyn_kbattachment_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_kbattachment msdyn_kbattachment_PrincipalObjectAttributeAccesses](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kbattachment`|
|ReferencedAttribute|`msdyn_kbattachmentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_kbattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses"></a> msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_kmfederatedsearchconfig msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses](msdyn_kmfederatedsearchconfig.md#BKMK_msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencedAttribute|`msdyn_kmfederatedsearchconfigid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_kmfederatedsearchconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses"></a> msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_kmpersonalizationsetting msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses](msdyn_kmpersonalizationsetting.md#BKMK_msdyn_kmpersonalizationsetting_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kmpersonalizationsetting`|
|ReferencedAttribute|`msdyn_kmpersonalizationsettingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_kmpersonalizationsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_knowledgearticleimage msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticleimage`|
|ReferencedAttribute|`msdyn_knowledgearticleimageid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_knowledgearticleimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_knowledgearticletemplate msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticletemplate`|
|ReferencedAttribute|`msdyn_knowledgearticletemplateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_knowledgearticletemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeassetconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgeassetconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_knowledgeassetconfiguration msdyn_knowledgeassetconfiguration_PrincipalObjectAttributeAccesses](msdyn_knowledgeassetconfiguration.md#BKMK_msdyn_knowledgeassetconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeassetconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeassetconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_knowledgeassetconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_knowledgeconfiguration msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses](msdyn_knowledgeconfiguration.md#BKMK_msdyn_knowledgeconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeconfiguration`|
|ReferencedAttribute|`msdyn_knowledgeconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_knowledgeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_knowledgeinteractioninsight msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses](msdyn_knowledgeinteractioninsight.md#BKMK_msdyn_knowledgeinteractioninsight_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencedAttribute|`msdyn_knowledgeinteractioninsightid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_knowledgeinteractioninsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_knowledgemanagementsetting msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses](msdyn_knowledgemanagementsetting.md#BKMK_msdyn_knowledgemanagementsetting_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgemanagementsetting`|
|ReferencedAttribute|`msdyn_knowledgemanagementsettingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_knowledgemanagementsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_knowledgepersonalfilter msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses](msdyn_knowledgepersonalfilter.md#BKMK_msdyn_knowledgepersonalfilter_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgepersonalfilter`|
|ReferencedAttribute|`msdyn_knowledgepersonalfilterid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_knowledgepersonalfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_knowledgesearchfilter msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses](msdyn_knowledgesearchfilter.md#BKMK_msdyn_knowledgesearchfilter_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchfilter`|
|ReferencedAttribute|`msdyn_knowledgesearchfilterid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_knowledgesearchfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_knowledgesearchinsight msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses](msdyn_knowledgesearchinsight.md#BKMK_msdyn_knowledgesearchinsight_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgesearchinsight`|
|ReferencedAttribute|`msdyn_knowledgesearchinsightid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_knowledgesearchinsight`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses"></a> msdyn_mobileapp_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_mobileapp msdyn_mobileapp_PrincipalObjectAttributeAccesses](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_mobileapp`|
|ReferencedAttribute|`msdyn_mobileappid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_mobileapp`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_modulerundetail_PrincipalObjectAttributeAccesses"></a> msdyn_modulerundetail_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_modulerundetail msdyn_modulerundetail_PrincipalObjectAttributeAccesses](msdyn_modulerundetail.md#BKMK_msdyn_modulerundetail_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_modulerundetail`|
|ReferencedAttribute|`msdyn_modulerundetailid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_modulerundetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses"></a> msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmanalysishistory msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses](msdyn_pmanalysishistory.md#BKMK_msdyn_pmanalysishistory_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmanalysishistory`|
|ReferencedAttribute|`msdyn_pmanalysishistoryid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmanalysishistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmbusinessruleautomationconfig_PrincipalObjectAttributeAccesses"></a> msdyn_pmbusinessruleautomationconfig_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmbusinessruleautomationconfig msdyn_pmbusinessruleautomationconfig_PrincipalObjectAttributeAccesses](msdyn_pmbusinessruleautomationconfig.md#BKMK_msdyn_pmbusinessruleautomationconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencedAttribute|`msdyn_pmbusinessruleautomationconfigid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmbusinessruleautomationconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendar_PrincipalObjectAttributeAccesses"></a> msdyn_pmcalendar_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmcalendar msdyn_pmcalendar_PrincipalObjectAttributeAccesses](msdyn_pmcalendar.md#BKMK_msdyn_pmcalendar_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendar`|
|ReferencedAttribute|`msdyn_pmcalendarid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmcalendar`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses"></a> msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmcalendarversion msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses](msdyn_pmcalendarversion.md#BKMK_msdyn_pmcalendarversion_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmcalendarversion`|
|ReferencedAttribute|`msdyn_pmcalendarversionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmcalendarversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pminferredtask_PrincipalObjectAttributeAccesses"></a> msdyn_pminferredtask_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pminferredtask msdyn_pminferredtask_PrincipalObjectAttributeAccesses](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pminferredtask`|
|ReferencedAttribute|`msdyn_pminferredtaskid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pminferredtask`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses"></a> msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmprocessextendedmetadataversion msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses](msdyn_pmprocessextendedmetadataversion.md#BKMK_msdyn_pmprocessextendedmetadataversion_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessextendedmetadataversion`|
|ReferencedAttribute|`msdyn_pmprocessextendedmetadataversionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmprocessextendedmetadataversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses"></a> msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmprocesstemplate msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses](msdyn_pmprocesstemplate.md#BKMK_msdyn_pmprocesstemplate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocesstemplate`|
|ReferencedAttribute|`msdyn_pmprocesstemplateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmprocesstemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses"></a> msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmprocessusersettings msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses](msdyn_pmprocessusersettings.md#BKMK_msdyn_pmprocessusersettings_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessusersettings`|
|ReferencedAttribute|`msdyn_pmprocessusersettingsid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmprocessusersettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmprocessversion_PrincipalObjectAttributeAccesses"></a> msdyn_pmprocessversion_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmprocessversion msdyn_pmprocessversion_PrincipalObjectAttributeAccesses](msdyn_pmprocessversion.md#BKMK_msdyn_pmprocessversion_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmprocessversion`|
|ReferencedAttribute|`msdyn_pmprocessversionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmprocessversion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmrecording_PrincipalObjectAttributeAccesses"></a> msdyn_pmrecording_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmrecording msdyn_pmrecording_PrincipalObjectAttributeAccesses](msdyn_pmrecording.md#BKMK_msdyn_pmrecording_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmrecording`|
|ReferencedAttribute|`msdyn_pmrecordingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmrecording`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmsimulation_PrincipalObjectAttributeAccesses"></a> msdyn_pmsimulation_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmsimulation msdyn_pmsimulation_PrincipalObjectAttributeAccesses](msdyn_pmsimulation.md#BKMK_msdyn_pmsimulation_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmsimulation`|
|ReferencedAttribute|`msdyn_pmsimulationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmsimulation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmtemplate_PrincipalObjectAttributeAccesses"></a> msdyn_pmtemplate_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmtemplate msdyn_pmtemplate_PrincipalObjectAttributeAccesses](msdyn_pmtemplate.md#BKMK_msdyn_pmtemplate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmtemplate`|
|ReferencedAttribute|`msdyn_pmtemplateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmtemplate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pmview_PrincipalObjectAttributeAccesses"></a> msdyn_pmview_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_pmview msdyn_pmview_PrincipalObjectAttributeAccesses](msdyn_pmview.md#BKMK_msdyn_pmview_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pmview`|
|ReferencedAttribute|`msdyn_pmviewid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pmview`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_qna_PrincipalObjectAttributeAccesses"></a> msdyn_qna_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_qna msdyn_qna_PrincipalObjectAttributeAccesses](msdyn_qna.md#BKMK_msdyn_qna_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_qna`|
|ReferencedAttribute|`msdyn_qnaid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_qna`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_richtextfile_PrincipalObjectAttributeAccesses"></a> msdyn_richtextfile_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_richtextfile msdyn_richtextfile_PrincipalObjectAttributeAccesses](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_richtextfile`|
|ReferencedAttribute|`msdyn_richtextfileid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_richtextfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredobject_PrincipalObjectAttributeAccesses"></a> msdyn_salesforcestructuredobject_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_salesforcestructuredobject msdyn_salesforcestructuredobject_PrincipalObjectAttributeAccesses](msdyn_salesforcestructuredobject.md#BKMK_msdyn_salesforcestructuredobject_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredobject`|
|ReferencedAttribute|`msdyn_salesforcestructuredobjectid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_salesforcestructuredobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_salesforcestructuredqnaconfig_PrincipalObjectAttributeAccesses"></a> msdyn_salesforcestructuredqnaconfig_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_salesforcestructuredqnaconfig msdyn_salesforcestructuredqnaconfig_PrincipalObjectAttributeAccesses](msdyn_salesforcestructuredqnaconfig.md#BKMK_msdyn_salesforcestructuredqnaconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_salesforcestructuredqnaconfig`|
|ReferencedAttribute|`msdyn_salesforcestructuredqnaconfigid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_salesforcestructuredqnaconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_schedule_PrincipalObjectAttributeAccesses"></a> msdyn_schedule_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_schedule msdyn_schedule_PrincipalObjectAttributeAccesses](msdyn_schedule.md#BKMK_msdyn_schedule_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_schedule`|
|ReferencedAttribute|`msdyn_scheduleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_schedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_serviceconfiguration msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses](msdyn_serviceconfiguration.md#BKMK_msdyn_serviceconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_serviceconfiguration`|
|ReferencedAttribute|`msdyn_serviceconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_serviceconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_slakpi_PrincipalObjectAttributeAccesses"></a> msdyn_slakpi_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_slakpi msdyn_slakpi_PrincipalObjectAttributeAccesses](msdyn_slakpi.md#BKMK_msdyn_slakpi_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_slakpi`|
|ReferencedAttribute|`msdyn_slakpiid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_slakpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses"></a> msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_solutionhealthrule msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses](msdyn_solutionhealthrule.md#BKMK_msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthrule`|
|ReferencedAttribute|`msdyn_solutionhealthruleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_solutionhealthrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses"></a> msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_solutionhealthruleargument msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses](msdyn_solutionhealthruleargument.md#BKMK_msdyn_solutionhealthruleargument_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleargument`|
|ReferencedAttribute|`msdyn_solutionhealthruleargumentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_solutionhealthruleargument`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses"></a> msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_solutionhealthruleset msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses](msdyn_solutionhealthruleset.md#BKMK_msdyn_solutionhealthruleset_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleset`|
|ReferencedAttribute|`msdyn_solutionhealthrulesetid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_solutionhealthruleset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_tour_PrincipalObjectAttributeAccesses"></a> msdyn_tour_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_tour msdyn_tour_PrincipalObjectAttributeAccesses](msdyn_tour.md#BKMK_msdyn_tour_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_tour`|
|ReferencedAttribute|`msdyn_tourid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_tour`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses"></a> msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_virtualtablecolumncandidate msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses](msdyn_virtualtablecolumncandidate.md#BKMK_msdyn_virtualtablecolumncandidate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencedAttribute|`msdyn_virtualtablecolumncandidateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_virtualtablecolumncandidate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses"></a> msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdyn_workflowactionstatus msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses](msdyn_workflowactionstatus.md#BKMK_msdyn_workflowactionstatus_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_workflowactionstatus`|
|ReferencedAttribute|`msdyn_workflowactionstatusid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_workflowactionstatus`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdynce_botcontent_PrincipalObjectAttributeAccesses"></a> msdynce_botcontent_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msdynce_botcontent msdynce_botcontent_PrincipalObjectAttributeAccesses](msdynce_botcontent.md#BKMK_msdynce_botcontent_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msdynce_botcontent`|
|ReferencedAttribute|`msdynce_botcontentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdynce_botcontent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses"></a> msgraphresourcetosubscription_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [msgraphresourcetosubscription msgraphresourcetosubscription_PrincipalObjectAttributeAccesses](msgraphresourcetosubscription.md#BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`msgraphresourcetosubscription`|
|ReferencedAttribute|`msgraphresourcetosubscriptionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msgraphresourcetosubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses"></a> mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [mspcat_catalogsubmissionfiles mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_catalogsubmissionfiles`|
|ReferencedAttribute|`mspcat_catalogsubmissionfilesid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_mspcat_catalogsubmissionfiles`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_packagestore_PrincipalObjectAttributeAccesses"></a> mspcat_packagestore_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [mspcat_packagestore mspcat_packagestore_PrincipalObjectAttributeAccesses](mspcat_packagestore.md#BKMK_mspcat_packagestore_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_packagestore`|
|ReferencedAttribute|`mspcat_packagestoreid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_mspcat_packagestore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncfnostate_PrincipalObjectAttributeAccesses"></a> organizationdatasyncfnostate_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [organizationdatasyncfnostate organizationdatasyncfnostate_PrincipalObjectAttributeAccesses](organizationdatasyncfnostate.md#BKMK_organizationdatasyncfnostate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncfnostate`|
|ReferencedAttribute|`organizationdatasyncfnostateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_organizationdatasyncfnostate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses"></a> organizationdatasyncstate_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [organizationdatasyncstate organizationdatasyncstate_PrincipalObjectAttributeAccesses](organizationdatasyncstate.md#BKMK_organizationdatasyncstate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncstate`|
|ReferencedAttribute|`organizationdatasyncstateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_organizationdatasyncstate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses"></a> organizationdatasyncsubscription_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [organizationdatasyncsubscription organizationdatasyncsubscription_PrincipalObjectAttributeAccesses](organizationdatasyncsubscription.md#BKMK_organizationdatasyncsubscription_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscription`|
|ReferencedAttribute|`organizationdatasyncsubscriptionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_organizationdatasyncsubscription`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses"></a> organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [organizationdatasyncsubscriptionentity organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses](organizationdatasyncsubscriptionentity.md#BKMK_organizationdatasyncsubscriptionentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionentity`|
|ReferencedAttribute|`organizationdatasyncsubscriptionentityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_organizationdatasyncsubscriptionentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses"></a> organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [organizationdatasyncsubscriptionfnotable organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses](organizationdatasyncsubscriptionfnotable.md#BKMK_organizationdatasyncsubscriptionfnotable_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`organizationdatasyncsubscriptionfnotable`|
|ReferencedAttribute|`organizationdatasyncsubscriptionfnotableid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_organizationdatasyncsubscriptionfnotable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_package_PrincipalObjectAttributeAccesses"></a> package_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [package package_PrincipalObjectAttributeAccesses](package.md#BKMK_package_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`package`|
|ReferencedAttribute|`packageid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_package`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_packagehistory_PrincipalObjectAttributeAccesses"></a> packagehistory_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [packagehistory packagehistory_PrincipalObjectAttributeAccesses](packagehistory.md#BKMK_packagehistory_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`packagehistory`|
|ReferencedAttribute|`packagehistoryid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_packagehistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_phonecall_principalobjectattributeaccess"></a> phonecall_principalobjectattributeaccess

One-To-Many Relationship: [phonecall phonecall_principalobjectattributeaccess](phonecall.md#BKMK_phonecall_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannerbusinessscenario_PrincipalObjectAttributeAccesses"></a> plannerbusinessscenario_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [plannerbusinessscenario plannerbusinessscenario_PrincipalObjectAttributeAccesses](plannerbusinessscenario.md#BKMK_plannerbusinessscenario_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`plannerbusinessscenario`|
|ReferencedAttribute|`plannerbusinessscenarioid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_plannerbusinessscenario`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plannersyncaction_PrincipalObjectAttributeAccesses"></a> plannersyncaction_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [plannersyncaction plannersyncaction_PrincipalObjectAttributeAccesses](plannersyncaction.md#BKMK_plannersyncaction_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`plannersyncaction`|
|ReferencedAttribute|`plannersyncactionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_plannersyncaction`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plugin_PrincipalObjectAttributeAccesses"></a> plugin_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [plugin plugin_PrincipalObjectAttributeAccesses](plugin.md#BKMK_plugin_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`plugin`|
|ReferencedAttribute|`pluginid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_plugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_pluginpackage_PrincipalObjectAttributeAccesses"></a> pluginpackage_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [pluginpackage pluginpackage_PrincipalObjectAttributeAccesses](pluginpackage.md#BKMK_pluginpackage_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`pluginpackage`|
|ReferencedAttribute|`pluginpackageid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_pluginpackage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_position_principalobjectattributeaccess"></a> position_principalobjectattributeaccess

One-To-Many Relationship: [position position_principalobjectattributeaccess](position.md#BKMK_position_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`position`|
|ReferencedAttribute|`positionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_position`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidataset_PrincipalObjectAttributeAccesses"></a> powerbidataset_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerbidataset powerbidataset_PrincipalObjectAttributeAccesses](powerbidataset.md#BKMK_powerbidataset_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidataset`|
|ReferencedAttribute|`powerbidatasetid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerbidataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidatasetapdx_PrincipalObjectAttributeAccesses"></a> powerbidatasetapdx_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerbidatasetapdx powerbidatasetapdx_PrincipalObjectAttributeAccesses](powerbidatasetapdx.md#BKMK_powerbidatasetapdx_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidatasetapdx`|
|ReferencedAttribute|`powerbidatasetapdxid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerbidatasetapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbimashupparameter_PrincipalObjectAttributeAccesses"></a> powerbimashupparameter_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerbimashupparameter powerbimashupparameter_PrincipalObjectAttributeAccesses](powerbimashupparameter.md#BKMK_powerbimashupparameter_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbimashupparameter`|
|ReferencedAttribute|`powerbimashupparameterid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerbimashupparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireport_PrincipalObjectAttributeAccesses"></a> powerbireport_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerbireport powerbireport_PrincipalObjectAttributeAccesses](powerbireport.md#BKMK_powerbireport_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireport`|
|ReferencedAttribute|`powerbireportid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerbireport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireportapdx_PrincipalObjectAttributeAccesses"></a> powerbireportapdx_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerbireportapdx powerbireportapdx_PrincipalObjectAttributeAccesses](powerbireportapdx.md#BKMK_powerbireportapdx_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireportapdx`|
|ReferencedAttribute|`powerbireportapdxid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerbireportapdx`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerfxrule_PrincipalObjectAttributeAccesses"></a> powerfxrule_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerfxrule powerfxrule_PrincipalObjectAttributeAccesses](powerfxrule.md#BKMK_powerfxrule_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerfxrule`|
|ReferencedAttribute|`powerfxruleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerfxrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagecomponent_PrincipalObjectAttributeAccesses"></a> powerpagecomponent_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerpagecomponent powerpagecomponent_PrincipalObjectAttributeAccesses](powerpagecomponent.md#BKMK_powerpagecomponent_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagecomponent`|
|ReferencedAttribute|`powerpagecomponentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerpagecomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesite_PrincipalObjectAttributeAccesses"></a> powerpagesite_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerpagesite powerpagesite_PrincipalObjectAttributeAccesses](powerpagesite.md#BKMK_powerpagesite_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesite`|
|ReferencedAttribute|`powerpagesiteid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerpagesite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitelanguage_PrincipalObjectAttributeAccesses"></a> powerpagesitelanguage_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerpagesitelanguage powerpagesitelanguage_PrincipalObjectAttributeAccesses](powerpagesitelanguage.md#BKMK_powerpagesitelanguage_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitelanguage`|
|ReferencedAttribute|`powerpagesitelanguageid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerpagesitelanguage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitepublished_PrincipalObjectAttributeAccesses"></a> powerpagesitepublished_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerpagesitepublished powerpagesitepublished_PrincipalObjectAttributeAccesses](powerpagesitepublished.md#BKMK_powerpagesitepublished_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitepublished`|
|ReferencedAttribute|`powerpagesitepublishedid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerpagesitepublished`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesmanagedidentity_PrincipalObjectAttributeAccesses"></a> powerpagesmanagedidentity_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerpagesmanagedidentity powerpagesmanagedidentity_PrincipalObjectAttributeAccesses](powerpagesmanagedidentity.md#BKMK_powerpagesmanagedidentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesmanagedidentity`|
|ReferencedAttribute|`powerpagesmanagedidentityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerpagesmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesscanreport_PrincipalObjectAttributeAccesses"></a> powerpagesscanreport_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [powerpagesscanreport powerpagesscanreport_PrincipalObjectAttributeAccesses](powerpagesscanreport.md#BKMK_powerpagesscanreport_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesscanreport`|
|ReferencedAttribute|`powerpagesscanreportid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerpagesscanreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerlog_PrincipalObjectAttributeAccesses"></a> privilegecheckerlog_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [privilegecheckerlog privilegecheckerlog_PrincipalObjectAttributeAccesses](privilegecheckerlog.md#BKMK_privilegecheckerlog_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerlog`|
|ReferencedAttribute|`privilegecheckerlogid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_privilegecheckerlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegecheckerrun_PrincipalObjectAttributeAccesses"></a> privilegecheckerrun_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [privilegecheckerrun privilegecheckerrun_PrincipalObjectAttributeAccesses](privilegecheckerrun.md#BKMK_privilegecheckerrun_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegecheckerrun`|
|ReferencedAttribute|`privilegecheckerrunid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_privilegecheckerrun`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_privilegesremovalsetting_PrincipalObjectAttributeAccesses"></a> privilegesremovalsetting_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [privilegesremovalsetting privilegesremovalsetting_PrincipalObjectAttributeAccesses](privilegesremovalsetting.md#BKMK_privilegesremovalsetting_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`privilegesremovalsetting`|
|ReferencedAttribute|`privilegesremovalsettingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_privilegesremovalsetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstageparameter_PrincipalObjectAttributeAccesses"></a> processstageparameter_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [processstageparameter processstageparameter_PrincipalObjectAttributeAccesses](processstageparameter.md#BKMK_processstageparameter_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`processstageparameter`|
|ReferencedAttribute|`processstageparameterid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_processstageparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses"></a> provisionlanguageforuser_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [provisionlanguageforuser provisionlanguageforuser_PrincipalObjectAttributeAccesses](provisionlanguageforuser.md#BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`provisionlanguageforuser`|
|ReferencedAttribute|`provisionlanguageforuserid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_provisionlanguageforuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_queue_principalobjectattributeaccess"></a> queue_principalobjectattributeaccess

One-To-Many Relationship: [queue queue_principalobjectattributeaccess](queue.md#BKMK_queue_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_queue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_queueitem_principalobjectattributeaccess"></a> queueitem_principalobjectattributeaccess

One-To-Many Relationship: [queueitem queueitem_principalobjectattributeaccess](queueitem.md#BKMK_queueitem_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`queueitem`|
|ReferencedAttribute|`queueitemid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_queueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recordfilter_PrincipalObjectAttributeAccesses"></a> recordfilter_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [recordfilter recordfilter_PrincipalObjectAttributeAccesses](recordfilter.md#BKMK_recordfilter_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`recordfilter`|
|ReferencedAttribute|`recordfilterid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_recordfilter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recurringappointmentmaster_principalobjectattributeaccess"></a> recurringappointmentmaster_principalobjectattributeaccess

One-To-Many Relationship: [recurringappointmentmaster recurringappointmentmaster_principalobjectattributeaccess](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`recurringappointmentmaster`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_recurringappointmentmaster`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_recyclebinconfig_PrincipalObjectAttributeAccesses"></a> recyclebinconfig_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [recyclebinconfig recyclebinconfig_PrincipalObjectAttributeAccesses](recyclebinconfig.md#BKMK_recyclebinconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`recyclebinconfig`|
|ReferencedAttribute|`recyclebinconfigid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_recyclebinconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_relationshipattribute_PrincipalObjectAttributeAccesses"></a> relationshipattribute_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [relationshipattribute relationshipattribute_PrincipalObjectAttributeAccesses](relationshipattribute.md#BKMK_relationshipattribute_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`relationshipattribute`|
|ReferencedAttribute|`relationshipattributeid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_relationshipattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_reportcategory_principalobjectattributeaccess"></a> reportcategory_principalobjectattributeaccess

One-To-Many Relationship: [reportcategory reportcategory_principalobjectattributeaccess](reportcategory.md#BKMK_reportcategory_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`reportcategory`|
|ReferencedAttribute|`reportcategoryid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_reportcategory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_reportparameter_PrincipalObjectAttributeAccesses"></a> reportparameter_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [reportparameter reportparameter_PrincipalObjectAttributeAccesses](reportparameter.md#BKMK_reportparameter_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`reportparameter`|
|ReferencedAttribute|`reportparameterid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_reportparameter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retaineddataexcel_PrincipalObjectAttributeAccesses"></a> retaineddataexcel_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [retaineddataexcel retaineddataexcel_PrincipalObjectAttributeAccesses](retaineddataexcel.md#BKMK_retaineddataexcel_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`retaineddataexcel`|
|ReferencedAttribute|`retaineddataexcelid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_retaineddataexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionconfig_PrincipalObjectAttributeAccesses"></a> retentionconfig_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [retentionconfig retentionconfig_PrincipalObjectAttributeAccesses](retentionconfig.md#BKMK_retentionconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionconfig`|
|ReferencedAttribute|`retentionconfigid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_retentionconfig`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionfailuredetail_PrincipalObjectAttributeAccesses"></a> retentionfailuredetail_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [retentionfailuredetail retentionfailuredetail_PrincipalObjectAttributeAccesses](retentionfailuredetail.md#BKMK_retentionfailuredetail_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionfailuredetail`|
|ReferencedAttribute|`retentionfailuredetailid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_retentionfailuredetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperation_PrincipalObjectAttributeAccesses"></a> retentionoperation_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [retentionoperation retentionoperation_PrincipalObjectAttributeAccesses](retentionoperation.md#BKMK_retentionoperation_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperation`|
|ReferencedAttribute|`retentionoperationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_retentionoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionoperationdetail_PrincipalObjectAttributeAccesses"></a> retentionoperationdetail_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [retentionoperationdetail retentionoperationdetail_PrincipalObjectAttributeAccesses](retentionoperationdetail.md#BKMK_retentionoperationdetail_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionoperationdetail`|
|ReferencedAttribute|`retentionoperationdetailid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_retentionoperationdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retentionsuccessdetail_PrincipalObjectAttributeAccesses"></a> retentionsuccessdetail_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [retentionsuccessdetail retentionsuccessdetail_PrincipalObjectAttributeAccesses](retentionsuccessdetail.md#BKMK_retentionsuccessdetail_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`retentionsuccessdetail`|
|ReferencedAttribute|`retentionsuccessdetailid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_retentionsuccessdetail`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_roleeditorlayout_PrincipalObjectAttributeAccesses"></a> roleeditorlayout_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [roleeditorlayout roleeditorlayout_PrincipalObjectAttributeAccesses](roleeditorlayout.md#BKMK_roleeditorlayout_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`roleeditorlayout`|
|ReferencedAttribute|`roleeditorlayoutid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_roleeditorlayout`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_savingrule_PrincipalObjectAttributeAccesses"></a> savingrule_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [savingrule savingrule_PrincipalObjectAttributeAccesses](savingrule.md#BKMK_savingrule_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`savingrule`|
|ReferencedAttribute|`savingruleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_savingrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchattributesettings_PrincipalObjectAttributeAccesses"></a> searchattributesettings_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [searchattributesettings searchattributesettings_PrincipalObjectAttributeAccesses](searchattributesettings.md#BKMK_searchattributesettings_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`searchattributesettings`|
|ReferencedAttribute|`searchattributesettingsid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_searchattributesettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchcustomanalyzer_PrincipalObjectAttributeAccesses"></a> searchcustomanalyzer_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [searchcustomanalyzer searchcustomanalyzer_PrincipalObjectAttributeAccesses](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`searchcustomanalyzer`|
|ReferencedAttribute|`searchcustomanalyzerid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_searchcustomanalyzer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchrelationshipsettings_PrincipalObjectAttributeAccesses"></a> searchrelationshipsettings_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [searchrelationshipsettings searchrelationshipsettings_PrincipalObjectAttributeAccesses](searchrelationshipsettings.md#BKMK_searchrelationshipsettings_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`searchrelationshipsettings`|
|ReferencedAttribute|`searchrelationshipsettingsid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_searchrelationshipsettings`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplan_PrincipalObjectAttributeAccesses"></a> serviceplan_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [serviceplan serviceplan_PrincipalObjectAttributeAccesses](serviceplan.md#BKMK_serviceplan_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplan`|
|ReferencedAttribute|`serviceplanid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_serviceplan`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceplanmapping_PrincipalObjectAttributeAccesses"></a> serviceplanmapping_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [serviceplanmapping serviceplanmapping_PrincipalObjectAttributeAccesses](serviceplanmapping.md#BKMK_serviceplanmapping_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceplanmapping`|
|ReferencedAttribute|`serviceplanmappingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_serviceplanmapping`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedlinksetting_PrincipalObjectAttributeAccesses"></a> sharedlinksetting_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [sharedlinksetting sharedlinksetting_PrincipalObjectAttributeAccesses](sharedlinksetting.md#BKMK_sharedlinksetting_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedlinksetting`|
|ReferencedAttribute|`sharedlinksettingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_sharedlinksetting`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedobject_PrincipalObjectAttributeAccesses"></a> sharedobject_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [sharedobject sharedobject_PrincipalObjectAttributeAccesses](sharedobject.md#BKMK_sharedobject_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedobject`|
|ReferencedAttribute|`sharedobjectid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_sharedobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspace_PrincipalObjectAttributeAccesses"></a> sharedworkspace_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [sharedworkspace sharedworkspace_PrincipalObjectAttributeAccesses](sharedworkspace.md#BKMK_sharedworkspace_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspace`|
|ReferencedAttribute|`sharedworkspaceid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_sharedworkspace`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharedworkspacepool_PrincipalObjectAttributeAccesses"></a> sharedworkspacepool_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [sharedworkspacepool sharedworkspacepool_PrincipalObjectAttributeAccesses](sharedworkspacepool.md#BKMK_sharedworkspacepool_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`sharedworkspacepool`|
|ReferencedAttribute|`sharedworkspacepoolid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_sharedworkspacepool`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharepointdocumentlocation_principalobjectattributeaccess"></a> sharepointdocumentlocation_principalobjectattributeaccess

One-To-Many Relationship: [sharepointdocumentlocation sharepointdocumentlocation_principalobjectattributeaccess](sharepointdocumentlocation.md#BKMK_sharepointdocumentlocation_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointdocumentlocation`|
|ReferencedAttribute|`sharepointdocumentlocationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_sharepointdocumentlocation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharepointmanagedidentity_PrincipalObjectAttributeAccesses"></a> sharepointmanagedidentity_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [sharepointmanagedidentity sharepointmanagedidentity_PrincipalObjectAttributeAccesses](sharepointmanagedidentity.md#BKMK_sharepointmanagedidentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointmanagedidentity`|
|ReferencedAttribute|`sharepointmanagedidentityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_sharepointmanagedidentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharepointsite_principalobjectattributeaccess"></a> sharepointsite_principalobjectattributeaccess

One-To-Many Relationship: [sharepointsite sharepointsite_principalobjectattributeaccess](sharepointsite.md#BKMK_sharepointsite_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointsite`|
|ReferencedAttribute|`sharepointsiteid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_sharepointsite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sideloadedaiplugin_PrincipalObjectAttributeAccesses"></a> sideloadedaiplugin_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [sideloadedaiplugin sideloadedaiplugin_PrincipalObjectAttributeAccesses](sideloadedaiplugin.md#BKMK_sideloadedaiplugin_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`sideloadedaiplugin`|
|ReferencedAttribute|`sideloadedaipluginid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_sideloadedaiplugin`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_socialactivity_principalobjectattributeaccess"></a> socialactivity_principalobjectattributeaccess

One-To-Many Relationship: [socialactivity socialactivity_principalobjectattributeaccess](socialactivity.md#BKMK_socialactivity_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_socialactivity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_socialprofile_principalobjectattributeaccess"></a> socialprofile_principalobjectattributeaccess

One-To-Many Relationship: [socialprofile socialprofile_principalobjectattributeaccess](socialprofile.md#BKMK_socialprofile_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`socialprofile`|
|ReferencedAttribute|`socialprofileid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_socialprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [solutioncomponentattributeconfiguration solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentattributeconfiguration`|
|ReferencedAttribute|`solutioncomponentattributeconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_solutioncomponentattributeconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [solutioncomponentbatchconfiguration solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses](solutioncomponentbatchconfiguration.md#BKMK_solutioncomponentbatchconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentbatchconfiguration`|
|ReferencedAttribute|`solutioncomponentbatchconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_solutioncomponentbatchconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [solutioncomponentconfiguration solutioncomponentconfiguration_PrincipalObjectAttributeAccesses](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentconfiguration`|
|ReferencedAttribute|`solutioncomponentconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_solutioncomponentconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [solutioncomponentrelationshipconfiguration solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses](solutioncomponentrelationshipconfiguration.md#BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentrelationshipconfiguration`|
|ReferencedAttribute|`solutioncomponentrelationshipconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_solutioncomponentrelationshipconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentity_PrincipalObjectAttributeAccesses"></a> stagedentity_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [stagedentity stagedentity_PrincipalObjectAttributeAccesses](stagedentity.md#BKMK_stagedentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentity`|
|ReferencedAttribute|`stagedentityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_stagedentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses"></a> stagedentityattribute_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [stagedentityattribute stagedentityattribute_PrincipalObjectAttributeAccesses](stagedentityattribute.md#BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedentityattribute`|
|ReferencedAttribute|`stagedentityattributeid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_stagedentityattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses"></a> stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [stagedmetadataasyncoperation stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses](stagedmetadataasyncoperation.md#BKMK_stagedmetadataasyncoperation_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`stagedmetadataasyncoperation`|
|ReferencedAttribute|`stagedmetadataasyncoperationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_stagedmetadataasyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagesolutionupload_PrincipalObjectAttributeAccesses"></a> stagesolutionupload_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [stagesolutionupload stagesolutionupload_PrincipalObjectAttributeAccesses](stagesolutionupload.md#BKMK_stagesolutionupload_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`stagesolutionupload`|
|ReferencedAttribute|`stagesolutionuploadid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_stagesolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_supportusertable_PrincipalObjectAttributeAccesses"></a> supportusertable_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [supportusertable supportusertable_PrincipalObjectAttributeAccesses](supportusertable.md#BKMK_supportusertable_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`supportusertable`|
|ReferencedAttribute|`supportusertableid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_supportusertable`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapsedatabase_PrincipalObjectAttributeAccesses"></a> synapsedatabase_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [synapsedatabase synapsedatabase_PrincipalObjectAttributeAccesses](synapsedatabase.md#BKMK_synapsedatabase_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`synapsedatabase`|
|ReferencedAttribute|`synapsedatabaseid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_synapsedatabase`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses"></a> synapselinkexternaltablestate_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [synapselinkexternaltablestate synapselinkexternaltablestate_PrincipalObjectAttributeAccesses](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkexternaltablestate`|
|ReferencedAttribute|`synapselinkexternaltablestateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_synapselinkexternaltablestate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses"></a> synapselinkprofile_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [synapselinkprofile synapselinkprofile_PrincipalObjectAttributeAccesses](synapselinkprofile.md#BKMK_synapselinkprofile_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofile`|
|ReferencedAttribute|`synapselinkprofileid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_synapselinkprofile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentity_PrincipalObjectAttributeAccesses"></a> synapselinkprofileentity_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [synapselinkprofileentity synapselinkprofileentity_PrincipalObjectAttributeAccesses](synapselinkprofileentity.md#BKMK_synapselinkprofileentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentity`|
|ReferencedAttribute|`synapselinkprofileentityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_synapselinkprofileentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses"></a> synapselinkprofileentitystate_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [synapselinkprofileentitystate synapselinkprofileentitystate_PrincipalObjectAttributeAccesses](synapselinkprofileentitystate.md#BKMK_synapselinkprofileentitystate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofileentitystate`|
|ReferencedAttribute|`synapselinkprofileentitystateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_synapselinkprofileentitystate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_synapselinkschedule_PrincipalObjectAttributeAccesses"></a> synapselinkschedule_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [synapselinkschedule synapselinkschedule_PrincipalObjectAttributeAccesses](synapselinkschedule.md#BKMK_synapselinkschedule_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkschedule`|
|ReferencedAttribute|`synapselinkscheduleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_synapselinkschedule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuser_principalobjectattributeaccess"></a> systemuser_principalobjectattributeaccess

One-To-Many Relationship: [systemuser systemuser_principalobjectattributeaccess](systemuser.md#BKMK_systemuser_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuser_principalobjectattributeaccess_principalid"></a> systemuser_principalobjectattributeaccess_principalid

One-To-Many Relationship: [systemuser systemuser_principalobjectattributeaccess_principalid](systemuser.md#BKMK_systemuser_principalobjectattributeaccess_principalid)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`principalid`|
|ReferencingEntityNavigationPropertyName|`principalid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses"></a> systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [systemuserauthorizationchangetracker systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses](systemuserauthorizationchangetracker.md#BKMK_systemuserauthorizationchangetracker_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuserauthorizationchangetracker`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_systemuserauthorizationchangetracker`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_tag_PrincipalObjectAttributeAccesses"></a> tag_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [tag tag_PrincipalObjectAttributeAccesses](tag.md#BKMK_tag_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`tag`|
|ReferencedAttribute|`tagid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_tag`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedflowsession_PrincipalObjectAttributeAccesses"></a> taggedflowsession_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [taggedflowsession taggedflowsession_PrincipalObjectAttributeAccesses](taggedflowsession.md#BKMK_taggedflowsession_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedflowsession`|
|ReferencedAttribute|`taggedflowsessionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_taggedflowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_taggedprocess_PrincipalObjectAttributeAccesses"></a> taggedprocess_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [taggedprocess taggedprocess_PrincipalObjectAttributeAccesses](taggedprocess.md#BKMK_taggedprocess_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`taggedprocess`|
|ReferencedAttribute|`taggedprocessid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_taggedprocess`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_task_principalobjectattributeaccess"></a> task_principalobjectattributeaccess

One-To-Many Relationship: [task task_principalobjectattributeaccess](task.md#BKMK_task_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_principalobjectattributeaccess"></a> team_principalobjectattributeaccess

One-To-Many Relationship: [team team_principalobjectattributeaccess](team.md#BKMK_team_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_principalobjectattributeaccess_principalid"></a> team_principalobjectattributeaccess_principalid

One-To-Many Relationship: [team team_principalobjectattributeaccess_principalid](team.md#BKMK_team_principalobjectattributeaccess_principalid)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`principalid`|
|ReferencingEntityNavigationPropertyName|`principalid_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses"></a> teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [teammobileofflineprofilemembership teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses](teammobileofflineprofilemembership.md#BKMK_teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`teammobileofflineprofilemembership`|
|ReferencedAttribute|`teammobileofflineprofilemembershipid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_teammobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_territory_principalobjectattributeaccess"></a> territory_principalobjectattributeaccess

One-To-Many Relationship: [territory territory_principalobjectattributeaccess](territory.md#BKMK_territory_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencedEntity|`territory`|
|ReferencedAttribute|`territoryid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_territory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchentity_PrincipalObjectAttributeAccesses"></a> unstructuredfilesearchentity_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [unstructuredfilesearchentity unstructuredfilesearchentity_PrincipalObjectAttributeAccesses](unstructuredfilesearchentity.md#BKMK_unstructuredfilesearchentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchentity`|
|ReferencedAttribute|`unstructuredfilesearchentityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_unstructuredfilesearchentity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses"></a> unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [unstructuredfilesearchrecord unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses](unstructuredfilesearchrecord.md#BKMK_unstructuredfilesearchrecord_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`unstructuredfilesearchrecord`|
|ReferencedAttribute|`unstructuredfilesearchrecordid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_unstructuredfilesearchrecord`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses"></a> usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [usermobileofflineprofilemembership usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses](usermobileofflineprofilemembership.md#BKMK_usermobileofflineprofilemembership_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`usermobileofflineprofilemembership`|
|ReferencedAttribute|`usermobileofflineprofilemembershipid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_usermobileofflineprofilemembership`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_userrating_PrincipalObjectAttributeAccesses"></a> userrating_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [userrating userrating_PrincipalObjectAttributeAccesses](userrating.md#BKMK_userrating_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`userrating`|
|ReferencedAttribute|`userratingid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_userrating`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_viewasexamplequestion_PrincipalObjectAttributeAccesses"></a> viewasexamplequestion_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [viewasexamplequestion viewasexamplequestion_PrincipalObjectAttributeAccesses](viewasexamplequestion.md#BKMK_viewasexamplequestion_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`viewasexamplequestion`|
|ReferencedAttribute|`viewasexamplequestionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_viewasexamplequestion`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_virtualentitymetadata_PrincipalObjectAttributeAccesses"></a> virtualentitymetadata_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [virtualentitymetadata virtualentitymetadata_PrincipalObjectAttributeAccesses](virtualentitymetadata.md#BKMK_virtualentitymetadata_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`virtualentitymetadata`|
|ReferencedAttribute|`virtualentitymetadataid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_virtualentitymetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowbinary_PrincipalObjectAttributeAccesses"></a> workflowbinary_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [workflowbinary workflowbinary_PrincipalObjectAttributeAccesses](workflowbinary.md#BKMK_workflowbinary_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowbinary`|
|ReferencedAttribute|`workflowbinaryid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_workflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowmetadata_PrincipalObjectAttributeAccesses"></a> workflowmetadata_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [workflowmetadata workflowmetadata_PrincipalObjectAttributeAccesses](workflowmetadata.md#BKMK_workflowmetadata_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowmetadata`|
|ReferencedAttribute|`workflowmetadataid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_workflowmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueue_PrincipalObjectAttributeAccesses"></a> workqueue_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [workqueue workqueue_PrincipalObjectAttributeAccesses](workqueue.md#BKMK_workqueue_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueue`|
|ReferencedAttribute|`workqueueid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_workqueue`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workqueueitem_PrincipalObjectAttributeAccesses"></a> workqueueitem_PrincipalObjectAttributeAccesses

One-To-Many Relationship: [workqueueitem workqueueitem_PrincipalObjectAttributeAccesses](workqueueitem.md#BKMK_workqueueitem_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencedEntity|`workqueueitem`|
|ReferencedAttribute|`workqueueitemid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_workqueueitem`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.principalobjectattributeaccess?displayProperty=fullName>
