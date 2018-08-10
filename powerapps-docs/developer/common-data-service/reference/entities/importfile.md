---
title: "ImportFile Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the ImportFile entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
---
# ImportFile Entity Reference

File name of file used for import.

## Entity Properties

**DisplayName**: Import Source File<br />
**DisplayCollectionName**: Imports<br />
**SchemaName**: ImportFile<br />
**CollectionSchemaName**: ImportFiles<br />
**LogicalName**: importfile<br />
**LogicalCollectionName**: importfiles<br />
**EntitySetName**: importfiles<br />
**PrimaryIdAttribute**: importfileid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

**Description**: Stores the content of the import file, stored as comma-separated values.<br />
**DisplayName**: <br />
**LogicalName**: content<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_DataDelimiterCode"></a> DataDelimiterCode

**Description**: Select the single-character data delimiter used in the import file. This is typically a single or double quotation mark.<br />
**DisplayName**: Data Delimiter<br />
**LogicalName**: datadelimitercode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: DoubleQuote
- **Value**: 2 **Label**: None
- **Value**: 3 **Label**: SingleQuote



### <a name="BKMK_EnableDuplicateDetection"></a> EnableDuplicateDetection

**Description**: Select whether duplicate-detection rules should be run against the import job.<br />
**DisplayName**: Enable Duplicate Detection<br />
**LogicalName**: enableduplicatedetection<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_EntityKeyId"></a> EntityKeyId

**Description**: Unique identifier of the Alternate key Id<br />
**DisplayName**: Entity Key ID<br />
**LogicalName**: entitykeyid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_FieldDelimiterCode"></a> FieldDelimiterCode

**Description**: Select the character that is used to separate each field in the import file. Typically, it is a comma.<br />
**DisplayName**: Field Delimiter<br />
**LogicalName**: fielddelimitercode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Colon
- **Value**: 2 **Label**: Comma
- **Value**: 3 **Label**: Tab
- **Value**: 4 **Label**: Semicolon



### <a name="BKMK_FileTypeCode"></a> FileTypeCode

**Description**: Shows the type of source file that is uploaded for import.<br />
**DisplayName**: File Type<br />
**LogicalName**: filetypecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: CSV
- **Value**: 1 **Label**: XML Spreadsheet 2003
- **Value**: 2 **Label**: Attachment
- **Value**: 3 **Label**: XLSX



### <a name="BKMK_ImportFileId"></a> ImportFileId

**Description**: Unique identifier of the import file.<br />
**DisplayName**: Import<br />
**LogicalName**: importfileid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ImportId"></a> ImportId

**Description**: Choose the import job that the file was uploaded for.<br />
**DisplayName**: Import Job ID<br />
**LogicalName**: importid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: import


### <a name="BKMK_ImportMapId"></a> ImportMapId

**Description**: Choose a data map to match the import file and its column headers with the record types and fields in Microsoft Dynamics 365. If the column headers in the file match the display names of the target fields in Microsoft Dynamics 365, we import the data automatically. If not, you can manually define matches during import.<br />
**DisplayName**: Data Map<br />
**LogicalName**: importmapid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: importmap


### <a name="BKMK_IsFirstRowHeader"></a> IsFirstRowHeader

**Description**: Select whether the first row of the import file contains column headings, which are used for data mapping during the import job.<br />
**DisplayName**: Is First Row Header<br />
**LogicalName**: isfirstrowheader<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Name"></a> Name

**Description**: Shows the name of the import file. This name is based on the name of the uploaded file.<br />
**DisplayName**: Import Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Enter the user who is assigned to follow up with or manage the import file. This field is updated every time the import file is assigned to a different user.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_ProcessCode"></a> ProcessCode

**Description**: Tells whether the import file should be ignored or processed during the import.<br />
**DisplayName**: Process Code<br />
**LogicalName**: processcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Process
- **Value**: 2 **Label**: Ignore
- **Value**: 3 **Label**: Internal



### <a name="BKMK_RecordsOwnerId"></a> RecordsOwnerId

**Description**: Choose the user that the records created during the import job should be assigned to.<br />
**DisplayName**: Records Owner<br />
**LogicalName**: recordsownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser,team


### <a name="BKMK_RecordsOwnerIdType"></a> RecordsOwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: recordsowneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_RelatedEntityColumns"></a> RelatedEntityColumns

**Description**: Shows the columns that are mapped to a related record type (entity) of the primary record type (entity) included in the import file.<br />
**DisplayName**: <br />
**LogicalName**: relatedentitycolumns<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_Size"></a> Size

**Description**: Shows the size of the import file, in kilobytes.<br />
**DisplayName**: Size<br />
**LogicalName**: size<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_Source"></a> Source

**Description**: Shows the name of the data source file uploaded in the import job.<br />
**DisplayName**: Source<br />
**LogicalName**: source<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_SourceEntityName"></a> SourceEntityName

**Description**: Shows the record type (entity) of the source data.<br />
**DisplayName**: Source Entity<br />
**LogicalName**: sourceentityname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows the status of the import file record. By default, all records are active and can't be deactivated.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 0 **InvariantName**: Active



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Shows the reason code that explains the import file's status to identify the stage of the import process, from parsing the data to completed.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 0 **Label**: Submitted **State**: 0
- **Value**: 1 **Label**: Parsing **State**: 0
- **Value**: 2 **Label**: Transforming **State**: 0
- **Value**: 3 **Label**: Importing **State**: 0
- **Value**: 4 **Label**: Completed **State**: 0
- **Value**: 5 **Label**: Failed **State**: 0



### <a name="BKMK_TargetEntityName"></a> TargetEntityName

**Description**: Select the target record type (entity) for the records that will be created during the import job.<br />
**DisplayName**: Target Entity<br />
**LogicalName**: targetentityname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_UpsertModeCode"></a> UpsertModeCode

**Description**: Select the value which is used for identify the upsert mode. By Default, it is a Create.<br />
**DisplayName**: Upsert Mode<br />
**LogicalName**: upsertmodecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Create
- **Value**: 1 **Label**: Update
- **Value**: 2 **Label**: Ignore



### <a name="BKMK_UseSystemMap"></a> UseSystemMap

**Description**: Tells whether an automatic system map was applied to the import file, which automatically maps the import data to the target entity in Microsoft Dynamics 365.<br />
**DisplayName**: Use System Map<br />
**LogicalName**: usesystemmap<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

**Description**: Time zone code that was in use when the record was created.<br />
**DisplayName**: <br />
**LogicalName**: utcconversiontimezonecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AdditionalHeaderRow](#BKMK_AdditionalHeaderRow)
- [CompletedOn](#BKMK_CompletedOn)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [FailureCount](#BKMK_FailureCount)
- [HeaderRow](#BKMK_HeaderRow)
- [ImportIdName](#BKMK_ImportIdName)
- [ImportMapIdName](#BKMK_ImportMapIdName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
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
- [RecordsOwnerIdName](#BKMK_RecordsOwnerIdName)
- [SuccessCount](#BKMK_SuccessCount)
- [TotalCount](#BKMK_TotalCount)


### <a name="BKMK_AdditionalHeaderRow"></a> AdditionalHeaderRow

**Description**: Shows the secondary column headers. The additional headers are used during the process of transforming the import file into import data records.<br />
**DisplayName**: Additional Header<br />
**LogicalName**: additionalheaderrow<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100000


### <a name="BKMK_CompletedOn"></a> CompletedOn

**Description**: Shows the date and time when the import associated with the import file was completed.<br />
**DisplayName**: Completed On<br />
**LogicalName**: completedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Shows who created the record.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_FailureCount"></a> FailureCount

**Description**: Shows the number of records in the import file that cannot be imported.<br />
**DisplayName**: Errors<br />
**LogicalName**: failurecount<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_HeaderRow"></a> HeaderRow

**Description**: Shows a list of each column header in the import file separated by a comma. The header is used for parsing the file during the import job.<br />
**DisplayName**: Header<br />
**LogicalName**: headerrow<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ImportIdName"></a> ImportIdName

**Description**: Name of the import.<br />
**DisplayName**: <br />
**LogicalName**: importidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ImportMapIdName"></a> ImportMapIdName

**Description**: Name of the import map.<br />
**DisplayName**: <br />
**LogicalName**: importmapidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows who last updated the record.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Shows the business unit that the record owner belongs to.<br />
**DisplayName**: <br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the import file.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the import file.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ParsedTableColumnPrefix"></a> ParsedTableColumnPrefix

**Description**: Shows the prefix applied to each column after the import file is parsed.<br />
**DisplayName**: Parse Table Column Prefix<br />
**LogicalName**: parsedtablecolumnprefix<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_ParsedTableColumnsNumber"></a> ParsedTableColumnsNumber

**Description**: Shows the number of columns included in the parsed import file.<br />
**DisplayName**: Parse Table Column Number<br />
**LogicalName**: parsedtablecolumnsnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ParsedTableName"></a> ParsedTableName

**Description**: Shows the name of the table that contains the parsed data from the import file.<br />
**DisplayName**: Parse Table<br />
**LogicalName**: parsedtablename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_PartialFailureCount"></a> PartialFailureCount

**Description**: Shows the number of records in this file that had failures during the import.<br />
**DisplayName**: Partial Failures<br />
**LogicalName**: partialfailurecount<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_ProcessingStatus"></a> ProcessingStatus

**Description**: Shows the import file's processing status code. This indicates whether the data in the import file has been parsed, transformed, or imported.<br />
**DisplayName**: Processing Status<br />
**LogicalName**: processingstatus<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Not Started
- **Value**: 2 **Label**: Parsing
- **Value**: 3 **Label**: Parsing Complete
- **Value**: 4 **Label**: Complex Transformation
- **Value**: 5 **Label**: Lookup Transformation
- **Value**: 6 **Label**: Picklist Transformation
- **Value**: 7 **Label**: Owner Transformation
- **Value**: 8 **Label**: Transformation Complete
- **Value**: 9 **Label**: Import Pass 1
- **Value**: 10 **Label**: Import Pass 2
- **Value**: 11 **Label**: Import Complete
- **Value**: 12 **Label**: Primary Key Transformation



### <a name="BKMK_ProgressCounter"></a> ProgressCounter

**Description**: Shows the progress code for the processing of the import file. This field is used when a paused import job is resumed.<br />
**DisplayName**: Progress Counter<br />
**LogicalName**: progresscounter<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_RecordsOwnerIdName"></a> RecordsOwnerIdName

**Description**: Name of the record owner.<br />
**DisplayName**: <br />
**LogicalName**: recordsowneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_SuccessCount"></a> SuccessCount

**Description**: Shows the number of records in the import file that are imported successfully.<br />
**DisplayName**: Successes<br />
**LogicalName**: successcount<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_TotalCount"></a> TotalCount

**Description**: Shows the total number of records in the import file.<br />
**DisplayName**: Total Processed<br />
**LogicalName**: totalcount<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [userentityinstancedata_importfile](#BKMK_userentityinstancedata_importfile)
- [ImportFile_BulkDeleteFailures](#BKMK_ImportFile_BulkDeleteFailures)
- [ImportLog_ImportFile](#BKMK_ImportLog_ImportFile)
- [ImportFile_AsyncOperations](#BKMK_ImportFile_AsyncOperations)


### <a name="BKMK_userentityinstancedata_importfile"></a> userentityinstancedata_importfile

Same as userentityinstancedata entity [userentityinstancedata_importfile](userentityinstancedata.md#BKMK_userentityinstancedata_importfile) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_importfile<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ImportFile_BulkDeleteFailures"></a> ImportFile_BulkDeleteFailures

Same as bulkdeletefailure entity [ImportFile_BulkDeleteFailures](bulkdeletefailure.md#BKMK_ImportFile_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ImportFile_BulkDeleteFailures<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ImportLog_ImportFile"></a> ImportLog_ImportFile

Same as importlog entity [ImportLog_ImportFile](importlog.md#BKMK_ImportLog_ImportFile) Many-To-One relationship.

**ReferencingEntity**: importlog<br />
**ReferencingAttribute**: importfileid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ImportLog_ImportFile<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ImportFile_AsyncOperations"></a> ImportFile_AsyncOperations

Same as asyncoperation entity [ImportFile_AsyncOperations](asyncoperation.md#BKMK_ImportFile_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ImportFile_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_importfilebase_createdby](#BKMK_lk_importfilebase_createdby)
- [lk_importfilebase_createdonbehalfby](#BKMK_lk_importfilebase_createdonbehalfby)
- [team_ImportFiles](#BKMK_team_ImportFiles)
- [ImportFile_Team](#BKMK_ImportFile_Team)
- [ImportFile_SystemUser](#BKMK_ImportFile_SystemUser)
- [SystemUser_ImportFiles](#BKMK_SystemUser_ImportFiles)
- [lk_importfilebase_modifiedonbehalfby](#BKMK_lk_importfilebase_modifiedonbehalfby)
- [Import_ImportFile](#BKMK_Import_ImportFile)
- [ImportMap_ImportFile](#BKMK_ImportMap_ImportFile)
- [lk_importfilebase_modifiedby](#BKMK_lk_importfilebase_modifiedby)
- [BusinessUnit_ImportFiles](#BKMK_BusinessUnit_ImportFiles)


### <a name="BKMK_lk_importfilebase_createdby"></a> lk_importfilebase_createdby

See systemuser Entity [lk_importfilebase_createdby](systemuser.md#BKMK_lk_importfilebase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_importfilebase_createdonbehalfby"></a> lk_importfilebase_createdonbehalfby

See systemuser Entity [lk_importfilebase_createdonbehalfby](systemuser.md#BKMK_lk_importfilebase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_team_ImportFiles"></a> team_ImportFiles

See team Entity [team_ImportFiles](team.md#BKMK_team_ImportFiles) One-To-Many relationship.

### <a name="BKMK_ImportFile_Team"></a> ImportFile_Team

See team Entity [ImportFile_Team](team.md#BKMK_ImportFile_Team) One-To-Many relationship.

### <a name="BKMK_ImportFile_SystemUser"></a> ImportFile_SystemUser

See systemuser Entity [ImportFile_SystemUser](systemuser.md#BKMK_ImportFile_SystemUser) One-To-Many relationship.

### <a name="BKMK_SystemUser_ImportFiles"></a> SystemUser_ImportFiles

See systemuser Entity [SystemUser_ImportFiles](systemuser.md#BKMK_SystemUser_ImportFiles) One-To-Many relationship.

### <a name="BKMK_lk_importfilebase_modifiedonbehalfby"></a> lk_importfilebase_modifiedonbehalfby

See systemuser Entity [lk_importfilebase_modifiedonbehalfby](systemuser.md#BKMK_lk_importfilebase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_Import_ImportFile"></a> Import_ImportFile

See import Entity [Import_ImportFile](import.md#BKMK_Import_ImportFile) One-To-Many relationship.

### <a name="BKMK_ImportMap_ImportFile"></a> ImportMap_ImportFile

See importmap Entity [ImportMap_ImportFile](importmap.md#BKMK_ImportMap_ImportFile) One-To-Many relationship.

### <a name="BKMK_lk_importfilebase_modifiedby"></a> lk_importfilebase_modifiedby

See systemuser Entity [lk_importfilebase_modifiedby](systemuser.md#BKMK_lk_importfilebase_modifiedby) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_ImportFiles"></a> BusinessUnit_ImportFiles

See businessunit Entity [BusinessUnit_ImportFiles](businessunit.md#BKMK_BusinessUnit_ImportFiles) One-To-Many relationship.
importfile

