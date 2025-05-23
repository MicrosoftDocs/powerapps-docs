---
title: "Solution Component (SolutionComponent) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Solution Component (SolutionComponent) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Solution Component (SolutionComponent) table/entity reference (Microsoft Dataverse)

A component of a CRM solution.

## Messages

The following table lists the messages for the Solution Component (SolutionComponent) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `AddSolutionComponent`<br />Event: False |<xref:Microsoft.Dynamics.CRM.AddSolutionComponent?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.AddSolutionComponentRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsComponentCustomizable`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsComponentCustomizable?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsComponentCustomizableRequest>|
| `RemoveSolutionComponent`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RemoveSolutionComponent?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RemoveSolutionComponentRequest>|
| `Retrieve`<br />Event: False |`GET` /solutioncomponents(*solutioncomponentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /solutioncomponents<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `UpdateSolutionComponent`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateSolutionComponent?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.UpdateSolutionComponentRequest>|

## Properties

The following table lists selected properties for the Solution Component (SolutionComponent) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Solution Component** |
| **DisplayCollectionName** | **Solution Components** |
| **SchemaName** | `SolutionComponent` |
| **CollectionSchemaName** | `SolutionComponents` |
| **EntitySetName** | `solutioncomponents`|
| **LogicalName** | `solutioncomponent` |
| **LogicalCollectionName** | `solutioncomponentss` |
| **PrimaryIdAttribute** | `solutioncomponentid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentType](#BKMK_ComponentType)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsMetadata](#BKMK_IsMetadata)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ObjectId](#BKMK_ObjectId)
- [RootComponentBehavior](#BKMK_RootComponentBehavior)
- [RootSolutionComponentId](#BKMK_RootSolutionComponentId)
- [SolutionComponentId](#BKMK_SolutionComponentId)
- [SolutionId](#BKMK_SolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentType"></a> ComponentType

|Property|Value|
|---|---|
|Description|**The object type code of the component.**|
|DisplayName|**Object Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componenttype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`componenttype`|

#### ComponentType Choices/Options

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

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the solution**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the solution was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who created the solution.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IsMetadata"></a> IsMetadata

|Property|Value|
|---|---|
|Description|**Indicates whether this component is metadata or data.**|
|DisplayName|**Is this component metadata**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismetadata`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponent_ismetadata`|
|DefaultValue|True|
|True Label|Metadata|
|False Label|Data|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the solution.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the solution was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who modified the solution.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the object with which the component is associated.**|
|DisplayName|**Regarding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RootComponentBehavior"></a> RootComponentBehavior

|Property|Value|
|---|---|
|Description|**Indicates the include behavior of the root component.**|
|DisplayName|**Root Component Behavior**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rootcomponentbehavior`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`solutioncomponent_rootcomponentbehavior`|

#### RootComponentBehavior Choices/Options

|Value|Label|
|---|---|
|0|**Include Subcomponents**|
|1|**Do not include subcomponents**|
|2|**Include As Shell Only**|

### <a name="BKMK_RootSolutionComponentId"></a> RootSolutionComponentId

|Property|Value|
|---|---|
|Description|**The parent ID of the subcomponent, which will be a root**|
|DisplayName|**Root Solution Component ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rootsolutioncomponentid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionComponentId"></a> SolutionComponentId

|Property|Value|
|---|---|
|Description|**Unique identifier of the solution component.**|
|DisplayName|**Solution Component Identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutioncomponentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the solution.**|
|DisplayName|**Solution**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|solution|

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

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_solutioncomponentbase_createdonbehalfby](#BKMK_lk_solutioncomponentbase_createdonbehalfby)
- [lk_solutioncomponentbase_modifiedonbehalfby](#BKMK_lk_solutioncomponentbase_modifiedonbehalfby)
- [solution_solutioncomponent](#BKMK_solution_solutioncomponent)
- [solutioncomponent_parent_solutioncomponent](#BKMK_solutioncomponent_parent_solutioncomponent-many-to-one)

### <a name="BKMK_lk_solutioncomponentbase_createdonbehalfby"></a> lk_solutioncomponentbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_solutioncomponentbase_createdonbehalfby](systemuser.md#BKMK_lk_solutioncomponentbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutioncomponentbase_modifiedonbehalfby"></a> lk_solutioncomponentbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_solutioncomponentbase_modifiedonbehalfby](systemuser.md#BKMK_lk_solutioncomponentbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solution_solutioncomponent"></a> solution_solutioncomponent

One-To-Many Relationship: [solution solution_solutioncomponent](solution.md#BKMK_solution_solutioncomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`solution`|
|ReferencedAttribute|`solutionid`|
|ReferencingAttribute|`solutionid`|
|ReferencingEntityNavigationPropertyName|`solutionid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_solutioncomponent_parent_solutioncomponent-many-to-one"></a> solutioncomponent_parent_solutioncomponent

One-To-Many Relationship: [solutioncomponent solutioncomponent_parent_solutioncomponent](#BKMK_solutioncomponent_parent_solutioncomponent-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponent`|
|ReferencedAttribute|`solutioncomponentid`|
|ReferencingAttribute|`rootsolutioncomponentid`|
|ReferencingEntityNavigationPropertyName|`rootsolutioncomponentid_solutioncomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_solutioncomponent_parent_solutioncomponent-one-to-many"></a> solutioncomponent_parent_solutioncomponent

Many-To-One Relationship: [solutioncomponent solutioncomponent_parent_solutioncomponent](#BKMK_solutioncomponent_parent_solutioncomponent-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponent`|
|ReferencingAttribute|`rootsolutioncomponentid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponent_parent_solutioncomponent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.solutioncomponent?displayProperty=fullName>
