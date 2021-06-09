---
title: "Owner table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Owner table/entity."
ms.date: 03/04/2021
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

# Owner table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Group of undeleted system users and undeleted teams. Owners can be used to control access to specific objects.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Owners|
|DisplayCollectionName|Owners|
|DisplayName|Owner|
|EntitySetName|owners|
|IsBPFEntity|False|
|LogicalCollectionName|owners|
|LogicalName|owner|
|OwnershipType|None|
|PrimaryIdAttribute|ownerid|
|PrimaryNameAttribute|name|
|SchemaName|Owner|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the Owner: systemuserid or teamid.|
|DisplayName|Owner|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [Name](#BKMK_Name)
- [OwnerIdType](#BKMK_OwnerIdType)
- [VersionNumber](#BKMK_VersionNumber)
- [YomiName](#BKMK_YomiName)


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the Owner.|
|DisplayName|Owner Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|160|
|RequiredLevel|ApplicationRequired|
|Type|String|


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


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_YomiName"></a> YomiName

|Property|Value|
|--------|-----|
|Description|Pronunciation of the name of the owner, written in phonetic hiragana or katakana characters.|
|DisplayName|Yomi Name|
|FormatName|PhoneticGuide|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yominame|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [owner_exchangesyncidmapping](#BKMK_owner_exchangesyncidmapping)
- [owner_interactionforemail](#BKMK_owner_interactionforemail)
- [owner_knowledgearticle](#BKMK_owner_knowledgearticle)
- [owner_sharepointsite](#BKMK_owner_sharepointsite)
- [owner_sharepointdocumentlocation](#BKMK_owner_sharepointdocumentlocation)
- [owner_goal](#BKMK_owner_goal)
- [owner_mailbox](#BKMK_owner_mailbox)
- [owner_importfiles](#BKMK_owner_importfiles)
- [owner_contacts](#BKMK_owner_contacts)
- [owner_userquerys](#BKMK_owner_userquerys)
- [owner_importmaps](#BKMK_owner_importmaps)
- [owner_workflows](#BKMK_owner_workflows)
- [owner_processsessions](#BKMK_owner_processsessions)
- [owner_postfollows](#BKMK_owner_postfollows)
- [owner_queues](#BKMK_owner_queues)
- [owner_emailserverprofile](#BKMK_owner_emailserverprofile)
- [owner_duplicaterules](#BKMK_owner_duplicaterules)
- [owner_SocialProfile](#BKMK_owner_SocialProfile)
- [owner_annotations](#BKMK_owner_annotations)
- [owner_mailmergetemplates](#BKMK_owner_mailmergetemplates)
- [owner_SyncError](#BKMK_owner_SyncError)
- [owner_asyncoperations](#BKMK_owner_asyncoperations)
- [slakpiinstance_owner](#BKMK_slakpiinstance_owner)
- [owner_accounts](#BKMK_owner_accounts)
- [owner_personaldocumenttemplates](#BKMK_owner_personaldocumenttemplates)
- [owner_feedback](#BKMK_owner_feedback)
- [owner_reports](#BKMK_owner_reports)
- [owner_connections](#BKMK_owner_connections)
- [owner_recurrencerules](#BKMK_owner_recurrencerules)
- [owner_actioncards](#BKMK_owner_actioncards)
- [owner_goalrollupquery](#BKMK_owner_goalrollupquery)
- [owner_userform](#BKMK_owner_userform)
- [owner_userqueryvisualizations](#BKMK_owner_userqueryvisualizations)
- [owner_slas](#BKMK_owner_slas)
- [owner_importdatas](#BKMK_owner_importdatas)
- [owner_importlogs](#BKMK_owner_importlogs)
- [owner_mailboxtrackingfolder](#BKMK_owner_mailboxtrackingfolder)
- [owner_categories](#BKMK_owner_categories)
- [owner_templates](#BKMK_owner_templates)
- [owner_activitypointers](#BKMK_owner_activitypointers)
- [owner_imports](#BKMK_owner_imports)
- [owner_emails](#BKMK_owner_emails)
- [owner_faxes](#BKMK_owner_faxes)
- [owner_letters](#BKMK_owner_letters)
- [owner_phonecalls](#BKMK_owner_phonecalls)
- [owner_tasks](#BKMK_owner_tasks)
- [owner_recurringappointmentmasters](#BKMK_owner_recurringappointmentmasters)
- [owner_socialactivities](#BKMK_owner_socialactivities)
- [owner_appointments](#BKMK_owner_appointments)
- [ActionCardUserState_Owner](#BKMK_ActionCardUserState_Owner)
- [owner_callbackregistration](#BKMK_owner_callbackregistration)
- [owner_canvasapp](#BKMK_owner_canvasapp)
- [owner_stagesolutionupload](#BKMK_owner_stagesolutionupload)
- [owner_exportsolutionupload](#BKMK_owner_exportsolutionupload)
- [owner_datalakefolder](#BKMK_owner_datalakefolder)
- [owner_datalakefolderpermission](#BKMK_owner_datalakefolderpermission)
- [owner_msdyn_dataflow](#BKMK_owner_msdyn_dataflow)
- [owner_connector](#BKMK_owner_connector)
- [owner_environmentvariabledefinition](#BKMK_owner_environmentvariabledefinition)
- [owner_environmentvariablevalue](#BKMK_owner_environmentvariablevalue)
- [owner_processstageparameter](#BKMK_owner_processstageparameter)
- [owner_flowsession](#BKMK_owner_flowsession)
- [owner_workflowbinary](#BKMK_owner_workflowbinary)
- [owner_connectionreference](#BKMK_owner_connectionreference)
- [owner_msdynce_botcontent](#BKMK_owner_msdynce_botcontent)
- [owner_conversationtranscript](#BKMK_owner_conversationtranscript)
- [owner_bot](#BKMK_owner_bot)
- [owner_botcomponent](#BKMK_owner_botcomponent)
- [owner_msdyn_serviceconfiguration](#BKMK_owner_msdyn_serviceconfiguration)
- [owner_msdyn_slakpi](#BKMK_owner_msdyn_slakpi)
- [owner_msdyn_federatedarticle](#BKMK_owner_msdyn_federatedarticle)
- [owner_msdyn_kmfederatedsearchconfig](#BKMK_owner_msdyn_kmfederatedsearchconfig)
- [owner_msdyn_knowledgearticleimage](#BKMK_owner_msdyn_knowledgearticleimage)
- [owner_msdyn_knowledgeinteractioninsight](#BKMK_owner_msdyn_knowledgeinteractioninsight)
- [owner_msdyn_knowledgesearchinsight](#BKMK_owner_msdyn_knowledgesearchinsight)
- [owner_msdyn_knowledgearticletemplate](#BKMK_owner_msdyn_knowledgearticletemplate)
- [owner_customapi](#BKMK_owner_customapi)
- [owner_customapirequestparameter](#BKMK_owner_customapirequestparameter)
- [owner_customapiresponseproperty](#BKMK_owner_customapiresponseproperty)
- [owner_msdyn_richtextfile](#BKMK_owner_msdyn_richtextfile)
- [owner_msdyn_aiconfiguration](#BKMK_owner_msdyn_aiconfiguration)
- [owner_msdyn_aimodel](#BKMK_owner_msdyn_aimodel)
- [owner_msdyn_aitemplate](#BKMK_owner_msdyn_aitemplate)
- [owner_msdyn_aibdataset](#BKMK_owner_msdyn_aibdataset)
- [owner_msdyn_aibdatasetfile](#BKMK_owner_msdyn_aibdatasetfile)
- [owner_msdyn_aibdatasetrecord](#BKMK_owner_msdyn_aibdatasetrecord)
- [owner_msdyn_aibdatasetscontainer](#BKMK_owner_msdyn_aibdatasetscontainer)
- [owner_msdyn_aibfile](#BKMK_owner_msdyn_aibfile)
- [owner_msdyn_aibfileattacheddata](#BKMK_owner_msdyn_aibfileattacheddata)
- [owner_msdyn_aifptrainingdocument](#BKMK_owner_msdyn_aifptrainingdocument)
- [owner_msdyn_aiodimage](#BKMK_owner_msdyn_aiodimage)
- [owner_msdyn_aiodlabel](#BKMK_owner_msdyn_aiodlabel)
- [owner_msdyn_aiodtrainingboundingbox](#BKMK_owner_msdyn_aiodtrainingboundingbox)
- [owner_msdyn_aiodtrainingimage](#BKMK_owner_msdyn_aiodtrainingimage)
- [owner_msdyn_analysiscomponent](#BKMK_owner_msdyn_analysiscomponent)
- [owner_msdyn_analysisjob](#BKMK_owner_msdyn_analysisjob)
- [owner_msdyn_analysisresult](#BKMK_owner_msdyn_analysisresult)
- [owner_msdyn_analysisresultdetail](#BKMK_owner_msdyn_analysisresultdetail)
- [owner_msdyn_solutionhealthrule](#BKMK_owner_msdyn_solutionhealthrule)
- [owner_msdyn_solutionhealthruleargument](#BKMK_owner_msdyn_solutionhealthruleargument)


### <a name="BKMK_owner_exchangesyncidmapping"></a> owner_exchangesyncidmapping

Same as exchangesyncidmapping table [owner_exchangesyncidmapping](exchangesyncidmapping.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|exchangesyncidmapping|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_exchangesyncidmapping|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_interactionforemail"></a> owner_interactionforemail

Same as interactionforemail table [owner_interactionforemail](interactionforemail.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|interactionforemail|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_new_interactionforemail|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_knowledgearticle"></a> owner_knowledgearticle

Same as knowledgearticle table [owner_knowledgearticle](knowledgearticle.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_knowledgearticle|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_sharepointsite"></a> owner_sharepointsite

Same as sharepointsite table [owner_sharepointsite](sharepointsite.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointsite|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_sharepointsite|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_sharepointdocumentlocation"></a> owner_sharepointdocumentlocation

Same as sharepointdocumentlocation table [owner_sharepointdocumentlocation](sharepointdocumentlocation.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_sharepointdocumentlocation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_goal"></a> owner_goal

Same as goal table [owner_goal](goal.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_goal|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_mailbox"></a> owner_mailbox

Same as mailbox table [owner_mailbox](mailbox.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailbox|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_mailbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_importfiles"></a> owner_importfiles

Same as importfile table [owner_importfiles](importfile.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importfile|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_importfiles|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_contacts"></a> owner_contacts

Same as contact table [owner_contacts](contact.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_contacts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_userquerys"></a> owner_userquerys

Same as userquery table [owner_userquerys](userquery.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userquery|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_userquerys|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_importmaps"></a> owner_importmaps

Same as importmap table [owner_importmaps](importmap.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importmap|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_importmaps|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_workflows"></a> owner_workflows

Same as workflow table [owner_workflows](workflow.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflow|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_workflows|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_processsessions"></a> owner_processsessions

Same as processsession table [owner_processsessions](processsession.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_processsessions|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_postfollows"></a> owner_postfollows

Same as postfollow table [owner_postfollows](postfollow.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_postfollows|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_queues"></a> owner_queues

Same as queue table [owner_queues](queue.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queue|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_queues|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_emailserverprofile"></a> owner_emailserverprofile

Same as emailserverprofile table [owner_emailserverprofile](emailserverprofile.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|emailserverprofile|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_emailserverprofile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_duplicaterules"></a> owner_duplicaterules

Same as duplicaterule table [owner_duplicaterules](duplicaterule.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterule|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_duplicaterules|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_SocialProfile"></a> owner_SocialProfile

Same as socialprofile table [owner_SocialProfile](socialprofile.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialprofile|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_SocialProfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_annotations"></a> owner_annotations

Same as annotation table [owner_annotations](annotation.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_annotations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_mailmergetemplates"></a> owner_mailmergetemplates

Same as mailmergetemplate table [owner_mailmergetemplates](mailmergetemplate.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailmergetemplate|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_mailmergetemplates|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_SyncError"></a> owner_SyncError

Same as syncerror table [owner_SyncError](syncerror.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_SyncError|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_asyncoperations"></a> owner_asyncoperations

Same as asyncoperation table [owner_asyncoperations](asyncoperation.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_asyncoperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_slakpiinstance_owner"></a> slakpiinstance_owner

Same as slakpiinstance table [slakpiinstance_owner](slakpiinstance.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slakpiinstance|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|slakpiinstance_owner|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_accounts"></a> owner_accounts

Same as account table [owner_accounts](account.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_accounts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_personaldocumenttemplates"></a> owner_personaldocumenttemplates

Same as personaldocumenttemplate table [owner_personaldocumenttemplates](personaldocumenttemplate.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|personaldocumenttemplate|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_personaldocumenttemplates|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_feedback"></a> owner_feedback

Same as feedback table [owner_feedback](feedback.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|feedback|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_feedback|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_reports"></a> owner_reports

Same as report table [owner_reports](report.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|report|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_reports|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_connections"></a> owner_connections

Same as connection table [owner_connections](connection.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_connections|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_recurrencerules"></a> owner_recurrencerules

Same as recurrencerule table [owner_recurrencerules](recurrencerule.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurrencerule|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_recurrencerules|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_actioncards"></a> owner_actioncards

Same as actioncard table [owner_actioncards](actioncard.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncard|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_actioncards|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_goalrollupquery"></a> owner_goalrollupquery

Same as goalrollupquery table [owner_goalrollupquery](goalrollupquery.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goalrollupquery|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_goalrollupquery|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_userform"></a> owner_userform

Same as userform table [owner_userform](userform.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userform|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_userform|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_userqueryvisualizations"></a> owner_userqueryvisualizations

Same as userqueryvisualization table [owner_userqueryvisualizations](userqueryvisualization.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userqueryvisualization|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_userqueryvisualizations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_slas"></a> owner_slas

Same as sla table [owner_slas](sla.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sla|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_slas|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_importdatas"></a> owner_importdatas

Same as importdata table [owner_importdatas](importdata.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importdata|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_importdatas|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_importlogs"></a> owner_importlogs

Same as importlog table [owner_importlogs](importlog.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importlog|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_importlogs|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_mailboxtrackingfolder"></a> owner_mailboxtrackingfolder

Same as mailboxtrackingfolder table [owner_mailboxtrackingfolder](mailboxtrackingfolder.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_mailboxtrackingfolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_categories"></a> owner_categories

Same as category table [owner_categories](category.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|category|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_categories|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_templates"></a> owner_templates

Same as template table [owner_templates](template.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|template|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_templates|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_activitypointers"></a> owner_activitypointers

Same as activitypointer table [owner_activitypointers](activitypointer.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_activitypointers|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_imports"></a> owner_imports

Same as import table [owner_imports](import.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|import|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_imports|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_emails"></a> owner_emails

Same as email table [owner_emails](email.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_emails|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_faxes"></a> owner_faxes

Same as fax table [owner_faxes](fax.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_faxes|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_letters"></a> owner_letters

Same as letter table [owner_letters](letter.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_letters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_phonecalls"></a> owner_phonecalls

Same as phonecall table [owner_phonecalls](phonecall.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_phonecalls|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_tasks"></a> owner_tasks

Same as task table [owner_tasks](task.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_tasks|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_recurringappointmentmasters"></a> owner_recurringappointmentmasters

Same as recurringappointmentmaster table [owner_recurringappointmentmasters](recurringappointmentmaster.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_recurringappointmentmasters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_socialactivities"></a> owner_socialactivities

Same as socialactivity table [owner_socialactivities](socialactivity.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_socialactivities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_appointments"></a> owner_appointments

Same as appointment table [owner_appointments](appointment.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_appointments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_ActionCardUserState_Owner"></a> ActionCardUserState_Owner

Same as actioncarduserstate table [ActionCardUserState_Owner](actioncarduserstate.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|actioncarduserstate|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|ActionCardUserState_Owner|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_callbackregistration"></a> owner_callbackregistration

Same as callbackregistration table [owner_callbackregistration](callbackregistration.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|callbackregistration|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_callbackregistration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_canvasapp"></a> owner_canvasapp

Same as canvasapp table [owner_canvasapp](canvasapp.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|canvasapp|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_canvasapp|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_stagesolutionupload"></a> owner_stagesolutionupload

**Added by**: Active Solution Solution

Same as stagesolutionupload table [owner_stagesolutionupload](stagesolutionupload.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|stagesolutionupload|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_stagesolutionupload|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_exportsolutionupload"></a> owner_exportsolutionupload

**Added by**: Active Solution Solution

Same as exportsolutionupload table [owner_exportsolutionupload](exportsolutionupload.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|exportsolutionupload|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_exportsolutionupload|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_datalakefolder"></a> owner_datalakefolder

**Added by**: Active Solution Solution

Same as datalakefolder table [owner_datalakefolder](datalakefolder.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolder|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_datalakefolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_datalakefolderpermission"></a> owner_datalakefolderpermission

**Added by**: Active Solution Solution

Same as datalakefolderpermission table [owner_datalakefolderpermission](datalakefolderpermission.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolderpermission|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_datalakefolderpermission|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_dataflow"></a> owner_msdyn_dataflow

**Added by**: Active Solution Solution

Same as msdyn_dataflow table [owner_msdyn_dataflow](msdyn_dataflow.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_msdyn_dataflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_connector"></a> owner_connector

**Added by**: Active Solution Solution

Same as connector table [owner_connector](connector.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connector|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_connector|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_environmentvariabledefinition"></a> owner_environmentvariabledefinition

**Added by**: Active Solution Solution

Same as environmentvariabledefinition table [owner_environmentvariabledefinition](environmentvariabledefinition.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariabledefinition|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_environmentvariabledefinition|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_environmentvariablevalue"></a> owner_environmentvariablevalue

**Added by**: Active Solution Solution

Same as environmentvariablevalue table [owner_environmentvariablevalue](environmentvariablevalue.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariablevalue|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_environmentvariablevalue|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_processstageparameter"></a> owner_processstageparameter

**Added by**: Active Solution Solution

Same as processstageparameter table [owner_processstageparameter](processstageparameter.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processstageparameter|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_processstageparameter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_flowsession"></a> owner_flowsession

**Added by**: Active Solution Solution

Same as flowsession table [owner_flowsession](flowsession.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowsession|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_flowsession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_workflowbinary"></a> owner_workflowbinary

**Added by**: Active Solution Solution

Same as workflowbinary table [owner_workflowbinary](workflowbinary.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowbinary|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_workflowbinary|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_connectionreference"></a> owner_connectionreference

**Added by**: Active Solution Solution

Same as connectionreference table [owner_connectionreference](connectionreference.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionreference|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_connectionreference|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdynce_botcontent"></a> owner_msdynce_botcontent

**Added by**: Active Solution Solution

Same as msdynce_botcontent table [owner_msdynce_botcontent](msdynce_botcontent.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdynce_botcontent|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdynce_botcontent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_conversationtranscript"></a> owner_conversationtranscript

**Added by**: Active Solution Solution

Same as conversationtranscript table [owner_conversationtranscript](conversationtranscript.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|conversationtranscript|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_conversationtranscript|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_bot"></a> owner_bot

**Added by**: Active Solution Solution

Same as bot table [owner_bot](bot.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bot|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_bot|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_botcomponent"></a> owner_botcomponent

**Added by**: Active Solution Solution

Same as botcomponent table [owner_botcomponent](botcomponent.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|botcomponent|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_botcomponent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_serviceconfiguration"></a> owner_msdyn_serviceconfiguration

**Added by**: Active Solution Solution

Same as msdyn_serviceconfiguration table [owner_msdyn_serviceconfiguration](msdyn_serviceconfiguration.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_serviceconfiguration|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_msdyn_serviceconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_slakpi"></a> owner_msdyn_slakpi

**Added by**: Active Solution Solution

Same as msdyn_slakpi table [owner_msdyn_slakpi](msdyn_slakpi.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_slakpi|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_msdyn_slakpi|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_federatedarticle"></a> owner_msdyn_federatedarticle

**Added by**: Active Solution Solution

Same as msdyn_federatedarticle table [owner_msdyn_federatedarticle](msdyn_federatedarticle.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticle|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_msdyn_federatedarticle|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_kmfederatedsearchconfig"></a> owner_msdyn_kmfederatedsearchconfig

**Added by**: Active Solution Solution

Same as msdyn_kmfederatedsearchconfig table [owner_msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmfederatedsearchconfig|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_msdyn_kmfederatedsearchconfig|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_knowledgearticleimage"></a> owner_msdyn_knowledgearticleimage

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticleimage table [owner_msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticleimage|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_msdyn_knowledgearticleimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_knowledgeinteractioninsight"></a> owner_msdyn_knowledgeinteractioninsight

**Added by**: Active Solution Solution

Same as msdyn_knowledgeinteractioninsight table [owner_msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgeinteractioninsight|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_msdyn_knowledgeinteractioninsight|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_knowledgesearchinsight"></a> owner_msdyn_knowledgesearchinsight

**Added by**: Active Solution Solution

Same as msdyn_knowledgesearchinsight table [owner_msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchinsight|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_msdyn_knowledgesearchinsight|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_knowledgearticletemplate"></a> owner_msdyn_knowledgearticletemplate

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticletemplate table [owner_msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticletemplate|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_msdyn_knowledgearticletemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_customapi"></a> owner_customapi

**Added by**: Active Solution Solution

Same as customapi table [owner_customapi](customapi.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapi|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_customapi|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_customapirequestparameter"></a> owner_customapirequestparameter

**Added by**: Active Solution Solution

Same as customapirequestparameter table [owner_customapirequestparameter](customapirequestparameter.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapirequestparameter|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_customapirequestparameter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_customapiresponseproperty"></a> owner_customapiresponseproperty

**Added by**: Active Solution Solution

Same as customapiresponseproperty table [owner_customapiresponseproperty](customapiresponseproperty.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapiresponseproperty|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_customapiresponseproperty|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_richtextfile"></a> owner_msdyn_richtextfile

**Added by**: Active Solution Solution

Same as msdyn_richtextfile table [owner_msdyn_richtextfile](msdyn_richtextfile.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_richtextfile|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|owner_msdyn_richtextfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aiconfiguration"></a> owner_msdyn_aiconfiguration

**Added by**: Active Solution Solution

Same as msdyn_aiconfiguration table [owner_msdyn_aiconfiguration](msdyn_aiconfiguration.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiconfiguration|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aiconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aimodel"></a> owner_msdyn_aimodel

**Added by**: Active Solution Solution

Same as msdyn_aimodel table [owner_msdyn_aimodel](msdyn_aimodel.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aimodel|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aimodel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aitemplate"></a> owner_msdyn_aitemplate

**Added by**: Active Solution Solution

Same as msdyn_aitemplate table [owner_msdyn_aitemplate](msdyn_aitemplate.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aitemplate|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aitemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aibdataset"></a> owner_msdyn_aibdataset

**Added by**: Active Solution Solution

Same as msdyn_aibdataset table [owner_msdyn_aibdataset](msdyn_aibdataset.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdataset|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aibdataset|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aibdatasetfile"></a> owner_msdyn_aibdatasetfile

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetfile table [owner_msdyn_aibdatasetfile](msdyn_aibdatasetfile.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetfile|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aibdatasetfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aibdatasetrecord"></a> owner_msdyn_aibdatasetrecord

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetrecord table [owner_msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetrecord|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aibdatasetrecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aibdatasetscontainer"></a> owner_msdyn_aibdatasetscontainer

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetscontainer table [owner_msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetscontainer|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aibdatasetscontainer|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aibfile"></a> owner_msdyn_aibfile

**Added by**: Active Solution Solution

Same as msdyn_aibfile table [owner_msdyn_aibfile](msdyn_aibfile.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfile|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aibfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aibfileattacheddata"></a> owner_msdyn_aibfileattacheddata

**Added by**: Active Solution Solution

Same as msdyn_aibfileattacheddata table [owner_msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfileattacheddata|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aibfileattacheddata|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aifptrainingdocument"></a> owner_msdyn_aifptrainingdocument

**Added by**: Active Solution Solution

Same as msdyn_aifptrainingdocument table [owner_msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aifptrainingdocument|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aifptrainingdocument|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aiodimage"></a> owner_msdyn_aiodimage

**Added by**: Active Solution Solution

Same as msdyn_aiodimage table [owner_msdyn_aiodimage](msdyn_aiodimage.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodimage|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aiodimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aiodlabel"></a> owner_msdyn_aiodlabel

**Added by**: Active Solution Solution

Same as msdyn_aiodlabel table [owner_msdyn_aiodlabel](msdyn_aiodlabel.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodlabel|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aiodlabel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aiodtrainingboundingbox"></a> owner_msdyn_aiodtrainingboundingbox

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingboundingbox table [owner_msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingboundingbox|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aiodtrainingboundingbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_aiodtrainingimage"></a> owner_msdyn_aiodtrainingimage

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingimage table [owner_msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingimage|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_aiodtrainingimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_analysiscomponent"></a> owner_msdyn_analysiscomponent

**Added by**: Active Solution Solution

Same as msdyn_analysiscomponent table [owner_msdyn_analysiscomponent](msdyn_analysiscomponent.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysiscomponent|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_analysiscomponent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_analysisjob"></a> owner_msdyn_analysisjob

**Added by**: Active Solution Solution

Same as msdyn_analysisjob table [owner_msdyn_analysisjob](msdyn_analysisjob.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisjob|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_analysisjob|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_analysisresult"></a> owner_msdyn_analysisresult

**Added by**: Active Solution Solution

Same as msdyn_analysisresult table [owner_msdyn_analysisresult](msdyn_analysisresult.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresult|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_analysisresult|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_analysisresultdetail"></a> owner_msdyn_analysisresultdetail

**Added by**: Active Solution Solution

Same as msdyn_analysisresultdetail table [owner_msdyn_analysisresultdetail](msdyn_analysisresultdetail.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresultdetail|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_analysisresultdetail|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_solutionhealthrule"></a> owner_msdyn_solutionhealthrule

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthrule table [owner_msdyn_solutionhealthrule](msdyn_solutionhealthrule.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthrule|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_solutionhealthrule|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_owner_msdyn_solutionhealthruleargument"></a> owner_msdyn_solutionhealthruleargument

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthruleargument table [owner_msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleargument|
|ReferencingAttribute|ownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|owner_msdyn_solutionhealthruleargument|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
