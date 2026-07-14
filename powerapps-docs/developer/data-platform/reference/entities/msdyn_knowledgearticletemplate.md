---
title: "Knowledge Article Template (msdyn_knowledgearticletemplate) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Knowledge Article Template (msdyn_knowledgearticletemplate) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Knowledge Article Template (msdyn_knowledgearticletemplate) table/entity reference (Microsoft Dataverse)

Organizational Knowledge Article Template for Internal and external creation of Knowledge Articles.

## Messages

The following table lists the messages for the Knowledge Article Template (msdyn_knowledgearticletemplate) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_knowledgearticletemplates(*msdyn_knowledgearticletemplateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_knowledgearticletemplates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_knowledgearticletemplates(*msdyn_knowledgearticletemplateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_knowledgearticletemplates(*msdyn_knowledgearticletemplateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_knowledgearticletemplates<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_knowledgearticletemplates(*msdyn_knowledgearticletemplateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_knowledgearticletemplates(*msdyn_knowledgearticletemplateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_knowledgearticletemplates(*msdyn_knowledgearticletemplateid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Knowledge Article Template (msdyn_knowledgearticletemplate) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Knowledge Article Template** |
| **DisplayCollectionName** | **Knowledge Article Templates** |
| **SchemaName** | `msdyn_knowledgearticletemplate` |
| **CollectionSchemaName** | `msdyn_knowledgearticletemplates` |
| **EntitySetName** | `msdyn_knowledgearticletemplates`|
| **LogicalName** | `msdyn_knowledgearticletemplate` |
| **LogicalCollectionName** | `msdyn_knowledgearticletemplates` |
| **PrimaryIdAttribute** | `msdyn_knowledgearticletemplateid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_Content](#BKMK_msdyn_Content)
- [msdyn_Description](#BKMK_msdyn_Description)
- [msdyn_isinternal](#BKMK_msdyn_isinternal)
- [msdyn_keywords](#BKMK_msdyn_keywords)
- [msdyn_knowledgearticletemplateId](#BKMK_msdyn_knowledgearticletemplateId)
- [msdyn_languagelocaleid](#BKMK_msdyn_languagelocaleid)
- [msdyn_LanguageLocaleIdName](#BKMK_msdyn_LanguageLocaleIdName)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_sectiondetails](#BKMK_msdyn_sectiondetails)
- [msdyn_subjectid](#BKMK_msdyn_subjectid)
- [msdyn_title](#BKMK_msdyn_title)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

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

### <a name="BKMK_msdyn_Content"></a> msdyn_Content

|Property|Value|
|---|---|
|Description|**Shows the body of the article stored in HTML format.**|
|DisplayName|**Content**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_content`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_msdyn_Description"></a> msdyn_Description

|Property|Value|
|---|---|
|Description||
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|155|

### <a name="BKMK_msdyn_isinternal"></a> msdyn_isinternal

|Property|Value|
|---|---|
|Description|**Shows whether this article is only visible internally.**|
|DisplayName|**Internal**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isinternal`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`knowledgearticle_isinternal`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_keywords"></a> msdyn_keywords

|Property|Value|
|---|---|
|Description||
|DisplayName|**Keywords**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_keywords`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_knowledgearticletemplateId"></a> msdyn_knowledgearticletemplateId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Knowledge Article Template**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_knowledgearticletemplateid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_languagelocaleid"></a> msdyn_languagelocaleid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Article Template Language Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_languagelocaleid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|36|

### <a name="BKMK_msdyn_LanguageLocaleIdName"></a> msdyn_LanguageLocaleIdName

|Property|Value|
|---|---|
|Description||
|DisplayName|**Article Language Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_LanguageLocaleIdName`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|320|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**Type a name for the Knowledge Article Template**|
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
|MaxLength|4000|

### <a name="BKMK_msdyn_sectiondetails"></a> msdyn_sectiondetails

|Property|Value|
|---|---|
|Description|**Shows the section details of the template for article generation.**|
|DisplayName|**Template Section Details**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_sectiondetails`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_subjectid"></a> msdyn_subjectid

|Property|Value|
|---|---|
|Description|**Choose the subject of the article to assist with article searches. You can configure subjects under Business Management in the Settings area.**|
|DisplayName|**Subject**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_subjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|subject|

### <a name="BKMK_msdyn_title"></a> msdyn_title

|Property|Value|
|---|---|
|Description|**Type a title for the Knowledge Article Template**|
|DisplayName|**Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_title`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Knowledge Article Template**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_knowledgearticletemplate_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Knowledge Article Template**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_knowledgearticletemplate_statuscode`|

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

- [business_unit_msdyn_knowledgearticletemplate](#BKMK_business_unit_msdyn_knowledgearticletemplate)
- [lk_msdyn_knowledgearticletemplate_createdby](#BKMK_lk_msdyn_knowledgearticletemplate_createdby)
- [lk_msdyn_knowledgearticletemplate_createdonbehalfby](#BKMK_lk_msdyn_knowledgearticletemplate_createdonbehalfby)
- [lk_msdyn_knowledgearticletemplate_modifiedby](#BKMK_lk_msdyn_knowledgearticletemplate_modifiedby)
- [lk_msdyn_knowledgearticletemplate_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgearticletemplate_modifiedonbehalfby)
- [msdyn_subject_knowledgearticletemplate_subjectid](#BKMK_msdyn_subject_knowledgearticletemplate_subjectid)
- [owner_msdyn_knowledgearticletemplate](#BKMK_owner_msdyn_knowledgearticletemplate)
- [team_msdyn_knowledgearticletemplate](#BKMK_team_msdyn_knowledgearticletemplate)
- [user_msdyn_knowledgearticletemplate](#BKMK_user_msdyn_knowledgearticletemplate)

### <a name="BKMK_business_unit_msdyn_knowledgearticletemplate"></a> business_unit_msdyn_knowledgearticletemplate

One-To-Many Relationship: [businessunit business_unit_msdyn_knowledgearticletemplate](businessunit.md#BKMK_business_unit_msdyn_knowledgearticletemplate)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgearticletemplate_createdby"></a> lk_msdyn_knowledgearticletemplate_createdby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgearticletemplate_createdby](systemuser.md#BKMK_lk_msdyn_knowledgearticletemplate_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgearticletemplate_createdonbehalfby"></a> lk_msdyn_knowledgearticletemplate_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgearticletemplate_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgearticletemplate_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgearticletemplate_modifiedby"></a> lk_msdyn_knowledgearticletemplate_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgearticletemplate_modifiedby](systemuser.md#BKMK_lk_msdyn_knowledgearticletemplate_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgearticletemplate_modifiedonbehalfby"></a> lk_msdyn_knowledgearticletemplate_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgearticletemplate_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgearticletemplate_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_subject_knowledgearticletemplate_subjectid"></a> msdyn_subject_knowledgearticletemplate_subjectid

One-To-Many Relationship: [subject msdyn_subject_knowledgearticletemplate_subjectid](subject.md#BKMK_msdyn_subject_knowledgearticletemplate_subjectid)

|Property|Value|
|---|---|
|ReferencedEntity|`subject`|
|ReferencedAttribute|`subjectid`|
|ReferencingAttribute|`msdyn_subjectid`|
|ReferencingEntityNavigationPropertyName|`msdyn_subjectid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_knowledgearticletemplate"></a> owner_msdyn_knowledgearticletemplate

One-To-Many Relationship: [owner owner_msdyn_knowledgearticletemplate](owner.md#BKMK_owner_msdyn_knowledgearticletemplate)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_knowledgearticletemplate"></a> team_msdyn_knowledgearticletemplate

One-To-Many Relationship: [team team_msdyn_knowledgearticletemplate](team.md#BKMK_team_msdyn_knowledgearticletemplate)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_knowledgearticletemplate"></a> user_msdyn_knowledgearticletemplate

One-To-Many Relationship: [systemuser user_msdyn_knowledgearticletemplate](systemuser.md#BKMK_user_msdyn_knowledgearticletemplate)

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

- [msdyn_knowledgearticletemplate_AsyncOperations](#BKMK_msdyn_knowledgearticletemplate_AsyncOperations)
- [msdyn_knowledgearticletemplate_BulkDeleteFailures](#BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures)
- [msdyn_knowledgearticletemplate_DuplicateBaseRecord](#BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord)
- [msdyn_knowledgearticletemplate_DuplicateMatchingRecord](#BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord)
- [msdyn_knowledgearticletemplate_MailboxTrackingFolders](#BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders)
- [msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgearticletemplate_ProcessSession](#BKMK_msdyn_knowledgearticletemplate_ProcessSession)
- [msdyn_knowledgearticletemplate_QueueItems](#BKMK_msdyn_knowledgearticletemplate_QueueItems)
- [msdyn_knowledgearticletemplate_SharePointDocumentLocations](#BKMK_msdyn_knowledgearticletemplate_SharePointDocumentLocations)
- [msdyn_knowledgearticletemplate_SyncErrors](#BKMK_msdyn_knowledgearticletemplate_SyncErrors)

### <a name="BKMK_msdyn_knowledgearticletemplate_AsyncOperations"></a> msdyn_knowledgearticletemplate_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_knowledgearticletemplate_AsyncOperations](asyncoperation.md#BKMK_msdyn_knowledgearticletemplate_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticletemplate_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures"></a> msdyn_knowledgearticletemplate_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_knowledgearticletemplate_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticletemplate_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord"></a> msdyn_knowledgearticletemplate_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_knowledgearticletemplate_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticletemplate_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord"></a> msdyn_knowledgearticletemplate_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_knowledgearticletemplate_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticletemplate_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders"></a> msdyn_knowledgearticletemplate_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_knowledgearticletemplate_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticletemplate_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticletemplate_ProcessSession"></a> msdyn_knowledgearticletemplate_ProcessSession

Many-To-One Relationship: [processsession msdyn_knowledgearticletemplate_ProcessSession](processsession.md#BKMK_msdyn_knowledgearticletemplate_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticletemplate_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticletemplate_QueueItems"></a> msdyn_knowledgearticletemplate_QueueItems

Many-To-One Relationship: [queueitem msdyn_knowledgearticletemplate_QueueItems](queueitem.md#BKMK_msdyn_knowledgearticletemplate_QueueItems)

|Property|Value|
|---|---|
|ReferencingEntity|`queueitem`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticletemplate_QueueItems`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticletemplate_SharePointDocumentLocations"></a> msdyn_knowledgearticletemplate_SharePointDocumentLocations

Many-To-One Relationship: [sharepointdocumentlocation msdyn_knowledgearticletemplate_SharePointDocumentLocations](sharepointdocumentlocation.md#BKMK_msdyn_knowledgearticletemplate_SharePointDocumentLocations)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointdocumentlocation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticletemplate_SharePointDocumentLocations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgearticletemplate_SyncErrors"></a> msdyn_knowledgearticletemplate_SyncErrors

Many-To-One Relationship: [syncerror msdyn_knowledgearticletemplate_SyncErrors](syncerror.md#BKMK_msdyn_knowledgearticletemplate_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgearticletemplate_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_knowledgearticletemplate?displayProperty=fullName>
