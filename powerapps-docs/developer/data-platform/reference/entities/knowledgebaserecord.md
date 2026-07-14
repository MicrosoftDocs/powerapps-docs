---
title: "Knowledge Base Record (KnowledgeBaseRecord) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Knowledge Base Record (KnowledgeBaseRecord) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Knowledge Base Record (KnowledgeBaseRecord) table/entity reference (Microsoft Dataverse)

Metadata of knowledge base (KB) articles associated with Microsoft Dynamics 365 entities.

## Messages

The following table lists the messages for the Knowledge Base Record (KnowledgeBaseRecord) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /knowledgebaserecords(*knowledgebaserecordid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /knowledgebaserecords<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /knowledgebaserecords(*knowledgebaserecordid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /knowledgebaserecords(*knowledgebaserecordid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /knowledgebaserecords<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /knowledgebaserecords(*knowledgebaserecordid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /knowledgebaserecords(*knowledgebaserecordid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /knowledgebaserecords(*knowledgebaserecordid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Knowledge Base Record (KnowledgeBaseRecord) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Knowledge Base Record** |
| **DisplayCollectionName** | **Knowledge Base Records** |
| **SchemaName** | `KnowledgeBaseRecord` |
| **CollectionSchemaName** | `KnowledgeBaseRecords` |
| **EntitySetName** | `knowledgebaserecords`|
| **LogicalName** | `knowledgebaserecord` |
| **LogicalCollectionName** | `knowledgebaserecords` |
| **PrimaryIdAttribute** | `knowledgebaserecordid` |
| **PrimaryNameAttribute** |`title` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [KnowledgeBaseRecordId](#BKMK_KnowledgeBaseRecordId)
- [PrivateUrl](#BKMK_PrivateUrl)
- [PublicUrl](#BKMK_PublicUrl)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Title](#BKMK_Title)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UniqueId](#BKMK_UniqueId)

### <a name="BKMK_KnowledgeBaseRecordId"></a> KnowledgeBaseRecordId

|Property|Value|
|---|---|
|Description|**This field will be used to store the Unique ID of the associated Knowledge Base records**|
|DisplayName|**ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`knowledgebaserecordid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_PrivateUrl"></a> PrivateUrl

|Property|Value|
|---|---|
|Description|**Shows the internal Parature service desk URL of the knowledge base records.**|
|DisplayName|**Private URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`privateurl`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_PublicUrl"></a> PublicUrl

|Property|Value|
|---|---|
|Description|**Shows the public Parature portal URL of the knowledge base records.**|
|DisplayName|**Public URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`publicurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

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

### <a name="BKMK_Title"></a> Title

|Property|Value|
|---|---|
|Description|**Shows the title of the knowledge base (KB) Record.**|
|DisplayName|**KB Record Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`title`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the Knowledge Base Record with respect to the base currency.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_UniqueId"></a> UniqueId

|Property|Value|
|---|---|
|Description|**Shows the unique ID of the linked knowledge base (KB) article.**|
|DisplayName|**Unique ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniqueid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
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

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the knowledge base record with respect to the base currency.**|
|DisplayName|**ExchangeRate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_KnowledgeBaseRecord_createdby](#BKMK_lk_KnowledgeBaseRecord_createdby)
- [lk_KnowledgeBaseRecord_createdonbehalfby](#BKMK_lk_KnowledgeBaseRecord_createdonbehalfby)
- [lk_KnowledgeBaseRecord_modifiedby](#BKMK_lk_KnowledgeBaseRecord_modifiedby)
- [lk_KnowledgeBaseRecord_modifiedonbehalfby](#BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby)
- [organization_KnowledgeBaseRecord](#BKMK_organization_KnowledgeBaseRecord)
- [TransactionCurrency_KnowledgeBaseRecord](#BKMK_TransactionCurrency_KnowledgeBaseRecord)

### <a name="BKMK_lk_KnowledgeBaseRecord_createdby"></a> lk_KnowledgeBaseRecord_createdby

One-To-Many Relationship: [systemuser lk_KnowledgeBaseRecord_createdby](systemuser.md#BKMK_lk_KnowledgeBaseRecord_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_KnowledgeBaseRecord_createdonbehalfby"></a> lk_KnowledgeBaseRecord_createdonbehalfby

One-To-Many Relationship: [systemuser lk_KnowledgeBaseRecord_createdonbehalfby](systemuser.md#BKMK_lk_KnowledgeBaseRecord_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_KnowledgeBaseRecord_modifiedby"></a> lk_KnowledgeBaseRecord_modifiedby

One-To-Many Relationship: [systemuser lk_KnowledgeBaseRecord_modifiedby](systemuser.md#BKMK_lk_KnowledgeBaseRecord_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby"></a> lk_KnowledgeBaseRecord_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_KnowledgeBaseRecord_modifiedonbehalfby](systemuser.md#BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_KnowledgeBaseRecord"></a> organization_KnowledgeBaseRecord

One-To-Many Relationship: [organization organization_KnowledgeBaseRecord](organization.md#BKMK_organization_KnowledgeBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_KnowledgeBaseRecord"></a> TransactionCurrency_KnowledgeBaseRecord

One-To-Many Relationship: [transactioncurrency TransactionCurrency_KnowledgeBaseRecord](transactioncurrency.md#BKMK_TransactionCurrency_KnowledgeBaseRecord)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [KnowledgeBaseRecord_ActivityPointers](#BKMK_KnowledgeBaseRecord_ActivityPointers)
- [knowledgebaserecord_adx_inviteredemptions](#BKMK_knowledgebaserecord_adx_inviteredemptions)
- [knowledgebaserecord_adx_portalcomments](#BKMK_knowledgebaserecord_adx_portalcomments)
- [KnowledgeBaseRecord_Annotations](#BKMK_KnowledgeBaseRecord_Annotations)
- [KnowledgeBaseRecord_Appointments](#BKMK_KnowledgeBaseRecord_Appointments)
- [KnowledgeBaseRecord_AsyncOperations](#BKMK_KnowledgeBaseRecord_AsyncOperations)
- [KnowledgeBaseRecord_BulkDeleteFailures](#BKMK_KnowledgeBaseRecord_BulkDeleteFailures)
- [knowledgebaserecord_chats](#BKMK_knowledgebaserecord_chats)
- [KnowledgeBaseRecord_connections1](#BKMK_KnowledgeBaseRecord_connections1)
- [KnowledgeBaseRecord_connections2](#BKMK_KnowledgeBaseRecord_connections2)
- [KnowledgeBaseRecord_DuplicateBaseRecord](#BKMK_KnowledgeBaseRecord_DuplicateBaseRecord)
- [KnowledgeBaseRecord_DuplicateMatchingRecord](#BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord)
- [KnowledgeBaseRecord_Emails](#BKMK_KnowledgeBaseRecord_Emails)
- [KnowledgeBaseRecord_Faxes](#BKMK_KnowledgeBaseRecord_Faxes)
- [KnowledgeBaseRecord_Letters](#BKMK_KnowledgeBaseRecord_Letters)
- [KnowledgeBaseRecord_PhoneCalls](#BKMK_KnowledgeBaseRecord_PhoneCalls)
- [KnowledgeBaseRecord_PrincipalObjectAttributeAccess](#BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess)
- [KnowledgeBaseRecord_ProcessSession](#BKMK_KnowledgeBaseRecord_ProcessSession)
- [KnowledgeBaseRecord_RecurringAppointmentMasters](#BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters)
- [KnowledgeBaseRecord_SocialActivities](#BKMK_KnowledgeBaseRecord_SocialActivities)
- [KnowledgeBaseRecord_SyncErrors](#BKMK_KnowledgeBaseRecord_SyncErrors)
- [KnowledgeBaseRecord_Tasks](#BKMK_KnowledgeBaseRecord_Tasks)

### <a name="BKMK_KnowledgeBaseRecord_ActivityPointers"></a> KnowledgeBaseRecord_ActivityPointers

Many-To-One Relationship: [activitypointer KnowledgeBaseRecord_ActivityPointers](activitypointer.md#BKMK_KnowledgeBaseRecord_ActivityPointers)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_ActivityPointers`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgebaserecord_adx_inviteredemptions"></a> knowledgebaserecord_adx_inviteredemptions

Many-To-One Relationship: [adx_inviteredemption knowledgebaserecord_adx_inviteredemptions](adx_inviteredemption.md#BKMK_knowledgebaserecord_adx_inviteredemptions)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgebaserecord_adx_inviteredemptions`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgebaserecord_adx_portalcomments"></a> knowledgebaserecord_adx_portalcomments

Many-To-One Relationship: [adx_portalcomment knowledgebaserecord_adx_portalcomments](adx_portalcomment.md#BKMK_knowledgebaserecord_adx_portalcomments)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgebaserecord_adx_portalcomments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_Annotations"></a> KnowledgeBaseRecord_Annotations

Many-To-One Relationship: [annotation KnowledgeBaseRecord_Annotations](annotation.md#BKMK_KnowledgeBaseRecord_Annotations)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_Annotations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_Appointments"></a> KnowledgeBaseRecord_Appointments

Many-To-One Relationship: [appointment KnowledgeBaseRecord_Appointments](appointment.md#BKMK_KnowledgeBaseRecord_Appointments)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_Appointments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_AsyncOperations"></a> KnowledgeBaseRecord_AsyncOperations

Many-To-One Relationship: [asyncoperation KnowledgeBaseRecord_AsyncOperations](asyncoperation.md#BKMK_KnowledgeBaseRecord_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_BulkDeleteFailures"></a> KnowledgeBaseRecord_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure KnowledgeBaseRecord_BulkDeleteFailures](bulkdeletefailure.md#BKMK_KnowledgeBaseRecord_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_knowledgebaserecord_chats"></a> knowledgebaserecord_chats

Many-To-One Relationship: [chat knowledgebaserecord_chats](chat.md#BKMK_knowledgebaserecord_chats)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`knowledgebaserecord_chats`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_connections1"></a> KnowledgeBaseRecord_connections1

Many-To-One Relationship: [connection KnowledgeBaseRecord_connections1](connection.md#BKMK_KnowledgeBaseRecord_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_connections2"></a> KnowledgeBaseRecord_connections2

Many-To-One Relationship: [connection KnowledgeBaseRecord_connections2](connection.md#BKMK_KnowledgeBaseRecord_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_DuplicateBaseRecord"></a> KnowledgeBaseRecord_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord KnowledgeBaseRecord_DuplicateBaseRecord](duplicaterecord.md#BKMK_KnowledgeBaseRecord_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord"></a> KnowledgeBaseRecord_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord KnowledgeBaseRecord_DuplicateMatchingRecord](duplicaterecord.md#BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_Emails"></a> KnowledgeBaseRecord_Emails

Many-To-One Relationship: [email KnowledgeBaseRecord_Emails](email.md#BKMK_KnowledgeBaseRecord_Emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_Emails`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_Faxes"></a> KnowledgeBaseRecord_Faxes

Many-To-One Relationship: [fax KnowledgeBaseRecord_Faxes](fax.md#BKMK_KnowledgeBaseRecord_Faxes)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_Faxes`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_Letters"></a> KnowledgeBaseRecord_Letters

Many-To-One Relationship: [letter KnowledgeBaseRecord_Letters](letter.md#BKMK_KnowledgeBaseRecord_Letters)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_Letters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_PhoneCalls"></a> KnowledgeBaseRecord_PhoneCalls

Many-To-One Relationship: [phonecall KnowledgeBaseRecord_PhoneCalls](phonecall.md#BKMK_KnowledgeBaseRecord_PhoneCalls)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_PhoneCalls`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess"></a> KnowledgeBaseRecord_PrincipalObjectAttributeAccess

Many-To-One Relationship: [principalobjectattributeaccess KnowledgeBaseRecord_PrincipalObjectAttributeAccess](principalobjectattributeaccess.md#BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_PrincipalObjectAttributeAccess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_ProcessSession"></a> KnowledgeBaseRecord_ProcessSession

Many-To-One Relationship: [processsession KnowledgeBaseRecord_ProcessSession](processsession.md#BKMK_KnowledgeBaseRecord_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters"></a> KnowledgeBaseRecord_RecurringAppointmentMasters

Many-To-One Relationship: [recurringappointmentmaster KnowledgeBaseRecord_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_RecurringAppointmentMasters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_SocialActivities"></a> KnowledgeBaseRecord_SocialActivities

Many-To-One Relationship: [socialactivity KnowledgeBaseRecord_SocialActivities](socialactivity.md#BKMK_KnowledgeBaseRecord_SocialActivities)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_SocialActivities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_SyncErrors"></a> KnowledgeBaseRecord_SyncErrors

Many-To-One Relationship: [syncerror KnowledgeBaseRecord_SyncErrors](syncerror.md#BKMK_KnowledgeBaseRecord_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_KnowledgeBaseRecord_Tasks"></a> KnowledgeBaseRecord_Tasks

Many-To-One Relationship: [task KnowledgeBaseRecord_Tasks](task.md#BKMK_KnowledgeBaseRecord_Tasks)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`KnowledgeBaseRecord_Tasks`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.knowledgebaserecord?displayProperty=fullName>
