---
title: "Model-driven App (AppModule) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Model-driven App (AppModule) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Model-driven App (AppModule) table/entity reference (Microsoft Dataverse)

A role-based, modular business app that provides task-based functionality for a particular area of work.

## Messages

The following table lists the messages for the Model-driven App (AppModule) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `AddAppComponents`<br />Event: False |<xref:Microsoft.Dynamics.CRM.AddAppComponents?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.AddAppComponentsRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /appmodules<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /appmodules(*appmoduleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RemoveAppComponents`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RemoveAppComponents?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RemoveAppComponentsRequest>|
| `Retrieve`<br />Event: False |`GET` /appmodules(*appmoduleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveAppComponents`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveAppComponents?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveAppComponentsRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /appmodules<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveUnpublished`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `Update`<br />Event: False |`PATCH` /appmodules(*appmoduleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /appmodules(*appmoduleid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `ValidateApp`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ValidateApp?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ValidateAppRequest>|

## Properties

The following table lists selected properties for the Model-driven App (AppModule) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Model-driven App** |
| **DisplayCollectionName** | **Model-driven Apps** |
| **SchemaName** | `AppModule` |
| **CollectionSchemaName** | `AppModules` |
| **EntitySetName** | `appmodules`|
| **LogicalName** | `appmodule` |
| **LogicalCollectionName** | `appmodules` |
| **PrimaryIdAttribute** | `appmoduleid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [aiappdescription](#BKMK_aiappdescription)
- [aidescriptiongeneratedon](#BKMK_aidescriptiongeneratedon)
- [appgraph](#BKMK_appgraph)
- [AppModuleId](#BKMK_AppModuleId)
- [AppModuleIdUnique](#BKMK_AppModuleIdUnique)
- [AppModuleVersion](#BKMK_AppModuleVersion)
- [AppModuleXmlManaged](#BKMK_AppModuleXmlManaged)
- [ClientType](#BKMK_ClientType)
- [ConfigXML](#BKMK_ConfigXML)
- [Description](#BKMK_Description)
- [EventHandlers](#BKMK_EventHandlers)
- [FormFactor](#BKMK_FormFactor)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsDefault](#BKMK_IsDefault)
- [IsFeatured](#BKMK_IsFeatured)
- [Name](#BKMK_Name)
- [NavigationType](#BKMK_NavigationType)
- [OptimizedFor](#BKMK_OptimizedFor)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PublishedOn](#BKMK_PublishedOn)
- [PublisherId](#BKMK_PublisherId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [UniqueName](#BKMK_UniqueName)
- [URL](#BKMK_URL)
- [WebResourceId](#BKMK_WebResourceId)
- [WelcomePageId](#BKMK_WelcomePageId)

### <a name="BKMK_aiappdescription"></a> aiappdescription

|Property|Value|
|---|---|
|Description|**This field is used to store AI generated Description for Model-driven App**|
|DisplayName|**AI App Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aiappdescription`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_aidescriptiongeneratedon"></a> aidescriptiongeneratedon

|Property|Value|
|---|---|
|Description|**This field stores the Time when last AI App Description was generated.**|
|DisplayName|**AI Description Generated On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`aidescriptiongeneratedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_appgraph"></a> appgraph

|Property|Value|
|---|---|
|Description|**This field is used to store App Graph for Model-driven App**|
|DisplayName|**App Graph**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`appgraph`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_AppModuleId"></a> AppModuleId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**AppModuleId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appmoduleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AppModuleIdUnique"></a> AppModuleIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the App Module used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook**|
|DisplayName|**App Module Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appmoduleidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AppModuleVersion"></a> AppModuleVersion

|Property|Value|
|---|---|
|Description|**App Module Version**|
|DisplayName|**App Module Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appmoduleversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_AppModuleXmlManaged"></a> AppModuleXmlManaged

|Property|Value|
|---|---|
|Description|**App Module Xml Managed**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`appmodulexmlmanaged`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ClientType"></a> ClientType

|Property|Value|
|---|---|
|Description|**Client Type such as Web or UCI**|
|DisplayName|**Client Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`clienttype`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|31|
|MinValue|1|

### <a name="BKMK_ConfigXML"></a> ConfigXML

|Property|Value|
|---|---|
|Description|**Contains configuration XML**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`configxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description for entity**|
|DisplayName|**Description**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|2000|

### <a name="BKMK_EventHandlers"></a> EventHandlers

|Property|Value|
|---|---|
|Description|**App Module Event Handlers**|
|DisplayName|**Event Handlers**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`eventhandlers`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_FormFactor"></a> FormFactor

|Property|Value|
|---|---|
|Description|**Form Factor**|
|DisplayName|**Form Factor**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`formfactor`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|8|
|MinValue|1|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Unique identifier of the data import or data migration that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the similarity rule is introduced.**|
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
|MaxLength|100|

### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|---|---|
|Description|**Is Default**|
|DisplayName|**Is Default**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdefault`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`appmodule_isdefault`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsFeatured"></a> IsFeatured

|Property|Value|
|---|---|
|Description|**Is Featured**|
|DisplayName|**IsFeatured**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isfeatured`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`appmodule_isfeatured`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of App Module**|
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

### <a name="BKMK_NavigationType"></a> NavigationType

|Property|Value|
|---|---|
|Description|**App navigation type**|
|DisplayName|**Navigation type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`navigationtype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`appmodule_navigationtype`|

#### NavigationType Choices/Options

|Value|Label|
|---|---|
|0|**Single session**|
|1|**Multi session**|

### <a name="BKMK_OptimizedFor"></a> OptimizedFor

|Property|Value|
|---|---|
|Description|**The client that this app is optimized for**|
|DisplayName|**Optimized Client**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`optimizedfor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PublishedOn"></a> PublishedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was published.**|
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

### <a name="BKMK_PublisherId"></a> PublisherId

|Property|Value|
|---|---|
|Description|**Unique identifier of the publisher.**|
|DisplayName|**Publisher**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publisherid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|publisher|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Model-driven App**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`appmodule_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Model-driven App**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|SystemRequired|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`appmodule_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|
|3|Label: **Deleted**<br />State:1<br />TransitionData: None|

### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|---|---|
|Description|**Unique Name of App Module**|
|DisplayName|**Unique Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`uniquename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_URL"></a> URL

|Property|Value|
|---|---|
|Description|**Contains URL**|
|DisplayName|**URL**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`url`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_WebResourceId"></a> WebResourceId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Web Resource**|
|DisplayName|**Web Resource Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`webresourceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_WelcomePageId"></a> WelcomePageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Web Resource as Welcome Page Id**|
|DisplayName|**Welcome Page Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`welcomepageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [Descriptor](#BKMK_Descriptor)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only**|
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

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
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
|Description|**Date and time when the record was created.**|
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
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_Descriptor"></a> Descriptor

|Property|Value|
|---|---|
|Description|**App Module Descriptor**|
|DisplayName|**Descriptor**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`descriptor`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Is Managed**|
|DisplayName|**IsManaged**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
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
|Description|**Date and time when the record was modified.**|
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
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the app.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**Internal use only**|
|DisplayName|**Overwrite Time**|
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

- [lk_appmodule_createdby](#BKMK_lk_appmodule_createdby)
- [lk_appmodule_createdonbehalfby](#BKMK_lk_appmodule_createdonbehalfby)
- [lk_appmodule_modifiedby](#BKMK_lk_appmodule_modifiedby)
- [lk_appmodule_modifiedonbehalfby](#BKMK_lk_appmodule_modifiedonbehalfby)
- [organization_appmodule](#BKMK_organization_appmodule)
- [publisher_appmodule](#BKMK_publisher_appmodule)

### <a name="BKMK_lk_appmodule_createdby"></a> lk_appmodule_createdby

One-To-Many Relationship: [systemuser lk_appmodule_createdby](systemuser.md#BKMK_lk_appmodule_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`appmodule_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appmodule_createdonbehalfby"></a> lk_appmodule_createdonbehalfby

One-To-Many Relationship: [systemuser lk_appmodule_createdonbehalfby](systemuser.md#BKMK_lk_appmodule_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`appmodule_createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appmodule_modifiedby"></a> lk_appmodule_modifiedby

One-To-Many Relationship: [systemuser lk_appmodule_modifiedby](systemuser.md#BKMK_lk_appmodule_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`appmodule_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_appmodule_modifiedonbehalfby"></a> lk_appmodule_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_appmodule_modifiedonbehalfby](systemuser.md#BKMK_lk_appmodule_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`appmodule_modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_appmodule"></a> organization_appmodule

One-To-Many Relationship: [organization organization_appmodule](organization.md#BKMK_organization_appmodule)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organization_appmodule_appmodule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_publisher_appmodule"></a> publisher_appmodule

One-To-Many Relationship: [publisher publisher_appmodule](publisher.md#BKMK_publisher_appmodule)

|Property|Value|
|---|---|
|ReferencedEntity|`publisher`|
|ReferencedAttribute|`publisherid`|
|ReferencingAttribute|`publisherid`|
|ReferencingEntityNavigationPropertyName|`publisher_appmodule_appmodule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [appmodule_appaction_appmoduleid](#BKMK_appmodule_appaction_appmoduleid)
- [appmodule_appconfig](#BKMK_appmodule_appconfig)
- [appmodule_appmodulecomponent](#BKMK_appmodule_appmodulecomponent)
- [appmodule_appnotification_app](#BKMK_appmodule_appnotification_app)
- [appmodule_userrating_app](#BKMK_appmodule_userrating_app)

### <a name="BKMK_appmodule_appaction_appmoduleid"></a> appmodule_appaction_appmoduleid

Many-To-One Relationship: [appaction appmodule_appaction_appmoduleid](appaction.md#BKMK_appmodule_appaction_appmoduleid)

|Property|Value|
|---|---|
|ReferencingEntity|`appaction`|
|ReferencingAttribute|`appmoduleid`|
|ReferencedEntityNavigationPropertyName|`appmodule_appaction_appmoduleid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appmodule_appconfig"></a> appmodule_appconfig

Many-To-One Relationship: [appconfig appmodule_appconfig](appconfig.md#BKMK_appmodule_appconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`appconfig`|
|ReferencingAttribute|`appmoduleid`|
|ReferencedEntityNavigationPropertyName|`appmodule_appconfig`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appmodule_appmodulecomponent"></a> appmodule_appmodulecomponent

Many-To-One Relationship: [appmodulecomponent appmodule_appmodulecomponent](appmodulecomponent.md#BKMK_appmodule_appmodulecomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`appmodulecomponent`|
|ReferencingAttribute|`appmoduleidunique`|
|ReferencedEntityNavigationPropertyName|`appmodule_appmodulecomponent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appmodule_appnotification_app"></a> appmodule_appnotification_app

Many-To-One Relationship: [appnotification appmodule_appnotification_app](appnotification.md#BKMK_appmodule_appnotification_app)

|Property|Value|
|---|---|
|ReferencingEntity|`appnotification`|
|ReferencingAttribute|`appmoduleid`|
|ReferencedEntityNavigationPropertyName|`appmodule_appnotification_app`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appmodule_userrating_app"></a> appmodule_userrating_app

Many-To-One Relationship: [userrating appmodule_userrating_app](userrating.md#BKMK_appmodule_userrating_app)

|Property|Value|
|---|---|
|ReferencingEntity|`userrating`|
|ReferencingAttribute|`appmoduleid`|
|ReferencedEntityNavigationPropertyName|`appmodule_userrating_app`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [appmoduleroles_association](#BKMK_appmoduleroles_association)
- [serviceplan_appmodule](#BKMK_serviceplan_appmodule)

### <a name="BKMK_appmoduleroles_association"></a> appmoduleroles_association

See [role appmoduleroles_association Many-To-Many Relationship](role.md#BKMK_appmoduleroles_association)

|Property|Value|
|---|---|
|IntersectEntityName|`appmoduleroles`|
|IsCustomizable|False|
|SchemaName|`appmoduleroles_association`|
|IntersectAttribute|`appmoduleid`|
|NavigationPropertyName|`appmoduleroles_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_serviceplan_appmodule"></a> serviceplan_appmodule

See [serviceplan serviceplan_appmodule Many-To-Many Relationship](serviceplan.md#BKMK_serviceplan_appmodule)

|Property|Value|
|---|---|
|IntersectEntityName|`serviceplanappmodules`|
|IsCustomizable|False|
|SchemaName|`serviceplan_appmodule`|
|IntersectAttribute|`appmoduleid`|
|NavigationPropertyName|`serviceplan_appmodule_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.appmodule?displayProperty=fullName>
