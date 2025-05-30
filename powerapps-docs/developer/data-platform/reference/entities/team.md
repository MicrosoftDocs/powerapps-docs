---
title: "Team table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Team table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Team table/entity reference (Microsoft Dataverse)

Collection of system users that routinely collaborate. Teams can be used to simplify record sharing and provide team members with common access to organization data when team members belong to different Business Units.

## Messages

The following table lists the messages for the Team table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `AddMembersTeam`<br />Event: True |<xref:Microsoft.Dynamics.CRM.AddMembersTeam?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.AddMembersTeamRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `ConvertOwnerTeamToAccessTeam`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ConvertOwnerTeamToAccessTeam?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ConvertOwnerTeamToAccessTeamRequest>|
| `Create`<br />Event: True |`POST` /teams<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /teams(*teamid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RemoveMembersTeam`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RemoveMembersTeam?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RemoveMembersTeamRequest>|
| `Retrieve`<br />Event: True |`GET` /teams(*teamid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMembersTeam`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.RetrieveMembersTeamRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /teams<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetParentBusinessUnit`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.SetParentBusinessUnitRequest>|
| `SetParentSystemUser`<br />Event: False |<xref:Microsoft.Dynamics.CRM.SetParentSystemUser?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SetParentSystemUserRequest>|
| `SetParentTeam`<br />Event: False |<xref:Microsoft.Dynamics.CRM.SetParentTeam?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SetParentTeamRequest>|
| `SyncGroupMembersToTeam`<br />Event: False |<xref:Microsoft.Dynamics.CRM.SyncGroupMembersToTeam?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Update`<br />Event: True |`PATCH` /teams(*teamid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /teams(*teamid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Team table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Team** |
| **DisplayCollectionName** | **Teams** |
| **SchemaName** | `Team` |
| **CollectionSchemaName** | `Teams` |
| **EntitySetName** | `teams`|
| **LogicalName** | `team` |
| **LogicalCollectionName** | `teams` |
| **PrimaryIdAttribute** | `teamid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `BusinessOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdministratorId](#BKMK_AdministratorId)
- [AzureActiveDirectoryObjectId](#BKMK_AzureActiveDirectoryObjectId)
- [BusinessUnitId](#BKMK_BusinessUnitId)
- [DelegatedAuthorizationId](#BKMK_DelegatedAuthorizationId)
- [Description](#BKMK_Description)
- [EMailAddress](#BKMK_EMailAddress)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [MembershipType](#BKMK_MembershipType)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ProcessId](#BKMK_ProcessId)
- [QueueId](#BKMK_QueueId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [StageId](#BKMK_StageId)
- [TeamId](#BKMK_TeamId)
- [TeamTemplateId](#BKMK_TeamTemplateId)
- [TeamType](#BKMK_TeamType)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)
- [YomiName](#BKMK_YomiName)

### <a name="BKMK_AdministratorId"></a> AdministratorId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user primary responsible for the team.**|
|DisplayName|**Administrator**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`administratorid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_AzureActiveDirectoryObjectId"></a> AzureActiveDirectoryObjectId

|Property|Value|
|---|---|
|Description|**The object Id for a group.**|
|DisplayName|**Object Id for a group**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`azureactivedirectoryobjectid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit with which the team is associated.**|
|DisplayName|**Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessunitid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_DelegatedAuthorizationId"></a> DelegatedAuthorizationId

|Property|Value|
|---|---|
|Description|**The delegated authorization context for the team.**|
|DisplayName|**Delegated authorization**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`delegatedauthorizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|delegatedauthorization|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the team.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_EMailAddress"></a> EMailAddress

|Property|Value|
|---|---|
|Description|**Email address for the team.**|
|DisplayName|**Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Email|
|FormatName|Email|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Unique identifier of the data import or data migration that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_MembershipType"></a> MembershipType

|Property|Value|
|---|---|
|Description||
|DisplayName|**Membership Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`membershiptype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`team_membershiptype`|

#### MembershipType Choices/Options

|Value|Label|
|---|---|
|0|**Members and guests**|
|1|**Members**|
|2|**Owners**|
|3|**Guests**|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the team.**|
|DisplayName|**Team Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

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

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**Shows the ID of the process.**|
|DisplayName|**Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_QueueId"></a> QueueId

|Property|Value|
|---|---|
|Description|**Unique identifier of the default queue for the team.**|
|DisplayName|**Default Queue**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`queueid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|queue|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Choose the record that the team relates to.**|
|DisplayName|**Regarding Object Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|knowledgearticle|

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description|**Type of the associated record for team - used for system managed access teams only.**|
|DisplayName|**Regarding Object Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|---|---|
|Description|**Shows the ID of the stage.**|
|DisplayName|**(Deprecated) Process Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_TeamId"></a> TeamId

|Property|Value|
|---|---|
|Description|**Unique identifier for the team.**|
|DisplayName|**Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`teamid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_TeamTemplateId"></a> TeamTemplateId

|Property|Value|
|---|---|
|Description|**Shows the team template that is associated with the team.**|
|DisplayName|**Team Template Identifier**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`teamtemplateid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|teamtemplate|

### <a name="BKMK_TeamType"></a> TeamType

|Property|Value|
|---|---|
|Description|**Select the team type.**|
|DisplayName|**Team Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`teamtype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`team_type`|

#### TeamType Choices/Options

|Value|Label|
|---|---|
|0|**Owner**|
|1|**Access**|
|2|**Security Group**|
|3|**Office Group**|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the currency associated with the team.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**(Deprecated) Traversed Path**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`traversedpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|

### <a name="BKMK_YomiName"></a> YomiName

|Property|Value|
|---|---|
|Description|**Pronunciation of the full name of the team, written in phonetic hiragana or katakana characters.**|
|DisplayName|**Yomi Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`yominame`|
|RequiredLevel|None|
|Type|String|
|Format|PhoneticGuide|
|FormatName|PhoneticGuide|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|160|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsDefault](#BKMK_IsDefault)
- [IsSasTokenSet](#BKMK_IsSasTokenSet)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [SasToken](#BKMK_SasToken)
- [ShareLinkQualifier](#BKMK_ShareLinkQualifier)
- [SystemManaged](#BKMK_SystemManaged)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the team.**|
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
|Description|**Date and time when the team was created.**|
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
|Description|**Unique identifier of the delegate user who created the team.**|
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
|Description|**Exchange rate for the currency associated with the team with respect to the base currency.**|
|DisplayName|**Exchange Rate**|
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

### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|---|---|
|Description|**Information about whether the team is a default business unit team.**|
|DisplayName|**Is Default**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdefault`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`team_isdefault`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsSasTokenSet"></a> IsSasTokenSet

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`issastokenset`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`isencryptedattributevalueset`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the team.**|
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
|Description|**Date and time when the team was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the team.**|
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
|Description|**Unique identifier of the organization associated with the team.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationidname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_SasToken"></a> SasToken

|Property|Value|
|---|---|
|Description|**Sas Token for Team.**|
|DisplayName|**Sas Token**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`sastoken`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_ShareLinkQualifier"></a> ShareLinkQualifier

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Share Link Qualifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sharelinkqualifier`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|

### <a name="BKMK_SystemManaged"></a> SystemManaged

|Property|Value|
|---|---|
|Description|**Select whether the team will be managed by the system.**|
|DisplayName|**Is System Managed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`systemmanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`team_systemmanaged`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the team.**|
|DisplayName|**Version number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_teams](#BKMK_business_unit_teams)
- [knowledgearticle_Teams](#BKMK_knowledgearticle_Teams)
- [lk_team_createdonbehalfby](#BKMK_lk_team_createdonbehalfby)
- [lk_team_modifiedonbehalfby](#BKMK_lk_team_modifiedonbehalfby)
- [lk_teambase_administratorid](#BKMK_lk_teambase_administratorid)
- [lk_teambase_createdby](#BKMK_lk_teambase_createdby)
- [lk_teambase_modifiedby](#BKMK_lk_teambase_modifiedby)
- [organization_teams](#BKMK_organization_teams)
- [processstage_teams](#BKMK_processstage_teams)
- [queue_team](#BKMK_queue_team)
- [team_delegatedauthorization](#BKMK_team_delegatedauthorization)
- [teamtemplate_Teams](#BKMK_teamtemplate_Teams)
- [TransactionCurrency_Team](#BKMK_TransactionCurrency_Team)

### <a name="BKMK_business_unit_teams"></a> business_unit_teams

One-To-Many Relationship: [businessunit business_unit_teams](businessunit.md#BKMK_business_unit_teams)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`businessunitid`|
|ReferencingEntityNavigationPropertyName|`businessunitid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_Teams"></a> knowledgearticle_Teams

One-To-Many Relationship: [knowledgearticle knowledgearticle_Teams](knowledgearticle.md#BKMK_knowledgearticle_Teams)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_team_createdonbehalfby"></a> lk_team_createdonbehalfby

One-To-Many Relationship: [systemuser lk_team_createdonbehalfby](systemuser.md#BKMK_lk_team_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_team_modifiedonbehalfby"></a> lk_team_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_team_modifiedonbehalfby](systemuser.md#BKMK_lk_team_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_teambase_administratorid"></a> lk_teambase_administratorid

One-To-Many Relationship: [systemuser lk_teambase_administratorid](systemuser.md#BKMK_lk_teambase_administratorid)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`administratorid`|
|ReferencingEntityNavigationPropertyName|`administratorid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_teambase_createdby"></a> lk_teambase_createdby

One-To-Many Relationship: [systemuser lk_teambase_createdby](systemuser.md#BKMK_lk_teambase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_teambase_modifiedby"></a> lk_teambase_modifiedby

One-To-Many Relationship: [systemuser lk_teambase_modifiedby](systemuser.md#BKMK_lk_teambase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_teams"></a> organization_teams

One-To-Many Relationship: [organization organization_teams](organization.md#BKMK_organization_teams)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid_organization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_processstage_teams"></a> processstage_teams

One-To-Many Relationship: [processstage processstage_teams](processstage.md#BKMK_processstage_teams)

|Property|Value|
|---|---|
|ReferencedEntity|`processstage`|
|ReferencedAttribute|`processstageid`|
|ReferencingAttribute|`stageid`|
|ReferencingEntityNavigationPropertyName|`stageid_processstage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_queue_team"></a> queue_team

One-To-Many Relationship: [queue queue_team](queue.md#BKMK_queue_team)

|Property|Value|
|---|---|
|ReferencedEntity|`queue`|
|ReferencedAttribute|`queueid`|
|ReferencingAttribute|`queueid`|
|ReferencingEntityNavigationPropertyName|`queueid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_delegatedauthorization"></a> team_delegatedauthorization

One-To-Many Relationship: [delegatedauthorization team_delegatedauthorization](delegatedauthorization.md#BKMK_team_delegatedauthorization)

|Property|Value|
|---|---|
|ReferencedEntity|`delegatedauthorization`|
|ReferencedAttribute|`delegatedauthorizationid`|
|ReferencingAttribute|`delegatedauthorizationid`|
|ReferencingEntityNavigationPropertyName|`delegatedauthorizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_teamtemplate_Teams"></a> teamtemplate_Teams

One-To-Many Relationship: [teamtemplate teamtemplate_Teams](teamtemplate.md#BKMK_teamtemplate_Teams)

|Property|Value|
|---|---|
|ReferencedEntity|`teamtemplate`|
|ReferencedAttribute|`teamtemplateid`|
|ReferencingAttribute|`teamtemplateid`|
|ReferencingEntityNavigationPropertyName|`associatedteamtemplateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_TransactionCurrency_Team"></a> TransactionCurrency_Team

One-To-Many Relationship: [transactioncurrency TransactionCurrency_Team](transactioncurrency.md#BKMK_TransactionCurrency_Team)

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

- [adx_inviteredemption_team_owningteam](#BKMK_adx_inviteredemption_team_owningteam)
- [adx_portalcomment_team_owningteam](#BKMK_adx_portalcomment_team_owningteam)
- [chat_team_owningteam](#BKMK_chat_team_owningteam)
- [ImportFile_Team](#BKMK_ImportFile_Team)
- [OwningTeam_postfollows](#BKMK_OwningTeam_postfollows)
- [team_accounts](#BKMK_team_accounts)
- [team_activity](#BKMK_team_activity)
- [team_activityfileattachment](#BKMK_team_activityfileattachment)
- [team_adx_invitation](#BKMK_team_adx_invitation)
- [team_adx_setting](#BKMK_team_adx_setting)
- [team_aiplugin](#BKMK_team_aiplugin)
- [team_aipluginauth](#BKMK_team_aipluginauth)
- [team_aipluginconversationstarter](#BKMK_team_aipluginconversationstarter)
- [team_aipluginconversationstartermapping](#BKMK_team_aipluginconversationstartermapping)
- [team_aipluginexternalschema](#BKMK_team_aipluginexternalschema)
- [team_aipluginexternalschemaproperty](#BKMK_team_aipluginexternalschemaproperty)
- [team_aiplugingovernance](#BKMK_team_aiplugingovernance)
- [team_aiplugingovernanceext](#BKMK_team_aiplugingovernanceext)
- [team_aiplugininstance](#BKMK_team_aiplugininstance)
- [team_aipluginoperation](#BKMK_team_aipluginoperation)
- [team_aipluginoperationparameter](#BKMK_team_aipluginoperationparameter)
- [team_aipluginoperationresponsetemplate](#BKMK_team_aipluginoperationresponsetemplate)
- [team_aipluginusersetting](#BKMK_team_aipluginusersetting)
- [team_annotations](#BKMK_team_annotations)
- [team_appnotification](#BKMK_team_appnotification)
- [team_appointment](#BKMK_team_appointment)
- [team_approvalprocess](#BKMK_team_approvalprocess)
- [team_approvalstageapproval](#BKMK_team_approvalstageapproval)
- [team_approvalstagecondition](#BKMK_team_approvalstagecondition)
- [team_approvalstageorder](#BKMK_team_approvalstageorder)
- [team_asyncoperation](#BKMK_team_asyncoperation)
- [Team_AsyncOperations](#BKMK_Team_AsyncOperations)
- [team_bot](#BKMK_team_bot)
- [team_botcomponent](#BKMK_team_botcomponent)
- [team_botcomponentcollection](#BKMK_team_botcomponentcollection)
- [Team_BulkDeleteFailures](#BKMK_Team_BulkDeleteFailures)
- [team_businessprocess](#BKMK_team_businessprocess)
- [team_card](#BKMK_team_card)
- [team_certificatecredential](#BKMK_team_certificatecredential)
- [team_componentversion](#BKMK_team_componentversion)
- [team_connectioninstance](#BKMK_team_connectioninstance)
- [team_connectionreference](#BKMK_team_connectionreference)
- [team_connections1](#BKMK_team_connections1)
- [team_connections2](#BKMK_team_connections2)
- [team_connector](#BKMK_team_connector)
- [team_contacts](#BKMK_team_contacts)
- [team_conversationtranscript](#BKMK_team_conversationtranscript)
- [team_copilotglossaryterm](#BKMK_team_copilotglossaryterm)
- [team_copilotsynonyms](#BKMK_team_copilotsynonyms)
- [team_credential](#BKMK_team_credential)
- [team_customapi](#BKMK_team_customapi)
- [team_datalakefolder](#BKMK_team_datalakefolder)
- [team_desktopflowbinary](#BKMK_team_desktopflowbinary)
- [team_desktopflowmodule](#BKMK_team_desktopflowmodule)
- [Team_DuplicateBaseRecord](#BKMK_Team_DuplicateBaseRecord)
- [Team_DuplicateMatchingRecord](#BKMK_Team_DuplicateMatchingRecord)
- [team_DuplicateRules](#BKMK_team_DuplicateRules)
- [team_dvfilesearch](#BKMK_team_dvfilesearch)
- [team_dvfilesearchattribute](#BKMK_team_dvfilesearchattribute)
- [team_dvfilesearchentity](#BKMK_team_dvfilesearchentity)
- [team_dvtablesearch](#BKMK_team_dvtablesearch)
- [team_dvtablesearchattribute](#BKMK_team_dvtablesearchattribute)
- [team_dvtablesearchentity](#BKMK_team_dvtablesearchentity)
- [team_email](#BKMK_team_email)
- [team_email_templates](#BKMK_team_email_templates)
- [team_emailserverprofile](#BKMK_team_emailserverprofile)
- [team_environmentvariabledefinition](#BKMK_team_environmentvariabledefinition)
- [team_exchangesyncidmapping](#BKMK_team_exchangesyncidmapping)
- [team_exportedexcel](#BKMK_team_exportedexcel)
- [team_exportsolutionupload](#BKMK_team_exportsolutionupload)
- [team_fabricaiskill](#BKMK_team_fabricaiskill)
- [team_fax](#BKMK_team_fax)
- [team_featurecontrolsetting](#BKMK_team_featurecontrolsetting)
- [team_federatedknowledgeconfiguration](#BKMK_team_federatedknowledgeconfiguration)
- [team_federatedknowledgeentityconfiguration](#BKMK_team_federatedknowledgeentityconfiguration)
- [team_flowaggregation](#BKMK_team_flowaggregation)
- [team_flowcapacityassignment](#BKMK_team_flowcapacityassignment)
- [team_flowcredentialapplication](#BKMK_team_flowcredentialapplication)
- [team_flowevent](#BKMK_team_flowevent)
- [team_flowmachine](#BKMK_team_flowmachine)
- [team_flowmachinegroup](#BKMK_team_flowmachinegroup)
- [team_flowmachineimage](#BKMK_team_flowmachineimage)
- [team_flowmachineimageversion](#BKMK_team_flowmachineimageversion)
- [team_flowmachinenetwork](#BKMK_team_flowmachinenetwork)
- [team_flowrun](#BKMK_team_flowrun)
- [team_flowsession](#BKMK_team_flowsession)
- [team_fxexpression](#BKMK_team_fxexpression)
- [team_goal](#BKMK_team_goal)
- [team_goal_goalowner](#BKMK_team_goal_goalowner)
- [team_goalrollupquery](#BKMK_team_goalrollupquery)
- [team_governanceconfiguration](#BKMK_team_governanceconfiguration)
- [team_ImportData](#BKMK_team_ImportData)
- [team_ImportFiles](#BKMK_team_ImportFiles)
- [team_ImportLogs](#BKMK_team_ImportLogs)
- [team_ImportMaps](#BKMK_team_ImportMaps)
- [team_Imports](#BKMK_team_Imports)
- [team_indexedtrait](#BKMK_team_indexedtrait)
- [team_interactionforemail](#BKMK_team_interactionforemail)
- [team_keyvaultreference](#BKMK_team_keyvaultreference)
- [team_knowledgearticle](#BKMK_team_knowledgearticle)
- [team_letter](#BKMK_team_letter)
- [team_mailbox](#BKMK_team_mailbox)
- [team_mailboxtrackingfolder](#BKMK_team_mailboxtrackingfolder)
- [team_managedidentity](#BKMK_team_managedidentity)
- [team_msdyn_aibdataset](#BKMK_team_msdyn_aibdataset)
- [team_msdyn_aibdatasetfile](#BKMK_team_msdyn_aibdatasetfile)
- [team_msdyn_aibdatasetrecord](#BKMK_team_msdyn_aibdatasetrecord)
- [team_msdyn_aibdatasetscontainer](#BKMK_team_msdyn_aibdatasetscontainer)
- [team_msdyn_aibfeedbackloop](#BKMK_team_msdyn_aibfeedbackloop)
- [team_msdyn_aibfile](#BKMK_team_msdyn_aibfile)
- [team_msdyn_aibfileattacheddata](#BKMK_team_msdyn_aibfileattacheddata)
- [team_msdyn_aidataprocessingevent](#BKMK_team_msdyn_aidataprocessingevent)
- [team_msdyn_aievaluationconfiguration](#BKMK_team_msdyn_aievaluationconfiguration)
- [team_msdyn_aievaluationrun](#BKMK_team_msdyn_aievaluationrun)
- [team_msdyn_aievent](#BKMK_team_msdyn_aievent)
- [team_msdyn_aifptrainingdocument](#BKMK_team_msdyn_aifptrainingdocument)
- [team_msdyn_aimodel](#BKMK_team_msdyn_aimodel)
- [team_msdyn_aiodimage](#BKMK_team_msdyn_aiodimage)
- [team_msdyn_aiodlabel](#BKMK_team_msdyn_aiodlabel)
- [team_msdyn_aiodtrainingboundingbox](#BKMK_team_msdyn_aiodtrainingboundingbox)
- [team_msdyn_aiodtrainingimage](#BKMK_team_msdyn_aiodtrainingimage)
- [team_msdyn_aitemplate](#BKMK_team_msdyn_aitemplate)
- [team_msdyn_aitestcase](#BKMK_team_msdyn_aitestcase)
- [team_msdyn_aitestcasedocument](#BKMK_team_msdyn_aitestcasedocument)
- [team_msdyn_aitestcaseinput](#BKMK_team_msdyn_aitestcaseinput)
- [team_msdyn_aitestrun](#BKMK_team_msdyn_aitestrun)
- [team_msdyn_aitestrunbatch](#BKMK_team_msdyn_aitestrunbatch)
- [team_msdyn_analysiscomponent](#BKMK_team_msdyn_analysiscomponent)
- [team_msdyn_analysisjob](#BKMK_team_msdyn_analysisjob)
- [team_msdyn_analysisoverride](#BKMK_team_msdyn_analysisoverride)
- [team_msdyn_analysisresult](#BKMK_team_msdyn_analysisresult)
- [team_msdyn_analysisresultdetail](#BKMK_team_msdyn_analysisresultdetail)
- [team_msdyn_copilotinteractions](#BKMK_team_msdyn_copilotinteractions)
- [team_msdyn_customcontrolextendedsettings](#BKMK_team_msdyn_customcontrolextendedsettings)
- [team_msdyn_dataflow](#BKMK_team_msdyn_dataflow)
- [team_msdyn_dataflow_datalakefolder](#BKMK_team_msdyn_dataflow_datalakefolder)
- [team_msdyn_dataflowconnectionreference](#BKMK_team_msdyn_dataflowconnectionreference)
- [team_msdyn_dataflowrefreshhistory](#BKMK_team_msdyn_dataflowrefreshhistory)
- [team_msdyn_dataflowtemplate](#BKMK_team_msdyn_dataflowtemplate)
- [team_msdyn_dmsrequest](#BKMK_team_msdyn_dmsrequest)
- [team_msdyn_dmsrequeststatus](#BKMK_team_msdyn_dmsrequeststatus)
- [team_msdyn_dmssyncrequest](#BKMK_team_msdyn_dmssyncrequest)
- [team_msdyn_dmssyncstatus](#BKMK_team_msdyn_dmssyncstatus)
- [team_msdyn_entitylinkchatconfiguration](#BKMK_team_msdyn_entitylinkchatconfiguration)
- [team_msdyn_entityrefreshhistory](#BKMK_team_msdyn_entityrefreshhistory)
- [team_msdyn_favoriteknowledgearticle](#BKMK_team_msdyn_favoriteknowledgearticle)
- [team_msdyn_federatedarticle](#BKMK_team_msdyn_federatedarticle)
- [team_msdyn_fileupload](#BKMK_team_msdyn_fileupload)
- [team_msdyn_flow_actionapprovalmodel](#BKMK_team_msdyn_flow_actionapprovalmodel)
- [team_msdyn_flow_approval](#BKMK_team_msdyn_flow_approval)
- [team_msdyn_flow_approvalrequest](#BKMK_team_msdyn_flow_approvalrequest)
- [team_msdyn_flow_approvalresponse](#BKMK_team_msdyn_flow_approvalresponse)
- [team_msdyn_flow_approvalstep](#BKMK_team_msdyn_flow_approvalstep)
- [team_msdyn_flow_awaitallactionapprovalmodel](#BKMK_team_msdyn_flow_awaitallactionapprovalmodel)
- [team_msdyn_flow_awaitallapprovalmodel](#BKMK_team_msdyn_flow_awaitallapprovalmodel)
- [team_msdyn_flow_basicapprovalmodel](#BKMK_team_msdyn_flow_basicapprovalmodel)
- [team_msdyn_flow_flowapproval](#BKMK_team_msdyn_flow_flowapproval)
- [team_msdyn_formmapping](#BKMK_team_msdyn_formmapping)
- [team_msdyn_function](#BKMK_team_msdyn_function)
- [team_msdyn_integratedsearchprovider](#BKMK_team_msdyn_integratedsearchprovider)
- [team_msdyn_kalanguagesetting](#BKMK_team_msdyn_kalanguagesetting)
- [team_msdyn_kbattachment](#BKMK_team_msdyn_kbattachment)
- [team_msdyn_kmfederatedsearchconfig](#BKMK_team_msdyn_kmfederatedsearchconfig)
- [team_msdyn_knowledgearticleimage](#BKMK_team_msdyn_knowledgearticleimage)
- [team_msdyn_knowledgearticletemplate](#BKMK_team_msdyn_knowledgearticletemplate)
- [team_msdyn_knowledgeassetconfiguration](#BKMK_team_msdyn_knowledgeassetconfiguration)
- [team_msdyn_knowledgeinteractioninsight](#BKMK_team_msdyn_knowledgeinteractioninsight)
- [team_msdyn_knowledgemanagementsetting](#BKMK_team_msdyn_knowledgemanagementsetting)
- [team_msdyn_knowledgepersonalfilter](#BKMK_team_msdyn_knowledgepersonalfilter)
- [team_msdyn_knowledgesearchfilter](#BKMK_team_msdyn_knowledgesearchfilter)
- [team_msdyn_knowledgesearchinsight](#BKMK_team_msdyn_knowledgesearchinsight)
- [team_msdyn_mobileapp](#BKMK_team_msdyn_mobileapp)
- [team_msdyn_pmanalysishistory](#BKMK_team_msdyn_pmanalysishistory)
- [team_msdyn_pmbusinessruleautomationconfig](#BKMK_team_msdyn_pmbusinessruleautomationconfig)
- [team_msdyn_pmcalendar](#BKMK_team_msdyn_pmcalendar)
- [team_msdyn_pmcalendarversion](#BKMK_team_msdyn_pmcalendarversion)
- [team_msdyn_pminferredtask](#BKMK_team_msdyn_pminferredtask)
- [team_msdyn_pmprocessextendedmetadataversion](#BKMK_team_msdyn_pmprocessextendedmetadataversion)
- [team_msdyn_pmprocesstemplate](#BKMK_team_msdyn_pmprocesstemplate)
- [team_msdyn_pmprocessusersettings](#BKMK_team_msdyn_pmprocessusersettings)
- [team_msdyn_pmprocessversion](#BKMK_team_msdyn_pmprocessversion)
- [team_msdyn_pmrecording](#BKMK_team_msdyn_pmrecording)
- [team_msdyn_pmsimulation](#BKMK_team_msdyn_pmsimulation)
- [team_msdyn_pmtemplate](#BKMK_team_msdyn_pmtemplate)
- [team_msdyn_pmview](#BKMK_team_msdyn_pmview)
- [team_msdyn_qna](#BKMK_team_msdyn_qna)
- [team_msdyn_richtextfile](#BKMK_team_msdyn_richtextfile)
- [team_msdyn_salesforcestructuredobject](#BKMK_team_msdyn_salesforcestructuredobject)
- [team_msdyn_salesforcestructuredqnaconfig](#BKMK_team_msdyn_salesforcestructuredqnaconfig)
- [team_msdyn_schedule](#BKMK_team_msdyn_schedule)
- [team_msdyn_serviceconfiguration](#BKMK_team_msdyn_serviceconfiguration)
- [team_msdyn_slakpi](#BKMK_team_msdyn_slakpi)
- [team_msdyn_solutionhealthrule](#BKMK_team_msdyn_solutionhealthrule)
- [team_msdyn_solutionhealthruleargument](#BKMK_team_msdyn_solutionhealthruleargument)
- [team_msdyn_virtualtablecolumncandidate](#BKMK_team_msdyn_virtualtablecolumncandidate)
- [team_msdynce_botcontent](#BKMK_team_msdynce_botcontent)
- [team_mspcat_catalogsubmissionfiles](#BKMK_team_mspcat_catalogsubmissionfiles)
- [team_mspcat_packagestore](#BKMK_team_mspcat_packagestore)
- [team_nlsqregistration](#BKMK_team_nlsqregistration)
- [team_phonecall](#BKMK_team_phonecall)
- [team_plannerbusinessscenario](#BKMK_team_plannerbusinessscenario)
- [team_plannersyncaction](#BKMK_team_plannersyncaction)
- [team_plugin](#BKMK_team_plugin)
- [team_PostRegardings](#BKMK_team_PostRegardings)
- [team_powerbidataset](#BKMK_team_powerbidataset)
- [team_powerbidatasetapdx](#BKMK_team_powerbidatasetapdx)
- [team_powerbimashupparameter](#BKMK_team_powerbimashupparameter)
- [team_powerbireport](#BKMK_team_powerbireport)
- [team_powerbireportapdx](#BKMK_team_powerbireportapdx)
- [team_powerfxrule](#BKMK_team_powerfxrule)
- [team_powerpagecomponent](#BKMK_team_powerpagecomponent)
- [team_powerpagesite](#BKMK_team_powerpagesite)
- [team_powerpagesitelanguage](#BKMK_team_powerpagesitelanguage)
- [team_powerpagesitepublished](#BKMK_team_powerpagesitepublished)
- [team_powerpageslog](#BKMK_team_powerpageslog)
- [team_powerpagesmanagedidentity](#BKMK_team_powerpagesmanagedidentity)
- [team_powerpagesscanreport](#BKMK_team_powerpagesscanreport)
- [team_powerpagessiteaifeedback](#BKMK_team_powerpagessiteaifeedback)
- [team_principalobjectattributeaccess](#BKMK_team_principalobjectattributeaccess)
- [team_principalobjectattributeaccess_principalid](#BKMK_team_principalobjectattributeaccess_principalid)
- [team_privilegecheckerrun](#BKMK_team_privilegecheckerrun)
- [team_processsession](#BKMK_team_processsession)
- [Team_ProcessSessions](#BKMK_Team_ProcessSessions)
- [team_processstageparameter](#BKMK_team_processstageparameter)
- [team_queueitembase_workerid](#BKMK_team_queueitembase_workerid)
- [team_recentlyused](#BKMK_team_recentlyused)
- [team_recurringappointmentmaster](#BKMK_team_recurringappointmentmaster)
- [team_retaineddataexcel](#BKMK_team_retaineddataexcel)
- [team_retentionconfig](#BKMK_team_retentionconfig)
- [team_retentionfailuredetail](#BKMK_team_retentionfailuredetail)
- [team_retentionoperation](#BKMK_team_retentionoperation)
- [team_retentionsuccessdetail](#BKMK_team_retentionsuccessdetail)
- [team_savingrule](#BKMK_team_savingrule)
- [team_sharepointdocumentlocation](#BKMK_team_sharepointdocumentlocation)
- [team_sharepointsite](#BKMK_team_sharepointsite)
- [team_sideloadedaiplugin](#BKMK_team_sideloadedaiplugin)
- [team_signal](#BKMK_team_signal)
- [team_slaBase](#BKMK_team_slaBase)
- [team_socialactivity](#BKMK_team_socialactivity)
- [team_solutioncomponentbatchconfiguration](#BKMK_team_solutioncomponentbatchconfiguration)
- [team_stagesolutionupload](#BKMK_team_stagesolutionupload)
- [team_synapsedatabase](#BKMK_team_synapsedatabase)
- [team_SyncError](#BKMK_team_SyncError)
- [Team_SyncErrors](#BKMK_Team_SyncErrors)
- [team_tag](#BKMK_team_tag)
- [team_taggedflowsession](#BKMK_team_taggedflowsession)
- [team_taggedprocess](#BKMK_team_taggedprocess)
- [team_task](#BKMK_team_task)
- [team_teammobileofflineprofilemembership_TeamId](#BKMK_team_teammobileofflineprofilemembership_TeamId)
- [team_trait](#BKMK_team_trait)
- [team_unstructuredfilesearchentity](#BKMK_team_unstructuredfilesearchentity)
- [team_unstructuredfilesearchrecord](#BKMK_team_unstructuredfilesearchrecord)
- [team_userform](#BKMK_team_userform)
- [team_userquery](#BKMK_team_userquery)
- [team_userqueryvisualizations](#BKMK_team_userqueryvisualizations)
- [team_workflow](#BKMK_team_workflow)
- [team_workflowbinary](#BKMK_team_workflowbinary)
- [team_workflowlog](#BKMK_team_workflowlog)
- [team_workflowmetadata](#BKMK_team_workflowmetadata)
- [team_workqueue](#BKMK_team_workqueue)
- [team_workqueueitem](#BKMK_team_workqueueitem)

### <a name="BKMK_adx_inviteredemption_team_owningteam"></a> adx_inviteredemption_team_owningteam

Many-To-One Relationship: [adx_inviteredemption adx_inviteredemption_team_owningteam](adx_inviteredemption.md#BKMK_adx_inviteredemption_team_owningteam)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`adx_inviteredemption_team_owningteam`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_portalcomment_team_owningteam"></a> adx_portalcomment_team_owningteam

Many-To-One Relationship: [adx_portalcomment adx_portalcomment_team_owningteam](adx_portalcomment.md#BKMK_adx_portalcomment_team_owningteam)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`adx_portalcomment_team_owningteam`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_chat_team_owningteam"></a> chat_team_owningteam

Many-To-One Relationship: [chat chat_team_owningteam](chat.md#BKMK_chat_team_owningteam)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`chat_team_owningteam`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ImportFile_Team"></a> ImportFile_Team

Many-To-One Relationship: [importfile ImportFile_Team](importfile.md#BKMK_ImportFile_Team)

|Property|Value|
|---|---|
|ReferencingEntity|`importfile`|
|ReferencingAttribute|`recordsownerid`|
|ReferencedEntityNavigationPropertyName|`ImportFile_Team`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_OwningTeam_postfollows"></a> OwningTeam_postfollows

Many-To-One Relationship: [postfollow OwningTeam_postfollows](postfollow.md#BKMK_OwningTeam_postfollows)

|Property|Value|
|---|---|
|ReferencingEntity|`postfollow`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`OwningTeam_postfollows`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_accounts"></a> team_accounts

Many-To-One Relationship: [account team_accounts](account.md#BKMK_team_accounts)

|Property|Value|
|---|---|
|ReferencingEntity|`account`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_accounts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_activity"></a> team_activity

Many-To-One Relationship: [activitypointer team_activity](activitypointer.md#BKMK_team_activity)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_activity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_activityfileattachment"></a> team_activityfileattachment

Many-To-One Relationship: [activityfileattachment team_activityfileattachment](activityfileattachment.md#BKMK_team_activityfileattachment)

|Property|Value|
|---|---|
|ReferencingEntity|`activityfileattachment`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_activityfileattachment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_adx_invitation"></a> team_adx_invitation

Many-To-One Relationship: [adx_invitation team_adx_invitation](adx_invitation.md#BKMK_team_adx_invitation)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_invitation`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_adx_invitation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_adx_setting"></a> team_adx_setting

Many-To-One Relationship: [adx_setting team_adx_setting](adx_setting.md#BKMK_team_adx_setting)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_setting`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_adx_setting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aiplugin"></a> team_aiplugin

Many-To-One Relationship: [aiplugin team_aiplugin](aiplugin.md#BKMK_team_aiplugin)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugin`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aiplugin`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aipluginauth"></a> team_aipluginauth

Many-To-One Relationship: [aipluginauth team_aipluginauth](aipluginauth.md#BKMK_team_aipluginauth)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginauth`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aipluginauth`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aipluginconversationstarter"></a> team_aipluginconversationstarter

Many-To-One Relationship: [aipluginconversationstarter team_aipluginconversationstarter](aipluginconversationstarter.md#BKMK_team_aipluginconversationstarter)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginconversationstarter`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aipluginconversationstarter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aipluginconversationstartermapping"></a> team_aipluginconversationstartermapping

Many-To-One Relationship: [aipluginconversationstartermapping team_aipluginconversationstartermapping](aipluginconversationstartermapping.md#BKMK_team_aipluginconversationstartermapping)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginconversationstartermapping`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aipluginconversationstartermapping`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aipluginexternalschema"></a> team_aipluginexternalschema

Many-To-One Relationship: [aipluginexternalschema team_aipluginexternalschema](aipluginexternalschema.md#BKMK_team_aipluginexternalschema)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginexternalschema`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aipluginexternalschema`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aipluginexternalschemaproperty"></a> team_aipluginexternalschemaproperty

Many-To-One Relationship: [aipluginexternalschemaproperty team_aipluginexternalschemaproperty](aipluginexternalschemaproperty.md#BKMK_team_aipluginexternalschemaproperty)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginexternalschemaproperty`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aipluginexternalschemaproperty`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aiplugingovernance"></a> team_aiplugingovernance

Many-To-One Relationship: [aiplugingovernance team_aiplugingovernance](aiplugingovernance.md#BKMK_team_aiplugingovernance)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugingovernance`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aiplugingovernance`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aiplugingovernanceext"></a> team_aiplugingovernanceext

Many-To-One Relationship: [aiplugingovernanceext team_aiplugingovernanceext](aiplugingovernanceext.md#BKMK_team_aiplugingovernanceext)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugingovernanceext`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aiplugingovernanceext`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aiplugininstance"></a> team_aiplugininstance

Many-To-One Relationship: [aiplugininstance team_aiplugininstance](aiplugininstance.md#BKMK_team_aiplugininstance)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugininstance`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aiplugininstance`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aipluginoperation"></a> team_aipluginoperation

Many-To-One Relationship: [aipluginoperation team_aipluginoperation](aipluginoperation.md#BKMK_team_aipluginoperation)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperation`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aipluginoperation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aipluginoperationparameter"></a> team_aipluginoperationparameter

Many-To-One Relationship: [aipluginoperationparameter team_aipluginoperationparameter](aipluginoperationparameter.md#BKMK_team_aipluginoperationparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperationparameter`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aipluginoperationparameter`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aipluginoperationresponsetemplate"></a> team_aipluginoperationresponsetemplate

Many-To-One Relationship: [aipluginoperationresponsetemplate team_aipluginoperationresponsetemplate](aipluginoperationresponsetemplate.md#BKMK_team_aipluginoperationresponsetemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperationresponsetemplate`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aipluginoperationresponsetemplate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_aipluginusersetting"></a> team_aipluginusersetting

Many-To-One Relationship: [aipluginusersetting team_aipluginusersetting](aipluginusersetting.md#BKMK_team_aipluginusersetting)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginusersetting`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_aipluginusersetting`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_annotations"></a> team_annotations

Many-To-One Relationship: [annotation team_annotations](annotation.md#BKMK_team_annotations)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_annotations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_appnotification"></a> team_appnotification

Many-To-One Relationship: [appnotification team_appnotification](appnotification.md#BKMK_team_appnotification)

|Property|Value|
|---|---|
|ReferencingEntity|`appnotification`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_appnotification`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_appointment"></a> team_appointment

Many-To-One Relationship: [appointment team_appointment](appointment.md#BKMK_team_appointment)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_appointment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_approvalprocess"></a> team_approvalprocess

Many-To-One Relationship: [approvalprocess team_approvalprocess](approvalprocess.md#BKMK_team_approvalprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalprocess`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_approvalprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_approvalstageapproval"></a> team_approvalstageapproval

Many-To-One Relationship: [approvalstageapproval team_approvalstageapproval](approvalstageapproval.md#BKMK_team_approvalstageapproval)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstageapproval`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_approvalstageapproval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_approvalstagecondition"></a> team_approvalstagecondition

Many-To-One Relationship: [approvalstagecondition team_approvalstagecondition](approvalstagecondition.md#BKMK_team_approvalstagecondition)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstagecondition`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_approvalstagecondition`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_approvalstageorder"></a> team_approvalstageorder

Many-To-One Relationship: [approvalstageorder team_approvalstageorder](approvalstageorder.md#BKMK_team_approvalstageorder)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstageorder`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_approvalstageorder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_asyncoperation"></a> team_asyncoperation

Many-To-One Relationship: [asyncoperation team_asyncoperation](asyncoperation.md#BKMK_team_asyncoperation)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_asyncoperation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Team_AsyncOperations"></a> Team_AsyncOperations

Many-To-One Relationship: [asyncoperation Team_AsyncOperations](asyncoperation.md#BKMK_Team_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Team_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_bot"></a> team_bot

Many-To-One Relationship: [bot team_bot](bot.md#BKMK_team_bot)

|Property|Value|
|---|---|
|ReferencingEntity|`bot`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_bot`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_botcomponent"></a> team_botcomponent

Many-To-One Relationship: [botcomponent team_botcomponent](botcomponent.md#BKMK_team_botcomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`botcomponent`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_botcomponent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_botcomponentcollection"></a> team_botcomponentcollection

Many-To-One Relationship: [botcomponentcollection team_botcomponentcollection](botcomponentcollection.md#BKMK_team_botcomponentcollection)

|Property|Value|
|---|---|
|ReferencingEntity|`botcomponentcollection`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_botcomponentcollection`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Team_BulkDeleteFailures"></a> Team_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Team_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Team_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Team_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_businessprocess"></a> team_businessprocess

Many-To-One Relationship: [businessprocess team_businessprocess](businessprocess.md#BKMK_team_businessprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`businessprocess`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_businessprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_card"></a> team_card

Many-To-One Relationship: [card team_card](card.md#BKMK_team_card)

|Property|Value|
|---|---|
|ReferencingEntity|`card`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_card`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_certificatecredential"></a> team_certificatecredential

Many-To-One Relationship: [certificatecredential team_certificatecredential](certificatecredential.md#BKMK_team_certificatecredential)

|Property|Value|
|---|---|
|ReferencingEntity|`certificatecredential`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_certificatecredential`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_componentversion"></a> team_componentversion

Many-To-One Relationship: [componentversion team_componentversion](componentversion.md#BKMK_team_componentversion)

|Property|Value|
|---|---|
|ReferencingEntity|`componentversion`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_componentversion`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: Versions<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_connectioninstance"></a> team_connectioninstance

Many-To-One Relationship: [connectioninstance team_connectioninstance](connectioninstance.md#BKMK_team_connectioninstance)

|Property|Value|
|---|---|
|ReferencingEntity|`connectioninstance`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_connectioninstance`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_connectionreference"></a> team_connectionreference

Many-To-One Relationship: [connectionreference team_connectionreference](connectionreference.md#BKMK_team_connectionreference)

|Property|Value|
|---|---|
|ReferencingEntity|`connectionreference`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_connectionreference`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_connections1"></a> team_connections1

Many-To-One Relationship: [connection team_connections1](connection.md#BKMK_team_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`team_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_connections2"></a> team_connections2

Many-To-One Relationship: [connection team_connections2](connection.md#BKMK_team_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`team_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_connector"></a> team_connector

Many-To-One Relationship: [connector team_connector](connector.md#BKMK_team_connector)

|Property|Value|
|---|---|
|ReferencingEntity|`connector`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_connector`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_contacts"></a> team_contacts

Many-To-One Relationship: [contact team_contacts](contact.md#BKMK_team_contacts)

|Property|Value|
|---|---|
|ReferencingEntity|`contact`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_contacts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_conversationtranscript"></a> team_conversationtranscript

Many-To-One Relationship: [conversationtranscript team_conversationtranscript](conversationtranscript.md#BKMK_team_conversationtranscript)

|Property|Value|
|---|---|
|ReferencingEntity|`conversationtranscript`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_conversationtranscript`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_copilotglossaryterm"></a> team_copilotglossaryterm

Many-To-One Relationship: [copilotglossaryterm team_copilotglossaryterm](copilotglossaryterm.md#BKMK_team_copilotglossaryterm)

|Property|Value|
|---|---|
|ReferencingEntity|`copilotglossaryterm`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_copilotglossaryterm`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_copilotsynonyms"></a> team_copilotsynonyms

Many-To-One Relationship: [copilotsynonyms team_copilotsynonyms](copilotsynonyms.md#BKMK_team_copilotsynonyms)

|Property|Value|
|---|---|
|ReferencingEntity|`copilotsynonyms`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_copilotsynonyms`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_credential"></a> team_credential

Many-To-One Relationship: [credential team_credential](credential.md#BKMK_team_credential)

|Property|Value|
|---|---|
|ReferencingEntity|`credential`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_credential`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_customapi"></a> team_customapi

Many-To-One Relationship: [customapi team_customapi](customapi.md#BKMK_team_customapi)

|Property|Value|
|---|---|
|ReferencingEntity|`customapi`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_customapi`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_datalakefolder"></a> team_datalakefolder

Many-To-One Relationship: [datalakefolder team_datalakefolder](datalakefolder.md#BKMK_team_datalakefolder)

|Property|Value|
|---|---|
|ReferencingEntity|`datalakefolder`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_datalakefolder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_desktopflowbinary"></a> team_desktopflowbinary

Many-To-One Relationship: [desktopflowbinary team_desktopflowbinary](desktopflowbinary.md#BKMK_team_desktopflowbinary)

|Property|Value|
|---|---|
|ReferencingEntity|`desktopflowbinary`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_desktopflowbinary`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_desktopflowmodule"></a> team_desktopflowmodule

Many-To-One Relationship: [desktopflowmodule team_desktopflowmodule](desktopflowmodule.md#BKMK_team_desktopflowmodule)

|Property|Value|
|---|---|
|ReferencingEntity|`desktopflowmodule`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_desktopflowmodule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Team_DuplicateBaseRecord"></a> Team_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord Team_DuplicateBaseRecord](duplicaterecord.md#BKMK_Team_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`Team_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Team_DuplicateMatchingRecord"></a> Team_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord Team_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Team_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`Team_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_DuplicateRules"></a> team_DuplicateRules

Many-To-One Relationship: [duplicaterule team_DuplicateRules](duplicaterule.md#BKMK_team_DuplicateRules)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterule`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_DuplicateRules`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_dvfilesearch"></a> team_dvfilesearch

Many-To-One Relationship: [dvfilesearch team_dvfilesearch](dvfilesearch.md#BKMK_team_dvfilesearch)

|Property|Value|
|---|---|
|ReferencingEntity|`dvfilesearch`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_dvfilesearch`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_dvfilesearchattribute"></a> team_dvfilesearchattribute

Many-To-One Relationship: [dvfilesearchattribute team_dvfilesearchattribute](dvfilesearchattribute.md#BKMK_team_dvfilesearchattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`dvfilesearchattribute`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_dvfilesearchattribute`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_dvfilesearchentity"></a> team_dvfilesearchentity

Many-To-One Relationship: [dvfilesearchentity team_dvfilesearchentity](dvfilesearchentity.md#BKMK_team_dvfilesearchentity)

|Property|Value|
|---|---|
|ReferencingEntity|`dvfilesearchentity`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_dvfilesearchentity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_dvtablesearch"></a> team_dvtablesearch

Many-To-One Relationship: [dvtablesearch team_dvtablesearch](dvtablesearch.md#BKMK_team_dvtablesearch)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearch`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_dvtablesearch`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_dvtablesearchattribute"></a> team_dvtablesearchattribute

Many-To-One Relationship: [dvtablesearchattribute team_dvtablesearchattribute](dvtablesearchattribute.md#BKMK_team_dvtablesearchattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearchattribute`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_dvtablesearchattribute`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_dvtablesearchentity"></a> team_dvtablesearchentity

Many-To-One Relationship: [dvtablesearchentity team_dvtablesearchentity](dvtablesearchentity.md#BKMK_team_dvtablesearchentity)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearchentity`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_dvtablesearchentity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_email"></a> team_email

Many-To-One Relationship: [email team_email](email.md#BKMK_team_email)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_email`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_email_templates"></a> team_email_templates

Many-To-One Relationship: [template team_email_templates](template.md#BKMK_team_email_templates)

|Property|Value|
|---|---|
|ReferencingEntity|`template`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_email_templates`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_emailserverprofile"></a> team_emailserverprofile

Many-To-One Relationship: [emailserverprofile team_emailserverprofile](emailserverprofile.md#BKMK_team_emailserverprofile)

|Property|Value|
|---|---|
|ReferencingEntity|`emailserverprofile`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_emailserverprofile`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_environmentvariabledefinition"></a> team_environmentvariabledefinition

Many-To-One Relationship: [environmentvariabledefinition team_environmentvariabledefinition](environmentvariabledefinition.md#BKMK_team_environmentvariabledefinition)

|Property|Value|
|---|---|
|ReferencingEntity|`environmentvariabledefinition`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_environmentvariabledefinition`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_exchangesyncidmapping"></a> team_exchangesyncidmapping

Many-To-One Relationship: [exchangesyncidmapping team_exchangesyncidmapping](exchangesyncidmapping.md#BKMK_team_exchangesyncidmapping)

|Property|Value|
|---|---|
|ReferencingEntity|`exchangesyncidmapping`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_exchangesyncidmapping`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_exportedexcel"></a> team_exportedexcel

Many-To-One Relationship: [exportedexcel team_exportedexcel](exportedexcel.md#BKMK_team_exportedexcel)

|Property|Value|
|---|---|
|ReferencingEntity|`exportedexcel`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_exportedexcel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_exportsolutionupload"></a> team_exportsolutionupload

Many-To-One Relationship: [exportsolutionupload team_exportsolutionupload](exportsolutionupload.md#BKMK_team_exportsolutionupload)

|Property|Value|
|---|---|
|ReferencingEntity|`exportsolutionupload`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_exportsolutionupload`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_fabricaiskill"></a> team_fabricaiskill

Many-To-One Relationship: [fabricaiskill team_fabricaiskill](fabricaiskill.md#BKMK_team_fabricaiskill)

|Property|Value|
|---|---|
|ReferencingEntity|`fabricaiskill`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_fabricaiskill`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_fax"></a> team_fax

Many-To-One Relationship: [fax team_fax](fax.md#BKMK_team_fax)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_fax`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_featurecontrolsetting"></a> team_featurecontrolsetting

Many-To-One Relationship: [featurecontrolsetting team_featurecontrolsetting](featurecontrolsetting.md#BKMK_team_featurecontrolsetting)

|Property|Value|
|---|---|
|ReferencingEntity|`featurecontrolsetting`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_featurecontrolsetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_federatedknowledgeconfiguration"></a> team_federatedknowledgeconfiguration

Many-To-One Relationship: [federatedknowledgeconfiguration team_federatedknowledgeconfiguration](federatedknowledgeconfiguration.md#BKMK_team_federatedknowledgeconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`federatedknowledgeconfiguration`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_federatedknowledgeconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_federatedknowledgeentityconfiguration"></a> team_federatedknowledgeentityconfiguration

Many-To-One Relationship: [federatedknowledgeentityconfiguration team_federatedknowledgeentityconfiguration](federatedknowledgeentityconfiguration.md#BKMK_team_federatedknowledgeentityconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`federatedknowledgeentityconfiguration`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_federatedknowledgeentityconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_flowaggregation"></a> team_flowaggregation

Many-To-One Relationship: [flowaggregation team_flowaggregation](flowaggregation.md#BKMK_team_flowaggregation)

|Property|Value|
|---|---|
|ReferencingEntity|`flowaggregation`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_flowaggregation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_flowcapacityassignment"></a> team_flowcapacityassignment

Many-To-One Relationship: [flowcapacityassignment team_flowcapacityassignment](flowcapacityassignment.md#BKMK_team_flowcapacityassignment)

|Property|Value|
|---|---|
|ReferencingEntity|`flowcapacityassignment`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_flowcapacityassignment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_flowcredentialapplication"></a> team_flowcredentialapplication

Many-To-One Relationship: [flowcredentialapplication team_flowcredentialapplication](flowcredentialapplication.md#BKMK_team_flowcredentialapplication)

|Property|Value|
|---|---|
|ReferencingEntity|`flowcredentialapplication`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_flowcredentialapplication`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_flowevent"></a> team_flowevent

Many-To-One Relationship: [flowevent team_flowevent](flowevent.md#BKMK_team_flowevent)

|Property|Value|
|---|---|
|ReferencingEntity|`flowevent`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_flowevent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_flowmachine"></a> team_flowmachine

Many-To-One Relationship: [flowmachine team_flowmachine](flowmachine.md#BKMK_team_flowmachine)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachine`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_flowmachine`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_flowmachinegroup"></a> team_flowmachinegroup

Many-To-One Relationship: [flowmachinegroup team_flowmachinegroup](flowmachinegroup.md#BKMK_team_flowmachinegroup)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachinegroup`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_flowmachinegroup`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_flowmachineimage"></a> team_flowmachineimage

Many-To-One Relationship: [flowmachineimage team_flowmachineimage](flowmachineimage.md#BKMK_team_flowmachineimage)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachineimage`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_flowmachineimage`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_flowmachineimageversion"></a> team_flowmachineimageversion

Many-To-One Relationship: [flowmachineimageversion team_flowmachineimageversion](flowmachineimageversion.md#BKMK_team_flowmachineimageversion)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachineimageversion`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_flowmachineimageversion`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_flowmachinenetwork"></a> team_flowmachinenetwork

Many-To-One Relationship: [flowmachinenetwork team_flowmachinenetwork](flowmachinenetwork.md#BKMK_team_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachinenetwork`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_flowmachinenetwork`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_flowrun"></a> team_flowrun

Many-To-One Relationship: [flowrun team_flowrun](flowrun.md#BKMK_team_flowrun)

|Property|Value|
|---|---|
|ReferencingEntity|`flowrun`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_flowrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_flowsession"></a> team_flowsession

Many-To-One Relationship: [flowsession team_flowsession](flowsession.md#BKMK_team_flowsession)

|Property|Value|
|---|---|
|ReferencingEntity|`flowsession`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_flowsession`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_fxexpression"></a> team_fxexpression

Many-To-One Relationship: [fxexpression team_fxexpression](fxexpression.md#BKMK_team_fxexpression)

|Property|Value|
|---|---|
|ReferencingEntity|`fxexpression`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_fxexpression`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_goal"></a> team_goal

Many-To-One Relationship: [goal team_goal](goal.md#BKMK_team_goal)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_goal`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_goal_goalowner"></a> team_goal_goalowner

Many-To-One Relationship: [goal team_goal_goalowner](goal.md#BKMK_team_goal_goalowner)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`goalownerid`|
|ReferencedEntityNavigationPropertyName|`team_goal_goalowner`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_goalrollupquery"></a> team_goalrollupquery

Many-To-One Relationship: [goalrollupquery team_goalrollupquery](goalrollupquery.md#BKMK_team_goalrollupquery)

|Property|Value|
|---|---|
|ReferencingEntity|`goalrollupquery`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_goalrollupquery`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_governanceconfiguration"></a> team_governanceconfiguration

Many-To-One Relationship: [governanceconfiguration team_governanceconfiguration](governanceconfiguration.md#BKMK_team_governanceconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`governanceconfiguration`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_governanceconfiguration`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_ImportData"></a> team_ImportData

Many-To-One Relationship: [importdata team_ImportData](importdata.md#BKMK_team_ImportData)

|Property|Value|
|---|---|
|ReferencingEntity|`importdata`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_ImportData`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_ImportFiles"></a> team_ImportFiles

Many-To-One Relationship: [importfile team_ImportFiles](importfile.md#BKMK_team_ImportFiles)

|Property|Value|
|---|---|
|ReferencingEntity|`importfile`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_ImportFiles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_ImportLogs"></a> team_ImportLogs

Many-To-One Relationship: [importlog team_ImportLogs](importlog.md#BKMK_team_ImportLogs)

|Property|Value|
|---|---|
|ReferencingEntity|`importlog`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_ImportLogs`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_ImportMaps"></a> team_ImportMaps

Many-To-One Relationship: [importmap team_ImportMaps](importmap.md#BKMK_team_ImportMaps)

|Property|Value|
|---|---|
|ReferencingEntity|`importmap`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_ImportMaps`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_Imports"></a> team_Imports

Many-To-One Relationship: [import team_Imports](import.md#BKMK_team_Imports)

|Property|Value|
|---|---|
|ReferencingEntity|`import`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_Imports`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_indexedtrait"></a> team_indexedtrait

Many-To-One Relationship: [indexedtrait team_indexedtrait](indexedtrait.md#BKMK_team_indexedtrait)

|Property|Value|
|---|---|
|ReferencingEntity|`indexedtrait`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_indexedtrait`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_interactionforemail"></a> team_interactionforemail

Many-To-One Relationship: [interactionforemail team_interactionforemail](interactionforemail.md#BKMK_team_interactionforemail)

|Property|Value|
|---|---|
|ReferencingEntity|`interactionforemail`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_new_interactionforemail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_keyvaultreference"></a> team_keyvaultreference

Many-To-One Relationship: [keyvaultreference team_keyvaultreference](keyvaultreference.md#BKMK_team_keyvaultreference)

|Property|Value|
|---|---|
|ReferencingEntity|`keyvaultreference`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_keyvaultreference`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_knowledgearticle"></a> team_knowledgearticle

Many-To-One Relationship: [knowledgearticle team_knowledgearticle](knowledgearticle.md#BKMK_team_knowledgearticle)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_knowledgearticle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_letter"></a> team_letter

Many-To-One Relationship: [letter team_letter](letter.md#BKMK_team_letter)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_letter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_mailbox"></a> team_mailbox

Many-To-One Relationship: [mailbox team_mailbox](mailbox.md#BKMK_team_mailbox)

|Property|Value|
|---|---|
|ReferencingEntity|`mailbox`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_mailbox`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_mailboxtrackingfolder"></a> team_mailboxtrackingfolder

Many-To-One Relationship: [mailboxtrackingfolder team_mailboxtrackingfolder](mailboxtrackingfolder.md#BKMK_team_mailboxtrackingfolder)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_mailboxtrackingfolder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_managedidentity"></a> team_managedidentity

Many-To-One Relationship: [managedidentity team_managedidentity](managedidentity.md#BKMK_team_managedidentity)

|Property|Value|
|---|---|
|ReferencingEntity|`managedidentity`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_managedidentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aibdataset"></a> team_msdyn_aibdataset

Many-To-One Relationship: [msdyn_aibdataset team_msdyn_aibdataset](msdyn_aibdataset.md#BKMK_team_msdyn_aibdataset)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdataset`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aibdataset`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aibdatasetfile"></a> team_msdyn_aibdatasetfile

Many-To-One Relationship: [msdyn_aibdatasetfile team_msdyn_aibdatasetfile](msdyn_aibdatasetfile.md#BKMK_team_msdyn_aibdatasetfile)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdatasetfile`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aibdatasetfile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aibdatasetrecord"></a> team_msdyn_aibdatasetrecord

Many-To-One Relationship: [msdyn_aibdatasetrecord team_msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md#BKMK_team_msdyn_aibdatasetrecord)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdatasetrecord`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aibdatasetrecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aibdatasetscontainer"></a> team_msdyn_aibdatasetscontainer

Many-To-One Relationship: [msdyn_aibdatasetscontainer team_msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md#BKMK_team_msdyn_aibdatasetscontainer)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdatasetscontainer`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aibdatasetscontainer`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aibfeedbackloop"></a> team_msdyn_aibfeedbackloop

Many-To-One Relationship: [msdyn_aibfeedbackloop team_msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md#BKMK_team_msdyn_aibfeedbackloop)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfeedbackloop`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aibfeedbackloop`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aibfile"></a> team_msdyn_aibfile

Many-To-One Relationship: [msdyn_aibfile team_msdyn_aibfile](msdyn_aibfile.md#BKMK_team_msdyn_aibfile)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfile`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aibfile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aibfileattacheddata"></a> team_msdyn_aibfileattacheddata

Many-To-One Relationship: [msdyn_aibfileattacheddata team_msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md#BKMK_team_msdyn_aibfileattacheddata)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfileattacheddata`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aibfileattacheddata`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aidataprocessingevent"></a> team_msdyn_aidataprocessingevent

Many-To-One Relationship: [msdyn_aidataprocessingevent team_msdyn_aidataprocessingevent](msdyn_aidataprocessingevent.md#BKMK_team_msdyn_aidataprocessingevent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aidataprocessingevent`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aidataprocessingevent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aievaluationconfiguration"></a> team_msdyn_aievaluationconfiguration

Many-To-One Relationship: [msdyn_aievaluationconfiguration team_msdyn_aievaluationconfiguration](msdyn_aievaluationconfiguration.md#BKMK_team_msdyn_aievaluationconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aievaluationconfiguration`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aievaluationconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aievaluationrun"></a> team_msdyn_aievaluationrun

Many-To-One Relationship: [msdyn_aievaluationrun team_msdyn_aievaluationrun](msdyn_aievaluationrun.md#BKMK_team_msdyn_aievaluationrun)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aievaluationrun`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aievaluationrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aievent"></a> team_msdyn_aievent

Many-To-One Relationship: [msdyn_aievent team_msdyn_aievent](msdyn_aievent.md#BKMK_team_msdyn_aievent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aievent`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aievent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aifptrainingdocument"></a> team_msdyn_aifptrainingdocument

Many-To-One Relationship: [msdyn_aifptrainingdocument team_msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md#BKMK_team_msdyn_aifptrainingdocument)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aifptrainingdocument`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aifptrainingdocument`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aimodel"></a> team_msdyn_aimodel

Many-To-One Relationship: [msdyn_aimodel team_msdyn_aimodel](msdyn_aimodel.md#BKMK_team_msdyn_aimodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aimodel`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aimodel`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aiodimage"></a> team_msdyn_aiodimage

Many-To-One Relationship: [msdyn_aiodimage team_msdyn_aiodimage](msdyn_aiodimage.md#BKMK_team_msdyn_aiodimage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodimage`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aiodimage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aiodlabel"></a> team_msdyn_aiodlabel

Many-To-One Relationship: [msdyn_aiodlabel team_msdyn_aiodlabel](msdyn_aiodlabel.md#BKMK_team_msdyn_aiodlabel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodlabel`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aiodlabel`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aiodtrainingboundingbox"></a> team_msdyn_aiodtrainingboundingbox

Many-To-One Relationship: [msdyn_aiodtrainingboundingbox team_msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md#BKMK_team_msdyn_aiodtrainingboundingbox)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aiodtrainingboundingbox`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aiodtrainingimage"></a> team_msdyn_aiodtrainingimage

Many-To-One Relationship: [msdyn_aiodtrainingimage team_msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md#BKMK_team_msdyn_aiodtrainingimage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodtrainingimage`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aiodtrainingimage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aitemplate"></a> team_msdyn_aitemplate

Many-To-One Relationship: [msdyn_aitemplate team_msdyn_aitemplate](msdyn_aitemplate.md#BKMK_team_msdyn_aitemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitemplate`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aitemplate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aitestcase"></a> team_msdyn_aitestcase

Many-To-One Relationship: [msdyn_aitestcase team_msdyn_aitestcase](msdyn_aitestcase.md#BKMK_team_msdyn_aitestcase)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestcase`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aitestcase`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aitestcasedocument"></a> team_msdyn_aitestcasedocument

Many-To-One Relationship: [msdyn_aitestcasedocument team_msdyn_aitestcasedocument](msdyn_aitestcasedocument.md#BKMK_team_msdyn_aitestcasedocument)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestcasedocument`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aitestcasedocument`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aitestcaseinput"></a> team_msdyn_aitestcaseinput

Many-To-One Relationship: [msdyn_aitestcaseinput team_msdyn_aitestcaseinput](msdyn_aitestcaseinput.md#BKMK_team_msdyn_aitestcaseinput)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestcaseinput`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aitestcaseinput`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aitestrun"></a> team_msdyn_aitestrun

Many-To-One Relationship: [msdyn_aitestrun team_msdyn_aitestrun](msdyn_aitestrun.md#BKMK_team_msdyn_aitestrun)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestrun`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aitestrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_aitestrunbatch"></a> team_msdyn_aitestrunbatch

Many-To-One Relationship: [msdyn_aitestrunbatch team_msdyn_aitestrunbatch](msdyn_aitestrunbatch.md#BKMK_team_msdyn_aitestrunbatch)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestrunbatch`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_aitestrunbatch`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_analysiscomponent"></a> team_msdyn_analysiscomponent

Many-To-One Relationship: [msdyn_analysiscomponent team_msdyn_analysiscomponent](msdyn_analysiscomponent.md#BKMK_team_msdyn_analysiscomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysiscomponent`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_analysiscomponent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_analysisjob"></a> team_msdyn_analysisjob

Many-To-One Relationship: [msdyn_analysisjob team_msdyn_analysisjob](msdyn_analysisjob.md#BKMK_team_msdyn_analysisjob)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisjob`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_analysisjob`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_analysisoverride"></a> team_msdyn_analysisoverride

Many-To-One Relationship: [msdyn_analysisoverride team_msdyn_analysisoverride](msdyn_analysisoverride.md#BKMK_team_msdyn_analysisoverride)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisoverride`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_analysisoverride`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_analysisresult"></a> team_msdyn_analysisresult

Many-To-One Relationship: [msdyn_analysisresult team_msdyn_analysisresult](msdyn_analysisresult.md#BKMK_team_msdyn_analysisresult)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisresult`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_analysisresult`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_analysisresultdetail"></a> team_msdyn_analysisresultdetail

Many-To-One Relationship: [msdyn_analysisresultdetail team_msdyn_analysisresultdetail](msdyn_analysisresultdetail.md#BKMK_team_msdyn_analysisresultdetail)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisresultdetail`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_analysisresultdetail`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_copilotinteractions"></a> team_msdyn_copilotinteractions

Many-To-One Relationship: [msdyn_copilotinteractions team_msdyn_copilotinteractions](msdyn_copilotinteractions.md#BKMK_team_msdyn_copilotinteractions)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_copilotinteractions`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_copilotinteractions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_customcontrolextendedsettings"></a> team_msdyn_customcontrolextendedsettings

Many-To-One Relationship: [msdyn_customcontrolextendedsettings team_msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md#BKMK_team_msdyn_customcontrolextendedsettings)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_customcontrolextendedsettings`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_customcontrolextendedsettings`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_dataflow"></a> team_msdyn_dataflow

Many-To-One Relationship: [msdyn_dataflow team_msdyn_dataflow](msdyn_dataflow.md#BKMK_team_msdyn_dataflow)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflow`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_dataflow`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_dataflow_datalakefolder"></a> team_msdyn_dataflow_datalakefolder

Many-To-One Relationship: [msdyn_dataflow_datalakefolder team_msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md#BKMK_team_msdyn_dataflow_datalakefolder)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflow_datalakefolder`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_dataflow_datalakefolder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_dataflowconnectionreference"></a> team_msdyn_dataflowconnectionreference

Many-To-One Relationship: [msdyn_dataflowconnectionreference team_msdyn_dataflowconnectionreference](msdyn_dataflowconnectionreference.md#BKMK_team_msdyn_dataflowconnectionreference)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflowconnectionreference`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_dataflowconnectionreference`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_dataflowrefreshhistory"></a> team_msdyn_dataflowrefreshhistory

Many-To-One Relationship: [msdyn_dataflowrefreshhistory team_msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md#BKMK_team_msdyn_dataflowrefreshhistory)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflowrefreshhistory`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_dataflowrefreshhistory`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_dataflowtemplate"></a> team_msdyn_dataflowtemplate

Many-To-One Relationship: [msdyn_dataflowtemplate team_msdyn_dataflowtemplate](msdyn_dataflowtemplate.md#BKMK_team_msdyn_dataflowtemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflowtemplate`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_dataflowtemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_dmsrequest"></a> team_msdyn_dmsrequest

Many-To-One Relationship: [msdyn_dmsrequest team_msdyn_dmsrequest](msdyn_dmsrequest.md#BKMK_team_msdyn_dmsrequest)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmsrequest`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_dmsrequest`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_dmsrequeststatus"></a> team_msdyn_dmsrequeststatus

Many-To-One Relationship: [msdyn_dmsrequeststatus team_msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md#BKMK_team_msdyn_dmsrequeststatus)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmsrequeststatus`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_dmsrequeststatus`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_dmssyncrequest"></a> team_msdyn_dmssyncrequest

Many-To-One Relationship: [msdyn_dmssyncrequest team_msdyn_dmssyncrequest](msdyn_dmssyncrequest.md#BKMK_team_msdyn_dmssyncrequest)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmssyncrequest`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_dmssyncrequest`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_dmssyncstatus"></a> team_msdyn_dmssyncstatus

Many-To-One Relationship: [msdyn_dmssyncstatus team_msdyn_dmssyncstatus](msdyn_dmssyncstatus.md#BKMK_team_msdyn_dmssyncstatus)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmssyncstatus`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_dmssyncstatus`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_entitylinkchatconfiguration"></a> team_msdyn_entitylinkchatconfiguration

Many-To-One Relationship: [msdyn_entitylinkchatconfiguration team_msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md#BKMK_team_msdyn_entitylinkchatconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_entitylinkchatconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_entityrefreshhistory"></a> team_msdyn_entityrefreshhistory

Many-To-One Relationship: [msdyn_entityrefreshhistory team_msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md#BKMK_team_msdyn_entityrefreshhistory)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_entityrefreshhistory`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_entityrefreshhistory`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_favoriteknowledgearticle"></a> team_msdyn_favoriteknowledgearticle

Many-To-One Relationship: [msdyn_favoriteknowledgearticle team_msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md#BKMK_team_msdyn_favoriteknowledgearticle)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_favoriteknowledgearticle`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_favoriteknowledgearticle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_federatedarticle"></a> team_msdyn_federatedarticle

Many-To-One Relationship: [msdyn_federatedarticle team_msdyn_federatedarticle](msdyn_federatedarticle.md#BKMK_team_msdyn_federatedarticle)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_federatedarticle`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_federatedarticle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_fileupload"></a> team_msdyn_fileupload

Many-To-One Relationship: [msdyn_fileupload team_msdyn_fileupload](msdyn_fileupload.md#BKMK_team_msdyn_fileupload)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_fileupload`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_fileupload`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_flow_actionapprovalmodel"></a> team_msdyn_flow_actionapprovalmodel

Many-To-One Relationship: [msdyn_flow_actionapprovalmodel team_msdyn_flow_actionapprovalmodel](msdyn_flow_actionapprovalmodel.md#BKMK_team_msdyn_flow_actionapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_flow_actionapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_flow_approval"></a> team_msdyn_flow_approval

Many-To-One Relationship: [msdyn_flow_approval team_msdyn_flow_approval](msdyn_flow_approval.md#BKMK_team_msdyn_flow_approval)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approval`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_flow_approval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_flow_approvalrequest"></a> team_msdyn_flow_approvalrequest

Many-To-One Relationship: [msdyn_flow_approvalrequest team_msdyn_flow_approvalrequest](msdyn_flow_approvalrequest.md#BKMK_team_msdyn_flow_approvalrequest)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalrequest`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_flow_approvalrequest`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_flow_approvalresponse"></a> team_msdyn_flow_approvalresponse

Many-To-One Relationship: [msdyn_flow_approvalresponse team_msdyn_flow_approvalresponse](msdyn_flow_approvalresponse.md#BKMK_team_msdyn_flow_approvalresponse)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalresponse`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_flow_approvalresponse`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_flow_approvalstep"></a> team_msdyn_flow_approvalstep

Many-To-One Relationship: [msdyn_flow_approvalstep team_msdyn_flow_approvalstep](msdyn_flow_approvalstep.md#BKMK_team_msdyn_flow_approvalstep)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalstep`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_flow_approvalstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_flow_awaitallactionapprovalmodel"></a> team_msdyn_flow_awaitallactionapprovalmodel

Many-To-One Relationship: [msdyn_flow_awaitallactionapprovalmodel team_msdyn_flow_awaitallactionapprovalmodel](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_team_msdyn_flow_awaitallactionapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_flow_awaitallactionapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_flow_awaitallapprovalmodel"></a> team_msdyn_flow_awaitallapprovalmodel

Many-To-One Relationship: [msdyn_flow_awaitallapprovalmodel team_msdyn_flow_awaitallapprovalmodel](msdyn_flow_awaitallapprovalmodel.md#BKMK_team_msdyn_flow_awaitallapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_flow_awaitallapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_flow_basicapprovalmodel"></a> team_msdyn_flow_basicapprovalmodel

Many-To-One Relationship: [msdyn_flow_basicapprovalmodel team_msdyn_flow_basicapprovalmodel](msdyn_flow_basicapprovalmodel.md#BKMK_team_msdyn_flow_basicapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_flow_basicapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_flow_flowapproval"></a> team_msdyn_flow_flowapproval

Many-To-One Relationship: [msdyn_flow_flowapproval team_msdyn_flow_flowapproval](msdyn_flow_flowapproval.md#BKMK_team_msdyn_flow_flowapproval)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_flowapproval`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_flow_flowapproval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_formmapping"></a> team_msdyn_formmapping

Many-To-One Relationship: [msdyn_formmapping team_msdyn_formmapping](msdyn_formmapping.md#BKMK_team_msdyn_formmapping)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_formmapping`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_formmapping`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_function"></a> team_msdyn_function

Many-To-One Relationship: [msdyn_function team_msdyn_function](msdyn_function.md#BKMK_team_msdyn_function)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_function`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_function`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_integratedsearchprovider"></a> team_msdyn_integratedsearchprovider

Many-To-One Relationship: [msdyn_integratedsearchprovider team_msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md#BKMK_team_msdyn_integratedsearchprovider)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_integratedsearchprovider`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_integratedsearchprovider`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_kalanguagesetting"></a> team_msdyn_kalanguagesetting

Many-To-One Relationship: [msdyn_kalanguagesetting team_msdyn_kalanguagesetting](msdyn_kalanguagesetting.md#BKMK_team_msdyn_kalanguagesetting)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_kalanguagesetting`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_kalanguagesetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_kbattachment"></a> team_msdyn_kbattachment

Many-To-One Relationship: [msdyn_kbattachment team_msdyn_kbattachment](msdyn_kbattachment.md#BKMK_team_msdyn_kbattachment)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_kbattachment`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_kbattachment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_kmfederatedsearchconfig"></a> team_msdyn_kmfederatedsearchconfig

Many-To-One Relationship: [msdyn_kmfederatedsearchconfig team_msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md#BKMK_team_msdyn_kmfederatedsearchconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_kmfederatedsearchconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_knowledgearticleimage"></a> team_msdyn_knowledgearticleimage

Many-To-One Relationship: [msdyn_knowledgearticleimage team_msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md#BKMK_team_msdyn_knowledgearticleimage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgearticleimage`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_knowledgearticleimage`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_knowledgearticletemplate"></a> team_msdyn_knowledgearticletemplate

Many-To-One Relationship: [msdyn_knowledgearticletemplate team_msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md#BKMK_team_msdyn_knowledgearticletemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgearticletemplate`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_knowledgearticletemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_knowledgeassetconfiguration"></a> team_msdyn_knowledgeassetconfiguration

Many-To-One Relationship: [msdyn_knowledgeassetconfiguration team_msdyn_knowledgeassetconfiguration](msdyn_knowledgeassetconfiguration.md#BKMK_team_msdyn_knowledgeassetconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgeassetconfiguration`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_knowledgeassetconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_knowledgeinteractioninsight"></a> team_msdyn_knowledgeinteractioninsight

Many-To-One Relationship: [msdyn_knowledgeinteractioninsight team_msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md#BKMK_team_msdyn_knowledgeinteractioninsight)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_knowledgeinteractioninsight`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_knowledgemanagementsetting"></a> team_msdyn_knowledgemanagementsetting

Many-To-One Relationship: [msdyn_knowledgemanagementsetting team_msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md#BKMK_team_msdyn_knowledgemanagementsetting)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgemanagementsetting`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_knowledgemanagementsetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_knowledgepersonalfilter"></a> team_msdyn_knowledgepersonalfilter

Many-To-One Relationship: [msdyn_knowledgepersonalfilter team_msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md#BKMK_team_msdyn_knowledgepersonalfilter)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgepersonalfilter`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_knowledgepersonalfilter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_knowledgesearchfilter"></a> team_msdyn_knowledgesearchfilter

Many-To-One Relationship: [msdyn_knowledgesearchfilter team_msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md#BKMK_team_msdyn_knowledgesearchfilter)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgesearchfilter`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_knowledgesearchfilter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_knowledgesearchinsight"></a> team_msdyn_knowledgesearchinsight

Many-To-One Relationship: [msdyn_knowledgesearchinsight team_msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md#BKMK_team_msdyn_knowledgesearchinsight)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgesearchinsight`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_knowledgesearchinsight`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_mobileapp"></a> team_msdyn_mobileapp

Many-To-One Relationship: [msdyn_mobileapp team_msdyn_mobileapp](msdyn_mobileapp.md#BKMK_team_msdyn_mobileapp)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_mobileapp`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmanalysishistory"></a> team_msdyn_pmanalysishistory

Many-To-One Relationship: [msdyn_pmanalysishistory team_msdyn_pmanalysishistory](msdyn_pmanalysishistory.md#BKMK_team_msdyn_pmanalysishistory)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmanalysishistory`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmanalysishistory`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmbusinessruleautomationconfig"></a> team_msdyn_pmbusinessruleautomationconfig

Many-To-One Relationship: [msdyn_pmbusinessruleautomationconfig team_msdyn_pmbusinessruleautomationconfig](msdyn_pmbusinessruleautomationconfig.md#BKMK_team_msdyn_pmbusinessruleautomationconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmbusinessruleautomationconfig`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmcalendar"></a> team_msdyn_pmcalendar

Many-To-One Relationship: [msdyn_pmcalendar team_msdyn_pmcalendar](msdyn_pmcalendar.md#BKMK_team_msdyn_pmcalendar)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmcalendar`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmcalendar`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmcalendarversion"></a> team_msdyn_pmcalendarversion

Many-To-One Relationship: [msdyn_pmcalendarversion team_msdyn_pmcalendarversion](msdyn_pmcalendarversion.md#BKMK_team_msdyn_pmcalendarversion)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmcalendarversion`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmcalendarversion`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pminferredtask"></a> team_msdyn_pminferredtask

Many-To-One Relationship: [msdyn_pminferredtask team_msdyn_pminferredtask](msdyn_pminferredtask.md#BKMK_team_msdyn_pminferredtask)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pminferredtask`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pminferredtask`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmprocessextendedmetadataversion"></a> team_msdyn_pmprocessextendedmetadataversion

Many-To-One Relationship: [msdyn_pmprocessextendedmetadataversion team_msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md#BKMK_team_msdyn_pmprocessextendedmetadataversion)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocessextendedmetadataversion`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmprocessextendedmetadataversion`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmprocesstemplate"></a> team_msdyn_pmprocesstemplate

Many-To-One Relationship: [msdyn_pmprocesstemplate team_msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md#BKMK_team_msdyn_pmprocesstemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocesstemplate`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmprocesstemplate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmprocessusersettings"></a> team_msdyn_pmprocessusersettings

Many-To-One Relationship: [msdyn_pmprocessusersettings team_msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md#BKMK_team_msdyn_pmprocessusersettings)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocessusersettings`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmprocessusersettings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmprocessversion"></a> team_msdyn_pmprocessversion

Many-To-One Relationship: [msdyn_pmprocessversion team_msdyn_pmprocessversion](msdyn_pmprocessversion.md#BKMK_team_msdyn_pmprocessversion)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocessversion`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmprocessversion`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmrecording"></a> team_msdyn_pmrecording

Many-To-One Relationship: [msdyn_pmrecording team_msdyn_pmrecording](msdyn_pmrecording.md#BKMK_team_msdyn_pmrecording)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmrecording`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmrecording`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmsimulation"></a> team_msdyn_pmsimulation

Many-To-One Relationship: [msdyn_pmsimulation team_msdyn_pmsimulation](msdyn_pmsimulation.md#BKMK_team_msdyn_pmsimulation)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmsimulation`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmsimulation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmtemplate"></a> team_msdyn_pmtemplate

Many-To-One Relationship: [msdyn_pmtemplate team_msdyn_pmtemplate](msdyn_pmtemplate.md#BKMK_team_msdyn_pmtemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmtemplate`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmtemplate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_pmview"></a> team_msdyn_pmview

Many-To-One Relationship: [msdyn_pmview team_msdyn_pmview](msdyn_pmview.md#BKMK_team_msdyn_pmview)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmview`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_pmview`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_qna"></a> team_msdyn_qna

Many-To-One Relationship: [msdyn_qna team_msdyn_qna](msdyn_qna.md#BKMK_team_msdyn_qna)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_qna`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_qna`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_richtextfile"></a> team_msdyn_richtextfile

Many-To-One Relationship: [msdyn_richtextfile team_msdyn_richtextfile](msdyn_richtextfile.md#BKMK_team_msdyn_richtextfile)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_richtextfile`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_richtextfile`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_salesforcestructuredobject"></a> team_msdyn_salesforcestructuredobject

Many-To-One Relationship: [msdyn_salesforcestructuredobject team_msdyn_salesforcestructuredobject](msdyn_salesforcestructuredobject.md#BKMK_team_msdyn_salesforcestructuredobject)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_salesforcestructuredobject`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_salesforcestructuredobject`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_salesforcestructuredqnaconfig"></a> team_msdyn_salesforcestructuredqnaconfig

Many-To-One Relationship: [msdyn_salesforcestructuredqnaconfig team_msdyn_salesforcestructuredqnaconfig](msdyn_salesforcestructuredqnaconfig.md#BKMK_team_msdyn_salesforcestructuredqnaconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_salesforcestructuredqnaconfig`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_salesforcestructuredqnaconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_schedule"></a> team_msdyn_schedule

Many-To-One Relationship: [msdyn_schedule team_msdyn_schedule](msdyn_schedule.md#BKMK_team_msdyn_schedule)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_schedule`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_schedule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_serviceconfiguration"></a> team_msdyn_serviceconfiguration

Many-To-One Relationship: [msdyn_serviceconfiguration team_msdyn_serviceconfiguration](msdyn_serviceconfiguration.md#BKMK_team_msdyn_serviceconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_serviceconfiguration`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_serviceconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_slakpi"></a> team_msdyn_slakpi

Many-To-One Relationship: [msdyn_slakpi team_msdyn_slakpi](msdyn_slakpi.md#BKMK_team_msdyn_slakpi)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_slakpi`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_slakpi`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_solutionhealthrule"></a> team_msdyn_solutionhealthrule

Many-To-One Relationship: [msdyn_solutionhealthrule team_msdyn_solutionhealthrule](msdyn_solutionhealthrule.md#BKMK_team_msdyn_solutionhealthrule)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_solutionhealthrule`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_solutionhealthrule`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_solutionhealthruleargument"></a> team_msdyn_solutionhealthruleargument

Many-To-One Relationship: [msdyn_solutionhealthruleargument team_msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md#BKMK_team_msdyn_solutionhealthruleargument)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_solutionhealthruleargument`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_solutionhealthruleargument`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdyn_virtualtablecolumncandidate"></a> team_msdyn_virtualtablecolumncandidate

Many-To-One Relationship: [msdyn_virtualtablecolumncandidate team_msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md#BKMK_team_msdyn_virtualtablecolumncandidate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdyn_virtualtablecolumncandidate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_msdynce_botcontent"></a> team_msdynce_botcontent

Many-To-One Relationship: [msdynce_botcontent team_msdynce_botcontent](msdynce_botcontent.md#BKMK_team_msdynce_botcontent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdynce_botcontent`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_msdynce_botcontent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_mspcat_catalogsubmissionfiles"></a> team_mspcat_catalogsubmissionfiles

Many-To-One Relationship: [mspcat_catalogsubmissionfiles team_mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md#BKMK_team_mspcat_catalogsubmissionfiles)

|Property|Value|
|---|---|
|ReferencingEntity|`mspcat_catalogsubmissionfiles`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_mspcat_catalogsubmissionfiles`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_mspcat_packagestore"></a> team_mspcat_packagestore

Many-To-One Relationship: [mspcat_packagestore team_mspcat_packagestore](mspcat_packagestore.md#BKMK_team_mspcat_packagestore)

|Property|Value|
|---|---|
|ReferencingEntity|`mspcat_packagestore`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_mspcat_packagestore`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_nlsqregistration"></a> team_nlsqregistration

Many-To-One Relationship: [nlsqregistration team_nlsqregistration](nlsqregistration.md#BKMK_team_nlsqregistration)

|Property|Value|
|---|---|
|ReferencingEntity|`nlsqregistration`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_nlsqregistration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_phonecall"></a> team_phonecall

Many-To-One Relationship: [phonecall team_phonecall](phonecall.md#BKMK_team_phonecall)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_phonecall`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_plannerbusinessscenario"></a> team_plannerbusinessscenario

Many-To-One Relationship: [plannerbusinessscenario team_plannerbusinessscenario](plannerbusinessscenario.md#BKMK_team_plannerbusinessscenario)

|Property|Value|
|---|---|
|ReferencingEntity|`plannerbusinessscenario`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_plannerbusinessscenario`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_plannersyncaction"></a> team_plannersyncaction

Many-To-One Relationship: [plannersyncaction team_plannersyncaction](plannersyncaction.md#BKMK_team_plannersyncaction)

|Property|Value|
|---|---|
|ReferencingEntity|`plannersyncaction`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_plannersyncaction`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_plugin"></a> team_plugin

Many-To-One Relationship: [plugin team_plugin](plugin.md#BKMK_team_plugin)

|Property|Value|
|---|---|
|ReferencingEntity|`plugin`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_plugin`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_PostRegardings"></a> team_PostRegardings

Many-To-One Relationship: [postregarding team_PostRegardings](postregarding.md#BKMK_team_PostRegardings)

|Property|Value|
|---|---|
|ReferencingEntity|`postregarding`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`team_PostRegardings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerbidataset"></a> team_powerbidataset

Many-To-One Relationship: [powerbidataset team_powerbidataset](powerbidataset.md#BKMK_team_powerbidataset)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbidataset`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerbidataset`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerbidatasetapdx"></a> team_powerbidatasetapdx

Many-To-One Relationship: [powerbidatasetapdx team_powerbidatasetapdx](powerbidatasetapdx.md#BKMK_team_powerbidatasetapdx)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbidatasetapdx`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerbidatasetapdx`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerbimashupparameter"></a> team_powerbimashupparameter

Many-To-One Relationship: [powerbimashupparameter team_powerbimashupparameter](powerbimashupparameter.md#BKMK_team_powerbimashupparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbimashupparameter`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerbimashupparameter`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerbireport"></a> team_powerbireport

Many-To-One Relationship: [powerbireport team_powerbireport](powerbireport.md#BKMK_team_powerbireport)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbireport`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerbireport`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerbireportapdx"></a> team_powerbireportapdx

Many-To-One Relationship: [powerbireportapdx team_powerbireportapdx](powerbireportapdx.md#BKMK_team_powerbireportapdx)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbireportapdx`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerbireportapdx`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerfxrule"></a> team_powerfxrule

Many-To-One Relationship: [powerfxrule team_powerfxrule](powerfxrule.md#BKMK_team_powerfxrule)

|Property|Value|
|---|---|
|ReferencingEntity|`powerfxrule`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerfxrule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerpagecomponent"></a> team_powerpagecomponent

Many-To-One Relationship: [powerpagecomponent team_powerpagecomponent](powerpagecomponent.md#BKMK_team_powerpagecomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagecomponent`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerpagecomponent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerpagesite"></a> team_powerpagesite

Many-To-One Relationship: [powerpagesite team_powerpagesite](powerpagesite.md#BKMK_team_powerpagesite)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesite`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerpagesite`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerpagesitelanguage"></a> team_powerpagesitelanguage

Many-To-One Relationship: [powerpagesitelanguage team_powerpagesitelanguage](powerpagesitelanguage.md#BKMK_team_powerpagesitelanguage)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesitelanguage`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerpagesitelanguage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerpagesitepublished"></a> team_powerpagesitepublished

Many-To-One Relationship: [powerpagesitepublished team_powerpagesitepublished](powerpagesitepublished.md#BKMK_team_powerpagesitepublished)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesitepublished`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerpagesitepublished`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerpageslog"></a> team_powerpageslog

Many-To-One Relationship: [powerpageslog team_powerpageslog](powerpageslog.md#BKMK_team_powerpageslog)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpageslog`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerpageslog`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerpagesmanagedidentity"></a> team_powerpagesmanagedidentity

Many-To-One Relationship: [powerpagesmanagedidentity team_powerpagesmanagedidentity](powerpagesmanagedidentity.md#BKMK_team_powerpagesmanagedidentity)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesmanagedidentity`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerpagesmanagedidentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerpagesscanreport"></a> team_powerpagesscanreport

Many-To-One Relationship: [powerpagesscanreport team_powerpagesscanreport](powerpagesscanreport.md#BKMK_team_powerpagesscanreport)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesscanreport`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerpagesscanreport`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_powerpagessiteaifeedback"></a> team_powerpagessiteaifeedback

Many-To-One Relationship: [powerpagessiteaifeedback team_powerpagessiteaifeedback](powerpagessiteaifeedback.md#BKMK_team_powerpagessiteaifeedback)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagessiteaifeedback`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_powerpagessiteaifeedback`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_principalobjectattributeaccess"></a> team_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess team_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_team_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`team_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_principalobjectattributeaccess_principalid"></a> team_principalobjectattributeaccess_principalid

Many-To-One Relationship: [principalobjectattributeaccess team_principalobjectattributeaccess_principalid](principalobjectattributeaccess.md#BKMK_team_principalobjectattributeaccess_principalid)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`principalid`|
|ReferencedEntityNavigationPropertyName|`team_principalobjectattributeaccess_principalid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_privilegecheckerrun"></a> team_privilegecheckerrun

Many-To-One Relationship: [privilegecheckerrun team_privilegecheckerrun](privilegecheckerrun.md#BKMK_team_privilegecheckerrun)

|Property|Value|
|---|---|
|ReferencingEntity|`privilegecheckerrun`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_privilegecheckerrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_processsession"></a> team_processsession

Many-To-One Relationship: [processsession team_processsession](processsession.md#BKMK_team_processsession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_processsession`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Team_ProcessSessions"></a> Team_ProcessSessions

Many-To-One Relationship: [processsession Team_ProcessSessions](processsession.md#BKMK_Team_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Team_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_processstageparameter"></a> team_processstageparameter

Many-To-One Relationship: [processstageparameter team_processstageparameter](processstageparameter.md#BKMK_team_processstageparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`processstageparameter`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_processstageparameter`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_queueitembase_workerid"></a> team_queueitembase_workerid

Many-To-One Relationship: [queueitem team_queueitembase_workerid](queueitem.md#BKMK_team_queueitembase_workerid)

|Property|Value|
|---|---|
|ReferencingEntity|`queueitem`|
|ReferencingAttribute|`workerid`|
|ReferencedEntityNavigationPropertyName|`team_queueitembase_workerid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_recentlyused"></a> team_recentlyused

Many-To-One Relationship: [recentlyused team_recentlyused](recentlyused.md#BKMK_team_recentlyused)

|Property|Value|
|---|---|
|ReferencingEntity|`recentlyused`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_recentlyused`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_recurringappointmentmaster"></a> team_recurringappointmentmaster

Many-To-One Relationship: [recurringappointmentmaster team_recurringappointmentmaster](recurringappointmentmaster.md#BKMK_team_recurringappointmentmaster)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_recurringappointmentmaster`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_retaineddataexcel"></a> team_retaineddataexcel

Many-To-One Relationship: [retaineddataexcel team_retaineddataexcel](retaineddataexcel.md#BKMK_team_retaineddataexcel)

|Property|Value|
|---|---|
|ReferencingEntity|`retaineddataexcel`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_retaineddataexcel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_retentionconfig"></a> team_retentionconfig

Many-To-One Relationship: [retentionconfig team_retentionconfig](retentionconfig.md#BKMK_team_retentionconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionconfig`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_retentionconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_retentionfailuredetail"></a> team_retentionfailuredetail

Many-To-One Relationship: [retentionfailuredetail team_retentionfailuredetail](retentionfailuredetail.md#BKMK_team_retentionfailuredetail)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionfailuredetail`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_retentionfailuredetail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_retentionoperation"></a> team_retentionoperation

Many-To-One Relationship: [retentionoperation team_retentionoperation](retentionoperation.md#BKMK_team_retentionoperation)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionoperation`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_retentionoperation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_retentionsuccessdetail"></a> team_retentionsuccessdetail

Many-To-One Relationship: [retentionsuccessdetail team_retentionsuccessdetail](retentionsuccessdetail.md#BKMK_team_retentionsuccessdetail)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionsuccessdetail`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_retentionsuccessdetail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_savingrule"></a> team_savingrule

Many-To-One Relationship: [savingrule team_savingrule](savingrule.md#BKMK_team_savingrule)

|Property|Value|
|---|---|
|ReferencingEntity|`savingrule`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_savingrule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_sharepointdocumentlocation"></a> team_sharepointdocumentlocation

Many-To-One Relationship: [sharepointdocumentlocation team_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_team_sharepointdocumentlocation)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointdocumentlocation`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_sharepointdocumentlocation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_sharepointsite"></a> team_sharepointsite

Many-To-One Relationship: [sharepointsite team_sharepointsite](sharepointsite.md#BKMK_team_sharepointsite)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointsite`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_sharepointsite`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_sideloadedaiplugin"></a> team_sideloadedaiplugin

Many-To-One Relationship: [sideloadedaiplugin team_sideloadedaiplugin](sideloadedaiplugin.md#BKMK_team_sideloadedaiplugin)

|Property|Value|
|---|---|
|ReferencingEntity|`sideloadedaiplugin`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_sideloadedaiplugin`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_signal"></a> team_signal

Many-To-One Relationship: [signal team_signal](signal.md#BKMK_team_signal)

|Property|Value|
|---|---|
|ReferencingEntity|`signal`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_signal`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_slaBase"></a> team_slaBase

Many-To-One Relationship: [sla team_slaBase](sla.md#BKMK_team_slaBase)

|Property|Value|
|---|---|
|ReferencingEntity|`sla`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_slaBase`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_socialactivity"></a> team_socialactivity

Many-To-One Relationship: [socialactivity team_socialactivity](socialactivity.md#BKMK_team_socialactivity)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_socialactivity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_solutioncomponentbatchconfiguration"></a> team_solutioncomponentbatchconfiguration

Many-To-One Relationship: [solutioncomponentbatchconfiguration team_solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md#BKMK_team_solutioncomponentbatchconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentbatchconfiguration`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_solutioncomponentbatchconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_stagesolutionupload"></a> team_stagesolutionupload

Many-To-One Relationship: [stagesolutionupload team_stagesolutionupload](stagesolutionupload.md#BKMK_team_stagesolutionupload)

|Property|Value|
|---|---|
|ReferencingEntity|`stagesolutionupload`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_stagesolutionupload`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_synapsedatabase"></a> team_synapsedatabase

Many-To-One Relationship: [synapsedatabase team_synapsedatabase](synapsedatabase.md#BKMK_team_synapsedatabase)

|Property|Value|
|---|---|
|ReferencingEntity|`synapsedatabase`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_synapsedatabase`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_SyncError"></a> team_SyncError

Many-To-One Relationship: [syncerror team_SyncError](syncerror.md#BKMK_team_SyncError)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_SyncError`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Team_SyncErrors"></a> Team_SyncErrors

Many-To-One Relationship: [syncerror Team_SyncErrors](syncerror.md#BKMK_Team_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Team_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_tag"></a> team_tag

Many-To-One Relationship: [tag team_tag](tag.md#BKMK_team_tag)

|Property|Value|
|---|---|
|ReferencingEntity|`tag`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_tag`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_taggedflowsession"></a> team_taggedflowsession

Many-To-One Relationship: [taggedflowsession team_taggedflowsession](taggedflowsession.md#BKMK_team_taggedflowsession)

|Property|Value|
|---|---|
|ReferencingEntity|`taggedflowsession`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_taggedflowsession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_taggedprocess"></a> team_taggedprocess

Many-To-One Relationship: [taggedprocess team_taggedprocess](taggedprocess.md#BKMK_team_taggedprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`taggedprocess`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_taggedprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_task"></a> team_task

Many-To-One Relationship: [task team_task](task.md#BKMK_team_task)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_task`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_teammobileofflineprofilemembership_TeamId"></a> team_teammobileofflineprofilemembership_TeamId

Many-To-One Relationship: [teammobileofflineprofilemembership team_teammobileofflineprofilemembership_TeamId](teammobileofflineprofilemembership.md#BKMK_team_teammobileofflineprofilemembership_TeamId)

|Property|Value|
|---|---|
|ReferencingEntity|`teammobileofflineprofilemembership`|
|ReferencingAttribute|`teamid`|
|ReferencedEntityNavigationPropertyName|`team_teammobileofflineprofilemembership_TeamId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_trait"></a> team_trait

Many-To-One Relationship: [trait team_trait](trait.md#BKMK_team_trait)

|Property|Value|
|---|---|
|ReferencingEntity|`trait`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_trait`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_unstructuredfilesearchentity"></a> team_unstructuredfilesearchentity

Many-To-One Relationship: [unstructuredfilesearchentity team_unstructuredfilesearchentity](unstructuredfilesearchentity.md#BKMK_team_unstructuredfilesearchentity)

|Property|Value|
|---|---|
|ReferencingEntity|`unstructuredfilesearchentity`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_unstructuredfilesearchentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_unstructuredfilesearchrecord"></a> team_unstructuredfilesearchrecord

Many-To-One Relationship: [unstructuredfilesearchrecord team_unstructuredfilesearchrecord](unstructuredfilesearchrecord.md#BKMK_team_unstructuredfilesearchrecord)

|Property|Value|
|---|---|
|ReferencingEntity|`unstructuredfilesearchrecord`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_unstructuredfilesearchrecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_userform"></a> team_userform

Many-To-One Relationship: [userform team_userform](userform.md#BKMK_team_userform)

|Property|Value|
|---|---|
|ReferencingEntity|`userform`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_userform`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_userquery"></a> team_userquery

Many-To-One Relationship: [userquery team_userquery](userquery.md#BKMK_team_userquery)

|Property|Value|
|---|---|
|ReferencingEntity|`userquery`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_userquery`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_userqueryvisualizations"></a> team_userqueryvisualizations

Many-To-One Relationship: [userqueryvisualization team_userqueryvisualizations](userqueryvisualization.md#BKMK_team_userqueryvisualizations)

|Property|Value|
|---|---|
|ReferencingEntity|`userqueryvisualization`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_userqueryvisualizations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_workflow"></a> team_workflow

Many-To-One Relationship: [workflow team_workflow](workflow.md#BKMK_team_workflow)

|Property|Value|
|---|---|
|ReferencingEntity|`workflow`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_workflow`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_workflowbinary"></a> team_workflowbinary

Many-To-One Relationship: [workflowbinary team_workflowbinary](workflowbinary.md#BKMK_team_workflowbinary)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowbinary`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_workflowbinary`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_workflowlog"></a> team_workflowlog

Many-To-One Relationship: [workflowlog team_workflowlog](workflowlog.md#BKMK_team_workflowlog)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowlog`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_workflowlog`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_workflowmetadata"></a> team_workflowmetadata

Many-To-One Relationship: [workflowmetadata team_workflowmetadata](workflowmetadata.md#BKMK_team_workflowmetadata)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowmetadata`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_workflowmetadata`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_workqueue"></a> team_workqueue

Many-To-One Relationship: [workqueue team_workqueue](workqueue.md#BKMK_team_workqueue)

|Property|Value|
|---|---|
|ReferencingEntity|`workqueue`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_workqueue`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_team_workqueueitem"></a> team_workqueueitem

Many-To-One Relationship: [workqueueitem team_workqueueitem](workqueueitem.md#BKMK_team_workqueueitem)

|Property|Value|
|---|---|
|ReferencingEntity|`workqueueitem`|
|ReferencingAttribute|`owningteam`|
|ReferencedEntityNavigationPropertyName|`team_workqueueitem`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [msdyn_flow_actionapprovalmodelrelationship_team](#BKMK_msdyn_flow_actionapprovalmodelrelationship_team)
- [msdyn_flow_awaitallactionmodelrelationship_team](#BKMK_msdyn_flow_awaitallactionmodelrelationship_team)
- [msdyn_flow_awaitallmodelrelationship_team](#BKMK_msdyn_flow_awaitallmodelrelationship_team)
- [msdyn_flow_basicapprovalmodelrelationship_team](#BKMK_msdyn_flow_basicapprovalmodelrelationship_team)
- [teammembership_association](#BKMK_teammembership_association)
- [teamprofiles_association](#BKMK_teamprofiles_association)
- [teamroles_association](#BKMK_teamroles_association)

### <a name="BKMK_msdyn_flow_actionapprovalmodelrelationship_team"></a> msdyn_flow_actionapprovalmodelrelationship_team

See [msdyn_flow_actionapprovalmodel msdyn_flow_actionapprovalmodelrelationship_team Many-To-Many Relationship](msdyn_flow_actionapprovalmodel.md#BKMK_msdyn_flow_actionapprovalmodelrelationship_team)

|Property|Value|
|---|---|
|IntersectEntityName|`msdyn_flow_actionapprovalmodel_team`|
|IsCustomizable|True|
|SchemaName|`msdyn_flow_actionapprovalmodelrelationship_team`|
|IntersectAttribute|`teamid`|
|NavigationPropertyName|`msdyn_flow_actionapprovalmodelrelationship_team`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_awaitallactionmodelrelationship_team"></a> msdyn_flow_awaitallactionmodelrelationship_team

See [msdyn_flow_awaitallactionapprovalmodel msdyn_flow_awaitallactionmodelrelationship_team Many-To-Many Relationship](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_msdyn_flow_awaitallactionmodelrelationship_team)

|Property|Value|
|---|---|
|IntersectEntityName|`msdyn_flow_awaitallactionapprovalmodel_team`|
|IsCustomizable|True|
|SchemaName|`msdyn_flow_awaitallactionmodelrelationship_team`|
|IntersectAttribute|`teamid`|
|NavigationPropertyName|`msdyn_flow_awaitallactionmodelrelationship_team`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_awaitallmodelrelationship_team"></a> msdyn_flow_awaitallmodelrelationship_team

See [msdyn_flow_awaitallapprovalmodel msdyn_flow_awaitallmodelrelationship_team Many-To-Many Relationship](msdyn_flow_awaitallapprovalmodel.md#BKMK_msdyn_flow_awaitallmodelrelationship_team)

|Property|Value|
|---|---|
|IntersectEntityName|`msdyn_flow_awaitallmodel_team`|
|IsCustomizable|True|
|SchemaName|`msdyn_flow_awaitallmodelrelationship_team`|
|IntersectAttribute|`teamid`|
|NavigationPropertyName|`msdyn_flow_awaitallmodelrelationship_team`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_flow_basicapprovalmodelrelationship_team"></a> msdyn_flow_basicapprovalmodelrelationship_team

See [msdyn_flow_basicapprovalmodel msdyn_flow_basicapprovalmodelrelationship_team Many-To-Many Relationship](msdyn_flow_basicapprovalmodel.md#BKMK_msdyn_flow_basicapprovalmodelrelationship_team)

|Property|Value|
|---|---|
|IntersectEntityName|`msdyn_flow_basicapprovalmodel_team`|
|IsCustomizable|True|
|SchemaName|`msdyn_flow_basicapprovalmodelrelationship_team`|
|IntersectAttribute|`teamid`|
|NavigationPropertyName|`msdyn_flow_basicapprovalmodelrelationship_team`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_teammembership_association"></a> teammembership_association

See [systemuser teammembership_association Many-To-Many Relationship](systemuser.md#BKMK_teammembership_association)

|Property|Value|
|---|---|
|IntersectEntityName|`teammembership`|
|IsCustomizable|False|
|SchemaName|`teammembership_association`|
|IntersectAttribute|`teamid`|
|NavigationPropertyName|`teammembership_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_teamprofiles_association"></a> teamprofiles_association

See [fieldsecurityprofile teamprofiles_association Many-To-Many Relationship](fieldsecurityprofile.md#BKMK_teamprofiles_association)

|Property|Value|
|---|---|
|IntersectEntityName|`teamprofiles`|
|IsCustomizable|False|
|SchemaName|`teamprofiles_association`|
|IntersectAttribute|`teamid`|
|NavigationPropertyName|`teamprofiles_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_teamroles_association"></a> teamroles_association

See [role teamroles_association Many-To-Many Relationship](role.md#BKMK_teamroles_association)

|Property|Value|
|---|---|
|IntersectEntityName|`teamroles`|
|IsCustomizable|False|
|SchemaName|`teamroles_association`|
|IntersectAttribute|`teamid`|
|NavigationPropertyName|`teamroles_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.team?displayProperty=fullName>
