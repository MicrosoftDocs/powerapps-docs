---
title: "Canvas App (CanvasApp) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Canvas App (CanvasApp) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Canvas App (CanvasApp) table/entity reference (Microsoft Dataverse)

An application built through a canvas-based editing experience.

## Messages

The following table lists the messages for the Canvas App (CanvasApp) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: False |`PATCH` /canvasapps(*canvasappid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /canvasapps<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /canvasapps(*canvasappid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /canvasapps(*canvasappid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /canvasapps<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `Update`<br />Event: False |`PATCH` /canvasapps(*canvasappid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /canvasapps(*canvasappid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Canvas App (CanvasApp) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Canvas App** |
| **DisplayCollectionName** | **Canvas Apps** |
| **SchemaName** | `CanvasApp` |
| **CollectionSchemaName** | `Canvas Apps` |
| **EntitySetName** | `canvasapps`|
| **LogicalName** | `canvasapp` |
| **LogicalCollectionName** | `canvasapps` |
| **PrimaryIdAttribute** | `canvasappid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

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
- [UniqueCanvasAppId](#BKMK_UniqueCanvasAppId)

### <a name="BKMK_AADCreatedById"></a> AADCreatedById

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the canvas app.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aadcreatedbyid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_AADLastModifiedById"></a> AADLastModifiedById

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the application.**|
|DisplayName|**Last Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aadlastmodifiedbyid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_AADLastPublishedById"></a> AADLastPublishedById

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last published the application.**|
|DisplayName|**Last Published By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aadlastpublishedbyid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_AdminControlBypassConsent"></a> AdminControlBypassConsent

|Property|Value|
|---|---|
|Description|**Indicates whether the canvas app was marked for bypass consent by an admin.**|
|DisplayName|**Admin Control Bypass Consent**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`admincontrolbypassconsent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`canvasapp_admincontrolbypassconsent`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_AppComponentDependencies"></a> AppComponentDependencies

|Property|Value|
|---|---|
|Description|**The app component dependencies.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appcomponentdependencies`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|768000|

### <a name="BKMK_AppComponents"></a> AppComponents

|Property|Value|
|---|---|
|Description|**The app components.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appcomponents`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|768000|

### <a name="BKMK_AppOpenUri"></a> AppOpenUri

|Property|Value|
|---|---|
|Description|**The app open URI.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appopenuri`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_AppVersion"></a> AppVersion

|Property|Value|
|---|---|
|Description|**The application version.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appversion`|
|RequiredLevel|SystemRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_AuthorizationReferences"></a> AuthorizationReferences

|Property|Value|
|---|---|
|Description|**The authorization references of the application.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`authorizationreferences`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_BackgroundColor"></a> BackgroundColor

|Property|Value|
|---|---|
|Description|**The background image color.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`backgroundcolor`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_BypassConsent"></a> BypassConsent

|Property|Value|
|---|---|
|Description|**Indicates whether the canvas app should bypass consent from consumers.**|
|DisplayName|**Bypass Consent**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`bypassconsent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`canvasapp_bypassconsent`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_CanConsumeAppPass"></a> CanConsumeAppPass

|Property|Value|
|---|---|
|Description|**The type of the canvas app.**|
|DisplayName|**Can Consume App Pass**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canconsumeapppass`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`canvasapp_canconsumeapppass`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_CanvasAppId"></a> CanvasAppId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canvasappid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_CanvasAppType"></a> CanvasAppType

|Property|Value|
|---|---|
|Description|**The type of the canvas app.**|
|DisplayName|**Canvas App Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canvasapptype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`canvasapp_canvasapptype`|

#### CanvasAppType Choices/Options

|Value|Label|
|---|---|
|0|**Classic Canvas App**|
|1|**App Component Library**|
|2|**Custom Canvas Page**|
|3|**Unified App**|

### <a name="BKMK_CdsDependencies"></a> CdsDependencies

|Property|Value|
|---|---|
|Description|**Internal use. The app dependency details.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`cdsdependencies`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|768000|

### <a name="BKMK_CommitMessage"></a> CommitMessage

|Property|Value|
|---|---|
|Description|**The commit message of the app.**|
|DisplayName|**The commit message.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`commitmessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_ConnectionReferences"></a> ConnectionReferences

|Property|Value|
|---|---|
|Description|**The connection references of the application.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`connectionreferences`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|768000|

### <a name="BKMK_CreatedByClientVersion"></a> CreatedByClientVersion

|Property|Value|
|---|---|
|Description|**The version of the client that was used to author the application.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdbyclientversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_CreatedTime"></a> CreatedTime

|Property|Value|
|---|---|
|Description|**Date and time when the application was created.**|
|DisplayName|**Created Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_DatabaseReferences"></a> DatabaseReferences

|Property|Value|
|---|---|
|Description|**The database references of the application.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`databasereferences`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|768000|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**The description of the app.**|
|DisplayName|**The description.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|---|---|
|Description|**The display name of the app.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`displayname`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_EmbeddedApp"></a> EmbeddedApp

|Property|Value|
|---|---|
|Description|**Internal use. The embedded app information.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`embeddedapp`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_GalleryItemId"></a> GalleryItemId

|Property|Value|
|---|---|
|Description|**The gallery item identifier.**|
|DisplayName|**The gallery item identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`galleryitemid`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the canvas app is introduced.**|
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

### <a name="BKMK_IsCdsUpgraded"></a> IsCdsUpgraded

|Property|Value|
|---|---|
|Description|**Indicates whether the canvas app contains CDS 1.0 references.**|
|DisplayName|**Is CDS Upgraded**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscdsupgraded`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`canvasapp_iscdsupgraded`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

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

### <a name="BKMK_IsFeaturedApp"></a> IsFeaturedApp

|Property|Value|
|---|---|
|Description|**Indicates whether the canvas app is a featured app.**|
|DisplayName|**Is Featured App**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isfeaturedapp`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`canvasapp_isfeatured`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_IsHeroApp"></a> IsHeroApp

|Property|Value|
|---|---|
|Description|**Indicates whether the canvas app is a hero app.**|
|DisplayName|**Is Hero App**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isheroapp`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`canvasapp_isheroapp`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_IsHidden"></a> IsHidden

|Property|Value|
|---|---|
|Description|**Indicates whether the canvas app is hidden from a user's list.**|
|DisplayName|**Is Hidden**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ishidden`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`canvasapp_ishidden`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

### <a name="BKMK_LastModifiedTime"></a> LastModifiedTime

|Property|Value|
|---|---|
|Description|**Date and time when the application was last modified.**|
|DisplayName|**Last Modified Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastmodifiedtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_LastPublishTime"></a> LastPublishTime

|Property|Value|
|---|---|
|Description|**Date and time when the application was last published.**|
|DisplayName|**Last Publish Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastpublishtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_MinClientVersion"></a> MinClientVersion

|Property|Value|
|---|---|
|Description|**The version of the client that was used to author the application.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`minclientversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the CanvasApp**|
|DisplayName|**CanvasApp Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the canvas app.**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser|

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

### <a name="BKMK_Publisher"></a> Publisher

|Property|Value|
|---|---|
|Description|**The publisher of the app.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publisher`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_Status"></a> Status

|Property|Value|
|---|---|
|Description|**A value indicating whether the application is ready for consumption.**|
|DisplayName|**Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`status`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_Tags"></a> Tags

|Property|Value|
|---|---|
|Description|**The metadata tags of the application.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`tags`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_UniqueCanvasAppId"></a> UniqueCanvasAppId

|Property|Value|
|---|---|
|Description|**The globally unique canvas app id**|
|DisplayName|**Unique CanvasApp Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniquecanvasappid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [Assets](#BKMK_Assets)
- [Assets_Name](#BKMK_Assets_Name)
- [BackgroundImage](#BKMK_BackgroundImage)
- [BackgroundImage_Name](#BKMK_BackgroundImage_Name)
- [CanvasAppRowId](#BKMK_CanvasAppRowId)
- [ComponentState](#BKMK_ComponentState)
- [Document](#BKMK_Document)
- [Document_Name](#BKMK_Document_Name)
- [IsManaged](#BKMK_IsManaged)
- [LargeIcon](#BKMK_LargeIcon)
- [LargeIcon_Name](#BKMK_LargeIcon_Name)
- [MediumIcon](#BKMK_MediumIcon)
- [MediumIcon_Name](#BKMK_MediumIcon_Name)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SmallIcon](#BKMK_SmallIcon)
- [SmallIcon_Name](#BKMK_SmallIcon_Name)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TeamsIcon](#BKMK_TeamsIcon)
- [TeamsIcon_Name](#BKMK_TeamsIcon_Name)
- [VersionNumber](#BKMK_VersionNumber)
- [WideIcon](#BKMK_WideIcon)
- [WideIcon_Name](#BKMK_WideIcon_Name)

### <a name="BKMK_Assets"></a> Assets

|Property|Value|
|---|---|
|Description|**Assets for Canvas Apps.**|
|DisplayName|**Assets**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`assets`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_Assets_Name"></a> Assets_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`assets_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_BackgroundImage"></a> BackgroundImage

|Property|Value|
|---|---|
|Description|**Background image for Canvas Apps.**|
|DisplayName|**Background Image**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`background_image`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_BackgroundImage_Name"></a> BackgroundImage_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`backgroundimage_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_CanvasAppRowId"></a> CanvasAppRowId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canvasapprowid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

### <a name="BKMK_Document"></a> Document

|Property|Value|
|---|---|
|Description|**Document for Canvas Apps.**|
|DisplayName|**Document**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`document`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_Document_Name"></a> Document_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`document_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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

### <a name="BKMK_LargeIcon"></a> LargeIcon

|Property|Value|
|---|---|
|Description|**Large icon for Canvas Apps.**|
|DisplayName|**Large Icon**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`large_icon`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_LargeIcon_Name"></a> LargeIcon_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`largeicon_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_MediumIcon"></a> MediumIcon

|Property|Value|
|---|---|
|Description|**Medium icon for Canvas Apps.**|
|DisplayName|**Medium Icon**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`medium_icon`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_MediumIcon_Name"></a> MediumIcon_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mediumicon_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit that owns the process.**|
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
|Description|**Unique identifier of the team who owns the process.**|
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
|Description|**Unique identifier of the user who owns the process.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_SmallIcon"></a> SmallIcon

|Property|Value|
|---|---|
|Description|**Small icon for Canvas Apps.**|
|DisplayName|**Small Icon**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`small_icon`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_SmallIcon_Name"></a> SmallIcon_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`smallicon_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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

### <a name="BKMK_TeamsIcon"></a> TeamsIcon

|Property|Value|
|---|---|
|Description|**Teams icon for Canvas Apps.**|
|DisplayName|**Teams Icon**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`teams_icon`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_TeamsIcon_Name"></a> TeamsIcon_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`teamsicon_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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

### <a name="BKMK_WideIcon"></a> WideIcon

|Property|Value|
|---|---|
|Description|**Wide icon for Canvas Apps.**|
|DisplayName|**Wide Icon**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`wide_icon`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_WideIcon_Name"></a> WideIcon_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`wideicon_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [businessunit_canvasapp](#BKMK_businessunit_canvasapp)
- [FileAttachment_CanvasApp_Assets](#BKMK_FileAttachment_CanvasApp_Assets)
- [FileAttachment_CanvasApp_BackgroundImage](#BKMK_FileAttachment_CanvasApp_BackgroundImage)
- [FileAttachment_CanvasApp_Document](#BKMK_FileAttachment_CanvasApp_Document)
- [FileAttachment_CanvasApp_LargeIcon](#BKMK_FileAttachment_CanvasApp_LargeIcon)
- [FileAttachment_CanvasApp_MediumIcon](#BKMK_FileAttachment_CanvasApp_MediumIcon)
- [FileAttachment_CanvasApp_SmallIcon](#BKMK_FileAttachment_CanvasApp_SmallIcon)
- [FileAttachment_CanvasApp_TeamsIcon](#BKMK_FileAttachment_CanvasApp_TeamsIcon)
- [FileAttachment_CanvasApp_WideIcon](#BKMK_FileAttachment_CanvasApp_WideIcon)
- [FK_CanvasApp_Solution](#BKMK_FK_CanvasApp_Solution)
- [owner_canvasapp](#BKMK_owner_canvasapp)

### <a name="BKMK_businessunit_canvasapp"></a> businessunit_canvasapp

One-To-Many Relationship: [businessunit businessunit_canvasapp](businessunit.md#BKMK_businessunit_canvasapp)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_CanvasApp_Assets"></a> FileAttachment_CanvasApp_Assets

One-To-Many Relationship: [fileattachment FileAttachment_CanvasApp_Assets](fileattachment.md#BKMK_FileAttachment_CanvasApp_Assets)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`assets`|
|ReferencingEntityNavigationPropertyName|`assets`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_CanvasApp_BackgroundImage"></a> FileAttachment_CanvasApp_BackgroundImage

One-To-Many Relationship: [fileattachment FileAttachment_CanvasApp_BackgroundImage](fileattachment.md#BKMK_FileAttachment_CanvasApp_BackgroundImage)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`background_image`|
|ReferencingEntityNavigationPropertyName|`backgroundimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_CanvasApp_Document"></a> FileAttachment_CanvasApp_Document

One-To-Many Relationship: [fileattachment FileAttachment_CanvasApp_Document](fileattachment.md#BKMK_FileAttachment_CanvasApp_Document)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`document`|
|ReferencingEntityNavigationPropertyName|`document`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_CanvasApp_LargeIcon"></a> FileAttachment_CanvasApp_LargeIcon

One-To-Many Relationship: [fileattachment FileAttachment_CanvasApp_LargeIcon](fileattachment.md#BKMK_FileAttachment_CanvasApp_LargeIcon)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`large_icon`|
|ReferencingEntityNavigationPropertyName|`largeicon`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_CanvasApp_MediumIcon"></a> FileAttachment_CanvasApp_MediumIcon

One-To-Many Relationship: [fileattachment FileAttachment_CanvasApp_MediumIcon](fileattachment.md#BKMK_FileAttachment_CanvasApp_MediumIcon)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`medium_icon`|
|ReferencingEntityNavigationPropertyName|`mediumicon`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_CanvasApp_SmallIcon"></a> FileAttachment_CanvasApp_SmallIcon

One-To-Many Relationship: [fileattachment FileAttachment_CanvasApp_SmallIcon](fileattachment.md#BKMK_FileAttachment_CanvasApp_SmallIcon)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`small_icon`|
|ReferencingEntityNavigationPropertyName|`smallicon`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_CanvasApp_TeamsIcon"></a> FileAttachment_CanvasApp_TeamsIcon

One-To-Many Relationship: [fileattachment FileAttachment_CanvasApp_TeamsIcon](fileattachment.md#BKMK_FileAttachment_CanvasApp_TeamsIcon)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`teams_icon`|
|ReferencingEntityNavigationPropertyName|`teamsicon`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_CanvasApp_WideIcon"></a> FileAttachment_CanvasApp_WideIcon

One-To-Many Relationship: [fileattachment FileAttachment_CanvasApp_WideIcon](fileattachment.md#BKMK_FileAttachment_CanvasApp_WideIcon)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`wide_icon`|
|ReferencingEntityNavigationPropertyName|`wideicon`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FK_CanvasApp_Solution"></a> FK_CanvasApp_Solution

One-To-Many Relationship: [solution FK_CanvasApp_Solution](solution.md#BKMK_FK_CanvasApp_Solution)

|Property|Value|
|---|---|
|ReferencedEntity|`solution`|
|ReferencedAttribute|`solutionid`|
|ReferencingAttribute|`solutionid`|
|ReferencingEntityNavigationPropertyName|`FK_CanvasApp_Solution`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_canvasapp"></a> owner_canvasapp

One-To-Many Relationship: [owner owner_canvasapp](owner.md#BKMK_owner_canvasapp)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [canvasapp_appaction_onclickeventformulacomponentlibraryid](#BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid)
- [canvasapp_appaction_visibilityformulacomponentlibraryid](#BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid)
- [canvasapp_FileAttachments](#BKMK_canvasapp_FileAttachments)
- [canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName](#BKMK_canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName)

### <a name="BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid"></a> canvasapp_appaction_onclickeventformulacomponentlibraryid

Many-To-One Relationship: [appaction canvasapp_appaction_onclickeventformulacomponentlibraryid](appaction.md#BKMK_canvasapp_appaction_onclickeventformulacomponentlibraryid)

|Property|Value|
|---|---|
|ReferencingEntity|`appaction`|
|ReferencingAttribute|`onclickeventformulacomponentlibraryid`|
|ReferencedEntityNavigationPropertyName|`canvasapp_appaction_onclickeventformulacomponentlibraryid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid"></a> canvasapp_appaction_visibilityformulacomponentlibraryid

Many-To-One Relationship: [appaction canvasapp_appaction_visibilityformulacomponentlibraryid](appaction.md#BKMK_canvasapp_appaction_visibilityformulacomponentlibraryid)

|Property|Value|
|---|---|
|ReferencingEntity|`appaction`|
|ReferencingAttribute|`visibilityformulacomponentlibraryid`|
|ReferencedEntityNavigationPropertyName|`canvasapp_appaction_visibilityformulacomponentlibraryid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_canvasapp_FileAttachments"></a> canvasapp_FileAttachments

Many-To-One Relationship: [fileattachment canvasapp_FileAttachments](fileattachment.md#BKMK_canvasapp_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`canvasapp_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName"></a> canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName

Many-To-One Relationship: [msdyn_mobileapp canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName](msdyn_mobileapp.md#BKMK_canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_primarypublishedappname`|
|ReferencedEntityNavigationPropertyName|`canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.canvasapp?displayProperty=fullName>
