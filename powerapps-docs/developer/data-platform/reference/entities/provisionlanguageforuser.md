---
title: "ProvisionLanguageForUser entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the ProvisionLanguageForUser table."
ms.date: 11/14/2020
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# ProvisionLanguageForUser entity reference

> [!NOTE]
> Effective Nov 2020, Common Data Service has been renamed to [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro).



**Added by**: msft_LocalizationExtension Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/provisionlanguageforusers<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/provisionlanguageforusers(*provisionlanguageforuserid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref href="Microsoft.Dynamics.CRM.IsValidStateTransition?text=IsValidStateTransition Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/provisionlanguageforusers(*provisionlanguageforuserid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/provisionlanguageforusers<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetState|PATCH [*org URI*]/api/data/v9.0/provisionlanguageforusers(*provisionlanguageforuserid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/provisionlanguageforusers(*provisionlanguageforuserid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Entity properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|ProvisionLanguageForUsers|
|DisplayCollectionName|ProvisionLanguageForUser|
|DisplayName|ProvisionLanguageForUser|
|EntitySetName|provisionlanguageforusers|
|IsBPFEntity|False|
|LogicalCollectionName|provisionlanguageforusers|
|LogicalName|provisionlanguageforuser|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|provisionlanguageforuserid|
|PrimaryNameAttribute|name|
|SchemaName|ProvisionLanguageForUser|

<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncOperationId](#BKMK_AsyncOperationId)
- [Lcid](#BKMK_Lcid)
- [Name](#BKMK_Name)
- [OperationStatus](#BKMK_OperationStatus)
- [ProvisionLanguageForUserId](#BKMK_ProvisionLanguageForUserId)
- [UserId](#BKMK_UserId)


### <a name="BKMK_AsyncOperationId"></a> AsyncOperationId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|AsyncOperationId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|asyncoperationid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_Lcid"></a> Lcid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Lcid|
|Format|Locale|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lcid|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_OperationStatus"></a> OperationStatus

|Property|Value|
|--------|-----|
|Description||
|DisplayName|OperationStatus|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|operationstatus|
|RequiredLevel|None|
|Type|Picklist|

#### OperationStatus Options

|Value|Label|
|-----|-----|
|0|Queued|
|1|Completed|
|2|Waiting For Language Provision|
|3|Failed|



### <a name="BKMK_ProvisionLanguageForUserId"></a> ProvisionLanguageForUserId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|ProvisionLanguageForUser|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|provisionlanguageforuserid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_UserId"></a> UserId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|UserId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|userid|
|RequiredLevel|None|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only attributes

These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Type|Uniqueidentifier|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [provisionlanguageforuser_SyncErrors](#BKMK_provisionlanguageforuser_SyncErrors)
- [provisionlanguageforuser_AsyncOperations](#BKMK_provisionlanguageforuser_AsyncOperations)
- [provisionlanguageforuser_MailboxTrackingFolders](#BKMK_provisionlanguageforuser_MailboxTrackingFolders)
- [provisionlanguageforuser_ProcessSession](#BKMK_provisionlanguageforuser_ProcessSession)
- [provisionlanguageforuser_BulkDeleteFailures](#BKMK_provisionlanguageforuser_BulkDeleteFailures)
- [provisionlanguageforuser_PrincipalObjectAttributeAccesses](#BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses)


### <a name="BKMK_provisionlanguageforuser_SyncErrors"></a> provisionlanguageforuser_SyncErrors

**Added by**: System Solution Solution

Same as syncerror entity [provisionlanguageforuser_SyncErrors](syncerror.md#BKMK_provisionlanguageforuser_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|provisionlanguageforuser_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_provisionlanguageforuser_AsyncOperations"></a> provisionlanguageforuser_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation entity [provisionlanguageforuser_AsyncOperations](asyncoperation.md#BKMK_provisionlanguageforuser_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|provisionlanguageforuser_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_provisionlanguageforuser_MailboxTrackingFolders"></a> provisionlanguageforuser_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder entity [provisionlanguageforuser_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_provisionlanguageforuser_MailboxTrackingFolders) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|provisionlanguageforuser_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_provisionlanguageforuser_ProcessSession"></a> provisionlanguageforuser_ProcessSession

**Added by**: System Solution Solution

Same as processsession entity [provisionlanguageforuser_ProcessSession](processsession.md#BKMK_provisionlanguageforuser_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|provisionlanguageforuser_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_provisionlanguageforuser_BulkDeleteFailures"></a> provisionlanguageforuser_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure entity [provisionlanguageforuser_BulkDeleteFailures](bulkdeletefailure.md#BKMK_provisionlanguageforuser_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|provisionlanguageforuser_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses"></a> provisionlanguageforuser_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess entity [provisionlanguageforuser_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_provisionlanguageforuser_PrincipalObjectAttributeAccesses) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|provisionlanguageforuser_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### See also

[About entity reference](../about-entity-reference.md)<br />
[Web API reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.provisionlanguageforuser?text=provisionlanguageforuser EntityType" />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]