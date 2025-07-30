---
title: "Data Lake Folder (datalakefolder) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Data Lake Folder (datalakefolder) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Data Lake Folder (datalakefolder) table/entity reference (Microsoft Dataverse)

A folder is a place to store data in Azure Data Lake.

## Messages

The following table lists the messages for the Data Lake Folder (datalakefolder) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /datalakefolders(*datalakefolderid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /datalakefolders<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /datalakefolders(*datalakefolderid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /datalakefolders(*datalakefolderid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /datalakefolders<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /datalakefolders(*datalakefolderid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /datalakefolders(*datalakefolderid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /datalakefolders(*datalakefolderid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Data Lake Folder (datalakefolder) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Data Lake Folder** |
| **DisplayCollectionName** | **Data Lake Folders** |
| **SchemaName** | `datalakefolder` |
| **CollectionSchemaName** | `datalakefolders` |
| **EntitySetName** | `datalakefolders`|
| **LogicalName** | `datalakefolder` |
| **LogicalCollectionName** | `datalakefolders` |
| **PrimaryIdAttribute** | `datalakefolderid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccessType](#BKMK_AccessType)
- [CDMPath](#BKMK_CDMPath)
- [ComplianceLakeLocation](#BKMK_ComplianceLakeLocation)
- [containerendpoint](#BKMK_containerendpoint)
- [ContributorSecurityGroupId](#BKMK_ContributorSecurityGroupId)
- [datalakefolder_UniqueName](#BKMK_datalakefolder_UniqueName)
- [datalakefolderId](#BKMK_datalakefolderId)
- [deltaLakePath](#BKMK_deltaLakePath)
- [extendedproperties](#BKMK_extendedproperties)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsComplianceLake](#BKMK_IsComplianceLake)
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
- [sharedforreadaccess](#BKMK_sharedforreadaccess)
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
|---|---|
|Description|**Azure Data Lake Access Type.**|
|DisplayName|**Access Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`accesstype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_CDMPath"></a> CDMPath

|Property|Value|
|---|---|
|Description|**Path to the CDM file.**|
|DisplayName|**CDM Path**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cdmpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ComplianceLakeLocation"></a> ComplianceLakeLocation

|Property|Value|
|---|---|
|Description|**Azure location where the compliance lake should be created.**|
|DisplayName|**Compliance Lake Location**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`compliancelakelocation`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_containerendpoint"></a> containerendpoint

|Property|Value|
|---|---|
|Description|**Azure Data Lake container endpoint for this folder.**|
|DisplayName|**Container Endpoint**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`containerendpoint`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ContributorSecurityGroupId"></a> ContributorSecurityGroupId

|Property|Value|
|---|---|
|Description|**The security group for contributor access.**|
|DisplayName|**Contributor Security Group Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contributorsecuritygroupid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_datalakefolder_UniqueName"></a> datalakefolder_UniqueName

|Property|Value|
|---|---|
|Description|**Unique Name for the entity.**|
|DisplayName|**Unique Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`datalakefolder_uniquename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_datalakefolderId"></a> datalakefolderId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Data Lake Folder**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`datalakefolderid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_deltaLakePath"></a> deltaLakePath

|Property|Value|
|---|---|
|Description|**Sub folder path to delta lake.**|
|DisplayName|**deltaLakePath**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`deltaLakePath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_extendedproperties"></a> extendedproperties

|Property|Value|
|---|---|
|Description|**Extended Properties associated with this folder.**|
|DisplayName|**Extended Properties**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`extendedproperties`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|800|

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

### <a name="BKMK_IsComplianceLake"></a> IsComplianceLake

|Property|Value|
|---|---|
|Description|**Indicates whether lake is used for compliance purposes or not.**|
|DisplayName|**Is Compliance Lake**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iscompliancelake`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`datalakefolder_iscompliancelake`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_iscustomercapacity"></a> iscustomercapacity

|Property|Value|
|---|---|
|Description|**Indicates if folder data storage uses customer capacity.**|
|DisplayName|**Is Customer Capacity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iscustomercapacity`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`datalakefolder_iscustomercapacity`|
|DefaultValue|True|
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

### <a name="BKMK_isdeepcopyenabled"></a> isdeepcopyenabled

|Property|Value|
|---|---|
|Description|**Indicates if deep copy is enabled for folder.**|
|DisplayName|**Is Deep Copy Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdeepcopyenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`datalakefolder_isdeepcopyenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsExternalLake"></a> IsExternalLake

|Property|Value|
|---|---|
|Description|**Indicates whether lake is managed or external.**|
|DisplayName|**Is External Lake**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isexternallake`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`datalakefolder_isexternallake`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsExternalLakeReadOnly"></a> IsExternalLakeReadOnly

|Property|Value|
|---|---|
|Description|**Indicates whether external lake is read only.**|
|DisplayName|**Is External Lake Read Only**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isexternallakereadonly`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`datalakefolder_isexternallakereadonly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_isprivate"></a> isprivate

|Property|Value|
|---|---|
|Description|**Indicates if folder data and metadata are visible to all applications, or only visible to the folder owner and applications with explicit permissions to the folder.**|
|DisplayName|**Is Private**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isprivate`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`datalakefolder_isprivate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
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

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Owner Id**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_owningappid"></a> owningappid

|Property|Value|
|---|---|
|Description|**The app id which owns this folder. The owning app id has full control i.e. read, write and execute permissions on the ADLS folder.**|
|DisplayName|**Owning App Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningappid`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_parentfolderid"></a> parentfolderid

|Property|Value|
|---|---|
|Description|**Unique identifier of the parent folder for this folder.**|
|DisplayName|**Parent Folder Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentfolderid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|datalakefolder|

### <a name="BKMK_path"></a> path

|Property|Value|
|---|---|
|Description|**Folder path in the Azure Data Lake container.**|
|DisplayName|**Path**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`path`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_ReaderSecurityGroupId"></a> ReaderSecurityGroupId

|Property|Value|
|---|---|
|Description|**The security group for reader access.**|
|DisplayName|**Reader Security Group Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`readersecuritygroupid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ResourceGroup"></a> ResourceGroup

|Property|Value|
|---|---|
|Description|**Azure resource group of the storage account.**|
|DisplayName|**ResourceGroup**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`resourcegroup`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_sharedforreadaccess"></a> sharedforreadaccess

|Property|Value|
|---|---|
|Description|**Indicates if folder is shared for readaccess for other FPAs.**|
|DisplayName|**Is Shared for Read Access**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sharedforreadaccess`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`datalakefolder_sharedforreadaccess`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Data Lake Folder**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`datalakefolder_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Data Lake Folder**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`datalakefolder_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_Subscription"></a> Subscription

|Property|Value|
|---|---|
|Description|**Azure subscription of the storage account.**|
|DisplayName|**Subscription**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subscription`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_SynchronizeSchemaToDataverse"></a> SynchronizeSchemaToDataverse

|Property|Value|
|---|---|
|Description|**Enable schema synchronization to Dataverse.**|
|DisplayName|**Synchronize Schema To Dataverse**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`synchronizeschematodataverse`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`datalakefolder_synchronizeschematodataverse`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SynchronizeSchemaToSynapseDb"></a> SynchronizeSchemaToSynapseDb

|Property|Value|
|---|---|
|Description|**Enable schema synchronization to Synapse database.**|
|DisplayName|**Synchronize Schema To Synapse Db**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`synchronizeschematosynapsedb`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`datalakefolder_synchronizeschematosynapsedb`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Tenant"></a> Tenant

|Property|Value|
|---|---|
|Description|**Azure tenant of the storage account.**|
|DisplayName|**Tenant**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tenant`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
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

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description|**Yomi name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier for the business unit that owns the record**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier for the team that owns the record.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

- [business_unit_datalakefolder](#BKMK_business_unit_datalakefolder)
- [datalakefolder_datalakesubfolder](#BKMK_datalakefolder_datalakesubfolder-many-to-one)
- [lk_datalakefolder_createdby](#BKMK_lk_datalakefolder_createdby)
- [lk_datalakefolder_createdonbehalfby](#BKMK_lk_datalakefolder_createdonbehalfby)
- [lk_datalakefolder_modifiedby](#BKMK_lk_datalakefolder_modifiedby)
- [lk_datalakefolder_modifiedonbehalfby](#BKMK_lk_datalakefolder_modifiedonbehalfby)
- [owner_datalakefolder](#BKMK_owner_datalakefolder)
- [team_datalakefolder](#BKMK_team_datalakefolder)
- [user_datalakefolder](#BKMK_user_datalakefolder)

### <a name="BKMK_business_unit_datalakefolder"></a> business_unit_datalakefolder

One-To-Many Relationship: [businessunit business_unit_datalakefolder](businessunit.md#BKMK_business_unit_datalakefolder)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_datalakefolder_datalakesubfolder-many-to-one"></a> datalakefolder_datalakesubfolder

One-To-Many Relationship: [datalakefolder datalakefolder_datalakesubfolder](#BKMK_datalakefolder_datalakesubfolder-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`datalakefolder`|
|ReferencedAttribute|`datalakefolderid`|
|ReferencingAttribute|`parentfolderid`|
|ReferencingEntityNavigationPropertyName|`parentfolderid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_datalakefolder_createdby"></a> lk_datalakefolder_createdby

One-To-Many Relationship: [systemuser lk_datalakefolder_createdby](systemuser.md#BKMK_lk_datalakefolder_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_datalakefolder_createdonbehalfby"></a> lk_datalakefolder_createdonbehalfby

One-To-Many Relationship: [systemuser lk_datalakefolder_createdonbehalfby](systemuser.md#BKMK_lk_datalakefolder_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_datalakefolder_modifiedby"></a> lk_datalakefolder_modifiedby

One-To-Many Relationship: [systemuser lk_datalakefolder_modifiedby](systemuser.md#BKMK_lk_datalakefolder_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_datalakefolder_modifiedonbehalfby"></a> lk_datalakefolder_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_datalakefolder_modifiedonbehalfby](systemuser.md#BKMK_lk_datalakefolder_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_datalakefolder"></a> owner_datalakefolder

One-To-Many Relationship: [owner owner_datalakefolder](owner.md#BKMK_owner_datalakefolder)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_datalakefolder"></a> team_datalakefolder

One-To-Many Relationship: [team team_datalakefolder](team.md#BKMK_team_datalakefolder)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_datalakefolder"></a> user_datalakefolder

One-To-Many Relationship: [systemuser user_datalakefolder](systemuser.md#BKMK_user_datalakefolder)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [datalakefolder_AsyncOperations](#BKMK_datalakefolder_AsyncOperations)
- [datalakefolder_BulkDeleteFailures](#BKMK_datalakefolder_BulkDeleteFailures)
- [datalakefolder_datalakefolderpermission](#BKMK_datalakefolder_datalakefolderpermission)
- [datalakefolder_datalakesubfolder](#BKMK_datalakefolder_datalakesubfolder-one-to-many)
- [datalakefolder_DuplicateBaseRecord](#BKMK_datalakefolder_DuplicateBaseRecord)
- [datalakefolder_DuplicateMatchingRecord](#BKMK_datalakefolder_DuplicateMatchingRecord)
- [datalakefolder_MailboxTrackingFolders](#BKMK_datalakefolder_MailboxTrackingFolders)
- [datalakefolder_PrincipalObjectAttributeAccesses](#BKMK_datalakefolder_PrincipalObjectAttributeAccesses)
- [datalakefolder_ProcessSession](#BKMK_datalakefolder_ProcessSession)
- [datalakefolder_SyncErrors](#BKMK_datalakefolder_SyncErrors)
- [msdyn_dataflow_datalakefolder_dlfolder](#BKMK_msdyn_dataflow_datalakefolder_dlfolder)
- [synapsedatabases](#BKMK_synapsedatabases)
- [synapselinkexternaltablestates](#BKMK_synapselinkexternaltablestates)
- [synapselinkprofiles](#BKMK_synapselinkprofiles)

### <a name="BKMK_datalakefolder_AsyncOperations"></a> datalakefolder_AsyncOperations

Many-To-One Relationship: [asyncoperation datalakefolder_AsyncOperations](asyncoperation.md#BKMK_datalakefolder_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`datalakefolder_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_datalakefolder_BulkDeleteFailures"></a> datalakefolder_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure datalakefolder_BulkDeleteFailures](bulkdeletefailure.md#BKMK_datalakefolder_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`datalakefolder_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_datalakefolder_datalakefolderpermission"></a> datalakefolder_datalakefolderpermission

Many-To-One Relationship: [datalakefolderpermission datalakefolder_datalakefolderpermission](datalakefolderpermission.md#BKMK_datalakefolder_datalakefolderpermission)

|Property|Value|
|---|---|
|ReferencingEntity|`datalakefolderpermission`|
|ReferencingAttribute|`folderid`|
|ReferencedEntityNavigationPropertyName|`datalakefolder_datalakefolderpermission`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_datalakefolder_datalakesubfolder-one-to-many"></a> datalakefolder_datalakesubfolder

Many-To-One Relationship: [datalakefolder datalakefolder_datalakesubfolder](#BKMK_datalakefolder_datalakesubfolder-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`datalakefolder`|
|ReferencingAttribute|`parentfolderid`|
|ReferencedEntityNavigationPropertyName|`datalakefolder_datalakesubfolder`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_datalakefolder_DuplicateBaseRecord"></a> datalakefolder_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord datalakefolder_DuplicateBaseRecord](duplicaterecord.md#BKMK_datalakefolder_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`datalakefolder_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_datalakefolder_DuplicateMatchingRecord"></a> datalakefolder_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord datalakefolder_DuplicateMatchingRecord](duplicaterecord.md#BKMK_datalakefolder_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`datalakefolder_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_datalakefolder_MailboxTrackingFolders"></a> datalakefolder_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder datalakefolder_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_datalakefolder_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`datalakefolder_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_datalakefolder_PrincipalObjectAttributeAccesses"></a> datalakefolder_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess datalakefolder_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_datalakefolder_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`datalakefolder_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_datalakefolder_ProcessSession"></a> datalakefolder_ProcessSession

Many-To-One Relationship: [processsession datalakefolder_ProcessSession](processsession.md#BKMK_datalakefolder_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`datalakefolder_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_datalakefolder_SyncErrors"></a> datalakefolder_SyncErrors

Many-To-One Relationship: [syncerror datalakefolder_SyncErrors](syncerror.md#BKMK_datalakefolder_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`datalakefolder_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_dataflow_datalakefolder_dlfolder"></a> msdyn_dataflow_datalakefolder_dlfolder

Many-To-One Relationship: [msdyn_dataflow_datalakefolder msdyn_dataflow_datalakefolder_dlfolder](msdyn_dataflow_datalakefolder.md#BKMK_msdyn_dataflow_datalakefolder_dlfolder)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflow_datalakefolder`|
|ReferencingAttribute|`msdyn_datalakefolder`|
|ReferencedEntityNavigationPropertyName|`msdyn_dataflow_datalakefolder_dlfolder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapsedatabases"></a> synapsedatabases

Many-To-One Relationship: [synapsedatabase synapsedatabases](synapsedatabase.md#BKMK_synapsedatabases)

|Property|Value|
|---|---|
|ReferencingEntity|`synapsedatabase`|
|ReferencingAttribute|`datalakefolder`|
|ReferencedEntityNavigationPropertyName|`synapsedatabases`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkexternaltablestates"></a> synapselinkexternaltablestates

Many-To-One Relationship: [synapselinkexternaltablestate synapselinkexternaltablestates](synapselinkexternaltablestate.md#BKMK_synapselinkexternaltablestates)

|Property|Value|
|---|---|
|ReferencingEntity|`synapselinkexternaltablestate`|
|ReferencingAttribute|`datalakefolder`|
|ReferencedEntityNavigationPropertyName|`synapselinkexternaltablestates`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofiles"></a> synapselinkprofiles

Many-To-One Relationship: [synapselinkprofile synapselinkprofiles](synapselinkprofile.md#BKMK_synapselinkprofiles)

|Property|Value|
|---|---|
|ReferencingEntity|`synapselinkprofile`|
|ReferencingAttribute|`datalakefolder`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofiles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.datalakefolder?displayProperty=fullName>
