---
title: "Dependency table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Dependency table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Dependency table/entity reference (Microsoft Dataverse)

A component dependency in CRM.

## Messages

The following table lists the messages for the Dependency table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /dependencies(*dependencyid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveDependenciesForDelete`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveDependenciesForDelete?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveDependenciesForDeleteRequest>|
| `RetrieveDependenciesForUninstall`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveDependenciesForUninstall?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveDependenciesForUninstallRequest>|
| `RetrieveDependentComponents`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveDependentComponents?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveDependentComponentsRequest>|
| `RetrieveMissingDependencies`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveMissingDependencies?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveMissingDependenciesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /dependencies<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveRequiredComponents`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveRequiredComponents?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveRequiredComponentsRequest>|

## Properties

The following table lists selected properties for the Dependency table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Dependency** |
| **DisplayCollectionName** | **Dependency** |
| **SchemaName** | `Dependency` |
| **CollectionSchemaName** | `Dependency` |
| **EntitySetName** | `dependencies`|
| **LogicalName** | `dependency` |
| **LogicalCollectionName** | `dependencies` |
| **PrimaryIdAttribute** | `dependencyid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [DependencyId](#BKMK_DependencyId)
- [DependencyType](#BKMK_DependencyType)
- [DependentComponentBaseSolutionId](#BKMK_DependentComponentBaseSolutionId)
- [DependentComponentNodeId](#BKMK_DependentComponentNodeId)
- [DependentComponentObjectId](#BKMK_DependentComponentObjectId)
- [DependentComponentParentId](#BKMK_DependentComponentParentId)
- [DependentComponentType](#BKMK_DependentComponentType)
- [RequiredComponentBaseSolutionId](#BKMK_RequiredComponentBaseSolutionId)
- [RequiredComponentIntroducedVersion](#BKMK_RequiredComponentIntroducedVersion)
- [RequiredComponentNodeId](#BKMK_RequiredComponentNodeId)
- [RequiredComponentObjectId](#BKMK_RequiredComponentObjectId)
- [RequiredComponentParentId](#BKMK_RequiredComponentParentId)
- [RequiredComponentType](#BKMK_RequiredComponentType)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_DependencyId"></a> DependencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of a dependency.**|
|DisplayName|**Dependency Identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependencyid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_DependencyType"></a> DependencyType

|Property|Value|
|---|---|
|Description|**The dependency type of the dependency.**|
|DisplayName|**Dependency Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependencytype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`dependencytype`|

#### DependencyType Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Solution Internal**|
|2|**Published**|
|4|**Unpublished**|

### <a name="BKMK_DependentComponentBaseSolutionId"></a> DependentComponentBaseSolutionId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependentcomponentbasesolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_DependentComponentNodeId"></a> DependentComponentNodeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the dependent component's node.**|
|DisplayName|**Dependent Component**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependentcomponentnodeid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|dependencynode|

### <a name="BKMK_DependentComponentObjectId"></a> DependentComponentObjectId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependentcomponentobjectid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_DependentComponentParentId"></a> DependentComponentParentId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependentcomponentparentid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_DependentComponentType"></a> DependentComponentType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependentcomponenttype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`componenttype`|

#### DependentComponentType Choices/Options

|Value|Label|
|---|---|
|1|**Entity**|
|2|**Attribute**|
|3|**Relationship**|
|4|**Attribute Picklist Value**|
|5|**Attribute Lookup Value**|
|6|**View Attribute**|
|7|**Localized Label**|
|8|**Relationship Extra Condition**|
|9|**Option Set**|
|10|**Entity Relationship**|
|11|**Entity Relationship Role**|
|12|**Entity Relationship Relationships**|
|13|**Managed Property**|
|14|**Entity Key**|
|16|**Privilege**|
|17|**PrivilegeObjectTypeCode**|
|18|**Index**|
|20|**Role**|
|21|**Role Privilege**|
|22|**Display String**|
|23|**Display String Map**|
|24|**Form**|
|25|**Organization**|
|26|**Saved Query**|
|29|**Workflow**|
|31|**Report**|
|32|**Report Entity**|
|33|**Report Category**|
|34|**Report Visibility**|
|35|**Attachment**|
|36|**Email Template**|
|37|**Contract Template**|
|38|**KB Article Template**|
|39|**Mail Merge Template**|
|44|**Duplicate Rule**|
|45|**Duplicate Rule Condition**|
|46|**Entity Map**|
|47|**Attribute Map**|
|48|**Ribbon Command**|
|49|**Ribbon Context Group**|
|50|**Ribbon Customization**|
|52|**Ribbon Rule**|
|53|**Ribbon Tab To Command Map**|
|55|**Ribbon Diff**|
|59|**Saved Query Visualization**|
|60|**System Form**|
|61|**Web Resource**|
|62|**Site Map**|
|63|**Connection Role**|
|64|**Complex Control**|
|65|**Hierarchy Rule**|
|66|**Custom Control**|
|68|**Custom Control Default Config**|
|70|**Field Security Profile**|
|71|**Field Permission**|
|90|**Plugin Type**|
|91|**Plugin Assembly**|
|92|**SDK Message Processing Step**|
|93|**SDK Message Processing Step Image**|
|95|**Service Endpoint**|
|150|**Routing Rule**|
|151|**Routing Rule Item**|
|152|**SLA**|
|153|**SLA Item**|
|154|**Convert Rule**|
|155|**Convert Rule Item**|
|161|**Mobile Offline Profile**|
|162|**Mobile Offline Profile Item**|
|165|**Similarity Rule**|
|166|**Data Source Mapping**|
|201|**SDKMessage**|
|202|**SDKMessageFilter**|
|203|**SdkMessagePair**|
|204|**SdkMessageRequest**|
|205|**SdkMessageRequestField**|
|206|**SdkMessageResponse**|
|207|**SdkMessageResponseField**|
|208|**Import Map**|
|210|**WebWizard**|
|300|**Canvas App**|
|371|**Connector**|
|372|**Connector**|
|380|**Environment Variable Definition**|
|381|**Environment Variable Value**|
|400|**AI Project Type**|
|401|**AI Project**|
|402|**AI Configuration**|
|430|**Entity Analytics Configuration**|
|431|**Attribute Image Configuration**|
|432|**Entity Image Configuration**|

### <a name="BKMK_RequiredComponentBaseSolutionId"></a> RequiredComponentBaseSolutionId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requiredcomponentbasesolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RequiredComponentIntroducedVersion"></a> RequiredComponentIntroducedVersion

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requiredcomponentintroducedversion`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_RequiredComponentNodeId"></a> RequiredComponentNodeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the required component's node**|
|DisplayName|**Required Component**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requiredcomponentnodeid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|dependencynode|

### <a name="BKMK_RequiredComponentObjectId"></a> RequiredComponentObjectId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requiredcomponentobjectid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RequiredComponentParentId"></a> RequiredComponentParentId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requiredcomponentparentid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RequiredComponentType"></a> RequiredComponentType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`requiredcomponenttype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`componenttype`|

#### RequiredComponentType Choices/Options

|Value|Label|
|---|---|
|1|**Entity**|
|2|**Attribute**|
|3|**Relationship**|
|4|**Attribute Picklist Value**|
|5|**Attribute Lookup Value**|
|6|**View Attribute**|
|7|**Localized Label**|
|8|**Relationship Extra Condition**|
|9|**Option Set**|
|10|**Entity Relationship**|
|11|**Entity Relationship Role**|
|12|**Entity Relationship Relationships**|
|13|**Managed Property**|
|14|**Entity Key**|
|16|**Privilege**|
|17|**PrivilegeObjectTypeCode**|
|18|**Index**|
|20|**Role**|
|21|**Role Privilege**|
|22|**Display String**|
|23|**Display String Map**|
|24|**Form**|
|25|**Organization**|
|26|**Saved Query**|
|29|**Workflow**|
|31|**Report**|
|32|**Report Entity**|
|33|**Report Category**|
|34|**Report Visibility**|
|35|**Attachment**|
|36|**Email Template**|
|37|**Contract Template**|
|38|**KB Article Template**|
|39|**Mail Merge Template**|
|44|**Duplicate Rule**|
|45|**Duplicate Rule Condition**|
|46|**Entity Map**|
|47|**Attribute Map**|
|48|**Ribbon Command**|
|49|**Ribbon Context Group**|
|50|**Ribbon Customization**|
|52|**Ribbon Rule**|
|53|**Ribbon Tab To Command Map**|
|55|**Ribbon Diff**|
|59|**Saved Query Visualization**|
|60|**System Form**|
|61|**Web Resource**|
|62|**Site Map**|
|63|**Connection Role**|
|64|**Complex Control**|
|65|**Hierarchy Rule**|
|66|**Custom Control**|
|68|**Custom Control Default Config**|
|70|**Field Security Profile**|
|71|**Field Permission**|
|90|**Plugin Type**|
|91|**Plugin Assembly**|
|92|**SDK Message Processing Step**|
|93|**SDK Message Processing Step Image**|
|95|**Service Endpoint**|
|150|**Routing Rule**|
|151|**Routing Rule Item**|
|152|**SLA**|
|153|**SLA Item**|
|154|**Convert Rule**|
|155|**Convert Rule Item**|
|161|**Mobile Offline Profile**|
|162|**Mobile Offline Profile Item**|
|165|**Similarity Rule**|
|166|**Data Source Mapping**|
|201|**SDKMessage**|
|202|**SDKMessageFilter**|
|203|**SdkMessagePair**|
|204|**SdkMessageRequest**|
|205|**SdkMessageRequestField**|
|206|**SdkMessageResponse**|
|207|**SdkMessageResponseField**|
|208|**Import Map**|
|210|**WebWizard**|
|300|**Canvas App**|
|371|**Connector**|
|372|**Connector**|
|380|**Environment Variable Definition**|
|381|**Environment Variable Value**|
|400|**AI Project Type**|
|401|**AI Project**|
|402|**AI Configuration**|
|430|**Entity Analytics Configuration**|
|431|**Attribute Image Configuration**|
|432|**Entity Image Configuration**|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.dependency?displayProperty=fullName>
