---
title: "Flow Machine (flowmachine) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Flow Machine (flowmachine) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Flow Machine (flowmachine) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Flow Machine (flowmachine) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /flowmachines(*flowmachineid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /flowmachines<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /flowmachines(*flowmachineid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `LeaveGroup`<br />Event: False |<xref:Microsoft.Dynamics.CRM.LeaveGroup?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `RestartHostedMachine`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RestartHostedMachine?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /flowmachines(*flowmachineid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /flowmachines<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /flowmachines(*flowmachineid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /flowmachines(*flowmachineid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /flowmachines(*flowmachineid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Flow Machine (flowmachine) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Flow Machine** |
| **DisplayCollectionName** | **Flow Machines** |
| **SchemaName** | `flowmachine` |
| **CollectionSchemaName** | `flowmachines` |
| **EntitySetName** | `flowmachines`|
| **LogicalName** | `flowmachine` |
| **LogicalCollectionName** | `flowmachines` |
| **PrimaryIdAttribute** | `flowmachineid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AgentVersion](#BKMK_AgentVersion)
- [ConnectivityConfiguration](#BKMK_ConnectivityConfiguration)
- [Description](#BKMK_Description)
- [FlowMachineGroupId](#BKMK_FlowMachineGroupId)
- [FlowMachineImageVersionId](#BKMK_FlowMachineImageVersionId)
- [FlowMachineNetworkId](#BKMK_FlowMachineNetworkId)
- [HostedMachineError](#BKMK_HostedMachineError)
- [HostedMachineState](#BKMK_HostedMachineState)
- [HostingType](#BKMK_HostingType)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [KeyDeliveryStatus](#BKMK_KeyDeliveryStatus)
- [KeyReceivedDate](#BKMK_KeyReceivedDate)
- [LastHeartbeatDate](#BKMK_LastHeartbeatDate)
- [LastKnownPictureInPictureSupport](#BKMK_LastKnownPictureInPictureSupport)
- [MachineMetadata](#BKMK_MachineMetadata)
- [name](#BKMK_name)
- [OvercapacitySince](#BKMK_OvercapacitySince)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [SessionCapacity](#BKMK_SessionCapacity)
- [SnapshotStartedAt](#BKMK_SnapshotStartedAt)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AgentVersion"></a> AgentVersion

|Property|Value|
|---|---|
|Description|**Version installed on the machine**|
|DisplayName|**Agent Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`agentversion`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ConnectivityConfiguration"></a> ConnectivityConfiguration

|Property|Value|
|---|---|
|Description|**For Internal Use Only.**|
|DisplayName|**Connectivity Configuration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectivityconfiguration`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25000|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the Flow Machine.**|
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

### <a name="BKMK_FlowMachineGroupId"></a> FlowMachineGroupId

|Property|Value|
|---|---|
|Description|**Group of this Flow Machine.**|
|DisplayName|**Flow Machine Group**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`flowmachinegroupid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|flowmachinegroup|

### <a name="BKMK_FlowMachineImageVersionId"></a> FlowMachineImageVersionId

|Property|Value|
|---|---|
|Description|**Unique identifier for Flow Machine Image Version associated with Flow Machine.**|
|DisplayName|**Flow Machine Image Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`flowmachineimageversionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowmachineimageversion|

### <a name="BKMK_FlowMachineNetworkId"></a> FlowMachineNetworkId

|Property|Value|
|---|---|
|Description|**Unique identifier for Flow Machine Network associated with Flow Machine.**|
|DisplayName|**Flow Machine Network**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`flowmachinenetworkid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowmachinenetwork|

### <a name="BKMK_HostedMachineError"></a> HostedMachineError

|Property|Value|
|---|---|
|Description|**Hosted flow machine error.**|
|DisplayName|**Hosted flow machine error.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`hostedmachineerror`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_HostedMachineState"></a> HostedMachineState

|Property|Value|
|---|---|
|Description|**The state of the machine if it is hosted.**|
|DisplayName|**Hosted Machine State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`hostedmachinestate`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowmachine_hostedmachinestate`|

#### HostedMachineState Choices/Options

|Value|Label|
|---|---|
|0|**Disabled**|
|1|**Enabled**|
|2|**Error**|

### <a name="BKMK_HostingType"></a> HostingType

|Property|Value|
|---|---|
|Description|**Flow Machine Hosting Type.**|
|DisplayName|**Flow Machine Hosting Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`hostingtype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowmachine_hostingtype`|

#### HostingType Choices/Options

|Value|Label|
|---|---|
|0|**Customer**|
|1|**Hosted**|
|2|**CloudPc**|

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

### <a name="BKMK_KeyDeliveryStatus"></a> KeyDeliveryStatus

|Property|Value|
|---|---|
|Description|**Delivery status of the machine's group's key.**|
|DisplayName|**Machine Key Delivery Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`keydeliverystatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`flowmachine_keydeliverystatus`|

#### KeyDeliveryStatus Choices/Options

|Value|Label|
|---|---|
|1|**Default**|
|2|**PendingNewKey**|
|3|**KeyExpired**|

### <a name="BKMK_KeyReceivedDate"></a> KeyReceivedDate

|Property|Value|
|---|---|
|Description|**Delivery date of the latest group key.**|
|DisplayName|**Machine Key Received Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`keyreceiveddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastHeartbeatDate"></a> LastHeartbeatDate

|Property|Value|
|---|---|
|Description|**Last date at which a heartbeat call was received from the machine.**|
|DisplayName|**Last heartbeat date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastheartbeatdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastKnownPictureInPictureSupport"></a> LastKnownPictureInPictureSupport

|Property|Value|
|---|---|
|Description|**Indicates the last known picture-in-picture feature support for the target record. Default value is Unknown.**|
|DisplayName|**Last known picture-in-picture support**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastknownpictureinpicturesupport`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`flowmachine_lastknownpictureinpicturesupport`|

#### LastKnownPictureInPictureSupport Choices/Options

|Value|Label|
|---|---|
|0|**Unknown**|
|1|**Disabled**|
|2|**Enabled**|

### <a name="BKMK_MachineMetadata"></a> MachineMetadata

|Property|Value|
|---|---|
|Description|**For Internal Use Only.**|
|DisplayName|**Machine Metadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`machinemetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25000|

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The Name of the Flow Machine.**|
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

### <a name="BKMK_OvercapacitySince"></a> OvercapacitySince

|Property|Value|
|---|---|
|Description|**Date and time of when the machine has been flagged as overcapacity.**|
|DisplayName|**Overcapacity since**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`overcapacitysince`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

### <a name="BKMK_SessionCapacity"></a> SessionCapacity

|Property|Value|
|---|---|
|Description|**Maximum Number of session in parallel.**|
|DisplayName|**Session Capacity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sessioncapacity`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_SnapshotStartedAt"></a> SnapshotStartedAt

|Property|Value|
|---|---|
|Description|**Time at which the snapshot capture started for a Hosted Hachine**|
|DisplayName|**Snapshot started at**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`snapshotstartedat`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Flow Machine**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`flowmachine_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|
|2|Label: **Maintenance**<br />DefaultStatus: 3<br />InvariantName: `Maintenance`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Flow Machine**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`flowmachine_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|
|3|Label: **RequiresReconnection**<br />State:2<br />TransitionData: None|
|4|Label: **ManualMaintenance**<br />State:2<br />TransitionData: None|
|5|Label: **DrainMode**<br />State:2<br />TransitionData: None|
|6|Label: **ToDelete**<br />State:2<br />TransitionData: None|
|7|Label: **Temporary**<br />State:2<br />TransitionData: None|
|8|Label: **Error**<br />State:2<br />TransitionData: None|
|9|Label: **Disabled**<br />State:2<br />TransitionData: None|
|10|Label: **Provisioning**<br />State:2<br />TransitionData: None|
|11|Label: **RequiresGroupKey**<br />State:2<br />TransitionData: None|
|12|Label: **ProvisionedWithError**<br />State:2<br />TransitionData: None|
|13|Label: **HostedMachineOvercapacity**<br />State:0<br />TransitionData: None|
|14|Label: **HostedMachineOvercapacityDeleted**<br />State:2<br />TransitionData: None|
|15|Label: **HostedMachineOvercapacityDisabled**<br />State:2<br />TransitionData: None|

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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [flowmachineId](#BKMK_flowmachineId)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

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

### <a name="BKMK_flowmachineId"></a> flowmachineId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Flow Machine**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`flowmachineid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

- [business_unit_flowmachine](#BKMK_business_unit_flowmachine)
- [flowmachine_flowmachineimageversion](#BKMK_flowmachine_flowmachineimageversion)
- [flowmachine_flowmachinenetwork](#BKMK_flowmachine_flowmachinenetwork)
- [flowmachinegroup_flowmachine](#BKMK_flowmachinegroup_flowmachine)
- [lk_flowmachine_createdby](#BKMK_lk_flowmachine_createdby)
- [lk_flowmachine_createdonbehalfby](#BKMK_lk_flowmachine_createdonbehalfby)
- [lk_flowmachine_modifiedby](#BKMK_lk_flowmachine_modifiedby)
- [lk_flowmachine_modifiedonbehalfby](#BKMK_lk_flowmachine_modifiedonbehalfby)
- [owner_flowmachine](#BKMK_owner_flowmachine)
- [team_flowmachine](#BKMK_team_flowmachine)
- [user_flowmachine](#BKMK_user_flowmachine)

### <a name="BKMK_business_unit_flowmachine"></a> business_unit_flowmachine

One-To-Many Relationship: [businessunit business_unit_flowmachine](businessunit.md#BKMK_business_unit_flowmachine)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachine_flowmachineimageversion"></a> flowmachine_flowmachineimageversion

One-To-Many Relationship: [flowmachineimageversion flowmachine_flowmachineimageversion](flowmachineimageversion.md#BKMK_flowmachine_flowmachineimageversion)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimageversion`|
|ReferencedAttribute|`flowmachineimageversionid`|
|ReferencingAttribute|`flowmachineimageversionid`|
|ReferencingEntityNavigationPropertyName|`FlowMachineImageVersionId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachine_flowmachinenetwork"></a> flowmachine_flowmachinenetwork

One-To-Many Relationship: [flowmachinenetwork flowmachine_flowmachinenetwork](flowmachinenetwork.md#BKMK_flowmachine_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinenetwork`|
|ReferencedAttribute|`flowmachinenetworkid`|
|ReferencingAttribute|`flowmachinenetworkid`|
|ReferencingEntityNavigationPropertyName|`FlowMachineNetworkId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachinegroup_flowmachine"></a> flowmachinegroup_flowmachine

One-To-Many Relationship: [flowmachinegroup flowmachinegroup_flowmachine](flowmachinegroup.md#BKMK_flowmachinegroup_flowmachine)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachinegroup`|
|ReferencedAttribute|`flowmachinegroupid`|
|ReferencingAttribute|`flowmachinegroupid`|
|ReferencingEntityNavigationPropertyName|`FlowMachineGroupId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_flowmachine_createdby"></a> lk_flowmachine_createdby

One-To-Many Relationship: [systemuser lk_flowmachine_createdby](systemuser.md#BKMK_lk_flowmachine_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachine_createdonbehalfby"></a> lk_flowmachine_createdonbehalfby

One-To-Many Relationship: [systemuser lk_flowmachine_createdonbehalfby](systemuser.md#BKMK_lk_flowmachine_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachine_modifiedby"></a> lk_flowmachine_modifiedby

One-To-Many Relationship: [systemuser lk_flowmachine_modifiedby](systemuser.md#BKMK_lk_flowmachine_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachine_modifiedonbehalfby"></a> lk_flowmachine_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_flowmachine_modifiedonbehalfby](systemuser.md#BKMK_lk_flowmachine_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_flowmachine"></a> owner_flowmachine

One-To-Many Relationship: [owner owner_flowmachine](owner.md#BKMK_owner_flowmachine)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_flowmachine"></a> team_flowmachine

One-To-Many Relationship: [team team_flowmachine](team.md#BKMK_team_flowmachine)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_flowmachine"></a> user_flowmachine

One-To-Many Relationship: [systemuser user_flowmachine](systemuser.md#BKMK_user_flowmachine)

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

- [flowcapacityassignment_flowmachine](#BKMK_flowcapacityassignment_flowmachine)
- [flowevent_flowmachine](#BKMK_flowevent_flowmachine)
- [flowmachine_AsyncOperations](#BKMK_flowmachine_AsyncOperations)
- [flowmachine_BulkDeleteFailures](#BKMK_flowmachine_BulkDeleteFailures)
- [flowmachine_flowlog_flowmachineid](#BKMK_flowmachine_flowlog_flowmachineid)
- [flowmachine_flowsession_MachineId](#BKMK_flowmachine_flowsession_MachineId)
- [flowmachine_MailboxTrackingFolders](#BKMK_flowmachine_MailboxTrackingFolders)
- [flowmachine_PrincipalObjectAttributeAccesses](#BKMK_flowmachine_PrincipalObjectAttributeAccesses)
- [flowmachine_ProcessSession](#BKMK_flowmachine_ProcessSession)
- [flowmachine_SyncErrors](#BKMK_flowmachine_SyncErrors)
- [flowmachineimageversion_flowmachine](#BKMK_flowmachineimageversion_flowmachine)

### <a name="BKMK_flowcapacityassignment_flowmachine"></a> flowcapacityassignment_flowmachine

Many-To-One Relationship: [flowcapacityassignment flowcapacityassignment_flowmachine](flowcapacityassignment.md#BKMK_flowcapacityassignment_flowmachine)

|Property|Value|
|---|---|
|ReferencingEntity|`flowcapacityassignment`|
|ReferencingAttribute|`regarding`|
|ReferencedEntityNavigationPropertyName|`flowcapacityassignment_flowmachine`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowevent_flowmachine"></a> flowevent_flowmachine

Many-To-One Relationship: [flowevent flowevent_flowmachine](flowevent.md#BKMK_flowevent_flowmachine)

|Property|Value|
|---|---|
|ReferencingEntity|`flowevent`|
|ReferencingAttribute|`parentobjectid`|
|ReferencedEntityNavigationPropertyName|`flowevent_flowmachine`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachine_AsyncOperations"></a> flowmachine_AsyncOperations

Many-To-One Relationship: [asyncoperation flowmachine_AsyncOperations](asyncoperation.md#BKMK_flowmachine_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachine_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachine_BulkDeleteFailures"></a> flowmachine_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure flowmachine_BulkDeleteFailures](bulkdeletefailure.md#BKMK_flowmachine_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachine_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachine_flowlog_flowmachineid"></a> flowmachine_flowlog_flowmachineid

Many-To-One Relationship: [flowlog flowmachine_flowlog_flowmachineid](flowlog.md#BKMK_flowmachine_flowlog_flowmachineid)

|Property|Value|
|---|---|
|ReferencingEntity|`flowlog`|
|ReferencingAttribute|`flowmachineid`|
|ReferencedEntityNavigationPropertyName|`flowmachine_flowlog_flowmachineid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachine_flowsession_MachineId"></a> flowmachine_flowsession_MachineId

Many-To-One Relationship: [flowsession flowmachine_flowsession_MachineId](flowsession.md#BKMK_flowmachine_flowsession_MachineId)

|Property|Value|
|---|---|
|ReferencingEntity|`flowsession`|
|ReferencingAttribute|`machineid`|
|ReferencedEntityNavigationPropertyName|`flowmachine_flowsession_MachineId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachine_MailboxTrackingFolders"></a> flowmachine_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder flowmachine_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_flowmachine_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachine_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachine_PrincipalObjectAttributeAccesses"></a> flowmachine_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess flowmachine_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_flowmachine_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`flowmachine_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachine_ProcessSession"></a> flowmachine_ProcessSession

Many-To-One Relationship: [processsession flowmachine_ProcessSession](processsession.md#BKMK_flowmachine_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachine_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachine_SyncErrors"></a> flowmachine_SyncErrors

Many-To-One Relationship: [syncerror flowmachine_SyncErrors](syncerror.md#BKMK_flowmachine_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachine_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachineimageversion_flowmachine"></a> flowmachineimageversion_flowmachine

Many-To-One Relationship: [flowmachineimageversion flowmachineimageversion_flowmachine](flowmachineimageversion.md#BKMK_flowmachineimageversion_flowmachine)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachineimageversion`|
|ReferencingAttribute|`sourcemachineid`|
|ReferencedEntityNavigationPropertyName|`flowmachineimageversion_flowmachine`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.flowmachine?displayProperty=fullName>
