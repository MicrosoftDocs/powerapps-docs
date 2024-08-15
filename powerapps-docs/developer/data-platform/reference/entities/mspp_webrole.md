---
title: "Web Role (mspp_webrole)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Web Role (mspp_webrole)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Web Role (mspp_webrole)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Sets the user's role for the Portal.

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_webroles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_webroles(*mspp_webroleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_webroles(*mspp_webroleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_webroles<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_webroles(*mspp_webroleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_webroles|
|DisplayCollectionName|Web Roles|
|DisplayName|Web Role|
|EntitySetName|mspp_webroles|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_webroles|
|LogicalName|mspp_webrole|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_webroleid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_webrole|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_anonymoususersrole](#BKMK_mspp_anonymoususersrole)
- [mspp_authenticatedusersrole](#BKMK_mspp_authenticatedusersrole)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_description](#BKMK_mspp_description)
- [mspp_key](#BKMK_mspp_key)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_webroleId](#BKMK_mspp_webroleId)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)


### <a name="BKMK_mspp_anonymoususersrole"></a> mspp_anonymoususersrole

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Anonymous Users Role|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_anonymoususersrole|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_anonymoususersrole Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_authenticatedusersrole"></a> mspp_authenticatedusersrole

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Authenticated Users Role|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_authenticatedusersrole|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_authenticatedusersrole Choices/Options

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


### <a name="BKMK_mspp_key"></a> mspp_key

|Property|Value|
|--------|-----|
|Description|An alternate key that is not intended to be localized to allow retrieval of a specific Web Role in workflows or code.|
|DisplayName|Key|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_key|
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


### <a name="BKMK_mspp_webroleId"></a> mspp_webroleId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Web Role|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_webroleid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Web Role.|
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
|Description|Status of the Web Role|
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
|Description|Reason for the status of the Web Role|
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

- [mspp_systemuser_mspp_webrole_createdby](#BKMK_mspp_systemuser_mspp_webrole_createdby)
- [mspp_systemuser_mspp_webrole_modifiedby](#BKMK_mspp_systemuser_mspp_webrole_modifiedby)
- [mspp_website_webrole](#BKMK_mspp_website_webrole)


### <a name="BKMK_mspp_systemuser_mspp_webrole_createdby"></a> mspp_systemuser_mspp_webrole_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webrole_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webrole_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_webrole_modifiedby"></a> mspp_systemuser_mspp_webrole_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webrole_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webrole_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_website_webrole"></a> mspp_website_webrole

See the [mspp_website_webrole](mspp_website.md#BKMK_mspp_website_webrole) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the mspp_webrole table is the first table in the relationship. Listed by **SchemaName**.

- [mspp_columnpermissionprofile_webrole](#BKMK_mspp_columnpermissionprofile_webrole)
- [mspp_entitypermission_webrole](#BKMK_mspp_entitypermission_webrole)
- [mspp_publishingstatetransitionrule_webrole](#BKMK_mspp_publishingstatetransitionrule_webrole)
- [mspp_webpageaccesscontrolrule_webrole](#BKMK_mspp_webpageaccesscontrolrule_webrole)
- [mspp_websiteaccess_webrole](#BKMK_mspp_websiteaccess_webrole)


### <a name="BKMK_mspp_columnpermissionprofile_webrole"></a> mspp_columnpermissionprofile_webrole

IntersectEntityName: mspp_columnpermissionprofile_webrole<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|mspp_webroleid|
|IsCustomizable|False|
|LogicalName|mspp_webrole|
|NavigationPropertyName|mspp_columnpermissionprofile_webrole|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|mspp_columnpermissionprofile|
|IntersectAttribute|mspp_columnpermissionprofileid|
|NavigationPropertyName|mspp_columnpermissionprofile_webrole|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|


### <a name="BKMK_mspp_entitypermission_webrole"></a> mspp_entitypermission_webrole

See the [mspp_entitypermission_webrole](mspp_entitypermission.md#BKMK_mspp_entitypermission_webrole) many-to-many relationship for the [mspp_entitypermission](mspp_entitypermission.md) table/entity.

### <a name="BKMK_mspp_publishingstatetransitionrule_webrole"></a> mspp_publishingstatetransitionrule_webrole

See the [mspp_publishingstatetransitionrule_webrole](mspp_publishingstatetransitionrule.md#BKMK_mspp_publishingstatetransitionrule_webrole) many-to-many relationship for the [mspp_publishingstatetransitionrule](mspp_publishingstatetransitionrule.md) table/entity.

### <a name="BKMK_mspp_webpageaccesscontrolrule_webrole"></a> mspp_webpageaccesscontrolrule_webrole

See the [mspp_webpageaccesscontrolrule_webrole](mspp_webpageaccesscontrolrule.md#BKMK_mspp_webpageaccesscontrolrule_webrole) many-to-many relationship for the [mspp_webpageaccesscontrolrule](mspp_webpageaccesscontrolrule.md) table/entity.

### <a name="BKMK_mspp_websiteaccess_webrole"></a> mspp_websiteaccess_webrole

See the [mspp_websiteaccess_webrole](mspp_websiteaccess.md#BKMK_mspp_websiteaccess_webrole) many-to-many relationship for the [mspp_websiteaccess](mspp_websiteaccess.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_webrole?text=mspp_webrole EntityType" />