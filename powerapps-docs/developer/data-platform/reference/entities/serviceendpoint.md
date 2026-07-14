---
title: "Service Endpoint (ServiceEndpoint) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Service Endpoint (ServiceEndpoint) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Service Endpoint (ServiceEndpoint) table/entity reference (Microsoft Dataverse)

Service endpoint that can be contacted.

## Messages

The following table lists the messages for the Service Endpoint (ServiceEndpoint) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /serviceendpoints<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /serviceendpoints(*serviceendpointid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /serviceendpoints(*serviceendpointid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /serviceendpoints<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `TriggerServiceEndpointCheck`<br />Event: True |<xref:Microsoft.Dynamics.CRM.TriggerServiceEndpointCheck?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.TriggerServiceEndpointCheckRequest>|
| `Update`<br />Event: False |`PATCH` /serviceendpoints(*serviceendpointid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /serviceendpoints(*serviceendpointid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Service Endpoint (ServiceEndpoint) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Service Endpoint** |
| **DisplayCollectionName** | **Service Endpoints** |
| **SchemaName** | `ServiceEndpoint` |
| **CollectionSchemaName** | `ServiceEndpoints` |
| **EntitySetName** | `serviceendpoints`|
| **LogicalName** | `serviceendpoint` |
| **LogicalCollectionName** | `serviceendpoints` |
| **PrimaryIdAttribute** | `serviceendpointid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

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
- [ManagedIdentityId](#BKMK_ManagedIdentityId)
- [MessageCharset](#BKMK_MessageCharset)
- [MessageFormat](#BKMK_MessageFormat)
- [Name](#BKMK_Name)
- [NamespaceAddress](#BKMK_NamespaceAddress)
- [NamespaceFormat](#BKMK_NamespaceFormat)
- [Path](#BKMK_Path)
- [RuntimeIntegrationProperties](#BKMK_RuntimeIntegrationProperties)
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
|---|---|
|Description|**Specifies mode of authentication with SB**|
|DisplayName|**Specifies mode of authentication with SB**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`authtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`serviceendpoint_authtype`|

#### AuthType Choices/Options

|Value|Label|
|---|---|
|0|**Not Specified**|
|1|**ACS**|
|2|**SAS Key**|
|3|**SAS Token**|
|4|**Webhook Key**|
|5|**Http Header**|
|6|**Http Query String**|
|7|**Connection String**|
|8|**Access Key**|
|9|**Managed Identity**|

### <a name="BKMK_AuthValue"></a> AuthValue

|Property|Value|
|---|---|
|Description|**Authentication Value**|
|DisplayName|**Authentication Value**|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|`authvalue`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_ConnectionMode"></a> ConnectionMode

|Property|Value|
|---|---|
|Description|**Connection mode to contact the service endpoint.**|
|DisplayName|**Connection Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectionmode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`serviceendpoint_connectionmode`|

#### ConnectionMode Choices/Options

|Value|Label|
|---|---|
|1|**Normal**|
|2|**Federated**|

### <a name="BKMK_Contract"></a> Contract

|Property|Value|
|---|---|
|Description|**Type of the endpoint contract.**|
|DisplayName|**Contract**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contract`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`serviceendpoint_contract`|

#### Contract Choices/Options

|Value|Label|
|---|---|
|1|**OneWay**|
|2|**Queue**|
|3|**Rest**|
|4|**TwoWay**|
|5|**Topic**|
|6|**Queue (Persistent)**|
|7|**Event Hub**|
|8|**Webhook**|
|9|**Event Grid**|
|10|**Managed Data Lake**|
|11|**Container Storage**|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the service endpoint.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

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
|Description|**Information that specifies whether this component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_KeyVaultReferenceId"></a> KeyVaultReferenceId

|Property|Value|
|---|---|
|Description|**Unique identifier for keyvaultreference associated with serviceendpoint.**|
|DisplayName|**KeyVaultReferenceId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`keyvaultreferenceid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|keyvaultreference|

### <a name="BKMK_ManagedIdentityId"></a> ManagedIdentityId

|Property|Value|
|---|---|
|Description|**Unique identifier for managed identity associated with serviceendpoint.**|
|DisplayName|**ManagedIdentityId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`managedidentityid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|managedidentity|

### <a name="BKMK_MessageCharset"></a> MessageCharset

|Property|Value|
|---|---|
|Description|**Specifies the character encoding for message content**|
|DisplayName|**Specifies the character encoding to be used for messages sent to a service endpoint**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`messagecharset`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`serviceendpoint_messagecharset`|

#### MessageCharset Choices/Options

|Value|Label|
|---|---|
|0|**Default**|
|1|**UTF8**|
|2|**Windows1252**|

### <a name="BKMK_MessageFormat"></a> MessageFormat

|Property|Value|
|---|---|
|Description|**Content type of the message**|
|DisplayName|**Content type of the message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`messageformat`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`serviceendpoint_messageformat`|

#### MessageFormat Choices/Options

|Value|Label|
|---|---|
|1|**Binary XML**|
|2|**Json**|
|3|**Text XML**|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of Service end point.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_NamespaceAddress"></a> NamespaceAddress

|Property|Value|
|---|---|
|Description|**Full service endpoint address.**|
|DisplayName|**Namespace Address**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`namespaceaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_NamespaceFormat"></a> NamespaceFormat

|Property|Value|
|---|---|
|Description|**Format of Service Bus Namespace**|
|DisplayName|**Format of Service Bus Namespace**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`namespaceformat`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`serviceendpoint_namespaceformat`|

#### NamespaceFormat Choices/Options

|Value|Label|
|---|---|
|1|**Namespace Name**|
|2|**Namespace Address**|

### <a name="BKMK_Path"></a> Path

|Property|Value|
|---|---|
|Description|**Path to the service endpoint.**|
|DisplayName|**Path**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`path`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_RuntimeIntegrationProperties"></a> RuntimeIntegrationProperties

|Property|Value|
|---|---|
|Description|**For internal use only. Holds miscellaneous properties related to runtime integration.**|
|DisplayName|**Runtime Integration Properties**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`runtimeintegrationproperties`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|512|

### <a name="BKMK_SASKey"></a> SASKey

|Property|Value|
|---|---|
|Description|**Shared Access Key**|
|DisplayName|**Shared Access Key**|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|`saskey`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SASKeyName"></a> SASKeyName

|Property|Value|
|---|---|
|Description|**Shared Access Key Name**|
|DisplayName|**Shared Access Key Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`saskeyname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SASToken"></a> SASToken

|Property|Value|
|---|---|
|Description|**Shared Access Token**|
|DisplayName|**Shared Access Token**|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|`sastoken`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SchemaType"></a> SchemaType

|Property|Value|
|---|---|
|Description|**Specifies schema type for event grid events**|
|DisplayName|**Specifies schema type for event grid events**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`schematype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`serviceendpoint_schematype`|

#### SchemaType Choices/Options

|Value|Label|
|---|---|
|1|**Event Grid**|
|2|**Cloud Events**|

### <a name="BKMK_ServiceEndpointId"></a> ServiceEndpointId

|Property|Value|
|---|---|
|Description|**Unique identifier of the service endpoint.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`serviceendpointid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionNamespace"></a> SolutionNamespace

|Property|Value|
|---|---|
|Description|**Namespace of the App Fabric solution.**|
|DisplayName|**Service Namespace**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionnamespace`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_Url"></a> Url

|Property|Value|
|---|---|
|Description|**Full service endpoint Url.**|
|DisplayName|**Url Address**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`url`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_UseKeyVaultConfiguration"></a> UseKeyVaultConfiguration

|Property|Value|
|---|---|
|Description|**Use Auth Information in KeyVault**|
|DisplayName|**Use Auth Information in KeyVault**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`usekeyvaultconfiguration`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`serviceendpoint_usekeyvaultconfiguration`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_UserClaim"></a> UserClaim

|Property|Value|
|---|---|
|Description|**Additional user claim value type.**|
|DisplayName|**User Claim**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`userclaim`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`serviceendpoint_userclaim`|

#### UserClaim Choices/Options

|Value|Label|
|---|---|
|1|**None**|
|2|**UserId**|
|3|**UserInfo**|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsAuthValueSet](#BKMK_IsAuthValueSet)
- [IsManaged](#BKMK_IsManaged)
- [IsSASKeySet](#BKMK_IsSASKeySet)
- [IsSASTokenSet](#BKMK_IsSASTokenSet)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [ServiceEndpointIdUnique](#BKMK_ServiceEndpointIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)

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
|Description|**Unique identifier of the user who created the service endpoint.**|
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
|Description|**Date and time when the service endpoint was created.**|
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
|Description|**Unique identifier of the delegate user who created the service endpoint.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IsAuthValueSet"></a> IsAuthValueSet

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isauthvalueset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isencryptedattributevalueset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component is managed.**|
|DisplayName|**State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_IsSASKeySet"></a> IsSASKeySet

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`issaskeyset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isencryptedattributevalueset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsSASTokenSet"></a> IsSASTokenSet

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`issastokenset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isencryptedattributevalueset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the service endpoint.**|
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
|Description|**Date and time when the service endpoint was last modified.**|
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
|Description|**Unique identifier of the delegate user who modified the service endpoint.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization with which the service endpoint is associated.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

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

### <a name="BKMK_ServiceEndpointIdUnique"></a> ServiceEndpointIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the service endpoint.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`serviceendpointidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [createdby_serviceendpoint](#BKMK_createdby_serviceendpoint)
- [keyvaultreference_ServiceEndpoint](#BKMK_keyvaultreference_ServiceEndpoint)
- [lk_serviceendpointbase_createdonbehalfby](#BKMK_lk_serviceendpointbase_createdonbehalfby)
- [lk_serviceendpointbase_modifiedonbehalfby](#BKMK_lk_serviceendpointbase_modifiedonbehalfby)
- [managedidentity_ServiceEndpoint](#BKMK_managedidentity_ServiceEndpoint)
- [modifiedby_serviceendpoint](#BKMK_modifiedby_serviceendpoint)
- [organization_serviceendpoint](#BKMK_organization_serviceendpoint)

### <a name="BKMK_createdby_serviceendpoint"></a> createdby_serviceendpoint

One-To-Many Relationship: [systemuser createdby_serviceendpoint](systemuser.md#BKMK_createdby_serviceendpoint)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_keyvaultreference_ServiceEndpoint"></a> keyvaultreference_ServiceEndpoint

One-To-Many Relationship: [keyvaultreference keyvaultreference_ServiceEndpoint](keyvaultreference.md#BKMK_keyvaultreference_ServiceEndpoint)

|Property|Value|
|---|---|
|ReferencedEntity|`keyvaultreference`|
|ReferencedAttribute|`keyvaultreferenceid`|
|ReferencingAttribute|`keyvaultreferenceid`|
|ReferencingEntityNavigationPropertyName|`keyvaultreferenceid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_serviceendpointbase_createdonbehalfby"></a> lk_serviceendpointbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_serviceendpointbase_createdonbehalfby](systemuser.md#BKMK_lk_serviceendpointbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_serviceendpointbase_modifiedonbehalfby"></a> lk_serviceendpointbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_serviceendpointbase_modifiedonbehalfby](systemuser.md#BKMK_lk_serviceendpointbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_managedidentity_ServiceEndpoint"></a> managedidentity_ServiceEndpoint

One-To-Many Relationship: [managedidentity managedidentity_ServiceEndpoint](managedidentity.md#BKMK_managedidentity_ServiceEndpoint)

|Property|Value|
|---|---|
|ReferencedEntity|`managedidentity`|
|ReferencedAttribute|`managedidentityid`|
|ReferencingAttribute|`managedidentityid`|
|ReferencingEntityNavigationPropertyName|`managedidentityid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_modifiedby_serviceendpoint"></a> modifiedby_serviceendpoint

One-To-Many Relationship: [systemuser modifiedby_serviceendpoint](systemuser.md#BKMK_modifiedby_serviceendpoint)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_serviceendpoint"></a> organization_serviceendpoint

One-To-Many Relationship: [organization organization_serviceendpoint](organization.md#BKMK_organization_serviceendpoint)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_serviceendpoint_sdkmessageprocessingstep"></a> serviceendpoint_sdkmessageprocessingstep

Many-To-One Relationship: [sdkmessageprocessingstep serviceendpoint_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_serviceendpoint_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessageprocessingstep`|
|ReferencingAttribute|`eventhandler`|
|ReferencedEntityNavigationPropertyName|`serviceendpoint_sdkmessageprocessingstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.serviceendpoint?displayProperty=fullName>
