---
title: "Sensitivity Label (sensitivitylabel) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Sensitivity Label (sensitivitylabel) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Sensitivity Label (sensitivitylabel) table/entity reference (Microsoft Dataverse)

Virtual entity that represents Sensitivity Labels

## Messages

The following table lists the messages for the Sensitivity Label (sensitivitylabel) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /sensitivitylabels<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /sensitivitylabels(*sensitivitylabelid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /sensitivitylabels(*sensitivitylabelid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /sensitivitylabels<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /sensitivitylabels(*sensitivitylabelid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /sensitivitylabels(*sensitivitylabelid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Sensitivity Label (sensitivitylabel) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Sensitivity Label** |
| **DisplayCollectionName** | **Sensitivity Labels** |
| **SchemaName** | `sensitivitylabel` |
| **CollectionSchemaName** | `sensitivitylabels` |
| **EntitySetName** | `sensitivitylabels`|
| **LogicalName** | `sensitivitylabel` |
| **LogicalCollectionName** | `sensitivitylabels` |
| **PrimaryIdAttribute** | `sensitivitylabelid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ApplicableTo](#BKMK_ApplicableTo)
- [Color](#BKMK_Color)
- [Description](#BKMK_Description)
- [DisplayName](#BKMK_DisplayName)
- [IsDefault](#BKMK_IsDefault)
- [IsEnabled](#BKMK_IsEnabled)
- [LabelActions](#BKMK_LabelActions)
- [Name](#BKMK_Name)
- [ParentSensitivityLabelId](#BKMK_ParentSensitivityLabelId)
- [Priority](#BKMK_Priority)
- [sensitivitylabelId](#BKMK_sensitivitylabelId)
- [Tooltip](#BKMK_Tooltip)

### <a name="BKMK_ApplicableTo"></a> ApplicableTo

|Property|Value|
|---|---|
|Description|**The formats that the sensitivity label is applicable to.**|
|DisplayName|**Applicable To**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicableto`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_Color"></a> Color

|Property|Value|
|---|---|
|Description|**The color of the sensitivity label.**|
|DisplayName|**Color**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`color`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**The description of the sensitivity label.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|---|---|
|Description|**The display name of the sensitivity label.**|
|DisplayName|**DisplayName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`displayname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|---|---|
|Description|**Indicates if the sensitivity label is the default.**|
|DisplayName|**Is Default**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdefault`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_sensitivitylabel_isdefault`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_IsEnabled"></a> IsEnabled

|Property|Value|
|---|---|
|Description|**Indicates if the sensitivity label is enabled.**|
|DisplayName|**Is Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_sensitivitylabel_isenabled`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_LabelActions"></a> LabelActions

|Property|Value|
|---|---|
|Description|**The label actions of the sensitivity label.**|
|DisplayName|**Label Actions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`labelactions`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the sensitivity label.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ParentSensitivityLabelId"></a> ParentSensitivityLabelId

|Property|Value|
|---|---|
|Description|**Unique identifier of a parent sensitivity label.**|
|DisplayName|**Parent Sensitivity Label Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentsensitivitylabelid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Priority"></a> Priority

|Property|Value|
|---|---|
|Description|**The priority of the sensitivity label.**|
|DisplayName|**Priority**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`priority`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_sensitivitylabelId"></a> sensitivitylabelId

|Property|Value|
|---|---|
|Description|**Unique identifier of a Sensitivity Label.**|
|DisplayName|**Sensitivity Label Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sensitivitylabelid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Tooltip"></a> Tooltip

|Property|Value|
|---|---|
|Description|**The tooltip of the sensitivity label.**|
|DisplayName|**Tooltip**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tooltip`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_sensitivitylabel_email_SensitivityLabelId"></a> sensitivitylabel_email_SensitivityLabelId

Many-To-One Relationship: [email sensitivitylabel_email_SensitivityLabelId](email.md#BKMK_sensitivitylabel_email_SensitivityLabelId)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`sensitivitylabelid`|
|ReferencedEntityNavigationPropertyName|`sensitivitylabel_email_SensitivityLabelId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sensitivitylabel?displayProperty=fullName>
