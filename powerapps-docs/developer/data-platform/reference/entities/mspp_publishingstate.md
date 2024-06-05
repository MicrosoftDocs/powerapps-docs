---
title: "Publishing State (mspp_publishingstate)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Publishing State (mspp_publishingstate)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Publishing State (mspp_publishingstate)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_publishingstates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_publishingstates(*mspp_publishingstateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_publishingstates(*mspp_publishingstateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_publishingstates<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_publishingstates(*mspp_publishingstateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_publishingstates|
|DisplayCollectionName|Publishing States|
|DisplayName|Publishing State|
|EntitySetName|mspp_publishingstates|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_publishingstates|
|LogicalName|mspp_publishingstate|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_publishingstateid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_publishingstate|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_displayorder](#BKMK_mspp_displayorder)
- [mspp_isdefault](#BKMK_mspp_isdefault)
- [mspp_isvisible](#BKMK_mspp_isvisible)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_publishingstateId](#BKMK_mspp_publishingstateId)
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
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_mspp_isdefault"></a> mspp_isdefault

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Is Default|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_isdefault|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### mspp_isdefault Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_isvisible"></a> mspp_isvisible

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Select whether the publishing state is visible.|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_isvisible|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### mspp_isvisible Choices/Options

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


### <a name="BKMK_mspp_publishingstateId"></a> mspp_publishingstateId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Publishing State|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_publishingstateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website associated with Publishing State.|
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
|Description|Status of the Publishing State|
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
|Description|Reason for the status of the Publishing State|
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

- [mspp_frompublishingstate_statetransition](#BKMK_mspp_frompublishingstate_statetransition)
- [mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState](#BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState)
- [mspp_publishingstate_webfile](#BKMK_mspp_publishingstate_webfile)
- [mspp_publishingstate_weblink](#BKMK_mspp_publishingstate_weblink)
- [mspp_publishingstate_weblinkset](#BKMK_mspp_publishingstate_weblinkset)
- [mspp_publishingstate_webpage](#BKMK_mspp_publishingstate_webpage)
- [mspp_topublishingstate_statetransition](#BKMK_mspp_topublishingstate_statetransition)


### <a name="BKMK_mspp_frompublishingstate_statetransition"></a> mspp_frompublishingstate_statetransition

Same as the [mspp_frompublishingstate_statetransition](mspp_publishingstatetransitionrule.md#BKMK_mspp_frompublishingstate_statetransition) many-to-one relationship for the [mspp_publishingstatetransitionrule](mspp_publishingstatetransitionrule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_publishingstatetransitionrule|
|ReferencingAttribute|mspp_fromstate_publishingstateid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_frompublishingstate_statetransition|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState"></a> mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState

Same as the [mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState](mspp_websitelanguage.md#BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState) many-to-one relationship for the [mspp_websitelanguage](mspp_websitelanguage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_websitelanguage|
|ReferencingAttribute|mspp_publishingstate|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstate_webfile"></a> mspp_publishingstate_webfile

Same as the [mspp_publishingstate_webfile](mspp_webfile.md#BKMK_mspp_publishingstate_webfile) many-to-one relationship for the [mspp_webfile](mspp_webfile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webfile|
|ReferencingAttribute|mspp_publishingstateid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_publishingstate_webfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstate_weblink"></a> mspp_publishingstate_weblink

Same as the [mspp_publishingstate_weblink](mspp_weblink.md#BKMK_mspp_publishingstate_weblink) many-to-one relationship for the [mspp_weblink](mspp_weblink.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_weblink|
|ReferencingAttribute|mspp_publishingstateid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_publishingstate_weblink|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstate_weblinkset"></a> mspp_publishingstate_weblinkset

Same as the [mspp_publishingstate_weblinkset](mspp_weblinkset.md#BKMK_mspp_publishingstate_weblinkset) many-to-one relationship for the [mspp_weblinkset](mspp_weblinkset.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_weblinkset|
|ReferencingAttribute|mspp_publishingstateid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_publishingstate_weblinkset|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_publishingstate_webpage"></a> mspp_publishingstate_webpage

Same as the [mspp_publishingstate_webpage](mspp_webpage.md#BKMK_mspp_publishingstate_webpage) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_publishingstateid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_publishingstate_webpage|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_topublishingstate_statetransition"></a> mspp_topublishingstate_statetransition

Same as the [mspp_topublishingstate_statetransition](mspp_publishingstatetransitionrule.md#BKMK_mspp_topublishingstate_statetransition) many-to-one relationship for the [mspp_publishingstatetransitionrule](mspp_publishingstatetransitionrule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_publishingstatetransitionrule|
|ReferencingAttribute|mspp_tostate_publishingstateid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_topublishingstate_statetransition|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_systemuser_mspp_publishingstate_createdby](#BKMK_mspp_systemuser_mspp_publishingstate_createdby)
- [mspp_systemuser_mspp_publishingstate_modifiedby](#BKMK_mspp_systemuser_mspp_publishingstate_modifiedby)
- [mspp_website_publishingstate](#BKMK_mspp_website_publishingstate)


### <a name="BKMK_mspp_systemuser_mspp_publishingstate_createdby"></a> mspp_systemuser_mspp_publishingstate_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_publishingstate_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_publishingstate_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_publishingstate_modifiedby"></a> mspp_systemuser_mspp_publishingstate_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_publishingstate_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_publishingstate_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_website_publishingstate"></a> mspp_website_publishingstate

See the [mspp_website_publishingstate](mspp_website.md#BKMK_mspp_website_publishingstate) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the mspp_publishingstate table is the first table in the relationship. Listed by **SchemaName**.


### <a name="BKMK_mspp_accesscontrolrule_publishingstate"></a> mspp_accesscontrolrule_publishingstate

See the [mspp_accesscontrolrule_publishingstate](mspp_webpageaccesscontrolrule.md#BKMK_mspp_accesscontrolrule_publishingstate) many-to-many relationship for the [mspp_webpageaccesscontrolrule](mspp_webpageaccesscontrolrule.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_publishingstate?text=mspp_publishingstate EntityType" />