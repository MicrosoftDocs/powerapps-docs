---
title: "Shortcut (mspp_shortcut)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Shortcut (mspp_shortcut)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Shortcut (mspp_shortcut)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_shortcuts<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_shortcuts(*mspp_shortcutid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_shortcuts(*mspp_shortcutid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_shortcuts<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_shortcuts(*mspp_shortcutid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_shortcuts|
|DisplayCollectionName|Shortcuts|
|DisplayName|Shortcut|
|EntitySetName|mspp_shortcuts|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_shortcuts|
|LogicalName|mspp_shortcut|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_shortcutid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_shortcut|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_description](#BKMK_mspp_description)
- [mspp_disabletargetvalidation](#BKMK_mspp_disabletargetvalidation)
- [mspp_displayorder](#BKMK_mspp_displayorder)
- [mspp_externalurl](#BKMK_mspp_externalurl)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_parentpage_webpageid](#BKMK_mspp_parentpage_webpageid)
- [mspp_shortcutId](#BKMK_mspp_shortcutId)
- [mspp_title](#BKMK_mspp_title)
- [mspp_webfileid](#BKMK_mspp_webfileid)
- [mspp_webpageid](#BKMK_mspp_webpageid)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)


### <a name="BKMK_mspp_createdby"></a> mspp_createdby

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_mspp_createdon"></a> mspp_createdon

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_mspp_description"></a> mspp_description

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_disabletargetvalidation"></a> mspp_disabletargetvalidation

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Disable Shortcut Target Validation|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_disabletargetvalidation|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_disabletargetvalidation Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_displayorder"></a> mspp_displayorder

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Display Order|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_displayorder|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|Recommended|
|Type|Integer|


### <a name="BKMK_mspp_externalurl"></a> mspp_externalurl

|Property|Value|
|--------|-----|
|Description||
|DisplayName|External URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_externalurl|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_modifiedby"></a> mspp_modifiedby

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_mspp_modifiedon"></a> mspp_modifiedon

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_mspp_name"></a> mspp_name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_parentpage_webpageid"></a> mspp_parentpage_webpageid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Page associated with Shortcut.|
|DisplayName|Parent Page|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_parentpage_webpageid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_webpage|
|Type|Lookup|


### <a name="BKMK_mspp_shortcutId"></a> mspp_shortcutId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Shortcut|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_shortcutid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_title"></a> mspp_title

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_title|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_webfileid"></a> mspp_webfileid

|Property|Value|
|--------|-----|
|Description|Web File that is pointed to by the shortcut|
|DisplayName|Web File|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webfileid|
|RequiredLevel|None|
|Targets|mspp_webfile|
|Type|Lookup|


### <a name="BKMK_mspp_webpageid"></a> mspp_webpageid

|Property|Value|
|--------|-----|
|Description|The web page that the shortcut points to|
|DisplayName|Web Page|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webpageid|
|RequiredLevel|None|
|Targets|mspp_webpage|
|Type|Lookup|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Shortcut.|
|DisplayName|Website|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_websiteid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_website|
|Type|Lookup|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Shortcut|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Shortcut|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|


<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [mspp_createdbyName](#BKMK_mspp_createdbyName)
- [mspp_createdbyYomiName](#BKMK_mspp_createdbyYomiName)
- [mspp_modifiedbyName](#BKMK_mspp_modifiedbyName)
- [mspp_modifiedbyYomiName](#BKMK_mspp_modifiedbyYomiName)
- [mspp_parentpage_webpageidName](#BKMK_mspp_parentpage_webpageidName)
- [mspp_webfileidName](#BKMK_mspp_webfileidName)
- [mspp_webpageidName](#BKMK_mspp_webpageidName)
- [mspp_websiteidName](#BKMK_mspp_websiteidName)


### <a name="BKMK_mspp_createdbyName"></a> mspp_createdbyName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_createdbyname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_createdbyYomiName"></a> mspp_createdbyYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_createdbyyominame|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_modifiedbyName"></a> mspp_modifiedbyName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_modifiedbyname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_modifiedbyYomiName"></a> mspp_modifiedbyYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_modifiedbyyominame|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_parentpage_webpageidName"></a> mspp_parentpage_webpageidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_parentpage_webpageidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_webfileidName"></a> mspp_webfileidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_webfileidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_webpageidName"></a> mspp_webpageidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_webpageidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_websiteidName"></a> mspp_websiteidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_websiteidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [mspp_shortcut_ActivityPointers](#BKMK_mspp_shortcut_ActivityPointers)
- [mspp_shortcut_adx_inviteredemptions](#BKMK_mspp_shortcut_adx_inviteredemptions)
- [mspp_shortcut_adx_portalcomments](#BKMK_mspp_shortcut_adx_portalcomments)
- [mspp_shortcut_chats](#BKMK_mspp_shortcut_chats)
- [mspp_shortcut_Appointments](#BKMK_mspp_shortcut_Appointments)
- [mspp_shortcut_Emails](#BKMK_mspp_shortcut_Emails)
- [mspp_shortcut_Faxes](#BKMK_mspp_shortcut_Faxes)
- [mspp_shortcut_Letters](#BKMK_mspp_shortcut_Letters)
- [mspp_shortcut_PhoneCalls](#BKMK_mspp_shortcut_PhoneCalls)
- [mspp_shortcut_Tasks](#BKMK_mspp_shortcut_Tasks)
- [mspp_shortcut_RecurringAppointmentMasters](#BKMK_mspp_shortcut_RecurringAppointmentMasters)
- [mspp_shortcut_SocialActivities](#BKMK_mspp_shortcut_SocialActivities)
- [mspp_shortcut_connections1](#BKMK_mspp_shortcut_connections1)
- [mspp_shortcut_connections2](#BKMK_mspp_shortcut_connections2)


### <a name="BKMK_mspp_shortcut_ActivityPointers"></a> mspp_shortcut_ActivityPointers

**Added by**: System Solution Solution

Same as the [mspp_shortcut_ActivityPointers](activitypointer.md#BKMK_mspp_shortcut_ActivityPointers) many-to-one relationship for the [activitypointer](activitypointer.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_ActivityPointers|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_adx_inviteredemptions"></a> mspp_shortcut_adx_inviteredemptions

**Added by**: Active Solution Solution

Same as the [mspp_shortcut_adx_inviteredemptions](adx_inviteredemption.md#BKMK_mspp_shortcut_adx_inviteredemptions) many-to-one relationship for the [adx_inviteredemption](adx_inviteredemption.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|adx_inviteredemption|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_adx_inviteredemptions|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_adx_portalcomments"></a> mspp_shortcut_adx_portalcomments

**Added by**: Active Solution Solution

Same as the [mspp_shortcut_adx_portalcomments](adx_portalcomment.md#BKMK_mspp_shortcut_adx_portalcomments) many-to-one relationship for the [adx_portalcomment](adx_portalcomment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|adx_portalcomment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_adx_portalcomments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_chats"></a> mspp_shortcut_chats

**Added by**: Activities Patch Solution

Same as the [mspp_shortcut_chats](chat.md#BKMK_mspp_shortcut_chats) many-to-one relationship for the [chat](chat.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|chat|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_chats|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_Appointments"></a> mspp_shortcut_Appointments

**Added by**: System Solution Solution

Same as the [mspp_shortcut_Appointments](appointment.md#BKMK_mspp_shortcut_Appointments) many-to-one relationship for the [appointment](appointment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_Appointments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_Emails"></a> mspp_shortcut_Emails

**Added by**: System Solution Solution

Same as the [mspp_shortcut_Emails](email.md#BKMK_mspp_shortcut_Emails) many-to-one relationship for the [email](email.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_Emails|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_Faxes"></a> mspp_shortcut_Faxes

**Added by**: System Solution Solution

Same as the [mspp_shortcut_Faxes](fax.md#BKMK_mspp_shortcut_Faxes) many-to-one relationship for the [fax](fax.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_Faxes|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_Letters"></a> mspp_shortcut_Letters

**Added by**: System Solution Solution

Same as the [mspp_shortcut_Letters](letter.md#BKMK_mspp_shortcut_Letters) many-to-one relationship for the [letter](letter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_Letters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_PhoneCalls"></a> mspp_shortcut_PhoneCalls

**Added by**: System Solution Solution

Same as the [mspp_shortcut_PhoneCalls](phonecall.md#BKMK_mspp_shortcut_PhoneCalls) many-to-one relationship for the [phonecall](phonecall.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_PhoneCalls|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_Tasks"></a> mspp_shortcut_Tasks

**Added by**: System Solution Solution

Same as the [mspp_shortcut_Tasks](task.md#BKMK_mspp_shortcut_Tasks) many-to-one relationship for the [task](task.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_Tasks|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_RecurringAppointmentMasters"></a> mspp_shortcut_RecurringAppointmentMasters

**Added by**: System Solution Solution

Same as the [mspp_shortcut_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_mspp_shortcut_RecurringAppointmentMasters) many-to-one relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_RecurringAppointmentMasters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_SocialActivities"></a> mspp_shortcut_SocialActivities

**Added by**: System Solution Solution

Same as the [mspp_shortcut_SocialActivities](socialactivity.md#BKMK_mspp_shortcut_SocialActivities) many-to-one relationship for the [socialactivity](socialactivity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_SocialActivities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_connections1"></a> mspp_shortcut_connections1

**Added by**: System Solution Solution

Same as the [mspp_shortcut_connections1](connection.md#BKMK_mspp_shortcut_connections1) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_shortcut_connections2"></a> mspp_shortcut_connections2

**Added by**: System Solution Solution

Same as the [mspp_shortcut_connections2](connection.md#BKMK_mspp_shortcut_connections2) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_shortcut_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_parentwebpage_shortcut](#BKMK_mspp_parentwebpage_shortcut)
- [mspp_systemuser_mspp_shortcut_createdby](#BKMK_mspp_systemuser_mspp_shortcut_createdby)
- [mspp_systemuser_mspp_shortcut_modifiedby](#BKMK_mspp_systemuser_mspp_shortcut_modifiedby)
- [mspp_webfile_shortcut](#BKMK_mspp_webfile_shortcut)
- [mspp_webpage_shortcut](#BKMK_mspp_webpage_shortcut)
- [mspp_website_shortcut](#BKMK_mspp_website_shortcut)


### <a name="BKMK_mspp_parentwebpage_shortcut"></a> mspp_parentwebpage_shortcut

See the [mspp_parentwebpage_shortcut](mspp_webpage.md#BKMK_mspp_parentwebpage_shortcut) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_shortcut_createdby"></a> mspp_systemuser_mspp_shortcut_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_shortcut_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_shortcut_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_shortcut_modifiedby"></a> mspp_systemuser_mspp_shortcut_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_shortcut_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_shortcut_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_webfile_shortcut"></a> mspp_webfile_shortcut

See the [mspp_webfile_shortcut](mspp_webfile.md#BKMK_mspp_webfile_shortcut) one-to-many relationship for the [mspp_webfile](mspp_webfile.md) table/entity.

### <a name="BKMK_mspp_webpage_shortcut"></a> mspp_webpage_shortcut

See the [mspp_webpage_shortcut](mspp_webpage.md#BKMK_mspp_webpage_shortcut) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_website_shortcut"></a> mspp_website_shortcut

See the [mspp_website_shortcut](mspp_website.md#BKMK_mspp_website_shortcut) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_shortcut?text=mspp_shortcut EntityType" />