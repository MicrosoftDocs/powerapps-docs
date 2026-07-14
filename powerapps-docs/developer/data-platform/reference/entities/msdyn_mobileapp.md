---
title: "Mobile App (msdyn_mobileapp) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Mobile App (msdyn_mobileapp) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Mobile App (msdyn_mobileapp) table/entity reference (Microsoft Dataverse)

Mobile App

## Messages

The following table lists the messages for the Mobile App (msdyn_mobileapp) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_mobileapps(*msdyn_mobileappid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_mobileapps<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_mobileapps(*msdyn_mobileappid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_mobileapps(*msdyn_mobileappid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_mobileapps<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_mobileapps(*msdyn_mobileappid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_mobileapps(*msdyn_mobileappid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_mobileapps(*msdyn_mobileappid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Mobile App (msdyn_mobileapp) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Mobile App (msdyn_mobileapp) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Mobile App** |
| **DisplayCollectionName** | **Mobile App** |
| **SchemaName** | `msdyn_mobileapp` |
| **CollectionSchemaName** | `msdyn_mobileapps` |
| **EntitySetName** | `msdyn_mobileapps`|
| **LogicalName** | `msdyn_mobileapp` |
| **LogicalCollectionName** | `msdyn_mobileapps` |
| **PrimaryIdAttribute** | `msdyn_mobileappid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

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
- [msdyn_azureBlobStorageAccountName](#BKMK_msdyn_azureBlobStorageAccountName)
- [msdyn_azureBlobStorageContainerName](#BKMK_msdyn_azureBlobStorageContainerName)
- [msdyn_branch](#BKMK_msdyn_branch)
- [msdyn_buildDetails](#BKMK_msdyn_buildDetails)
- [msdyn_bundleIdentifier](#BKMK_msdyn_bundleIdentifier)
- [msdyn_buttonColor](#BKMK_msdyn_buttonColor)
- [msdyn_customDimensions](#BKMK_msdyn_customDimensions)
- [msdyn_displayName](#BKMK_msdyn_displayName)
- [msdyn_fillColor](#BKMK_msdyn_fillColor)
- [msdyn_headingTextColor](#BKMK_msdyn_headingTextColor)
- [msdyn_hyperLinkColor](#BKMK_msdyn_hyperLinkColor)
- [msdyn_IOSAppCenterAPIToken](#BKMK_msdyn_IOSAppCenterAPIToken)
- [msdyn_IOSAppCenterAPITokenSaved](#BKMK_msdyn_IOSAppCenterAPITokenSaved)
- [msdyn_iosEnterpriseSigningEnabled](#BKMK_msdyn_iosEnterpriseSigningEnabled)
- [msdyn_isAppSigningEnabled](#BKMK_msdyn_isAppSigningEnabled)
- [msdyn_keyVaultUri](#BKMK_msdyn_keyVaultUri)
- [msdyn_mobileappId](#BKMK_msdyn_mobileappId)
- [msdyn_orgName](#BKMK_msdyn_orgName)
- [msdyn_platformType](#BKMK_msdyn_platformType)
- [msdyn_primaryPublishedAppName](#BKMK_msdyn_primaryPublishedAppName)
- [msdyn_pushNotificationsEnabled_android](#BKMK_msdyn_pushNotificationsEnabled_android)
- [msdyn_pushNotificationsEnabled_ios](#BKMK_msdyn_pushNotificationsEnabled_ios)
- [msdyn_recentBuild](#BKMK_msdyn_recentBuild)
- [msdyn_secondaryApps](#BKMK_msdyn_secondaryApps)
- [msdyn_secondaryPublishedAppNames](#BKMK_msdyn_secondaryPublishedAppNames)
- [msdyn_statusBarContentColorMode](#BKMK_msdyn_statusBarContentColorMode)
- [msdyn_storageTypeForUpload](#BKMK_msdyn_storageTypeForUpload)
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

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_msdyn_actionButtonHighlight"></a> msdyn_actionButtonHighlight

|Property|Value|
|---|---|
|Description|**Color used for action button when highlighted.**|
|DisplayName|**Action Button Highlight**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_actionbuttonhighlight`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_adalClientId"></a> msdyn_adalClientId

|Property|Value|
|---|---|
|Description|**Active Directory Authentication Library Id used for Wrap.**|
|DisplayName|**Active Directory Authentication Library Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_adalclientid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_adalRedirectUri"></a> msdyn_adalRedirectUri

|Property|Value|
|---|---|
|Description|**Active Directory Authentication Library redirect URI used for Wrap.**|
|DisplayName|**Active Directory Authentication Library redirect URI**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_adalredirecturi`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_AndroidAppCenterAPIToken"></a> msdyn_AndroidAppCenterAPIToken

|Property|Value|
|---|---|
|Description|**Android App center API token**|
|DisplayName|**Android App center API token**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_androidappcenterapitoken`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_AndroidAppCenterAPITokenSaved"></a> msdyn_AndroidAppCenterAPITokenSaved

|Property|Value|
|---|---|
|Description|**Notify if the user have saved the Android token.**|
|DisplayName|**AndroidAppCenterAPITokenSaved**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_androidappcenterapitokensaved`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_appCenterAppIdAab"></a> msdyn_appCenterAppIdAab

|Property|Value|
|---|---|
|Description|**Android App Center AppId aab.**|
|DisplayName|**App Center AppId Aab**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appcenterappidaab`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_appCenterAppIdApk"></a> msdyn_appCenterAppIdApk

|Property|Value|
|---|---|
|Description|**Android App Center AppId.**|
|DisplayName|**App Center AppId Apk**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appcenterappidapk`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_appCenterAppIdIpa"></a> msdyn_appCenterAppIdIpa

|Property|Value|
|---|---|
|Description|**IOS App center app id for ipa.**|
|DisplayName|**IOS App Center Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appcenterappidipa`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_azureBlobStorageAccountName"></a> msdyn_azureBlobStorageAccountName

|Property|Value|
|---|---|
|Description|**Account Name of the Azure Blob Storage where the builds will be uploaded.**|
|DisplayName|**Azure Blob Storage Account Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_azureblobstorageaccountname`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_azureBlobStorageContainerName"></a> msdyn_azureBlobStorageContainerName

|Property|Value|
|---|---|
|Description|**Container Name of the Azure Blob Storage where the builds will be uploaded.**|
|DisplayName|**Azure Blob Storage Container Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_azureblobstoragecontainername`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_branch"></a> msdyn_branch

|Property|Value|
|---|---|
|Description|**Branch.**|
|DisplayName|**Branch**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_branch`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_buildDetails"></a> msdyn_buildDetails

|Property|Value|
|---|---|
|Description|**All Build details of the App.**|
|DisplayName|**Build Details**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_builddetails`|
|RequiredLevel|None|
|Type|Memo|
|Format|Email|
|FormatName|Email|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_msdyn_bundleIdentifier"></a> msdyn_bundleIdentifier

|Property|Value|
|---|---|
|Description|**The bundleIds resource represents the app's unique identifier that you can register, modify, and delete.**|
|DisplayName|**Bundle Identifier for App**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_bundleidentifier`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_buttonColor"></a> msdyn_buttonColor

|Property|Value|
|---|---|
|Description|**The Button color used in the App.**|
|DisplayName|**Button Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_buttoncolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_customDimensions"></a> msdyn_customDimensions

|Property|Value|
|---|---|
|Description|**Custom Dimensions.**|
|DisplayName|**Custom Dimensions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_customdimensions`|
|RequiredLevel|None|
|Type|Memo|
|Format|Email|
|FormatName|Email|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_msdyn_displayName"></a> msdyn_displayName

|Property|Value|
|---|---|
|Description|**Display name of the App.**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_displayname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_fillColor"></a> msdyn_fillColor

|Property|Value|
|---|---|
|Description|**Fill color of the App.**|
|DisplayName|**Fill Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_fillcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_headingTextColor"></a> msdyn_headingTextColor

|Property|Value|
|---|---|
|Description|**Heading Text Color in the App.**|
|DisplayName|**Heading Text Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_headingtextcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_hyperLinkColor"></a> msdyn_hyperLinkColor

|Property|Value|
|---|---|
|Description|**Hyper Link Color in the App.**|
|DisplayName|**Hyper Link Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_hyperlinkcolor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_IOSAppCenterAPIToken"></a> msdyn_IOSAppCenterAPIToken

|Property|Value|
|---|---|
|Description|**IOS App Center API token**|
|DisplayName|**IOS App Center API token**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_iosappcenterapitoken`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_IOSAppCenterAPITokenSaved"></a> msdyn_IOSAppCenterAPITokenSaved

|Property|Value|
|---|---|
|Description|**Notify if the user have saved the IOS token.**|
|DisplayName|**IOSAppCenterAPITokenSaved**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_iosappcenterapitokensaved`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_iosEnterpriseSigningEnabled"></a> msdyn_iosEnterpriseSigningEnabled

|Property|Value|
|---|---|
|Description|**iOS Enterprise Signing Enabled.**|
|DisplayName|**iOS Enterprise Signing Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_iosenterprisesigningenabled`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_isAppSigningEnabled"></a> msdyn_isAppSigningEnabled

|Property|Value|
|---|---|
|Description|**Is App Signing Enabled.**|
|DisplayName|**Is App Signing Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isappsigningenabled`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_keyVaultUri"></a> msdyn_keyVaultUri

|Property|Value|
|---|---|
|Description|**Key Vault Uri.**|
|DisplayName|**Key Vault Uri**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_keyvaulturi`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_mobileappId"></a> msdyn_mobileappId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Mobile App Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_mobileappid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_orgName"></a> msdyn_orgName

|Property|Value|
|---|---|
|Description|**Organization Name in App Center**|
|DisplayName|**Organization Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_orgname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_platformType"></a> msdyn_platformType

|Property|Value|
|---|---|
|Description|**Platform Type of Phone IOS/Android.**|
|DisplayName|**Platform Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_platformtype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_primaryPublishedAppName"></a> msdyn_primaryPublishedAppName

|Property|Value|
|---|---|
|Description|**Primary Published Canvas App to used in the Wrap.**|
|DisplayName|**Primary Published Canvas App**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_primarypublishedappname`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|canvasapp|

### <a name="BKMK_msdyn_pushNotificationsEnabled_android"></a> msdyn_pushNotificationsEnabled_android

|Property|Value|
|---|---|
|Description|**Push Notifications Enabled Android.**|
|DisplayName|**Push Notifications Enabled Android**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_pushnotificationsenabled_android`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_pushNotificationsEnabled_ios"></a> msdyn_pushNotificationsEnabled_ios

|Property|Value|
|---|---|
|Description|**Push Notifications Enabled iOS.**|
|DisplayName|**Push Notifications Enabled iOS**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_pushnotificationsenabled_ios`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_recentBuild"></a> msdyn_recentBuild

|Property|Value|
|---|---|
|Description|**Recent build details of the App.**|
|DisplayName|**Recent build**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_recentbuild`|
|RequiredLevel|None|
|Type|Memo|
|Format|Email|
|FormatName|Email|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_msdyn_secondaryApps"></a> msdyn_secondaryApps

|Property|Value|
|---|---|
|Description|**Secondary Apps used for Wrap.**|
|DisplayName|**Secondary Apps used for Wrap**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_secondaryapps`|
|RequiredLevel|None|
|Type|Memo|
|Format|Email|
|FormatName|Email|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_msdyn_secondaryPublishedAppNames"></a> msdyn_secondaryPublishedAppNames

|Property|Value|
|---|---|
|Description|**Secondary Published App Names to used in the Wrap.**|
|DisplayName|**Secondary Published App Names**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_secondarypublishedappnames`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_statusBarContentColorMode"></a> msdyn_statusBarContentColorMode

|Property|Value|
|---|---|
|Description|**Status Bar Content Color Mode of the App.**|
|DisplayName|**Status Bar Content Color Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_statusbarcontentcolormode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_storageTypeForUpload"></a> msdyn_storageTypeForUpload

|Property|Value|
|---|---|
|Description|**Storage type where the builds will be uploaded.**|
|DisplayName|**Storage Type For Upload**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_storagetypeforupload`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_UniqueName"></a> msdyn_UniqueName

|Property|Value|
|---|---|
|Description|**Unique Name for the entity.**|
|DisplayName|**Unique Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_uniquename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
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
|Description|**Owner Id**|
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
|Description|**Status of the MobileApp**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mobileapp_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the msdyn\_mobileapp**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mobileapp_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
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
- [msdyn_proDev_customPackage](#BKMK_msdyn_proDev_customPackage)
- [msdyn_proDev_customPackage_Name](#BKMK_msdyn_proDev_customPackage_Name)
- [msdyn_pushNotificationsAndroidJson](#BKMK_msdyn_pushNotificationsAndroidJson)
- [msdyn_pushNotificationsAndroidJson_Name](#BKMK_msdyn_pushNotificationsAndroidJson_Name)
- [msdyn_pushNotificationsIosPlist](#BKMK_msdyn_pushNotificationsIosPlist)
- [msdyn_pushNotificationsIosPlist_Name](#BKMK_msdyn_pushNotificationsIosPlist_Name)
- [msdyn_tenantSplashImage](#BKMK_msdyn_tenantSplashImage)
- [msdyn_tenantSplashImage_Name](#BKMK_msdyn_tenantSplashImage_Name)
- [msdyn_tenantWelcomeImage](#BKMK_msdyn_tenantWelcomeImage)
- [msdyn_tenantWelcomeImage_Name](#BKMK_msdyn_tenantWelcomeImage_Name)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
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
|DefaultFormValue||
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
|Description|**Date and time when the record was created.**|
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

### <a name="BKMK_msdyn_appIcon1024x1024"></a> msdyn_appIcon1024x1024

|Property|Value|
|---|---|
|Description|**App Icon with 1024 x 1024 dimension**|
|DisplayName|**IOS App Icon 1024x1024**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appicon1024x1024`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_appIcon1024x1024_Name"></a> msdyn_appIcon1024x1024_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_appicon1024x1024_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_appIcon120x120"></a> msdyn_appIcon120x120

|Property|Value|
|---|---|
|Description|**App Icon with 120 x 120 dimension**|
|DisplayName|**IOS App Icon 120x120**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appicon120x120`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_appIcon120x120_Name"></a> msdyn_appIcon120x120_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_appicon120x120_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_appIcon152x152"></a> msdyn_appIcon152x152

|Property|Value|
|---|---|
|Description|**App Icon with 152 x 152 dimension**|
|DisplayName|**IOS App Icon 152x152**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appicon152x152`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_appIcon152x152_Name"></a> msdyn_appIcon152x152_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_appicon152x152_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_appIcon167x167"></a> msdyn_appIcon167x167

|Property|Value|
|---|---|
|Description|**App Icon with 167 x 167 dimension**|
|DisplayName|**IOS App Icon 167x167**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appicon167x167`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_appIcon167x167_Name"></a> msdyn_appIcon167x167_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_appicon167x167_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_appIcon180x180"></a> msdyn_appIcon180x180

|Property|Value|
|---|---|
|Description|**App Icon with 180 x 180 dimension**|
|DisplayName|**IOS App Icon 180x180**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appicon180x180`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_appIcon180x180_Name"></a> msdyn_appIcon180x180_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_appicon180x180_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_appIconHdpi"></a> msdyn_appIconHdpi

|Property|Value|
|---|---|
|Description|**App Icon with 162 x 162 dimension**|
|DisplayName|**Android App Icon Hdpi**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appiconhdpi`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_appIconHdpi_Name"></a> msdyn_appIconHdpi_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_appiconhdpi_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_appIconMdpi"></a> msdyn_appIconMdpi

|Property|Value|
|---|---|
|Description|**App Icon with 108 x 108 dimension**|
|DisplayName|**Android App Icon Mdpi**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appiconmdpi`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_appIconMdpi_Name"></a> msdyn_appIconMdpi_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_appiconmdpi_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_appIconXdpi"></a> msdyn_appIconXdpi

|Property|Value|
|---|---|
|Description|**App Icon with 216 x 216 dimension**|
|DisplayName|**Android App Icon Xdpi**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appiconxdpi`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_appIconXdpi_Name"></a> msdyn_appIconXdpi_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_appiconxdpi_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_appIconXxhdpi"></a> msdyn_appIconXxhdpi

|Property|Value|
|---|---|
|Description|**App Icon with 324 x 324 dimension**|
|DisplayName|**Android App Icon XXdpi**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appiconxxhdpi`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_appIconXxhdpi_Name"></a> msdyn_appIconXxhdpi_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_appiconxxhdpi_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_appIconXxxhdpi"></a> msdyn_appIconXxxhdpi

|Property|Value|
|---|---|
|Description|**App Icon with 432 x 432 dimension**|
|DisplayName|**Android App Icon XXXdpi**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appiconxxxhdpi`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_appIconXxxhdpi_Name"></a> msdyn_appIconXxxhdpi_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_appiconxxxhdpi_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_launchAppResources"></a> msdyn_launchAppResources

|Property|Value|
|---|---|
|Description|**Launch App Resources used to package the App.**|
|DisplayName|**Launch App Resources**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_launchappresources`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_launchAppResources_Name"></a> msdyn_launchAppResources_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_launchappresources_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_mobileAppDefinitionAndroid"></a> msdyn_mobileAppDefinitionAndroid

|Property|Value|
|---|---|
|Description|**Mobile App Definition Android to package App.**|
|DisplayName|**Mobile App Definition Android**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_mobileappdefinitionandroid`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_mobileAppDefinitionAndroid_Name"></a> msdyn_mobileAppDefinitionAndroid_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_mobileappdefinitionandroid_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_mobileAppDefinitionIOS"></a> msdyn_mobileAppDefinitionIOS

|Property|Value|
|---|---|
|Description|**Mobile App Definition IOS to package App.**|
|DisplayName|**Mobile App Definition IOS**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_mobileappdefinitionios`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_mobileAppDefinitionIOS_Name"></a> msdyn_mobileAppDefinitionIOS_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_mobileappdefinitionios_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_proDev_customPackage"></a> msdyn_proDev_customPackage

|Property|Value|
|---|---|
|Description|**Pro Dev Custom Package.**|
|DisplayName|**Pro Dev Custom Package**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_prodev_custompackage`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_proDev_customPackage_Name"></a> msdyn_proDev_customPackage_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_prodev_custompackage_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_pushNotificationsAndroidJson"></a> msdyn_pushNotificationsAndroidJson

|Property|Value|
|---|---|
|Description|**Push Notifications Android JSON.**|
|DisplayName|**Push Notifications Android JSON**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_pushnotificationsandroidjson`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_pushNotificationsAndroidJson_Name"></a> msdyn_pushNotificationsAndroidJson_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_pushnotificationsandroidjson_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_pushNotificationsIosPlist"></a> msdyn_pushNotificationsIosPlist

|Property|Value|
|---|---|
|Description|**Push Notifications iOS Plist.**|
|DisplayName|**Push Notifications iOS Plist**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_pushnotificationsiosplist`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_pushNotificationsIosPlist_Name"></a> msdyn_pushNotificationsIosPlist_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_pushnotificationsiosplist_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_tenantSplashImage"></a> msdyn_tenantSplashImage

|Property|Value|
|---|---|
|Description|**Tenant Splash Image in the App.**|
|DisplayName|**Tenant Splash Image**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_tenantsplashimage`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_tenantSplashImage_Name"></a> msdyn_tenantSplashImage_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_tenantsplashimage_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_tenantWelcomeImage"></a> msdyn_tenantWelcomeImage

|Property|Value|
|---|---|
|Description|**Tenant Welcome Image in the App.**|
|DisplayName|**Tenant Welcome Image**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_tenantwelcomeimage`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_tenantWelcomeImage_Name"></a> msdyn_tenantWelcomeImage_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_tenantwelcomeimage_name`|
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
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

- [business_unit_msdyn_mobileapp](#BKMK_business_unit_msdyn_mobileapp)
- [canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName](#BKMK_canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName)
- [FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024)
- [FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120)
- [FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152)
- [FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167)
- [FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180)
- [FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi)
- [FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi)
- [FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi)
- [FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi)
- [FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi)
- [FileAttachment_msdyn_mobileapp_msdyn_launchAppResources](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_launchAppResources)
- [FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid)
- [FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS)
- [FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage)
- [FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson)
- [FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist)
- [FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage)
- [FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage)
- [lk_msdyn_mobileapp_createdby](#BKMK_lk_msdyn_mobileapp_createdby)
- [lk_msdyn_mobileapp_createdonbehalfby](#BKMK_lk_msdyn_mobileapp_createdonbehalfby)
- [lk_msdyn_mobileapp_modifiedby](#BKMK_lk_msdyn_mobileapp_modifiedby)
- [lk_msdyn_mobileapp_modifiedonbehalfby](#BKMK_lk_msdyn_mobileapp_modifiedonbehalfby)
- [owner_msdyn_mobileapp](#BKMK_owner_msdyn_mobileapp)
- [team_msdyn_mobileapp](#BKMK_team_msdyn_mobileapp)
- [user_msdyn_mobileapp](#BKMK_user_msdyn_mobileapp)

### <a name="BKMK_business_unit_msdyn_mobileapp"></a> business_unit_msdyn_mobileapp

One-To-Many Relationship: [businessunit business_unit_msdyn_mobileapp](businessunit.md#BKMK_business_unit_msdyn_mobileapp)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName"></a> canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName

One-To-Many Relationship: [canvasapp canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName](canvasapp.md#BKMK_canvasapp_msdyn_mobileapp_msdyn_primaryPublishedAppName)

|Property|Value|
|---|---|
|ReferencedEntity|`canvasapp`|
|ReferencedAttribute|`canvasappid`|
|ReferencingAttribute|`msdyn_primarypublishedappname`|
|ReferencingEntityNavigationPropertyName|`msdyn_primaryPublishedAppName`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024"></a> FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_appicon1024x1024`|
|ReferencingEntityNavigationPropertyName|`msdyn_appicon1024x1024`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120"></a> FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_appicon120x120`|
|ReferencingEntityNavigationPropertyName|`msdyn_appicon120x120`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152"></a> FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_appicon152x152`|
|ReferencingEntityNavigationPropertyName|`msdyn_appicon152x152`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167"></a> FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_appicon167x167`|
|ReferencingEntityNavigationPropertyName|`msdyn_appicon167x167`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180"></a> FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_appicon180x180`|
|ReferencingEntityNavigationPropertyName|`msdyn_appicon180x180`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi"></a> FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_appiconhdpi`|
|ReferencingEntityNavigationPropertyName|`msdyn_appiconhdpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi"></a> FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_appiconmdpi`|
|ReferencingEntityNavigationPropertyName|`msdyn_appiconmdpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi"></a> FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_appiconxdpi`|
|ReferencingEntityNavigationPropertyName|`msdyn_appiconxdpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi"></a> FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_appiconxxhdpi`|
|ReferencingEntityNavigationPropertyName|`msdyn_appiconxxhdpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi"></a> FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_appiconxxxhdpi`|
|ReferencingEntityNavigationPropertyName|`msdyn_appiconxxxhdpi`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_launchAppResources"></a> FileAttachment_msdyn_mobileapp_msdyn_launchAppResources

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_launchAppResources](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_launchAppResources)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_launchappresources`|
|ReferencingEntityNavigationPropertyName|`msdyn_launchappresources`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid"></a> FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_mobileappdefinitionandroid`|
|ReferencingEntityNavigationPropertyName|`msdyn_mobileappdefinitionandroid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS"></a> FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_mobileappdefinitionios`|
|ReferencingEntityNavigationPropertyName|`msdyn_mobileappdefinitionios`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage"></a> FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_prodev_custompackage`|
|ReferencingEntityNavigationPropertyName|`msdyn_prodev_custompackage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson"></a> FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_pushnotificationsandroidjson`|
|ReferencingEntityNavigationPropertyName|`msdyn_pushnotificationsandroidjson`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist"></a> FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_pushnotificationsiosplist`|
|ReferencingEntityNavigationPropertyName|`msdyn_pushnotificationsiosplist`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage"></a> FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_tenantsplashimage`|
|ReferencingEntityNavigationPropertyName|`msdyn_tenantsplashimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage"></a> FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage](fileattachment.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_tenantwelcomeimage`|
|ReferencingEntityNavigationPropertyName|`msdyn_tenantwelcomeimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_mobileapp_createdby"></a> lk_msdyn_mobileapp_createdby

One-To-Many Relationship: [systemuser lk_msdyn_mobileapp_createdby](systemuser.md#BKMK_lk_msdyn_mobileapp_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_mobileapp_createdonbehalfby"></a> lk_msdyn_mobileapp_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_mobileapp_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_mobileapp_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_mobileapp_modifiedby"></a> lk_msdyn_mobileapp_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_mobileapp_modifiedby](systemuser.md#BKMK_lk_msdyn_mobileapp_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_mobileapp_modifiedonbehalfby"></a> lk_msdyn_mobileapp_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_mobileapp_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_mobileapp_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_mobileapp"></a> owner_msdyn_mobileapp

One-To-Many Relationship: [owner owner_msdyn_mobileapp](owner.md#BKMK_owner_msdyn_mobileapp)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_mobileapp"></a> team_msdyn_mobileapp

One-To-Many Relationship: [team team_msdyn_mobileapp](team.md#BKMK_team_msdyn_mobileapp)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_mobileapp"></a> user_msdyn_mobileapp

One-To-Many Relationship: [systemuser user_msdyn_mobileapp](systemuser.md#BKMK_user_msdyn_mobileapp)

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

- [msdyn_mobileapp_AsyncOperations](#BKMK_msdyn_mobileapp_AsyncOperations)
- [msdyn_mobileapp_BulkDeleteFailures](#BKMK_msdyn_mobileapp_BulkDeleteFailures)
- [msdyn_mobileapp_DuplicateBaseRecord](#BKMK_msdyn_mobileapp_DuplicateBaseRecord)
- [msdyn_mobileapp_DuplicateMatchingRecord](#BKMK_msdyn_mobileapp_DuplicateMatchingRecord)
- [msdyn_mobileapp_FileAttachments](#BKMK_msdyn_mobileapp_FileAttachments)
- [msdyn_mobileapp_MailboxTrackingFolders](#BKMK_msdyn_mobileapp_MailboxTrackingFolders)
- [msdyn_mobileapp_PrincipalObjectAttributeAccesses](#BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses)
- [msdyn_mobileapp_ProcessSession](#BKMK_msdyn_mobileapp_ProcessSession)
- [msdyn_mobileapp_SyncErrors](#BKMK_msdyn_mobileapp_SyncErrors)

### <a name="BKMK_msdyn_mobileapp_AsyncOperations"></a> msdyn_mobileapp_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_mobileapp_AsyncOperations](asyncoperation.md#BKMK_msdyn_mobileapp_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_mobileapp_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_mobileapp_BulkDeleteFailures"></a> msdyn_mobileapp_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_mobileapp_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_mobileapp_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_mobileapp_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_mobileapp_DuplicateBaseRecord"></a> msdyn_mobileapp_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_mobileapp_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_mobileapp_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_mobileapp_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_mobileapp_DuplicateMatchingRecord"></a> msdyn_mobileapp_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_mobileapp_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_mobileapp_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_mobileapp_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_mobileapp_FileAttachments"></a> msdyn_mobileapp_FileAttachments

Many-To-One Relationship: [fileattachment msdyn_mobileapp_FileAttachments](fileattachment.md#BKMK_msdyn_mobileapp_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_mobileapp_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_mobileapp_MailboxTrackingFolders"></a> msdyn_mobileapp_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_mobileapp_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_mobileapp_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_mobileapp_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses"></a> msdyn_mobileapp_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_mobileapp_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_mobileapp_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_mobileapp_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_mobileapp_ProcessSession"></a> msdyn_mobileapp_ProcessSession

Many-To-One Relationship: [processsession msdyn_mobileapp_ProcessSession](processsession.md#BKMK_msdyn_mobileapp_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_mobileapp_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_mobileapp_SyncErrors"></a> msdyn_mobileapp_SyncErrors

Many-To-One Relationship: [syncerror msdyn_mobileapp_SyncErrors](syncerror.md#BKMK_msdyn_mobileapp_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_mobileapp_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_mobileapp?displayProperty=fullName>
