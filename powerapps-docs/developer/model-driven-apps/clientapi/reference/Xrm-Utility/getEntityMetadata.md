---
title: "getEntityMetadata (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getEntityMetadata method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getEntityMetadata (Client API)



[!INCLUDE[./includes/getEntityMetadata-description.md](./includes/getEntityMetadata-description.md)] 

## Syntax

`Xrm.Utility.getEntityMetadata(entityName,attributes).then(successCallback, errorCallback)`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|`entityName`|String|Yes|The logical name of the table.|
|`attributes`|Array of strings|No|The columns to get definitions for.|
|`successCallback`|function|No|A function to call when the table definitions are returned.|
|`errorCallback`|function|No|A function to call when the operation fails.|

## Returns

**Type**: Object

**Description**: An object containing the table definitions information with the following values.

|Name|Type|Description|
|---|---|---|
|`ActivityTypeMask`|Number|Whether a custom activity should appear in the activity menus in the Web application. `0` indicates that the custom activity doesn't appear; `1` indicates that it does appear.|
|`AutoRouteToOwnerQueue`|Boolean|Indicates whether to automatically move records to the owner's default queue when a record of this type is created or assigned.|
|`CanEnableSyncToExternalSearchIndex`|Boolean|For internal use only.|
|`CanTriggerWorkflow`|Boolean|Indicates whether the table can trigger a workflow process.|
|`Description`|String|Description for the table.|
|`DisplayCollectionName`|String|Plural display name for the table.|
|`DisplayName`|String|Display name for the table.|
|`EnforceStateTransitions`|Boolean|Indicates whether the table will enforce custom state transitions.|
|`EntityColor`|String|The hexadecimal code to represent the color to be used for this table in the application.|
|`EntitySetName`|String|The name of the Web API table set for this table.|
|`HasActivities`|Boolean|Indicates whether activities are associated with this table.|
|`IsActivity`|Boolean|Indicates whether the table is an activity.|
|`IsActivityParty`|Boolean|Indicates whether the email messages can be sent to an email address stored in a record of this type.|
|`IsBusinessProcessEnabled`|Boolean|Indicates whether the table is enabled for business process flows.|
|`IsBPFEntity`|Boolean|Indicates whether the table is a business process flow table.|
|`IsChildEntity`|Boolean|Indicates whether the table is a child table.|
|`IsConnectionsEnabled`|Boolean|Indicates whether connections are enabled for this table.|
|`IsCustomEntity`|Boolean|Indicates whether the table is a custom table.|
|`IsCustomizable`|Boolean|Indicates whether the table is customizable.|
|`IsDocumentManagementEnabled`|Boolean|Indicates whether document management is enabled.|
|`IsDocumentRecommendationsEnabled`|Boolean|Indicates whether the document recommendations is enabled.|
|`IsDuplicateDetectionEnabled`|Boolean|Indicates whether duplicate detection is enabled.|
|`IsEnabledForCharts`|Boolean|Indicates whether charts are enabled.|
|`IsImportable`|Boolean|Indicates whether the table can be imported using the Import Wizard.|
|`IsInteractionCentricEnabled`|Boolean|Indicates the table is enabled for interactive experience.|
|`IsKnowledgeManagementEnabled`|Boolean|Indicates whether knowledge management is enabled for the table.|
|`IsMailMergeEnabled`|Boolean|Indicates whether mail merge is enabled for this table.|
|`IsManaged`|Boolean|Indicates whether the table is part of a managed solution.|
|`IsOneNoteIntegrationEnabled`|Boolean|Indicates whether OneNote integration is enabled for the table.|
|`IsOptimisticConcurrencyEnabled`|Boolean|Indicates whether optimistic concurrency is enabled for the table.|
|`IsQuickCreateEnabled`|Boolean|Indicates whether the table is enabled for quick create forms.|
|`IsStateModelAware`|Boolean|Indicates whether the table supports setting custom state transitions.|
|`IsValidForAdvancedFind`|Boolean|Indicates whether the table is will be shown in Advanced Find.|
|`IsVisibleInMobileClient`|Boolean|Indicates whether Microsoft Dynamics 365 for tablets users can see data for this table.|
|`IsEnabledInUnifiedInterface`|Boolean|Indicates whether the table is enabled for Unified Interface.|
|`LogicalCollectionName`|String|The logical collection name.|
|`LogicalName`|String|The logical name for the table.|
|`ObjectTypeCode`|Number|The table type code.|
|`OwnershipType`|String|The ownership type for the table: `UserOwned` or `OrganizationOwned`.|
|`PrimaryIdAttribute`|String|The name of the column that is the primary id for the table.|
|`PrimaryImageAttribute`|String|The name of the primary image column for a table.|
|`PrimaryNameAttribute`|String|The name of the primary column for a table.|
|`Privileges`|Array of objects|Objects that define the security privilege for access to a table. See [Privilege object](#privilege-object)|
|`Attributes`|Collection|A collection of column definitions objects. See [Attribute objects](#attribute-objects)|

### Privilege object

Privilege objects have the following properties to define the security privilege for access to a table:

|Name|Type|Description|
|---|---|---|
|`CanBeBasic`|Boolean|Whether the privilege can be basic access level.|
|`CanBeDeep`|Boolean|Whether the privilege can be deep access level.|
|`CanBeEntityReference`|Boolean|Whether the privilege for an external party can be basic access level.|
|`CanBeGlobal`|Boolean|Whether the privilege can be global access level.|
|`CanBeLocal`|Boolean|Whether the privilege can be local access level.|
|`CanBeParentEntityReference`|Boolean|Whether the privilege for an external party can be parent access level.|
|`Name`|String|The name of the privilege.|
|`PrivilegeId`|String|The ID of the privilege.|
|`PrivilegeType`|Number|The type of privilege, which is one of the following:<br />0 : None<br />1 : Create<br />2 : Read<br />3 : Write<br />4 : Delete<br />5 : Assign<br />6 : Share<br />7 : Append<br />8 : AppendTo|

### Attribute objects

The object returned depends on the type of column definitions.

#### Base (AttributeMetadata) columns

All column definitions have these shared properties:

|Name|Type|Description|
|---|---|---|
|`AttributeType`|Number|Type of a column. For a list of column type values, see [AttributeTypeCode Enum](xref:Microsoft.Xrm.Sdk.Metadata.AttributeTypeCode) |
|`DisplayName`|String|Display name for the column|
|`EntityLogicalName`|String|Logical name of the table that contains the column.|
|`LogicalName`|String|Logical name for the column.|

#### Yes/No (BooleanAttributeMetadata) columns

Yes/No columns have these properties:

|Name|Type|Description|
|---|---|---|
|`DefaultFormValue`|Boolean|Default value for a Yes/No column.|
|`OptionSet`|Object|Options for the boolean column where each option is a key:value pair.|

#### Choice (PicklistAttributeMetadata) columns

Choice columns have this property:

|Name|Type|Description|
|---|---|---|
|`OptionSet`|Object|Options for the column where each option is a key:value pair.|

#### Choices (MultiSelectPicklistAttributeMetadata ) columns

Choices columns have these properties:

|Name|Type|Description|
|---|---|---|
|`DefaultFormValue`|Boolean|Default value for the column.|
|`OptionSet`|Object|Options for the boolean column where each option is a key:value pair.|

#### State (StateAttributeMetadata) columns

State columns have this property:

|Name|Type|Description|
|---|---|---|
|`OptionSet`|Object|Options for the column where each option is a key:value pair.|

State columns also have these methods that accept the value of one of the `OptionSet` option values as the `arg` parameter.

|Name|Return Type|Description|
|---|---|---|
|`getDefaultStatus(arg)`|Number|Returns the default status (number) based on the passed in state value for a table. For default state and status values for a table, see table definitions information of the table in [Dataverse table/entity reference](../../../../data-platform/reference/about-entity-reference.md).|
|`getStatusValuesForState(arg)`|Array of numbers|Returns possible status values (array of numbers) for a specified state value. For state and status values for a table, see table definitions information of the table in [Dataverse table/entity reference](../../../../data-platform/reference/about-entity-reference.md).|


#### Status (StatusAttributeMetadata) columns

Status columns have this property:

|Name|Type|Description|
|---|---|---|
|`OptionSet`|Object|Options for the column where each option is a key:value pair.|

Status columns also have this method that accepts the value of one of the `OptionSet` option values as the `arg` parameter.

|Name|Return Type|Description|
|---|---|---|
|`getState(arg)`|Number|Returns the state value (number) for the specified status value (number). For default state and status values for a table, see table definitions information of the table in  [Dataverse table/entity reference](../../../../data-platform/reference/about-entity-reference.md).|



### Related articles

[Xrm.Utility](../xrm-utility.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
