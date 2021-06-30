---
title: "solutioncomponentrelationshipconfiguration table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the solutioncomponentrelationshipconfiguration table/entity."
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

# solutioncomponentrelationshipconfiguration table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Solution Component Configuration Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/solutioncomponentrelationshipconfigurations<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/solutioncomponentrelationshipconfigurations(*solutioncomponentrelationshipconfigurationid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref href="Microsoft.Dynamics.CRM.IsValidStateTransition?text=IsValidStateTransition Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/solutioncomponentrelationshipconfigurations(*solutioncomponentrelationshipconfigurationid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/solutioncomponentrelationshipconfigurations<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH [*org URI*]/api/data/v9.0/solutioncomponentrelationshipconfigurations(*solutioncomponentrelationshipconfigurationid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/solutioncomponentrelationshipconfigurations(*solutioncomponentrelationshipconfigurationid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|solutioncomponentrelationshipconfigurations|
|DisplayCollectionName|Solution Component Relationship Configurations|
|DisplayName|Solution Component Relationship Configuration|
|EntitySetName|solutioncomponentrelationshipconfigurations|
|IsBPFEntity|False|
|LogicalCollectionName|solutioncomponentrelationshipconfigurations|
|LogicalName|solutioncomponentrelationshipconfiguration|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|solutioncomponentrelationshipconfigurationid|
|PrimaryNameAttribute|name|
|SchemaName|solutioncomponentrelationshipconfiguration|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AddRelatedComponents](#BKMK_AddRelatedComponents)
- [EntityRelationshipId](#BKMK_EntityRelationshipId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PrimaryEntityDependencyType](#BKMK_PrimaryEntityDependencyType)
- [SecondaryEntityDependencyType](#BKMK_SecondaryEntityDependencyType)
- [solutioncomponentrelationshipconfigurationId](#BKMK_solutioncomponentrelationshipconfigurationId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_AddRelatedComponents"></a> AddRelatedComponents

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Add Related Components|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|addrelatedcomponents|
|RequiredLevel|None|
|Type|Boolean|

#### AddRelatedComponents Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_EntityRelationshipId"></a> EntityRelationshipId

|Property|Value|
|--------|-----|
|Description|Unique identifier for Entity Relationship associated with Solution Component Relationship Configuration.|
|DisplayName|Entity Relationship|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|entityrelationshipid|
|RequiredLevel|SystemRequired|
|Targets|entityrelationship|
|Type|Lookup|


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


### <a name="BKMK_PrimaryEntityDependencyType"></a> PrimaryEntityDependencyType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|PrimaryEntityDependencyType|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|primaryentitydependencytype|
|RequiredLevel|None|
|Type|Picklist|

#### PrimaryEntityDependencyType Choices/Options

|Value|Label|
|-----|-----|
|0|Hard Dependency|
|1|Soft Dependency|



### <a name="BKMK_SecondaryEntityDependencyType"></a> SecondaryEntityDependencyType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|SecondaryEntityDependencyType|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|secondaryentitydependencytype|
|RequiredLevel|None|
|Type|Picklist|

#### SecondaryEntityDependencyType Choices/Options

|Value|Label|
|-----|-----|
|0|Hard Dependency|
|1|Soft Dependency|



### <a name="BKMK_solutioncomponentrelationshipconfigurationId"></a> solutioncomponentrelationshipconfigurationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Solution Component Relationship Configuration|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|solutioncomponentrelationshipconfigurationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Solution Component Relationship Configuration|
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
|Description|Reason for the status of the Solution Component Relationship Configuration|
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
- [EntityRelationshipIdName](#BKMK_EntityRelationshipIdName)
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


### <a name="BKMK_EntityRelationshipIdName"></a> EntityRelationshipIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityrelationshipidname|
|MaxLength|100|
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

- [solutioncomponentrelationshipconfiguration_SyncErrors](#BKMK_solutioncomponentrelationshipconfiguration_SyncErrors)
- [solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord)
- [solutioncomponentrelationshipconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord)
- [solutioncomponentrelationshipconfiguration_AsyncOperations](#BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations)
- [solutioncomponentrelationshipconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders)
- [solutioncomponentrelationshipconfiguration_ProcessSession](#BKMK_solutioncomponentrelationshipconfiguration_ProcessSession)
- [solutioncomponentrelationshipconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures)
- [solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses)


### <a name="BKMK_solutioncomponentrelationshipconfiguration_SyncErrors"></a> solutioncomponentrelationshipconfiguration_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [solutioncomponentrelationshipconfiguration_SyncErrors](syncerror.md#BKMK_solutioncomponentrelationshipconfiguration_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentrelationshipconfiguration_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord"></a> solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord](duplicaterecord.md#BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord"></a> solutioncomponentrelationshipconfiguration_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [solutioncomponentrelationshipconfiguration_DuplicateBaseRecord](duplicaterecord.md#BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentrelationshipconfiguration_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations"></a> solutioncomponentrelationshipconfiguration_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [solutioncomponentrelationshipconfiguration_AsyncOperations](asyncoperation.md#BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentrelationshipconfiguration_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders"></a> solutioncomponentrelationshipconfiguration_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [solutioncomponentrelationshipconfiguration_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentrelationshipconfiguration_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentrelationshipconfiguration_ProcessSession"></a> solutioncomponentrelationshipconfiguration_ProcessSession

**Added by**: System Solution Solution

Same as processsession table [solutioncomponentrelationshipconfiguration_ProcessSession](processsession.md#BKMK_solutioncomponentrelationshipconfiguration_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentrelationshipconfiguration_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures"></a> solutioncomponentrelationshipconfiguration_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [solutioncomponentrelationshipconfiguration_BulkDeleteFailures](bulkdeletefailure.md#BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentrelationshipconfiguration_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_solutioncomponentrelationshipconfiguration_createdby](#BKMK_lk_solutioncomponentrelationshipconfiguration_createdby)
- [lk_solutioncomponentrelationshipconfiguration_createdonbehalfby](#BKMK_lk_solutioncomponentrelationshipconfiguration_createdonbehalfby)
- [lk_solutioncomponentrelationshipconfiguration_modifiedby](#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedby)
- [lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby](#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby)
- [organization_solutioncomponentrelationshipconfiguration](#BKMK_organization_solutioncomponentrelationshipconfiguration)
- [entityrelationship_config](#BKMK_entityrelationship_config)


### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_createdby"></a> lk_solutioncomponentrelationshipconfiguration_createdby

**Added by**: System Solution Solution

See systemuser Table [lk_solutioncomponentrelationshipconfiguration_createdby](systemuser.md#BKMK_lk_solutioncomponentrelationshipconfiguration_createdby) One-To-Many relationship.

### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_createdonbehalfby"></a> lk_solutioncomponentrelationshipconfiguration_createdonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_solutioncomponentrelationshipconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_solutioncomponentrelationshipconfiguration_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedby"></a> lk_solutioncomponentrelationshipconfiguration_modifiedby

**Added by**: System Solution Solution

See systemuser Table [lk_solutioncomponentrelationshipconfiguration_modifiedby](systemuser.md#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby"></a> lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_solutioncomponentrelationshipconfiguration"></a> organization_solutioncomponentrelationshipconfiguration

**Added by**: System Solution Solution

See organization Table [organization_solutioncomponentrelationshipconfiguration](organization.md#BKMK_organization_solutioncomponentrelationshipconfiguration) One-To-Many relationship.

### <a name="BKMK_entityrelationship_config"></a> entityrelationship_config

**Added by**: System Solution Solution

See entityrelationship Table [entityrelationship_config](entityrelationship.md#BKMK_entityrelationship_config) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.solutioncomponentrelationshipconfiguration?text=solutioncomponentrelationshipconfiguration EntityType" />