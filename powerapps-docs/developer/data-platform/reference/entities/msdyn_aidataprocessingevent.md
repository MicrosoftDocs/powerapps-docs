---
title: "Data Processing Event (msdyn_AIDataProcessingEvent) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Data Processing Event (msdyn_AIDataProcessingEvent) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Data Processing Event (msdyn_AIDataProcessingEvent) table/entity reference (Microsoft Dataverse)

Events that are triggered by Data Processing.

## Messages

The following table lists the messages for the Data Processing Event (msdyn_AIDataProcessingEvent) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_aidataprocessingevents(*msdyn_aidataprocessingeventid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_aidataprocessingevents<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_aidataprocessingevents(*msdyn_aidataprocessingeventid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_aidataprocessingevents(*msdyn_aidataprocessingeventid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_aidataprocessingevents<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_aidataprocessingevents(*msdyn_aidataprocessingeventid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_aidataprocessingevents(*msdyn_aidataprocessingeventid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_aidataprocessingevents(*msdyn_aidataprocessingeventid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Data Processing Event (msdyn_AIDataProcessingEvent) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Data Processing Event** |
| **DisplayCollectionName** | **Data Processing Events** |
| **SchemaName** | `msdyn_AIDataProcessingEvent` |
| **CollectionSchemaName** | `msdyn_AIDataProcessingEvents` |
| **EntitySetName** | `msdyn_aidataprocessingevents`|
| **LogicalName** | `msdyn_aidataprocessingevent` |
| **LogicalCollectionName** | `msdyn_aidataprocessingevents` |
| **PrimaryIdAttribute** | `msdyn_aidataprocessingeventid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_AIDataProcessingEventId](#BKMK_msdyn_AIDataProcessingEventId)
- [msdyn_CustomData](#BKMK_msdyn_CustomData)
- [msdyn_InputDataFormat](#BKMK_msdyn_InputDataFormat)
- [msdyn_Name](#BKMK_msdyn_Name)
- [msdyn_ProcessedData](#BKMK_msdyn_ProcessedData)
- [msdyn_ProcessingStatus](#BKMK_msdyn_ProcessingStatus)
- [msdyn_ProcessorName](#BKMK_msdyn_ProcessorName)
- [msdyn_ProcessorType](#BKMK_msdyn_ProcessorType)
- [msdyn_ReceivedDate](#BKMK_msdyn_ReceivedDate)
- [msdyn_UpdatedDate](#BKMK_msdyn_UpdatedDate)
- [msdyn_ValidationResult](#BKMK_msdyn_ValidationResult)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

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

### <a name="BKMK_msdyn_AIDataProcessingEventId"></a> msdyn_AIDataProcessingEventId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Data Processing Event**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_aidataprocessingeventid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_CustomData"></a> msdyn_CustomData

|Property|Value|
|---|---|
|Description|**Free area. Used for instructions to a reviewer, or JSON for cases where maker needs more customized info.**|
|DisplayName|**Custom Data**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_customdata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_msdyn_InputDataFormat"></a> msdyn_InputDataFormat

|Property|Value|
|---|---|
|Description|**Format of Input Data (JSON, XML, etc)**|
|DisplayName|**Input Data Format**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_inputdataformat`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_Name"></a> msdyn_Name

|Property|Value|
|---|---|
|Description|**Name of data source (e.g. file name on Document Processing)**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|850|

### <a name="BKMK_msdyn_ProcessedData"></a> msdyn_ProcessedData

|Property|Value|
|---|---|
|Description|**Output of AI models for this data. (e.g. Extracted data from Documents in Doc. Processing)**|
|DisplayName|**Processed Data**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_processeddata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_ProcessingStatus"></a> msdyn_ProcessingStatus

|Property|Value|
|---|---|
|Description|**Current processing status of data.**|
|DisplayName|**Processing Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_processingstatus`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|375150000|
|GlobalChoiceName|`msdyn_aidataprocessingevent_msdyn_processingstatus`|

#### msdyn_ProcessingStatus Choices/Options

|Value|Label|
|---|---|
|375150000|**New**|
|375150001|**Processed**|
|375150002|**Processing Failed**|
|375150003|**Validated**|
|375150004|**Manual Review**|
|375150005|**Exported**|
|375150006|**Exporting Failed**|
|375150007|**Rejected**|

### <a name="BKMK_msdyn_ProcessorName"></a> msdyn_ProcessorName

|Property|Value|
|---|---|
|Description|**Agent or Model processing this data.**|
|DisplayName|**Processor Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_processorname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_ProcessorType"></a> msdyn_ProcessorType

|Property|Value|
|---|---|
|Description|**Type of processor (e.g. bot or workflow)**|
|DisplayName|**Processor Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_processortype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_ReceivedDate"></a> msdyn_ReceivedDate

|Property|Value|
|---|---|
|Description|**Date input data was received.**|
|DisplayName|**Received Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_receiveddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_UpdatedDate"></a> msdyn_UpdatedDate

|Property|Value|
|---|---|
|Description|**Date the last update of Processing Status happened.**|
|DisplayName|**Updated Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_updateddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_ValidationResult"></a> msdyn_ValidationResult

|Property|Value|
|---|---|
|Description|**Result of validation process when this data is handled by an agent or AI model.**|
|DisplayName|**Validation Result**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_validationresult`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

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
|Description|**Status of the DataProcessingEvent**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aidataprocessingevent_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the DataProcessingEvent**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aidataprocessingevent_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

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
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [msdyn_InputData](#BKMK_msdyn_InputData)
- [msdyn_InputData_Name](#BKMK_msdyn_InputData_Name)
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

### <a name="BKMK_msdyn_InputData"></a> msdyn_InputData

|Property|Value|
|---|---|
|Description|**Input data of the process (e.g. file content for Document Processing).**|
|DisplayName|**Input Data**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_inputdata`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_InputData_Name"></a> msdyn_InputData_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_inputdata_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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
|RequiredLevel|SystemRequired|
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

- [business_unit_msdyn_aidataprocessingevent](#BKMK_business_unit_msdyn_aidataprocessingevent)
- [FileAttachment_msdyn_AIDataProcessingEvent_msdyn_InputData](#BKMK_FileAttachment_msdyn_AIDataProcessingEvent_msdyn_InputData)
- [lk_msdyn_aidataprocessingevent_createdby](#BKMK_lk_msdyn_aidataprocessingevent_createdby)
- [lk_msdyn_aidataprocessingevent_createdonbehalfby](#BKMK_lk_msdyn_aidataprocessingevent_createdonbehalfby)
- [lk_msdyn_aidataprocessingevent_modifiedby](#BKMK_lk_msdyn_aidataprocessingevent_modifiedby)
- [lk_msdyn_aidataprocessingevent_modifiedonbehalfby](#BKMK_lk_msdyn_aidataprocessingevent_modifiedonbehalfby)
- [owner_msdyn_aidataprocessingevent](#BKMK_owner_msdyn_aidataprocessingevent)
- [team_msdyn_aidataprocessingevent](#BKMK_team_msdyn_aidataprocessingevent)
- [user_msdyn_aidataprocessingevent](#BKMK_user_msdyn_aidataprocessingevent)

### <a name="BKMK_business_unit_msdyn_aidataprocessingevent"></a> business_unit_msdyn_aidataprocessingevent

One-To-Many Relationship: [businessunit business_unit_msdyn_aidataprocessingevent](businessunit.md#BKMK_business_unit_msdyn_aidataprocessingevent)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_AIDataProcessingEvent_msdyn_InputData"></a> FileAttachment_msdyn_AIDataProcessingEvent_msdyn_InputData

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_AIDataProcessingEvent_msdyn_InputData](fileattachment.md#BKMK_FileAttachment_msdyn_AIDataProcessingEvent_msdyn_InputData)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_inputdata`|
|ReferencingEntityNavigationPropertyName|`msdyn_inputdata`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aidataprocessingevent_createdby"></a> lk_msdyn_aidataprocessingevent_createdby

One-To-Many Relationship: [systemuser lk_msdyn_aidataprocessingevent_createdby](systemuser.md#BKMK_lk_msdyn_aidataprocessingevent_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aidataprocessingevent_createdonbehalfby"></a> lk_msdyn_aidataprocessingevent_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aidataprocessingevent_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_aidataprocessingevent_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aidataprocessingevent_modifiedby"></a> lk_msdyn_aidataprocessingevent_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_aidataprocessingevent_modifiedby](systemuser.md#BKMK_lk_msdyn_aidataprocessingevent_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aidataprocessingevent_modifiedonbehalfby"></a> lk_msdyn_aidataprocessingevent_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aidataprocessingevent_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_aidataprocessingevent_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_aidataprocessingevent"></a> owner_msdyn_aidataprocessingevent

One-To-Many Relationship: [owner owner_msdyn_aidataprocessingevent](owner.md#BKMK_owner_msdyn_aidataprocessingevent)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_aidataprocessingevent"></a> team_msdyn_aidataprocessingevent

One-To-Many Relationship: [team team_msdyn_aidataprocessingevent](team.md#BKMK_team_msdyn_aidataprocessingevent)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_aidataprocessingevent"></a> user_msdyn_aidataprocessingevent

One-To-Many Relationship: [systemuser user_msdyn_aidataprocessingevent](systemuser.md#BKMK_user_msdyn_aidataprocessingevent)

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

- [msdyn_aidataprocessingevent_AsyncOperations](#BKMK_msdyn_aidataprocessingevent_AsyncOperations)
- [msdyn_aidataprocessingevent_BulkDeleteFailures](#BKMK_msdyn_aidataprocessingevent_BulkDeleteFailures)
- [msdyn_aidataprocessingevent_FileAttachments](#BKMK_msdyn_aidataprocessingevent_FileAttachments)
- [msdyn_aidataprocessingevent_MailboxTrackingFolders](#BKMK_msdyn_aidataprocessingevent_MailboxTrackingFolders)
- [msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses)
- [msdyn_aidataprocessingevent_ProcessSession](#BKMK_msdyn_aidataprocessingevent_ProcessSession)
- [msdyn_aidataprocessingevent_SyncErrors](#BKMK_msdyn_aidataprocessingevent_SyncErrors)

### <a name="BKMK_msdyn_aidataprocessingevent_AsyncOperations"></a> msdyn_aidataprocessingevent_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_aidataprocessingevent_AsyncOperations](asyncoperation.md#BKMK_msdyn_aidataprocessingevent_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aidataprocessingevent_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aidataprocessingevent_BulkDeleteFailures"></a> msdyn_aidataprocessingevent_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_aidataprocessingevent_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_aidataprocessingevent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aidataprocessingevent_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aidataprocessingevent_FileAttachments"></a> msdyn_aidataprocessingevent_FileAttachments

Many-To-One Relationship: [fileattachment msdyn_aidataprocessingevent_FileAttachments](fileattachment.md#BKMK_msdyn_aidataprocessingevent_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aidataprocessingevent_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aidataprocessingevent_MailboxTrackingFolders"></a> msdyn_aidataprocessingevent_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_aidataprocessingevent_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_aidataprocessingevent_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aidataprocessingevent_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses"></a> msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aidataprocessingevent_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aidataprocessingevent_ProcessSession"></a> msdyn_aidataprocessingevent_ProcessSession

Many-To-One Relationship: [processsession msdyn_aidataprocessingevent_ProcessSession](processsession.md#BKMK_msdyn_aidataprocessingevent_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aidataprocessingevent_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aidataprocessingevent_SyncErrors"></a> msdyn_aidataprocessingevent_SyncErrors

Many-To-One Relationship: [syncerror msdyn_aidataprocessingevent_SyncErrors](syncerror.md#BKMK_msdyn_aidataprocessingevent_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aidataprocessingevent_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_aidataprocessingevent?displayProperty=fullName>
