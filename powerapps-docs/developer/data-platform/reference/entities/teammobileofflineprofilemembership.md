---
title: "teammobileofflineprofilemembership table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the teammobileofflineprofilemembership table/entity."
ms.date: 03/04/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# teammobileofflineprofilemembership table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: MobileOfflineMembership Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|teammobileofflineprofilememberships|
|DisplayCollectionName|TeamMobileOfflineProfileMemberships|
|DisplayName|TeamMobileOfflineProfileMembership|
|EntitySetName|teammobileofflineprofilememberships|
|IsBPFEntity|False|
|LogicalCollectionName|teammobileofflineprofilememberships|
|LogicalName|teammobileofflineprofilemembership|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|teammobileofflineprofilemembershipid|
|PrimaryNameAttribute|name|
|SchemaName|teammobileofflineprofilemembership|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [MobileOfflineProfileId](#BKMK_MobileOfflineProfileId)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TeamId](#BKMK_TeamId)
- [teammobileofflineprofilemembershipId](#BKMK_teammobileofflineprofilemembershipId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_MobileOfflineProfileId"></a> MobileOfflineProfileId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|MobileOfflineProfileId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mobileofflineprofileid|
|RequiredLevel|None|
|Targets|mobileofflineprofile|
|Type|Lookup|


### <a name="BKMK_name"></a> name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the TeamMobileOfflineProfileMembership|
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
|Description|Reason for the status of the TeamMobileOfflineProfileMembership|
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



### <a name="BKMK_TeamId"></a> TeamId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|TeamId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|teamid|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_teammobileofflineprofilemembershipId"></a> teammobileofflineprofilemembershipId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|TeamMobileOfflineProfileMembership|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|teammobileofflineprofilemembershipid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [MobileOfflineProfileIdName](#BKMK_MobileOfflineProfileIdName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [TeamIdName](#BKMK_TeamIdName)
- [TeamIdYomiName](#BKMK_TeamIdYomiName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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


### <a name="BKMK_MobileOfflineProfileIdName"></a> MobileOfflineProfileIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mobileofflineprofileidname|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|Description|Date and time when the record was modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Added by**: Active Solution Solution

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


### <a name="BKMK_TeamIdName"></a> TeamIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|teamidname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TeamIdYomiName"></a> TeamIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|teamidyominame|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version number of TeamMobileOfflineProfileMembership.|
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

- [teammobileofflineprofilemembership_SyncErrors](#BKMK_teammobileofflineprofilemembership_SyncErrors)
- [teammobileofflineprofilemembership_AsyncOperations](#BKMK_teammobileofflineprofilemembership_AsyncOperations)
- [teammobileofflineprofilemembership_MailboxTrackingFolders](#BKMK_teammobileofflineprofilemembership_MailboxTrackingFolders)
- [teammobileofflineprofilemembership_ProcessSession](#BKMK_teammobileofflineprofilemembership_ProcessSession)
- [teammobileofflineprofilemembership_BulkDeleteFailures](#BKMK_teammobileofflineprofilemembership_BulkDeleteFailures)
- [teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses](#BKMK_teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses)


### <a name="BKMK_teammobileofflineprofilemembership_SyncErrors"></a> teammobileofflineprofilemembership_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [teammobileofflineprofilemembership_SyncErrors](syncerror.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|teammobileofflineprofilemembership_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_teammobileofflineprofilemembership_AsyncOperations"></a> teammobileofflineprofilemembership_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [teammobileofflineprofilemembership_AsyncOperations](asyncoperation.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|teammobileofflineprofilemembership_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_teammobileofflineprofilemembership_MailboxTrackingFolders"></a> teammobileofflineprofilemembership_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [teammobileofflineprofilemembership_MailboxTrackingFolders](mailboxtrackingfolder.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|teammobileofflineprofilemembership_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_teammobileofflineprofilemembership_ProcessSession"></a> teammobileofflineprofilemembership_ProcessSession

**Added by**: System Solution Solution

Same as processsession table [teammobileofflineprofilemembership_ProcessSession](processsession.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|teammobileofflineprofilemembership_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_teammobileofflineprofilemembership_BulkDeleteFailures"></a> teammobileofflineprofilemembership_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [teammobileofflineprofilemembership_BulkDeleteFailures](bulkdeletefailure.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|teammobileofflineprofilemembership_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses"></a> teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|teammobileofflineprofilemembership_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_teammobileofflineprofilemembership_createdby](#BKMK_lk_teammobileofflineprofilemembership_createdby)
- [lk_teammobileofflineprofilemembership_createdonbehalfby](#BKMK_lk_teammobileofflineprofilemembership_createdonbehalfby)
- [lk_teammobileofflineprofilemembership_modifiedby](#BKMK_lk_teammobileofflineprofilemembership_modifiedby)
- [lk_teammobileofflineprofilemembership_modifiedonbehalfby](#BKMK_lk_teammobileofflineprofilemembership_modifiedonbehalfby)
- [organization_teammobileofflineprofilemembership](#BKMK_organization_teammobileofflineprofilemembership)
- [mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId](#BKMK_mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId)
- [team_teammobileofflineprofilemembership_TeamId](#BKMK_team_teammobileofflineprofilemembership_TeamId)


### <a name="BKMK_lk_teammobileofflineprofilemembership_createdby"></a> lk_teammobileofflineprofilemembership_createdby

**Added by**: System Solution Solution

See systemuser Table [lk_teammobileofflineprofilemembership_createdby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_lk_teammobileofflineprofilemembership_createdonbehalfby"></a> lk_teammobileofflineprofilemembership_createdonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_teammobileofflineprofilemembership_createdonbehalfby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_lk_teammobileofflineprofilemembership_modifiedby"></a> lk_teammobileofflineprofilemembership_modifiedby

**Added by**: System Solution Solution

See systemuser Table [lk_teammobileofflineprofilemembership_modifiedby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_lk_teammobileofflineprofilemembership_modifiedonbehalfby"></a> lk_teammobileofflineprofilemembership_modifiedonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_teammobileofflineprofilemembership_modifiedonbehalfby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_organization_teammobileofflineprofilemembership"></a> organization_teammobileofflineprofilemembership

**Added by**: System Solution Solution

See organization Table [organization_teammobileofflineprofilemembership](organization.md) One-To-Many relationship.

### <a name="BKMK_mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId"></a> mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId

**Added by**: System Solution Solution

See mobileofflineprofile Table [mobileofflineprofile_teammobileofflineprofilemembership_MobileOfflineProfileId](mobileofflineprofile.md) One-To-Many relationship.

### <a name="BKMK_team_teammobileofflineprofilemembership_TeamId"></a> team_teammobileofflineprofilemembership_TeamId

**Added by**: System Solution Solution

See team Table [team_teammobileofflineprofilemembership_TeamId](team.md) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.teammobileofflineprofilemembership?text=teammobileofflineprofilemembership EntityType" />