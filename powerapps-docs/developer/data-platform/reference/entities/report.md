---
title: "Report table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Report table/entity."
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

# Report table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Data summary in an easy-to-read layout.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/reports(*reportid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/reports<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/reports(*reportid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|DownloadReportDefinition|<xref href="Microsoft.Dynamics.CRM.DownloadReportDefinition?text=DownloadReportDefinition Function" />|<xref:Microsoft.Crm.Sdk.Messages.DownloadReportDefinitionRequest>|
|GetReportHistoryLimit|<xref href="Microsoft.Dynamics.CRM.GetReportHistoryLimit?text=GetReportHistoryLimit Function" />|<xref:Microsoft.Crm.Sdk.Messages.GetReportHistoryLimitRequest>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/reports(*reportid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/reports<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetReportRelated|<xref href="Microsoft.Dynamics.CRM.SetReportRelated?text=SetReportRelated Action" />|<xref:Microsoft.Crm.Sdk.Messages.SetReportRelatedRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/reports(*reportid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Reports|
|DisplayCollectionName|Reports|
|DisplayName|Report|
|EntitySetName|reports|
|IsBPFEntity|False|
|LogicalCollectionName|reports|
|LogicalName|report|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|reportid|
|PrimaryNameAttribute|name|
|SchemaName|Report|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [BodyBinary](#BKMK_BodyBinary)
- [BodyText](#BKMK_BodyText)
- [BodyUrl](#BKMK_BodyUrl)
- [CreatedInMajorVersion](#BKMK_CreatedInMajorVersion)
- [DefaultFilter](#BKMK_DefaultFilter)
- [Description](#BKMK_Description)
- [FileName](#BKMK_FileName)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsPersonal](#BKMK_IsPersonal)
- [LanguageCode](#BKMK_LanguageCode)
- [MimeType](#BKMK_MimeType)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParentReportId](#BKMK_ParentReportId)
- [ReportId](#BKMK_ReportId)
- [ReportTypeCode](#BKMK_ReportTypeCode)
- [SignatureDate](#BKMK_SignatureDate)
- [SignatureId](#BKMK_SignatureId)
- [SignatureLcid](#BKMK_SignatureLcid)
- [SignatureMajorVersion](#BKMK_SignatureMajorVersion)
- [SignatureMinorVersion](#BKMK_SignatureMinorVersion)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_BodyBinary"></a> BodyBinary

|Property|Value|
|--------|-----|
|Description|Binary report contents (base-64 encoded).|
|DisplayName|Body Binary|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|bodybinary|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_BodyText"></a> BodyText

|Property|Value|
|--------|-----|
|Description|Text contents of the RDL file for a Reporting Services report.|
|DisplayName|Body Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|bodytext|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_BodyUrl"></a> BodyUrl

|Property|Value|
|--------|-----|
|Description|URL for a linked report.|
|DisplayName|Linked Report URL|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|bodyurl|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedInMajorVersion"></a> CreatedInMajorVersion

|Property|Value|
|--------|-----|
|Description|Major version number of Crm, used to identify the version of Crm in which report is created.|
|DisplayName|Crm Version in which the Report is created|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|createdinmajorversion|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_DefaultFilter"></a> DefaultFilter

|Property|Value|
|--------|-----|
|Description|Default filter for the report.|
|DisplayName|Default filter|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|defaultfilter|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the report.|
|DisplayName|Description|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FileName"></a> FileName

|Property|Value|
|--------|-----|
|Description|File name of the report.|
|DisplayName|File Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|filename|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the report is introduced.|
|DisplayName|Introduced Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|introducedversion|
|MaxLength|48|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component can be customized.|
|DisplayName|Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_IsPersonal"></a> IsPersonal

|Property|Value|
|--------|-----|
|Description|Information about whether the report is personal or is available to all users.|
|DisplayName|Viewable By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ispersonal|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsPersonal Choices/Options

|Value|Label|
|-----|-----|
|1|Individual|
|0|Organization|

**DefaultValue**: True



### <a name="BKMK_LanguageCode"></a> LanguageCode

|Property|Value|
|--------|-----|
|Description|Language in which the report will be displayed.|
|DisplayName|Language|
|Format|Language|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|languagecode|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_MimeType"></a> MimeType

|Property|Value|
|--------|-----|
|Description|MIME type of the report.|
|DisplayName|Mime Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mimetype|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the report.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|425|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the report.|
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


### <a name="BKMK_ParentReportId"></a> ParentReportId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the parent report.|
|DisplayName|Parent Report|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentreportid|
|RequiredLevel|None|
|Targets|report|
|Type|Lookup|


### <a name="BKMK_ReportId"></a> ReportId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the report.|
|DisplayName|Report|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|reportid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ReportTypeCode"></a> ReportTypeCode

|Property|Value|
|--------|-----|
|Description|Type of the report.|
|DisplayName|Report Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|reporttypecode|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### ReportTypeCode Choices/Options

|Value|Label|
|-----|-----|
|1|Reporting Services Report|
|2|Other Report|
|3|Linked Report|



### <a name="BKMK_SignatureDate"></a> SignatureDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Report signature date, used to identify a report for upgrades and hotfixes.|
|DisplayName|Report Signature Date|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|signaturedate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_SignatureId"></a> SignatureId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the report signature used to identify a report for upgrades and hotfixes.|
|DisplayName|Signature|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|signatureid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_SignatureLcid"></a> SignatureLcid

|Property|Value|
|--------|-----|
|Description|Report signature language code used to identify a report for upgrades and hotfixes.|
|DisplayName|Signature Language Code|
|Format|Language|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|signaturelcid|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_SignatureMajorVersion"></a> SignatureMajorVersion

|Property|Value|
|--------|-----|
|Description|Report signature major version, used to identify a report for upgrades and hotfixes.|
|DisplayName|Report Signature Major Version|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|signaturemajorversion|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_SignatureMinorVersion"></a> SignatureMinorVersion

|Property|Value|
|--------|-----|
|Description|Report signature minor version, used to identify a report for upgrades and hotfixes.|
|DisplayName|Report Signature Minor Version|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|signatureminorversion|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
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

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomReportXml](#BKMK_CustomReportXml)
- [FileSize](#BKMK_FileSize)
- [IsCustomReport](#BKMK_IsCustomReport)
- [IsManaged](#BKMK_IsManaged)
- [IsScheduledReport](#BKMK_IsScheduledReport)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OriginalBodyText](#BKMK_OriginalBodyText)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ParentReportIdName](#BKMK_ParentReportIdName)
- [QueryInfo](#BKMK_QueryInfo)
- [RdlHash](#BKMK_RdlHash)
- [ReportIdUnique](#BKMK_ReportIdUnique)
- [ReportNameOnSRS](#BKMK_ReportNameOnSRS)
- [ScheduleXml](#BKMK_ScheduleXml)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|
|-----|-----|
|0|Published|
|1|Unpublished|
|2|Deleted|
|3|Deleted Unpublished|



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the report.|
|DisplayName|Created By|
|IsValidForForm|True|
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
|Description|Date and time when the report was created.|
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
|Description|Unique identifier of the delegate user who created the report.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
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


### <a name="BKMK_CustomReportXml"></a> CustomReportXml

|Property|Value|
|--------|-----|
|Description|XML used to define a custom report.|
|DisplayName|Custom Report XML|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|customreportxml|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FileSize"></a> FileSize

|Property|Value|
|--------|-----|
|Description|File size of the report.|
|DisplayName|File Size (Bytes)|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|filesize|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsCustomReport"></a> IsCustomReport

|Property|Value|
|--------|-----|
|Description|Information about whether the report is a custom report.|
|DisplayName|Is Custom Report|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomreport|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsCustomReport Choices/Options

|Value|Label|
|-----|-----|
|1|True|
|0|False|

**DefaultValue**: False



### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|Indicates whether the solution component is part of a managed solution.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|
|-----|-----|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_IsScheduledReport"></a> IsScheduledReport

|Property|Value|
|--------|-----|
|Description|Information about whether the report is a scheduled report.|
|DisplayName|Is Scheduled Report|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isscheduledreport|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsScheduledReport Choices/Options

|Value|Label|
|-----|-----|
|1|True|
|0|False|

**DefaultValue**: False



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the report.|
|DisplayName|Modified By|
|IsValidForForm|True|
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
|Description|Date and time when the report was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the report.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
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


### <a name="BKMK_OriginalBodyText"></a> OriginalBodyText

|Property|Value|
|--------|-----|
|Description|Original Text contents of the RDL file for a Reporting Services report.|
|DisplayName|Body Text|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|originalbodytext|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


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
|Description|Unique identifier of the business unit that owns the report.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the report.|
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
|Description|Unique identifier of the user who owns the report.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ParentReportIdName"></a> ParentReportIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentreportidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_QueryInfo"></a> QueryInfo

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Query Info Structure|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|queryinfo|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RdlHash"></a> RdlHash

|Property|Value|
|--------|-----|
|Description|Hash value of the body text of the report.|
|DisplayName|Body Text Hash|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rdlhash|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ReportIdUnique"></a> ReportIdUnique

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Report|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|reportidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ReportNameOnSRS"></a> ReportNameOnSRS

|Property|Value|
|--------|-----|
|Description|Name of the report on SRS.|
|DisplayName|Name on SRS|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|reportnameonsrs|
|MaxLength|425|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ScheduleXml"></a> ScheduleXml

|Property|Value|
|--------|-----|
|Description|XML used for defining the report schedule.|
|DisplayName|Schedule Definition XML|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|schedulexml|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the report.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [Report_ProcessSessions](#BKMK_Report_ProcessSessions)
- [Report_SyncErrors](#BKMK_Report_SyncErrors)
- [Report_AsyncOperations](#BKMK_Report_AsyncOperations)
- [report_reportcategories](#BKMK_report_reportcategories)
- [report_parent_report](#BKMK_report_parent_report)


### <a name="BKMK_Report_ProcessSessions"></a> Report_ProcessSessions

Same as processsession table [Report_ProcessSessions](processsession.md#BKMK_Report_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Report_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Report_SyncErrors"></a> Report_SyncErrors

Same as syncerror table [Report_SyncErrors](syncerror.md#BKMK_Report_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Report_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Report_AsyncOperations"></a> Report_AsyncOperations

Same as asyncoperation table [Report_AsyncOperations](asyncoperation.md#BKMK_Report_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Report_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_report_reportcategories"></a> report_reportcategories

Same as reportcategory table [report_reportcategories](reportcategory.md#BKMK_report_reportcategories) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|reportcategory|
|ReferencingAttribute|reportid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|report_reportcategories|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_report_parent_report"></a> report_parent_report

Same as report table [report_parent_report](report.md#BKMK_report_parent_report) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|report|
|ReferencingAttribute|parentreportid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|report_parent_report|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_report_createdonbehalfby](#BKMK_lk_report_createdonbehalfby)
- [lk_report_modifiedonbehalfby](#BKMK_lk_report_modifiedonbehalfby)
- [report_parent_report](#BKMK_report_parent_report)
- [lk_reportbase_modifiedby](#BKMK_lk_reportbase_modifiedby)
- [business_unit_reports](#BKMK_business_unit_reports)
- [lk_reportbase_createdby](#BKMK_lk_reportbase_createdby)


### <a name="BKMK_lk_report_createdonbehalfby"></a> lk_report_createdonbehalfby

See systemuser Table [lk_report_createdonbehalfby](systemuser.md#BKMK_lk_report_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_report_modifiedonbehalfby"></a> lk_report_modifiedonbehalfby

See systemuser Table [lk_report_modifiedonbehalfby](systemuser.md#BKMK_lk_report_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_report_parent_report"></a> report_parent_report

See report Table [report_parent_report](report.md#BKMK_report_parent_report) One-To-Many relationship.

### <a name="BKMK_lk_reportbase_modifiedby"></a> lk_reportbase_modifiedby

See systemuser Table [lk_reportbase_modifiedby](systemuser.md#BKMK_lk_reportbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_business_unit_reports"></a> business_unit_reports

See businessunit Table [business_unit_reports](businessunit.md#BKMK_business_unit_reports) One-To-Many relationship.

### <a name="BKMK_lk_reportbase_createdby"></a> lk_reportbase_createdby

See systemuser Table [lk_reportbase_createdby](systemuser.md#BKMK_lk_reportbase_createdby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.report?text=report EntityType" />