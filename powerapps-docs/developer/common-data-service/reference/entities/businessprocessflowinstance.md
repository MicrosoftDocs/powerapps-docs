---
title: "BusinessProcessFlowInstance Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the BusinessProcessFlowInstance entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# BusinessProcessFlowInstance Entity Reference

Active path associated with every Business Process Flow instance

## Entity Properties

**DisplayName**: Business Process Flow Instance<br />
**DisplayCollectionName**: Business Process Flow Instances<br />
**SchemaName**: BusinessProcessFlowInstance<br />
**CollectionSchemaName**: BusinessProcessFlowInstances<br />
**LogicalName**: businessprocessflowinstance<br />
**LogicalCollectionName**: businessprocessflowinstances<br />
**EntitySetName**: businessprocessflowinstances<br />
**PrimaryIdAttribute**: businessprocessflowinstanceid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [BusinessProcessFlowInstanceId](#BKMK_BusinessProcessFlowInstanceId)
- [Entity1Id](#BKMK_Entity1Id)
- [Entity1ObjectTypeCode](#BKMK_Entity1ObjectTypeCode)
- [Entity2Id](#BKMK_Entity2Id)
- [Entity2ObjectTypeCode](#BKMK_Entity2ObjectTypeCode)
- [Entity3Id](#BKMK_Entity3Id)
- [Entity3ObjectTypeCode](#BKMK_Entity3ObjectTypeCode)
- [Entity4Id](#BKMK_Entity4Id)
- [Entity4ObjectTypeCode](#BKMK_Entity4ObjectTypeCode)
- [Entity5Id](#BKMK_Entity5Id)
- [Entity5ObjectTypeCode](#BKMK_Entity5ObjectTypeCode)
- [Name](#BKMK_Name)
- [ProcessId](#BKMK_ProcessId)
- [ProcessStageId](#BKMK_ProcessStageId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TraversedPath](#BKMK_TraversedPath)


### <a name="BKMK_BusinessProcessFlowInstanceId"></a> BusinessProcessFlowInstanceId

**Description**: Unique identifier of the business process flow instance.<br />
**DisplayName**: Process Instance ID<br />
**LogicalName**: businessprocessflowinstanceid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Entity1Id"></a> Entity1Id

**Description**: Unique identifier of the first entity instance.<br />
**DisplayName**: Entity 1 ID<br />
**LogicalName**: entity1id<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Entity1ObjectTypeCode"></a> Entity1ObjectTypeCode

**Description**: Object type code for the first entity of the business process flow instance.<br />
**DisplayName**: Entity1ObjectTypeCode<br />
**LogicalName**: entity1objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_Entity2Id"></a> Entity2Id

**Description**: Unique identifier of the second entity instance.<br />
**DisplayName**: Entity 2 ID<br />
**LogicalName**: entity2id<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Entity2ObjectTypeCode"></a> Entity2ObjectTypeCode

**Description**: Object type code for the second entity of the business process flow instance.<br />
**DisplayName**: Entity2ObjectTypeCode<br />
**LogicalName**: entity2objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_Entity3Id"></a> Entity3Id

**Description**: Unique identifier of the third entity instance.<br />
**DisplayName**: Entity 3 ID<br />
**LogicalName**: entity3id<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Entity3ObjectTypeCode"></a> Entity3ObjectTypeCode

**Description**: Object type code for the third entity of the business process flow instance.<br />
**DisplayName**: Entity3ObjectTypeCode<br />
**LogicalName**: entity3objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_Entity4Id"></a> Entity4Id

**Description**: Unique identifier of the fourth entity instance.<br />
**DisplayName**: Entity 4 Id<br />
**LogicalName**: entity4id<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Entity4ObjectTypeCode"></a> Entity4ObjectTypeCode

**Description**: Object type code for the fourth entity of the business process flow instance.<br />
**DisplayName**: Entity4ObjectTypeCode<br />
**LogicalName**: entity4objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_Entity5Id"></a> Entity5Id

**Description**: Unique identifier of the fifth entity instance.<br />
**DisplayName**: Entity 5 ID<br />
**LogicalName**: entity5id<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Entity5ObjectTypeCode"></a> Entity5ObjectTypeCode

**Description**: Object type code for the fifth entity of the business process flow instance.<br />
**DisplayName**: Entity5ObjectTypeCode<br />
**LogicalName**: entity5objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_Name"></a> Name

**Description**: Type a descriptive name for the instance.<br />
**DisplayName**: Instance Name<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_ProcessId"></a> ProcessId

**Description**: Unique identifier of the business process flow.<br />
**DisplayName**: Process<br />
**LogicalName**: processid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: workflow


### <a name="BKMK_ProcessStageId"></a> ProcessStageId

**Description**: Unique identifier of active stage in the business process flow instance.<br />
**DisplayName**: Active Stage ID<br />
**LogicalName**: processstageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the business process flow instance is active or inactive.<br />
**DisplayName**: State<br />
**LogicalName**: statecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 1 **InvariantName**: Active
- **Value**: 1 **Label**: Inactive **DefaultStatus**: 2 **InvariantName**: Inactive



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Business process flow instance's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Active **State**: 0
- **Value**: 2 **Label**: Finished **State**: 1
- **Value**: 3 **Label**: Aborted **State**: 1



### <a name="BKMK_TraversedPath"></a> TraversedPath

**Description**: For internal use only.<br />
**DisplayName**: Active Path<br />
**LogicalName**: traversedpath<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1250

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ActiveStageStartedOn](#BKMK_ActiveStageStartedOn)
- [CompletedOn](#BKMK_CompletedOn)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ActiveStageStartedOn"></a> ActiveStageStartedOn

**Description**: Date and time when the active stage was started.<br />
**DisplayName**: Active Stage Started On<br />
**LogicalName**: activestagestartedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CompletedOn"></a> CompletedOn

**Description**: Date and time when the process completed.<br />
**DisplayName**: Completed On<br />
**LogicalName**: completedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Shows who created the record.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows who last updated the record.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the business process flow instance.<br />
**DisplayName**: Version Number<br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_businessprocessflowinstancebase_modifiedonbehalfby](#BKMK_lk_businessprocessflowinstancebase_modifiedonbehalfby)
- [lk_businessprocessflowinstancebase_createdonbehalfby](#BKMK_lk_businessprocessflowinstancebase_createdonbehalfby)
- [lk_businessprocessflowinstancebase_createdby](#BKMK_lk_businessprocessflowinstancebase_createdby)
- [lk_businessprocessflowinstancebase_modifiedby](#BKMK_lk_businessprocessflowinstancebase_modifiedby)


### <a name="BKMK_lk_businessprocessflowinstancebase_modifiedonbehalfby"></a> lk_businessprocessflowinstancebase_modifiedonbehalfby

See systemuser Entity [lk_businessprocessflowinstancebase_modifiedonbehalfby](systemuser.md#BKMK_lk_businessprocessflowinstancebase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_businessprocessflowinstancebase_createdonbehalfby"></a> lk_businessprocessflowinstancebase_createdonbehalfby

See systemuser Entity [lk_businessprocessflowinstancebase_createdonbehalfby](systemuser.md#BKMK_lk_businessprocessflowinstancebase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_businessprocessflowinstancebase_createdby"></a> lk_businessprocessflowinstancebase_createdby

See systemuser Entity [lk_businessprocessflowinstancebase_createdby](systemuser.md#BKMK_lk_businessprocessflowinstancebase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_businessprocessflowinstancebase_modifiedby"></a> lk_businessprocessflowinstancebase_modifiedby

See systemuser Entity [lk_businessprocessflowinstancebase_modifiedby](systemuser.md#BKMK_lk_businessprocessflowinstancebase_modifiedby) One-To-Many relationship.
businessprocessflowinstance

