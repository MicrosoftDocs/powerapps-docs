---
title: "SharePointDocumentLocation Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SharePointDocumentLocation entity."
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
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# SharePointDocumentLocation Entity Reference

Document libraries or folders on a SharePoint server from where documents can be managed in Microsoft Dynamics 365.

## Entity Properties

**DisplayName**: Document Location<br />
**DisplayCollectionName**: Document Locations<br />
**SchemaName**: SharePointDocumentLocation<br />
**CollectionSchemaName**: SharePointDocumentLocations<br />
**LogicalName**: sharepointdocumentlocation<br />
**LogicalCollectionName**: sharePointdocumentlocations<br />
**EntitySetName**: sharepointdocumentlocations<br />
**PrimaryIdAttribute**: sharepointdocumentlocationid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

**Description**: Absolute URL of the SharePoint document location.<br />
**DisplayName**: Absolute URL<br />
**LogicalName**: absoluteurl<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Url<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_Description"></a> Description

**Description**: Description of the SharePoint document location record.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: Sequence number of the import that created the SharePoint document location record.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_LocationType"></a> LocationType

**Description**: Location type of the SharePoint document location.<br />
**DisplayName**: Location Type <br />
**LogicalName**: locationtype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: General
- **Value**: 1 **Label**: Dedicated for OneNote Integration



### <a name="BKMK_Name"></a> Name

**Description**: Name of the SharePoint document location record.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the SharePoint document location record.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: Owner Id Type<br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_ParentSiteOrLocation"></a> ParentSiteOrLocation

**Description**: Unique identifier of the parent site or location.<br />
**DisplayName**: Parent Site or Location<br />
**LogicalName**: parentsiteorlocation<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: sharepointdocumentlocation,sharepointsite


### <a name="BKMK_ParentSiteOrLocationTypeCode"></a> ParentSiteOrLocationTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: parentsiteorlocationtypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Unique identifier of the object with which the SharePoint document location record is associated.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account,kbarticle,knowledgearticle


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_RelativeUrl"></a> RelativeUrl

**Description**: Relative URL of the SharePoint document location.<br />
**DisplayName**: Relative URL<br />
**LogicalName**: relativeurl<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 255


### <a name="BKMK_ServiceType"></a> ServiceType

**Description**: Shows the service type of the SharePoint site.<br />
**DisplayName**: Service Type<br />
**LogicalName**: servicetype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: SharePoint
- **Value**: 1 **Label**: OneDrive
- **Value**: 2 **Label**: Shared with me



### <a name="BKMK_SharePointDocumentLocationId"></a> SharePointDocumentLocationId

**Description**: Unique identifier of the SharePoint document location record.<br />
**DisplayName**: SharePoint Document Location ID<br />
**LogicalName**: sharepointdocumentlocationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the SharePoint document location record.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 1 **InvariantName**: Active
- **Value**: 1 **Label**: Inactive **DefaultStatus**: 2 **InvariantName**: Inactive



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Reason for the status of the SharePoint document location record.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Active **State**: 0
- **Value**: 2 **Label**: Inactive **State**: 1



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


### <a name="BKMK_UserId"></a> UserId

**Description**: Choose the user who owns the SharePoint document location.<br />
**DisplayName**: SharePoint Document Location Owner<br />
**LogicalName**: userid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


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

**Description**: Unique identifier of the user who created the SharePoint document location record.<br />
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

**Description**: Date and time when the SharePoint document location record was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the SharePoint document location record.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate between the currency associated with the SharePoint document location record and the base currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the SharePoint document location record.<br />
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

**Description**: Date and time when the SharePoint document location record was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the SharePoint document location record.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
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

**Description**: Name of the owner<br />
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

**Description**: Yomi name of the owner<br />
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

**Description**: Unique identifier of the business unit that owns the SharePoint document location record.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the SharePoint document location record.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the SharePoint document location record.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ParentSiteOrLocationName"></a> ParentSiteOrLocationName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: parentsiteorlocationname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_SiteCollectionId"></a> SiteCollectionId

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: sitecollectionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Unique identifier of the currency associated with the SharePoint document location record.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: transactioncurrencyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [sharepointdocumentlocation_parent_sharepointdocumentlocation](#BKMK_sharepointdocumentlocation_parent_sharepointdocumentlocation)
- [SharePointDocumentLocation_AsyncOperations](#BKMK_SharePointDocumentLocation_AsyncOperations)
- [userentityinstancedata_sharepointdocumentlocation](#BKMK_userentityinstancedata_sharepointdocumentlocation)
- [sharepointdocumentlocation_principalobjectattributeaccess](#BKMK_sharepointdocumentlocation_principalobjectattributeaccess)
- [SharePointDocumentLocation_DuplicateBaseRecord](#BKMK_SharePointDocumentLocation_DuplicateBaseRecord)
- [sharepointdata_sharepointdocumentlocation](#BKMK_sharepointdata_sharepointdocumentlocation)
- [SharePointDocumentLocation_ProcessSessions](#BKMK_SharePointDocumentLocation_ProcessSessions)
- [SharePointDocumentLocation_SyncErrors](#BKMK_SharePointDocumentLocation_SyncErrors)
- [SharePointDocumentLocation_DuplicateMatchingRecord](#BKMK_SharePointDocumentLocation_DuplicateMatchingRecord)


### <a name="BKMK_sharepointdocumentlocation_parent_sharepointdocumentlocation"></a> sharepointdocumentlocation_parent_sharepointdocumentlocation

Same as sharepointdocumentlocation entity [sharepointdocumentlocation_parent_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_sharepointdocumentlocation_parent_sharepointdocumentlocation) Many-To-One relationship.

**ReferencingEntity**: sharepointdocumentlocation<br />
**ReferencingAttribute**: parentsiteorlocation<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sharepointdocumentlocation_parent_sharepointdocumentlocation<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 40

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_SharePointDocumentLocation_AsyncOperations"></a> SharePointDocumentLocation_AsyncOperations

Same as asyncoperation entity [SharePointDocumentLocation_AsyncOperations](asyncoperation.md#BKMK_SharePointDocumentLocation_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SharePointDocumentLocation_AsyncOperations<br />
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


### <a name="BKMK_userentityinstancedata_sharepointdocumentlocation"></a> userentityinstancedata_sharepointdocumentlocation

Same as userentityinstancedata entity [userentityinstancedata_sharepointdocumentlocation](userentityinstancedata.md#BKMK_userentityinstancedata_sharepointdocumentlocation) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_sharepointdocumentlocation<br />
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


### <a name="BKMK_sharepointdocumentlocation_principalobjectattributeaccess"></a> sharepointdocumentlocation_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [sharepointdocumentlocation_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_sharepointdocumentlocation_principalobjectattributeaccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: sharepointdocumentlocation_principalobjectattributeaccess<br />
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


### <a name="BKMK_SharePointDocumentLocation_DuplicateBaseRecord"></a> SharePointDocumentLocation_DuplicateBaseRecord

Same as duplicaterecord entity [SharePointDocumentLocation_DuplicateBaseRecord](duplicaterecord.md#BKMK_SharePointDocumentLocation_DuplicateBaseRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: baserecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SharePointDocumentLocation_DuplicateBaseRecord<br />
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


### <a name="BKMK_sharepointdata_sharepointdocumentlocation"></a> sharepointdata_sharepointdocumentlocation

Same as sharepointdata entity [sharepointdata_sharepointdocumentlocation](sharepointdata.md#BKMK_sharepointdata_sharepointdocumentlocation) Many-To-One relationship.

**ReferencingEntity**: sharepointdata<br />
**ReferencingAttribute**: location<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sharepointdata_sharepointdocumentlocation<br />
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


### <a name="BKMK_SharePointDocumentLocation_ProcessSessions"></a> SharePointDocumentLocation_ProcessSessions

Same as processsession entity [SharePointDocumentLocation_ProcessSessions](processsession.md#BKMK_SharePointDocumentLocation_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SharePointDocumentLocation_ProcessSessions<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 110

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_SharePointDocumentLocation_SyncErrors"></a> SharePointDocumentLocation_SyncErrors

Same as syncerror entity [SharePointDocumentLocation_SyncErrors](syncerror.md#BKMK_SharePointDocumentLocation_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: SharePointDocumentLocation_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_SharePointDocumentLocation_DuplicateMatchingRecord"></a> SharePointDocumentLocation_DuplicateMatchingRecord

Same as duplicaterecord entity [SharePointDocumentLocation_DuplicateMatchingRecord](duplicaterecord.md#BKMK_SharePointDocumentLocation_DuplicateMatchingRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: duplicaterecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SharePointDocumentLocation_DuplicateMatchingRecord<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

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


### <a name="BKMK_knowledgearticle_SharePointDocumentLocations"></a> knowledgearticle_SharePointDocumentLocations

See knowledgearticle Entity [knowledgearticle_SharePointDocumentLocations](knowledgearticle.md#BKMK_knowledgearticle_SharePointDocumentLocations) One-To-Many relationship.

### <a name="BKMK_user_sharepointdocumentlocation"></a> user_sharepointdocumentlocation

See systemuser Entity [user_sharepointdocumentlocation](systemuser.md#BKMK_user_sharepointdocumentlocation) One-To-Many relationship.

### <a name="BKMK_team_sharepointdocumentlocation"></a> team_sharepointdocumentlocation

See team Entity [team_sharepointdocumentlocation](team.md#BKMK_team_sharepointdocumentlocation) One-To-Many relationship.

### <a name="BKMK_business_unit_sharepointdocumentlocation"></a> business_unit_sharepointdocumentlocation

See businessunit Entity [business_unit_sharepointdocumentlocation](businessunit.md#BKMK_business_unit_sharepointdocumentlocation) One-To-Many relationship.

### <a name="BKMK_lk_sharepointdocumentlocationbase_createdby"></a> lk_sharepointdocumentlocationbase_createdby

See systemuser Entity [lk_sharepointdocumentlocationbase_createdby](systemuser.md#BKMK_lk_sharepointdocumentlocationbase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_sharepointdocumentlocationbase_modifiedby"></a> lk_sharepointdocumentlocationbase_modifiedby

See systemuser Entity [lk_sharepointdocumentlocationbase_modifiedby](systemuser.md#BKMK_lk_sharepointdocumentlocationbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_sharepointdocumentlocation_parent_sharepointdocumentlocation"></a> sharepointdocumentlocation_parent_sharepointdocumentlocation

See sharepointdocumentlocation Entity [sharepointdocumentlocation_parent_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_sharepointdocumentlocation_parent_sharepointdocumentlocation) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_SharePointDocumentLocation"></a> TransactionCurrency_SharePointDocumentLocation

See transactioncurrency Entity [TransactionCurrency_SharePointDocumentLocation](transactioncurrency.md#BKMK_TransactionCurrency_SharePointDocumentLocation) One-To-Many relationship.

### <a name="BKMK_lk_sharepointdocumentlocationbase_createdonbehalfby"></a> lk_sharepointdocumentlocationbase_createdonbehalfby

See systemuser Entity [lk_sharepointdocumentlocationbase_createdonbehalfby](systemuser.md#BKMK_lk_sharepointdocumentlocationbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_Account_SharepointDocumentLocation"></a> Account_SharepointDocumentLocation

See account Entity [Account_SharepointDocumentLocation](account.md#BKMK_Account_SharepointDocumentLocation) One-To-Many relationship.

### <a name="BKMK_lk_sharepointdocumentlocationbase_modifiedonbehalfby"></a> lk_sharepointdocumentlocationbase_modifiedonbehalfby

See systemuser Entity [lk_sharepointdocumentlocationbase_modifiedonbehalfby](systemuser.md#BKMK_lk_sharepointdocumentlocationbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_KbArticle_SharepointDocumentLocation"></a> KbArticle_SharepointDocumentLocation

See kbarticle Entity [KbArticle_SharepointDocumentLocation](kbarticle.md#BKMK_KbArticle_SharepointDocumentLocation) One-To-Many relationship.

### <a name="BKMK_sharepointdocumentlocation_parent_sharepointsite"></a> sharepointdocumentlocation_parent_sharepointsite

See sharepointsite Entity [sharepointdocumentlocation_parent_sharepointsite](sharepointsite.md#BKMK_sharepointdocumentlocation_parent_sharepointsite) One-To-Many relationship.
sharepointdocumentlocation

