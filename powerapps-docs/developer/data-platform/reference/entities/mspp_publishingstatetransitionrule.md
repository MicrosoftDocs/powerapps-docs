---
title: "Publishing State Transition Rule (mspp_publishingstatetransitionrule)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Publishing State Transition Rule (mspp_publishingstatetransitionrule)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Publishing State Transition Rule (mspp_publishingstatetransitionrule)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_publishingstatetransitionrules<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_publishingstatetransitionrules(*mspp_publishingstatetransitionruleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_publishingstatetransitionrules(*mspp_publishingstatetransitionruleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_publishingstatetransitionrules<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_publishingstatetransitionrules(*mspp_publishingstatetransitionruleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_publishingstatetransitionrules|
|DisplayCollectionName|Publishing State Transition Rules|
|DisplayName|Publishing State Transition Rule|
|EntitySetName|mspp_publishingstatetransitionrules|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_publishingstatetransitionrules|
|LogicalName|mspp_publishingstatetransitionrule|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_publishingstatetransitionruleid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_publishingstatetransitionrule|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_fromstate_publishingstateid](#BKMK_mspp_fromstate_publishingstateid)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_publishingstatetransitionruleId](#BKMK_mspp_publishingstatetransitionruleId)
- [mspp_tostate_publishingstateid](#BKMK_mspp_tostate_publishingstateid)
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


### <a name="BKMK_mspp_fromstate_publishingstateid"></a> mspp_fromstate_publishingstateid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Publishing State associated with Publishing State Transition Rule.|
|DisplayName|From State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_fromstate_publishingstateid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_publishingstate|
|Type|Lookup|


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


### <a name="BKMK_mspp_publishingstatetransitionruleId"></a> mspp_publishingstatetransitionruleId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Publishing State Transition Rule|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_publishingstatetransitionruleid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_tostate_publishingstateid"></a> mspp_tostate_publishingstateid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Publishing State associated with Publishing State Transition Rule.|
|DisplayName|To State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_tostate_publishingstateid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_publishingstate|
|Type|Lookup|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Publishing State Transition Rule.|
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
|Description|Status of the Publishing State Transition Rule|
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
|Description|Reason for the status of the Publishing State Transition Rule|
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
- [mspp_fromstate_publishingstateidName](#BKMK_mspp_fromstate_publishingstateidName)
- [mspp_modifiedbyName](#BKMK_mspp_modifiedbyName)
- [mspp_modifiedbyYomiName](#BKMK_mspp_modifiedbyYomiName)
- [mspp_tostate_publishingstateidName](#BKMK_mspp_tostate_publishingstateidName)
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


### <a name="BKMK_mspp_fromstate_publishingstateidName"></a> mspp_fromstate_publishingstateidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_fromstate_publishingstateidname|
|MaxLength|100|
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


### <a name="BKMK_mspp_tostate_publishingstateidName"></a> mspp_tostate_publishingstateidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_tostate_publishingstateidname|
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

- [mspp_publishingstatetransitionrule_ActivityPointers](#BKMK_mspp_publishingstatetransitionrule_ActivityPointers)
- [mspp_publishingstatetransitionrule_adx_inviteredemptions](#BKMK_mspp_publishingstatetransitionrule_adx_inviteredemptions)
- [mspp_publishingstatetransitionrule_adx_portalcomments](#BKMK_mspp_publishingstatetransitionrule_adx_portalcomments)
- [mspp_publishingstatetransitionrule_chats](#BKMK_mspp_publishingstatetransitionrule_chats)
- [mspp_publishingstatetransitionrule_Appointments](#BKMK_mspp_publishingstatetransitionrule_Appointments)
- [mspp_publishingstatetransitionrule_Emails](#BKMK_mspp_publishingstatetransitionrule_Emails)
- [mspp_publishingstatetransitionrule_Faxes](#BKMK_mspp_publishingstatetransitionrule_Faxes)
- [mspp_publishingstatetransitionrule_Letters](#BKMK_mspp_publishingstatetransitionrule_Letters)
- [mspp_publishingstatetransitionrule_PhoneCalls](#BKMK_mspp_publishingstatetransitionrule_PhoneCalls)
- [mspp_publishingstatetransitionrule_Tasks](#BKMK_mspp_publishingstatetransitionrule_Tasks)
- [mspp_publishingstatetransitionrule_RecurringAppointmentMasters](#BKMK_mspp_publishingstatetransitionrule_RecurringAppointmentMasters)
- [mspp_publishingstatetransitionrule_SocialActivities](#BKMK_mspp_publishingstatetransitionrule_SocialActivities)
- [mspp_publishingstatetransitionrule_connections1](#BKMK_mspp_publishingstatetransitionrule_connections1)
- [mspp_publishingstatetransitionrule_connections2](#BKMK_mspp_publishingstatetransitionrule_connections2)


### <a name="BKMK_mspp_publishingstatetransitionrule_ActivityPointers"></a> mspp_publishingstatetransitionrule_ActivityPointers

**Added by**: System Solution Solution

Same as the [mspp_publishingstatetransitionrule_ActivityPointers](activitypointer.md#BKMK_mspp_publishingstatetransitionrule_ActivityPointers) many-to-one relationship for the [activitypointer](activitypointer.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_ActivityPointers|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_adx_inviteredemptions"></a> mspp_publishingstatetransitionrule_adx_inviteredemptions

**Added by**: Active Solution Solution

Same as the [mspp_publishingstatetransitionrule_adx_inviteredemptions](adx_inviteredemption.md#BKMK_mspp_publishingstatetransitionrule_adx_inviteredemptions) many-to-one relationship for the [adx_inviteredemption](adx_inviteredemption.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|adx_inviteredemption|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_adx_inviteredemptions|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_adx_portalcomments"></a> mspp_publishingstatetransitionrule_adx_portalcomments

**Added by**: Active Solution Solution

Same as the [mspp_publishingstatetransitionrule_adx_portalcomments](adx_portalcomment.md#BKMK_mspp_publishingstatetransitionrule_adx_portalcomments) many-to-one relationship for the [adx_portalcomment](adx_portalcomment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|adx_portalcomment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_adx_portalcomments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_chats"></a> mspp_publishingstatetransitionrule_chats

**Added by**: Activities Patch Solution

Same as the [mspp_publishingstatetransitionrule_chats](chat.md#BKMK_mspp_publishingstatetransitionrule_chats) many-to-one relationship for the [chat](chat.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|chat|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_chats|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_Appointments"></a> mspp_publishingstatetransitionrule_Appointments

**Added by**: System Solution Solution

Same as the [mspp_publishingstatetransitionrule_Appointments](appointment.md#BKMK_mspp_publishingstatetransitionrule_Appointments) many-to-one relationship for the [appointment](appointment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_Appointments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_Emails"></a> mspp_publishingstatetransitionrule_Emails

**Added by**: System Solution Solution

Same as the [mspp_publishingstatetransitionrule_Emails](email.md#BKMK_mspp_publishingstatetransitionrule_Emails) many-to-one relationship for the [email](email.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_Emails|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_Faxes"></a> mspp_publishingstatetransitionrule_Faxes

**Added by**: System Solution Solution

Same as the [mspp_publishingstatetransitionrule_Faxes](fax.md#BKMK_mspp_publishingstatetransitionrule_Faxes) many-to-one relationship for the [fax](fax.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_Faxes|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_Letters"></a> mspp_publishingstatetransitionrule_Letters

**Added by**: System Solution Solution

Same as the [mspp_publishingstatetransitionrule_Letters](letter.md#BKMK_mspp_publishingstatetransitionrule_Letters) many-to-one relationship for the [letter](letter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_Letters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_PhoneCalls"></a> mspp_publishingstatetransitionrule_PhoneCalls

**Added by**: System Solution Solution

Same as the [mspp_publishingstatetransitionrule_PhoneCalls](phonecall.md#BKMK_mspp_publishingstatetransitionrule_PhoneCalls) many-to-one relationship for the [phonecall](phonecall.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_PhoneCalls|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_Tasks"></a> mspp_publishingstatetransitionrule_Tasks

**Added by**: System Solution Solution

Same as the [mspp_publishingstatetransitionrule_Tasks](task.md#BKMK_mspp_publishingstatetransitionrule_Tasks) many-to-one relationship for the [task](task.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_Tasks|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_RecurringAppointmentMasters"></a> mspp_publishingstatetransitionrule_RecurringAppointmentMasters

**Added by**: System Solution Solution

Same as the [mspp_publishingstatetransitionrule_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_mspp_publishingstatetransitionrule_RecurringAppointmentMasters) many-to-one relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_RecurringAppointmentMasters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_SocialActivities"></a> mspp_publishingstatetransitionrule_SocialActivities

**Added by**: System Solution Solution

Same as the [mspp_publishingstatetransitionrule_SocialActivities](socialactivity.md#BKMK_mspp_publishingstatetransitionrule_SocialActivities) many-to-one relationship for the [socialactivity](socialactivity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_SocialActivities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_connections1"></a> mspp_publishingstatetransitionrule_connections1

**Added by**: System Solution Solution

Same as the [mspp_publishingstatetransitionrule_connections1](connection.md#BKMK_mspp_publishingstatetransitionrule_connections1) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstatetransitionrule_connections2"></a> mspp_publishingstatetransitionrule_connections2

**Added by**: System Solution Solution

Same as the [mspp_publishingstatetransitionrule_connections2](connection.md#BKMK_mspp_publishingstatetransitionrule_connections2) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_publishingstatetransitionrule_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_frompublishingstate_statetransition](#BKMK_mspp_frompublishingstate_statetransition)
- [mspp_systemuser_mspp_publishingstatetransitionrule_createdby](#BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_createdby)
- [mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby](#BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby)
- [mspp_topublishingstate_statetransition](#BKMK_mspp_topublishingstate_statetransition)
- [mspp_website_publishingstatetransition](#BKMK_mspp_website_publishingstatetransition)


### <a name="BKMK_mspp_frompublishingstate_statetransition"></a> mspp_frompublishingstate_statetransition

See the [mspp_frompublishingstate_statetransition](mspp_publishingstate.md#BKMK_mspp_frompublishingstate_statetransition) one-to-many relationship for the [mspp_publishingstate](mspp_publishingstate.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_createdby"></a> mspp_systemuser_mspp_publishingstatetransitionrule_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_publishingstatetransitionrule_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby"></a> mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_publishingstatetransitionrule_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_topublishingstate_statetransition"></a> mspp_topublishingstate_statetransition

See the [mspp_topublishingstate_statetransition](mspp_publishingstate.md#BKMK_mspp_topublishingstate_statetransition) one-to-many relationship for the [mspp_publishingstate](mspp_publishingstate.md) table/entity.

### <a name="BKMK_mspp_website_publishingstatetransition"></a> mspp_website_publishingstatetransition

See the [mspp_website_publishingstatetransition](mspp_website.md#BKMK_mspp_website_publishingstatetransition) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the mspp_publishingstatetransitionrule table is the first table in the relationship. Listed by **SchemaName**.


### <a name="BKMK_mspp_publishingstatetransitionrule_webrole"></a> mspp_publishingstatetransitionrule_webrole

IntersectEntityName: mspp_publishingstatetransitionrule_webrole<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|mspp_publishingstatetransitionruleid|
|IsCustomizable|False|
|LogicalName|mspp_publishingstatetransitionrule|
|NavigationPropertyName|mspp_publishingstatetransitionrule_webrole|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|mspp_webrole|
|IntersectAttribute|mspp_webroleid|
|NavigationPropertyName|mspp_publishingstatetransitionrule_webrole|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|


### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_publishingstatetransitionrule?text=mspp_publishingstatetransitionrule EntityType" />