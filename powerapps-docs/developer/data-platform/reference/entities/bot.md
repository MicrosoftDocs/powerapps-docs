---
title: "Copilot (bot) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Copilot (bot) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Copilot (bot) table/entity reference (Microsoft Dataverse)

Represents a copilot created in Copilot Studio. https://copilotstudio.microsoft.com/

## Messages

The following table lists the messages for the Copilot (bot) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /bots(*botid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /bots<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /bots(*botid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `PvaAuthorize`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PvaAuthorize?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PvaCreateBotComponents`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PvaCreateBotComponents?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PvaCreateContentSnapshot`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PvaCreateContentSnapshot?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PvaDeleteBot`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PvaDeleteBot?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PvaGetDirectLineEndpoint`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PvaGetDirectLineEndpoint?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PvaProvision`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PvaProvision?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PvaPublish`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PvaPublish?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PvaPublishStatus`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PvaPublishStatus?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: False |`GET` /bots(*botid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /bots<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /bots(*botid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /bots(*botid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /bots(*botid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Copilot (bot) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Copilot** |
| **DisplayCollectionName** | **Copilots** |
| **SchemaName** | `bot` |
| **CollectionSchemaName** | `bots` |
| **EntitySetName** | `bots`|
| **LogicalName** | `bot` |
| **LogicalCollectionName** | `bots` |
| **PrimaryIdAttribute** | `botid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [accesscontrolpolicy](#BKMK_accesscontrolpolicy)
- [applicationmanifestinformation](#BKMK_applicationmanifestinformation)
- [authenticationconfiguration](#BKMK_authenticationconfiguration)
- [authenticationmode](#BKMK_authenticationmode)
- [authenticationtrigger](#BKMK_authenticationtrigger)
- [authorizedsecuritygroupids](#BKMK_authorizedsecuritygroupids)
- [botId](#BKMK_botId)
- [Configuration](#BKMK_Configuration)
- [iconbase64](#BKMK_iconbase64)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [Language](#BKMK_Language)
- [name](#BKMK_name)
- [Origin](#BKMK_Origin)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ProviderConnectionReferenceId](#BKMK_ProviderConnectionReferenceId)
- [publishedby](#BKMK_publishedby)
- [publishedon](#BKMK_publishedon)
- [RuntimeProvider](#BKMK_RuntimeProvider)
- [SchemaName](#BKMK_SchemaName)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [SupportedLanguages](#BKMK_SupportedLanguages)
- [SynchronizationStatus](#BKMK_SynchronizationStatus)
- [Template](#BKMK_Template)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_accesscontrolpolicy"></a> accesscontrolpolicy

|Property|Value|
|---|---|
|Description|**Defines which users may interact with the bot.**|
|DisplayName|**Access Control Policy**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`accesscontrolpolicy`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`bot_accesscontrolpolicy`|

#### accesscontrolpolicy Choices/Options

|Value|Label|
|---|---|
|0|**Any**|
|1|**Copilot readers**|
|2|**Group membership**|
|3|**Any (multi-tenant)**|

### <a name="BKMK_applicationmanifestinformation"></a> applicationmanifestinformation

|Property|Value|
|---|---|
|Description|**Stores information with application manifest data such as Teams application information.**|
|DisplayName|**Application Manifest Information**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicationmanifestinformation`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_authenticationconfiguration"></a> authenticationconfiguration

|Property|Value|
|---|---|
|Description|**Stores information for the authentication configuration.**|
|DisplayName|**Authentication Configuration Information**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`authenticationconfiguration`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_authenticationmode"></a> authenticationmode

|Property|Value|
|---|---|
|Description|**Defines how the bot should be authenticated to the user.**|
|DisplayName|**Authentication Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`authenticationmode`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`bot_authenticationmode`|

#### authenticationmode Choices/Options

|Value|Label|
|---|---|
|0|**Unspecified**|
|1|**None**|
|2|**Integrated**|
|3|**Custom Azure Active Directory**|
|4|**Generic OAuth2**|

### <a name="BKMK_authenticationtrigger"></a> authenticationtrigger

|Property|Value|
|---|---|
|Description|**Defines at which point authentication for the bot should be triggered. Security can be enforced at the bot entry point, removing the need for explicit authentication nodes in the dialog flow.**|
|DisplayName|**Authentication trigger**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`authenticationtrigger`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`bot_authenticationtrigger`|

#### authenticationtrigger Choices/Options

|Value|Label|
|---|---|
|0|**As Needed**|
|1|**Always**|

### <a name="BKMK_authorizedsecuritygroupids"></a> authorizedsecuritygroupids

|Property|Value|
|---|---|
|Description|**Contains a comma-delimited list of up to 20 Azure Active Directory Group IDs that are allowed to interact with the bot. This field is ignored if Access Control Policy is not set to Group membership.**|
|DisplayName|**Authorized Security Groups**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`authorizedsecuritygroupids`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|739|

### <a name="BKMK_botId"></a> botId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Copilot.**|
|DisplayName|**Bot**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`botid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Configuration"></a> Configuration

|Property|Value|
|---|---|
|Description|**Used to store content of bot configuration data.**|
|DisplayName|**Configuration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`configuration`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_iconbase64"></a> iconbase64

|Property|Value|
|---|---|
|Description|**Used to visually identify your bot in channels and services. Represented in a base64 encoded string. Must be in PNG format, and no larger than 30K in size. This value can be changed at any time.**|
|DisplayName|**Icon (Base64)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iconbase64`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|51200|

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

### <a name="BKMK_Language"></a> Language

|Property|Value|
|---|---|
|Description|**The language identifier (LCID) of this Copilot.**|
|DisplayName|**Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`language`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|1033|
|GlobalChoiceName|`bot_language`|

#### Language Choices/Options

|Value|Label|
|---|---|
|1025|**Arabic**|
|1028|**Chinese (Traditional)**|
|1029|**Czech**|
|1030|**Danish**|
|1031|**German**|
|1032|**Greek**|
|1033|**English**|
|1034|**Spanish**|
|1035|**Finnish**|
|1036|**French**|
|1037|**Hebrew**|
|1040|**Italian**|
|1041|**Japanese**|
|1042|**Korean**|
|1043|**Dutch**|
|1044|**Norwegian**|
|1045|**Polish**|
|1046|**Portuguese (Brazilian)**|
|1049|**Russian**|
|1053|**Swedish**|
|1054|**Thai**|
|1055|**Turkish**|
|1057|**Indonesian**|
|1081|**Hindi**|
|2052|**Chinese (Simplified)**|
|2057|**English (United Kingdom)**|
|2070|**Portuguese (Portugal)**|
|3081|**English (Australia)**|
|3084|**French (Canada)**|
|21514|**Spanish (United States)**|

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The display name of the Copilot.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Origin"></a> Origin

|Property|Value|
|---|---|
|Description|**Used to identify the origin used to create the bot.**|
|DisplayName|**Origin**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`origin`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

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

### <a name="BKMK_ProviderConnectionReferenceId"></a> ProviderConnectionReferenceId

|Property|Value|
|---|---|
|Description|**Unique identifier for Connection Reference associated with Copilot.**|
|DisplayName|**Provider connection reference**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`providerconnectionreferenceid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|connectionreference|

### <a name="BKMK_publishedby"></a> publishedby

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last published the bot.**|
|DisplayName|**Published By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`publishedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_publishedon"></a> publishedon

|Property|Value|
|---|---|
|Description|**Date and time when the Copilot was last published**|
|DisplayName|**Published On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`publishedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_RuntimeProvider"></a> RuntimeProvider

|Property|Value|
|---|---|
|Description||
|DisplayName|**Runtime provider**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`runtimeprovider`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`bot_runtimeprovider`|

#### RuntimeProvider Choices/Options

|Value|Label|
|---|---|
|0|**Power Virtual Agents**|
|1|**Nuance Mix Shell**|

### <a name="BKMK_SchemaName"></a> SchemaName

|Property|Value|
|---|---|
|Description|**Unique name identifying the Copilot.**|
|DisplayName|**SchemaName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`schemaname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Copilot**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`bot_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Copilot**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`bot_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Provisioned**<br />State:0<br />TransitionData:<br />`<allowedtransitions xmlns="http://schemas.microsoft.com/crm/2009/WebServices"><allowedtransition sourcestatusid="1" tostatusid="5" /></allowedtransitions>`|
|2|Label: **Deprovisioned**<br />State:1<br />TransitionData:<br />`<allowedtransitions xmlns="http://schemas.microsoft.com/crm/2009/WebServices"><allowedtransition sourcestatusid="2" tostatusid="3" /></allowedtransitions>`|
|3|Label: **Provisioning**<br />State:1<br />TransitionData:<br />`<allowedtransitions xmlns="http://schemas.microsoft.com/crm/2009/WebServices"><allowedtransition sourcestatusid="3" tostatusid="1" /><allowedtransition sourcestatusid="3" tostatusid="4" /><allowedtransition sourcestatusid="3" tostatusid="5" /></allowedtransitions>`|
|4|Label: **ProvisionFailed**<br />State:1<br />TransitionData:<br />`<allowedtransitions xmlns="http://schemas.microsoft.com/crm/2009/WebServices"><allowedtransition sourcestatusid="4" tostatusid="3" /></allowedtransitions>`|
|5|Label: **MissingLicense**<br />State:1<br />TransitionData:<br />`<allowedtransitions xmlns="http://schemas.microsoft.com/crm/2009/WebServices"><allowedtransition sourcestatusid="5" tostatusid="1" /><allowedtransition sourcestatusid="5" tostatusid="3" /></allowedtransitions>`|

### <a name="BKMK_SupportedLanguages"></a> SupportedLanguages

|Property|Value|
|---|---|
|Description|**The list of supported languages by this bot**|
|DisplayName|**Supported languages**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`supportedlanguages`|
|RequiredLevel|None|
|Type|MultiSelectPicklist|
|DefaultFormValue||
|GlobalChoiceName|`chatbotlanguage`|

#### SupportedLanguages Choices/Options

|Value|Label|
|---|---|
|1025|**Arabic**|
|1028|**Chinese (Traditional)**|
|1029|**Czech**|
|1030|**Danish**|
|1031|**German**|
|1032|**Greek**|
|1033|**English**|
|1034|**Spanish**|
|1035|**Finnish**|
|1036|**French**|
|1037|**Hebrew**|
|1040|**Italian**|
|1041|**Japanese**|
|1042|**Korean**|
|1043|**Dutch**|
|1044|**Norwegian**|
|1045|**Polish**|
|1046|**Portuguese (Brazilian)**|
|1049|**Russian**|
|1053|**Swedish**|
|1054|**Thai**|
|1055|**Turkish**|
|1057|**Indonesian**|
|1081|**Hindi**|
|2052|**Chinese (Simplified)**|
|2057|**English (United Kingdom)**|
|2070|**Portuguese (Portugal)**|
|3081|**English (Australia)**|
|3084|**French (Canada)**|
|21514|**Spanish (United States)**|

### <a name="BKMK_SynchronizationStatus"></a> SynchronizationStatus

|Property|Value|
|---|---|
|Description|**Used to store information about the synchronization operations of the bot**|
|DisplayName|**SynchronizationStatus**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`synchronizationstatus`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_Template"></a> Template

|Property|Value|
|---|---|
|Description|**Used to identify the template and version used for the bot default content**|
|DisplayName|**Template**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`template`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

- [bot_connectionreference](#BKMK_bot_connectionreference)
- [business_unit_bot](#BKMK_business_unit_bot)
- [lk_bot_createdby](#BKMK_lk_bot_createdby)
- [lk_bot_createdonbehalfby](#BKMK_lk_bot_createdonbehalfby)
- [lk_bot_modifiedby](#BKMK_lk_bot_modifiedby)
- [lk_bot_modifiedonbehalfby](#BKMK_lk_bot_modifiedonbehalfby)
- [owner_bot](#BKMK_owner_bot)
- [systemuser_bot_publishedby](#BKMK_systemuser_bot_publishedby)
- [team_bot](#BKMK_team_bot)
- [user_bot](#BKMK_user_bot)

### <a name="BKMK_bot_connectionreference"></a> bot_connectionreference

One-To-Many Relationship: [connectionreference bot_connectionreference](connectionreference.md#BKMK_bot_connectionreference)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionreference`|
|ReferencedAttribute|`connectionreferenceid`|
|ReferencingAttribute|`providerconnectionreferenceid`|
|ReferencingEntityNavigationPropertyName|`ProviderConnectionReferenceId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_business_unit_bot"></a> business_unit_bot

One-To-Many Relationship: [businessunit business_unit_bot](businessunit.md#BKMK_business_unit_bot)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_bot_createdby"></a> lk_bot_createdby

One-To-Many Relationship: [systemuser lk_bot_createdby](systemuser.md#BKMK_lk_bot_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_bot_createdonbehalfby"></a> lk_bot_createdonbehalfby

One-To-Many Relationship: [systemuser lk_bot_createdonbehalfby](systemuser.md#BKMK_lk_bot_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_bot_modifiedby"></a> lk_bot_modifiedby

One-To-Many Relationship: [systemuser lk_bot_modifiedby](systemuser.md#BKMK_lk_bot_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_bot_modifiedonbehalfby"></a> lk_bot_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_bot_modifiedonbehalfby](systemuser.md#BKMK_lk_bot_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_bot"></a> owner_bot

One-To-Many Relationship: [owner owner_bot](owner.md#BKMK_owner_bot)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_systemuser_bot_publishedby"></a> systemuser_bot_publishedby

One-To-Many Relationship: [systemuser systemuser_bot_publishedby](systemuser.md#BKMK_systemuser_bot_publishedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`publishedby`|
|ReferencingEntityNavigationPropertyName|`publishedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_bot"></a> team_bot

One-To-Many Relationship: [team team_bot](team.md#BKMK_team_bot)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_bot"></a> user_bot

One-To-Many Relationship: [systemuser user_bot](systemuser.md#BKMK_user_bot)

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

- [bot_AsyncOperations](#BKMK_bot_AsyncOperations)
- [bot_BulkDeleteFailures](#BKMK_bot_BulkDeleteFailures)
- [bot_conversationtranscript](#BKMK_bot_conversationtranscript)
- [bot_MailboxTrackingFolders](#BKMK_bot_MailboxTrackingFolders)
- [bot_PrincipalObjectAttributeAccesses](#BKMK_bot_PrincipalObjectAttributeAccesses)
- [bot_ProcessSession](#BKMK_bot_ProcessSession)
- [bot_SyncErrors](#BKMK_bot_SyncErrors)
- [botcomponent_parent_bot](#BKMK_botcomponent_parent_bot)

### <a name="BKMK_bot_AsyncOperations"></a> bot_AsyncOperations

Many-To-One Relationship: [asyncoperation bot_AsyncOperations](asyncoperation.md#BKMK_bot_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`bot_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_bot_BulkDeleteFailures"></a> bot_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure bot_BulkDeleteFailures](bulkdeletefailure.md#BKMK_bot_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`bot_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_bot_conversationtranscript"></a> bot_conversationtranscript

Many-To-One Relationship: [conversationtranscript bot_conversationtranscript](conversationtranscript.md#BKMK_bot_conversationtranscript)

|Property|Value|
|---|---|
|ReferencingEntity|`conversationtranscript`|
|ReferencingAttribute|`bot_conversationtranscriptid`|
|ReferencedEntityNavigationPropertyName|`bot_conversationtranscript`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_bot_MailboxTrackingFolders"></a> bot_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder bot_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_bot_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`bot_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_bot_PrincipalObjectAttributeAccesses"></a> bot_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess bot_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_bot_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`bot_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_bot_ProcessSession"></a> bot_ProcessSession

Many-To-One Relationship: [processsession bot_ProcessSession](processsession.md#BKMK_bot_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`bot_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_bot_SyncErrors"></a> bot_SyncErrors

Many-To-One Relationship: [syncerror bot_SyncErrors](syncerror.md#BKMK_bot_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`bot_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_parent_bot"></a> botcomponent_parent_bot

Many-To-One Relationship: [botcomponent botcomponent_parent_bot](botcomponent.md#BKMK_botcomponent_parent_bot)

|Property|Value|
|---|---|
|ReferencingEntity|`botcomponent`|
|ReferencingAttribute|`parentbotid`|
|ReferencedEntityNavigationPropertyName|`botcomponent_parent_bot`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [bot_botcomponent](#BKMK_bot_botcomponent)
- [bot_botcomponentcollection](#BKMK_bot_botcomponentcollection)
- [bot_environmentvariabledefinition](#BKMK_bot_environmentvariabledefinition)

### <a name="BKMK_bot_botcomponent"></a> bot_botcomponent

See [botcomponent bot_botcomponent Many-To-Many Relationship](botcomponent.md#BKMK_bot_botcomponent)

|Property|Value|
|---|---|
|IntersectEntityName|`bot_botcomponent`|
|IsCustomizable|False|
|SchemaName|`bot_botcomponent`|
|IntersectAttribute|`botid`|
|NavigationPropertyName|`bot_botcomponent`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_bot_botcomponentcollection"></a> bot_botcomponentcollection

See [botcomponentcollection bot_botcomponentcollection Many-To-Many Relationship](botcomponentcollection.md#BKMK_bot_botcomponentcollection)

|Property|Value|
|---|---|
|IntersectEntityName|`bot_botcomponentcollection`|
|IsCustomizable|False|
|SchemaName|`bot_botcomponentcollection`|
|IntersectAttribute|`botid`|
|NavigationPropertyName|`bot_botcomponentcollection`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_bot_environmentvariabledefinition"></a> bot_environmentvariabledefinition

See [environmentvariabledefinition bot_environmentvariabledefinition Many-To-Many Relationship](environmentvariabledefinition.md#BKMK_bot_environmentvariabledefinition)

|Property|Value|
|---|---|
|IntersectEntityName|`bot_environmentvariabledefinition`|
|IsCustomizable|False|
|SchemaName|`bot_environmentvariabledefinition`|
|IntersectAttribute|`botid`|
|NavigationPropertyName|`bot_environmentvariabledefinition`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.bot?displayProperty=fullName>
