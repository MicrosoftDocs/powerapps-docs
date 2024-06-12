---
title: "Web Link (mspp_weblink)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Web Link (mspp_weblink)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Web Link (mspp_weblink)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

A textual or imaged based link to an interal or external URL.

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_weblinks<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_weblinks(*mspp_weblinkid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_weblinks(*mspp_weblinkid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_weblinks<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_weblinks(*mspp_weblinkid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_weblinks|
|DisplayCollectionName|Web Links|
|DisplayName|Web Link|
|EntitySetName|mspp_weblinks|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_weblinks|
|LogicalName|mspp_weblink|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_weblinkid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_weblink|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdbyipaddress](#BKMK_mspp_createdbyipaddress)
- [mspp_createdbyusername](#BKMK_mspp_createdbyusername)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_description](#BKMK_mspp_description)
- [mspp_disablepagevalidation](#BKMK_mspp_disablepagevalidation)
- [mspp_displayimageonly](#BKMK_mspp_displayimageonly)
- [mspp_displayorder](#BKMK_mspp_displayorder)
- [mspp_displaypagechildlinks](#BKMK_mspp_displaypagechildlinks)
- [mspp_externalurl](#BKMK_mspp_externalurl)
- [mspp_imagealttext](#BKMK_mspp_imagealttext)
- [mspp_imageheight](#BKMK_mspp_imageheight)
- [mspp_imageurl](#BKMK_mspp_imageurl)
- [mspp_imagewidth](#BKMK_mspp_imagewidth)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedbyipaddress](#BKMK_mspp_modifiedbyipaddress)
- [mspp_modifiedbyusername](#BKMK_mspp_modifiedbyusername)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_openinnewwindow](#BKMK_mspp_openinnewwindow)
- [mspp_pageid](#BKMK_mspp_pageid)
- [mspp_parentweblinkid](#BKMK_mspp_parentweblinkid)
- [mspp_publishingstateid](#BKMK_mspp_publishingstateid)
- [mspp_robotsfollowlink](#BKMK_mspp_robotsfollowlink)
- [mspp_weblinkId](#BKMK_mspp_weblinkId)
- [mspp_weblinksetid](#BKMK_mspp_weblinksetid)
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
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_disablepagevalidation"></a> mspp_disablepagevalidation

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Disable Page Validation|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_disablepagevalidation|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_disablepagevalidation Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_displayimageonly"></a> mspp_displayimageonly

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Display Image Only|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_displayimageonly|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_displayimageonly Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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
|RequiredLevel|Recommended|
|Type|Integer|


### <a name="BKMK_mspp_displaypagechildlinks"></a> mspp_displaypagechildlinks

|Property|Value|
|--------|-----|
|Description|Select whether to display the children of the page as child links for this link.|
|DisplayName|Display Page Child Links|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_displaypagechildlinks|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_displaypagechildlinks Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_externalurl"></a> mspp_externalurl

|Property|Value|
|--------|-----|
|Description||
|DisplayName|External Url|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_externalurl|
|MaxLength|2048|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_imagealttext"></a> mspp_imagealttext

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Image Alt Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_imagealttext|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_imageheight"></a> mspp_imageheight

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Image Height|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_imageheight|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_imageurl"></a> mspp_imageurl

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Image Url|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_imageurl|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_imagewidth"></a> mspp_imagewidth

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Image Width|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_imagewidth|
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


### <a name="BKMK_mspp_openinnewwindow"></a> mspp_openinnewwindow

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Open In New Window|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_openinnewwindow|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### mspp_openinnewwindow Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_pageid"></a> mspp_pageid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Page associated with Web Link.|
|DisplayName|Page|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_pageid|
|RequiredLevel|None|
|Targets|mspp_webpage|
|Type|Lookup|


### <a name="BKMK_mspp_parentweblinkid"></a> mspp_parentweblinkid

|Property|Value|
|--------|-----|
|Description|Unique identifier for parent Web Link associated with Web Link.|
|DisplayName|Parent Web Link|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_parentweblinkid|
|RequiredLevel|None|
|Targets|mspp_weblink|
|Type|Lookup|


### <a name="BKMK_mspp_publishingstateid"></a> mspp_publishingstateid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Publishing State associated with Web Link.|
|DisplayName|Publishing State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_publishingstateid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_publishingstate|
|Type|Lookup|


### <a name="BKMK_mspp_robotsfollowlink"></a> mspp_robotsfollowlink

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Robots Follow Link|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_robotsfollowlink|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### mspp_robotsfollowlink Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_mspp_weblinkId"></a> mspp_weblinkId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Web Link|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_weblinkid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_weblinksetid"></a> mspp_weblinksetid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Link Set associated with Web Link.|
|DisplayName|Web Link Set|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_weblinksetid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_weblinkset|
|Type|Lookup|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Web Link|
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
|Description|Reason for the status of the Web Link|
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
- [mspp_pageidName](#BKMK_mspp_pageidName)
- [mspp_parentweblinkidName](#BKMK_mspp_parentweblinkidName)
- [mspp_publishingstateidName](#BKMK_mspp_publishingstateidName)
- [mspp_weblinksetidName](#BKMK_mspp_weblinksetidName)


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


### <a name="BKMK_mspp_pageidName"></a> mspp_pageidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_pageidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_parentweblinkidName"></a> mspp_parentweblinkidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_parentweblinkidname|
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


### <a name="BKMK_mspp_weblinksetidName"></a> mspp_weblinksetidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_weblinksetidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_mspp_weblink_weblink"></a> mspp_weblink_weblink

Same as the [mspp_weblink_weblink](mspp_weblink.md#BKMK_mspp_weblink_weblink) many-to-one relationship for the [mspp_weblink](mspp_weblink.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_weblink|
|ReferencingAttribute|mspp_parentweblinkid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_weblink_weblink|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Child Links<br />Order: 100500|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_publishingstate_weblink](#BKMK_mspp_publishingstate_weblink)
- [mspp_systemuser_mspp_weblink_createdby](#BKMK_mspp_systemuser_mspp_weblink_createdby)
- [mspp_systemuser_mspp_weblink_modifiedby](#BKMK_mspp_systemuser_mspp_weblink_modifiedby)
- [mspp_weblink_weblink](#BKMK_mspp_weblink_weblink)
- [mspp_weblinkset_weblink](#BKMK_mspp_weblinkset_weblink)
- [mspp_webpage_weblink](#BKMK_mspp_webpage_weblink)


### <a name="BKMK_mspp_publishingstate_weblink"></a> mspp_publishingstate_weblink

See the [mspp_publishingstate_weblink](mspp_publishingstate.md#BKMK_mspp_publishingstate_weblink) one-to-many relationship for the [mspp_publishingstate](mspp_publishingstate.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_weblink_createdby"></a> mspp_systemuser_mspp_weblink_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_weblink_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_weblink_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_weblink_modifiedby"></a> mspp_systemuser_mspp_weblink_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_weblink_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_weblink_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_weblink_weblink"></a> mspp_weblink_weblink

See the [mspp_weblink_weblink](mspp_weblink.md#BKMK_mspp_weblink_weblink) one-to-many relationship for the [mspp_weblink](mspp_weblink.md) table/entity.

### <a name="BKMK_mspp_weblinkset_weblink"></a> mspp_weblinkset_weblink

See the [mspp_weblinkset_weblink](mspp_weblinkset.md#BKMK_mspp_weblinkset_weblink) one-to-many relationship for the [mspp_weblinkset](mspp_weblinkset.md) table/entity.

### <a name="BKMK_mspp_webpage_weblink"></a> mspp_webpage_weblink

See the [mspp_webpage_weblink](mspp_webpage.md#BKMK_mspp_webpage_weblink) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_weblink?text=mspp_weblink EntityType" />