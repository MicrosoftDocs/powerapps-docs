---
title: "MobileOfflineProfileItemAssociation table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the MobileOfflineProfileItemAssociation table/entity."
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

# MobileOfflineProfileItemAssociation table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Information on relationships to be used to follow related entity's records for mobile offline profile item.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/mobileofflineprofileitemassociations<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/mobileofflineprofileitemassociations(*mobileofflineprofileitemassociationid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/mobileofflineprofileitemassociations(*mobileofflineprofileitemassociationid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/mobileofflineprofileitemassociations<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrieveUnpublished|<xref href="Microsoft.Dynamics.CRM.RetrieveUnpublished?text=RetrieveUnpublished Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
|RetrieveUnpublishedMultiple|<xref href="Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?text=RetrieveUnpublishedMultiple Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/mobileofflineprofileitemassociations(*mobileofflineprofileitemassociationid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|MobileOfflineProfileItemAssociations|
|DisplayCollectionName|Mobile Offline Profile Item Associations|
|DisplayName|Mobile Offline Profile Item Association|
|EntitySetName|mobileofflineprofileitemassociations|
|IsBPFEntity|False|
|LogicalCollectionName|mobileofflineprofileitemassociations|
|LogicalName|mobileofflineprofileitemassociation|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|mobileofflineprofileitemassociationid|
|PrimaryNameAttribute|name|
|SchemaName|MobileOfflineProfileItemAssociation|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [IntroducedVersion](#BKMK_IntroducedVersion)
- [MobileOfflineProfileItemAssociationId](#BKMK_MobileOfflineProfileItemAssociationId)
- [MobileOfflineProfileItemId](#BKMK_MobileOfflineProfileItemId)
- [MobileOfflineProfileItemIdName](#BKMK_MobileOfflineProfileItemIdName)
- [Name](#BKMK_Name)
- [ProcessId](#BKMK_ProcessId)
- [ProfileItemAssociationEntityFilter](#BKMK_ProfileItemAssociationEntityFilter)
- [RelationshipData](#BKMK_RelationshipData)
- [RelationshipDisplayName](#BKMK_RelationshipDisplayName)
- [RelationshipId](#BKMK_RelationshipId)
- [SelectedRelationShipsSchema](#BKMK_SelectedRelationShipsSchema)
- [StageId](#BKMK_StageId)
- [TraversedPath](#BKMK_TraversedPath)


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the Mobile offline Profile Item Association is introduced.|
|DisplayName|Introduced Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|introducedversion|
|MaxLength|48|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MobileOfflineProfileItemAssociationId"></a> MobileOfflineProfileItemAssociationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the mobile offline profile item associaition.|
|DisplayName|Mobile Offline profileitemassociation|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mobileofflineprofileitemassociationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_MobileOfflineProfileItemId"></a> MobileOfflineProfileItemId

|Property|Value|
|--------|-----|
|Description|Id of the parent profile item.|
|DisplayName|Regarding|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mobileofflineprofileitemid|
|RequiredLevel|SystemRequired|
|Targets|mobileofflineprofileitem|
|Type|Lookup|


### <a name="BKMK_MobileOfflineProfileItemIdName"></a> MobileOfflineProfileItemIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|mobileofflineprofileitemidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Enter the name of the mobile offline profile item association.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|name|
|MaxLength|200|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the process.|
|DisplayName|Process|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ProfileItemAssociationEntityFilter"></a> ProfileItemAssociationEntityFilter

|Property|Value|
|--------|-----|
|Description|Profile item association entity filter criteria.|
|DisplayName|Profile item association entity filter|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|profileitemassociationentityfilter|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_RelationshipData"></a> RelationshipData

|Property|Value|
|--------|-----|
|Description|Internal Use Only|
|DisplayName|Internal Use Only|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|relationshipdata|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_RelationshipDisplayName"></a> RelationshipDisplayName

|Property|Value|
|--------|-----|
|Description|Entity relationship schema name|
|DisplayName|Entity Relationship|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|relationshipdisplayname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RelationshipId"></a> RelationshipId

|Property|Value|
|--------|-----|
|Description|Shows the relationship|
|DisplayName|Shows the relationship|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|relationshipid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SelectedRelationShipsSchema"></a> SelectedRelationShipsSchema

|Property|Value|
|--------|-----|
|Description|List of relationships of entity selected in parent profile item|
|DisplayName|Entity Relationship|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|selectedrelationshipsschema|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### SelectedRelationShipsSchema Choices/Options

|Value|Label|Description|
|-----|-----|--------|




### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the stage.|
|DisplayName|(Deprecated) Process Stage|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|stageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|(Deprecated) Traversed Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|traversedpath|
|MaxLength|1250|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [IsValidated](#BKMK_IsValidated)
- [MobileOfflineProfileItemAssociationIdUnique](#BKMK_MobileOfflineProfileItemAssociationIdUnique)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PublishedOn](#BKMK_PublishedOn)
- [RelationshipName](#BKMK_RelationshipName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|200|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record on behalf of another user.|
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
|MaxLength|200|
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
|MaxLength|200|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_IsValidated"></a> IsValidated

|Property|Value|
|--------|-----|
|Description|Information about whether profile item association is validated or not|
|DisplayName|Is Valid For Mobile Offline|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isvalidated|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsValidated Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_MobileOfflineProfileItemAssociationIdUnique"></a> MobileOfflineProfileItemAssociationIdUnique

|Property|Value|
|--------|-----|
|Description|For Internal Use Only|
|DisplayName|Unique Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mobileofflineprofileitemassociationidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|200|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who updated the record on behalf of another user.|
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
|MaxLength|200|
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
|MaxLength|200|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the Mobile Offline Profile Item Association.|
|DisplayName|Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_PublishedOn"></a> PublishedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Displays the last published date time.|
|DisplayName|Published On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|publishedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_RelationshipName"></a> RelationshipName

|Property|Value|
|--------|-----|
|Description|Display name of entity relationship|
|DisplayName|Entity Relationship|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|relationshipname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the Mobile Offline profileitemassociation.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_mobileofflineprofileitemassociation_modifiedby](#BKMK_lk_mobileofflineprofileitemassociation_modifiedby)
- [lk_mobileofflineprofileitemassociation_modifiedonbehalfby](#BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby)
- [MobileOfflineProfileItem_MobileOfflineProfileItemAssociation](#BKMK_MobileOfflineProfileItem_MobileOfflineProfileItemAssociation)
- [lk_MobileOfflineProfileItemAssociation_createdby](#BKMK_lk_MobileOfflineProfileItemAssociation_createdby)
- [MobileOfflineProfileItemAssociation_organization](#BKMK_MobileOfflineProfileItemAssociation_organization)
- [lk_mobileofflineprofileitemassociation_createdonbehalfby](#BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby)


### <a name="BKMK_lk_mobileofflineprofileitemassociation_modifiedby"></a> lk_mobileofflineprofileitemassociation_modifiedby

See systemuser Table [lk_mobileofflineprofileitemassociation_modifiedby](systemuser.md#BKMK_lk_mobileofflineprofileitemassociation_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby"></a> lk_mobileofflineprofileitemassociation_modifiedonbehalfby

See systemuser Table [lk_mobileofflineprofileitemassociation_modifiedonbehalfby](systemuser.md#BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_MobileOfflineProfileItem_MobileOfflineProfileItemAssociation"></a> MobileOfflineProfileItem_MobileOfflineProfileItemAssociation

See mobileofflineprofileitem Table [MobileOfflineProfileItem_MobileOfflineProfileItemAssociation](mobileofflineprofileitem.md#BKMK_MobileOfflineProfileItem_MobileOfflineProfileItemAssociation) One-To-Many relationship.

### <a name="BKMK_lk_MobileOfflineProfileItemAssociation_createdby"></a> lk_MobileOfflineProfileItemAssociation_createdby

See systemuser Table [lk_MobileOfflineProfileItemAssociation_createdby](systemuser.md#BKMK_lk_MobileOfflineProfileItemAssociation_createdby) One-To-Many relationship.

### <a name="BKMK_MobileOfflineProfileItemAssociation_organization"></a> MobileOfflineProfileItemAssociation_organization

See organization Table [MobileOfflineProfileItemAssociation_organization](organization.md#BKMK_MobileOfflineProfileItemAssociation_organization) One-To-Many relationship.

### <a name="BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby"></a> lk_mobileofflineprofileitemassociation_createdonbehalfby

See systemuser Table [lk_mobileofflineprofileitemassociation_createdonbehalfby](systemuser.md#BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.mobileofflineprofileitemassociation?text=mobileofflineprofileitemassociation EntityType" />