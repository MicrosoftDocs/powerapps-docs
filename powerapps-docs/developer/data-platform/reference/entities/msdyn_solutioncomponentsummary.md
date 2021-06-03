---
title: "msdyn_solutioncomponentsummary table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_solutioncomponentsummary table/entity."
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

# msdyn_solutioncomponentsummary table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Microsoft Dynamics 365 Settings APIs Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_solutioncomponentsummaries<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_solutioncomponentsummaries(*msdyn_solutioncomponentsummaryid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_solutioncomponentsummaries(*msdyn_solutioncomponentsummaryid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_solutioncomponentsummaries<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_solutioncomponentsummaries(*msdyn_solutioncomponentsummaryid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_solutioncomponentsummaries|
|DisplayCollectionName|Solution Component Summaries|
|DisplayName|Solution Component Summary|
|EntitySetName|msdyn_solutioncomponentsummaries|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_solutioncomponentsummaries|
|LogicalName|msdyn_solutioncomponentsummary|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|msdyn_solutioncomponentsummaryid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_solutioncomponentsummary|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description||
|DisplayName|Canvas App Unique Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_canvasappuniqueid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_componentlogicalname"></a> msdyn_componentlogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Component Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_componentlogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_componenttype"></a> msdyn_componenttype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_componenttype|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_componenttype|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_msdyn_componenttypename"></a> msdyn_componenttypename

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Component Type Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_componenttypename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_connectorinternalid"></a> msdyn_connectorinternalid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Connector Internal Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_connectorinternalid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_createdon"></a> msdyn_createdon

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_createdon|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_createdon|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_culture"></a> msdyn_culture

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_culture|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_culture|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_deployment"></a> msdyn_deployment

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_deployment|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_deployment|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_description"></a> msdyn_description

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_description|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_description|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_displayname"></a> msdyn_displayname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_displayname|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_displayname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_eventhandler"></a> msdyn_eventhandler

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_eventhandler|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_eventhandler|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_executionorder"></a> msdyn_executionorder

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_executionorder|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_executionorder|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_executionstage"></a> msdyn_executionstage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_executionstage|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_executionstage|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_fieldsecurity"></a> msdyn_fieldsecurity

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Field Security|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_fieldsecurity|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_fieldtype"></a> msdyn_fieldtype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Field Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_fieldtype|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_isappaware"></a> msdyn_isappaware

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_isappaware|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isappaware|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_isappawarename"></a> msdyn_isappawarename

|Property|Value|
|--------|-----|
|Description||
|DisplayName|App Aware Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isappawarename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_isauditenabled"></a> msdyn_isauditenabled

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_isauditenabled|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isauditenabled|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_isauditenabledname"></a> msdyn_isauditenabledname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Audit Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isauditenabledname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_iscustom"></a> msdyn_iscustom

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_iscustom|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_iscustom|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_iscustomizable"></a> msdyn_iscustomizable

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_iscustomizable|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_iscustomizable|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_iscustomizablename"></a> msdyn_iscustomizablename

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Customizable Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_iscustomizablename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_iscustomname"></a> msdyn_iscustomname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Is Custom Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_iscustomname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_isdefault"></a> msdyn_isdefault

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Default|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isdefault|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_isdefaultname"></a> msdyn_isdefaultname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Default Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isdefaultname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_ismanaged"></a> msdyn_ismanaged

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_ismanaged|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_ismanaged|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_ismanagedname"></a> msdyn_ismanagedname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Managed Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_ismanagedname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_isolationmode"></a> msdyn_isolationmode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_isolationmode|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isolationmode|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_istableenabled"></a> msdyn_istableenabled

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_istableenabled|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_istableenabled|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_logicalcollectionname"></a> msdyn_logicalcollectionname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Logical Collection Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_logicalcollectionname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_modifiedon"></a> msdyn_modifiedon

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_modifiedon|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_modifiedon|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|msdyn_name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_objectid"></a> msdyn_objectid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_objectid|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_objectid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_objecttypecode"></a> msdyn_objecttypecode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_objecttypecode|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_objecttypecode|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_owner"></a> msdyn_owner

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_owner|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_owner|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_owningbusinessunit"></a> msdyn_owningbusinessunit

|Property|Value|
|--------|-----|
|Description||
|DisplayName|owning business unit|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_owningbusinessunit|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_primaryentityname"></a> msdyn_primaryentityname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Primary Entity Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_primaryentityname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_primaryidattribute"></a> msdyn_primaryidattribute

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Name of the primary id attribute|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_primaryidattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_publickeytoken"></a> msdyn_publickeytoken

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_publickeytoken|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_publickeytoken|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_relatedentity"></a> msdyn_relatedentity

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Related Entity|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_relatedentity|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_relatedentityattribute"></a> msdyn_relatedentityattribute

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Related Entity Attribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_relatedentityattribute|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_schemaname"></a> msdyn_schemaname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_schemaname|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_schemaname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_sdkmessagename"></a> msdyn_sdkmessagename

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_sdkmessagename|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_sdkmessagename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_solutioncomponentsummaryId"></a> msdyn_solutioncomponentsummaryId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|SolutionComponentSummary|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_solutioncomponentsummaryid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_solutionid"></a> msdyn_solutionid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_solutionid|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_solutionid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_status"></a> msdyn_status

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_status|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_status|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_statusname"></a> msdyn_statusname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Status Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_statusname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_subtype"></a> msdyn_subtype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_subtype|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_subtype|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_synctoexternalsearchindex"></a> msdyn_synctoexternalsearchindex

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_synctoexternalsearchindex|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_synctoexternalsearchindex|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_total"></a> msdyn_total

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_total|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_total|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_msdyn_typename"></a> msdyn_typename

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_typename|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_typename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_uniquename"></a> msdyn_uniquename

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_uniquename|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_uniquename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_version"></a> msdyn_version

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_version|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_workflowcategory"></a> msdyn_workflowcategory

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_workflowcategory|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_workflowcategory|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_workflowcategoryname"></a> msdyn_workflowcategoryname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Workflow Category Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_workflowcategoryname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_workflowidunique"></a> msdyn_workflowidunique

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Workflow Id Unique|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_workflowidunique|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.


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



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_solutioncomponentsummary?text=msdyn_solutioncomponentsummary EntityType" />