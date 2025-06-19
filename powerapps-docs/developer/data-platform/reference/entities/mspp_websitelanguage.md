---
title: "Website Language (mspp_websitelanguage) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Website Language (mspp_websitelanguage) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Website Language (mspp_websitelanguage) table/entity reference (Microsoft Dataverse)

Languages supported and publishing status for the portal

## Messages

The following table lists the messages for the Website Language (mspp_websitelanguage) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_websitelanguages<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_websitelanguages(*mspp_websitelanguageid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_websitelanguages(*mspp_websitelanguageid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_websitelanguages<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_websitelanguages(*mspp_websitelanguageid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_websitelanguages(*mspp_websitelanguageid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Website Language (mspp_websitelanguage) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Website Language (mspp_websitelanguage) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Website Language** |
| **DisplayCollectionName** | **Website Languages** |
| **SchemaName** | `mspp_websitelanguage` |
| **CollectionSchemaName** | `mspp_websitelanguages` |
| **EntitySetName** | `mspp_websitelanguages`|
| **LogicalName** | `mspp_websitelanguage` |
| **LogicalCollectionName** | `mspp_websitelanguages` |
| **PrimaryIdAttribute** | `mspp_websitelanguageid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

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
|MaxLength|2000|

### <a name="BKMK_mspp_displayname"></a> mspp_displayname

|Property|Value|
|---|---|
|Description|**Localized display name of the portal language**|
|DisplayName|**Portal Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_displayname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_languagecode"></a> mspp_languagecode

|Property|Value|
|---|---|
|Description|**Locale or language identifier that appears in the URL to indicate the portal language**|
|DisplayName|**Language Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_languagecode`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_lcid"></a> mspp_lcid

|Property|Value|
|---|---|
|Description|**Locale ID that is assigned to the portal language**|
|DisplayName|**Language Code Identifier**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_lcid`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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

### <a name="BKMK_mspp_name"></a> mspp_name

|Property|Value|
|---|---|
|Description|**Name of the portal language**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_publishingstate"></a> mspp_publishingstate

|Property|Value|
|---|---|
|Description|**Lookup to Publishing State - publishing state of this website/language instance (draft/published)**|
|DisplayName|**Publishing State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_publishingstate`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_publishingstate|

### <a name="BKMK_mspp_systemlanguage"></a> mspp_systemlanguage

|Property|Value|
|---|---|
|Description|**The system language determines which portal languages are available**|
|DisplayName|**System Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_systemlanguage`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Lookup to Website**|
|DisplayName|**Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_websiteid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_website|

### <a name="BKMK_mspp_websitelanguageId"></a> mspp_websitelanguageId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Website Language**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_websitelanguageid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_websitelcid"></a> mspp_websitelcid

|Property|Value|
|---|---|
|Description|**This attribute is used only in Power Pages Management App, and only for UI purpose. It's value is mapped to mspp\_systemlanguage.**|
|DisplayName|**Power Pages Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_websitelcid`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`powerpagelanguages`|

#### mspp_websitelcid Choices/Options

|Value|Label|
|---|---|
|1025|**Arabic**|
|1026|**Bulgarian - Bulgaria**|
|1027|**Catalan - Catalan**|
|1028|**Chinese - Traditional**|
|1029|**Czech - Czech Republic**|
|1030|**Danish - Denmark**|
|1031|**German - Germany**|
|1032|**Greek - Greece**|
|1033|**English**|
|1035|**Finnish - Finland**|
|1036|**French - France**|
|1037|**Hebrew**|
|1038|**Hungarian - Hungary**|
|1040|**Italian - Italy**|
|1041|**Japanese - Japan**|
|1042|**Korean - Korea**|
|1043|**Dutch - Netherlands**|
|1044|**Norwegian (Bokmål) - Norway**|
|1045|**Polish - Poland**|
|1046|**Portuguese - Brazil**|
|1048|**Romanian - Romania**|
|1049|**Russian - Russia**|
|1050|**Croatian - Croatia**|
|1051|**Slovak - Slovakia**|
|1053|**Swedish - Sweden**|
|1054|**Thai - Thailand**|
|1055|**Turkish - Türkiye**|
|1057|**Indonesian - Indonesia**|
|1058|**Ukrainian - Ukraine**|
|1060|**Slovenian - Slovenia**|
|1061|**Estonian - Estonia**|
|1062|**Latvian - Latvia**|
|1063|**Lithuanian - Lithuania**|
|1066|**Vietnamese - Vietnam**|
|1069|**Basque - Basque**|
|1081|**Hindi - India**|
|1086|**Malay - Malaysia**|
|1087|**Kazakh - Kazakhstan**|
|1110|**Galician - Spain**|
|2052|**Chinese - China**|
|2070|**Portuguese - Portugal**|
|2074|**Serbian (Latin) - Serbia**|
|3076|**Chinese - Hong Kong SAR**|
|3082|**Spanish (Traditional Sort) - Spain**|
|3098|**Serbian (Cyrillic) - Serbia**|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Website Language**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_websitelanguage_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Website Language**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_websitelanguage_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState](#BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState)
- [mspp_mspp_website_mspp_websitelanguage](#BKMK_mspp_mspp_website_mspp_websitelanguage)
- [mspp_systemuser_mspp_websitelanguage_createdby](#BKMK_mspp_systemuser_mspp_websitelanguage_createdby)
- [mspp_systemuser_mspp_websitelanguage_modifiedby](#BKMK_mspp_systemuser_mspp_websitelanguage_modifiedby)

### <a name="BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState"></a> mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState

One-To-Many Relationship: [mspp_publishingstate mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState](mspp_publishingstate.md#BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstate`|
|ReferencedAttribute|`mspp_publishingstateid`|
|ReferencingAttribute|`mspp_publishingstate`|
|ReferencingEntityNavigationPropertyName|`mspp_PublishingState`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_mspp_website_mspp_websitelanguage"></a> mspp_mspp_website_mspp_websitelanguage

One-To-Many Relationship: [mspp_website mspp_mspp_website_mspp_websitelanguage](mspp_website.md#BKMK_mspp_mspp_website_mspp_websitelanguage)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_WebsiteId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_websitelanguage_createdby"></a> mspp_systemuser_mspp_websitelanguage_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_websitelanguage_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_websitelanguage_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_websitelanguage_modifiedby"></a> mspp_systemuser_mspp_websitelanguage_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_websitelanguage_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_websitelanguage_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [mspp_mspp_websitelanguage_mspp_website_DefaultLanguage](#BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage)
- [mspp_websitelanguage_contentsnippet_contentsnippetlanguageid](#BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid)
- [mspp_websitelanguage_weblinkset](#BKMK_mspp_websitelanguage_weblinkset)
- [mspp_websitelanguage_webpage_webpagelanguageid](#BKMK_mspp_websitelanguage_webpage_webpagelanguageid)

### <a name="BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage"></a> mspp_mspp_websitelanguage_mspp_website_DefaultLanguage

Many-To-One Relationship: [mspp_website mspp_mspp_websitelanguage_mspp_website_DefaultLanguage](mspp_website.md#BKMK_mspp_mspp_websitelanguage_mspp_website_DefaultLanguage)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_website`|
|ReferencingAttribute|`mspp_defaultlanguage`|
|ReferencedEntityNavigationPropertyName|`mspp_mspp_websitelanguage_mspp_website_DefaultLanguage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid"></a> mspp_websitelanguage_contentsnippet_contentsnippetlanguageid

Many-To-One Relationship: [mspp_contentsnippet mspp_websitelanguage_contentsnippet_contentsnippetlanguageid](mspp_contentsnippet.md#BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_contentsnippet`|
|ReferencingAttribute|`mspp_contentsnippetlanguageid`|
|ReferencedEntityNavigationPropertyName|`mspp_websitelanguage_contentsnippet_contentsnippetlanguageid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_websitelanguage_weblinkset"></a> mspp_websitelanguage_weblinkset

Many-To-One Relationship: [mspp_weblinkset mspp_websitelanguage_weblinkset](mspp_weblinkset.md#BKMK_mspp_websitelanguage_weblinkset)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_weblinkset`|
|ReferencingAttribute|`mspp_websitelanguageid`|
|ReferencedEntityNavigationPropertyName|`mspp_websitelanguage_weblinkset`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_websitelanguage_webpage_webpagelanguageid"></a> mspp_websitelanguage_webpage_webpagelanguageid

Many-To-One Relationship: [mspp_webpage mspp_websitelanguage_webpage_webpagelanguageid](mspp_webpage.md#BKMK_mspp_websitelanguage_webpage_webpagelanguageid)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_webpagelanguageid`|
|ReferencedEntityNavigationPropertyName|`mspp_websitelanguage_webpage_webpagelanguageid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_websitelanguage?displayProperty=fullName>
