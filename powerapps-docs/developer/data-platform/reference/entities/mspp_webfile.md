---
title: "Web File (mspp_webfile)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Web File (mspp_webfile)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Web File (mspp_webfile)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Storage of files used in the web Portals.

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_webfiles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_webfiles(*mspp_webfileid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_webfiles(*mspp_webfileid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_webfiles<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_webfiles(*mspp_webfileid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_webfiles|
|DisplayCollectionName|Web Files|
|DisplayName|Web File|
|EntitySetName|mspp_webfiles|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_webfiles|
|LogicalName|mspp_webfile|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_webfileid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_webfile|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_alloworigin](#BKMK_mspp_alloworigin)
- [mspp_cloudblobaddress](#BKMK_mspp_cloudblobaddress)
- [mspp_contentdisposition](#BKMK_mspp_contentdisposition)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdbyipaddress](#BKMK_mspp_createdbyipaddress)
- [mspp_createdbyusername](#BKMK_mspp_createdbyusername)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_displaydate](#BKMK_mspp_displaydate)
- [mspp_displayorder](#BKMK_mspp_displayorder)
- [mspp_excludefromsearch](#BKMK_mspp_excludefromsearch)
- [mspp_expirationdate](#BKMK_mspp_expirationdate)
- [mspp_hiddenfromsitemap](#BKMK_mspp_hiddenfromsitemap)
- [mspp_masterwebfileid](#BKMK_mspp_masterwebfileid)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedbyipaddress](#BKMK_mspp_modifiedbyipaddress)
- [mspp_modifiedbyusername](#BKMK_mspp_modifiedbyusername)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_parentpageid](#BKMK_mspp_parentpageid)
- [mspp_partialurl](#BKMK_mspp_partialurl)
- [mspp_publishingstateid](#BKMK_mspp_publishingstateid)
- [mspp_releasedate](#BKMK_mspp_releasedate)
- [mspp_summary](#BKMK_mspp_summary)
- [mspp_title](#BKMK_mspp_title)
- [mspp_webfileId](#BKMK_mspp_webfileId)
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


### <a name="BKMK_mspp_cloudblobaddress"></a> mspp_cloudblobaddress

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Cloud Blob Address|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_cloudblobaddress|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_contentdisposition"></a> mspp_contentdisposition

|Property|Value|
|--------|-----|
|Description|Shows the value to be applied to the HTTP Response Headers Content-Disposition.|
|DisplayName|Content-Disposition|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_contentdisposition|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_contentdisposition Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|inline|File should be automatically displayed.|
|756150001|attachment|File is not displayed automatically and requires some form of action from the user to open it.|



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


### <a name="BKMK_mspp_excludefromsearch"></a> mspp_excludefromsearch

|Property|Value|
|--------|-----|
|Description|Shows whether the web file is excluded from the portal search.|
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



### <a name="BKMK_mspp_masterwebfileid"></a> mspp_masterwebfileid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web File associated with Web File.|
|DisplayName|Master Web File|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_masterwebfileid|
|RequiredLevel|None|
|Targets|mspp_webfile|
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


### <a name="BKMK_mspp_parentpageid"></a> mspp_parentpageid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Page associated with Web File.|
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
|MaxLength|1024|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_publishingstateid"></a> mspp_publishingstateid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Publishing State associated with Web File.|
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


### <a name="BKMK_mspp_webfileId"></a> mspp_webfileId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Web File|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_webfileid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Web File.|
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
|Description|Status of the Web File|
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
|Description|Reason for the status of the Web File|
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
- [mspp_masterwebfileidName](#BKMK_mspp_masterwebfileidName)
- [mspp_modifiedbyName](#BKMK_mspp_modifiedbyName)
- [mspp_modifiedbyYomiName](#BKMK_mspp_modifiedbyYomiName)
- [mspp_parentpageidName](#BKMK_mspp_parentpageidName)
- [mspp_publishingstateidName](#BKMK_mspp_publishingstateidName)
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


### <a name="BKMK_mspp_masterwebfileidName"></a> mspp_masterwebfileidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_masterwebfileidname|
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

- [mspp_webfile_masterwebfile](#BKMK_mspp_webfile_masterwebfile)
- [mspp_webfile_shortcut](#BKMK_mspp_webfile_shortcut)
- [mspp_webfile_webpage_image](#BKMK_mspp_webfile_webpage_image)


### <a name="BKMK_mspp_webfile_masterwebfile"></a> mspp_webfile_masterwebfile

Same as the [mspp_webfile_masterwebfile](mspp_webfile.md#BKMK_mspp_webfile_masterwebfile) many-to-one relationship for the [mspp_webfile](mspp_webfile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webfile|
|ReferencingAttribute|mspp_masterwebfileid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webfile_masterwebfile|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Subscriber Web Files<br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webfile_shortcut"></a> mspp_webfile_shortcut

Same as the [mspp_webfile_shortcut](mspp_shortcut.md#BKMK_mspp_webfile_shortcut) many-to-one relationship for the [mspp_shortcut](mspp_shortcut.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_shortcut|
|ReferencingAttribute|mspp_webfileid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webfile_shortcut|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webfile_webpage_image"></a> mspp_webfile_webpage_image

Same as the [mspp_webfile_webpage_image](mspp_webpage.md#BKMK_mspp_webfile_webpage_image) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_image|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webfile_webpage_image|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_publishingstate_webfile](#BKMK_mspp_publishingstate_webfile)
- [mspp_systemuser_mspp_webfile_createdby](#BKMK_mspp_systemuser_mspp_webfile_createdby)
- [mspp_systemuser_mspp_webfile_modifiedby](#BKMK_mspp_systemuser_mspp_webfile_modifiedby)
- [mspp_webfile_masterwebfile](#BKMK_mspp_webfile_masterwebfile)
- [mspp_webpage_webfile](#BKMK_mspp_webpage_webfile)
- [mspp_website_webfile](#BKMK_mspp_website_webfile)


### <a name="BKMK_mspp_publishingstate_webfile"></a> mspp_publishingstate_webfile

See the [mspp_publishingstate_webfile](mspp_publishingstate.md#BKMK_mspp_publishingstate_webfile) one-to-many relationship for the [mspp_publishingstate](mspp_publishingstate.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_webfile_createdby"></a> mspp_systemuser_mspp_webfile_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webfile_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webfile_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_webfile_modifiedby"></a> mspp_systemuser_mspp_webfile_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webfile_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webfile_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_webfile_masterwebfile"></a> mspp_webfile_masterwebfile

See the [mspp_webfile_masterwebfile](mspp_webfile.md#BKMK_mspp_webfile_masterwebfile) one-to-many relationship for the [mspp_webfile](mspp_webfile.md) table/entity.

### <a name="BKMK_mspp_webpage_webfile"></a> mspp_webpage_webfile

See the [mspp_webpage_webfile](mspp_webpage.md#BKMK_mspp_webpage_webfile) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_website_webfile"></a> mspp_website_webfile

See the [mspp_website_webfile](mspp_website.md#BKMK_mspp_website_webfile) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_webfile?text=mspp_webfile EntityType" />