---
title: "credential table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the credential table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# credential table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the credential table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /credentials(*credentialid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /credentials<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /credentials(*credentialid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ListCredentialDependencies`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ListCredentialDependencies?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /credentials(*credentialid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /credentials<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /credentials(*credentialid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /credentials(*credentialid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /credentials(*credentialid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the credential table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Credential** |
| **DisplayCollectionName** | **Credentials** |
| **SchemaName** | `credential` |
| **CollectionSchemaName** | `credentials` |
| **EntitySetName** | `credentials`|
| **LogicalName** | `credential` |
| **LogicalCollectionName** | `credentials` |
| **PrimaryIdAttribute** | `credentialid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [certificate](#BKMK_certificate)
- [connectionreference](#BKMK_connectionreference)
- [connectiontype](#BKMK_connectiontype)
- [credentialId](#BKMK_credentialId)
- [credentials](#BKMK_credentials)
- [credentialtype](#BKMK_credentialtype)
- [cyberarkapplicationid](#BKMK_cyberarkapplicationid)
- [cyberarkobject](#BKMK_cyberarkobject)
- [cyberarksafe](#BKMK_cyberarksafe)
- [cyberarkusername](#BKMK_cyberarkusername)
- [defaultcredential](#BKMK_defaultcredential)
- [description](#BKMK_description)
- [groupmapping](#BKMK_groupmapping)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [logincontext](#BKMK_logincontext)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [password](#BKMK_password)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [usagetype](#BKMK_usagetype)
- [username](#BKMK_username)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_certificate"></a> certificate

|Property|Value|
|---|---|
|Description|**Certificate used for authentication**|
|DisplayName|**Certificate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`certificate`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|environmentvariabledefinition|

### <a name="BKMK_connectionreference"></a> connectionreference

|Property|Value|
|---|---|
|Description|**Reference to a connection containing credentials**|
|DisplayName|**Connection Reference**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectionreference`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|connectionreference|

### <a name="BKMK_connectiontype"></a> connectiontype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Connection Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectiontype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`credential_connectiontype`|

#### connectiontype Choices/Options

|Value|Label|
|---|---|
|1|**UsernamePassword**|
|2|**UsernamePasswordList**|
|3|**UsernamePasswordListWithGroupMapping**|
|4|**CyberArkIdentity**|
|5|**CertificateBasedAuthentication**|
|6|**MachineMapping**|
|7|**ConnectionReference**|

### <a name="BKMK_credentialId"></a> credentialId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Credential**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`credentialid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_credentials"></a> credentials

|Property|Value|
|---|---|
|Description||
|DisplayName|**Credentials**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`credentials`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_credentialtype"></a> credentialtype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Credential Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`credentialtype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`credential_credentialtype`|

#### credentialtype Choices/Options

|Value|Label|
|---|---|
|1|**SingleCredential**|
|2|**ListOfCredentials**|

### <a name="BKMK_cyberarkapplicationid"></a> cyberarkapplicationid

|Property|Value|
|---|---|
|Description||
|DisplayName|**CyberArk Application Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cyberarkapplicationid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_cyberarkobject"></a> cyberarkobject

|Property|Value|
|---|---|
|Description||
|DisplayName|**CyberArk Object**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cyberarkobject`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|environmentvariabledefinition|

### <a name="BKMK_cyberarksafe"></a> cyberarksafe

|Property|Value|
|---|---|
|Description|**Metadata of the CyberArk safe where the password is stored: Hostname or IP address of the CCP endpoint, Folder and Name of the CyberArk safe where the password is stored**|
|DisplayName|**CyberArk Safe**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cyberarksafe`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|environmentvariabledefinition|

### <a name="BKMK_cyberarkusername"></a> cyberarkusername

|Property|Value|
|---|---|
|Description||
|DisplayName|**CyberArk Username**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cyberarkusername`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|environmentvariabledefinition|

### <a name="BKMK_defaultcredential"></a> defaultcredential

|Property|Value|
|---|---|
|Description|**This credential will be used if there is no matching mapping.**|
|DisplayName|**Default credential for mappings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`defaultcredential`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|credential|

### <a name="BKMK_description"></a> description

|Property|Value|
|---|---|
|Description|**The description of the credential.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_groupmapping"></a> groupmapping

|Property|Value|
|---|---|
|Description||
|DisplayName|**Group Mapping**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`groupmapping`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

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

### <a name="BKMK_logincontext"></a> logincontext

|Property|Value|
|---|---|
|Description|**The login context in which the credential should be used.**|
|DisplayName|**Login context**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logincontext`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

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

### <a name="BKMK_password"></a> password

|Property|Value|
|---|---|
|Description||
|DisplayName|**Password**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`password`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|environmentvariabledefinition|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Credential**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`credential_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Credential**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`credential_statuscode`|

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

### <a name="BKMK_usagetype"></a> usagetype

|Property|Value|
|---|---|
|Description|**Types of allowed usage for the credential.**|
|DisplayName|**Usage Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`usagetype`|
|RequiredLevel|ApplicationRequired|
|Type|MultiSelectPicklist|
|DefaultFormValue|280920000|
|GlobalChoiceName|`credential_usagetype`|

#### usagetype Choices/Options

|Value|Label|
|---|---|
|280920000|**Connection**|
|280920001|**DesktopScript**|
|280920002|**Network**|
|280920003|**Cua**|

### <a name="BKMK_username"></a> username

|Property|Value|
|---|---|
|Description||
|DisplayName|**Username**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`username`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|environmentvariabledefinition|

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

- [business_unit_credential](#BKMK_business_unit_credential)
- [credential_connectionreference](#BKMK_credential_connectionreference)
- [credential_credential_defaultcredential](#BKMK_credential_credential_defaultcredential-many-to-one)
- [environmentvariabledefinition_credential_certificate](#BKMK_environmentvariabledefinition_credential_certificate)
- [environmentvariabledefinition_credential_cyberarkobject](#BKMK_environmentvariabledefinition_credential_cyberarkobject)
- [environmentvariabledefinition_credential_cyberarksafe](#BKMK_environmentvariabledefinition_credential_cyberarksafe)
- [environmentvariabledefinition_credential_cyberarkusername](#BKMK_environmentvariabledefinition_credential_cyberarkusername)
- [environmentvariabledefinition_credential_password](#BKMK_environmentvariabledefinition_credential_password)
- [environmentvariabledefinition_credential_username](#BKMK_environmentvariabledefinition_credential_username)
- [lk_credential_createdby](#BKMK_lk_credential_createdby)
- [lk_credential_createdonbehalfby](#BKMK_lk_credential_createdonbehalfby)
- [lk_credential_modifiedby](#BKMK_lk_credential_modifiedby)
- [lk_credential_modifiedonbehalfby](#BKMK_lk_credential_modifiedonbehalfby)
- [owner_credential](#BKMK_owner_credential)
- [team_credential](#BKMK_team_credential)
- [user_credential](#BKMK_user_credential)

### <a name="BKMK_business_unit_credential"></a> business_unit_credential

One-To-Many Relationship: [businessunit business_unit_credential](businessunit.md#BKMK_business_unit_credential)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_credential_connectionreference"></a> credential_connectionreference

One-To-Many Relationship: [connectionreference credential_connectionreference](connectionreference.md#BKMK_credential_connectionreference)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionreference`|
|ReferencedAttribute|`connectionreferenceid`|
|ReferencingAttribute|`connectionreference`|
|ReferencingEntityNavigationPropertyName|`connectionreference`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_credential_credential_defaultcredential-many-to-one"></a> credential_credential_defaultcredential

One-To-Many Relationship: [credential credential_credential_defaultcredential](#BKMK_credential_credential_defaultcredential-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`credential`|
|ReferencedAttribute|`credentialid`|
|ReferencingAttribute|`defaultcredential`|
|ReferencingEntityNavigationPropertyName|`defaultcredential`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_credential_certificate"></a> environmentvariabledefinition_credential_certificate

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_credential_certificate](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_credential_certificate)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`certificate`|
|ReferencingEntityNavigationPropertyName|`certificate`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_credential_cyberarkobject"></a> environmentvariabledefinition_credential_cyberarkobject

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_credential_cyberarkobject](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_credential_cyberarkobject)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`cyberarkobject`|
|ReferencingEntityNavigationPropertyName|`cyberarkobject`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_credential_cyberarksafe"></a> environmentvariabledefinition_credential_cyberarksafe

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_credential_cyberarksafe](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_credential_cyberarksafe)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`cyberarksafe`|
|ReferencingEntityNavigationPropertyName|`cyberarksafe`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_credential_cyberarkusername"></a> environmentvariabledefinition_credential_cyberarkusername

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_credential_cyberarkusername](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_credential_cyberarkusername)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`cyberarkusername`|
|ReferencingEntityNavigationPropertyName|`cyberarkusername`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_credential_password"></a> environmentvariabledefinition_credential_password

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_credential_password](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_credential_password)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`password`|
|ReferencingEntityNavigationPropertyName|`password`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_environmentvariabledefinition_credential_username"></a> environmentvariabledefinition_credential_username

One-To-Many Relationship: [environmentvariabledefinition environmentvariabledefinition_credential_username](environmentvariabledefinition.md#BKMK_environmentvariabledefinition_credential_username)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`username`|
|ReferencingEntityNavigationPropertyName|`username`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_credential_createdby"></a> lk_credential_createdby

One-To-Many Relationship: [systemuser lk_credential_createdby](systemuser.md#BKMK_lk_credential_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_credential_createdonbehalfby"></a> lk_credential_createdonbehalfby

One-To-Many Relationship: [systemuser lk_credential_createdonbehalfby](systemuser.md#BKMK_lk_credential_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_credential_modifiedby"></a> lk_credential_modifiedby

One-To-Many Relationship: [systemuser lk_credential_modifiedby](systemuser.md#BKMK_lk_credential_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_credential_modifiedonbehalfby"></a> lk_credential_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_credential_modifiedonbehalfby](systemuser.md#BKMK_lk_credential_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_credential"></a> owner_credential

One-To-Many Relationship: [owner owner_credential](owner.md#BKMK_owner_credential)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_credential"></a> team_credential

One-To-Many Relationship: [team team_credential](team.md#BKMK_team_credential)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_credential"></a> user_credential

One-To-Many Relationship: [systemuser user_credential](systemuser.md#BKMK_user_credential)

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

- [connectioninstance_CredentialId_credential](#BKMK_connectioninstance_CredentialId_credential)
- [credential_AsyncOperations](#BKMK_credential_AsyncOperations)
- [credential_BulkDeleteFailures](#BKMK_credential_BulkDeleteFailures)
- [credential_credential_defaultcredential](#BKMK_credential_credential_defaultcredential-one-to-many)
- [credential_DuplicateBaseRecord](#BKMK_credential_DuplicateBaseRecord)
- [credential_DuplicateMatchingRecord](#BKMK_credential_DuplicateMatchingRecord)
- [credential_flowmachinenetwork](#BKMK_credential_flowmachinenetwork)
- [credential_MailboxTrackingFolders](#BKMK_credential_MailboxTrackingFolders)
- [credential_PrincipalObjectAttributeAccesses](#BKMK_credential_PrincipalObjectAttributeAccesses)
- [credential_ProcessSession](#BKMK_credential_ProcessSession)
- [credential_SyncErrors](#BKMK_credential_SyncErrors)

### <a name="BKMK_connectioninstance_CredentialId_credential"></a> connectioninstance_CredentialId_credential

Many-To-One Relationship: [connectioninstance connectioninstance_CredentialId_credential](connectioninstance.md#BKMK_connectioninstance_CredentialId_credential)

|Property|Value|
|---|---|
|ReferencingEntity|`connectioninstance`|
|ReferencingAttribute|`credentialid`|
|ReferencedEntityNavigationPropertyName|`connectioninstance_CredentialId_credential`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_credential_AsyncOperations"></a> credential_AsyncOperations

Many-To-One Relationship: [asyncoperation credential_AsyncOperations](asyncoperation.md#BKMK_credential_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`credential_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_credential_BulkDeleteFailures"></a> credential_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure credential_BulkDeleteFailures](bulkdeletefailure.md#BKMK_credential_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`credential_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_credential_credential_defaultcredential-one-to-many"></a> credential_credential_defaultcredential

Many-To-One Relationship: [credential credential_credential_defaultcredential](#BKMK_credential_credential_defaultcredential-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`credential`|
|ReferencingAttribute|`defaultcredential`|
|ReferencedEntityNavigationPropertyName|`credential_credential_defaultcredential`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: Default credential for a mapping<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_credential_DuplicateBaseRecord"></a> credential_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord credential_DuplicateBaseRecord](duplicaterecord.md#BKMK_credential_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`credential_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_credential_DuplicateMatchingRecord"></a> credential_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord credential_DuplicateMatchingRecord](duplicaterecord.md#BKMK_credential_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`credential_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_credential_flowmachinenetwork"></a> credential_flowmachinenetwork

Many-To-One Relationship: [flowmachinenetwork credential_flowmachinenetwork](flowmachinenetwork.md#BKMK_credential_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachinenetwork`|
|ReferencingAttribute|`credentialid`|
|ReferencedEntityNavigationPropertyName|`flowmachinenetwork_credentialId_credential`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_credential_MailboxTrackingFolders"></a> credential_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder credential_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_credential_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`credential_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_credential_PrincipalObjectAttributeAccesses"></a> credential_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess credential_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_credential_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`credential_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_credential_ProcessSession"></a> credential_ProcessSession

Many-To-One Relationship: [processsession credential_ProcessSession](processsession.md#BKMK_credential_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`credential_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_credential_SyncErrors"></a> credential_SyncErrors

Many-To-One Relationship: [syncerror credential_SyncErrors](syncerror.md#BKMK_credential_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`credential_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.credential?displayProperty=fullName>
