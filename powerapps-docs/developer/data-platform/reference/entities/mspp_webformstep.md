---
title: "Form Step (mspp_webformstep) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Form Step (mspp_webformstep) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Form Step (mspp_webformstep) table/entity reference (Microsoft Dataverse)

Defines the flow logic of the form's user experience such as steps and conditional branching.

## Messages

The following table lists the messages for the Form Step (mspp_webformstep) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_webformsteps<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_webformsteps(*mspp_webformstepid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_webformsteps(*mspp_webformstepid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_webformsteps<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_webformsteps(*mspp_webformstepid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_webformsteps(*mspp_webformstepid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Form Step (mspp_webformstep) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Form Step (mspp_webformstep) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Form Step** |
| **DisplayCollectionName** | **Form Steps** |
| **SchemaName** | `mspp_webformstep` |
| **CollectionSchemaName** | `mspp_webformsteps` |
| **EntitySetName** | `mspp_webformsteps`|
| **LogicalName** | `mspp_webformstep` |
| **LogicalCollectionName** | `mspp_webformsteps` |
| **PrimaryIdAttribute** | `mspp_webformstepid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_accept](#BKMK_mspp_accept)
- [mspp_allowmultiplefiles](#BKMK_mspp_allowmultiplefiles)
- [mspp_appendquerystring](#BKMK_mspp_appendquerystring)
- [mspp_associatecurrentportaluser](#BKMK_mspp_associatecurrentportaluser)
- [mspp_attachfile](#BKMK_mspp_attachfile)
- [mspp_attachfilelabel](#BKMK_mspp_attachfilelabel)
- [mspp_attachfilemaxsize](#BKMK_mspp_attachfilemaxsize)
- [mspp_attachfilerequired](#BKMK_mspp_attachfilerequired)
- [mspp_attachfilerequirederrormessage](#BKMK_mspp_attachfilerequirederrormessage)
- [mspp_attachfilerestrictaccept](#BKMK_mspp_attachfilerestrictaccept)
- [mspp_attachfilesizeerrormessage](#BKMK_mspp_attachfilesizeerrormessage)
- [mspp_attachfilestoragelocation](#BKMK_mspp_attachfilestoragelocation)
- [mspp_attachfiletypeerrormessage](#BKMK_mspp_attachfiletypeerrormessage)
- [mspp_autogeneratesteps](#BKMK_mspp_autogeneratesteps)
- [mspp_autonumberattributelogicalname](#BKMK_mspp_autonumberattributelogicalname)
- [mspp_autonumberdefinitionname](#BKMK_mspp_autonumberdefinitionname)
- [mspp_captcharequired](#BKMK_mspp_captcharequired)
- [mspp_condition](#BKMK_mspp_condition)
- [mspp_conditiondefaultnextstep](#BKMK_mspp_conditiondefaultnextstep)
- [mspp_containername](#BKMK_mspp_containername)
- [mspp_createautonumber](#BKMK_mspp_createautonumber)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_editexistingrecordpermitted](#BKMK_mspp_editexistingrecordpermitted)
- [mspp_editexpiredmessage](#BKMK_mspp_editexpiredmessage)
- [mspp_editexpiredstatecode](#BKMK_mspp_editexpiredstatecode)
- [mspp_editexpiredstatusreason](#BKMK_mspp_editexpiredstatusreason)
- [mspp_editnotpermittedmessage](#BKMK_mspp_editnotpermittedmessage)
- [mspp_entitypermissionsenabled](#BKMK_mspp_entitypermissionsenabled)
- [mspp_entitysourcestep](#BKMK_mspp_entitysourcestep)
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
- [mspp_loadeventkeyname](#BKMK_mspp_loadeventkeyname)
- [mspp_loguser](#BKMK_mspp_loguser)
- [mspp_maximumnooffiles](#BKMK_mspp_maximumnooffiles)
- [mspp_mode](#BKMK_mspp_mode)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_movepreviouseventkeyname](#BKMK_mspp_movepreviouseventkeyname)
- [mspp_movepreviouspermitted](#BKMK_mspp_movepreviouspermitted)
- [mspp_multiplerecordsperuserpermitted](#BKMK_mspp_multiplerecordsperuserpermitted)
- [mspp_name](#BKMK_mspp_name)
- [mspp_nextbuttoncssclass](#BKMK_mspp_nextbuttoncssclass)
- [mspp_nextbuttontext](#BKMK_mspp_nextbuttontext)
- [mspp_nextstep](#BKMK_mspp_nextstep)
- [mspp_populatereferenceentitylookupfield](#BKMK_mspp_populatereferenceentitylookupfield)
- [mspp_portaluserlookupattributeisactivityparty](#BKMK_mspp_portaluserlookupattributeisactivityparty)
- [mspp_postbackurl](#BKMK_mspp_postbackurl)
- [mspp_previousbuttoncssclass](#BKMK_mspp_previousbuttoncssclass)
- [mspp_previousbuttontext](#BKMK_mspp_previousbuttontext)
- [mspp_previousstep](#BKMK_mspp_previousstep)
- [mspp_primarykeyattributelogicalname](#BKMK_mspp_primarykeyattributelogicalname)
- [mspp_primarykeyquerystringparametername](#BKMK_mspp_primarykeyquerystringparametername)
- [mspp_provisionedlanguages](#BKMK_mspp_provisionedlanguages)
- [mspp_recommendedfieldsrequired](#BKMK_mspp_recommendedfieldsrequired)
- [mspp_recordnotfoundmessage](#BKMK_mspp_recordnotfoundmessage)
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
- [mspp_referenceentitystep](#BKMK_mspp_referenceentitystep)
- [mspp_referencequeryattributelogicalname](#BKMK_mspp_referencequeryattributelogicalname)
- [mspp_referencequerystringisprimarykey](#BKMK_mspp_referencequerystringisprimarykey)
- [mspp_referencequerystringname](#BKMK_mspp_referencequerystringname)
- [mspp_referencerecordsourcerelationshipname](#BKMK_mspp_referencerecordsourcerelationshipname)
- [mspp_referencesourceentitylogicalname](#BKMK_mspp_referencesourceentitylogicalname)
- [mspp_referencetargetlookupattributelogicalname](#BKMK_mspp_referencetargetlookupattributelogicalname)
- [mspp_registerstartupscript](#BKMK_mspp_registerstartupscript)
- [mspp_renderwebresourcesinline](#BKMK_mspp_renderwebresourcesinline)
- [mspp_savedeventkeyname](#BKMK_mspp_savedeventkeyname)
- [mspp_savingeventkeyname](#BKMK_mspp_savingeventkeyname)
- [mspp_setentityreference](#BKMK_mspp_setentityreference)
- [mspp_settings](#BKMK_mspp_settings)
- [mspp_showcaptchaforauthenticatedusers](#BKMK_mspp_showcaptchaforauthenticatedusers)
- [mspp_showownerfields](#BKMK_mspp_showownerfields)
- [mspp_showunsupportedfields](#BKMK_mspp_showunsupportedfields)
- [mspp_storageaccountname](#BKMK_mspp_storageaccountname)
- [mspp_submitbuttonbusytext](#BKMK_mspp_submitbuttonbusytext)
- [mspp_submitbuttoncssclass](#BKMK_mspp_submitbuttoncssclass)
- [mspp_submitbuttontext](#BKMK_mspp_submitbuttontext)
- [mspp_submiteventkeyname](#BKMK_mspp_submiteventkeyname)
- [mspp_successmessage](#BKMK_mspp_successmessage)
- [mspp_tabname](#BKMK_mspp_tabname)
- [mspp_targetentitylogicalname](#BKMK_mspp_targetentitylogicalname)
- [mspp_targetentityportaluserlookupattribute](#BKMK_mspp_targetentityportaluserlookupattribute)
- [mspp_targetentityprimarykeylogicalname](#BKMK_mspp_targetentityprimarykeylogicalname)
- [mspp_title](#BKMK_mspp_title)
- [mspp_tooltipenabled](#BKMK_mspp_tooltipenabled)
- [mspp_type](#BKMK_mspp_type)
- [mspp_usercontrolpath](#BKMK_mspp_usercontrolpath)
- [mspp_usercontroltitle](#BKMK_mspp_usercontroltitle)
- [mspp_userhostaddressattributelogicalname](#BKMK_mspp_userhostaddressattributelogicalname)
- [mspp_useridentitynameattributelogicalname](#BKMK_mspp_useridentitynameattributelogicalname)
- [mspp_validationgroup](#BKMK_mspp_validationgroup)
- [mspp_validationsummarycssclass](#BKMK_mspp_validationsummarycssclass)
- [mspp_validationsummaryheadertext](#BKMK_mspp_validationsummaryheadertext)
- [mspp_validationsummarylinksenabled](#BKMK_mspp_validationsummarylinksenabled)
- [mspp_validationsummarylinktext](#BKMK_mspp_validationsummarylinktext)
- [mspp_webform](#BKMK_mspp_webform)
- [mspp_webformstepId](#BKMK_mspp_webformstepId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

### <a name="BKMK_mspp_accept"></a> mspp_accept

|Property|Value|
|---|---|
|Description|**The accept attribute specifies the MIME types of files that the server accepts through file upload. To specify more than one value, separate the values with a comma (e.g. audio/\*,video/\*,image/\*).**|
|DisplayName|**Accept**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_accept`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_allowmultiplefiles"></a> mspp_allowmultiplefiles

|Property|Value|
|---|---|
|Description||
|DisplayName|**Allow Multiple Files**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_allowmultiplefiles`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformstep_mspp_allowmultiplefiles`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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
|GlobalChoiceName|`mspp_webformstep_mspp_appendquerystring`|
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
|GlobalChoiceName|`mspp_webformstep_mspp_associatecurrentportaluser`|
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
|GlobalChoiceName|`mspp_webformstep_mspp_attachfile`|
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
|DisplayName|**Attach File Maximum Size**|
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
|GlobalChoiceName|`mspp_webformstep_mspp_attachfilerequired`|
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
|DisplayName|**Attach File Restrict Accept**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attachfilerestrictaccept`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformstep_mspp_attachfilerestrictaccept`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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
|GlobalChoiceName|`mspp_webformstep_mspp_attachfilestoragelocation`|

#### mspp_attachfilestoragelocation Choices/Options

|Value|Label|
|---|---|
|756150000|**Note Document**|
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
|GlobalChoiceName|`mspp_webformstep_mspp_autogeneratesteps`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_autonumberattributelogicalname"></a> mspp_autonumberattributelogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Auto Number Attribute Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_autonumberattributelogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_autonumberdefinitionname"></a> mspp_autonumberdefinitionname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Auto Number Definition Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_autonumberdefinitionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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
|GlobalChoiceName|`mspp_webformstep_mspp_captcharequired`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_condition"></a> mspp_condition

|Property|Value|
|---|---|
|Description||
|DisplayName|**Condition**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_condition`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_conditiondefaultnextstep"></a> mspp_conditiondefaultnextstep

|Property|Value|
|---|---|
|Description|**If the condition test fails, this is the next step.**|
|DisplayName|**Condition Default Next Step**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_conditiondefaultnextstep`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webformstep|

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

### <a name="BKMK_mspp_createautonumber"></a> mspp_createautonumber

|Property|Value|
|---|---|
|Description||
|DisplayName|**Create Auto Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createautonumber`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformstep_mspp_createautonumber`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_mspp_editexistingrecordpermitted"></a> mspp_editexistingrecordpermitted

|Property|Value|
|---|---|
|Description||
|DisplayName|**Edit Existing Record Permitted**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_editexistingrecordpermitted`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformstep_mspp_editexistingrecordpermitted`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_editexpiredmessage"></a> mspp_editexpiredmessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Edit Expired Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_editexpiredmessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_mspp_editexpiredstatecode"></a> mspp_editexpiredstatecode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Edit Expired State Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_editexpiredstatecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_editexpiredstatusreason"></a> mspp_editexpiredstatusreason

|Property|Value|
|---|---|
|Description||
|DisplayName|**Edit Expired Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_editexpiredstatusreason`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_editnotpermittedmessage"></a> mspp_editnotpermittedmessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Edit Not Permitted Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_editnotpermittedmessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_mspp_entitypermissionsenabled"></a> mspp_entitypermissionsenabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Enable Table Permissions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entitypermissionsenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformstep_mspp_entitypermissionsenabled`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_entitysourcestep"></a> mspp_entitysourcestep

|Property|Value|
|---|---|
|Description|**Unique identifier for Form Step associated with Form Step.**|
|DisplayName|**Entity Source Step**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entitysourcestep`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webformstep|

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
|GlobalChoiceName|`mspp_webformstep_mspp_entitysourcetype`|

#### mspp_entitysourcetype Choices/Options

|Value|Label|
|---|---|
|100000001|**Query String**|
|100000002|**Current Portal User**|
|100000003|**Result From Previous Step**|
|100000004|**Record Associated to Current Portal User**|

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
|GlobalChoiceName|`mspp_webformstep_mspp_forceallfieldsrequired`|
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
|RequiredLevel|None|
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
|GlobalChoiceName|`mspp_webformstep_mspp_geolocation_displaymap`|
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
|GlobalChoiceName|`mspp_webformstep_mspp_geolocation_enabled`|
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
|GlobalChoiceName|`mspp_webformstep_mspp_geolocation_maptype`|

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
|GlobalChoiceName|`mspp_webformstep_mspp_hideformonsuccess`|
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

### <a name="BKMK_mspp_loadeventkeyname"></a> mspp_loadeventkeyname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Load Event Key Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_loadeventkeyname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_mspp_loguser"></a> mspp_loguser

|Property|Value|
|---|---|
|Description||
|DisplayName|**Log User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_loguser`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformstep_mspp_loguser`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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
|GlobalChoiceName|`mspp_webformstep_mspp_mode`|

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

### <a name="BKMK_mspp_movepreviouseventkeyname"></a> mspp_movepreviouseventkeyname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Move Previous Event Key Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_movepreviouseventkeyname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_mspp_movepreviouspermitted"></a> mspp_movepreviouspermitted

|Property|Value|
|---|---|
|Description||
|DisplayName|**Move Previous Permitted**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_movepreviouspermitted`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformstep_mspp_movepreviouspermitted`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_multiplerecordsperuserpermitted"></a> mspp_multiplerecordsperuserpermitted

|Property|Value|
|---|---|
|Description||
|DisplayName|**Multiple Records Per User Permitted**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_multiplerecordsperuserpermitted`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformstep_mspp_multiplerecordsperuserpermitted`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_mspp_nextstep"></a> mspp_nextstep

|Property|Value|
|---|---|
|Description|**Pointer to the next step.**|
|DisplayName|**Next Step**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_nextstep`|
|RequiredLevel|Recommended|
|Type|Lookup|
|Targets|mspp_webformstep|

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
|GlobalChoiceName|`mspp_webformstep_mspp_populatereferenceentitylookupfield`|
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
|GlobalChoiceName|`mspp_webformstep_mspp_portaluserlookupattributeisactivityparty`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_postbackurl"></a> mspp_postbackurl

|Property|Value|
|---|---|
|Description||
|DisplayName|**Post Back URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_postbackurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

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

### <a name="BKMK_mspp_previousstep"></a> mspp_previousstep

|Property|Value|
|---|---|
|Description|**Pointer to the previous step.**|
|DisplayName|**Previous Step**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_previousstep`|
|RequiredLevel|Recommended|
|Type|Lookup|
|Targets|mspp_webformstep|

### <a name="BKMK_mspp_primarykeyattributelogicalname"></a> mspp_primarykeyattributelogicalname

|Property|Value|
|---|---|
|Description|**The logical name of the primary key attribute of the target entity.**|
|DisplayName|**Primary Key Attribute Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_primarykeyattributelogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_primarykeyquerystringparametername"></a> mspp_primarykeyquerystringparametername

|Property|Value|
|---|---|
|Description||
|DisplayName|**Primary Key Query String Parameter Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_primarykeyquerystringparametername`|
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
|GlobalChoiceName|`mspp_webformstep_mspp_recommendedfieldsrequired`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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
|MaxLength|100|

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
|GlobalChoiceName|`mspp_webformstep_mspp_redirecturlappendentityidquerystring`|
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
|GlobalChoiceName|`mspp_webformstep_mspp_referenceentityshowreadonlyform`|
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
|DefaultFormValue|100000001|
|GlobalChoiceName|`mspp_webformstep_mspp_referenceentitysourcetype`|

#### mspp_referenceentitysourcetype Choices/Options

|Value|Label|
|---|---|
|100000000|**Query String**|
|100000001|**Previous Step**|
|100000002|**Record Associated to Current Portal User**|

### <a name="BKMK_mspp_referenceentitystep"></a> mspp_referenceentitystep

|Property|Value|
|---|---|
|Description|**Unique identifier for Form Step associated with Form Step.**|
|DisplayName|**Reference Entity Step**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referenceentitystep`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webformstep|

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
|GlobalChoiceName|`mspp_webformstep_mspp_referencequerystringisprimarykey`|
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

### <a name="BKMK_mspp_referencesourceentitylogicalname"></a> mspp_referencesourceentitylogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Reference Source Table name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_referencesourceentitylogicalname`|
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
|Description|**Shows your custom JavaScript that will be placed at the bottom of the page right before the closing </form> element.**|
|DisplayName|**Custom JavaScript**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_registerstartupscript`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
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
|GlobalChoiceName|`mspp_webformstep_mspp_renderwebresourcesinline`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_savedeventkeyname"></a> mspp_savedeventkeyname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Saved Event Key Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_savedeventkeyname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_mspp_savingeventkeyname"></a> mspp_savingeventkeyname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Saving Event Key Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_savingeventkeyname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

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
|GlobalChoiceName|`mspp_webformstep_mspp_setentityreference`|
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
|DisplayName|**Show Captcha for authenticated users**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_showcaptchaforauthenticatedusers`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformstep_mspp_showcaptchaforauthenticatedusers`|
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
|GlobalChoiceName|`mspp_webformstep_mspp_showownerfields`|
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
|GlobalChoiceName|`mspp_webformstep_mspp_showunsupportedfields`|
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

### <a name="BKMK_mspp_submiteventkeyname"></a> mspp_submiteventkeyname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Submit Event Key Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_submiteventkeyname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

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

### <a name="BKMK_mspp_targetentitylogicalname"></a> mspp_targetentitylogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Target Table name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_targetentitylogicalname`|
|RequiredLevel|Recommended|
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

### <a name="BKMK_mspp_targetentityprimarykeylogicalname"></a> mspp_targetentityprimarykeylogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Target Entity Primary Key Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_targetentityprimarykeylogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_title"></a> mspp_title

|Property|Value|
|---|---|
|Description||
|DisplayName|**Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_title`|
|RequiredLevel|Recommended|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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
|GlobalChoiceName|`mspp_webformstep_mspp_tooltipenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_type"></a> mspp_type

|Property|Value|
|---|---|
|Description||
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_type`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|100000001|
|GlobalChoiceName|`mspp_webformstep_mspp_type`|

#### mspp_type Choices/Options

|Value|Label|
|---|---|
|100000000|**Condition**|
|100000001|**Load Form**|
|100000002|**Load Tab**|
|100000003|**Redirect**|
|100000004|**Load User Control**|

### <a name="BKMK_mspp_usercontrolpath"></a> mspp_usercontrolpath

|Property|Value|
|---|---|
|Description||
|DisplayName|**User Control Path**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_usercontrolpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_mspp_usercontroltitle"></a> mspp_usercontroltitle

|Property|Value|
|---|---|
|Description||
|DisplayName|**User Control Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_usercontroltitle`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_userhostaddressattributelogicalname"></a> mspp_userhostaddressattributelogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**User Host Address Attribute Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_userhostaddressattributelogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_useridentitynameattributelogicalname"></a> mspp_useridentitynameattributelogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**User Identity Name Attribute Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_useridentitynameattributelogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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
|GlobalChoiceName|`mspp_webformstep_mspp_validationsummarylinksenabled`|
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

### <a name="BKMK_mspp_webform"></a> mspp_webform

|Property|Value|
|---|---|
|Description|**Unique identifier for Multistep Form associated with Form Step.**|
|DisplayName|**Multistep Form**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webform`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_webform|

### <a name="BKMK_mspp_webformstepId"></a> mspp_webformstepId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Form Step**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_webformstepid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Form Step**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webformstep_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Form Step**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webformstep_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_systemuser_mspp_webformstep_createdby](#BKMK_mspp_systemuser_mspp_webformstep_createdby)
- [mspp_systemuser_mspp_webformstep_modifiedby](#BKMK_mspp_systemuser_mspp_webformstep_modifiedby)
- [mspp_webformstep_conditiondefaultnextstep](#BKMK_mspp_webformstep_conditiondefaultnextstep-many-to-one)
- [mspp_webformstep_entitysourcestep](#BKMK_mspp_webformstep_entitysourcestep-many-to-one)
- [mspp_webformstep_nextstep](#BKMK_mspp_webformstep_nextstep-many-to-one)
- [mspp_webformstep_previousstep](#BKMK_mspp_webformstep_previousstep-many-to-one)
- [mspp_webformstep_redirectwebpage](#BKMK_mspp_webformstep_redirectwebpage)
- [mspp_webformstep_referenceentitystep](#BKMK_mspp_webformstep_referenceentitystep-many-to-one)
- [mspp_webformstep_webform](#BKMK_mspp_webformstep_webform)

### <a name="BKMK_mspp_systemuser_mspp_webformstep_createdby"></a> mspp_systemuser_mspp_webformstep_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webformstep_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webformstep_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_webformstep_modifiedby"></a> mspp_systemuser_mspp_webformstep_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webformstep_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webformstep_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webformstep_conditiondefaultnextstep-many-to-one"></a> mspp_webformstep_conditiondefaultnextstep

One-To-Many Relationship: [mspp_webformstep mspp_webformstep_conditiondefaultnextstep](#BKMK_mspp_webformstep_conditiondefaultnextstep-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webformstep`|
|ReferencedAttribute|`mspp_webformstepid`|
|ReferencingAttribute|`mspp_conditiondefaultnextstep`|
|ReferencingEntityNavigationPropertyName|`mspp_conditiondefaultnextstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webformstep_entitysourcestep-many-to-one"></a> mspp_webformstep_entitysourcestep

One-To-Many Relationship: [mspp_webformstep mspp_webformstep_entitysourcestep](#BKMK_mspp_webformstep_entitysourcestep-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webformstep`|
|ReferencedAttribute|`mspp_webformstepid`|
|ReferencingAttribute|`mspp_entitysourcestep`|
|ReferencingEntityNavigationPropertyName|`mspp_entitysourcestep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webformstep_nextstep-many-to-one"></a> mspp_webformstep_nextstep

One-To-Many Relationship: [mspp_webformstep mspp_webformstep_nextstep](#BKMK_mspp_webformstep_nextstep-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webformstep`|
|ReferencedAttribute|`mspp_webformstepid`|
|ReferencingAttribute|`mspp_nextstep`|
|ReferencingEntityNavigationPropertyName|`mspp_nextstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webformstep_previousstep-many-to-one"></a> mspp_webformstep_previousstep

One-To-Many Relationship: [mspp_webformstep mspp_webformstep_previousstep](#BKMK_mspp_webformstep_previousstep-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webformstep`|
|ReferencedAttribute|`mspp_webformstepid`|
|ReferencingAttribute|`mspp_previousstep`|
|ReferencingEntityNavigationPropertyName|`mspp_previousstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webformstep_redirectwebpage"></a> mspp_webformstep_redirectwebpage

One-To-Many Relationship: [mspp_webpage mspp_webformstep_redirectwebpage](mspp_webpage.md#BKMK_mspp_webformstep_redirectwebpage)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_redirectwebpage`|
|ReferencingEntityNavigationPropertyName|`mspp_redirectwebpage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webformstep_referenceentitystep-many-to-one"></a> mspp_webformstep_referenceentitystep

One-To-Many Relationship: [mspp_webformstep mspp_webformstep_referenceentitystep](#BKMK_mspp_webformstep_referenceentitystep-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webformstep`|
|ReferencedAttribute|`mspp_webformstepid`|
|ReferencingAttribute|`mspp_referenceentitystep`|
|ReferencingEntityNavigationPropertyName|`mspp_referenceentitystep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webformstep_webform"></a> mspp_webformstep_webform

One-To-Many Relationship: [mspp_webform mspp_webformstep_webform](mspp_webform.md#BKMK_mspp_webformstep_webform)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webform`|
|ReferencedAttribute|`mspp_webformid`|
|ReferencingAttribute|`mspp_webform`|
|ReferencingEntityNavigationPropertyName|`mspp_webform`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [mspp_webform_startstep](#BKMK_mspp_webform_startstep)
- [mspp_webformmetadata_webformstep](#BKMK_mspp_webformmetadata_webformstep)
- [mspp_webformstep_conditiondefaultnextstep](#BKMK_mspp_webformstep_conditiondefaultnextstep-one-to-many)
- [mspp_webformstep_entitysourcestep](#BKMK_mspp_webformstep_entitysourcestep-one-to-many)
- [mspp_webformstep_nextstep](#BKMK_mspp_webformstep_nextstep-one-to-many)
- [mspp_webformstep_previousstep](#BKMK_mspp_webformstep_previousstep-one-to-many)
- [mspp_webformstep_referenceentitystep](#BKMK_mspp_webformstep_referenceentitystep-one-to-many)

### <a name="BKMK_mspp_webform_startstep"></a> mspp_webform_startstep

Many-To-One Relationship: [mspp_webform mspp_webform_startstep](mspp_webform.md#BKMK_mspp_webform_startstep)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webform`|
|ReferencingAttribute|`mspp_startstep`|
|ReferencedEntityNavigationPropertyName|`mspp_webform_startstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webformmetadata_webformstep"></a> mspp_webformmetadata_webformstep

Many-To-One Relationship: [mspp_webformmetadata mspp_webformmetadata_webformstep](mspp_webformmetadata.md#BKMK_mspp_webformmetadata_webformstep)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webformmetadata`|
|ReferencingAttribute|`mspp_webformstep`|
|ReferencedEntityNavigationPropertyName|`mspp_webformmetadata_webformstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Metadata<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webformstep_conditiondefaultnextstep-one-to-many"></a> mspp_webformstep_conditiondefaultnextstep

Many-To-One Relationship: [mspp_webformstep mspp_webformstep_conditiondefaultnextstep](#BKMK_mspp_webformstep_conditiondefaultnextstep-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webformstep`|
|ReferencingAttribute|`mspp_conditiondefaultnextstep`|
|ReferencedEntityNavigationPropertyName|`mspp_webformstep_conditiondefaultnextstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webformstep_entitysourcestep-one-to-many"></a> mspp_webformstep_entitysourcestep

Many-To-One Relationship: [mspp_webformstep mspp_webformstep_entitysourcestep](#BKMK_mspp_webformstep_entitysourcestep-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webformstep`|
|ReferencingAttribute|`mspp_entitysourcestep`|
|ReferencedEntityNavigationPropertyName|`mspp_webformstep_entitysourcestep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Entity Source Steps<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webformstep_nextstep-one-to-many"></a> mspp_webformstep_nextstep

Many-To-One Relationship: [mspp_webformstep mspp_webformstep_nextstep](#BKMK_mspp_webformstep_nextstep-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webformstep`|
|ReferencingAttribute|`mspp_nextstep`|
|ReferencedEntityNavigationPropertyName|`mspp_webformstep_nextstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webformstep_previousstep-one-to-many"></a> mspp_webformstep_previousstep

Many-To-One Relationship: [mspp_webformstep mspp_webformstep_previousstep](#BKMK_mspp_webformstep_previousstep-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webformstep`|
|ReferencingAttribute|`mspp_previousstep`|
|ReferencedEntityNavigationPropertyName|`mspp_webformstep_previousstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webformstep_referenceentitystep-one-to-many"></a> mspp_webformstep_referenceentitystep

Many-To-One Relationship: [mspp_webformstep mspp_webformstep_referenceentitystep](#BKMK_mspp_webformstep_referenceentitystep-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webformstep`|
|ReferencingAttribute|`mspp_referenceentitystep`|
|ReferencedEntityNavigationPropertyName|`mspp_webformstep_referenceentitystep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Reference Entity Steps<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_webformstep?displayProperty=fullName>
