---
title: "Import Source File (ImportFile) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Import Source File (ImportFile) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Import Source File (ImportFile) table/entity reference (Microsoft Dataverse)

File name of file used for import.

## Messages

The following table lists the messages for the Import Source File (ImportFile) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: False |`PATCH` /importfiles(*importfileid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /importfiles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /importfiles(*importfileid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GetDistinctValuesImportFile`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GetDistinctValuesImportFile?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GetDistinctValuesImportFileRequest>|
| `GetHeaderColumnsImportFile`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GetHeaderColumnsImportFile?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GetHeaderColumnsImportFileRequest>|
| `GrantAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /importfiles(*importfileid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /importfiles<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveParsedDataImportFile`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveParsedDataImportFile?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveParsedDataImportFileRequest>|
| `RetrievePrincipalAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `Update`<br />Event: False |`PATCH` /importfiles(*importfileid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /importfiles(*importfileid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Import Source File (ImportFile) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Import Source File** |
| **DisplayCollectionName** | **Imports** |
| **SchemaName** | `ImportFile` |
| **CollectionSchemaName** | `ImportFiles` |
| **EntitySetName** | `importfiles`|
| **LogicalName** | `importfile` |
| **LogicalCollectionName** | `importfiles` |
| **PrimaryIdAttribute** | `importfileid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Content](#BKMK_Content)
- [DataDelimiterCode](#BKMK_DataDelimiterCode)
- [EnableDuplicateDetection](#BKMK_EnableDuplicateDetection)
- [EntityKeyId](#BKMK_EntityKeyId)
- [FieldDelimiterCode](#BKMK_FieldDelimiterCode)
- [FileTypeCode](#BKMK_FileTypeCode)
- [ImportFileId](#BKMK_ImportFileId)
- [ImportId](#BKMK_ImportId)
- [ImportMapId](#BKMK_ImportMapId)
- [IsFirstRowHeader](#BKMK_IsFirstRowHeader)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ProcessCode](#BKMK_ProcessCode)
- [RecordsOwnerId](#BKMK_RecordsOwnerId)
- [RecordsOwnerIdType](#BKMK_RecordsOwnerIdType)
- [RelatedEntityColumns](#BKMK_RelatedEntityColumns)
- [Size](#BKMK_Size)
- [Source](#BKMK_Source)
- [SourceEntityName](#BKMK_SourceEntityName)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TargetEntityName](#BKMK_TargetEntityName)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UpsertModeCode](#BKMK_UpsertModeCode)
- [UseSystemMap](#BKMK_UseSystemMap)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_Content"></a> Content

|Property|Value|
|---|---|
|Description|**Stores the content of the import file, stored as comma-separated values.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`content`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_DataDelimiterCode"></a> DataDelimiterCode

|Property|Value|
|---|---|
|Description|**Select the single-character data delimiter used in the import file. This is typically a single or double quotation mark.**|
|DisplayName|**Data Delimiter**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`datadelimitercode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`importfile_datadelimitercode`|

#### DataDelimiterCode Choices/Options

|Value|Label|
|---|---|
|1|**DoubleQuote**|
|2|**None**|
|3|**SingleQuote**|

### <a name="BKMK_EnableDuplicateDetection"></a> EnableDuplicateDetection

|Property|Value|
|---|---|
|Description|**Select whether duplicate-detection rules should be run against the import job.**|
|DisplayName|**Enable Duplicate Detection**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enableduplicatedetection`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`importfile_enableduplicatedetection`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EntityKeyId"></a> EntityKeyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Alternate key Id**|
|DisplayName|**Entity Key ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entitykeyid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_FieldDelimiterCode"></a> FieldDelimiterCode

|Property|Value|
|---|---|
|Description|**Select the character that is used to separate each field in the import file. Typically, it is a comma.**|
|DisplayName|**Field Delimiter**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fielddelimitercode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`importfile_fielddelimitercode`|

#### FieldDelimiterCode Choices/Options

|Value|Label|
|---|---|
|1|**Colon**|
|2|**Comma**|
|3|**Tab**|
|4|**Semicolon**|

### <a name="BKMK_FileTypeCode"></a> FileTypeCode

|Property|Value|
|---|---|
|Description|**Shows the type of source file that is uploaded for import.**|
|DisplayName|**File Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`filetypecode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`importfile_filetypecode`|

#### FileTypeCode Choices/Options

|Value|Label|
|---|---|
|0|**CSV**|
|1|**XML Spreadsheet 2003**|
|2|**Attachment**|
|3|**XLSX**|

### <a name="BKMK_ImportFileId"></a> ImportFileId

|Property|Value|
|---|---|
|Description|**Unique identifier of the import file.**|
|DisplayName|**Import**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importfileid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ImportId"></a> ImportId

|Property|Value|
|---|---|
|Description|**Choose the import job that the file was uploaded for.**|
|DisplayName|**Import Job ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`importid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|import|

### <a name="BKMK_ImportMapId"></a> ImportMapId

|Property|Value|
|---|---|
|Description|**Choose a data map to match the import file and its column headers with the record types and fields in Microsoft Dynamics 365. If the column headers in the file match the display names of the target fields in Microsoft Dynamics 365, we import the data automatically. If not, you can manually define matches during import.**|
|DisplayName|**Data Map**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`importmapid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|importmap|

### <a name="BKMK_IsFirstRowHeader"></a> IsFirstRowHeader

|Property|Value|
|---|---|
|Description|**Select whether the first row of the import file contains column headings, which are used for data mapping during the import job.**|
|DisplayName|**Is First Row Header**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isfirstrowheader`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`importfile_isfirstrowheader`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Shows the name of the import file. This name is based on the name of the uploaded file.**|
|DisplayName|**Import Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user who is assigned to follow up with or manage the import file. This field is updated every time the import file is assigned to a different user.**|
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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_ProcessCode"></a> ProcessCode

|Property|Value|
|---|---|
|Description|**Tells whether the import file should be ignored or processed during the import.**|
|DisplayName|**Process Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processcode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`importfile_processcode`|

#### ProcessCode Choices/Options

|Value|Label|
|---|---|
|1|**Process**|
|2|**Ignore**|
|3|**Internal**|

### <a name="BKMK_RecordsOwnerId"></a> RecordsOwnerId

|Property|Value|
|---|---|
|Description|**Choose the user that the records created during the import job should be assigned to.**|
|DisplayName|**Records Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordsownerid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser, team|

### <a name="BKMK_RecordsOwnerIdType"></a> RecordsOwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`recordsowneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_RelatedEntityColumns"></a> RelatedEntityColumns

|Property|Value|
|---|---|
|Description|**Shows the columns that are mapped to a related record type (entity) of the primary record type (entity) included in the import file.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`relatedentitycolumns`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Size"></a> Size

|Property|Value|
|---|---|
|Description|**Shows the size of the import file, in kilobytes.**|
|DisplayName|**Size**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`size`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_Source"></a> Source

|Property|Value|
|---|---|
|Description|**Shows the name of the data source file uploaded in the import job.**|
|DisplayName|**Source**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`source`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SourceEntityName"></a> SourceEntityName

|Property|Value|
|---|---|
|Description|**Shows the record type (entity) of the source data.**|
|DisplayName|**Source Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourceentityname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows the status of the import file record. By default, all records are active and can't be deactivated.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`importfile_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 0<br />InvariantName: `Active`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Shows the reason code that explains the import file's status to identify the stage of the import process, from parsing the data to completed.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`importfile_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Submitted**<br />State:0<br />TransitionData: None|
|1|Label: **Parsing**<br />State:0<br />TransitionData: None|
|2|Label: **Transforming**<br />State:0<br />TransitionData: None|
|3|Label: **Importing**<br />State:0<br />TransitionData: None|
|4|Label: **Completed**<br />State:0<br />TransitionData: None|
|5|Label: **Failed**<br />State:0<br />TransitionData: None|

### <a name="BKMK_TargetEntityName"></a> TargetEntityName

|Property|Value|
|---|---|
|Description|**Select the target record type (entity) for the records that will be created during the import job.**|
|DisplayName|**Target Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`targetentityname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UpsertModeCode"></a> UpsertModeCode

|Property|Value|
|---|---|
|Description|**Select the value which is used for identify the upsert mode. By Default, it is a Create.**|
|DisplayName|**Upsert Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`upsertmodecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`importfile_upsertmodecode`|

#### UpsertModeCode Choices/Options

|Value|Label|
|---|---|
|0|**Create**|
|1|**Update**|
|2|**Ignore**|

### <a name="BKMK_UseSystemMap"></a> UseSystemMap

|Property|Value|
|---|---|
|Description|**Tells whether an automatic system map was applied to the import file, which automatically maps the import data to the target entity in Microsoft Dynamics 365.**|
|DisplayName|**Use System Map**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`usesystemmap`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`importfile_usesystemmap`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AdditionalHeaderRow](#BKMK_AdditionalHeaderRow)
- [CompletedOn](#BKMK_CompletedOn)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [FailureCount](#BKMK_FailureCount)
- [HeaderRow](#BKMK_HeaderRow)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ParsedTableColumnPrefix](#BKMK_ParsedTableColumnPrefix)
- [ParsedTableColumnsNumber](#BKMK_ParsedTableColumnsNumber)
- [ParsedTableName](#BKMK_ParsedTableName)
- [PartialFailureCount](#BKMK_PartialFailureCount)
- [ProcessingStatus](#BKMK_ProcessingStatus)
- [ProgressCounter](#BKMK_ProgressCounter)
- [SuccessCount](#BKMK_SuccessCount)
- [TotalCount](#BKMK_TotalCount)

### <a name="BKMK_AdditionalHeaderRow"></a> AdditionalHeaderRow

|Property|Value|
|---|---|
|Description|**Shows the secondary column headers. The additional headers are used during the process of transforming the import file into import data records.**|
|DisplayName|**Additional Header**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`additionalheaderrow`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the import associated with the import file was completed.**|
|DisplayName|**Completed On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`completedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Shows who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_FailureCount"></a> FailureCount

|Property|Value|
|---|---|
|Description|**Shows the number of records in the import file that cannot be imported.**|
|DisplayName|**Errors**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`failurecount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_HeaderRow"></a> HeaderRow

|Property|Value|
|---|---|
|Description|**Shows a list of each column header in the import file separated by a comma. The header is used for parsing the file during the import job.**|
|DisplayName|**Header**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`headerrow`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description||
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
|Description||
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
|Description|**Shows the business unit that the record owner belongs to.**|
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier of the team who owns the import file.**|
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
|Description|**Unique identifier of the user who owns the import file.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ParsedTableColumnPrefix"></a> ParsedTableColumnPrefix

|Property|Value|
|---|---|
|Description|**Shows the prefix applied to each column after the import file is parsed.**|
|DisplayName|**Parse Table Column Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parsedtablecolumnprefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_ParsedTableColumnsNumber"></a> ParsedTableColumnsNumber

|Property|Value|
|---|---|
|Description|**Shows the number of columns included in the parsed import file.**|
|DisplayName|**Parse Table Column Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parsedtablecolumnsnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ParsedTableName"></a> ParsedTableName

|Property|Value|
|---|---|
|Description|**Shows the name of the table that contains the parsed data from the import file.**|
|DisplayName|**Parse Table**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parsedtablename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_PartialFailureCount"></a> PartialFailureCount

|Property|Value|
|---|---|
|Description|**Shows the number of records in this file that had failures during the import.**|
|DisplayName|**Partial Failures**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`partialfailurecount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_ProcessingStatus"></a> ProcessingStatus

|Property|Value|
|---|---|
|Description|**Shows the import file's processing status code. This indicates whether the data in the import file has been parsed, transformed, or imported.**|
|DisplayName|**Processing Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processingstatus`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`importfile_processingstatus`|

#### ProcessingStatus Choices/Options

|Value|Label|
|---|---|
|1|**Not Started**|
|2|**Parsing**|
|3|**Parsing Complete**|
|4|**Complex Transformation**|
|5|**Lookup Transformation**|
|6|**Picklist Transformation**|
|7|**Owner Transformation**|
|8|**Transformation Complete**|
|9|**Import Pass 1**|
|10|**Import Pass 2**|
|11|**Import Complete**|
|12|**Primary Key Transformation**|

### <a name="BKMK_ProgressCounter"></a> ProgressCounter

|Property|Value|
|---|---|
|Description|**Shows the progress code for the processing of the import file. This field is used when a paused import job is resumed.**|
|DisplayName|**Progress Counter**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`progresscounter`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_SuccessCount"></a> SuccessCount

|Property|Value|
|---|---|
|Description|**Shows the number of records in the import file that are imported successfully.**|
|DisplayName|**Successes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`successcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_TotalCount"></a> TotalCount

|Property|Value|
|---|---|
|Description|**Shows the total number of records in the import file.**|
|DisplayName|**Total Processed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`totalcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [BusinessUnit_ImportFiles](#BKMK_BusinessUnit_ImportFiles)
- [Import_ImportFile](#BKMK_Import_ImportFile)
- [ImportFile_SystemUser](#BKMK_ImportFile_SystemUser)
- [ImportFile_Team](#BKMK_ImportFile_Team)
- [ImportMap_ImportFile](#BKMK_ImportMap_ImportFile)
- [lk_importfilebase_createdby](#BKMK_lk_importfilebase_createdby)
- [lk_importfilebase_createdonbehalfby](#BKMK_lk_importfilebase_createdonbehalfby)
- [lk_importfilebase_modifiedby](#BKMK_lk_importfilebase_modifiedby)
- [lk_importfilebase_modifiedonbehalfby](#BKMK_lk_importfilebase_modifiedonbehalfby)
- [owner_importfiles](#BKMK_owner_importfiles)
- [SystemUser_ImportFiles](#BKMK_SystemUser_ImportFiles)
- [team_ImportFiles](#BKMK_team_ImportFiles)

### <a name="BKMK_BusinessUnit_ImportFiles"></a> BusinessUnit_ImportFiles

One-To-Many Relationship: [businessunit BusinessUnit_ImportFiles](businessunit.md#BKMK_BusinessUnit_ImportFiles)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Import_ImportFile"></a> Import_ImportFile

One-To-Many Relationship: [import Import_ImportFile](import.md#BKMK_Import_ImportFile)

|Property|Value|
|---|---|
|ReferencedEntity|`import`|
|ReferencedAttribute|`importid`|
|ReferencingAttribute|`importid`|
|ReferencingEntityNavigationPropertyName|`importid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportFile_SystemUser"></a> ImportFile_SystemUser

One-To-Many Relationship: [systemuser ImportFile_SystemUser](systemuser.md#BKMK_ImportFile_SystemUser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`recordsownerid`|
|ReferencingEntityNavigationPropertyName|`recordsownerid_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportFile_Team"></a> ImportFile_Team

One-To-Many Relationship: [team ImportFile_Team](team.md#BKMK_ImportFile_Team)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`recordsownerid`|
|ReferencingEntityNavigationPropertyName|`recordsownerid_team`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportMap_ImportFile"></a> ImportMap_ImportFile

One-To-Many Relationship: [importmap ImportMap_ImportFile](importmap.md#BKMK_ImportMap_ImportFile)

|Property|Value|
|---|---|
|ReferencedEntity|`importmap`|
|ReferencedAttribute|`importmapid`|
|ReferencingAttribute|`importmapid`|
|ReferencingEntityNavigationPropertyName|`importmapid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importfilebase_createdby"></a> lk_importfilebase_createdby

One-To-Many Relationship: [systemuser lk_importfilebase_createdby](systemuser.md#BKMK_lk_importfilebase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importfilebase_createdonbehalfby"></a> lk_importfilebase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_importfilebase_createdonbehalfby](systemuser.md#BKMK_lk_importfilebase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importfilebase_modifiedby"></a> lk_importfilebase_modifiedby

One-To-Many Relationship: [systemuser lk_importfilebase_modifiedby](systemuser.md#BKMK_lk_importfilebase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importfilebase_modifiedonbehalfby"></a> lk_importfilebase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_importfilebase_modifiedonbehalfby](systemuser.md#BKMK_lk_importfilebase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_importfiles"></a> owner_importfiles

One-To-Many Relationship: [owner owner_importfiles](owner.md#BKMK_owner_importfiles)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemUser_ImportFiles"></a> SystemUser_ImportFiles

One-To-Many Relationship: [systemuser SystemUser_ImportFiles](systemuser.md#BKMK_SystemUser_ImportFiles)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_ImportFiles"></a> team_ImportFiles

One-To-Many Relationship: [team team_ImportFiles](team.md#BKMK_team_ImportFiles)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [ImportFile_AsyncOperations](#BKMK_ImportFile_AsyncOperations)
- [ImportFile_BulkDeleteFailures](#BKMK_ImportFile_BulkDeleteFailures)
- [ImportFile_ImportData](#BKMK_ImportFile_ImportData)
- [ImportLog_ImportFile](#BKMK_ImportLog_ImportFile)

### <a name="BKMK_ImportFile_AsyncOperations"></a> ImportFile_AsyncOperations

Many-To-One Relationship: [asyncoperation ImportFile_AsyncOperations](asyncoperation.md#BKMK_ImportFile_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ImportFile_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ImportFile_BulkDeleteFailures"></a> ImportFile_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure ImportFile_BulkDeleteFailures](bulkdeletefailure.md#BKMK_ImportFile_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ImportFile_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ImportFile_ImportData"></a> ImportFile_ImportData

Many-To-One Relationship: [importdata ImportFile_ImportData](importdata.md#BKMK_ImportFile_ImportData)

|Property|Value|
|---|---|
|ReferencingEntity|`importdata`|
|ReferencingAttribute|`importfileid`|
|ReferencedEntityNavigationPropertyName|`ImportFile_ImportData`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ImportLog_ImportFile"></a> ImportLog_ImportFile

Many-To-One Relationship: [importlog ImportLog_ImportFile](importlog.md#BKMK_ImportLog_ImportFile)

|Property|Value|
|---|---|
|ReferencingEntity|`importlog`|
|ReferencingAttribute|`importfileid`|
|ReferencedEntityNavigationPropertyName|`ImportLog_ImportFile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.importfile?displayProperty=fullName>
