---
title: "Flow Machine Network (flowmachinenetwork) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Flow Machine Network (flowmachinenetwork) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Flow Machine Network (flowmachinenetwork) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Flow Machine Network (flowmachinenetwork) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /flowmachinenetworks(*flowmachinenetworkid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /flowmachinenetworks<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateFlowMachineNetwork`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateFlowMachineNetwork?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /flowmachinenetworks(*flowmachinenetworkid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /flowmachinenetworks(*flowmachinenetworkid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /flowmachinenetworks<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /flowmachinenetworks(*flowmachinenetworkid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /flowmachinenetworks(*flowmachinenetworkid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateFlowMachineNetwork`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateFlowMachineNetwork?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /flowmachinenetworks(*flowmachinenetworkid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Flow Machine Network (flowmachinenetwork) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Flow Machine Network** |
| **DisplayCollectionName** | **Flow Machine Networks** |
| **SchemaName** | `flowmachinenetwork` |
| **CollectionSchemaName** | `flowmachinenetworks` |
| **EntitySetName** | `flowmachinenetworks`|
| **LogicalName** | `flowmachinenetwork` |
| **LogicalCollectionName** | `flowmachinenetworks` |
| **PrimaryIdAttribute** | `flowmachinenetworkid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CredentialId](#BKMK_CredentialId)
- [description](#BKMK_description)
- [DomainName](#BKMK_DomainName)
- [DomainPassword](#BKMK_DomainPassword)
- [DomainUsername](#BKMK_DomainUsername)
- [flowmachinenetworkId](#BKMK_flowmachinenetworkId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [name](#BKMK_name)
- [NetworkMetadata](#BKMK_NetworkMetadata)
- [OrganizationalUnit](#BKMK_OrganizationalUnit)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ProvisioningState](#BKMK_ProvisioningState)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [statuserrormessage](#BKMK_statuserrormessage)
- [subnet](#BKMK_subnet)
- [SupportedScenario](#BKMK_SupportedScenario)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [type](#BKMK_type)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_CredentialId"></a> CredentialId

|Property|Value|
|---|---|
|Description|**Unique identifier of a Credential entity providing user name and password to be used in hybrid Entra join configurations to join machines to the domain.**|
|DisplayName|**Credential ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`credentialid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|credential|

### <a name="BKMK_description"></a> description

|Property|Value|
|---|---|
|Description||
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_DomainName"></a> DomainName

|Property|Value|
|---|---|
|Description|**Deprecated.**|
|DisplayName|**AD domain name (Deprecated)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`domainname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|64|

### <a name="BKMK_DomainPassword"></a> DomainPassword

|Property|Value|
|---|---|
|Description|**Unique identifier for the secret environment variable holding the password used to join machines to the domain in hybrid Entra join configurations.**|
|DisplayName|**Domain Password**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`domainpassword`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|environmentvariabledefinition|

### <a name="BKMK_DomainUsername"></a> DomainUsername

|Property|Value|
|---|---|
|Description|**Unique identifier for the environment variable holding the username used to join machines to the domain in hybrid Entra join configurations.**|
|DisplayName|**Domain Username**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`domainusername`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|environmentvariabledefinition|

### <a name="BKMK_flowmachinenetworkId"></a> flowmachinenetworkId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Flow Machine Network**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`flowmachinenetworkid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

### <a name="BKMK_NetworkMetadata"></a> NetworkMetadata

|Property|Value|
|---|---|
|Description|**Internal Use Only.**|
|DisplayName|**Network Metadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`networkmetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25000|

### <a name="BKMK_OrganizationalUnit"></a> OrganizationalUnit

|Property|Value|
|---|---|
|Description|**Deprecated.**|
|DisplayName|**Organizational unit (Deprecated)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`organizationalunit`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|260|

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

### <a name="BKMK_ProvisioningState"></a> ProvisioningState

|Property|Value|
|---|---|
|Description|**The provisioning state of the flow machine network.**|
|DisplayName|**Provisioning State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`provisioningstate`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowmachinenetwork_provisioningstate`|

#### ProvisioningState Choices/Options

|Value|Label|
|---|---|
|0|**Created**|
|1|**Provisioning**|
|2|**Provisioned**|
|3|**Error**|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Flow Machine Network**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`flowmachinenetwork_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Flow Machine Network**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`flowmachinenetwork_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|
|3|Label: **Error**<br />State:1<br />TransitionData: None|

### <a name="BKMK_statuserrormessage"></a> statuserrormessage

|Property|Value|
|---|---|
|Description|**Flow Machine Network Error Message.**|
|DisplayName|**Flow Machine Network Error Message.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuserrormessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_subnet"></a> subnet

|Property|Value|
|---|---|
|Description|**The subnet associated to the Flow machine network.**|
|DisplayName|**Subnet**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subnet`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_SupportedScenario"></a> SupportedScenario

|Property|Value|
|---|---|
|Description|**The Flow machine network supported scenario.**|
|DisplayName|**Supported Scenario**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`supportedscenario`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|2|
|GlobalChoiceName|`flowmachinenetwork_supportedscenario`|

#### SupportedScenario Choices/Options

|Value|Label|
|---|---|
|1|**HostedMachineGroup**|
|2|**RpaBox**|
|3|**HostedMachineGroupdAndRpaBox**|

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

### <a name="BKMK_type"></a> type

|Property|Value|
|---|---|
|Description|**The Flow machine network type.**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|100000000|
|GlobalChoiceName|`flowmachinenetwork_type`|

#### type Choices/Options

|Value|Label|
|---|---|
|100000000|**azureAdJoin**|
|100000001|**hybridAdJoin**|

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

- [business_unit_flowmachinenetwork](#BKMK_business_unit_flowmachinenetwork)
- [credential_flowmachinenetwork](#BKMK_credential_flowmachinenetwork)
- [environmentvariabledefinition_flowmachinenetwork_domainpassword](#BKMK_environmentvariabledefinition_flowmachinenetwork_domainpassword)
- [environmentvariabledefinition_flowmachinenetwork_domainusername](#BKMK_environmentvariabledefinition_flowmachinenetwork_domainusername)
- [lk_flowmachinenetwork_createdby](#BKMK_lk_flowmachinenetwork_createdby)
- [lk_flowmachinenetwork_createdonbehalfby](#BKMK_lk_flowmachinenetwork_createdonbehalfby)
- [lk_flowmachinenetwork_modifiedby](#BKMK_lk_flowmachinenetwork_modifiedby)
- [lk_flowmachinenetwork_modifiedonbehalfby](#BKMK_lk_flowmachinenetwork_modifiedonbehalfby)
- [owner_flowmachinenetwork](#BKMK_owner_flowmachinenetwork)
- [team_flowmachinenetwork](#BKMK_team_flowmachinenetwork)
- [user_flowmachinenetwork](#BKMK_user_flowmachinenetwork)

### <a name="BKMK_business_unit_flowmachinenetwork"></a> business_unit_flowmachinenetwork

One-To-Many Relationship: [businessunit business_unit_flowmachinenetwork](businessunit.md#BKMK_business_unit_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_credential_flowmachinenetwork"></a> credential_flowmachinenetwork

One-To-Many Relationship: [credential credential_flowmachinenetwork](credential.md#BKMK_credential_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencedEntity|`credential`|
|ReferencedAttribute|`credentialid`|
|ReferencingAttribute|`credentialid`|
|ReferencingEntityNavigationPropertyName|`CredentialId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_flowmachinenetwork_domainpassword"></a> environmentvariabledefinition_flowmachinenetwork_domainpassword

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_flowmachinenetwork_domainpassword](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_flowmachinenetwork_domainpassword)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`domainpassword`|
|ReferencingEntityNavigationPropertyName|`DomainPassword`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_flowmachinenetwork_domainusername"></a> environmentvariabledefinition_flowmachinenetwork_domainusername

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_flowmachinenetwork_domainusername](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_flowmachinenetwork_domainusername)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`domainusername`|
|ReferencingEntityNavigationPropertyName|`DomainUsername`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachinenetwork_createdby"></a> lk_flowmachinenetwork_createdby

One-To-Many Relationship: [systemuser lk_flowmachinenetwork_createdby](systemuser.md#BKMK_lk_flowmachinenetwork_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachinenetwork_createdonbehalfby"></a> lk_flowmachinenetwork_createdonbehalfby

One-To-Many Relationship: [systemuser lk_flowmachinenetwork_createdonbehalfby](systemuser.md#BKMK_lk_flowmachinenetwork_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachinenetwork_modifiedby"></a> lk_flowmachinenetwork_modifiedby

One-To-Many Relationship: [systemuser lk_flowmachinenetwork_modifiedby](systemuser.md#BKMK_lk_flowmachinenetwork_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachinenetwork_modifiedonbehalfby"></a> lk_flowmachinenetwork_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_flowmachinenetwork_modifiedonbehalfby](systemuser.md#BKMK_lk_flowmachinenetwork_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_flowmachinenetwork"></a> owner_flowmachinenetwork

One-To-Many Relationship: [owner owner_flowmachinenetwork](owner.md#BKMK_owner_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_flowmachinenetwork"></a> team_flowmachinenetwork

One-To-Many Relationship: [team team_flowmachinenetwork](team.md#BKMK_team_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_flowmachinenetwork"></a> user_flowmachinenetwork

One-To-Many Relationship: [systemuser user_flowmachinenetwork](systemuser.md#BKMK_user_flowmachinenetwork)

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

- [flowmachine_flowmachinenetwork](#BKMK_flowmachine_flowmachinenetwork)
- [flowmachinegroup_flowmachinenetwork](#BKMK_flowmachinegroup_flowmachinenetwork)
- [flowmachinenetwork_AsyncOperations](#BKMK_flowmachinenetwork_AsyncOperations)
- [flowmachinenetwork_BulkDeleteFailures](#BKMK_flowmachinenetwork_BulkDeleteFailures)
- [flowmachinenetwork_DuplicateBaseRecord](#BKMK_flowmachinenetwork_DuplicateBaseRecord)
- [flowmachinenetwork_DuplicateMatchingRecord](#BKMK_flowmachinenetwork_DuplicateMatchingRecord)
- [flowmachinenetwork_MailboxTrackingFolders](#BKMK_flowmachinenetwork_MailboxTrackingFolders)
- [flowmachinenetwork_PrincipalObjectAttributeAccesses](#BKMK_flowmachinenetwork_PrincipalObjectAttributeAccesses)
- [flowmachinenetwork_ProcessSession](#BKMK_flowmachinenetwork_ProcessSession)
- [flowmachinenetwork_SyncErrors](#BKMK_flowmachinenetwork_SyncErrors)

### <a name="BKMK_flowmachine_flowmachinenetwork"></a> flowmachine_flowmachinenetwork

Many-To-One Relationship: [flowmachine flowmachine_flowmachinenetwork](flowmachine.md#BKMK_flowmachine_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachine`|
|ReferencingAttribute|`flowmachinenetworkid`|
|ReferencedEntityNavigationPropertyName|`flowmachine_flowmachinenetwork`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_flowmachinenetwork"></a> flowmachinegroup_flowmachinenetwork

Many-To-One Relationship: [flowmachinegroup flowmachinegroup_flowmachinenetwork](flowmachinegroup.md#BKMK_flowmachinegroup_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachinegroup`|
|ReferencingAttribute|`flowmachinenetwork`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_flowmachinenetwork`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinenetwork_AsyncOperations"></a> flowmachinenetwork_AsyncOperations

Many-To-One Relationship: [asyncoperation flowmachinenetwork_AsyncOperations](asyncoperation.md#BKMK_flowmachinenetwork_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinenetwork_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinenetwork_BulkDeleteFailures"></a> flowmachinenetwork_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure flowmachinenetwork_BulkDeleteFailures](bulkdeletefailure.md#BKMK_flowmachinenetwork_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinenetwork_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinenetwork_DuplicateBaseRecord"></a> flowmachinenetwork_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord flowmachinenetwork_DuplicateBaseRecord](duplicaterecord.md#BKMK_flowmachinenetwork_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`flowmachinenetwork_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinenetwork_DuplicateMatchingRecord"></a> flowmachinenetwork_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord flowmachinenetwork_DuplicateMatchingRecord](duplicaterecord.md#BKMK_flowmachinenetwork_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`flowmachinenetwork_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinenetwork_MailboxTrackingFolders"></a> flowmachinenetwork_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder flowmachinenetwork_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_flowmachinenetwork_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinenetwork_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinenetwork_PrincipalObjectAttributeAccesses"></a> flowmachinenetwork_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess flowmachinenetwork_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_flowmachinenetwork_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinenetwork_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinenetwork_ProcessSession"></a> flowmachinenetwork_ProcessSession

Many-To-One Relationship: [processsession flowmachinenetwork_ProcessSession](processsession.md#BKMK_flowmachinenetwork_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinenetwork_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinenetwork_SyncErrors"></a> flowmachinenetwork_SyncErrors

Many-To-One Relationship: [syncerror flowmachinenetwork_SyncErrors](syncerror.md#BKMK_flowmachinenetwork_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinenetwork_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.flowmachinenetwork?displayProperty=fullName>
