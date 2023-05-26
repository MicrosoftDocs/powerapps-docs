---
title: "MobileOfflineProfile table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the MobileOfflineProfile table/entity."
ms.date: 05/23/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# MobileOfflineProfile table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Information to administer and manage the data available to mobile devices in offline mode.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|CloneMobileOfflineProfile|<xref:Microsoft.Dynamics.CRM.CloneMobileOfflineProfile?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.CloneMobileOfflineProfileRequest>|
|Create|POST [*org URI*]/api/data/v9.2/mobileofflineprofiles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.2/mobileofflineprofiles(*mobileofflineprofileid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.2/mobileofflineprofiles(*mobileofflineprofileid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.2/mobileofflineprofiles<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrieveUnpublished|<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
|RetrieveUnpublishedMultiple|<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
|Update|PATCH [*org URI*]/api/data/v9.2/mobileofflineprofiles(*mobileofflineprofileid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|Validate|<xref:Microsoft.Dynamics.CRM.Validate?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ValidateRequest>|
|ValidateSavedQuery|<xref:Microsoft.Dynamics.CRM.ValidateSavedQuery?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ValidateSavedQueryRequest>|
|ValidateUnpublished|<xref:Microsoft.Dynamics.CRM.ValidateUnpublished?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ValidateUnpublishedRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|MobileOfflineProfiles|
|DisplayCollectionName|Mobile Offline Profiles|
|DisplayName|Mobile Offline Profile|
|EntitySetName|mobileofflineprofiles|
|IsBPFEntity|False|
|LogicalCollectionName|mobileofflineprofiles|
|LogicalName|mobileofflineprofile|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mobileofflineprofileid|
|PrimaryNameAttribute|name|
|SchemaName|MobileOfflineProfile|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Description](#BKMK_Description)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [MobileOfflineProfileId](#BKMK_MobileOfflineProfileId)
- [Name](#BKMK_Name)
- [ProcessId](#BKMK_ProcessId)
- [StageId](#BKMK_StageId)
- [TraversedPath](#BKMK_TraversedPath)


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Enter a description of the mobile offline profile.|
|DisplayName|Description|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the Mobile offline Profile is introduced.|
|DisplayName|Introduced Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|introducedversion|
|MaxLength|48|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MobileOfflineProfileId"></a> MobileOfflineProfileId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the mobile offline profile.|
|DisplayName|Mobile Offline Profile|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mobileofflineprofileid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Enter the name of the mobile offline profile.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|255|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the process.|
|DisplayName|Process|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the stage.|
|DisplayName|(Deprecated) Process Stage|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|stageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|(Deprecated) Traversed Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|traversedpath|
|MaxLength|1250|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [IsValidated](#BKMK_IsValidated)
- [MobileOfflineProfileIdUnique](#BKMK_MobileOfflineProfileIdUnique)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PublishedOn](#BKMK_PublishedOn)
- [SelectedEntityMetadata](#BKMK_SelectedEntityMetadata)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record on behalf of another user.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed||
|0|Unmanaged||

**DefaultValue**: 0



### <a name="BKMK_IsValidated"></a> IsValidated

|Property|Value|
|--------|-----|
|Description|Information about whether profile is validated or not|
|DisplayName|Is Validated|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isvalidated|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsValidated Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_MobileOfflineProfileIdUnique"></a> MobileOfflineProfileIdUnique

|Property|Value|
|--------|-----|
|Description|For Internal Use Only|
|DisplayName|Unique Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mobileofflineprofileidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who updated the record on behalf of another user.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the Mobile Offline Profile.|
|DisplayName|Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_PublishedOn"></a> PublishedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Displays the last published date time.|
|DisplayName|Published On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|publishedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_SelectedEntityMetadata"></a> SelectedEntityMetadata

|Property|Value|
|--------|-----|
|Description|Internal Use Only|
|DisplayName|Internal Use Only|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|selectedentitymetadata|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the Mobile Offline Profile.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [DefaultMobileOfflineProfile_Organization](#BKMK_DefaultMobileOfflineProfile_Organization)
- [MobileOfflineProfile_MobileOfflineProfileItem](#BKMK_MobileOfflineProfile_MobileOfflineProfileItem)
- [MobileOfflineProfile_SystemUser](#BKMK_MobileOfflineProfile_SystemUser)
- [mobileofflineprofile_profileextension](#BKMK_mobileofflineprofile_profileextension)
- [mobileofflineprofile_mobileofflineprofile](#BKMK_mobileofflineprofile_mobileofflineprofile)
- [mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId](#BKMK_mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId)
- [mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId](#BKMK_mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId)


### <a name="BKMK_DefaultMobileOfflineProfile_Organization"></a> DefaultMobileOfflineProfile_Organization

Same as the [DefaultMobileOfflineProfile_Organization](organization.md#BKMK_DefaultMobileOfflineProfile_Organization) many-to-one relationship for the [organization](organization.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|organization|
|ReferencingAttribute|defaultmobileofflineprofileid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|DefaultMobileOfflineProfile_Organization|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_MobileOfflineProfile_MobileOfflineProfileItem"></a> MobileOfflineProfile_MobileOfflineProfileItem

Same as the [MobileOfflineProfile_MobileOfflineProfileItem](mobileofflineprofileitem.md#BKMK_MobileOfflineProfile_MobileOfflineProfileItem) many-to-one relationship for the [mobileofflineprofileitem](mobileofflineprofileitem.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofileitem|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|MobileOfflineProfile_MobileOfflineProfileItem|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_MobileOfflineProfile_SystemUser"></a> MobileOfflineProfile_SystemUser

Same as the [MobileOfflineProfile_SystemUser](systemuser.md#BKMK_MobileOfflineProfile_SystemUser) many-to-one relationship for the [systemuser](systemuser.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|mobileofflineprofileid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|MobileOfflineProfile_SystemUser|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mobileofflineprofile_profileextension"></a> mobileofflineprofile_profileextension

**Added by**: MobileOfflineProfileExtensionSolution Solution

Same as the [mobileofflineprofile_profileextension](mobileofflineprofileextension.md#BKMK_mobileofflineprofile_profileextension) many-to-one relationship for the [mobileofflineprofileextension](mobileofflineprofileextension.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofileextension|
|ReferencingAttribute|mobileofflineprofileid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|mobileofflineprofile_profileextension|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mobileofflineprofile_mobileofflineprofile"></a> mobileofflineprofile_mobileofflineprofile

**Added by**: MobileOfflineDirectDeviceSync Solution

Same as the [mobileofflineprofile_mobileofflineprofile](mobileofflineprofileitemfilter.md#BKMK_mobileofflineprofile_mobileofflineprofile) many-to-one relationship for the [mobileofflineprofileitemfilter](mobileofflineprofileitemfilter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mobileofflineprofileitemfilter|
|ReferencingAttribute|mobileofflineprofileid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mobileofflineprofile_mobileofflineprofile|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId"></a> mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId

**Added by**: MobileOfflineMembership Solution

Same as the [mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId](teammobileofflineprofilemembership.md#BKMK_mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId) many-to-one relationship for the [teammobileofflineprofilemembership](teammobileofflineprofilemembership.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|teammobileofflineprofilemembership|
|ReferencingAttribute|mobileofflineprofileid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId"></a> mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId

**Added by**: MobileOfflineMembership Solution

Same as the [mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId](usermobileofflineprofilemembership.md#BKMK_mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId) many-to-one relationship for the [usermobileofflineprofilemembership](usermobileofflineprofilemembership.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|usermobileofflineprofilemembership|
|ReferencingAttribute|mobileofflineprofileid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_MobileOfflineProfile_modifiedby](#BKMK_lk_MobileOfflineProfile_modifiedby)
- [MobileOfflineProfile_organization](#BKMK_MobileOfflineProfile_organization)
- [lk_MobileOfflineProfile_createdby](#BKMK_lk_MobileOfflineProfile_createdby)
- [lk_MobileOfflineProfile_createdonbehalfby](#BKMK_lk_MobileOfflineProfile_createdonbehalfby)
- [lk_MobileOfflineProfile_modifiedonbehalfby](#BKMK_lk_MobileOfflineProfile_modifiedonbehalfby)


### <a name="BKMK_lk_MobileOfflineProfile_modifiedby"></a> lk_MobileOfflineProfile_modifiedby

See the [lk_MobileOfflineProfile_modifiedby](systemuser.md#BKMK_lk_MobileOfflineProfile_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_MobileOfflineProfile_organization"></a> MobileOfflineProfile_organization

See the [MobileOfflineProfile_organization](organization.md#BKMK_MobileOfflineProfile_organization) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_lk_MobileOfflineProfile_createdby"></a> lk_MobileOfflineProfile_createdby

See the [lk_MobileOfflineProfile_createdby](systemuser.md#BKMK_lk_MobileOfflineProfile_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_MobileOfflineProfile_createdonbehalfby"></a> lk_MobileOfflineProfile_createdonbehalfby

See the [lk_MobileOfflineProfile_createdonbehalfby](systemuser.md#BKMK_lk_MobileOfflineProfile_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_MobileOfflineProfile_modifiedonbehalfby"></a> lk_MobileOfflineProfile_modifiedonbehalfby

See the [lk_MobileOfflineProfile_modifiedonbehalfby](systemuser.md#BKMK_lk_MobileOfflineProfile_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.mobileofflineprofile?text=mobileofflineprofile EntityType" />