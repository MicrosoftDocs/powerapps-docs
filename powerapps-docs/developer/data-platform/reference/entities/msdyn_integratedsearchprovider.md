---
title: "Integrated search provider (msdyn_integratedsearchprovider) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Integrated search provider (msdyn_integratedsearchprovider) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Integrated search provider (msdyn_integratedsearchprovider) table/entity reference (Microsoft Dataverse)

Ingest and search files, documents, or articles from data sources outside of your current Dynamics 365 organization with a unified ranking.

## Messages

The following table lists the messages for the Integrated search provider (msdyn_integratedsearchprovider) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_integratedsearchproviders(*msdyn_integratedsearchproviderid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_integratedsearchproviders<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_integratedsearchproviders(*msdyn_integratedsearchproviderid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_integratedsearchproviders(*msdyn_integratedsearchproviderid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_integratedsearchproviders<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_integratedsearchproviders(*msdyn_integratedsearchproviderid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_integratedsearchproviders(*msdyn_integratedsearchproviderid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_integratedsearchproviders(*msdyn_integratedsearchproviderid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Integrated search provider (msdyn_integratedsearchprovider) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Integrated search provider** |
| **DisplayCollectionName** | **Integrated search providers** |
| **SchemaName** | `msdyn_integratedsearchprovider` |
| **CollectionSchemaName** | `msdyn_integratedsearchproviders` |
| **EntitySetName** | `msdyn_integratedsearchproviders`|
| **LogicalName** | `msdyn_integratedsearchprovider` |
| **LogicalCollectionName** | `msdyn_integratedsearchproviders` |
| **PrimaryIdAttribute** | `msdyn_integratedsearchproviderid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_allowedlanguages](#BKMK_msdyn_allowedlanguages)
- [msdyn_articlepropertiesmapping](#BKMK_msdyn_articlepropertiesmapping)
- [msdyn_authenticationtype](#BKMK_msdyn_authenticationtype)
- [msdyn_clientid](#BKMK_msdyn_clientid)
- [msdyn_clientsecret](#BKMK_msdyn_clientsecret)
- [msdyn_datasourcetype](#BKMK_msdyn_datasourcetype)
- [msdyn_description](#BKMK_msdyn_description)
- [msdyn_htmlmetatags](#BKMK_msdyn_htmlmetatags)
- [msdyn_includedsitemapurls](#BKMK_msdyn_includedsitemapurls)
- [msdyn_integratedsearchproviderId](#BKMK_msdyn_integratedsearchproviderId)
- [msdyn_isfieldmappingoptionselected](#BKMK_msdyn_isfieldmappingoptionselected)
- [msdyn_lastfetchtime](#BKMK_msdyn_lastfetchtime)
- [msdyn_lookbackperiod](#BKMK_msdyn_lookbackperiod)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_refreshschedule](#BKMK_msdyn_refreshschedule)
- [msdyn_resourceid](#BKMK_msdyn_resourceid)
- [msdyn_rooturl](#BKMK_msdyn_rooturl)
- [msdyn_tenantid](#BKMK_msdyn_tenantid)
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

### <a name="BKMK_msdyn_allowedlanguages"></a> msdyn_allowedlanguages

|Property|Value|
|---|---|
|Description|**Languages allowed for ingestion**|
|DisplayName|**Allowed Languages**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_allowedlanguages`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_msdyn_articlepropertiesmapping"></a> msdyn_articlepropertiesmapping

|Property|Value|
|---|---|
|Description|**Map external search provider fields and knowledge article table columns in Dataverse**|
|DisplayName|**Article properties**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_articlepropertiesmapping`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_authenticationtype"></a> msdyn_authenticationtype

|Property|Value|
|---|---|
|Description|**Authentication type for the search provider**|
|DisplayName|**Authentication**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_authenticationtype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`msdyn_integratedsearchprovider_msdyn_authenticationtype`|

#### msdyn_authenticationtype Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**OAuth**|

### <a name="BKMK_msdyn_clientid"></a> msdyn_clientid

|Property|Value|
|---|---|
|Description|**Client ID for the OAuth**|
|DisplayName|**Client ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_clientid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_clientsecret"></a> msdyn_clientsecret

|Property|Value|
|---|---|
|Description|**Secret of the external search provider**|
|DisplayName|**External search provider secret**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_clientsecret`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_datasourcetype"></a> msdyn_datasourcetype

|Property|Value|
|---|---|
|Description|**Type of the external search provider**|
|DisplayName|**External search provider type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_datasourcetype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`msdyn_integratedsearchprovider_msdyn_datasourcetype`|

#### msdyn_datasourcetype Choices/Options

|Value|Label|
|---|---|
|0|**Website**|

### <a name="BKMK_msdyn_description"></a> msdyn_description

|Property|Value|
|---|---|
|Description|**Description of the external search provider**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_htmlmetatags"></a> msdyn_htmlmetatags

|Property|Value|
|---|---|
|Description|**Information about the meta tags extracted from sample dataprovider html**|
|DisplayName|**Html meta tags information**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_htmlmetatags`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_includedsitemapurls"></a> msdyn_includedsitemapurls

|Property|Value|
|---|---|
|Description|**List of URLs that are allowed**|
|DisplayName|**Allowlist URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_includedsitemapurls`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20000|

### <a name="BKMK_msdyn_integratedsearchproviderId"></a> msdyn_integratedsearchproviderId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Integrated search provider**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_integratedsearchproviderid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_isfieldmappingoptionselected"></a> msdyn_isfieldmappingoptionselected

|Property|Value|
|---|---|
|Description|**Value is true when field mapping option is selected**|
|DisplayName|**Is Field Mapping Option Selected**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isfieldmappingoptionselected`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_integratedsearchprovider_msdyn_isfieldmappingoptionselected`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_lastfetchtime"></a> msdyn_lastfetchtime

|Property|Value|
|---|---|
|Description|**Date and time at which the recent ingestion was started**|
|DisplayName|**Last fetch time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lastfetchtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_lookbackperiod"></a> msdyn_lookbackperiod

|Property|Value|
|---|---|
|Description|**Time interval for ingesting any articles that might have been missed during the sync and ingestion overlap**|
|DisplayName|**Lookback period**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lookbackperiod`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`msdyn_integratedsearchprovider_msdyn_lookbackperiod`|

#### msdyn_lookbackperiod Choices/Options

|Value|Label|
|---|---|
|0|**No Lookback**|
|1|**2 hours**|
|2|**4 hours**|
|3|**6 hours**|
|4|**8 hours**|
|5|**30 mins**|
|6|**1 hour**|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**Name of the external search provider**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_msdyn_refreshschedule"></a> msdyn_refreshschedule

|Property|Value|
|---|---|
|Description|**Time interval for ingesting newly created and updated articles from the external search provider**|
|DisplayName|**Refresh schedule**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_refreshschedule`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`msdyn_integratedsearchprovider_msdyn_refreshschedule`|

#### msdyn_refreshschedule Choices/Options

|Value|Label|
|---|---|
|0|**No refresh**|
|1|**15 mins**|
|2|**30 mins**|
|3|**45 mins**|
|4|**1 hour**|
|5|**2 hours**|
|6|**4 hours**|
|7|**8 hours**|
|8|**1 day**|
|9|**2 days**|
|10|**4 days**|
|11|**7 days**|

### <a name="BKMK_msdyn_resourceid"></a> msdyn_resourceid

|Property|Value|
|---|---|
|Description|**Resource ID for OAuth**|
|DisplayName|**Resource ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_resourceid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_msdyn_rooturl"></a> msdyn_rooturl

|Property|Value|
|---|---|
|Description|**Root URL of the website**|
|DisplayName|**Root URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_rooturl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_msdyn_tenantid"></a> msdyn_tenantid

|Property|Value|
|---|---|
|Description|**Tenant ID for OAuth**|
|DisplayName|**Tenant ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_tenantid`|
|RequiredLevel|None|
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
|Description|**Owner of the external search provider record**|
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
|Description|**State of the external search provider**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_integratedsearchprovider_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Integrated search provider**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_integratedsearchprovider_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Ingestion Ready**<br />State:0<br />TransitionData: None|
|2|Label: **Validated**<br />State:1<br />TransitionData: None|
|3|Label: **Draft**<br />State:1<br />TransitionData: None|

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
- [msdyn_htmlsample](#BKMK_msdyn_htmlsample)
- [msdyn_htmlsample_Name](#BKMK_msdyn_htmlsample_Name)
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
|Description|**Date and time of the external search provider creation**|
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

### <a name="BKMK_msdyn_htmlsample"></a> msdyn_htmlsample

|Property|Value|
|---|---|
|Description|**The reference to the sample html file uploaded for the integrated search provider**|
|DisplayName|**Sample HTML File of Data Provider uploaded for metatags extraction**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_htmlsample`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_htmlsample_Name"></a> msdyn_htmlsample_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_htmlsample_name`|
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

- [business_unit_msdyn_integratedsearchprovider](#BKMK_business_unit_msdyn_integratedsearchprovider)
- [FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample](#BKMK_FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample)
- [lk_msdyn_integratedsearchprovider_createdby](#BKMK_lk_msdyn_integratedsearchprovider_createdby)
- [lk_msdyn_integratedsearchprovider_createdonbehalfby](#BKMK_lk_msdyn_integratedsearchprovider_createdonbehalfby)
- [lk_msdyn_integratedsearchprovider_modifiedby](#BKMK_lk_msdyn_integratedsearchprovider_modifiedby)
- [lk_msdyn_integratedsearchprovider_modifiedonbehalfby](#BKMK_lk_msdyn_integratedsearchprovider_modifiedonbehalfby)
- [owner_msdyn_integratedsearchprovider](#BKMK_owner_msdyn_integratedsearchprovider)
- [team_msdyn_integratedsearchprovider](#BKMK_team_msdyn_integratedsearchprovider)
- [user_msdyn_integratedsearchprovider](#BKMK_user_msdyn_integratedsearchprovider)

### <a name="BKMK_business_unit_msdyn_integratedsearchprovider"></a> business_unit_msdyn_integratedsearchprovider

One-To-Many Relationship: [businessunit business_unit_msdyn_integratedsearchprovider](businessunit.md#BKMK_business_unit_msdyn_integratedsearchprovider)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample"></a> FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample](fileattachment.md#BKMK_FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_htmlsample`|
|ReferencingEntityNavigationPropertyName|`msdyn_htmlsample`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_integratedsearchprovider_createdby"></a> lk_msdyn_integratedsearchprovider_createdby

One-To-Many Relationship: [systemuser lk_msdyn_integratedsearchprovider_createdby](systemuser.md#BKMK_lk_msdyn_integratedsearchprovider_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_integratedsearchprovider_createdonbehalfby"></a> lk_msdyn_integratedsearchprovider_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_integratedsearchprovider_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_integratedsearchprovider_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_integratedsearchprovider_modifiedby"></a> lk_msdyn_integratedsearchprovider_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_integratedsearchprovider_modifiedby](systemuser.md#BKMK_lk_msdyn_integratedsearchprovider_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_integratedsearchprovider_modifiedonbehalfby"></a> lk_msdyn_integratedsearchprovider_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_integratedsearchprovider_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_integratedsearchprovider_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_integratedsearchprovider"></a> owner_msdyn_integratedsearchprovider

One-To-Many Relationship: [owner owner_msdyn_integratedsearchprovider](owner.md#BKMK_owner_msdyn_integratedsearchprovider)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_integratedsearchprovider"></a> team_msdyn_integratedsearchprovider

One-To-Many Relationship: [team team_msdyn_integratedsearchprovider](team.md#BKMK_team_msdyn_integratedsearchprovider)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_integratedsearchprovider"></a> user_msdyn_integratedsearchprovider

One-To-Many Relationship: [systemuser user_msdyn_integratedsearchprovider](systemuser.md#BKMK_user_msdyn_integratedsearchprovider)

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

- [msdyn_integratedsearchprovider_AsyncOperations](#BKMK_msdyn_integratedsearchprovider_AsyncOperations)
- [msdyn_integratedsearchprovider_BulkDeleteFailures](#BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures)
- [msdyn_integratedsearchprovider_DuplicateBaseRecord](#BKMK_msdyn_integratedsearchprovider_DuplicateBaseRecord)
- [msdyn_integratedsearchprovider_DuplicateMatchingRecord](#BKMK_msdyn_integratedsearchprovider_DuplicateMatchingRecord)
- [msdyn_integratedsearchprovider_FileAttachments](#BKMK_msdyn_integratedsearchprovider_FileAttachments)
- [msdyn_integratedsearchprovider_MailboxTrackingFolders](#BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders)
- [msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses](#BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses)
- [msdyn_integratedsearchprovider_ProcessSession](#BKMK_msdyn_integratedsearchprovider_ProcessSession)
- [msdyn_integratedsearchprovider_SyncErrors](#BKMK_msdyn_integratedsearchprovider_SyncErrors)
- [msdyn_knowledgearticle_integratedsearchprovider](#BKMK_msdyn_knowledgearticle_integratedsearchprovider)

### <a name="BKMK_msdyn_integratedsearchprovider_AsyncOperations"></a> msdyn_integratedsearchprovider_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_integratedsearchprovider_AsyncOperations](asyncoperation.md#BKMK_msdyn_integratedsearchprovider_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_integratedsearchprovider_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures"></a> msdyn_integratedsearchprovider_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_integratedsearchprovider_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_integratedsearchprovider_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_integratedsearchprovider_DuplicateBaseRecord"></a> msdyn_integratedsearchprovider_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_integratedsearchprovider_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_integratedsearchprovider_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_integratedsearchprovider_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_integratedsearchprovider_DuplicateMatchingRecord"></a> msdyn_integratedsearchprovider_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_integratedsearchprovider_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_integratedsearchprovider_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_integratedsearchprovider_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_integratedsearchprovider_FileAttachments"></a> msdyn_integratedsearchprovider_FileAttachments

Many-To-One Relationship: [fileattachment msdyn_integratedsearchprovider_FileAttachments](fileattachment.md#BKMK_msdyn_integratedsearchprovider_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_integratedsearchprovider_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders"></a> msdyn_integratedsearchprovider_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_integratedsearchprovider_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_integratedsearchprovider_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses"></a> msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_integratedsearchprovider_ProcessSession"></a> msdyn_integratedsearchprovider_ProcessSession

Many-To-One Relationship: [processsession msdyn_integratedsearchprovider_ProcessSession](processsession.md#BKMK_msdyn_integratedsearchprovider_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_integratedsearchprovider_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_integratedsearchprovider_SyncErrors"></a> msdyn_integratedsearchprovider_SyncErrors

Many-To-One Relationship: [syncerror msdyn_integratedsearchprovider_SyncErrors](syncerror.md#BKMK_msdyn_integratedsearchprovider_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_integratedsearchprovider_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticle_integratedsearchprovider"></a> msdyn_knowledgearticle_integratedsearchprovider

Many-To-One Relationship: [knowledgearticle msdyn_knowledgearticle_integratedsearchprovider](knowledgearticle.md#BKMK_msdyn_knowledgearticle_integratedsearchprovider)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`msdyn_integratedsearchproviderid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticle_integratedsearchprovider`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_integratedsearchprovider?displayProperty=fullName>
