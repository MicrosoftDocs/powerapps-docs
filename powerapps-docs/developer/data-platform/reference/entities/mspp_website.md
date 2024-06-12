---
title: "Website (mspp_website)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Website (mspp_website)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Website (mspp_website)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Web Portal

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_websites<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_websites(*mspp_websiteid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_websites(*mspp_websiteid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_websites<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_websites(*mspp_websiteid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_websites|
|DisplayCollectionName|Websites|
|DisplayName|Website|
|EntitySetName|mspp_websites|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_websites|
|LogicalName|mspp_website|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_websiteid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_website|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_defaultlanguage](#BKMK_mspp_defaultlanguage)
- [mspp_footerwebtemplateid](#BKMK_mspp_footerwebtemplateid)
- [mspp_headerwebtemplateid](#BKMK_mspp_headerwebtemplateid)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_parentwebsiteid](#BKMK_mspp_parentwebsiteid)
- [mspp_partialurl](#BKMK_mspp_partialurl)
- [mspp_primarydomainname](#BKMK_mspp_primarydomainname)
- [mspp_website_language](#BKMK_mspp_website_language)
- [mspp_website_version](#BKMK_mspp_website_version)
- [mspp_websiteId](#BKMK_mspp_websiteId)
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


### <a name="BKMK_mspp_defaultlanguage"></a> mspp_defaultlanguage

|Property|Value|
|--------|-----|
|Description|Lookup to Website Language - the current default language of the website|
|DisplayName|Default Language|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_defaultlanguage|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_websitelanguage|
|Type|Lookup|


### <a name="BKMK_mspp_footerwebtemplateid"></a> mspp_footerwebtemplateid

|Property|Value|
|--------|-----|
|Description|Web Template to use as Website footer content.|
|DisplayName|Footer Template|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_footerwebtemplateid|
|RequiredLevel|None|
|Targets|mspp_webtemplate|
|Type|Lookup|


### <a name="BKMK_mspp_headerwebtemplateid"></a> mspp_headerwebtemplateid

|Property|Value|
|--------|-----|
|Description|Web Template to use as Website header content.|
|DisplayName|Header Template|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_headerwebtemplateid|
|RequiredLevel|None|
|Targets|mspp_webtemplate|
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


### <a name="BKMK_mspp_parentwebsiteid"></a> mspp_parentwebsiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Website.|
|DisplayName|Parent Website|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_parentwebsiteid|
|RequiredLevel|None|
|Targets|mspp_website|
|Type|Lookup|


### <a name="BKMK_mspp_partialurl"></a> mspp_partialurl

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Partial URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_partialurl|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_primarydomainname"></a> mspp_primarydomainname

|Property|Value|
|--------|-----|
|Description|Tracks the primary domain name of the Portal|
|DisplayName|Primary Domain Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_primarydomainname|
|MaxLength|253|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_website_language"></a> mspp_website_language

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Language|
|Format|Language|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_website_language|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_mspp_website_version"></a> mspp_website_version

|Property|Value|
|--------|-----|
|Description|Version of the website record|
|DisplayName|Website Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_website_version|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_websiteId"></a> mspp_websiteId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Website|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_websiteid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Website|
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
|Description|Reason for the status of the Website|
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
- [mspp_defaultlanguageName](#BKMK_mspp_defaultlanguageName)
- [mspp_footerwebtemplateidName](#BKMK_mspp_footerwebtemplateidName)
- [mspp_headerwebtemplateidName](#BKMK_mspp_headerwebtemplateidName)
- [mspp_modifiedbyName](#BKMK_mspp_modifiedbyName)
- [mspp_modifiedbyYomiName](#BKMK_mspp_modifiedbyYomiName)
- [mspp_parentwebsiteidName](#BKMK_mspp_parentwebsiteidName)


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


### <a name="BKMK_mspp_defaultlanguageName"></a> mspp_defaultlanguageName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_defaultlanguagename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_footerwebtemplateidName"></a> mspp_footerwebtemplateidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_footerwebtemplateidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_headerwebtemplateidName"></a> mspp_headerwebtemplateidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_headerwebtemplateidname|
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


### <a name="BKMK_mspp_parentwebsiteidName"></a> mspp_parentwebsiteidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_parentwebsiteidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [mspp_website_ActivityPointers](#BKMK_mspp_website_ActivityPointers)
- [mspp_website_adx_inviteredemptions](#BKMK_mspp_website_adx_inviteredemptions)
- [mspp_website_adx_portalcomments](#BKMK_mspp_website_adx_portalcomments)
- [mspp_website_chats](#BKMK_mspp_website_chats)
- [mspp_website_SharePointDocumentLocations](#BKMK_mspp_website_SharePointDocumentLocations)
- [mspp_website_Appointments](#BKMK_mspp_website_Appointments)
- [mspp_website_Emails](#BKMK_mspp_website_Emails)
- [mspp_website_Faxes](#BKMK_mspp_website_Faxes)
- [mspp_website_Letters](#BKMK_mspp_website_Letters)
- [mspp_website_PhoneCalls](#BKMK_mspp_website_PhoneCalls)
- [mspp_website_Tasks](#BKMK_mspp_website_Tasks)
- [mspp_website_RecurringAppointmentMasters](#BKMK_mspp_website_RecurringAppointmentMasters)
- [mspp_website_SocialActivities](#BKMK_mspp_website_SocialActivities)
- [mspp_website_connections1](#BKMK_mspp_website_connections1)
- [mspp_website_connections2](#BKMK_mspp_website_connections2)
- [mspp_columnpermissionprofile_website](#BKMK_mspp_columnpermissionprofile_website)
- [mspp_mspp_website_mspp_websitelanguage](#BKMK_mspp_mspp_website_mspp_websitelanguage)
- [mspp_website_adplacement](#BKMK_mspp_website_adplacement)
- [mspp_website_contentsnippet](#BKMK_mspp_website_contentsnippet)
- [mspp_website_entityform](#BKMK_mspp_website_entityform)
- [mspp_website_entitylist](#BKMK_mspp_website_entitylist)
- [mspp_website_mspp_entitypermission](#BKMK_mspp_website_mspp_entitypermission)
- [mspp_website_mspp_webtemplate](#BKMK_mspp_website_mspp_webtemplate)
- [mspp_website_pagetemplate](#BKMK_mspp_website_pagetemplate)
- [mspp_website_parentwebsite](#BKMK_mspp_website_parentwebsite)
- [mspp_website_pollplacement](#BKMK_mspp_website_pollplacement)
- [mspp_website_publishingstate](#BKMK_mspp_website_publishingstate)
- [mspp_website_publishingstatetransition](#BKMK_mspp_website_publishingstatetransition)
- [mspp_website_redirect](#BKMK_mspp_website_redirect)
- [mspp_website_shortcut](#BKMK_mspp_website_shortcut)
- [mspp_website_sitemarker](#BKMK_mspp_website_sitemarker)
- [mspp_website_sitesetting](#BKMK_mspp_website_sitesetting)
- [mspp_website_webfile](#BKMK_mspp_website_webfile)
- [mspp_website_webform](#BKMK_mspp_website_webform)
- [mspp_website_weblinkset](#BKMK_mspp_website_weblinkset)
- [mspp_website_webpage](#BKMK_mspp_website_webpage)
- [mspp_website_webpageaccesscontrolrule](#BKMK_mspp_website_webpageaccesscontrolrule)
- [mspp_website_webrole](#BKMK_mspp_website_webrole)
- [mspp_website_websiteaccess](#BKMK_mspp_website_websiteaccess)


### <a name="BKMK_mspp_website_ActivityPointers"></a> mspp_website_ActivityPointers

**Added by**: System Solution Solution

Same as the [mspp_website_ActivityPointers](activitypointer.md#BKMK_mspp_website_ActivityPointers) many-to-one relationship for the [activitypointer](activitypointer.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_ActivityPointers|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_adx_inviteredemptions"></a> mspp_website_adx_inviteredemptions

**Added by**: Active Solution Solution

Same as the [mspp_website_adx_inviteredemptions](adx_inviteredemption.md#BKMK_mspp_website_adx_inviteredemptions) many-to-one relationship for the [adx_inviteredemption](adx_inviteredemption.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|adx_inviteredemption|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_adx_inviteredemptions|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_adx_portalcomments"></a> mspp_website_adx_portalcomments

**Added by**: Active Solution Solution

Same as the [mspp_website_adx_portalcomments](adx_portalcomment.md#BKMK_mspp_website_adx_portalcomments) many-to-one relationship for the [adx_portalcomment](adx_portalcomment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|adx_portalcomment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_adx_portalcomments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_chats"></a> mspp_website_chats

**Added by**: Activities Patch Solution

Same as the [mspp_website_chats](chat.md#BKMK_mspp_website_chats) many-to-one relationship for the [chat](chat.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|chat|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_chats|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_SharePointDocumentLocations"></a> mspp_website_SharePointDocumentLocations

**Added by**: System Solution Solution

Same as the [mspp_website_SharePointDocumentLocations](sharepointdocumentlocation.md#BKMK_mspp_website_SharePointDocumentLocations) many-to-one relationship for the [sharepointdocumentlocation](sharepointdocumentlocation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_SharePointDocumentLocations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_Appointments"></a> mspp_website_Appointments

**Added by**: System Solution Solution

Same as the [mspp_website_Appointments](appointment.md#BKMK_mspp_website_Appointments) many-to-one relationship for the [appointment](appointment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_Appointments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_Emails"></a> mspp_website_Emails

**Added by**: System Solution Solution

Same as the [mspp_website_Emails](email.md#BKMK_mspp_website_Emails) many-to-one relationship for the [email](email.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_Emails|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_Faxes"></a> mspp_website_Faxes

**Added by**: System Solution Solution

Same as the [mspp_website_Faxes](fax.md#BKMK_mspp_website_Faxes) many-to-one relationship for the [fax](fax.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_Faxes|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_Letters"></a> mspp_website_Letters

**Added by**: System Solution Solution

Same as the [mspp_website_Letters](letter.md#BKMK_mspp_website_Letters) many-to-one relationship for the [letter](letter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_Letters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_PhoneCalls"></a> mspp_website_PhoneCalls

**Added by**: System Solution Solution

Same as the [mspp_website_PhoneCalls](phonecall.md#BKMK_mspp_website_PhoneCalls) many-to-one relationship for the [phonecall](phonecall.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_PhoneCalls|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_Tasks"></a> mspp_website_Tasks

**Added by**: System Solution Solution

Same as the [mspp_website_Tasks](task.md#BKMK_mspp_website_Tasks) many-to-one relationship for the [task](task.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_Tasks|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_RecurringAppointmentMasters"></a> mspp_website_RecurringAppointmentMasters

**Added by**: System Solution Solution

Same as the [mspp_website_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_mspp_website_RecurringAppointmentMasters) many-to-one relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_RecurringAppointmentMasters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_SocialActivities"></a> mspp_website_SocialActivities

**Added by**: System Solution Solution

Same as the [mspp_website_SocialActivities](socialactivity.md#BKMK_mspp_website_SocialActivities) many-to-one relationship for the [socialactivity](socialactivity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_SocialActivities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_connections1"></a> mspp_website_connections1

**Added by**: System Solution Solution

Same as the [mspp_website_connections1](connection.md#BKMK_mspp_website_connections1) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_connections2"></a> mspp_website_connections2

**Added by**: System Solution Solution

Same as the [mspp_website_connections2](connection.md#BKMK_mspp_website_connections2) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mspp_website_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_columnpermissionprofile_website"></a> mspp_columnpermissionprofile_website

Same as the [mspp_columnpermissionprofile_website](mspp_columnpermissionprofile.md#BKMK_mspp_columnpermissionprofile_website) many-to-one relationship for the [mspp_columnpermissionprofile](mspp_columnpermissionprofile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_columnpermissionprofile|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_columnpermissionprofile_website|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_mspp_website_mspp_websitelanguage"></a> mspp_mspp_website_mspp_websitelanguage

Same as the [mspp_mspp_website_mspp_websitelanguage](mspp_websitelanguage.md#BKMK_mspp_mspp_website_mspp_websitelanguage) many-to-one relationship for the [mspp_websitelanguage](mspp_websitelanguage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_websitelanguage|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_mspp_website_mspp_websitelanguage|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_adplacement"></a> mspp_website_adplacement

Same as the [mspp_website_adplacement](mspp_adplacement.md#BKMK_mspp_website_adplacement) many-to-one relationship for the [mspp_adplacement](mspp_adplacement.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_adplacement|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_adplacement|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_contentsnippet"></a> mspp_website_contentsnippet

Same as the [mspp_website_contentsnippet](mspp_contentsnippet.md#BKMK_mspp_website_contentsnippet) many-to-one relationship for the [mspp_contentsnippet](mspp_contentsnippet.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_contentsnippet|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_contentsnippet|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100700|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_entityform"></a> mspp_website_entityform

Same as the [mspp_website_entityform](mspp_entityform.md#BKMK_mspp_website_entityform) many-to-one relationship for the [mspp_entityform](mspp_entityform.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_entityform|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_entityform|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_entitylist"></a> mspp_website_entitylist

Same as the [mspp_website_entitylist](mspp_entitylist.md#BKMK_mspp_website_entitylist) many-to-one relationship for the [mspp_entitylist](mspp_entitylist.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_entitylist|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_entitylist|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_mspp_entitypermission"></a> mspp_website_mspp_entitypermission

Same as the [mspp_website_mspp_entitypermission](mspp_entitypermission.md#BKMK_mspp_website_mspp_entitypermission) many-to-one relationship for the [mspp_entitypermission](mspp_entitypermission.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_entitypermission|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_mspp_entitypermission|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_mspp_webtemplate"></a> mspp_website_mspp_webtemplate

Same as the [mspp_website_mspp_webtemplate](mspp_webtemplate.md#BKMK_mspp_website_mspp_webtemplate) many-to-one relationship for the [mspp_webtemplate](mspp_webtemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webtemplate|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_mspp_webtemplate|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_pagetemplate"></a> mspp_website_pagetemplate

Same as the [mspp_website_pagetemplate](mspp_pagetemplate.md#BKMK_mspp_website_pagetemplate) many-to-one relationship for the [mspp_pagetemplate](mspp_pagetemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_pagetemplate|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_pagetemplate|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 102100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_parentwebsite"></a> mspp_website_parentwebsite

Same as the [mspp_website_parentwebsite](mspp_website.md#BKMK_mspp_website_parentwebsite) many-to-one relationship for the [mspp_website](mspp_website.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_website|
|ReferencingAttribute|mspp_parentwebsiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_parentwebsite|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Child Websites<br />Order: 100500|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_pollplacement"></a> mspp_website_pollplacement

Same as the [mspp_website_pollplacement](mspp_pollplacement.md#BKMK_mspp_website_pollplacement) many-to-one relationship for the [mspp_pollplacement](mspp_pollplacement.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_pollplacement|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_pollplacement|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 102200|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_publishingstate"></a> mspp_website_publishingstate

Same as the [mspp_website_publishingstate](mspp_publishingstate.md#BKMK_mspp_website_publishingstate) many-to-one relationship for the [mspp_publishingstate](mspp_publishingstate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_publishingstate|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_publishingstate|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 102500|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_publishingstatetransition"></a> mspp_website_publishingstatetransition

Same as the [mspp_website_publishingstatetransition](mspp_publishingstatetransitionrule.md#BKMK_mspp_website_publishingstatetransition) many-to-one relationship for the [mspp_publishingstatetransitionrule](mspp_publishingstatetransitionrule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_publishingstatetransitionrule|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_publishingstatetransition|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 102400|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_redirect"></a> mspp_website_redirect

Same as the [mspp_website_redirect](mspp_redirect.md#BKMK_mspp_website_redirect) many-to-one relationship for the [mspp_redirect](mspp_redirect.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_redirect|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_redirect|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 102600|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_shortcut"></a> mspp_website_shortcut

Same as the [mspp_website_shortcut](mspp_shortcut.md#BKMK_mspp_website_shortcut) many-to-one relationship for the [mspp_shortcut](mspp_shortcut.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_shortcut|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_shortcut|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 102700|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_sitemarker"></a> mspp_website_sitemarker

Same as the [mspp_website_sitemarker](mspp_sitemarker.md#BKMK_mspp_website_sitemarker) many-to-one relationship for the [mspp_sitemarker](mspp_sitemarker.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_sitemarker|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_sitemarker|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 102800|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_sitesetting"></a> mspp_website_sitesetting

Same as the [mspp_website_sitesetting](mspp_sitesetting.md#BKMK_mspp_website_sitesetting) many-to-one relationship for the [mspp_sitesetting](mspp_sitesetting.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_sitesetting|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_sitesetting|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 102900|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_webfile"></a> mspp_website_webfile

Same as the [mspp_website_webfile](mspp_webfile.md#BKMK_mspp_website_webfile) many-to-one relationship for the [mspp_webfile](mspp_webfile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webfile|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_webfile|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 103200|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_webform"></a> mspp_website_webform

Same as the [mspp_website_webform](mspp_webform.md#BKMK_mspp_website_webform) many-to-one relationship for the [mspp_webform](mspp_webform.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webform|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_webform|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_weblinkset"></a> mspp_website_weblinkset

Same as the [mspp_website_weblinkset](mspp_weblinkset.md#BKMK_mspp_website_weblinkset) many-to-one relationship for the [mspp_weblinkset](mspp_weblinkset.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_weblinkset|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_weblinkset|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 103300|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_webpage"></a> mspp_website_webpage

Same as the [mspp_website_webpage](mspp_webpage.md#BKMK_mspp_website_webpage) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_webpage|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 103500|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_webpageaccesscontrolrule"></a> mspp_website_webpageaccesscontrolrule

Same as the [mspp_website_webpageaccesscontrolrule](mspp_webpageaccesscontrolrule.md#BKMK_mspp_website_webpageaccesscontrolrule) many-to-one relationship for the [mspp_webpageaccesscontrolrule](mspp_webpageaccesscontrolrule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpageaccesscontrolrule|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_webpageaccesscontrolrule|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 103400|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_webrole"></a> mspp_website_webrole

Same as the [mspp_website_webrole](mspp_webrole.md#BKMK_mspp_website_webrole) many-to-one relationship for the [mspp_webrole](mspp_webrole.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webrole|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_webrole|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 103600|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_website_websiteaccess"></a> mspp_website_websiteaccess

Same as the [mspp_website_websiteaccess](mspp_websiteaccess.md#BKMK_mspp_website_websiteaccess) many-to-one relationship for the [mspp_websiteaccess](mspp_websiteaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_websiteaccess|
|ReferencingAttribute|mspp_websiteid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_website_websiteaccess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 103700|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_mspp_websitelanguage_mspp_website_DefaultLanguage](#BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage)
- [mspp_systemuser_mspp_website_createdby](#BKMK_mspp_systemuser_mspp_website_createdby)
- [mspp_systemuser_mspp_website_modifiedby](#BKMK_mspp_systemuser_mspp_website_modifiedby)
- [mspp_website_parentwebsite](#BKMK_mspp_website_parentwebsite)
- [mspp_webtemplate_website_footer](#BKMK_mspp_webtemplate_website_footer)
- [mspp_webtemplate_website_header](#BKMK_mspp_webtemplate_website_header)


### <a name="BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage"></a> mspp_mspp_websitelanguage_mspp_website_DefaultLanguage

See the [mspp_mspp_websitelanguage_mspp_website_DefaultLanguage](mspp_websitelanguage.md#BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage) one-to-many relationship for the [mspp_websitelanguage](mspp_websitelanguage.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_website_createdby"></a> mspp_systemuser_mspp_website_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_website_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_website_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_website_modifiedby"></a> mspp_systemuser_mspp_website_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_website_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_website_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_website_parentwebsite"></a> mspp_website_parentwebsite

See the [mspp_website_parentwebsite](mspp_website.md#BKMK_mspp_website_parentwebsite) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### <a name="BKMK_mspp_webtemplate_website_footer"></a> mspp_webtemplate_website_footer

See the [mspp_webtemplate_website_footer](mspp_webtemplate.md#BKMK_mspp_webtemplate_website_footer) one-to-many relationship for the [mspp_webtemplate](mspp_webtemplate.md) table/entity.

### <a name="BKMK_mspp_webtemplate_website_header"></a> mspp_webtemplate_website_header

See the [mspp_webtemplate_website_header](mspp_webtemplate.md#BKMK_mspp_webtemplate_website_header) one-to-many relationship for the [mspp_webtemplate](mspp_webtemplate.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_website?text=mspp_website EntityType" />