---
title: "msdyn_solutionhistory table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_solutionhistory table/entity."
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

# msdyn_solutionhistory table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Microsoft Dynamics 365 Solution History APIs Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_solutionhistories<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_solutionhistories(*msdyn_solutionhistoryid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_solutionhistories(*msdyn_solutionhistoryid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_solutionhistories<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_solutionhistories(*msdyn_solutionhistoryid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_solutionhistories|
|DisplayCollectionName|Solutions History|
|DisplayName|Solution History|
|EntitySetName|msdyn_solutionhistories|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_solutionhistories|
|LogicalName|msdyn_solutionhistory|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|msdyn_solutionhistoryid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_solutionhistory|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_activityid](#BKMK_msdyn_activityid)
- [msdyn_correlationid](#BKMK_msdyn_correlationid)
- [msdyn_endtime](#BKMK_msdyn_endtime)
- [msdyn_errorcode](#BKMK_msdyn_errorcode)
- [msdyn_exceptionmessage](#BKMK_msdyn_exceptionmessage)
- [msdyn_exceptionstack](#BKMK_msdyn_exceptionstack)
- [msdyn_ismanaged](#BKMK_msdyn_ismanaged)
- [msdyn_isoverwritecustomizations](#BKMK_msdyn_isoverwritecustomizations)
- [msdyn_ispatch](#BKMK_msdyn_ispatch)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_operation](#BKMK_msdyn_operation)
- [msdyn_packagename](#BKMK_msdyn_packagename)
- [msdyn_packageversion](#BKMK_msdyn_packageversion)
- [msdyn_publisherid](#BKMK_msdyn_publisherid)
- [msdyn_publishername](#BKMK_msdyn_publishername)
- [msdyn_result](#BKMK_msdyn_result)
- [msdyn_solutionhistoryId](#BKMK_msdyn_solutionhistoryId)
- [msdyn_solutionid](#BKMK_msdyn_solutionid)
- [msdyn_solutionversion](#BKMK_msdyn_solutionversion)
- [msdyn_starttime](#BKMK_msdyn_starttime)
- [msdyn_status](#BKMK_msdyn_status)
- [msdyn_suboperation](#BKMK_msdyn_suboperation)
- [msdyn_totaltime](#BKMK_msdyn_totaltime)


### <a name="BKMK_msdyn_activityid"></a> msdyn_activityid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Activity Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_activityid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_correlationid"></a> msdyn_correlationid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Correlation Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_correlationid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_endtime"></a> msdyn_endtime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|End Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_endtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_msdyn_errorcode"></a> msdyn_errorcode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Error Code|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_errorcode|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_exceptionmessage"></a> msdyn_exceptionmessage

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Exception Message|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_exceptionmessage|
|MaxLength|10000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_exceptionstack"></a> msdyn_exceptionstack

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Exception Stack|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_exceptionstack|
|MaxLength|10000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_ismanaged"></a> msdyn_ismanaged

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Managed|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_ismanaged|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_ismanaged Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_msdyn_isoverwritecustomizations"></a> msdyn_isoverwritecustomizations

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Overwrite Customizations|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isoverwritecustomizations|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isoverwritecustomizations Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_msdyn_ispatch"></a> msdyn_ispatch

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Patch|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_ispatch|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_ispatch Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Solution Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_operation"></a> msdyn_operation

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Operation|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_operation|
|RequiredLevel|None|
|Type|Picklist|

#### msdyn_operation Choices/Options

|Value|Label|
|-----|-----|
|0|Import|
|1|Uninstall|
|2|Export|
|3|Publish|
|4|PublishAll|
|5|LanguageProvision|
|6|ImportTranslation|
|7|RibbonMetadataGeneration|
|8|WorkflowSetState|
|9|None|



### <a name="BKMK_msdyn_packagename"></a> msdyn_packagename

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Package Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_packagename|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_packageversion"></a> msdyn_packageversion

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Package Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_packageversion|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_publisherid"></a> msdyn_publisherid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Publisher Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_publisherid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_publishername"></a> msdyn_publishername

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Publisher Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_publishername|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_result"></a> msdyn_result

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Result|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_result|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_result Choices/Options

|Value|Label|
|-----|-----|
|1|Success|
|0|Failure|

**DefaultValue**: False



### <a name="BKMK_msdyn_solutionhistoryId"></a> msdyn_solutionhistoryId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Solutionhistory|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_solutionhistoryid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_solutionid"></a> msdyn_solutionid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Solution Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_solutionid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_solutionversion"></a> msdyn_solutionversion

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Solution Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_solutionversion|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_starttime"></a> msdyn_starttime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|Start Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_starttime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_msdyn_status"></a> msdyn_status

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_status|
|RequiredLevel|None|
|Type|Picklist|

#### msdyn_status Choices/Options

|Value|Label|
|-----|-----|
|0|Started|
|1|Completed|



### <a name="BKMK_msdyn_suboperation"></a> msdyn_suboperation

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Suboperation|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_suboperation|
|RequiredLevel|None|
|Type|Picklist|

#### msdyn_suboperation Choices/Options

|Value|Label|
|-----|-----|
|0|None|
|1|New|
|2|Upgrade|
|3|Update|
|4|Delete|



### <a name="BKMK_msdyn_totaltime"></a> msdyn_totaltime

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Total Time (seconds)|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_totaltime|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_solutionhistory?text=msdyn_solutionhistory EntityType" />