---
title: "Page Template (mspp_pagetemplate)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Page Template (mspp_pagetemplate)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Page Template (mspp_pagetemplate)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

URL of the .aspx page used to create new webpages.

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_pagetemplates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_pagetemplates(*mspp_pagetemplateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_pagetemplates(*mspp_pagetemplateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_pagetemplates<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_pagetemplates(*mspp_pagetemplateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_pagetemplates|
|DisplayCollectionName|Page Templates|
|DisplayName|Page Template|
|EntitySetName|mspp_pagetemplates|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_pagetemplates|
|LogicalName|mspp_pagetemplate|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_pagetemplateid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_pagetemplate|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_description](#BKMK_mspp_description)
- [mspp_entityname](#BKMK_mspp_entityname)
- [mspp_isdefault](#BKMK_mspp_isdefault)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_pagetemplateId](#BKMK_mspp_pagetemplateId)
- [mspp_rewriteurl](#BKMK_mspp_rewriteurl)
- [mspp_type](#BKMK_mspp_type)
- [mspp_usewebsiteheaderandfooter](#BKMK_mspp_usewebsiteheaderandfooter)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [mspp_webtemplateid](#BKMK_mspp_webtemplateid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)


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


### <a name="BKMK_mspp_description"></a> mspp_description

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_description|
|MaxLength|2000|
|RequiredLevel|Recommended|
|Type|Memo|


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
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_isdefault"></a> mspp_isdefault

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Is Default|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_isdefault|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_isdefault Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_mspp_pagetemplateId"></a> mspp_pagetemplateId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Page Template|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_pagetemplateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_rewriteurl"></a> mspp_rewriteurl

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Rewrite Url|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_rewriteurl|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_type"></a> mspp_type

|Property|Value|
|--------|-----|
|Description|The type of the record.|
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_type|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### mspp_type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Rewrite||
|756150001|Web Template||



### <a name="BKMK_mspp_usewebsiteheaderandfooter"></a> mspp_usewebsiteheaderandfooter

|Property|Value|
|--------|-----|
|Description|Control whether this web template page template will be rendered using the website header and footer, or control rendering of all page content.|
|DisplayName|Use Website Header and Footer|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_usewebsiteheaderandfooter|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_usewebsiteheaderandfooter Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Page Template.|
|DisplayName|Website|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_websiteid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_website|
|Type|Lookup|


### <a name="BKMK_mspp_webtemplateid"></a> mspp_webtemplateid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Template associated with Page Template.|
|DisplayName|Web Template|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webtemplateid|
|RequiredLevel|None|
|Targets|mspp_webtemplate|
|Type|Lookup|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Page Template|
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
|Description|Reason for the status of the Page Template|
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
- [mspp_websiteidName](#BKMK_mspp_websiteidName)
- [mspp_webtemplateidName](#BKMK_mspp_webtemplateidName)


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


### <a name="BKMK_mspp_webtemplateidName"></a> mspp_webtemplateidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_webtemplateidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_mspp_pagetemplate_webpage"></a> mspp_pagetemplate_webpage

Same as the [mspp_pagetemplate_webpage](mspp_webpage.md#BKMK_mspp_pagetemplate_webpage) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_pagetemplateid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_pagetemplate_webpage|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_systemuser_mspp_pagetemplate_createdby](#BKMK_mspp_systemuser_mspp_pagetemplate_createdby)
- [mspp_systemuser_mspp_pagetemplate_modifiedby](#BKMK_mspp_systemuser_mspp_pagetemplate_modifiedby)
- [mspp_website_pagetemplate](#BKMK_mspp_website_pagetemplate)
- [mspp_webtemplate_pagetemplate](#BKMK_mspp_webtemplate_pagetemplate)


### <a name="BKMK_mspp_systemuser_mspp_pagetemplate_createdby"></a> mspp_systemuser_mspp_pagetemplate_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_pagetemplate_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_pagetemplate_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_pagetemplate_modifiedby"></a> mspp_systemuser_mspp_pagetemplate_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_pagetemplate_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_pagetemplate_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_website_pagetemplate"></a> mspp_website_pagetemplate

See the [mspp_website_pagetemplate](mspp_website.md#BKMK_mspp_website_pagetemplate) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### <a name="BKMK_mspp_webtemplate_pagetemplate"></a> mspp_webtemplate_pagetemplate

See the [mspp_webtemplate_pagetemplate](mspp_webtemplate.md#BKMK_mspp_webtemplate_pagetemplate) one-to-many relationship for the [mspp_webtemplate](mspp_webtemplate.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_pagetemplate?text=mspp_pagetemplate EntityType" />