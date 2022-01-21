---
title: "WebResource table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the WebResource table/entity."
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

# WebResource table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Data equivalent to files used in Web development. Web resources provide client-side components that are used to provide custom user interface elements.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/webresourceset<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/webresourceset(*webresourceid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/webresourceset(*webresourceid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/webresourceset<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrieveUnpublished|<xref href="Microsoft.Dynamics.CRM.RetrieveUnpublished?text=RetrieveUnpublished Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
|RetrieveUnpublishedMultiple|<xref href="Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?text=RetrieveUnpublishedMultiple Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/webresourceset(*webresourceid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|WebResources|
|DisplayCollectionName|Web Resources|
|DisplayName|Web Resource|
|EntitySetName|webresourceset|
|IsBPFEntity|False|
|LogicalCollectionName|webresources|
|LogicalName|webresource|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|webresourceid|
|PrimaryNameAttribute|name|
|SchemaName|WebResource|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Information that specifies whether this component can be deleted.|
|DisplayName|Can Be Deleted|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canbedeleted|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_Content"></a> Content

|Property|Value|
|--------|-----|
|Description|Bytes of the web resource, in Base64 format.|
|DisplayName||
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|content|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ContentJson"></a> ContentJson

|Property|Value|
|--------|-----|
|Description|Json representation of the content of the resource.|
|DisplayName||
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|contentjson|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_DependencyXml"></a> DependencyXml

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|DependencyXML|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|dependencyxml|
|MaxLength|5000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the web resource.|
|DisplayName|Description|
|Format|TextArea|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_DisplayName"></a> DisplayName

|Property|Value|
|--------|-----|
|Description|Display name of the web resource.|
|DisplayName|Display Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|displayname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_IsAvailableForMobileOffline"></a> IsAvailableForMobileOffline

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this web resource is available for mobile client in offline mode.|
|DisplayName|Is Available For Mobile Offline|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isavailableformobileoffline|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsAvailableForMobileOffline Choices/Options

|Value|Label|Description|
|-----|-----|--------|
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


### <a name="BKMK_IsEnabledForMobileClient"></a> IsEnabledForMobileClient

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this web resource is enabled for mobile client.|
|DisplayName|Is Enabled For Mobile Client|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isenabledformobileclient|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsEnabledForMobileClient Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsHidden"></a> IsHidden

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component should be hidden.|
|DisplayName|Hidden|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ishidden|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_LanguageCode"></a> LanguageCode

|Property|Value|
|--------|-----|
|Description|Language of the web resource.|
|DisplayName|Language|
|Format|Language|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|languagecode|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the web resource.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|name|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_SilverlightVersion"></a> SilverlightVersion

|Property|Value|
|--------|-----|
|Description|Silverlight runtime version number required by a silverlight web resource.|
|DisplayName|Silverlight Version|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|silverlightversion|
|MaxLength|20|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_WebResourceId"></a> WebResourceId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the web resource.|
|DisplayName|Web Resource Identifier|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|webresourceid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_WebResourceType"></a> WebResourceType

|Property|Value|
|--------|-----|
|Description|Drop-down list for selecting the type of the web resource.|
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|webresourcetype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### WebResourceType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Webpage (HTML)||
|2|Style Sheet (CSS)||
|3|Script (JScript)||
|4|Data (XML)||
|5|PNG format||
|6|JPG format||
|7|GIF format||
|8|Silverlight (XAP)||
|9|Style Sheet (XSL)||
|10|ICO format||
|11|Vector format (SVG)||
|12|String (RESX)||


<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [ContentFileRef_Name](#BKMK_ContentFileRef_Name)
- [ContentJsonFileRef_Name](#BKMK_ContentJsonFileRef_Name)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)
- [WebResourceIdUnique](#BKMK_WebResourceIdUnique)


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



### <a name="BKMK_ContentFileRef_Name"></a> ContentFileRef_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|contentfileref_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ContentJsonFileRef_Name"></a> ContentJsonFileRef_Name

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|contentjsonfileref_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the web resource.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the web resource was created.|
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
|Description|Unique identifier of the delegate user who created the web resource.|
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


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
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



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the web resource.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the web resource was last modified.|
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
|Description|Unique identifier of the delegate user who modified the web resource.|
|DisplayName|Created By (Delegate)|
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the web resource.|
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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_WebResourceIdUnique"></a> WebResourceIdUnique

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|webresourceidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [webresource_savedqueryvisualizations](#BKMK_webresource_savedqueryvisualizations)
- [solution_configuration_webresource](#BKMK_solution_configuration_webresource)
- [webresource_userqueryvisualizations](#BKMK_webresource_userqueryvisualizations)
- [lk_theme_logoid](#BKMK_lk_theme_logoid)
- [webresource_appaction_iconwebresourceid](#BKMK_webresource_appaction_iconwebresourceid)
- [webresource_appaction_onclickeventjavascriptwebresourceid](#BKMK_webresource_appaction_onclickeventjavascriptwebresourceid)


### <a name="BKMK_webresource_savedqueryvisualizations"></a> webresource_savedqueryvisualizations

Same as savedqueryvisualization table [webresource_savedqueryvisualizations](savedqueryvisualization.md#BKMK_webresource_savedqueryvisualizations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|savedqueryvisualization|
|ReferencingAttribute|webresourceid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|webresource_savedqueryvisualizations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_solution_configuration_webresource"></a> solution_configuration_webresource

Same as solution table [solution_configuration_webresource](solution.md#BKMK_solution_configuration_webresource) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|solution|
|ReferencingAttribute|configurationpageid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|solution_configuration_webresource|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_webresource_userqueryvisualizations"></a> webresource_userqueryvisualizations

Same as userqueryvisualization table [webresource_userqueryvisualizations](userqueryvisualization.md#BKMK_webresource_userqueryvisualizations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userqueryvisualization|
|ReferencingAttribute|webresourceid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|webresource_userqueryvisualizations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_theme_logoid"></a> lk_theme_logoid

Same as theme table [lk_theme_logoid](theme.md#BKMK_lk_theme_logoid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|theme|
|ReferencingAttribute|logoid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_theme_logoid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_webresource_appaction_iconwebresourceid"></a> webresource_appaction_iconwebresourceid

**Added by**: Power Apps Actions Solution

Same as appaction table [webresource_appaction_iconwebresourceid](appaction.md#BKMK_webresource_appaction_iconwebresourceid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appaction|
|ReferencingAttribute|iconwebresourceid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|webresource_appaction_iconwebresourceid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_webresource_appaction_onclickeventjavascriptwebresourceid"></a> webresource_appaction_onclickeventjavascriptwebresourceid

**Added by**: Power Apps Actions Solution

Same as appaction table [webresource_appaction_onclickeventjavascriptwebresourceid](appaction.md#BKMK_webresource_appaction_onclickeventjavascriptwebresourceid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appaction|
|ReferencingAttribute|onclickeventjavascriptwebresourceid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|webresource_appaction_onclickeventjavascriptwebresourceid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_webresourcebase_modifiedonbehalfby](#BKMK_lk_webresourcebase_modifiedonbehalfby)
- [webresource_createdby](#BKMK_webresource_createdby)
- [lk_webresourcebase_createdonbehalfby](#BKMK_lk_webresourcebase_createdonbehalfby)
- [webresource_modifiedby](#BKMK_webresource_modifiedby)
- [webresource_organization](#BKMK_webresource_organization)


### <a name="BKMK_lk_webresourcebase_modifiedonbehalfby"></a> lk_webresourcebase_modifiedonbehalfby

See systemuser Table [lk_webresourcebase_modifiedonbehalfby](systemuser.md#BKMK_lk_webresourcebase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_webresource_createdby"></a> webresource_createdby

See systemuser Table [webresource_createdby](systemuser.md#BKMK_webresource_createdby) One-To-Many relationship.

### <a name="BKMK_lk_webresourcebase_createdonbehalfby"></a> lk_webresourcebase_createdonbehalfby

See systemuser Table [lk_webresourcebase_createdonbehalfby](systemuser.md#BKMK_lk_webresourcebase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_webresource_modifiedby"></a> webresource_modifiedby

See systemuser Table [webresource_modifiedby](systemuser.md#BKMK_webresource_modifiedby) One-To-Many relationship.

### <a name="BKMK_webresource_organization"></a> webresource_organization

See organization Table [webresource_organization](organization.md#BKMK_webresource_organization) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.webresource?text=webresource EntityType" />