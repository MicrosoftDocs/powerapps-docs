---
title: "ProcessStage Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the ProcessStage entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# ProcessStage Entity Reference

Stage associated with a process.

## Entity Properties

**DisplayName**: Process Stage<br />
**DisplayCollectionName**: Process Stages<br />
**SchemaName**: ProcessStage<br />
**CollectionSchemaName**: ProcessStages<br />
**LogicalName**: processstage<br />
**LogicalCollectionName**: processstages<br />
**EntitySetName**: processstages<br />
**PrimaryIdAttribute**: processstageid<br />
**PrimaryNameAttribute**: stagename<br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [PrimaryEntityTypeCode](#BKMK_PrimaryEntityTypeCode)
- [ProcessId](#BKMK_ProcessId)
- [ProcessStageId](#BKMK_ProcessStageId)
- [StageCategory](#BKMK_StageCategory)
- [StageName](#BKMK_StageName)


### <a name="BKMK_PrimaryEntityTypeCode"></a> PrimaryEntityTypeCode

**Description**: Primary entity associated with the stage.<br />
**DisplayName**: Primary Entity<br />
**LogicalName**: primaryentitytypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_ProcessId"></a> ProcessId

**Description**: Shows the ID of the process.<br />
**DisplayName**: Process<br />
**LogicalName**: processid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: workflow


### <a name="BKMK_ProcessStageId"></a> ProcessStageId

**Description**: Shows the ID of the process stage record.<br />
**DisplayName**: Process Stage<br />
**LogicalName**: processstageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_StageCategory"></a> StageCategory

**Description**: Select the category of the sales process.<br />
**DisplayName**: Stage Category<br />
**LogicalName**: stagecategory<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Qualify
- **Value**: 1 **Label**: Develop
- **Value**: 2 **Label**: Propose
- **Value**: 3 **Label**: Close
- **Value**: 4 **Label**: Identify
- **Value**: 5 **Label**: Research
- **Value**: 6 **Label**: Resolve
- **Value**: 7 **Label**: Approval



### <a name="BKMK_StageName"></a> StageName

**Description**: Type a name for the process stage.<br />
**DisplayName**: Process Stage Name<br />
**LogicalName**: stagename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ClientData](#BKMK_ClientData)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [ProcessIdName](#BKMK_ProcessIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ClientData"></a> ClientData

**Description**: Step metadata for process stage<br />
**DisplayName**: Client Data<br />
**LogicalName**: clientdata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Select the business unit that owns the record.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ProcessIdName"></a> ProcessIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: processidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the process stage.<br />
**DisplayName**: Version Number<br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

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


### <a name="BKMK_processstage_knowledgearticle"></a> processstage_knowledgearticle

Same as knowledgearticle entity [processstage_knowledgearticle](knowledgearticle.md#BKMK_processstage_knowledgearticle) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_knowledgearticle<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processstage_contact"></a> processstage_contact

Same as contact entity [processstage_contact](contact.md#BKMK_processstage_contact) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_contact<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processstage_teams"></a> processstage_teams

Same as team entity [processstage_teams](team.md#BKMK_processstage_teams) Many-To-One relationship.

**ReferencingEntity**: team<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_teams<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ProcessStage_SyncErrors"></a> ProcessStage_SyncErrors

Same as syncerror entity [ProcessStage_SyncErrors](syncerror.md#BKMK_ProcessStage_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: ProcessStage_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_processstage_recurringappointmentmasters"></a> processstage_recurringappointmentmasters

Same as recurringappointmentmaster entity [processstage_recurringappointmentmasters](recurringappointmentmaster.md#BKMK_processstage_recurringappointmentmasters) Many-To-One relationship.

**ReferencingEntity**: recurringappointmentmaster<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_recurringappointmentmasters<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processstage_letters"></a> processstage_letters

Same as letter entity [processstage_letters](letter.md#BKMK_processstage_letters) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_letters<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processstage_faxes"></a> processstage_faxes

Same as fax entity [processstage_faxes](fax.md#BKMK_processstage_faxes) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_faxes<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processstage_tasks"></a> processstage_tasks

Same as task entity [processstage_tasks](task.md#BKMK_processstage_tasks) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_tasks<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processstage_account"></a> processstage_account

Same as account entity [processstage_account](account.md#BKMK_processstage_account) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_account<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_translationprocess_activestageid"></a> lk_translationprocess_activestageid

Same as translationprocess entity [lk_translationprocess_activestageid](translationprocess.md#BKMK_lk_translationprocess_activestageid) Many-To-One relationship.

**ReferencingEntity**: translationprocess<br />
**ReferencingAttribute**: activestageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: processstage_translationprocess<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processstage_systemusers"></a> processstage_systemusers

Same as systemuser entity [processstage_systemusers](systemuser.md#BKMK_processstage_systemusers) Many-To-One relationship.

**ReferencingEntity**: systemuser<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_systemusers<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_newprocess_activestageid"></a> lk_newprocess_activestageid

Same as newprocess entity [lk_newprocess_activestageid](newprocess.md#BKMK_lk_newprocess_activestageid) Many-To-One relationship.

**ReferencingEntity**: newprocess<br />
**ReferencingAttribute**: activestageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: processstage_newprocess<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processstage_emails"></a> processstage_emails

Same as email entity [processstage_emails](email.md#BKMK_processstage_emails) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_emails<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processstage_appointments"></a> processstage_appointments

Same as appointment entity [processstage_appointments](appointment.md#BKMK_processstage_appointments) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_appointments<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processstage_phonecalls"></a> processstage_phonecalls

Same as phonecall entity [processstage_phonecalls](phonecall.md#BKMK_processstage_phonecalls) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: stageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processstage_phonecalls<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_expiredprocess_activestageid"></a> lk_expiredprocess_activestageid

Same as expiredprocess entity [lk_expiredprocess_activestageid](expiredprocess.md#BKMK_lk_expiredprocess_activestageid) Many-To-One relationship.

**ReferencingEntity**: expiredprocess<br />
**ReferencingAttribute**: activestageid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: processstage_expiredprocess<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.


### <a name="BKMK_process_processstage"></a> process_processstage

See workflow Entity [process_processstage](workflow.md#BKMK_process_processstage) One-To-Many relationship.
processstage

