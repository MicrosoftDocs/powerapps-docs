---
title: "Flow Machine Group (flowmachinegroup) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Flow Machine Group (flowmachinegroup) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Flow Machine Group (flowmachinegroup) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Flow Machine Group (flowmachinegroup) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /flowmachinegroups(*flowmachinegroupid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /flowmachinegroups<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateFlowCredentialApplication`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateFlowCredentialApplication?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /flowmachinegroups(*flowmachinegroupid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteFlowMachineGroup`<br />Event: False |<xref:Microsoft.Dynamics.CRM.DeleteFlowMachineGroup?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GetPublicKey`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GetPublicKey?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /flowmachinegroups(*flowmachinegroupid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /flowmachinegroups<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `RotateGroupKey`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RotateGroupKey?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `SetState`<br />Event: True |`PATCH` /flowmachinegroups(*flowmachinegroupid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /flowmachinegroups(*flowmachinegroupid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateAccountCredentials`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateAccountCredentials?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /flowmachinegroups(*flowmachinegroupid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Flow Machine Group (flowmachinegroup) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Flow Machine Group** |
| **DisplayCollectionName** | **Flow Machine Groups** |
| **SchemaName** | `flowmachinegroup` |
| **CollectionSchemaName** | `flowmachinegroups` |
| **EntitySetName** | `flowmachinegroups`|
| **LogicalName** | `flowmachinegroup` |
| **LogicalCollectionName** | `flowmachinegroups` |
| **PrimaryIdAttribute** | `flowmachinegroupid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Description](#BKMK_Description)
- [DisconnectionPlannedOn](#BKMK_DisconnectionPlannedOn)
- [DomainSetting](#BKMK_DomainSetting)
- [FlowGroupType](#BKMK_FlowGroupType)
- [flowmachineimage](#BKMK_flowmachineimage)
- [flowmachinenetwork](#BKMK_flowmachinenetwork)
- [GroupMetadata](#BKMK_GroupMetadata)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [KeyCreationDate](#BKMK_KeyCreationDate)
- [KeyExpiryGracePeriod](#BKMK_KeyExpiryGracePeriod)
- [KeyValidityPeriod](#BKMK_KeyValidityPeriod)
- [LastRunDate](#BKMK_LastRunDate)
- [ManagementType](#BKMK_ManagementType)
- [MaxManagedMachineCount](#BKMK_MaxManagedMachineCount)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PasswordChangedBy](#BKMK_PasswordChangedBy)
- [PasswordChangedDate](#BKMK_PasswordChangedDate)
- [PreferredQueuingType](#BKMK_PreferredQueuingType)
- [PrimaryKeyPackage](#BKMK_PrimaryKeyPackage)
- [PrimaryPublicKey](#BKMK_PrimaryPublicKey)
- [ProvisioningError](#BKMK_ProvisioningError)
- [ProvisioningState](#BKMK_ProvisioningState)
- [RotationStartedBy](#BKMK_RotationStartedBy)
- [SecondaryKeyPackage](#BKMK_SecondaryKeyPackage)
- [SecondaryPublicKey](#BKMK_SecondaryPublicKey)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [trytoreusewindowssession](#BKMK_trytoreusewindowssession)
- [UsageType](#BKMK_UsageType)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of this Group of Flow Machine**|
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

### <a name="BKMK_DisconnectionPlannedOn"></a> DisconnectionPlannedOn

|Property|Value|
|---|---|
|Description|**If set, the date on which the machines of the group will be disconnected.**|
|DisplayName|**Disconnection planned on**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`disconnectionplannedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_DomainSetting"></a> DomainSetting

|Property|Value|
|---|---|
|Description|**Setting for domain joining of machines in this group.**|
|DisplayName|**Domain setting**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`domainsetting`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowmachinegroup_domainsetting`|

#### DomainSetting Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**AadJoined**|
|2|**HybridEntraJoined**|

### <a name="BKMK_FlowGroupType"></a> FlowGroupType

|Property|Value|
|---|---|
|Description|**Internal Use Only.**|
|DisplayName|**Flow Group Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`flowgrouptype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|545940000|
|GlobalChoiceName|`flowmachinegroup_flowgrouptype`|

#### FlowGroupType Choices/Options

|Value|Label|
|---|---|
|545940000|**Keyless**|
|545940001|**Standard**|
|545940002|**Default**|

### <a name="BKMK_flowmachineimage"></a> flowmachineimage

|Property|Value|
|---|---|
|Description|**Unique identifier for Flow Machine Image associated with Flow Machine Group.**|
|DisplayName|**Flow Machine Image**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`flowmachineimage`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowmachineimage|

### <a name="BKMK_flowmachinenetwork"></a> flowmachinenetwork

|Property|Value|
|---|---|
|Description|**Unique identifier for the Flow Machine Network associated with the Flow Machine Group.**|
|DisplayName|**Flow Machine Network**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`flowmachinenetwork`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowmachinenetwork|

### <a name="BKMK_GroupMetadata"></a> GroupMetadata

|Property|Value|
|---|---|
|Description|**Internal Use Only.**|
|DisplayName|**Group Metadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`groupmetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25000|

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

### <a name="BKMK_KeyCreationDate"></a> KeyCreationDate

|Property|Value|
|---|---|
|Description|**Creation date for group's primary key.**|
|DisplayName|**Key Creation Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`keycreationdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_KeyExpiryGracePeriod"></a> KeyExpiryGracePeriod

|Property|Value|
|---|---|
|Description|**Grace period for machines and connections to update before a certificate rotation. In minutes.**|
|DisplayName|**Group Key Expiry Grace Period**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`keyexpirygraceperiod`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|64800|

### <a name="BKMK_KeyValidityPeriod"></a> KeyValidityPeriod

|Property|Value|
|---|---|
|Description||
|DisplayName|**Group Key Validity Period**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`keyvalidityperiod`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2628000|
|MinValue|129600|

### <a name="BKMK_LastRunDate"></a> LastRunDate

|Property|Value|
|---|---|
|Description|**Last date at which a run has targeted the group.**|
|DisplayName|**Last run date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastrundate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_ManagementType"></a> ManagementType

|Property|Value|
|---|---|
|Description|**Management Type.**|
|DisplayName|**Management Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`managementtype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowmachinegroup_managementtype`|

#### ManagementType Choices/Options

|Value|Label|
|---|---|
|0|**Customer**|
|1|**Managed**|
|2|**Shared**|

### <a name="BKMK_MaxManagedMachineCount"></a> MaxManagedMachineCount

|Property|Value|
|---|---|
|Description|**Maximum managed machine count. Only for use in managed machine groups.**|
|DisplayName|**Maximum managed machine count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`maxmanagedmachinecount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

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

### <a name="BKMK_PasswordChangedBy"></a> PasswordChangedBy

|Property|Value|
|---|---|
|Description|**User who initiated the last password change.**|
|DisplayName|**Group Password Changed By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`passwordchangedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_PasswordChangedDate"></a> PasswordChangedDate

|Property|Value|
|---|---|
|Description|**Date for latest password change.**|
|DisplayName|**Group Password Changed Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`passwordchangeddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_PreferredQueuingType"></a> PreferredQueuingType

|Property|Value|
|---|---|
|Description|**Indicates the preferred queuing type in a given machine group**|
|DisplayName|**Preferred Queing Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`preferredqueuingtype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`flowmachinegroup_preferredqueuingtype`|

#### PreferredQueuingType Choices/Options

|Value|Label|
|---|---|
|0|**FIFO**|
|1|**ExtendedQueuePrioritization**|

### <a name="BKMK_PrimaryKeyPackage"></a> PrimaryKeyPackage

|Property|Value|
|---|---|
|Description|**Internal Use Only**|
|DisplayName|**Primary Key Package**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`primarykeypackage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25000|

### <a name="BKMK_PrimaryPublicKey"></a> PrimaryPublicKey

|Property|Value|
|---|---|
|Description|**Internal Use Only.**|
|DisplayName|**Primary Public Key**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`primarypublickey`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25000|

### <a name="BKMK_ProvisioningError"></a> ProvisioningError

|Property|Value|
|---|---|
|Description||
|DisplayName|**Flow group provisioning error**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`provisioningerror`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_ProvisioningState"></a> ProvisioningState

|Property|Value|
|---|---|
|Description|**The provisioning state of the managed machine group.**|
|DisplayName|**Provisioning State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`provisioningstate`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowmachinegroup_provisioningstate`|

#### ProvisioningState Choices/Options

|Value|Label|
|---|---|
|0|**Created**|
|1|**Provisioning**|
|2|**Provisioned**|
|3|**Error**|

### <a name="BKMK_RotationStartedBy"></a> RotationStartedBy

|Property|Value|
|---|---|
|Description|**User who initiated a group key rotation.**|
|DisplayName|**Group Rotation Started By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`rotationstartedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_SecondaryKeyPackage"></a> SecondaryKeyPackage

|Property|Value|
|---|---|
|Description|**Internal Use Only.**|
|DisplayName|**Secondary Key Package**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`secondarykeypackage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25000|

### <a name="BKMK_SecondaryPublicKey"></a> SecondaryPublicKey

|Property|Value|
|---|---|
|Description|**Internal Use Only.**|
|DisplayName|**Secondary Public Key**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`secondarypublickey`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25000|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Flow Machine Group**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`flowmachinegroup_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|
|2|Label: **Maintenance**<br />DefaultStatus: 3<br />InvariantName: `Maintenance`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Flow Machine Group**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`flowmachinegroup_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|
|3|Label: **ManualMaintenance**<br />State:2<br />TransitionData: None|
|4|Label: **KeyExpired**<br />State:1<br />TransitionData: None|
|5|Label: **HmgIslandMove**<br />State:2<br />TransitionData: None|
|6|Label: **Quarantined**<br />State:2<br />TransitionData: None|
|7|Label: **HmgCmkOperation**<br />State:2<br />TransitionData: None|

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

### <a name="BKMK_trytoreusewindowssession"></a> trytoreusewindowssession

|Property|Value|
|---|---|
|Description|**Indicates whether we will try to reuse non unlocked Windows sessions. Default value is No.**|
|DisplayName|**Try to reuse non unlocked Windows sessions.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`trytoreusewindowssession`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`flowmachinegroup_trytoreusewindowssession`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UsageType"></a> UsageType

|Property|Value|
|---|---|
|Description|**Flow Machine Group Usage Type.**|
|DisplayName|**Flow Machine Group Usage Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`usagetype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowmachinegroup_usagetype`|

#### UsageType Choices/Options

|Value|Label|
|---|---|
|0|**RpaOnly**|
|1|**CuaOnly**|
|2|**RpaAndCua**|

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
- [flowmachinegroupId](#BKMK_flowmachinegroupId)
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

### <a name="BKMK_flowmachinegroupId"></a> flowmachinegroupId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Flow Machine Group**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`flowmachinegroupid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

- [business_unit_flowmachinegroup](#BKMK_business_unit_flowmachinegroup)
- [flowmachinegroup_flowmachineimage](#BKMK_flowmachinegroup_flowmachineimage)
- [flowmachinegroup_flowmachinenetwork](#BKMK_flowmachinegroup_flowmachinenetwork)
- [flowmachinegroup_PasswordChangedBy](#BKMK_flowmachinegroup_PasswordChangedBy)
- [flowmachinegroup_RotationStartedBy](#BKMK_flowmachinegroup_RotationStartedBy)
- [lk_flowmachinegroup_createdby](#BKMK_lk_flowmachinegroup_createdby)
- [lk_flowmachinegroup_createdonbehalfby](#BKMK_lk_flowmachinegroup_createdonbehalfby)
- [lk_flowmachinegroup_modifiedby](#BKMK_lk_flowmachinegroup_modifiedby)
- [lk_flowmachinegroup_modifiedonbehalfby](#BKMK_lk_flowmachinegroup_modifiedonbehalfby)
- [owner_flowmachinegroup](#BKMK_owner_flowmachinegroup)
- [team_flowmachinegroup](#BKMK_team_flowmachinegroup)
- [user_flowmachinegroup](#BKMK_user_flowmachinegroup)

### <a name="BKMK_business_unit_flowmachinegroup"></a> business_unit_flowmachinegroup

One-To-Many Relationship: [businessunit business_unit_flowmachinegroup](businessunit.md#BKMK_business_unit_flowmachinegroup)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_flowmachineimage"></a> flowmachinegroup_flowmachineimage

One-To-Many Relationship: [flowmachineimage flowmachinegroup_flowmachineimage](flowmachineimage.md#BKMK_flowmachinegroup_flowmachineimage)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimage`|
|ReferencedAttribute|`flowmachineimageid`|
|ReferencingAttribute|`flowmachineimage`|
|ReferencingEntityNavigationPropertyName|`flowmachineimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_flowmachinenetwork"></a> flowmachinegroup_flowmachinenetwork

One-To-Many Relationship: [flowmachinenetwork flowmachinegroup_flowmachinenetwork](flowmachinenetwork.md#BKMK_flowmachinegroup_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinenetwork`|
|ReferencedAttribute|`flowmachinenetworkid`|
|ReferencingAttribute|`flowmachinenetwork`|
|ReferencingEntityNavigationPropertyName|`flowmachinenetwork`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_PasswordChangedBy"></a> flowmachinegroup_PasswordChangedBy

One-To-Many Relationship: [systemuser flowmachinegroup_PasswordChangedBy](systemuser.md#BKMK_flowmachinegroup_PasswordChangedBy)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`passwordchangedby`|
|ReferencingEntityNavigationPropertyName|`PasswordChangedBy`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_RotationStartedBy"></a> flowmachinegroup_RotationStartedBy

One-To-Many Relationship: [systemuser flowmachinegroup_RotationStartedBy](systemuser.md#BKMK_flowmachinegroup_RotationStartedBy)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`rotationstartedby`|
|ReferencingEntityNavigationPropertyName|`RotationStartedBy`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachinegroup_createdby"></a> lk_flowmachinegroup_createdby

One-To-Many Relationship: [systemuser lk_flowmachinegroup_createdby](systemuser.md#BKMK_lk_flowmachinegroup_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachinegroup_createdonbehalfby"></a> lk_flowmachinegroup_createdonbehalfby

One-To-Many Relationship: [systemuser lk_flowmachinegroup_createdonbehalfby](systemuser.md#BKMK_lk_flowmachinegroup_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachinegroup_modifiedby"></a> lk_flowmachinegroup_modifiedby

One-To-Many Relationship: [systemuser lk_flowmachinegroup_modifiedby](systemuser.md#BKMK_lk_flowmachinegroup_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachinegroup_modifiedonbehalfby"></a> lk_flowmachinegroup_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_flowmachinegroup_modifiedonbehalfby](systemuser.md#BKMK_lk_flowmachinegroup_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_flowmachinegroup"></a> owner_flowmachinegroup

One-To-Many Relationship: [owner owner_flowmachinegroup](owner.md#BKMK_owner_flowmachinegroup)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_flowmachinegroup"></a> team_flowmachinegroup

One-To-Many Relationship: [team team_flowmachinegroup](team.md#BKMK_team_flowmachinegroup)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_flowmachinegroup"></a> user_flowmachinegroup

One-To-Many Relationship: [systemuser user_flowmachinegroup](systemuser.md#BKMK_user_flowmachinegroup)

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

- [flowcapacityassignment_flowmachinegroup](#BKMK_flowcapacityassignment_flowmachinegroup)
- [flowcredentialapplication_flowmachinegroup](#BKMK_flowcredentialapplication_flowmachinegroup)
- [flowevent_flowmachinegroup](#BKMK_flowevent_flowmachinegroup)
- [flowmachinegroup_AsyncOperations](#BKMK_flowmachinegroup_AsyncOperations)
- [flowmachinegroup_BulkDeleteFailures](#BKMK_flowmachinegroup_BulkDeleteFailures)
- [flowmachinegroup_DuplicateBaseRecord](#BKMK_flowmachinegroup_DuplicateBaseRecord)
- [flowmachinegroup_DuplicateMatchingRecord](#BKMK_flowmachinegroup_DuplicateMatchingRecord)
- [flowmachinegroup_flowlog_flowmachinegroupid](#BKMK_flowmachinegroup_flowlog_flowmachinegroupid)
- [flowmachinegroup_flowlog_parentobjectid](#BKMK_flowmachinegroup_flowlog_parentobjectid)
- [flowmachinegroup_flowmachine](#BKMK_flowmachinegroup_flowmachine)
- [flowmachinegroup_flowsession_MachineGroupId](#BKMK_flowmachinegroup_flowsession_MachineGroupId)
- [flowmachinegroup_MailboxTrackingFolders](#BKMK_flowmachinegroup_MailboxTrackingFolders)
- [flowmachinegroup_PrincipalObjectAttributeAccesses](#BKMK_flowmachinegroup_PrincipalObjectAttributeAccesses)
- [flowmachinegroup_ProcessSession](#BKMK_flowmachinegroup_ProcessSession)
- [flowmachinegroup_SyncErrors](#BKMK_flowmachinegroup_SyncErrors)

### <a name="BKMK_flowcapacityassignment_flowmachinegroup"></a> flowcapacityassignment_flowmachinegroup

Many-To-One Relationship: [flowcapacityassignment flowcapacityassignment_flowmachinegroup](flowcapacityassignment.md#BKMK_flowcapacityassignment_flowmachinegroup)

|Property|Value|
|---|---|
|ReferencingEntity|`flowcapacityassignment`|
|ReferencingAttribute|`regarding`|
|ReferencedEntityNavigationPropertyName|`flowcapacityassignment_flowmachinegroup`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowcredentialapplication_flowmachinegroup"></a> flowcredentialapplication_flowmachinegroup

Many-To-One Relationship: [flowcredentialapplication flowcredentialapplication_flowmachinegroup](flowcredentialapplication.md#BKMK_flowcredentialapplication_flowmachinegroup)

|Property|Value|
|---|---|
|ReferencingEntity|`flowcredentialapplication`|
|ReferencingAttribute|`flowmachinegroupid`|
|ReferencedEntityNavigationPropertyName|`flowcredentialapplication_flowmachinegroup`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowevent_flowmachinegroup"></a> flowevent_flowmachinegroup

Many-To-One Relationship: [flowevent flowevent_flowmachinegroup](flowevent.md#BKMK_flowevent_flowmachinegroup)

|Property|Value|
|---|---|
|ReferencingEntity|`flowevent`|
|ReferencingAttribute|`parentobjectid`|
|ReferencedEntityNavigationPropertyName|`flowevent_flowmachinegroup`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_AsyncOperations"></a> flowmachinegroup_AsyncOperations

Many-To-One Relationship: [asyncoperation flowmachinegroup_AsyncOperations](asyncoperation.md#BKMK_flowmachinegroup_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_BulkDeleteFailures"></a> flowmachinegroup_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure flowmachinegroup_BulkDeleteFailures](bulkdeletefailure.md#BKMK_flowmachinegroup_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_DuplicateBaseRecord"></a> flowmachinegroup_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord flowmachinegroup_DuplicateBaseRecord](duplicaterecord.md#BKMK_flowmachinegroup_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_DuplicateMatchingRecord"></a> flowmachinegroup_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord flowmachinegroup_DuplicateMatchingRecord](duplicaterecord.md#BKMK_flowmachinegroup_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_flowlog_flowmachinegroupid"></a> flowmachinegroup_flowlog_flowmachinegroupid

Many-To-One Relationship: [flowlog flowmachinegroup_flowlog_flowmachinegroupid](flowlog.md#BKMK_flowmachinegroup_flowlog_flowmachinegroupid)

|Property|Value|
|---|---|
|ReferencingEntity|`flowlog`|
|ReferencingAttribute|`flowmachinegroupid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_flowlog_flowmachinegroupid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_flowlog_parentobjectid"></a> flowmachinegroup_flowlog_parentobjectid

Many-To-One Relationship: [flowlog flowmachinegroup_flowlog_parentobjectid](flowlog.md#BKMK_flowmachinegroup_flowlog_parentobjectid)

|Property|Value|
|---|---|
|ReferencingEntity|`flowlog`|
|ReferencingAttribute|`parentobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_flowlog_parentobjectid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_flowmachine"></a> flowmachinegroup_flowmachine

Many-To-One Relationship: [flowmachine flowmachinegroup_flowmachine](flowmachine.md#BKMK_flowmachinegroup_flowmachine)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachine`|
|ReferencingAttribute|`flowmachinegroupid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_flowmachine`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_flowsession_MachineGroupId"></a> flowmachinegroup_flowsession_MachineGroupId

Many-To-One Relationship: [flowsession flowmachinegroup_flowsession_MachineGroupId](flowsession.md#BKMK_flowmachinegroup_flowsession_MachineGroupId)

|Property|Value|
|---|---|
|ReferencingEntity|`flowsession`|
|ReferencingAttribute|`machinegroupid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_flowsession_MachineGroupId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_MailboxTrackingFolders"></a> flowmachinegroup_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder flowmachinegroup_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_flowmachinegroup_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_PrincipalObjectAttributeAccesses"></a> flowmachinegroup_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess flowmachinegroup_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_flowmachinegroup_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_ProcessSession"></a> flowmachinegroup_ProcessSession

Many-To-One Relationship: [processsession flowmachinegroup_ProcessSession](processsession.md#BKMK_flowmachinegroup_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachinegroup_SyncErrors"></a> flowmachinegroup_SyncErrors

Many-To-One Relationship: [syncerror flowmachinegroup_SyncErrors](syncerror.md#BKMK_flowmachinegroup_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachinegroup_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.flowmachinegroup?displayProperty=fullName>
