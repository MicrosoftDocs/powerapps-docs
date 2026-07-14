---
title: "Mobile Offline Profile (MobileOfflineProfile) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Mobile Offline Profile (MobileOfflineProfile) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Mobile Offline Profile (MobileOfflineProfile) table/entity reference (Microsoft Dataverse)

Information to administer and manage the data available to mobile devices in offline mode.

## Messages

The following table lists the messages for the Mobile Offline Profile (MobileOfflineProfile) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `CloneMobileOfflineProfile`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CloneMobileOfflineProfile?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.CloneMobileOfflineProfileRequest>|
| `Create`<br />Event: False |`POST` /mobileofflineprofiles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /mobileofflineprofiles(*mobileofflineprofileid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /mobileofflineprofiles(*mobileofflineprofileid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /mobileofflineprofiles<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveUnpublished`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `Update`<br />Event: False |`PATCH` /mobileofflineprofiles(*mobileofflineprofileid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /mobileofflineprofiles(*mobileofflineprofileid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `Validate`<br />Event: False |<xref:Microsoft.Dynamics.CRM.Validate?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ValidateRequest>|
| `ValidateSavedQuery`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ValidateSavedQuery?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ValidateSavedQueryRequest>|
| `ValidateUnpublished`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ValidateUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ValidateUnpublishedRequest>|

## Properties

The following table lists selected properties for the Mobile Offline Profile (MobileOfflineProfile) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Mobile Offline Profile** |
| **DisplayCollectionName** | **Mobile Offline Profiles** |
| **SchemaName** | `MobileOfflineProfile` |
| **CollectionSchemaName** | `MobileOfflineProfiles` |
| **EntitySetName** | `mobileofflineprofiles`|
| **LogicalName** | `mobileofflineprofile` |
| **LogicalCollectionName** | `mobileofflineprofiles` |
| **PrimaryIdAttribute** | `mobileofflineprofileid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

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
|---|---|
|Description|**Enter a description of the mobile offline profile.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the Mobile offline Profile is introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_MobileOfflineProfileId"></a> MobileOfflineProfileId

|Property|Value|
|---|---|
|Description|**Unique identifier of the mobile offline profile.**|
|DisplayName|**Mobile Offline Profile**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mobileofflineprofileid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Enter the name of the mobile offline profile.**|
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
|MaxLength|255|

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**Shows the ID of the process.**|
|DisplayName|**Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|---|---|
|Description|**Shows the ID of the stage.**|
|DisplayName|**(Deprecated) Process Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**(Deprecated) Traversed Path**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`traversedpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [IsValidated](#BKMK_IsValidated)
- [MobileOfflineProfileIdUnique](#BKMK_MobileOfflineProfileIdUnique)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PublishedOn](#BKMK_PublishedOn)
- [SelectedEntityMetadata](#BKMK_SelectedEntityMetadata)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

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
|DefaultFormValue|-1|
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
|Description|**Shows who created the record.**|
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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**For internal use only.**|
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

### <a name="BKMK_IsValidated"></a> IsValidated

|Property|Value|
|---|---|
|Description|**Information about whether profile is validated or not**|
|DisplayName|**Is Validated**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isvalidated`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`mobileofflineprofile_isvalidated`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MobileOfflineProfileIdUnique"></a> MobileOfflineProfileIdUnique

|Property|Value|
|---|---|
|Description|**For Internal Use Only**|
|DisplayName|**Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mobileofflineprofileidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who updated the record on behalf of another user.**|
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
|Description|**Unique identifier of the organization associated with the Mobile Offline Profile.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
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
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PublishedOn"></a> PublishedOn

|Property|Value|
|---|---|
|Description|**Displays the last published date time.**|
|DisplayName|**Published On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publishedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SelectedEntityMetadata"></a> SelectedEntityMetadata

|Property|Value|
|---|---|
|Description|**Internal Use Only**|
|DisplayName|**Internal Use Only**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`selectedentitymetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

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
|Description|**Version number of the Mobile Offline Profile.**|
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

- [lk_MobileOfflineProfile_createdby](#BKMK_lk_MobileOfflineProfile_createdby)
- [lk_MobileOfflineProfile_createdonbehalfby](#BKMK_lk_MobileOfflineProfile_createdonbehalfby)
- [lk_MobileOfflineProfile_modifiedby](#BKMK_lk_MobileOfflineProfile_modifiedby)
- [lk_MobileOfflineProfile_modifiedonbehalfby](#BKMK_lk_MobileOfflineProfile_modifiedonbehalfby)
- [MobileOfflineProfile_organization](#BKMK_MobileOfflineProfile_organization)

### <a name="BKMK_lk_MobileOfflineProfile_createdby"></a> lk_MobileOfflineProfile_createdby

One-To-Many Relationship: [systemuser lk_MobileOfflineProfile_createdby](systemuser.md#BKMK_lk_MobileOfflineProfile_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_MobileOfflineProfile_createdonbehalfby"></a> lk_MobileOfflineProfile_createdonbehalfby

One-To-Many Relationship: [systemuser lk_MobileOfflineProfile_createdonbehalfby](systemuser.md#BKMK_lk_MobileOfflineProfile_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_MobileOfflineProfile_modifiedby"></a> lk_MobileOfflineProfile_modifiedby

One-To-Many Relationship: [systemuser lk_MobileOfflineProfile_modifiedby](systemuser.md#BKMK_lk_MobileOfflineProfile_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_MobileOfflineProfile_modifiedonbehalfby"></a> lk_MobileOfflineProfile_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_MobileOfflineProfile_modifiedonbehalfby](systemuser.md#BKMK_lk_MobileOfflineProfile_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_MobileOfflineProfile_organization"></a> MobileOfflineProfile_organization

One-To-Many Relationship: [organization MobileOfflineProfile_organization](organization.md#BKMK_MobileOfflineProfile_organization)

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

- [DefaultMobileOfflineProfile_Organization](#BKMK_DefaultMobileOfflineProfile_Organization)
- [mobileofflineprofile_mobileofflineprofile](#BKMK_mobileofflineprofile_mobileofflineprofile)
- [MobileOfflineProfile_MobileOfflineProfileItem](#BKMK_MobileOfflineProfile_MobileOfflineProfileItem)
- [mobileofflineprofile_profileextension](#BKMK_mobileofflineprofile_profileextension)
- [MobileOfflineProfile_SystemUser](#BKMK_MobileOfflineProfile_SystemUser)
- [mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId](#BKMK_mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId)
- [mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId](#BKMK_mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId)

### <a name="BKMK_DefaultMobileOfflineProfile_Organization"></a> DefaultMobileOfflineProfile_Organization

Many-To-One Relationship: [organization DefaultMobileOfflineProfile_Organization](organization.md#BKMK_DefaultMobileOfflineProfile_Organization)

|Property|Value|
|---|---|
|ReferencingEntity|`organization`|
|ReferencingAttribute|`defaultmobileofflineprofileid`|
|ReferencedEntityNavigationPropertyName|`DefaultMobileOfflineProfile_Organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mobileofflineprofile_mobileofflineprofile"></a> mobileofflineprofile_mobileofflineprofile

Many-To-One Relationship: [mobileofflineprofileitemfilter mobileofflineprofile_mobileofflineprofile](mobileofflineprofileitemfilter.md#BKMK_mobileofflineprofile_mobileofflineprofile)

|Property|Value|
|---|---|
|ReferencingEntity|`mobileofflineprofileitemfilter`|
|ReferencingAttribute|`mobileofflineprofileid`|
|ReferencedEntityNavigationPropertyName|`mobileofflineprofile_mobileofflineprofile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_MobileOfflineProfile_MobileOfflineProfileItem"></a> MobileOfflineProfile_MobileOfflineProfileItem

Many-To-One Relationship: [mobileofflineprofileitem MobileOfflineProfile_MobileOfflineProfileItem](mobileofflineprofileitem.md#BKMK_MobileOfflineProfile_MobileOfflineProfileItem)

|Property|Value|
|---|---|
|ReferencingEntity|`mobileofflineprofileitem`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`MobileOfflineProfile_MobileOfflineProfileItem`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mobileofflineprofile_profileextension"></a> mobileofflineprofile_profileextension

Many-To-One Relationship: [mobileofflineprofileextension mobileofflineprofile_profileextension](mobileofflineprofileextension.md#BKMK_mobileofflineprofile_profileextension)

|Property|Value|
|---|---|
|ReferencingEntity|`mobileofflineprofileextension`|
|ReferencingAttribute|`mobileofflineprofileid`|
|ReferencedEntityNavigationPropertyName|`mobileofflineprofile_profileextension`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_MobileOfflineProfile_SystemUser"></a> MobileOfflineProfile_SystemUser

Many-To-One Relationship: [systemuser MobileOfflineProfile_SystemUser](systemuser.md#BKMK_MobileOfflineProfile_SystemUser)

|Property|Value|
|---|---|
|ReferencingEntity|`systemuser`|
|ReferencingAttribute|`mobileofflineprofileid`|
|ReferencedEntityNavigationPropertyName|`MobileOfflineProfile_SystemUser`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId"></a> mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId

Many-To-One Relationship: [teammobileofflineprofilemembership mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId](teammobileofflineprofilemembership.md#BKMK_mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId)

|Property|Value|
|---|---|
|ReferencingEntity|`teammobileofflineprofilemembership`|
|ReferencingAttribute|`mobileofflineprofileid`|
|ReferencedEntityNavigationPropertyName|`mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId"></a> mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId

Many-To-One Relationship: [usermobileofflineprofilemembership mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId](usermobileofflineprofilemembership.md#BKMK_mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId)

|Property|Value|
|---|---|
|ReferencingEntity|`usermobileofflineprofilemembership`|
|ReferencingAttribute|`mobileofflineprofileid`|
|ReferencedEntityNavigationPropertyName|`mobileofflineprofile_usermobileofflineprofilemembership_MobileOfflineProfileId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mobileofflineprofile?displayProperty=fullName>
