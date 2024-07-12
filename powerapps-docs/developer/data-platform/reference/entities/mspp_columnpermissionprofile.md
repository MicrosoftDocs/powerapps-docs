---
title: "Column Permission Profile (mspp_columnpermissionprofile)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Column Permission Profile (mspp_columnpermissionprofile)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Column Permission Profile (mspp_columnpermissionprofile)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_columnpermissionprofiles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_columnpermissionprofiles(*mspp_columnpermissionprofileid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_columnpermissionprofiles(*mspp_columnpermissionprofileid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_columnpermissionprofiles<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_columnpermissionprofiles(*mspp_columnpermissionprofileid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_columnpermissionprofiles|
|DisplayCollectionName|Column Permission Profiles|
|DisplayName|Column Permission Profile|
|EntitySetName|mspp_columnpermissionprofiles|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_columnpermissionprofiles|
|LogicalName|mspp_columnpermissionprofile|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_columnpermissionprofileid|
|PrimaryNameAttribute|mspp_profilename|
|SchemaName|mspp_columnpermissionprofile|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_allcolumnpermissions](#BKMK_mspp_allcolumnpermissions)
- [mspp_columnpermissionprofileId](#BKMK_mspp_columnpermissionprofileId)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_profilename](#BKMK_mspp_profilename)
- [mspp_tablename](#BKMK_mspp_tablename)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)


### <a name="BKMK_mspp_allcolumnpermissions"></a> mspp_allcolumnpermissions

|Property|Value|
|--------|-----|
|Description||
|DisplayName|All Column Permissions|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_allcolumnpermissions|
|RequiredLevel|None|
|Type|MultiSelectPicklist|

#### mspp_allcolumnpermissions Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|746610000|Create||
|746610001|Read||
|746610002|Update||



### <a name="BKMK_mspp_columnpermissionprofileId"></a> mspp_columnpermissionprofileId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Column Permission Profile|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_columnpermissionprofileid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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


### <a name="BKMK_mspp_profilename"></a> mspp_profilename

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Profile Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_profilename|
|MaxLength|400|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_tablename"></a> mspp_tablename

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Table Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_tablename|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description||
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
|Description|Status of the Column Permission Profile|
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
|Description|Reason for the status of the Column Permission Profile|
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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_mspp_columnpermission_columnpermissionprofile"></a> mspp_columnpermission_columnpermissionprofile

Same as the [mspp_columnpermission_columnpermissionprofile](mspp_columnpermission.md#BKMK_mspp_columnpermission_columnpermissionprofile) many-to-one relationship for the [mspp_columnpermission](mspp_columnpermission.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_columnpermission|
|ReferencingAttribute|mspp_columnpermissionprofileid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_columnpermission_columnpermissionprofile|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_columnpermissionprofile_website](#BKMK_mspp_columnpermissionprofile_website)
- [mspp_systemuser_mspp_columnpermissionprofile_createdby](#BKMK_mspp_systemuser_mspp_columnpermissionprofile_createdby)
- [mspp_systemuser_mspp_columnpermissionprofile_modifiedby](#BKMK_mspp_systemuser_mspp_columnpermissionprofile_modifiedby)


### <a name="BKMK_mspp_columnpermissionprofile_website"></a> mspp_columnpermissionprofile_website

See the [mspp_columnpermissionprofile_website](mspp_website.md#BKMK_mspp_columnpermissionprofile_website) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_columnpermissionprofile_createdby"></a> mspp_systemuser_mspp_columnpermissionprofile_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_columnpermissionprofile_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_columnpermissionprofile_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_columnpermissionprofile_modifiedby"></a> mspp_systemuser_mspp_columnpermissionprofile_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_columnpermissionprofile_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_columnpermissionprofile_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the mspp_columnpermissionprofile table is the first table in the relationship. Listed by **SchemaName**.


### <a name="BKMK_mspp_columnpermissionprofile_webrole"></a> mspp_columnpermissionprofile_webrole

See the [mspp_columnpermissionprofile_webrole](mspp_webrole.md#BKMK_mspp_columnpermissionprofile_webrole) many-to-many relationship for the [mspp_webrole](mspp_webrole.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_columnpermissionprofile?text=mspp_columnpermissionprofile EntityType" />