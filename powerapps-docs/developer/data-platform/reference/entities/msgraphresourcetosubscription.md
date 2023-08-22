---
title: "MsGraphResourceToSubscription table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the MsGraphResourceToSubscription table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# MsGraphResourceToSubscription table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

For internal use only. The mapping between Ms Graph Resources and Subscriptions.

**Added by**: msft_ActivitiesInfra_Extensions Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /msgraphresourcetosubscriptions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /msgraphresourcetosubscriptions(*msgraphresourcetosubscriptionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /msgraphresourcetosubscriptions(*msgraphresourcetosubscriptionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /msgraphresourcetosubscriptions<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH /msgraphresourcetosubscriptions(*msgraphresourcetosubscriptionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|MsGraphResourceToSubscriptions|
|DisplayCollectionName|Ms Graph Resource To Subscriptions|
|DisplayName|Ms Graph Resource To Subscription|
|EntitySetName|msgraphresourcetosubscriptions|
|IsBPFEntity|False|
|LogicalCollectionName|msgraphresourcetosubscriptions|
|LogicalName|msgraphresourcetosubscription|
|OwnershipType|None|
|PrimaryIdAttribute|msgraphresourcetosubscriptionid|
|PrimaryNameAttribute|resourceid|
|SchemaName|MsGraphResourceToSubscription|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CreatedInGraphOn](#BKMK_CreatedInGraphOn)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [MsGraphResourceToSubscriptionId](#BKMK_MsGraphResourceToSubscriptionId)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ResourceId](#BKMK_ResourceId)
- [ResourceType](#BKMK_ResourceType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [SubscriptionId](#BKMK_SubscriptionId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_CreatedInGraphOn"></a> CreatedInGraphOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|TimeZoneIndependent|
|Description|For internal use only. Date and time when the record was created in Graph.|
|DisplayName|Created In Graph On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|createdingraphon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_MsGraphResourceToSubscriptionId"></a> MsGraphResourceToSubscriptionId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Ms Graph Resource To Subscription|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msgraphresourcetosubscriptionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ResourceId"></a> ResourceId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Resource Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|resourceid|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ResourceType"></a> ResourceType

|Property|Value|
|--------|-----|
|Description|For internal use only. Shows the different options for resource type.|
|DisplayName|Resource Type|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|resourcetype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ResourceType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Teams Chat Messages||



### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Ms Graph Resource To Subscription|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Ms Graph Resource To Subscription|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_SubscriptionId"></a> SubscriptionId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Subscription Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|subscriptionid|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version Number|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [msgraphresourcetosubscription_SyncErrors](#BKMK_msgraphresourcetosubscription_SyncErrors)
- [msgraphresourcetosubscription_AsyncOperations](#BKMK_msgraphresourcetosubscription_AsyncOperations)
- [msgraphresourcetosubscription_MailboxTrackingFolders](#BKMK_msgraphresourcetosubscription_MailboxTrackingFolders)
- [msgraphresourcetosubscription_ProcessSession](#BKMK_msgraphresourcetosubscription_ProcessSession)
- [msgraphresourcetosubscription_BulkDeleteFailures](#BKMK_msgraphresourcetosubscription_BulkDeleteFailures)
- [msgraphresourcetosubscription_PrincipalObjectAttributeAccesses](#BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses)


### <a name="BKMK_msgraphresourcetosubscription_SyncErrors"></a> msgraphresourcetosubscription_SyncErrors

**Added by**: System Solution Solution

Same as the [msgraphresourcetosubscription_SyncErrors](syncerror.md#BKMK_msgraphresourcetosubscription_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msgraphresourcetosubscription_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msgraphresourcetosubscription_AsyncOperations"></a> msgraphresourcetosubscription_AsyncOperations

**Added by**: System Solution Solution

Same as the [msgraphresourcetosubscription_AsyncOperations](asyncoperation.md#BKMK_msgraphresourcetosubscription_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msgraphresourcetosubscription_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msgraphresourcetosubscription_MailboxTrackingFolders"></a> msgraphresourcetosubscription_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msgraphresourcetosubscription_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msgraphresourcetosubscription_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msgraphresourcetosubscription_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msgraphresourcetosubscription_ProcessSession"></a> msgraphresourcetosubscription_ProcessSession

**Added by**: System Solution Solution

Same as the [msgraphresourcetosubscription_ProcessSession](processsession.md#BKMK_msgraphresourcetosubscription_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msgraphresourcetosubscription_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msgraphresourcetosubscription_BulkDeleteFailures"></a> msgraphresourcetosubscription_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msgraphresourcetosubscription_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msgraphresourcetosubscription_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msgraphresourcetosubscription_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses"></a> msgraphresourcetosubscription_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msgraphresourcetosubscription_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msgraphresourcetosubscription_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msgraphresourcetosubscription_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msgraphresourcetosubscription?text=msgraphresourcetosubscription EntityType" />