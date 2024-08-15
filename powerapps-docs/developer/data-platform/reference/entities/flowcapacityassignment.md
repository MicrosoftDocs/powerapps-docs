---
title: "flowcapacityassignment table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the flowcapacityassignment table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# flowcapacityassignment table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Capacity assignment for usage in Power Automate

**Added by**: Power Automate Core Components Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /flowcapacityassignments(*flowcapacityassignmentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST /flowcapacityassignments<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /flowcapacityassignments(*flowcapacityassignmentid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET /flowcapacityassignments(*flowcapacityassignmentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /flowcapacityassignments<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH /flowcapacityassignments(*flowcapacityassignmentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /flowcapacityassignments(*flowcapacityassignmentid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|flowcapacityassignments|
|DisplayCollectionName|Flow Capacity Assignments|
|DisplayName|Flow Capacity Assignment|
|EntitySetName|flowcapacityassignments|
|IsBPFEntity|False|
|LogicalCollectionName|flowcapacityassignments|
|LogicalName|flowcapacityassignment|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|flowcapacityassignmentid|
|PrimaryNameAttribute|name|
|SchemaName|flowcapacityassignment|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AllocationOrigin](#BKMK_AllocationOrigin)
- [AllowAutoAllocation](#BKMK_AllowAutoAllocation)
- [CapacityOverage](#BKMK_CapacityOverage)
- [CapacitySource](#BKMK_CapacitySource)
- [CapacityType](#BKMK_CapacityType)
- [Count](#BKMK_Count)
- [flowcapacityassignmentId](#BKMK_flowcapacityassignmentId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [regarding](#BKMK_regarding)
- [regardingIdType](#BKMK_regardingIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_AllocationOrigin"></a> AllocationOrigin

|Property|Value|
|--------|-----|
|Description|Origin of the capacity assigned to a target entity.|
|DisplayName|Allocation Origin|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|allocationorigin|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### AllocationOrigin Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|User|Capacity was assigned by a user.|
|1|System|Capacity was assigned by the system.|



### <a name="BKMK_AllowAutoAllocation"></a> AllowAutoAllocation

|Property|Value|
|--------|-----|
|Description|Indicates whether the capacity auto-allocation feature is allowed for the target record. Default value is Yes.|
|DisplayName|Allow capacity auto-allocation for the target record.|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|allowautoallocation|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### AllowAutoAllocation Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_CapacityOverage"></a> CapacityOverage

|Property|Value|
|--------|-----|
|Description|Number of missing add-ons to be compliant|
|DisplayName|CapacityOverage|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|capacityoverage|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_CapacitySource"></a> CapacitySource

|Property|Value|
|--------|-----|
|Description|Source of the capacity assigned to a target entity.|
|DisplayName|CapacitySource|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|capacitysource|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### CapacitySource Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|AddOn|Capacity comes from the add-on.|
|1|ViralAdoption|Capacity comes from the viral adoption.|
|2|UserTrial|Capacity comes from a user trial.|
|3|FailOpen|Capacity comes from the fail open strategy.|



### <a name="BKMK_CapacityType"></a> CapacityType

|Property|Value|
|--------|-----|
|Description|Type of the capacity assigned to a target entity|
|DisplayName|CapacityType|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|capacitytype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### CapacityType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|PowerAutomateHostedRpa|Power Automate Hosted RPA add-on|
|1|PowerAutomatePerProcess|Power Automate Per Process add-on|



### <a name="BKMK_Count"></a> Count

|Property|Value|
|--------|-----|
|Description|Number of units assigned|
|DisplayName|Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|count|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_flowcapacityassignmentId"></a> flowcapacityassignmentId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Flow Capacity Assignment|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|flowcapacityassignmentid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description||
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


### <a name="BKMK_OwnerId"></a> OwnerId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_regarding"></a> regarding

|Property|Value|
|--------|-----|
|Description|The target of the capacity assignment|
|DisplayName|Assignment target|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|regarding|
|RequiredLevel|SystemRequired|
|Targets|flowmachine,flowmachinegroup,workflow|
|Type|Lookup|


### <a name="BKMK_regardingIdType"></a> regardingIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingidtype|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Flow Capacity Assignment|
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
|Description|Reason for the status of the Flow Capacity Assignment|
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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [regardingName](#BKMK_regardingName)
- [regardingYomiName](#BKMK_regardingYomiName)
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Yomi name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunitname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_regardingName"></a> regardingName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingname|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_regardingYomiName"></a> regardingYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingyominame|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


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

- [flowcapacityassignment_SyncErrors](#BKMK_flowcapacityassignment_SyncErrors)
- [flowcapacityassignment_AsyncOperations](#BKMK_flowcapacityassignment_AsyncOperations)
- [flowcapacityassignment_MailboxTrackingFolders](#BKMK_flowcapacityassignment_MailboxTrackingFolders)
- [flowcapacityassignment_ProcessSession](#BKMK_flowcapacityassignment_ProcessSession)
- [flowcapacityassignment_BulkDeleteFailures](#BKMK_flowcapacityassignment_BulkDeleteFailures)
- [flowcapacityassignment_PrincipalObjectAttributeAccesses](#BKMK_flowcapacityassignment_PrincipalObjectAttributeAccesses)


### <a name="BKMK_flowcapacityassignment_SyncErrors"></a> flowcapacityassignment_SyncErrors

**Added by**: System Solution Solution

Same as the [flowcapacityassignment_SyncErrors](syncerror.md#BKMK_flowcapacityassignment_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|flowcapacityassignment_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_flowcapacityassignment_AsyncOperations"></a> flowcapacityassignment_AsyncOperations

**Added by**: System Solution Solution

Same as the [flowcapacityassignment_AsyncOperations](asyncoperation.md#BKMK_flowcapacityassignment_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|flowcapacityassignment_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_flowcapacityassignment_MailboxTrackingFolders"></a> flowcapacityassignment_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [flowcapacityassignment_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_flowcapacityassignment_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|flowcapacityassignment_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_flowcapacityassignment_ProcessSession"></a> flowcapacityassignment_ProcessSession

**Added by**: System Solution Solution

Same as the [flowcapacityassignment_ProcessSession](processsession.md#BKMK_flowcapacityassignment_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|flowcapacityassignment_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_flowcapacityassignment_BulkDeleteFailures"></a> flowcapacityassignment_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [flowcapacityassignment_BulkDeleteFailures](bulkdeletefailure.md#BKMK_flowcapacityassignment_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|flowcapacityassignment_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_flowcapacityassignment_PrincipalObjectAttributeAccesses"></a> flowcapacityassignment_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [flowcapacityassignment_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_flowcapacityassignment_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|flowcapacityassignment_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_flowcapacityassignment_createdby](#BKMK_lk_flowcapacityassignment_createdby)
- [lk_flowcapacityassignment_createdonbehalfby](#BKMK_lk_flowcapacityassignment_createdonbehalfby)
- [lk_flowcapacityassignment_modifiedby](#BKMK_lk_flowcapacityassignment_modifiedby)
- [lk_flowcapacityassignment_modifiedonbehalfby](#BKMK_lk_flowcapacityassignment_modifiedonbehalfby)
- [user_flowcapacityassignment](#BKMK_user_flowcapacityassignment)
- [team_flowcapacityassignment](#BKMK_team_flowcapacityassignment)
- [business_unit_flowcapacityassignment](#BKMK_business_unit_flowcapacityassignment)
- [flowcapacityassignment_flowmachine](#BKMK_flowcapacityassignment_flowmachine)
- [flowcapacityassignment_flowmachinegroup](#BKMK_flowcapacityassignment_flowmachinegroup)
- [flowcapacityassignment_workflow](#BKMK_flowcapacityassignment_workflow)


### <a name="BKMK_lk_flowcapacityassignment_createdby"></a> lk_flowcapacityassignment_createdby

**Added by**: System Solution Solution

See the [lk_flowcapacityassignment_createdby](systemuser.md#BKMK_lk_flowcapacityassignment_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_flowcapacityassignment_createdonbehalfby"></a> lk_flowcapacityassignment_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_flowcapacityassignment_createdonbehalfby](systemuser.md#BKMK_lk_flowcapacityassignment_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_flowcapacityassignment_modifiedby"></a> lk_flowcapacityassignment_modifiedby

**Added by**: System Solution Solution

See the [lk_flowcapacityassignment_modifiedby](systemuser.md#BKMK_lk_flowcapacityassignment_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_flowcapacityassignment_modifiedonbehalfby"></a> lk_flowcapacityassignment_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_flowcapacityassignment_modifiedonbehalfby](systemuser.md#BKMK_lk_flowcapacityassignment_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_flowcapacityassignment"></a> user_flowcapacityassignment

**Added by**: System Solution Solution

See the [user_flowcapacityassignment](systemuser.md#BKMK_user_flowcapacityassignment) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_flowcapacityassignment"></a> team_flowcapacityassignment

**Added by**: System Solution Solution

See the [team_flowcapacityassignment](team.md#BKMK_team_flowcapacityassignment) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_flowcapacityassignment"></a> business_unit_flowcapacityassignment

**Added by**: System Solution Solution

See the [business_unit_flowcapacityassignment](businessunit.md#BKMK_business_unit_flowcapacityassignment) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_flowcapacityassignment_flowmachine"></a> flowcapacityassignment_flowmachine

See the [flowcapacityassignment_flowmachine](flowmachine.md#BKMK_flowcapacityassignment_flowmachine) one-to-many relationship for the [flowmachine](flowmachine.md) table/entity.

### <a name="BKMK_flowcapacityassignment_flowmachinegroup"></a> flowcapacityassignment_flowmachinegroup

See the [flowcapacityassignment_flowmachinegroup](flowmachinegroup.md#BKMK_flowcapacityassignment_flowmachinegroup) one-to-many relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

### <a name="BKMK_flowcapacityassignment_workflow"></a> flowcapacityassignment_workflow

**Added by**: System Solution Solution

See the [flowcapacityassignment_workflow](workflow.md#BKMK_flowcapacityassignment_workflow) one-to-many relationship for the [workflow](workflow.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.flowcapacityassignment?text=flowcapacityassignment EntityType" />