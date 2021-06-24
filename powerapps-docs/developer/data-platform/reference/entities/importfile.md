---
title: "ImportFile table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the ImportFile table/entity."
ms.date: 05/20/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# ImportFile table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

File name of file used for import.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/importfiles(*importfileid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/importfiles<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/importfiles(*importfileid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GetDistinctValuesImportFile|<xref href="Microsoft.Dynamics.CRM.GetDistinctValuesImportFile?text=GetDistinctValuesImportFile Function" />|<xref:Microsoft.Crm.Sdk.Messages.GetDistinctValuesImportFileRequest>|
|GetHeaderColumnsImportFile|<xref href="Microsoft.Dynamics.CRM.GetHeaderColumnsImportFile?text=GetHeaderColumnsImportFile Function" />|<xref:Microsoft.Crm.Sdk.Messages.GetHeaderColumnsImportFileRequest>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/importfiles(*importfileid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/importfiles<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrieveParsedDataImportFile|<xref href="Microsoft.Dynamics.CRM.RetrieveParsedDataImportFile?text=RetrieveParsedDataImportFile Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveParsedDataImportFileRequest>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/importfiles(*importfileid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|ImportFiles|
|DisplayCollectionName|Imports|
|DisplayName|Import Source File|
|EntitySetName|importfiles|
|IsBPFEntity|False|
|LogicalCollectionName|importfiles|
|LogicalName|importfile|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|importfileid|
|PrimaryNameAttribute|name|
|SchemaName|ImportFile|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Stores the content of the import file, stored as comma-separated values.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|content|
|MaxLength|1073741823|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_DataDelimiterCode"></a> DataDelimiterCode

|Property|Value|
|--------|-----|
|Description|Select the single-character data delimiter used in the import file. This is typically a single or double quotation mark.|
|DisplayName|Data Delimiter|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|datadelimitercode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### DataDelimiterCode Choices/Options

|Value|Label|
|-----|-----|
|1|DoubleQuote|
|2|None|
|3|SingleQuote|



### <a name="BKMK_EnableDuplicateDetection"></a> EnableDuplicateDetection

|Property|Value|
|--------|-----|
|Description|Select whether duplicate-detection rules should be run against the import job.|
|DisplayName|Enable Duplicate Detection|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|enableduplicatedetection|
|RequiredLevel|None|
|Type|Boolean|

#### EnableDuplicateDetection Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_EntityKeyId"></a> EntityKeyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Alternate key Id|
|DisplayName|Entity Key ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entitykeyid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_FieldDelimiterCode"></a> FieldDelimiterCode

|Property|Value|
|--------|-----|
|Description|Select the character that is used to separate each field in the import file. Typically, it is a comma.|
|DisplayName|Field Delimiter|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|fielddelimitercode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### FieldDelimiterCode Choices/Options

|Value|Label|
|-----|-----|
|1|Colon|
|2|Comma|
|3|Tab|
|4|Semicolon|



### <a name="BKMK_FileTypeCode"></a> FileTypeCode

|Property|Value|
|--------|-----|
|Description|Shows the type of source file that is uploaded for import.|
|DisplayName|File Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|filetypecode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### FileTypeCode Choices/Options

|Value|Label|
|-----|-----|
|0|CSV|
|1|XML Spreadsheet 2003|
|2|Attachment|
|3|XLSX|



### <a name="BKMK_ImportFileId"></a> ImportFileId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the import file.|
|DisplayName|Import|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importfileid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ImportId"></a> ImportId

|Property|Value|
|--------|-----|
|Description|Choose the import job that the file was uploaded for.|
|DisplayName|Import Job ID|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|importid|
|RequiredLevel|SystemRequired|
|Targets|import|
|Type|Lookup|


### <a name="BKMK_ImportMapId"></a> ImportMapId

|Property|Value|
|--------|-----|
|Description|Choose a data map to match the import file and its column headers with the record types and fields in Microsoft Dynamics 365. If the column headers in the file match the display names of the target fields in Microsoft Dynamics 365, we import the data automatically. If not, you can manually define matches during import.|
|DisplayName|Data Map|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|importmapid|
|RequiredLevel|None|
|Targets|importmap|
|Type|Lookup|


### <a name="BKMK_IsFirstRowHeader"></a> IsFirstRowHeader

|Property|Value|
|--------|-----|
|Description|Select whether the first row of the import file contains column headings, which are used for data mapping during the import job.|
|DisplayName|Is First Row Header|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isfirstrowheader|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsFirstRowHeader Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Shows the name of the import file. This name is based on the name of the uploaded file.|
|DisplayName|Import Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Enter the user who is assigned to follow up with or manage the import file. This field is updated every time the import file is assigned to a different user.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_ProcessCode"></a> ProcessCode

|Property|Value|
|--------|-----|
|Description|Tells whether the import file should be ignored or processed during the import.|
|DisplayName|Process Code|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|processcode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ProcessCode Choices/Options

|Value|Label|
|-----|-----|
|1|Process|
|2|Ignore|
|3|Internal|



### <a name="BKMK_RecordsOwnerId"></a> RecordsOwnerId

|Property|Value|
|--------|-----|
|Description|Choose the user that the records created during the import job should be assigned to.|
|DisplayName|Records Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|recordsownerid|
|RequiredLevel|None|
|Targets|systemuser,team|
|Type|Lookup|


### <a name="BKMK_RecordsOwnerIdType"></a> RecordsOwnerIdType

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|recordsowneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_RelatedEntityColumns"></a> RelatedEntityColumns

|Property|Value|
|--------|-----|
|Description|Shows the columns that are mapped to a related record type (entity) of the primary record type (entity) included in the import file.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|relatedentitycolumns|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Size"></a> Size

|Property|Value|
|--------|-----|
|Description|Shows the size of the import file, in kilobytes.|
|DisplayName|Size|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|size|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Source"></a> Source

|Property|Value|
|--------|-----|
|Description|Shows the name of the data source file uploaded in the import job.|
|DisplayName|Source|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|source|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SourceEntityName"></a> SourceEntityName

|Property|Value|
|--------|-----|
|Description|Shows the record type (entity) of the source data.|
|DisplayName|Source Entity|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|sourceentityname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows the status of the import file record. By default, all records are active and can't be deactivated.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|0|Active|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Shows the reason code that explains the import file's status to identify the stage of the import process, from parsing the data to completed.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|0|Submitted|0|
|1|Parsing|0|
|2|Transforming|0|
|3|Importing|0|
|4|Completed|0|
|5|Failed|0|



### <a name="BKMK_TargetEntityName"></a> TargetEntityName

|Property|Value|
|--------|-----|
|Description|Select the target record type (entity) for the records that will be created during the import job.|
|DisplayName|Target Entity|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|targetentityname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UpsertModeCode"></a> UpsertModeCode

|Property|Value|
|--------|-----|
|Description|Select the value which is used for identify the upsert mode. By Default, it is a Create.|
|DisplayName|Upsert Mode|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|upsertmodecode|
|RequiredLevel|None|
|Type|Picklist|

#### UpsertModeCode Choices/Options

|Value|Label|
|-----|-----|
|0|Create|
|1|Update|
|2|Ignore|



### <a name="BKMK_UseSystemMap"></a> UseSystemMap

|Property|Value|
|--------|-----|
|Description|Tells whether an automatic system map was applied to the import file, which automatically maps the import data to the target entity in Microsoft Dynamics 365.|
|DisplayName|Use System Map|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|usesystemmap|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### UseSystemMap Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

|Property|Value|
|--------|-----|
|Description|Shows the secondary column headers. The additional headers are used during the process of transforming the import file into import data records.|
|DisplayName|Additional Header|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|additionalheaderrow|
|MaxLength|100000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the import associated with the import file was completed.|
|DisplayName|Completed On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|completedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
|DisplayName|Created By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record on behalf of another user.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FailureCount"></a> FailureCount

|Property|Value|
|--------|-----|
|Description|Shows the number of records in the import file that cannot be imported.|
|DisplayName|Errors|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|failurecount|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_HeaderRow"></a> HeaderRow

|Property|Value|
|--------|-----|
|Description|Shows a list of each column header in the import file separated by a comma. The header is used for parsing the file during the import job.|
|DisplayName|Header|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|headerrow|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ImportIdName"></a> ImportIdName

|Property|Value|
|--------|-----|
|Description|Name of the import.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|importidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ImportMapIdName"></a> ImportMapIdName

|Property|Value|
|--------|-----|
|Description|Name of the import map.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|importmapidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
|DisplayName|Modified By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record on behalf of another user.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Shows the business unit that the record owner belongs to.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the import file.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who owns the import file.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ParsedTableColumnPrefix"></a> ParsedTableColumnPrefix

|Property|Value|
|--------|-----|
|Description|Shows the prefix applied to each column after the import file is parsed.|
|DisplayName|Parse Table Column Prefix|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parsedtablecolumnprefix|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ParsedTableColumnsNumber"></a> ParsedTableColumnsNumber

|Property|Value|
|--------|-----|
|Description|Shows the number of columns included in the parsed import file.|
|DisplayName|Parse Table Column Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parsedtablecolumnsnumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ParsedTableName"></a> ParsedTableName

|Property|Value|
|--------|-----|
|Description|Shows the name of the table that contains the parsed data from the import file.|
|DisplayName|Parse Table|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parsedtablename|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PartialFailureCount"></a> PartialFailureCount

|Property|Value|
|--------|-----|
|Description|Shows the number of records in this file that had failures during the import.|
|DisplayName|Partial Failures|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|partialfailurecount|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ProcessingStatus"></a> ProcessingStatus

|Property|Value|
|--------|-----|
|Description|Shows the import file's processing status code. This indicates whether the data in the import file has been parsed, transformed, or imported.|
|DisplayName|Processing Status|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processingstatus|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ProcessingStatus Choices/Options

|Value|Label|
|-----|-----|
|1|Not Started|
|2|Parsing|
|3|Parsing Complete|
|4|Complex Transformation|
|5|Lookup Transformation|
|6|Picklist Transformation|
|7|Owner Transformation|
|8|Transformation Complete|
|9|Import Pass 1|
|10|Import Pass 2|
|11|Import Complete|
|12|Primary Key Transformation|



### <a name="BKMK_ProgressCounter"></a> ProgressCounter

|Property|Value|
|--------|-----|
|Description|Shows the progress code for the processing of the import file. This field is used when a paused import job is resumed.|
|DisplayName|Progress Counter|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|progresscounter|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_RecordsOwnerIdName"></a> RecordsOwnerIdName

|Property|Value|
|--------|-----|
|Description|Name of the record owner.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|recordsowneridname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SuccessCount"></a> SuccessCount

|Property|Value|
|--------|-----|
|Description|Shows the number of records in the import file that are imported successfully.|
|DisplayName|Successes|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|successcount|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_TotalCount"></a> TotalCount

|Property|Value|
|--------|-----|
|Description|Shows the total number of records in the import file.|
|DisplayName|Total Processed|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|totalcount|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [ImportFile_BulkDeleteFailures](#BKMK_ImportFile_BulkDeleteFailures)
- [ImportLog_ImportFile](#BKMK_ImportLog_ImportFile)
- [ImportFile_AsyncOperations](#BKMK_ImportFile_AsyncOperations)


### <a name="BKMK_ImportFile_BulkDeleteFailures"></a> ImportFile_BulkDeleteFailures

Same as bulkdeletefailure table [ImportFile_BulkDeleteFailures](bulkdeletefailure.md#BKMK_ImportFile_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|ImportFile_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_ImportLog_ImportFile"></a> ImportLog_ImportFile

Same as importlog table [ImportLog_ImportFile](importlog.md#BKMK_ImportLog_ImportFile) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importlog|
|ReferencingAttribute|importfileid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|ImportLog_ImportFile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_ImportFile_AsyncOperations"></a> ImportFile_AsyncOperations

Same as asyncoperation table [ImportFile_AsyncOperations](asyncoperation.md#BKMK_ImportFile_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|ImportFile_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

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

See systemuser Table [lk_importfilebase_createdby](systemuser.md#BKMK_lk_importfilebase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_importfilebase_createdonbehalfby"></a> lk_importfilebase_createdonbehalfby

See systemuser Table [lk_importfilebase_createdonbehalfby](systemuser.md#BKMK_lk_importfilebase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_team_ImportFiles"></a> team_ImportFiles

See team Table [team_ImportFiles](team.md#BKMK_team_ImportFiles) One-To-Many relationship.

### <a name="BKMK_ImportFile_Team"></a> ImportFile_Team

See team Table [ImportFile_Team](team.md#BKMK_ImportFile_Team) One-To-Many relationship.

### <a name="BKMK_ImportFile_SystemUser"></a> ImportFile_SystemUser

See systemuser Table [ImportFile_SystemUser](systemuser.md#BKMK_ImportFile_SystemUser) One-To-Many relationship.

### <a name="BKMK_SystemUser_ImportFiles"></a> SystemUser_ImportFiles

See systemuser Table [SystemUser_ImportFiles](systemuser.md#BKMK_SystemUser_ImportFiles) One-To-Many relationship.

### <a name="BKMK_lk_importfilebase_modifiedonbehalfby"></a> lk_importfilebase_modifiedonbehalfby

See systemuser Table [lk_importfilebase_modifiedonbehalfby](systemuser.md#BKMK_lk_importfilebase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_Import_ImportFile"></a> Import_ImportFile

See import Table [Import_ImportFile](import.md#BKMK_Import_ImportFile) One-To-Many relationship.

### <a name="BKMK_ImportMap_ImportFile"></a> ImportMap_ImportFile

See importmap Table [ImportMap_ImportFile](importmap.md#BKMK_ImportMap_ImportFile) One-To-Many relationship.

### <a name="BKMK_lk_importfilebase_modifiedby"></a> lk_importfilebase_modifiedby

See systemuser Table [lk_importfilebase_modifiedby](systemuser.md#BKMK_lk_importfilebase_modifiedby) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_ImportFiles"></a> BusinessUnit_ImportFiles

See businessunit Table [BusinessUnit_ImportFiles](businessunit.md#BKMK_BusinessUnit_ImportFiles) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.importfile?text=importfile EntityType" />