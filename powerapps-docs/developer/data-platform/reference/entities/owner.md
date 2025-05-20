---
title: "Owner table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Owner table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Owner table/entity reference (Microsoft Dataverse)

Group of undeleted system users and undeleted teams. Owners can be used to control access to specific objects.

## Messages

The following table lists the messages for the Owner table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the Owner table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Owner** |
| **DisplayCollectionName** | **Owners** |
| **SchemaName** | `Owner` |
| **CollectionSchemaName** | `Owners` |
| **EntitySetName** | `owners`|
| **LogicalName** | `owner` |
| **LogicalCollectionName** | `owners` |
| **PrimaryIdAttribute** | `ownerid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier for the Owner: systemuserid or teamid.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [Name](#BKMK_Name)
- [OwnerIdType](#BKMK_OwnerIdType)
- [VersionNumber](#BKMK_VersionNumber)
- [YomiName](#BKMK_YomiName)

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the Owner.**|
|DisplayName|**Owner Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

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

### <a name="BKMK_YomiName"></a> YomiName

|Property|Value|
|---|---|
|Description|**Pronunciation of the name of the owner, written in phonetic hiragana or katakana characters.**|
|DisplayName|**Yomi Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`yominame`|
|RequiredLevel|None|
|Type|String|
|Format|PhoneticGuide|
|FormatName|PhoneticGuide|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|160|

## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [ActionCardUserState_Owner](#BKMK_ActionCardUserState_Owner)
- [adx_inviteredemption_owner_ownerid](#BKMK_adx_inviteredemption_owner_ownerid)
- [adx_portalcomment_owner_ownerid](#BKMK_adx_portalcomment_owner_ownerid)
- [chat_owner_ownerid](#BKMK_chat_owner_ownerid)
- [owner_accounts](#BKMK_owner_accounts)
- [owner_actioncards](#BKMK_owner_actioncards)
- [owner_activityfileattachment](#BKMK_owner_activityfileattachment)
- [owner_activitypointers](#BKMK_owner_activitypointers)
- [owner_adx_invitation](#BKMK_owner_adx_invitation)
- [owner_adx_setting](#BKMK_owner_adx_setting)
- [owner_aiplugin](#BKMK_owner_aiplugin)
- [owner_aipluginauth](#BKMK_owner_aipluginauth)
- [owner_aipluginconversationstarter](#BKMK_owner_aipluginconversationstarter)
- [owner_aipluginconversationstartermapping](#BKMK_owner_aipluginconversationstartermapping)
- [owner_aipluginexternalschema](#BKMK_owner_aipluginexternalschema)
- [owner_aipluginexternalschemaproperty](#BKMK_owner_aipluginexternalschemaproperty)
- [owner_aiplugingovernance](#BKMK_owner_aiplugingovernance)
- [owner_aiplugingovernanceext](#BKMK_owner_aiplugingovernanceext)
- [owner_aiplugininstance](#BKMK_owner_aiplugininstance)
- [owner_aipluginoperation](#BKMK_owner_aipluginoperation)
- [owner_aipluginoperationparameter](#BKMK_owner_aipluginoperationparameter)
- [owner_aipluginoperationresponsetemplate](#BKMK_owner_aipluginoperationresponsetemplate)
- [owner_aipluginusersetting](#BKMK_owner_aipluginusersetting)
- [owner_annotations](#BKMK_owner_annotations)
- [owner_appnotification](#BKMK_owner_appnotification)
- [owner_appointments](#BKMK_owner_appointments)
- [owner_approvalprocess](#BKMK_owner_approvalprocess)
- [owner_approvalstageapproval](#BKMK_owner_approvalstageapproval)
- [owner_approvalstagecondition](#BKMK_owner_approvalstagecondition)
- [owner_approvalstageorder](#BKMK_owner_approvalstageorder)
- [owner_asyncoperations](#BKMK_owner_asyncoperations)
- [owner_bot](#BKMK_owner_bot)
- [owner_botcomponent](#BKMK_owner_botcomponent)
- [owner_botcomponentcollection](#BKMK_owner_botcomponentcollection)
- [owner_businessprocess](#BKMK_owner_businessprocess)
- [owner_callbackregistration](#BKMK_owner_callbackregistration)
- [owner_canvasapp](#BKMK_owner_canvasapp)
- [owner_card](#BKMK_owner_card)
- [owner_categories](#BKMK_owner_categories)
- [owner_certificatecredential](#BKMK_owner_certificatecredential)
- [owner_connectioninstance](#BKMK_owner_connectioninstance)
- [owner_connectionreference](#BKMK_owner_connectionreference)
- [owner_connections](#BKMK_owner_connections)
- [owner_connector](#BKMK_owner_connector)
- [owner_contacts](#BKMK_owner_contacts)
- [owner_conversationtranscript](#BKMK_owner_conversationtranscript)
- [owner_copilotglossaryterm](#BKMK_owner_copilotglossaryterm)
- [owner_copilotsynonyms](#BKMK_owner_copilotsynonyms)
- [owner_credential](#BKMK_owner_credential)
- [owner_customapi](#BKMK_owner_customapi)
- [owner_datalakefolder](#BKMK_owner_datalakefolder)
- [owner_desktopflowbinary](#BKMK_owner_desktopflowbinary)
- [owner_desktopflowmodule](#BKMK_owner_desktopflowmodule)
- [owner_duplicaterules](#BKMK_owner_duplicaterules)
- [owner_dvfilesearch](#BKMK_owner_dvfilesearch)
- [owner_dvfilesearchattribute](#BKMK_owner_dvfilesearchattribute)
- [owner_dvfilesearchentity](#BKMK_owner_dvfilesearchentity)
- [owner_dvtablesearch](#BKMK_owner_dvtablesearch)
- [owner_dvtablesearchattribute](#BKMK_owner_dvtablesearchattribute)
- [owner_dvtablesearchentity](#BKMK_owner_dvtablesearchentity)
- [owner_emails](#BKMK_owner_emails)
- [owner_emailserverprofile](#BKMK_owner_emailserverprofile)
- [owner_environmentvariabledefinition](#BKMK_owner_environmentvariabledefinition)
- [owner_exchangesyncidmapping](#BKMK_owner_exchangesyncidmapping)
- [owner_exportedexcel](#BKMK_owner_exportedexcel)
- [owner_exportsolutionupload](#BKMK_owner_exportsolutionupload)
- [owner_fabricaiskill](#BKMK_owner_fabricaiskill)
- [owner_faxes](#BKMK_owner_faxes)
- [owner_featurecontrolsetting](#BKMK_owner_featurecontrolsetting)
- [owner_federatedknowledgeconfiguration](#BKMK_owner_federatedknowledgeconfiguration)
- [owner_federatedknowledgeentityconfiguration](#BKMK_owner_federatedknowledgeentityconfiguration)
- [owner_feedback](#BKMK_owner_feedback)
- [owner_flowaggregation](#BKMK_owner_flowaggregation)
- [owner_flowcapacityassignment](#BKMK_owner_flowcapacityassignment)
- [owner_flowcredentialapplication](#BKMK_owner_flowcredentialapplication)
- [owner_flowevent](#BKMK_owner_flowevent)
- [owner_flowmachine](#BKMK_owner_flowmachine)
- [owner_flowmachinegroup](#BKMK_owner_flowmachinegroup)
- [owner_flowmachineimage](#BKMK_owner_flowmachineimage)
- [owner_flowmachineimageversion](#BKMK_owner_flowmachineimageversion)
- [owner_flowmachinenetwork](#BKMK_owner_flowmachinenetwork)
- [owner_flowrun](#BKMK_owner_flowrun)
- [owner_flowsession](#BKMK_owner_flowsession)
- [owner_fxexpression](#BKMK_owner_fxexpression)
- [owner_goal](#BKMK_owner_goal)
- [owner_goalrollupquery](#BKMK_owner_goalrollupquery)
- [owner_governanceconfiguration](#BKMK_owner_governanceconfiguration)
- [owner_importdatas](#BKMK_owner_importdatas)
- [owner_importfiles](#BKMK_owner_importfiles)
- [owner_importlogs](#BKMK_owner_importlogs)
- [owner_importmaps](#BKMK_owner_importmaps)
- [owner_imports](#BKMK_owner_imports)
- [owner_indexedtrait](#BKMK_owner_indexedtrait)
- [owner_interactionforemail](#BKMK_owner_interactionforemail)
- [owner_keyvaultreference](#BKMK_owner_keyvaultreference)
- [owner_knowledgearticle](#BKMK_owner_knowledgearticle)
- [owner_letters](#BKMK_owner_letters)
- [owner_mailbox](#BKMK_owner_mailbox)
- [owner_mailboxtrackingfolder](#BKMK_owner_mailboxtrackingfolder)
- [owner_mailmergetemplates](#BKMK_owner_mailmergetemplates)
- [owner_managedidentity](#BKMK_owner_managedidentity)
- [owner_msdyn_aibdataset](#BKMK_owner_msdyn_aibdataset)
- [owner_msdyn_aibdatasetfile](#BKMK_owner_msdyn_aibdatasetfile)
- [owner_msdyn_aibdatasetrecord](#BKMK_owner_msdyn_aibdatasetrecord)
- [owner_msdyn_aibdatasetscontainer](#BKMK_owner_msdyn_aibdatasetscontainer)
- [owner_msdyn_aibfeedbackloop](#BKMK_owner_msdyn_aibfeedbackloop)
- [owner_msdyn_aibfile](#BKMK_owner_msdyn_aibfile)
- [owner_msdyn_aibfileattacheddata](#BKMK_owner_msdyn_aibfileattacheddata)
- [owner_msdyn_aidataprocessingevent](#BKMK_owner_msdyn_aidataprocessingevent)
- [owner_msdyn_aievaluationconfiguration](#BKMK_owner_msdyn_aievaluationconfiguration)
- [owner_msdyn_aievaluationrun](#BKMK_owner_msdyn_aievaluationrun)
- [owner_msdyn_aievent](#BKMK_owner_msdyn_aievent)
- [owner_msdyn_aifptrainingdocument](#BKMK_owner_msdyn_aifptrainingdocument)
- [owner_msdyn_aimodel](#BKMK_owner_msdyn_aimodel)
- [owner_msdyn_aimodelcatalog](#BKMK_owner_msdyn_aimodelcatalog)
- [owner_msdyn_aiodimage](#BKMK_owner_msdyn_aiodimage)
- [owner_msdyn_aiodlabel](#BKMK_owner_msdyn_aiodlabel)
- [owner_msdyn_aiodtrainingboundingbox](#BKMK_owner_msdyn_aiodtrainingboundingbox)
- [owner_msdyn_aiodtrainingimage](#BKMK_owner_msdyn_aiodtrainingimage)
- [owner_msdyn_aitemplate](#BKMK_owner_msdyn_aitemplate)
- [owner_msdyn_aitestcase](#BKMK_owner_msdyn_aitestcase)
- [owner_msdyn_aitestcasedocument](#BKMK_owner_msdyn_aitestcasedocument)
- [owner_msdyn_aitestcaseinput](#BKMK_owner_msdyn_aitestcaseinput)
- [owner_msdyn_aitestrun](#BKMK_owner_msdyn_aitestrun)
- [owner_msdyn_aitestrunbatch](#BKMK_owner_msdyn_aitestrunbatch)
- [owner_msdyn_analysiscomponent](#BKMK_owner_msdyn_analysiscomponent)
- [owner_msdyn_analysisjob](#BKMK_owner_msdyn_analysisjob)
- [owner_msdyn_analysisoverride](#BKMK_owner_msdyn_analysisoverride)
- [owner_msdyn_analysisresult](#BKMK_owner_msdyn_analysisresult)
- [owner_msdyn_analysisresultdetail](#BKMK_owner_msdyn_analysisresultdetail)
- [owner_msdyn_copilotinteractions](#BKMK_owner_msdyn_copilotinteractions)
- [owner_msdyn_customcontrolextendedsettings](#BKMK_owner_msdyn_customcontrolextendedsettings)
- [owner_msdyn_dataflow](#BKMK_owner_msdyn_dataflow)
- [owner_msdyn_dataflow_datalakefolder](#BKMK_owner_msdyn_dataflow_datalakefolder)
- [owner_msdyn_dataflowconnectionreference](#BKMK_owner_msdyn_dataflowconnectionreference)
- [owner_msdyn_dataflowrefreshhistory](#BKMK_owner_msdyn_dataflowrefreshhistory)
- [owner_msdyn_dataflowtemplate](#BKMK_owner_msdyn_dataflowtemplate)
- [owner_msdyn_dmsrequest](#BKMK_owner_msdyn_dmsrequest)
- [owner_msdyn_dmsrequeststatus](#BKMK_owner_msdyn_dmsrequeststatus)
- [owner_msdyn_dmssyncrequest](#BKMK_owner_msdyn_dmssyncrequest)
- [owner_msdyn_dmssyncstatus](#BKMK_owner_msdyn_dmssyncstatus)
- [owner_msdyn_entitylinkchatconfiguration](#BKMK_owner_msdyn_entitylinkchatconfiguration)
- [owner_msdyn_entityrefreshhistory](#BKMK_owner_msdyn_entityrefreshhistory)
- [owner_msdyn_favoriteknowledgearticle](#BKMK_owner_msdyn_favoriteknowledgearticle)
- [owner_msdyn_federatedarticle](#BKMK_owner_msdyn_federatedarticle)
- [owner_msdyn_fileupload](#BKMK_owner_msdyn_fileupload)
- [owner_msdyn_flow_actionapprovalmodel](#BKMK_owner_msdyn_flow_actionapprovalmodel)
- [owner_msdyn_flow_approval](#BKMK_owner_msdyn_flow_approval)
- [owner_msdyn_flow_approvalrequest](#BKMK_owner_msdyn_flow_approvalrequest)
- [owner_msdyn_flow_approvalresponse](#BKMK_owner_msdyn_flow_approvalresponse)
- [owner_msdyn_flow_approvalstep](#BKMK_owner_msdyn_flow_approvalstep)
- [owner_msdyn_flow_awaitallactionapprovalmodel](#BKMK_owner_msdyn_flow_awaitallactionapprovalmodel)
- [owner_msdyn_flow_awaitallapprovalmodel](#BKMK_owner_msdyn_flow_awaitallapprovalmodel)
- [owner_msdyn_flow_basicapprovalmodel](#BKMK_owner_msdyn_flow_basicapprovalmodel)
- [owner_msdyn_flow_flowapproval](#BKMK_owner_msdyn_flow_flowapproval)
- [owner_msdyn_formmapping](#BKMK_owner_msdyn_formmapping)
- [owner_msdyn_function](#BKMK_owner_msdyn_function)
- [owner_msdyn_integratedsearchprovider](#BKMK_owner_msdyn_integratedsearchprovider)
- [owner_msdyn_kalanguagesetting](#BKMK_owner_msdyn_kalanguagesetting)
- [owner_msdyn_kbattachment](#BKMK_owner_msdyn_kbattachment)
- [owner_msdyn_kmfederatedsearchconfig](#BKMK_owner_msdyn_kmfederatedsearchconfig)
- [owner_msdyn_knowledgearticleimage](#BKMK_owner_msdyn_knowledgearticleimage)
- [owner_msdyn_knowledgearticletemplate](#BKMK_owner_msdyn_knowledgearticletemplate)
- [owner_msdyn_knowledgeassetconfiguration](#BKMK_owner_msdyn_knowledgeassetconfiguration)
- [owner_msdyn_knowledgeinteractioninsight](#BKMK_owner_msdyn_knowledgeinteractioninsight)
- [owner_msdyn_knowledgemanagementsetting](#BKMK_owner_msdyn_knowledgemanagementsetting)
- [owner_msdyn_knowledgepersonalfilter](#BKMK_owner_msdyn_knowledgepersonalfilter)
- [owner_msdyn_knowledgesearchfilter](#BKMK_owner_msdyn_knowledgesearchfilter)
- [owner_msdyn_knowledgesearchinsight](#BKMK_owner_msdyn_knowledgesearchinsight)
- [owner_msdyn_mobileapp](#BKMK_owner_msdyn_mobileapp)
- [owner_msdyn_pmanalysishistory](#BKMK_owner_msdyn_pmanalysishistory)
- [owner_msdyn_pmbusinessruleautomationconfig](#BKMK_owner_msdyn_pmbusinessruleautomationconfig)
- [owner_msdyn_pmcalendar](#BKMK_owner_msdyn_pmcalendar)
- [owner_msdyn_pmcalendarversion](#BKMK_owner_msdyn_pmcalendarversion)
- [owner_msdyn_pminferredtask](#BKMK_owner_msdyn_pminferredtask)
- [owner_msdyn_pmprocessextendedmetadataversion](#BKMK_owner_msdyn_pmprocessextendedmetadataversion)
- [owner_msdyn_pmprocesstemplate](#BKMK_owner_msdyn_pmprocesstemplate)
- [owner_msdyn_pmprocessusersettings](#BKMK_owner_msdyn_pmprocessusersettings)
- [owner_msdyn_pmprocessversion](#BKMK_owner_msdyn_pmprocessversion)
- [owner_msdyn_pmrecording](#BKMK_owner_msdyn_pmrecording)
- [owner_msdyn_pmsimulation](#BKMK_owner_msdyn_pmsimulation)
- [owner_msdyn_pmtemplate](#BKMK_owner_msdyn_pmtemplate)
- [owner_msdyn_pmview](#BKMK_owner_msdyn_pmview)
- [owner_msdyn_qna](#BKMK_owner_msdyn_qna)
- [owner_msdyn_richtextfile](#BKMK_owner_msdyn_richtextfile)
- [owner_msdyn_salesforcestructuredobject](#BKMK_owner_msdyn_salesforcestructuredobject)
- [owner_msdyn_salesforcestructuredqnaconfig](#BKMK_owner_msdyn_salesforcestructuredqnaconfig)
- [owner_msdyn_schedule](#BKMK_owner_msdyn_schedule)
- [owner_msdyn_serviceconfiguration](#BKMK_owner_msdyn_serviceconfiguration)
- [owner_msdyn_slakpi](#BKMK_owner_msdyn_slakpi)
- [owner_msdyn_solutionhealthrule](#BKMK_owner_msdyn_solutionhealthrule)
- [owner_msdyn_solutionhealthruleargument](#BKMK_owner_msdyn_solutionhealthruleargument)
- [owner_msdyn_virtualtablecolumncandidate](#BKMK_owner_msdyn_virtualtablecolumncandidate)
- [owner_msdynce_botcontent](#BKMK_owner_msdynce_botcontent)
- [owner_mspcat_catalogsubmissionfiles](#BKMK_owner_mspcat_catalogsubmissionfiles)
- [owner_mspcat_packagestore](#BKMK_owner_mspcat_packagestore)
- [owner_nlsqregistration](#BKMK_owner_nlsqregistration)
- [owner_personaldocumenttemplates](#BKMK_owner_personaldocumenttemplates)
- [owner_phonecalls](#BKMK_owner_phonecalls)
- [owner_plannerbusinessscenario](#BKMK_owner_plannerbusinessscenario)
- [owner_plannersyncaction](#BKMK_owner_plannersyncaction)
- [owner_plugin](#BKMK_owner_plugin)
- [owner_postfollows](#BKMK_owner_postfollows)
- [owner_powerbidataset](#BKMK_owner_powerbidataset)
- [owner_powerbidatasetapdx](#BKMK_owner_powerbidatasetapdx)
- [owner_powerbimashupparameter](#BKMK_owner_powerbimashupparameter)
- [owner_powerbireport](#BKMK_owner_powerbireport)
- [owner_powerbireportapdx](#BKMK_owner_powerbireportapdx)
- [owner_powerfxrule](#BKMK_owner_powerfxrule)
- [owner_powerpagecomponent](#BKMK_owner_powerpagecomponent)
- [owner_powerpagesite](#BKMK_owner_powerpagesite)
- [owner_powerpagesitelanguage](#BKMK_owner_powerpagesitelanguage)
- [owner_powerpagesitepublished](#BKMK_owner_powerpagesitepublished)
- [owner_powerpageslog](#BKMK_owner_powerpageslog)
- [owner_powerpagesmanagedidentity](#BKMK_owner_powerpagesmanagedidentity)
- [owner_powerpagesscanreport](#BKMK_owner_powerpagesscanreport)
- [owner_powerpagessiteaifeedback](#BKMK_owner_powerpagessiteaifeedback)
- [owner_principalentitybusinessunitmap](#BKMK_owner_principalentitybusinessunitmap)
- [owner_privilegecheckerrun](#BKMK_owner_privilegecheckerrun)
- [owner_processsessions](#BKMK_owner_processsessions)
- [owner_processstageparameter](#BKMK_owner_processstageparameter)
- [owner_queues](#BKMK_owner_queues)
- [owner_recentlyused](#BKMK_owner_recentlyused)
- [owner_recurrencerules](#BKMK_owner_recurrencerules)
- [owner_recurringappointmentmasters](#BKMK_owner_recurringappointmentmasters)
- [owner_reports](#BKMK_owner_reports)
- [owner_retaineddataexcel](#BKMK_owner_retaineddataexcel)
- [owner_retentionconfig](#BKMK_owner_retentionconfig)
- [owner_retentionfailuredetail](#BKMK_owner_retentionfailuredetail)
- [owner_retentionoperation](#BKMK_owner_retentionoperation)
- [owner_retentionsuccessdetail](#BKMK_owner_retentionsuccessdetail)
- [owner_savingrule](#BKMK_owner_savingrule)
- [owner_sharepointdocumentlocation](#BKMK_owner_sharepointdocumentlocation)
- [owner_sharepointsite](#BKMK_owner_sharepointsite)
- [owner_sideloadedaiplugin](#BKMK_owner_sideloadedaiplugin)
- [owner_signal](#BKMK_owner_signal)
- [owner_slas](#BKMK_owner_slas)
- [owner_socialactivities](#BKMK_owner_socialactivities)
- [owner_SocialProfile](#BKMK_owner_SocialProfile)
- [owner_solutioncomponentbatchconfiguration](#BKMK_owner_solutioncomponentbatchconfiguration)
- [owner_stagesolutionupload](#BKMK_owner_stagesolutionupload)
- [owner_synapsedatabase](#BKMK_owner_synapsedatabase)
- [owner_SyncError](#BKMK_owner_SyncError)
- [owner_tag](#BKMK_owner_tag)
- [owner_taggedflowsession](#BKMK_owner_taggedflowsession)
- [owner_taggedprocess](#BKMK_owner_taggedprocess)
- [owner_tasks](#BKMK_owner_tasks)
- [owner_templates](#BKMK_owner_templates)
- [owner_trait](#BKMK_owner_trait)
- [owner_unstructuredfilesearchentity](#BKMK_owner_unstructuredfilesearchentity)
- [owner_unstructuredfilesearchrecord](#BKMK_owner_unstructuredfilesearchrecord)
- [owner_userform](#BKMK_owner_userform)
- [owner_userquerys](#BKMK_owner_userquerys)
- [owner_userqueryvisualizations](#BKMK_owner_userqueryvisualizations)
- [owner_workflowbinary](#BKMK_owner_workflowbinary)
- [owner_workflowmetadata](#BKMK_owner_workflowmetadata)
- [owner_workflows](#BKMK_owner_workflows)
- [owner_workqueue](#BKMK_owner_workqueue)
- [owner_workqueueitem](#BKMK_owner_workqueueitem)
- [slakpiinstance_owner](#BKMK_slakpiinstance_owner)

### <a name="BKMK_ActionCardUserState_Owner"></a> ActionCardUserState_Owner

Many-To-One Relationship: [actioncarduserstate ActionCardUserState_Owner](actioncarduserstate.md#BKMK_ActionCardUserState_Owner)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncarduserstate`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`ActionCardUserState_Owner`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_inviteredemption_owner_ownerid"></a> adx_inviteredemption_owner_ownerid

Many-To-One Relationship: [adx_inviteredemption adx_inviteredemption_owner_ownerid](adx_inviteredemption.md#BKMK_adx_inviteredemption_owner_ownerid)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`adx_inviteredemption_owner_ownerid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_portalcomment_owner_ownerid"></a> adx_portalcomment_owner_ownerid

Many-To-One Relationship: [adx_portalcomment adx_portalcomment_owner_ownerid](adx_portalcomment.md#BKMK_adx_portalcomment_owner_ownerid)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`adx_portalcomment_owner_ownerid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_chat_owner_ownerid"></a> chat_owner_ownerid

Many-To-One Relationship: [chat chat_owner_ownerid](chat.md#BKMK_chat_owner_ownerid)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`chat_owner_ownerid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_accounts"></a> owner_accounts

Many-To-One Relationship: [account owner_accounts](account.md#BKMK_owner_accounts)

|Property|Value|
|---|---|
|ReferencingEntity|`account`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_accounts`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_actioncards"></a> owner_actioncards

Many-To-One Relationship: [actioncard owner_actioncards](actioncard.md#BKMK_owner_actioncards)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncard`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_actioncards`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_activityfileattachment"></a> owner_activityfileattachment

Many-To-One Relationship: [activityfileattachment owner_activityfileattachment](activityfileattachment.md#BKMK_owner_activityfileattachment)

|Property|Value|
|---|---|
|ReferencingEntity|`activityfileattachment`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_activityfileattachment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_activitypointers"></a> owner_activitypointers

Many-To-One Relationship: [activitypointer owner_activitypointers](activitypointer.md#BKMK_owner_activitypointers)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_activitypointers`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_adx_invitation"></a> owner_adx_invitation

Many-To-One Relationship: [adx_invitation owner_adx_invitation](adx_invitation.md#BKMK_owner_adx_invitation)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_invitation`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_adx_invitation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_adx_setting"></a> owner_adx_setting

Many-To-One Relationship: [adx_setting owner_adx_setting](adx_setting.md#BKMK_owner_adx_setting)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_setting`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_adx_setting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aiplugin"></a> owner_aiplugin

Many-To-One Relationship: [aiplugin owner_aiplugin](aiplugin.md#BKMK_owner_aiplugin)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugin`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aiplugin`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aipluginauth"></a> owner_aipluginauth

Many-To-One Relationship: [aipluginauth owner_aipluginauth](aipluginauth.md#BKMK_owner_aipluginauth)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginauth`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aipluginauth`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aipluginconversationstarter"></a> owner_aipluginconversationstarter

Many-To-One Relationship: [aipluginconversationstarter owner_aipluginconversationstarter](aipluginconversationstarter.md#BKMK_owner_aipluginconversationstarter)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginconversationstarter`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aipluginconversationstarter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aipluginconversationstartermapping"></a> owner_aipluginconversationstartermapping

Many-To-One Relationship: [aipluginconversationstartermapping owner_aipluginconversationstartermapping](aipluginconversationstartermapping.md#BKMK_owner_aipluginconversationstartermapping)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginconversationstartermapping`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aipluginconversationstartermapping`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aipluginexternalschema"></a> owner_aipluginexternalschema

Many-To-One Relationship: [aipluginexternalschema owner_aipluginexternalschema](aipluginexternalschema.md#BKMK_owner_aipluginexternalschema)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginexternalschema`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aipluginexternalschema`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aipluginexternalschemaproperty"></a> owner_aipluginexternalschemaproperty

Many-To-One Relationship: [aipluginexternalschemaproperty owner_aipluginexternalschemaproperty](aipluginexternalschemaproperty.md#BKMK_owner_aipluginexternalschemaproperty)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginexternalschemaproperty`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aipluginexternalschemaproperty`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aiplugingovernance"></a> owner_aiplugingovernance

Many-To-One Relationship: [aiplugingovernance owner_aiplugingovernance](aiplugingovernance.md#BKMK_owner_aiplugingovernance)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugingovernance`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aiplugingovernance`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aiplugingovernanceext"></a> owner_aiplugingovernanceext

Many-To-One Relationship: [aiplugingovernanceext owner_aiplugingovernanceext](aiplugingovernanceext.md#BKMK_owner_aiplugingovernanceext)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugingovernanceext`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aiplugingovernanceext`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aiplugininstance"></a> owner_aiplugininstance

Many-To-One Relationship: [aiplugininstance owner_aiplugininstance](aiplugininstance.md#BKMK_owner_aiplugininstance)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugininstance`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aiplugininstance`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aipluginoperation"></a> owner_aipluginoperation

Many-To-One Relationship: [aipluginoperation owner_aipluginoperation](aipluginoperation.md#BKMK_owner_aipluginoperation)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperation`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aipluginoperation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aipluginoperationparameter"></a> owner_aipluginoperationparameter

Many-To-One Relationship: [aipluginoperationparameter owner_aipluginoperationparameter](aipluginoperationparameter.md#BKMK_owner_aipluginoperationparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperationparameter`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aipluginoperationparameter`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aipluginoperationresponsetemplate"></a> owner_aipluginoperationresponsetemplate

Many-To-One Relationship: [aipluginoperationresponsetemplate owner_aipluginoperationresponsetemplate](aipluginoperationresponsetemplate.md#BKMK_owner_aipluginoperationresponsetemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperationresponsetemplate`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aipluginoperationresponsetemplate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_aipluginusersetting"></a> owner_aipluginusersetting

Many-To-One Relationship: [aipluginusersetting owner_aipluginusersetting](aipluginusersetting.md#BKMK_owner_aipluginusersetting)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginusersetting`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_aipluginusersetting`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_annotations"></a> owner_annotations

Many-To-One Relationship: [annotation owner_annotations](annotation.md#BKMK_owner_annotations)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_annotations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_appnotification"></a> owner_appnotification

Many-To-One Relationship: [appnotification owner_appnotification](appnotification.md#BKMK_owner_appnotification)

|Property|Value|
|---|---|
|ReferencingEntity|`appnotification`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_appnotification`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_appointments"></a> owner_appointments

Many-To-One Relationship: [appointment owner_appointments](appointment.md#BKMK_owner_appointments)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_appointments`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_approvalprocess"></a> owner_approvalprocess

Many-To-One Relationship: [approvalprocess owner_approvalprocess](approvalprocess.md#BKMK_owner_approvalprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalprocess`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_approvalprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_approvalstageapproval"></a> owner_approvalstageapproval

Many-To-One Relationship: [approvalstageapproval owner_approvalstageapproval](approvalstageapproval.md#BKMK_owner_approvalstageapproval)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstageapproval`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_approvalstageapproval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_approvalstagecondition"></a> owner_approvalstagecondition

Many-To-One Relationship: [approvalstagecondition owner_approvalstagecondition](approvalstagecondition.md#BKMK_owner_approvalstagecondition)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstagecondition`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_approvalstagecondition`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_approvalstageorder"></a> owner_approvalstageorder

Many-To-One Relationship: [approvalstageorder owner_approvalstageorder](approvalstageorder.md#BKMK_owner_approvalstageorder)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstageorder`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_approvalstageorder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_asyncoperations"></a> owner_asyncoperations

Many-To-One Relationship: [asyncoperation owner_asyncoperations](asyncoperation.md#BKMK_owner_asyncoperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_asyncoperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_bot"></a> owner_bot

Many-To-One Relationship: [bot owner_bot](bot.md#BKMK_owner_bot)

|Property|Value|
|---|---|
|ReferencingEntity|`bot`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_bot`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_botcomponent"></a> owner_botcomponent

Many-To-One Relationship: [botcomponent owner_botcomponent](botcomponent.md#BKMK_owner_botcomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`botcomponent`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_botcomponent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_botcomponentcollection"></a> owner_botcomponentcollection

Many-To-One Relationship: [botcomponentcollection owner_botcomponentcollection](botcomponentcollection.md#BKMK_owner_botcomponentcollection)

|Property|Value|
|---|---|
|ReferencingEntity|`botcomponentcollection`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_botcomponentcollection`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_businessprocess"></a> owner_businessprocess

Many-To-One Relationship: [businessprocess owner_businessprocess](businessprocess.md#BKMK_owner_businessprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`businessprocess`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_businessprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_callbackregistration"></a> owner_callbackregistration

Many-To-One Relationship: [callbackregistration owner_callbackregistration](callbackregistration.md#BKMK_owner_callbackregistration)

|Property|Value|
|---|---|
|ReferencingEntity|`callbackregistration`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_callbackregistration`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_canvasapp"></a> owner_canvasapp

Many-To-One Relationship: [canvasapp owner_canvasapp](canvasapp.md#BKMK_owner_canvasapp)

|Property|Value|
|---|---|
|ReferencingEntity|`canvasapp`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_canvasapp`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_card"></a> owner_card

Many-To-One Relationship: [card owner_card](card.md#BKMK_owner_card)

|Property|Value|
|---|---|
|ReferencingEntity|`card`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_card`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_categories"></a> owner_categories

Many-To-One Relationship: [category owner_categories](category.md#BKMK_owner_categories)

|Property|Value|
|---|---|
|ReferencingEntity|`category`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_categories`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_certificatecredential"></a> owner_certificatecredential

Many-To-One Relationship: [certificatecredential owner_certificatecredential](certificatecredential.md#BKMK_owner_certificatecredential)

|Property|Value|
|---|---|
|ReferencingEntity|`certificatecredential`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_certificatecredential`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_connectioninstance"></a> owner_connectioninstance

Many-To-One Relationship: [connectioninstance owner_connectioninstance](connectioninstance.md#BKMK_owner_connectioninstance)

|Property|Value|
|---|---|
|ReferencingEntity|`connectioninstance`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_connectioninstance`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_connectionreference"></a> owner_connectionreference

Many-To-One Relationship: [connectionreference owner_connectionreference](connectionreference.md#BKMK_owner_connectionreference)

|Property|Value|
|---|---|
|ReferencingEntity|`connectionreference`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_connectionreference`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_connections"></a> owner_connections

Many-To-One Relationship: [connection owner_connections](connection.md#BKMK_owner_connections)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_connections`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_connector"></a> owner_connector

Many-To-One Relationship: [connector owner_connector](connector.md#BKMK_owner_connector)

|Property|Value|
|---|---|
|ReferencingEntity|`connector`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_connector`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_contacts"></a> owner_contacts

Many-To-One Relationship: [contact owner_contacts](contact.md#BKMK_owner_contacts)

|Property|Value|
|---|---|
|ReferencingEntity|`contact`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_contacts`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_conversationtranscript"></a> owner_conversationtranscript

Many-To-One Relationship: [conversationtranscript owner_conversationtranscript](conversationtranscript.md#BKMK_owner_conversationtranscript)

|Property|Value|
|---|---|
|ReferencingEntity|`conversationtranscript`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_conversationtranscript`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_copilotglossaryterm"></a> owner_copilotglossaryterm

Many-To-One Relationship: [copilotglossaryterm owner_copilotglossaryterm](copilotglossaryterm.md#BKMK_owner_copilotglossaryterm)

|Property|Value|
|---|---|
|ReferencingEntity|`copilotglossaryterm`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_copilotglossaryterm`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_copilotsynonyms"></a> owner_copilotsynonyms

Many-To-One Relationship: [copilotsynonyms owner_copilotsynonyms](copilotsynonyms.md#BKMK_owner_copilotsynonyms)

|Property|Value|
|---|---|
|ReferencingEntity|`copilotsynonyms`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_copilotsynonyms`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_credential"></a> owner_credential

Many-To-One Relationship: [credential owner_credential](credential.md#BKMK_owner_credential)

|Property|Value|
|---|---|
|ReferencingEntity|`credential`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_credential`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_customapi"></a> owner_customapi

Many-To-One Relationship: [customapi owner_customapi](customapi.md#BKMK_owner_customapi)

|Property|Value|
|---|---|
|ReferencingEntity|`customapi`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_customapi`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_datalakefolder"></a> owner_datalakefolder

Many-To-One Relationship: [datalakefolder owner_datalakefolder](datalakefolder.md#BKMK_owner_datalakefolder)

|Property|Value|
|---|---|
|ReferencingEntity|`datalakefolder`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_datalakefolder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_desktopflowbinary"></a> owner_desktopflowbinary

Many-To-One Relationship: [desktopflowbinary owner_desktopflowbinary](desktopflowbinary.md#BKMK_owner_desktopflowbinary)

|Property|Value|
|---|---|
|ReferencingEntity|`desktopflowbinary`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_desktopflowbinary`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_desktopflowmodule"></a> owner_desktopflowmodule

Many-To-One Relationship: [desktopflowmodule owner_desktopflowmodule](desktopflowmodule.md#BKMK_owner_desktopflowmodule)

|Property|Value|
|---|---|
|ReferencingEntity|`desktopflowmodule`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_desktopflowmodule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_duplicaterules"></a> owner_duplicaterules

Many-To-One Relationship: [duplicaterule owner_duplicaterules](duplicaterule.md#BKMK_owner_duplicaterules)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterule`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_duplicaterules`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_dvfilesearch"></a> owner_dvfilesearch

Many-To-One Relationship: [dvfilesearch owner_dvfilesearch](dvfilesearch.md#BKMK_owner_dvfilesearch)

|Property|Value|
|---|---|
|ReferencingEntity|`dvfilesearch`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_dvfilesearch`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_dvfilesearchattribute"></a> owner_dvfilesearchattribute

Many-To-One Relationship: [dvfilesearchattribute owner_dvfilesearchattribute](dvfilesearchattribute.md#BKMK_owner_dvfilesearchattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`dvfilesearchattribute`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_dvfilesearchattribute`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_dvfilesearchentity"></a> owner_dvfilesearchentity

Many-To-One Relationship: [dvfilesearchentity owner_dvfilesearchentity](dvfilesearchentity.md#BKMK_owner_dvfilesearchentity)

|Property|Value|
|---|---|
|ReferencingEntity|`dvfilesearchentity`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_dvfilesearchentity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_dvtablesearch"></a> owner_dvtablesearch

Many-To-One Relationship: [dvtablesearch owner_dvtablesearch](dvtablesearch.md#BKMK_owner_dvtablesearch)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearch`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_dvtablesearch`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_dvtablesearchattribute"></a> owner_dvtablesearchattribute

Many-To-One Relationship: [dvtablesearchattribute owner_dvtablesearchattribute](dvtablesearchattribute.md#BKMK_owner_dvtablesearchattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearchattribute`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_dvtablesearchattribute`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_dvtablesearchentity"></a> owner_dvtablesearchentity

Many-To-One Relationship: [dvtablesearchentity owner_dvtablesearchentity](dvtablesearchentity.md#BKMK_owner_dvtablesearchentity)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearchentity`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_dvtablesearchentity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_emails"></a> owner_emails

Many-To-One Relationship: [email owner_emails](email.md#BKMK_owner_emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_emails`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_emailserverprofile"></a> owner_emailserverprofile

Many-To-One Relationship: [emailserverprofile owner_emailserverprofile](emailserverprofile.md#BKMK_owner_emailserverprofile)

|Property|Value|
|---|---|
|ReferencingEntity|`emailserverprofile`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_emailserverprofile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_environmentvariabledefinition"></a> owner_environmentvariabledefinition

Many-To-One Relationship: [environmentvariabledefinition owner_environmentvariabledefinition](environmentvariabledefinition.md#BKMK_owner_environmentvariabledefinition)

|Property|Value|
|---|---|
|ReferencingEntity|`environmentvariabledefinition`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_environmentvariabledefinition`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_exchangesyncidmapping"></a> owner_exchangesyncidmapping

Many-To-One Relationship: [exchangesyncidmapping owner_exchangesyncidmapping](exchangesyncidmapping.md#BKMK_owner_exchangesyncidmapping)

|Property|Value|
|---|---|
|ReferencingEntity|`exchangesyncidmapping`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_exchangesyncidmapping`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_exportedexcel"></a> owner_exportedexcel

Many-To-One Relationship: [exportedexcel owner_exportedexcel](exportedexcel.md#BKMK_owner_exportedexcel)

|Property|Value|
|---|---|
|ReferencingEntity|`exportedexcel`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_exportedexcel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_exportsolutionupload"></a> owner_exportsolutionupload

Many-To-One Relationship: [exportsolutionupload owner_exportsolutionupload](exportsolutionupload.md#BKMK_owner_exportsolutionupload)

|Property|Value|
|---|---|
|ReferencingEntity|`exportsolutionupload`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_exportsolutionupload`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_fabricaiskill"></a> owner_fabricaiskill

Many-To-One Relationship: [fabricaiskill owner_fabricaiskill](fabricaiskill.md#BKMK_owner_fabricaiskill)

|Property|Value|
|---|---|
|ReferencingEntity|`fabricaiskill`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_fabricaiskill`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_faxes"></a> owner_faxes

Many-To-One Relationship: [fax owner_faxes](fax.md#BKMK_owner_faxes)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_faxes`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_featurecontrolsetting"></a> owner_featurecontrolsetting

Many-To-One Relationship: [featurecontrolsetting owner_featurecontrolsetting](featurecontrolsetting.md#BKMK_owner_featurecontrolsetting)

|Property|Value|
|---|---|
|ReferencingEntity|`featurecontrolsetting`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_featurecontrolsetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_federatedknowledgeconfiguration"></a> owner_federatedknowledgeconfiguration

Many-To-One Relationship: [federatedknowledgeconfiguration owner_federatedknowledgeconfiguration](federatedknowledgeconfiguration.md#BKMK_owner_federatedknowledgeconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`federatedknowledgeconfiguration`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_federatedknowledgeconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_federatedknowledgeentityconfiguration"></a> owner_federatedknowledgeentityconfiguration

Many-To-One Relationship: [federatedknowledgeentityconfiguration owner_federatedknowledgeentityconfiguration](federatedknowledgeentityconfiguration.md#BKMK_owner_federatedknowledgeentityconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`federatedknowledgeentityconfiguration`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_federatedknowledgeentityconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_feedback"></a> owner_feedback

Many-To-One Relationship: [feedback owner_feedback](feedback.md#BKMK_owner_feedback)

|Property|Value|
|---|---|
|ReferencingEntity|`feedback`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_feedback`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_flowaggregation"></a> owner_flowaggregation

Many-To-One Relationship: [flowaggregation owner_flowaggregation](flowaggregation.md#BKMK_owner_flowaggregation)

|Property|Value|
|---|---|
|ReferencingEntity|`flowaggregation`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_flowaggregation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_flowcapacityassignment"></a> owner_flowcapacityassignment

Many-To-One Relationship: [flowcapacityassignment owner_flowcapacityassignment](flowcapacityassignment.md#BKMK_owner_flowcapacityassignment)

|Property|Value|
|---|---|
|ReferencingEntity|`flowcapacityassignment`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_flowcapacityassignment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_flowcredentialapplication"></a> owner_flowcredentialapplication

Many-To-One Relationship: [flowcredentialapplication owner_flowcredentialapplication](flowcredentialapplication.md#BKMK_owner_flowcredentialapplication)

|Property|Value|
|---|---|
|ReferencingEntity|`flowcredentialapplication`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_flowcredentialapplication`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_flowevent"></a> owner_flowevent

Many-To-One Relationship: [flowevent owner_flowevent](flowevent.md#BKMK_owner_flowevent)

|Property|Value|
|---|---|
|ReferencingEntity|`flowevent`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_flowevent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_flowmachine"></a> owner_flowmachine

Many-To-One Relationship: [flowmachine owner_flowmachine](flowmachine.md#BKMK_owner_flowmachine)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachine`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_flowmachine`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_flowmachinegroup"></a> owner_flowmachinegroup

Many-To-One Relationship: [flowmachinegroup owner_flowmachinegroup](flowmachinegroup.md#BKMK_owner_flowmachinegroup)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachinegroup`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_flowmachinegroup`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_flowmachineimage"></a> owner_flowmachineimage

Many-To-One Relationship: [flowmachineimage owner_flowmachineimage](flowmachineimage.md#BKMK_owner_flowmachineimage)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachineimage`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_flowmachineimage`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_flowmachineimageversion"></a> owner_flowmachineimageversion

Many-To-One Relationship: [flowmachineimageversion owner_flowmachineimageversion](flowmachineimageversion.md#BKMK_owner_flowmachineimageversion)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachineimageversion`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_flowmachineimageversion`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_flowmachinenetwork"></a> owner_flowmachinenetwork

Many-To-One Relationship: [flowmachinenetwork owner_flowmachinenetwork](flowmachinenetwork.md#BKMK_owner_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachinenetwork`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_flowmachinenetwork`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_flowrun"></a> owner_flowrun

Many-To-One Relationship: [flowrun owner_flowrun](flowrun.md#BKMK_owner_flowrun)

|Property|Value|
|---|---|
|ReferencingEntity|`flowrun`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_flowrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_flowsession"></a> owner_flowsession

Many-To-One Relationship: [flowsession owner_flowsession](flowsession.md#BKMK_owner_flowsession)

|Property|Value|
|---|---|
|ReferencingEntity|`flowsession`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_flowsession`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_fxexpression"></a> owner_fxexpression

Many-To-One Relationship: [fxexpression owner_fxexpression](fxexpression.md#BKMK_owner_fxexpression)

|Property|Value|
|---|---|
|ReferencingEntity|`fxexpression`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_fxexpression`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_goal"></a> owner_goal

Many-To-One Relationship: [goal owner_goal](goal.md#BKMK_owner_goal)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_goal`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_goalrollupquery"></a> owner_goalrollupquery

Many-To-One Relationship: [goalrollupquery owner_goalrollupquery](goalrollupquery.md#BKMK_owner_goalrollupquery)

|Property|Value|
|---|---|
|ReferencingEntity|`goalrollupquery`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_goalrollupquery`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_governanceconfiguration"></a> owner_governanceconfiguration

Many-To-One Relationship: [governanceconfiguration owner_governanceconfiguration](governanceconfiguration.md#BKMK_owner_governanceconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`governanceconfiguration`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_governanceconfiguration`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_importdatas"></a> owner_importdatas

Many-To-One Relationship: [importdata owner_importdatas](importdata.md#BKMK_owner_importdatas)

|Property|Value|
|---|---|
|ReferencingEntity|`importdata`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_importdatas`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_importfiles"></a> owner_importfiles

Many-To-One Relationship: [importfile owner_importfiles](importfile.md#BKMK_owner_importfiles)

|Property|Value|
|---|---|
|ReferencingEntity|`importfile`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_importfiles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_importlogs"></a> owner_importlogs

Many-To-One Relationship: [importlog owner_importlogs](importlog.md#BKMK_owner_importlogs)

|Property|Value|
|---|---|
|ReferencingEntity|`importlog`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_importlogs`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_importmaps"></a> owner_importmaps

Many-To-One Relationship: [importmap owner_importmaps](importmap.md#BKMK_owner_importmaps)

|Property|Value|
|---|---|
|ReferencingEntity|`importmap`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_importmaps`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_imports"></a> owner_imports

Many-To-One Relationship: [import owner_imports](import.md#BKMK_owner_imports)

|Property|Value|
|---|---|
|ReferencingEntity|`import`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_imports`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_indexedtrait"></a> owner_indexedtrait

Many-To-One Relationship: [indexedtrait owner_indexedtrait](indexedtrait.md#BKMK_owner_indexedtrait)

|Property|Value|
|---|---|
|ReferencingEntity|`indexedtrait`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_indexedtrait`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_interactionforemail"></a> owner_interactionforemail

Many-To-One Relationship: [interactionforemail owner_interactionforemail](interactionforemail.md#BKMK_owner_interactionforemail)

|Property|Value|
|---|---|
|ReferencingEntity|`interactionforemail`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_new_interactionforemail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_keyvaultreference"></a> owner_keyvaultreference

Many-To-One Relationship: [keyvaultreference owner_keyvaultreference](keyvaultreference.md#BKMK_owner_keyvaultreference)

|Property|Value|
|---|---|
|ReferencingEntity|`keyvaultreference`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_keyvaultreference`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_knowledgearticle"></a> owner_knowledgearticle

Many-To-One Relationship: [knowledgearticle owner_knowledgearticle](knowledgearticle.md#BKMK_owner_knowledgearticle)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_knowledgearticle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_letters"></a> owner_letters

Many-To-One Relationship: [letter owner_letters](letter.md#BKMK_owner_letters)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_letters`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_mailbox"></a> owner_mailbox

Many-To-One Relationship: [mailbox owner_mailbox](mailbox.md#BKMK_owner_mailbox)

|Property|Value|
|---|---|
|ReferencingEntity|`mailbox`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_mailbox`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_mailboxtrackingfolder"></a> owner_mailboxtrackingfolder

Many-To-One Relationship: [mailboxtrackingfolder owner_mailboxtrackingfolder](mailboxtrackingfolder.md#BKMK_owner_mailboxtrackingfolder)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_mailboxtrackingfolder`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_mailmergetemplates"></a> owner_mailmergetemplates

Many-To-One Relationship: [mailmergetemplate owner_mailmergetemplates](mailmergetemplate.md#BKMK_owner_mailmergetemplates)

|Property|Value|
|---|---|
|ReferencingEntity|`mailmergetemplate`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_mailmergetemplates`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_managedidentity"></a> owner_managedidentity

Many-To-One Relationship: [managedidentity owner_managedidentity](managedidentity.md#BKMK_owner_managedidentity)

|Property|Value|
|---|---|
|ReferencingEntity|`managedidentity`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_managedidentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aibdataset"></a> owner_msdyn_aibdataset

Many-To-One Relationship: [msdyn_aibdataset owner_msdyn_aibdataset](msdyn_aibdataset.md#BKMK_owner_msdyn_aibdataset)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdataset`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aibdataset`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aibdatasetfile"></a> owner_msdyn_aibdatasetfile

Many-To-One Relationship: [msdyn_aibdatasetfile owner_msdyn_aibdatasetfile](msdyn_aibdatasetfile.md#BKMK_owner_msdyn_aibdatasetfile)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdatasetfile`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aibdatasetfile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aibdatasetrecord"></a> owner_msdyn_aibdatasetrecord

Many-To-One Relationship: [msdyn_aibdatasetrecord owner_msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md#BKMK_owner_msdyn_aibdatasetrecord)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdatasetrecord`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aibdatasetrecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aibdatasetscontainer"></a> owner_msdyn_aibdatasetscontainer

Many-To-One Relationship: [msdyn_aibdatasetscontainer owner_msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md#BKMK_owner_msdyn_aibdatasetscontainer)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdatasetscontainer`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aibdatasetscontainer`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aibfeedbackloop"></a> owner_msdyn_aibfeedbackloop

Many-To-One Relationship: [msdyn_aibfeedbackloop owner_msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md#BKMK_owner_msdyn_aibfeedbackloop)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfeedbackloop`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aibfeedbackloop`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aibfile"></a> owner_msdyn_aibfile

Many-To-One Relationship: [msdyn_aibfile owner_msdyn_aibfile](msdyn_aibfile.md#BKMK_owner_msdyn_aibfile)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfile`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aibfile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aibfileattacheddata"></a> owner_msdyn_aibfileattacheddata

Many-To-One Relationship: [msdyn_aibfileattacheddata owner_msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md#BKMK_owner_msdyn_aibfileattacheddata)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfileattacheddata`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aibfileattacheddata`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aidataprocessingevent"></a> owner_msdyn_aidataprocessingevent

Many-To-One Relationship: [msdyn_aidataprocessingevent owner_msdyn_aidataprocessingevent](msdyn_aidataprocessingevent.md#BKMK_owner_msdyn_aidataprocessingevent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aidataprocessingevent`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aidataprocessingevent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aievaluationconfiguration"></a> owner_msdyn_aievaluationconfiguration

Many-To-One Relationship: [msdyn_aievaluationconfiguration owner_msdyn_aievaluationconfiguration](msdyn_aievaluationconfiguration.md#BKMK_owner_msdyn_aievaluationconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aievaluationconfiguration`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aievaluationconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aievaluationrun"></a> owner_msdyn_aievaluationrun

Many-To-One Relationship: [msdyn_aievaluationrun owner_msdyn_aievaluationrun](msdyn_aievaluationrun.md#BKMK_owner_msdyn_aievaluationrun)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aievaluationrun`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aievaluationrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aievent"></a> owner_msdyn_aievent

Many-To-One Relationship: [msdyn_aievent owner_msdyn_aievent](msdyn_aievent.md#BKMK_owner_msdyn_aievent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aievent`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aievent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aifptrainingdocument"></a> owner_msdyn_aifptrainingdocument

Many-To-One Relationship: [msdyn_aifptrainingdocument owner_msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md#BKMK_owner_msdyn_aifptrainingdocument)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aifptrainingdocument`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aifptrainingdocument`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aimodel"></a> owner_msdyn_aimodel

Many-To-One Relationship: [msdyn_aimodel owner_msdyn_aimodel](msdyn_aimodel.md#BKMK_owner_msdyn_aimodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aimodel`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aimodel`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aimodelcatalog"></a> owner_msdyn_aimodelcatalog

Many-To-One Relationship: [msdyn_aimodelcatalog owner_msdyn_aimodelcatalog](msdyn_aimodelcatalog.md#BKMK_owner_msdyn_aimodelcatalog)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aimodelcatalog`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aimodelcatalog`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aiodimage"></a> owner_msdyn_aiodimage

Many-To-One Relationship: [msdyn_aiodimage owner_msdyn_aiodimage](msdyn_aiodimage.md#BKMK_owner_msdyn_aiodimage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodimage`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aiodimage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aiodlabel"></a> owner_msdyn_aiodlabel

Many-To-One Relationship: [msdyn_aiodlabel owner_msdyn_aiodlabel](msdyn_aiodlabel.md#BKMK_owner_msdyn_aiodlabel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodlabel`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aiodlabel`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aiodtrainingboundingbox"></a> owner_msdyn_aiodtrainingboundingbox

Many-To-One Relationship: [msdyn_aiodtrainingboundingbox owner_msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md#BKMK_owner_msdyn_aiodtrainingboundingbox)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aiodtrainingboundingbox`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aiodtrainingimage"></a> owner_msdyn_aiodtrainingimage

Many-To-One Relationship: [msdyn_aiodtrainingimage owner_msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md#BKMK_owner_msdyn_aiodtrainingimage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodtrainingimage`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aiodtrainingimage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aitemplate"></a> owner_msdyn_aitemplate

Many-To-One Relationship: [msdyn_aitemplate owner_msdyn_aitemplate](msdyn_aitemplate.md#BKMK_owner_msdyn_aitemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitemplate`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aitemplate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aitestcase"></a> owner_msdyn_aitestcase

Many-To-One Relationship: [msdyn_aitestcase owner_msdyn_aitestcase](msdyn_aitestcase.md#BKMK_owner_msdyn_aitestcase)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestcase`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aitestcase`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aitestcasedocument"></a> owner_msdyn_aitestcasedocument

Many-To-One Relationship: [msdyn_aitestcasedocument owner_msdyn_aitestcasedocument](msdyn_aitestcasedocument.md#BKMK_owner_msdyn_aitestcasedocument)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestcasedocument`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aitestcasedocument`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aitestcaseinput"></a> owner_msdyn_aitestcaseinput

Many-To-One Relationship: [msdyn_aitestcaseinput owner_msdyn_aitestcaseinput](msdyn_aitestcaseinput.md#BKMK_owner_msdyn_aitestcaseinput)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestcaseinput`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aitestcaseinput`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aitestrun"></a> owner_msdyn_aitestrun

Many-To-One Relationship: [msdyn_aitestrun owner_msdyn_aitestrun](msdyn_aitestrun.md#BKMK_owner_msdyn_aitestrun)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestrun`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aitestrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_aitestrunbatch"></a> owner_msdyn_aitestrunbatch

Many-To-One Relationship: [msdyn_aitestrunbatch owner_msdyn_aitestrunbatch](msdyn_aitestrunbatch.md#BKMK_owner_msdyn_aitestrunbatch)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestrunbatch`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_aitestrunbatch`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_analysiscomponent"></a> owner_msdyn_analysiscomponent

Many-To-One Relationship: [msdyn_analysiscomponent owner_msdyn_analysiscomponent](msdyn_analysiscomponent.md#BKMK_owner_msdyn_analysiscomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysiscomponent`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_analysiscomponent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_analysisjob"></a> owner_msdyn_analysisjob

Many-To-One Relationship: [msdyn_analysisjob owner_msdyn_analysisjob](msdyn_analysisjob.md#BKMK_owner_msdyn_analysisjob)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisjob`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_analysisjob`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_analysisoverride"></a> owner_msdyn_analysisoverride

Many-To-One Relationship: [msdyn_analysisoverride owner_msdyn_analysisoverride](msdyn_analysisoverride.md#BKMK_owner_msdyn_analysisoverride)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisoverride`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_analysisoverride`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_analysisresult"></a> owner_msdyn_analysisresult

Many-To-One Relationship: [msdyn_analysisresult owner_msdyn_analysisresult](msdyn_analysisresult.md#BKMK_owner_msdyn_analysisresult)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisresult`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_analysisresult`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_analysisresultdetail"></a> owner_msdyn_analysisresultdetail

Many-To-One Relationship: [msdyn_analysisresultdetail owner_msdyn_analysisresultdetail](msdyn_analysisresultdetail.md#BKMK_owner_msdyn_analysisresultdetail)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisresultdetail`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_analysisresultdetail`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_copilotinteractions"></a> owner_msdyn_copilotinteractions

Many-To-One Relationship: [msdyn_copilotinteractions owner_msdyn_copilotinteractions](msdyn_copilotinteractions.md#BKMK_owner_msdyn_copilotinteractions)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_copilotinteractions`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_copilotinteractions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_customcontrolextendedsettings"></a> owner_msdyn_customcontrolextendedsettings

Many-To-One Relationship: [msdyn_customcontrolextendedsettings owner_msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md#BKMK_owner_msdyn_customcontrolextendedsettings)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_customcontrolextendedsettings`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_customcontrolextendedsettings`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_dataflow"></a> owner_msdyn_dataflow

Many-To-One Relationship: [msdyn_dataflow owner_msdyn_dataflow](msdyn_dataflow.md#BKMK_owner_msdyn_dataflow)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflow`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_dataflow`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_dataflow_datalakefolder"></a> owner_msdyn_dataflow_datalakefolder

Many-To-One Relationship: [msdyn_dataflow_datalakefolder owner_msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md#BKMK_owner_msdyn_dataflow_datalakefolder)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflow_datalakefolder`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_dataflow_datalakefolder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_dataflowconnectionreference"></a> owner_msdyn_dataflowconnectionreference

Many-To-One Relationship: [msdyn_dataflowconnectionreference owner_msdyn_dataflowconnectionreference](msdyn_dataflowconnectionreference.md#BKMK_owner_msdyn_dataflowconnectionreference)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflowconnectionreference`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_dataflowconnectionreference`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_dataflowrefreshhistory"></a> owner_msdyn_dataflowrefreshhistory

Many-To-One Relationship: [msdyn_dataflowrefreshhistory owner_msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md#BKMK_owner_msdyn_dataflowrefreshhistory)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflowrefreshhistory`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_dataflowrefreshhistory`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_dataflowtemplate"></a> owner_msdyn_dataflowtemplate

Many-To-One Relationship: [msdyn_dataflowtemplate owner_msdyn_dataflowtemplate](msdyn_dataflowtemplate.md#BKMK_owner_msdyn_dataflowtemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflowtemplate`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_dataflowtemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_dmsrequest"></a> owner_msdyn_dmsrequest

Many-To-One Relationship: [msdyn_dmsrequest owner_msdyn_dmsrequest](msdyn_dmsrequest.md#BKMK_owner_msdyn_dmsrequest)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmsrequest`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_dmsrequest`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_dmsrequeststatus"></a> owner_msdyn_dmsrequeststatus

Many-To-One Relationship: [msdyn_dmsrequeststatus owner_msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md#BKMK_owner_msdyn_dmsrequeststatus)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmsrequeststatus`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_dmsrequeststatus`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_dmssyncrequest"></a> owner_msdyn_dmssyncrequest

Many-To-One Relationship: [msdyn_dmssyncrequest owner_msdyn_dmssyncrequest](msdyn_dmssyncrequest.md#BKMK_owner_msdyn_dmssyncrequest)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmssyncrequest`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_dmssyncrequest`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_dmssyncstatus"></a> owner_msdyn_dmssyncstatus

Many-To-One Relationship: [msdyn_dmssyncstatus owner_msdyn_dmssyncstatus](msdyn_dmssyncstatus.md#BKMK_owner_msdyn_dmssyncstatus)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmssyncstatus`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_dmssyncstatus`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_entitylinkchatconfiguration"></a> owner_msdyn_entitylinkchatconfiguration

Many-To-One Relationship: [msdyn_entitylinkchatconfiguration owner_msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md#BKMK_owner_msdyn_entitylinkchatconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_entitylinkchatconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_entityrefreshhistory"></a> owner_msdyn_entityrefreshhistory

Many-To-One Relationship: [msdyn_entityrefreshhistory owner_msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md#BKMK_owner_msdyn_entityrefreshhistory)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_entityrefreshhistory`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_entityrefreshhistory`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_favoriteknowledgearticle"></a> owner_msdyn_favoriteknowledgearticle

Many-To-One Relationship: [msdyn_favoriteknowledgearticle owner_msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md#BKMK_owner_msdyn_favoriteknowledgearticle)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_favoriteknowledgearticle`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_favoriteknowledgearticle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_federatedarticle"></a> owner_msdyn_federatedarticle

Many-To-One Relationship: [msdyn_federatedarticle owner_msdyn_federatedarticle](msdyn_federatedarticle.md#BKMK_owner_msdyn_federatedarticle)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_federatedarticle`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_federatedarticle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_fileupload"></a> owner_msdyn_fileupload

Many-To-One Relationship: [msdyn_fileupload owner_msdyn_fileupload](msdyn_fileupload.md#BKMK_owner_msdyn_fileupload)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_fileupload`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_fileupload`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_flow_actionapprovalmodel"></a> owner_msdyn_flow_actionapprovalmodel

Many-To-One Relationship: [msdyn_flow_actionapprovalmodel owner_msdyn_flow_actionapprovalmodel](msdyn_flow_actionapprovalmodel.md#BKMK_owner_msdyn_flow_actionapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_flow_actionapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_flow_approval"></a> owner_msdyn_flow_approval

Many-To-One Relationship: [msdyn_flow_approval owner_msdyn_flow_approval](msdyn_flow_approval.md#BKMK_owner_msdyn_flow_approval)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approval`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_flow_approval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_flow_approvalrequest"></a> owner_msdyn_flow_approvalrequest

Many-To-One Relationship: [msdyn_flow_approvalrequest owner_msdyn_flow_approvalrequest](msdyn_flow_approvalrequest.md#BKMK_owner_msdyn_flow_approvalrequest)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalrequest`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_flow_approvalrequest`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_flow_approvalresponse"></a> owner_msdyn_flow_approvalresponse

Many-To-One Relationship: [msdyn_flow_approvalresponse owner_msdyn_flow_approvalresponse](msdyn_flow_approvalresponse.md#BKMK_owner_msdyn_flow_approvalresponse)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalresponse`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_flow_approvalresponse`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_flow_approvalstep"></a> owner_msdyn_flow_approvalstep

Many-To-One Relationship: [msdyn_flow_approvalstep owner_msdyn_flow_approvalstep](msdyn_flow_approvalstep.md#BKMK_owner_msdyn_flow_approvalstep)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalstep`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_flow_approvalstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_flow_awaitallactionapprovalmodel"></a> owner_msdyn_flow_awaitallactionapprovalmodel

Many-To-One Relationship: [msdyn_flow_awaitallactionapprovalmodel owner_msdyn_flow_awaitallactionapprovalmodel](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_owner_msdyn_flow_awaitallactionapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_flow_awaitallactionapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_flow_awaitallapprovalmodel"></a> owner_msdyn_flow_awaitallapprovalmodel

Many-To-One Relationship: [msdyn_flow_awaitallapprovalmodel owner_msdyn_flow_awaitallapprovalmodel](msdyn_flow_awaitallapprovalmodel.md#BKMK_owner_msdyn_flow_awaitallapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_flow_awaitallapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_flow_basicapprovalmodel"></a> owner_msdyn_flow_basicapprovalmodel

Many-To-One Relationship: [msdyn_flow_basicapprovalmodel owner_msdyn_flow_basicapprovalmodel](msdyn_flow_basicapprovalmodel.md#BKMK_owner_msdyn_flow_basicapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_flow_basicapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_flow_flowapproval"></a> owner_msdyn_flow_flowapproval

Many-To-One Relationship: [msdyn_flow_flowapproval owner_msdyn_flow_flowapproval](msdyn_flow_flowapproval.md#BKMK_owner_msdyn_flow_flowapproval)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_flowapproval`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_flow_flowapproval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_formmapping"></a> owner_msdyn_formmapping

Many-To-One Relationship: [msdyn_formmapping owner_msdyn_formmapping](msdyn_formmapping.md#BKMK_owner_msdyn_formmapping)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_formmapping`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_formmapping`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_function"></a> owner_msdyn_function

Many-To-One Relationship: [msdyn_function owner_msdyn_function](msdyn_function.md#BKMK_owner_msdyn_function)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_function`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_function`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_integratedsearchprovider"></a> owner_msdyn_integratedsearchprovider

Many-To-One Relationship: [msdyn_integratedsearchprovider owner_msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md#BKMK_owner_msdyn_integratedsearchprovider)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_integratedsearchprovider`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_integratedsearchprovider`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_kalanguagesetting"></a> owner_msdyn_kalanguagesetting

Many-To-One Relationship: [msdyn_kalanguagesetting owner_msdyn_kalanguagesetting](msdyn_kalanguagesetting.md#BKMK_owner_msdyn_kalanguagesetting)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_kalanguagesetting`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_kalanguagesetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_kbattachment"></a> owner_msdyn_kbattachment

Many-To-One Relationship: [msdyn_kbattachment owner_msdyn_kbattachment](msdyn_kbattachment.md#BKMK_owner_msdyn_kbattachment)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_kbattachment`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_kbattachment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_kmfederatedsearchconfig"></a> owner_msdyn_kmfederatedsearchconfig

Many-To-One Relationship: [msdyn_kmfederatedsearchconfig owner_msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md#BKMK_owner_msdyn_kmfederatedsearchconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_kmfederatedsearchconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_knowledgearticleimage"></a> owner_msdyn_knowledgearticleimage

Many-To-One Relationship: [msdyn_knowledgearticleimage owner_msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md#BKMK_owner_msdyn_knowledgearticleimage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgearticleimage`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_knowledgearticleimage`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_knowledgearticletemplate"></a> owner_msdyn_knowledgearticletemplate

Many-To-One Relationship: [msdyn_knowledgearticletemplate owner_msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md#BKMK_owner_msdyn_knowledgearticletemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgearticletemplate`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_knowledgearticletemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_knowledgeassetconfiguration"></a> owner_msdyn_knowledgeassetconfiguration

Many-To-One Relationship: [msdyn_knowledgeassetconfiguration owner_msdyn_knowledgeassetconfiguration](msdyn_knowledgeassetconfiguration.md#BKMK_owner_msdyn_knowledgeassetconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgeassetconfiguration`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_knowledgeassetconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_knowledgeinteractioninsight"></a> owner_msdyn_knowledgeinteractioninsight

Many-To-One Relationship: [msdyn_knowledgeinteractioninsight owner_msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md#BKMK_owner_msdyn_knowledgeinteractioninsight)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_knowledgeinteractioninsight`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_knowledgemanagementsetting"></a> owner_msdyn_knowledgemanagementsetting

Many-To-One Relationship: [msdyn_knowledgemanagementsetting owner_msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md#BKMK_owner_msdyn_knowledgemanagementsetting)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgemanagementsetting`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_knowledgemanagementsetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_knowledgepersonalfilter"></a> owner_msdyn_knowledgepersonalfilter

Many-To-One Relationship: [msdyn_knowledgepersonalfilter owner_msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md#BKMK_owner_msdyn_knowledgepersonalfilter)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgepersonalfilter`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_knowledgepersonalfilter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_knowledgesearchfilter"></a> owner_msdyn_knowledgesearchfilter

Many-To-One Relationship: [msdyn_knowledgesearchfilter owner_msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md#BKMK_owner_msdyn_knowledgesearchfilter)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgesearchfilter`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_knowledgesearchfilter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_knowledgesearchinsight"></a> owner_msdyn_knowledgesearchinsight

Many-To-One Relationship: [msdyn_knowledgesearchinsight owner_msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md#BKMK_owner_msdyn_knowledgesearchinsight)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgesearchinsight`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_knowledgesearchinsight`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_mobileapp"></a> owner_msdyn_mobileapp

Many-To-One Relationship: [msdyn_mobileapp owner_msdyn_mobileapp](msdyn_mobileapp.md#BKMK_owner_msdyn_mobileapp)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_mobileapp`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmanalysishistory"></a> owner_msdyn_pmanalysishistory

Many-To-One Relationship: [msdyn_pmanalysishistory owner_msdyn_pmanalysishistory](msdyn_pmanalysishistory.md#BKMK_owner_msdyn_pmanalysishistory)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmanalysishistory`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmanalysishistory`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmbusinessruleautomationconfig"></a> owner_msdyn_pmbusinessruleautomationconfig

Many-To-One Relationship: [msdyn_pmbusinessruleautomationconfig owner_msdyn_pmbusinessruleautomationconfig](msdyn_pmbusinessruleautomationconfig.md#BKMK_owner_msdyn_pmbusinessruleautomationconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmbusinessruleautomationconfig`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmcalendar"></a> owner_msdyn_pmcalendar

Many-To-One Relationship: [msdyn_pmcalendar owner_msdyn_pmcalendar](msdyn_pmcalendar.md#BKMK_owner_msdyn_pmcalendar)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmcalendar`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmcalendar`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmcalendarversion"></a> owner_msdyn_pmcalendarversion

Many-To-One Relationship: [msdyn_pmcalendarversion owner_msdyn_pmcalendarversion](msdyn_pmcalendarversion.md#BKMK_owner_msdyn_pmcalendarversion)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmcalendarversion`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmcalendarversion`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pminferredtask"></a> owner_msdyn_pminferredtask

Many-To-One Relationship: [msdyn_pminferredtask owner_msdyn_pminferredtask](msdyn_pminferredtask.md#BKMK_owner_msdyn_pminferredtask)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pminferredtask`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pminferredtask`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmprocessextendedmetadataversion"></a> owner_msdyn_pmprocessextendedmetadataversion

Many-To-One Relationship: [msdyn_pmprocessextendedmetadataversion owner_msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md#BKMK_owner_msdyn_pmprocessextendedmetadataversion)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocessextendedmetadataversion`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmprocessextendedmetadataversion`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmprocesstemplate"></a> owner_msdyn_pmprocesstemplate

Many-To-One Relationship: [msdyn_pmprocesstemplate owner_msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md#BKMK_owner_msdyn_pmprocesstemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocesstemplate`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmprocesstemplate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmprocessusersettings"></a> owner_msdyn_pmprocessusersettings

Many-To-One Relationship: [msdyn_pmprocessusersettings owner_msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md#BKMK_owner_msdyn_pmprocessusersettings)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocessusersettings`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmprocessusersettings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmprocessversion"></a> owner_msdyn_pmprocessversion

Many-To-One Relationship: [msdyn_pmprocessversion owner_msdyn_pmprocessversion](msdyn_pmprocessversion.md#BKMK_owner_msdyn_pmprocessversion)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocessversion`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmprocessversion`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmrecording"></a> owner_msdyn_pmrecording

Many-To-One Relationship: [msdyn_pmrecording owner_msdyn_pmrecording](msdyn_pmrecording.md#BKMK_owner_msdyn_pmrecording)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmrecording`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmrecording`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmsimulation"></a> owner_msdyn_pmsimulation

Many-To-One Relationship: [msdyn_pmsimulation owner_msdyn_pmsimulation](msdyn_pmsimulation.md#BKMK_owner_msdyn_pmsimulation)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmsimulation`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmsimulation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmtemplate"></a> owner_msdyn_pmtemplate

Many-To-One Relationship: [msdyn_pmtemplate owner_msdyn_pmtemplate](msdyn_pmtemplate.md#BKMK_owner_msdyn_pmtemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmtemplate`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmtemplate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_pmview"></a> owner_msdyn_pmview

Many-To-One Relationship: [msdyn_pmview owner_msdyn_pmview](msdyn_pmview.md#BKMK_owner_msdyn_pmview)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmview`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_pmview`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_qna"></a> owner_msdyn_qna

Many-To-One Relationship: [msdyn_qna owner_msdyn_qna](msdyn_qna.md#BKMK_owner_msdyn_qna)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_qna`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_qna`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_richtextfile"></a> owner_msdyn_richtextfile

Many-To-One Relationship: [msdyn_richtextfile owner_msdyn_richtextfile](msdyn_richtextfile.md#BKMK_owner_msdyn_richtextfile)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_richtextfile`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_richtextfile`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_salesforcestructuredobject"></a> owner_msdyn_salesforcestructuredobject

Many-To-One Relationship: [msdyn_salesforcestructuredobject owner_msdyn_salesforcestructuredobject](msdyn_salesforcestructuredobject.md#BKMK_owner_msdyn_salesforcestructuredobject)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_salesforcestructuredobject`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_salesforcestructuredobject`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_salesforcestructuredqnaconfig"></a> owner_msdyn_salesforcestructuredqnaconfig

Many-To-One Relationship: [msdyn_salesforcestructuredqnaconfig owner_msdyn_salesforcestructuredqnaconfig](msdyn_salesforcestructuredqnaconfig.md#BKMK_owner_msdyn_salesforcestructuredqnaconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_salesforcestructuredqnaconfig`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_salesforcestructuredqnaconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_schedule"></a> owner_msdyn_schedule

Many-To-One Relationship: [msdyn_schedule owner_msdyn_schedule](msdyn_schedule.md#BKMK_owner_msdyn_schedule)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_schedule`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_schedule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_serviceconfiguration"></a> owner_msdyn_serviceconfiguration

Many-To-One Relationship: [msdyn_serviceconfiguration owner_msdyn_serviceconfiguration](msdyn_serviceconfiguration.md#BKMK_owner_msdyn_serviceconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_serviceconfiguration`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_serviceconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_slakpi"></a> owner_msdyn_slakpi

Many-To-One Relationship: [msdyn_slakpi owner_msdyn_slakpi](msdyn_slakpi.md#BKMK_owner_msdyn_slakpi)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_slakpi`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_slakpi`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_solutionhealthrule"></a> owner_msdyn_solutionhealthrule

Many-To-One Relationship: [msdyn_solutionhealthrule owner_msdyn_solutionhealthrule](msdyn_solutionhealthrule.md#BKMK_owner_msdyn_solutionhealthrule)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_solutionhealthrule`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_solutionhealthrule`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_solutionhealthruleargument"></a> owner_msdyn_solutionhealthruleargument

Many-To-One Relationship: [msdyn_solutionhealthruleargument owner_msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md#BKMK_owner_msdyn_solutionhealthruleargument)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_solutionhealthruleargument`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_solutionhealthruleargument`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdyn_virtualtablecolumncandidate"></a> owner_msdyn_virtualtablecolumncandidate

Many-To-One Relationship: [msdyn_virtualtablecolumncandidate owner_msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md#BKMK_owner_msdyn_virtualtablecolumncandidate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdyn_virtualtablecolumncandidate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_msdynce_botcontent"></a> owner_msdynce_botcontent

Many-To-One Relationship: [msdynce_botcontent owner_msdynce_botcontent](msdynce_botcontent.md#BKMK_owner_msdynce_botcontent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdynce_botcontent`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_msdynce_botcontent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_mspcat_catalogsubmissionfiles"></a> owner_mspcat_catalogsubmissionfiles

Many-To-One Relationship: [mspcat_catalogsubmissionfiles owner_mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md#BKMK_owner_mspcat_catalogsubmissionfiles)

|Property|Value|
|---|---|
|ReferencingEntity|`mspcat_catalogsubmissionfiles`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_mspcat_catalogsubmissionfiles`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_mspcat_packagestore"></a> owner_mspcat_packagestore

Many-To-One Relationship: [mspcat_packagestore owner_mspcat_packagestore](mspcat_packagestore.md#BKMK_owner_mspcat_packagestore)

|Property|Value|
|---|---|
|ReferencingEntity|`mspcat_packagestore`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_mspcat_packagestore`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_nlsqregistration"></a> owner_nlsqregistration

Many-To-One Relationship: [nlsqregistration owner_nlsqregistration](nlsqregistration.md#BKMK_owner_nlsqregistration)

|Property|Value|
|---|---|
|ReferencingEntity|`nlsqregistration`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_nlsqregistration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_personaldocumenttemplates"></a> owner_personaldocumenttemplates

Many-To-One Relationship: [personaldocumenttemplate owner_personaldocumenttemplates](personaldocumenttemplate.md#BKMK_owner_personaldocumenttemplates)

|Property|Value|
|---|---|
|ReferencingEntity|`personaldocumenttemplate`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_personaldocumenttemplates`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_phonecalls"></a> owner_phonecalls

Many-To-One Relationship: [phonecall owner_phonecalls](phonecall.md#BKMK_owner_phonecalls)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_phonecalls`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_plannerbusinessscenario"></a> owner_plannerbusinessscenario

Many-To-One Relationship: [plannerbusinessscenario owner_plannerbusinessscenario](plannerbusinessscenario.md#BKMK_owner_plannerbusinessscenario)

|Property|Value|
|---|---|
|ReferencingEntity|`plannerbusinessscenario`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_plannerbusinessscenario`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_plannersyncaction"></a> owner_plannersyncaction

Many-To-One Relationship: [plannersyncaction owner_plannersyncaction](plannersyncaction.md#BKMK_owner_plannersyncaction)

|Property|Value|
|---|---|
|ReferencingEntity|`plannersyncaction`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_plannersyncaction`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_plugin"></a> owner_plugin

Many-To-One Relationship: [plugin owner_plugin](plugin.md#BKMK_owner_plugin)

|Property|Value|
|---|---|
|ReferencingEntity|`plugin`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_plugin`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_postfollows"></a> owner_postfollows

Many-To-One Relationship: [postfollow owner_postfollows](postfollow.md#BKMK_owner_postfollows)

|Property|Value|
|---|---|
|ReferencingEntity|`postfollow`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_postfollows`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerbidataset"></a> owner_powerbidataset

Many-To-One Relationship: [powerbidataset owner_powerbidataset](powerbidataset.md#BKMK_owner_powerbidataset)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbidataset`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerbidataset`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerbidatasetapdx"></a> owner_powerbidatasetapdx

Many-To-One Relationship: [powerbidatasetapdx owner_powerbidatasetapdx](powerbidatasetapdx.md#BKMK_owner_powerbidatasetapdx)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbidatasetapdx`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerbidatasetapdx`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerbimashupparameter"></a> owner_powerbimashupparameter

Many-To-One Relationship: [powerbimashupparameter owner_powerbimashupparameter](powerbimashupparameter.md#BKMK_owner_powerbimashupparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbimashupparameter`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerbimashupparameter`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerbireport"></a> owner_powerbireport

Many-To-One Relationship: [powerbireport owner_powerbireport](powerbireport.md#BKMK_owner_powerbireport)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbireport`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerbireport`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerbireportapdx"></a> owner_powerbireportapdx

Many-To-One Relationship: [powerbireportapdx owner_powerbireportapdx](powerbireportapdx.md#BKMK_owner_powerbireportapdx)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbireportapdx`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerbireportapdx`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerfxrule"></a> owner_powerfxrule

Many-To-One Relationship: [powerfxrule owner_powerfxrule](powerfxrule.md#BKMK_owner_powerfxrule)

|Property|Value|
|---|---|
|ReferencingEntity|`powerfxrule`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerfxrule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerpagecomponent"></a> owner_powerpagecomponent

Many-To-One Relationship: [powerpagecomponent owner_powerpagecomponent](powerpagecomponent.md#BKMK_owner_powerpagecomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagecomponent`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerpagecomponent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerpagesite"></a> owner_powerpagesite

Many-To-One Relationship: [powerpagesite owner_powerpagesite](powerpagesite.md#BKMK_owner_powerpagesite)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesite`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerpagesite`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerpagesitelanguage"></a> owner_powerpagesitelanguage

Many-To-One Relationship: [powerpagesitelanguage owner_powerpagesitelanguage](powerpagesitelanguage.md#BKMK_owner_powerpagesitelanguage)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesitelanguage`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerpagesitelanguage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerpagesitepublished"></a> owner_powerpagesitepublished

Many-To-One Relationship: [powerpagesitepublished owner_powerpagesitepublished](powerpagesitepublished.md#BKMK_owner_powerpagesitepublished)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesitepublished`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerpagesitepublished`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerpageslog"></a> owner_powerpageslog

Many-To-One Relationship: [powerpageslog owner_powerpageslog](powerpageslog.md#BKMK_owner_powerpageslog)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpageslog`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerpageslog`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerpagesmanagedidentity"></a> owner_powerpagesmanagedidentity

Many-To-One Relationship: [powerpagesmanagedidentity owner_powerpagesmanagedidentity](powerpagesmanagedidentity.md#BKMK_owner_powerpagesmanagedidentity)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesmanagedidentity`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerpagesmanagedidentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerpagesscanreport"></a> owner_powerpagesscanreport

Many-To-One Relationship: [powerpagesscanreport owner_powerpagesscanreport](powerpagesscanreport.md#BKMK_owner_powerpagesscanreport)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesscanreport`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerpagesscanreport`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_powerpagessiteaifeedback"></a> owner_powerpagessiteaifeedback

Many-To-One Relationship: [powerpagessiteaifeedback owner_powerpagessiteaifeedback](powerpagessiteaifeedback.md#BKMK_owner_powerpagessiteaifeedback)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagessiteaifeedback`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_powerpagessiteaifeedback`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_principalentitybusinessunitmap"></a> owner_principalentitybusinessunitmap

Many-To-One Relationship: [principalentitybusinessunitmap owner_principalentitybusinessunitmap](principalentitybusinessunitmap.md#BKMK_owner_principalentitybusinessunitmap)

|Property|Value|
|---|---|
|ReferencingEntity|`principalentitybusinessunitmap`|
|ReferencingAttribute|`principalid`|
|ReferencedEntityNavigationPropertyName|`owner_principalentitybusinessunitmap`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_privilegecheckerrun"></a> owner_privilegecheckerrun

Many-To-One Relationship: [privilegecheckerrun owner_privilegecheckerrun](privilegecheckerrun.md#BKMK_owner_privilegecheckerrun)

|Property|Value|
|---|---|
|ReferencingEntity|`privilegecheckerrun`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_privilegecheckerrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_processsessions"></a> owner_processsessions

Many-To-One Relationship: [processsession owner_processsessions](processsession.md#BKMK_owner_processsessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_processsessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_processstageparameter"></a> owner_processstageparameter

Many-To-One Relationship: [processstageparameter owner_processstageparameter](processstageparameter.md#BKMK_owner_processstageparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`processstageparameter`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_processstageparameter`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_queues"></a> owner_queues

Many-To-One Relationship: [queue owner_queues](queue.md#BKMK_owner_queues)

|Property|Value|
|---|---|
|ReferencingEntity|`queue`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_queues`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_recentlyused"></a> owner_recentlyused

Many-To-One Relationship: [recentlyused owner_recentlyused](recentlyused.md#BKMK_owner_recentlyused)

|Property|Value|
|---|---|
|ReferencingEntity|`recentlyused`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_recentlyused`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_recurrencerules"></a> owner_recurrencerules

Many-To-One Relationship: [recurrencerule owner_recurrencerules](recurrencerule.md#BKMK_owner_recurrencerules)

|Property|Value|
|---|---|
|ReferencingEntity|`recurrencerule`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_recurrencerules`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_recurringappointmentmasters"></a> owner_recurringappointmentmasters

Many-To-One Relationship: [recurringappointmentmaster owner_recurringappointmentmasters](recurringappointmentmaster.md#BKMK_owner_recurringappointmentmasters)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_recurringappointmentmasters`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_reports"></a> owner_reports

Many-To-One Relationship: [report owner_reports](report.md#BKMK_owner_reports)

|Property|Value|
|---|---|
|ReferencingEntity|`report`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_reports`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_retaineddataexcel"></a> owner_retaineddataexcel

Many-To-One Relationship: [retaineddataexcel owner_retaineddataexcel](retaineddataexcel.md#BKMK_owner_retaineddataexcel)

|Property|Value|
|---|---|
|ReferencingEntity|`retaineddataexcel`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_retaineddataexcel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_retentionconfig"></a> owner_retentionconfig

Many-To-One Relationship: [retentionconfig owner_retentionconfig](retentionconfig.md#BKMK_owner_retentionconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionconfig`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_retentionconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_retentionfailuredetail"></a> owner_retentionfailuredetail

Many-To-One Relationship: [retentionfailuredetail owner_retentionfailuredetail](retentionfailuredetail.md#BKMK_owner_retentionfailuredetail)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionfailuredetail`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_retentionfailuredetail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_retentionoperation"></a> owner_retentionoperation

Many-To-One Relationship: [retentionoperation owner_retentionoperation](retentionoperation.md#BKMK_owner_retentionoperation)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionoperation`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_retentionoperation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_retentionsuccessdetail"></a> owner_retentionsuccessdetail

Many-To-One Relationship: [retentionsuccessdetail owner_retentionsuccessdetail](retentionsuccessdetail.md#BKMK_owner_retentionsuccessdetail)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionsuccessdetail`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_retentionsuccessdetail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_savingrule"></a> owner_savingrule

Many-To-One Relationship: [savingrule owner_savingrule](savingrule.md#BKMK_owner_savingrule)

|Property|Value|
|---|---|
|ReferencingEntity|`savingrule`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_savingrule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_sharepointdocumentlocation"></a> owner_sharepointdocumentlocation

Many-To-One Relationship: [sharepointdocumentlocation owner_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_owner_sharepointdocumentlocation)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointdocumentlocation`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_sharepointdocumentlocation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_sharepointsite"></a> owner_sharepointsite

Many-To-One Relationship: [sharepointsite owner_sharepointsite](sharepointsite.md#BKMK_owner_sharepointsite)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointsite`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_sharepointsite`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_sideloadedaiplugin"></a> owner_sideloadedaiplugin

Many-To-One Relationship: [sideloadedaiplugin owner_sideloadedaiplugin](sideloadedaiplugin.md#BKMK_owner_sideloadedaiplugin)

|Property|Value|
|---|---|
|ReferencingEntity|`sideloadedaiplugin`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_sideloadedaiplugin`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_signal"></a> owner_signal

Many-To-One Relationship: [signal owner_signal](signal.md#BKMK_owner_signal)

|Property|Value|
|---|---|
|ReferencingEntity|`signal`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_signal`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_slas"></a> owner_slas

Many-To-One Relationship: [sla owner_slas](sla.md#BKMK_owner_slas)

|Property|Value|
|---|---|
|ReferencingEntity|`sla`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_slas`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_socialactivities"></a> owner_socialactivities

Many-To-One Relationship: [socialactivity owner_socialactivities](socialactivity.md#BKMK_owner_socialactivities)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_socialactivities`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_SocialProfile"></a> owner_SocialProfile

Many-To-One Relationship: [socialprofile owner_SocialProfile](socialprofile.md#BKMK_owner_SocialProfile)

|Property|Value|
|---|---|
|ReferencingEntity|`socialprofile`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_SocialProfile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_solutioncomponentbatchconfiguration"></a> owner_solutioncomponentbatchconfiguration

Many-To-One Relationship: [solutioncomponentbatchconfiguration owner_solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md#BKMK_owner_solutioncomponentbatchconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentbatchconfiguration`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_solutioncomponentbatchconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_stagesolutionupload"></a> owner_stagesolutionupload

Many-To-One Relationship: [stagesolutionupload owner_stagesolutionupload](stagesolutionupload.md#BKMK_owner_stagesolutionupload)

|Property|Value|
|---|---|
|ReferencingEntity|`stagesolutionupload`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_stagesolutionupload`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_synapsedatabase"></a> owner_synapsedatabase

Many-To-One Relationship: [synapsedatabase owner_synapsedatabase](synapsedatabase.md#BKMK_owner_synapsedatabase)

|Property|Value|
|---|---|
|ReferencingEntity|`synapsedatabase`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_synapsedatabase`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_SyncError"></a> owner_SyncError

Many-To-One Relationship: [syncerror owner_SyncError](syncerror.md#BKMK_owner_SyncError)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_SyncError`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_tag"></a> owner_tag

Many-To-One Relationship: [tag owner_tag](tag.md#BKMK_owner_tag)

|Property|Value|
|---|---|
|ReferencingEntity|`tag`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_tag`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_taggedflowsession"></a> owner_taggedflowsession

Many-To-One Relationship: [taggedflowsession owner_taggedflowsession](taggedflowsession.md#BKMK_owner_taggedflowsession)

|Property|Value|
|---|---|
|ReferencingEntity|`taggedflowsession`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_taggedflowsession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_taggedprocess"></a> owner_taggedprocess

Many-To-One Relationship: [taggedprocess owner_taggedprocess](taggedprocess.md#BKMK_owner_taggedprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`taggedprocess`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_taggedprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_tasks"></a> owner_tasks

Many-To-One Relationship: [task owner_tasks](task.md#BKMK_owner_tasks)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_tasks`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_templates"></a> owner_templates

Many-To-One Relationship: [template owner_templates](template.md#BKMK_owner_templates)

|Property|Value|
|---|---|
|ReferencingEntity|`template`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_templates`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_trait"></a> owner_trait

Many-To-One Relationship: [trait owner_trait](trait.md#BKMK_owner_trait)

|Property|Value|
|---|---|
|ReferencingEntity|`trait`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_trait`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_unstructuredfilesearchentity"></a> owner_unstructuredfilesearchentity

Many-To-One Relationship: [unstructuredfilesearchentity owner_unstructuredfilesearchentity](unstructuredfilesearchentity.md#BKMK_owner_unstructuredfilesearchentity)

|Property|Value|
|---|---|
|ReferencingEntity|`unstructuredfilesearchentity`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_unstructuredfilesearchentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_unstructuredfilesearchrecord"></a> owner_unstructuredfilesearchrecord

Many-To-One Relationship: [unstructuredfilesearchrecord owner_unstructuredfilesearchrecord](unstructuredfilesearchrecord.md#BKMK_owner_unstructuredfilesearchrecord)

|Property|Value|
|---|---|
|ReferencingEntity|`unstructuredfilesearchrecord`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_unstructuredfilesearchrecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_userform"></a> owner_userform

Many-To-One Relationship: [userform owner_userform](userform.md#BKMK_owner_userform)

|Property|Value|
|---|---|
|ReferencingEntity|`userform`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_userform`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_userquerys"></a> owner_userquerys

Many-To-One Relationship: [userquery owner_userquerys](userquery.md#BKMK_owner_userquerys)

|Property|Value|
|---|---|
|ReferencingEntity|`userquery`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_userquerys`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_userqueryvisualizations"></a> owner_userqueryvisualizations

Many-To-One Relationship: [userqueryvisualization owner_userqueryvisualizations](userqueryvisualization.md#BKMK_owner_userqueryvisualizations)

|Property|Value|
|---|---|
|ReferencingEntity|`userqueryvisualization`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_userqueryvisualizations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_workflowbinary"></a> owner_workflowbinary

Many-To-One Relationship: [workflowbinary owner_workflowbinary](workflowbinary.md#BKMK_owner_workflowbinary)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowbinary`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_workflowbinary`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_workflowmetadata"></a> owner_workflowmetadata

Many-To-One Relationship: [workflowmetadata owner_workflowmetadata](workflowmetadata.md#BKMK_owner_workflowmetadata)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowmetadata`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_workflowmetadata`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_workflows"></a> owner_workflows

Many-To-One Relationship: [workflow owner_workflows](workflow.md#BKMK_owner_workflows)

|Property|Value|
|---|---|
|ReferencingEntity|`workflow`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_workflows`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_workqueue"></a> owner_workqueue

Many-To-One Relationship: [workqueue owner_workqueue](workqueue.md#BKMK_owner_workqueue)

|Property|Value|
|---|---|
|ReferencingEntity|`workqueue`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_workqueue`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_owner_workqueueitem"></a> owner_workqueueitem

Many-To-One Relationship: [workqueueitem owner_workqueueitem](workqueueitem.md#BKMK_owner_workqueueitem)

|Property|Value|
|---|---|
|ReferencingEntity|`workqueueitem`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`owner_workqueueitem`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_slakpiinstance_owner"></a> slakpiinstance_owner

Many-To-One Relationship: [slakpiinstance slakpiinstance_owner](slakpiinstance.md#BKMK_slakpiinstance_owner)

|Property|Value|
|---|---|
|ReferencingEntity|`slakpiinstance`|
|ReferencingAttribute|`ownerid`|
|ReferencedEntityNavigationPropertyName|`slakpiinstance_owner`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

