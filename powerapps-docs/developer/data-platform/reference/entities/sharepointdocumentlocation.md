---
title: "Document Location (SharePointDocumentLocation) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Document Location (SharePointDocumentLocation) table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Document Location (SharePointDocumentLocation) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Document libraries or folders on a SharePoint server from where documents can be managed in Microsoft Dynamics 365.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/sharepointdocumentlocations(*sharepointdocumentlocationid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/sharepointdocumentlocations<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/sharepointdocumentlocations(*sharepointdocumentlocationid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/sharepointdocumentlocations(*sharepointdocumentlocationid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveAbsoluteAndSiteCollectionUrl|<xref href="Microsoft.Dynamics.CRM.RetrieveAbsoluteAndSiteCollectionUrl?text=RetrieveAbsoluteAndSiteCollectionUrl Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAbsoluteAndSiteCollectionUrlRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/sharepointdocumentlocations<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/sharepointdocumentlocations(*sharepointdocumentlocationid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/sharepointdocumentlocations(*sharepointdocumentlocationid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SharePointDocumentLocations|
|DisplayCollectionName|Document Locations|
|DisplayName|Document Location|
|EntitySetName|sharepointdocumentlocations|
|IsBPFEntity|False|
|LogicalCollectionName|sharePointdocumentlocations|
|LogicalName|sharepointdocumentlocation|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|sharepointdocumentlocationid|
|PrimaryNameAttribute|name|
|SchemaName|SharePointDocumentLocation|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AbsoluteURL](#BKMK_AbsoluteURL)
- [Description](#BKMK_Description)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [LocationType](#BKMK_LocationType)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParentSiteOrLocation](#BKMK_ParentSiteOrLocation)
- [ParentSiteOrLocationTypeCode](#BKMK_ParentSiteOrLocationTypeCode)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [RelativeUrl](#BKMK_RelativeUrl)
- [ServiceType](#BKMK_ServiceType)
- [SharePointDocumentLocationId](#BKMK_SharePointDocumentLocationId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UserId](#BKMK_UserId)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_AbsoluteURL"></a> AbsoluteURL

|Property|Value|
|--------|-----|
|Description|Absolute URL of the SharePoint document location.|
|DisplayName|Absolute URL|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|absoluteurl|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the SharePoint document location record.|
|DisplayName|Description|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created the SharePoint document location record.|
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


### <a name="BKMK_LocationType"></a> LocationType

|Property|Value|
|--------|-----|
|Description|Location type of the SharePoint document location.|
|DisplayName|Location Type |
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|locationtype|
|RequiredLevel|None|
|Type|Picklist|

#### LocationType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|General||
|1|Dedicated for OneNote Integration||



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the SharePoint document location record.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|160|
|RequiredLevel|SystemRequired|
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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the SharePoint document location record.|
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
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_ParentSiteOrLocation"></a> ParentSiteOrLocation

|Property|Value|
|--------|-----|
|Description|Unique identifier of the parent site or location.|
|DisplayName|Parent Site or Location|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentsiteorlocation|
|RequiredLevel|None|
|Targets|sharepointdocumentlocation,sharepointsite|
|Type|Lookup|


### <a name="BKMK_ParentSiteOrLocationTypeCode"></a> ParentSiteOrLocationTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentsiteorlocationtypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the object with which the SharePoint document location record is associated.|
|DisplayName|Regarding|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|account,kbarticle,knowledgearticle,msdyn_knowledgearticletemplate|
|Type|Lookup|


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidname|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjectidyominame|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_RelativeUrl"></a> RelativeUrl

|Property|Value|
|--------|-----|
|Description|Relative URL of the SharePoint document location.|
|DisplayName|Relative URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|relativeurl|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ServiceType"></a> ServiceType

|Property|Value|
|--------|-----|
|Description|Shows the service type of the SharePoint site.|
|DisplayName|Service Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|servicetype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ServiceType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|SharePoint||
|1|OneDrive||
|2|Shared with me||
|3|MS Teams||



### <a name="BKMK_SharePointDocumentLocationId"></a> SharePointDocumentLocationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the SharePoint document location record.|
|DisplayName|SharePoint Document Location ID|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|sharepointdocumentlocationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Status of the SharePoint document location record.|
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
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the SharePoint document location record.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



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


### <a name="BKMK_UserId"></a> UserId

|Property|Value|
|--------|-----|
|Description|Choose the user who owns the SharePoint document location.|
|DisplayName|SharePoint Document Location Owner|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|userid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
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
- [ParentSiteOrLocationName](#BKMK_ParentSiteOrLocationName)
- [SiteCollectionId](#BKMK_SiteCollectionId)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the SharePoint document location record.|
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
|Description|Date and time when the SharePoint document location record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the SharePoint document location record.|
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Exchange rate between the currency associated with the SharePoint document location record and the base currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the SharePoint document location record.|
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
|Description|Date and time when the SharePoint document location record was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the SharePoint document location record.|
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit that owns the SharePoint document location record.|
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
|Description|Unique identifier of the team who owns the SharePoint document location record.|
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
|Description|Unique identifier of the user who owns the SharePoint document location record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ParentSiteOrLocationName"></a> ParentSiteOrLocationName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentsiteorlocationname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SiteCollectionId"></a> SiteCollectionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sitecollectionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the currency associated with the SharePoint document location record.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
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

- [sharepointdocumentlocation_parent_sharepointdocumentlocation](#BKMK_sharepointdocumentlocation_parent_sharepointdocumentlocation)
- [SharePointDocumentLocation_AsyncOperations](#BKMK_SharePointDocumentLocation_AsyncOperations)
- [sharepointdocumentlocation_principalobjectattributeaccess](#BKMK_sharepointdocumentlocation_principalobjectattributeaccess)
- [SharePointDocumentLocation_DuplicateBaseRecord](#BKMK_SharePointDocumentLocation_DuplicateBaseRecord)
- [SharePointDocumentLocation_ProcessSessions](#BKMK_SharePointDocumentLocation_ProcessSessions)
- [SharePointDocumentLocation_SyncErrors](#BKMK_SharePointDocumentLocation_SyncErrors)
- [SharePointDocumentLocation_DuplicateMatchingRecord](#BKMK_SharePointDocumentLocation_DuplicateMatchingRecord)


### <a name="BKMK_sharepointdocumentlocation_parent_sharepointdocumentlocation"></a> sharepointdocumentlocation_parent_sharepointdocumentlocation

Same as sharepointdocumentlocation table [sharepointdocumentlocation_parent_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_sharepointdocumentlocation_parent_sharepointdocumentlocation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|parentsiteorlocation|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|sharepointdocumentlocation_parent_sharepointdocumentlocation|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 40|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SharePointDocumentLocation_AsyncOperations"></a> SharePointDocumentLocation_AsyncOperations

Same as asyncoperation table [SharePointDocumentLocation_AsyncOperations](asyncoperation.md#BKMK_SharePointDocumentLocation_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SharePointDocumentLocation_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_sharepointdocumentlocation_principalobjectattributeaccess"></a> sharepointdocumentlocation_principalobjectattributeaccess

Same as principalobjectattributeaccess table [sharepointdocumentlocation_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_sharepointdocumentlocation_principalobjectattributeaccess) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|sharepointdocumentlocation_principalobjectattributeaccess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SharePointDocumentLocation_DuplicateBaseRecord"></a> SharePointDocumentLocation_DuplicateBaseRecord

Same as duplicaterecord table [SharePointDocumentLocation_DuplicateBaseRecord](duplicaterecord.md#BKMK_SharePointDocumentLocation_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SharePointDocumentLocation_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SharePointDocumentLocation_ProcessSessions"></a> SharePointDocumentLocation_ProcessSessions

Same as processsession table [SharePointDocumentLocation_ProcessSessions](processsession.md#BKMK_SharePointDocumentLocation_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SharePointDocumentLocation_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SharePointDocumentLocation_SyncErrors"></a> SharePointDocumentLocation_SyncErrors

Same as syncerror table [SharePointDocumentLocation_SyncErrors](syncerror.md#BKMK_SharePointDocumentLocation_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|SharePointDocumentLocation_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_SharePointDocumentLocation_DuplicateMatchingRecord"></a> SharePointDocumentLocation_DuplicateMatchingRecord

Same as duplicaterecord table [SharePointDocumentLocation_DuplicateMatchingRecord](duplicaterecord.md#BKMK_SharePointDocumentLocation_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SharePointDocumentLocation_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [knowledgearticle_SharePointDocumentLocations](#BKMK_knowledgearticle_SharePointDocumentLocations)
- [user_sharepointdocumentlocation](#BKMK_user_sharepointdocumentlocation)
- [team_sharepointdocumentlocation](#BKMK_team_sharepointdocumentlocation)
- [business_unit_sharepointdocumentlocation](#BKMK_business_unit_sharepointdocumentlocation)
- [lk_sharepointdocumentlocationbase_createdby](#BKMK_lk_sharepointdocumentlocationbase_createdby)
- [lk_sharepointdocumentlocationbase_modifiedby](#BKMK_lk_sharepointdocumentlocationbase_modifiedby)
- [sharepointdocumentlocation_parent_sharepointdocumentlocation](#BKMK_sharepointdocumentlocation_parent_sharepointdocumentlocation)
- [TransactionCurrency_SharePointDocumentLocation](#BKMK_TransactionCurrency_SharePointDocumentLocation)
- [lk_sharepointdocumentlocationbase_createdonbehalfby](#BKMK_lk_sharepointdocumentlocationbase_createdonbehalfby)
- [Account_SharepointDocumentLocation](#BKMK_Account_SharepointDocumentLocation)
- [lk_sharepointdocumentlocationbase_modifiedonbehalfby](#BKMK_lk_sharepointdocumentlocationbase_modifiedonbehalfby)
- [KbArticle_SharepointDocumentLocation](#BKMK_KbArticle_SharepointDocumentLocation)
- [sharepointdocumentlocation_parent_sharepointsite](#BKMK_sharepointdocumentlocation_parent_sharepointsite)
- [msdyn_knowledgearticletemplate_SharePointDocumentLocations](#BKMK_msdyn_knowledgearticletemplate_SharePointDocumentLocations)


### <a name="BKMK_knowledgearticle_SharePointDocumentLocations"></a> knowledgearticle_SharePointDocumentLocations

See knowledgearticle Table [knowledgearticle_SharePointDocumentLocations](knowledgearticle.md#BKMK_knowledgearticle_SharePointDocumentLocations) One-To-Many relationship.

### <a name="BKMK_user_sharepointdocumentlocation"></a> user_sharepointdocumentlocation

See systemuser Table [user_sharepointdocumentlocation](systemuser.md#BKMK_user_sharepointdocumentlocation) One-To-Many relationship.

### <a name="BKMK_team_sharepointdocumentlocation"></a> team_sharepointdocumentlocation

See team Table [team_sharepointdocumentlocation](team.md#BKMK_team_sharepointdocumentlocation) One-To-Many relationship.

### <a name="BKMK_business_unit_sharepointdocumentlocation"></a> business_unit_sharepointdocumentlocation

See businessunit Table [business_unit_sharepointdocumentlocation](businessunit.md#BKMK_business_unit_sharepointdocumentlocation) One-To-Many relationship.

### <a name="BKMK_lk_sharepointdocumentlocationbase_createdby"></a> lk_sharepointdocumentlocationbase_createdby

See systemuser Table [lk_sharepointdocumentlocationbase_createdby](systemuser.md#BKMK_lk_sharepointdocumentlocationbase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_sharepointdocumentlocationbase_modifiedby"></a> lk_sharepointdocumentlocationbase_modifiedby

See systemuser Table [lk_sharepointdocumentlocationbase_modifiedby](systemuser.md#BKMK_lk_sharepointdocumentlocationbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_sharepointdocumentlocation_parent_sharepointdocumentlocation"></a> sharepointdocumentlocation_parent_sharepointdocumentlocation

See sharepointdocumentlocation Table [sharepointdocumentlocation_parent_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_sharepointdocumentlocation_parent_sharepointdocumentlocation) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_SharePointDocumentLocation"></a> TransactionCurrency_SharePointDocumentLocation

See transactioncurrency Table [TransactionCurrency_SharePointDocumentLocation](transactioncurrency.md#BKMK_TransactionCurrency_SharePointDocumentLocation) One-To-Many relationship.

### <a name="BKMK_lk_sharepointdocumentlocationbase_createdonbehalfby"></a> lk_sharepointdocumentlocationbase_createdonbehalfby

See systemuser Table [lk_sharepointdocumentlocationbase_createdonbehalfby](systemuser.md#BKMK_lk_sharepointdocumentlocationbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_Account_SharepointDocumentLocation"></a> Account_SharepointDocumentLocation

See account Table [Account_SharepointDocumentLocation](account.md#BKMK_Account_SharepointDocumentLocation) One-To-Many relationship.

### <a name="BKMK_lk_sharepointdocumentlocationbase_modifiedonbehalfby"></a> lk_sharepointdocumentlocationbase_modifiedonbehalfby

See systemuser Table [lk_sharepointdocumentlocationbase_modifiedonbehalfby](systemuser.md#BKMK_lk_sharepointdocumentlocationbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_KbArticle_SharepointDocumentLocation"></a> KbArticle_SharepointDocumentLocation

See kbarticle Table [KbArticle_SharepointDocumentLocation](kbarticle.md#BKMK_KbArticle_SharepointDocumentLocation) One-To-Many relationship.

### <a name="BKMK_sharepointdocumentlocation_parent_sharepointsite"></a> sharepointdocumentlocation_parent_sharepointsite

See sharepointsite Table [sharepointdocumentlocation_parent_sharepointsite](sharepointsite.md#BKMK_sharepointdocumentlocation_parent_sharepointsite) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticletemplate_SharePointDocumentLocations"></a> msdyn_knowledgearticletemplate_SharePointDocumentLocations

**Added by**: Knowledge Management Features Solution

See msdyn_knowledgearticletemplate Table [msdyn_knowledgearticletemplate_SharePointDocumentLocations](msdyn_knowledgearticletemplate.md#BKMK_msdyn_knowledgearticletemplate_SharePointDocumentLocations) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.sharepointdocumentlocation?text=sharepointdocumentlocation EntityType" />