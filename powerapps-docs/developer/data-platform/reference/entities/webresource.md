---
title: "Web Resource (WebResource) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Web Resource (WebResource) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Web Resource (WebResource) table/entity reference (Microsoft Dataverse)

Data equivalent to files used in Web development. Web resources provide client-side components that are used to provide custom user interface elements.

## Messages

The following table lists the messages for the Web Resource (WebResource) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /webresourceset<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /webresourceset(*webresourceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /webresourceset(*webresourceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /webresourceset<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveUnpublished`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `Update`<br />Event: True |`PATCH` /webresourceset(*webresourceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /webresourceset(*webresourceid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Web Resource (WebResource) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Web Resource** |
| **DisplayCollectionName** | **Web Resources** |
| **SchemaName** | `WebResource` |
| **CollectionSchemaName** | `WebResources` |
| **EntitySetName** | `webresourceset`|
| **LogicalName** | `webresource` |
| **LogicalCollectionName** | `webresources` |
| **PrimaryIdAttribute** | `webresourceid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CanBeDeleted](#BKMK_CanBeDeleted)
- [Content](#BKMK_Content)
- [ContentJson](#BKMK_ContentJson)
- [DependencyXml](#BKMK_DependencyXml)
- [Description](#BKMK_Description)
- [DisplayName](#BKMK_DisplayName)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsAvailableForMobileOffline](#BKMK_IsAvailableForMobileOffline)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsEnabledForMobileClient](#BKMK_IsEnabledForMobileClient)
- [IsHidden](#BKMK_IsHidden)
- [LanguageCode](#BKMK_LanguageCode)
- [Name](#BKMK_Name)
- [SilverlightVersion](#BKMK_SilverlightVersion)
- [WebResourceId](#BKMK_WebResourceId)
- [WebResourceType](#BKMK_WebResourceType)

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

### <a name="BKMK_Content"></a> Content

|Property|Value|
|---|---|
|Description|**Bytes of the web resource, in Base64 format.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`content`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ContentJson"></a> ContentJson

|Property|Value|
|---|---|
|Description|**Json representation of the content of the resource.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`contentjson`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_DependencyXml"></a> DependencyXml

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**DependencyXML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`dependencyxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the web resource.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|2000|

### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|---|---|
|Description|**Display name of the web resource.**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`displayname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|200|

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

### <a name="BKMK_IsAvailableForMobileOffline"></a> IsAvailableForMobileOffline

|Property|Value|
|---|---|
|Description|**Information that specifies whether this web resource is available for mobile client in offline mode.**|
|DisplayName|**Is Available For Mobile Offline**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isavailableformobileoffline`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`webresource_isavailableformobileoffline`|
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

### <a name="BKMK_IsEnabledForMobileClient"></a> IsEnabledForMobileClient

|Property|Value|
|---|---|
|Description|**Information that specifies whether this web resource is enabled for mobile client.**|
|DisplayName|**Is Enabled For Mobile Client**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isenabledformobileclient`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`webresource_isenabledformobileclient`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsHidden"></a> IsHidden

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component should be hidden.**|
|DisplayName|**Hidden**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ishidden`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_LanguageCode"></a> LanguageCode

|Property|Value|
|---|---|
|Description|**Language of the web resource.**|
|DisplayName|**Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`languagecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the web resource.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SilverlightVersion"></a> SilverlightVersion

|Property|Value|
|---|---|
|Description|**Silverlight runtime version number required by a silverlight web resource.**|
|DisplayName|**Silverlight Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`silverlightversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|20|

### <a name="BKMK_WebResourceId"></a> WebResourceId

|Property|Value|
|---|---|
|Description|**Unique identifier of the web resource.**|
|DisplayName|**Web Resource Identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`webresourceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_WebResourceType"></a> WebResourceType

|Property|Value|
|---|---|
|Description|**Drop-down list for selecting the type of the web resource.**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`webresourcetype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`webresource_webresourcetype`|

#### WebResourceType Choices/Options

|Value|Label|
|---|---|
|1|**Webpage (HTML)**|
|2|**Style Sheet (CSS)**|
|3|**Script (JScript)**|
|4|**Data (XML)**|
|5|**PNG format**|
|6|**JPG format**|
|7|**GIF format**|
|8|**Silverlight (XAP)**|
|9|**Style Sheet (XSL)**|
|10|**ICO format**|
|11|**Vector format (SVG)**|
|12|**String (RESX)**|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [ContentFileRef](#BKMK_ContentFileRef)
- [ContentFileRef_Name](#BKMK_ContentFileRef_Name)
- [ContentJsonFileRef](#BKMK_ContentJsonFileRef)
- [ContentJsonFileRef_Name](#BKMK_ContentJsonFileRef_Name)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)
- [WebResourceIdUnique](#BKMK_WebResourceIdUnique)

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

### <a name="BKMK_ContentFileRef"></a> ContentFileRef

|Property|Value|
|---|---|
|Description|**Reference to the content file on Azure.**|
|DisplayName|**ContentFileRef**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contentfileref`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|10485760|

### <a name="BKMK_ContentFileRef_Name"></a> ContentFileRef_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`contentfileref_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ContentJsonFileRef"></a> ContentJsonFileRef

|Property|Value|
|---|---|
|Description|**Reference to the Json content file on Azure.**|
|DisplayName|**ContentJsonFileRef**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contentjsonfileref`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|10485760|

### <a name="BKMK_ContentJsonFileRef_Name"></a> ContentJsonFileRef_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`contentjsonfileref_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the web resource.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the web resource was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
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
|Description|**Unique identifier of the delegate user who created the web resource.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the web resource.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the web resource was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
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
|Description|**Unique identifier of the delegate user who modified the web resource.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the web resource.**|
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

### <a name="BKMK_WebResourceIdUnique"></a> WebResourceIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`webresourceidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [FileAttachment_WebResource_ContentFileRef](#BKMK_FileAttachment_WebResource_ContentFileRef)
- [FileAttachment_WebResource_ContentJsonFileRef](#BKMK_FileAttachment_WebResource_ContentJsonFileRef)
- [lk_webresourcebase_createdonbehalfby](#BKMK_lk_webresourcebase_createdonbehalfby)
- [lk_webresourcebase_modifiedonbehalfby](#BKMK_lk_webresourcebase_modifiedonbehalfby)
- [webresource_createdby](#BKMK_webresource_createdby)
- [webresource_modifiedby](#BKMK_webresource_modifiedby)
- [webresource_organization](#BKMK_webresource_organization)

### <a name="BKMK_FileAttachment_WebResource_ContentFileRef"></a> FileAttachment_WebResource_ContentFileRef

One-To-Many Relationship: [fileattachment FileAttachment_WebResource_ContentFileRef](fileattachment.md#BKMK_FileAttachment_WebResource_ContentFileRef)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`contentfileref`|
|ReferencingEntityNavigationPropertyName|`ContentFileRef`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_WebResource_ContentJsonFileRef"></a> FileAttachment_WebResource_ContentJsonFileRef

One-To-Many Relationship: [fileattachment FileAttachment_WebResource_ContentJsonFileRef](fileattachment.md#BKMK_FileAttachment_WebResource_ContentJsonFileRef)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`contentjsonfileref`|
|ReferencingEntityNavigationPropertyName|`ContentJsonFileRef`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_webresourcebase_createdonbehalfby"></a> lk_webresourcebase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_webresourcebase_createdonbehalfby](systemuser.md#BKMK_lk_webresourcebase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_webresourcebase_modifiedonbehalfby"></a> lk_webresourcebase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_webresourcebase_modifiedonbehalfby](systemuser.md#BKMK_lk_webresourcebase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_webresource_createdby"></a> webresource_createdby

One-To-Many Relationship: [systemuser webresource_createdby](systemuser.md#BKMK_webresource_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_webresource_modifiedby"></a> webresource_modifiedby

One-To-Many Relationship: [systemuser webresource_modifiedby](systemuser.md#BKMK_webresource_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_webresource_organization"></a> webresource_organization

One-To-Many Relationship: [organization webresource_organization](organization.md#BKMK_webresource_organization)

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

- [lk_theme_logoid](#BKMK_lk_theme_logoid)
- [solution_configuration_webresource](#BKMK_solution_configuration_webresource)
- [webresource_appaction_iconwebresourceid](#BKMK_webresource_appaction_iconwebresourceid)
- [webresource_appaction_onclickeventjavascriptwebresourceid](#BKMK_webresource_appaction_onclickeventjavascriptwebresourceid)
- [webresource_FileAttachments](#BKMK_webresource_FileAttachments)
- [webresource_savedqueryvisualizations](#BKMK_webresource_savedqueryvisualizations)
- [webresource_userqueryvisualizations](#BKMK_webresource_userqueryvisualizations)

### <a name="BKMK_lk_theme_logoid"></a> lk_theme_logoid

Many-To-One Relationship: [theme lk_theme_logoid](theme.md#BKMK_lk_theme_logoid)

|Property|Value|
|---|---|
|ReferencingEntity|`theme`|
|ReferencingAttribute|`logoid`|
|ReferencedEntityNavigationPropertyName|`lk_theme_logoid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solution_configuration_webresource"></a> solution_configuration_webresource

Many-To-One Relationship: [solution solution_configuration_webresource](solution.md#BKMK_solution_configuration_webresource)

|Property|Value|
|---|---|
|ReferencingEntity|`solution`|
|ReferencingAttribute|`configurationpageid`|
|ReferencedEntityNavigationPropertyName|`solution_configuration_webresource`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_webresource_appaction_iconwebresourceid"></a> webresource_appaction_iconwebresourceid

Many-To-One Relationship: [appaction webresource_appaction_iconwebresourceid](appaction.md#BKMK_webresource_appaction_iconwebresourceid)

|Property|Value|
|---|---|
|ReferencingEntity|`appaction`|
|ReferencingAttribute|`iconwebresourceid`|
|ReferencedEntityNavigationPropertyName|`webresource_appaction_iconwebresourceid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_webresource_appaction_onclickeventjavascriptwebresourceid"></a> webresource_appaction_onclickeventjavascriptwebresourceid

Many-To-One Relationship: [appaction webresource_appaction_onclickeventjavascriptwebresourceid](appaction.md#BKMK_webresource_appaction_onclickeventjavascriptwebresourceid)

|Property|Value|
|---|---|
|ReferencingEntity|`appaction`|
|ReferencingAttribute|`onclickeventjavascriptwebresourceid`|
|ReferencedEntityNavigationPropertyName|`webresource_appaction_onclickeventjavascriptwebresourceid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_webresource_FileAttachments"></a> webresource_FileAttachments

Many-To-One Relationship: [fileattachment webresource_FileAttachments](fileattachment.md#BKMK_webresource_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`webresource_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_webresource_savedqueryvisualizations"></a> webresource_savedqueryvisualizations

Many-To-One Relationship: [savedqueryvisualization webresource_savedqueryvisualizations](savedqueryvisualization.md#BKMK_webresource_savedqueryvisualizations)

|Property|Value|
|---|---|
|ReferencingEntity|`savedqueryvisualization`|
|ReferencingAttribute|`webresourceid`|
|ReferencedEntityNavigationPropertyName|`webresource_savedqueryvisualizations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_webresource_userqueryvisualizations"></a> webresource_userqueryvisualizations

Many-To-One Relationship: [userqueryvisualization webresource_userqueryvisualizations](userqueryvisualization.md#BKMK_webresource_userqueryvisualizations)

|Property|Value|
|---|---|
|ReferencingEntity|`userqueryvisualization`|
|ReferencingAttribute|`webresourceid`|
|ReferencedEntityNavigationPropertyName|`webresource_userqueryvisualizations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_appactionrule_webresource_scripts"></a> appactionrule_webresource_scripts

See [appactionrule appactionrule_webresource_scripts Many-To-Many Relationship](appactionrule.md#BKMK_appactionrule_webresource_scripts)

|Property|Value|
|---|---|
|IntersectEntityName|`appactionrule_webresource_scripts`|
|IsCustomizable|False|
|SchemaName|`appactionrule_webresource_scripts`|
|IntersectAttribute|`webresourceid`|
|NavigationPropertyName|`appactionrule_webresource_scripts`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.webresource?displayProperty=fullName>
