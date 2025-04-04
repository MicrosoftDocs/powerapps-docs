---
title: "Component Layer (msdyn_componentlayer) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Component Layer (msdyn_componentlayer) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Component Layer (msdyn_componentlayer) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Component Layer (msdyn_componentlayer) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /msdyn_componentlayers<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /msdyn_componentlayers(*msdyn_componentlayerid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: True |`GET` /msdyn_componentlayers(*msdyn_componentlayerid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_componentlayers<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /msdyn_componentlayers(*msdyn_componentlayerid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /msdyn_componentlayers(*msdyn_componentlayerid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Component Layer (msdyn_componentlayer) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Component Layer** |
| **DisplayCollectionName** | **Component Layers** |
| **SchemaName** | `msdyn_componentlayer` |
| **CollectionSchemaName** | `msdyn_componentlayers` |
| **EntitySetName** | `msdyn_componentlayers`|
| **LogicalName** | `msdyn_componentlayer` |
| **LogicalCollectionName** | `msdyn_componentlayers` |
| **PrimaryIdAttribute** | `msdyn_componentlayerid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_changes](#BKMK_msdyn_changes)
- [msdyn_children](#BKMK_msdyn_children)
- [msdyn_componentid](#BKMK_msdyn_componentid)
- [msdyn_componentjson](#BKMK_msdyn_componentjson)
- [msdyn_componentlayerId](#BKMK_msdyn_componentlayerId)
- [msdyn_endtime](#BKMK_msdyn_endtime)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_order](#BKMK_msdyn_order)
- [msdyn_publishername](#BKMK_msdyn_publishername)
- [msdyn_solutioncomponentname](#BKMK_msdyn_solutioncomponentname)
- [msdyn_solutionname](#BKMK_msdyn_solutionname)

### <a name="BKMK_msdyn_changes"></a> msdyn_changes

|Property|Value|
|---|---|
|Description||
|DisplayName|**Changes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_changes`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_msdyn_children"></a> msdyn_children

|Property|Value|
|---|---|
|Description||
|DisplayName|**Children**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_children`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_componentid"></a> msdyn_componentid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Component Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componentid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_componentjson"></a> msdyn_componentjson

|Property|Value|
|---|---|
|Description||
|DisplayName|**Component Json**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componentjson`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_msdyn_componentlayerId"></a> msdyn_componentlayerId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Component Layer**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_componentlayerid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_endtime"></a> msdyn_endtime

|Property|Value|
|---|---|
|Description||
|DisplayName|**Overwrite Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_overwritetime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**The name of the component.**|
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
|MaxLength|100|

### <a name="BKMK_msdyn_order"></a> msdyn_order

|Property|Value|
|---|---|
|Description||
|DisplayName|**Order**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_order`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|500|
|MinValue|0|

### <a name="BKMK_msdyn_publishername"></a> msdyn_publishername

|Property|Value|
|---|---|
|Description||
|DisplayName|**Publisher Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_publishername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_solutioncomponentname"></a> msdyn_solutioncomponentname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Solution Component Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_solutioncomponentname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_solutionname"></a> msdyn_solutionname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Solution Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_solutionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_componentlayer?displayProperty=fullName>
