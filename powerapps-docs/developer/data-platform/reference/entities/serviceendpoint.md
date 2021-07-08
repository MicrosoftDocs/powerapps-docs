---
title: "ServiceEndpoint table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the ServiceEndpoint table/entity."
ms.date: 05/20/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# ServiceEndpoint table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Service endpoint that can be contacted.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/serviceendpoints<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/serviceendpoints(*serviceendpointid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/serviceendpoints(*serviceendpointid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/serviceendpoints<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|TriggerServiceEndpointCheck|<xref href="Microsoft.Dynamics.CRM.TriggerServiceEndpointCheck?text=TriggerServiceEndpointCheck Action" />|<xref:Microsoft.Crm.Sdk.Messages.TriggerServiceEndpointCheckRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/serviceendpoints(*serviceendpointid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|ServiceEndpoints|
|DisplayCollectionName|Service Endpoints|
|DisplayName|Service Endpoint|
|EntitySetName|serviceendpoints|
|IsBPFEntity|False|
|LogicalCollectionName|serviceendpoints|
|LogicalName|serviceendpoint|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|serviceendpointid|
|PrimaryNameAttribute|name|
|SchemaName|ServiceEndpoint|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AuthType](#BKMK_AuthType)
- [AuthValue](#BKMK_AuthValue)
- [ConnectionMode](#BKMK_ConnectionMode)
- [Contract](#BKMK_Contract)
- [Description](#BKMK_Description)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [KeyVaultReferenceId](#BKMK_KeyVaultReferenceId)
- [MessageFormat](#BKMK_MessageFormat)
- [Name](#BKMK_Name)
- [NamespaceAddress](#BKMK_NamespaceAddress)
- [NamespaceFormat](#BKMK_NamespaceFormat)
- [Path](#BKMK_Path)
- [SASKey](#BKMK_SASKey)
- [SASKeyName](#BKMK_SASKeyName)
- [SASToken](#BKMK_SASToken)
- [SchemaType](#BKMK_SchemaType)
- [ServiceEndpointId](#BKMK_ServiceEndpointId)
- [SolutionNamespace](#BKMK_SolutionNamespace)
- [Url](#BKMK_Url)
- [UseKeyVaultConfiguration](#BKMK_UseKeyVaultConfiguration)
- [UserClaim](#BKMK_UserClaim)


### <a name="BKMK_AuthType"></a> AuthType

|Property|Value|
|--------|-----|
|Description|Specifies mode of authentication with SB|
|DisplayName|Specifies mode of authentication with SB|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|authtype|
|RequiredLevel|None|
|Type|Picklist|

#### AuthType Choices/Options

|Value|Label|
|-----|-----|
|1|ACS|
|2|SAS Key|
|3|SAS Token|
|4|Webhook Key|
|5|Http Header|
|6|Http Query String|
|7|Connection String|
|8|Access Key|



### <a name="BKMK_AuthValue"></a> AuthValue

|Property|Value|
|--------|-----|
|Description|Authentication Value|
|DisplayName|Authentication Value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|authvalue|
|MaxLength|2048|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ConnectionMode"></a> ConnectionMode

|Property|Value|
|--------|-----|
|Description|Connection mode to contact the service endpoint.|
|DisplayName|Connection Mode|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|connectionmode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ConnectionMode Choices/Options

|Value|Label|
|-----|-----|
|1|Normal|
|2|Federated|



### <a name="BKMK_Contract"></a> Contract

|Property|Value|
|--------|-----|
|Description|Type of the endpoint contract.|
|DisplayName|Contract|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|contract|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Contract Choices/Options

|Value|Label|
|-----|-----|
|1|OneWay|
|2|Queue|
|3|Rest|
|4|TwoWay|
|5|Topic|
|6|Queue (Persistent)|
|7|Event Hub|
|8|Webhook|
|9|Event Grid|



### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the service endpoint.|
|DisplayName|Description|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


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
|Description|Information that specifies whether this component can be customized.|
|DisplayName|Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_KeyVaultReferenceId"></a> KeyVaultReferenceId

**Added by**: ManagedIdentityExtensions Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for keyvaultreference associated with serviceendpoint.|
|DisplayName|KeyVaultReferenceId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|keyvaultreferenceid|
|RequiredLevel|None|
|Targets|keyvaultreference|
|Type|Lookup|


### <a name="BKMK_MessageFormat"></a> MessageFormat

|Property|Value|
|--------|-----|
|Description|Content type of the message|
|DisplayName|Content type of the message|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|messageformat|
|RequiredLevel|None|
|Type|Picklist|

#### MessageFormat Choices/Options

|Value|Label|
|-----|-----|
|1|Binary XML|
|2|Json|
|3|Text XML|



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of Service end point.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_NamespaceAddress"></a> NamespaceAddress

|Property|Value|
|--------|-----|
|Description|Full service endpoint address.|
|DisplayName|Namespace Address|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|namespaceaddress|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_NamespaceFormat"></a> NamespaceFormat

|Property|Value|
|--------|-----|
|Description|Format of Service Bus Namespace|
|DisplayName|Format of Service Bus Namespace|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|namespaceformat|
|RequiredLevel|None|
|Type|Picklist|

#### NamespaceFormat Choices/Options

|Value|Label|
|-----|-----|
|1|Namespace Name|
|2|Namespace Address|



### <a name="BKMK_Path"></a> Path

|Property|Value|
|--------|-----|
|Description|Path to the service endpoint.|
|DisplayName|Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|path|
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_SASKey"></a> SASKey

|Property|Value|
|--------|-----|
|Description|Shared Access Key|
|DisplayName|Shared Access Key|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|saskey|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SASKeyName"></a> SASKeyName

|Property|Value|
|--------|-----|
|Description|Shared Access Key Name|
|DisplayName|Shared Access Key Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|saskeyname|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SASToken"></a> SASToken

|Property|Value|
|--------|-----|
|Description|Shared Access Token|
|DisplayName|Shared Access Token|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|sastoken|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SchemaType"></a> SchemaType

**Added by**: ServiceEndpointInfrastructure Solution

|Property|Value|
|--------|-----|
|Description|Specifies schema type for event grid events|
|DisplayName|Specifies schema type for event grid events|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|schematype|
|RequiredLevel|None|
|Type|Picklist|

#### SchemaType Choices/Options

|Value|Label|
|-----|-----|
|1|Event Grid|
|2|Cloud Events|



### <a name="BKMK_ServiceEndpointId"></a> ServiceEndpointId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the service endpoint.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|serviceendpointid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SolutionNamespace"></a> SolutionNamespace

|Property|Value|
|--------|-----|
|Description|Namespace of the App Fabric solution.|
|DisplayName|Service Namespace|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|solutionnamespace|
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_Url"></a> Url

|Property|Value|
|--------|-----|
|Description|Full service endpoint Url.|
|DisplayName|Url Address|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|url|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_UseKeyVaultConfiguration"></a> UseKeyVaultConfiguration

**Added by**: ManagedIdentityExtensions Solution

|Property|Value|
|--------|-----|
|Description|Use Auth Information in KeyVault|
|DisplayName|Use Auth Information in KeyVault|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|usekeyvaultconfiguration|
|RequiredLevel|None|
|Type|Boolean|

#### UseKeyVaultConfiguration Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_UserClaim"></a> UserClaim

|Property|Value|
|--------|-----|
|Description|Additional user claim value type.|
|DisplayName|User Claim|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|userclaim|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### UserClaim Choices/Options

|Value|Label|
|-----|-----|
|1|None|
|2|UserId|
|3|UserInfo|


<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsAuthValueSet](#BKMK_IsAuthValueSet)
- [IsManaged](#BKMK_IsManaged)
- [IsSASKeySet](#BKMK_IsSASKeySet)
- [IsSASTokenSet](#BKMK_IsSASTokenSet)
- [keyvaultreferenceidName](#BKMK_keyvaultreferenceidName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [ServiceEndpointIdUnique](#BKMK_ServiceEndpointIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)


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

|Value|Label|
|-----|-----|
|0|Published|
|1|Unpublished|
|2|Deleted|
|3|Deleted Unpublished|



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the service endpoint.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the service endpoint was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the service endpoint.|
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


### <a name="BKMK_IsAuthValueSet"></a> IsAuthValueSet

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isauthvalueset|
|RequiredLevel|None|
|Type|Boolean|

#### IsAuthValueSet Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component is managed.|
|DisplayName|State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|
|-----|-----|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_IsSASKeySet"></a> IsSASKeySet

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|issaskeyset|
|RequiredLevel|None|
|Type|Boolean|

#### IsSASKeySet Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsSASTokenSet"></a> IsSASTokenSet

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|issastokenset|
|RequiredLevel|None|
|Type|Boolean|

#### IsSASTokenSet Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_keyvaultreferenceidName"></a> keyvaultreferenceidName

**Added by**: ManagedIdentityExtensions Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|keyvaultreferenceidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the service endpoint.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the service endpoint was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the service endpoint.|
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization with which the service endpoint is associated.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


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


### <a name="BKMK_ServiceEndpointIdUnique"></a> ServiceEndpointIdUnique

|Property|Value|
|--------|-----|
|Description|Unique identifier of the service endpoint.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|serviceendpointidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_serviceendpoint_sdkmessageprocessingstep"></a> serviceendpoint_sdkmessageprocessingstep

Same as sdkmessageprocessingstep table [serviceendpoint_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_serviceendpoint_sdkmessageprocessingstep) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstep|
|ReferencingAttribute|eventhandler|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|serviceendpoint_sdkmessageprocessingstep|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [createdby_serviceendpoint](#BKMK_createdby_serviceendpoint)
- [lk_serviceendpointbase_modifiedonbehalfby](#BKMK_lk_serviceendpointbase_modifiedonbehalfby)
- [modifiedby_serviceendpoint](#BKMK_modifiedby_serviceendpoint)
- [organization_serviceendpoint](#BKMK_organization_serviceendpoint)
- [lk_serviceendpointbase_createdonbehalfby](#BKMK_lk_serviceendpointbase_createdonbehalfby)
- [keyvaultreference_ServiceEndpoint](#BKMK_keyvaultreference_ServiceEndpoint)


### <a name="BKMK_createdby_serviceendpoint"></a> createdby_serviceendpoint

See systemuser Table [createdby_serviceendpoint](systemuser.md#BKMK_createdby_serviceendpoint) One-To-Many relationship.

### <a name="BKMK_lk_serviceendpointbase_modifiedonbehalfby"></a> lk_serviceendpointbase_modifiedonbehalfby

See systemuser Table [lk_serviceendpointbase_modifiedonbehalfby](systemuser.md#BKMK_lk_serviceendpointbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_modifiedby_serviceendpoint"></a> modifiedby_serviceendpoint

See systemuser Table [modifiedby_serviceendpoint](systemuser.md#BKMK_modifiedby_serviceendpoint) One-To-Many relationship.

### <a name="BKMK_organization_serviceendpoint"></a> organization_serviceendpoint

See organization Table [organization_serviceendpoint](organization.md#BKMK_organization_serviceendpoint) One-To-Many relationship.

### <a name="BKMK_lk_serviceendpointbase_createdonbehalfby"></a> lk_serviceendpointbase_createdonbehalfby

See systemuser Table [lk_serviceendpointbase_createdonbehalfby](systemuser.md#BKMK_lk_serviceendpointbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_keyvaultreference_ServiceEndpoint"></a> keyvaultreference_ServiceEndpoint

**Added by**: ManagedIdentityExtensions Solution

See keyvaultreference Table [keyvaultreference_ServiceEndpoint](keyvaultreference.md#BKMK_keyvaultreference_ServiceEndpoint) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.serviceendpoint?text=serviceendpoint EntityType" />