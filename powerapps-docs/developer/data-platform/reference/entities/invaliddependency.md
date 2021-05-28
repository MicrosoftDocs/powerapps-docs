---
title: "InvalidDependency table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the InvalidDependency table/entity."
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

# InvalidDependency table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

An invalid dependency in the CRM system.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/invaliddependencies(*invaliddependencyid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/invaliddependencies<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|InvalidDependencies|
|DisplayCollectionName|Invalid Dependencies|
|DisplayName|Invalid Dependency|
|EntitySetName|invaliddependencies|
|IsBPFEntity|False|
|LogicalCollectionName|invaliddependencies|
|LogicalName|invaliddependency|
|OwnershipType|None|
|PrimaryIdAttribute|invaliddependencyid|
|PrimaryNameAttribute||
|SchemaName|InvalidDependency|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_MissingComponentId"></a> MissingComponentId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the missing component.|
|DisplayName|Regarding|
|IsValidForCreate|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|missingcomponentid|
|RequiredLevel|None|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ExistingComponentId](#BKMK_ExistingComponentId)
- [ExistingComponentType](#BKMK_ExistingComponentType)
- [ExistingDependencyType](#BKMK_ExistingDependencyType)
- [InvalidDependencyId](#BKMK_InvalidDependencyId)
- [IsExistingNodeRequiredComponent](#BKMK_IsExistingNodeRequiredComponent)
- [MissingComponentInfo](#BKMK_MissingComponentInfo)
- [MissingComponentLookupType](#BKMK_MissingComponentLookupType)
- [MissingComponentType](#BKMK_MissingComponentType)


### <a name="BKMK_ExistingComponentId"></a> ExistingComponentId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the object that has an invalid dependency|
|DisplayName|Existing Object Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|existingcomponentid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ExistingComponentType"></a> ExistingComponentType

|Property|Value|
|--------|-----|
|Description|Component type of the object that has an invalid dependency|
|DisplayName|Existing Object's Component Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|existingcomponenttype|
|RequiredLevel|None|
|Type|Picklist|

#### ExistingComponentType Choices/Options

|Value|Label|
|-----|-----|
|1|Entity|
|2|Attribute|
|3|Relationship|
|4|Attribute Picklist Value|
|5|Attribute Lookup Value|
|6|View Attribute|
|7|Localized Label|
|8|Relationship Extra Condition|
|9|Option Set|
|10|Entity Relationship|
|11|Entity Relationship Role|
|12|Entity Relationship Relationships|
|13|Managed Property|
|14|Entity Key|
|16|Privilege|
|17|PrivilegeObjectTypeCode|
|18|Index|
|20|Role|
|21|Role Privilege|
|22|Display String|
|23|Display String Map|
|24|Form|
|25|Organization|
|26|Saved Query|
|29|Workflow|
|31|Report|
|32|Report Entity|
|33|Report Category|
|34|Report Visibility|
|35|Attachment|
|36|Email Template|
|37|Contract Template|
|38|KB Article Template|
|39|Mail Merge Template|
|44|Duplicate Rule|
|45|Duplicate Rule Condition|
|46|Entity Map|
|47|Attribute Map|
|48|Ribbon Command|
|49|Ribbon Context Group|
|50|Ribbon Customization|
|52|Ribbon Rule|
|53|Ribbon Tab To Command Map|
|55|Ribbon Diff|
|59|Saved Query Visualization|
|60|System Form|
|61|Web Resource|
|62|Site Map|
|63|Connection Role|
|64|Complex Control|
|65|Hierarchy Rule|
|66|Custom Control|
|68|Custom Control Default Config|
|70|Field Security Profile|
|71|Field Permission|
|90|Plugin Type|
|91|Plugin Assembly|
|92|SDK Message Processing Step|
|93|SDK Message Processing Step Image|
|95|Service Endpoint|
|150|Routing Rule|
|151|Routing Rule Item|
|152|SLA|
|153|SLA Item|
|154|Convert Rule|
|155|Convert Rule Item|
|161|Mobile Offline Profile|
|162|Mobile Offline Profile Item|
|165|Similarity Rule|
|166|Data Source Mapping|
|201|SDKMessage|
|202|SDKMessageFilter|
|203|SdkMessagePair|
|204|SdkMessageRequest|
|205|SdkMessageRequestField|
|206|SdkMessageResponse|
|207|SdkMessageResponseField|
|208|Import Map|
|210|WebWizard|
|300|Canvas App|
|371|Connector|
|372|Connector|
|380|Environment Variable Definition|
|381|Environment Variable Value|
|400|AI Project Type|
|401|AI Project|
|402|AI Configuration|
|430|Entity Analytics Configuration|
|431|Attribute Image Configuration|
|432|Entity Image Configuration|



### <a name="BKMK_ExistingDependencyType"></a> ExistingDependencyType

|Property|Value|
|--------|-----|
|Description|The dependency type of the invalid dependency.|
|DisplayName|Weight|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|existingdependencytype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ExistingDependencyType Choices/Options

|Value|Label|
|-----|-----|
|0|None|
|1|Solution Internal|
|2|Published|
|4|Unpublished|



### <a name="BKMK_InvalidDependencyId"></a> InvalidDependencyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the invalid dependency.|
|DisplayName|Invalid Dependency Identifier|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|invaliddependencyid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_IsExistingNodeRequiredComponent"></a> IsExistingNodeRequiredComponent

|Property|Value|
|--------|-----|
|Description|Indicates whether the existing node is the required component in the dependency|
|DisplayName|Is this node the required component|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isexistingnoderequiredcomponent|
|RequiredLevel|None|
|Type|Boolean|

#### IsExistingNodeRequiredComponent Choices/Options

|Value|Label|
|-----|-----|
|1|Ancestor|
|0|Descendent|

**DefaultValue**: True



### <a name="BKMK_MissingComponentInfo"></a> MissingComponentInfo

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|missingcomponentinfo|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MissingComponentLookupType"></a> MissingComponentLookupType

|Property|Value|
|--------|-----|
|Description|The lookup type of the missing component.|
|DisplayName|Lookup Type|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|missingcomponentlookuptype|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_MissingComponentType"></a> MissingComponentType

|Property|Value|
|--------|-----|
|Description|The object type code of the missing component.|
|DisplayName|Type Code|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|missingcomponenttype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### MissingComponentType Choices/Options

|Value|Label|
|-----|-----|
|1|Entity|
|2|Attribute|
|3|Relationship|
|4|Attribute Picklist Value|
|5|Attribute Lookup Value|
|6|View Attribute|
|7|Localized Label|
|8|Relationship Extra Condition|
|9|Option Set|
|10|Entity Relationship|
|11|Entity Relationship Role|
|12|Entity Relationship Relationships|
|13|Managed Property|
|14|Entity Key|
|16|Privilege|
|17|PrivilegeObjectTypeCode|
|18|Index|
|20|Role|
|21|Role Privilege|
|22|Display String|
|23|Display String Map|
|24|Form|
|25|Organization|
|26|Saved Query|
|29|Workflow|
|31|Report|
|32|Report Entity|
|33|Report Category|
|34|Report Visibility|
|35|Attachment|
|36|Email Template|
|37|Contract Template|
|38|KB Article Template|
|39|Mail Merge Template|
|44|Duplicate Rule|
|45|Duplicate Rule Condition|
|46|Entity Map|
|47|Attribute Map|
|48|Ribbon Command|
|49|Ribbon Context Group|
|50|Ribbon Customization|
|52|Ribbon Rule|
|53|Ribbon Tab To Command Map|
|55|Ribbon Diff|
|59|Saved Query Visualization|
|60|System Form|
|61|Web Resource|
|62|Site Map|
|63|Connection Role|
|64|Complex Control|
|65|Hierarchy Rule|
|66|Custom Control|
|68|Custom Control Default Config|
|70|Field Security Profile|
|71|Field Permission|
|90|Plugin Type|
|91|Plugin Assembly|
|92|SDK Message Processing Step|
|93|SDK Message Processing Step Image|
|95|Service Endpoint|
|150|Routing Rule|
|151|Routing Rule Item|
|152|SLA|
|153|SLA Item|
|154|Convert Rule|
|155|Convert Rule Item|
|161|Mobile Offline Profile|
|162|Mobile Offline Profile Item|
|165|Similarity Rule|
|166|Data Source Mapping|
|201|SDKMessage|
|202|SDKMessageFilter|
|203|SdkMessagePair|
|204|SdkMessageRequest|
|205|SdkMessageRequestField|
|206|SdkMessageResponse|
|207|SdkMessageResponseField|
|208|Import Map|
|210|WebWizard|
|300|Canvas App|
|371|Connector|
|372|Connector|
|380|Environment Variable Definition|
|381|Environment Variable Value|
|400|AI Project Type|
|401|AI Project|
|402|AI Configuration|
|430|Entity Analytics Configuration|
|431|Attribute Image Configuration|
|432|Entity Image Configuration|




### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.invaliddependency?text=invaliddependency EntityType" />