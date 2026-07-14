---
title: "Report table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Report table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Report table/entity reference (Microsoft Dataverse)

Data summary in an easy-to-read layout.

## Messages

The following table lists the messages for the Report table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: False |`PATCH` /reports(*reportid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /reports<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /reports(*reportid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `DownloadReportDefinition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.DownloadReportDefinition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.DownloadReportDefinitionRequest>|
| `GetReportHistoryLimit`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GetReportHistoryLimit?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GetReportHistoryLimitRequest>|
| `GrantAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `MakeAvailableToOrganizationReport`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.MakeAvailableToOrganizationReportRequest>|
| `MakeAvailableToOrganizationTemplate`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.MakeAvailableToOrganizationTemplateRequest>|
| `MakeUnavailableToOrganizationReport`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.MakeUnavailableToOrganizationReportRequest>|
| `MakeUnavailableToOrganizationTemplate`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.MakeUnavailableToOrganizationTemplateRequest>|
| `ModifyAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /reports(*reportid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /reports<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetReportRelated`<br />Event: False |<xref:Microsoft.Dynamics.CRM.SetReportRelated?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SetReportRelatedRequest>|
| `Update`<br />Event: False |`PATCH` /reports(*reportid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /reports(*reportid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Report table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Report** |
| **DisplayCollectionName** | **Reports** |
| **SchemaName** | `Report` |
| **CollectionSchemaName** | `Reports` |
| **EntitySetName** | `reports`|
| **LogicalName** | `report` |
| **LogicalCollectionName** | `reports` |
| **PrimaryIdAttribute** | `reportid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [BodyBinary](#BKMK_BodyBinary)
- [BodyText](#BKMK_BodyText)
- [BodyUrl](#BKMK_BodyUrl)
- [CreatedInMajorVersion](#BKMK_CreatedInMajorVersion)
- [DefaultFilter](#BKMK_DefaultFilter)
- [DependentModelReportId](#BKMK_DependentModelReportId)
- [Description](#BKMK_Description)
- [FileName](#BKMK_FileName)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsPersonal](#BKMK_IsPersonal)
- [LanguageCode](#BKMK_LanguageCode)
- [ManagedType](#BKMK_ManagedType)
- [MimeType](#BKMK_MimeType)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParentReportId](#BKMK_ParentReportId)
- [PowerBiFeatureTag](#BKMK_PowerBiFeatureTag)
- [ReportId](#BKMK_ReportId)
- [ReportStatus](#BKMK_ReportStatus)
- [ReportTypeCode](#BKMK_ReportTypeCode)
- [ReportVersion](#BKMK_ReportVersion)
- [SignatureDate](#BKMK_SignatureDate)
- [SignatureId](#BKMK_SignatureId)
- [SignatureLcid](#BKMK_SignatureLcid)
- [SignatureMajorVersion](#BKMK_SignatureMajorVersion)
- [SignatureMinorVersion](#BKMK_SignatureMinorVersion)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_BodyBinary"></a> BodyBinary

|Property|Value|
|---|---|
|Description|**Binary report contents (base-64 encoded).**|
|DisplayName|**Body Binary**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`bodybinary`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_BodyText"></a> BodyText

|Property|Value|
|---|---|
|Description|**Text contents of the RDL file for a Reporting Services report.**|
|DisplayName|**Body Text**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`bodytext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_BodyUrl"></a> BodyUrl

|Property|Value|
|---|---|
|Description|**URL for a linked report.**|
|DisplayName|**Linked Report URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`bodyurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_CreatedInMajorVersion"></a> CreatedInMajorVersion

|Property|Value|
|---|---|
|Description|**Major version number of Crm, used to identify the version of Crm in which report is created.**|
|DisplayName|**Crm Version in which the Report is created**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdinmajorversion`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_DefaultFilter"></a> DefaultFilter

|Property|Value|
|---|---|
|Description|**Default filter for the report.**|
|DisplayName|**Default filter**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`defaultfilter`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_DependentModelReportId"></a> DependentModelReportId

|Property|Value|
|---|---|
|Description|**Field to represent the dependent report dataset model.**|
|DisplayName|**Dependent Model Report Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dependentmodelreportid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|report|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the report.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_FileName"></a> FileName

|Property|Value|
|---|---|
|Description|**File name of the report.**|
|DisplayName|**File Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the report is introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsPersonal"></a> IsPersonal

|Property|Value|
|---|---|
|Description|**Information about whether the report is personal or is available to all users.**|
|DisplayName|**Viewable By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispersonal`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`report_ispersonal`|
|DefaultValue|True|
|True Label|Individual|
|False Label|Organization|

### <a name="BKMK_LanguageCode"></a> LanguageCode

|Property|Value|
|---|---|
|Description|**Language in which the report will be displayed.**|
|DisplayName|**Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`languagecode`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ManagedType"></a> ManagedType

|Property|Value|
|---|---|
|Description|**Determine how the report workspace is managed.**|
|DisplayName|**ManagedType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`managedtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`reportentity_managedtype`|

#### ManagedType Choices/Options

|Value|Label|
|---|---|
|0|**Dataverse**|
|1|**Customer**|

### <a name="BKMK_MimeType"></a> MimeType

|Property|Value|
|---|---|
|Description|**MIME type of the report.**|
|DisplayName|**Mime Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mimetype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the report.**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|425|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the report.**|
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

### <a name="BKMK_ParentReportId"></a> ParentReportId

|Property|Value|
|---|---|
|Description|**Unique identifier of the parent report.**|
|DisplayName|**Parent Report**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentreportid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|report|

### <a name="BKMK_PowerBiFeatureTag"></a> PowerBiFeatureTag

|Property|Value|
|---|---|
|Description|**Field to maintain the sub application id and feature tag for powerbi reports.**|
|DisplayName|**powerbifeaturetag**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerbifeaturetag`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_ReportId"></a> ReportId

|Property|Value|
|---|---|
|Description|**Unique identifier of the report.**|
|DisplayName|**Report**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`reportid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ReportStatus"></a> ReportStatus

|Property|Value|
|---|---|
|Description|**Represents the status of the Report.**|
|DisplayName|**Report Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`reportstatus`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ReportTypeCode"></a> ReportTypeCode

|Property|Value|
|---|---|
|Description|**Type of the report.**|
|DisplayName|**Report Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`reporttypecode`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`report_reporttypecode`|

#### ReportTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Reporting Services Report**|
|2|**Other Report**|
|3|**Linked Report**|
|4|**Power BI Paginated Report**|
|5|**Power BI Analytic Report**|
|6|**Excel Embedded Report**|
|7|**Excel Embedded Report Template**|

### <a name="BKMK_ReportVersion"></a> ReportVersion

|Property|Value|
|---|---|
|Description|**Represents the version of a report.**|
|DisplayName|**Report Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`reportversion`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_SignatureDate"></a> SignatureDate

|Property|Value|
|---|---|
|Description|**Report signature date, used to identify a report for upgrades and hotfixes.**|
|DisplayName|**Report Signature Date**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`signaturedate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SignatureId"></a> SignatureId

|Property|Value|
|---|---|
|Description|**Unique identifier of the report signature used to identify a report for upgrades and hotfixes.**|
|DisplayName|**Signature**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`signatureid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_SignatureLcid"></a> SignatureLcid

|Property|Value|
|---|---|
|Description|**Report signature language code used to identify a report for upgrades and hotfixes.**|
|DisplayName|**Signature Language Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`signaturelcid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_SignatureMajorVersion"></a> SignatureMajorVersion

|Property|Value|
|---|---|
|Description|**Report signature major version, used to identify a report for upgrades and hotfixes.**|
|DisplayName|**Report Signature Major Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`signaturemajorversion`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_SignatureMinorVersion"></a> SignatureMinorVersion

|Property|Value|
|---|---|
|Description|**Report signature minor version, used to identify a report for upgrades and hotfixes.**|
|DisplayName|**Report Signature Minor Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`signatureminorversion`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

- [ApplicationId](#BKMK_ApplicationId)
- [CdsDatasetId](#BKMK_CdsDatasetId)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CustomReportXml](#BKMK_CustomReportXml)
- [FileContent](#BKMK_FileContent)
- [FileContent_Name](#BKMK_FileContent_Name)
- [FileSize](#BKMK_FileSize)
- [IsCustomReport](#BKMK_IsCustomReport)
- [IsManaged](#BKMK_IsManaged)
- [IsScheduledReport](#BKMK_IsScheduledReport)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OriginalBodyText](#BKMK_OriginalBodyText)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PowerBiDatasetId](#BKMK_PowerBiDatasetId)
- [PowerBiReportId](#BKMK_PowerBiReportId)
- [PowerBiReportInternalState](#BKMK_PowerBiReportInternalState)
- [PowerBiReportName](#BKMK_PowerBiReportName)
- [PowerBiWorkspaceInfo](#BKMK_PowerBiWorkspaceInfo)
- [QueryInfo](#BKMK_QueryInfo)
- [RdlHash](#BKMK_RdlHash)
- [ReportIdUnique](#BKMK_ReportIdUnique)
- [ReportNameOnSRS](#BKMK_ReportNameOnSRS)
- [ScheduleXml](#BKMK_ScheduleXml)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ApplicationId"></a> ApplicationId

|Property|Value|
|---|---|
|Description|**Represents the application id to which a CDS powerbi report belongs to.**|
|DisplayName|**ApplicationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicationid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_CdsDatasetId"></a> CdsDatasetId

|Property|Value|
|---|---|
|Description|**Represents the dataset id of a report.**|
|DisplayName|**cdsdatasetid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cdsdatasetid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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
|DefaultFormValue|-1|
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
|Description|**Unique identifier of the user who created the report.**|
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
|Description|**Date and time when the report was created.**|
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
|Description|**Unique identifier of the delegate user who created the report.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CustomReportXml"></a> CustomReportXml

|Property|Value|
|---|---|
|Description|**XML used to define a custom report.**|
|DisplayName|**Custom Report XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customreportxml`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_FileContent"></a> FileContent

|Property|Value|
|---|---|
|Description||
|DisplayName|**File Content**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`filecontent`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|10485760|

### <a name="BKMK_FileContent_Name"></a> FileContent_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filecontent_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_FileSize"></a> FileSize

|Property|Value|
|---|---|
|Description|**File size of the report.**|
|DisplayName|**File Size (Bytes)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filesize`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_IsCustomReport"></a> IsCustomReport

|Property|Value|
|---|---|
|Description|**Information about whether the report is a custom report.**|
|DisplayName|**Is Custom Report**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomreport`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`report_iscustomreport`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

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

### <a name="BKMK_IsScheduledReport"></a> IsScheduledReport

|Property|Value|
|---|---|
|Description|**Information about whether the report is a scheduled report.**|
|DisplayName|**Is Scheduled Report**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isscheduledreport`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`report_isscheduledreport`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the report.**|
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
|Description|**Date and time when the report was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the report.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OriginalBodyText"></a> OriginalBodyText

|Property|Value|
|---|---|
|Description|**Original Text contents of the RDL file for a Reporting Services report.**|
|DisplayName|**Body Text**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`originalbodytext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

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
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

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
|Description|**Unique identifier of the business unit that owns the report.**|
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
|Description|**Unique identifier of the team who owns the report.**|
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
|Description|**Unique identifier of the user who owns the report.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_PowerBiDatasetId"></a> PowerBiDatasetId

|Property|Value|
|---|---|
|Description|**Represents the Power BI dataset id of a report.**|
|DisplayName|**PowerBI Dataset Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerbidatasetid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_PowerBiReportId"></a> PowerBiReportId

|Property|Value|
|---|---|
|Description|**Represents the powerbi report id for a CDS report.**|
|DisplayName|**PowerBiReportId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerbireportid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_PowerBiReportInternalState"></a> PowerBiReportInternalState

|Property|Value|
|---|---|
|Description|**Field to maintain the internal state of the report**|
|DisplayName|**powerbireportinternalstate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerbireportinternalstate`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_PowerBiReportName"></a> PowerBiReportName

|Property|Value|
|---|---|
|Description|**Contains the name of the Power Bi embedded report.**|
|DisplayName|**Power Bi Report Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`powerbireportname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_PowerBiWorkspaceInfo"></a> PowerBiWorkspaceInfo

|Property|Value|
|---|---|
|Description|**Contains the workspace information of the Power Bi embedded report.**|
|DisplayName|**Power Bi Workspace Information**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerbiworkspaceinfo`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_QueryInfo"></a> QueryInfo

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Query Info Structure**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`queryinfo`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_RdlHash"></a> RdlHash

|Property|Value|
|---|---|
|Description|**Hash value of the body text of the report.**|
|DisplayName|**Body Text Hash**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rdlhash`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ReportIdUnique"></a> ReportIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Report**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`reportidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ReportNameOnSRS"></a> ReportNameOnSRS

|Property|Value|
|---|---|
|Description|**Name of the report on SRS.**|
|DisplayName|**Name on SRS**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`reportnameonsrs`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|425|

### <a name="BKMK_ScheduleXml"></a> ScheduleXml

|Property|Value|
|---|---|
|Description|**XML used for defining the report schedule.**|
|DisplayName|**Schedule Definition XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`schedulexml`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

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
|Description|**Version number of the report.**|
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

- [business_unit_reports](#BKMK_business_unit_reports)
- [FileAttachment_Report_FileContent](#BKMK_FileAttachment_Report_FileContent)
- [lk_report_createdonbehalfby](#BKMK_lk_report_createdonbehalfby)
- [lk_report_modifiedonbehalfby](#BKMK_lk_report_modifiedonbehalfby)
- [lk_reportbase_createdby](#BKMK_lk_reportbase_createdby)
- [lk_reportbase_modifiedby](#BKMK_lk_reportbase_modifiedby)
- [owner_reports](#BKMK_owner_reports)
- [report_parent_report](#BKMK_report_parent_report-many-to-one)
- [Report_Report_DependentModelReportId](#BKMK_Report_Report_DependentModelReportId-many-to-one)

### <a name="BKMK_business_unit_reports"></a> business_unit_reports

One-To-Many Relationship: [businessunit business_unit_reports](businessunit.md#BKMK_business_unit_reports)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_Report_FileContent"></a> FileAttachment_Report_FileContent

One-To-Many Relationship: [fileattachment FileAttachment_Report_FileContent](fileattachment.md#BKMK_FileAttachment_Report_FileContent)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`filecontent`|
|ReferencingEntityNavigationPropertyName|`filecontent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_report_createdonbehalfby"></a> lk_report_createdonbehalfby

One-To-Many Relationship: [systemuser lk_report_createdonbehalfby](systemuser.md#BKMK_lk_report_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_report_modifiedonbehalfby"></a> lk_report_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_report_modifiedonbehalfby](systemuser.md#BKMK_lk_report_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_reportbase_createdby"></a> lk_reportbase_createdby

One-To-Many Relationship: [systemuser lk_reportbase_createdby](systemuser.md#BKMK_lk_reportbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_reportbase_modifiedby"></a> lk_reportbase_modifiedby

One-To-Many Relationship: [systemuser lk_reportbase_modifiedby](systemuser.md#BKMK_lk_reportbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_reports"></a> owner_reports

One-To-Many Relationship: [owner owner_reports](owner.md#BKMK_owner_reports)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_report_parent_report-many-to-one"></a> report_parent_report

One-To-Many Relationship: [report report_parent_report](#BKMK_report_parent_report-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`report`|
|ReferencedAttribute|`reportid`|
|ReferencingAttribute|`parentreportid`|
|ReferencingEntityNavigationPropertyName|`parentreportid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_Report_Report_DependentModelReportId-many-to-one"></a> Report_Report_DependentModelReportId

One-To-Many Relationship: [report Report_Report_DependentModelReportId](#BKMK_Report_Report_DependentModelReportId-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`report`|
|ReferencedAttribute|`reportid`|
|ReferencingAttribute|`dependentmodelreportid`|
|ReferencingEntityNavigationPropertyName|`DependentModelReportId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [Report_AsyncOperations](#BKMK_Report_AsyncOperations)
- [report_FileAttachments](#BKMK_report_FileAttachments)
- [report_parent_report](#BKMK_report_parent_report-one-to-many)
- [Report_ProcessSessions](#BKMK_Report_ProcessSessions)
- [Report_Report_DependentModelReportId](#BKMK_Report_Report_DependentModelReportId-one-to-many)
- [report_reportcategories](#BKMK_report_reportcategories)
- [Report_ReportParameter_ReportId](#BKMK_Report_ReportParameter_ReportId)
- [Report_SyncErrors](#BKMK_Report_SyncErrors)

### <a name="BKMK_Report_AsyncOperations"></a> Report_AsyncOperations

Many-To-One Relationship: [asyncoperation Report_AsyncOperations](asyncoperation.md#BKMK_Report_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Report_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_report_FileAttachments"></a> report_FileAttachments

Many-To-One Relationship: [fileattachment report_FileAttachments](fileattachment.md#BKMK_report_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`report_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_report_parent_report-one-to-many"></a> report_parent_report

Many-To-One Relationship: [report report_parent_report](#BKMK_report_parent_report-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`report`|
|ReferencingAttribute|`parentreportid`|
|ReferencedEntityNavigationPropertyName|`report_parent_report`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Report_ProcessSessions"></a> Report_ProcessSessions

Many-To-One Relationship: [processsession Report_ProcessSessions](processsession.md#BKMK_Report_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Report_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Report_Report_DependentModelReportId-one-to-many"></a> Report_Report_DependentModelReportId

Many-To-One Relationship: [report Report_Report_DependentModelReportId](#BKMK_Report_Report_DependentModelReportId-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`report`|
|ReferencingAttribute|`dependentmodelreportid`|
|ReferencedEntityNavigationPropertyName|`Report_Report_DependentModelReportId`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_report_reportcategories"></a> report_reportcategories

Many-To-One Relationship: [reportcategory report_reportcategories](reportcategory.md#BKMK_report_reportcategories)

|Property|Value|
|---|---|
|ReferencingEntity|`reportcategory`|
|ReferencingAttribute|`reportid`|
|ReferencedEntityNavigationPropertyName|`report_reportcategories`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Report_ReportParameter_ReportId"></a> Report_ReportParameter_ReportId

Many-To-One Relationship: [reportparameter Report_ReportParameter_ReportId](reportparameter.md#BKMK_Report_ReportParameter_ReportId)

|Property|Value|
|---|---|
|ReferencingEntity|`reportparameter`|
|ReferencingAttribute|`reportid`|
|ReferencedEntityNavigationPropertyName|`Report_ReportParameters`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: Represents collection of ReportParameters belonging to a Report.<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Report_SyncErrors"></a> Report_SyncErrors

Many-To-One Relationship: [syncerror Report_SyncErrors](syncerror.md#BKMK_Report_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Report_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.report?displayProperty=fullName>
