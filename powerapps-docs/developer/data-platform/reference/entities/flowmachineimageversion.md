---
title: "Flow Machine Image Version (flowmachineimageversion) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Flow Machine Image Version (flowmachineimageversion) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Flow Machine Image Version (flowmachineimageversion) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Flow Machine Image Version (flowmachineimageversion) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /flowmachineimageversions(*flowmachineimageversionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /flowmachineimageversions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /flowmachineimageversions(*flowmachineimageversionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /flowmachineimageversions(*flowmachineimageversionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /flowmachineimageversions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /flowmachineimageversions(*flowmachineimageversionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /flowmachineimageversions(*flowmachineimageversionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /flowmachineimageversions(*flowmachineimageversionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Flow Machine Image Version (flowmachineimageversion) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Flow Machine Image Version** |
| **DisplayCollectionName** | **Flow Machine Image Versions** |
| **SchemaName** | `flowmachineimageversion` |
| **CollectionSchemaName** | `flowmachineimageversions` |
| **EntitySetName** | `flowmachineimageversions`|
| **LogicalName** | `flowmachineimageversion` |
| **LogicalCollectionName** | `flowmachineimageversions` |
| **PrimaryIdAttribute** | `flowmachineimageversionid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [flowmachineimage](#BKMK_flowmachineimage)
- [flowmachineimageversionId](#BKMK_flowmachineimageversionId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ProvisioningError](#BKMK_ProvisioningError)
- [reference](#BKMK_reference)
- [sourcemachineid](#BKMK_sourcemachineid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [statuserrormessage](#BKMK_statuserrormessage)
- [SupportedScenario](#BKMK_SupportedScenario)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [Version](#BKMK_Version)

### <a name="BKMK_flowmachineimage"></a> flowmachineimage

|Property|Value|
|---|---|
|Description|**Unique identifier for Flow Machine Image associated with Flow Machine Image Version.**|
|DisplayName|**Flow Machine Image**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`flowmachineimage`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|flowmachineimage|

### <a name="BKMK_flowmachineimageversionId"></a> flowmachineimageversionId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Flow Machine Image Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`flowmachineimageversionid`|
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

### <a name="BKMK_ProvisioningError"></a> ProvisioningError

|Property|Value|
|---|---|
|Description||
|DisplayName|**Flow machine image provisioning error**|
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

### <a name="BKMK_reference"></a> reference

|Property|Value|
|---|---|
|Description|**The reference to the underlying image, can be an Azure resource, a blob uri or internal resource.**|
|DisplayName|**Reference**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`reference`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_sourcemachineid"></a> sourcemachineid

|Property|Value|
|---|---|
|Description|**The Hosted Machine which the image was created from**|
|DisplayName|**Source machine**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourcemachineid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|flowmachine|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Flow Machine Image Version**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`flowmachineimageversion_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Flow Machine Image Version**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`flowmachineimageversion_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|
|3|Label: **Error**<br />State:1<br />TransitionData: None|
|4|Label: **Provisioning**<br />State:0<br />TransitionData: None|
|5|Label: **ProvisioningFailed**<br />State:1<br />TransitionData: None|

### <a name="BKMK_statuserrormessage"></a> statuserrormessage

|Property|Value|
|---|---|
|Description|**Flow Machine Image Version Error Message.**|
|DisplayName|**Flow Machine Image Version Error Message.**|
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

### <a name="BKMK_SupportedScenario"></a> SupportedScenario

|Property|Value|
|---|---|
|Description|**The Flow machine image version supported scenario.**|
|DisplayName|**SupportedScenario**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`supportedscenario`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`flowmachineimageversion_supportedscenario`|

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
|Description|**The version of the image**|
|DisplayName|**Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`version`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [generalizationlogs](#BKMK_generalizationlogs)
- [generalizationlogs_Name](#BKMK_generalizationlogs_Name)
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

### <a name="BKMK_generalizationlogs"></a> generalizationlogs

|Property|Value|
|---|---|
|Description|**File containing logs of image generalization process to help debug provisioning errors.**|
|DisplayName|**Generalization logs**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`generalizationlogs`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_generalizationlogs_Name"></a> generalizationlogs_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`generalizationlogs_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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

- [business_unit_flowmachineimageversion](#BKMK_business_unit_flowmachineimageversion)
- [FileAttachment_flowmachineimageversion_generalizationlogs](#BKMK_FileAttachment_flowmachineimageversion_generalizationlogs)
- [flowmachineimage_flowmachineimageversion](#BKMK_flowmachineimage_flowmachineimageversion)
- [flowmachineimageversion_flowmachine](#BKMK_flowmachineimageversion_flowmachine)
- [lk_flowmachineimageversion_createdby](#BKMK_lk_flowmachineimageversion_createdby)
- [lk_flowmachineimageversion_createdonbehalfby](#BKMK_lk_flowmachineimageversion_createdonbehalfby)
- [lk_flowmachineimageversion_modifiedby](#BKMK_lk_flowmachineimageversion_modifiedby)
- [lk_flowmachineimageversion_modifiedonbehalfby](#BKMK_lk_flowmachineimageversion_modifiedonbehalfby)
- [owner_flowmachineimageversion](#BKMK_owner_flowmachineimageversion)
- [team_flowmachineimageversion](#BKMK_team_flowmachineimageversion)
- [user_flowmachineimageversion](#BKMK_user_flowmachineimageversion)

### <a name="BKMK_business_unit_flowmachineimageversion"></a> business_unit_flowmachineimageversion

One-To-Many Relationship: [businessunit business_unit_flowmachineimageversion](businessunit.md#BKMK_business_unit_flowmachineimageversion)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_flowmachineimageversion_generalizationlogs"></a> FileAttachment_flowmachineimageversion_generalizationlogs

One-To-Many Relationship: [fileattachment FileAttachment_flowmachineimageversion_generalizationlogs](fileattachment.md#BKMK_FileAttachment_flowmachineimageversion_generalizationlogs)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`generalizationlogs`|
|ReferencingEntityNavigationPropertyName|`generalizationlogs`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowmachineimage_flowmachineimageversion"></a> flowmachineimage_flowmachineimageversion

One-To-Many Relationship: [flowmachineimage flowmachineimage_flowmachineimageversion](flowmachineimage.md#BKMK_flowmachineimage_flowmachineimageversion)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachineimage`|
|ReferencedAttribute|`flowmachineimageid`|
|ReferencingAttribute|`flowmachineimage`|
|ReferencingEntityNavigationPropertyName|`flowmachineimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_flowmachineimageversion_flowmachine"></a> flowmachineimageversion_flowmachine

One-To-Many Relationship: [flowmachine flowmachineimageversion_flowmachine](flowmachine.md#BKMK_flowmachineimageversion_flowmachine)

|Property|Value|
|---|---|
|ReferencedEntity|`flowmachine`|
|ReferencedAttribute|`flowmachineid`|
|ReferencingAttribute|`sourcemachineid`|
|ReferencingEntityNavigationPropertyName|`sourcemachineid_flowmachine`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachineimageversion_createdby"></a> lk_flowmachineimageversion_createdby

One-To-Many Relationship: [systemuser lk_flowmachineimageversion_createdby](systemuser.md#BKMK_lk_flowmachineimageversion_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachineimageversion_createdonbehalfby"></a> lk_flowmachineimageversion_createdonbehalfby

One-To-Many Relationship: [systemuser lk_flowmachineimageversion_createdonbehalfby](systemuser.md#BKMK_lk_flowmachineimageversion_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachineimageversion_modifiedby"></a> lk_flowmachineimageversion_modifiedby

One-To-Many Relationship: [systemuser lk_flowmachineimageversion_modifiedby](systemuser.md#BKMK_lk_flowmachineimageversion_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_flowmachineimageversion_modifiedonbehalfby"></a> lk_flowmachineimageversion_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_flowmachineimageversion_modifiedonbehalfby](systemuser.md#BKMK_lk_flowmachineimageversion_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_flowmachineimageversion"></a> owner_flowmachineimageversion

One-To-Many Relationship: [owner owner_flowmachineimageversion](owner.md#BKMK_owner_flowmachineimageversion)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_flowmachineimageversion"></a> team_flowmachineimageversion

One-To-Many Relationship: [team team_flowmachineimageversion](team.md#BKMK_team_flowmachineimageversion)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_flowmachineimageversion"></a> user_flowmachineimageversion

One-To-Many Relationship: [systemuser user_flowmachineimageversion](systemuser.md#BKMK_user_flowmachineimageversion)

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

- [flowmachine_flowmachineimageversion](#BKMK_flowmachine_flowmachineimageversion)
- [flowmachineimageversion_AsyncOperations](#BKMK_flowmachineimageversion_AsyncOperations)
- [flowmachineimageversion_BulkDeleteFailures](#BKMK_flowmachineimageversion_BulkDeleteFailures)
- [flowmachineimageversion_DuplicateBaseRecord](#BKMK_flowmachineimageversion_DuplicateBaseRecord)
- [flowmachineimageversion_DuplicateMatchingRecord](#BKMK_flowmachineimageversion_DuplicateMatchingRecord)
- [flowmachineimageversion_FileAttachments](#BKMK_flowmachineimageversion_FileAttachments)
- [flowmachineimageversion_MailboxTrackingFolders](#BKMK_flowmachineimageversion_MailboxTrackingFolders)
- [flowmachineimageversion_PrincipalObjectAttributeAccesses](#BKMK_flowmachineimageversion_PrincipalObjectAttributeAccesses)
- [flowmachineimageversion_ProcessSession](#BKMK_flowmachineimageversion_ProcessSession)
- [flowmachineimageversion_SyncErrors](#BKMK_flowmachineimageversion_SyncErrors)

### <a name="BKMK_flowmachine_flowmachineimageversion"></a> flowmachine_flowmachineimageversion

Many-To-One Relationship: [flowmachine flowmachine_flowmachineimageversion](flowmachine.md#BKMK_flowmachine_flowmachineimageversion)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachine`|
|ReferencingAttribute|`flowmachineimageversionid`|
|ReferencedEntityNavigationPropertyName|`flowmachine_flowmachineimageversion`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachineimageversion_AsyncOperations"></a> flowmachineimageversion_AsyncOperations

Many-To-One Relationship: [asyncoperation flowmachineimageversion_AsyncOperations](asyncoperation.md#BKMK_flowmachineimageversion_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachineimageversion_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachineimageversion_BulkDeleteFailures"></a> flowmachineimageversion_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure flowmachineimageversion_BulkDeleteFailures](bulkdeletefailure.md#BKMK_flowmachineimageversion_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachineimageversion_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachineimageversion_DuplicateBaseRecord"></a> flowmachineimageversion_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord flowmachineimageversion_DuplicateBaseRecord](duplicaterecord.md#BKMK_flowmachineimageversion_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`flowmachineimageversion_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachineimageversion_DuplicateMatchingRecord"></a> flowmachineimageversion_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord flowmachineimageversion_DuplicateMatchingRecord](duplicaterecord.md#BKMK_flowmachineimageversion_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`flowmachineimageversion_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachineimageversion_FileAttachments"></a> flowmachineimageversion_FileAttachments

Many-To-One Relationship: [fileattachment flowmachineimageversion_FileAttachments](fileattachment.md#BKMK_flowmachineimageversion_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`flowmachineimageversion_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachineimageversion_MailboxTrackingFolders"></a> flowmachineimageversion_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder flowmachineimageversion_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_flowmachineimageversion_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachineimageversion_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachineimageversion_PrincipalObjectAttributeAccesses"></a> flowmachineimageversion_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess flowmachineimageversion_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_flowmachineimageversion_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`flowmachineimageversion_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachineimageversion_ProcessSession"></a> flowmachineimageversion_ProcessSession

Many-To-One Relationship: [processsession flowmachineimageversion_ProcessSession](processsession.md#BKMK_flowmachineimageversion_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachineimageversion_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowmachineimageversion_SyncErrors"></a> flowmachineimageversion_SyncErrors

Many-To-One Relationship: [syncerror flowmachineimageversion_SyncErrors](syncerror.md#BKMK_flowmachineimageversion_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`flowmachineimageversion_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.flowmachineimageversion?displayProperty=fullName>
