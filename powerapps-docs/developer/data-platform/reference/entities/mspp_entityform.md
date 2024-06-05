---
title: "Basic Form (mspp_entityform)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Basic Form (mspp_entityform)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Basic Form (mspp_entityform)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Defines the form to render for a given entity type.

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_entityforms<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_entityforms(*mspp_entityformid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_entityforms(*mspp_entityformid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_entityforms<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_entityforms(*mspp_entityformid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_entityforms|
|DisplayCollectionName|Basic Forms|
|DisplayName|Basic Form|
|EntitySetName|mspp_entityforms|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_entityforms|
|LogicalName|mspp_entityform|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_entityformid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_entityform|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description||
|DisplayName|Append Query String|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_appendquerystring|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_appendquerystring Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_associatecurrentportaluser"></a> mspp_associatecurrentportaluser

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Associate Current Portal User|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_associatecurrentportaluser|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_associatecurrentportaluser Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_attachfile"></a> mspp_attachfile

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Attach File|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfile|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_attachfile Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_attachfileaccept"></a> mspp_attachfileaccept

|Property|Value|
|--------|-----|
|Description|The accept attribute specifies the MIME types of files that the server accepts through file upload. To specify more than one value, separate the values with a comma (e.g. audio/*,video/*,image/*).|
|DisplayName|Attach File MIME Type Accept|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfileaccept|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_attachfileacceptextensions"></a> mspp_attachfileacceptextensions

|Property|Value|
|--------|-----|
|Description|The accept attribute specifies the extension types of files that the server accepts through file upload. To specify more than one value, separate the values with a comma (e.g. .docx,.pdf,.txt).|
|DisplayName|Attach File Extension Type Accept|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfileacceptextensions|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_attachfileallowmultiple"></a> mspp_attachfileallowmultiple

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Attach File Allow Multiple|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfileallowmultiple|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_attachfileallowmultiple Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_attachfilelabel"></a> mspp_attachfilelabel

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Attach File Label|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfilelabel|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_attachfilemaxsize"></a> mspp_attachfilemaxsize

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Maximum File Size|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfilemaxsize|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_attachfilerequired"></a> mspp_attachfilerequired

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Attach File Required|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfilerequired|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_attachfilerequired Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_attachfilerequirederrormessage"></a> mspp_attachfilerequirederrormessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Attach File Required Error Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfilerequirederrormessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_attachfilerestrictaccept"></a> mspp_attachfilerestrictaccept

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Restrict Files To Accepted Types|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfilerestrictaccept|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_attachfilerestrictaccept Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_attachfilesaveoption"></a> mspp_attachfilesaveoption

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Attach File Save Option|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfilesaveoption|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_attachfilesaveoption Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Notes||
|756150001|Portal Comment||



### <a name="BKMK_mspp_attachfilesizeerrormessage"></a> mspp_attachfilesizeerrormessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Attach File Size Error Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfilesizeerrormessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_attachfilestoragelocation"></a> mspp_attachfilestoragelocation

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Attach File Storage Location|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfilestoragelocation|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_attachfilestoragelocation Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Note Attachment||
|756150001|Azure Blob Storage||



### <a name="BKMK_mspp_attachfiletypeerrormessage"></a> mspp_attachfiletypeerrormessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Attach File Type Error Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attachfiletypeerrormessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_autogeneratesteps"></a> mspp_autogeneratesteps

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Auto Generate Steps From Tabs|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_autogeneratesteps|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_autogeneratesteps Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_captcharequired"></a> mspp_captcharequired

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Captcha Required|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_captcharequired|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_captcharequired Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_containername"></a> mspp_containername

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Container Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_containername|
|MaxLength|100|
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


### <a name="BKMK_mspp_entityformId"></a> mspp_entityformId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Basic Form|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_entityformid|
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
|Description|Indicates whether or not the table permission provider will assert privileges.|
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



### <a name="BKMK_mspp_entitysourcetype"></a> mspp_entitysourcetype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Table Source Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_entitysourcetype|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_entitysourcetype Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150001|Query String||
|756150002|Current Portal User||
|756150003|Record Associated to Current Portal User||



### <a name="BKMK_mspp_forceallfieldsrequired"></a> mspp_forceallfieldsrequired

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Make All Fields Required|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_forceallfieldsrequired|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_forceallfieldsrequired Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_formname"></a> mspp_formname

|Property|Value|
|--------|-----|
|Description|Shows the name of the entity form to render.|
|DisplayName|Form Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_formname|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_geolocation_addresslinefieldname"></a> mspp_geolocation_addresslinefieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Address Line Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_addresslinefieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_geolocation_cityfieldname"></a> mspp_geolocation_cityfieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|City Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_cityfieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_geolocation_countryfieldname"></a> mspp_geolocation_countryfieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Country/Region Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_countryfieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_geolocation_countyfieldname"></a> mspp_geolocation_countyfieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|County Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_countyfieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_geolocation_displaymap"></a> mspp_geolocation_displaymap

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Display Map|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_displaymap|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_geolocation_displaymap Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_geolocation_enabled"></a> mspp_geolocation_enabled

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Enabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_enabled|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_geolocation_enabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_geolocation_formattedaddressfieldname"></a> mspp_geolocation_formattedaddressfieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Formatted Address Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_formattedaddressfieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_geolocation_latitudefieldname"></a> mspp_geolocation_latitudefieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Latitude Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_latitudefieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_geolocation_longitudefieldname"></a> mspp_geolocation_longitudefieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Longitude Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_longitudefieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_geolocation_maptype"></a> mspp_geolocation_maptype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Map Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_maptype|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_geolocation_maptype Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Bing||
|756150001|Google||
|756150002|Esri||



### <a name="BKMK_mspp_geolocation_neighborhoodfieldname"></a> mspp_geolocation_neighborhoodfieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Neighborhood Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_neighborhoodfieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_geolocation_postalcodefieldname"></a> mspp_geolocation_postalcodefieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Zip/Postal Code Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_postalcodefieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_geolocation_statefieldname"></a> mspp_geolocation_statefieldname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|State or Province Field Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocation_statefieldname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_hideformonsuccess"></a> mspp_hideformonsuccess

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Hide Form on Success|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_hideformonsuccess|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_hideformonsuccess Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_mspp_instructions"></a> mspp_instructions

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Instructions|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_instructions|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_maximumnooffiles"></a> mspp_maximumnooffiles

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Maximum No Of Files|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_maximumnooffiles|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_mode"></a> mspp_mode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Mode|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_mode|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_mode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|100000000|Insert||
|100000001|Edit||
|100000002|ReadOnly||



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


### <a name="BKMK_mspp_nextbuttoncssclass"></a> mspp_nextbuttoncssclass

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Next Button CSS Class|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_nextbuttoncssclass|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_nextbuttontext"></a> mspp_nextbuttontext

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Next Button Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_nextbuttontext|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_onsuccess"></a> mspp_onsuccess

|Property|Value|
|--------|-----|
|Description||
|DisplayName|On Success|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_onsuccess|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_onsuccess Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Display Success Message||
|756150001|Redirect||



### <a name="BKMK_mspp_populatereferenceentitylookupfield"></a> mspp_populatereferenceentitylookupfield

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Populate Table Reference Lookup Field|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_populatereferenceentitylookupfield|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_populatereferenceentitylookupfield Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_portaluserlookupattributeisactivityparty"></a> mspp_portaluserlookupattributeisactivityparty

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Is Activity Party|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_portaluserlookupattributeisactivityparty|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_portaluserlookupattributeisactivityparty Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_previousbuttoncssclass"></a> mspp_previousbuttoncssclass

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Previous Button CSS Class|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_previousbuttoncssclass|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_previousbuttontext"></a> mspp_previousbuttontext

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Previous Button Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_previousbuttontext|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_mspp_recommendedfieldsrequired"></a> mspp_recommendedfieldsrequired

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Recommended Fields Required|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_recommendedfieldsrequired|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_recommendedfieldsrequired Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_recordidquerystringparametername"></a> mspp_recordidquerystringparametername

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Record ID Parameter Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_recordidquerystringparametername|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_recordnotfoundmessage"></a> mspp_recordnotfoundmessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Record Not Found Message|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_recordnotfoundmessage|
|MaxLength|10000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_recordsourceallowcreateonnull"></a> mspp_recordsourceallowcreateonnull

|Property|Value|
|--------|-----|
|Description|This flag, when set to "true," allows the user to create a record if the record doesn't already exist and the Record Source Type is "Record Associated with Current Portal User."|
|DisplayName|Allow Create If Null|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_recordsourceallowcreateonnull|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_recordsourceallowcreateonnull Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_recordsourceentitylogicalname"></a> mspp_recordsourceentitylogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Record Source Table Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_recordsourceentitylogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_recordsourcerelationshipname"></a> mspp_recordsourcerelationshipname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Relationship Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_recordsourcerelationshipname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_redirecturl"></a> mspp_redirecturl

|Property|Value|
|--------|-----|
|Description|Shows the URL to redirect to.|
|DisplayName|Redirect URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_redirecturl|
|MaxLength|300|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_redirecturlappendentityidquerystring"></a> mspp_redirecturlappendentityidquerystring

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Append Table ID To Query String|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_redirecturlappendentityidquerystring|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_redirecturlappendentityidquerystring Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_redirecturlcustomquerystring"></a> mspp_redirecturlcustomquerystring

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Custom Query String|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_redirecturlcustomquerystring|
|MaxLength|300|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_redirecturlquerystringattribute"></a> mspp_redirecturlquerystringattribute

|Property|Value|
|--------|-----|
|Description|Add an attribute value as a query string value by specifying the logical name of the attribute to assign its value to the query string.|
|DisplayName|Attribute Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_redirecturlquerystringattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_redirecturlquerystringattributeparamname"></a> mspp_redirecturlquerystringattributeparamname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Query String Parameter Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_redirecturlquerystringattributeparamname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_redirecturlquerystringname"></a> mspp_redirecturlquerystringname

|Property|Value|
|--------|-----|
|Description|The url to redirect to is dynamically retrieved from the query string using this parameter name|
|DisplayName|Redirect URL Query String Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_redirecturlquerystringname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_redirectwebpage"></a> mspp_redirectwebpage

|Property|Value|
|--------|-----|
|Description|Web Page to redirect to.|
|DisplayName|Redirect Web Page|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_redirectwebpage|
|RequiredLevel|None|
|Targets|mspp_webpage|
|Type|Lookup|


### <a name="BKMK_mspp_referenceentitylogicalname"></a> mspp_referenceentitylogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Reference Table name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referenceentitylogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_referenceentityprimarykeylogicalname"></a> mspp_referenceentityprimarykeylogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Reference Table Primary Key Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referenceentityprimarykeylogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_referenceentityreadonlyformname"></a> mspp_referenceentityreadonlyformname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Reference Entity ReadOnly Form Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referenceentityreadonlyformname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_referenceentityrelationshipname"></a> mspp_referenceentityrelationshipname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Reference Entity Relationship Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referenceentityrelationshipname|
|MaxLength|150|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_referenceentityshowreadonlyform"></a> mspp_referenceentityshowreadonlyform

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Show Reference Entity ReadOnly Form|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referenceentityshowreadonlyform|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_referenceentityshowreadonlyform Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_referenceentitysourcetype"></a> mspp_referenceentitysourcetype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Source Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referenceentitysourcetype|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_referenceentitysourcetype Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Query String||
|756150001|Record Associated to Current Portal User||



### <a name="BKMK_mspp_referencequeryattributelogicalname"></a> mspp_referencequeryattributelogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Reference Query Attribute Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referencequeryattributelogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_referencequerystringisprimarykey"></a> mspp_referencequerystringisprimarykey

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Reference Query String Is Primary Key|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referencequerystringisprimarykey|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_referencequerystringisprimarykey Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_mspp_referencequerystringname"></a> mspp_referencequerystringname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Reference Query String Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referencequerystringname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_referencerecordsourcerelationshipname"></a> mspp_referencerecordsourcerelationshipname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Record Source Relationship Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referencerecordsourcerelationshipname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_referencetargetlookupattributelogicalname"></a> mspp_referencetargetlookupattributelogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Reference Target Lookup Attribute Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referencetargetlookupattributelogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_registerstartupscript"></a> mspp_registerstartupscript

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Custom JavaScript|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_registerstartupscript|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_renderwebresourcesinline"></a> mspp_renderwebresourcesinline

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Render Web Resources Inline|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_renderwebresourcesinline|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_renderwebresourcesinline Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_setentityreference"></a> mspp_setentityreference

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Set Table Reference|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_setentityreference|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_setentityreference Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_mspp_showcaptchaforauthenticatedusers"></a> mspp_showcaptchaforauthenticatedusers

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Show Captcha for Authenticated Users|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_showcaptchaforauthenticatedusers|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_showcaptchaforauthenticatedusers Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_showownerfields"></a> mspp_showownerfields

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Show Owner Fields|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_showownerfields|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_showownerfields Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_showunsupportedfields"></a> mspp_showunsupportedfields

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Show Unsupported Fields|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_showunsupportedfields|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_showunsupportedfields Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_storageaccountname"></a> mspp_storageaccountname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Storage Account Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_storageaccountname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_submitbuttonbusytext"></a> mspp_submitbuttonbusytext

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Submit Button Busy Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_submitbuttonbusytext|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_submitbuttoncssclass"></a> mspp_submitbuttoncssclass

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Submit Button CSS Class|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_submitbuttoncssclass|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_submitbuttontext"></a> mspp_submitbuttontext

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Submit Button Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_submitbuttontext|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_successmessage"></a> mspp_successmessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Success Message|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_successmessage|
|MaxLength|10000|
|RequiredLevel|Recommended|
|Type|Memo|


### <a name="BKMK_mspp_tabname"></a> mspp_tabname

|Property|Value|
|--------|-----|
|Description|The name of the tab on an entity form to render.|
|DisplayName|Tab Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_tabname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_targetentityportaluserlookupattribute"></a> mspp_targetentityportaluserlookupattribute

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Portal User Lookup Column|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_targetentityportaluserlookupattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_tooltipenabled"></a> mspp_tooltipenabled

|Property|Value|
|--------|-----|
|Description||
|DisplayName|ToolTip Enabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_tooltipenabled|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_tooltipenabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_validationgroup"></a> mspp_validationgroup

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Validation Group|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_validationgroup|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_validationsummarycssclass"></a> mspp_validationsummarycssclass

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Validation Summary CSS Class|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_validationsummarycssclass|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_validationsummaryheadertext"></a> mspp_validationsummaryheadertext

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Validation Summary Header Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_validationsummaryheadertext|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_validationsummarylinksenabled"></a> mspp_validationsummarylinksenabled

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Enable Validation Summary Links|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_validationsummarylinksenabled|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_validationsummarylinksenabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_mspp_validationsummarylinktext"></a> mspp_validationsummarylinktext

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Validation Summary Link Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_validationsummarylinktext|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website entity associated with this record.|
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
|Description|Status of the Basic Form|
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
|Description|Reason for the status of the Basic Form|
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
- [mspp_redirectwebpageName](#BKMK_mspp_redirectwebpageName)
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


### <a name="BKMK_mspp_redirectwebpageName"></a> mspp_redirectwebpageName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_redirectwebpagename|
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

- [mspp_entityform_entityformmetadata_entityformforcreate](#BKMK_mspp_entityform_entityformmetadata_entityformforcreate)
- [mspp_entityform_webformmetadata_entityformforcreate](#BKMK_mspp_entityform_webformmetadata_entityformforcreate)
- [mspp_entityformmetadata_entityform](#BKMK_mspp_entityformmetadata_entityform)
- [mspp_webpage_entityform](#BKMK_mspp_webpage_entityform)


### <a name="BKMK_mspp_entityform_entityformmetadata_entityformforcreate"></a> mspp_entityform_entityformmetadata_entityformforcreate

Same as the [mspp_entityform_entityformmetadata_entityformforcreate](mspp_entityformmetadata.md#BKMK_mspp_entityform_entityformmetadata_entityformforcreate) many-to-one relationship for the [mspp_entityformmetadata](mspp_entityformmetadata.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_entityformmetadata|
|ReferencingAttribute|mspp_entityformforcreate|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_entityform_entityformmetadata_entityformforcreate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_entityform_webformmetadata_entityformforcreate"></a> mspp_entityform_webformmetadata_entityformforcreate

Same as the [mspp_entityform_webformmetadata_entityformforcreate](mspp_webformmetadata.md#BKMK_mspp_entityform_webformmetadata_entityformforcreate) many-to-one relationship for the [mspp_webformmetadata](mspp_webformmetadata.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webformmetadata|
|ReferencingAttribute|mspp_entityformforcreateinwebformmetadata|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_entityform_webformmetadata_entityformforcreate|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_entityformmetadata_entityform"></a> mspp_entityformmetadata_entityform

Same as the [mspp_entityformmetadata_entityform](mspp_entityformmetadata.md#BKMK_mspp_entityformmetadata_entityform) many-to-one relationship for the [mspp_entityformmetadata](mspp_entityformmetadata.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_entityformmetadata|
|ReferencingAttribute|mspp_entityform|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_entityformmetadata_entityform|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_entityform"></a> mspp_webpage_entityform

Same as the [mspp_webpage_entityform](mspp_webpage.md#BKMK_mspp_webpage_entityform) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_entityform|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_entityform|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_entityform_redirectwebpage](#BKMK_mspp_entityform_redirectwebpage)
- [mspp_systemuser_mspp_entityform_createdby](#BKMK_mspp_systemuser_mspp_entityform_createdby)
- [mspp_systemuser_mspp_entityform_modifiedby](#BKMK_mspp_systemuser_mspp_entityform_modifiedby)
- [mspp_website_entityform](#BKMK_mspp_website_entityform)


### <a name="BKMK_mspp_entityform_redirectwebpage"></a> mspp_entityform_redirectwebpage

See the [mspp_entityform_redirectwebpage](mspp_webpage.md#BKMK_mspp_entityform_redirectwebpage) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_entityform_createdby"></a> mspp_systemuser_mspp_entityform_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_entityform_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_entityform_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_entityform_modifiedby"></a> mspp_systemuser_mspp_entityform_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_entityform_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_entityform_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_website_entityform"></a> mspp_website_entityform

See the [mspp_website_entityform](mspp_website.md#BKMK_mspp_website_entityform) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_entityform?text=mspp_entityform EntityType" />