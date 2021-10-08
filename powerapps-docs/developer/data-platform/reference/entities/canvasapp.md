---
title: "CanvasApp table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the CanvasApp table/entity."
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

# CanvasApp table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

An application built through a canvas-based editing experience.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/canvasapps(*canvasappid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/canvasapps<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/canvasapps(*canvasappid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/canvasapps(*canvasappid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/canvasapps<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/canvasapps(*canvasappid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Canvas Apps|
|DisplayCollectionName|Canvas Apps|
|DisplayName|Canvas App|
|EntitySetName|canvasapps|
|IsBPFEntity|False|
|LogicalCollectionName|canvasapps|
|LogicalName|canvasapp|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|canvasappid|
|PrimaryNameAttribute|name|
|SchemaName|CanvasApp|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AADCreatedById](#BKMK_AADCreatedById)
- [AADLastModifiedById](#BKMK_AADLastModifiedById)
- [AADLastPublishedById](#BKMK_AADLastPublishedById)
- [AdminControlBypassConsent](#BKMK_AdminControlBypassConsent)
- [AppComponentDependencies](#BKMK_AppComponentDependencies)
- [AppComponents](#BKMK_AppComponents)
- [AppOpenUri](#BKMK_AppOpenUri)
- [AppVersion](#BKMK_AppVersion)
- [AuthorizationReferences](#BKMK_AuthorizationReferences)
- [BackgroundColor](#BKMK_BackgroundColor)
- [BypassConsent](#BKMK_BypassConsent)
- [CanConsumeAppPass](#BKMK_CanConsumeAppPass)
- [CanvasAppId](#BKMK_CanvasAppId)
- [CanvasAppType](#BKMK_CanvasAppType)
- [CdsDependencies](#BKMK_CdsDependencies)
- [CommitMessage](#BKMK_CommitMessage)
- [ConnectionReferences](#BKMK_ConnectionReferences)
- [CreatedByClientVersion](#BKMK_CreatedByClientVersion)
- [CreatedTime](#BKMK_CreatedTime)
- [DatabaseReferences](#BKMK_DatabaseReferences)
- [Description](#BKMK_Description)
- [DisplayName](#BKMK_DisplayName)
- [EmbeddedApp](#BKMK_EmbeddedApp)
- [GalleryItemId](#BKMK_GalleryItemId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCdsUpgraded](#BKMK_IsCdsUpgraded)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsFeaturedApp](#BKMK_IsFeaturedApp)
- [IsHeroApp](#BKMK_IsHeroApp)
- [IsHidden](#BKMK_IsHidden)
- [LastModifiedTime](#BKMK_LastModifiedTime)
- [LastPublishTime](#BKMK_LastPublishTime)
- [MinClientVersion](#BKMK_MinClientVersion)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Publisher](#BKMK_Publisher)
- [Status](#BKMK_Status)
- [Tags](#BKMK_Tags)


### <a name="BKMK_AADCreatedById"></a> AADCreatedById

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the canvas app.|
|DisplayName|Created By|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aadcreatedbyid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AADLastModifiedById"></a> AADLastModifiedById

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the application.|
|DisplayName|Last Modified By|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aadlastmodifiedbyid|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_AADLastPublishedById"></a> AADLastPublishedById

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last published the application.|
|DisplayName|Last Published By|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|aadlastpublishedbyid|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_AdminControlBypassConsent"></a> AdminControlBypassConsent

|Property|Value|
|--------|-----|
|Description|Indicates whether the canvas app was marked for bypass consent by an admin.|
|DisplayName|Admin Control Bypass Consent|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|admincontrolbypassconsent|
|RequiredLevel|None|
|Type|Boolean|

#### AdminControlBypassConsent Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|True|
|0|False|

**DefaultValue**: False



### <a name="BKMK_AppComponentDependencies"></a> AppComponentDependencies

|Property|Value|
|--------|-----|
|Description|The app component dependencies.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appcomponentdependencies|
|MaxLength|768000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_AppComponents"></a> AppComponents

|Property|Value|
|--------|-----|
|Description|The app components.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appcomponents|
|MaxLength|768000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_AppOpenUri"></a> AppOpenUri

|Property|Value|
|--------|-----|
|Description|The app open URI.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appopenuri|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_AppVersion"></a> AppVersion

|Property|Value|
|--------|-----|
|Description|The application version.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appversion|
|MaxLength|2000|
|RequiredLevel|SystemRequired|
|Type|Memo|


### <a name="BKMK_AuthorizationReferences"></a> AuthorizationReferences

|Property|Value|
|--------|-----|
|Description|The authorization references of the application.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|authorizationreferences|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_BackgroundColor"></a> BackgroundColor

|Property|Value|
|--------|-----|
|Description|The background image color.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|backgroundcolor|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_BypassConsent"></a> BypassConsent

|Property|Value|
|--------|-----|
|Description|Indicates whether the canvas app should bypass consent from consumers.|
|DisplayName|Bypass Consent|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|bypassconsent|
|RequiredLevel|None|
|Type|Boolean|

#### BypassConsent Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|True|
|0|False|

**DefaultValue**: False



### <a name="BKMK_CanConsumeAppPass"></a> CanConsumeAppPass

|Property|Value|
|--------|-----|
|Description|The type of the canvas app.|
|DisplayName|Can Consume App Pass|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canconsumeapppass|
|RequiredLevel|None|
|Type|Boolean|

#### CanConsumeAppPass Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|True|
|0|False|

**DefaultValue**: False



### <a name="BKMK_CanvasAppId"></a> CanvasAppId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canvasappid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_CanvasAppType"></a> CanvasAppType

|Property|Value|
|--------|-----|
|Description|The type of the canvas app.|
|DisplayName|Canvas App Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canvasapptype|
|RequiredLevel|None|
|Type|Picklist|

#### CanvasAppType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Classic Canvas App||
|1|App Component Library||
|2|Custom Canvas Page||
|3|Unified App||



### <a name="BKMK_CdsDependencies"></a> CdsDependencies

|Property|Value|
|--------|-----|
|Description|Internal use. The app dependency details.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|cdsdependencies|
|MaxLength|768000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_CommitMessage"></a> CommitMessage

|Property|Value|
|--------|-----|
|Description|The commit message of the app.|
|DisplayName|The commit message.|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|commitmessage|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ConnectionReferences"></a> ConnectionReferences

|Property|Value|
|--------|-----|
|Description|The connection references of the application.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|connectionreferences|
|MaxLength|768000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_CreatedByClientVersion"></a> CreatedByClientVersion

|Property|Value|
|--------|-----|
|Description|The version of the client that was used to author the application.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyclientversion|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedTime"></a> CreatedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the application was created.|
|DisplayName|Created Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_DatabaseReferences"></a> DatabaseReferences

|Property|Value|
|--------|-----|
|Description|The database references of the application.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|databasereferences|
|MaxLength|768000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|The description of the app.|
|DisplayName|The description.|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|--------|-----|
|Description|The display name of the app.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|displayname|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_EmbeddedApp"></a> EmbeddedApp

|Property|Value|
|--------|-----|
|Description|Internal use. The embedded app information.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|embeddedapp|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_GalleryItemId"></a> GalleryItemId

|Property|Value|
|--------|-----|
|Description|The gallery item identifier.|
|DisplayName|The gallery item identifier|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|galleryitemid|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the canvas app is introduced.|
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


### <a name="BKMK_IsCdsUpgraded"></a> IsCdsUpgraded

|Property|Value|
|--------|-----|
|Description|Indicates whether the canvas app contains CDS 1.0 references.|
|DisplayName|Is CDS Upgraded|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscdsupgraded|
|RequiredLevel|None|
|Type|Boolean|

#### IsCdsUpgraded Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|True|
|0|False|

**DefaultValue**: False



### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Added by**: Canvas App Metadata Extension Solution

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component can be customized.|
|DisplayName|Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_IsFeaturedApp"></a> IsFeaturedApp

|Property|Value|
|--------|-----|
|Description|Indicates whether the canvas app is a featured app.|
|DisplayName|Is Featured App|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isfeaturedapp|
|RequiredLevel|None|
|Type|Boolean|

#### IsFeaturedApp Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|True|
|0|False|

**DefaultValue**: False



### <a name="BKMK_IsHeroApp"></a> IsHeroApp

|Property|Value|
|--------|-----|
|Description|Indicates whether the canvas app is a hero app.|
|DisplayName|Is Hero App|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isheroapp|
|RequiredLevel|None|
|Type|Boolean|

#### IsHeroApp Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|True|
|0|False|

**DefaultValue**: False



### <a name="BKMK_IsHidden"></a> IsHidden

|Property|Value|
|--------|-----|
|Description|Indicates whether the canvas app is hidden from a user's list.|
|DisplayName|Is Hidden|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ishidden|
|RequiredLevel|None|
|Type|Boolean|

#### IsHidden Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|True|
|0|False|

**DefaultValue**: False



### <a name="BKMK_LastModifiedTime"></a> LastModifiedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the application was last modified.|
|DisplayName|Last Modified Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastmodifiedtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastPublishTime"></a> LastPublishTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the application was last published.|
|DisplayName|Last Publish Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastpublishtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_MinClientVersion"></a> MinClientVersion

|Property|Value|
|--------|-----|
|Description|The version of the client that was used to author the application.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|minclientversion|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the CanvasApp|
|DisplayName|CanvasApp Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the canvas app.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser|
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


### <a name="BKMK_Publisher"></a> Publisher

|Property|Value|
|--------|-----|
|Description|The publisher of the app.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|publisher|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Status"></a> Status

|Property|Value|
|--------|-----|
|Description|A value indicating whether the application is ready for consumption.|
|DisplayName|Status|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|status|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Tags"></a> Tags

|Property|Value|
|--------|-----|
|Description|The metadata tags of the application.|
|DisplayName||
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|tags|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [Assets_Name](#BKMK_Assets_Name)
- [BackgroundImage_Name](#BKMK_BackgroundImage_Name)
- [CanvasAppRowId](#BKMK_CanvasAppRowId)
- [ComponentState](#BKMK_ComponentState)
- [Document_Name](#BKMK_Document_Name)
- [IsManaged](#BKMK_IsManaged)
- [LargeIcon_Name](#BKMK_LargeIcon_Name)
- [MediumIcon_Name](#BKMK_MediumIcon_Name)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SmallIcon_Name](#BKMK_SmallIcon_Name)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TeamsIcon_Name](#BKMK_TeamsIcon_Name)
- [VersionNumber](#BKMK_VersionNumber)
- [WideIcon_Name](#BKMK_WideIcon_Name)


### <a name="BKMK_Assets_Name"></a> Assets_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|assets_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_BackgroundImage_Name"></a> BackgroundImage_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|backgroundimage_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CanvasAppRowId"></a> CanvasAppRowId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canvasapprowid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



### <a name="BKMK_Document_Name"></a> Document_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|document_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


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

|Value|Label|Description|
|-----|-----|--------|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_LargeIcon_Name"></a> LargeIcon_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|largeicon_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MediumIcon_Name"></a> MediumIcon_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mediumicon_name|
|MaxLength|200|
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


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit that owns the process.|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the process.|
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
|Description|Unique identifier of the user who owns the process.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_SmallIcon_Name"></a> SmallIcon_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|smallicon_name|
|MaxLength|200|
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


### <a name="BKMK_TeamsIcon_Name"></a> TeamsIcon_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|teamsicon_name|
|MaxLength|200|
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


### <a name="BKMK_WideIcon_Name"></a> WideIcon_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|wideicon_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [canvasapp_appaction_onclickeventformulacomponentlibraryid](#BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid)
- [canvasapp_appaction_visibilityformulacomponentlibraryid](#BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid)


### <a name="BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid"></a> canvasapp_appaction_onclickeventformulacomponentlibraryid

**Added by**: Power Apps Actions Solution

Same as appaction table [canvasapp_appaction_onclickeventformulacomponentlibraryid](appaction.md#BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appaction|
|ReferencingAttribute|onclickeventformulacomponentlibraryid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|canvasapp_appaction_onclickeventformulacomponentlibraryid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid"></a> canvasapp_appaction_visibilityformulacomponentlibraryid

**Added by**: Power Apps Actions Solution

Same as appaction table [canvasapp_appaction_visibilityformulacomponentlibraryid](appaction.md#BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appaction|
|ReferencingAttribute|visibilityformulacomponentlibraryid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|canvasapp_appaction_visibilityformulacomponentlibraryid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [businessunit_canvasapp](#BKMK_businessunit_canvasapp)
- [FK_CanvasApp_Solution](#BKMK_FK_CanvasApp_Solution)


### <a name="BKMK_businessunit_canvasapp"></a> businessunit_canvasapp

See businessunit Table [businessunit_canvasapp](businessunit.md#BKMK_businessunit_canvasapp) One-To-Many relationship.

### <a name="BKMK_FK_CanvasApp_Solution"></a> FK_CanvasApp_Solution

See solution Table [FK_CanvasApp_Solution](solution.md#BKMK_FK_CanvasApp_Solution) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.canvasapp?text=canvasapp EntityType" />