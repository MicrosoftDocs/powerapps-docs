---
title: "TraceLog Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the TraceLog entity."

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
# TraceLog Entity Reference

A trace log.

## Entity Properties

**DisplayName**: Trace<br />
**DisplayCollectionName**: Traces<br />
**SchemaName**: TraceLog<br />
**CollectionSchemaName**: TraceLogs<br />
**LogicalName**: tracelog<br />
**LogicalCollectionName**: tracelogs<br />
**EntitySetName**: tracelogs<br />
**PrimaryIdAttribute**: tracelogid<br />
**PrimaryNameAttribute**: text<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CanBeDeleted](#BKMK_CanBeDeleted)
- [CollationLevel](#BKMK_CollationLevel)
- [ErrorDetails](#BKMK_ErrorDetails)
- [ErrorTypeDisplay](#BKMK_ErrorTypeDisplay)
- [IsUnique](#BKMK_IsUnique)
- [Level](#BKMK_Level)
- [MachineName](#BKMK_MachineName)
- [ParentTraceLogId](#BKMK_ParentTraceLogId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [Text](#BKMK_Text)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TraceActionXml](#BKMK_TraceActionXml)
- [TraceCode](#BKMK_TraceCode)
- [TraceDetailXml](#BKMK_TraceDetailXml)
- [TraceLogId](#BKMK_TraceLogId)
- [TraceParameterXml](#BKMK_TraceParameterXml)
- [TraceStatus](#BKMK_TraceStatus)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_CanBeDeleted"></a> CanBeDeleted

**Description**: Indicates if this trace log can be deleted.<br />
**DisplayName**: Trace CanBeDeleted Flag<br />
**LogicalName**: canbedeleted<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_CollationLevel"></a> CollationLevel

**Description**: Indicates the collation level<br />
**DisplayName**: Collation Level<br />
**LogicalName**: collationlevel<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_ErrorDetails"></a> ErrorDetails

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: errordetails<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2048


### <a name="BKMK_ErrorTypeDisplay"></a> ErrorTypeDisplay

**Description**: <br />
**DisplayName**: Trace Error Details<br />
**LogicalName**: errortypedisplay<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 320


### <a name="BKMK_IsUnique"></a> IsUnique

**Description**: Tells if this traceLog is created uniquely(only one) for the associated entity.<br />
**DisplayName**: Is Unique Trace<br />
**LogicalName**: isunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Level"></a> Level

**Description**: Information about the trace level.<br />
**DisplayName**: Level<br />
**LogicalName**: level<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Information
- **Value**: 2 **Label**: Warning
- **Value**: 3 **Label**: Error



### <a name="BKMK_MachineName"></a> MachineName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: machinename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 320


### <a name="BKMK_ParentTraceLogId"></a> ParentTraceLogId

**Description**: Indicates the parent ID of the trace log.<br />
**DisplayName**: Parent Id<br />
**LogicalName**: parenttracelogid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: tracelog


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Regarding mailbox or email server profile.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: emailserverprofile,mailbox


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: Type of the regarding object.<br />
**DisplayName**: Regarding Object Type<br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_Text"></a> Text

**Description**: Text of the trace.<br />
**DisplayName**: Text<br />
**LogicalName**: text<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: Time Zone Rule Version Number<br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_TraceActionXml"></a> TraceActionXml

**Description**: XML representation of the trace actions.<br />
**DisplayName**: Trace Actions XML<br />
**LogicalName**: traceactionxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_TraceCode"></a> TraceCode

**Description**: Error code.<br />
**DisplayName**: Error Code<br />
**LogicalName**: tracecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_TraceDetailXml"></a> TraceDetailXml

**Description**: XML representation of the trace details.<br />
**DisplayName**: Trace Detail XML<br />
**LogicalName**: tracedetailxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_TraceLogId"></a> TraceLogId

**Description**: Unique identifier of the trace.<br />
**DisplayName**: Trace<br />
**LogicalName**: tracelogid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TraceParameterXml"></a> TraceParameterXml

**Description**: XML representation of the trace parameters.<br />
**DisplayName**: Trace Parameter XML<br />
**LogicalName**: traceparameterxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_TraceStatus"></a> TraceStatus

**Description**: Status about the trace.<br />
**DisplayName**: Trace Status<br />
**LogicalName**: tracestatus<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Success
- **FalseOption Value**: 0 **Label**: Failure

**DefaultValue**: False


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

**Description**: Time zone code that was in use when the trace was created.<br />
**DisplayName**: UTC Conversion Time Zone Code<br />
**LogicalName**: utcconversiontimezonecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1

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
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [RegardingObjectOwnerId](#BKMK_RegardingObjectOwnerId)
- [RegardingObjectOwnerIdType](#BKMK_RegardingObjectOwnerIdType)
- [RegardingObjectOwningBusinessUnit](#BKMK_RegardingObjectOwningBusinessUnit)
- [TraceParameterHash](#BKMK_TraceParameterHash)
- [TraceRegardingId](#BKMK_TraceRegardingId)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the trace.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
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

**Description**: Time the error is created and logged.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the trace.<br />
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

**Description**: Unique identifier of the user who modified the trace.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
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

**Description**: Time the error is updated and logged for the same regarding object.<br />
**DisplayName**: Last Update On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the trace.<br />
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the trace.<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: organizationidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4000


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RegardingObjectOwnerId"></a> RegardingObjectOwnerId

**Description**: Unique identifier of the user or team who owns the regarding object.<br />
**DisplayName**: Owner<br />
**LogicalName**: regardingobjectownerid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_RegardingObjectOwnerIdType"></a> RegardingObjectOwnerIdType

**Description**: Owner type of the regarding object.<br />
**DisplayName**: Owner Type<br />
**LogicalName**: regardingobjectowneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_RegardingObjectOwningBusinessUnit"></a> RegardingObjectOwningBusinessUnit

**Description**: Unique identifier of the business unit that owns the regarding object.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: regardingobjectowningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_TraceParameterHash"></a> TraceParameterHash

**Description**: Stores the hash of the entity object associated with this tracelog. Hash is computed using the object type code and its id.<br />
**DisplayName**: Trace Parameter Hash<br />
**LogicalName**: traceparameterhash<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_TraceRegardingId"></a> TraceRegardingId

**Description**: For internal use only.<br />
**DisplayName**: Trace Regarding<br />
**LogicalName**: traceregardingid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: traceregarding

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_tracelog_parent_tracelog"></a> tracelog_parent_tracelog

Same as tracelog entity [tracelog_parent_tracelog](tracelog.md#BKMK_tracelog_parent_tracelog) Many-To-One relationship.

**ReferencingEntity**: tracelog<br />
**ReferencingAttribute**: parenttracelogid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: tracelog_parent_tracelog<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [tracelog_EmailServerProfile](#BKMK_tracelog_EmailServerProfile)
- [tracelog_Mailbox](#BKMK_tracelog_Mailbox)
- [organization_tracelog](#BKMK_organization_tracelog)
- [lk_tracelog_createdonbehalfby](#BKMK_lk_tracelog_createdonbehalfby)
- [lk_tracelog_modifiedby](#BKMK_lk_tracelog_modifiedby)
- [lk_tracelog_createdby](#BKMK_lk_tracelog_createdby)
- [tracelog_parent_tracelog](#BKMK_tracelog_parent_tracelog)
- [lk_tracelog_modifiedonbehalfby](#BKMK_lk_tracelog_modifiedonbehalfby)


### <a name="BKMK_tracelog_EmailServerProfile"></a> tracelog_EmailServerProfile

See emailserverprofile Entity [tracelog_EmailServerProfile](emailserverprofile.md#BKMK_tracelog_EmailServerProfile) One-To-Many relationship.

### <a name="BKMK_tracelog_Mailbox"></a> tracelog_Mailbox

See mailbox Entity [tracelog_Mailbox](mailbox.md#BKMK_tracelog_Mailbox) One-To-Many relationship.

### <a name="BKMK_organization_tracelog"></a> organization_tracelog

See organization Entity [organization_tracelog](organization.md#BKMK_organization_tracelog) One-To-Many relationship.

### <a name="BKMK_lk_tracelog_createdonbehalfby"></a> lk_tracelog_createdonbehalfby

See systemuser Entity [lk_tracelog_createdonbehalfby](systemuser.md#BKMK_lk_tracelog_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_tracelog_modifiedby"></a> lk_tracelog_modifiedby

See systemuser Entity [lk_tracelog_modifiedby](systemuser.md#BKMK_lk_tracelog_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_tracelog_createdby"></a> lk_tracelog_createdby

See systemuser Entity [lk_tracelog_createdby](systemuser.md#BKMK_lk_tracelog_createdby) One-To-Many relationship.

### <a name="BKMK_tracelog_parent_tracelog"></a> tracelog_parent_tracelog

See tracelog Entity [tracelog_parent_tracelog](tracelog.md#BKMK_tracelog_parent_tracelog) One-To-Many relationship.

### <a name="BKMK_lk_tracelog_modifiedonbehalfby"></a> lk_tracelog_modifiedonbehalfby

See systemuser Entity [lk_tracelog_modifiedonbehalfby](systemuser.md#BKMK_lk_tracelog_modifiedonbehalfby) One-To-Many relationship.
tracelog

