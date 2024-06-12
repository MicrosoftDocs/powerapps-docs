---
title: "Multistep Form (mspp_webform)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Multistep Form (mspp_webform)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Multistep Form (mspp_webform)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Defines the necessary properties and relationships to the other key entities in order to control the initialization of the form within a web portal.

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_webforms<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_webforms(*mspp_webformid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_webforms(*mspp_webformid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_webforms<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_webforms(*mspp_webformid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_webforms|
|DisplayCollectionName|Multistep Forms|
|DisplayName|Multistep Form|
|EntitySetName|mspp_webforms|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_webforms|
|LogicalName|mspp_webform|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_webformid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_webform|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_authenticationrequired](#BKMK_mspp_authenticationrequired)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_editexistingrecordpermitted](#BKMK_mspp_editexistingrecordpermitted)
- [mspp_editexpiredmessage](#BKMK_mspp_editexpiredmessage)
- [mspp_editexpiredstatecode](#BKMK_mspp_editexpiredstatecode)
- [mspp_editexpiredstatuscode](#BKMK_mspp_editexpiredstatuscode)
- [mspp_editnotpermittedmessage](#BKMK_mspp_editnotpermittedmessage)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_multiplerecordsperuserpermitted](#BKMK_mspp_multiplerecordsperuserpermitted)
- [mspp_name](#BKMK_mspp_name)
- [mspp_progressindicatorenabled](#BKMK_mspp_progressindicatorenabled)
- [mspp_progressindicatorignorelaststep](#BKMK_mspp_progressindicatorignorelaststep)
- [mspp_progressindicatorposition](#BKMK_mspp_progressindicatorposition)
- [mspp_progressindicatorprependstepnum](#BKMK_mspp_progressindicatorprependstepnum)
- [mspp_progressindicatortype](#BKMK_mspp_progressindicatortype)
- [mspp_provisionedlanguages](#BKMK_mspp_provisionedlanguages)
- [mspp_savechangeswarningmessage](#BKMK_mspp_savechangeswarningmessage)
- [mspp_savechangeswarningonclose](#BKMK_mspp_savechangeswarningonclose)
- [mspp_startnewsessiononload](#BKMK_mspp_startnewsessiononload)
- [mspp_startstep](#BKMK_mspp_startstep)
- [mspp_webformId](#BKMK_mspp_webformId)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)


### <a name="BKMK_mspp_authenticationrequired"></a> mspp_authenticationrequired

|Property|Value|
|--------|-----|
|Description|Redirect to sign in if the user is anonymous.|
|DisplayName|Authentication Required|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_authenticationrequired|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_authenticationrequired Choices/Options

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


### <a name="BKMK_mspp_editexistingrecordpermitted"></a> mspp_editexistingrecordpermitted

|Property|Value|
|--------|-----|
|Description|Determines if an existing record can be edited. This setting is ignored If the form mode on the form step is set to edit mode. Otherwise, an edit form wouldn't function properly.|
|DisplayName|Edit Existing Record Permitted|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_editexistingrecordpermitted|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_editexistingrecordpermitted Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_mspp_editexpiredmessage"></a> mspp_editexpiredmessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Edit Expired Message|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_editexpiredmessage|
|MaxLength|10000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_editexpiredstatecode"></a> mspp_editexpiredstatecode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Edit Expired State Code|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_editexpiredstatecode|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_editexpiredstatuscode"></a> mspp_editexpiredstatuscode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Edit Expired Status Code|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_editexpiredstatuscode|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_editnotpermittedmessage"></a> mspp_editnotpermittedmessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Edit Not Permitted Message|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_editnotpermittedmessage|
|MaxLength|10000|
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


### <a name="BKMK_mspp_multiplerecordsperuserpermitted"></a> mspp_multiplerecordsperuserpermitted

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Multiple Records Per User Permitted|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_multiplerecordsperuserpermitted|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_multiplerecordsperuserpermitted Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



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


### <a name="BKMK_mspp_progressindicatorenabled"></a> mspp_progressindicatorenabled

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Enabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_progressindicatorenabled|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_progressindicatorenabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_progressindicatorignorelaststep"></a> mspp_progressindicatorignorelaststep

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Ignore Last Step In Progress Count|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_progressindicatorignorelaststep|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_progressindicatorignorelaststep Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_progressindicatorposition"></a> mspp_progressindicatorposition

|Property|Value|
|--------|-----|
|Description|Location of the progress indicator relative to the form|
|DisplayName|Position|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_progressindicatorposition|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_progressindicatorposition Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Top||
|756150001|Bottom||
|756150002|Left||
|756150003|Right||



### <a name="BKMK_mspp_progressindicatorprependstepnum"></a> mspp_progressindicatorprependstepnum

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Prepend Step Number to Step Title|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_progressindicatorprependstepnum|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_progressindicatorprependstepnum Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_progressindicatortype"></a> mspp_progressindicatortype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_progressindicatortype|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_progressindicatortype Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Title||
|756150001|Numeric (Step 1 of N)||
|756150002|Progress Bar||



### <a name="BKMK_mspp_provisionedlanguages"></a> mspp_provisionedlanguages

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Provisioned Languages|
|Format|Language|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_provisionedlanguages|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_savechangeswarningmessage"></a> mspp_savechangeswarningmessage

|Property|Value|
|--------|-----|
|Description|Default message: Your changes have not been saved. To stay on the page so that you can save your changes, click Cancel.|
|DisplayName|Save Changes Warning Message|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_savechangeswarningmessage|
|MaxLength|10000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_savechangeswarningonclose"></a> mspp_savechangeswarningonclose

|Property|Value|
|--------|-----|
|Description|Displays a warning message to the user if they close the browser, or refresh the page, or click the previous button in a multiple step form and they have changes that haven't been saved.|
|DisplayName|Display Save Changes Warning On Close|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_savechangeswarningonclose|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_savechangeswarningonclose Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_startnewsessiononload"></a> mspp_startnewsessiononload

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Start New Session On Load|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_startnewsessiononload|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_startnewsessiononload Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_startstep"></a> mspp_startstep

|Property|Value|
|--------|-----|
|Description|Unique identifier for Form Step associated with Multistep Form.|
|DisplayName|Start Step|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_startstep|
|RequiredLevel|None|
|Targets|mspp_webformstep|
|Type|Lookup|


### <a name="BKMK_mspp_webformId"></a> mspp_webformId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Multistep Form|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_webformid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Unique identifier for Website entity associated with this record|
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
|Description|Status of the Multistep Form|
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
|Description|Reason for the status of the Multistep Form|
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
- [mspp_startstepName](#BKMK_mspp_startstepName)
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


### <a name="BKMK_mspp_startstepName"></a> mspp_startstepName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_startstepname|
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

- [mspp_webform_webformmetadata_entityformforcreate](#BKMK_mspp_webform_webformmetadata_entityformforcreate)
- [mspp_webformstep_webform](#BKMK_mspp_webformstep_webform)
- [mspp_webpage_webform](#BKMK_mspp_webpage_webform)


### <a name="BKMK_mspp_webform_webformmetadata_entityformforcreate"></a> mspp_webform_webformmetadata_entityformforcreate

Same as the [mspp_webform_webformmetadata_entityformforcreate](mspp_webformmetadata.md#BKMK_mspp_webform_webformmetadata_entityformforcreate) many-to-one relationship for the [mspp_webformmetadata](mspp_webformmetadata.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webformmetadata|
|ReferencingAttribute|mspp_entityformforcreate|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webform_webformmetadata_entityformforcreate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webformstep_webform"></a> mspp_webformstep_webform

Same as the [mspp_webformstep_webform](mspp_webformstep.md#BKMK_mspp_webformstep_webform) many-to-one relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webformstep|
|ReferencingAttribute|mspp_webform|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webformstep_webform|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Steps<br />Order: 103100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_webpage_webform"></a> mspp_webpage_webform

Same as the [mspp_webpage_webform](mspp_webpage.md#BKMK_mspp_webpage_webform) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_webform|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_webpage_webform|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 107000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_systemuser_mspp_webform_createdby](#BKMK_mspp_systemuser_mspp_webform_createdby)
- [mspp_systemuser_mspp_webform_modifiedby](#BKMK_mspp_systemuser_mspp_webform_modifiedby)
- [mspp_webform_startstep](#BKMK_mspp_webform_startstep)
- [mspp_website_webform](#BKMK_mspp_website_webform)


### <a name="BKMK_mspp_systemuser_mspp_webform_createdby"></a> mspp_systemuser_mspp_webform_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webform_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webform_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_webform_modifiedby"></a> mspp_systemuser_mspp_webform_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webform_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webform_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_webform_startstep"></a> mspp_webform_startstep

See the [mspp_webform_startstep](mspp_webformstep.md#BKMK_mspp_webform_startstep) one-to-many relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

### <a name="BKMK_mspp_website_webform"></a> mspp_website_webform

See the [mspp_website_webform](mspp_website.md#BKMK_mspp_website_webform) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_webform?text=mspp_webform EntityType" />