---
title: "Customer Voice satisfaction metric (msfp_satisfactionmetric) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Customer Voice satisfaction metric (msfp_satisfactionmetric) table/entity with Microsoft Dataverse."
ms.date: 01/06/2025
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Customer Voice satisfaction metric (msfp_satisfactionmetric) table/entity reference

Satisfaction metric defined for a project.

## Messages

The following table lists the messages for the Customer Voice satisfaction metric (msfp_satisfactionmetric) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msfp_satisfactionmetrics(*msfp_satisfactionmetricid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Create`<br />Event: True |`POST` /msfp_satisfactionmetrics<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msfp_satisfactionmetrics(*msfp_satisfactionmetricid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msfp_satisfactionmetrics(*msfp_satisfactionmetricid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msfp_satisfactionmetrics<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msfp_satisfactionmetrics(*msfp_satisfactionmetricid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msfp_satisfactionmetrics(*msfp_satisfactionmetricid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msfp_satisfactionmetrics(*msfp_satisfactionmetricid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Customer Voice satisfaction metric (msfp_satisfactionmetric) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Customer Voice satisfaction metric (msfp_satisfactionmetric) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Customer Voice satisfaction metric** |
| **DisplayCollectionName** | **Customer Voice satisfaction metrics** |
| **SchemaName** | `msfp_satisfactionmetric` |
| **CollectionSchemaName** | `msfp_satisfactionmetrics` |
| **EntitySetName** | `msfp_satisfactionmetrics`|
| **LogicalName** | `msfp_satisfactionmetric` |
| **LogicalCollectionName** | `msfp_satisfactionmetrics` |
| **PrimaryIdAttribute** | `msfp_satisfactionmetricid` |
| **PrimaryNameAttribute** |`msfp_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msfp_description](#BKMK_msfp_description)
- [msfp_historicalcomputedvalue](#BKMK_msfp_historicalcomputedvalue)
- [msfp_issystemkpi](#BKMK_msfp_issystemkpi)
- [msfp_lastcomputedon](#BKMK_msfp_lastcomputedon)
- [msfp_lastcomputedvalue](#BKMK_msfp_lastcomputedvalue)
- [msfp_maximumvalue](#BKMK_msfp_maximumvalue)
- [msfp_minimumvalue](#BKMK_msfp_minimumvalue)
- [msfp_name](#BKMK_msfp_name)
- [msfp_project](#BKMK_msfp_project)
- [msfp_questions](#BKMK_msfp_questions)
- [msfp_satisfactionmetricId](#BKMK_msfp_satisfactionmetricId)
- [msfp_status](#BKMK_msfp_status)
- [msfp_threshold](#BKMK_msfp_threshold)
- [msfp_type](#BKMK_msfp_type)
- [msfp_versionnumber](#BKMK_msfp_versionnumber)
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

### <a name="BKMK_msfp_description"></a> msfp_description

|Property|Value|
|---|---|
|Description|**Description of the satisfaction metric.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000000|

### <a name="BKMK_msfp_historicalcomputedvalue"></a> msfp_historicalcomputedvalue

|Property|Value|
|---|---|
|Description|**Historical computed value of the satisfaction metric.**|
|DisplayName|**Historical computed value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_historicalcomputedvalue`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000000|

### <a name="BKMK_msfp_issystemkpi"></a> msfp_issystemkpi

|Property|Value|
|---|---|
|Description|**Indicates if the satisfaction metric is system defined or user defined.**|
|DisplayName|**Is system KPI**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_issystemkpi`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msfp_satisfactionmetric_msfp_issystemkpi`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_msfp_lastcomputedon"></a> msfp_lastcomputedon

|Property|Value|
|---|---|
|Description|**Date and time when the satisfaction metric was last computed.**|
|DisplayName|**Last computed on**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_lastcomputedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msfp_lastcomputedvalue"></a> msfp_lastcomputedvalue

|Property|Value|
|---|---|
|Description|**Last computed value of the satisfaction metric.**|
|DisplayName|**Last Computed Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_lastcomputedvalue`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msfp_maximumvalue"></a> msfp_maximumvalue

|Property|Value|
|---|---|
|Description|**Maximum value of the satisfaction metric.**|
|DisplayName|**Maximum value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_maximumvalue`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msfp_minimumvalue"></a> msfp_minimumvalue

|Property|Value|
|---|---|
|Description|**Minimum value of the satisfaction metric.**|
|DisplayName|**Minimum value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_minimumvalue`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msfp_name"></a> msfp_name

|Property|Value|
|---|---|
|Description|**Name of the satisfaction metric.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|550|

### <a name="BKMK_msfp_project"></a> msfp_project

|Property|Value|
|---|---|
|Description|**Project to which the satisfaction metric belongs.**|
|DisplayName|**Project**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_project`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|msfp_project|

### <a name="BKMK_msfp_questions"></a> msfp_questions

|Property|Value|
|---|---|
|Description|**Questions on which the satisfaction metric is calculated.**|
|DisplayName|**Questions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_questions`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50000|

### <a name="BKMK_msfp_satisfactionmetricId"></a> msfp_satisfactionmetricId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Customer Voice satisfaction metric**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_satisfactionmetricid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msfp_status"></a> msfp_status

|Property|Value|
|---|---|
|Description|**Status of the satisfaction metric.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_status`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|647390000|
|GlobalChoiceName|`msfp_satisfactionmetric_msfp_status`|

#### msfp_status Choices/Options

|Value|Label|
|---|---|
|647390000|**Active**|
|647390001|**InActive**|

### <a name="BKMK_msfp_threshold"></a> msfp_threshold

|Property|Value|
|---|---|
|Description|**Threshold value of the satisfaction metric.**|
|DisplayName|**Threshold**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_threshold`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msfp_type"></a> msfp_type

|Property|Value|
|---|---|
|Description|**Type of the satisfaction metric.**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_type`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_versionnumber"></a> msfp_versionnumber

|Property|Value|
|---|---|
|Description|**Version number of the satisfaction metric.**|
|DisplayName|**Version number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_versionnumber`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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
|Description|**User who owns the satisfaction metric.**|
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
|Description|**Status of the Satisfaction metric**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msfp_satisfactionmetric_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Satisfaction metric**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msfp_satisfactionmetric_statuscode`|

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

- [business_unit_msfp_satisfactionmetric](#BKMK_business_unit_msfp_satisfactionmetric)
- [lk_msfp_satisfactionmetric_createdby](#BKMK_lk_msfp_satisfactionmetric_createdby)
- [lk_msfp_satisfactionmetric_createdonbehalfby](#BKMK_lk_msfp_satisfactionmetric_createdonbehalfby)
- [lk_msfp_satisfactionmetric_modifiedby](#BKMK_lk_msfp_satisfactionmetric_modifiedby)
- [lk_msfp_satisfactionmetric_modifiedonbehalfby](#BKMK_lk_msfp_satisfactionmetric_modifiedonbehalfby)
- [msfp_msfp_project_msfp_satisfactionmetric_project](#BKMK_msfp_msfp_project_msfp_satisfactionmetric_project)
- [owner_msfp_satisfactionmetric](#BKMK_owner_msfp_satisfactionmetric)
- [team_msfp_satisfactionmetric](#BKMK_team_msfp_satisfactionmetric)
- [user_msfp_satisfactionmetric](#BKMK_user_msfp_satisfactionmetric)

### <a name="BKMK_business_unit_msfp_satisfactionmetric"></a> business_unit_msfp_satisfactionmetric

One-To-Many Relationship: [businessunit business_unit_msfp_satisfactionmetric](businessunit.md#BKMK_business_unit_msfp_satisfactionmetric)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_satisfactionmetric_createdby"></a> lk_msfp_satisfactionmetric_createdby

One-To-Many Relationship: [systemuser lk_msfp_satisfactionmetric_createdby](systemuser.md#BKMK_lk_msfp_satisfactionmetric_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_satisfactionmetric_createdonbehalfby"></a> lk_msfp_satisfactionmetric_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msfp_satisfactionmetric_createdonbehalfby](systemuser.md#BKMK_lk_msfp_satisfactionmetric_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_satisfactionmetric_modifiedby"></a> lk_msfp_satisfactionmetric_modifiedby

One-To-Many Relationship: [systemuser lk_msfp_satisfactionmetric_modifiedby](systemuser.md#BKMK_lk_msfp_satisfactionmetric_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_satisfactionmetric_modifiedonbehalfby"></a> lk_msfp_satisfactionmetric_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msfp_satisfactionmetric_modifiedonbehalfby](systemuser.md#BKMK_lk_msfp_satisfactionmetric_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_msfp_project_msfp_satisfactionmetric_project"></a> msfp_msfp_project_msfp_satisfactionmetric_project

One-To-Many Relationship: [msfp_project msfp_msfp_project_msfp_satisfactionmetric_project](msfp_project.md#BKMK_msfp_msfp_project_msfp_satisfactionmetric_project)

|Property|Value|
|---|---|
|ReferencedEntity|`msfp_project`|
|ReferencedAttribute|`msfp_projectid`|
|ReferencingAttribute|`msfp_project`|
|ReferencingEntityNavigationPropertyName|`msfp_project`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msfp_satisfactionmetric"></a> owner_msfp_satisfactionmetric

One-To-Many Relationship: [owner owner_msfp_satisfactionmetric](owner.md#BKMK_owner_msfp_satisfactionmetric)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msfp_satisfactionmetric"></a> team_msfp_satisfactionmetric

One-To-Many Relationship: [team team_msfp_satisfactionmetric](team.md#BKMK_team_msfp_satisfactionmetric)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msfp_satisfactionmetric"></a> user_msfp_satisfactionmetric

One-To-Many Relationship: [systemuser user_msfp_satisfactionmetric](systemuser.md#BKMK_user_msfp_satisfactionmetric)

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

- [msfp_msfp_satisfactionmetric_msfp_alert](#BKMK_msfp_msfp_satisfactionmetric_msfp_alert)
- [msfp_msfp_satisfactionmetric_msfp_alertrule](#BKMK_msfp_msfp_satisfactionmetric_msfp_alertrule)
- [msfp_satisfactionmetric_AsyncOperations](#BKMK_msfp_satisfactionmetric_AsyncOperations)
- [msfp_satisfactionmetric_BulkDeleteFailures](#BKMK_msfp_satisfactionmetric_BulkDeleteFailures)
- [msfp_satisfactionmetric_MailboxTrackingFolders](#BKMK_msfp_satisfactionmetric_MailboxTrackingFolders)
- [msfp_satisfactionmetric_PrincipalObjectAttributeAccesses](#BKMK_msfp_satisfactionmetric_PrincipalObjectAttributeAccesses)
- [msfp_satisfactionmetric_ProcessSession](#BKMK_msfp_satisfactionmetric_ProcessSession)
- [msfp_satisfactionmetric_SyncErrors](#BKMK_msfp_satisfactionmetric_SyncErrors)

### <a name="BKMK_msfp_msfp_satisfactionmetric_msfp_alert"></a> msfp_msfp_satisfactionmetric_msfp_alert

Many-To-One Relationship: [msfp_alert msfp_msfp_satisfactionmetric_msfp_alert](msfp_alert.md#BKMK_msfp_msfp_satisfactionmetric_msfp_alert)

|Property|Value|
|---|---|
|ReferencingEntity|`msfp_alert`|
|ReferencingAttribute|`msfp_satisfactionmetric`|
|ReferencedEntityNavigationPropertyName|`msfp_msfp_satisfactionmetric_msfp_alert`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_msfp_satisfactionmetric_msfp_alertrule"></a> msfp_msfp_satisfactionmetric_msfp_alertrule

Many-To-One Relationship: [msfp_alertrule msfp_msfp_satisfactionmetric_msfp_alertrule](msfp_alertrule.md#BKMK_msfp_msfp_satisfactionmetric_msfp_alertrule)

|Property|Value|
|---|---|
|ReferencingEntity|`msfp_alertrule`|
|ReferencingAttribute|`msfp_satisfactionmetric`|
|ReferencedEntityNavigationPropertyName|`msfp_msfp_satisfactionmetric_msfp_alertrule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_satisfactionmetric_AsyncOperations"></a> msfp_satisfactionmetric_AsyncOperations

Many-To-One Relationship: [asyncoperation msfp_satisfactionmetric_AsyncOperations](asyncoperation.md#BKMK_msfp_satisfactionmetric_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_satisfactionmetric_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_satisfactionmetric_BulkDeleteFailures"></a> msfp_satisfactionmetric_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msfp_satisfactionmetric_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msfp_satisfactionmetric_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_satisfactionmetric_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_satisfactionmetric_MailboxTrackingFolders"></a> msfp_satisfactionmetric_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msfp_satisfactionmetric_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msfp_satisfactionmetric_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_satisfactionmetric_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_satisfactionmetric_PrincipalObjectAttributeAccesses"></a> msfp_satisfactionmetric_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msfp_satisfactionmetric_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msfp_satisfactionmetric_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msfp_satisfactionmetric_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_satisfactionmetric_ProcessSession"></a> msfp_satisfactionmetric_ProcessSession

Many-To-One Relationship: [processsession msfp_satisfactionmetric_ProcessSession](processsession.md#BKMK_msfp_satisfactionmetric_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_satisfactionmetric_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_satisfactionmetric_SyncErrors"></a> msfp_satisfactionmetric_SyncErrors

Many-To-One Relationship: [syncerror msfp_satisfactionmetric_SyncErrors](syncerror.md#BKMK_msfp_satisfactionmetric_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_satisfactionmetric_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

