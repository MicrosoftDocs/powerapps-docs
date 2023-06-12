---
title: "datalakefolder table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the datalakefolder table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# datalakefolder table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

A folder is a place to store data in Azure Data Lake.

**Added by**: Data lake workspaces Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /datalakefolders(*datalakefolderid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST /datalakefolders<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /datalakefolders(*datalakefolderid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET /datalakefolders(*datalakefolderid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /datalakefolders<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH /datalakefolders(*datalakefolderid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /datalakefolders(*datalakefolderid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|datalakefolders|
|DisplayCollectionName|Data Lake Folders|
|DisplayName|Data Lake Folder|
|EntitySetName|datalakefolders|
|IsBPFEntity|False|
|LogicalCollectionName|datalakefolders|
|LogicalName|datalakefolder|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|datalakefolderid|
|PrimaryNameAttribute|name|
|SchemaName|datalakefolder|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccessType](#BKMK_AccessType)
- [CDMPath](#BKMK_CDMPath)
- [containerendpoint](#BKMK_containerendpoint)
- [ContributorSecurityGroupId](#BKMK_ContributorSecurityGroupId)
- [datalakefolder_UniqueName](#BKMK_datalakefolder_UniqueName)
- [datalakefolderId](#BKMK_datalakefolderId)
- [deltaLakePath](#BKMK_deltaLakePath)
- [extendedproperties](#BKMK_extendedproperties)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [iscustomercapacity](#BKMK_iscustomercapacity)
- [IsCustomizable](#BKMK_IsCustomizable)
- [isdeepcopyenabled](#BKMK_isdeepcopyenabled)
- [IsExternalLake](#BKMK_IsExternalLake)
- [IsExternalLakeReadOnly](#BKMK_IsExternalLakeReadOnly)
- [isprivate](#BKMK_isprivate)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [owningappid](#BKMK_owningappid)
- [parentfolderid](#BKMK_parentfolderid)
- [path](#BKMK_path)
- [ReaderSecurityGroupId](#BKMK_ReaderSecurityGroupId)
- [ResourceGroup](#BKMK_ResourceGroup)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [Subscription](#BKMK_Subscription)
- [SynchronizeSchemaToDataverse](#BKMK_SynchronizeSchemaToDataverse)
- [SynchronizeSchemaToSynapseDb](#BKMK_SynchronizeSchemaToSynapseDb)
- [Tenant](#BKMK_Tenant)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_AccessType"></a> AccessType

|Property|Value|
|--------|-----|
|Description|Azure Data Lake Access Type.|
|DisplayName|Access Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|accesstype|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CDMPath"></a> CDMPath

|Property|Value|
|--------|-----|
|Description|Path to the CDM file.|
|DisplayName|CDM Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|cdmpath|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_containerendpoint"></a> containerendpoint

|Property|Value|
|--------|-----|
|Description|Azure Data Lake container endpoint for this folder.|
|DisplayName|Container Endpoint|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|containerendpoint|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ContributorSecurityGroupId"></a> ContributorSecurityGroupId

|Property|Value|
|--------|-----|
|Description|The security group for contributor access.|
|DisplayName|Contributor Security Group Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|contributorsecuritygroupid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_datalakefolder_UniqueName"></a> datalakefolder_UniqueName

|Property|Value|
|--------|-----|
|Description|Unique Name for the entity.|
|DisplayName|Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|datalakefolder_uniquename|
|MaxLength|128|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_datalakefolderId"></a> datalakefolderId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Data Lake Folder|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|datalakefolderid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_deltaLakePath"></a> deltaLakePath

|Property|Value|
|--------|-----|
|Description|Sub folder path to delta lake.|
|DisplayName|deltaLakePath|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|deltaLakePath|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_extendedproperties"></a> extendedproperties

|Property|Value|
|--------|-----|
|Description|Extended Properties associated with this folder.|
|DisplayName|Extended Properties|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|extendedproperties|
|MaxLength|800|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_iscustomercapacity"></a> iscustomercapacity

|Property|Value|
|--------|-----|
|Description|Indicates if folder data storage uses customer capacity.|
|DisplayName|Is Customer Capacity|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|iscustomercapacity|
|RequiredLevel|None|
|Type|Boolean|

#### iscustomercapacity Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



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


### <a name="BKMK_isdeepcopyenabled"></a> isdeepcopyenabled

|Property|Value|
|--------|-----|
|Description|Indicates if deep copy is enabled for folder.|
|DisplayName|Is Deep Copy Enabled|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isdeepcopyenabled|
|RequiredLevel|None|
|Type|Boolean|

#### isdeepcopyenabled Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_IsExternalLake"></a> IsExternalLake

|Property|Value|
|--------|-----|
|Description|Indicates whether lake is managed or external.|
|DisplayName|Is External Lake|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|isexternallake|
|RequiredLevel|None|
|Type|Boolean|

#### IsExternalLake Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_IsExternalLakeReadOnly"></a> IsExternalLakeReadOnly

|Property|Value|
|--------|-----|
|Description|Indicates whether external lake is read only.|
|DisplayName|Is External Lake Read Only|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isexternallakereadonly|
|RequiredLevel|None|
|Type|Boolean|

#### IsExternalLakeReadOnly Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_isprivate"></a> isprivate

|Property|Value|
|--------|-----|
|Description|Indicates if folder data and metadata are visible to all applications, or only visible to the folder owner and applications with explicit permissions to the folder.|
|DisplayName|Is Private|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isprivate|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### isprivate Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_owningappid"></a> owningappid

|Property|Value|
|--------|-----|
|Description|The app id which owns this folder. The owning app id has full control i.e. read, write and execute permissions on the ADLS folder.|
|DisplayName|Owning App Id|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|owningappid|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_parentfolderid"></a> parentfolderid

|Property|Value|
|--------|-----|
|Description|Unique identifier of the parent folder for this folder.|
|DisplayName|Parent Folder Id|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|parentfolderid|
|RequiredLevel|None|
|Targets|datalakefolder|
|Type|Lookup|


### <a name="BKMK_path"></a> path

|Property|Value|
|--------|-----|
|Description|Folder path in the Azure Data Lake container.|
|DisplayName|Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|path|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ReaderSecurityGroupId"></a> ReaderSecurityGroupId

|Property|Value|
|--------|-----|
|Description|The security group for reader access.|
|DisplayName|Reader Security Group Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|readersecuritygroupid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ResourceGroup"></a> ResourceGroup

|Property|Value|
|--------|-----|
|Description|Azure resource group of the storage account.|
|DisplayName|ResourceGroup|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|resourcegroup|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Data Lake Folder|
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
|Description|Reason for the status of the Data Lake Folder|
|DisplayName|Status Reason|
|IsValidForCreate|False|
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



### <a name="BKMK_Subscription"></a> Subscription

|Property|Value|
|--------|-----|
|Description|Azure subscription of the storage account.|
|DisplayName|Subscription|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|subscription|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SynchronizeSchemaToDataverse"></a> SynchronizeSchemaToDataverse

|Property|Value|
|--------|-----|
|Description|Enable schema synchronization to Dataverse.|
|DisplayName|Synchronize Schema To Dataverse|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|synchronizeschematodataverse|
|RequiredLevel|None|
|Type|Boolean|

#### SynchronizeSchemaToDataverse Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_SynchronizeSchemaToSynapseDb"></a> SynchronizeSchemaToSynapseDb

|Property|Value|
|--------|-----|
|Description|Enable schema synchronization to Synapse database.|
|DisplayName|Synchronize Schema To Synapse Db|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|synchronizeschematosynapsedb|
|RequiredLevel|None|
|Type|Boolean|

#### SynchronizeSchemaToSynapseDb Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_Tenant"></a> Tenant

|Property|Value|
|--------|-----|
|Description|Azure tenant of the storage account.|
|DisplayName|Tenant|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|tenant|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [parentfolderidName](#BKMK_parentfolderidName)
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

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



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

|Value|Label|Description|
|-----|-----|--------|
|1|Managed||
|0|Unmanaged||

**DefaultValue**: 0



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


### <a name="BKMK_parentfolderidName"></a> parentfolderidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentfolderidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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

- [datalakefolder_SyncErrors](#BKMK_datalakefolder_SyncErrors)
- [datalakefolder_DuplicateMatchingRecord](#BKMK_datalakefolder_DuplicateMatchingRecord)
- [datalakefolder_DuplicateBaseRecord](#BKMK_datalakefolder_DuplicateBaseRecord)
- [datalakefolder_AsyncOperations](#BKMK_datalakefolder_AsyncOperations)
- [datalakefolder_MailboxTrackingFolders](#BKMK_datalakefolder_MailboxTrackingFolders)
- [datalakefolder_ProcessSession](#BKMK_datalakefolder_ProcessSession)
- [datalakefolder_BulkDeleteFailures](#BKMK_datalakefolder_BulkDeleteFailures)
- [datalakefolder_PrincipalObjectAttributeAccesses](#BKMK_datalakefolder_PrincipalObjectAttributeAccesses)
- [datalakefolder_datalakefolderpermission](#BKMK_datalakefolder_datalakefolderpermission)
- [datalakefolder_datalakesubfolder](#BKMK_datalakefolder_datalakesubfolder)
- [synapsedatabases](#BKMK_synapsedatabases)
- [synapselinkexternaltablestates](#BKMK_synapselinkexternaltablestates)
- [synapselinkprofiles](#BKMK_synapselinkprofiles)
- [msdyn_dataflow_datalakefolder_dlfolder](#BKMK_msdyn_dataflow_datalakefolder_dlfolder)


### <a name="BKMK_datalakefolder_SyncErrors"></a> datalakefolder_SyncErrors

**Added by**: System Solution Solution

Same as the [datalakefolder_SyncErrors](syncerror.md#BKMK_datalakefolder_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|datalakefolder_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_datalakefolder_DuplicateMatchingRecord"></a> datalakefolder_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [datalakefolder_DuplicateMatchingRecord](duplicaterecord.md#BKMK_datalakefolder_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|datalakefolder_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_datalakefolder_DuplicateBaseRecord"></a> datalakefolder_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [datalakefolder_DuplicateBaseRecord](duplicaterecord.md#BKMK_datalakefolder_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|datalakefolder_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_datalakefolder_AsyncOperations"></a> datalakefolder_AsyncOperations

**Added by**: System Solution Solution

Same as the [datalakefolder_AsyncOperations](asyncoperation.md#BKMK_datalakefolder_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|datalakefolder_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_datalakefolder_MailboxTrackingFolders"></a> datalakefolder_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [datalakefolder_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_datalakefolder_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|datalakefolder_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_datalakefolder_ProcessSession"></a> datalakefolder_ProcessSession

**Added by**: System Solution Solution

Same as the [datalakefolder_ProcessSession](processsession.md#BKMK_datalakefolder_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|datalakefolder_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_datalakefolder_BulkDeleteFailures"></a> datalakefolder_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [datalakefolder_BulkDeleteFailures](bulkdeletefailure.md#BKMK_datalakefolder_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|datalakefolder_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_datalakefolder_PrincipalObjectAttributeAccesses"></a> datalakefolder_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [datalakefolder_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_datalakefolder_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|datalakefolder_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_datalakefolder_datalakefolderpermission"></a> datalakefolder_datalakefolderpermission

Same as the [datalakefolder_datalakefolderpermission](datalakefolderpermission.md#BKMK_datalakefolder_datalakefolderpermission) many-to-one relationship for the [datalakefolderpermission](datalakefolderpermission.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolderpermission|
|ReferencingAttribute|folderid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|datalakefolder_datalakefolderpermission|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_datalakefolder_datalakesubfolder"></a> datalakefolder_datalakesubfolder

Same as the [datalakefolder_datalakesubfolder](datalakefolder.md#BKMK_datalakefolder_datalakesubfolder) many-to-one relationship for the [datalakefolder](datalakefolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolder|
|ReferencingAttribute|parentfolderid|
|IsHierarchical|True|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|datalakefolder_datalakesubfolder|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_synapsedatabases"></a> synapsedatabases

Same as the [synapsedatabases](synapsedatabase.md#BKMK_synapsedatabases) many-to-one relationship for the [synapsedatabase](synapsedatabase.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|synapsedatabase|
|ReferencingAttribute|datalakefolder|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|synapsedatabases|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_synapselinkexternaltablestates"></a> synapselinkexternaltablestates

**Added by**: Synapse Link Solution

Same as the [synapselinkexternaltablestates](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestates) many-to-one relationship for the [synapselinkexternaltablestate](synapselinkexternaltablestate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|synapselinkexternaltablestate|
|ReferencingAttribute|datalakefolder|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|synapselinkexternaltablestates|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_synapselinkprofiles"></a> synapselinkprofiles

**Added by**: Synapse Link Solution

Same as the [synapselinkprofiles](synapselinkprofile.md#BKMK_synapselinkprofiles) many-to-one relationship for the [synapselinkprofile](synapselinkprofile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|synapselinkprofile|
|ReferencingAttribute|datalakefolder|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|synapselinkprofiles|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_dataflow_datalakefolder_dlfolder"></a> msdyn_dataflow_datalakefolder_dlfolder

**Added by**: Insights App Platform Solution

Same as the [msdyn_dataflow_datalakefolder_dlfolder](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_dlfolder) many-to-one relationship for the [msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow_datalakefolder|
|ReferencingAttribute|msdyn_datalakefolder|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_dataflow_datalakefolder_dlfolder|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_datalakefolder_createdby](#BKMK_lk_datalakefolder_createdby)
- [lk_datalakefolder_createdonbehalfby](#BKMK_lk_datalakefolder_createdonbehalfby)
- [lk_datalakefolder_modifiedby](#BKMK_lk_datalakefolder_modifiedby)
- [lk_datalakefolder_modifiedonbehalfby](#BKMK_lk_datalakefolder_modifiedonbehalfby)
- [user_datalakefolder](#BKMK_user_datalakefolder)
- [team_datalakefolder](#BKMK_team_datalakefolder)
- [business_unit_datalakefolder](#BKMK_business_unit_datalakefolder)
- [datalakefolder_datalakesubfolder](#BKMK_datalakefolder_datalakesubfolder)


### <a name="BKMK_lk_datalakefolder_createdby"></a> lk_datalakefolder_createdby

**Added by**: System Solution Solution

See the [lk_datalakefolder_createdby](systemuser.md#BKMK_lk_datalakefolder_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_datalakefolder_createdonbehalfby"></a> lk_datalakefolder_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_datalakefolder_createdonbehalfby](systemuser.md#BKMK_lk_datalakefolder_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_datalakefolder_modifiedby"></a> lk_datalakefolder_modifiedby

**Added by**: System Solution Solution

See the [lk_datalakefolder_modifiedby](systemuser.md#BKMK_lk_datalakefolder_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_datalakefolder_modifiedonbehalfby"></a> lk_datalakefolder_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_datalakefolder_modifiedonbehalfby](systemuser.md#BKMK_lk_datalakefolder_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_datalakefolder"></a> user_datalakefolder

**Added by**: System Solution Solution

See the [user_datalakefolder](systemuser.md#BKMK_user_datalakefolder) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_datalakefolder"></a> team_datalakefolder

**Added by**: System Solution Solution

See the [team_datalakefolder](team.md#BKMK_team_datalakefolder) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_datalakefolder"></a> business_unit_datalakefolder

**Added by**: System Solution Solution

See the [business_unit_datalakefolder](businessunit.md#BKMK_business_unit_datalakefolder) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_datalakefolder_datalakesubfolder"></a> datalakefolder_datalakesubfolder

See the [datalakefolder_datalakesubfolder](datalakefolder.md#BKMK_datalakefolder_datalakesubfolder) one-to-many relationship for the [datalakefolder](datalakefolder.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.datalakefolder?text=datalakefolder EntityType" />