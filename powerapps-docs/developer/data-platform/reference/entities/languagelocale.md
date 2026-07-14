---
title: "Language (LanguageLocale) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Language (LanguageLocale) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Language (LanguageLocale) table/entity reference (Microsoft Dataverse)

Language

## Messages

The following table lists the messages for the Language (LanguageLocale) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /languagelocale(*languagelocaleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /languagelocale<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /languagelocale(*languagelocaleid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /languagelocale(*languagelocaleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|

## Properties

The following table lists selected properties for the Language (LanguageLocale) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Language** |
| **DisplayCollectionName** | **Languages** |
| **SchemaName** | `LanguageLocale` |
| **CollectionSchemaName** | `LanguageLocales` |
| **EntitySetName** | `languagelocale`|
| **LogicalName** | `languagelocale` |
| **LogicalCollectionName** | `languagelocales` |
| **PrimaryIdAttribute** | `languagelocaleid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [LanguageLocaleId](#BKMK_LanguageLocaleId)
- [LocaleId](#BKMK_LocaleId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

### <a name="BKMK_LanguageLocaleId"></a> LanguageLocaleId

|Property|Value|
|---|---|
|Description|**LanguageLocaleId**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`languagelocaleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_LocaleId"></a> LocaleId

|Property|Value|
|---|---|
|Description|**Locale ID**|
|DisplayName|**Locale ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`localeid`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**State Code**|
|DisplayName|**State Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`languagelocale_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Language Status Code**|
|DisplayName|**Language Status Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`languagelocale_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [Code](#BKMK_Code)
- [Language](#BKMK_Language)
- [Name](#BKMK_Name)
- [OrganizationId](#BKMK_OrganizationId)
- [Region](#BKMK_Region)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_Code"></a> Code

|Property|Value|
|---|---|
|Description|**Code**|
|DisplayName|**Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`code`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Language"></a> Language

|Property|Value|
|---|---|
|Description|**Language**|
|DisplayName|**Language**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`language`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the language locale.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_Region"></a> Region

|Property|Value|
|---|---|
|Description|**Region**|
|DisplayName|**Region**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`region`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

### <a name="BKMK_languagelocale_organization"></a> languagelocale_organization

One-To-Many Relationship: [organization languagelocale_organization](organization.md#BKMK_languagelocale_organization)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_knowledgearticle_languagelocaleid"></a> knowledgearticle_languagelocaleid

Many-To-One Relationship: [knowledgearticle knowledgearticle_languagelocaleid](knowledgearticle.md#BKMK_knowledgearticle_languagelocaleid)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`languagelocaleid`|
|ReferencedEntityNavigationPropertyName|`knowledgearticle_languagelocaleid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.languagelocale?displayProperty=fullName>
