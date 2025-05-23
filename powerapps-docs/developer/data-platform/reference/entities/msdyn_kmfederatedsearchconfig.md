---
title: "Search provider (msdyn_kmfederatedsearchconfig) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Search provider (msdyn_kmfederatedsearchconfig) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Search provider (msdyn_kmfederatedsearchconfig) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Search provider (msdyn_kmfederatedsearchconfig) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_kmfederatedsearchconfigs(*msdyn_kmfederatedsearchconfigid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_kmfederatedsearchconfigs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_kmfederatedsearchconfigs(*msdyn_kmfederatedsearchconfigid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_kmfederatedsearchconfigs(*msdyn_kmfederatedsearchconfigid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_kmfederatedsearchconfigs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_kmfederatedsearchconfigs(*msdyn_kmfederatedsearchconfigid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_kmfederatedsearchconfigs(*msdyn_kmfederatedsearchconfigid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_kmfederatedsearchconfigs(*msdyn_kmfederatedsearchconfigid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Search provider (msdyn_kmfederatedsearchconfig) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Search provider** |
| **DisplayCollectionName** | **Search providers** |
| **SchemaName** | `msdyn_kmfederatedsearchconfig` |
| **CollectionSchemaName** | `msdyn_kmfederatedsearchconfigs` |
| **EntitySetName** | `msdyn_kmfederatedsearchconfigs`|
| **LogicalName** | `msdyn_kmfederatedsearchconfig` |
| **LogicalCollectionName** | `msdyn_kmfederatedsearchconfigs` |
| **PrimaryIdAttribute** | `msdyn_kmfederatedsearchconfigid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ConnectionId](#BKMK_ConnectionId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_Description](#BKMK_msdyn_Description)
- [msdyn_kmfederatedsearchconfigId](#BKMK_msdyn_kmfederatedsearchconfigId)
- [msdyn_Name](#BKMK_msdyn_Name)
- [Organization](#BKMK_Organization)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [SearchType](#BKMK_SearchType)
- [SharepointURL](#BKMK_SharepointURL)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ConnectionId"></a> ConnectionId

|Property|Value|
|---|---|
|Description|**Unique identifier when you create a connector in Microsoft search, please check the documentation above.**|
|DisplayName|**Connection Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073|

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

### <a name="BKMK_msdyn_Description"></a> msdyn_Description

|Property|Value|
|---|---|
|Description|**This field specifies the description of Search provider record**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_msdyn_kmfederatedsearchconfigId"></a> msdyn_kmfederatedsearchconfigId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Search Provider Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_kmfederatedsearchconfigid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_Name"></a> msdyn_Name

|Property|Value|
|---|---|
|Description|**The name of the search provider**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Organization"></a> Organization

|Property|Value|
|---|---|
|Description||
|DisplayName|**Organization**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`organization`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_SearchType"></a> SearchType

|Property|Value|
|---|---|
|Description||
|DisplayName|**Search Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`searchtype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_kmfederatedsearchconfig_searchtype`|

#### SearchType Choices/Options

|Value|Label|
|---|---|
|100000000|**Cross-Organizational Search**|
|100000001|**Sharepoint**|
|100000002|**Microsoft Graph Connector**|

### <a name="BKMK_SharepointURL"></a> SharepointURL

|Property|Value|
|---|---|
|Description||
|DisplayName|**Sharepoint URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sharepointurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the kmfederatedsearchconfig**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_kmfederatedsearchconfig_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the kmfederatedsearchconfig**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_kmfederatedsearchconfig_statuscode`|

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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

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

- [business_unit_msdyn_kmfederatedsearchconfig](#BKMK_business_unit_msdyn_kmfederatedsearchconfig)
- [lk_msdyn_kmfederatedsearchconfig_createdby](#BKMK_lk_msdyn_kmfederatedsearchconfig_createdby)
- [lk_msdyn_kmfederatedsearchconfig_createdonbehalfby](#BKMK_lk_msdyn_kmfederatedsearchconfig_createdonbehalfby)
- [lk_msdyn_kmfederatedsearchconfig_modifiedby](#BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedby)
- [lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby](#BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby)
- [owner_msdyn_kmfederatedsearchconfig](#BKMK_owner_msdyn_kmfederatedsearchconfig)
- [team_msdyn_kmfederatedsearchconfig](#BKMK_team_msdyn_kmfederatedsearchconfig)
- [user_msdyn_kmfederatedsearchconfig](#BKMK_user_msdyn_kmfederatedsearchconfig)

### <a name="BKMK_business_unit_msdyn_kmfederatedsearchconfig"></a> business_unit_msdyn_kmfederatedsearchconfig

One-To-Many Relationship: [businessunit business_unit_msdyn_kmfederatedsearchconfig](businessunit.md#BKMK_business_unit_msdyn_kmfederatedsearchconfig)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_kmfederatedsearchconfig_createdby"></a> lk_msdyn_kmfederatedsearchconfig_createdby

One-To-Many Relationship: [systemuser lk_msdyn_kmfederatedsearchconfig_createdby](systemuser.md#BKMK_lk_msdyn_kmfederatedsearchconfig_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_kmfederatedsearchconfig_createdonbehalfby"></a> lk_msdyn_kmfederatedsearchconfig_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_kmfederatedsearchconfig_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_kmfederatedsearchconfig_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedby"></a> lk_msdyn_kmfederatedsearchconfig_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_kmfederatedsearchconfig_modifiedby](systemuser.md#BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby"></a> lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_kmfederatedsearchconfig_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_kmfederatedsearchconfig"></a> owner_msdyn_kmfederatedsearchconfig

One-To-Many Relationship: [owner owner_msdyn_kmfederatedsearchconfig](owner.md#BKMK_owner_msdyn_kmfederatedsearchconfig)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_kmfederatedsearchconfig"></a> team_msdyn_kmfederatedsearchconfig

One-To-Many Relationship: [team team_msdyn_kmfederatedsearchconfig](team.md#BKMK_team_msdyn_kmfederatedsearchconfig)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_kmfederatedsearchconfig"></a> user_msdyn_kmfederatedsearchconfig

One-To-Many Relationship: [systemuser user_msdyn_kmfederatedsearchconfig](systemuser.md#BKMK_user_msdyn_kmfederatedsearchconfig)

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

- [IK_msdyn_kmfederatedsearchconfig_msdyn_federatedarticle_searchproviderid](#BKMK_IK_msdyn_kmfederatedsearchconfig_msdyn_federatedarticle_searchproviderid)
- [msdyn_kmfederatedsearchconfig_AsyncOperations](#BKMK_msdyn_kmfederatedsearchconfig_AsyncOperations)
- [msdyn_kmfederatedsearchconfig_BulkDeleteFailures](#BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures)
- [msdyn_kmfederatedsearchconfig_DuplicateBaseRecord](#BKMK_msdyn_kmfederatedsearchconfig_DuplicateBaseRecord)
- [msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord](#BKMK_msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord)
- [msdyn_kmfederatedsearchconfig_MailboxTrackingFolders](#BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders)
- [msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses](#BKMK_msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses)
- [msdyn_kmfederatedsearchconfig_ProcessSession](#BKMK_msdyn_kmfederatedsearchconfig_ProcessSession)
- [msdyn_kmfederatedsearchconfig_SyncErrors](#BKMK_msdyn_kmfederatedsearchconfig_SyncErrors)

### <a name="BKMK_IK_msdyn_kmfederatedsearchconfig_msdyn_federatedarticle_searchproviderid"></a> IK_msdyn_kmfederatedsearchconfig_msdyn_federatedarticle_searchproviderid

Many-To-One Relationship: [msdyn_federatedarticle IK_msdyn_kmfederatedsearchconfig_msdyn_federatedarticle_searchproviderid](msdyn_federatedarticle.md#BKMK_IK_msdyn_kmfederatedsearchconfig_msdyn_federatedarticle_searchproviderid)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_federatedarticle`|
|ReferencingAttribute|`msdyn_searchproviderid`|
|ReferencedEntityNavigationPropertyName|`IK_msdyn_kmfederatedsearchconfig_msdyn_federatedarticle_searchproviderid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_AsyncOperations"></a> msdyn_kmfederatedsearchconfig_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_kmfederatedsearchconfig_AsyncOperations](asyncoperation.md#BKMK_msdyn_kmfederatedsearchconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_kmfederatedsearchconfig_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures"></a> msdyn_kmfederatedsearchconfig_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_kmfederatedsearchconfig_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_kmfederatedsearchconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_kmfederatedsearchconfig_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_DuplicateBaseRecord"></a> msdyn_kmfederatedsearchconfig_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_kmfederatedsearchconfig_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_kmfederatedsearchconfig_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_kmfederatedsearchconfig_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord"></a> msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_kmfederatedsearchconfig_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders"></a> msdyn_kmfederatedsearchconfig_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_kmfederatedsearchconfig_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_kmfederatedsearchconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_kmfederatedsearchconfig_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses"></a> msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_kmfederatedsearchconfig_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_ProcessSession"></a> msdyn_kmfederatedsearchconfig_ProcessSession

Many-To-One Relationship: [processsession msdyn_kmfederatedsearchconfig_ProcessSession](processsession.md#BKMK_msdyn_kmfederatedsearchconfig_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_kmfederatedsearchconfig_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_kmfederatedsearchconfig_SyncErrors"></a> msdyn_kmfederatedsearchconfig_SyncErrors

Many-To-One Relationship: [syncerror msdyn_kmfederatedsearchconfig_SyncErrors](syncerror.md#BKMK_msdyn_kmfederatedsearchconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_kmfederatedsearchconfig_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_kmfederatedsearchconfig?displayProperty=fullName>
