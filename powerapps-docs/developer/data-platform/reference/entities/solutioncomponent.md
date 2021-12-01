---
title: "SolutionComponent table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SolutionComponent table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# SolutionComponent table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

A component of a CRM solution.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|AddSolutionComponent|<xref href="Microsoft.Dynamics.CRM.AddSolutionComponent?text=AddSolutionComponent Action" />|<xref:Microsoft.Crm.Sdk.Messages.AddSolutionComponentRequest>|
|IsComponentCustomizable|<xref href="Microsoft.Dynamics.CRM.IsComponentCustomizable?text=IsComponentCustomizable Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsComponentCustomizableRequest>|
|RemoveSolutionComponent|<xref href="Microsoft.Dynamics.CRM.RemoveSolutionComponent?text=RemoveSolutionComponent Action" />|<xref:Microsoft.Crm.Sdk.Messages.RemoveSolutionComponentRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/solutioncomponents(*solutioncomponentid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/solutioncomponents<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|UpdateSolutionComponent|<xref href="Microsoft.Dynamics.CRM.UpdateSolutionComponent?text=UpdateSolutionComponent Action" />|<xref:Microsoft.Crm.Sdk.Messages.UpdateSolutionComponentRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SolutionComponents|
|DisplayCollectionName|Solution Components|
|DisplayName|Solution Component|
|EntitySetName|solutioncomponents|
|IsBPFEntity|False|
|LogicalCollectionName|solutioncomponentss|
|LogicalName|solutioncomponent|
|OwnershipType|None|
|PrimaryIdAttribute|solutioncomponentid|
|PrimaryNameAttribute||
|SchemaName|SolutionComponent|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentType](#BKMK_ComponentType)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsMetadata](#BKMK_IsMetadata)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [ObjectId](#BKMK_ObjectId)
- [RootComponentBehavior](#BKMK_RootComponentBehavior)
- [RootSolutionComponentId](#BKMK_RootSolutionComponentId)
- [SolutionComponentId](#BKMK_SolutionComponentId)
- [SolutionId](#BKMK_SolutionId)
- [SolutionIdName](#BKMK_SolutionIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentType"></a> ComponentType

|Property|Value|
|--------|-----|
|Description|The object type code of the component.|
|DisplayName|Object Type Code|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componenttype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Entity||
|2|Attribute||
|3|Relationship||
|4|Attribute Picklist Value||
|5|Attribute Lookup Value||
|6|View Attribute||
|7|Localized Label||
|8|Relationship Extra Condition||
|9|Option Set||
|10|Entity Relationship||
|11|Entity Relationship Role||
|12|Entity Relationship Relationships||
|13|Managed Property||
|14|Entity Key||
|16|Privilege||
|17|PrivilegeObjectTypeCode||
|18|Index||
|20|Role||
|21|Role Privilege||
|22|Display String||
|23|Display String Map||
|24|Form||
|25|Organization||
|26|Saved Query||
|29|Workflow||
|31|Report||
|32|Report Entity||
|33|Report Category||
|34|Report Visibility||
|35|Attachment||
|36|Email Template||
|37|Contract Template||
|38|KB Article Template||
|39|Mail Merge Template||
|44|Duplicate Rule||
|45|Duplicate Rule Condition||
|46|Entity Map||
|47|Attribute Map||
|48|Ribbon Command||
|49|Ribbon Context Group||
|50|Ribbon Customization||
|52|Ribbon Rule||
|53|Ribbon Tab To Command Map||
|55|Ribbon Diff||
|59|Saved Query Visualization||
|60|System Form||
|61|Web Resource||
|62|Site Map||
|63|Connection Role||
|64|Complex Control||
|65|Hierarchy Rule||
|66|Custom Control||
|68|Custom Control Default Config||
|70|Field Security Profile||
|71|Field Permission||
|90|Plugin Type||
|91|Plugin Assembly||
|92|SDK Message Processing Step||
|93|SDK Message Processing Step Image||
|95|Service Endpoint||
|150|Routing Rule||
|151|Routing Rule Item||
|152|SLA||
|153|SLA Item||
|154|Convert Rule||
|155|Convert Rule Item||
|161|Mobile Offline Profile||
|162|Mobile Offline Profile Item||
|165|Similarity Rule||
|166|Data Source Mapping||
|201|SDKMessage||
|202|SDKMessageFilter||
|203|SdkMessagePair||
|204|SdkMessageRequest||
|205|SdkMessageRequestField||
|206|SdkMessageResponse||
|207|SdkMessageResponseField||
|208|Import Map||
|210|WebWizard||
|300|Canvas App||
|371|Connector||
|372|Connector||
|380|Environment Variable Definition||
|381|Environment Variable Value||
|400|AI Project Type||
|401|AI Project||
|402|AI Configuration||
|430|Entity Analytics Configuration||
|431|Attribute Image Configuration||
|432|Entity Image Configuration||



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the solution|
|DisplayName|Created By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the solution was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the solution.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsMetadata"></a> IsMetadata

|Property|Value|
|--------|-----|
|Description|Indicates whether this component is metadata or data.|
|DisplayName|Is this component metadata|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismetadata|
|RequiredLevel|None|
|Type|Boolean|

#### IsMetadata Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Metadata|
|0|Data|

**DefaultValue**: True



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the solution.|
|DisplayName|Modified By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the solution was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the solution.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the object with which the component is associated.|
|DisplayName|Regarding|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_RootComponentBehavior"></a> RootComponentBehavior

|Property|Value|
|--------|-----|
|Description|Indicates the include behavior of the root component.|
|DisplayName|Root Component Behavior|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rootcomponentbehavior|
|RequiredLevel|None|
|Type|Picklist|

#### RootComponentBehavior Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Include Subcomponents||
|1|Do not include subcomponents||
|2|Include As Shell Only||



### <a name="BKMK_RootSolutionComponentId"></a> RootSolutionComponentId

|Property|Value|
|--------|-----|
|Description|The parent ID of the subcomponent, which will be a root|
|DisplayName|Root Solution Component ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rootsolutioncomponentid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_SolutionComponentId"></a> SolutionComponentId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the solution component.|
|DisplayName|Solution Component Identifier|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutioncomponentid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the solution.|
|DisplayName|Solution|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|None|
|Targets|solution|
|Type|Lookup|


### <a name="BKMK_SolutionIdName"></a> SolutionIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionidname|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_solutioncomponent_parent_solutioncomponent"></a> solutioncomponent_parent_solutioncomponent

Same as solutioncomponent table [solutioncomponent_parent_solutioncomponent](solutioncomponent.md#BKMK_solutioncomponent_parent_solutioncomponent) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponent|
|ReferencingAttribute|rootsolutioncomponentid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|solutioncomponent_parent_solutioncomponent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_solutioncomponentbase_modifiedonbehalfby](#BKMK_lk_solutioncomponentbase_modifiedonbehalfby)
- [lk_solutioncomponentbase_createdonbehalfby](#BKMK_lk_solutioncomponentbase_createdonbehalfby)
- [solution_solutioncomponent](#BKMK_solution_solutioncomponent)
- [solutioncomponent_parent_solutioncomponent](#BKMK_solutioncomponent_parent_solutioncomponent)


### <a name="BKMK_lk_solutioncomponentbase_modifiedonbehalfby"></a> lk_solutioncomponentbase_modifiedonbehalfby

See systemuser Table [lk_solutioncomponentbase_modifiedonbehalfby](systemuser.md#BKMK_lk_solutioncomponentbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_solutioncomponentbase_createdonbehalfby"></a> lk_solutioncomponentbase_createdonbehalfby

See systemuser Table [lk_solutioncomponentbase_createdonbehalfby](systemuser.md#BKMK_lk_solutioncomponentbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_solution_solutioncomponent"></a> solution_solutioncomponent

See solution Table [solution_solutioncomponent](solution.md#BKMK_solution_solutioncomponent) One-To-Many relationship.

### <a name="BKMK_solutioncomponent_parent_solutioncomponent"></a> solutioncomponent_parent_solutioncomponent

See solutioncomponent Table [solutioncomponent_parent_solutioncomponent](solutioncomponent.md#BKMK_solutioncomponent_parent_solutioncomponent) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.solutioncomponent?text=solutioncomponent EntityType" />