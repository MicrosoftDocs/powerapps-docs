---
title: "View (SavedQuery) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the View (SavedQuery) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# View (SavedQuery) table/entity reference (Microsoft Dataverse)

Saved query against the database.

## Messages

The following table lists the messages for the View (SavedQuery) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /savedqueries<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /savedqueries(*savedqueryid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `ExecuteByIdSavedQuery`<br />Event: True | |<xref:Microsoft.Crm.Sdk.Messages.ExecuteByIdSavedQueryRequest>|
| `ExecuteByIdUserQuery`<br />Event: True | |<xref:Microsoft.Crm.Sdk.Messages.ExecuteByIdUserQueryRequest>|
| `InstantiateFilters`<br />Event: False |<xref:Microsoft.Dynamics.CRM.InstantiateFilters?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.InstantiateFiltersRequest>|
| `Retrieve`<br />Event: True |`GET` /savedqueries(*savedqueryid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /savedqueries<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveUnpublished`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `SetState`<br />Event: True |`PATCH` /savedqueries(*savedqueryid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /savedqueries(*savedqueryid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /savedqueries(*savedqueryid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `Validate`<br />Event: False |<xref:Microsoft.Dynamics.CRM.Validate?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ValidateRequest>|
| `ValidateSavedQuery`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ValidateSavedQuery?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ValidateSavedQueryRequest>|
| `ValidateUnpublished`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ValidateUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ValidateUnpublishedRequest>|

## Properties

The following table lists selected properties for the View (SavedQuery) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **View** |
| **DisplayCollectionName** | **Views** |
| **SchemaName** | `SavedQuery` |
| **CollectionSchemaName** | `SavedQueries` |
| **EntitySetName** | `savedqueries`|
| **LogicalName** | `savedquery` |
| **LogicalCollectionName** | `savedqueries` |
| **PrimaryIdAttribute** | `savedqueryid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdvancedGroupBy](#BKMK_AdvancedGroupBy)
- [CanBeDeleted](#BKMK_CanBeDeleted)
- [ColumnSetXml](#BKMK_ColumnSetXml)
- [ConditionalFormatting](#BKMK_ConditionalFormatting)
- [Description](#BKMK_Description)
- [EnableCrossPartition](#BKMK_EnableCrossPartition)
- [FetchXml](#BKMK_FetchXml)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsDefault](#BKMK_IsDefault)
- [IsQuickFindQuery](#BKMK_IsQuickFindQuery)
- [LayoutJson](#BKMK_LayoutJson)
- [LayoutXml](#BKMK_LayoutXml)
- [Name](#BKMK_Name)
- [OfflineSqlQuery](#BKMK_OfflineSqlQuery)
- [QueryAppUsage](#BKMK_QueryAppUsage)
- [QueryType](#BKMK_QueryType)
- [ReturnedTypeCode](#BKMK_ReturnedTypeCode)
- [RoleDisplayConditionsXml](#BKMK_RoleDisplayConditionsXml)
- [SavedQueryId](#BKMK_SavedQueryId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)

### <a name="BKMK_AdvancedGroupBy"></a> AdvancedGroupBy

|Property|Value|
|---|---|
|Description|**Type the column name that will be used to group the results from the data collected across multiple records from a system view.**|
|DisplayName|**Advanced Group By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`advancedgroupby`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_CanBeDeleted"></a> CanBeDeleted

|Property|Value|
|---|---|
|Description|**Tells whether the view can be deleted.**|
|DisplayName|**Can Be Deleted**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbedeleted`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_ColumnSetXml"></a> ColumnSetXml

|Property|Value|
|---|---|
|Description|**Contains the columns and sorting criteria for the view, stored in XML format.**|
|DisplayName|**Column Set XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`columnsetxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ConditionalFormatting"></a> ConditionalFormatting

|Property|Value|
|---|---|
|Description|**Type information about how the items in the system view are formatted.**|
|DisplayName|**Conditional formatting**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`conditionalformatting`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type additional information to describe the view, such as the filter criteria or intended results set.**|
|DisplayName|**Description**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|2000|

### <a name="BKMK_EnableCrossPartition"></a> EnableCrossPartition

|Property|Value|
|---|---|
|Description|**Tells whether the view can retrieve data from all cluster partitions.**|
|DisplayName|**Default**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`enablecrosspartition`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`savedquery_enablecrosspartition`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_FetchXml"></a> FetchXml

|Property|Value|
|---|---|
|Description|**String specifying the query in Fetch XML language.**|
|DisplayName|**Fetch XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fetchxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

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

### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|---|---|
|Description|**Tells whether the view is the default view for the specified record type (entity).**|
|DisplayName|**Default**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdefault`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`savedquery_isdefault`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsQuickFindQuery"></a> IsQuickFindQuery

|Property|Value|
|---|---|
|Description|**Choose whether the view is compatible with Quick Find. When users search for specific items, you define the fields that are searched in.**|
|DisplayName|**Quick Find Compatible**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isquickfindquery`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`savedquery_isquickfindquery`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_LayoutJson"></a> LayoutJson

|Property|Value|
|---|---|
|Description|**Layout data in JSON format.**|
|DisplayName|**Layout data in JSON format.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`layoutjson`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_LayoutXml"></a> LayoutXml

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Layout XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`layoutxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Type a name for the view to describe what results the view will contain. This name is visible to users in the View list.**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|200|

### <a name="BKMK_OfflineSqlQuery"></a> OfflineSqlQuery

|Property|Value|
|---|---|
|Description|**String specifying the corresponding sql query for the fetch xml specified for offline use.**|
|DisplayName|**Offline SQL Query**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`offlinesqlquery`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_QueryAppUsage"></a> QueryAppUsage

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Query Application Usage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`queryappusage`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_QueryType"></a> QueryType

|Property|Value|
|---|---|
|Description|**Shows the type of the query.**|
|DisplayName|**Query Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`querytype`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_ReturnedTypeCode"></a> ReturnedTypeCode

|Property|Value|
|---|---|
|Description|**Type of entity displayed in the view.**|
|DisplayName|**Entity Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`returnedtypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_RoleDisplayConditionsXml"></a> RoleDisplayConditionsXml

|Property|Value|
|---|---|
|Description|**Contains the role display conditions for the SavedQuery.**|
|DisplayName|**Role display conditions for the SavedQuery**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`roledisplayconditionsxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_SavedQueryId"></a> SavedQueryId

|Property|Value|
|---|---|
|Description|**Unique identifier of the view.**|
|DisplayName|**View**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`savedqueryid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows the status of the view.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`savedquery_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Shows the reason code that explains the status of the record.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`savedquery_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsCustom](#BKMK_IsCustom)
- [IsManaged](#BKMK_IsManaged)
- [IsPrivate](#BKMK_IsPrivate)
- [IsUserDefined](#BKMK_IsUserDefined)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationTabOrder](#BKMK_OrganizationTabOrder)
- [OverwriteTime](#BKMK_OverwriteTime)
- [QueryAPI](#BKMK_QueryAPI)
- [SavedQueryIdUnique](#BKMK_SavedQueryIdUnique)
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
|Description|**Shows who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IsCustom"></a> IsCustom

|Property|Value|
|---|---|
|Description|**Tells whether a user created the view.**|
|DisplayName|**Is Custom**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustom`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`savedquery_iscustom`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Tells whether the record is part of a managed solution.**|
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

### <a name="BKMK_IsPrivate"></a> IsPrivate

|Property|Value|
|---|---|
|Description|**Indicates whether or not this is viewable by the entire organization.**|
|DisplayName|**Is Private**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isprivate`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`savedquery_isprivate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsUserDefined"></a> IsUserDefined

|Property|Value|
|---|---|
|Description|**Tells whether the view was created by a user.**|
|DisplayName|**User Defined**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isuserdefined`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`savedquery_isuserdefined`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
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
|Description|**Shows who last updated the record on behalf of another user.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Choose the ID of the organization that the record is associated with.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_OrganizationTabOrder"></a> OrganizationTabOrder

|Property|Value|
|---|---|
|Description|**For the organization, type the tab order to determine how users navigate through the screen using only the Tab key.**|
|DisplayName|**Default Organization tab order**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationtaborder`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

### <a name="BKMK_QueryAPI"></a> QueryAPI

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Query API**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`queryapi`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_SavedQueryIdUnique"></a> SavedQueryIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`savedqueryidunique`|
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

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the view.**|
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

- [lk_savedquery_createdonbehalfby](#BKMK_lk_savedquery_createdonbehalfby)
- [lk_savedquery_modifiedonbehalfby](#BKMK_lk_savedquery_modifiedonbehalfby)
- [lk_savedquerybase_createdby](#BKMK_lk_savedquerybase_createdby)
- [lk_savedquerybase_modifiedby](#BKMK_lk_savedquerybase_modifiedby)
- [organization_saved_queries](#BKMK_organization_saved_queries)

### <a name="BKMK_lk_savedquery_createdonbehalfby"></a> lk_savedquery_createdonbehalfby

One-To-Many Relationship: [systemuser lk_savedquery_createdonbehalfby](systemuser.md#BKMK_lk_savedquery_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_savedquery_modifiedonbehalfby"></a> lk_savedquery_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_savedquery_modifiedonbehalfby](systemuser.md#BKMK_lk_savedquery_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_savedquerybase_createdby"></a> lk_savedquerybase_createdby

One-To-Many Relationship: [systemuser lk_savedquerybase_createdby](systemuser.md#BKMK_lk_savedquerybase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_savedquerybase_modifiedby"></a> lk_savedquerybase_modifiedby

One-To-Many Relationship: [systemuser lk_savedquerybase_modifiedby](systemuser.md#BKMK_lk_savedquerybase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_saved_queries"></a> organization_saved_queries

One-To-Many Relationship: [organization organization_saved_queries](organization.md#BKMK_organization_saved_queries)

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

- [lk_mobileofflineprofileitem_savedquery](#BKMK_lk_mobileofflineprofileitem_savedquery)
- [SavedQuery_AsyncOperations](#BKMK_SavedQuery_AsyncOperations)
- [SavedQuery_BulkDeleteFailures](#BKMK_SavedQuery_BulkDeleteFailures)
- [SavedQuery_SyncErrors](#BKMK_SavedQuery_SyncErrors)

### <a name="BKMK_lk_mobileofflineprofileitem_savedquery"></a> lk_mobileofflineprofileitem_savedquery

Many-To-One Relationship: [mobileofflineprofileitem lk_mobileofflineprofileitem_savedquery](mobileofflineprofileitem.md#BKMK_lk_mobileofflineprofileitem_savedquery)

|Property|Value|
|---|---|
|ReferencingEntity|`mobileofflineprofileitem`|
|ReferencingAttribute|`profileitemrule`|
|ReferencedEntityNavigationPropertyName|`lk_mobileofflineprofileitem_savedquery`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SavedQuery_AsyncOperations"></a> SavedQuery_AsyncOperations

Many-To-One Relationship: [asyncoperation SavedQuery_AsyncOperations](asyncoperation.md#BKMK_SavedQuery_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SavedQuery_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SavedQuery_BulkDeleteFailures"></a> SavedQuery_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure SavedQuery_BulkDeleteFailures](bulkdeletefailure.md#BKMK_SavedQuery_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SavedQuery_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SavedQuery_SyncErrors"></a> SavedQuery_SyncErrors

Many-To-One Relationship: [syncerror SavedQuery_SyncErrors](syncerror.md#BKMK_SavedQuery_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SavedQuery_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.savedquery?displayProperty=fullName>
