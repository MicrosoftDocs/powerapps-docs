---
title: "Website Language (mspp_websitelanguage)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Website Language (mspp_websitelanguage)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Website Language (mspp_websitelanguage)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Languages supported and publishing status for the portal

**Added by**: Power Pages Apps Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /mspp_websitelanguages<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /mspp_websitelanguages(*mspp_websitelanguageid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /mspp_websitelanguages(*mspp_websitelanguageid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /mspp_websitelanguages<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /mspp_websitelanguages(*mspp_websitelanguageid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|mspp_websitelanguages|
|DisplayCollectionName|Website Languages|
|DisplayName|Website Language|
|EntitySetName|mspp_websitelanguages|
|IsBPFEntity|False|
|LogicalCollectionName|mspp_websitelanguages|
|LogicalName|mspp_websitelanguage|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mspp_websitelanguageid|
|PrimaryNameAttribute|mspp_name|
|SchemaName|mspp_websitelanguage|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_description](#BKMK_mspp_description)
- [mspp_displayname](#BKMK_mspp_displayname)
- [mspp_languagecode](#BKMK_mspp_languagecode)
- [mspp_lcid](#BKMK_mspp_lcid)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_publishingstate](#BKMK_mspp_publishingstate)
- [mspp_systemlanguage](#BKMK_mspp_systemlanguage)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [mspp_websitelanguageId](#BKMK_mspp_websitelanguageId)
- [mspp_websitelcid](#BKMK_mspp_websitelcid)
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


### <a name="BKMK_mspp_displayname"></a> mspp_displayname

|Property|Value|
|--------|-----|
|Description|Localized display name of the portal language|
|DisplayName|Portal Display Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_displayname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_languagecode"></a> mspp_languagecode

|Property|Value|
|--------|-----|
|Description|Locale or language identifier that appears in the URL to indicate the portal language|
|DisplayName|Language Code|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_languagecode|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_lcid"></a> mspp_lcid

|Property|Value|
|--------|-----|
|Description|Locale ID that is assigned to the portal language|
|DisplayName|Language Code Identifier|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_lcid|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|ApplicationRequired|
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


### <a name="BKMK_mspp_name"></a> mspp_name

|Property|Value|
|--------|-----|
|Description|Name of the portal language|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_mspp_publishingstate"></a> mspp_publishingstate

|Property|Value|
|--------|-----|
|Description|Lookup to Publishing State - publishing state of this website/language instance (draft/published)|
|DisplayName|Publishing State|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_publishingstate|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_publishingstate|
|Type|Lookup|


### <a name="BKMK_mspp_systemlanguage"></a> mspp_systemlanguage

|Property|Value|
|--------|-----|
|Description|The system language determines which portal languages are available|
|DisplayName|System Language|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_systemlanguage|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|--------|-----|
|Description|Lookup to Website|
|DisplayName|Website|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_websiteid|
|RequiredLevel|ApplicationRequired|
|Targets|mspp_website|
|Type|Lookup|


### <a name="BKMK_mspp_websitelanguageId"></a> mspp_websitelanguageId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Website Language|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mspp_websitelanguageid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_mspp_websitelcid"></a> mspp_websitelcid

|Property|Value|
|--------|-----|
|Description|This attribute is used only in Power Pages Management App, and only for UI purpose. It's value is mapped to mspp_systemlanguage.|
|DisplayName|Power Pages Language|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_websitelcid|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### mspp_websitelcid Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1025|Arabic||
|1026|Bulgarian - Bulgaria||
|1027|Catalan - Catalan||
|1028|Chinese - Traditional||
|1029|Czech - Czech Republic||
|1030|Danish - Denmark||
|1031|German - Germany||
|1032|Greek - Greece||
|1033|English||
|1035|Finnish - Finland||
|1036|French - France||
|1037|Hebrew||
|1038|Hungarian - Hungary||
|1040|Italian - Italy||
|1041|Japanese - Japan||
|1042|Korean - Korea||
|1043|Dutch - Netherlands||
|1044|Norwegian (Bokmål) - Norway||
|1045|Polish - Poland||
|1046|Portuguese - Brazil||
|1048|Romanian - Romania||
|1049|Russian - Russia||
|1050|Croatian - Croatia||
|1051|Slovak - Slovakia||
|1053|Swedish - Sweden||
|1054|Thai - Thailand||
|1055|Turkish - Türkiye||
|1057|Indonesian - Indonesia||
|1058|Ukrainian - Ukraine||
|1060|Slovenian - Slovenia||
|1061|Estonian - Estonia||
|1062|Latvian - Latvia||
|1063|Lithuanian - Lithuania||
|1066|Vietnamese - Vietnam||
|1069|Basque - Basque||
|1081|Hindi - India||
|1086|Malay - Malaysia||
|1087|Kazakh - Kazakhstan||
|1110|Galician - Spain||
|2052|Chinese - China||
|2070|Portuguese - Portugal||
|2074|Serbian (Latin) - Serbia||
|3076|Chinese - Hong Kong SAR||
|3082|Spanish (Traditional Sort) - Spain||
|3098|Serbian (Cyrillic) - Serbia||



### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Website Language|
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
|Description|Reason for the status of the Website Language|
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
- [mspp_publishingstateName](#BKMK_mspp_publishingstateName)
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


### <a name="BKMK_mspp_publishingstateName"></a> mspp_publishingstateName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_publishingstatename|
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

- [mspp_mspp_websitelanguage_mspp_website_DefaultLanguage](#BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage)
- [mspp_websitelanguage_contentsnippet_contentsnippetlanguageid](#BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid)
- [mspp_websitelanguage_weblinkset](#BKMK_mspp_websitelanguage_weblinkset)
- [mspp_websitelanguage_webpage_webpagelanguageid](#BKMK_mspp_websitelanguage_webpage_webpagelanguageid)


### <a name="BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage"></a> mspp_mspp_websitelanguage_mspp_website_DefaultLanguage

Same as the [mspp_mspp_websitelanguage_mspp_website_DefaultLanguage](mspp_website.md#BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage) many-to-one relationship for the [mspp_website](mspp_website.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_website|
|ReferencingAttribute|mspp_defaultlanguage|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_mspp_websitelanguage_mspp_website_DefaultLanguage|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid"></a> mspp_websitelanguage_contentsnippet_contentsnippetlanguageid

Same as the [mspp_websitelanguage_contentsnippet_contentsnippetlanguageid](mspp_contentsnippet.md#BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid) many-to-one relationship for the [mspp_contentsnippet](mspp_contentsnippet.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_contentsnippet|
|ReferencingAttribute|mspp_contentsnippetlanguageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_websitelanguage_contentsnippet_contentsnippetlanguageid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_websitelanguage_weblinkset"></a> mspp_websitelanguage_weblinkset

Same as the [mspp_websitelanguage_weblinkset](mspp_weblinkset.md#BKMK_mspp_websitelanguage_weblinkset) many-to-one relationship for the [mspp_weblinkset](mspp_weblinkset.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_weblinkset|
|ReferencingAttribute|mspp_websitelanguageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_websitelanguage_weblinkset|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mspp_websitelanguage_webpage_webpagelanguageid"></a> mspp_websitelanguage_webpage_webpagelanguageid

Same as the [mspp_websitelanguage_webpage_webpagelanguageid](mspp_webpage.md#BKMK_mspp_websitelanguage_webpage_webpagelanguageid) many-to-one relationship for the [mspp_webpage](mspp_webpage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspp_webpage|
|ReferencingAttribute|mspp_webpagelanguageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mspp_websitelanguage_webpage_webpagelanguageid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState](#BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState)
- [mspp_mspp_website_mspp_websitelanguage](#BKMK_mspp_mspp_website_mspp_websitelanguage)
- [mspp_systemuser_mspp_websitelanguage_createdby](#BKMK_mspp_systemuser_mspp_websitelanguage_createdby)
- [mspp_systemuser_mspp_websitelanguage_modifiedby](#BKMK_mspp_systemuser_mspp_websitelanguage_modifiedby)


### <a name="BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState"></a> mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState

See the [mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState](mspp_publishingstate.md#BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState) one-to-many relationship for the [mspp_publishingstate](mspp_publishingstate.md) table/entity.

### <a name="BKMK_mspp_mspp_website_mspp_websitelanguage"></a> mspp_mspp_website_mspp_websitelanguage

See the [mspp_mspp_website_mspp_websitelanguage](mspp_website.md#BKMK_mspp_mspp_website_mspp_websitelanguage) one-to-many relationship for the [mspp_website](mspp_website.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_websitelanguage_createdby"></a> mspp_systemuser_mspp_websitelanguage_createdby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_websitelanguage_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_websitelanguage_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_mspp_systemuser_mspp_websitelanguage_modifiedby"></a> mspp_systemuser_mspp_websitelanguage_modifiedby

**Added by**: System Solution Solution

See the [mspp_systemuser_mspp_websitelanguage_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_websitelanguage_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mspp_websitelanguage?text=mspp_websitelanguage EntityType" />