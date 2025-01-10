---
title: "Customer Voice file response (msfp_fileresponse) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Customer Voice file response (msfp_fileresponse) table/entity with Microsoft Dataverse."
ms.date: 01/06/2025
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Customer Voice file response (msfp_fileresponse) table/entity reference

Response to a file upload question.

## Messages

The following table lists the messages for the Customer Voice file response (msfp_fileresponse) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msfp_fileresponses(*msfp_fileresponseid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Create`<br />Event: True |`POST` /msfp_fileresponses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msfp_fileresponses(*msfp_fileresponseid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msfp_fileresponses(*msfp_fileresponseid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msfp_fileresponses<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msfp_fileresponses(*msfp_fileresponseid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msfp_fileresponses(*msfp_fileresponseid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msfp_fileresponses(*msfp_fileresponseid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Customer Voice file response (msfp_fileresponse) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Customer Voice file response (msfp_fileresponse) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Customer Voice file response** |
| **DisplayCollectionName** | **Customer Voice file responses** |
| **SchemaName** | `msfp_fileresponse` |
| **CollectionSchemaName** | `msfp_fileresponses` |
| **EntitySetName** | `msfp_fileresponses`|
| **LogicalName** | `msfp_fileresponse` |
| **LogicalCollectionName** | `msfp_fileresponses` |
| **PrimaryIdAttribute** | `msfp_fileresponseid` |
| **PrimaryNameAttribute** |`msfp_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msfp_fileresponseId](#BKMK_msfp_fileresponseId)
- [msfp_name](#BKMK_msfp_name)
- [msfp_otherproperties](#BKMK_msfp_otherproperties)
- [msfp_question](#BKMK_msfp_question)
- [msfp_questionresponse](#BKMK_msfp_questionresponse)
- [msfp_sourcequestionidentifier](#BKMK_msfp_sourcequestionidentifier)
- [msfp_sourcesurveyidentifier](#BKMK_msfp_sourcesurveyidentifier)
- [msfp_survey](#BKMK_msfp_survey)
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

### <a name="BKMK_msfp_fileresponseId"></a> msfp_fileresponseId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Customer Voice file response**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_fileresponseid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msfp_name"></a> msfp_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
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
|MaxLength|100|

### <a name="BKMK_msfp_otherproperties"></a> msfp_otherproperties

|Property|Value|
|---|---|
|Description|**Stores other properties in JSON format.**|
|DisplayName|**Other properties**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_otherproperties`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msfp_question"></a> msfp_question

|Property|Value|
|---|---|
|Description|**(Deprecated) Question associated with the question response.**|
|DisplayName|**(Deprecated) Question**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_question`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msfp_question|

### <a name="BKMK_msfp_questionresponse"></a> msfp_questionresponse

|Property|Value|
|---|---|
|Description|**Question Response with which the File Response is associated.**|
|DisplayName|**Question Response**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_questionresponse`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msfp_questionresponse|

### <a name="BKMK_msfp_sourcequestionidentifier"></a> msfp_sourcequestionidentifier

|Property|Value|
|---|---|
|Description|**Unique identifier for the question in the source application.**|
|DisplayName|**Source question identifier**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_sourcequestionidentifier`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msfp_sourcesurveyidentifier"></a> msfp_sourcesurveyidentifier

|Property|Value|
|---|---|
|Description|**Unique identifier for the survey in the source application.**|
|DisplayName|**Source survey identifier**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_sourcesurveyidentifier`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msfp_survey"></a> msfp_survey

|Property|Value|
|---|---|
|Description|**(Deprecated) Unique identifier of the survey to which the question belongs.**|
|DisplayName|**(Deprecated) Survey**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_survey`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msfp_survey|

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
|Description|**Status of the Customer Voice file response**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msfp_fileresponse_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Customer Voice file response**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msfp_fileresponse_statuscode`|

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
- [msfp_file1](#BKMK_msfp_file1)
- [msfp_file1_Name](#BKMK_msfp_file1_Name)
- [msfp_file10](#BKMK_msfp_file10)
- [msfp_file10_Name](#BKMK_msfp_file10_Name)
- [msfp_file2](#BKMK_msfp_file2)
- [msfp_file2_Name](#BKMK_msfp_file2_Name)
- [msfp_file3](#BKMK_msfp_file3)
- [msfp_file3_Name](#BKMK_msfp_file3_Name)
- [msfp_file4](#BKMK_msfp_file4)
- [msfp_file4_Name](#BKMK_msfp_file4_Name)
- [msfp_file5](#BKMK_msfp_file5)
- [msfp_file5_Name](#BKMK_msfp_file5_Name)
- [msfp_file6](#BKMK_msfp_file6)
- [msfp_file6_Name](#BKMK_msfp_file6_Name)
- [msfp_file7](#BKMK_msfp_file7)
- [msfp_file7_Name](#BKMK_msfp_file7_Name)
- [msfp_file8](#BKMK_msfp_file8)
- [msfp_file8_Name](#BKMK_msfp_file8_Name)
- [msfp_file9](#BKMK_msfp_file9)
- [msfp_file9_Name](#BKMK_msfp_file9_Name)
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

### <a name="BKMK_msfp_file1"></a> msfp_file1

|Property|Value|
|---|---|
|Description|**First uploaded file.**|
|DisplayName|**File 1**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_file1`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msfp_file1_Name"></a> msfp_file1_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_file1_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_file10"></a> msfp_file10

|Property|Value|
|---|---|
|Description|**Tenth uploaded file.**|
|DisplayName|**File 10**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_file10`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msfp_file10_Name"></a> msfp_file10_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_file10_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_file2"></a> msfp_file2

|Property|Value|
|---|---|
|Description|**Second uploaded file.**|
|DisplayName|**File 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_file2`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msfp_file2_Name"></a> msfp_file2_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_file2_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_file3"></a> msfp_file3

|Property|Value|
|---|---|
|Description|**Third uploaded file.**|
|DisplayName|**File 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_file3`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msfp_file3_Name"></a> msfp_file3_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_file3_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_file4"></a> msfp_file4

|Property|Value|
|---|---|
|Description|**Fourth uploaded file.**|
|DisplayName|**File 4**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_file4`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msfp_file4_Name"></a> msfp_file4_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_file4_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_file5"></a> msfp_file5

|Property|Value|
|---|---|
|Description|**Fifth uploaded file.**|
|DisplayName|**File 5**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_file5`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msfp_file5_Name"></a> msfp_file5_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_file5_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_file6"></a> msfp_file6

|Property|Value|
|---|---|
|Description|**Sixth uploaded file.**|
|DisplayName|**File 6**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_file6`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msfp_file6_Name"></a> msfp_file6_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_file6_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_file7"></a> msfp_file7

|Property|Value|
|---|---|
|Description|**Seventh uploaded file.**|
|DisplayName|**File 7**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_file7`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msfp_file7_Name"></a> msfp_file7_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_file7_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_file8"></a> msfp_file8

|Property|Value|
|---|---|
|Description|**Eighth uploaded file.**|
|DisplayName|**File 8**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_file8`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msfp_file8_Name"></a> msfp_file8_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_file8_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msfp_file9"></a> msfp_file9

|Property|Value|
|---|---|
|Description|**Ninth uploaded file.**|
|DisplayName|**File 9**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msfp_file9`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msfp_file9_Name"></a> msfp_file9_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msfp_file9_name`|
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

- [business_unit_msfp_fileresponse](#BKMK_business_unit_msfp_fileresponse)
- [FileAttachment_msfp_fileresponse_msfp_file1](#BKMK_FileAttachment_msfp_fileresponse_msfp_file1)
- [FileAttachment_msfp_fileresponse_msfp_file10](#BKMK_FileAttachment_msfp_fileresponse_msfp_file10)
- [FileAttachment_msfp_fileresponse_msfp_file2](#BKMK_FileAttachment_msfp_fileresponse_msfp_file2)
- [FileAttachment_msfp_fileresponse_msfp_file3](#BKMK_FileAttachment_msfp_fileresponse_msfp_file3)
- [FileAttachment_msfp_fileresponse_msfp_file4](#BKMK_FileAttachment_msfp_fileresponse_msfp_file4)
- [FileAttachment_msfp_fileresponse_msfp_file5](#BKMK_FileAttachment_msfp_fileresponse_msfp_file5)
- [FileAttachment_msfp_fileresponse_msfp_file6](#BKMK_FileAttachment_msfp_fileresponse_msfp_file6)
- [FileAttachment_msfp_fileresponse_msfp_file7](#BKMK_FileAttachment_msfp_fileresponse_msfp_file7)
- [FileAttachment_msfp_fileresponse_msfp_file8](#BKMK_FileAttachment_msfp_fileresponse_msfp_file8)
- [FileAttachment_msfp_fileresponse_msfp_file9](#BKMK_FileAttachment_msfp_fileresponse_msfp_file9)
- [lk_msfp_fileresponse_createdby](#BKMK_lk_msfp_fileresponse_createdby)
- [lk_msfp_fileresponse_createdonbehalfby](#BKMK_lk_msfp_fileresponse_createdonbehalfby)
- [lk_msfp_fileresponse_modifiedby](#BKMK_lk_msfp_fileresponse_modifiedby)
- [lk_msfp_fileresponse_modifiedonbehalfby](#BKMK_lk_msfp_fileresponse_modifiedonbehalfby)
- [msfp_msfp_question_msfp_fileresponse_question](#BKMK_msfp_msfp_question_msfp_fileresponse_question)
- [msfp_msfp_questionresponse_msfp_fileresponse_questionresponse](#BKMK_msfp_msfp_questionresponse_msfp_fileresponse_questionresponse)
- [msfp_msfp_survey_msfp_fileresponse_survey](#BKMK_msfp_msfp_survey_msfp_fileresponse_survey)
- [owner_msfp_fileresponse](#BKMK_owner_msfp_fileresponse)
- [team_msfp_fileresponse](#BKMK_team_msfp_fileresponse)
- [user_msfp_fileresponse](#BKMK_user_msfp_fileresponse)

### <a name="BKMK_business_unit_msfp_fileresponse"></a> business_unit_msfp_fileresponse

One-To-Many Relationship: [businessunit business_unit_msfp_fileresponse](businessunit.md#BKMK_business_unit_msfp_fileresponse)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msfp_fileresponse_msfp_file1"></a> FileAttachment_msfp_fileresponse_msfp_file1

One-To-Many Relationship: [fileattachment FileAttachment_msfp_fileresponse_msfp_file1](fileattachment.md#BKMK_FileAttachment_msfp_fileresponse_msfp_file1)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msfp_file1`|
|ReferencingEntityNavigationPropertyName|`msfp_file1`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msfp_fileresponse_msfp_file10"></a> FileAttachment_msfp_fileresponse_msfp_file10

One-To-Many Relationship: [fileattachment FileAttachment_msfp_fileresponse_msfp_file10](fileattachment.md#BKMK_FileAttachment_msfp_fileresponse_msfp_file10)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msfp_file10`|
|ReferencingEntityNavigationPropertyName|`msfp_file10`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msfp_fileresponse_msfp_file2"></a> FileAttachment_msfp_fileresponse_msfp_file2

One-To-Many Relationship: [fileattachment FileAttachment_msfp_fileresponse_msfp_file2](fileattachment.md#BKMK_FileAttachment_msfp_fileresponse_msfp_file2)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msfp_file2`|
|ReferencingEntityNavigationPropertyName|`msfp_file2`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msfp_fileresponse_msfp_file3"></a> FileAttachment_msfp_fileresponse_msfp_file3

One-To-Many Relationship: [fileattachment FileAttachment_msfp_fileresponse_msfp_file3](fileattachment.md#BKMK_FileAttachment_msfp_fileresponse_msfp_file3)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msfp_file3`|
|ReferencingEntityNavigationPropertyName|`msfp_file3`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msfp_fileresponse_msfp_file4"></a> FileAttachment_msfp_fileresponse_msfp_file4

One-To-Many Relationship: [fileattachment FileAttachment_msfp_fileresponse_msfp_file4](fileattachment.md#BKMK_FileAttachment_msfp_fileresponse_msfp_file4)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msfp_file4`|
|ReferencingEntityNavigationPropertyName|`msfp_file4`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msfp_fileresponse_msfp_file5"></a> FileAttachment_msfp_fileresponse_msfp_file5

One-To-Many Relationship: [fileattachment FileAttachment_msfp_fileresponse_msfp_file5](fileattachment.md#BKMK_FileAttachment_msfp_fileresponse_msfp_file5)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msfp_file5`|
|ReferencingEntityNavigationPropertyName|`msfp_file5`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msfp_fileresponse_msfp_file6"></a> FileAttachment_msfp_fileresponse_msfp_file6

One-To-Many Relationship: [fileattachment FileAttachment_msfp_fileresponse_msfp_file6](fileattachment.md#BKMK_FileAttachment_msfp_fileresponse_msfp_file6)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msfp_file6`|
|ReferencingEntityNavigationPropertyName|`msfp_file6`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msfp_fileresponse_msfp_file7"></a> FileAttachment_msfp_fileresponse_msfp_file7

One-To-Many Relationship: [fileattachment FileAttachment_msfp_fileresponse_msfp_file7](fileattachment.md#BKMK_FileAttachment_msfp_fileresponse_msfp_file7)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msfp_file7`|
|ReferencingEntityNavigationPropertyName|`msfp_file7`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msfp_fileresponse_msfp_file8"></a> FileAttachment_msfp_fileresponse_msfp_file8

One-To-Many Relationship: [fileattachment FileAttachment_msfp_fileresponse_msfp_file8](fileattachment.md#BKMK_FileAttachment_msfp_fileresponse_msfp_file8)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msfp_file8`|
|ReferencingEntityNavigationPropertyName|`msfp_file8`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msfp_fileresponse_msfp_file9"></a> FileAttachment_msfp_fileresponse_msfp_file9

One-To-Many Relationship: [fileattachment FileAttachment_msfp_fileresponse_msfp_file9](fileattachment.md#BKMK_FileAttachment_msfp_fileresponse_msfp_file9)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msfp_file9`|
|ReferencingEntityNavigationPropertyName|`msfp_file9`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_fileresponse_createdby"></a> lk_msfp_fileresponse_createdby

One-To-Many Relationship: [systemuser lk_msfp_fileresponse_createdby](systemuser.md#BKMK_lk_msfp_fileresponse_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_fileresponse_createdonbehalfby"></a> lk_msfp_fileresponse_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msfp_fileresponse_createdonbehalfby](systemuser.md#BKMK_lk_msfp_fileresponse_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_fileresponse_modifiedby"></a> lk_msfp_fileresponse_modifiedby

One-To-Many Relationship: [systemuser lk_msfp_fileresponse_modifiedby](systemuser.md#BKMK_lk_msfp_fileresponse_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msfp_fileresponse_modifiedonbehalfby"></a> lk_msfp_fileresponse_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msfp_fileresponse_modifiedonbehalfby](systemuser.md#BKMK_lk_msfp_fileresponse_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_msfp_question_msfp_fileresponse_question"></a> msfp_msfp_question_msfp_fileresponse_question

One-To-Many Relationship: [msfp_question msfp_msfp_question_msfp_fileresponse_question](msfp_question.md#BKMK_msfp_msfp_question_msfp_fileresponse_question)

|Property|Value|
|---|---|
|ReferencedEntity|`msfp_question`|
|ReferencedAttribute|`msfp_questionid`|
|ReferencingAttribute|`msfp_question`|
|ReferencingEntityNavigationPropertyName|`msfp_question`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_msfp_questionresponse_msfp_fileresponse_questionresponse"></a> msfp_msfp_questionresponse_msfp_fileresponse_questionresponse

One-To-Many Relationship: [msfp_questionresponse msfp_msfp_questionresponse_msfp_fileresponse_questionresponse](msfp_questionresponse.md#BKMK_msfp_msfp_questionresponse_msfp_fileresponse_questionresponse)

|Property|Value|
|---|---|
|ReferencedEntity|`msfp_questionresponse`|
|ReferencedAttribute|`msfp_questionresponseid`|
|ReferencingAttribute|`msfp_questionresponse`|
|ReferencingEntityNavigationPropertyName|`msfp_questionresponse`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msfp_msfp_survey_msfp_fileresponse_survey"></a> msfp_msfp_survey_msfp_fileresponse_survey

One-To-Many Relationship: [msfp_survey msfp_msfp_survey_msfp_fileresponse_survey](msfp_survey.md#BKMK_msfp_msfp_survey_msfp_fileresponse_survey)

|Property|Value|
|---|---|
|ReferencedEntity|`msfp_survey`|
|ReferencedAttribute|`msfp_surveyid`|
|ReferencingAttribute|`msfp_survey`|
|ReferencingEntityNavigationPropertyName|`msfp_survey`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msfp_fileresponse"></a> owner_msfp_fileresponse

One-To-Many Relationship: [owner owner_msfp_fileresponse](owner.md#BKMK_owner_msfp_fileresponse)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msfp_fileresponse"></a> team_msfp_fileresponse

One-To-Many Relationship: [team team_msfp_fileresponse](team.md#BKMK_team_msfp_fileresponse)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msfp_fileresponse"></a> user_msfp_fileresponse

One-To-Many Relationship: [systemuser user_msfp_fileresponse](systemuser.md#BKMK_user_msfp_fileresponse)

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

- [msfp_fileresponse_AsyncOperations](#BKMK_msfp_fileresponse_AsyncOperations)
- [msfp_fileresponse_BulkDeleteFailures](#BKMK_msfp_fileresponse_BulkDeleteFailures)
- [msfp_fileresponse_DuplicateBaseRecord](#BKMK_msfp_fileresponse_DuplicateBaseRecord)
- [msfp_fileresponse_DuplicateMatchingRecord](#BKMK_msfp_fileresponse_DuplicateMatchingRecord)
- [msfp_fileresponse_FileAttachments](#BKMK_msfp_fileresponse_FileAttachments)
- [msfp_fileresponse_MailboxTrackingFolders](#BKMK_msfp_fileresponse_MailboxTrackingFolders)
- [msfp_fileresponse_PrincipalObjectAttributeAccesses](#BKMK_msfp_fileresponse_PrincipalObjectAttributeAccesses)
- [msfp_fileresponse_ProcessSession](#BKMK_msfp_fileresponse_ProcessSession)
- [msfp_fileresponse_SyncErrors](#BKMK_msfp_fileresponse_SyncErrors)

### <a name="BKMK_msfp_fileresponse_AsyncOperations"></a> msfp_fileresponse_AsyncOperations

Many-To-One Relationship: [asyncoperation msfp_fileresponse_AsyncOperations](asyncoperation.md#BKMK_msfp_fileresponse_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_fileresponse_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_fileresponse_BulkDeleteFailures"></a> msfp_fileresponse_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msfp_fileresponse_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msfp_fileresponse_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_fileresponse_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_fileresponse_DuplicateBaseRecord"></a> msfp_fileresponse_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msfp_fileresponse_DuplicateBaseRecord](duplicaterecord.md#BKMK_msfp_fileresponse_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msfp_fileresponse_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_fileresponse_DuplicateMatchingRecord"></a> msfp_fileresponse_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msfp_fileresponse_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msfp_fileresponse_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msfp_fileresponse_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_fileresponse_FileAttachments"></a> msfp_fileresponse_FileAttachments

Many-To-One Relationship: [fileattachment msfp_fileresponse_FileAttachments](fileattachment.md#BKMK_msfp_fileresponse_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msfp_fileresponse_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_fileresponse_MailboxTrackingFolders"></a> msfp_fileresponse_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msfp_fileresponse_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msfp_fileresponse_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_fileresponse_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_fileresponse_PrincipalObjectAttributeAccesses"></a> msfp_fileresponse_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msfp_fileresponse_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msfp_fileresponse_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msfp_fileresponse_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_fileresponse_ProcessSession"></a> msfp_fileresponse_ProcessSession

Many-To-One Relationship: [processsession msfp_fileresponse_ProcessSession](processsession.md#BKMK_msfp_fileresponse_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_fileresponse_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msfp_fileresponse_SyncErrors"></a> msfp_fileresponse_SyncErrors

Many-To-One Relationship: [syncerror msfp_fileresponse_SyncErrors](syncerror.md#BKMK_msfp_fileresponse_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msfp_fileresponse_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

