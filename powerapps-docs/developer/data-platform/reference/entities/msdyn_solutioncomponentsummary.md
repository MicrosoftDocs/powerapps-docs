---
title: "Solution Component Summary (msdyn_solutioncomponentsummary) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Solution Component Summary (msdyn_solutioncomponentsummary) table/entity with Microsoft Dataverse."
ms.date: 08/30/2024
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Solution Component Summary (msdyn_solutioncomponentsummary) table/entity reference



## Messages

The following table lists the messages for the Solution Component Summary (msdyn_solutioncomponentsummary) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /msdyn_solutioncomponentsummaries<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /msdyn_solutioncomponentsummaries(*msdyn_solutioncomponentsummaryid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: False |`GET` /msdyn_solutioncomponentsummaries(*msdyn_solutioncomponentsummaryid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /msdyn_solutioncomponentsummaries<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /msdyn_solutioncomponentsummaries(*msdyn_solutioncomponentsummaryid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /msdyn_solutioncomponentsummaries(*msdyn_solutioncomponentsummaryid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Solution Component Summary (msdyn_solutioncomponentsummary) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Solution Component Summary** |
| **DisplayCollectionName** | **Solution Component Summaries** |
| **SchemaName** | `msdyn_solutioncomponentsummary` |
| **CollectionSchemaName** | `msdyn_solutioncomponentsummaries` |
| **EntitySetName** | `msdyn_solutioncomponentsummaries`|
| **LogicalName** | `msdyn_solutioncomponentsummary` |
| **LogicalCollectionName** | `msdyn_solutioncomponentsummaries` |
| **PrimaryIdAttribute** | `msdyn_solutioncomponentsummaryid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_canvasappuniqueid](#BKMK_msdyn_canvasappuniqueid)
- [msdyn_componentlogicalname](#BKMK_msdyn_componentlogicalname)
- [msdyn_componenttype](#BKMK_msdyn_componenttype)
- [msdyn_componenttypename](#BKMK_msdyn_componenttypename)
- [msdyn_connectorinternalid](#BKMK_msdyn_connectorinternalid)
- [msdyn_createdon](#BKMK_msdyn_createdon)
- [msdyn_culture](#BKMK_msdyn_culture)
- [msdyn_deployment](#BKMK_msdyn_deployment)
- [msdyn_description](#BKMK_msdyn_description)
- [msdyn_displayname](#BKMK_msdyn_displayname)
- [msdyn_eventhandler](#BKMK_msdyn_eventhandler)
- [msdyn_executionorder](#BKMK_msdyn_executionorder)
- [msdyn_executionstage](#BKMK_msdyn_executionstage)
- [msdyn_fieldsecurity](#BKMK_msdyn_fieldsecurity)
- [msdyn_fieldtype](#BKMK_msdyn_fieldtype)
- [msdyn_hasactivecustomization](#BKMK_msdyn_hasactivecustomization)
- [msdyn_isappaware](#BKMK_msdyn_isappaware)
- [msdyn_isappawarename](#BKMK_msdyn_isappawarename)
- [msdyn_isauditenabled](#BKMK_msdyn_isauditenabled)
- [msdyn_isauditenabledname](#BKMK_msdyn_isauditenabledname)
- [msdyn_iscustom](#BKMK_msdyn_iscustom)
- [msdyn_iscustomizable](#BKMK_msdyn_iscustomizable)
- [msdyn_iscustomizablename](#BKMK_msdyn_iscustomizablename)
- [msdyn_iscustomname](#BKMK_msdyn_iscustomname)
- [msdyn_isdefault](#BKMK_msdyn_isdefault)
- [msdyn_isdefaultname](#BKMK_msdyn_isdefaultname)
- [msdyn_ismanaged](#BKMK_msdyn_ismanaged)
- [msdyn_ismanagedname](#BKMK_msdyn_ismanagedname)
- [msdyn_isolationmode](#BKMK_msdyn_isolationmode)
- [msdyn_istableenabled](#BKMK_msdyn_istableenabled)
- [msdyn_lcid](#BKMK_msdyn_lcid)
- [msdyn_logicalcollectionname](#BKMK_msdyn_logicalcollectionname)
- [msdyn_modifiedon](#BKMK_msdyn_modifiedon)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_objectid](#BKMK_msdyn_objectid)
- [msdyn_objecttypecode](#BKMK_msdyn_objecttypecode)
- [msdyn_owner](#BKMK_msdyn_owner)
- [msdyn_owningbusinessunit](#BKMK_msdyn_owningbusinessunit)
- [msdyn_primaryentityname](#BKMK_msdyn_primaryentityname)
- [msdyn_primaryidattribute](#BKMK_msdyn_primaryidattribute)
- [msdyn_publickeytoken](#BKMK_msdyn_publickeytoken)
- [msdyn_relatedentity](#BKMK_msdyn_relatedentity)
- [msdyn_relatedentityattribute](#BKMK_msdyn_relatedentityattribute)
- [msdyn_schemaname](#BKMK_msdyn_schemaname)
- [msdyn_sdkmessagename](#BKMK_msdyn_sdkmessagename)
- [msdyn_solutioncomponentsummaryId](#BKMK_msdyn_solutioncomponentsummaryId)
- [msdyn_solutionid](#BKMK_msdyn_solutionid)
- [msdyn_standardstatus](#BKMK_msdyn_standardstatus)
- [msdyn_status](#BKMK_msdyn_status)
- [msdyn_statusname](#BKMK_msdyn_statusname)
- [msdyn_subtype](#BKMK_msdyn_subtype)
- [msdyn_synctoexternalsearchindex](#BKMK_msdyn_synctoexternalsearchindex)
- [msdyn_total](#BKMK_msdyn_total)
- [msdyn_typename](#BKMK_msdyn_typename)
- [msdyn_uniquename](#BKMK_msdyn_uniquename)
- [msdyn_version](#BKMK_msdyn_version)
- [msdyn_workflowcategory](#BKMK_msdyn_workflowcategory)
- [msdyn_workflowcategoryname](#BKMK_msdyn_workflowcategoryname)
- [msdyn_workflowidunique](#BKMK_msdyn_workflowidunique)

### <a name="BKMK_msdyn_canvasappuniqueid"></a> msdyn_canvasappuniqueid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Canvas App Unique Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_canvasappuniqueid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_componentlogicalname"></a> msdyn_componentlogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Component Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componentlogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_componenttype"></a> msdyn_componenttype

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_componenttype**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componenttype`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_componenttypename"></a> msdyn_componenttypename

|Property|Value|
|---|---|
|Description||
|DisplayName|**Component Type Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componenttypename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_connectorinternalid"></a> msdyn_connectorinternalid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Connector Internal Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_connectorinternalid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_createdon"></a> msdyn_createdon

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_createdon**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_createdon`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_culture"></a> msdyn_culture

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_culture**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_culture`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_deployment"></a> msdyn_deployment

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_deployment**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_deployment`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_description"></a> msdyn_description

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_displayname"></a> msdyn_displayname

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_displayname**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_displayname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_eventhandler"></a> msdyn_eventhandler

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_eventhandler**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_eventhandler`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_executionorder"></a> msdyn_executionorder

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_executionorder**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_executionorder`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_executionstage"></a> msdyn_executionstage

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_executionstage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_executionstage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_fieldsecurity"></a> msdyn_fieldsecurity

|Property|Value|
|---|---|
|Description||
|DisplayName|**Field Security**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_fieldsecurity`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_fieldtype"></a> msdyn_fieldtype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Field Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_fieldtype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_hasactivecustomization"></a> msdyn_hasactivecustomization

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_hasactivecustomization**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_hasactivecustomization`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_isappaware"></a> msdyn_isappaware

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_isappaware**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isappaware`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_isappawarename"></a> msdyn_isappawarename

|Property|Value|
|---|---|
|Description||
|DisplayName|**App Aware Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isappawarename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_isauditenabled"></a> msdyn_isauditenabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_isauditenabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isauditenabled`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_isauditenabledname"></a> msdyn_isauditenabledname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Audit Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isauditenabledname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_iscustom"></a> msdyn_iscustom

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_iscustom**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_iscustom`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_iscustomizable"></a> msdyn_iscustomizable

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_iscustomizable**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_iscustomizable`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_iscustomizablename"></a> msdyn_iscustomizablename

|Property|Value|
|---|---|
|Description||
|DisplayName|**Customizable Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_iscustomizablename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_iscustomname"></a> msdyn_iscustomname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is Custom Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_iscustomname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_isdefault"></a> msdyn_isdefault

|Property|Value|
|---|---|
|Description||
|DisplayName|**Default**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isdefault`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_isdefaultname"></a> msdyn_isdefaultname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Default Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isdefaultname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_ismanaged"></a> msdyn_ismanaged

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_ismanaged**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_ismanaged`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_ismanagedname"></a> msdyn_ismanagedname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Managed Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_ismanagedname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_isolationmode"></a> msdyn_isolationmode

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_isolationmode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isolationmode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_istableenabled"></a> msdyn_istableenabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_istableenabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_istableenabled`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_lcid"></a> msdyn_lcid

|Property|Value|
|---|---|
|Description|**Language code for component**|
|DisplayName|**msdyn_lcid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lcid`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_logicalcollectionname"></a> msdyn_logicalcollectionname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Logical Collection Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_logicalcollectionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_modifiedon"></a> msdyn_modifiedon

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_modifiedon**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_modifiedon`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**msdyn_name**|
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

### <a name="BKMK_msdyn_objectid"></a> msdyn_objectid

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_objectid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_objectid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_objecttypecode"></a> msdyn_objecttypecode

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_objecttypecode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_objecttypecode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_owner"></a> msdyn_owner

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_owner`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_owningbusinessunit"></a> msdyn_owningbusinessunit

|Property|Value|
|---|---|
|Description||
|DisplayName|**owning business unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_owningbusinessunit`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_primaryentityname"></a> msdyn_primaryentityname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Primary Entity Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_primaryentityname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_primaryidattribute"></a> msdyn_primaryidattribute

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name of the primary id attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_primaryidattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_publickeytoken"></a> msdyn_publickeytoken

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_publickeytoken**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_publickeytoken`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_relatedentity"></a> msdyn_relatedentity

|Property|Value|
|---|---|
|Description||
|DisplayName|**Related Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_relatedentity`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_relatedentityattribute"></a> msdyn_relatedentityattribute

|Property|Value|
|---|---|
|Description||
|DisplayName|**Related Entity Attribute Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_relatedentityattribute`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_schemaname"></a> msdyn_schemaname

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_schemaname**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_schemaname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_sdkmessagename"></a> msdyn_sdkmessagename

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_sdkmessagename**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_sdkmessagename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_solutioncomponentsummaryId"></a> msdyn_solutioncomponentsummaryId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**SolutionComponentSummary**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_solutioncomponentsummaryid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_solutionid"></a> msdyn_solutionid

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_solutionid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_solutionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_standardstatus"></a> msdyn_standardstatus

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_standardstatus**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_standardstatus`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_status"></a> msdyn_status

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_status`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_statusname"></a> msdyn_statusname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Status Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_statusname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_subtype"></a> msdyn_subtype

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_subtype**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_subtype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_synctoexternalsearchindex"></a> msdyn_synctoexternalsearchindex

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_synctoexternalsearchindex**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_synctoexternalsearchindex`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_total"></a> msdyn_total

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_total**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_total`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Auto|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_typename"></a> msdyn_typename

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_typename**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_typename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_uniquename"></a> msdyn_uniquename

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_uniquename**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_uniquename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_version"></a> msdyn_version

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_version`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_workflowcategory"></a> msdyn_workflowcategory

|Property|Value|
|---|---|
|Description||
|DisplayName|**msdyn_workflowcategory**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_workflowcategory`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_workflowcategoryname"></a> msdyn_workflowcategoryname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Workflow Category Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_workflowcategoryname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_workflowidunique"></a> msdyn_workflowidunique

|Property|Value|
|---|---|
|Description||
|DisplayName|**Workflow Id Unique**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_workflowidunique`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|


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



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_solutioncomponentsummary?displayProperty=fullName>
