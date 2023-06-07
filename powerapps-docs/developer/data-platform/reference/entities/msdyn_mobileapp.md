---
title: "msdyn_mobileapp table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the msdyn_mobileapp table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# msdyn_mobileapp table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Mobile App

**Added by**: Mobile Apps Solution Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /msdyn_mobileapps(*msdyn_mobileappid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /msdyn_mobileapps<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msdyn_mobileapps(*msdyn_mobileappid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /msdyn_mobileapps(*msdyn_mobileappid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /msdyn_mobileapps<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /msdyn_mobileapps(*msdyn_mobileappid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /msdyn_mobileapps(*msdyn_mobileappid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_mobileapps|
|DisplayCollectionName|Mobile App|
|DisplayName|Mobile App|
|EntitySetName|msdyn_mobileapps|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_mobileapps|
|LogicalName|msdyn_mobileapp|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_mobileappid|
|PrimaryNameAttribute|name|
|SchemaName|msdyn_mobileapp|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [msdyn_actionButtonHighlight](#BKMK_msdyn_actionButtonHighlight)
- [msdyn_adalClientId](#BKMK_msdyn_adalClientId)
- [msdyn_adalRedirectUri](#BKMK_msdyn_adalRedirectUri)
- [msdyn_AndroidAppCenterAPIToken](#BKMK_msdyn_AndroidAppCenterAPIToken)
- [msdyn_AndroidAppCenterAPITokenSaved](#BKMK_msdyn_AndroidAppCenterAPITokenSaved)
- [msdyn_appCenterAppIdAab](#BKMK_msdyn_appCenterAppIdAab)
- [msdyn_appCenterAppIdApk](#BKMK_msdyn_appCenterAppIdApk)
- [msdyn_appCenterAppIdIpa](#BKMK_msdyn_appCenterAppIdIpa)
- [msdyn_buildDetails](#BKMK_msdyn_buildDetails)
- [msdyn_bundleIdentifier](#BKMK_msdyn_bundleIdentifier)
- [msdyn_buttonColor](#BKMK_msdyn_buttonColor)
- [msdyn_displayName](#BKMK_msdyn_displayName)
- [msdyn_fillColor](#BKMK_msdyn_fillColor)
- [msdyn_headingTextColor](#BKMK_msdyn_headingTextColor)
- [msdyn_hyperLinkColor](#BKMK_msdyn_hyperLinkColor)
- [msdyn_IOSAppCenterAPIToken](#BKMK_msdyn_IOSAppCenterAPIToken)
- [msdyn_IOSAppCenterAPITokenSaved](#BKMK_msdyn_IOSAppCenterAPITokenSaved)
- [msdyn_keyVaultUri](#BKMK_msdyn_keyVaultUri)
- [msdyn_mobileappId](#BKMK_msdyn_mobileappId)
- [msdyn_orgName](#BKMK_msdyn_orgName)
- [msdyn_platformType](#BKMK_msdyn_platformType)
- [msdyn_primaryPublishedAppName](#BKMK_msdyn_primaryPublishedAppName)
- [msdyn_recentBuild](#BKMK_msdyn_recentBuild)
- [msdyn_secondaryApps](#BKMK_msdyn_secondaryApps)
- [msdyn_secondaryPublishedAppNames](#BKMK_msdyn_secondaryPublishedAppNames)
- [msdyn_statusBarContentColorMode](#BKMK_msdyn_statusBarContentColorMode)
- [msdyn_UniqueName](#BKMK_msdyn_UniqueName)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Added by**: Basic Solution Solution

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


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_msdyn_actionButtonHighlight"></a> msdyn_actionButtonHighlight

|Property|Value|
|--------|-----|
|Description|Color used for action button when highlighted.|
|DisplayName|Action Button Highlight|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_actionbuttonhighlight|
|MaxLength|5000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_adalClientId"></a> msdyn_adalClientId

|Property|Value|
|--------|-----|
|Description|Active Directory Authentication Library Id used for Wrap.|
|DisplayName|Active Directory Authentication Library Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_adalclientid|
|MaxLength|5000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_adalRedirectUri"></a> msdyn_adalRedirectUri

|Property|Value|
|--------|-----|
|Description|Active Directory Authentication Library redirect URI used for Wrap.|
|DisplayName|Active Directory Authentication Library redirect URI|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_adalredirecturi|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_AndroidAppCenterAPIToken"></a> msdyn_AndroidAppCenterAPIToken

|Property|Value|
|--------|-----|
|Description|Android App center API token|
|DisplayName|Android App center API token|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_androidappcenterapitoken|
|MaxLength|5000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_AndroidAppCenterAPITokenSaved"></a> msdyn_AndroidAppCenterAPITokenSaved

|Property|Value|
|--------|-----|
|Description|Notify if the user have saved the Android token.|
|DisplayName|AndroidAppCenterAPITokenSaved|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_androidappcenterapitokensaved|
|MaxLength|5000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_appCenterAppIdAab"></a> msdyn_appCenterAppIdAab

|Property|Value|
|--------|-----|
|Description|Android App Center AppId aab.|
|DisplayName|App Center AppId Aab|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appcenterappidaab|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_appCenterAppIdApk"></a> msdyn_appCenterAppIdApk

|Property|Value|
|--------|-----|
|Description|Android App Center AppId.|
|DisplayName|App Center AppId Apk|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appcenterappidapk|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_appCenterAppIdIpa"></a> msdyn_appCenterAppIdIpa

|Property|Value|
|--------|-----|
|Description|IOS App center app id for ipa.|
|DisplayName|IOS App Center Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appcenterappidipa|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_buildDetails"></a> msdyn_buildDetails

|Property|Value|
|--------|-----|
|Description|All Build details of the App.|
|DisplayName|Build Details|
|Format|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_builddetails|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_bundleIdentifier"></a> msdyn_bundleIdentifier

|Property|Value|
|--------|-----|
|Description|The bundleIds resource represents the app's unique identifier that you can register, modify, and delete.|
|DisplayName|Bundle Identifier for App|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_bundleidentifier|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_buttonColor"></a> msdyn_buttonColor

|Property|Value|
|--------|-----|
|Description|The Button color used in the App.|
|DisplayName|Button Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_buttoncolor|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_displayName"></a> msdyn_displayName

|Property|Value|
|--------|-----|
|Description|Display name of the App.|
|DisplayName|Display Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_displayname|
|MaxLength|5000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_fillColor"></a> msdyn_fillColor

|Property|Value|
|--------|-----|
|Description|Fill color of the App.|
|DisplayName|Fill Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_fillcolor|
|MaxLength|5000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_headingTextColor"></a> msdyn_headingTextColor

|Property|Value|
|--------|-----|
|Description|Heading Text Color in the App.|
|DisplayName|Heading Text Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_headingtextcolor|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_hyperLinkColor"></a> msdyn_hyperLinkColor

|Property|Value|
|--------|-----|
|Description|Hyper Link Color in the App.|
|DisplayName|Hyper Link Color|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_hyperlinkcolor|
|MaxLength|5000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_IOSAppCenterAPIToken"></a> msdyn_IOSAppCenterAPIToken

|Property|Value|
|--------|-----|
|Description|IOS App Center API token|
|DisplayName|IOS App Center API token|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_iosappcenterapitoken|
|MaxLength|5000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_IOSAppCenterAPITokenSaved"></a> msdyn_IOSAppCenterAPITokenSaved

|Property|Value|
|--------|-----|
|Description|Notify if the user have saved the IOS token.|
|DisplayName|IOSAppCenterAPITokenSaved|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_iosappcenterapitokensaved|
|MaxLength|5000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_keyVaultUri"></a> msdyn_keyVaultUri

|Property|Value|
|--------|-----|
|Description|Key Vault Uri.|
|DisplayName|Key Vault Uri|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_keyvaulturi|
|MaxLength|5000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_mobileappId"></a> msdyn_mobileappId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Mobile App Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_mobileappid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_orgName"></a> msdyn_orgName

|Property|Value|
|--------|-----|
|Description|Organization Name in App Center|
|DisplayName|Organization Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_orgname|
|MaxLength|5000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_platformType"></a> msdyn_platformType

|Property|Value|
|--------|-----|
|Description|Platform Type of Phone IOS/Android.|
|DisplayName|Platform Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_platformtype|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_primaryPublishedAppName"></a> msdyn_primaryPublishedAppName

|Property|Value|
|--------|-----|
|Description|Primary Published Canvas App to used in the Wrap.|
|DisplayName|Primary Published Canvas App|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_primarypublishedappname|
|RequiredLevel|ApplicationRequired|
|Targets|canvasapp|
|Type|Lookup|


### <a name="BKMK_msdyn_recentBuild"></a> msdyn_recentBuild

|Property|Value|
|--------|-----|
|Description|Recent build details of the App.|
|DisplayName|Recent build|
|Format|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_recentbuild|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_secondaryApps"></a> msdyn_secondaryApps

|Property|Value|
|--------|-----|
|Description|Secondary Apps used for Wrap.|
|DisplayName|Secondary Apps used for Wrap|
|Format|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_secondaryapps|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_secondaryPublishedAppNames"></a> msdyn_secondaryPublishedAppNames

|Property|Value|
|--------|-----|
|Description|Secondary Published App Names to used in the Wrap.|
|DisplayName|Secondary Published App Names|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_secondarypublishedappnames|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_statusBarContentColorMode"></a> msdyn_statusBarContentColorMode

|Property|Value|
|--------|-----|
|Description|Status Bar Content Color Mode of the App.|
|DisplayName|Status Bar Content Color Mode|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_statusbarcontentcolormode|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_UniqueName"></a> msdyn_UniqueName

|Property|Value|
|--------|-----|
|Description|Unique Name for the entity.|
|DisplayName|Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_uniquename|
|MaxLength|128|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_name"></a> name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
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
|Description|Owner Id|
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
|Description|Status of the MobileApp|
|DisplayName|Status|
|IsValidForCreate|False|
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
|Description|Reason for the status of the msdyn_mobileapp|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [msdyn_appIcon1024x1024](#BKMK_msdyn_appIcon1024x1024)
- [msdyn_appIcon1024x1024_Name](#BKMK_msdyn_appIcon1024x1024_Name)
- [msdyn_appIcon120x120](#BKMK_msdyn_appIcon120x120)
- [msdyn_appIcon120x120_Name](#BKMK_msdyn_appIcon120x120_Name)
- [msdyn_appIcon152x152](#BKMK_msdyn_appIcon152x152)
- [msdyn_appIcon152x152_Name](#BKMK_msdyn_appIcon152x152_Name)
- [msdyn_appIcon167x167](#BKMK_msdyn_appIcon167x167)
- [msdyn_appIcon167x167_Name](#BKMK_msdyn_appIcon167x167_Name)
- [msdyn_appIcon180x180](#BKMK_msdyn_appIcon180x180)
- [msdyn_appIcon180x180_Name](#BKMK_msdyn_appIcon180x180_Name)
- [msdyn_appIconHdpi](#BKMK_msdyn_appIconHdpi)
- [msdyn_appIconHdpi_Name](#BKMK_msdyn_appIconHdpi_Name)
- [msdyn_appIconMdpi](#BKMK_msdyn_appIconMdpi)
- [msdyn_appIconMdpi_Name](#BKMK_msdyn_appIconMdpi_Name)
- [msdyn_appIconXdpi](#BKMK_msdyn_appIconXdpi)
- [msdyn_appIconXdpi_Name](#BKMK_msdyn_appIconXdpi_Name)
- [msdyn_appIconXxhdpi](#BKMK_msdyn_appIconXxhdpi)
- [msdyn_appIconXxhdpi_Name](#BKMK_msdyn_appIconXxhdpi_Name)
- [msdyn_appIconXxxhdpi](#BKMK_msdyn_appIconXxxhdpi)
- [msdyn_appIconXxxhdpi_Name](#BKMK_msdyn_appIconXxxhdpi_Name)
- [msdyn_launchAppResources](#BKMK_msdyn_launchAppResources)
- [msdyn_launchAppResources_Name](#BKMK_msdyn_launchAppResources_Name)
- [msdyn_mobileAppDefinitionAndroid](#BKMK_msdyn_mobileAppDefinitionAndroid)
- [msdyn_mobileAppDefinitionAndroid_Name](#BKMK_msdyn_mobileAppDefinitionAndroid_Name)
- [msdyn_mobileAppDefinitionIOS](#BKMK_msdyn_mobileAppDefinitionIOS)
- [msdyn_mobileAppDefinitionIOS_Name](#BKMK_msdyn_mobileAppDefinitionIOS_Name)
- [msdyn_primaryPublishedAppNameName](#BKMK_msdyn_primaryPublishedAppNameName)
- [msdyn_tenantSplashImage](#BKMK_msdyn_tenantSplashImage)
- [msdyn_tenantSplashImage_Name](#BKMK_msdyn_tenantSplashImage_Name)
- [msdyn_tenantWelcomeImage](#BKMK_msdyn_tenantWelcomeImage)
- [msdyn_tenantWelcomeImage_Name](#BKMK_msdyn_tenantWelcomeImage_Name)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Row id unique|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ComponentState"></a> ComponentState

**Added by**: Basic Solution Solution

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
|Description|Date and time when the record was created.|
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


### <a name="BKMK_IsManaged"></a> IsManaged

**Added by**: Basic Solution Solution

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
|1|Managed||
|0|Unmanaged||

**DefaultValue**: 0



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


### <a name="BKMK_msdyn_appIcon1024x1024"></a> msdyn_appIcon1024x1024

|Property|Value|
|--------|-----|
|Description|App Icon with 1024 x 1024 dimension|
|DisplayName|IOS App Icon 1024x1024|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appicon1024x1024|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_appIcon1024x1024_Name"></a> msdyn_appIcon1024x1024_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_appicon1024x1024_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_appIcon120x120"></a> msdyn_appIcon120x120

|Property|Value|
|--------|-----|
|Description|App Icon with 120 x 120 dimension|
|DisplayName|IOS App Icon 120x120|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appicon120x120|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_appIcon120x120_Name"></a> msdyn_appIcon120x120_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_appicon120x120_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_appIcon152x152"></a> msdyn_appIcon152x152

|Property|Value|
|--------|-----|
|Description|App Icon with 152 x 152 dimension|
|DisplayName|IOS App Icon 152x152|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appicon152x152|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_appIcon152x152_Name"></a> msdyn_appIcon152x152_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_appicon152x152_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_appIcon167x167"></a> msdyn_appIcon167x167

|Property|Value|
|--------|-----|
|Description|App Icon with 167 x 167 dimension|
|DisplayName|IOS App Icon 167x167|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appicon167x167|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_appIcon167x167_Name"></a> msdyn_appIcon167x167_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_appicon167x167_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_appIcon180x180"></a> msdyn_appIcon180x180

|Property|Value|
|--------|-----|
|Description|App Icon with 180 x 180 dimension|
|DisplayName|IOS App Icon 180x180|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appicon180x180|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_appIcon180x180_Name"></a> msdyn_appIcon180x180_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_appicon180x180_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_appIconHdpi"></a> msdyn_appIconHdpi

|Property|Value|
|--------|-----|
|Description|App Icon with 162 x 162 dimension|
|DisplayName|Android App Icon Hdpi|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appiconhdpi|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_appIconHdpi_Name"></a> msdyn_appIconHdpi_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_appiconhdpi_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_appIconMdpi"></a> msdyn_appIconMdpi

|Property|Value|
|--------|-----|
|Description|App Icon with 108 x 108 dimension|
|DisplayName|Android App Icon Mdpi|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appiconmdpi|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_appIconMdpi_Name"></a> msdyn_appIconMdpi_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_appiconmdpi_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_appIconXdpi"></a> msdyn_appIconXdpi

|Property|Value|
|--------|-----|
|Description|App Icon with 216 x 216 dimension|
|DisplayName|Android App Icon Xdpi|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appiconxdpi|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_appIconXdpi_Name"></a> msdyn_appIconXdpi_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_appiconxdpi_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_appIconXxhdpi"></a> msdyn_appIconXxhdpi

|Property|Value|
|--------|-----|
|Description|App Icon with 324 x 324 dimension|
|DisplayName|Android App Icon XXdpi|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appiconxxhdpi|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_appIconXxhdpi_Name"></a> msdyn_appIconXxhdpi_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_appiconxxhdpi_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_appIconXxxhdpi"></a> msdyn_appIconXxxhdpi

|Property|Value|
|--------|-----|
|Description|App Icon with 432 x 432 dimension|
|DisplayName|Android App Icon XXXdpi|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appiconxxxhdpi|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_appIconXxxhdpi_Name"></a> msdyn_appIconXxxhdpi_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_appiconxxxhdpi_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_launchAppResources"></a> msdyn_launchAppResources

|Property|Value|
|--------|-----|
|Description|Launch App Resources used to package the App.|
|DisplayName|Launch App Resources|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_launchappresources|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_launchAppResources_Name"></a> msdyn_launchAppResources_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_launchappresources_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_mobileAppDefinitionAndroid"></a> msdyn_mobileAppDefinitionAndroid

|Property|Value|
|--------|-----|
|Description|Mobile App Definition Android to package App.|
|DisplayName|Mobile App Definition Android|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_mobileappdefinitionandroid|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_mobileAppDefinitionAndroid_Name"></a> msdyn_mobileAppDefinitionAndroid_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_mobileappdefinitionandroid_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_mobileAppDefinitionIOS"></a> msdyn_mobileAppDefinitionIOS

|Property|Value|
|--------|-----|
|Description|Mobile App Definition IOS to package App.|
|DisplayName|Mobile App Definition IOS|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_mobileappdefinitionios|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_mobileAppDefinitionIOS_Name"></a> msdyn_mobileAppDefinitionIOS_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_mobileappdefinitionios_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_primaryPublishedAppNameName"></a> msdyn_primaryPublishedAppNameName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_primarypublishedappnamename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_tenantSplashImage"></a> msdyn_tenantSplashImage

|Property|Value|
|--------|-----|
|Description|Tenant Splash Image in the App.|
|DisplayName|Tenant Splash Image|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_tenantsplashimage|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_tenantSplashImage_Name"></a> msdyn_tenantSplashImage_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_tenantsplashimage_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_tenantWelcomeImage"></a> msdyn_tenantWelcomeImage

|Property|Value|
|--------|-----|
|Description|Tenant Welcome Image in the App.|
|DisplayName|Tenant Welcome Image|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_tenantwelcomeimage|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_tenantWelcomeImage_Name"></a> msdyn_tenantWelcomeImage_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_tenantwelcomeimage_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


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


### <a name="BKMK_SolutionId"></a> SolutionId

**Added by**: Basic Solution Solution

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

**Added by**: Basic Solution Solution

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

- [msdyn_mobileapp_SyncErrors](#BKMK_msdyn_mobileapp_SyncErrors)
- [msdyn_mobileapp_DuplicateMatchingRecord](#BKMK_msdyn_mobileapp_DuplicateMatchingRecord)
- [msdyn_mobileapp_DuplicateBaseRecord](#BKMK_msdyn_mobileapp_DuplicateBaseRecord)
- [msdyn_mobileapp_AsyncOperations](#BKMK_msdyn_mobileapp_AsyncOperations)
- [msdyn_mobileapp_MailboxTrackingFolders](#BKMK_msdyn_mobileapp_MailboxTrackingFolders)
- [msdyn_mobileapp_ProcessSession](#BKMK_msdyn_mobileapp_ProcessSession)
- [msdyn_mobileapp_BulkDeleteFailures](#BKMK_msdyn_mobileapp_BulkDeleteFailures)
- [msdyn_mobileapp_PrincipalObjectAttributeAccesses](#BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses)


### <a name="BKMK_msdyn_mobileapp_SyncErrors"></a> msdyn_mobileapp_SyncErrors

**Added by**: System Solution Solution

Same as the [msdyn_mobileapp_SyncErrors](syncerror.md#BKMK_msdyn_mobileapp_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_mobileapp_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_mobileapp_DuplicateMatchingRecord"></a> msdyn_mobileapp_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [msdyn_mobileapp_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_mobileapp_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_mobileapp_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_mobileapp_DuplicateBaseRecord"></a> msdyn_mobileapp_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [msdyn_mobileapp_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_mobileapp_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_mobileapp_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_mobileapp_AsyncOperations"></a> msdyn_mobileapp_AsyncOperations

**Added by**: System Solution Solution

Same as the [msdyn_mobileapp_AsyncOperations](asyncoperation.md#BKMK_msdyn_mobileapp_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_mobileapp_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_mobileapp_MailboxTrackingFolders"></a> msdyn_mobileapp_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msdyn_mobileapp_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_mobileapp_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_mobileapp_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_mobileapp_ProcessSession"></a> msdyn_mobileapp_ProcessSession

**Added by**: System Solution Solution

Same as the [msdyn_mobileapp_ProcessSession](processsession.md#BKMK_msdyn_mobileapp_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_mobileapp_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_mobileapp_BulkDeleteFailures"></a> msdyn_mobileapp_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msdyn_mobileapp_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_mobileapp_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_mobileapp_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses"></a> msdyn_mobileapp_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msdyn_mobileapp_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_mobileapp_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_mobileapp_createdby](#BKMK_lk_msdyn_mobileapp_createdby)
- [lk_msdyn_mobileapp_createdonbehalfby](#BKMK_lk_msdyn_mobileapp_createdonbehalfby)
- [lk_msdyn_mobileapp_modifiedby](#BKMK_lk_msdyn_mobileapp_modifiedby)
- [lk_msdyn_mobileapp_modifiedonbehalfby](#BKMK_lk_msdyn_mobileapp_modifiedonbehalfby)
- [user_msdyn_mobileapp](#BKMK_user_msdyn_mobileapp)
- [team_msdyn_mobileapp](#BKMK_team_msdyn_mobileapp)
- [business_unit_msdyn_mobileapp](#BKMK_business_unit_msdyn_mobileapp)
- [canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName](#BKMK_canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName)


### <a name="BKMK_lk_msdyn_mobileapp_createdby"></a> lk_msdyn_mobileapp_createdby

**Added by**: System Solution Solution

See the [lk_msdyn_mobileapp_createdby](systemuser.md#BKMK_lk_msdyn_mobileapp_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_mobileapp_createdonbehalfby"></a> lk_msdyn_mobileapp_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_mobileapp_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_mobileapp_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_mobileapp_modifiedby"></a> lk_msdyn_mobileapp_modifiedby

**Added by**: System Solution Solution

See the [lk_msdyn_mobileapp_modifiedby](systemuser.md#BKMK_lk_msdyn_mobileapp_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_mobileapp_modifiedonbehalfby"></a> lk_msdyn_mobileapp_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_mobileapp_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_mobileapp_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_msdyn_mobileapp"></a> user_msdyn_mobileapp

**Added by**: System Solution Solution

See the [user_msdyn_mobileapp](systemuser.md#BKMK_user_msdyn_mobileapp) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_msdyn_mobileapp"></a> team_msdyn_mobileapp

**Added by**: System Solution Solution

See the [team_msdyn_mobileapp](team.md#BKMK_team_msdyn_mobileapp) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_msdyn_mobileapp"></a> business_unit_msdyn_mobileapp

**Added by**: System Solution Solution

See the [business_unit_msdyn_mobileapp](businessunit.md#BKMK_business_unit_msdyn_mobileapp) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName"></a> canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName

**Added by**: System Solution Solution

See the [canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName](canvasapp.md#BKMK_canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName) one-to-many relationship for the [canvasapp](canvasapp.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msdyn_mobileapp?text=msdyn_mobileapp EntityType" />