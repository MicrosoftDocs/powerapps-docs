---
title: "Multistep Form Session (adx_webformsession) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Multistep Form Session (adx_webformsession) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Multistep Form Session (adx_webformsession) table/entity reference (Microsoft Dataverse)

Serves as a mechanism to log the occurrence of an incomplete multistep form entry for a given user so they can return and complete it later.

## Messages

The following table lists the messages for the Multistep Form Session (adx_webformsession) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /adx_webformsessions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /adx_webformsessions(*adx_webformsessionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /adx_webformsessions(*adx_webformsessionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /adx_webformsessions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /adx_webformsessions(*adx_webformsessionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /adx_webformsessions(*adx_webformsessionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /adx_webformsessions(*adx_webformsessionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Multistep Form Session (adx_webformsession) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Multistep Form Session (adx_webformsession) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Multistep Form Session** |
| **DisplayCollectionName** | **Multistep Form Sessions** |
| **SchemaName** | `adx_webformsession` |
| **CollectionSchemaName** | `adx_webformsessions` |
| **EntitySetName** | `adx_webformsessions`|
| **LogicalName** | `adx_webformsession` |
| **LogicalCollectionName** | `adx_webformsessions` |
| **PrimaryIdAttribute** | `adx_webformsessionid` |
| **PrimaryNameAttribute** |`adx_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [adx_anonymousidentification](#BKMK_adx_anonymousidentification)
- [adx_contact](#BKMK_adx_contact)
- [adx_currentstepindex](#BKMK_adx_currentstepindex)
- [adx_name](#BKMK_adx_name)
- [adx_primaryrecordentitykeyname](#BKMK_adx_primaryrecordentitykeyname)
- [adx_primaryrecordentitylogicalname](#BKMK_adx_primaryrecordentitylogicalname)
- [adx_primaryrecordid](#BKMK_adx_primaryrecordid)
- [adx_stephistory](#BKMK_adx_stephistory)
- [adx_systemuser](#BKMK_adx_systemuser)
- [adx_userhostaddress](#BKMK_adx_userhostaddress)
- [adx_useridentityname](#BKMK_adx_useridentityname)
- [adx_webformsessionId](#BKMK_adx_webformsessionId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [mspp_webformid](#BKMK_mspp_webformid)
- [mspp_webformstepid](#BKMK_mspp_webformstepid)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_adx_anonymousidentification"></a> adx_anonymousidentification

|Property|Value|
|---|---|
|Description||
|DisplayName|**Anonymous Identification**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_anonymousidentification`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_adx_contact"></a> adx_contact

|Property|Value|
|---|---|
|Description|**Unique identifier for Contact associated with Multistep Form Session.**|
|DisplayName|**Contact**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_contact`|
|RequiredLevel|Recommended|
|Type|Lookup|
|Targets|contact|

### <a name="BKMK_adx_currentstepindex"></a> adx_currentstepindex

|Property|Value|
|---|---|
|Description|**The index of the current step the user last visited.**|
|DisplayName|**Current Step Index**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_currentstepindex`|
|RequiredLevel|Recommended|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_adx_name"></a> adx_name

|Property|Value|
|---|---|
|Description|**Type the name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_adx_primaryrecordentitykeyname"></a> adx_primaryrecordentitykeyname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Primary Record Entity Primary Key Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_primaryrecordentitykeyname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_adx_primaryrecordentitylogicalname"></a> adx_primaryrecordentitylogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Primary Record Table name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_primaryrecordentitylogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_adx_primaryrecordid"></a> adx_primaryrecordid

|Property|Value|
|---|---|
|Description|**Shows the ID of the primary record created by the multistep form.  Used to retrieve the appropriate session record.**|
|DisplayName|**Primary Record ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_primaryrecordid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|38|

### <a name="BKMK_adx_stephistory"></a> adx_stephistory

|Property|Value|
|---|---|
|Description|**History of steps in JSON**|
|DisplayName|**Step History**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_stephistory`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20000|

### <a name="BKMK_adx_systemuser"></a> adx_systemuser

|Property|Value|
|---|---|
|Description|**Unique identifier for User associated with Multistep Form Session.**|
|DisplayName|**System User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_systemuser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_adx_userhostaddress"></a> adx_userhostaddress

|Property|Value|
|---|---|
|Description||
|DisplayName|**User Host Address**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_userhostaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_adx_useridentityname"></a> adx_useridentityname

|Property|Value|
|---|---|
|Description||
|DisplayName|**User Identity Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_useridentityname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_adx_webformsessionId"></a> adx_webformsessionId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Multistep Form Session**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`adx_webformsessionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Shows the sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_mspp_webformid"></a> mspp_webformid

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Form associated with Web Form Session.**|
|DisplayName|**Multistep Form**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webformid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|powerpagecomponent|

### <a name="BKMK_mspp_webformstepid"></a> mspp_webformstepid

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Multistep Form Session**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webformstepid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|powerpagecomponent|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was migrated. The date and time are displayed in the time zone selected in the solution options.**|
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

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Shows the status of the multistep form session.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`adx_webformsession_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Select the Multistep Form Session's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`adx_webformsession_statuscode`|

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
|Description|**Shows the time zone code that was in use when the record was created.**|
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
- [OrganizationId](#BKMK_OrganizationId)
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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in the solution options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
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
|Description|**Shows the date and time when the record was updated. The date and time are displayed in the time zone selected in the solution options.**|
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
|Description|**Shows who last updated the record on behalf of another user.**|
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
|Description|**Shows the organization.**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

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

- [adx_webformsession_contact](#BKMK_adx_webformsession_contact)
- [adx_webformsession_systemuser](#BKMK_adx_webformsession_systemuser)
- [lk_adx_webformsession_createdby](#BKMK_lk_adx_webformsession_createdby)
- [lk_adx_webformsession_createdonbehalfby](#BKMK_lk_adx_webformsession_createdonbehalfby)
- [lk_adx_webformsession_modifiedby](#BKMK_lk_adx_webformsession_modifiedby)
- [lk_adx_webformsession_modifiedonbehalfby](#BKMK_lk_adx_webformsession_modifiedonbehalfby)
- [organization_adx_webformsession](#BKMK_organization_adx_webformsession)
- [powerpagecomponent_mspp_webformid_adx_webformsession](#BKMK_powerpagecomponent_mspp_webformid_adx_webformsession)
- [powerpagecomponent_mspp_webformstepid_adx_webformsession](#BKMK_powerpagecomponent_mspp_webformstepid_adx_webformsession)

### <a name="BKMK_adx_webformsession_contact"></a> adx_webformsession_contact

One-To-Many Relationship: [contact adx_webformsession_contact](contact.md#BKMK_adx_webformsession_contact)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`adx_contact`|
|ReferencingEntityNavigationPropertyName|`adx_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_webformsession_systemuser"></a> adx_webformsession_systemuser

One-To-Many Relationship: [systemuser adx_webformsession_systemuser](systemuser.md#BKMK_adx_webformsession_systemuser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`adx_systemuser`|
|ReferencingEntityNavigationPropertyName|`adx_systemuser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_adx_webformsession_createdby"></a> lk_adx_webformsession_createdby

One-To-Many Relationship: [systemuser lk_adx_webformsession_createdby](systemuser.md#BKMK_lk_adx_webformsession_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_adx_webformsession_createdonbehalfby"></a> lk_adx_webformsession_createdonbehalfby

One-To-Many Relationship: [systemuser lk_adx_webformsession_createdonbehalfby](systemuser.md#BKMK_lk_adx_webformsession_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_adx_webformsession_modifiedby"></a> lk_adx_webformsession_modifiedby

One-To-Many Relationship: [systemuser lk_adx_webformsession_modifiedby](systemuser.md#BKMK_lk_adx_webformsession_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_adx_webformsession_modifiedonbehalfby"></a> lk_adx_webformsession_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_adx_webformsession_modifiedonbehalfby](systemuser.md#BKMK_lk_adx_webformsession_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_adx_webformsession"></a> organization_adx_webformsession

One-To-Many Relationship: [organization organization_adx_webformsession](organization.md#BKMK_organization_adx_webformsession)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagecomponent_mspp_webformid_adx_webformsession"></a> powerpagecomponent_mspp_webformid_adx_webformsession

One-To-Many Relationship: [powerpagecomponent powerpagecomponent_mspp_webformid_adx_webformsession](powerpagecomponent.md#BKMK_powerpagecomponent_mspp_webformid_adx_webformsession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagecomponent`|
|ReferencedAttribute|`powerpagecomponentid`|
|ReferencingAttribute|`mspp_webformid`|
|ReferencingEntityNavigationPropertyName|`mspp_webformid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_powerpagecomponent_mspp_webformstepid_adx_webformsession"></a> powerpagecomponent_mspp_webformstepid_adx_webformsession

One-To-Many Relationship: [powerpagecomponent powerpagecomponent_mspp_webformstepid_adx_webformsession](powerpagecomponent.md#BKMK_powerpagecomponent_mspp_webformstepid_adx_webformsession)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagecomponent`|
|ReferencedAttribute|`powerpagecomponentid`|
|ReferencingAttribute|`mspp_webformstepid`|
|ReferencingEntityNavigationPropertyName|`mspp_webformstepid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [adx_webformsession_AsyncOperations](#BKMK_adx_webformsession_AsyncOperations)
- [adx_webformsession_BulkDeleteFailures](#BKMK_adx_webformsession_BulkDeleteFailures)
- [adx_webformsession_MailboxTrackingFolders](#BKMK_adx_webformsession_MailboxTrackingFolders)
- [adx_webformsession_PrincipalObjectAttributeAccesses](#BKMK_adx_webformsession_PrincipalObjectAttributeAccesses)
- [adx_webformsession_ProcessSession](#BKMK_adx_webformsession_ProcessSession)
- [adx_webformsession_SyncErrors](#BKMK_adx_webformsession_SyncErrors)

### <a name="BKMK_adx_webformsession_AsyncOperations"></a> adx_webformsession_AsyncOperations

Many-To-One Relationship: [asyncoperation adx_webformsession_AsyncOperations](asyncoperation.md#BKMK_adx_webformsession_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_webformsession_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_webformsession_BulkDeleteFailures"></a> adx_webformsession_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure adx_webformsession_BulkDeleteFailures](bulkdeletefailure.md#BKMK_adx_webformsession_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_webformsession_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_webformsession_MailboxTrackingFolders"></a> adx_webformsession_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder adx_webformsession_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_adx_webformsession_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_webformsession_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_webformsession_PrincipalObjectAttributeAccesses"></a> adx_webformsession_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess adx_webformsession_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_adx_webformsession_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`adx_webformsession_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_webformsession_ProcessSession"></a> adx_webformsession_ProcessSession

Many-To-One Relationship: [processsession adx_webformsession_ProcessSession](processsession.md#BKMK_adx_webformsession_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_webformsession_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_webformsession_SyncErrors"></a> adx_webformsession_SyncErrors

Many-To-One Relationship: [syncerror adx_webformsession_SyncErrors](syncerror.md#BKMK_adx_webformsession_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_webformsession_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.adx_webformsession?displayProperty=fullName>
