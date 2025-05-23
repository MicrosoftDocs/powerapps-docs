---
title: "Site Component (powerpagecomponent) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Site Component (powerpagecomponent) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Site Component (powerpagecomponent) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Site Component (powerpagecomponent) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /powerpagecomponents(*powerpagecomponentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /powerpagecomponents<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /powerpagecomponents(*powerpagecomponentid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /powerpagecomponents(*powerpagecomponentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /powerpagecomponents<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /powerpagecomponents(*powerpagecomponentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /powerpagecomponents(*powerpagecomponentid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /powerpagecomponents(*powerpagecomponentid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Site Component (powerpagecomponent) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Site Component (powerpagecomponent) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Site Component** |
| **DisplayCollectionName** | **Site Components** |
| **SchemaName** | `powerpagecomponent` |
| **CollectionSchemaName** | `powerpagecomponents` |
| **EntitySetName** | `powerpagecomponents`|
| **LogicalName** | `powerpagecomponent` |
| **LogicalCollectionName** | `powerpagecomponents` |
| **PrimaryIdAttribute** | `powerpagecomponentid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [content](#BKMK_content)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [powerpagecomponentId](#BKMK_powerpagecomponentId)
- [powerpagecomponenttype](#BKMK_powerpagecomponenttype)
- [powerpagesiteid](#BKMK_powerpagesiteid)
- [powerpagesitelanguageid](#BKMK_powerpagesitelanguageid)
- [searchcontent](#BKMK_searchcontent)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_content"></a> content

|Property|Value|
|---|---|
|Description||
|DisplayName|**Content**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`content`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|400|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Owner Id**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_powerpagecomponentId"></a> powerpagecomponentId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Power Pages Component**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`powerpagecomponentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_powerpagecomponenttype"></a> powerpagecomponenttype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Component Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerpagecomponenttype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`powerpagecomponenttype`|

#### powerpagecomponenttype Choices/Options

|Value|Label|
|---|---|
|1|**Publishing State**|
|2|**Web Page**|
|3|**Web File**|
|4|**Web Link Set**|
|5|**Web Link**|
|6|**Page Template**|
|7|**Content Snippet**|
|8|**Web Template**|
|9|**Site Setting**|
|10|**Web Page Access Control Rule**|
|11|**Web Role**|
|12|**Website Access**|
|13|**Site Marker**|
|15|**Basic Form**|
|16|**Basic Form Metadata**|
|17|**List**|
|18|**Table Permission**|
|19|**Advanced Form**|
|20|**Advanced Form Step**|
|21|**Advanced Form Metadata**|
|24|**Poll Placement**|
|26|**Ad Placement**|
|27|**Bot Consumer**|
|28|**Column Permission Profile**|
|29|**Column Permission**|
|30|**Redirect**|
|31|**Publishing State Transition Rule**|
|32|**Shortcut**|
|33|**Cloud Flow**|
|34|**UX Component**|

### <a name="BKMK_powerpagesiteid"></a> powerpagesiteid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Power Pages Site id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerpagesiteid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|powerpagesite|

### <a name="BKMK_powerpagesitelanguageid"></a> powerpagesitelanguageid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Power Pages Site Language Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerpagesitelanguageid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|powerpagesitelanguage|

### <a name="BKMK_searchcontent"></a> searchcontent

|Property|Value|
|---|---|
|Description||
|DisplayName|**Search Content**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`searchcontent`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Power Pages Component**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`powerpagecomponent_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Power Pages Component**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`powerpagecomponent_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [filecontent](#BKMK_filecontent)
- [filecontent_Name](#BKMK_filecontent_Name)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
|DefaultFormValue||
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
|Description|**Unique identifier of the user who created the record.**|
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
|Description|**Date and time when the record was created.**|
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
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_filecontent"></a> filecontent

|Property|Value|
|---|---|
|Description|**File Content column contains portal web files e.g. png, css etc.**|
|DisplayName|**File Content**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`filecontent`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|131072|

### <a name="BKMK_filecontent_Name"></a> filecontent_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filecontent_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
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
|Description|**Date and time when the record was modified.**|
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
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description|**Yomi name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier for the business unit that owns the record**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier for the team that owns the record.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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
|Description|**Version Number**|
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

- [business_unit_powerpagecomponent](#BKMK_business_unit_powerpagecomponent)
- [FileAttachment_powerpagecomponent_filecontent](#BKMK_FileAttachment_powerpagecomponent_filecontent)
- [lk_powerpagecomponent_createdby](#BKMK_lk_powerpagecomponent_createdby)
- [lk_powerpagecomponent_createdonbehalfby](#BKMK_lk_powerpagecomponent_createdonbehalfby)
- [lk_powerpagecomponent_modifiedby](#BKMK_lk_powerpagecomponent_modifiedby)
- [lk_powerpagecomponent_modifiedonbehalfby](#BKMK_lk_powerpagecomponent_modifiedonbehalfby)
- [owner_powerpagecomponent](#BKMK_owner_powerpagecomponent)
- [powerpagesite_powerpagecomponent_powerpagesiteid](#BKMK_powerpagesite_powerpagecomponent_powerpagesiteid)
- [powerpagesitelanguage_powerpagecomponent_powerpagesitelanguageid](#BKMK_powerpagesitelanguage_powerpagecomponent_powerpagesitelanguageid)
- [team_powerpagecomponent](#BKMK_team_powerpagecomponent)
- [user_powerpagecomponent](#BKMK_user_powerpagecomponent)

### <a name="BKMK_business_unit_powerpagecomponent"></a> business_unit_powerpagecomponent

One-To-Many Relationship: [businessunit business_unit_powerpagecomponent](businessunit.md#BKMK_business_unit_powerpagecomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_powerpagecomponent_filecontent"></a> FileAttachment_powerpagecomponent_filecontent

One-To-Many Relationship: [fileattachment FileAttachment_powerpagecomponent_filecontent](fileattachment.md#BKMK_FileAttachment_powerpagecomponent_filecontent)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`filecontent`|
|ReferencingEntityNavigationPropertyName|`filecontent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_powerpagecomponent_createdby"></a> lk_powerpagecomponent_createdby

One-To-Many Relationship: [systemuser lk_powerpagecomponent_createdby](systemuser.md#BKMK_lk_powerpagecomponent_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_powerpagecomponent_createdonbehalfby"></a> lk_powerpagecomponent_createdonbehalfby

One-To-Many Relationship: [systemuser lk_powerpagecomponent_createdonbehalfby](systemuser.md#BKMK_lk_powerpagecomponent_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_powerpagecomponent_modifiedby"></a> lk_powerpagecomponent_modifiedby

One-To-Many Relationship: [systemuser lk_powerpagecomponent_modifiedby](systemuser.md#BKMK_lk_powerpagecomponent_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_powerpagecomponent_modifiedonbehalfby"></a> lk_powerpagecomponent_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_powerpagecomponent_modifiedonbehalfby](systemuser.md#BKMK_lk_powerpagecomponent_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_powerpagecomponent"></a> owner_powerpagecomponent

One-To-Many Relationship: [owner owner_powerpagecomponent](owner.md#BKMK_owner_powerpagecomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesite_powerpagecomponent_powerpagesiteid"></a> powerpagesite_powerpagecomponent_powerpagesiteid

One-To-Many Relationship: [powerpagesite powerpagesite_powerpagecomponent_powerpagesiteid](powerpagesite.md#BKMK_powerpagesite_powerpagecomponent_powerpagesiteid)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesite`|
|ReferencedAttribute|`powerpagesiteid`|
|ReferencingAttribute|`powerpagesiteid`|
|ReferencingEntityNavigationPropertyName|`powerpagesiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_powerpagesitelanguage_powerpagecomponent_powerpagesitelanguageid"></a> powerpagesitelanguage_powerpagecomponent_powerpagesitelanguageid

One-To-Many Relationship: [powerpagesitelanguage powerpagesitelanguage_powerpagecomponent_powerpagesitelanguageid](powerpagesitelanguage.md#BKMK_powerpagesitelanguage_powerpagecomponent_powerpagesitelanguageid)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitelanguage`|
|ReferencedAttribute|`powerpagesitelanguageid`|
|ReferencingAttribute|`powerpagesitelanguageid`|
|ReferencingEntityNavigationPropertyName|`powerpagesitelanguageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_powerpagecomponent"></a> team_powerpagecomponent

One-To-Many Relationship: [team team_powerpagecomponent](team.md#BKMK_team_powerpagecomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_powerpagecomponent"></a> user_powerpagecomponent

One-To-Many Relationship: [systemuser user_powerpagecomponent](systemuser.md#BKMK_user_powerpagecomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [powerpagecomponent_AsyncOperations](#BKMK_powerpagecomponent_AsyncOperations)
- [powerpagecomponent_BulkDeleteFailures](#BKMK_powerpagecomponent_BulkDeleteFailures)
- [powerpagecomponent_FileAttachments](#BKMK_powerpagecomponent_FileAttachments)
- [powerpagecomponent_MailboxTrackingFolders](#BKMK_powerpagecomponent_MailboxTrackingFolders)
- [powerpagecomponent_mspp_webformid_adx_webformsession](#BKMK_powerpagecomponent_mspp_webformid_adx_webformsession)
- [powerpagecomponent_mspp_webformstepid_adx_webformsession](#BKMK_powerpagecomponent_mspp_webformstepid_adx_webformsession)
- [powerpagecomponent_PrincipalObjectAttributeAccesses](#BKMK_powerpagecomponent_PrincipalObjectAttributeAccesses)
- [powerpagecomponent_ProcessSession](#BKMK_powerpagecomponent_ProcessSession)
- [powerpagecomponent_SyncErrors](#BKMK_powerpagecomponent_SyncErrors)

### <a name="BKMK_powerpagecomponent_AsyncOperations"></a> powerpagecomponent_AsyncOperations

Many-To-One Relationship: [asyncoperation powerpagecomponent_AsyncOperations](asyncoperation.md#BKMK_powerpagecomponent_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`powerpagecomponent_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_BulkDeleteFailures"></a> powerpagecomponent_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure powerpagecomponent_BulkDeleteFailures](bulkdeletefailure.md#BKMK_powerpagecomponent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`powerpagecomponent_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_FileAttachments"></a> powerpagecomponent_FileAttachments

Many-To-One Relationship: [fileattachment powerpagecomponent_FileAttachments](fileattachment.md#BKMK_powerpagecomponent_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`powerpagecomponent_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_MailboxTrackingFolders"></a> powerpagecomponent_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder powerpagecomponent_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_powerpagecomponent_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`powerpagecomponent_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_mspp_webformid_adx_webformsession"></a> powerpagecomponent_mspp_webformid_adx_webformsession

Many-To-One Relationship: [adx_webformsession powerpagecomponent_mspp_webformid_adx_webformsession](adx_webformsession.md#BKMK_powerpagecomponent_mspp_webformid_adx_webformsession)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_webformsession`|
|ReferencingAttribute|`mspp_webformid`|
|ReferencedEntityNavigationPropertyName|`powerpagecomponent_mspp_webformid_adx_webformsession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Sessions<br />MenuId: null<br />Order: 103000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_mspp_webformstepid_adx_webformsession"></a> powerpagecomponent_mspp_webformstepid_adx_webformsession

Many-To-One Relationship: [adx_webformsession powerpagecomponent_mspp_webformstepid_adx_webformsession](adx_webformsession.md#BKMK_powerpagecomponent_mspp_webformstepid_adx_webformsession)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_webformsession`|
|ReferencingAttribute|`mspp_webformstepid`|
|ReferencedEntityNavigationPropertyName|`powerpagecomponent_mspp_webformstepid_adx_webformsession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_PrincipalObjectAttributeAccesses"></a> powerpagecomponent_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess powerpagecomponent_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_powerpagecomponent_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`powerpagecomponent_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_ProcessSession"></a> powerpagecomponent_ProcessSession

Many-To-One Relationship: [processsession powerpagecomponent_ProcessSession](processsession.md#BKMK_powerpagecomponent_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`powerpagecomponent_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_SyncErrors"></a> powerpagecomponent_SyncErrors

Many-To-One Relationship: [syncerror powerpagecomponent_SyncErrors](syncerror.md#BKMK_powerpagecomponent_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`powerpagecomponent_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [adx_invitation_mspp_webrole_powerpagecomponent](#BKMK_adx_invitation_mspp_webrole_powerpagecomponent)
- [powerpagecomponent_mspp_webrole_account](#BKMK_powerpagecomponent_mspp_webrole_account)
- [powerpagecomponent_mspp_webrole_contact](#BKMK_powerpagecomponent_mspp_webrole_contact)
- [powerpagecomponent_powerpagecomponent](#BKMK_powerpagecomponent_powerpagecomponent)
- [powerpagecomponent_webrole_systemuser](#BKMK_powerpagecomponent_webrole_systemuser)

### <a name="BKMK_adx_invitation_mspp_webrole_powerpagecomponent"></a> adx_invitation_mspp_webrole_powerpagecomponent

See [adx_invitation adx_invitation_mspp_webrole_powerpagecomponent Many-To-Many Relationship](adx_invitation.md#BKMK_adx_invitation_mspp_webrole_powerpagecomponent)

|Property|Value|
|---|---|
|IntersectEntityName|`adx_invitation_mspp_webrole_powerpagecomponent`|
|IsCustomizable|True|
|SchemaName|`adx_invitation_mspp_webrole_powerpagecomponent`|
|IntersectAttribute|`powerpagecomponentid`|
|NavigationPropertyName|`adx_invitation_mspp_webrole_powerpagecomponent`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: Assign To Web Roles<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_mspp_webrole_account"></a> powerpagecomponent_mspp_webrole_account

See [account powerpagecomponent_mspp_webrole_account Many-To-Many Relationship](account.md#BKMK_powerpagecomponent_mspp_webrole_account)

|Property|Value|
|---|---|
|IntersectEntityName|`powerpagecomponent_mspp_webrole_account`|
|IsCustomizable|True|
|SchemaName|`powerpagecomponent_mspp_webrole_account`|
|IntersectAttribute|`powerpagecomponentid`|
|NavigationPropertyName|`powerpagecomponent_mspp_webrole_account`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100600<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_mspp_webrole_contact"></a> powerpagecomponent_mspp_webrole_contact

See [contact powerpagecomponent_mspp_webrole_contact Many-To-Many Relationship](contact.md#BKMK_powerpagecomponent_mspp_webrole_contact)

|Property|Value|
|---|---|
|IntersectEntityName|`powerpagecomponent_mspp_webrole_contact`|
|IsCustomizable|True|
|SchemaName|`powerpagecomponent_mspp_webrole_contact`|
|IntersectAttribute|`powerpagecomponentid`|
|NavigationPropertyName|`powerpagecomponent_mspp_webrole_contact`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 103100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_powerpagecomponent"></a> powerpagecomponent_powerpagecomponent

This is a self-referencing many-to-many relationship.

|Property|Value|
|---|---|
|IntersectEntityName|`powerpagecomponent_powerpagecomponent`|
|IsCustomizable|False|
|SchemaName|`powerpagecomponent_powerpagecomponent`|
|Entity1IntersectAttribute|`powerpagecomponentidone`|
|Entity2IntersectAttribute|`powerpagecomponentidtwo`|
|Entity1NavigationPropertyName|`powerpagecomponent_powerpagecomponent`|
|Entity2NavigationPropertyName|`powerpagecomponent_powerpagecomponent`|
|Entity1AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 20000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|
|Entity2AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Power Pages Component Power Pages Component<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_powerpagecomponent_webrole_systemuser"></a> powerpagecomponent_webrole_systemuser

See [systemuser powerpagecomponent_webrole_systemuser Many-To-Many Relationship](systemuser.md#BKMK_powerpagecomponent_webrole_systemuser)

|Property|Value|
|---|---|
|IntersectEntityName|`powerpagecomponent_webrole_systemuser`|
|IsCustomizable|False|
|SchemaName|`powerpagecomponent_webrole_systemuser`|
|IntersectAttribute|`powerpagecomponentid`|
|NavigationPropertyName|`powerpagecomponent_webrole_systemuser`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 20000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.powerpagecomponent?displayProperty=fullName>
