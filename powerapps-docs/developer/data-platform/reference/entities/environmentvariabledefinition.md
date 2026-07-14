---
title: "Environment Variable Definition (EnvironmentVariableDefinition) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Environment Variable Definition (EnvironmentVariableDefinition) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Environment Variable Definition (EnvironmentVariableDefinition) table/entity reference (Microsoft Dataverse)

Contains information about the settable variable: its type, default value, and etc.

## Messages

The following table lists the messages for the Environment Variable Definition (EnvironmentVariableDefinition) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /environmentvariabledefinitions(*environmentvariabledefinitionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /environmentvariabledefinitions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /environmentvariabledefinitions(*environmentvariabledefinitionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /environmentvariabledefinitions(*environmentvariabledefinitionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveAllCompositeDataSources`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveAllCompositeDataSources?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RetrieveCompositeDataSource`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveCompositeDataSource?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RetrieveEnvironmentVariables`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveEnvironmentVariables?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RetrieveEnvironmentVariableValue`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveEnvironmentVariableValue?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RetrieveMultiple`<br />Event: False |`GET` /environmentvariabledefinitions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /environmentvariabledefinitions(*environmentvariabledefinitionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /environmentvariabledefinitions(*environmentvariabledefinitionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /environmentvariabledefinitions(*environmentvariabledefinitionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Environment Variable Definition (EnvironmentVariableDefinition) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Environment Variable Definition** |
| **DisplayCollectionName** | **Environment Variable Definitions** |
| **SchemaName** | `EnvironmentVariableDefinition` |
| **CollectionSchemaName** | `EnvironmentVariableDefinitions` |
| **EntitySetName** | `environmentvariabledefinitions`|
| **LogicalName** | `environmentvariabledefinition` |
| **LogicalCollectionName** | `environmentvariabledefinitions` |
| **PrimaryIdAttribute** | `environmentvariabledefinitionid` |
| **PrimaryNameAttribute** |`schemaname` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ApiId](#BKMK_ApiId)
- [ConnectionReferenceId](#BKMK_ConnectionReferenceId)
- [DefaultValue](#BKMK_DefaultValue)
- [Description](#BKMK_Description)
- [DisplayName](#BKMK_DisplayName)
- [EnvironmentVariableDefinitionId](#BKMK_EnvironmentVariableDefinitionId)
- [Hint](#BKMK_Hint)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [InputControlConfig](#BKMK_InputControlConfig)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsRequired](#BKMK_IsRequired)
- [LearnMoreUrl](#BKMK_LearnMoreUrl)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParameterKey](#BKMK_ParameterKey)
- [ParentDefinitionId](#BKMK_ParentDefinitionId)
- [SchemaName](#BKMK_SchemaName)
- [SecretStore](#BKMK_SecretStore)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Type](#BKMK_Type)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [ValueSchema](#BKMK_ValueSchema)

### <a name="BKMK_ApiId"></a> ApiId

|Property|Value|
|---|---|
|Description||
|DisplayName|**API Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`apiid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|150|

### <a name="BKMK_ConnectionReferenceId"></a> ConnectionReferenceId

|Property|Value|
|---|---|
|Description|**Unique identifier for Connection Reference associated with Environment Variable Definition.**|
|DisplayName|**Connection Reference**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectionreferenceid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_DefaultValue"></a> DefaultValue

|Property|Value|
|---|---|
|Description|**Default variable value to be used if no associated EnvironmentVariableValue entities exist.**|
|DisplayName|**Default Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`defaultvalue`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the variable definition.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|2000|

### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|---|---|
|Description|**Display Name of the variable definition.**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`displayname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|100|

### <a name="BKMK_EnvironmentVariableDefinitionId"></a> EnvironmentVariableDefinitionId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Environment Variable Definition**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`environmentvariabledefinitionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Hint"></a> Hint

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Hint**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`hint`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|2000|

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

### <a name="BKMK_InputControlConfig"></a> InputControlConfig

|Property|Value|
|---|---|
|Description|**A JSON object describing the options for the input control that should be presented to the user for setting the current value of the Environment variable.**|
|DisplayName|**Input Control Config**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`inputcontrolconfig`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the form is introduced.**|
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

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**Tells whether the component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsRequired"></a> IsRequired

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Required**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isrequired`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`environmentvariabledefinition_isrequired`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_LearnMoreUrl"></a> LearnMoreUrl

|Property|Value|
|---|---|
|Description|**Clicking on this url will take the user to a webpage which further explains the environment variable being populated.**|
|DisplayName|**Learn More Url**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`learnmoreurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

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

### <a name="BKMK_ParameterKey"></a> ParameterKey

|Property|Value|
|---|---|
|Description||
|DisplayName|**Parameter Key**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parameterkey`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|150|

### <a name="BKMK_ParentDefinitionId"></a> ParentDefinitionId

|Property|Value|
|---|---|
|Description|**Unique identifier for Environment Variable Definition associated with Environment Variable Definition.**|
|DisplayName|**Parent Definition**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentdefinitionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|environmentvariabledefinition|

### <a name="BKMK_SchemaName"></a> SchemaName

|Property|Value|
|---|---|
|Description|**Unique entity name.**|
|DisplayName|**Schema Name**|
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

### <a name="BKMK_SecretStore"></a> SecretStore

|Property|Value|
|---|---|
|Description|**Environment variable secret store.**|
|DisplayName|**SecretStore**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`secretstore`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`environmentvariabledefinition_secretstore`|

#### SecretStore Choices/Options

|Value|Label|
|---|---|
|0|**Azure Key Vault**|
|1|**Microsoft Dataverse**|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Environment Variable Definition**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`environmentvariabledefinition_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Environment Variable Definition**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`environmentvariabledefinition_statuscode`|

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

### <a name="BKMK_Type"></a> Type

|Property|Value|
|---|---|
|Description|**Environment variable value type.**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|100000000|
|GlobalChoiceName|`environmentvariabledefinition_type`|

#### Type Choices/Options

|Value|Label|
|---|---|
|100000000|**String**|
|100000001|**Number**|
|100000002|**Boolean**|
|100000003|**JSON**|
|100000004|**Data Source**|
|100000005|**Secret**|

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

### <a name="BKMK_ValueSchema"></a> ValueSchema

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Value Schema**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`valueschema`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EnvironmentVariableDefinitionIdUnique](#BKMK_EnvironmentVariableDefinitionIdUnique)
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

### <a name="BKMK_EnvironmentVariableDefinitionIdUnique"></a> EnvironmentVariableDefinitionIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`environmentvariabledefinitionidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
|Format|DateOnly|
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

- [business_unit_environmentvariabledefinition](#BKMK_business_unit_environmentvariabledefinition)
- [envdefinition_envdefinition](#BKMK_envdefinition_envdefinition-many-to-one)
- [lk_environmentvariabledefinition_createdby](#BKMK_lk_environmentvariabledefinition_createdby)
- [lk_environmentvariabledefinition_createdonbehalfby](#BKMK_lk_environmentvariabledefinition_createdonbehalfby)
- [lk_environmentvariabledefinition_modifiedby](#BKMK_lk_environmentvariabledefinition_modifiedby)
- [lk_environmentvariabledefinition_modifiedonbehalfby](#BKMK_lk_environmentvariabledefinition_modifiedonbehalfby)
- [owner_environmentvariabledefinition](#BKMK_owner_environmentvariabledefinition)
- [team_environmentvariabledefinition](#BKMK_team_environmentvariabledefinition)
- [user_environmentvariabledefinition](#BKMK_user_environmentvariabledefinition)

### <a name="BKMK_business_unit_environmentvariabledefinition"></a> business_unit_environmentvariabledefinition

One-To-Many Relationship: [businessunit business_unit_environmentvariabledefinition](businessunit.md#BKMK_business_unit_environmentvariabledefinition)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_envdefinition_envdefinition-many-to-one"></a> envdefinition_envdefinition

One-To-Many Relationship: [environmentvariabledefinition envdefinition_envdefinition](#BKMK_envdefinition_envdefinition-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`environmentvariabledefinition`|
|ReferencedAttribute|`environmentvariabledefinitionid`|
|ReferencingAttribute|`parentdefinitionid`|
|ReferencingEntityNavigationPropertyName|`ParentDefinitionId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_environmentvariabledefinition_createdby"></a> lk_environmentvariabledefinition_createdby

One-To-Many Relationship: [systemuser lk_environmentvariabledefinition_createdby](systemuser.md#BKMK_lk_environmentvariabledefinition_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_environmentvariabledefinition_createdonbehalfby"></a> lk_environmentvariabledefinition_createdonbehalfby

One-To-Many Relationship: [systemuser lk_environmentvariabledefinition_createdonbehalfby](systemuser.md#BKMK_lk_environmentvariabledefinition_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_environmentvariabledefinition_modifiedby"></a> lk_environmentvariabledefinition_modifiedby

One-To-Many Relationship: [systemuser lk_environmentvariabledefinition_modifiedby](systemuser.md#BKMK_lk_environmentvariabledefinition_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_environmentvariabledefinition_modifiedonbehalfby"></a> lk_environmentvariabledefinition_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_environmentvariabledefinition_modifiedonbehalfby](systemuser.md#BKMK_lk_environmentvariabledefinition_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_environmentvariabledefinition"></a> owner_environmentvariabledefinition

One-To-Many Relationship: [owner owner_environmentvariabledefinition](owner.md#BKMK_owner_environmentvariabledefinition)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_environmentvariabledefinition"></a> team_environmentvariabledefinition

One-To-Many Relationship: [team team_environmentvariabledefinition](team.md#BKMK_team_environmentvariabledefinition)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_environmentvariabledefinition"></a> user_environmentvariabledefinition

One-To-Many Relationship: [systemuser user_environmentvariabledefinition](systemuser.md#BKMK_user_environmentvariabledefinition)

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

- [envdefinition_envdefinition](#BKMK_envdefinition_envdefinition-one-to-many)
- [environmentvariabledefinition_AsyncOperations](#BKMK_environmentvariabledefinition_AsyncOperations)
- [environmentvariabledefinition_BulkDeleteFailures](#BKMK_environmentvariabledefinition_BulkDeleteFailures)
- [environmentvariabledefinition_credential_certificate](#BKMK_environmentvariabledefinition_credential_certificate)
- [environmentvariabledefinition_credential_cyberarkobject](#BKMK_environmentvariabledefinition_credential_cyberarkobject)
- [environmentvariabledefinition_credential_cyberarksafe](#BKMK_environmentvariabledefinition_credential_cyberarksafe)
- [environmentvariabledefinition_credential_cyberarkusername](#BKMK_environmentvariabledefinition_credential_cyberarkusername)
- [environmentvariabledefinition_credential_password](#BKMK_environmentvariabledefinition_credential_password)
- [environmentvariabledefinition_credential_username](#BKMK_environmentvariabledefinition_credential_username)
- [environmentvariabledefinition_DuplicateBaseRecord](#BKMK_environmentvariabledefinition_DuplicateBaseRecord)
- [environmentvariabledefinition_DuplicateMatchingRecord](#BKMK_environmentvariabledefinition_DuplicateMatchingRecord)
- [environmentvariabledefinition_environmentvariablevalue](#BKMK_environmentvariabledefinition_environmentvariablevalue)
- [environmentvariabledefinition_flowmachinenetwork_domainpassword](#BKMK_environmentvariabledefinition_flowmachinenetwork_domainpassword)
- [environmentvariabledefinition_flowmachinenetwork_domainusername](#BKMK_environmentvariabledefinition_flowmachinenetwork_domainusername)
- [environmentvariabledefinition_MailboxTrackingFolders](#BKMK_environmentvariabledefinition_MailboxTrackingFolders)
- [environmentvariabledefinition_PrincipalObjectAttributeAccesses](#BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses)
- [environmentvariabledefinition_ProcessSession](#BKMK_environmentvariabledefinition_ProcessSession)
- [EnvironmentVariableDefinition_ReportParameter_EvironmentVariableDefinitionId](#BKMK_EnvironmentVariableDefinition_ReportParameter_EvironmentVariableDefinitionId)
- [environmentvariabledefinition_SyncErrors](#BKMK_environmentvariabledefinition_SyncErrors)
- [envvardefinition_powerbimashupparameter](#BKMK_envvardefinition_powerbimashupparameter)
- [mspp_environmentvariabledefinition_mspp_sitesetting_environmentvariable](#BKMK_mspp_environmentvariabledefinition_mspp_sitesetting_environmentvariable)

### <a name="BKMK_envdefinition_envdefinition-one-to-many"></a> envdefinition_envdefinition

Many-To-One Relationship: [environmentvariabledefinition envdefinition_envdefinition](#BKMK_envdefinition_envdefinition-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`environmentvariabledefinition`|
|ReferencingAttribute|`parentdefinitionid`|
|ReferencedEntityNavigationPropertyName|`envdefinition_envdefinition`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_AsyncOperations"></a> environmentvariabledefinition_AsyncOperations

Many-To-One Relationship: [asyncoperation environmentvariabledefinition_AsyncOperations](asyncoperation.md#BKMK_environmentvariabledefinition_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_BulkDeleteFailures"></a> environmentvariabledefinition_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure environmentvariabledefinition_BulkDeleteFailures](bulkdeletefailure.md#BKMK_environmentvariabledefinition_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_credential_certificate"></a> environmentvariabledefinition_credential_certificate

Many-To-One Relationship: [credential environmentvariabledefinition_credential_certificate](credential.md#BKMK_environmentvariabledefinition_credential_certificate)

|Property|Value|
|---|---|
|ReferencingEntity|`credential`|
|ReferencingAttribute|`certificate`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_credential_certificate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_credential_cyberarkobject"></a> environmentvariabledefinition_credential_cyberarkobject

Many-To-One Relationship: [credential environmentvariabledefinition_credential_cyberarkobject](credential.md#BKMK_environmentvariabledefinition_credential_cyberarkobject)

|Property|Value|
|---|---|
|ReferencingEntity|`credential`|
|ReferencingAttribute|`cyberarkobject`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_credential_cyberarkobject`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_credential_cyberarksafe"></a> environmentvariabledefinition_credential_cyberarksafe

Many-To-One Relationship: [credential environmentvariabledefinition_credential_cyberarksafe](credential.md#BKMK_environmentvariabledefinition_credential_cyberarksafe)

|Property|Value|
|---|---|
|ReferencingEntity|`credential`|
|ReferencingAttribute|`cyberarksafe`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_credential_cyberarksafe`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_credential_cyberarkusername"></a> environmentvariabledefinition_credential_cyberarkusername

Many-To-One Relationship: [credential environmentvariabledefinition_credential_cyberarkusername](credential.md#BKMK_environmentvariabledefinition_credential_cyberarkusername)

|Property|Value|
|---|---|
|ReferencingEntity|`credential`|
|ReferencingAttribute|`cyberarkusername`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_credential_cyberarkusername`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_credential_password"></a> environmentvariabledefinition_credential_password

Many-To-One Relationship: [credential environmentvariabledefinition_credential_password](credential.md#BKMK_environmentvariabledefinition_credential_password)

|Property|Value|
|---|---|
|ReferencingEntity|`credential`|
|ReferencingAttribute|`password`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_credential_password`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_credential_username"></a> environmentvariabledefinition_credential_username

Many-To-One Relationship: [credential environmentvariabledefinition_credential_username](credential.md#BKMK_environmentvariabledefinition_credential_username)

|Property|Value|
|---|---|
|ReferencingEntity|`credential`|
|ReferencingAttribute|`username`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_credential_username`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_DuplicateBaseRecord"></a> environmentvariabledefinition_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord environmentvariabledefinition_DuplicateBaseRecord](duplicaterecord.md#BKMK_environmentvariabledefinition_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_DuplicateMatchingRecord"></a> environmentvariabledefinition_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord environmentvariabledefinition_DuplicateMatchingRecord](duplicaterecord.md#BKMK_environmentvariabledefinition_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_environmentvariablevalue"></a> environmentvariabledefinition_environmentvariablevalue

Many-To-One Relationship: [environmentvariablevalue environmentvariabledefinition_environmentvariablevalue](environmentvariablevalue.md#BKMK_environmentvariabledefinition_environmentvariablevalue)

|Property|Value|
|---|---|
|ReferencingEntity|`environmentvariablevalue`|
|ReferencingAttribute|`environmentvariabledefinitionid`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_environmentvariablevalue`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_flowmachinenetwork_domainpassword"></a> environmentvariabledefinition_flowmachinenetwork_domainpassword

Many-To-One Relationship: [flowmachinenetwork environmentvariabledefinition_flowmachinenetwork_domainpassword](flowmachinenetwork.md#BKMK_environmentvariabledefinition_flowmachinenetwork_domainpassword)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachinenetwork`|
|ReferencingAttribute|`domainpassword`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_flowmachinenetwork_domainpassword`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_flowmachinenetwork_domainusername"></a> environmentvariabledefinition_flowmachinenetwork_domainusername

Many-To-One Relationship: [flowmachinenetwork environmentvariabledefinition_flowmachinenetwork_domainusername](flowmachinenetwork.md#BKMK_environmentvariabledefinition_flowmachinenetwork_domainusername)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachinenetwork`|
|ReferencingAttribute|`domainusername`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_credential_domainusername`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_MailboxTrackingFolders"></a> environmentvariabledefinition_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder environmentvariabledefinition_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_environmentvariabledefinition_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses"></a> environmentvariabledefinition_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess environmentvariabledefinition_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_ProcessSession"></a> environmentvariabledefinition_ProcessSession

Many-To-One Relationship: [processsession environmentvariabledefinition_ProcessSession](processsession.md#BKMK_environmentvariabledefinition_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_EnvironmentVariableDefinition_ReportParameter_EvironmentVariableDefinitionId"></a> EnvironmentVariableDefinition_ReportParameter_EvironmentVariableDefinitionId

Many-To-One Relationship: [reportparameter EnvironmentVariableDefinition_ReportParameter_EvironmentVariableDefinitionId](reportparameter.md#BKMK_EnvironmentVariableDefinition_ReportParameter_EvironmentVariableDefinitionId)

|Property|Value|
|---|---|
|ReferencingEntity|`reportparameter`|
|ReferencingAttribute|`environmentvariabledefinitionid`|
|ReferencedEntityNavigationPropertyName|`EnvironmentVariableDefinition_ReportParameters`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_environmentvariabledefinition_SyncErrors"></a> environmentvariabledefinition_SyncErrors

Many-To-One Relationship: [syncerror environmentvariabledefinition_SyncErrors](syncerror.md#BKMK_environmentvariabledefinition_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`environmentvariabledefinition_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_envvardefinition_powerbimashupparameter"></a> envvardefinition_powerbimashupparameter

Many-To-One Relationship: [powerbimashupparameter envvardefinition_powerbimashupparameter](powerbimashupparameter.md#BKMK_envvardefinition_powerbimashupparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbimashupparameter`|
|ReferencingAttribute|`environmentvariableid`|
|ReferencedEntityNavigationPropertyName|`envvardefinition_powerbimashupparameter`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_environmentvariabledefinition_mspp_sitesetting_environmentvariable"></a> mspp_environmentvariabledefinition_mspp_sitesetting_environmentvariable

Many-To-One Relationship: [mspp_sitesetting mspp_environmentvariabledefinition_mspp_sitesetting_environmentvariable](mspp_sitesetting.md#BKMK_mspp_environmentvariabledefinition_mspp_sitesetting_environmentvariable)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_sitesetting`|
|ReferencingAttribute|`mspp_environmentvariable`|
|ReferencedEntityNavigationPropertyName|`mspp_environmentvariabledefinition_mspp_sitesetting_environmentvariable`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [bot_environmentvariabledefinition](#BKMK_bot_environmentvariabledefinition)
- [botcomponent_environmentvariabledefinition](#BKMK_botcomponent_environmentvariabledefinition)
- [msdyn_connectordatasource_environmentvariable](#BKMK_msdyn_connectordatasource_environmentvariable)

### <a name="BKMK_bot_environmentvariabledefinition"></a> bot_environmentvariabledefinition

See [bot bot_environmentvariabledefinition Many-To-Many Relationship](bot.md#BKMK_bot_environmentvariabledefinition)

|Property|Value|
|---|---|
|IntersectEntityName|`bot_environmentvariabledefinition`|
|IsCustomizable|False|
|SchemaName|`bot_environmentvariabledefinition`|
|IntersectAttribute|`environmentvariabledefinitionid`|
|NavigationPropertyName|`bot_environmentvariabledefinition`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_botcomponent_environmentvariabledefinition"></a> botcomponent_environmentvariabledefinition

See [botcomponent botcomponent_environmentvariabledefinition Many-To-Many Relationship](botcomponent.md#BKMK_botcomponent_environmentvariabledefinition)

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_environmentvariabledefinition`|
|IsCustomizable|False|
|SchemaName|`botcomponent_environmentvariabledefinition`|
|IntersectAttribute|`environmentvariabledefinitionid`|
|NavigationPropertyName|`botcomponent_environmentvariabledefinition`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_connectordatasource_environmentvariable"></a> msdyn_connectordatasource_environmentvariable

See [msdyn_connectordatasource msdyn_connectordatasource_environmentvariable Many-To-Many Relationship](msdyn_connectordatasource.md#BKMK_msdyn_connectordatasource_environmentvariable)

|Property|Value|
|---|---|
|IntersectEntityName|`msdyn_connectordatasource_environmentva`|
|IsCustomizable|True|
|SchemaName|`msdyn_connectordatasource_environmentvariable`|
|IntersectAttribute|`environmentvariabledefinitionid`|
|NavigationPropertyName|`msdyn_connectordatasource_environmentvari`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.environmentvariabledefinition?displayProperty=fullName>
