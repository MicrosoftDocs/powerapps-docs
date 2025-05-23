---
title: "ProvisionLanguageForUser table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the ProvisionLanguageForUser table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# ProvisionLanguageForUser table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the ProvisionLanguageForUser table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /provisionlanguageforusers<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /provisionlanguageforusers(*provisionlanguageforuserid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /provisionlanguageforusers(*provisionlanguageforuserid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /provisionlanguageforusers<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /provisionlanguageforusers(*provisionlanguageforuserid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /provisionlanguageforusers(*provisionlanguageforuserid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /provisionlanguageforusers(*provisionlanguageforuserid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the ProvisionLanguageForUser table.

|Property|Value|
| --- | --- |
| **DisplayName** | **ProvisionLanguageForUser** |
| **DisplayCollectionName** | **ProvisionLanguageForUser** |
| **SchemaName** | `ProvisionLanguageForUser` |
| **CollectionSchemaName** | `ProvisionLanguageForUsers` |
| **EntitySetName** | `provisionlanguageforusers`|
| **LogicalName** | `provisionlanguageforuser` |
| **LogicalCollectionName** | `provisionlanguageforusers` |
| **PrimaryIdAttribute** | `provisionlanguageforuserid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncOperationId](#BKMK_AsyncOperationId)
- [Lcid](#BKMK_Lcid)
- [Name](#BKMK_Name)
- [OperationStatus](#BKMK_OperationStatus)
- [ProvisionLanguageForUserId](#BKMK_ProvisionLanguageForUserId)
- [UserId](#BKMK_UserId)

### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|---|---|
|Description||
|DisplayName|**AsyncOperationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`asyncoperationid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Lcid"></a> Lcid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Lcid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lcid`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_Name"></a> Name

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
|MaxLength|100|

### <a name="BKMK_OperationStatus"></a> OperationStatus

|Property|Value|
|---|---|
|Description||
|DisplayName|**OperationStatus**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operationstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|356770000|
|GlobalChoiceName|`provisionlanguageforuser_operationstatus`|

#### OperationStatus Choices/Options

|Value|Label|
|---|---|
|0|**Queued**|
|1|**Completed**|
|2|**Waiting For Language Provision**|
|3|**Failed**|

### <a name="BKMK_ProvisionLanguageForUserId"></a> ProvisionLanguageForUserId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**ProvisionLanguageForUser**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`provisionlanguageforuserid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_UserId"></a> UserId

|Property|Value|
|---|---|
|Description||
|DisplayName|**UserId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`userid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [provisionlanguageforuser_AsyncOperations](#BKMK_provisionlanguageforuser_AsyncOperations)
- [provisionlanguageforuser_BulkDeleteFailures](#BKMK_provisionlanguageforuser_BulkDeleteFailures)
- [provisionlanguageforuser_MailboxTrackingFolders](#BKMK_provisionlanguageforuser_MailboxTrackingFolders)
- [provisionlanguageforuser_PrincipalObjectAttributeAccesses](#BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses)
- [provisionlanguageforuser_ProcessSession](#BKMK_provisionlanguageforuser_ProcessSession)
- [provisionlanguageforuser_SyncErrors](#BKMK_provisionlanguageforuser_SyncErrors)

### <a name="BKMK_provisionlanguageforuser_AsyncOperations"></a> provisionlanguageforuser_AsyncOperations

Many-To-One Relationship: [asyncoperation provisionlanguageforuser_AsyncOperations](asyncoperation.md#BKMK_provisionlanguageforuser_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`provisionlanguageforuser_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_provisionlanguageforuser_BulkDeleteFailures"></a> provisionlanguageforuser_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure provisionlanguageforuser_BulkDeleteFailures](bulkdeletefailure.md#BKMK_provisionlanguageforuser_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`provisionlanguageforuser_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_provisionlanguageforuser_MailboxTrackingFolders"></a> provisionlanguageforuser_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder provisionlanguageforuser_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_provisionlanguageforuser_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`provisionlanguageforuser_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses"></a> provisionlanguageforuser_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess provisionlanguageforuser_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`provisionlanguageforuser_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_provisionlanguageforuser_ProcessSession"></a> provisionlanguageforuser_ProcessSession

Many-To-One Relationship: [processsession provisionlanguageforuser_ProcessSession](processsession.md#BKMK_provisionlanguageforuser_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`provisionlanguageforuser_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_provisionlanguageforuser_SyncErrors"></a> provisionlanguageforuser_SyncErrors

Many-To-One Relationship: [syncerror provisionlanguageforuser_SyncErrors](syncerror.md#BKMK_provisionlanguageforuser_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`provisionlanguageforuser_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.provisionlanguageforuser?displayProperty=fullName>
