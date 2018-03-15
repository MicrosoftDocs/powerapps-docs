---
title: "ImportLog Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the ImportLog entity."

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
---
# ImportLog Entity Reference

Failure reason and other detailed information for a record that failed to import.

## Entity Properties

**DisplayName**: Import Log<br />
**DisplayCollectionName**: ImportLogs<br />
**SchemaName**: ImportLog<br />
**CollectionSchemaName**: ImportLogs<br />
**LogicalName**: importlog<br />
**LogicalCollectionName**: importlogs<br />
**EntitySetName**: importlogs<br />
**PrimaryIdAttribute**: importlogid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdditionalInfo](#BKMK_AdditionalInfo)
- [ColumnValue](#BKMK_ColumnValue)
- [ErrorDescription](#BKMK_ErrorDescription)
- [ErrorNumber](#BKMK_ErrorNumber)
- [HeaderColumn](#BKMK_HeaderColumn)
- [ImportDataId](#BKMK_ImportDataId)
- [ImportFileId](#BKMK_ImportFileId)
- [ImportLogId](#BKMK_ImportLogId)
- [LineNumber](#BKMK_LineNumber)
- [LogPhaseCode](#BKMK_LogPhaseCode)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [StatusCode](#BKMK_StatusCode)


### <a name="BKMK_AdditionalInfo"></a> AdditionalInfo

**Description**: Additional information related to the error.<br />
**DisplayName**: More Information<br />
**LogicalName**: additionalinfo<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 5000


### <a name="BKMK_ColumnValue"></a> ColumnValue

**Description**: Value in the column.<br />
**DisplayName**: Column Value<br />
**LogicalName**: columnvalue<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_ErrorDescription"></a> ErrorDescription

**Description**: Description of an error.<br />
**DisplayName**: Description<br />
**LogicalName**: errordescription<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 512


### <a name="BKMK_ErrorNumber"></a> ErrorNumber

**Description**: Error code of an error.<br />
**DisplayName**: Error Code<br />
**LogicalName**: errornumber<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 10000000<br />
**MinValue**: 0


### <a name="BKMK_HeaderColumn"></a> HeaderColumn

**Description**: Name of the column heading.<br />
**DisplayName**: Column Heading<br />
**LogicalName**: headercolumn<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ImportDataId"></a> ImportDataId

**Description**: Unique identifier of the import data for this import log.<br />
**DisplayName**: Source Row<br />
**LogicalName**: importdataid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: importdata


### <a name="BKMK_ImportFileId"></a> ImportFileId

**Description**: Unique identifier of the import file for this import log.<br />
**DisplayName**: Import File Id<br />
**LogicalName**: importfileid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: importfile


### <a name="BKMK_ImportLogId"></a> ImportLogId

**Description**: Unique identifier of the import log.<br />
**DisplayName**: <br />
**LogicalName**: importlogid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_LineNumber"></a> LineNumber

**Description**: Original line number of the data used in this log.<br />
**DisplayName**: Original Row Number<br />
**LogicalName**: linenumber<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 10000000<br />
**MinValue**: 0


### <a name="BKMK_LogPhaseCode"></a> LogPhaseCode

**Description**: Phase for which the log is recorded.<br />
**DisplayName**: Log Phase<br />
**LogicalName**: logphasecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Parse
- **Value**: 1 **Label**: Transform
- **Value**: 2 **Label**: Import Create
- **Value**: 3 **Label**: Import Update



### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the import log.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Reason for the status of the import log.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Status<br />
**Options**:

- **Value**: 0 **Label**: Active **State**: 0


<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ImportDataIdName](#BKMK_ImportDataIdName)
- [ImportFileIdName](#BKMK_ImportFileIdName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SequenceNumber](#BKMK_SequenceNumber)
- [StateCode](#BKMK_StateCode)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the import log.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
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

**Description**: Date and time when the import log was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the importlog.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: False<br />
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


### <a name="BKMK_ImportDataIdName"></a> ImportDataIdName

**Description**: Name of the import data.<br />
**DisplayName**: <br />
**LogicalName**: importdataidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ImportFileIdName"></a> ImportFileIdName

**Description**: Name of the import file.<br />
**DisplayName**: <br />
**LogicalName**: importfileidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the import log.<br />
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

**Description**: Date and time when the import log was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the importlog.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: False<br />
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Business unit that owns the import log.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the import log.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the import log.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_SequenceNumber"></a> SequenceNumber

**Description**: Sequence number of the error in this log.<br />
**DisplayName**: Sequence Number<br />
**LogicalName**: sequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 10000000<br />
**MinValue**: 0


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the import log.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 0 **InvariantName**: Active


<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [userentityinstancedata_importlog](#BKMK_userentityinstancedata_importlog)
- [ImportLog_BulkDeleteFailures](#BKMK_ImportLog_BulkDeleteFailures)
- [ImportLog_AsyncOperations](#BKMK_ImportLog_AsyncOperations)


### <a name="BKMK_userentityinstancedata_importlog"></a> userentityinstancedata_importlog

Same as userentityinstancedata entity [userentityinstancedata_importlog](userentityinstancedata.md#BKMK_userentityinstancedata_importlog) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_importlog<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ImportLog_BulkDeleteFailures"></a> ImportLog_BulkDeleteFailures

Same as bulkdeletefailure entity [ImportLog_BulkDeleteFailures](bulkdeletefailure.md#BKMK_ImportLog_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ImportLog_BulkDeleteFailures<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ImportLog_AsyncOperations"></a> ImportLog_AsyncOperations

Same as asyncoperation entity [ImportLog_AsyncOperations](asyncoperation.md#BKMK_ImportLog_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ImportLog_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_importlog_createdonbehalfby](#BKMK_lk_importlog_createdonbehalfby)
- [BusinessUnit_ImportLogs](#BKMK_BusinessUnit_ImportLogs)
- [SystemUser_ImportLogs](#BKMK_SystemUser_ImportLogs)
- [lk_importlogbase_modifiedby](#BKMK_lk_importlogbase_modifiedby)
- [lk_importlogbase_createdby](#BKMK_lk_importlogbase_createdby)
- [ImportLog_ImportFile](#BKMK_ImportLog_ImportFile)
- [team_ImportLogs](#BKMK_team_ImportLogs)
- [lk_importlog_modifiedonbehalfby](#BKMK_lk_importlog_modifiedonbehalfby)


### <a name="BKMK_lk_importlog_createdonbehalfby"></a> lk_importlog_createdonbehalfby

See systemuser Entity [lk_importlog_createdonbehalfby](systemuser.md#BKMK_lk_importlog_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_ImportLogs"></a> BusinessUnit_ImportLogs

See businessunit Entity [BusinessUnit_ImportLogs](businessunit.md#BKMK_BusinessUnit_ImportLogs) One-To-Many relationship.

### <a name="BKMK_SystemUser_ImportLogs"></a> SystemUser_ImportLogs

See systemuser Entity [SystemUser_ImportLogs](systemuser.md#BKMK_SystemUser_ImportLogs) One-To-Many relationship.

### <a name="BKMK_lk_importlogbase_modifiedby"></a> lk_importlogbase_modifiedby

See systemuser Entity [lk_importlogbase_modifiedby](systemuser.md#BKMK_lk_importlogbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_importlogbase_createdby"></a> lk_importlogbase_createdby

See systemuser Entity [lk_importlogbase_createdby](systemuser.md#BKMK_lk_importlogbase_createdby) One-To-Many relationship.

### <a name="BKMK_ImportLog_ImportFile"></a> ImportLog_ImportFile

See importfile Entity [ImportLog_ImportFile](importfile.md#BKMK_ImportLog_ImportFile) One-To-Many relationship.

### <a name="BKMK_team_ImportLogs"></a> team_ImportLogs

See team Entity [team_ImportLogs](team.md#BKMK_team_ImportLogs) One-To-Many relationship.

### <a name="BKMK_lk_importlog_modifiedonbehalfby"></a> lk_importlog_modifiedonbehalfby

See systemuser Entity [lk_importlog_modifiedonbehalfby](systemuser.md#BKMK_lk_importlog_modifiedonbehalfby) One-To-Many relationship.
importlog

