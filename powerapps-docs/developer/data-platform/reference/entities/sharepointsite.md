---
title: "SharePoint Site (SharePointSite) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the SharePoint Site (SharePointSite) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# SharePoint Site (SharePointSite) table/entity reference (Microsoft Dataverse)

SharePoint site from where documents can be managed in Microsoft Dynamics 365.

## Messages

The following table lists the messages for the SharePoint Site (SharePointSite) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /sharepointsites(*sharepointsiteid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /sharepointsites<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /sharepointsites(*sharepointsiteid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /sharepointsites(*sharepointsiteid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveAbsoluteAndSiteCollectionUrl`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveAbsoluteAndSiteCollectionUrl?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveAbsoluteAndSiteCollectionUrlRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /sharepointsites<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /sharepointsites(*sharepointsiteid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /sharepointsites(*sharepointsiteid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /sharepointsites(*sharepointsiteid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the SharePoint Site (SharePointSite) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **SharePoint Site** |
| **DisplayCollectionName** | **SharePoint Sites** |
| **SchemaName** | `SharePointSite` |
| **CollectionSchemaName** | `SharePointSites` |
| **EntitySetName** | `sharepointsites`|
| **LogicalName** | `sharepointsite` |
| **LogicalCollectionName** | `sharepointsites` |
| **PrimaryIdAttribute** | `sharepointsiteid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AbsoluteURL](#BKMK_AbsoluteURL)
- [Description](#BKMK_Description)
- [FolderStructureEntity](#BKMK_FolderStructureEntity)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsDefault](#BKMK_IsDefault)
- [IsGridPresent](#BKMK_IsGridPresent)
- [IsPowerBISite](#BKMK_IsPowerBISite)
- [LastValidated](#BKMK_LastValidated)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParentSite](#BKMK_ParentSite)
- [ParentSiteObjectTypeCode](#BKMK_ParentSiteObjectTypeCode)
- [RelativeUrl](#BKMK_RelativeUrl)
- [ServiceType](#BKMK_ServiceType)
- [SharePointSiteId](#BKMK_SharePointSiteId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UserId](#BKMK_UserId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [ValidationStatus](#BKMK_ValidationStatus)
- [ValidationStatusErrorCode](#BKMK_ValidationStatusErrorCode)

### <a name="BKMK_AbsoluteURL"></a> AbsoluteURL

|Property|Value|
|---|---|
|Description|**Absolute URL of the SharePoint site.**|
|DisplayName|**Absolute URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`absoluteurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the SharePoint site record.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_FolderStructureEntity"></a> FolderStructureEntity

|Property|Value|
|---|---|
|Description|**Entity on which the folder structure for Microsoft Dynamics 365 records will be created in SharePoint.**|
|DisplayName|**Entity for SharePoint Folder Structure**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`folderstructureentity`|
|RequiredLevel|None|
|Type|EntityName|

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

### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|---|---|
|Description|**Indicates whether the SharePoint site is the default site or not.**|
|DisplayName|**Default Site**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdefault`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sharepointsite_isdefault`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsGridPresent"></a> IsGridPresent

|Property|Value|
|---|---|
|Description|**Indicates if SharePoint Grid is present or not.**|
|DisplayName|**List component is installed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isgridpresent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sharepointsite_isgridpresent`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPowerBISite"></a> IsPowerBISite

|Property|Value|
|---|---|
|Description|**Allows embedding of Power BI Reports available in this SharePoint site.**|
|DisplayName|**Allow Embedding of Power BI Reports**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ispowerbisite`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`sharepointsite_ispowerbisite`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_LastValidated"></a> LastValidated

|Property|Value|
|---|---|
|Description|**Date and time when the SharePoint site URL was last validated.**|
|DisplayName|**Last Validated**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastvalidated`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the SharePoint site record.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

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
|Description|**Unique identifier of the user or team who owns the SharePoint site.**|
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

### <a name="BKMK_ParentSite"></a> ParentSite

|Property|Value|
|---|---|
|Description|**Unique identifier of the parent SharePoint site.**|
|DisplayName|**Parent Site**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentsite`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sharepointsite|

### <a name="BKMK_ParentSiteObjectTypeCode"></a> ParentSiteObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentsiteobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_RelativeUrl"></a> RelativeUrl

|Property|Value|
|---|---|
|Description|**Relative URL of the SharePoint site.**|
|DisplayName|**Relative URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`relativeurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_ServiceType"></a> ServiceType

|Property|Value|
|---|---|
|Description|**Shows the service type of location of the SharePoint site.**|
|DisplayName|**Service Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`servicetype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sharepointsite_servicetype`|

#### ServiceType Choices/Options

|Value|Label|
|---|---|
|0|**SharePoint**|
|1|**OneDrive**|
|2|**Shared with me**|
|3|**MS Teams**|

### <a name="BKMK_SharePointSiteId"></a> SharePointSiteId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SharePoint site in Dynamics 365**|
|DisplayName|**SharePoint Site ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sharepointsiteid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the SharePoint site record.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`sharepointsite_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the SharePoint site record.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`sharepointsite_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

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

### <a name="BKMK_UserId"></a> UserId

|Property|Value|
|---|---|
|Description|**Choose the user who owns the SharePoint site.**|
|DisplayName|**SharePoint Site Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`userid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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

### <a name="BKMK_ValidationStatus"></a> ValidationStatus

|Property|Value|
|---|---|
|Description|**Validation status of the SharePoint site URL.**|
|DisplayName|**Last Validation Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`validationstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`sharepoint_validationstatus`|

#### ValidationStatus Choices/Options

|Value|Label|
|---|---|
|1|**Not Validated**|
|2|**In Progress**|
|3|**Invalid**|
|4|**Valid**|
|5|**Could not validate**|

### <a name="BKMK_ValidationStatusErrorCode"></a> ValidationStatusErrorCode

|Property|Value|
|---|---|
|Description|**Reason for validation status of the URL**|
|DisplayName|**Additional Information**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`validationstatuserrorcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`sharepoint_validationstatusreason`|

#### ValidationStatusErrorCode Choices/Options

|Value|Label|
|---|---|
|1|**This record's URL has not been validated.**|
|2|**This record's URL is valid.**|
|3|**This record's URL is not valid.**|
|4|**The URL schemes of Microsoft Dynamics 365 and SharePoint are different.**|
|5|**The URL could not be accessed because of Internet Explorer security settings.**|
|6|**Authentication failure.**|
|7|**Invalid certificates.**|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SiteCollectionId](#BKMK_SiteCollectionId)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the SharePoint site record.**|
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
|Description|**Date and time when the SharePoint site record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who created the SharePoint site record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate between the currency associated with the SharePoint site record and the base currency.**|
|DisplayName|**Exchange Rate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the SharePoint site record.**|
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
|Description|**Date and time when the SharePoint site record was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who modified the SharePoint site record.**|
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
|Description|**Unique identifier for the business unit that owns the document location record.**|
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
|Description|**Unique identifier of the team that owns the SharePoint site record.**|
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
|Description|**Unique identifier of the user who owns the SharePoint site record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_SiteCollectionId"></a> SiteCollectionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sitecollectionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the currency associated with the SharePoint site record.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_sharepointsites](#BKMK_business_unit_sharepointsites)
- [lk_sharepointsitebase_createdby](#BKMK_lk_sharepointsitebase_createdby)
- [lk_sharepointsitebase_createdonbehalfby](#BKMK_lk_sharepointsitebase_createdonbehalfby)
- [lk_sharepointsitebase_modifiedby](#BKMK_lk_sharepointsitebase_modifiedby)
- [lk_sharepointsitebase_modifiedonbehalfby](#BKMK_lk_sharepointsitebase_modifiedonbehalfby)
- [owner_sharepointsite](#BKMK_owner_sharepointsite)
- [sharepointsite_parentsite_sharepointsite](#BKMK_sharepointsite_parentsite_sharepointsite-many-to-one)
- [team_sharepointsite](#BKMK_team_sharepointsite)
- [TransactionCurrency_SharePointSite](#BKMK_TransactionCurrency_SharePointSite)
- [user_sharepointsite](#BKMK_user_sharepointsite)

### <a name="BKMK_business_unit_sharepointsites"></a> business_unit_sharepointsites

One-To-Many Relationship: [businessunit business_unit_sharepointsites](businessunit.md#BKMK_business_unit_sharepointsites)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sharepointsitebase_createdby"></a> lk_sharepointsitebase_createdby

One-To-Many Relationship: [systemuser lk_sharepointsitebase_createdby](systemuser.md#BKMK_lk_sharepointsitebase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sharepointsitebase_createdonbehalfby"></a> lk_sharepointsitebase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sharepointsitebase_createdonbehalfby](systemuser.md#BKMK_lk_sharepointsitebase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sharepointsitebase_modifiedby"></a> lk_sharepointsitebase_modifiedby

One-To-Many Relationship: [systemuser lk_sharepointsitebase_modifiedby](systemuser.md#BKMK_lk_sharepointsitebase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sharepointsitebase_modifiedonbehalfby"></a> lk_sharepointsitebase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sharepointsitebase_modifiedonbehalfby](systemuser.md#BKMK_lk_sharepointsitebase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_sharepointsite"></a> owner_sharepointsite

One-To-Many Relationship: [owner owner_sharepointsite](owner.md#BKMK_owner_sharepointsite)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sharepointsite_parentsite_sharepointsite-many-to-one"></a> sharepointsite_parentsite_sharepointsite

One-To-Many Relationship: [sharepointsite sharepointsite_parentsite_sharepointsite](#BKMK_sharepointsite_parentsite_sharepointsite-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`sharepointsite`|
|ReferencedAttribute|`sharepointsiteid`|
|ReferencingAttribute|`parentsite`|
|ReferencingEntityNavigationPropertyName|`parentsite`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_sharepointsite"></a> team_sharepointsite

One-To-Many Relationship: [team team_sharepointsite](team.md#BKMK_team_sharepointsite)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_SharePointSite"></a> TransactionCurrency_SharePointSite

One-To-Many Relationship: [transactioncurrency TransactionCurrency_SharePointSite](transactioncurrency.md#BKMK_TransactionCurrency_SharePointSite)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_sharepointsite"></a> user_sharepointsite

One-To-Many Relationship: [systemuser user_sharepointsite](systemuser.md#BKMK_user_sharepointsite)

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

- [sharepointdocumentlocation_parent_sharepointsite](#BKMK_sharepointdocumentlocation_parent_sharepointsite)
- [SharePointSite_AsyncOperations](#BKMK_SharePointSite_AsyncOperations)
- [SharePointSite_DuplicateBaseRecord](#BKMK_SharePointSite_DuplicateBaseRecord)
- [SharePointSite_DuplicateMatchingRecord](#BKMK_SharePointSite_DuplicateMatchingRecord)
- [sharepointsite_parentsite_sharepointsite](#BKMK_sharepointsite_parentsite_sharepointsite-one-to-many)
- [sharepointsite_principalobjectattributeaccess](#BKMK_sharepointsite_principalobjectattributeaccess)
- [SharePointSite_ProcessSessions](#BKMK_SharePointSite_ProcessSessions)
- [SharePointSite_SyncErrors](#BKMK_SharePointSite_SyncErrors)

### <a name="BKMK_sharepointdocumentlocation_parent_sharepointsite"></a> sharepointdocumentlocation_parent_sharepointsite

Many-To-One Relationship: [sharepointdocumentlocation sharepointdocumentlocation_parent_sharepointsite](sharepointdocumentlocation.md#BKMK_sharepointdocumentlocation_parent_sharepointsite)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointdocumentlocation`|
|ReferencingAttribute|`parentsiteorlocation`|
|ReferencedEntityNavigationPropertyName|`sharepointdocumentlocation_parent_sharepointsite`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 40<br />QueryApi: `CRMSharePointDocumentLocation.RetrieveSubSharePointDocumentLocations`<br />ViewId: `757f2447-c680-437b-8d46-0d5f84cc2f03`|

### <a name="BKMK_SharePointSite_AsyncOperations"></a> SharePointSite_AsyncOperations

Many-To-One Relationship: [asyncoperation SharePointSite_AsyncOperations](asyncoperation.md#BKMK_SharePointSite_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SharePointSite_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SharePointSite_DuplicateBaseRecord"></a> SharePointSite_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord SharePointSite_DuplicateBaseRecord](duplicaterecord.md#BKMK_SharePointSite_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`SharePointSite_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SharePointSite_DuplicateMatchingRecord"></a> SharePointSite_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord SharePointSite_DuplicateMatchingRecord](duplicaterecord.md#BKMK_SharePointSite_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`SharePointSite_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sharepointsite_parentsite_sharepointsite-one-to-many"></a> sharepointsite_parentsite_sharepointsite

Many-To-One Relationship: [sharepointsite sharepointsite_parentsite_sharepointsite](#BKMK_sharepointsite_parentsite_sharepointsite-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointsite`|
|ReferencingAttribute|`parentsite`|
|ReferencedEntityNavigationPropertyName|`sharepointsite_parentsite_sharepointsite`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 40<br />QueryApi: `CRMSharePointSites.RetrieveSharePointSubSites`<br />ViewId: `df2fe6da-f97f-4878-80b6-8deb7d9d6a09`|

### <a name="BKMK_sharepointsite_principalobjectattributeaccess"></a> sharepointsite_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess sharepointsite_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_sharepointsite_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`sharepointsite_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SharePointSite_ProcessSessions"></a> SharePointSite_ProcessSessions

Many-To-One Relationship: [processsession SharePointSite_ProcessSessions](processsession.md#BKMK_SharePointSite_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SharePointSite_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SharePointSite_SyncErrors"></a> SharePointSite_SyncErrors

Many-To-One Relationship: [syncerror SharePointSite_SyncErrors](syncerror.md#BKMK_SharePointSite_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SharePointSite_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sharepointsite?displayProperty=fullName>
