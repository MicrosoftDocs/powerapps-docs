---
title: "CallbackRegistration Entity Reference (Common Data Service)| MicrosoftDocs"
description: "Includes schema information and supported messages for the CallbackRegistration entity in Common Data Service."
ms.date: 11/07/2019
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
---
# CallbackRegistration Entity Reference

Callback Registration that stores configuration.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/callbackregistrations<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/callbackregistrations(*callbackregistrationid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/callbackregistrations(*callbackregistrationid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/callbackregistrations<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/callbackregistrations(*callbackregistrationid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Entity Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|CallbackRegistrations|
|DisplayCollectionName|Callback Registrations|
|DisplayName|Callback Registration|
|EntitySetName|callbackregistrations|
|IsBPFEntity|False|
|LogicalCollectionName|callbackregistrations|
|LogicalName|callbackregistration|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|callbackregistrationid|
|PrimaryNameAttribute|name|
|SchemaName|CallbackRegistration|

<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CallbackRegistrationId](#BKMK_CallbackRegistrationId)
- [EntityName](#BKMK_EntityName)
- [FilterExpression](#BKMK_FilterExpression)
- [FilteringAttributes](#BKMK_FilteringAttributes)
- [Message](#BKMK_Message)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PostponeUntil](#BKMK_PostponeUntil)
- [Scope](#BKMK_Scope)
- [Url](#BKMK_Url)
- [Version](#BKMK_Version)


### <a name="BKMK_CallbackRegistrationId"></a> CallbackRegistrationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the callback registration.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|callbackregistrationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_EntityName"></a> EntityName

|Property|Value|
|--------|-----|
|Description|Entity Name.|
|DisplayName|Entity Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|entityname|
|MaxLength|255|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_FilterExpression"></a> FilterExpression

|Property|Value|
|--------|-----|
|Description|condition represented with OData $filter syntax|
|DisplayName|Filter Expression|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|filterexpression|
|MaxLength|100000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FilteringAttributes"></a> FilteringAttributes

|Property|Value|
|--------|-----|
|Description|Comma-separated list of attributes. If at least one of these attributes is modified, the callback url should be called.|
|DisplayName|Filtering Attributes|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|filteringattributes|
|MaxLength|100000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Message"></a> Message

|Property|Value|
|--------|-----|
|Description|Specifies the message type|
|DisplayName|Specifies the message type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|message|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Message Options

|Value|Label|
|-----|-----|
|1|Create|
|2|Delete|
|3|Update|
|4|Create or Update|
|5|Create or Delete|
|6|Update or Delete|
|7|Create or Update or Delete|



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of callback registration.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the callback registration.|
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


### <a name="BKMK_PostponeUntil"></a> PostponeUntil

|Property|Value|
|--------|-----|
|Description|delay represented with OData expression|
|DisplayName|Postpone Until|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|postponeuntil|
|MaxLength|100000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Scope"></a> Scope

|Property|Value|
|--------|-----|
|Description|Specifies the Scope|
|DisplayName|Specifies the scope type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|scope|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Scope Options

|Value|Label|
|-----|-----|
|1|User|
|2|BusinessUnit|
|3|ParentChildBusinessUnit|
|4|Organization|



### <a name="BKMK_Url"></a> Url

|Property|Value|
|--------|-----|
|Description|Full callback registration Url.|
|DisplayName|Url Address|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|url|
|MaxLength|2000|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_Version"></a> Version

|Property|Value|
|--------|-----|
|Description|Specifies the Callback registration version type|
|DisplayName|Specifies the Callback registration version type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|version|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Version Options

|Value|Label|
|-----|-----|
|1|V1|


<a name="read-only-attributes"></a>

## Read-only attributes

These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
|DisplayName|Created By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

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


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the callback registration was created.|
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
|Description|Shows who created the record on behalfÂ of another user.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|False|
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
|DisplayName|Modified By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

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


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the callback registration was last modified.|
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
|Description|Shows who last updated the record on behalf of another user.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
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
|Description|Unique identifier of the business unit that owns the callback registration.|
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
|Description|Unique identifier of the team who owns the callback registration.|
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
|Description|Unique identifier of the user who owns the callback registration.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_callbackregistration_modifiedonbehalfby](#BKMK_lk_callbackregistration_modifiedonbehalfby)
- [lk_callbackregistration_modifiedby](#BKMK_lk_callbackregistration_modifiedby)
- [lk_callbackregistration_createdby](#BKMK_lk_callbackregistration_createdby)
- [businessunit_callbackregistration](#BKMK_businessunit_callbackregistration)
- [lk_callbackregistration_createdonbehalfby](#BKMK_lk_callbackregistration_createdonbehalfby)


### <a name="BKMK_lk_callbackregistration_modifiedonbehalfby"></a> lk_callbackregistration_modifiedonbehalfby

See systemuser Entity [lk_callbackregistration_modifiedonbehalfby](systemuser.md#BKMK_lk_callbackregistration_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_callbackregistration_modifiedby"></a> lk_callbackregistration_modifiedby

See systemuser Entity [lk_callbackregistration_modifiedby](systemuser.md#BKMK_lk_callbackregistration_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_callbackregistration_createdby"></a> lk_callbackregistration_createdby

See systemuser Entity [lk_callbackregistration_createdby](systemuser.md#BKMK_lk_callbackregistration_createdby) One-To-Many relationship.

### <a name="BKMK_businessunit_callbackregistration"></a> businessunit_callbackregistration

See businessunit Entity [businessunit_callbackregistration](businessunit.md#BKMK_businessunit_callbackregistration) One-To-Many relationship.

### <a name="BKMK_lk_callbackregistration_createdonbehalfby"></a> lk_callbackregistration_createdonbehalfby

See systemuser Entity [lk_callbackregistration_createdonbehalfby](systemuser.md#BKMK_lk_callbackregistration_createdonbehalfby) One-To-Many relationship.

### See also

[About the Entity Reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.callbackregistration?text=callbackregistration EntityType" />