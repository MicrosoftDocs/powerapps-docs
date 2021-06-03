---
title: "SystemForm table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SystemForm table/entity."
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

# SystemForm table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Organization-owned entity customizations including form layout and dashboards.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|CopySystemForm|<xref href="Microsoft.Dynamics.CRM.CopySystemForm?text=CopySystemForm Action" />|<xref:Microsoft.Crm.Sdk.Messages.CopySystemFormRequest>|
|Create|POST [*org URI*]/api/data/v9.0/systemforms<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/systemforms(*formid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/systemforms(*formid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveFilteredForms|<xref href="Microsoft.Dynamics.CRM.RetrieveFilteredForms?text=RetrieveFilteredForms Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveFilteredFormsRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/systemforms<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrieveUnpublished|<xref href="Microsoft.Dynamics.CRM.RetrieveUnpublished?text=RetrieveUnpublished Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
|RetrieveUnpublishedMultiple|<xref href="Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?text=RetrieveUnpublishedMultiple Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/systemforms(*formid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SystemForms|
|DisplayCollectionName|System Forms|
|DisplayName|System Form|
|EntitySetName|systemforms|
|IsBPFEntity|False|
|LogicalCollectionName|systemforms|
|LogicalName|systemform|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|formid|
|PrimaryNameAttribute|name|
|SchemaName|SystemForm|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AncestorFormId](#BKMK_AncestorFormId)
- [CanBeDeleted](#BKMK_CanBeDeleted)
- [Description](#BKMK_Description)
- [FormActivationState](#BKMK_FormActivationState)
- [FormId](#BKMK_FormId)
- [FormJson](#BKMK_FormJson)
- [FormPresentation](#BKMK_FormPresentation)
- [FormXml](#BKMK_FormXml)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsAIRMerged](#BKMK_IsAIRMerged)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsDefault](#BKMK_IsDefault)
- [IsDesktopEnabled](#BKMK_IsDesktopEnabled)
- [IsTabletEnabled](#BKMK_IsTabletEnabled)
- [Name](#BKMK_Name)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [Type](#BKMK_Type)
- [UniqueName](#BKMK_UniqueName)
- [Version](#BKMK_Version)


### <a name="BKMK_AncestorFormId"></a> AncestorFormId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the parent form.|
|DisplayName|Parent Form|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|ancestorformid|
|RequiredLevel|None|
|Targets|systemform|
|Type|Lookup|


### <a name="BKMK_CanBeDeleted"></a> CanBeDeleted

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component can be deleted.|
|DisplayName|Can Be Deleted|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canbedeleted|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the form or dashboard.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_FormActivationState"></a> FormActivationState

|Property|Value|
|--------|-----|
|Description|Specifies the state of the form.|
|DisplayName|Form State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|formactivationstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### FormActivationState Choices/Options

|Value|Label|
|-----|-----|
|0|Inactive|
|1|Active|



### <a name="BKMK_FormId"></a> FormId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the record type form.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|formid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_FormJson"></a> FormJson

|Property|Value|
|--------|-----|
|Description|Json representation of the form layout.|
|DisplayName||
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|formjson|
|MaxLength|1073741823|
|RequiredLevel|SystemRequired|
|Type|Memo|


### <a name="BKMK_FormPresentation"></a> FormPresentation

|Property|Value|
|--------|-----|
|Description|Specifies whether this form is in the updated UI layout in Microsoft Dynamics CRM 2015 or Microsoft Dynamics CRM Online 2015 Update.|
|DisplayName|AIR Refreshed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|formpresentation|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### FormPresentation Choices/Options

|Value|Label|
|-----|-----|
|0|ClassicForm|
|1|AirForm|
|2|ConvertedICForm|



### <a name="BKMK_FormXml"></a> FormXml

|Property|Value|
|--------|-----|
|Description|XML representation of the form layout.|
|DisplayName||
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|formxml|
|MaxLength|1073741823|
|RequiredLevel|SystemRequired|
|Type|Memo|


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the form is introduced.|
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


### <a name="BKMK_IsAIRMerged"></a> IsAIRMerged

|Property|Value|
|--------|-----|
|Description|Specifies whether this form is merged with the updated UI layout in Microsoft Dynamics CRM 2015 or Microsoft Dynamics CRM Online 2015 Update.|
|DisplayName|Refreshed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isairmerged|
|RequiredLevel|None|
|Type|Boolean|

#### IsAIRMerged Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component can be customized.|
|DisplayName|Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|--------|-----|
|Description|Information that specifies whether the form or the dashboard is the system default.|
|DisplayName|Default Form|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isdefault|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsDefault Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsDesktopEnabled"></a> IsDesktopEnabled

|Property|Value|
|--------|-----|
|Description|Information that specifies whether the dashboard is enabled for desktop.|
|DisplayName|Is Desktop Enabled|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isdesktopenabled|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsDesktopEnabled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsTabletEnabled"></a> IsTabletEnabled

|Property|Value|
|--------|-----|
|Description|Information that specifies whether the dashboard is enabled for tablet.|
|DisplayName|Is Tablet Enabled|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|istabletenabled|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsTabletEnabled Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the form.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Code that represents the record type.|
|DisplayName|Entity Name|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|objecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_Type"></a> Type

|Property|Value|
|--------|-----|
|Description|Type of the form, for example, Dashboard or Preview.|
|DisplayName|Form Type|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|type|
|RequiredLevel|None|
|Type|Picklist|

#### Type Choices/Options

|Value|Label|
|-----|-----|
|0|Dashboard|
|1|AppointmentBook|
|2|Main|
|3|MiniCampaignBO|
|4|Preview|
|5|Mobile - Express|
|6|Quick View Form|
|7|Quick Create|
|8|Dialog|
|9|Task Flow Form|
|10|InteractionCentricDashboard|
|11|Card|
|12|Main - Interactive experience|
|13|Contextual Dashboard|
|100|Other|
|101|MainBackup|
|102|AppointmentBookBackup|
|103|Power BI Dashboard|



### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|--------|-----|
|Description|Unique Name|
|DisplayName|Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|uniquename|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Version"></a> Version

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|version|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AncestorFormIdName](#BKMK_AncestorFormIdName)
- [ComponentState](#BKMK_ComponentState)
- [FormIdUnique](#BKMK_FormIdUnique)
- [FormXmlManaged](#BKMK_FormXmlManaged)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PublishedOn](#BKMK_PublishedOn)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AncestorFormIdName"></a> AncestorFormIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ancestorformidname|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


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

|Value|Label|
|-----|-----|
|0|Published|
|1|Unpublished|
|2|Deleted|
|3|Deleted Unpublished|



### <a name="BKMK_FormIdUnique"></a> FormIdUnique

|Property|Value|
|--------|-----|
|Description|Unique identifier of the form used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|formidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_FormXmlManaged"></a> FormXmlManaged

|Property|Value|
|--------|-----|
|Description|formXml diff as in a managed solution. for internal use only|
|DisplayName||
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|formxmlmanaged|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description||
|DisplayName|State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|
|-----|-----|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization.|
|DisplayName||
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
|Description||
|DisplayName|Published On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|publishedon|
|RequiredLevel|None|
|Type|DateTime|


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
|Description|Represents a version of customizations to be synchronized with the Microsoft Dynamics 365 client for Outlook.|
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

- [form_ancestor_form](#BKMK_form_ancestor_form)
- [SystemForm_AsyncOperations](#BKMK_SystemForm_AsyncOperations)
- [processtrigger_systemform](#BKMK_processtrigger_systemform)
- [SystemForm_BulkDeleteFailures](#BKMK_SystemForm_BulkDeleteFailures)


### <a name="BKMK_form_ancestor_form"></a> form_ancestor_form

Same as systemform table [form_ancestor_form](systemform.md#BKMK_form_ancestor_form) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemform|
|ReferencingAttribute|ancestorformid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|form_ancestor_form|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemForm_AsyncOperations"></a> SystemForm_AsyncOperations

Same as asyncoperation table [SystemForm_AsyncOperations](asyncoperation.md#BKMK_SystemForm_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemForm_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_processtrigger_systemform"></a> processtrigger_systemform

Same as processtrigger table [processtrigger_systemform](processtrigger.md#BKMK_processtrigger_systemform) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processtrigger|
|ReferencingAttribute|formid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|processtrigger_systemform|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_SystemForm_BulkDeleteFailures"></a> SystemForm_BulkDeleteFailures

Same as bulkdeletefailure table [SystemForm_BulkDeleteFailures](bulkdeletefailure.md#BKMK_SystemForm_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|SystemForm_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [form_ancestor_form](#BKMK_form_ancestor_form)
- [organization_systemforms](#BKMK_organization_systemforms)


### <a name="BKMK_form_ancestor_form"></a> form_ancestor_form

See systemform Table [form_ancestor_form](systemform.md#BKMK_form_ancestor_form) One-To-Many relationship.

### <a name="BKMK_organization_systemforms"></a> organization_systemforms

See organization Table [organization_systemforms](organization.md#BKMK_organization_systemforms) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.systemform?text=systemform EntityType" />