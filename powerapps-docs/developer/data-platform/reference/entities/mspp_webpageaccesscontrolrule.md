---
title: "Web Page Access Control Rule (mspp_webpageaccesscontrolrule)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Web Page Access Control Rule (mspp_webpageaccesscontrolrule)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Web Page Access Control Rule (mspp_webpageaccesscontrolrule)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_webpageaccesscontrolrules<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_webpageaccesscontrolrules(*mspp_webpageaccesscontrolruleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_webpageaccesscontrolrules(*mspp_webpageaccesscontrolruleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_webpageaccesscontrolrules<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_webpageaccesscontrolrules(*mspp_webpageaccesscontrolruleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_webpageaccesscontrolrules|
|DisplayCollectionName|Web Page Access Control Rules|
|DisplayName|Web Page Access Control Rule|
|EntitySetName|mspp_webpageaccesscontrolrules|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_webpageaccesscontrolrules|
|LogicalName|mspp_webpageaccesscontrolrule|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_webpageaccesscontrolruleid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_webpageaccesscontrolrule|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_description](#BKMK_mspp_description)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_right](#BKMK_mspp_right)
- [mspp_scope](#BKMK_mspp_scope)
- [mspp_webpageaccesscontrolruleId](#BKMK_mspp_webpageaccesscontrolruleId)
- [mspp_webpageid](#BKMK_mspp_webpageid)
- [mspp_websiteid](#BKMK_mspp_websiteid)
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
|RequiredLevel|None|
|Type|Memo|


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
|MaxLength|200|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_right"></a> mspp_right

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Right|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_right|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### mspp_right Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Grant Change||
|2|Restrict Read||



### <a name="BKMK_mspp_scope"></a> mspp_scope

|Property|Value|
|--------|-----|
|Description|All child web files directly related to this web page will be excluded from security validation. This does not exclude the children's descendants.|
|DisplayName|Access Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_scope|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### mspp_scope Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|All content||
|2|Exclude direct child web files||



### <a name="BKMK_mspp_webpageaccesscontrolruleId"></a> mspp_webpageaccesscontrolruleId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Webpage Access Control Rule|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_webpageaccesscontrolruleid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_webpageid"></a> mspp_webpageid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Page associated with Web Page Access Control Rule.|
|DisplayName|Web Page|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webpageid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_webpage|
|Type|Lookup|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Web Page Access Control Rule.|
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
|Description|Status of the Web Page Access Control Rule|
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
|Description|Reason for the status of the Web Page Access Control Rule|
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
- [mspp_webpageidName](#BKMK_mspp_webpageidName)
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


### <a name="BKMK_mspp_webpageidName"></a> mspp_webpageidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_webpageidname|
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_systemuser_mspp_webpageaccesscontrolrule_createdby](#BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_createdby)
- [mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby](#BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby)
- [mspp_webpage_webpageaccesscontrolrule](#BKMK_mspp_webpage_webpageaccesscontrolrule)
- [mspp_website_webpageaccesscontrolrule](#BKMK_mspp_website_webpageaccesscontrolrule)


### <a name="BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_createdby"></a> mspp_systemuser_mspp_webpageaccesscontrolrule_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webpageaccesscontrolrule_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby"></a> mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_webpage_webpageaccesscontrolrule"></a> mspp_webpage_webpageaccesscontrolrule

See the [mspp_webpage_webpageaccesscontrolrule](mspp_webpage.md#BKMK_mspp_webpage_webpageaccesscontrolrule) one-to-many relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

### <a name="BKMK_mspp_website_webpageaccesscontrolrule"></a> mspp_website_webpageaccesscontrolrule

See the [mspp_website_webpageaccesscontrolrule](mspp_website.md#BKMK_mspp_website_webpageaccesscontrolrule) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the mspp_webpageaccesscontrolrule table is the first table in the relationship. Listed by **SchemaName**.

- [mspp_accesscontrolrule_publishingstate](#BKMK_mspp_accesscontrolrule_publishingstate)
- [mspp_webpageaccesscontrolrule_webrole](#BKMK_mspp_webpageaccesscontrolrule_webrole)


### <a name="BKMK_mspp_accesscontrolrule_publishingstate"></a> mspp_accesscontrolrule_publishingstate

IntersectEntityName: mspp_accesscontrolrule_publishingstate<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|mspp_webpageaccesscontrolruleid|
|IsCustomizable|False|
|LogicalName|mspp_webpageaccesscontrolrule|
|NavigationPropertyName|mspp_accesscontrolrule_publishingstate|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|mspp_publishingstate|
|IntersectAttribute|mspp_publishingstateid|
|NavigationPropertyName|mspp_accesscontrolrule_publishingstate|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|


### <a name="BKMK_mspp_webpageaccesscontrolrule_webrole"></a> mspp_webpageaccesscontrolrule_webrole

IntersectEntityName: mspp_webpageaccesscontrolrule_webrole<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|mspp_webpageaccesscontrolruleid|
|IsCustomizable|False|
|LogicalName|mspp_webpageaccesscontrolrule|
|NavigationPropertyName|mspp_webpageaccesscontrolrule_webrole|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|mspp_webrole|
|IntersectAttribute|mspp_webroleid|
|NavigationPropertyName|mspp_webpageaccesscontrolrule_webrole|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|


### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_webpageaccesscontrolrule?text=mspp_webpageaccesscontrolrule EntityType" />