---
title: "List (mspp_entitylist) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the List (mspp_entitylist) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# List (mspp_entitylist) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the List (mspp_entitylist) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_entitylists<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_entitylists(*mspp_entitylistid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_entitylists(*mspp_entitylistid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_entitylists<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_entitylists(*mspp_entitylistid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_entitylists(*mspp_entitylistid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the List (mspp_entitylist) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the List (mspp_entitylist) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **List** |
| **DisplayCollectionName** | **Lists** |
| **SchemaName** | `mspp_entitylist` |
| **CollectionSchemaName** | `mspp_entitylists` |
| **EntitySetName** | `mspp_entitylists`|
| **LogicalName** | `mspp_entitylist` |
| **LogicalCollectionName** | `mspp_entitylists` |
| **PrimaryIdAttribute** | `mspp_entitylistid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_calendar_alldayfieldname](#BKMK_mspp_calendar_alldayfieldname)
- [mspp_calendar_descriptionfieldname](#BKMK_mspp_calendar_descriptionfieldname)
- [mspp_calendar_enabled](#BKMK_mspp_calendar_enabled)
- [mspp_calendar_enddatefieldname](#BKMK_mspp_calendar_enddatefieldname)
- [mspp_calendar_initialdate](#BKMK_mspp_calendar_initialdate)
- [mspp_calendar_initialview](#BKMK_mspp_calendar_initialview)
- [mspp_calendar_locationfieldname](#BKMK_mspp_calendar_locationfieldname)
- [mspp_calendar_organizerfieldname](#BKMK_mspp_calendar_organizerfieldname)
- [mspp_calendar_startdatefieldname](#BKMK_mspp_calendar_startdatefieldname)
- [mspp_calendar_style](#BKMK_mspp_calendar_style)
- [mspp_calendar_summaryfieldname](#BKMK_mspp_calendar_summaryfieldname)
- [mspp_calendar_timezone](#BKMK_mspp_calendar_timezone)
- [mspp_calendar_timezonemode](#BKMK_mspp_calendar_timezonemode)
- [mspp_createbuttonlabel](#BKMK_mspp_createbuttonlabel)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_detailsbuttonlabel](#BKMK_mspp_detailsbuttonlabel)
- [mspp_emptylisttext](#BKMK_mspp_emptylisttext)
- [mspp_entitylistId](#BKMK_mspp_entitylistId)
- [mspp_entityname](#BKMK_mspp_entityname)
- [mspp_entitypermissionsenabled](#BKMK_mspp_entitypermissionsenabled)
- [mspp_filter_applybuttonlabel](#BKMK_mspp_filter_applybuttonlabel)
- [mspp_filter_definition](#BKMK_mspp_filter_definition)
- [mspp_filter_enabled](#BKMK_mspp_filter_enabled)
- [mspp_filter_orientation](#BKMK_mspp_filter_orientation)
- [mspp_filteraccount](#BKMK_mspp_filteraccount)
- [mspp_filterportaluser](#BKMK_mspp_filterportaluser)
- [mspp_filterwebsite](#BKMK_mspp_filterwebsite)
- [mspp_idquerystringparametername](#BKMK_mspp_idquerystringparametername)
- [mspp_iscodecomponent](#BKMK_mspp_iscodecomponent)
- [mspp_key](#BKMK_mspp_key)
- [mspp_map_credentials](#BKMK_mspp_map_credentials)
- [mspp_map_distanceunits](#BKMK_mspp_map_distanceunits)
- [mspp_map_distancevalues](#BKMK_mspp_map_distancevalues)
- [mspp_map_enabled](#BKMK_mspp_map_enabled)
- [mspp_map_infoboxdescriptionfieldname](#BKMK_mspp_map_infoboxdescriptionfieldname)
- [mspp_map_infoboxoffsetx](#BKMK_mspp_map_infoboxoffsetx)
- [mspp_map_infoboxoffsety](#BKMK_mspp_map_infoboxoffsety)
- [mspp_map_infoboxtitlefieldname](#BKMK_mspp_map_infoboxtitlefieldname)
- [mspp_map_latitude](#BKMK_mspp_map_latitude)
- [mspp_map_latitudefieldname](#BKMK_mspp_map_latitudefieldname)
- [mspp_map_longitude](#BKMK_mspp_map_longitude)
- [mspp_map_longitudefieldname](#BKMK_mspp_map_longitudefieldname)
- [mspp_map_pushpinheight](#BKMK_mspp_map_pushpinheight)
- [mspp_map_pushpinurl](#BKMK_mspp_map_pushpinurl)
- [mspp_map_pushpinwidth](#BKMK_mspp_map_pushpinwidth)
- [mspp_map_resturl](#BKMK_mspp_map_resturl)
- [mspp_map_type](#BKMK_mspp_map_type)
- [mspp_map_zoom](#BKMK_mspp_map_zoom)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_odata_enabled](#BKMK_mspp_odata_enabled)
- [mspp_odata_entitysetname](#BKMK_mspp_odata_entitysetname)
- [mspp_odata_entitytypename](#BKMK_mspp_odata_entitytypename)
- [mspp_odata_view](#BKMK_mspp_odata_view)
- [mspp_pagesize](#BKMK_mspp_pagesize)
- [mspp_primarykeyname](#BKMK_mspp_primarykeyname)
- [mspp_provisionedlanguages](#BKMK_mspp_provisionedlanguages)
- [mspp_registerstartupscript](#BKMK_mspp_registerstartupscript)
- [mspp_searchenabled](#BKMK_mspp_searchenabled)
- [mspp_searchplaceholdertext](#BKMK_mspp_searchplaceholdertext)
- [mspp_searchtooltiptext](#BKMK_mspp_searchtooltiptext)
- [mspp_settings](#BKMK_mspp_settings)
- [mspp_view](#BKMK_mspp_view)
- [mspp_views](#BKMK_mspp_views)
- [mspp_webpageforcreate](#BKMK_mspp_webpageforcreate)
- [mspp_webpagefordetailsview](#BKMK_mspp_webpagefordetailsview)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

### <a name="BKMK_mspp_calendar_alldayfieldname"></a> mspp_calendar_alldayfieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is All Day Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_alldayfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_calendar_descriptionfieldname"></a> mspp_calendar_descriptionfieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Description Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_descriptionfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_calendar_enabled"></a> mspp_calendar_enabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Calendar View Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_enabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitylist_mspp_calendar_enabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_calendar_enddatefieldname"></a> mspp_calendar_enddatefieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**End Date Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_enddatefieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_calendar_initialdate"></a> mspp_calendar_initialdate

|Property|Value|
|---|---|
|Description||
|DisplayName|**Calendar Initial Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_initialdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_mspp_calendar_initialview"></a> mspp_calendar_initialview

|Property|Value|
|---|---|
|Description||
|DisplayName|**Calendar Initial View**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_initialview`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150001|
|GlobalChoiceName|`mspp_entitylist_mspp_calendar_initialview`|

#### mspp_calendar_initialview Choices/Options

|Value|Label|
|---|---|
|756150000|**Year**|
|756150001|**Month**|
|756150002|**Week**|
|756150003|**Day**|

### <a name="BKMK_mspp_calendar_locationfieldname"></a> mspp_calendar_locationfieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Location Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_locationfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_calendar_organizerfieldname"></a> mspp_calendar_organizerfieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Organizer Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_organizerfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_calendar_startdatefieldname"></a> mspp_calendar_startdatefieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Start Date Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_startdatefieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_calendar_style"></a> mspp_calendar_style

|Property|Value|
|---|---|
|Description||
|DisplayName|**Calendar Style**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_style`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150000|
|GlobalChoiceName|`mspp_entitylist_mspp_calendar_style`|

#### mspp_calendar_style Choices/Options

|Value|Label|
|---|---|
|756150000|**Full calendar**|
|756150001|**Event list**|

### <a name="BKMK_mspp_calendar_summaryfieldname"></a> mspp_calendar_summaryfieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Summary Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_summaryfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_calendar_timezone"></a> mspp_calendar_timezone

|Property|Value|
|---|---|
|Description||
|DisplayName|**Display Time Zone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_timezone`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1500|
|MinValue|-1500|

### <a name="BKMK_mspp_calendar_timezonemode"></a> mspp_calendar_timezonemode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Time Zone Display Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_calendar_timezonemode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150000|
|GlobalChoiceName|`mspp_entitylist_mspp_calendar_timezonemode`|

#### mspp_calendar_timezonemode Choices/Options

|Value|Label|
|---|---|
|756150000|**User Local Time Zone**|
|756150001|**Specific Time Zone**|

### <a name="BKMK_mspp_createbuttonlabel"></a> mspp_createbuttonlabel

|Property|Value|
|---|---|
|Description||
|DisplayName|**Create Button Label**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createbuttonlabel`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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

### <a name="BKMK_mspp_detailsbuttonlabel"></a> mspp_detailsbuttonlabel

|Property|Value|
|---|---|
|Description||
|DisplayName|**Details Button Label**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_detailsbuttonlabel`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_emptylisttext"></a> mspp_emptylisttext

|Property|Value|
|---|---|
|Description||
|DisplayName|**Empty List Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_emptylisttext`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_mspp_entitylistId"></a> mspp_entitylistId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**List**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_entitylistid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_entityname"></a> mspp_entityname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Table Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entityname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_entitypermissionsenabled"></a> mspp_entitypermissionsenabled

|Property|Value|
|---|---|
|Description|**Indicates whether or not the table permission provider will assert privileges on the entity type associated with this list.**|
|DisplayName|**Enable Table Permissions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entitypermissionsenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitylist_mspp_entitypermissionsenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_filter_applybuttonlabel"></a> mspp_filter_applybuttonlabel

|Property|Value|
|---|---|
|Description||
|DisplayName|**Apply Button Label**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_filter_applybuttonlabel`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_filter_definition"></a> mspp_filter_definition

|Property|Value|
|---|---|
|Description||
|DisplayName|**Filter Definition**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_filter_definition`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|65536|

### <a name="BKMK_mspp_filter_enabled"></a> mspp_filter_enabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Filter Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_filter_enabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitylist_mspp_filter_enabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_filter_orientation"></a> mspp_filter_orientation

|Property|Value|
|---|---|
|Description||
|DisplayName|**Filter Orientation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_filter_orientation`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspp_entitylist_mspp_filter_orientation`|

#### mspp_filter_orientation Choices/Options

|Value|Label|
|---|---|
|756150000|**Horizontal**|
|756150001|**Vertical**|

### <a name="BKMK_mspp_filteraccount"></a> mspp_filteraccount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Filter Account Attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_filteraccount`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_mspp_filterportaluser"></a> mspp_filterportaluser

|Property|Value|
|---|---|
|Description||
|DisplayName|**Filter Portal User Attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_filterportaluser`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_mspp_filterwebsite"></a> mspp_filterwebsite

|Property|Value|
|---|---|
|Description||
|DisplayName|**Filter Website Attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_filterwebsite`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_mspp_idquerystringparametername"></a> mspp_idquerystringparametername

|Property|Value|
|---|---|
|Description|**The name of the parameter added to the Query String of the list item's URL that will contain the list item record's ID.**|
|DisplayName|**ID Query String Parameter Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_idquerystringparametername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_iscodecomponent"></a> mspp_iscodecomponent

|Property|Value|
|---|---|
|Description|**Use a configured code component**|
|DisplayName|**Use a configured code component**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_iscodecomponent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitylist_mspp_iscodecomponent`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_key"></a> mspp_key

|Property|Value|
|---|---|
|Description|**A non-localizable string that can be used by queries to retrieve the record.**|
|DisplayName|**Key**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_key`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_map_credentials"></a> mspp_map_credentials

|Property|Value|
|---|---|
|Description||
|DisplayName|**Credentials**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_credentials`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_map_distanceunits"></a> mspp_map_distanceunits

|Property|Value|
|---|---|
|Description||
|DisplayName|**Distance Units**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_distanceunits`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150001|
|GlobalChoiceName|`mspp_entitylist_mspp_map_distanceunits`|

#### mspp_map_distanceunits Choices/Options

|Value|Label|
|---|---|
|756150000|**Km**|
|756150001|**miles**|

### <a name="BKMK_mspp_map_distancevalues"></a> mspp_map_distancevalues

|Property|Value|
|---|---|
|Description|**Shows a comma-delimited list of integer values to be populated in the drop-down list  in the web portal for selecting the distance to search for a location on the map.**|
|DisplayName|**Distance Values**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_distancevalues`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_map_enabled"></a> mspp_map_enabled

|Property|Value|
|---|---|
|Description|**Indicates if a map view of the data is to be rendered.**|
|DisplayName|**Map Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_enabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitylist_mspp_map_enabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_map_infoboxdescriptionfieldname"></a> mspp_map_infoboxdescriptionfieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Infobox Description Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_infoboxdescriptionfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_map_infoboxoffsetx"></a> mspp_map_infoboxoffsetx

|Property|Value|
|---|---|
|Description||
|DisplayName|**Infobox Offset x**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_infoboxoffsetx`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_mspp_map_infoboxoffsety"></a> mspp_map_infoboxoffsety

|Property|Value|
|---|---|
|Description||
|DisplayName|**Infobox Offset y**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_infoboxoffsety`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_mspp_map_infoboxtitlefieldname"></a> mspp_map_infoboxtitlefieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Infobox Title Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_infoboxtitlefieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_map_latitude"></a> mspp_map_latitude

|Property|Value|
|---|---|
|Description||
|DisplayName|**Latitude**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_latitude`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|90|
|MinValue|-90|
|Precision|5|

### <a name="BKMK_mspp_map_latitudefieldname"></a> mspp_map_latitudefieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Latitude Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_latitudefieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_map_longitude"></a> mspp_map_longitude

|Property|Value|
|---|---|
|Description||
|DisplayName|**Longitude**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_longitude`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|180|
|MinValue|-180|
|Precision|5|

### <a name="BKMK_mspp_map_longitudefieldname"></a> mspp_map_longitudefieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Longitude Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_longitudefieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_map_pushpinheight"></a> mspp_map_pushpinheight

|Property|Value|
|---|---|
|Description||
|DisplayName|**Pin Image Height**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_pushpinheight`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_map_pushpinurl"></a> mspp_map_pushpinurl

|Property|Value|
|---|---|
|Description||
|DisplayName|**Pin Image URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_pushpinurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

### <a name="BKMK_mspp_map_pushpinwidth"></a> mspp_map_pushpinwidth

|Property|Value|
|---|---|
|Description||
|DisplayName|**Pin Image Width**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_pushpinwidth`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_map_resturl"></a> mspp_map_resturl

|Property|Value|
|---|---|
|Description||
|DisplayName|**REST URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_resturl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

### <a name="BKMK_mspp_map_type"></a> mspp_map_type

|Property|Value|
|---|---|
|Description||
|DisplayName|**Map Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_type`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150000|
|GlobalChoiceName|`mspp_entitylist_mspp_map_type`|

#### mspp_map_type Choices/Options

|Value|Label|
|---|---|
|756150000|**Bing**|
|756150001|**Google**|
|756150002|**Esri**|

### <a name="BKMK_mspp_map_zoom"></a> mspp_map_zoom

|Property|Value|
|---|---|
|Description||
|DisplayName|**Zoom**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_map_zoom`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

### <a name="BKMK_mspp_odata_enabled"></a> mspp_odata_enabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**OData Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_odata_enabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitylist_mspp_odata_enabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_odata_entitysetname"></a> mspp_odata_entitysetname

|Property|Value|
|---|---|
|Description||
|DisplayName|**OData Entity Set Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_odata_entitysetname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_odata_entitytypename"></a> mspp_odata_entitytypename

|Property|Value|
|---|---|
|Description||
|DisplayName|**OData Entity Type Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_odata_entitytypename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_odata_view"></a> mspp_odata_view

|Property|Value|
|---|---|
|Description|**The entity view that defines the columns that will be mapped to properties of the entity exposed in the OData feed.**|
|DisplayName|**OData View**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_odata_view`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_pagesize"></a> mspp_pagesize

|Property|Value|
|---|---|
|Description||
|DisplayName|**Page Size**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_pagesize`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_mspp_primarykeyname"></a> mspp_primarykeyname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Primary Key Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_primarykeyname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_provisionedlanguages"></a> mspp_provisionedlanguages

|Property|Value|
|---|---|
|Description||
|DisplayName|**Provisioned Languages**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_provisionedlanguages`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_registerstartupscript"></a> mspp_registerstartupscript

|Property|Value|
|---|---|
|Description|**Shows your custom JavaScript that will be placed at the bottom of the page right before the closing </form> element.**|
|DisplayName|**Custom JavaScript**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_registerstartupscript`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_mspp_searchenabled"></a> mspp_searchenabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Search Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_searchenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitylist_mspp_searchenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_searchplaceholdertext"></a> mspp_searchplaceholdertext

|Property|Value|
|---|---|
|Description||
|DisplayName|**Search Placeholder Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_searchplaceholdertext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_searchtooltiptext"></a> mspp_searchtooltiptext

|Property|Value|
|---|---|
|Description||
|DisplayName|**Search Tooltip Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_searchtooltiptext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_settings"></a> mspp_settings

|Property|Value|
|---|---|
|Description||
|DisplayName|**Settings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_settings`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_mspp_view"></a> mspp_view

|Property|Value|
|---|---|
|Description|**Deprecated**|
|DisplayName|**View**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_view`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_views"></a> mspp_views

|Property|Value|
|---|---|
|Description||
|DisplayName|**Views**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_views`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_mspp_webpageforcreate"></a> mspp_webpageforcreate

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Page associated with Entity List.**|
|DisplayName|**Web Page for Create**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webpageforcreate`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webpage|

### <a name="BKMK_mspp_webpagefordetailsview"></a> mspp_webpagefordetailsview

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Page associated with Entity List.**|
|DisplayName|**Web Page for Details View**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webpagefordetailsview`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webpage|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website entity associated with this record**|
|DisplayName|**Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_websiteid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_website|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the List**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_entitylist_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the List**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_entitylist_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_entitylist_webpageforcreate](#BKMK_mspp_entitylist_webpageforcreate)
- [mspp_entitylist_webpagefordetailsview](#BKMK_mspp_entitylist_webpagefordetailsview)
- [mspp_systemuser_mspp_entitylist_createdby](#BKMK_mspp_systemuser_mspp_entitylist_createdby)
- [mspp_systemuser_mspp_entitylist_modifiedby](#BKMK_mspp_systemuser_mspp_entitylist_modifiedby)
- [mspp_website_entitylist](#BKMK_mspp_website_entitylist)

### <a name="BKMK_mspp_entitylist_webpageforcreate"></a> mspp_entitylist_webpageforcreate

One-To-Many Relationship: [mspp_webpage mspp_entitylist_webpageforcreate](mspp_webpage.md#BKMK_mspp_entitylist_webpageforcreate)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_webpageforcreate`|
|ReferencingEntityNavigationPropertyName|`mspp_webpageforcreate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_entitylist_webpagefordetailsview"></a> mspp_entitylist_webpagefordetailsview

One-To-Many Relationship: [mspp_webpage mspp_entitylist_webpagefordetailsview](mspp_webpage.md#BKMK_mspp_entitylist_webpagefordetailsview)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_webpagefordetailsview`|
|ReferencingEntityNavigationPropertyName|`mspp_webpagefordetailsview`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_entitylist_createdby"></a> mspp_systemuser_mspp_entitylist_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_entitylist_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_entitylist_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_entitylist_modifiedby"></a> mspp_systemuser_mspp_entitylist_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_entitylist_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_entitylist_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_entitylist"></a> mspp_website_entitylist

One-To-Many Relationship: [mspp_website mspp_website_entitylist](mspp_website.md#BKMK_mspp_website_entitylist)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_websiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_mspp_webpage_entitylist"></a> mspp_webpage_entitylist

Many-To-One Relationship: [mspp_webpage mspp_webpage_entitylist](mspp_webpage.md#BKMK_mspp_webpage_entitylist)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_entitylist`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_entitylist`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_entitylist?displayProperty=fullName>
