---
title: "AIPluginTitle table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the AIPluginTitle table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# AIPluginTitle table/entity reference (Microsoft Dataverse)

AIPlugin Title

## Messages

The following table lists the messages for the AIPluginTitle table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /aiplugintitles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /aiplugintitles(*aiplugintitleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /aiplugintitles(*aiplugintitleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /aiplugintitles<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveUnpublished`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `SetState`<br />Event: True |`PATCH` /aiplugintitles(*aiplugintitleid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /aiplugintitles(*aiplugintitleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /aiplugintitles(*aiplugintitleid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the AIPluginTitle table.

|Property|Value|
| --- | --- |
| **DisplayName** | **AIPluginTitle** |
| **DisplayCollectionName** | **AIPluginTitles** |
| **SchemaName** | `AIPluginTitle` |
| **CollectionSchemaName** | `AIPluginTitles` |
| **EntitySetName** | `aiplugintitles`|
| **LogicalName** | `aiplugintitle` |
| **LogicalCollectionName** | `aiplugintitles` |
| **PrimaryIdAttribute** | `aiplugintitleid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccentColor](#BKMK_AccentColor)
- [AIPluginTitleId](#BKMK_AIPluginTitleId)
- [BaseArtifactId](#BKMK_BaseArtifactId)
- [Description](#BKMK_Description)
- [DeveloperName](#BKMK_DeveloperName)
- [DisplayName](#BKMK_DisplayName)
- [Icon](#BKMK_Icon)
- [IconsColorImage](#BKMK_IconsColorImage)
- [IconsOutlineImage](#BKMK_IconsOutlineImage)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustom](#BKMK_IsCustom)
- [IsCustomizable](#BKMK_IsCustomizable)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PluginTitleVersion](#BKMK_PluginTitleVersion)
- [PrivacyURL](#BKMK_PrivacyURL)
- [ShortDescription](#BKMK_ShortDescription)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TermsOfUseUrl](#BKMK_TermsOfUseUrl)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [WebsiteUrl](#BKMK_WebsiteUrl)

### <a name="BKMK_AccentColor"></a> AccentColor

|Property|Value|
|---|---|
|Description|**Accent Color**|
|DisplayName|**Accent Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`accentcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25|

### <a name="BKMK_AIPluginTitleId"></a> AIPluginTitleId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**AIPluginTitle**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`aiplugintitleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_BaseArtifactId"></a> BaseArtifactId

|Property|Value|
|---|---|
|Description|**BaseArtifact Id**|
|DisplayName|**BaseArtifactId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`baseartifactid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_DeveloperName"></a> DeveloperName

|Property|Value|
|---|---|
|Description|**Developer Name**|
|DisplayName|**Developer Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`developername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|---|---|
|Description|**Display Name**|
|DisplayName|**DisplayName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`displayname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Icon"></a> Icon

|Property|Value|
|---|---|
|Description|**Icon URI**|
|DisplayName|**Icon**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`icon`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_IconsColorImage"></a> IconsColorImage

|Property|Value|
|---|---|
|Description|**Icons Color Image**|
|DisplayName|**Icons Color Image**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iconscolorimage`|
|RequiredLevel|None|
|Type|Image|
|CanStoreFullImage|True|
|IsPrimaryImage|True|
|MaxHeight|144|
|MaxSizeInKB|10240|
|MaxWidth|144|

### <a name="BKMK_IconsOutlineImage"></a> IconsOutlineImage

|Property|Value|
|---|---|
|Description|**Icons Outline Image**|
|DisplayName|**Icons Outline Image**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iconsoutlineimage`|
|RequiredLevel|None|
|Type|Image|
|CanStoreFullImage|True|
|IsPrimaryImage|False|
|MaxHeight|144|
|MaxSizeInKB|10240|
|MaxWidth|144|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsCustom"></a> IsCustom

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsCustom**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iscustom`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`aiplugintitle_iscustom`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PluginTitleVersion"></a> PluginTitleVersion

|Property|Value|
|---|---|
|Description|**Plugin Title Version**|
|DisplayName|**Plugin Title Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`plugintitleversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25|

### <a name="BKMK_PrivacyURL"></a> PrivacyURL

|Property|Value|
|---|---|
|Description|**Privacy URL**|
|DisplayName|**PrivacyURL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`privacyurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ShortDescription"></a> ShortDescription

|Property|Value|
|---|---|
|Description|**Short Description**|
|DisplayName|**Short Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`shortdescription`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the AIPluginTitle**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`aiplugintitle_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the AIPluginTitle**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`aiplugintitle_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TermsOfUseUrl"></a> TermsOfUseUrl

|Property|Value|
|---|---|
|Description|**Terms Of Use Url**|
|DisplayName|**Terms Of Use Url**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`termsofuseurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_WebsiteUrl"></a> WebsiteUrl

|Property|Value|
|---|---|
|Description|**Website Url**|
|DisplayName|**Website Url**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`websiteurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|300|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IconsColorImage_Timestamp](#BKMK_IconsColorImage_Timestamp)
- [IconsColorImage_URL](#BKMK_IconsColorImage_URL)
- [IconsColorImageId](#BKMK_IconsColorImageId)
- [IconsOutlineImage_Timestamp](#BKMK_IconsOutlineImage_Timestamp)
- [IconsOutlineImage_URL](#BKMK_IconsOutlineImage_URL)
- [IconsOutlineImageId](#BKMK_IconsOutlineImageId)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IconsColorImage_Timestamp"></a> IconsColorImage_Timestamp

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iconscolorimage_timestamp`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_IconsColorImage_URL"></a> IconsColorImage_URL

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iconscolorimage_url`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_IconsColorImageId"></a> IconsColorImageId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iconscolorimageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_IconsOutlineImage_Timestamp"></a> IconsOutlineImage_Timestamp

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iconsoutlineimage_timestamp`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_IconsOutlineImage_URL"></a> IconsOutlineImage_URL

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iconsoutlineimage_url`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_IconsOutlineImageId"></a> IconsOutlineImageId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iconsoutlineimageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_aiplugintitle_createdby](#BKMK_lk_aiplugintitle_createdby)
- [lk_aiplugintitle_createdonbehalfby](#BKMK_lk_aiplugintitle_createdonbehalfby)
- [lk_aiplugintitle_modifiedby](#BKMK_lk_aiplugintitle_modifiedby)
- [lk_aiplugintitle_modifiedonbehalfby](#BKMK_lk_aiplugintitle_modifiedonbehalfby)
- [organization_aiplugintitle](#BKMK_organization_aiplugintitle)

### <a name="BKMK_lk_aiplugintitle_createdby"></a> lk_aiplugintitle_createdby

One-To-Many Relationship: [systemuser lk_aiplugintitle_createdby](systemuser.md#BKMK_lk_aiplugintitle_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_aiplugintitle_createdonbehalfby"></a> lk_aiplugintitle_createdonbehalfby

One-To-Many Relationship: [systemuser lk_aiplugintitle_createdonbehalfby](systemuser.md#BKMK_lk_aiplugintitle_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_aiplugintitle_modifiedby"></a> lk_aiplugintitle_modifiedby

One-To-Many Relationship: [systemuser lk_aiplugintitle_modifiedby](systemuser.md#BKMK_lk_aiplugintitle_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_aiplugintitle_modifiedonbehalfby"></a> lk_aiplugintitle_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_aiplugintitle_modifiedonbehalfby](systemuser.md#BKMK_lk_aiplugintitle_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_aiplugintitle"></a> organization_aiplugintitle

One-To-Many Relationship: [organization organization_aiplugintitle](organization.md#BKMK_organization_aiplugintitle)

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

- [aiplugin_AIPluginTitle_aiplugintitle](#BKMK_aiplugin_AIPluginTitle_aiplugintitle)
- [aiplugintitle_AsyncOperations](#BKMK_aiplugintitle_AsyncOperations)
- [aiplugintitle_BulkDeleteFailures](#BKMK_aiplugintitle_BulkDeleteFailures)
- [aiplugintitle_DuplicateBaseRecord](#BKMK_aiplugintitle_DuplicateBaseRecord)
- [aiplugintitle_DuplicateMatchingRecord](#BKMK_aiplugintitle_DuplicateMatchingRecord)
- [aiplugintitle_MailboxTrackingFolders](#BKMK_aiplugintitle_MailboxTrackingFolders)
- [aiplugintitle_PrincipalObjectAttributeAccesses](#BKMK_aiplugintitle_PrincipalObjectAttributeAccesses)
- [aiplugintitle_ProcessSession](#BKMK_aiplugintitle_ProcessSession)
- [aiplugintitle_SyncErrors](#BKMK_aiplugintitle_SyncErrors)

### <a name="BKMK_aiplugin_AIPluginTitle_aiplugintitle"></a> aiplugin_AIPluginTitle_aiplugintitle

Many-To-One Relationship: [aiplugin aiplugin_AIPluginTitle_aiplugintitle](aiplugin.md#BKMK_aiplugin_AIPluginTitle_aiplugintitle)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugin`|
|ReferencingAttribute|`aiplugintitle`|
|ReferencedEntityNavigationPropertyName|`aiplugin_AIPluginTitle_aiplugintitle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugintitle_AsyncOperations"></a> aiplugintitle_AsyncOperations

Many-To-One Relationship: [asyncoperation aiplugintitle_AsyncOperations](asyncoperation.md#BKMK_aiplugintitle_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aiplugintitle_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugintitle_BulkDeleteFailures"></a> aiplugintitle_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure aiplugintitle_BulkDeleteFailures](bulkdeletefailure.md#BKMK_aiplugintitle_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aiplugintitle_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugintitle_DuplicateBaseRecord"></a> aiplugintitle_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord aiplugintitle_DuplicateBaseRecord](duplicaterecord.md#BKMK_aiplugintitle_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`aiplugintitle_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugintitle_DuplicateMatchingRecord"></a> aiplugintitle_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord aiplugintitle_DuplicateMatchingRecord](duplicaterecord.md#BKMK_aiplugintitle_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`aiplugintitle_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugintitle_MailboxTrackingFolders"></a> aiplugintitle_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder aiplugintitle_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_aiplugintitle_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aiplugintitle_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugintitle_PrincipalObjectAttributeAccesses"></a> aiplugintitle_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess aiplugintitle_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_aiplugintitle_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`aiplugintitle_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugintitle_ProcessSession"></a> aiplugintitle_ProcessSession

Many-To-One Relationship: [processsession aiplugintitle_ProcessSession](processsession.md#BKMK_aiplugintitle_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aiplugintitle_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_aiplugintitle_SyncErrors"></a> aiplugintitle_SyncErrors

Many-To-One Relationship: [syncerror aiplugintitle_SyncErrors](syncerror.md#BKMK_aiplugintitle_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`aiplugintitle_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.aiplugintitle?displayProperty=fullName>
