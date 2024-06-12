---
title: "Web Link Set (mspp_weblinkset)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Web Link Set (mspp_weblinkset)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Web Link Set (mspp_weblinkset)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

A grouping of web links.

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_weblinksets<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_weblinksets(*mspp_weblinksetid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_weblinksets(*mspp_weblinksetid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_weblinksets<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_weblinksets(*mspp_weblinksetid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_weblinksets|
|DisplayCollectionName|Web Link Sets|
|DisplayName|Web Link Set|
|EntitySetName|mspp_weblinksets|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_weblinksets|
|LogicalName|mspp_weblinkset|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_weblinksetid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_weblinkset|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_copy](#BKMK_mspp_copy)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_display_name](#BKMK_mspp_display_name)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_publishingstateid](#BKMK_mspp_publishingstateid)
- [mspp_title](#BKMK_mspp_title)
- [mspp_weblinksetId](#BKMK_mspp_weblinksetId)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [mspp_websitelanguageid](#BKMK_mspp_websitelanguageid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)


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
|MaxLength|25000|
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


### <a name="BKMK_mspp_display_name"></a> mspp_display_name

|Property|Value|
|--------|-----|
|Description|Stores the label that is shown on the user interface (UI) in the data editing mode.|
|DisplayName|Display Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_display_name|
|MaxLength|100|
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


### <a name="BKMK_mspp_publishingstateid"></a> mspp_publishingstateid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Publishing State associated with Web Link Set.|
|DisplayName|Publishing State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_publishingstateid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_publishingstate|
|Type|Lookup|


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
|MaxLength|500|
|RequiredLevel|Recommended|
|Type|String|


### <a name="BKMK_mspp_weblinksetId"></a> mspp_weblinksetId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Web Link Set|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_weblinksetid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Web Link Set.|
|DisplayName|Website|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_websiteid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_website|
|Type|Lookup|


### <a name="BKMK_mspp_websitelanguageid"></a> mspp_websitelanguageid

|Property|Value|
|--------|-----|
|Description|Optional language to associate with web link sets for language-specific primary navigation|
|DisplayName|Web Link Set Language|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_websitelanguageid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_websitelanguage|
|Type|Lookup|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Web Link Set|
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
|Description|Reason for the status of the Web Link Set|
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
- [mspp_publishingstateidName](#BKMK_mspp_publishingstateidName)
- [mspp_websiteidName](#BKMK_mspp_websiteidName)
- [mspp_websitelanguageidName](#BKMK_mspp_websitelanguageidName)


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


### <a name="BKMK_mspp_websitelanguageidName"></a> mspp_websitelanguageidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_websitelanguageidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [mspp_weblinkset_weblink](#BKMK_mspp_weblinkset_weblink)
- [mspp_webpage_navigation_weblinkset](#BKMK_mspp_webpage_navigation_weblinkset)


### <a name="BKMK_mspp_weblinkset_weblink"></a> mspp_weblinkset_weblink

Same as the [mspp_weblinkset_weblink](mspp_weblink.md#BKMK_mspp_weblinkset_weblink) many-to-one relationship for the [mspp_weblink](mspp_weblink.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_weblink|
|ReferencingAttribute|mspp_weblinksetid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_weblinkset_weblink|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_navigation_weblinkset"></a> mspp_webpage_navigation_weblinkset

Same as the [mspp_webpage_navigation_weblinkset](mspp_webpage.md#BKMK_mspp_webpage_navigation_weblinkset) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_navigation|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_navigation_weblinkset|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_publishingstate_weblinkset](#BKMK_mspp_publishingstate_weblinkset)
- [mspp_systemuser_mspp_weblinkset_createdby](#BKMK_mspp_systemuser_mspp_weblinkset_createdby)
- [mspp_systemuser_mspp_weblinkset_modifiedby](#BKMK_mspp_systemuser_mspp_weblinkset_modifiedby)
- [mspp_website_weblinkset](#BKMK_mspp_website_weblinkset)
- [mspp_websitelanguage_weblinkset](#BKMK_mspp_websitelanguage_weblinkset)


### <a name="BKMK_mspp_publishingstate_weblinkset"></a> mspp_publishingstate_weblinkset

See the [mspp_publishingstate_weblinkset](mspp_publishingstate.md#BKMK_mspp_publishingstate_weblinkset) one-to-many relationship for the [mspp_publishingstate](mspp_publishingstate.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_weblinkset_createdby"></a> mspp_systemuser_mspp_weblinkset_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_weblinkset_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_weblinkset_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_weblinkset_modifiedby"></a> mspp_systemuser_mspp_weblinkset_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_weblinkset_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_weblinkset_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_website_weblinkset"></a> mspp_website_weblinkset

See the [mspp_website_weblinkset](mspp_website.md#BKMK_mspp_website_weblinkset) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### <a name="BKMK_mspp_websitelanguage_weblinkset"></a> mspp_websitelanguage_weblinkset

See the [mspp_websitelanguage_weblinkset](mspp_websitelanguage.md#BKMK_mspp_websitelanguage_weblinkset) one-to-many relationship for the [mspp_websitelanguage](mspp_websitelanguage.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_weblinkset?text=mspp_weblinkset EntityType" />