---
title: "Saved View (UserQuery) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Saved View (UserQuery) table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Saved View (UserQuery) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Saved database query that is owned by a user.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/userqueries(*userqueryid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/userqueries<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/userqueries(*userqueryid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|ExecuteByIdUserQuery|[Retrieve and execute predefined queries](/powerapps/developer/common-data-service/webapi/retrieve-and-execute-predefined-queries)|<xref:Microsoft.Crm.Sdk.Messages.ExecuteByIdUserQueryRequest>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/userqueries(*userqueryid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/userqueries<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/userqueries(*userqueryid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/userqueries(*userqueryid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|UserQueries|
|DisplayCollectionName|Saved Views|
|DisplayName|Saved View|
|EntitySetName|userqueries|
|IsBPFEntity|False|
|LogicalCollectionName|userqueries|
|LogicalName|userquery|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|userqueryid|
|PrimaryNameAttribute|name|
|SchemaName|UserQuery|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdvancedGroupBy](#BKMK_AdvancedGroupBy)
- [ColumnSetXml](#BKMK_ColumnSetXml)
- [ConditionalFormatting](#BKMK_ConditionalFormatting)
- [Description](#BKMK_Description)
- [FetchXml](#BKMK_FetchXml)
- [LayoutJson](#BKMK_LayoutJson)
- [LayoutXml](#BKMK_LayoutXml)
- [Name](#BKMK_Name)
- [OfflineSqlQuery](#BKMK_OfflineSqlQuery)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ParentQueryId](#BKMK_ParentQueryId)
- [QueryType](#BKMK_QueryType)
- [ReturnedTypeCode](#BKMK_ReturnedTypeCode)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [UserQueryId](#BKMK_UserQueryId)


### <a name="BKMK_AdvancedGroupBy"></a> AdvancedGroupBy

|Property|Value|
|--------|-----|
|Description|Type the column name that will be used to group the results from the data collected across multiple records from a user view.|
|DisplayName|Advanced Group By|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|advancedgroupby|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ColumnSetXml"></a> ColumnSetXml

|Property|Value|
|--------|-----|
|Description|Shows the columns and sorting criteria for the saved view, stored in XML format.|
|DisplayName|Column Set XML|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|columnsetxml|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ConditionalFormatting"></a> ConditionalFormatting

|Property|Value|
|--------|-----|
|Description|Type information about how the items in the user view are formatted.|
|DisplayName|User Group By|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|conditionalformatting|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Type additional information to describe the saved view, such as the filter criteria or intended results set.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_FetchXml"></a> FetchXml

|Property|Value|
|--------|-----|
|Description|Contains the Fetch XML query that defines the entities and attributes included in the saved view.|
|DisplayName|Fetch XML|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|fetchxml|
|MaxLength|1073741823|
|RequiredLevel|SystemRequired|
|Type|Memo|


### <a name="BKMK_LayoutJson"></a> LayoutJson

|Property|Value|
|--------|-----|
|Description|Layout data in JSON format.|
|DisplayName|Layout data in JSON format.|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|layoutjson|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_LayoutXml"></a> LayoutXml

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Layout XML|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|layoutxml|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Type a descriptive name for the saved view.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|200|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OfflineSqlQuery"></a> OfflineSqlQuery

|Property|Value|
|--------|-----|
|Description|String specifying the corresponding sql query for the fetch xml specified for offline use.|
|DisplayName|Offline SQL Query|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|offlinesqlquery|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description|Type of the owner of the saved view, such as user, team, or business unit.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_ParentQueryId"></a> ParentQueryId

|Property|Value|
|--------|-----|
|Description|Choose the ID of the saved query that the record was created from.|
|DisplayName|Parent Query|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentqueryid|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_QueryType"></a> QueryType

|Property|Value|
|--------|-----|
|Description|Shows the code for the query type to indicate whether the saved view is an address book filter, advanced search, or other view.|
|DisplayName|Query Type|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|querytype|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_ReturnedTypeCode"></a> ReturnedTypeCode

|Property|Value|
|--------|-----|
|Description|Type of entity that the saved view displays.|
|DisplayName|Returned Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|returnedtypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows whether the saved view is active or inactive.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Select the item's status.|
|DisplayName|Status Reason|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|
|3|All|0|



### <a name="BKMK_UserQueryId"></a> UserQueryId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the saved view.|
|DisplayName|User Query|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|userqueryid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
|DisplayName|Created By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|SystemRequired|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description|Name of the user who created the saved view.|
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
|Description|YomiName of the user who created the saved view.|
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
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record on behalf of another user.|
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|SystemRequired|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description|Name of the user who last modified the saved view.|
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
|Description|YomiName of the user who last modified the saved view.|
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
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Last Modified|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record on behalf of another user.|
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
|Description|Name of the owner of the saved view.|
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
|Description|Shows the business unit that the record owner belongs to.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns this saved view.|
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
|Description|Unique identifier of the user who owns this saved view.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the saved view.|
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

- [UserQuery_BulkDeleteFailures](#BKMK_UserQuery_BulkDeleteFailures)
- [UserQuery_SyncErrors](#BKMK_UserQuery_SyncErrors)
- [UserQuery_AsyncOperations](#BKMK_UserQuery_AsyncOperations)


### <a name="BKMK_UserQuery_BulkDeleteFailures"></a> UserQuery_BulkDeleteFailures

Same as bulkdeletefailure table [UserQuery_BulkDeleteFailures](bulkdeletefailure.md#BKMK_UserQuery_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|UserQuery_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_UserQuery_SyncErrors"></a> UserQuery_SyncErrors

Same as syncerror table [UserQuery_SyncErrors](syncerror.md#BKMK_UserQuery_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|UserQuery_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_UserQuery_AsyncOperations"></a> UserQuery_AsyncOperations

Same as asyncoperation table [UserQuery_AsyncOperations](asyncoperation.md#BKMK_UserQuery_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|UserQuery_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_userquery_modifiedonbehalfby](#BKMK_lk_userquery_modifiedonbehalfby)
- [business_unit_userquery](#BKMK_business_unit_userquery)
- [user_userquery](#BKMK_user_userquery)
- [team_userquery](#BKMK_team_userquery)
- [lk_userquery_modifiedby](#BKMK_lk_userquery_modifiedby)
- [lk_userquery_createdby](#BKMK_lk_userquery_createdby)
- [lk_userquery_createdonbehalfby](#BKMK_lk_userquery_createdonbehalfby)


### <a name="BKMK_lk_userquery_modifiedonbehalfby"></a> lk_userquery_modifiedonbehalfby

See systemuser Table [lk_userquery_modifiedonbehalfby](systemuser.md#BKMK_lk_userquery_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_business_unit_userquery"></a> business_unit_userquery

See businessunit Table [business_unit_userquery](businessunit.md#BKMK_business_unit_userquery) One-To-Many relationship.

### <a name="BKMK_user_userquery"></a> user_userquery

See systemuser Table [user_userquery](systemuser.md#BKMK_user_userquery) One-To-Many relationship.

### <a name="BKMK_team_userquery"></a> team_userquery

See team Table [team_userquery](team.md#BKMK_team_userquery) One-To-Many relationship.

### <a name="BKMK_lk_userquery_modifiedby"></a> lk_userquery_modifiedby

See systemuser Table [lk_userquery_modifiedby](systemuser.md#BKMK_lk_userquery_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_userquery_createdby"></a> lk_userquery_createdby

See systemuser Table [lk_userquery_createdby](systemuser.md#BKMK_lk_userquery_createdby) One-To-Many relationship.

### <a name="BKMK_lk_userquery_createdonbehalfby"></a> lk_userquery_createdonbehalfby

See systemuser Table [lk_userquery_createdonbehalfby](systemuser.md#BKMK_lk_userquery_createdonbehalfby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.userquery?text=userquery EntityType" />