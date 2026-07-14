---
title: "Website (mspp_website) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Website (mspp_website) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Website (mspp_website) table/entity reference (Microsoft Dataverse)

Web Portal

## Messages

The following table lists the messages for the Website (mspp_website) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_websites<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_websites(*mspp_websiteid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_websites(*mspp_websiteid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_websites<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_websites(*mspp_websiteid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_websites(*mspp_websiteid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Website (mspp_website) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Website (mspp_website) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Website** |
| **DisplayCollectionName** | **Websites** |
| **SchemaName** | `mspp_website` |
| **CollectionSchemaName** | `mspp_websites` |
| **EntitySetName** | `mspp_websites`|
| **LogicalName** | `mspp_website` |
| **LogicalCollectionName** | `mspp_websites` |
| **PrimaryIdAttribute** | `mspp_websiteid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

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
|---|---|
|Description|**Shows who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_mspp_createdon"></a> mspp_createdon

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_mspp_defaultlanguage"></a> mspp_defaultlanguage

|Property|Value|
|---|---|
|Description|**Lookup to Website Language - the current default language of the website**|
|DisplayName|**Default Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_defaultlanguage`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_websitelanguage|

### <a name="BKMK_mspp_footerwebtemplateid"></a> mspp_footerwebtemplateid

|Property|Value|
|---|---|
|Description|**Web Template to use as Website footer content.**|
|DisplayName|**Footer Template**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_footerwebtemplateid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webtemplate|

### <a name="BKMK_mspp_headerwebtemplateid"></a> mspp_headerwebtemplateid

|Property|Value|
|---|---|
|Description|**Web Template to use as Website header content.**|
|DisplayName|**Header Template**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_headerwebtemplateid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webtemplate|

### <a name="BKMK_mspp_modifiedby"></a> mspp_modifiedby

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_mspp_modifiedon"></a> mspp_modifiedon

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_mspp_name"></a> mspp_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_parentwebsiteid"></a> mspp_parentwebsiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website associated with Website.**|
|DisplayName|**Parent Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_parentwebsiteid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_website|

### <a name="BKMK_mspp_partialurl"></a> mspp_partialurl

|Property|Value|
|---|---|
|Description||
|DisplayName|**Partial URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_partialurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_primarydomainname"></a> mspp_primarydomainname

|Property|Value|
|---|---|
|Description|**Tracks the primary domain name of the Portal**|
|DisplayName|**Primary Domain Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_primarydomainname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|253|

### <a name="BKMK_mspp_website_language"></a> mspp_website_language

|Property|Value|
|---|---|
|Description||
|DisplayName|**Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_website_language`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_website_version"></a> mspp_website_version

|Property|Value|
|---|---|
|Description|**Version of the website record**|
|DisplayName|**Website Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_website_version`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_mspp_websiteId"></a> mspp_websiteId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Website**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_websiteid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Website**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_website_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Website**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_website_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_mspp_websitelanguage_mspp_website_DefaultLanguage](#BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage)
- [mspp_systemuser_mspp_website_createdby](#BKMK_mspp_systemuser_mspp_website_createdby)
- [mspp_systemuser_mspp_website_modifiedby](#BKMK_mspp_systemuser_mspp_website_modifiedby)
- [mspp_website_parentwebsite](#BKMK_mspp_website_parentwebsite-many-to-one)
- [mspp_webtemplate_website_footer](#BKMK_mspp_webtemplate_website_footer)
- [mspp_webtemplate_website_header](#BKMK_mspp_webtemplate_website_header)

### <a name="BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage"></a> mspp_mspp_websitelanguage_mspp_website_DefaultLanguage

One-To-Many Relationship: [mspp_websitelanguage mspp_mspp_websitelanguage_mspp_website_DefaultLanguage](mspp_websitelanguage.md#BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_websitelanguage`|
|ReferencedAttribute|`mspp_websitelanguageid`|
|ReferencingAttribute|`mspp_defaultlanguage`|
|ReferencingEntityNavigationPropertyName|`mspp_DefaultLanguage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_website_createdby"></a> mspp_systemuser_mspp_website_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_website_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_website_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_website_modifiedby"></a> mspp_systemuser_mspp_website_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_website_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_website_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_parentwebsite-many-to-one"></a> mspp_website_parentwebsite

One-To-Many Relationship: [mspp_website mspp_website_parentwebsite](#BKMK_mspp_website_parentwebsite-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_parentwebsiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_parentwebsiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webtemplate_website_footer"></a> mspp_webtemplate_website_footer

One-To-Many Relationship: [mspp_webtemplate mspp_webtemplate_website_footer](mspp_webtemplate.md#BKMK_mspp_webtemplate_website_footer)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webtemplate`|
|ReferencedAttribute|`mspp_webtemplateid`|
|ReferencingAttribute|`mspp_footerwebtemplateid`|
|ReferencingEntityNavigationPropertyName|`mspp_footerwebtemplateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webtemplate_website_header"></a> mspp_webtemplate_website_header

One-To-Many Relationship: [mspp_webtemplate mspp_webtemplate_website_header](mspp_webtemplate.md#BKMK_mspp_webtemplate_website_header)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webtemplate`|
|ReferencedAttribute|`mspp_webtemplateid`|
|ReferencingAttribute|`mspp_headerwebtemplateid`|
|ReferencingEntityNavigationPropertyName|`mspp_headerwebtemplateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [mspp_columnpermissionprofile_website](#BKMK_mspp_columnpermissionprofile_website)
- [mspp_mspp_website_mspp_websitelanguage](#BKMK_mspp_mspp_website_mspp_websitelanguage)
- [mspp_website_ActivityPointers](#BKMK_mspp_website_ActivityPointers)
- [mspp_website_adplacement](#BKMK_mspp_website_adplacement)
- [mspp_website_adx_inviteredemptions](#BKMK_mspp_website_adx_inviteredemptions)
- [mspp_website_adx_portalcomments](#BKMK_mspp_website_adx_portalcomments)
- [mspp_website_Appointments](#BKMK_mspp_website_Appointments)
- [mspp_website_chats](#BKMK_mspp_website_chats)
- [mspp_website_connections1](#BKMK_mspp_website_connections1)
- [mspp_website_connections2](#BKMK_mspp_website_connections2)
- [mspp_website_contentsnippet](#BKMK_mspp_website_contentsnippet)
- [mspp_website_Emails](#BKMK_mspp_website_Emails)
- [mspp_website_entityform](#BKMK_mspp_website_entityform)
- [mspp_website_entitylist](#BKMK_mspp_website_entitylist)
- [mspp_website_Faxes](#BKMK_mspp_website_Faxes)
- [mspp_website_Letters](#BKMK_mspp_website_Letters)
- [mspp_website_mspp_entitypermission](#BKMK_mspp_website_mspp_entitypermission)
- [mspp_website_mspp_webtemplate](#BKMK_mspp_website_mspp_webtemplate)
- [mspp_website_pagetemplate](#BKMK_mspp_website_pagetemplate)
- [mspp_website_parentwebsite](#BKMK_mspp_website_parentwebsite-one-to-many)
- [mspp_website_PhoneCalls](#BKMK_mspp_website_PhoneCalls)
- [mspp_website_pollplacement](#BKMK_mspp_website_pollplacement)
- [mspp_website_publishingstate](#BKMK_mspp_website_publishingstate)
- [mspp_website_publishingstatetransition](#BKMK_mspp_website_publishingstatetransition)
- [mspp_website_RecurringAppointmentMasters](#BKMK_mspp_website_RecurringAppointmentMasters)
- [mspp_website_redirect](#BKMK_mspp_website_redirect)
- [mspp_website_SharePointDocumentLocations](#BKMK_mspp_website_SharePointDocumentLocations)
- [mspp_website_shortcut](#BKMK_mspp_website_shortcut)
- [mspp_website_sitemarker](#BKMK_mspp_website_sitemarker)
- [mspp_website_sitesetting](#BKMK_mspp_website_sitesetting)
- [mspp_website_SocialActivities](#BKMK_mspp_website_SocialActivities)
- [mspp_website_Tasks](#BKMK_mspp_website_Tasks)
- [mspp_website_webfile](#BKMK_mspp_website_webfile)
- [mspp_website_webform](#BKMK_mspp_website_webform)
- [mspp_website_weblinkset](#BKMK_mspp_website_weblinkset)
- [mspp_website_webpage](#BKMK_mspp_website_webpage)
- [mspp_website_webpageaccesscontrolrule](#BKMK_mspp_website_webpageaccesscontrolrule)
- [mspp_website_webrole](#BKMK_mspp_website_webrole)
- [mspp_website_websiteaccess](#BKMK_mspp_website_websiteaccess)

### <a name="BKMK_mspp_columnpermissionprofile_website"></a> mspp_columnpermissionprofile_website

Many-To-One Relationship: [mspp_columnpermissionprofile mspp_columnpermissionprofile_website](mspp_columnpermissionprofile.md#BKMK_mspp_columnpermissionprofile_website)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_columnpermissionprofile`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_columnpermissionprofile_website`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_mspp_website_mspp_websitelanguage"></a> mspp_mspp_website_mspp_websitelanguage

Many-To-One Relationship: [mspp_websitelanguage mspp_mspp_website_mspp_websitelanguage](mspp_websitelanguage.md#BKMK_mspp_mspp_website_mspp_websitelanguage)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_websitelanguage`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_mspp_website_mspp_websitelanguage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_ActivityPointers"></a> mspp_website_ActivityPointers

Many-To-One Relationship: [activitypointer mspp_website_ActivityPointers](activitypointer.md#BKMK_mspp_website_ActivityPointers)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_ActivityPointers`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_adplacement"></a> mspp_website_adplacement

Many-To-One Relationship: [mspp_adplacement mspp_website_adplacement](mspp_adplacement.md#BKMK_mspp_website_adplacement)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_adplacement`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_adplacement`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_adx_inviteredemptions"></a> mspp_website_adx_inviteredemptions

Many-To-One Relationship: [adx_inviteredemption mspp_website_adx_inviteredemptions](adx_inviteredemption.md#BKMK_mspp_website_adx_inviteredemptions)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_adx_inviteredemptions`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_adx_portalcomments"></a> mspp_website_adx_portalcomments

Many-To-One Relationship: [adx_portalcomment mspp_website_adx_portalcomments](adx_portalcomment.md#BKMK_mspp_website_adx_portalcomments)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_adx_portalcomments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_Appointments"></a> mspp_website_Appointments

Many-To-One Relationship: [appointment mspp_website_Appointments](appointment.md#BKMK_mspp_website_Appointments)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_Appointments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_chats"></a> mspp_website_chats

Many-To-One Relationship: [chat mspp_website_chats](chat.md#BKMK_mspp_website_chats)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_chats`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_connections1"></a> mspp_website_connections1

Many-To-One Relationship: [connection mspp_website_connections1](connection.md#BKMK_mspp_website_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`mspp_website_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_connections2"></a> mspp_website_connections2

Many-To-One Relationship: [connection mspp_website_connections2](connection.md#BKMK_mspp_website_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`mspp_website_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_contentsnippet"></a> mspp_website_contentsnippet

Many-To-One Relationship: [mspp_contentsnippet mspp_website_contentsnippet](mspp_contentsnippet.md#BKMK_mspp_website_contentsnippet)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_contentsnippet`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_contentsnippet`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100700<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_Emails"></a> mspp_website_Emails

Many-To-One Relationship: [email mspp_website_Emails](email.md#BKMK_mspp_website_Emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_Emails`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_entityform"></a> mspp_website_entityform

Many-To-One Relationship: [mspp_entityform mspp_website_entityform](mspp_entityform.md#BKMK_mspp_website_entityform)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_entityform`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_entityform`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_entitylist"></a> mspp_website_entitylist

Many-To-One Relationship: [mspp_entitylist mspp_website_entitylist](mspp_entitylist.md#BKMK_mspp_website_entitylist)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_entitylist`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_entitylist`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_Faxes"></a> mspp_website_Faxes

Many-To-One Relationship: [fax mspp_website_Faxes](fax.md#BKMK_mspp_website_Faxes)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_Faxes`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_Letters"></a> mspp_website_Letters

Many-To-One Relationship: [letter mspp_website_Letters](letter.md#BKMK_mspp_website_Letters)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_Letters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_mspp_entitypermission"></a> mspp_website_mspp_entitypermission

Many-To-One Relationship: [mspp_entitypermission mspp_website_mspp_entitypermission](mspp_entitypermission.md#BKMK_mspp_website_mspp_entitypermission)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_entitypermission`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_mspp_entitypermission`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_mspp_webtemplate"></a> mspp_website_mspp_webtemplate

Many-To-One Relationship: [mspp_webtemplate mspp_website_mspp_webtemplate](mspp_webtemplate.md#BKMK_mspp_website_mspp_webtemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webtemplate`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_mspp_webtemplate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_pagetemplate"></a> mspp_website_pagetemplate

Many-To-One Relationship: [mspp_pagetemplate mspp_website_pagetemplate](mspp_pagetemplate.md#BKMK_mspp_website_pagetemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_pagetemplate`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_pagetemplate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 102100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_parentwebsite-one-to-many"></a> mspp_website_parentwebsite

Many-To-One Relationship: [mspp_website mspp_website_parentwebsite](#BKMK_mspp_website_parentwebsite-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_website`|
|ReferencingAttribute|`mspp_parentwebsiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_parentwebsite`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Child Websites<br />MenuId: null<br />Order: 100500<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_PhoneCalls"></a> mspp_website_PhoneCalls

Many-To-One Relationship: [phonecall mspp_website_PhoneCalls](phonecall.md#BKMK_mspp_website_PhoneCalls)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_PhoneCalls`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_pollplacement"></a> mspp_website_pollplacement

Many-To-One Relationship: [mspp_pollplacement mspp_website_pollplacement](mspp_pollplacement.md#BKMK_mspp_website_pollplacement)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_pollplacement`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_pollplacement`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 102200<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_publishingstate"></a> mspp_website_publishingstate

Many-To-One Relationship: [mspp_publishingstate mspp_website_publishingstate](mspp_publishingstate.md#BKMK_mspp_website_publishingstate)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_publishingstate`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_publishingstate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 102500<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_publishingstatetransition"></a> mspp_website_publishingstatetransition

Many-To-One Relationship: [mspp_publishingstatetransitionrule mspp_website_publishingstatetransition](mspp_publishingstatetransitionrule.md#BKMK_mspp_website_publishingstatetransition)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_publishingstatetransitionrule`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_publishingstatetransition`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 102400<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_RecurringAppointmentMasters"></a> mspp_website_RecurringAppointmentMasters

Many-To-One Relationship: [recurringappointmentmaster mspp_website_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_mspp_website_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_RecurringAppointmentMasters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_redirect"></a> mspp_website_redirect

Many-To-One Relationship: [mspp_redirect mspp_website_redirect](mspp_redirect.md#BKMK_mspp_website_redirect)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_redirect`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_redirect`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 102600<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_SharePointDocumentLocations"></a> mspp_website_SharePointDocumentLocations

Many-To-One Relationship: [sharepointdocumentlocation mspp_website_SharePointDocumentLocations](sharepointdocumentlocation.md#BKMK_mspp_website_SharePointDocumentLocations)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointdocumentlocation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_SharePointDocumentLocations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_shortcut"></a> mspp_website_shortcut

Many-To-One Relationship: [mspp_shortcut mspp_website_shortcut](mspp_shortcut.md#BKMK_mspp_website_shortcut)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_shortcut`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_shortcut`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 102700<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_sitemarker"></a> mspp_website_sitemarker

Many-To-One Relationship: [mspp_sitemarker mspp_website_sitemarker](mspp_sitemarker.md#BKMK_mspp_website_sitemarker)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_sitemarker`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_sitemarker`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 102800<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_sitesetting"></a> mspp_website_sitesetting

Many-To-One Relationship: [mspp_sitesetting mspp_website_sitesetting](mspp_sitesetting.md#BKMK_mspp_website_sitesetting)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_sitesetting`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_sitesetting`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 102900<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_SocialActivities"></a> mspp_website_SocialActivities

Many-To-One Relationship: [socialactivity mspp_website_SocialActivities](socialactivity.md#BKMK_mspp_website_SocialActivities)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_SocialActivities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_Tasks"></a> mspp_website_Tasks

Many-To-One Relationship: [task mspp_website_Tasks](task.md#BKMK_mspp_website_Tasks)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_Tasks`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_webfile"></a> mspp_website_webfile

Many-To-One Relationship: [mspp_webfile mspp_website_webfile](mspp_webfile.md#BKMK_mspp_website_webfile)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webfile`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_webfile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 103200<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_webform"></a> mspp_website_webform

Many-To-One Relationship: [mspp_webform mspp_website_webform](mspp_webform.md#BKMK_mspp_website_webform)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webform`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_webform`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_weblinkset"></a> mspp_website_weblinkset

Many-To-One Relationship: [mspp_weblinkset mspp_website_weblinkset](mspp_weblinkset.md#BKMK_mspp_website_weblinkset)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_weblinkset`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_weblinkset`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 103300<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_webpage"></a> mspp_website_webpage

Many-To-One Relationship: [mspp_webpage mspp_website_webpage](mspp_webpage.md#BKMK_mspp_website_webpage)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_webpage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 103500<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_webpageaccesscontrolrule"></a> mspp_website_webpageaccesscontrolrule

Many-To-One Relationship: [mspp_webpageaccesscontrolrule mspp_website_webpageaccesscontrolrule](mspp_webpageaccesscontrolrule.md#BKMK_mspp_website_webpageaccesscontrolrule)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpageaccesscontrolrule`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_webpageaccesscontrolrule`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 103400<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_webrole"></a> mspp_website_webrole

Many-To-One Relationship: [mspp_webrole mspp_website_webrole](mspp_webrole.md#BKMK_mspp_website_webrole)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webrole`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_webrole`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 103600<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_website_websiteaccess"></a> mspp_website_websiteaccess

Many-To-One Relationship: [mspp_websiteaccess mspp_website_websiteaccess](mspp_websiteaccess.md#BKMK_mspp_website_websiteaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_websiteaccess`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencedEntityNavigationPropertyName|`mspp_website_websiteaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 103700<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_website?displayProperty=fullName>
