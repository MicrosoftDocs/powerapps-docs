---
title: "Managed Identity (ManagedIdentity) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Managed Identity (ManagedIdentity) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Managed Identity (ManagedIdentity) table/entity reference (Microsoft Dataverse)

Contains data to represent an Azure Active Directory Application used to connect to secure web-hosted resources.

## Messages

The following table lists the messages for the Managed Identity (ManagedIdentity) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /managedidentities(*managedidentityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /managedidentities<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /managedidentities(*managedidentityid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /managedidentities(*managedidentityid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /managedidentities<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /managedidentities(*managedidentityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /managedidentities(*managedidentityid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /managedidentities(*managedidentityid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Managed Identity (ManagedIdentity) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Managed Identity** |
| **DisplayCollectionName** | **Managed Identities** |
| **SchemaName** | `ManagedIdentity` |
| **CollectionSchemaName** | `ManagedIdentities` |
| **EntitySetName** | `managedidentities`|
| **LogicalName** | `managedidentity` |
| **LogicalCollectionName** | `managedidentities` |
| **PrimaryIdAttribute** | `managedidentityid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ApplicationId](#BKMK_ApplicationId)
- [ClientSecret](#BKMK_ClientSecret)
- [CredentialSource](#BKMK_CredentialSource)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [KeyVaultReferenceId](#BKMK_KeyVaultReferenceId)
- [ManagedIdentityId](#BKMK_ManagedIdentityId)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [SubjectScope](#BKMK_SubjectScope)
- [TenantId](#BKMK_TenantId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [Version](#BKMK_Version)

### <a name="BKMK_ApplicationId"></a> ApplicationId

|Property|Value|
|---|---|
|Description|**Application Id**|
|DisplayName|**ApplicationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicationid`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ClientSecret"></a> ClientSecret

|Property|Value|
|---|---|
|Description|**Contains a secret for the Azure Active Directory application. Once set, it cannot be read except by Dataverse.**|
|DisplayName|**Client Secret**|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|`clientsecret`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_CredentialSource"></a> CredentialSource

|Property|Value|
|---|---|
|Description|**Where the Managed Identity will get the credentials to use.**|
|DisplayName|**Credential Source**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`credentialsource`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`credentialsource`|

#### CredentialSource Choices/Options

|Value|Label|
|---|---|
|0|**ClientSecret**|
|1|**KeyVault**|
|2|**IsManaged**|
|3|**MicrosoftFirstPartyCertificate**|

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

### <a name="BKMK_KeyVaultReferenceId"></a> KeyVaultReferenceId

|Property|Value|
|---|---|
|Description|**Unique identifier for keyvaultreference which contains the secret.**|
|DisplayName|**KeyVaultReferenceId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`keyvaultreferenceid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|keyvaultreference|

### <a name="BKMK_ManagedIdentityId"></a> ManagedIdentityId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**ManagedIdentity Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`managedidentityid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name assigned to this Managed Identity.**|
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

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Managed Identity**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`managedidentity_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Managed Identity**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`managedidentity_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SubjectScope"></a> SubjectScope

|Property|Value|
|---|---|
|Description|**Where the Scope of the SubjectName for Managed Identity will be determined.**|
|DisplayName|**Subject Scope**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subjectscope`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`subjectscope`|

#### SubjectScope Choices/Options

|Value|Label|
|---|---|
|0|**GlobalScope**|
|1|**EnviornmentScope**|
|2|**DevOnlyScope**|

### <a name="BKMK_TenantId"></a> TenantId

|Property|Value|
|---|---|
|Description|**The Id of the Azure Active Directory Tenant that the Application is part of.**|
|DisplayName|**TenantId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tenantid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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

### <a name="BKMK_Version"></a> Version

|Property|Value|
|---|---|
|Description|**Version indicating the format of the FIC subject.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`version`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|


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
- [ObjectId](#BKMK_ObjectId)
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

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**ObjectId**|
|DisplayName|**ObjectId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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

- [business_unit_managedidentity](#BKMK_business_unit_managedidentity)
- [keyvaultreference_ManagedIdentity](#BKMK_keyvaultreference_ManagedIdentity)
- [lk_managedidentity_createdby](#BKMK_lk_managedidentity_createdby)
- [lk_managedidentity_createdonbehalfby](#BKMK_lk_managedidentity_createdonbehalfby)
- [lk_managedidentity_modifiedby](#BKMK_lk_managedidentity_modifiedby)
- [lk_managedidentity_modifiedonbehalfby](#BKMK_lk_managedidentity_modifiedonbehalfby)
- [owner_managedidentity](#BKMK_owner_managedidentity)
- [team_managedidentity](#BKMK_team_managedidentity)
- [user_managedidentity](#BKMK_user_managedidentity)

### <a name="BKMK_business_unit_managedidentity"></a> business_unit_managedidentity

One-To-Many Relationship: [businessunit business_unit_managedidentity](businessunit.md#BKMK_business_unit_managedidentity)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_keyvaultreference_ManagedIdentity"></a> keyvaultreference_ManagedIdentity

One-To-Many Relationship: [keyvaultreference keyvaultreference_ManagedIdentity](keyvaultreference.md#BKMK_keyvaultreference_ManagedIdentity)

|Property|Value|
|---|---|
|ReferencedEntity|`keyvaultreference`|
|ReferencedAttribute|`keyvaultreferenceid`|
|ReferencingAttribute|`keyvaultreferenceid`|
|ReferencingEntityNavigationPropertyName|`keyvaultreferenceid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_managedidentity_createdby"></a> lk_managedidentity_createdby

One-To-Many Relationship: [systemuser lk_managedidentity_createdby](systemuser.md#BKMK_lk_managedidentity_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_managedidentity_createdonbehalfby"></a> lk_managedidentity_createdonbehalfby

One-To-Many Relationship: [systemuser lk_managedidentity_createdonbehalfby](systemuser.md#BKMK_lk_managedidentity_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_managedidentity_modifiedby"></a> lk_managedidentity_modifiedby

One-To-Many Relationship: [systemuser lk_managedidentity_modifiedby](systemuser.md#BKMK_lk_managedidentity_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_managedidentity_modifiedonbehalfby"></a> lk_managedidentity_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_managedidentity_modifiedonbehalfby](systemuser.md#BKMK_lk_managedidentity_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_managedidentity"></a> owner_managedidentity

One-To-Many Relationship: [owner owner_managedidentity](owner.md#BKMK_owner_managedidentity)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_managedidentity"></a> team_managedidentity

One-To-Many Relationship: [team team_managedidentity](team.md#BKMK_team_managedidentity)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_managedidentity"></a> user_managedidentity

One-To-Many Relationship: [systemuser user_managedidentity](systemuser.md#BKMK_user_managedidentity)

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

- [ComponentId_CertificateCredential_Managedidentity](#BKMK_ComponentId_CertificateCredential_Managedidentity)
- [managedidentity_AsyncOperations](#BKMK_managedidentity_AsyncOperations)
- [managedidentity_BulkDeleteFailures](#BKMK_managedidentity_BulkDeleteFailures)
- [managedidentity_DuplicateBaseRecord](#BKMK_managedidentity_DuplicateBaseRecord)
- [managedidentity_DuplicateMatchingRecord](#BKMK_managedidentity_DuplicateMatchingRecord)
- [managedidentity_emailserverprofile_acsmanagedidentityid](#BKMK_managedidentity_emailserverprofile_acsmanagedidentityid)
- [managedidentity_emailserverprofile_managedidentityid](#BKMK_managedidentity_emailserverprofile_managedidentityid)
- [managedidentity_emailserverprofile_purviewmanagedidentityid](#BKMK_managedidentity_emailserverprofile_purviewmanagedidentityid)
- [managedidentity_KeyVaultReference](#BKMK_managedidentity_KeyVaultReference)
- [managedidentity_MailboxTrackingFolders](#BKMK_managedidentity_MailboxTrackingFolders)
- [managedidentity_PluginAssembly](#BKMK_managedidentity_PluginAssembly)
- [managedidentity_pluginpackage](#BKMK_managedidentity_pluginpackage)
- [managedidentity_PrincipalObjectAttributeAccesses](#BKMK_managedidentity_PrincipalObjectAttributeAccesses)
- [managedidentity_ProcessSession](#BKMK_managedidentity_ProcessSession)
- [managedidentity_ServiceEndpoint](#BKMK_managedidentity_ServiceEndpoint)
- [ManagedIdentity_SharePointManagedIdentity_ManagedIdentityId](#BKMK_ManagedIdentity_SharePointManagedIdentity_ManagedIdentityId)
- [managedidentity_SyncErrors](#BKMK_managedidentity_SyncErrors)
- [PowerPagesManagedIdentity_ManagedIdentity_ManagedIdentity](#BKMK_PowerPagesManagedIdentity_ManagedIdentity_ManagedIdentity)

### <a name="BKMK_ComponentId_CertificateCredential_Managedidentity"></a> ComponentId_CertificateCredential_Managedidentity

Many-To-One Relationship: [certificatecredential ComponentId_CertificateCredential_Managedidentity](certificatecredential.md#BKMK_ComponentId_CertificateCredential_Managedidentity)

|Property|Value|
|---|---|
|ReferencingEntity|`certificatecredential`|
|ReferencingAttribute|`componentid`|
|ReferencedEntityNavigationPropertyName|`ComponentId_CertificateCredential_Managedidentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_AsyncOperations"></a> managedidentity_AsyncOperations

Many-To-One Relationship: [asyncoperation managedidentity_AsyncOperations](asyncoperation.md#BKMK_managedidentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_BulkDeleteFailures"></a> managedidentity_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure managedidentity_BulkDeleteFailures](bulkdeletefailure.md#BKMK_managedidentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_DuplicateBaseRecord"></a> managedidentity_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord managedidentity_DuplicateBaseRecord](duplicaterecord.md#BKMK_managedidentity_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_DuplicateMatchingRecord"></a> managedidentity_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord managedidentity_DuplicateMatchingRecord](duplicaterecord.md#BKMK_managedidentity_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_emailserverprofile_acsmanagedidentityid"></a> managedidentity_emailserverprofile_acsmanagedidentityid

Many-To-One Relationship: [emailserverprofile managedidentity_emailserverprofile_acsmanagedidentityid](emailserverprofile.md#BKMK_managedidentity_emailserverprofile_acsmanagedidentityid)

|Property|Value|
|---|---|
|ReferencingEntity|`emailserverprofile`|
|ReferencingAttribute|`acsmanagedidentityid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_emailserverprofile_acsmanagedidentityid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_emailserverprofile_managedidentityid"></a> managedidentity_emailserverprofile_managedidentityid

Many-To-One Relationship: [emailserverprofile managedidentity_emailserverprofile_managedidentityid](emailserverprofile.md#BKMK_managedidentity_emailserverprofile_managedidentityid)

|Property|Value|
|---|---|
|ReferencingEntity|`emailserverprofile`|
|ReferencingAttribute|`managedidentityid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_emailserverprofile_managedidentityid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_emailserverprofile_purviewmanagedidentityid"></a> managedidentity_emailserverprofile_purviewmanagedidentityid

Many-To-One Relationship: [emailserverprofile managedidentity_emailserverprofile_purviewmanagedidentityid](emailserverprofile.md#BKMK_managedidentity_emailserverprofile_purviewmanagedidentityid)

|Property|Value|
|---|---|
|ReferencingEntity|`emailserverprofile`|
|ReferencingAttribute|`purviewmanagedidentityid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_emailserverprofile_purviewmanagedidentityid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_KeyVaultReference"></a> managedidentity_KeyVaultReference

Many-To-One Relationship: [keyvaultreference managedidentity_KeyVaultReference](keyvaultreference.md#BKMK_managedidentity_KeyVaultReference)

|Property|Value|
|---|---|
|ReferencingEntity|`keyvaultreference`|
|ReferencingAttribute|`managedidentityid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_KeyVaultReference`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_MailboxTrackingFolders"></a> managedidentity_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder managedidentity_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_managedidentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_PluginAssembly"></a> managedidentity_PluginAssembly

Many-To-One Relationship: [pluginassembly managedidentity_PluginAssembly](pluginassembly.md#BKMK_managedidentity_PluginAssembly)

|Property|Value|
|---|---|
|ReferencingEntity|`pluginassembly`|
|ReferencingAttribute|`managedidentityid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_PluginAssembly`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_pluginpackage"></a> managedidentity_pluginpackage

Many-To-One Relationship: [pluginpackage managedidentity_pluginpackage](pluginpackage.md#BKMK_managedidentity_pluginpackage)

|Property|Value|
|---|---|
|ReferencingEntity|`pluginpackage`|
|ReferencingAttribute|`managedidentityid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_pluginpackage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_PrincipalObjectAttributeAccesses"></a> managedidentity_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess managedidentity_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_managedidentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_ProcessSession"></a> managedidentity_ProcessSession

Many-To-One Relationship: [processsession managedidentity_ProcessSession](processsession.md#BKMK_managedidentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_ServiceEndpoint"></a> managedidentity_ServiceEndpoint

Many-To-One Relationship: [serviceendpoint managedidentity_ServiceEndpoint](serviceendpoint.md#BKMK_managedidentity_ServiceEndpoint)

|Property|Value|
|---|---|
|ReferencingEntity|`serviceendpoint`|
|ReferencingAttribute|`managedidentityid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_ServiceEndpoint`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ManagedIdentity_SharePointManagedIdentity_ManagedIdentityId"></a> ManagedIdentity_SharePointManagedIdentity_ManagedIdentityId

Many-To-One Relationship: [sharepointmanagedidentity ManagedIdentity_SharePointManagedIdentity_ManagedIdentityId](sharepointmanagedidentity.md#BKMK_ManagedIdentity_SharePointManagedIdentity_ManagedIdentityId)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointmanagedidentity`|
|ReferencingAttribute|`managedidentityid`|
|ReferencedEntityNavigationPropertyName|`ManagedIdentity_SharePointManagedIdentity_ManagedIdentityId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_managedidentity_SyncErrors"></a> managedidentity_SyncErrors

Many-To-One Relationship: [syncerror managedidentity_SyncErrors](syncerror.md#BKMK_managedidentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`managedidentity_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_PowerPagesManagedIdentity_ManagedIdentity_ManagedIdentity"></a> PowerPagesManagedIdentity_ManagedIdentity_ManagedIdentity

Many-To-One Relationship: [powerpagesmanagedidentity PowerPagesManagedIdentity_ManagedIdentity_ManagedIdentity](powerpagesmanagedidentity.md#BKMK_PowerPagesManagedIdentity_ManagedIdentity_ManagedIdentity)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesmanagedidentity`|
|ReferencingAttribute|`managedidentity`|
|ReferencedEntityNavigationPropertyName|`PowerPagesManagedIdentity_ManagedIdentity_ManagedIdentity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.managedidentity?displayProperty=fullName>
