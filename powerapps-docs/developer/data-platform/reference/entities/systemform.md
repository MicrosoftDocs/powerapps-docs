---
title: "System Form (SystemForm) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the System Form (SystemForm) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# System Form (SystemForm) table/entity reference (Microsoft Dataverse)

Organization-owned entity customizations including form layout and dashboards.

## Messages

The following table lists the messages for the System Form (SystemForm) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `CopySystemForm`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CopySystemForm?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.CopySystemFormRequest>|
| `Create`<br />Event: False |`POST` /systemforms<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /systemforms(*formid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /systemforms(*formid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveFilteredForms`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveFilteredForms?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveFilteredFormsRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /systemforms<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveUnpublished`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `Update`<br />Event: False |`PATCH` /systemforms(*formid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /systemforms(*formid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the System Form (SystemForm) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **System Form** |
| **DisplayCollectionName** | **System Forms** |
| **SchemaName** | `SystemForm` |
| **CollectionSchemaName** | `SystemForms` |
| **EntitySetName** | `systemforms`|
| **LogicalName** | `systemform` |
| **LogicalCollectionName** | `systemforms` |
| **PrimaryIdAttribute** | `formid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

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
|---|---|
|Description|**Unique identifier of the parent form.**|
|DisplayName|**Parent Form**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ancestorformid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemform|

### <a name="BKMK_CanBeDeleted"></a> CanBeDeleted

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component can be deleted.**|
|DisplayName|**Can Be Deleted**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbedeleted`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the form or dashboard.**|
|DisplayName|**Description**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|2000|

### <a name="BKMK_FormActivationState"></a> FormActivationState

|Property|Value|
|---|---|
|Description|**Specifies the state of the form.**|
|DisplayName|**Form State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`formactivationstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`systemform_formactivationstate`|

#### FormActivationState Choices/Options

|Value|Label|
|---|---|
|0|**Inactive**|
|1|**Active**|

### <a name="BKMK_FormId"></a> FormId

|Property|Value|
|---|---|
|Description|**Unique identifier of the record type form.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`formid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_FormJson"></a> FormJson

|Property|Value|
|---|---|
|Description|**Json representation of the form layout.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`formjson`|
|RequiredLevel|SystemRequired|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_FormPresentation"></a> FormPresentation

|Property|Value|
|---|---|
|Description|**Specifies whether this form is in the updated UI layout in Microsoft Dynamics CRM 2015 or Microsoft Dynamics CRM Online 2015 Update.**|
|DisplayName|**AIR Refreshed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`formpresentation`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`systemform_formpresentation`|

#### FormPresentation Choices/Options

|Value|Label|
|---|---|
|0|**ClassicForm**|
|1|**AirForm**|
|2|**ConvertedICForm**|

### <a name="BKMK_FormXml"></a> FormXml

|Property|Value|
|---|---|
|Description|**XML representation of the form layout.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`formxml`|
|RequiredLevel|SystemRequired|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the form is introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_IsAIRMerged"></a> IsAIRMerged

|Property|Value|
|---|---|
|Description|**Specifies whether this form is merged with the updated UI layout in Microsoft Dynamics CRM 2015 or Microsoft Dynamics CRM Online 2015 Update.**|
|DisplayName|**Refreshed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isairmerged`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`systemform_isairmerged`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|---|---|
|Description|**Information that specifies whether the form or the dashboard is the system default.**|
|DisplayName|**Default Form**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdefault`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`systemform_isdefault`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsDesktopEnabled"></a> IsDesktopEnabled

|Property|Value|
|---|---|
|Description|**Information that specifies whether the dashboard is enabled for desktop.**|
|DisplayName|**Is Desktop Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdesktopenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`systemform_isdesktopenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsTabletEnabled"></a> IsTabletEnabled

|Property|Value|
|---|---|
|Description|**Information that specifies whether the dashboard is enabled for tablet.**|
|DisplayName|**Is Tablet Enabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`istabletenabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`systemform_istabletenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the form.**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|100|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Code that represents the record type.**|
|DisplayName|**Entity Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_Type"></a> Type

|Property|Value|
|---|---|
|Description|**Type of the form, for example, Dashboard or Preview.**|
|DisplayName|**Form Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`systemform_type`|

#### Type Choices/Options

|Value|Label|
|---|---|
|0|**Dashboard**|
|1|**AppointmentBook**|
|2|**Main**|
|3|**MiniCampaignBO**|
|4|**Preview**|
|5|**Mobile - Express**|
|6|**Quick View Form**|
|7|**Quick Create**|
|8|**Dialog**|
|9|**Task Flow Form**|
|10|**InteractionCentricDashboard**|
|11|**Card**|
|12|**Main - Interactive experience**|
|13|**Contextual Dashboard**|
|100|**Other**|
|101|**MainBackup**|
|102|**AppointmentBookBackup**|
|103|**Power BI Dashboard**|

### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|---|---|
|Description|**Unique Name**|
|DisplayName|**Unique Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`uniquename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_Version"></a> Version

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`version`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [FormIdUnique](#BKMK_FormIdUnique)
- [FormXmlManaged](#BKMK_FormXmlManaged)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PublishedOn](#BKMK_PublishedOn)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

### <a name="BKMK_FormIdUnique"></a> FormIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the form used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`formidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_FormXmlManaged"></a> FormXmlManaged

|Property|Value|
|---|---|
|Description|**formXml diff as in a managed solution. for internal use only**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`formxmlmanaged`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description||
|DisplayName|**State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PublishedOn"></a> PublishedOn

|Property|Value|
|---|---|
|Description||
|DisplayName|**Published On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publishedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Represents a version of customizations to be synchronized with the Microsoft Dynamics 365 client for Outlook.**|
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

- [form_ancestor_form](#BKMK_form_ancestor_form-many-to-one)
- [organization_systemforms](#BKMK_organization_systemforms)

### <a name="BKMK_form_ancestor_form-many-to-one"></a> form_ancestor_form

One-To-Many Relationship: [systemform form_ancestor_form](#BKMK_form_ancestor_form-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`systemform`|
|ReferencedAttribute|`formid`|
|ReferencingAttribute|`ancestorformid`|
|ReferencingEntityNavigationPropertyName|`ancestorformid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_systemforms"></a> organization_systemforms

One-To-Many Relationship: [organization organization_systemforms](organization.md#BKMK_organization_systemforms)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [form_ancestor_form](#BKMK_form_ancestor_form-one-to-many)
- [processtrigger_systemform](#BKMK_processtrigger_systemform)
- [SystemForm_AsyncOperations](#BKMK_SystemForm_AsyncOperations)
- [SystemForm_BulkDeleteFailures](#BKMK_SystemForm_BulkDeleteFailures)

### <a name="BKMK_form_ancestor_form-one-to-many"></a> form_ancestor_form

Many-To-One Relationship: [systemform form_ancestor_form](#BKMK_form_ancestor_form-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`systemform`|
|ReferencingAttribute|`ancestorformid`|
|ReferencedEntityNavigationPropertyName|`form_ancestor_form`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processtrigger_systemform"></a> processtrigger_systemform

Many-To-One Relationship: [processtrigger processtrigger_systemform](processtrigger.md#BKMK_processtrigger_systemform)

|Property|Value|
|---|---|
|ReferencingEntity|`processtrigger`|
|ReferencingAttribute|`formid`|
|ReferencedEntityNavigationPropertyName|`processtrigger_systemform`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SystemForm_AsyncOperations"></a> SystemForm_AsyncOperations

Many-To-One Relationship: [asyncoperation SystemForm_AsyncOperations](asyncoperation.md#BKMK_SystemForm_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SystemForm_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SystemForm_BulkDeleteFailures"></a> SystemForm_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure SystemForm_BulkDeleteFailures](bulkdeletefailure.md#BKMK_SystemForm_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SystemForm_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.systemform?displayProperty=fullName>
