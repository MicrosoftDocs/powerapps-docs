---
title: "Multistep Form Metadata (mspp_webformmetadata) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Multistep Form Metadata (mspp_webformmetadata) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Multistep Form Metadata (mspp_webformmetadata) table/entity reference (Microsoft Dataverse)

Defines the additional behavior modification logic to augment or override the functionality of form fields that is not possible with Dynamics 365 entity and form metadata.

## Messages

The following table lists the messages for the Multistep Form Metadata (mspp_webformmetadata) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_webformmetadatas<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_webformmetadatas(*mspp_webformmetadataid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_webformmetadatas(*mspp_webformmetadataid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_webformmetadatas<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_webformmetadatas(*mspp_webformmetadataid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_webformmetadatas(*mspp_webformmetadataid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Multistep Form Metadata (mspp_webformmetadata) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Multistep Form Metadata (mspp_webformmetadata) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Multistep Form Metadata** |
| **DisplayCollectionName** | **Multistep Form Metadata** |
| **SchemaName** | `mspp_webformmetadata` |
| **CollectionSchemaName** | `mspp_webformmetadatas` |
| **EntitySetName** | `mspp_webformmetadatas`|
| **LogicalName** | `mspp_webformmetadata` |
| **LogicalCollectionName** | `mspp_webformmetadatas` |
| **PrimaryIdAttribute** | `mspp_webformmetadataid` |
| **PrimaryNameAttribute** |`mspp_attributelogicalname` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_adddescription](#BKMK_mspp_adddescription)
- [mspp_attributelogicalname](#BKMK_mspp_attributelogicalname)
- [mspp_constantsummaximumtotal](#BKMK_mspp_constantsummaximumtotal)
- [mspp_constantsumminimumtotal](#BKMK_mspp_constantsumminimumtotal)
- [mspp_constantsumvalidationerrormessage](#BKMK_mspp_constantsumvalidationerrormessage)
- [mspp_controlstyle](#BKMK_mspp_controlstyle)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_cssclass](#BKMK_mspp_cssclass)
- [mspp_description](#BKMK_mspp_description)
- [mspp_descriptionposition](#BKMK_mspp_descriptionposition)
- [mspp_entityformforcreate](#BKMK_mspp_entityformforcreate)
- [mspp_entityformforcreateinwebformmetadata](#BKMK_mspp_entityformforcreateinwebformmetadata)
- [mspp_fieldisrequired](#BKMK_mspp_fieldisrequired)
- [mspp_geolocationvalidatorerrormessage](#BKMK_mspp_geolocationvalidatorerrormessage)
- [mspp_groupname](#BKMK_mspp_groupname)
- [mspp_ignoredefaultvalue](#BKMK_mspp_ignoredefaultvalue)
- [mspp_label](#BKMK_mspp_label)
- [mspp_maxmultiplechoiceselectedcount](#BKMK_mspp_maxmultiplechoiceselectedcount)
- [mspp_minmultiplechoiceselectedcount](#BKMK_mspp_minmultiplechoiceselectedcount)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_multiplechoicevalidationerrormessage](#BKMK_mspp_multiplechoicevalidationerrormessage)
- [mspp_notes_settings](#BKMK_mspp_notes_settings)
- [mspp_onsavefromattribute](#BKMK_mspp_onsavefromattribute)
- [mspp_onsavetype](#BKMK_mspp_onsavetype)
- [mspp_onsavevalue](#BKMK_mspp_onsavevalue)
- [mspp_prepopulatefromattribute](#BKMK_mspp_prepopulatefromattribute)
- [mspp_prepopulatetype](#BKMK_mspp_prepopulatetype)
- [mspp_prepopulatevalue](#BKMK_mspp_prepopulatevalue)
- [mspp_provisionedlanguages](#BKMK_mspp_provisionedlanguages)
- [mspp_purchasecreateinvoiceonpayment](#BKMK_mspp_purchasecreateinvoiceonpayment)
- [mspp_purchasefulfillorderonpayment](#BKMK_mspp_purchasefulfillorderonpayment)
- [mspp_purchaselineitemdescriptionattribute](#BKMK_mspp_purchaselineitemdescriptionattribute)
- [mspp_purchaselineiteminstructionsattribute](#BKMK_mspp_purchaselineiteminstructionsattribute)
- [mspp_purchaselineitemorderattribute](#BKMK_mspp_purchaselineitemorderattribute)
- [mspp_purchaselineitemproductattribute](#BKMK_mspp_purchaselineitemproductattribute)
- [mspp_purchaselineitemquantityattribute](#BKMK_mspp_purchaselineitemquantityattribute)
- [mspp_purchaselineitemrelationship](#BKMK_mspp_purchaselineitemrelationship)
- [mspp_purchaselineitemrequiredattribute](#BKMK_mspp_purchaselineitemrequiredattribute)
- [mspp_purchaselineitemuomattribute](#BKMK_mspp_purchaselineitemuomattribute)
- [mspp_purchaseoptionalproductsrelationship](#BKMK_mspp_purchaseoptionalproductsrelationship)
- [mspp_purchasequotename](#BKMK_mspp_purchasequotename)
- [mspp_purchaserequiredproductsrelationship](#BKMK_mspp_purchaserequiredproductsrelationship)
- [mspp_purchaserequiresshipping](#BKMK_mspp_purchaserequiresshipping)
- [mspp_purchasetargetentityinvoicerelationship](#BKMK_mspp_purchasetargetentityinvoicerelationship)
- [mspp_purchasetargetentityorderrelationship](#BKMK_mspp_purchasetargetentityorderrelationship)
- [mspp_purchasetargetentityrelationship](#BKMK_mspp_purchasetargetentityrelationship)
- [mspp_randomizeoptionsetvalues](#BKMK_mspp_randomizeoptionsetvalues)
- [mspp_rangevalidationerrormessage](#BKMK_mspp_rangevalidationerrormessage)
- [mspp_rankordernotiesvalidationerrormessage](#BKMK_mspp_rankordernotiesvalidationerrormessage)
- [mspp_requiredfieldvalidationerrormessage](#BKMK_mspp_requiredfieldvalidationerrormessage)
- [mspp_sectionname](#BKMK_mspp_sectionname)
- [mspp_setvalueonsave](#BKMK_mspp_setvalueonsave)
- [mspp_subgrid_name](#BKMK_mspp_subgrid_name)
- [mspp_subgrid_settings](#BKMK_mspp_subgrid_settings)
- [mspp_tabname](#BKMK_mspp_tabname)
- [mspp_timeline_settings](#BKMK_mspp_timeline_settings)
- [mspp_type](#BKMK_mspp_type)
- [mspp_useattributedescriptionproperty](#BKMK_mspp_useattributedescriptionproperty)
- [mspp_validationerrormessage](#BKMK_mspp_validationerrormessage)
- [mspp_validationregularexpression](#BKMK_mspp_validationregularexpression)
- [mspp_validationregularexpressionerrormessage](#BKMK_mspp_validationregularexpressionerrormessage)
- [mspp_webformmetadataId](#BKMK_mspp_webformmetadataId)
- [mspp_webformstep](#BKMK_mspp_webformstep)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

### <a name="BKMK_mspp_adddescription"></a> mspp_adddescription

|Property|Value|
|---|---|
|Description||
|DisplayName|**Add Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_adddescription`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformmetadata_mspp_adddescription`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_attributelogicalname"></a> mspp_attributelogicalname

|Property|Value|
|---|---|
|Description|**The name of the attribute field to be modified.**|
|DisplayName|**Attribute Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_attributelogicalname`|
|RequiredLevel|Recommended|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_constantsummaximumtotal"></a> mspp_constantsummaximumtotal

|Property|Value|
|---|---|
|Description||
|DisplayName|**Constant Sum Maximum Total**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_constantsummaximumtotal`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_constantsumminimumtotal"></a> mspp_constantsumminimumtotal

|Property|Value|
|---|---|
|Description||
|DisplayName|**Constant Sum Minimum Total**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_constantsumminimumtotal`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_constantsumvalidationerrormessage"></a> mspp_constantsumvalidationerrormessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Constant Sum Validation Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_constantsumvalidationerrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_controlstyle"></a> mspp_controlstyle

|Property|Value|
|---|---|
|Description|**Specifies how the control should be modified or enhanced.**|
|DisplayName|**Control Style**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_controlstyle`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspp_webformmetadata_mspp_controlstyle`|

#### mspp_controlstyle Choices/Options

|Value|Label|
|---|---|
|100000000|**Option Set as Vertical Radio Button List**|
|100000001|**Option Set as Horizontal Radio Button List**|
|100000002|**Single Line of Text as Geolocation Lookup Validator**|
|100000003|**Group Whole Number as Constant Sum**|
|100000004|**Group Whole Number as Rank Order Scale No Ties**|
|100000005|**Group Whole Number as Rank Order Scale Allow Ties**|
|100000006|**Multiple Choice Matrix**|
|100000007|**Multiple Choice**|
|100000008|**Group Whole Number as Stack Rank**|
|756150000|**Render Lookup as Dropdown**|
|756150001|**Code component**|

### <a name="BKMK_mspp_createdby"></a> mspp_createdby

|Property|Value|
|---|---|
|Description|**Shows who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_mspp_createdon"></a> mspp_createdon

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_mspp_cssclass"></a> mspp_cssclass

|Property|Value|
|---|---|
|Description||
|DisplayName|**CSS Class**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_cssclass`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_description"></a> mspp_description

|Property|Value|
|---|---|
|Description||
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_mspp_descriptionposition"></a> mspp_descriptionposition

|Property|Value|
|---|---|
|Description||
|DisplayName|**Position**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_descriptionposition`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|100000000|
|GlobalChoiceName|`mspp_webformmetadata_mspp_descriptionposition`|

#### mspp_descriptionposition Choices/Options

|Value|Label|
|---|---|
|100000000|**Above the field**|
|100000001|**Below the field**|
|100000002|**Above the label**|

### <a name="BKMK_mspp_entityformforcreate"></a> mspp_entityformforcreate

|Property|Value|
|---|---|
|Description||
|DisplayName|**Basic Form for Create**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entityformforcreate`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webform|

### <a name="BKMK_mspp_entityformforcreateinwebformmetadata"></a> mspp_entityformforcreateinwebformmetadata

|Property|Value|
|---|---|
|Description||
|DisplayName|**Basic Form for Create**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entityformforcreateinwebformmetadata`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_entityform|

### <a name="BKMK_mspp_fieldisrequired"></a> mspp_fieldisrequired

|Property|Value|
|---|---|
|Description||
|DisplayName|**Field is Required**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_fieldisrequired`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformmetadata_mspp_fieldisrequired`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_geolocationvalidatorerrormessage"></a> mspp_geolocationvalidatorerrormessage

|Property|Value|
|---|---|
|Description|**The error message to be displayed when the geolocation validator validation fails.**|
|DisplayName|**Geolocation Validator Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_geolocationvalidatorerrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_groupname"></a> mspp_groupname

|Property|Value|
|---|---|
|Description|**Shows which attributes are to be grouped and rendered as a composite control if the control style is a groupings type such as "Group Whole Number as Constant Sum."**|
|DisplayName|**Group Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_groupname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_ignoredefaultvalue"></a> mspp_ignoredefaultvalue

|Property|Value|
|---|---|
|Description||
|DisplayName|**Ignore Default Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_ignoredefaultvalue`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformmetadata_mspp_ignoredefaultvalue`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_label"></a> mspp_label

|Property|Value|
|---|---|
|Description||
|DisplayName|**Label**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_label`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_mspp_maxmultiplechoiceselectedcount"></a> mspp_maxmultiplechoiceselectedcount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Multiple Choice Max Selected Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_maxmultiplechoiceselectedcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_mspp_minmultiplechoiceselectedcount"></a> mspp_minmultiplechoiceselectedcount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Multiple Choice Minimum Required Selected Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_minmultiplechoiceselectedcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_mspp_modifiedby"></a> mspp_modifiedby

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_mspp_modifiedon"></a> mspp_modifiedon

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_mspp_multiplechoicevalidationerrormessage"></a> mspp_multiplechoicevalidationerrormessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Multiple Choice Validation Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_multiplechoicevalidationerrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_notes_settings"></a> mspp_notes_settings

|Property|Value|
|---|---|
|Description||
|DisplayName|**Notes Settings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_notes_settings`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_mspp_onsavefromattribute"></a> mspp_onsavefromattribute

|Property|Value|
|---|---|
|Description|**Use this field, in conjunction with On Save Type = Current User Contact, to map any attribute from the current user’s contact record to this record’s attribute logical name.**|
|DisplayName|**On Save From Attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_onsavefromattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_onsavetype"></a> mspp_onsavetype

|Property|Value|
|---|---|
|Description|**Shows the mechanisms for populating a field with a value.**|
|DisplayName|**On Save Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_onsavetype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspp_webformmetadata_mspp_onsavetype`|

#### mspp_onsavetype Choices/Options

|Value|Label|
|---|---|
|100000000|**Value**|
|100000001|**Today's Date**|
|100000002|**Current Portal User**|

### <a name="BKMK_mspp_onsavevalue"></a> mspp_onsavevalue

|Property|Value|
|---|---|
|Description||
|DisplayName|**Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_onsavevalue`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_prepopulatefromattribute"></a> mspp_prepopulatefromattribute

|Property|Value|
|---|---|
|Description|**Use this field, in conjunction with Prepopulate Type = Current User Contact, to map any attribute from the current user’s contact record to this record’s attribute logical name.**|
|DisplayName|**Prepopulate From Attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_prepopulatefromattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_prepopulatetype"></a> mspp_prepopulatetype

|Property|Value|
|---|---|
|Description|**Shows the mechanisms for populating a field with a value.**|
|DisplayName|**Prepopulate Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_prepopulatetype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspp_webformmetadata_mspp_prepopulatetype`|

#### mspp_prepopulatetype Choices/Options

|Value|Label|
|---|---|
|100000000|**Value**|
|100000001|**Today's Date**|
|100000002|**Current Portal User**|

### <a name="BKMK_mspp_prepopulatevalue"></a> mspp_prepopulatevalue

|Property|Value|
|---|---|
|Description|**The value to prepopulate the field.**|
|DisplayName|**Prepopulate Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_prepopulatevalue`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_provisionedlanguages"></a> mspp_provisionedlanguages

|Property|Value|
|---|---|
|Description||
|DisplayName|**Provisioned Languages**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_provisionedlanguages`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_purchasecreateinvoiceonpayment"></a> mspp_purchasecreateinvoiceonpayment

|Property|Value|
|---|---|
|Description||
|DisplayName|**Create Invoice on Payment**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchasecreateinvoiceonpayment`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformmetadata_mspp_purchasecreateinvoiceonpayment`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_purchasefulfillorderonpayment"></a> mspp_purchasefulfillorderonpayment

|Property|Value|
|---|---|
|Description||
|DisplayName|**Fulfill Order on Payment**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchasefulfillorderonpayment`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformmetadata_mspp_purchasefulfillorderonpayment`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_purchaselineitemdescriptionattribute"></a> mspp_purchaselineitemdescriptionattribute

|Property|Value|
|---|---|
|Description||
|DisplayName|**Line Item Description Attribute Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchaselineitemdescriptionattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_purchaselineiteminstructionsattribute"></a> mspp_purchaselineiteminstructionsattribute

|Property|Value|
|---|---|
|Description|**Purchase line item entity attribute name for instructions.**|
|DisplayName|**Line Item Instructions Attribute Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchaselineiteminstructionsattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_purchaselineitemorderattribute"></a> mspp_purchaselineitemorderattribute

|Property|Value|
|---|---|
|Description|**Purchase line item entity attribute name for the order in which a line item should be displayed.**|
|DisplayName|**Line Item Order Attribute Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchaselineitemorderattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_purchaselineitemproductattribute"></a> mspp_purchaselineitemproductattribute

|Property|Value|
|---|---|
|Description|**Purchase line item entity attribute name for Product lookup. If this value is not present and set, the corresponding line item will be excluded from the purchase.**|
|DisplayName|**Line Item Product Attribute Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchaselineitemproductattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_purchaselineitemquantityattribute"></a> mspp_purchaselineitemquantityattribute

|Property|Value|
|---|---|
|Description|**Purchase line item entity attribute name for item quantity. (Should be a decimal attribute.)**|
|DisplayName|**Line Item Quantity Attribute Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchaselineitemquantityattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_purchaselineitemrelationship"></a> mspp_purchaselineitemrelationship

|Property|Value|
|---|---|
|Description|**Relationship from the purchase entity that defines purchase line items.**|
|DisplayName|**Line Item Relationship Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchaselineitemrelationship`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_mspp_purchaselineitemrequiredattribute"></a> mspp_purchaselineitemrequiredattribute

|Property|Value|
|---|---|
|Description|**Purchase line item entity attribute name for whether a line item is required.**|
|DisplayName|**Line Item Required Attribute Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchaselineitemrequiredattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_purchaselineitemuomattribute"></a> mspp_purchaselineitemuomattribute

|Property|Value|
|---|---|
|Description|**Purchase line item entity attribute name for Unit of Measure lookup.**|
|DisplayName|**Line Item UoM Attribute Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchaselineitemuomattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_purchaseoptionalproductsrelationship"></a> mspp_purchaseoptionalproductsrelationship

|Property|Value|
|---|---|
|Description|**Relationship from the purchase entity for products to be purchased that are optional (the user must opt-in to purchase of these items).**|
|DisplayName|**Optional Products Relationship Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchaseoptionalproductsrelationship`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_mspp_purchasequotename"></a> mspp_purchasequotename

|Property|Value|
|---|---|
|Description|**The name to be used for all purchase quotes generated by this step.**|
|DisplayName|**Quote Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchasequotename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_mspp_purchaserequiredproductsrelationship"></a> mspp_purchaserequiredproductsrelationship

|Property|Value|
|---|---|
|Description|**Relationship from the purchase entity for products to be purchased that are a required part of the purchase.**|
|DisplayName|**Required Products Relationship Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchaserequiredproductsrelationship`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_mspp_purchaserequiresshipping"></a> mspp_purchaserequiresshipping

|Property|Value|
|---|---|
|Description|**Select whether to require the purchase process to collect shipping information.**|
|DisplayName|**Requires Shipping**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchaserequiresshipping`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformmetadata_mspp_purchaserequiresshipping`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_purchasetargetentityinvoicerelationship"></a> mspp_purchasetargetentityinvoicerelationship

|Property|Value|
|---|---|
|Description||
|DisplayName|**Target Entity Invoice Relationship Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchasetargetentityinvoicerelationship`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_purchasetargetentityorderrelationship"></a> mspp_purchasetargetentityorderrelationship

|Property|Value|
|---|---|
|Description||
|DisplayName|**Target Entity Order Relationship Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchasetargetentityorderrelationship`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_purchasetargetentityrelationship"></a> mspp_purchasetargetentityrelationship

|Property|Value|
|---|---|
|Description|**Relationship from the form step target entity to the purchase entity, if the step target is not the purchase entity.**|
|DisplayName|**Target Entity Relationship Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_purchasetargetentityrelationship`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_mspp_randomizeoptionsetvalues"></a> mspp_randomizeoptionsetvalues

|Property|Value|
|---|---|
|Description||
|DisplayName|**Randomize Option Set Values**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_randomizeoptionsetvalues`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformmetadata_mspp_randomizeoptionsetvalues`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_rangevalidationerrormessage"></a> mspp_rangevalidationerrormessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Range Validation Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_rangevalidationerrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_rankordernotiesvalidationerrormessage"></a> mspp_rankordernotiesvalidationerrormessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Rank Order No Ties Validation Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_rankordernotiesvalidationerrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_requiredfieldvalidationerrormessage"></a> mspp_requiredfieldvalidationerrormessage

|Property|Value|
|---|---|
|Description|**The error message shown when a required field does not contain a value.**|
|DisplayName|**Required Field Validation Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_requiredfieldvalidationerrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_sectionname"></a> mspp_sectionname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Section Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_sectionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_mspp_setvalueonsave"></a> mspp_setvalueonsave

|Property|Value|
|---|---|
|Description||
|DisplayName|**Set Value On Save**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_setvalueonsave`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformmetadata_mspp_setvalueonsave`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_subgrid_name"></a> mspp_subgrid_name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Subgrid Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_subgrid_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|150|

### <a name="BKMK_mspp_subgrid_settings"></a> mspp_subgrid_settings

|Property|Value|
|---|---|
|Description||
|DisplayName|**Subgrid Settings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_subgrid_settings`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_mspp_tabname"></a> mspp_tabname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Tab Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_tabname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_mspp_timeline_settings"></a> mspp_timeline_settings

|Property|Value|
|---|---|
|Description||
|DisplayName|**Timeline Settings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_timeline_settings`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_mspp_type"></a> mspp_type

|Property|Value|
|---|---|
|Description||
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_type`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|100000000|
|GlobalChoiceName|`mspp_webformmetadata_mspp_type`|

#### mspp_type Choices/Options

|Value|Label|
|---|---|
|100000000|**Attribute**|
|100000001|**Section**|
|100000002|**Tab**|
|100000003|**Purchase**|
|100000004|**Subgrid**|
|100000005|**Notes**|
|756150000|**Timeline**|

### <a name="BKMK_mspp_useattributedescriptionproperty"></a> mspp_useattributedescriptionproperty

|Property|Value|
|---|---|
|Description||
|DisplayName|**Use Attribute's Description Property**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_useattributedescriptionproperty`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webformmetadata_mspp_useattributedescriptionproperty`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_validationerrormessage"></a> mspp_validationerrormessage

|Property|Value|
|---|---|
|Description|**The error message defined for the validation.**|
|DisplayName|**Validation Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_validationerrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_validationregularexpression"></a> mspp_validationregularexpression

|Property|Value|
|---|---|
|Description|**Adds a regular expression validator with the specified regular expression.**|
|DisplayName|**Validation Regular Expression**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_validationregularexpression`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_validationregularexpressionerrormessage"></a> mspp_validationregularexpressionerrormessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Regular Expression Validation Error Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_validationregularexpressionerrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_mspp_webformmetadataId"></a> mspp_webformmetadataId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Multistep Form Metadata**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_webformmetadataid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_webformstep"></a> mspp_webformstep

|Property|Value|
|---|---|
|Description|**Unique identifier for Form Step associated with Multistep Form Metadata.**|
|DisplayName|**Form Step**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webformstep`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_webformstep|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Multistep Form Metadata**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webformmetadata_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Multistep Form Metadata**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webformmetadata_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_entityform_webformmetadata_entityformforcreate](#BKMK_mspp_entityform_webformmetadata_entityformforcreate)
- [mspp_systemuser_mspp_webformmetadata_createdby](#BKMK_mspp_systemuser_mspp_webformmetadata_createdby)
- [mspp_systemuser_mspp_webformmetadata_modifiedby](#BKMK_mspp_systemuser_mspp_webformmetadata_modifiedby)
- [mspp_webform_webformmetadata_entityformforcreate](#BKMK_mspp_webform_webformmetadata_entityformforcreate)
- [mspp_webformmetadata_webformstep](#BKMK_mspp_webformmetadata_webformstep)

### <a name="BKMK_mspp_entityform_webformmetadata_entityformforcreate"></a> mspp_entityform_webformmetadata_entityformforcreate

One-To-Many Relationship: [mspp_entityform mspp_entityform_webformmetadata_entityformforcreate](mspp_entityform.md#BKMK_mspp_entityform_webformmetadata_entityformforcreate)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_entityform`|
|ReferencedAttribute|`mspp_entityformid`|
|ReferencingAttribute|`mspp_entityformforcreateinwebformmetadata`|
|ReferencingEntityNavigationPropertyName|`mspp_entityformforcreateinwebformmetadata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_webformmetadata_createdby"></a> mspp_systemuser_mspp_webformmetadata_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webformmetadata_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webformmetadata_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_webformmetadata_modifiedby"></a> mspp_systemuser_mspp_webformmetadata_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webformmetadata_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webformmetadata_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webform_webformmetadata_entityformforcreate"></a> mspp_webform_webformmetadata_entityformforcreate

One-To-Many Relationship: [mspp_webform mspp_webform_webformmetadata_entityformforcreate](mspp_webform.md#BKMK_mspp_webform_webformmetadata_entityformforcreate)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webform`|
|ReferencedAttribute|`mspp_webformid`|
|ReferencingAttribute|`mspp_entityformforcreate`|
|ReferencingEntityNavigationPropertyName|`mspp_entityformforcreate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webformmetadata_webformstep"></a> mspp_webformmetadata_webformstep

One-To-Many Relationship: [mspp_webformstep mspp_webformmetadata_webformstep](mspp_webformstep.md#BKMK_mspp_webformmetadata_webformstep)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webformstep`|
|ReferencedAttribute|`mspp_webformstepid`|
|ReferencingAttribute|`mspp_webformstep`|
|ReferencingEntityNavigationPropertyName|`mspp_webformstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_webformmetadata?displayProperty=fullName>
