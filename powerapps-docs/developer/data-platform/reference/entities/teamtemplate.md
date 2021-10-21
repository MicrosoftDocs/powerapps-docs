---
title: "TeamTemplate table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the TeamTemplate table/entity."
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

# TeamTemplate table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Team template for an entity enabled for automatically created access teams.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|AddUserToRecordTeam|<xref href="Microsoft.Dynamics.CRM.AddUserToRecordTeam?text=AddUserToRecordTeam Action" />|<xref:Microsoft.Crm.Sdk.Messages.AddUserToRecordTeamRequest>|
|Create|POST [*org URI*]/api/data/v9.0/teamtemplates<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/teamtemplates(*teamtemplateid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|RemoveUserFromRecordTeam|<xref href="Microsoft.Dynamics.CRM.RemoveUserFromRecordTeam?text=RemoveUserFromRecordTeam Action" />|<xref:Microsoft.Crm.Sdk.Messages.RemoveUserFromRecordTeamRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/teamtemplates(*teamtemplateid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/teamtemplates<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/teamtemplates(*teamtemplateid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|TeamTemplates|
|DisplayCollectionName|Team templates|
|DisplayName|Team template|
|EntitySetName|teamtemplates|
|IsBPFEntity|False|
|LogicalCollectionName|teamtemplates|
|LogicalName|teamtemplate|
|OwnershipType|None|
|PrimaryIdAttribute|teamtemplateid|
|PrimaryNameAttribute|teamtemplatename|
|SchemaName|TeamTemplate|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DefaultAccessRightsMask](#BKMK_DefaultAccessRightsMask)
- [Description](#BKMK_Description)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [TeamTemplateId](#BKMK_TeamTemplateId)
- [TeamTemplateName](#BKMK_TeamTemplateName)


### <a name="BKMK_DefaultAccessRightsMask"></a> DefaultAccessRightsMask

|Property|Value|
|--------|-----|
|Description|Default access rights mask for the access teams associated with entity instances.|
|DisplayName|Access Rights|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|defaultaccessrightsmask|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Type additional information that describes the team.|
|DisplayName|Description|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Object type code of entity which is enabled for access teams|
|DisplayName|Entity|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|objecttypecode|
|MaxValue|100000|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TeamTemplateId"></a> TeamTemplateId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team template.|
|DisplayName|Primary key for team template|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|teamtemplateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_TeamTemplateName"></a> TeamTemplateName

|Property|Value|
|--------|-----|
|Description|Type the name of the team template.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|teamtemplatename|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsSystem](#BKMK_IsSystem)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [versionnumber](#BKMK_versionnumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the team template.|
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


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the team template was created.|
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
|Description|Unique identifier of the delegate user who created the team template.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsSystem"></a> IsSystem

|Property|Value|
|--------|-----|
|Description|Information about whether this team template is user-defined or system-defined.|
|DisplayName|Is System|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|issystem|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsSystem Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the team template.|
|DisplayName|Modified By|
|IsValidForForm|False|
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


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the team template was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the team template.|
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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_versionnumber"></a> versionnumber

**Added by**: Access Team Solution

|Property|Value|
|--------|-----|
|Description|Version number for team template.|
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

- [teamtemplate_Teams](#BKMK_teamtemplate_Teams)
- [TeamTemplate_SyncErrors](#BKMK_TeamTemplate_SyncErrors)


### <a name="BKMK_teamtemplate_Teams"></a> teamtemplate_Teams

Same as team table [teamtemplate_Teams](team.md#BKMK_teamtemplate_Teams) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|team|
|ReferencingAttribute|teamtemplateid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|teamtemplate_Teams|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_TeamTemplate_SyncErrors"></a> TeamTemplate_SyncErrors

Same as syncerror table [TeamTemplate_SyncErrors](syncerror.md#BKMK_TeamTemplate_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|TeamTemplate_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_teamtemplate_createdonbehalfby](#BKMK_lk_teamtemplate_createdonbehalfby)
- [lk_teamtemplate_modifiedby](#BKMK_lk_teamtemplate_modifiedby)
- [lk_teamtemplate_createdby](#BKMK_lk_teamtemplate_createdby)
- [lk_teamtemplate_modifiedonbehalfby](#BKMK_lk_teamtemplate_modifiedonbehalfby)


### <a name="BKMK_lk_teamtemplate_createdonbehalfby"></a> lk_teamtemplate_createdonbehalfby

See systemuser Table [lk_teamtemplate_createdonbehalfby](systemuser.md#BKMK_lk_teamtemplate_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_teamtemplate_modifiedby"></a> lk_teamtemplate_modifiedby

See systemuser Table [lk_teamtemplate_modifiedby](systemuser.md#BKMK_lk_teamtemplate_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_teamtemplate_createdby"></a> lk_teamtemplate_createdby

See systemuser Table [lk_teamtemplate_createdby](systemuser.md#BKMK_lk_teamtemplate_createdby) One-To-Many relationship.

### <a name="BKMK_lk_teamtemplate_modifiedonbehalfby"></a> lk_teamtemplate_modifiedonbehalfby

See systemuser Table [lk_teamtemplate_modifiedonbehalfby](systemuser.md#BKMK_lk_teamtemplate_modifiedonbehalfby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.teamtemplate?text=teamtemplate EntityType" />