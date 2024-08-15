---
title: "Multistep Form Metadata (mspp_webformmetadata)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Multistep Form Metadata (mspp_webformmetadata)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Multistep Form Metadata (mspp_webformmetadata)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Defines the additional behavior modification logic to augment or override the functionality of form fields that is not possible with Dynamics 365 entity and form metadata.

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_webformmetadatas<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_webformmetadatas(*mspp_webformmetadataid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_webformmetadatas(*mspp_webformmetadataid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_webformmetadatas<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_webformmetadatas(*mspp_webformmetadataid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_webformmetadatas|
|DisplayCollectionName|Multistep Form Metadata|
|DisplayName|Multistep Form Metadata|
|EntitySetName|mspp_webformmetadatas|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_webformmetadatas|
|LogicalName|mspp_webformmetadata|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_webformmetadataid|
|PrimaryNameAttribute|mspp_attributelogicalname|
|SchemaName|mspp_webformmetadata|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description||
|DisplayName|Add Description|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_adddescription|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_adddescription Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_attributelogicalname"></a> mspp_attributelogicalname

|Property|Value|
|--------|-----|
|Description|The name of the attribute field to be modified.|
|DisplayName|Attribute Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_attributelogicalname|
|MaxLength|100|
|RequiredLevel|Recommended|
|Type|String|


### <a name="BKMK_mspp_constantsummaximumtotal"></a> mspp_constantsummaximumtotal

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Constant Sum Maximum Total|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_constantsummaximumtotal|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_constantsumminimumtotal"></a> mspp_constantsumminimumtotal

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Constant Sum Minimum Total|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_constantsumminimumtotal|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_constantsumvalidationerrormessage"></a> mspp_constantsumvalidationerrormessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Constant Sum Validation Error Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_constantsumvalidationerrormessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_controlstyle"></a> mspp_controlstyle

|Property|Value|
|--------|-----|
|Description|Specifies how the control should be modified or enhanced.|
|DisplayName|Control Style|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_controlstyle|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_controlstyle Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|100000000|Option Set as Vertical Radio Button List||
|100000001|Option Set as Horizontal Radio Button List||
|100000002|Single Line of Text as Geolocation Lookup Validator||
|100000003|Group Whole Number as Constant Sum||
|100000004|Group Whole Number as Rank Order Scale No Ties||
|100000005|Group Whole Number as Rank Order Scale Allow Ties||
|100000006|Multiple Choice Matrix||
|100000007|Multiple Choice||
|100000008|Group Whole Number as Stack Rank||
|756150000|Render Lookup as Dropdown||
|756150001|Code component||



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


### <a name="BKMK_mspp_cssclass"></a> mspp_cssclass

|Property|Value|
|--------|-----|
|Description||
|DisplayName|CSS Class|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_cssclass|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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
|MaxLength|10000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_descriptionposition"></a> mspp_descriptionposition

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Position|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_descriptionposition|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_descriptionposition Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|100000000|Above the field||
|100000001|Below the field||
|100000002|Above the label||



### <a name="BKMK_mspp_entityformforcreate"></a> mspp_entityformforcreate

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Basic Form for Create|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_entityformforcreate|
|RequiredLevel|None|
|Targets|mspp_webform|
|Type|Lookup|


### <a name="BKMK_mspp_entityformforcreateinwebformmetadata"></a> mspp_entityformforcreateinwebformmetadata

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Basic Form for Create|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_entityformforcreateinwebformmetadata|
|RequiredLevel|None|
|Targets|mspp_entityform|
|Type|Lookup|


### <a name="BKMK_mspp_fieldisrequired"></a> mspp_fieldisrequired

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Field is Required|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_fieldisrequired|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_fieldisrequired Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_geolocationvalidatorerrormessage"></a> mspp_geolocationvalidatorerrormessage

|Property|Value|
|--------|-----|
|Description|The error message to be displayed when the geolocation validator validation fails.|
|DisplayName|Geolocation Validator Error Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_geolocationvalidatorerrormessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_groupname"></a> mspp_groupname

|Property|Value|
|--------|-----|
|Description|Shows which attributes are to be grouped and rendered as a composite control if the control style is a groupings type such as "Group Whole Number as Constant Sum."|
|DisplayName|Group Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_groupname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_ignoredefaultvalue"></a> mspp_ignoredefaultvalue

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Ignore Default Value|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_ignoredefaultvalue|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_ignoredefaultvalue Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_label"></a> mspp_label

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Label|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_label|
|MaxLength|10000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_maxmultiplechoiceselectedcount"></a> mspp_maxmultiplechoiceselectedcount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Multiple Choice Max Selected Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_maxmultiplechoiceselectedcount|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_mspp_minmultiplechoiceselectedcount"></a> mspp_minmultiplechoiceselectedcount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Multiple Choice Minimum Required Selected Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_minmultiplechoiceselectedcount|
|MaxValue|100|
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


### <a name="BKMK_mspp_multiplechoicevalidationerrormessage"></a> mspp_multiplechoicevalidationerrormessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Multiple Choice Validation Error Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_multiplechoicevalidationerrormessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_notes_settings"></a> mspp_notes_settings

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Notes Settings|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_notes_settings|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_onsavefromattribute"></a> mspp_onsavefromattribute

|Property|Value|
|--------|-----|
|Description|Use this field, in conjunction with On Save Type = Current User Contact, to map any attribute from the current user’s contact record to this record’s attribute logical name.|
|DisplayName|On Save From Attribute|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_onsavefromattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_onsavetype"></a> mspp_onsavetype

|Property|Value|
|--------|-----|
|Description|Shows the mechanisms for populating a field with a value.|
|DisplayName|On Save Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_onsavetype|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_onsavetype Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|100000000|Value||
|100000001|Today's Date||
|100000002|Current Portal User||



### <a name="BKMK_mspp_onsavevalue"></a> mspp_onsavevalue

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_onsavevalue|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_prepopulatefromattribute"></a> mspp_prepopulatefromattribute

|Property|Value|
|--------|-----|
|Description|Use this field, in conjunction with Prepopulate Type = Current User Contact, to map any attribute from the current user’s contact record to this record’s attribute logical name.|
|DisplayName|Prepopulate From Attribute|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_prepopulatefromattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_prepopulatetype"></a> mspp_prepopulatetype

|Property|Value|
|--------|-----|
|Description|Shows the mechanisms for populating a field with a value.|
|DisplayName|Prepopulate Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_prepopulatetype|
|RequiredLevel|None|
|Type|Picklist|

#### mspp_prepopulatetype Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|100000000|Value||
|100000001|Today's Date||
|100000002|Current Portal User||



### <a name="BKMK_mspp_prepopulatevalue"></a> mspp_prepopulatevalue

|Property|Value|
|--------|-----|
|Description|The value to prepopulate the field.|
|DisplayName|Prepopulate Value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_prepopulatevalue|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_mspp_purchasecreateinvoiceonpayment"></a> mspp_purchasecreateinvoiceonpayment

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Create Invoice on Payment|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchasecreateinvoiceonpayment|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_purchasecreateinvoiceonpayment Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_purchasefulfillorderonpayment"></a> mspp_purchasefulfillorderonpayment

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Fulfill Order on Payment|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchasefulfillorderonpayment|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_purchasefulfillorderonpayment Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_purchaselineitemdescriptionattribute"></a> mspp_purchaselineitemdescriptionattribute

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Line Item Description Attribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchaselineitemdescriptionattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchaselineiteminstructionsattribute"></a> mspp_purchaselineiteminstructionsattribute

|Property|Value|
|--------|-----|
|Description|Purchase line item entity attribute name for instructions.|
|DisplayName|Line Item Instructions Attribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchaselineiteminstructionsattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchaselineitemorderattribute"></a> mspp_purchaselineitemorderattribute

|Property|Value|
|--------|-----|
|Description|Purchase line item entity attribute name for the order in which a line item should be displayed.|
|DisplayName|Line Item Order Attribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchaselineitemorderattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchaselineitemproductattribute"></a> mspp_purchaselineitemproductattribute

|Property|Value|
|--------|-----|
|Description|Purchase line item entity attribute name for Product lookup. If this value is not present and set, the corresponding line item will be excluded from the purchase.|
|DisplayName|Line Item Product Attribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchaselineitemproductattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchaselineitemquantityattribute"></a> mspp_purchaselineitemquantityattribute

|Property|Value|
|--------|-----|
|Description|Purchase line item entity attribute name for item quantity. (Should be a decimal attribute.)|
|DisplayName|Line Item Quantity Attribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchaselineitemquantityattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchaselineitemrelationship"></a> mspp_purchaselineitemrelationship

|Property|Value|
|--------|-----|
|Description|Relationship from the purchase entity that defines purchase line items.|
|DisplayName|Line Item Relationship Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchaselineitemrelationship|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchaselineitemrequiredattribute"></a> mspp_purchaselineitemrequiredattribute

|Property|Value|
|--------|-----|
|Description|Purchase line item entity attribute name for whether a line item is required.|
|DisplayName|Line Item Required Attribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchaselineitemrequiredattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchaselineitemuomattribute"></a> mspp_purchaselineitemuomattribute

|Property|Value|
|--------|-----|
|Description|Purchase line item entity attribute name for Unit of Measure lookup.|
|DisplayName|Line Item UoM Attribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchaselineitemuomattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchaseoptionalproductsrelationship"></a> mspp_purchaseoptionalproductsrelationship

|Property|Value|
|--------|-----|
|Description|Relationship from the purchase entity for products to be purchased that are optional (the user must opt-in to purchase of these items).|
|DisplayName|Optional Products Relationship Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchaseoptionalproductsrelationship|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchasequotename"></a> mspp_purchasequotename

|Property|Value|
|--------|-----|
|Description|The name to be used for all purchase quotes generated by this step.|
|DisplayName|Quote Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchasequotename|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchaserequiredproductsrelationship"></a> mspp_purchaserequiredproductsrelationship

|Property|Value|
|--------|-----|
|Description|Relationship from the purchase entity for products to be purchased that are a required part of the purchase.|
|DisplayName|Required Products Relationship Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchaserequiredproductsrelationship|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchaserequiresshipping"></a> mspp_purchaserequiresshipping

|Property|Value|
|--------|-----|
|Description|Select whether to require the purchase process to collect shipping information.|
|DisplayName|Requires Shipping|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchaserequiresshipping|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_purchaserequiresshipping Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_purchasetargetentityinvoicerelationship"></a> mspp_purchasetargetentityinvoicerelationship

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Target Entity Invoice Relationship Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchasetargetentityinvoicerelationship|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchasetargetentityorderrelationship"></a> mspp_purchasetargetentityorderrelationship

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Target Entity Order Relationship Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchasetargetentityorderrelationship|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_purchasetargetentityrelationship"></a> mspp_purchasetargetentityrelationship

|Property|Value|
|--------|-----|
|Description|Relationship from the form step target entity to the purchase entity, if the step target is not the purchase entity.|
|DisplayName|Target Entity Relationship Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_purchasetargetentityrelationship|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_randomizeoptionsetvalues"></a> mspp_randomizeoptionsetvalues

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Randomize Option Set Values|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_randomizeoptionsetvalues|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_randomizeoptionsetvalues Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_rangevalidationerrormessage"></a> mspp_rangevalidationerrormessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Range Validation Error Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_rangevalidationerrormessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_rankordernotiesvalidationerrormessage"></a> mspp_rankordernotiesvalidationerrormessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Rank Order No Ties Validation Error Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_rankordernotiesvalidationerrormessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_requiredfieldvalidationerrormessage"></a> mspp_requiredfieldvalidationerrormessage

|Property|Value|
|--------|-----|
|Description|The error message shown when a required field does not contain a value.|
|DisplayName|Required Field Validation Error Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_requiredfieldvalidationerrormessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_sectionname"></a> mspp_sectionname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Section Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_sectionname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_setvalueonsave"></a> mspp_setvalueonsave

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Set Value On Save|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_setvalueonsave|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_setvalueonsave Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_subgrid_name"></a> mspp_subgrid_name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Subgrid Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_subgrid_name|
|MaxLength|150|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_subgrid_settings"></a> mspp_subgrid_settings

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Subgrid Settings|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_subgrid_settings|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_tabname"></a> mspp_tabname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Tab Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_tabname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_timeline_settings"></a> mspp_timeline_settings

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Timeline Settings|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_timeline_settings|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_mspp_type"></a> mspp_type

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_type|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### mspp_type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|100000000|Attribute||
|100000001|Section||
|100000002|Tab||
|100000003|Purchase||
|100000004|Subgrid||
|100000005|Notes||
|756150000|Timeline||



### <a name="BKMK_mspp_useattributedescriptionproperty"></a> mspp_useattributedescriptionproperty

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Use Attribute's Description Property|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_useattributedescriptionproperty|
|RequiredLevel|None|
|Type|Boolean|

#### mspp_useattributedescriptionproperty Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_mspp_validationerrormessage"></a> mspp_validationerrormessage

|Property|Value|
|--------|-----|
|Description|The error message defined for the validation.|
|DisplayName|Validation Error Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_validationerrormessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_validationregularexpression"></a> mspp_validationregularexpression

|Property|Value|
|--------|-----|
|Description|Adds a regular expression validator with the specified regular expression.|
|DisplayName|Validation Regular Expression|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_validationregularexpression|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_validationregularexpressionerrormessage"></a> mspp_validationregularexpressionerrormessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Regular Expression Validation Error Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_validationregularexpressionerrormessage|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_webformmetadataId"></a> mspp_webformmetadataId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Multistep Form Metadata|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_webformmetadataid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_webformstep"></a> mspp_webformstep

|Property|Value|
|--------|-----|
|Description|Unique identifier for Form Step associated with Multistep Form Metadata.|
|DisplayName|Form Step|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webformstep|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_webformstep|
|Type|Lookup|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Multistep Form Metadata|
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
|Description|Reason for the status of the Multistep Form Metadata|
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
- [mspp_entityformforcreateinwebformmetadataName](#BKMK_mspp_entityformforcreateinwebformmetadataName)
- [mspp_entityformforcreateName](#BKMK_mspp_entityformforcreateName)
- [mspp_modifiedbyName](#BKMK_mspp_modifiedbyName)
- [mspp_modifiedbyYomiName](#BKMK_mspp_modifiedbyYomiName)
- [mspp_webformstepName](#BKMK_mspp_webformstepName)


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


### <a name="BKMK_mspp_entityformforcreateinwebformmetadataName"></a> mspp_entityformforcreateinwebformmetadataName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_entityformforcreateinwebformmetadataname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_entityformforcreateName"></a> mspp_entityformforcreateName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_entityformforcreatename|
|MaxLength|100|
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


### <a name="BKMK_mspp_webformstepName"></a> mspp_webformstepName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_webformstepname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_entityform_webformmetadata_entityformforcreate](#BKMK_mspp_entityform_webformmetadata_entityformforcreate)
- [mspp_systemuser_mspp_webformmetadata_createdby](#BKMK_mspp_systemuser_mspp_webformmetadata_createdby)
- [mspp_systemuser_mspp_webformmetadata_modifiedby](#BKMK_mspp_systemuser_mspp_webformmetadata_modifiedby)
- [mspp_webform_webformmetadata_entityformforcreate](#BKMK_mspp_webform_webformmetadata_entityformforcreate)
- [mspp_webformmetadata_webformstep](#BKMK_mspp_webformmetadata_webformstep)


### <a name="BKMK_mspp_entityform_webformmetadata_entityformforcreate"></a> mspp_entityform_webformmetadata_entityformforcreate

See the [mspp_entityform_webformmetadata_entityformforcreate](mspp_entityform.md#BKMK_mspp_entityform_webformmetadata_entityformforcreate) one-to-many relationship for the [mspp_entityform](mspp_entityform.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_webformmetadata_createdby"></a> mspp_systemuser_mspp_webformmetadata_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webformmetadata_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webformmetadata_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_webformmetadata_modifiedby"></a> mspp_systemuser_mspp_webformmetadata_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_webformmetadata_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webformmetadata_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_webform_webformmetadata_entityformforcreate"></a> mspp_webform_webformmetadata_entityformforcreate

See the [mspp_webform_webformmetadata_entityformforcreate](mspp_webform.md#BKMK_mspp_webform_webformmetadata_entityformforcreate) one-to-many relationship for the [mspp_webform](mspp_webform.md) table/entity.

### <a name="BKMK_mspp_webformmetadata_webformstep"></a> mspp_webformmetadata_webformstep

See the [mspp_webformmetadata_webformstep](mspp_webformstep.md#BKMK_mspp_webformmetadata_webformstep) one-to-many relationship for the [mspp_webformstep](mspp_webformstep.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_webformmetadata?text=mspp_webformmetadata EntityType" />