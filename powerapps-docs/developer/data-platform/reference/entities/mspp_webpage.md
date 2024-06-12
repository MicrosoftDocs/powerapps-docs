---
title: "Web Page (mspp_webpage)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Web Page (mspp_webpage)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Web Page (mspp_webpage)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Web Page

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_webpages<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_webpages(*mspp_webpageid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_webpages(*mspp_webpageid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_webpages<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_webpages(*mspp_webpageid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_webpages|
|DisplayCollectionName|Web Pages|
|DisplayName|Web Page|
|EntitySetName|mspp_webpages|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_webpages|
|LogicalName|mspp_webpage|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_webpageid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_webpage|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_alloworigin](#BKMK_mspp_alloworigin)
- [mspp_category](#BKMK_mspp_category)
- [mspp_copy](#BKMK_mspp_copy)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdbyipaddress](#BKMK_mspp_createdbyipaddress)
- [mspp_createdbyusername](#BKMK_mspp_createdbyusername)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_customcss](#BKMK_mspp_customcss)
- [mspp_customjavascript](#BKMK_mspp_customjavascript)
- [mspp_displaydate](#BKMK_mspp_displaydate)
- [mspp_displayorder](#BKMK_mspp_displayorder)
- [mspp_editorialcomments](#BKMK_mspp_editorialcomments)
- [mspp_enablerating](#BKMK_mspp_enablerating)
- [mspp_entityform](#BKMK_mspp_entityform)
- [mspp_entitylist](#BKMK_mspp_entitylist)
- [mspp_excludefromsearch](#BKMK_mspp_excludefromsearch)
- [mspp_expirationdate](#BKMK_mspp_expirationdate)
- [mspp_feedbackpolicy](#BKMK_mspp_feedbackpolicy)
- [mspp_hiddenfromsitemap](#BKMK_mspp_hiddenfromsitemap)
- [mspp_image](#BKMK_mspp_image)
- [mspp_imageurl](#BKMK_mspp_imageurl)
- [mspp_isofflinecached](#BKMK_mspp_isofflinecached)
- [mspp_isroot](#BKMK_mspp_isroot)
- [mspp_masterwebpageid](#BKMK_mspp_masterwebpageid)
- [mspp_meta_description](#BKMK_mspp_meta_description)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedbyipaddress](#BKMK_mspp_modifiedbyipaddress)
- [mspp_modifiedbyusername](#BKMK_mspp_modifiedbyusername)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_navigation](#BKMK_mspp_navigation)
- [mspp_pagetemplateid](#BKMK_mspp_pagetemplateid)
- [mspp_parentpageid](#BKMK_mspp_parentpageid)
- [mspp_partialurl](#BKMK_mspp_partialurl)
- [mspp_publishingstateid](#BKMK_mspp_publishingstateid)
- [mspp_releasedate](#BKMK_mspp_releasedate)
- [mspp_rootwebpageid](#BKMK_mspp_rootwebpageid)
- [mspp_sharedpageconfiguration](#BKMK_mspp_sharedpageconfiguration)
- [mspp_summary](#BKMK_mspp_summary)
- [mspp_title](#BKMK_mspp_title)
- [mspp_webform](#BKMK_mspp_webform)
- [mspp_webpageId](#BKMK_mspp_webpageId)
- [mspp_webpagelanguageid](#BKMK_mspp_webpagelanguageid)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)


### <a name="BKMK_mspp_alloworigin"></a> mspp_alloworigin

|Property|Value|
|--------|-----|
|Description|Defines CORS header Access-Control-Allow-Origin for cross origin requests.|
|DisplayName|Allow Origin|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_alloworigin|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_category"></a> mspp_category

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Category|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_category|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_category Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|News||



### <a name="BKMK_mspp_copy"></a> mspp_copy

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Copy|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_copy|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


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


### <a name="BKMK_mspp_createdbyipaddress"></a> mspp_createdbyipaddress

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Created By IP Address|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_createdbyipaddress|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_createdbyusername"></a> mspp_createdbyusername

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Created By Username|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_createdbyusername|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_mspp_customcss"></a> mspp_customcss

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Custom CSS|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_customcss|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_customjavascript"></a> mspp_customjavascript

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Custom JavaScript|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_customjavascript|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_displaydate"></a> mspp_displaydate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|Display Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_displaydate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_mspp_displayorder"></a> mspp_displayorder

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Display Order|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_displayorder|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_editorialcomments"></a> mspp_editorialcomments

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Editorial Comments|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_editorialcomments|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_enablerating"></a> mspp_enablerating

|Property|Value|
|--------|-----|
|Description|Setting this value to 'Yes' will allow users to rate the web page.|
|DisplayName|Enable Ratings|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_enablerating|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_enablerating Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_entityform"></a> mspp_entityform

|Property|Value|
|--------|-----|
|Description|Unique identifier for Entity Form associated with Web Page.|
|DisplayName|Basic Form|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_entityform|
|RequiredLevel|None|
|Targets|mspp_entityform|
|Type|Lookup|


### <a name="BKMK_mspp_entitylist"></a> mspp_entitylist

|Property|Value|
|--------|-----|
|Description|Unique identifier for Entity List associated with Web Page.|
|DisplayName|List|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_entitylist|
|RequiredLevel|None|
|Targets|mspp_entitylist|
|Type|Lookup|


### <a name="BKMK_mspp_excludefromsearch"></a> mspp_excludefromsearch

|Property|Value|
|--------|-----|
|Description|Shows whether the webpage is excluded from the portal search.|
|DisplayName|Exclude From Search|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_excludefromsearch|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_excludefromsearch Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_expirationdate"></a> mspp_expirationdate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|Expiration Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_expirationdate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_mspp_feedbackpolicy"></a> mspp_feedbackpolicy

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Comment Policy|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_feedbackpolicy|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_feedbackpolicy Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Inherit||
|756150001|None||
|756150002|Open||
|756150003|Item||
|756150004|Moderated||
|756150005|Closed||



### <a name="BKMK_mspp_hiddenfromsitemap"></a> mspp_hiddenfromsitemap

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Hidden From Sitemap|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_hiddenfromsitemap|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### mspp_hiddenfromsitemap Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_image"></a> mspp_image

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web File associated with Web Page.|
|DisplayName|Image|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_image|
|RequiredLevel|None|
|Targets|mspp_webfile|
|Type|Lookup|


### <a name="BKMK_mspp_imageurl"></a> mspp_imageurl

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Image URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_imageurl|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_isofflinecached"></a> mspp_isofflinecached

|Property|Value|
|--------|-----|
|Description|Define whether to cache this page for PWA.|
|DisplayName|isOfflineCached|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_isofflinecached|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_isofflinecached Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_isroot"></a> mspp_isroot

|Property|Value|
|--------|-----|
|Description|Defines whether this is the "root" record of this translated group of Web Pages.|
|DisplayName|Is Root|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_isroot|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### mspp_isroot Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_masterwebpageid"></a> mspp_masterwebpageid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Page associated with Web Page.|
|DisplayName|Master Web Page|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_masterwebpageid|
|RequiredLevel|None|
|Targets|mspp_webpage|
|Type|Lookup|


### <a name="BKMK_mspp_meta_description"></a> mspp_meta_description

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Description|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_meta_description|
|MaxLength|255|
|RequiredLevel|None|
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


### <a name="BKMK_mspp_modifiedbyipaddress"></a> mspp_modifiedbyipaddress

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Modified By IP Address|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_modifiedbyipaddress|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_modifiedbyusername"></a> mspp_modifiedbyusername

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Modified By Username|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_modifiedbyusername|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_mspp_navigation"></a> mspp_navigation

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Link Set associated with Web Page.|
|DisplayName|Navigation|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_navigation|
|RequiredLevel|None|
|Targets|mspp_weblinkset|
|Type|Lookup|


### <a name="BKMK_mspp_pagetemplateid"></a> mspp_pagetemplateid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Page Template associated with Web Page.|
|DisplayName|Page Template|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_pagetemplateid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_pagetemplate|
|Type|Lookup|


### <a name="BKMK_mspp_parentpageid"></a> mspp_parentpageid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Page associated with Web Page.|
|DisplayName|Parent Page|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_parentpageid|
|RequiredLevel|Recommended|
|Targets|mspp_webpage|
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
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_publishingstateid"></a> mspp_publishingstateid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Publishing State associated with Web Page.|
|DisplayName|Publishing State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_publishingstateid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_publishingstate|
|Type|Lookup|


### <a name="BKMK_mspp_releasedate"></a> mspp_releasedate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|Release Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_releasedate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_mspp_rootwebpageid"></a> mspp_rootwebpageid

|Property|Value|
|--------|-----|
|Description|Lookup to root WebPage.|
|DisplayName|Root Webpage|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_rootwebpageid|
|RequiredLevel|None|
|Targets|mspp_webpage|
|Type|Lookup|


### <a name="BKMK_mspp_sharedpageconfiguration"></a> mspp_sharedpageconfiguration

|Property|Value|
|--------|-----|
|Description|Determines if the content page uses the root page configuration|
|DisplayName|Shared Page Configuration|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_sharedpageconfiguration|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### mspp_sharedpageconfiguration Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_mspp_summary"></a> mspp_summary

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Summary|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_summary|
|MaxLength|25000|
|RequiredLevel|None|
|Type|Memo|


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
|MaxLength|512|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_webform"></a> mspp_webform

|Property|Value|
|--------|-----|
|Description|Unique identifier for Multistep Form associated with Web Page.|
|DisplayName|Multistep Form|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webform|
|RequiredLevel|None|
|Targets|mspp_webform|
|Type|Lookup|


### <a name="BKMK_mspp_webpageId"></a> mspp_webpageId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Web Page|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_webpageid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_webpagelanguageid"></a> mspp_webpagelanguageid

|Property|Value|
|--------|-----|
|Description|Language of this web page.|
|DisplayName|Webpage Language|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webpagelanguageid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_websitelanguage|
|Type|Lookup|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Web Page.|
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
|Description|Status of the Web Page|
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
|Description|Reason for the status of the Web Page|
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
- [mspp_entityformName](#BKMK_mspp_entityformName)
- [mspp_entitylistName](#BKMK_mspp_entitylistName)
- [mspp_imageName](#BKMK_mspp_imageName)
- [mspp_masterwebpageidName](#BKMK_mspp_masterwebpageidName)
- [mspp_modifiedbyName](#BKMK_mspp_modifiedbyName)
- [mspp_modifiedbyYomiName](#BKMK_mspp_modifiedbyYomiName)
- [mspp_navigationName](#BKMK_mspp_navigationName)
- [mspp_pagetemplateidName](#BKMK_mspp_pagetemplateidName)
- [mspp_parentpageidName](#BKMK_mspp_parentpageidName)
- [mspp_publishingstateidName](#BKMK_mspp_publishingstateidName)
- [mspp_rootwebpageidName](#BKMK_mspp_rootwebpageidName)
- [mspp_webformName](#BKMK_mspp_webformName)
- [mspp_webpagelanguageidName](#BKMK_mspp_webpagelanguageidName)
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


### <a name="BKMK_mspp_entityformName"></a> mspp_entityformName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_entityformname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_entitylistName"></a> mspp_entitylistName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_entitylistname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_imageName"></a> mspp_imageName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_imagename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_masterwebpageidName"></a> mspp_masterwebpageidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_masterwebpageidname|
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


### <a name="BKMK_mspp_navigationName"></a> mspp_navigationName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_navigationname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_pagetemplateidName"></a> mspp_pagetemplateidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_pagetemplateidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_parentpageidName"></a> mspp_parentpageidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_parentpageidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_publishingstateidName"></a> mspp_publishingstateidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_publishingstateidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_rootwebpageidName"></a> mspp_rootwebpageidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_rootwebpageidname|
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


### <a name="BKMK_mspp_webpagelanguageidName"></a> mspp_webpagelanguageidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_webpagelanguageidname|
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

- [mspp_entityform_redirectwebpage](#BKMK_mspp_entityform_redirectwebpage)
- [mspp_entitylist_webpageforcreate](#BKMK_mspp_entitylist_webpageforcreate)
- [mspp_entitylist_webpagefordetailsview](#BKMK_mspp_entitylist_webpagefordetailsview)
- [mspp_parentwebpage_shortcut](#BKMK_mspp_parentwebpage_shortcut)
- [mspp_webformstep_redirectwebpage](#BKMK_mspp_webformstep_redirectwebpage)
- [mspp_webpage_masterwebpage](#BKMK_mspp_webpage_masterwebpage)
- [mspp_webpage_redirect](#BKMK_mspp_webpage_redirect)
- [mspp_webpage_shortcut](#BKMK_mspp_webpage_shortcut)
- [mspp_webpage_sitemarker](#BKMK_mspp_webpage_sitemarker)
- [mspp_webpage_webfile](#BKMK_mspp_webpage_webfile)
- [mspp_webpage_weblink](#BKMK_mspp_webpage_weblink)
- [mspp_webpage_webpage](#BKMK_mspp_webpage_webpage)
- [mspp_webpage_webpage_rootwebpageid](#BKMK_mspp_webpage_webpage_rootwebpageid)
- [mspp_webpage_webpageaccesscontrolrule](#BKMK_mspp_webpage_webpageaccesscontrolrule)


### <a name="BKMK_mspp_entityform_redirectwebpage"></a> mspp_entityform_redirectwebpage

Same as the [mspp_entityform_redirectwebpage](mspp_entityform.md#BKMK_mspp_entityform_redirectwebpage) many-to-one relationship for the [mspp_entityform](mspp_entityform.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_entityform|
|ReferencingAttribute|mspp_redirectwebpage|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_entityform_redirectwebpage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_entitylist_webpageforcreate"></a> mspp_entitylist_webpageforcreate

Same as the [mspp_entitylist_webpageforcreate](mspp_entitylist.md#BKMK_mspp_entitylist_webpageforcreate) many-to-one relationship for the [mspp_entitylist](mspp_entitylist.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_entitylist|
|ReferencingAttribute|mspp_webpageforcreate|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_entitylist_webpageforcreate|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_entitylist_webpagefordetailsview"></a> mspp_entitylist_webpagefordetailsview

Same as the [mspp_entitylist_webpagefordetailsview](mspp_entitylist.md#BKMK_mspp_entitylist_webpagefordetailsview) many-to-one relationship for the [mspp_entitylist](mspp_entitylist.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_entitylist|
|ReferencingAttribute|mspp_webpagefordetailsview|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_entitylist_webpagefordetailsview|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Entity List (Details View)<br />Order: 100590|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_parentwebpage_shortcut"></a> mspp_parentwebpage_shortcut

Same as the [mspp_parentwebpage_shortcut](mspp_shortcut.md#BKMK_mspp_parentwebpage_shortcut) many-to-one relationship for the [mspp_shortcut](mspp_shortcut.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_shortcut|
|ReferencingAttribute|mspp_parentpage_webpageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_parentwebpage_shortcut|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 101200|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webformstep_redirectwebpage"></a> mspp_webformstep_redirectwebpage

Same as the [mspp_webformstep_redirectwebpage](mspp_webformstep.md#BKMK_mspp_webformstep_redirectwebpage) many-to-one relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webformstep|
|ReferencingAttribute|mspp_redirectwebpage|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webformstep_redirectwebpage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_masterwebpage"></a> mspp_webpage_masterwebpage

Same as the [mspp_webpage_masterwebpage](mspp_webpage.md#BKMK_mspp_webpage_masterwebpage) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_masterwebpageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_masterwebpage|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Subscriber Web Pages<br />Order: 101400|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_redirect"></a> mspp_webpage_redirect

Same as the [mspp_webpage_redirect](mspp_redirect.md#BKMK_mspp_webpage_redirect) many-to-one relationship for the [mspp_redirect](mspp_redirect.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_redirect|
|ReferencingAttribute|mspp_webpageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_redirect|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 101100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_shortcut"></a> mspp_webpage_shortcut

Same as the [mspp_webpage_shortcut](mspp_shortcut.md#BKMK_mspp_webpage_shortcut) many-to-one relationship for the [mspp_shortcut](mspp_shortcut.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_shortcut|
|ReferencingAttribute|mspp_webpageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_shortcut|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 101200|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_sitemarker"></a> mspp_webpage_sitemarker

Same as the [mspp_webpage_sitemarker](mspp_sitemarker.md#BKMK_mspp_webpage_sitemarker) many-to-one relationship for the [mspp_sitemarker](mspp_sitemarker.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_sitemarker|
|ReferencingAttribute|mspp_pageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_sitemarker|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100300|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_webfile"></a> mspp_webpage_webfile

Same as the [mspp_webpage_webfile](mspp_webfile.md#BKMK_mspp_webpage_webfile) many-to-one relationship for the [mspp_webfile](mspp_webfile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webfile|
|ReferencingAttribute|mspp_parentpageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_webfile|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Child Files<br />Order: 100100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_weblink"></a> mspp_webpage_weblink

Same as the [mspp_webpage_weblink](mspp_weblink.md#BKMK_mspp_webpage_weblink) many-to-one relationship for the [mspp_weblink](mspp_weblink.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_weblink|
|ReferencingAttribute|mspp_pageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_weblink|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100400|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_webpage"></a> mspp_webpage_webpage

Same as the [mspp_webpage_webpage](mspp_webpage.md#BKMK_mspp_webpage_webpage) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_parentpageid|
|IsHierarchical|True|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_webpage|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Child Pages<br />Order: 100200|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_webpage_rootwebpageid"></a> mspp_webpage_webpage_rootwebpageid

Same as the [mspp_webpage_webpage_rootwebpageid](mspp_webpage.md#BKMK_mspp_webpage_webpage_rootwebpageid) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_rootwebpageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_webpage_rootwebpageid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_webpageaccesscontrolrule"></a> mspp_webpage_webpageaccesscontrolrule

Same as the [mspp_webpage_webpageaccesscontrolrule](mspp_webpageaccesscontrolrule.md#BKMK_mspp_webpage_webpageaccesscontrolrule) many-to-one relationship for the [mspp_webpageaccesscontrolrule](mspp_webpageaccesscontrolrule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpageaccesscontrolrule|
|ReferencingAttribute|mspp_webpageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_webpageaccesscontrolrule|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Access Control Rules<br />Order: 100100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_pagetemplate_webpage](#BKMK_mspp_pagetemplate_webpage)
- [mspp_publishingstate_webpage](#BKMK_mspp_publishingstate_webpage)
- [mspp_systemuser_mspp_webpage_createdby](#BKMK_mspp_systemuser_mspp_webpage_createdby)
- [mspp_systemuser_mspp_webpage_modifiedby](#BKMK_mspp_systemuser_mspp_webpage_modifiedby)
- [mspp_webfile_webpage_image](#BKMK_mspp_webfile_webpage_image)
- [mspp_webpage_entityform](#BKMK_mspp_webpage_entityform)
- [mspp_webpage_entitylist](#BKMK_mspp_webpage_entitylist)
- [mspp_webpage_masterwebpage](#BKMK_mspp_webpage_masterwebpage)
- [mspp_webpage_navigation_weblinkset](#BKMK_mspp_webpage_navigation_weblinkset)
- [mspp_webpage_webform](#BKMK_mspp_webpage_webform)
- [mspp_webpage_webpage](#BKMK_mspp_webpage_webpage)
- [mspp_webpage_webpage_rootwebpageid](#BKMK_mspp_webpage_webpage_rootwebpageid)
- [mspp_website_webpage](#BKMK_mspp_website_webpage)
- [mspp_websitelanguage_webpage_webpagelanguageid](#BKMK_mspp_websitelanguage_webpage_webpagelanguageid)


### <a name="BKMK_mspp_pagetemplate_webpage"></a> mspp_pagetemplate_webpage

See the [mspp_pagetemplate_webpage](mspp_pagetemplate.md#BKMK_mspp_pagetemplate_webpage) one-to-many relationship for the [mspp_pagetemplate](mspp_pagetemplate.md) table/entity.

### <a name="BKMK_mspp_publishingstate_webpage"></a> mspp_publishingstate_webpage

See the [mspp_publishingstate_webpage](mspp_publishingstate.md#BKMK_mspp_publishingstate_webpage) one-to-many relationship for the [mspp_publishingstate](mspp_publishingstate.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_webpage_createdby"></a> mspp_systemuser_mspp_webpage_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webpage_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webpage_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_webpage_modifiedby"></a> mspp_systemuser_mspp_webpage_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webpage_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webpage_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_webfile_webpage_image"></a> mspp_webfile_webpage_image

See the [mspp_webfile_webpage_image](mspp_webfile.md#BKMK_mspp_webfile_webpage_image) one-to-many relationship for the [mspp_webfile](mspp_webfile.md) table/entity.

### <a name="BKMK_mspp_webpage_entityform"></a> mspp_webpage_entityform

See the [mspp_webpage_entityform](mspp_entityform.md#BKMK_mspp_webpage_entityform) one-to-many relationship for the [mspp_entityform](mspp_entityform.md) table/entity.

### <a name="BKMK_mspp_webpage_entitylist"></a> mspp_webpage_entitylist

See the [mspp_webpage_entitylist](mspp_entitylist.md#BKMK_mspp_webpage_entitylist) one-to-many relationship for the [mspp_entitylist](mspp_entitylist.md) table/entity.

### <a name="BKMK_mspp_webpage_masterwebpage"></a> mspp_webpage_masterwebpage

See the [mspp_webpage_masterwebpage](mspp_webpage.md#BKMK_mspp_webpage_masterwebpage) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_webpage_navigation_weblinkset"></a> mspp_webpage_navigation_weblinkset

See the [mspp_webpage_navigation_weblinkset](mspp_weblinkset.md#BKMK_mspp_webpage_navigation_weblinkset) one-to-many relationship for the [mspp_weblinkset](mspp_weblinkset.md) table/entity.

### <a name="BKMK_mspp_webpage_webform"></a> mspp_webpage_webform

See the [mspp_webpage_webform](mspp_webform.md#BKMK_mspp_webpage_webform) one-to-many relationship for the [mspp_webform](mspp_webform.md) table/entity.

### <a name="BKMK_mspp_webpage_webpage"></a> mspp_webpage_webpage

See the [mspp_webpage_webpage](mspp_webpage.md#BKMK_mspp_webpage_webpage) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_webpage_webpage_rootwebpageid"></a> mspp_webpage_webpage_rootwebpageid

See the [mspp_webpage_webpage_rootwebpageid](mspp_webpage.md#BKMK_mspp_webpage_webpage_rootwebpageid) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_website_webpage"></a> mspp_website_webpage

See the [mspp_website_webpage](mspp_website.md#BKMK_mspp_website_webpage) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### <a name="BKMK_mspp_websitelanguage_webpage_webpagelanguageid"></a> mspp_websitelanguage_webpage_webpagelanguageid

See the [mspp_websitelanguage_webpage_webpagelanguageid](mspp_websitelanguage.md#BKMK_mspp_websitelanguage_webpage_webpagelanguageid) one-to-many relationship for the [mspp_websitelanguage](mspp_websitelanguage.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_webpage?text=mspp_webpage EntityType" />