---
title: "EnvironmentVariableDefinition table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the EnvironmentVariableDefinition table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# EnvironmentVariableDefinition table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Contains information about the settable variable: its type, default value, and etc.

**Added by**: Environment Variables Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /environmentvariabledefinitions(*environmentvariabledefinitionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST /environmentvariabledefinitions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /environmentvariabledefinitions(*environmentvariabledefinitionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET /environmentvariabledefinitions(*environmentvariabledefinitionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveAllCompositeDataSources|<xref:Microsoft.Dynamics.CRM.RetrieveAllCompositeDataSources?displayProperty=nameWithType />|Use <xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/>where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName> = RetrieveAllCompositeDataSources|
|RetrieveCompositeDataSource|<xref:Microsoft.Dynamics.CRM.RetrieveCompositeDataSource?displayProperty=nameWithType />|Use <xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/>where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName> = RetrieveCompositeDataSource|
|RetrieveEnvironmentVariables|<xref:Microsoft.Dynamics.CRM.RetrieveEnvironmentVariables?displayProperty=nameWithType />|Use <xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/>where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName> = RetrieveEnvironmentVariables|
|RetrieveEnvironmentVariableValue|<xref:Microsoft.Dynamics.CRM.RetrieveEnvironmentVariableValue?displayProperty=nameWithType />|Use <xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/>where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName> = RetrieveEnvironmentVariableValue|
|RetrieveMultiple|GET /environmentvariabledefinitions<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH /environmentvariabledefinitions(*environmentvariabledefinitionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /environmentvariabledefinitions(*environmentvariabledefinitionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|EnvironmentVariableDefinitions|
|DisplayCollectionName|Environment Variable Definitions|
|DisplayName|Environment Variable Definition|
|EntitySetName|environmentvariabledefinitions|
|IsBPFEntity|False|
|LogicalCollectionName|environmentvariabledefinitions|
|LogicalName|environmentvariabledefinition|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|environmentvariabledefinitionid|
|PrimaryNameAttribute|schemaname|
|SchemaName|EnvironmentVariableDefinition|

<a name="writable-attributes"></a>

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
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsRequired](#BKMK_IsRequired)
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
|--------|-----|
|Description||
|DisplayName|API Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|apiid|
|MaxLength|150|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ConnectionReferenceId"></a> ConnectionReferenceId

|Property|Value|
|--------|-----|
|Description|Unique identifier for Connection Reference associated with Environment Variable Definition.|
|DisplayName|Connection Reference|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|connectionreferenceid|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_DefaultValue"></a> DefaultValue

|Property|Value|
|--------|-----|
|Description|Default variable value to be used if no associated EnvironmentVariableValue entities exist.|
|DisplayName|Default Value|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|defaultvalue|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the variable definition.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|--------|-----|
|Description|Display Name of the variable definition.|
|DisplayName|Display Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|displayname|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_EnvironmentVariableDefinitionId"></a> EnvironmentVariableDefinitionId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Environment Variable Definition|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|environmentvariabledefinitionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_Hint"></a> Hint

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Hint|
|Format|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|hint|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


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


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the form is introduced.|
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


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|--------|-----|
|Description|Tells whether the component can be customized.|
|DisplayName|Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_IsRequired"></a> IsRequired

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Required|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isrequired|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### IsRequired Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_ParameterKey"></a> ParameterKey

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Parameter Key|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parameterkey|
|MaxLength|150|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ParentDefinitionId"></a> ParentDefinitionId

|Property|Value|
|--------|-----|
|Description|Unique identifier for Environment Variable Definition associated with Environment Variable Definition.|
|DisplayName|Parent Definition|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentdefinitionid|
|RequiredLevel|None|
|Targets|environmentvariabledefinition|
|Type|Lookup|


### <a name="BKMK_SchemaName"></a> SchemaName

|Property|Value|
|--------|-----|
|Description|Unique entity name.|
|DisplayName|Schema Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|schemaname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_SecretStore"></a> SecretStore

|Property|Value|
|--------|-----|
|Description|Environment variable secret store.|
|DisplayName|SecretStore|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|secretstore|
|RequiredLevel|None|
|Type|Picklist|

#### SecretStore Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Azure Key Vault||
|1|Microsoft Dataverse||



### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Environment Variable Definition|
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
|Description|Reason for the status of the Environment Variable Definition|
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


### <a name="BKMK_Type"></a> Type

|Property|Value|
|--------|-----|
|Description|Environment variable value type.|
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|type|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### Type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|100000000|String||
|100000001|Number||
|100000002|Boolean||
|100000003|JSON||
|100000004|Data Source||
|100000005|Secret||



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


### <a name="BKMK_ValueSchema"></a> ValueSchema

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Value Schema|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|valueschema|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [EnvironmentVariableDefinitionIdUnique](#BKMK_EnvironmentVariableDefinitionIdUnique)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ParentDefinitionIdName](#BKMK_ParentDefinitionIdName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


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


### <a name="BKMK_EnvironmentVariableDefinitionIdUnique"></a> EnvironmentVariableDefinitionIdUnique

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|environmentvariabledefinitionidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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


### <a name="BKMK_ParentDefinitionIdName"></a> ParentDefinitionIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentdefinitionidname|
|MaxLength|100|
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

- [environmentvariabledefinition_SyncErrors](#BKMK_environmentvariabledefinition_SyncErrors)
- [environmentvariabledefinition_DuplicateMatchingRecord](#BKMK_environmentvariabledefinition_DuplicateMatchingRecord)
- [environmentvariabledefinition_DuplicateBaseRecord](#BKMK_environmentvariabledefinition_DuplicateBaseRecord)
- [environmentvariabledefinition_AsyncOperations](#BKMK_environmentvariabledefinition_AsyncOperations)
- [environmentvariabledefinition_MailboxTrackingFolders](#BKMK_environmentvariabledefinition_MailboxTrackingFolders)
- [environmentvariabledefinition_ProcessSession](#BKMK_environmentvariabledefinition_ProcessSession)
- [environmentvariabledefinition_BulkDeleteFailures](#BKMK_environmentvariabledefinition_BulkDeleteFailures)
- [environmentvariabledefinition_PrincipalObjectAttributeAccesses](#BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses)
- [environmentvariabledefinition_environmentvariablevalue](#BKMK_environmentvariabledefinition_environmentvariablevalue)
- [envdefinition_envdefinition](#BKMK_envdefinition_envdefinition)
- [envvardefinition_powerbimashupparameter](#BKMK_envvardefinition_powerbimashupparameter)


### <a name="BKMK_environmentvariabledefinition_SyncErrors"></a> environmentvariabledefinition_SyncErrors

**Added by**: System Solution Solution

Same as the [environmentvariabledefinition_SyncErrors](syncerror.md#BKMK_environmentvariabledefinition_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|environmentvariabledefinition_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_environmentvariabledefinition_DuplicateMatchingRecord"></a> environmentvariabledefinition_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [environmentvariabledefinition_DuplicateMatchingRecord](duplicaterecord.md#BKMK_environmentvariabledefinition_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|environmentvariabledefinition_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_environmentvariabledefinition_DuplicateBaseRecord"></a> environmentvariabledefinition_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [environmentvariabledefinition_DuplicateBaseRecord](duplicaterecord.md#BKMK_environmentvariabledefinition_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|environmentvariabledefinition_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_environmentvariabledefinition_AsyncOperations"></a> environmentvariabledefinition_AsyncOperations

**Added by**: System Solution Solution

Same as the [environmentvariabledefinition_AsyncOperations](asyncoperation.md#BKMK_environmentvariabledefinition_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|environmentvariabledefinition_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_environmentvariabledefinition_MailboxTrackingFolders"></a> environmentvariabledefinition_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [environmentvariabledefinition_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_environmentvariabledefinition_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|environmentvariabledefinition_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_environmentvariabledefinition_ProcessSession"></a> environmentvariabledefinition_ProcessSession

**Added by**: System Solution Solution

Same as the [environmentvariabledefinition_ProcessSession](processsession.md#BKMK_environmentvariabledefinition_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|environmentvariabledefinition_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_environmentvariabledefinition_BulkDeleteFailures"></a> environmentvariabledefinition_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [environmentvariabledefinition_BulkDeleteFailures](bulkdeletefailure.md#BKMK_environmentvariabledefinition_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|environmentvariabledefinition_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses"></a> environmentvariabledefinition_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [environmentvariabledefinition_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_environmentvariabledefinition_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|environmentvariabledefinition_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_environmentvariabledefinition_environmentvariablevalue"></a> environmentvariabledefinition_environmentvariablevalue

Same as the [environmentvariabledefinition_environmentvariablevalue](environmentvariablevalue.md#BKMK_environmentvariabledefinition_environmentvariablevalue) many-to-one relationship for the [environmentvariablevalue](environmentvariablevalue.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariablevalue|
|ReferencingAttribute|environmentvariabledefinitionid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|environmentvariabledefinition_environmentvariablevalue|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_envdefinition_envdefinition"></a> envdefinition_envdefinition

Same as the [envdefinition_envdefinition](environmentvariabledefinition.md#BKMK_envdefinition_envdefinition) many-to-one relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariabledefinition|
|ReferencingAttribute|parentdefinitionid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|envdefinition_envdefinition|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_envvardefinition_powerbimashupparameter"></a> envvardefinition_powerbimashupparameter

**Added by**: Power BI Entities Solution

Same as the [envvardefinition_powerbimashupparameter](powerbimashupparameter.md#BKMK_envvardefinition_powerbimashupparameter) many-to-one relationship for the [powerbimashupparameter](powerbimashupparameter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|powerbimashupparameter|
|ReferencingAttribute|environmentvariableid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|envvardefinition_powerbimashupparameter|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_environmentvariabledefinition_createdby](#BKMK_lk_environmentvariabledefinition_createdby)
- [lk_environmentvariabledefinition_createdonbehalfby](#BKMK_lk_environmentvariabledefinition_createdonbehalfby)
- [lk_environmentvariabledefinition_modifiedby](#BKMK_lk_environmentvariabledefinition_modifiedby)
- [lk_environmentvariabledefinition_modifiedonbehalfby](#BKMK_lk_environmentvariabledefinition_modifiedonbehalfby)
- [user_environmentvariabledefinition](#BKMK_user_environmentvariabledefinition)
- [team_environmentvariabledefinition](#BKMK_team_environmentvariabledefinition)
- [business_unit_environmentvariabledefinition](#BKMK_business_unit_environmentvariabledefinition)
- [envdefinition_envdefinition](#BKMK_envdefinition_envdefinition)


### <a name="BKMK_lk_environmentvariabledefinition_createdby"></a> lk_environmentvariabledefinition_createdby

**Added by**: System Solution Solution

See the [lk_environmentvariabledefinition_createdby](systemuser.md#BKMK_lk_environmentvariabledefinition_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_environmentvariabledefinition_createdonbehalfby"></a> lk_environmentvariabledefinition_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_environmentvariabledefinition_createdonbehalfby](systemuser.md#BKMK_lk_environmentvariabledefinition_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_environmentvariabledefinition_modifiedby"></a> lk_environmentvariabledefinition_modifiedby

**Added by**: System Solution Solution

See the [lk_environmentvariabledefinition_modifiedby](systemuser.md#BKMK_lk_environmentvariabledefinition_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_environmentvariabledefinition_modifiedonbehalfby"></a> lk_environmentvariabledefinition_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_environmentvariabledefinition_modifiedonbehalfby](systemuser.md#BKMK_lk_environmentvariabledefinition_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_environmentvariabledefinition"></a> user_environmentvariabledefinition

**Added by**: System Solution Solution

See the [user_environmentvariabledefinition](systemuser.md#BKMK_user_environmentvariabledefinition) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_environmentvariabledefinition"></a> team_environmentvariabledefinition

**Added by**: System Solution Solution

See the [team_environmentvariabledefinition](team.md#BKMK_team_environmentvariabledefinition) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_environmentvariabledefinition"></a> business_unit_environmentvariabledefinition

**Added by**: System Solution Solution

See the [business_unit_environmentvariabledefinition](businessunit.md#BKMK_business_unit_environmentvariabledefinition) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_envdefinition_envdefinition"></a> envdefinition_envdefinition

See the [envdefinition_envdefinition](environmentvariabledefinition.md#BKMK_envdefinition_envdefinition) one-to-many relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the EnvironmentVariableDefinition table is the first table in the relationship. Listed by **SchemaName**.

- [bot_environmentvariabledefinition](#BKMK_bot_environmentvariabledefinition)
- [botcomponent_environmentvariabledefinition](#BKMK_botcomponent_environmentvariabledefinition)


### <a name="BKMK_bot_environmentvariabledefinition"></a> bot_environmentvariabledefinition

See the [bot_environmentvariabledefinition](bot.md#BKMK_bot_environmentvariabledefinition) many-to-many relationship for the [bot](bot.md) table/entity.

### <a name="BKMK_botcomponent_environmentvariabledefinition"></a> botcomponent_environmentvariabledefinition

See the [botcomponent_environmentvariabledefinition](botcomponent.md#BKMK_botcomponent_environmentvariabledefinition) many-to-many relationship for the [botcomponent](botcomponent.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.environmentvariabledefinition?text=environmentvariabledefinition EntityType" />