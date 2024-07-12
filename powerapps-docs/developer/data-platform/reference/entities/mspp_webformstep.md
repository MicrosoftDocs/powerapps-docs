---
title: "Form Step (mspp_webformstep)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Form Step (mspp_webformstep)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Form Step (mspp_webformstep)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Defines the flow logic of the form's user experience such as steps and conditional branching.

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_webformsteps<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_webformsteps(*mspp_webformstepid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_webformsteps(*mspp_webformstepid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_webformsteps<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_webformsteps(*mspp_webformstepid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_webformsteps|
|DisplayCollectionName|Form Steps|
|DisplayName|Form Step|
|EntitySetName|mspp_webformsteps|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_webformsteps|
|LogicalName|mspp_webformstep|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_webformstepid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_webformstep|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|The accept attribute specifies the MIME types of files that the server accepts through file upload. To specify more than one value, separate the values with a comma (e.g. audio/*,video/*,image/*).|
|DisplayName|Accept|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_accept|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_allowmultiplefiles"></a> mspp_allowmultiplefiles

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Allow Multiple Files|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_allowmultiplefiles|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_allowmultiplefiles Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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
|DisplayName|Attach File Maximum Size|
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
|DisplayName|Attach File Restrict Accept|
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
|756150000|Note Document||
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



### <a name="BKMK_mspp_autonumberattributelogicalname"></a> mspp_autonumberattributelogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Auto Number Attribute Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_autonumberattributelogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_autonumberdefinitionname"></a> mspp_autonumberdefinitionname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Auto Number Definition Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_autonumberdefinitionname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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



### <a name="BKMK_mspp_condition"></a> mspp_condition

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Condition|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_condition|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_conditiondefaultnextstep"></a> mspp_conditiondefaultnextstep

|Property|Value|
|--------|-----|
|Description|If the condition test fails, this is the next step.|
|DisplayName|Condition Default Next Step|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_conditiondefaultnextstep|
|RequiredLevel|None|
|Targets|mspp_webformstep|
|Type|Lookup|


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


### <a name="BKMK_mspp_createautonumber"></a> mspp_createautonumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Create Auto Number|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_createautonumber|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_createautonumber Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_mspp_editexistingrecordpermitted"></a> mspp_editexistingrecordpermitted

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Edit Existing Record Permitted|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_editexistingrecordpermitted|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_editexistingrecordpermitted Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_editexpiredmessage"></a> mspp_editexpiredmessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Edit Expired Message|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_editexpiredmessage|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_editexpiredstatecode"></a> mspp_editexpiredstatecode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Edit Expired State Code|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_editexpiredstatecode|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_editexpiredstatusreason"></a> mspp_editexpiredstatusreason

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Edit Expired Status Reason|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_editexpiredstatusreason|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_editnotpermittedmessage"></a> mspp_editnotpermittedmessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Edit Not Permitted Message|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_editnotpermittedmessage|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_entitypermissionsenabled"></a> mspp_entitypermissionsenabled

|Property|Value|
|--------|-----|
|Description||
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



### <a name="BKMK_mspp_entitysourcestep"></a> mspp_entitysourcestep

|Property|Value|
|--------|-----|
|Description|Unique identifier for Form Step associated with Form Step.|
|DisplayName|Entity Source Step|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_entitysourcestep|
|RequiredLevel|None|
|Targets|mspp_webformstep|
|Type|Lookup|


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
|100000001|Query String||
|100000002|Current Portal User||
|100000003|Result From Previous Step||
|100000004|Record Associated to Current Portal User||



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
|RequiredLevel|None|
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


### <a name="BKMK_mspp_loadeventkeyname"></a> mspp_loadeventkeyname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Load Event Key Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_loadeventkeyname|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_loguser"></a> mspp_loguser

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Log User|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_loguser|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_loguser Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_mspp_movepreviouseventkeyname"></a> mspp_movepreviouseventkeyname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Move Previous Event Key Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_movepreviouseventkeyname|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_movepreviouspermitted"></a> mspp_movepreviouspermitted

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Move Previous Permitted|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_movepreviouspermitted|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_movepreviouspermitted Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_mspp_multiplerecordsperuserpermitted"></a> mspp_multiplerecordsperuserpermitted

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Multiple Records Per User Permitted|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_multiplerecordsperuserpermitted|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_multiplerecordsperuserpermitted Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_mspp_nextstep"></a> mspp_nextstep

|Property|Value|
|--------|-----|
|Description|Pointer to the next step.|
|DisplayName|Next Step|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_nextstep|
|RequiredLevel|Recommended|
|Targets|mspp_webformstep|
|Type|Lookup|


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



### <a name="BKMK_mspp_postbackurl"></a> mspp_postbackurl

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Post Back URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_postbackurl|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_mspp_previousstep"></a> mspp_previousstep

|Property|Value|
|--------|-----|
|Description|Pointer to the previous step.|
|DisplayName|Previous Step|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_previousstep|
|RequiredLevel|Recommended|
|Targets|mspp_webformstep|
|Type|Lookup|


### <a name="BKMK_mspp_primarykeyattributelogicalname"></a> mspp_primarykeyattributelogicalname

|Property|Value|
|--------|-----|
|Description|The logical name of the primary key attribute of the target entity.|
|DisplayName|Primary Key Attribute Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_primarykeyattributelogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_primarykeyquerystringparametername"></a> mspp_primarykeyquerystringparametername

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Primary Key Query String Parameter Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_primarykeyquerystringparametername|
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
|MaxLength|100|
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
|100000000|Query String||
|100000001|Previous Step||
|100000002|Record Associated to Current Portal User||



### <a name="BKMK_mspp_referenceentitystep"></a> mspp_referenceentitystep

|Property|Value|
|--------|-----|
|Description|Unique identifier for Form Step associated with Form Step.|
|DisplayName|Reference Entity Step|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referenceentitystep|
|RequiredLevel|None|
|Targets|mspp_webformstep|
|Type|Lookup|


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


### <a name="BKMK_mspp_referencesourceentitylogicalname"></a> mspp_referencesourceentitylogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Reference Source Table name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_referencesourceentitylogicalname|
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



### <a name="BKMK_mspp_savedeventkeyname"></a> mspp_savedeventkeyname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Saved Event Key Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_savedeventkeyname|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_savingeventkeyname"></a> mspp_savingeventkeyname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Saving Event Key Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_savingeventkeyname|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


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
|DisplayName|Show Captcha for authenticated users|
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


### <a name="BKMK_mspp_submiteventkeyname"></a> mspp_submiteventkeyname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Submit Event Key Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_submiteventkeyname|
|MaxLength|1000|
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


### <a name="BKMK_mspp_targetentitylogicalname"></a> mspp_targetentitylogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Target Table name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_targetentitylogicalname|
|MaxLength|100|
|RequiredLevel|Recommended|
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


### <a name="BKMK_mspp_targetentityprimarykeylogicalname"></a> mspp_targetentityprimarykeylogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Target Entity Primary Key Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_targetentityprimarykeylogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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
|MaxLength|4000|
|RequiredLevel|Recommended|
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



### <a name="BKMK_mspp_type"></a> mspp_type

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_type|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### mspp_type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|100000000|Condition||
|100000001|Load Form||
|100000002|Load Tab||
|100000003|Redirect||
|100000004|Load User Control||



### <a name="BKMK_mspp_usercontrolpath"></a> mspp_usercontrolpath

|Property|Value|
|--------|-----|
|Description||
|DisplayName|User Control Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_usercontrolpath|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_usercontroltitle"></a> mspp_usercontroltitle

|Property|Value|
|--------|-----|
|Description||
|DisplayName|User Control Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_usercontroltitle|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_userhostaddressattributelogicalname"></a> mspp_userhostaddressattributelogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|User Host Address Attribute Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_userhostaddressattributelogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_useridentitynameattributelogicalname"></a> mspp_useridentitynameattributelogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|User Identity Name Attribute Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_useridentitynameattributelogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_mspp_webform"></a> mspp_webform

|Property|Value|
|--------|-----|
|Description|Unique identifier for Multistep Form associated with Form Step.|
|DisplayName|Multistep Form|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webform|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_webform|
|Type|Lookup|


### <a name="BKMK_mspp_webformstepId"></a> mspp_webformstepId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Form Step|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_webformstepid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Form Step|
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
|Description|Reason for the status of the Form Step|
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

- [mspp_conditiondefaultnextstepName](#BKMK_mspp_conditiondefaultnextstepName)
- [mspp_createdbyName](#BKMK_mspp_createdbyName)
- [mspp_createdbyYomiName](#BKMK_mspp_createdbyYomiName)
- [mspp_entitysourcestepName](#BKMK_mspp_entitysourcestepName)
- [mspp_modifiedbyName](#BKMK_mspp_modifiedbyName)
- [mspp_modifiedbyYomiName](#BKMK_mspp_modifiedbyYomiName)
- [mspp_nextstepName](#BKMK_mspp_nextstepName)
- [mspp_previousstepName](#BKMK_mspp_previousstepName)
- [mspp_redirectwebpageName](#BKMK_mspp_redirectwebpageName)
- [mspp_referenceentitystepName](#BKMK_mspp_referenceentitystepName)
- [mspp_webformName](#BKMK_mspp_webformName)


### <a name="BKMK_mspp_conditiondefaultnextstepName"></a> mspp_conditiondefaultnextstepName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_conditiondefaultnextstepname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_mspp_entitysourcestepName"></a> mspp_entitysourcestepName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_entitysourcestepname|
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


### <a name="BKMK_mspp_nextstepName"></a> mspp_nextstepName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_nextstepname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_previousstepName"></a> mspp_previousstepName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_previousstepname|
|MaxLength|100|
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


### <a name="BKMK_mspp_referenceentitystepName"></a> mspp_referenceentitystepName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_referenceentitystepname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_webformName"></a> mspp_webformName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_webformname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [mspp_webform_startstep](#BKMK_mspp_webform_startstep)
- [mspp_webformmetadata_webformstep](#BKMK_mspp_webformmetadata_webformstep)
- [mspp_webformstep_conditiondefaultnextstep](#BKMK_mspp_webformstep_conditiondefaultnextstep)
- [mspp_webformstep_entitysourcestep](#BKMK_mspp_webformstep_entitysourcestep)
- [mspp_webformstep_nextstep](#BKMK_mspp_webformstep_nextstep)
- [mspp_webformstep_previousstep](#BKMK_mspp_webformstep_previousstep)
- [mspp_webformstep_referenceentitystep](#BKMK_mspp_webformstep_referenceentitystep)


### <a name="BKMK_mspp_webform_startstep"></a> mspp_webform_startstep

Same as the [mspp_webform_startstep](mspp_webform.md#BKMK_mspp_webform_startstep) many-to-one relationship for the [mspp_webform](mspp_webform.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webform|
|ReferencingAttribute|mspp_startstep|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webform_startstep|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webformmetadata_webformstep"></a> mspp_webformmetadata_webformstep

Same as the [mspp_webformmetadata_webformstep](mspp_webformmetadata.md#BKMK_mspp_webformmetadata_webformstep) many-to-one relationship for the [mspp_webformmetadata](mspp_webformmetadata.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webformmetadata|
|ReferencingAttribute|mspp_webformstep|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webformmetadata_webformstep|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Metadata<br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webformstep_conditiondefaultnextstep"></a> mspp_webformstep_conditiondefaultnextstep

Same as the [mspp_webformstep_conditiondefaultnextstep](mspp_webformstep.md#BKMK_mspp_webformstep_conditiondefaultnextstep) many-to-one relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webformstep|
|ReferencingAttribute|mspp_conditiondefaultnextstep|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webformstep_conditiondefaultnextstep|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webformstep_entitysourcestep"></a> mspp_webformstep_entitysourcestep

Same as the [mspp_webformstep_entitysourcestep](mspp_webformstep.md#BKMK_mspp_webformstep_entitysourcestep) many-to-one relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webformstep|
|ReferencingAttribute|mspp_entitysourcestep|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webformstep_entitysourcestep|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Entity Source Steps<br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webformstep_nextstep"></a> mspp_webformstep_nextstep

Same as the [mspp_webformstep_nextstep](mspp_webformstep.md#BKMK_mspp_webformstep_nextstep) many-to-one relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webformstep|
|ReferencingAttribute|mspp_nextstep|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webformstep_nextstep|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webformstep_previousstep"></a> mspp_webformstep_previousstep

Same as the [mspp_webformstep_previousstep](mspp_webformstep.md#BKMK_mspp_webformstep_previousstep) many-to-one relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webformstep|
|ReferencingAttribute|mspp_previousstep|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webformstep_previousstep|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webformstep_referenceentitystep"></a> mspp_webformstep_referenceentitystep

Same as the [mspp_webformstep_referenceentitystep](mspp_webformstep.md#BKMK_mspp_webformstep_referenceentitystep) many-to-one relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webformstep|
|ReferencingAttribute|mspp_referenceentitystep|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webformstep_referenceentitystep|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Reference Entity Steps<br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_systemuser_mspp_webformstep_createdby](#BKMK_mspp_systemuser_mspp_webformstep_createdby)
- [mspp_systemuser_mspp_webformstep_modifiedby](#BKMK_mspp_systemuser_mspp_webformstep_modifiedby)
- [mspp_webformstep_conditiondefaultnextstep](#BKMK_mspp_webformstep_conditiondefaultnextstep)
- [mspp_webformstep_entitysourcestep](#BKMK_mspp_webformstep_entitysourcestep)
- [mspp_webformstep_nextstep](#BKMK_mspp_webformstep_nextstep)
- [mspp_webformstep_previousstep](#BKMK_mspp_webformstep_previousstep)
- [mspp_webformstep_redirectwebpage](#BKMK_mspp_webformstep_redirectwebpage)
- [mspp_webformstep_referenceentitystep](#BKMK_mspp_webformstep_referenceentitystep)
- [mspp_webformstep_webform](#BKMK_mspp_webformstep_webform)


### <a name="BKMK_mspp_systemuser_mspp_webformstep_createdby"></a> mspp_systemuser_mspp_webformstep_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webformstep_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webformstep_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_webformstep_modifiedby"></a> mspp_systemuser_mspp_webformstep_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webformstep_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webformstep_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_webformstep_conditiondefaultnextstep"></a> mspp_webformstep_conditiondefaultnextstep

See the [mspp_webformstep_conditiondefaultnextstep](mspp_webformstep.md#BKMK_mspp_webformstep_conditiondefaultnextstep) one-to-many relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

### <a name="BKMK_mspp_webformstep_entitysourcestep"></a> mspp_webformstep_entitysourcestep

See the [mspp_webformstep_entitysourcestep](mspp_webformstep.md#BKMK_mspp_webformstep_entitysourcestep) one-to-many relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

### <a name="BKMK_mspp_webformstep_nextstep"></a> mspp_webformstep_nextstep

See the [mspp_webformstep_nextstep](mspp_webformstep.md#BKMK_mspp_webformstep_nextstep) one-to-many relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

### <a name="BKMK_mspp_webformstep_previousstep"></a> mspp_webformstep_previousstep

See the [mspp_webformstep_previousstep](mspp_webformstep.md#BKMK_mspp_webformstep_previousstep) one-to-many relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

### <a name="BKMK_mspp_webformstep_redirectwebpage"></a> mspp_webformstep_redirectwebpage

See the [mspp_webformstep_redirectwebpage](mspp_webpage.md#BKMK_mspp_webformstep_redirectwebpage) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_webformstep_referenceentitystep"></a> mspp_webformstep_referenceentitystep

See the [mspp_webformstep_referenceentitystep](mspp_webformstep.md#BKMK_mspp_webformstep_referenceentitystep) one-to-many relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

### <a name="BKMK_mspp_webformstep_webform"></a> mspp_webformstep_webform

See the [mspp_webformstep_webform](mspp_webform.md#BKMK_mspp_webformstep_webform) one-to-many relationship for the [mspp_webform](mspp_webform.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_webformstep?text=mspp_webformstep EntityType" />