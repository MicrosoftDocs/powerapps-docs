---
title: "ImportData table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the ImportData table/entity."
ms.date: 03/04/2021
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

# ImportData table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Unprocessed data from imported files.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|ImportDatas|
|DisplayCollectionName|Import Data|
|DisplayName|Import Data|
|EntitySetName|importdataset|
|IsBPFEntity|False|
|LogicalCollectionName|importdatas|
|LogicalName|importdata|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|importdataid|
|PrimaryNameAttribute|data|
|SchemaName|ImportData|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Data](#BKMK_Data)
- [ErrorType](#BKMK_ErrorType)
- [HasError](#BKMK_HasError)
- [ImportDataId](#BKMK_ImportDataId)
- [ImportFileId](#BKMK_ImportFileId)
- [LineNumber](#BKMK_LineNumber)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [RecordId](#BKMK_RecordId)
- [StatusCode](#BKMK_StatusCode)


### <a name="BKMK_Data"></a> Data

|Property|Value|
|--------|-----|
|Description|Data row of the import file.|
|DisplayName|Data|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|data|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ErrorType"></a> ErrorType

|Property|Value|
|--------|-----|
|Description|Type of the import error.|
|DisplayName|Error Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|errortype|
|RequiredLevel|None|
|Type|Picklist|

#### ErrorType Choices/Options

|Value|Label|
|-----|-----|
|0|Create|
|1|Update|



### <a name="BKMK_HasError"></a> HasError

|Property|Value|
|--------|-----|
|Description|Information about whether this import data has an error.|
|DisplayName|Has Error|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|haserror|
|RequiredLevel|None|
|Type|Boolean|

#### HasError Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_ImportDataId"></a> ImportDataId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the import data.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importdataid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ImportFileId"></a> ImportFileId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the import file for this import data.|
|DisplayName|Import File Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|importfileid|
|RequiredLevel|None|
|Targets|importfile|
|Type|Lookup|


### <a name="BKMK_LineNumber"></a> LineNumber

|Property|Value|
|--------|-----|
|Description|Original line number of the data present in the file.|
|DisplayName|Line Number|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|linenumber|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the import data.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_RecordId"></a> RecordId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the record.|
|DisplayName|Record|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|recordid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the import data.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|SystemRequired|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|0|Active|0|


<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
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
- [StateCode](#BKMK_StateCode)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the import data.|
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


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the import data was created.|
|DisplayName||
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the importdata.|
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


### <a name="BKMK_ImportFileIdName"></a> ImportFileIdName

|Property|Value|
|--------|-----|
|Description|Name of the import file.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|importfileidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the import data.|
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


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the import data was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the importdata.|
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


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|--------|-----|
|Description||
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

|Property|Value|
|--------|-----|
|Description|Business unit that owns the import data.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the import data.|
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
|Description|Unique identifier of the user who owns the import data.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Status of the import data.|
|DisplayName|Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|0|Active|


<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [ImportLog_ImportData](#BKMK_ImportLog_ImportData)
- [ImportData_AsyncOperations](#BKMK_ImportData_AsyncOperations)
- [ImportData_BulkDeleteFailures](#BKMK_ImportData_BulkDeleteFailures)


### <a name="BKMK_ImportLog_ImportData"></a> ImportLog_ImportData

Same as importlog table [ImportLog_ImportData](importlog.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importlog|
|ReferencingAttribute|importdataid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|ImportLog_ImportData|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_ImportData_AsyncOperations"></a> ImportData_AsyncOperations

Same as asyncoperation table [ImportData_AsyncOperations](asyncoperation.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|ImportData_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_ImportData_BulkDeleteFailures"></a> ImportData_BulkDeleteFailures

Same as bulkdeletefailure table [ImportData_BulkDeleteFailures](bulkdeletefailure.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|ImportData_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_importdatabase_modifiedby](#BKMK_lk_importdatabase_modifiedby)
- [BusinessUnit_ImportData](#BKMK_BusinessUnit_ImportData)
- [lk_importdata_modifiedonbehalfby](#BKMK_lk_importdata_modifiedonbehalfby)
- [lk_importdatabase_createdby](#BKMK_lk_importdatabase_createdby)
- [lk_importdata_createdonbehalfby](#BKMK_lk_importdata_createdonbehalfby)
- [team_ImportData](#BKMK_team_ImportData)
- [SystemUser_ImportData](#BKMK_SystemUser_ImportData)
- [owner_importdatas](#BKMK_owner_importdatas)
- [ImportFile_ImportData](#BKMK_ImportFile_ImportData)


### <a name="BKMK_lk_importdatabase_modifiedby"></a> lk_importdatabase_modifiedby

See systemuser Table [lk_importdatabase_modifiedby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_ImportData"></a> BusinessUnit_ImportData

See businessunit Table [BusinessUnit_ImportData](businessunit.md) One-To-Many relationship.

### <a name="BKMK_lk_importdata_modifiedonbehalfby"></a> lk_importdata_modifiedonbehalfby

See systemuser Table [lk_importdata_modifiedonbehalfby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_lk_importdatabase_createdby"></a> lk_importdatabase_createdby

See systemuser Table [lk_importdatabase_createdby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_lk_importdata_createdonbehalfby"></a> lk_importdata_createdonbehalfby

See systemuser Table [lk_importdata_createdonbehalfby](systemuser.md) One-To-Many relationship.

### <a name="BKMK_team_ImportData"></a> team_ImportData

See team Table [team_ImportData](team.md) One-To-Many relationship.

### <a name="BKMK_SystemUser_ImportData"></a> SystemUser_ImportData

See systemuser Table [SystemUser_ImportData](systemuser.md) One-To-Many relationship.

### <a name="BKMK_owner_importdatas"></a> owner_importdatas

See owner Table [owner_importdatas](owner.md) One-To-Many relationship.

### <a name="BKMK_ImportFile_ImportData"></a> ImportFile_ImportData

See importfile Table [ImportFile_ImportData](importfile.md) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.importdata?text=importdata EntityType" />