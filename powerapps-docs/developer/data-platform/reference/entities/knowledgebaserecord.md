---
title: "KnowledgeBaseRecord table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the KnowledgeBaseRecord table/entity."
ms.date: 05/20/2021
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

# KnowledgeBaseRecord table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Metadata of knowledge base (KB) articles associated with Microsoft Dynamics 365 entities.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/knowledgebaserecords(*knowledgebaserecordid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/knowledgebaserecords<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/knowledgebaserecords(*knowledgebaserecordid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/knowledgebaserecords(*knowledgebaserecordid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/knowledgebaserecords<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/knowledgebaserecords(*knowledgebaserecordid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/knowledgebaserecords(*knowledgebaserecordid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|KnowledgeBaseRecords|
|DisplayCollectionName|Knowledge Base Records|
|DisplayName|Knowledge Base Record|
|EntitySetName|knowledgebaserecords|
|IsBPFEntity|False|
|LogicalCollectionName|knowledgebaserecords|
|LogicalName|knowledgebaserecord|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|knowledgebaserecordid|
|PrimaryNameAttribute|title|
|SchemaName|KnowledgeBaseRecord|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|This field will be used to store the Unique ID of the associated Knowledge Base records|
|DisplayName|ID|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|knowledgebaserecordid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_PrivateUrl"></a> PrivateUrl

|Property|Value|
|--------|-----|
|Description|Shows the internal Parature service desk URL of the knowledge base records.|
|DisplayName|Private URL|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|privateurl|
|MaxLength|256|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_PublicUrl"></a> PublicUrl

|Property|Value|
|--------|-----|
|Description|Shows the public Parature portal URL of the knowledge base records.|
|DisplayName|Public URL|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|publicurl|
|MaxLength|256|
|RequiredLevel|None|
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


### <a name="BKMK_Title"></a> Title

|Property|Value|
|--------|-----|
|Description|Shows the title of the knowledge base (KB) Record.|
|DisplayName|KB Record Title|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|title|
|MaxLength|4000|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the Knowledge Base Record with respect to the base currency.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_UniqueId"></a> UniqueId

|Property|Value|
|--------|-----|
|Description|Shows the unique ID of the linked knowledge base (KB) article.|
|DisplayName|Unique ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|uniqueid|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|

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
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the knowledge base record with respect to the base currency.|
|DisplayName|ExchangeRate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.0000000001|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
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

- [KnowledgeBaseRecord_ActivityPointers](#BKMK_KnowledgeBaseRecord_ActivityPointers)
- [KnowledgeBaseRecord_Appointments](#BKMK_KnowledgeBaseRecord_Appointments)
- [KnowledgeBaseRecord_Emails](#BKMK_KnowledgeBaseRecord_Emails)
- [KnowledgeBaseRecord_Faxes](#BKMK_KnowledgeBaseRecord_Faxes)
- [KnowledgeBaseRecord_Letters](#BKMK_KnowledgeBaseRecord_Letters)
- [KnowledgeBaseRecord_PhoneCalls](#BKMK_KnowledgeBaseRecord_PhoneCalls)
- [KnowledgeBaseRecord_Tasks](#BKMK_KnowledgeBaseRecord_Tasks)
- [KnowledgeBaseRecord_RecurringAppointmentMasters](#BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters)
- [KnowledgeBaseRecord_SocialActivities](#BKMK_KnowledgeBaseRecord_SocialActivities)
- [KnowledgeBaseRecord_connections1](#BKMK_KnowledgeBaseRecord_connections1)
- [KnowledgeBaseRecord_connections2](#BKMK_KnowledgeBaseRecord_connections2)
- [KnowledgeBaseRecord_DuplicateMatchingRecord](#BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord)
- [KnowledgeBaseRecord_DuplicateBaseRecord](#BKMK_KnowledgeBaseRecord_DuplicateBaseRecord)
- [KnowledgeBaseRecord_Annotations](#BKMK_KnowledgeBaseRecord_Annotations)
- [KnowledgeBaseRecord_AsyncOperations](#BKMK_KnowledgeBaseRecord_AsyncOperations)
- [KnowledgeBaseRecord_ProcessSession](#BKMK_KnowledgeBaseRecord_ProcessSession)
- [KnowledgeBaseRecord_BulkDeleteFailures](#BKMK_KnowledgeBaseRecord_BulkDeleteFailures)
- [KnowledgeBaseRecord_PrincipalObjectAttributeAccess](#BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess)
- [KnowledgeBaseRecord_SyncErrors](#BKMK_KnowledgeBaseRecord_SyncErrors)


### <a name="BKMK_KnowledgeBaseRecord_ActivityPointers"></a> KnowledgeBaseRecord_ActivityPointers

Same as activitypointer table [KnowledgeBaseRecord_ActivityPointers](activitypointer.md#BKMK_KnowledgeBaseRecord_ActivityPointers) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_ActivityPointers|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_Appointments"></a> KnowledgeBaseRecord_Appointments

Same as appointment table [KnowledgeBaseRecord_Appointments](appointment.md#BKMK_KnowledgeBaseRecord_Appointments) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_Appointments|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_Emails"></a> KnowledgeBaseRecord_Emails

Same as email table [KnowledgeBaseRecord_Emails](email.md#BKMK_KnowledgeBaseRecord_Emails) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_Emails|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_Faxes"></a> KnowledgeBaseRecord_Faxes

Same as fax table [KnowledgeBaseRecord_Faxes](fax.md#BKMK_KnowledgeBaseRecord_Faxes) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_Faxes|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_Letters"></a> KnowledgeBaseRecord_Letters

Same as letter table [KnowledgeBaseRecord_Letters](letter.md#BKMK_KnowledgeBaseRecord_Letters) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_Letters|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_PhoneCalls"></a> KnowledgeBaseRecord_PhoneCalls

Same as phonecall table [KnowledgeBaseRecord_PhoneCalls](phonecall.md#BKMK_KnowledgeBaseRecord_PhoneCalls) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_PhoneCalls|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_Tasks"></a> KnowledgeBaseRecord_Tasks

Same as task table [KnowledgeBaseRecord_Tasks](task.md#BKMK_KnowledgeBaseRecord_Tasks) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_Tasks|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters"></a> KnowledgeBaseRecord_RecurringAppointmentMasters

Same as recurringappointmentmaster table [KnowledgeBaseRecord_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_KnowledgeBaseRecord_RecurringAppointmentMasters) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_RecurringAppointmentMasters|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_SocialActivities"></a> KnowledgeBaseRecord_SocialActivities

Same as socialactivity table [KnowledgeBaseRecord_SocialActivities](socialactivity.md#BKMK_KnowledgeBaseRecord_SocialActivities) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_SocialActivities|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_connections1"></a> KnowledgeBaseRecord_connections1

Same as connection table [KnowledgeBaseRecord_connections1](connection.md#BKMK_KnowledgeBaseRecord_connections1) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_connections2"></a> KnowledgeBaseRecord_connections2

Same as connection table [KnowledgeBaseRecord_connections2](connection.md#BKMK_KnowledgeBaseRecord_connections2) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_connections2|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord"></a> KnowledgeBaseRecord_DuplicateMatchingRecord

Same as duplicaterecord table [KnowledgeBaseRecord_DuplicateMatchingRecord](duplicaterecord.md#BKMK_KnowledgeBaseRecord_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_DuplicateBaseRecord"></a> KnowledgeBaseRecord_DuplicateBaseRecord

Same as duplicaterecord table [KnowledgeBaseRecord_DuplicateBaseRecord](duplicaterecord.md#BKMK_KnowledgeBaseRecord_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_Annotations"></a> KnowledgeBaseRecord_Annotations

Same as annotation table [KnowledgeBaseRecord_Annotations](annotation.md#BKMK_KnowledgeBaseRecord_Annotations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_Annotations|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_AsyncOperations"></a> KnowledgeBaseRecord_AsyncOperations

Same as asyncoperation table [KnowledgeBaseRecord_AsyncOperations](asyncoperation.md#BKMK_KnowledgeBaseRecord_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_ProcessSession"></a> KnowledgeBaseRecord_ProcessSession

Same as processsession table [KnowledgeBaseRecord_ProcessSession](processsession.md#BKMK_KnowledgeBaseRecord_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_ProcessSession|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_BulkDeleteFailures"></a> KnowledgeBaseRecord_BulkDeleteFailures

Same as bulkdeletefailure table [KnowledgeBaseRecord_BulkDeleteFailures](bulkdeletefailure.md#BKMK_KnowledgeBaseRecord_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess"></a> KnowledgeBaseRecord_PrincipalObjectAttributeAccess

Same as principalobjectattributeaccess table [KnowledgeBaseRecord_PrincipalObjectAttributeAccess](principalobjectattributeaccess.md#BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_PrincipalObjectAttributeAccess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_KnowledgeBaseRecord_SyncErrors"></a> KnowledgeBaseRecord_SyncErrors

Same as syncerror table [KnowledgeBaseRecord_SyncErrors](syncerror.md#BKMK_KnowledgeBaseRecord_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|KnowledgeBaseRecord_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_KnowledgeBaseRecord_createdby](#BKMK_lk_KnowledgeBaseRecord_createdby)
- [lk_KnowledgeBaseRecord_createdonbehalfby](#BKMK_lk_KnowledgeBaseRecord_createdonbehalfby)
- [lk_KnowledgeBaseRecord_modifiedby](#BKMK_lk_KnowledgeBaseRecord_modifiedby)
- [lk_KnowledgeBaseRecord_modifiedonbehalfby](#BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby)
- [organization_KnowledgeBaseRecord](#BKMK_organization_KnowledgeBaseRecord)
- [TransactionCurrency_KnowledgeBaseRecord](#BKMK_TransactionCurrency_KnowledgeBaseRecord)


### <a name="BKMK_lk_KnowledgeBaseRecord_createdby"></a> lk_KnowledgeBaseRecord_createdby

See systemuser Table [lk_KnowledgeBaseRecord_createdby](systemuser.md#BKMK_lk_KnowledgeBaseRecord_createdby) One-To-Many relationship.

### <a name="BKMK_lk_KnowledgeBaseRecord_createdonbehalfby"></a> lk_KnowledgeBaseRecord_createdonbehalfby

See systemuser Table [lk_KnowledgeBaseRecord_createdonbehalfby](systemuser.md#BKMK_lk_KnowledgeBaseRecord_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_KnowledgeBaseRecord_modifiedby"></a> lk_KnowledgeBaseRecord_modifiedby

See systemuser Table [lk_KnowledgeBaseRecord_modifiedby](systemuser.md#BKMK_lk_KnowledgeBaseRecord_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby"></a> lk_KnowledgeBaseRecord_modifiedonbehalfby

See systemuser Table [lk_KnowledgeBaseRecord_modifiedonbehalfby](systemuser.md#BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_KnowledgeBaseRecord"></a> organization_KnowledgeBaseRecord

See organization Table [organization_KnowledgeBaseRecord](organization.md#BKMK_organization_KnowledgeBaseRecord) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_KnowledgeBaseRecord"></a> TransactionCurrency_KnowledgeBaseRecord

See transactioncurrency Table [TransactionCurrency_KnowledgeBaseRecord](transactioncurrency.md#BKMK_TransactionCurrency_KnowledgeBaseRecord) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.knowledgebaserecord?text=knowledgebaserecord EntityType" />