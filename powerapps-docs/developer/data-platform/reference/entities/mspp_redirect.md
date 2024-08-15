---
title: "Redirect (mspp_redirect)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Redirect (mspp_redirect)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Redirect (mspp_redirect)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_redirects<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_redirects(*mspp_redirectid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_redirects(*mspp_redirectid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_redirects<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_redirects(*mspp_redirectid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_redirects|
|DisplayCollectionName|Redirects|
|DisplayName|Redirect|
|EntitySetName|mspp_redirects|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_redirects|
|LogicalName|mspp_redirect|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_redirectid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_redirect|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_inboundurl](#BKMK_mspp_inboundurl)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_redirectId](#BKMK_mspp_redirectId)
- [mspp_redirecturl](#BKMK_mspp_redirecturl)
- [mspp_sitemarkerid](#BKMK_mspp_sitemarkerid)
- [mspp_statuscode](#BKMK_mspp_statuscode)
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


### <a name="BKMK_mspp_inboundurl"></a> mspp_inboundurl

|Property|Value|
|--------|-----|
|Description|The path to redirect visitors from|
|DisplayName|Inbound URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_inboundurl|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
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


### <a name="BKMK_mspp_redirectId"></a> mspp_redirectId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Redirect|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_redirectid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_redirecturl"></a> mspp_redirecturl

|Property|Value|
|--------|-----|
|Description|The path to redirect visitors to|
|DisplayName|Redirect URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_redirecturl|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_sitemarkerid"></a> mspp_sitemarkerid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Site Marker associated with Redirect.|
|DisplayName|Site Marker|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_sitemarkerid|
|RequiredLevel|None|
|Targets|mspp_sitemarker|
|Type|Lookup|


### <a name="BKMK_mspp_statuscode"></a> mspp_statuscode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Status Code|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_statuscode|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### mspp_statuscode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|301|301 (Permanent Redirect)||
|302|302 (Temporary Redirect)||



### <a name="BKMK_mspp_webpageid"></a> mspp_webpageid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Page associated with Redirect.|
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
|Description|Unique identifier for Website associated with Redirect.|
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
|Description|Status of the Redirect|
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
|Description|Reason for the status of the Redirect|
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
- [mspp_sitemarkeridName](#BKMK_mspp_sitemarkeridName)
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


### <a name="BKMK_mspp_sitemarkeridName"></a> mspp_sitemarkeridName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_sitemarkeridname|
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

- [mspp_redirect_ActivityPointers](#BKMK_mspp_redirect_ActivityPointers)
- [mspp_redirect_adx_inviteredemptions](#BKMK_mspp_redirect_adx_inviteredemptions)
- [mspp_redirect_adx_portalcomments](#BKMK_mspp_redirect_adx_portalcomments)
- [mspp_redirect_chats](#BKMK_mspp_redirect_chats)
- [mspp_redirect_Appointments](#BKMK_mspp_redirect_Appointments)
- [mspp_redirect_Emails](#BKMK_mspp_redirect_Emails)
- [mspp_redirect_Faxes](#BKMK_mspp_redirect_Faxes)
- [mspp_redirect_Letters](#BKMK_mspp_redirect_Letters)
- [mspp_redirect_PhoneCalls](#BKMK_mspp_redirect_PhoneCalls)
- [mspp_redirect_Tasks](#BKMK_mspp_redirect_Tasks)
- [mspp_redirect_RecurringAppointmentMasters](#BKMK_mspp_redirect_RecurringAppointmentMasters)
- [mspp_redirect_SocialActivities](#BKMK_mspp_redirect_SocialActivities)


### <a name="BKMK_mspp_redirect_ActivityPointers"></a> mspp_redirect_ActivityPointers

**Added by**: System Solution Solution

Same as the [mspp_redirect_ActivityPointers](activitypointer.md#BKMK_mspp_redirect_ActivityPointers) many-to-one relationship for the [activitypointer](activitypointer.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_ActivityPointers|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_redirect_adx_inviteredemptions"></a> mspp_redirect_adx_inviteredemptions

**Added by**: Active Solution Solution

Same as the [mspp_redirect_adx_inviteredemptions](adx_inviteredemption.md#BKMK_mspp_redirect_adx_inviteredemptions) many-to-one relationship for the [adx_inviteredemption](adx_inviteredemption.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|adx_inviteredemption|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_adx_inviteredemptions|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_redirect_adx_portalcomments"></a> mspp_redirect_adx_portalcomments

**Added by**: Active Solution Solution

Same as the [mspp_redirect_adx_portalcomments](adx_portalcomment.md#BKMK_mspp_redirect_adx_portalcomments) many-to-one relationship for the [adx_portalcomment](adx_portalcomment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|adx_portalcomment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_adx_portalcomments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_redirect_chats"></a> mspp_redirect_chats

**Added by**: Activities Patch Solution

Same as the [mspp_redirect_chats](chat.md#BKMK_mspp_redirect_chats) many-to-one relationship for the [chat](chat.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|chat|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_chats|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_redirect_Appointments"></a> mspp_redirect_Appointments

**Added by**: System Solution Solution

Same as the [mspp_redirect_Appointments](appointment.md#BKMK_mspp_redirect_Appointments) many-to-one relationship for the [appointment](appointment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_Appointments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_redirect_Emails"></a> mspp_redirect_Emails

**Added by**: System Solution Solution

Same as the [mspp_redirect_Emails](email.md#BKMK_mspp_redirect_Emails) many-to-one relationship for the [email](email.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_Emails|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_redirect_Faxes"></a> mspp_redirect_Faxes

**Added by**: System Solution Solution

Same as the [mspp_redirect_Faxes](fax.md#BKMK_mspp_redirect_Faxes) many-to-one relationship for the [fax](fax.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_Faxes|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_redirect_Letters"></a> mspp_redirect_Letters

**Added by**: System Solution Solution

Same as the [mspp_redirect_Letters](letter.md#BKMK_mspp_redirect_Letters) many-to-one relationship for the [letter](letter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_Letters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_redirect_PhoneCalls"></a> mspp_redirect_PhoneCalls

**Added by**: System Solution Solution

Same as the [mspp_redirect_PhoneCalls](phonecall.md#BKMK_mspp_redirect_PhoneCalls) many-to-one relationship for the [phonecall](phonecall.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_PhoneCalls|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_redirect_Tasks"></a> mspp_redirect_Tasks

**Added by**: System Solution Solution

Same as the [mspp_redirect_Tasks](task.md#BKMK_mspp_redirect_Tasks) many-to-one relationship for the [task](task.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_Tasks|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_redirect_RecurringAppointmentMasters"></a> mspp_redirect_RecurringAppointmentMasters

**Added by**: System Solution Solution

Same as the [mspp_redirect_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_mspp_redirect_RecurringAppointmentMasters) many-to-one relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_RecurringAppointmentMasters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_redirect_SocialActivities"></a> mspp_redirect_SocialActivities

**Added by**: System Solution Solution

Same as the [mspp_redirect_SocialActivities](socialactivity.md#BKMK_mspp_redirect_SocialActivities) many-to-one relationship for the [socialactivity](socialactivity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_redirect_SocialActivities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_sitemarker_redirect](#BKMK_mspp_sitemarker_redirect)
- [mspp_systemuser_mspp_redirect_createdby](#BKMK_mspp_systemuser_mspp_redirect_createdby)
- [mspp_systemuser_mspp_redirect_modifiedby](#BKMK_mspp_systemuser_mspp_redirect_modifiedby)
- [mspp_webpage_redirect](#BKMK_mspp_webpage_redirect)
- [mspp_website_redirect](#BKMK_mspp_website_redirect)


### <a name="BKMK_mspp_sitemarker_redirect"></a> mspp_sitemarker_redirect

See the [mspp_sitemarker_redirect](mspp_sitemarker.md#BKMK_mspp_sitemarker_redirect) one-to-many relationship for the [mspp_sitemarker](mspp_sitemarker.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_redirect_createdby"></a> mspp_systemuser_mspp_redirect_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_redirect_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_redirect_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_redirect_modifiedby"></a> mspp_systemuser_mspp_redirect_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_redirect_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_redirect_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_webpage_redirect"></a> mspp_webpage_redirect

See the [mspp_webpage_redirect](mspp_webpage.md#BKMK_mspp_webpage_redirect) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_website_redirect"></a> mspp_website_redirect

See the [mspp_website_redirect](mspp_website.md#BKMK_mspp_website_redirect) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_redirect?text=mspp_redirect EntityType" />