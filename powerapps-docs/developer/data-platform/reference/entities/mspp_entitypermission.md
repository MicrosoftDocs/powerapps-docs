---
title: "Table Permission (mspp_entitypermission)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Table Permission (mspp_entitypermission)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Table Permission (mspp_entitypermission)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_entitypermissions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_entitypermissions(*mspp_entitypermissionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_entitypermissions(*mspp_entitypermissionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_entitypermissions<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_entitypermissions(*mspp_entitypermissionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_entitypermissions|
|DisplayCollectionName|Table Permissions|
|DisplayName|Table Permission|
|EntitySetName|mspp_entitypermissions|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_entitypermissions|
|LogicalName|mspp_entitypermission|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_entitypermissionid|
|PrimaryNameAttribute|mspp_entityname|
|SchemaName|mspp_entitypermission|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_accountrelationship](#BKMK_mspp_accountrelationship)
- [mspp_append](#BKMK_mspp_append)
- [mspp_appendto](#BKMK_mspp_appendto)
- [mspp_contactrelationship](#BKMK_mspp_contactrelationship)
- [mspp_create](#BKMK_mspp_create)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_delete](#BKMK_mspp_delete)
- [mspp_entitylogicalname](#BKMK_mspp_entitylogicalname)
- [mspp_entityname](#BKMK_mspp_entityname)
- [mspp_entitypermissionId](#BKMK_mspp_entitypermissionId)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_parententitypermission](#BKMK_mspp_parententitypermission)
- [mspp_parentrelationship](#BKMK_mspp_parentrelationship)
- [mspp_read](#BKMK_mspp_read)
- [mspp_scope](#BKMK_mspp_scope)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [mspp_write](#BKMK_mspp_write)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)


### <a name="BKMK_mspp_accountrelationship"></a> mspp_accountrelationship

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Account Relationship|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_accountrelationship|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_append"></a> mspp_append

|Property|Value|
|--------|-----|
|Description|Controls whether the user can attach another record to the specified record. The Append and Append To permissions work in combination.|
|DisplayName|Append|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_append|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_append Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_appendto"></a> mspp_appendto

|Property|Value|
|--------|-----|
|Description|Controls whether the user can append the specified record to another record. The Append and Append To permissions work in combination.|
|DisplayName|Append To|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_appendto|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_appendto Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_contactrelationship"></a> mspp_contactrelationship

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Contact Relationship|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_contactrelationship|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_create"></a> mspp_create

|Property|Value|
|--------|-----|
|Description|The Create privilege controls whether you can create a record.|
|DisplayName|Create|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_create|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_create Choices/Options

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


### <a name="BKMK_mspp_delete"></a> mspp_delete

|Property|Value|
|--------|-----|
|Description|Controls whether the user can delete a record.|
|DisplayName|Delete|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_delete|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_delete Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_entitylogicalname"></a> mspp_entitylogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Table Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_entitylogicalname|
|MaxLength|250|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_entityname"></a> mspp_entityname

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_entityname|
|MaxLength|400|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_entitypermissionId"></a> mspp_entitypermissionId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Table Permission|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_entitypermissionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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


### <a name="BKMK_mspp_parententitypermission"></a> mspp_parententitypermission

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Parent Table Permission|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_parententitypermission|
|RequiredLevel|None|
|Targets|mspp_entitypermission|
|Type|Lookup|


### <a name="BKMK_mspp_parentrelationship"></a> mspp_parentrelationship

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Parent Relationship|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_parentrelationship|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_read"></a> mspp_read

|Property|Value|
|--------|-----|
|Description|Controls whether the user can read a record.|
|DisplayName|Read|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_read|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_read Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_scope"></a> mspp_scope

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Access Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_scope|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### mspp_scope Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Global||
|756150001|Contact||
|756150002|Account||
|756150003|Parent||
|756150004|Self||



### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Entity Permission|
|DisplayName|Website|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_websiteid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_website|
|Type|Lookup|


### <a name="BKMK_mspp_write"></a> mspp_write

|Property|Value|
|--------|-----|
|Description|Controls whether the user can update a record.|
|DisplayName|Write|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_write|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_write Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Table Permission|
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
|Description|Reason for the status of the Table Permission|
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
- [mspp_parententitypermissionName](#BKMK_mspp_parententitypermissionName)
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


### <a name="BKMK_mspp_parententitypermissionName"></a> mspp_parententitypermissionName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_parententitypermissionname|
|MaxLength|400|
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


### <a name="BKMK_mspp_entitypermission_parententitypermission"></a> mspp_entitypermission_parententitypermission

Same as the [mspp_entitypermission_parententitypermission](mspp_entitypermission.md#BKMK_mspp_entitypermission_parententitypermission) many-to-one relationship for the [mspp_entitypermission](mspp_entitypermission.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_entitypermission|
|ReferencingAttribute|mspp_parententitypermission|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_entitypermission_parententitypermission|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_entitypermission_parententitypermission](#BKMK_mspp_entitypermission_parententitypermission)
- [mspp_systemuser_mspp_entitypermission_createdby](#BKMK_mspp_systemuser_mspp_entitypermission_createdby)
- [mspp_systemuser_mspp_entitypermission_modifiedby](#BKMK_mspp_systemuser_mspp_entitypermission_modifiedby)
- [mspp_website_mspp_entitypermission](#BKMK_mspp_website_mspp_entitypermission)


### <a name="BKMK_mspp_entitypermission_parententitypermission"></a> mspp_entitypermission_parententitypermission

See the [mspp_entitypermission_parententitypermission](mspp_entitypermission.md#BKMK_mspp_entitypermission_parententitypermission) one-to-many relationship for the [mspp_entitypermission](mspp_entitypermission.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_entitypermission_createdby"></a> mspp_systemuser_mspp_entitypermission_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_entitypermission_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_entitypermission_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_entitypermission_modifiedby"></a> mspp_systemuser_mspp_entitypermission_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_entitypermission_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_entitypermission_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_website_mspp_entitypermission"></a> mspp_website_mspp_entitypermission

See the [mspp_website_mspp_entitypermission](mspp_website.md#BKMK_mspp_website_mspp_entitypermission) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the mspp_entitypermission table is the first table in the relationship. Listed by **SchemaName**.


### <a name="BKMK_mspp_entitypermission_webrole"></a> mspp_entitypermission_webrole

IntersectEntityName: mspp_entitypermission_webrole<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|mspp_entitypermissionid|
|IsCustomizable|False|
|LogicalName|mspp_entitypermission|
|NavigationPropertyName|mspp_entitypermission_webrole|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|mspp_webrole|
|IntersectAttribute|mspp_webroleid|
|NavigationPropertyName|mspp_entitypermission_webrole|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|


### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_entitypermission?text=mspp_entitypermission EntityType" />