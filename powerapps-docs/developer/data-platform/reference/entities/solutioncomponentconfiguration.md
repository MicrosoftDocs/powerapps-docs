---
title: "solutioncomponentconfiguration table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the solutioncomponentconfiguration table/entity."
ms.date: 05/20/2021
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

# solutioncomponentconfiguration table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Solution Component Configuration Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/solutioncomponentconfigurations<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/solutioncomponentconfigurations(*solutioncomponentconfigurationid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref href="Microsoft.Dynamics.CRM.IsValidStateTransition?text=IsValidStateTransition Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/solutioncomponentconfigurations(*solutioncomponentconfigurationid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/solutioncomponentconfigurations<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH [*org URI*]/api/data/v9.0/solutioncomponentconfigurations(*solutioncomponentconfigurationid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/solutioncomponentconfigurations(*solutioncomponentconfigurationid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|solutioncomponentconfigurations|
|DisplayCollectionName|Solution Component Configurations|
|DisplayName|Solution Component Configuration|
|EntitySetName|solutioncomponentconfigurations|
|IsBPFEntity|False|
|LogicalCollectionName|solutioncomponentconfigurations|
|LogicalName|solutioncomponentconfiguration|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|solutioncomponentconfigurationid|
|PrimaryNameAttribute|name|
|SchemaName|solutioncomponentconfiguration|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EntityId](#BKMK_EntityId)
- [FileFormat](#BKMK_FileFormat)
- [FileScope](#BKMK_FileScope)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [isdisplayable](#BKMK_isdisplayable)
- [IsSoftDeleteEnabled](#BKMK_IsSoftDeleteEnabled)
- [KeepActiveCustomizationAfterConversion](#BKMK_KeepActiveCustomizationAfterConversion)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [solutioncomponentconfigurationId](#BKMK_solutioncomponentconfigurationId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_EntityId"></a> EntityId

|Property|Value|
|--------|-----|
|Description|Unique identifier for Entity associated with Solution Component Configuration.|
|DisplayName|Entity|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|entityid|
|RequiredLevel|SystemRequired|
|Targets|entity|
|Type|Lookup|


### <a name="BKMK_FileFormat"></a> FileFormat

|Property|Value|
|--------|-----|
|Description||
|DisplayName|File Format|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|fileformat|
|RequiredLevel|None|
|Type|Picklist|

#### FileFormat Choices/Options

|Value|Label|
|-----|-----|
|0|xml|
|1|json|



### <a name="BKMK_FileScope"></a> FileScope

|Property|Value|
|--------|-----|
|Description||
|DisplayName|File Scope|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|filescope|
|RequiredLevel|None|
|Type|Picklist|

#### FileScope Choices/Options

|Value|Label|
|-----|-----|
|0|None|
|1|Individual|
|2|Global|



### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Added by**: Basic Solution Solution

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


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_isdisplayable"></a> isdisplayable

|Property|Value|
|--------|-----|
|Description|Boolean that indicates if the component has user interface enabled.|
|DisplayName|Displayable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isdisplayable|
|RequiredLevel|None|
|Type|Boolean|

#### isdisplayable Choices/Options

|Value|Label|
|-----|-----|


### <a name="BKMK_IsSoftDeleteEnabled"></a> IsSoftDeleteEnabled

|Property|Value|
|--------|-----|
|Description||
|DisplayName|IsSoftDeleteEnabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|issoftdeleteenabled|
|RequiredLevel|None|
|Type|Boolean|

#### IsSoftDeleteEnabled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_KeepActiveCustomizationAfterConversion"></a> KeepActiveCustomizationAfterConversion

|Property|Value|
|--------|-----|
|Description|Boolean that indicates if the component should retain its unmanaged customization after conversion.|
|DisplayName|Keep Active Customization After Conversion|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|keepactivecustomizationafterconversion|
|RequiredLevel|None|
|Type|Boolean|

#### KeepActiveCustomizationAfterConversion Choices/Options

|Value|Label|
|-----|-----|


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


### <a name="BKMK_solutioncomponentconfigurationId"></a> solutioncomponentconfigurationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Solution Component Configuration|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|solutioncomponentconfigurationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Solution Component Configuration|
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
|Description|Reason for the status of the Solution Component Configuration|
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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [EntityIdName](#BKMK_EntityIdName)
- [IsManaged](#BKMK_IsManaged)
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
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Row id unique|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ComponentState"></a> ComponentState

**Added by**: Basic Solution Solution

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

|Value|Label|
|-----|-----|
|0|Published|
|1|Unpublished|
|2|Deleted|
|3|Deleted Unpublished|



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


### <a name="BKMK_EntityIdName"></a> EntityIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityidname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsManaged"></a> IsManaged

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|Indicates whether the solution component is part of a managed solution.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|
|-----|-----|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



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


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_SolutionId"></a> SolutionId

**Added by**: Basic Solution Solution

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

**Added by**: Basic Solution Solution

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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version Number|
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

- [solutioncomponentconfiguration_SyncErrors](#BKMK_solutioncomponentconfiguration_SyncErrors)
- [solutioncomponentconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord)
- [solutioncomponentconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentconfiguration_DuplicateBaseRecord)
- [solutioncomponentconfiguration_AsyncOperations](#BKMK_solutioncomponentconfiguration_AsyncOperations)
- [solutioncomponentconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentconfiguration_MailboxTrackingFolders)
- [solutioncomponentconfiguration_ProcessSession](#BKMK_solutioncomponentconfiguration_ProcessSession)
- [solutioncomponentconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentconfiguration_BulkDeleteFailures)
- [solutioncomponentconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses)
- [solutioncomponentconfig_solutioncomponentattrconfig](#BKMK_solutioncomponentconfig_solutioncomponentattrconfig)


### <a name="BKMK_solutioncomponentconfiguration_SyncErrors"></a> solutioncomponentconfiguration_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [solutioncomponentconfiguration_SyncErrors](syncerror.md#BKMK_solutioncomponentconfiguration_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentconfiguration_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord"></a> solutioncomponentconfiguration_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [solutioncomponentconfiguration_DuplicateMatchingRecord](duplicaterecord.md#BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentconfiguration_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentconfiguration_DuplicateBaseRecord"></a> solutioncomponentconfiguration_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [solutioncomponentconfiguration_DuplicateBaseRecord](duplicaterecord.md#BKMK_solutioncomponentconfiguration_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentconfiguration_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentconfiguration_AsyncOperations"></a> solutioncomponentconfiguration_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [solutioncomponentconfiguration_AsyncOperations](asyncoperation.md#BKMK_solutioncomponentconfiguration_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentconfiguration_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentconfiguration_MailboxTrackingFolders"></a> solutioncomponentconfiguration_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [solutioncomponentconfiguration_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_solutioncomponentconfiguration_MailboxTrackingFolders) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentconfiguration_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentconfiguration_ProcessSession"></a> solutioncomponentconfiguration_ProcessSession

**Added by**: System Solution Solution

Same as processsession table [solutioncomponentconfiguration_ProcessSession](processsession.md#BKMK_solutioncomponentconfiguration_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentconfiguration_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentconfiguration_BulkDeleteFailures"></a> solutioncomponentconfiguration_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [solutioncomponentconfiguration_BulkDeleteFailures](bulkdeletefailure.md#BKMK_solutioncomponentconfiguration_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentconfiguration_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentconfiguration_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [solutioncomponentconfiguration_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentconfiguration_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentconfig_solutioncomponentattrconfig"></a> solutioncomponentconfig_solutioncomponentattrconfig

Same as solutioncomponentattributeconfiguration table [solutioncomponentconfig_solutioncomponentattrconfig](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentconfig_solutioncomponentattrconfig) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentattributeconfiguration|
|ReferencingAttribute|solutioncomponentconfigurationid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentconfig_solutioncomponentattrconfig|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_solutioncomponentconfiguration_createdby](#BKMK_lk_solutioncomponentconfiguration_createdby)
- [lk_solutioncomponentconfiguration_createdonbehalfby](#BKMK_lk_solutioncomponentconfiguration_createdonbehalfby)
- [lk_solutioncomponentconfiguration_modifiedby](#BKMK_lk_solutioncomponentconfiguration_modifiedby)
- [lk_solutioncomponentconfiguration_modifiedonbehalfby](#BKMK_lk_solutioncomponentconfiguration_modifiedonbehalfby)
- [organization_solutioncomponentconfiguration](#BKMK_organization_solutioncomponentconfiguration)
- [entity_solutioncomponentconfiguration](#BKMK_entity_solutioncomponentconfiguration)


### <a name="BKMK_lk_solutioncomponentconfiguration_createdby"></a> lk_solutioncomponentconfiguration_createdby

**Added by**: System Solution Solution

See systemuser Table [lk_solutioncomponentconfiguration_createdby](systemuser.md#BKMK_lk_solutioncomponentconfiguration_createdby) One-To-Many relationship.

### <a name="BKMK_lk_solutioncomponentconfiguration_createdonbehalfby"></a> lk_solutioncomponentconfiguration_createdonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_solutioncomponentconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_solutioncomponentconfiguration_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_solutioncomponentconfiguration_modifiedby"></a> lk_solutioncomponentconfiguration_modifiedby

**Added by**: System Solution Solution

See systemuser Table [lk_solutioncomponentconfiguration_modifiedby](systemuser.md#BKMK_lk_solutioncomponentconfiguration_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_solutioncomponentconfiguration_modifiedonbehalfby"></a> lk_solutioncomponentconfiguration_modifiedonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_solutioncomponentconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_solutioncomponentconfiguration_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_solutioncomponentconfiguration"></a> organization_solutioncomponentconfiguration

**Added by**: System Solution Solution

See organization Table [organization_solutioncomponentconfiguration](organization.md#BKMK_organization_solutioncomponentconfiguration) One-To-Many relationship.

### <a name="BKMK_entity_solutioncomponentconfiguration"></a> entity_solutioncomponentconfiguration

**Added by**: System Solution Solution

See entity Table [entity_solutioncomponentconfiguration](entity.md#BKMK_entity_solutioncomponentconfiguration) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.solutioncomponentconfiguration?text=solutioncomponentconfiguration EntityType" />