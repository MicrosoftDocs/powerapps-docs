---
title: "List (mspp_entitylist)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the List (mspp_entitylist)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# List (mspp_entitylist)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_entitylists<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_entitylists(*mspp_entitylistid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_entitylists(*mspp_entitylistid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_entitylists<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_entitylists(*mspp_entitylistid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_entitylists|
|DisplayCollectionName|Lists|
|DisplayName|List|
|EntitySetName|mspp_entitylists|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_entitylists|
|LogicalName|mspp_entitylist|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_entitylistid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_entitylist|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description||
|DisplayName|Is All Day Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_alldayfieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_calendar_descriptionfieldname"></a> mspp_calendar_descriptionfieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Description Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_descriptionfieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_calendar_enabled"></a> mspp_calendar_enabled

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Calendar View Enabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_enabled|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_calendar_enabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_calendar_enddatefieldname"></a> mspp_calendar_enddatefieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|End Date Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_enddatefieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_calendar_initialdate"></a> mspp_calendar_initialdate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|Calendar Initial Date|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_initialdate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_mspp_calendar_initialview"></a> mspp_calendar_initialview

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Calendar Initial View|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_initialview|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_calendar_initialview Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Year||
|756150001|Month||
|756150002|Week||
|756150003|Day||



### <a name="BKMK_mspp_calendar_locationfieldname"></a> mspp_calendar_locationfieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Location Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_locationfieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_calendar_organizerfieldname"></a> mspp_calendar_organizerfieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Organizer Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_organizerfieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_calendar_startdatefieldname"></a> mspp_calendar_startdatefieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Start Date Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_startdatefieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_calendar_style"></a> mspp_calendar_style

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Calendar Style|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_style|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_calendar_style Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Full calendar||
|756150001|Event list||



### <a name="BKMK_mspp_calendar_summaryfieldname"></a> mspp_calendar_summaryfieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Summary Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_summaryfieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_calendar_timezone"></a> mspp_calendar_timezone

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Display Time Zone|
|Format|TimeZone|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_timezone|
|MaxValue|1500|
|MinValue|-1500|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_calendar_timezonemode"></a> mspp_calendar_timezonemode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Time Zone Display Mode|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_calendar_timezonemode|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_calendar_timezonemode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|User Local Time Zone||
|756150001|Specific Time Zone||



### <a name="BKMK_mspp_createbuttonlabel"></a> mspp_createbuttonlabel

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Create Button Label|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_createbuttonlabel|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_mspp_detailsbuttonlabel"></a> mspp_detailsbuttonlabel

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Details Button Label|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_detailsbuttonlabel|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_emptylisttext"></a> mspp_emptylisttext

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Empty List Text|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_emptylisttext|
|MaxLength|10000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_entitylistId"></a> mspp_entitylistId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|List|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_entitylistid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_entityname"></a> mspp_entityname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Table Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_entityname|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_entitypermissionsenabled"></a> mspp_entitypermissionsenabled

|Property|Value|
|--------|-----|
|Description|Indicates whether or not the table permission provider will assert privileges on the entity type associated with this list.|
|DisplayName|Enable Table Permissions|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_entitypermissionsenabled|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_entitypermissionsenabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_mspp_filter_applybuttonlabel"></a> mspp_filter_applybuttonlabel

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Apply Button Label|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_filter_applybuttonlabel|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_filter_definition"></a> mspp_filter_definition

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Filter Definition|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_filter_definition|
|MaxLength|65536|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_filter_enabled"></a> mspp_filter_enabled

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Filter Enabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_filter_enabled|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_filter_enabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_filter_orientation"></a> mspp_filter_orientation

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Filter Orientation|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_filter_orientation|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_filter_orientation Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Horizontal||
|756150001|Vertical||



### <a name="BKMK_mspp_filteraccount"></a> mspp_filteraccount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Filter Account Attribute|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_filteraccount|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_filterportaluser"></a> mspp_filterportaluser

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Filter Portal User Attribute|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_filterportaluser|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_filterwebsite"></a> mspp_filterwebsite

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Filter Website Attribute|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_filterwebsite|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_idquerystringparametername"></a> mspp_idquerystringparametername

|Property|Value|
|--------|-----|
|Description|The name of the parameter added to the Query String of the list item's URL that will contain the list item record's ID.|
|DisplayName|ID Query String Parameter Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_idquerystringparametername|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_iscodecomponent"></a> mspp_iscodecomponent

|Property|Value|
|--------|-----|
|Description|Use a configured code component|
|DisplayName|Use a configured code component|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_iscodecomponent|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_iscodecomponent Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_key"></a> mspp_key

|Property|Value|
|--------|-----|
|Description|A non-localizable string that can be used by queries to retrieve the record.|
|DisplayName|Key|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_key|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_map_credentials"></a> mspp_map_credentials

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Credentials|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_credentials|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_map_distanceunits"></a> mspp_map_distanceunits

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Distance Units|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_distanceunits|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_map_distanceunits Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Km||
|756150001|miles||



### <a name="BKMK_mspp_map_distancevalues"></a> mspp_map_distancevalues

|Property|Value|
|--------|-----|
|Description|Shows a comma-delimited list of integer values to be populated in the drop-down list  in the web portal for selecting the distance to search for a location on the map.|
|DisplayName|Distance Values|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_distancevalues|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_map_enabled"></a> mspp_map_enabled

|Property|Value|
|--------|-----|
|Description|Indicates if a map view of the data is to be rendered.|
|DisplayName|Map Enabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_enabled|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_map_enabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_map_infoboxdescriptionfieldname"></a> mspp_map_infoboxdescriptionfieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Infobox Description Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_infoboxdescriptionfieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_map_infoboxoffsetx"></a> mspp_map_infoboxoffsetx

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Infobox Offset x|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_infoboxoffsetx|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_map_infoboxoffsety"></a> mspp_map_infoboxoffsety

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Infobox Offset y|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_infoboxoffsety|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_map_infoboxtitlefieldname"></a> mspp_map_infoboxtitlefieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Infobox Title Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_infoboxtitlefieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_map_latitude"></a> mspp_map_latitude

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Latitude|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_latitude|
|MaxValue|90|
|MinValue|-90|
|Precision|5|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_mspp_map_latitudefieldname"></a> mspp_map_latitudefieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Latitude Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_latitudefieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_map_longitude"></a> mspp_map_longitude

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Longitude|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_longitude|
|MaxValue|180|
|MinValue|-180|
|Precision|5|
|RequiredLevel|None|
|Type|Double|


### <a name="BKMK_mspp_map_longitudefieldname"></a> mspp_map_longitudefieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Longitude Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_longitudefieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_map_pushpinheight"></a> mspp_map_pushpinheight

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Pin Image Height|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_pushpinheight|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_map_pushpinurl"></a> mspp_map_pushpinurl

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Pin Image URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_pushpinurl|
|MaxLength|300|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_map_pushpinwidth"></a> mspp_map_pushpinwidth

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Pin Image Width|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_pushpinwidth|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_map_resturl"></a> mspp_map_resturl

|Property|Value|
|--------|-----|
|Description||
|DisplayName|REST URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_resturl|
|MaxLength|300|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_map_type"></a> mspp_map_type

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Map Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_type|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_map_type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Bing||
|756150001|Google||
|756150002|Esri||



### <a name="BKMK_mspp_map_zoom"></a> mspp_map_zoom

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Zoom|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_map_zoom|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


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


### <a name="BKMK_mspp_odata_enabled"></a> mspp_odata_enabled

|Property|Value|
|--------|-----|
|Description||
|DisplayName|OData Enabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_odata_enabled|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_odata_enabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_odata_entitysetname"></a> mspp_odata_entitysetname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|OData Entity Set Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_odata_entitysetname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_odata_entitytypename"></a> mspp_odata_entitytypename

|Property|Value|
|--------|-----|
|Description||
|DisplayName|OData Entity Type Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_odata_entitytypename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_odata_view"></a> mspp_odata_view

|Property|Value|
|--------|-----|
|Description|The entity view that defines the columns that will be mapped to properties of the entity exposed in the OData feed.|
|DisplayName|OData View|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_odata_view|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_pagesize"></a> mspp_pagesize

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Page Size|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_pagesize|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_mspp_primarykeyname"></a> mspp_primarykeyname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Primary Key Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_primarykeyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_provisionedlanguages"></a> mspp_provisionedlanguages

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Provisioned Languages|
|Format|Language|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_provisionedlanguages|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_registerstartupscript"></a> mspp_registerstartupscript

|Property|Value|
|--------|-----|
|Description|Shows your custom JavaScript that will be placed at the bottom of the page right before the closing </form> element.|
|DisplayName|Custom JavaScript|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_registerstartupscript|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_searchenabled"></a> mspp_searchenabled

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Search Enabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_searchenabled|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_searchenabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_searchplaceholdertext"></a> mspp_searchplaceholdertext

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Search Placeholder Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_searchplaceholdertext|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_searchtooltiptext"></a> mspp_searchtooltiptext

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Search Tooltip Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_searchtooltiptext|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_settings"></a> mspp_settings

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Settings|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_settings|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_view"></a> mspp_view

|Property|Value|
|--------|-----|
|Description|Deprecated|
|DisplayName|View|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_view|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_views"></a> mspp_views

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Views|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_views|
|MaxLength|100000|
|RequiredLevel|ApplicationRequired|
|Type|Memo|


### <a name="BKMK_mspp_webpageforcreate"></a> mspp_webpageforcreate

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Page associated with Entity List.|
|DisplayName|Web Page for Create|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webpageforcreate|
|RequiredLevel|None|
|Targets|mspp_webpage|
|Type|Lookup|


### <a name="BKMK_mspp_webpagefordetailsview"></a> mspp_webpagefordetailsview

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Page associated with Entity List.|
|DisplayName|Web Page for Details View|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webpagefordetailsview|
|RequiredLevel|None|
|Targets|mspp_webpage|
|Type|Lookup|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website entity associated with this record|
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
|Description|Status of the List|
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
|Description|Reason for the status of the List|
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
- [mspp_webpageforcreateName](#BKMK_mspp_webpageforcreateName)
- [mspp_webpagefordetailsviewName](#BKMK_mspp_webpagefordetailsviewName)
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


### <a name="BKMK_mspp_webpageforcreateName"></a> mspp_webpageforcreateName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_webpageforcreatename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_webpagefordetailsviewName"></a> mspp_webpagefordetailsviewName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_webpagefordetailsviewname|
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


### <a name="BKMK_mspp_webpage_entitylist"></a> mspp_webpage_entitylist

Same as the [mspp_webpage_entitylist](mspp_webpage.md#BKMK_mspp_webpage_entitylist) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_entitylist|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_entitylist|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_entitylist_webpageforcreate](#BKMK_mspp_entitylist_webpageforcreate)
- [mspp_entitylist_webpagefordetailsview](#BKMK_mspp_entitylist_webpagefordetailsview)
- [mspp_systemuser_mspp_entitylist_createdby](#BKMK_mspp_systemuser_mspp_entitylist_createdby)
- [mspp_systemuser_mspp_entitylist_modifiedby](#BKMK_mspp_systemuser_mspp_entitylist_modifiedby)
- [mspp_website_entitylist](#BKMK_mspp_website_entitylist)


### <a name="BKMK_mspp_entitylist_webpageforcreate"></a> mspp_entitylist_webpageforcreate

See the [mspp_entitylist_webpageforcreate](mspp_webpage.md#BKMK_mspp_entitylist_webpageforcreate) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_entitylist_webpagefordetailsview"></a> mspp_entitylist_webpagefordetailsview

See the [mspp_entitylist_webpagefordetailsview](mspp_webpage.md#BKMK_mspp_entitylist_webpagefordetailsview) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_entitylist_createdby"></a> mspp_systemuser_mspp_entitylist_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_entitylist_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_entitylist_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_entitylist_modifiedby"></a> mspp_systemuser_mspp_entitylist_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_entitylist_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_entitylist_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_website_entitylist"></a> mspp_website_entitylist

See the [mspp_website_entitylist](mspp_website.md#BKMK_mspp_website_entitylist) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_entitylist?text=mspp_entitylist EntityType" />