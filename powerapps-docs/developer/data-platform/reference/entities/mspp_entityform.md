---
title: "Basic Form (mspp_entityform) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Basic Form (mspp_entityform) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Basic Form (mspp_entityform) table/entity reference (Microsoft Dataverse)

Defines the form to render for a given entity type.

## Messages

The following table lists the messages for the Basic Form (mspp_entityform) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_entityforms<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_entityforms(*mspp_entityformid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_entityforms(*mspp_entityformid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_entityforms<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_entityforms(*mspp_entityformid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_entityforms(*mspp_entityformid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Basic Form (mspp_entityform) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Basic Form (mspp_entityform) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Basic Form** |
| **DisplayCollectionName** | **Basic Forms** |
| **SchemaName** | `mspp_entityform` |
| **CollectionSchemaName** | `mspp_entityforms` |
| **EntitySetName** | `mspp_entityforms`|
| **LogicalName** | `mspp_entityform` |
| **LogicalCollectionName** | `mspp_entityforms` |
| **PrimaryIdAttribute** | `mspp_entityformid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_appendquerystring](#BKMK_mspp_appendquerystring)
- [mspp_associatecurrentportaluser](#BKMK_mspp_associatecurrentportaluser)
- [mspp_attachfile](#BKMK_mspp_attachfile)
- [mspp_attachfileaccept](#BKMK_mspp_attachfileaccept)
- [mspp_attachfileacceptextensions](#BKMK_mspp_attachfileacceptextensions)
- [mspp_attachfileallowmultiple](#BKMK_mspp_attachfileallowmultiple)
- [mspp_attachfilelabel](#BKMK_mspp_attachfilelabel)
- [mspp_attachfilemaxsize](#BKMK_mspp_attachfilemaxsize)
- [mspp_attachfilerequired](#BKMK_mspp_attachfilerequired)
- [mspp_attachfilerequirederrormessage](#BKMK_mspp_attachfilerequirederrormessage)
- [mspp_attachfilerestrictaccept](#BKMK_mspp_attachfilerestrictaccept)
- [mspp_attachfilesaveoption](#BKMK_mspp_attachfilesaveoption)
- [mspp_attachfilesizeerrormessage](#BKMK_mspp_attachfilesizeerrormessage)
- [mspp_attachfilestoragelocation](#BKMK_mspp_attachfilestoragelocation)
- [mspp_attachfiletypeerrormessage](#BKMK_mspp_attachfiletypeerrormessage)
- [mspp_autogeneratesteps](#BKMK_mspp_autogeneratesteps)
- [mspp_captcharequired](#BKMK_mspp_captcharequired)
- [mspp_containername](#BKMK_mspp_containername)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_entityformId](#BKMK_mspp_entityformId)
- [mspp_entityname](#BKMK_mspp_entityname)
- [mspp_entitypermissionsenabled](#BKMK_mspp_entitypermissionsenabled)
- [mspp_entitysourcetype](#BKMK_mspp_entitysourcetype)
- [mspp_forceallfieldsrequired](#BKMK_mspp_forceallfieldsrequired)
- [mspp_formname](#BKMK_mspp_formname)
- [mspp_geolocation_addresslinefieldname](#BKMK_mspp_geolocation_addresslinefieldname)
- [mspp_geolocation_cityfieldname](#BKMK_mspp_geolocation_cityfieldname)
- [mspp_geolocation_countryfieldname](#BKMK_mspp_geolocation_countryfieldname)
- [mspp_geolocation_countyfieldname](#BKMK_mspp_geolocation_countyfieldname)
- [mspp_geolocation_displaymap](#BKMK_mspp_geolocation_displaymap)
- [mspp_geolocation_enabled](#BKMK_mspp_geolocation_enabled)
- [mspp_geolocation_formattedaddressfieldname](#BKMK_mspp_geolocation_formattedaddressfieldname)
- [mspp_geolocation_latitudefieldname](#BKMK_mspp_geolocation_latitudefieldname)
- [mspp_geolocation_longitudefieldname](#BKMK_mspp_geolocation_longitudefieldname)
- [mspp_geolocation_maptype](#BKMK_mspp_geolocation_maptype)
- [mspp_geolocation_neighborhoodfieldname](#BKMK_mspp_geolocation_neighborhoodfieldname)
- [mspp_geolocation_postalcodefieldname](#BKMK_mspp_geolocation_postalcodefieldname)
- [mspp_geolocation_statefieldname](#BKMK_mspp_geolocation_statefieldname)
- [mspp_hideformonsuccess](#BKMK_mspp_hideformonsuccess)
- [mspp_instructions](#BKMK_mspp_instructions)
- [mspp_maximumnooffiles](#BKMK_mspp_maximumnooffiles)
- [mspp_mode](#BKMK_mspp_mode)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_nextbuttoncssclass](#BKMK_mspp_nextbuttoncssclass)
- [mspp_nextbuttontext](#BKMK_mspp_nextbuttontext)
- [mspp_onsuccess](#BKMK_mspp_onsuccess)
- [mspp_populatereferenceentitylookupfield](#BKMK_mspp_populatereferenceentitylookupfield)
- [mspp_portaluserlookupattributeisactivityparty](#BKMK_mspp_portaluserlookupattributeisactivityparty)
- [mspp_previousbuttoncssclass](#BKMK_mspp_previousbuttoncssclass)
- [mspp_previousbuttontext](#BKMK_mspp_previousbuttontext)
- [mspp_primarykeyname](#BKMK_mspp_primarykeyname)
- [mspp_provisionedlanguages](#BKMK_mspp_provisionedlanguages)
- [mspp_recommendedfieldsrequired](#BKMK_mspp_recommendedfieldsrequired)
- [mspp_recordidquerystringparametername](#BKMK_mspp_recordidquerystringparametername)
- [mspp_recordnotfoundmessage](#BKMK_mspp_recordnotfoundmessage)
- [mspp_recordsourceallowcreateonnull](#BKMK_mspp_recordsourceallowcreateonnull)
- [mspp_recordsourceentitylogicalname](#BKMK_mspp_recordsourceentitylogicalname)
- [mspp_recordsourcerelationshipname](#BKMK_mspp_recordsourcerelationshipname)
- [mspp_redirecturl](#BKMK_mspp_redirecturl)
- [mspp_redirecturlappendentityidquerystring](#BKMK_mspp_redirecturlappendentityidquerystring)
- [mspp_redirecturlcustomquerystring](#BKMK_mspp_redirecturlcustomquerystring)
- [mspp_redirecturlquerystringattribute](#BKMK_mspp_redirecturlquerystringattribute)
- [mspp_redirecturlquerystringattributeparamname](#BKMK_mspp_redirecturlquerystringattributeparamname)
- [mspp_redirecturlquerystringname](#BKMK_mspp_redirecturlquerystringname)
- [mspp_redirectwebpage](#BKMK_mspp_redirectwebpage)
- [mspp_referenceentitylogicalname](#BKMK_mspp_referenceentitylogicalname)
- [mspp_referenceentityprimarykeylogicalname](#BKMK_mspp_referenceentityprimarykeylogicalname)
- [mspp_referenceentityreadonlyformname](#BKMK_mspp_referenceentityreadonlyformname)
- [mspp_referenceentityrelationshipname](#BKMK_mspp_referenceentityrelationshipname)
- [mspp_referenceentityshowreadonlyform](#BKMK_mspp_referenceentityshowreadonlyform)
- [mspp_referenceentitysourcetype](#BKMK_mspp_referenceentitysourcetype)
- [mspp_referencequeryattributelogicalname](#BKMK_mspp_referencequeryattributelogicalname)
- [mspp_referencequerystringisprimarykey](#BKMK_mspp_referencequerystringisprimarykey)
- [mspp_referencequerystringname](#BKMK_mspp_referencequerystringname)
- [mspp_referencerecordsourcerelationshipname](#BKMK_mspp_referencerecordsourcerelationshipname)
- [mspp_referencetargetlookupattributelogicalname](#BKMK_mspp_referencetargetlookupattributelogicalname)
- [mspp_registerstartupscript](#BKMK_mspp_registerstartupscript)
- [mspp_renderwebresourcesinline](#BKMK_mspp_renderwebresourcesinline)
- [mspp_setentityreference](#BKMK_mspp_setentityreference)
- [mspp_settings](#BKMK_mspp_settings)
- [mspp_showcaptchaforauthenticatedusers](#BKMK_mspp_showcaptchaforauthenticatedusers)
- [mspp_showownerfields](#BKMK_mspp_showownerfields)
- [mspp_showunsupportedfields](#BKMK_mspp_showunsupportedfields)
- [mspp_storageaccountname](#BKMK_mspp_storageaccountname)
- [mspp_submitbuttonbusytext](#BKMK_mspp_submitbuttonbusytext)
- [mspp_submitbuttoncssclass](#BKMK_mspp_submitbuttoncssclass)
- [mspp_submitbuttontext](#BKMK_mspp_submitbuttontext)
- [mspp_successmessage](#BKMK_mspp_successmessage)
- [mspp_tabname](#BKMK_mspp_tabname)
- [mspp_targetentityportaluserlookupattribute](#BKMK_mspp_targetentityportaluserlookupattribute)
- [mspp_tooltipenabled](#BKMK_mspp_tooltipenabled)
- [mspp_validationgroup](#BKMK_mspp_validationgroup)
- [mspp_validationsummarycssclass](#BKMK_mspp_validationsummarycssclass)
- [mspp_validationsummaryheadertext](#BKMK_mspp_validationsummaryheadertext)
- [mspp_validationsummarylinksenabled](#BKMK_mspp_validationsummarylinksenabled)
- [mspp_validationsummarylinktext](#BKMK_mspp_validationsummarylinktext)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

### <a name="BKMK_mspp_appendquerystring"></a> mspp_appendquerystring

|Property|Value|
|---|---|
|Description||
|DisplayName|**Append Query String**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_appendquerystring`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_appendquerystring`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_associatecurrentportaluser"></a> mspp_associatecurrentportaluser

|Property|Value|
|---|---|
|Description||
|DisplayName|**Associate Current Portal User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_associatecurrentportaluser`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_associatecurrentportaluser`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_attachfile"></a> mspp_attachfile

|Property|Value|
|---|---|
|Description||
|DisplayName|**Attach File**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfile`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_attachfile`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_attachfileaccept"></a> mspp_attachfileaccept

|Property|Value|
|---|---|
|Description|**The accept attribute specifies the MIME types of files that the server accepts through file upload. To specify more than one value, separate the values with a comma (e.g. audio/\*,video/\*,image/\*).**|
|DisplayName|**Attach File MIME Type Accept**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfileaccept`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_mspp_attachfileacceptextensions"></a> mspp_attachfileacceptextensions

|Property|Value|
|---|---|
|Description|**The accept attribute specifies the extension types of files that the server accepts through file upload. To specify more than one value, separate the values with a comma (e.g. .docx,.pdf,.txt).**|
|DisplayName|**Attach File Extension Type Accept**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfileacceptextensions`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_mspp_attachfileallowmultiple"></a> mspp_attachfileallowmultiple

|Property|Value|
|---|---|
|Description||
|DisplayName|**Attach File Allow Multiple**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfileallowmultiple`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_attachfileallowmultiple`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_attachfilelabel"></a> mspp_attachfilelabel

|Property|Value|
|---|---|
|Description||
|DisplayName|**Attach File Label**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfilelabel`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_attachfilemaxsize"></a> mspp_attachfilemaxsize

|Property|Value|
|---|---|
|Description||
|DisplayName|**Maximum File Size**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfilemaxsize`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_attachfilerequired"></a> mspp_attachfilerequired

|Property|Value|
|---|---|
|Description||
|DisplayName|**Attach File Required**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfilerequired`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_attachfilerequired`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_attachfilerequirederrormessage"></a> mspp_attachfilerequirederrormessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Attach File Required Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfilerequirederrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_attachfilerestrictaccept"></a> mspp_attachfilerestrictaccept

|Property|Value|
|---|---|
|Description||
|DisplayName|**Restrict Files To Accepted Types**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfilerestrictaccept`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_attachfilerestrictaccept`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_attachfilesaveoption"></a> mspp_attachfilesaveoption

|Property|Value|
|---|---|
|Description||
|DisplayName|**Attach File Save Option**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfilesaveoption`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspp_entityform_mspp_attachfilesaveoption`|

#### mspp_attachfilesaveoption Choices/Options

|Value|Label|
|---|---|
|756150000|**Notes**|
|756150001|**Portal Comment**|

### <a name="BKMK_mspp_attachfilesizeerrormessage"></a> mspp_attachfilesizeerrormessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Attach File Size Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfilesizeerrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_attachfilestoragelocation"></a> mspp_attachfilestoragelocation

|Property|Value|
|---|---|
|Description||
|DisplayName|**Attach File Storage Location**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfilestoragelocation`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspp_entityform_mspp_attachfilestoragelocation`|

#### mspp_attachfilestoragelocation Choices/Options

|Value|Label|
|---|---|
|756150000|**Note Attachment**|
|756150001|**Azure Blob Storage**|

### <a name="BKMK_mspp_attachfiletypeerrormessage"></a> mspp_attachfiletypeerrormessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Attach File Type Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfiletypeerrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_autogeneratesteps"></a> mspp_autogeneratesteps

|Property|Value|
|---|---|
|Description||
|DisplayName|**Auto Generate Steps From Tabs**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_autogeneratesteps`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_autogeneratesteps`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_captcharequired"></a> mspp_captcharequired

|Property|Value|
|---|---|
|Description||
|DisplayName|**Captcha Required**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_captcharequired`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_captcharequired`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_containername"></a> mspp_containername

|Property|Value|
|---|---|
|Description||
|DisplayName|**Container Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_containername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_mspp_entityformId"></a> mspp_entityformId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Basic Form**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_entityformid`|
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
|Description|**Indicates whether or not the table permission provider will assert privileges.**|
|DisplayName|**Enable Table Permissions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entitypermissionsenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_entitypermissionsenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_entitysourcetype"></a> mspp_entitysourcetype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Table Source Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entitysourcetype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspp_entityform_mspp_entitysourcetype`|

#### mspp_entitysourcetype Choices/Options

|Value|Label|
|---|---|
|756150001|**Query String**|
|756150002|**Current Portal User**|
|756150003|**Record Associated to Current Portal User**|

### <a name="BKMK_mspp_forceallfieldsrequired"></a> mspp_forceallfieldsrequired

|Property|Value|
|---|---|
|Description||
|DisplayName|**Make All Fields Required**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_forceallfieldsrequired`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_forceallfieldsrequired`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_formname"></a> mspp_formname

|Property|Value|
|---|---|
|Description|**Shows the name of the entity form to render.**|
|DisplayName|**Form Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_formname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_geolocation_addresslinefieldname"></a> mspp_geolocation_addresslinefieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Address Line Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_addresslinefieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_geolocation_cityfieldname"></a> mspp_geolocation_cityfieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**City Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_cityfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_geolocation_countryfieldname"></a> mspp_geolocation_countryfieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Country/Region Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_countryfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_geolocation_countyfieldname"></a> mspp_geolocation_countyfieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**County Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_countyfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_geolocation_displaymap"></a> mspp_geolocation_displaymap

|Property|Value|
|---|---|
|Description||
|DisplayName|**Display Map**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_displaymap`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_geolocation_displaymap`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_geolocation_enabled"></a> mspp_geolocation_enabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_enabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_geolocation_enabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_geolocation_formattedaddressfieldname"></a> mspp_geolocation_formattedaddressfieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Formatted Address Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_formattedaddressfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_geolocation_latitudefieldname"></a> mspp_geolocation_latitudefieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Latitude Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_latitudefieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_geolocation_longitudefieldname"></a> mspp_geolocation_longitudefieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Longitude Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_longitudefieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_geolocation_maptype"></a> mspp_geolocation_maptype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Map Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_maptype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150000|
|GlobalChoiceName|`mspp_entityform_mspp_geolocation_maptype`|

#### mspp_geolocation_maptype Choices/Options

|Value|Label|
|---|---|
|756150000|**Bing**|
|756150001|**Google**|
|756150002|**Esri**|

### <a name="BKMK_mspp_geolocation_neighborhoodfieldname"></a> mspp_geolocation_neighborhoodfieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Neighborhood Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_neighborhoodfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_geolocation_postalcodefieldname"></a> mspp_geolocation_postalcodefieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Zip/Postal Code Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_postalcodefieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_geolocation_statefieldname"></a> mspp_geolocation_statefieldname

|Property|Value|
|---|---|
|Description||
|DisplayName|**State or Province Field Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocation_statefieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_hideformonsuccess"></a> mspp_hideformonsuccess

|Property|Value|
|---|---|
|Description||
|DisplayName|**Hide Form on Success**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_hideformonsuccess`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_hideformonsuccess`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_instructions"></a> mspp_instructions

|Property|Value|
|---|---|
|Description||
|DisplayName|**Instructions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_instructions`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_mspp_maximumnooffiles"></a> mspp_maximumnooffiles

|Property|Value|
|---|---|
|Description||
|DisplayName|**Maximum No Of Files**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_maximumnooffiles`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_mode"></a> mspp_mode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_mode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|100000000|
|GlobalChoiceName|`mspp_entityform_mspp_mode`|

#### mspp_mode Choices/Options

|Value|Label|
|---|---|
|100000000|**Insert**|
|100000001|**Edit**|
|100000002|**ReadOnly**|

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

### <a name="BKMK_mspp_nextbuttoncssclass"></a> mspp_nextbuttoncssclass

|Property|Value|
|---|---|
|Description||
|DisplayName|**Next Button CSS Class**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_nextbuttoncssclass`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_nextbuttontext"></a> mspp_nextbuttontext

|Property|Value|
|---|---|
|Description||
|DisplayName|**Next Button Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_nextbuttontext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_onsuccess"></a> mspp_onsuccess

|Property|Value|
|---|---|
|Description||
|DisplayName|**On Success**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_onsuccess`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150000|
|GlobalChoiceName|`mspp_entityform_mspp_onsuccess`|

#### mspp_onsuccess Choices/Options

|Value|Label|
|---|---|
|756150000|**Display Success Message**|
|756150001|**Redirect**|

### <a name="BKMK_mspp_populatereferenceentitylookupfield"></a> mspp_populatereferenceentitylookupfield

|Property|Value|
|---|---|
|Description||
|DisplayName|**Populate Table Reference Lookup Field**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_populatereferenceentitylookupfield`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_populatereferenceentitylookupfield`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_portaluserlookupattributeisactivityparty"></a> mspp_portaluserlookupattributeisactivityparty

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is Activity Party**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_portaluserlookupattributeisactivityparty`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_portaluserlookupattributeisactivityparty`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_previousbuttoncssclass"></a> mspp_previousbuttoncssclass

|Property|Value|
|---|---|
|Description||
|DisplayName|**Previous Button CSS Class**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_previousbuttoncssclass`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_previousbuttontext"></a> mspp_previousbuttontext

|Property|Value|
|---|---|
|Description||
|DisplayName|**Previous Button Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_previousbuttontext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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

### <a name="BKMK_mspp_recommendedfieldsrequired"></a> mspp_recommendedfieldsrequired

|Property|Value|
|---|---|
|Description||
|DisplayName|**Recommended Fields Required**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_recommendedfieldsrequired`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_recommendedfieldsrequired`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_recordidquerystringparametername"></a> mspp_recordidquerystringparametername

|Property|Value|
|---|---|
|Description||
|DisplayName|**Record ID Parameter Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_recordidquerystringparametername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_recordnotfoundmessage"></a> mspp_recordnotfoundmessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Record Not Found Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_recordnotfoundmessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_mspp_recordsourceallowcreateonnull"></a> mspp_recordsourceallowcreateonnull

|Property|Value|
|---|---|
|Description|**This flag, when set to "true," allows the user to create a record if the record doesn't already exist and the Record Source Type is "Record Associated with Current Portal User."**|
|DisplayName|**Allow Create If Null**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_recordsourceallowcreateonnull`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_recordsourceallowcreateonnull`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_recordsourceentitylogicalname"></a> mspp_recordsourceentitylogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Record Source Table Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_recordsourceentitylogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_recordsourcerelationshipname"></a> mspp_recordsourcerelationshipname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Relationship Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_recordsourcerelationshipname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_mspp_redirecturl"></a> mspp_redirecturl

|Property|Value|
|---|---|
|Description|**Shows the URL to redirect to.**|
|DisplayName|**Redirect URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_redirecturl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

### <a name="BKMK_mspp_redirecturlappendentityidquerystring"></a> mspp_redirecturlappendentityidquerystring

|Property|Value|
|---|---|
|Description||
|DisplayName|**Append Table ID To Query String**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_redirecturlappendentityidquerystring`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_redirecturlappendentityidquerystring`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_redirecturlcustomquerystring"></a> mspp_redirecturlcustomquerystring

|Property|Value|
|---|---|
|Description||
|DisplayName|**Custom Query String**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_redirecturlcustomquerystring`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

### <a name="BKMK_mspp_redirecturlquerystringattribute"></a> mspp_redirecturlquerystringattribute

|Property|Value|
|---|---|
|Description|**Add an attribute value as a query string value by specifying the logical name of the attribute to assign its value to the query string.**|
|DisplayName|**Attribute Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_redirecturlquerystringattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_redirecturlquerystringattributeparamname"></a> mspp_redirecturlquerystringattributeparamname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Query String Parameter Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_redirecturlquerystringattributeparamname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_redirecturlquerystringname"></a> mspp_redirecturlquerystringname

|Property|Value|
|---|---|
|Description|**The url to redirect to is dynamically retrieved from the query string using this parameter name**|
|DisplayName|**Redirect URL Query String Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_redirecturlquerystringname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_redirectwebpage"></a> mspp_redirectwebpage

|Property|Value|
|---|---|
|Description|**Web Page to redirect to.**|
|DisplayName|**Redirect Web Page**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_redirectwebpage`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webpage|

### <a name="BKMK_mspp_referenceentitylogicalname"></a> mspp_referenceentitylogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Reference Table name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referenceentitylogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_referenceentityprimarykeylogicalname"></a> mspp_referenceentityprimarykeylogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Reference Table Primary Key Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referenceentityprimarykeylogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_referenceentityreadonlyformname"></a> mspp_referenceentityreadonlyformname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Reference Entity ReadOnly Form Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referenceentityreadonlyformname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_referenceentityrelationshipname"></a> mspp_referenceentityrelationshipname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Reference Entity Relationship Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referenceentityrelationshipname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|150|

### <a name="BKMK_mspp_referenceentityshowreadonlyform"></a> mspp_referenceentityshowreadonlyform

|Property|Value|
|---|---|
|Description||
|DisplayName|**Show Reference Entity ReadOnly Form**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referenceentityshowreadonlyform`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_referenceentityshowreadonlyform`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_referenceentitysourcetype"></a> mspp_referenceentitysourcetype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Source Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referenceentitysourcetype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspp_entityform_mspp_referenceentitysourcetype`|

#### mspp_referenceentitysourcetype Choices/Options

|Value|Label|
|---|---|
|756150000|**Query String**|
|756150001|**Record Associated to Current Portal User**|

### <a name="BKMK_mspp_referencequeryattributelogicalname"></a> mspp_referencequeryattributelogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Reference Query Attribute Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referencequeryattributelogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_referencequerystringisprimarykey"></a> mspp_referencequerystringisprimarykey

|Property|Value|
|---|---|
|Description||
|DisplayName|**Reference Query String Is Primary Key**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referencequerystringisprimarykey`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_referencequerystringisprimarykey`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_referencequerystringname"></a> mspp_referencequerystringname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Reference Query String Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referencequerystringname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_referencerecordsourcerelationshipname"></a> mspp_referencerecordsourcerelationshipname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Record Source Relationship Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referencerecordsourcerelationshipname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_referencetargetlookupattributelogicalname"></a> mspp_referencetargetlookupattributelogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Reference Target Lookup Attribute Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referencetargetlookupattributelogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_registerstartupscript"></a> mspp_registerstartupscript

|Property|Value|
|---|---|
|Description||
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

### <a name="BKMK_mspp_renderwebresourcesinline"></a> mspp_renderwebresourcesinline

|Property|Value|
|---|---|
|Description||
|DisplayName|**Render Web Resources Inline**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_renderwebresourcesinline`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_renderwebresourcesinline`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_setentityreference"></a> mspp_setentityreference

|Property|Value|
|---|---|
|Description||
|DisplayName|**Set Table Reference**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_setentityreference`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_setentityreference`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_mspp_showcaptchaforauthenticatedusers"></a> mspp_showcaptchaforauthenticatedusers

|Property|Value|
|---|---|
|Description||
|DisplayName|**Show Captcha for Authenticated Users**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_showcaptchaforauthenticatedusers`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_showcaptchaforauthenticatedusers`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_showownerfields"></a> mspp_showownerfields

|Property|Value|
|---|---|
|Description||
|DisplayName|**Show Owner Fields**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_showownerfields`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_showownerfields`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_showunsupportedfields"></a> mspp_showunsupportedfields

|Property|Value|
|---|---|
|Description||
|DisplayName|**Show Unsupported Fields**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_showunsupportedfields`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_showunsupportedfields`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_storageaccountname"></a> mspp_storageaccountname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Storage Account Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_storageaccountname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_submitbuttonbusytext"></a> mspp_submitbuttonbusytext

|Property|Value|
|---|---|
|Description||
|DisplayName|**Submit Button Busy Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_submitbuttonbusytext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_submitbuttoncssclass"></a> mspp_submitbuttoncssclass

|Property|Value|
|---|---|
|Description||
|DisplayName|**Submit Button CSS Class**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_submitbuttoncssclass`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_submitbuttontext"></a> mspp_submitbuttontext

|Property|Value|
|---|---|
|Description||
|DisplayName|**Submit Button Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_submitbuttontext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_successmessage"></a> mspp_successmessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Success Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_successmessage`|
|RequiredLevel|Recommended|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_mspp_tabname"></a> mspp_tabname

|Property|Value|
|---|---|
|Description|**The name of the tab on an entity form to render.**|
|DisplayName|**Tab Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_tabname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_targetentityportaluserlookupattribute"></a> mspp_targetentityportaluserlookupattribute

|Property|Value|
|---|---|
|Description||
|DisplayName|**Portal User Lookup Column**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_targetentityportaluserlookupattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_tooltipenabled"></a> mspp_tooltipenabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**ToolTip Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_tooltipenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_tooltipenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_validationgroup"></a> mspp_validationgroup

|Property|Value|
|---|---|
|Description||
|DisplayName|**Validation Group**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_validationgroup`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_validationsummarycssclass"></a> mspp_validationsummarycssclass

|Property|Value|
|---|---|
|Description||
|DisplayName|**Validation Summary CSS Class**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_validationsummarycssclass`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_validationsummaryheadertext"></a> mspp_validationsummaryheadertext

|Property|Value|
|---|---|
|Description||
|DisplayName|**Validation Summary Header Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_validationsummaryheadertext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_validationsummarylinksenabled"></a> mspp_validationsummarylinksenabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Enable Validation Summary Links**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_validationsummarylinksenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entityform_mspp_validationsummarylinksenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_validationsummarylinktext"></a> mspp_validationsummarylinktext

|Property|Value|
|---|---|
|Description||
|DisplayName|**Validation Summary Link Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_validationsummarylinktext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website entity associated with this record.**|
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
|Description|**Status of the Basic Form**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_entityform_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Basic Form**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_entityform_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_entityform_redirectwebpage](#BKMK_mspp_entityform_redirectwebpage)
- [mspp_systemuser_mspp_entityform_createdby](#BKMK_mspp_systemuser_mspp_entityform_createdby)
- [mspp_systemuser_mspp_entityform_modifiedby](#BKMK_mspp_systemuser_mspp_entityform_modifiedby)
- [mspp_website_entityform](#BKMK_mspp_website_entityform)

### <a name="BKMK_mspp_entityform_redirectwebpage"></a> mspp_entityform_redirectwebpage

One-To-Many Relationship: [mspp_webpage mspp_entityform_redirectwebpage](mspp_webpage.md#BKMK_mspp_entityform_redirectwebpage)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_redirectwebpage`|
|ReferencingEntityNavigationPropertyName|`mspp_redirectwebpage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_entityform_createdby"></a> mspp_systemuser_mspp_entityform_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_entityform_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_entityform_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_entityform_modifiedby"></a> mspp_systemuser_mspp_entityform_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_entityform_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_entityform_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_entityform"></a> mspp_website_entityform

One-To-Many Relationship: [mspp_website mspp_website_entityform](mspp_website.md#BKMK_mspp_website_entityform)

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

- [mspp_entityform_entityformmetadata_entityformforcreate](#BKMK_mspp_entityform_entityformmetadata_entityformforcreate)
- [mspp_entityform_webformmetadata_entityformforcreate](#BKMK_mspp_entityform_webformmetadata_entityformforcreate)
- [mspp_entityformmetadata_entityform](#BKMK_mspp_entityformmetadata_entityform)
- [mspp_webpage_entityform](#BKMK_mspp_webpage_entityform)

### <a name="BKMK_mspp_entityform_entityformmetadata_entityformforcreate"></a> mspp_entityform_entityformmetadata_entityformforcreate

Many-To-One Relationship: [mspp_entityformmetadata mspp_entityform_entityformmetadata_entityformforcreate](mspp_entityformmetadata.md#BKMK_mspp_entityform_entityformmetadata_entityformforcreate)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_entityformmetadata`|
|ReferencingAttribute|`mspp_entityformforcreate`|
|ReferencedEntityNavigationPropertyName|`mspp_entityform_entityformmetadata_entityformforcreate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_entityform_webformmetadata_entityformforcreate"></a> mspp_entityform_webformmetadata_entityformforcreate

Many-To-One Relationship: [mspp_webformmetadata mspp_entityform_webformmetadata_entityformforcreate](mspp_webformmetadata.md#BKMK_mspp_entityform_webformmetadata_entityformforcreate)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webformmetadata`|
|ReferencingAttribute|`mspp_entityformforcreateinwebformmetadata`|
|ReferencedEntityNavigationPropertyName|`mspp_entityform_webformmetadata_entityformforcreate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_entityformmetadata_entityform"></a> mspp_entityformmetadata_entityform

Many-To-One Relationship: [mspp_entityformmetadata mspp_entityformmetadata_entityform](mspp_entityformmetadata.md#BKMK_mspp_entityformmetadata_entityform)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_entityformmetadata`|
|ReferencingAttribute|`mspp_entityform`|
|ReferencedEntityNavigationPropertyName|`mspp_entityformmetadata_entityform`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_entityform"></a> mspp_webpage_entityform

Many-To-One Relationship: [mspp_webpage mspp_webpage_entityform](mspp_webpage.md#BKMK_mspp_webpage_entityform)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_entityform`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_entityform`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_entityform?displayProperty=fullName>
