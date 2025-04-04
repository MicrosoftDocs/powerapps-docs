---
title: "Subject table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Subject table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Subject table/entity reference (Microsoft Dataverse)

Information regarding subjects available in the system.

## Messages

The following table lists the messages for the Subject table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /subjects<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /subjects(*subjectid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /subjects(*subjectid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /subjects<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /subjects(*subjectid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /subjects(*subjectid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Subject table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Subject** |
| **DisplayCollectionName** | **Subjects** |
| **SchemaName** | `Subject` |
| **CollectionSchemaName** | `Subjects` |
| **EntitySetName** | `subjects`|
| **LogicalName** | `subject` |
| **LogicalCollectionName** | `subjects` |
| **PrimaryIdAttribute** | `subjectid` |
| **PrimaryNameAttribute** |`title` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Description](#BKMK_Description)
- [FeatureMask](#BKMK_FeatureMask)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ParentSubject](#BKMK_ParentSubject)
- [SubjectId](#BKMK_SubjectId)
- [Title](#BKMK_Title)

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the subject.**|
|DisplayName|**Description**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_FeatureMask"></a> FeatureMask

|Property|Value|
|---|---|
|Description|**Information that specifies when the subject will be displayed in lists of subjects.**|
|DisplayName|**Feature Mask**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`featuremask`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Unique identifier of the data import or data migration that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
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

### <a name="BKMK_ParentSubject"></a> ParentSubject

|Property|Value|
|---|---|
|Description|**Unique identifier of the parent subject.**|
|DisplayName|**Parent Subject**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentsubject`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|subject|

### <a name="BKMK_SubjectId"></a> SubjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the subject.**|
|DisplayName|**Subject**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subjectid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Title"></a> Title

|Property|Value|
|---|---|
|Description|**Title of the subject.**|
|DisplayName|**Title**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`title`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByExternalParty](#BKMK_CreatedByExternalParty)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByExternalParty](#BKMK_ModifiedByExternalParty)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the subject.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedByExternalParty"></a> CreatedByExternalParty

|Property|Value|
|---|---|
|Description|**Shows the external party who created the record.**|
|DisplayName|**Created By (External Party)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdbyexternalparty`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|externalparty|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the subject was created.**|
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
|Description|**Unique identifier of the delegate user who created the subject.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the subject.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedByExternalParty"></a> ModifiedByExternalParty

|Property|Value|
|---|---|
|Description|**Shows the external party who modified the record.**|
|DisplayName|**Modified By (External Party)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedbyexternalparty`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|externalparty|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the subject was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the subject.**|
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
|Description|**Unique identifier for the organization associated with the subject.**|
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
|Description|**Version number of the subject.**|
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

- [lk_subject_createdonbehalfby](#BKMK_lk_subject_createdonbehalfby)
- [lk_subject_modifiedonbehalfby](#BKMK_lk_subject_modifiedonbehalfby)
- [lk_subjectbase_createdby](#BKMK_lk_subjectbase_createdby)
- [lk_subjectbase_modifiedby](#BKMK_lk_subjectbase_modifiedby)
- [organization_subjects](#BKMK_organization_subjects)
- [subject_parent_subject](#BKMK_subject_parent_subject-many-to-one)

### <a name="BKMK_lk_subject_createdonbehalfby"></a> lk_subject_createdonbehalfby

One-To-Many Relationship: [systemuser lk_subject_createdonbehalfby](systemuser.md#BKMK_lk_subject_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_subject_modifiedonbehalfby"></a> lk_subject_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_subject_modifiedonbehalfby](systemuser.md#BKMK_lk_subject_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_subjectbase_createdby"></a> lk_subjectbase_createdby

One-To-Many Relationship: [systemuser lk_subjectbase_createdby](systemuser.md#BKMK_lk_subjectbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_subjectbase_modifiedby"></a> lk_subjectbase_modifiedby

One-To-Many Relationship: [systemuser lk_subjectbase_modifiedby](systemuser.md#BKMK_lk_subjectbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_subjects"></a> organization_subjects

One-To-Many Relationship: [organization organization_subjects](organization.md#BKMK_organization_subjects)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_subject_parent_subject-many-to-one"></a> subject_parent_subject

One-To-Many Relationship: [subject subject_parent_subject](#BKMK_subject_parent_subject-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`subject`|
|ReferencedAttribute|`subjectid`|
|ReferencingAttribute|`parentsubject`|
|ReferencingEntityNavigationPropertyName|`parentsubject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [msdyn_subject_knowledgearticletemplate_subjectid](#BKMK_msdyn_subject_knowledgearticletemplate_subjectid)
- [Subject_AsyncOperations](#BKMK_Subject_AsyncOperations)
- [Subject_BulkDeleteFailures](#BKMK_Subject_BulkDeleteFailures)
- [subject_kb_articles](#BKMK_subject_kb_articles)
- [subject_knowledgearticles](#BKMK_subject_knowledgearticles)
- [subject_parent_subject](#BKMK_subject_parent_subject-one-to-many)
- [Subject_ProcessSessions](#BKMK_Subject_ProcessSessions)
- [Subject_SyncErrors](#BKMK_Subject_SyncErrors)

### <a name="BKMK_msdyn_subject_knowledgearticletemplate_subjectid"></a> msdyn_subject_knowledgearticletemplate_subjectid

Many-To-One Relationship: [msdyn_knowledgearticletemplate msdyn_subject_knowledgearticletemplate_subjectid](msdyn_knowledgearticletemplate.md#BKMK_msdyn_subject_knowledgearticletemplate_subjectid)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgearticletemplate`|
|ReferencingAttribute|`msdyn_subjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_subject_knowledgearticletemplate_subjectid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Subject_AsyncOperations"></a> Subject_AsyncOperations

Many-To-One Relationship: [asyncoperation Subject_AsyncOperations](asyncoperation.md#BKMK_Subject_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Subject_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Subject_BulkDeleteFailures"></a> Subject_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Subject_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Subject_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Subject_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_subject_kb_articles"></a> subject_kb_articles

Many-To-One Relationship: [kbarticle subject_kb_articles](kbarticle.md#BKMK_subject_kb_articles)

|Property|Value|
|---|---|
|ReferencingEntity|`kbarticle`|
|ReferencingAttribute|`subjectid`|
|ReferencedEntityNavigationPropertyName|`subject_kb_articles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_subject_knowledgearticles"></a> subject_knowledgearticles

Many-To-One Relationship: [knowledgearticle subject_knowledgearticles](knowledgearticle.md#BKMK_subject_knowledgearticles)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`subjectid`|
|ReferencedEntityNavigationPropertyName|`subject_knowledgearticles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_subject_parent_subject-one-to-many"></a> subject_parent_subject

Many-To-One Relationship: [subject subject_parent_subject](#BKMK_subject_parent_subject-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`subject`|
|ReferencingAttribute|`parentsubject`|
|ReferencedEntityNavigationPropertyName|`subject_parent_subject`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Subject_ProcessSessions"></a> Subject_ProcessSessions

Many-To-One Relationship: [processsession Subject_ProcessSessions](processsession.md#BKMK_Subject_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Subject_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Subject_SyncErrors"></a> Subject_SyncErrors

Many-To-One Relationship: [syncerror Subject_SyncErrors](syncerror.md#BKMK_Subject_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Subject_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.subject?displayProperty=fullName>
