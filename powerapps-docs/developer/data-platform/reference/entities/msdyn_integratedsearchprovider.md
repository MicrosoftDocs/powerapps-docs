---
title: "msdyn_integratedsearchprovider table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the msdyn_integratedsearchprovider table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# msdyn_integratedsearchprovider table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Ingest and search files, documents, or articles from data sources outside of your current Dynamics 365 organization with a unified ranking.

**Added by**: Knowledge Management Online Features Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /msdyn_integratedsearchproviders(*msdyn_integratedsearchproviderid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST /msdyn_integratedsearchproviders<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msdyn_integratedsearchproviders(*msdyn_integratedsearchproviderid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET /msdyn_integratedsearchproviders(*msdyn_integratedsearchproviderid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /msdyn_integratedsearchproviders<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH /msdyn_integratedsearchproviders(*msdyn_integratedsearchproviderid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /msdyn_integratedsearchproviders(*msdyn_integratedsearchproviderid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_integratedsearchproviders|
|DisplayCollectionName|Integrated search providers|
|DisplayName|Integrated search provider|
|EntitySetName|msdyn_integratedsearchproviders|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_integratedsearchproviders|
|LogicalName|msdyn_integratedsearchprovider|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_integratedsearchproviderid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_integratedsearchprovider|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Sequence number of the import that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_allowedlanguages"></a> msdyn_allowedlanguages

|Property|Value|
|--------|-----|
|Description|Languages allowed for ingestion|
|DisplayName|Allowed Languages|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_allowedlanguages|
|MaxLength|10000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_articlepropertiesmapping"></a> msdyn_articlepropertiesmapping

|Property|Value|
|--------|-----|
|Description|Map external search provider fields and knowledge article table columns in Dataverse|
|DisplayName|Article properties|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_articlepropertiesmapping|
|MaxLength|1048576|
|RequiredLevel|ApplicationRequired|
|Type|Memo|


### <a name="BKMK_msdyn_authenticationtype"></a> msdyn_authenticationtype

|Property|Value|
|--------|-----|
|Description|Authentication type for the search provider|
|DisplayName|Authentication|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_authenticationtype|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### msdyn_authenticationtype Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None||
|1|OAuth||



### <a name="BKMK_msdyn_clientid"></a> msdyn_clientid

|Property|Value|
|--------|-----|
|Description|Client ID for the OAuth|
|DisplayName|Client ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_clientid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_clientsecret"></a> msdyn_clientsecret

|Property|Value|
|--------|-----|
|Description|Secret of the external search provider|
|DisplayName|External search provider secret|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_clientsecret|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_datasourcetype"></a> msdyn_datasourcetype

|Property|Value|
|--------|-----|
|Description|Type of the external search provider|
|DisplayName|External search provider type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_datasourcetype|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### msdyn_datasourcetype Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Website||



### <a name="BKMK_msdyn_description"></a> msdyn_description

|Property|Value|
|--------|-----|
|Description|Description of the external search provider|
|DisplayName|Description|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_description|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_htmlmetatags"></a> msdyn_htmlmetatags

|Property|Value|
|--------|-----|
|Description|Information about the meta tags extracted from sample dataprovider html|
|DisplayName|Html meta tags information|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_htmlmetatags|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_includedsitemapurls"></a> msdyn_includedsitemapurls

|Property|Value|
|--------|-----|
|Description|List of URLs that are allowed|
|DisplayName|Allowlist URL|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_includedsitemapurls|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_integratedsearchproviderId"></a> msdyn_integratedsearchproviderId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Integrated search provider|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_integratedsearchproviderid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_isfieldmappingoptionselected"></a> msdyn_isfieldmappingoptionselected

|Property|Value|
|--------|-----|
|Description|Value is true when field mapping option is selected|
|DisplayName|Is Field Mapping Option Selected|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isfieldmappingoptionselected|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isfieldmappingoptionselected Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_msdyn_lastfetchtime"></a> msdyn_lastfetchtime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time at which the recent ingestion was started|
|DisplayName|Last fetch time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_lastfetchtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_msdyn_lookbackperiod"></a> msdyn_lookbackperiod

|Property|Value|
|--------|-----|
|Description|Time interval for ingesting any articles that might have been missed during the sync and ingestion overlap|
|DisplayName|Lookback period|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_lookbackperiod|
|RequiredLevel|None|
|Type|Picklist|

#### msdyn_lookbackperiod Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|No Lookback||
|1|2 hours||
|2|4 hours||
|3|6 hours||
|4|8 hours||



### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|--------|-----|
|Description|Name of the external search provider|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_name|
|MaxLength|255|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_refreshschedule"></a> msdyn_refreshschedule

|Property|Value|
|--------|-----|
|Description|Time interval for ingesting newly created and updated articles from the external search provider|
|DisplayName|Refresh schedule|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_refreshschedule|
|RequiredLevel|None|
|Type|Picklist|

#### msdyn_refreshschedule Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|No refresh||
|1|15 mins||
|2|30 mins||
|3|45 mins||
|4|1 hour||
|5|2 hours||
|6|4 hours||
|7|8 hours||
|8|1 day||
|9|2 days||
|10|4 days||
|11|7 days||



### <a name="BKMK_msdyn_resourceid"></a> msdyn_resourceid

|Property|Value|
|--------|-----|
|Description|Resource ID for OAuth|
|DisplayName|Resource ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_resourceid|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_rooturl"></a> msdyn_rooturl

|Property|Value|
|--------|-----|
|Description|Root URL of the website|
|DisplayName|Root URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_rooturl|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_tenantid"></a> msdyn_tenantid

|Property|Value|
|--------|-----|
|Description|Tenant ID for OAuth|
|DisplayName|Tenant ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_tenantid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OwnerId"></a> OwnerId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner of the external search provider record|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|State of the external search provider|
|DisplayName|Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Integrated search provider|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Ingestion Ready|0|
|2|Validated|1|
|3|Draft|1|



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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [msdyn_htmlsample](#BKMK_msdyn_htmlsample)
- [msdyn_htmlsample_Name](#BKMK_msdyn_htmlsample_Name)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time of the external search provider creation|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_msdyn_htmlsample"></a> msdyn_htmlsample

|Property|Value|
|--------|-----|
|Description|The reference to the sample html file uploaded for the integrated search provider|
|DisplayName|Sample HTML File of Data Provider uploaded for metatags extraction|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_htmlsample|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_htmlsample_Name"></a> msdyn_htmlsample_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_htmlsample_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Name of the owner|
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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Yomi name of the owner|
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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunitname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version Number|
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

- [msdyn_integratedsearchprovider_SyncErrors](#BKMK_msdyn_integratedsearchprovider_SyncErrors)
- [msdyn_integratedsearchprovider_DuplicateMatchingRecord](#BKMK_msdyn_integratedsearchprovider_DuplicateMatchingRecord)
- [msdyn_integratedsearchprovider_DuplicateBaseRecord](#BKMK_msdyn_integratedsearchprovider_DuplicateBaseRecord)
- [msdyn_integratedsearchprovider_AsyncOperations](#BKMK_msdyn_integratedsearchprovider_AsyncOperations)
- [msdyn_integratedsearchprovider_MailboxTrackingFolders](#BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders)
- [msdyn_integratedsearchprovider_ProcessSession](#BKMK_msdyn_integratedsearchprovider_ProcessSession)
- [msdyn_integratedsearchprovider_BulkDeleteFailures](#BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures)
- [msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses](#BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgearticle_integratedsearchprovider](#BKMK_msdyn_knowledgearticle_integratedsearchprovider)


### <a name="BKMK_msdyn_integratedsearchprovider_SyncErrors"></a> msdyn_integratedsearchprovider_SyncErrors

**Added by**: System Solution Solution

Same as the [msdyn_integratedsearchprovider_SyncErrors](syncerror.md#BKMK_msdyn_integratedsearchprovider_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_integratedsearchprovider_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_integratedsearchprovider_DuplicateMatchingRecord"></a> msdyn_integratedsearchprovider_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [msdyn_integratedsearchprovider_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_integratedsearchprovider_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_integratedsearchprovider_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_integratedsearchprovider_DuplicateBaseRecord"></a> msdyn_integratedsearchprovider_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [msdyn_integratedsearchprovider_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_integratedsearchprovider_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_integratedsearchprovider_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_integratedsearchprovider_AsyncOperations"></a> msdyn_integratedsearchprovider_AsyncOperations

**Added by**: System Solution Solution

Same as the [msdyn_integratedsearchprovider_AsyncOperations](asyncoperation.md#BKMK_msdyn_integratedsearchprovider_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_integratedsearchprovider_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders"></a> msdyn_integratedsearchprovider_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msdyn_integratedsearchprovider_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_integratedsearchprovider_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_integratedsearchprovider_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_integratedsearchprovider_ProcessSession"></a> msdyn_integratedsearchprovider_ProcessSession

**Added by**: System Solution Solution

Same as the [msdyn_integratedsearchprovider_ProcessSession](processsession.md#BKMK_msdyn_integratedsearchprovider_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_integratedsearchprovider_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures"></a> msdyn_integratedsearchprovider_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msdyn_integratedsearchprovider_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_integratedsearchprovider_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_integratedsearchprovider_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses"></a> msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_integratedsearchprovider_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgearticle_integratedsearchprovider"></a> msdyn_knowledgearticle_integratedsearchprovider

Same as the [msdyn_knowledgearticle_integratedsearchprovider](knowledgearticle.md#BKMK_msdyn_knowledgearticle_integratedsearchprovider) many-to-one relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|msdyn_integratedsearchproviderid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticle_integratedsearchprovider|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_integratedsearchprovider_createdby](#BKMK_lk_msdyn_integratedsearchprovider_createdby)
- [lk_msdyn_integratedsearchprovider_createdonbehalfby](#BKMK_lk_msdyn_integratedsearchprovider_createdonbehalfby)
- [lk_msdyn_integratedsearchprovider_modifiedby](#BKMK_lk_msdyn_integratedsearchprovider_modifiedby)
- [lk_msdyn_integratedsearchprovider_modifiedonbehalfby](#BKMK_lk_msdyn_integratedsearchprovider_modifiedonbehalfby)
- [user_msdyn_integratedsearchprovider](#BKMK_user_msdyn_integratedsearchprovider)
- [team_msdyn_integratedsearchprovider](#BKMK_team_msdyn_integratedsearchprovider)
- [business_unit_msdyn_integratedsearchprovider](#BKMK_business_unit_msdyn_integratedsearchprovider)


### <a name="BKMK_lk_msdyn_integratedsearchprovider_createdby"></a> lk_msdyn_integratedsearchprovider_createdby

**Added by**: System Solution Solution

See the [lk_msdyn_integratedsearchprovider_createdby](systemuser.md#BKMK_lk_msdyn_integratedsearchprovider_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_integratedsearchprovider_createdonbehalfby"></a> lk_msdyn_integratedsearchprovider_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_integratedsearchprovider_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_integratedsearchprovider_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_integratedsearchprovider_modifiedby"></a> lk_msdyn_integratedsearchprovider_modifiedby

**Added by**: System Solution Solution

See the [lk_msdyn_integratedsearchprovider_modifiedby](systemuser.md#BKMK_lk_msdyn_integratedsearchprovider_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_integratedsearchprovider_modifiedonbehalfby"></a> lk_msdyn_integratedsearchprovider_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_integratedsearchprovider_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_integratedsearchprovider_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_msdyn_integratedsearchprovider"></a> user_msdyn_integratedsearchprovider

**Added by**: System Solution Solution

See the [user_msdyn_integratedsearchprovider](systemuser.md#BKMK_user_msdyn_integratedsearchprovider) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_msdyn_integratedsearchprovider"></a> team_msdyn_integratedsearchprovider

**Added by**: System Solution Solution

See the [team_msdyn_integratedsearchprovider](team.md#BKMK_team_msdyn_integratedsearchprovider) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_msdyn_integratedsearchprovider"></a> business_unit_msdyn_integratedsearchprovider

**Added by**: System Solution Solution

See the [business_unit_msdyn_integratedsearchprovider](businessunit.md#BKMK_business_unit_msdyn_integratedsearchprovider) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msdyn_integratedsearchprovider?text=msdyn_integratedsearchprovider EntityType" />