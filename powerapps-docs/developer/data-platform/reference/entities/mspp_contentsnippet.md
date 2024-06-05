---
title: "Content Snippet (mspp_contentsnippet)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Content Snippet (mspp_contentsnippet)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Content Snippet (mspp_contentsnippet)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Content snippets are inserted in page templates so that any label, text string or image in the template can be content-managed.

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_contentsnippets<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_contentsnippets(*mspp_contentsnippetid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_contentsnippets(*mspp_contentsnippetid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_contentsnippets<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_contentsnippets(*mspp_contentsnippetid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_contentsnippets|
|DisplayCollectionName|Content Snippets|
|DisplayName|Content Snippet|
|EntitySetName|mspp_contentsnippets|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_contentsnippets|
|LogicalName|mspp_contentsnippet|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_contentsnippetid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_contentsnippet|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_contentsnippetId](#BKMK_mspp_contentsnippetId)
- [mspp_contentsnippetlanguageid](#BKMK_mspp_contentsnippetlanguageid)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdbyipaddress](#BKMK_mspp_createdbyipaddress)
- [mspp_createdbyusername](#BKMK_mspp_createdbyusername)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_display_name](#BKMK_mspp_display_name)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedbyipaddress](#BKMK_mspp_modifiedbyipaddress)
- [mspp_modifiedbyusername](#BKMK_mspp_modifiedbyusername)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_type](#BKMK_mspp_type)
- [mspp_value](#BKMK_mspp_value)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)


### <a name="BKMK_mspp_contentsnippetId"></a> mspp_contentsnippetId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Content Snippet|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_contentsnippetid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_contentsnippetlanguageid"></a> mspp_contentsnippetlanguageid

|Property|Value|
|--------|-----|
|Description|Option to make content snippets language specific|
|DisplayName|Content Snippet Language|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_contentsnippetlanguageid|
|RequiredLevel|None|
|Targets|mspp_websitelanguage|
|Type|Lookup|


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
|MaxLength|250|
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


### <a name="BKMK_mspp_type"></a> mspp_type

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_type|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Text||
|756150001|HTML||



### <a name="BKMK_mspp_value"></a> mspp_value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Value|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_value|
|MaxLength|1048576|
|RequiredLevel|Recommended|
|Type|Memo|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Content Snippet.|
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
|Description|Status of the Content Snippet|
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
|Description|Reason for the status of the Content Snippet|
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

- [mspp_contentsnippetlanguageidName](#BKMK_mspp_contentsnippetlanguageidName)
- [mspp_createdbyName](#BKMK_mspp_createdbyName)
- [mspp_createdbyYomiName](#BKMK_mspp_createdbyYomiName)
- [mspp_modifiedbyName](#BKMK_mspp_modifiedbyName)
- [mspp_modifiedbyYomiName](#BKMK_mspp_modifiedbyYomiName)
- [mspp_websiteidName](#BKMK_mspp_websiteidName)


### <a name="BKMK_mspp_contentsnippetlanguageidName"></a> mspp_contentsnippetlanguageidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_contentsnippetlanguageidname|
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_systemuser_mspp_contentsnippet_createdby](#BKMK_mspp_systemuser_mspp_contentsnippet_createdby)
- [mspp_systemuser_mspp_contentsnippet_modifiedby](#BKMK_mspp_systemuser_mspp_contentsnippet_modifiedby)
- [mspp_website_contentsnippet](#BKMK_mspp_website_contentsnippet)
- [mspp_websitelanguage_contentsnippet_contentsnippetlanguageid](#BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid)


### <a name="BKMK_mspp_systemuser_mspp_contentsnippet_createdby"></a> mspp_systemuser_mspp_contentsnippet_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_contentsnippet_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_contentsnippet_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_contentsnippet_modifiedby"></a> mspp_systemuser_mspp_contentsnippet_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_contentsnippet_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_contentsnippet_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_website_contentsnippet"></a> mspp_website_contentsnippet

See the [mspp_website_contentsnippet](mspp_website.md#BKMK_mspp_website_contentsnippet) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### <a name="BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid"></a> mspp_websitelanguage_contentsnippet_contentsnippetlanguageid

See the [mspp_websitelanguage_contentsnippet_contentsnippetlanguageid](mspp_websitelanguage.md#BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid) one-to-many relationship for the [mspp_websitelanguage](mspp_websitelanguage.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_contentsnippet?text=mspp_contentsnippet EntityType" />