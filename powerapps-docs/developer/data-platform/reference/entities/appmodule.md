---
title: "Model-driven App (AppModule) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Model-driven App (AppModule) table/entity."
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

# Model-driven App (AppModule) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

A role-based, modular business app that provides task-based functionality for a particular area of work.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|AddAppComponents|<xref href="Microsoft.Dynamics.CRM.AddAppComponents?text=AddAppComponents Action" />|<xref:Microsoft.Crm.Sdk.Messages.AddAppComponentsRequest>|
|Create|POST [*org URI*]/api/data/v9.0/appmodules<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/appmodules(*appmoduleid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|RemoveAppComponents|<xref href="Microsoft.Dynamics.CRM.RemoveAppComponents?text=RemoveAppComponents Action" />|<xref:Microsoft.Crm.Sdk.Messages.RemoveAppComponentsRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/appmodules(*appmoduleid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveAppComponents|<xref href="Microsoft.Dynamics.CRM.RetrieveAppComponents?text=RetrieveAppComponents Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAppComponentsRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/appmodules<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrieveUnpublished|<xref href="Microsoft.Dynamics.CRM.RetrieveUnpublished?text=RetrieveUnpublished Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
|RetrieveUnpublishedMultiple|<xref href="Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?text=RetrieveUnpublishedMultiple Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/appmodules(*appmoduleid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|ValidateApp|<xref href="Microsoft.Dynamics.CRM.ValidateApp?text=ValidateApp Function" />|<xref:Microsoft.Crm.Sdk.Messages.ValidateAppRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|AppModules|
|DisplayCollectionName|Model-driven Apps|
|DisplayName|Model-driven App|
|EntitySetName|appmodules|
|IsBPFEntity|False|
|LogicalCollectionName|appmodules|
|LogicalName|appmodule|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|appmoduleid|
|PrimaryNameAttribute|name|
|SchemaName|AppModule|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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


### <a name="BKMK_AppModuleId"></a> AppModuleId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|AppModuleId|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appmoduleid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_AppModuleIdUnique"></a> AppModuleIdUnique

|Property|Value|
|--------|-----|
|Description|Unique identifier of the App Module used when synchronizing customizations for the Microsoft Dynamics 365 client for Outlook|
|DisplayName|App Module Unique Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|appmoduleidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_AppModuleVersion"></a> AppModuleVersion

|Property|Value|
|--------|-----|
|Description|App Module Version|
|DisplayName|App Module Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appmoduleversion|
|MaxLength|48|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AppModuleXmlManaged"></a> AppModuleXmlManaged

|Property|Value|
|--------|-----|
|Description|App Module Xml Managed|
|DisplayName||
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|appmodulexmlmanaged|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ClientType"></a> ClientType

|Property|Value|
|--------|-----|
|Description|Client Type such as Web or UCI|
|DisplayName|Client Type|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|clienttype|
|MaxValue|31|
|MinValue|1|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_ConfigXML"></a> ConfigXML

|Property|Value|
|--------|-----|
|Description|Contains configuration XML|
|DisplayName||
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|configxml|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description for entity|
|DisplayName|Description|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EventHandlers"></a> EventHandlers

|Property|Value|
|--------|-----|
|Description|App Module Event Handlers|
|DisplayName|Event Handlers|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|eventhandlers|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FormFactor"></a> FormFactor

|Property|Value|
|--------|-----|
|Description|Form Factor|
|DisplayName|Form Factor|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|formfactor|
|MaxValue|8|
|MinValue|1|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Unique identifier of the data import or data migration that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the similarity rule is introduced.|
|DisplayName|Introduced Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|introducedversion|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|--------|-----|
|Description|Is Default|
|DisplayName|Is Default|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isdefault|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|

#### IsDefault Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsFeatured"></a> IsFeatured

|Property|Value|
|--------|-----|
|Description|Is Featured|
|DisplayName|IsFeatured|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isfeatured|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsFeatured Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of App Module|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_NavigationType"></a> NavigationType

|Property|Value|
|--------|-----|
|Description|App navigation type|
|DisplayName|Navigation type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|navigationtype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### NavigationType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Single session||
|1|Multi session||



### <a name="BKMK_OptimizedFor"></a> OptimizedFor

|Property|Value|
|--------|-----|
|Description|The client that this app is optimized for|
|DisplayName|Optimized Client|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|optimizedfor|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_PublishedOn"></a> PublishedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was published.|
|DisplayName|Published On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|publishedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_PublisherId"></a> PublisherId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the publisher.|
|DisplayName|Publisher|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|publisherid|
|RequiredLevel|ApplicationRequired|
|Targets|publisher|
|Type|Lookup|


### <a name="BKMK_statecode"></a> statecode

**Added by**: App Module Metadata Solution

|Property|Value|
|--------|-----|
|Description|Status of the Model-driven App|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

**Added by**: App Module Metadata Solution

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Model-driven App|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|SystemRequired|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|
|3|Deleted|1|



### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|--------|-----|
|Description|Unique Name of App Module|
|DisplayName|Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|uniquename|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_URL"></a> URL

|Property|Value|
|--------|-----|
|Description|Contains URL|
|DisplayName|URL|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|url|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_WebResourceId"></a> WebResourceId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Web Resource|
|DisplayName|Web Resource Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|webresourceid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_WelcomePageId"></a> WelcomePageId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Web Resource as Welcome Page Id|
|DisplayName|Welcome Page Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|welcomepageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [Descriptor](#BKMK_Descriptor)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PublisherIdName](#BKMK_PublisherIdName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|--------|-----|
|Description|For internal use only|
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
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|False|
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
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
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
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|False|
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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_Descriptor"></a> Descriptor

|Property|Value|
|--------|-----|
|Description|App Module Descriptor|
|DisplayName|Descriptor|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|descriptor|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|Is Managed|
|DisplayName|IsManaged|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|ApplicationRequired|
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
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|False|
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
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was modified.|
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
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the app.|
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
|Description|Internal use only|
|DisplayName|Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_PublisherIdName"></a> PublisherIdName

|Property|Value|
|--------|-----|
|Description|name of the publisher.|
|DisplayName|Publisher|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|publisheridname|
|MaxLength|100|
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

- [appmodule_appconfig](#BKMK_appmodule_appconfig)
- [appmodule_appmodulecomponent](#BKMK_appmodule_appmodulecomponent)
- [appmodule_appnotification_app](#BKMK_appmodule_appnotification_app)
- [appmodule_appaction_appmoduleid](#BKMK_appmodule_appaction_appmoduleid)


### <a name="BKMK_appmodule_appconfig"></a> appmodule_appconfig

Same as appconfig table [appmodule_appconfig](appconfig.md#BKMK_appmodule_appconfig) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appconfig|
|ReferencingAttribute|appmoduleid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|appmodule_appconfig|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appmodule_appmodulecomponent"></a> appmodule_appmodulecomponent

Same as appmodulecomponent table [appmodule_appmodulecomponent](appmodulecomponent.md#BKMK_appmodule_appmodulecomponent) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appmodulecomponent|
|ReferencingAttribute|appmoduleidunique|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|appmodule_appmodulecomponent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_appmodule_appnotification_app"></a> appmodule_appnotification_app

**Added by**: AppNotifications Solution

Same as appnotification table [appmodule_appnotification_app](appnotification.md#BKMK_appmodule_appnotification_app) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appnotification|
|ReferencingAttribute|appmoduleid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|appmodule_appnotification_app|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_appmodule_appaction_appmoduleid"></a> appmodule_appaction_appmoduleid

**Added by**: Power Apps Actions Solution

Same as appaction table [appmodule_appaction_appmoduleid](appaction.md#BKMK_appmodule_appaction_appmoduleid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appaction|
|ReferencingAttribute|appmoduleid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|appmodule_appaction_appmoduleid|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [organization_appmodule](#BKMK_organization_appmodule)
- [lk_appmodule_modifiedby](#BKMK_lk_appmodule_modifiedby)
- [publisher_appmodule](#BKMK_publisher_appmodule)
- [lk_appmodule_modifiedonbehalfby](#BKMK_lk_appmodule_modifiedonbehalfby)
- [lk_appmodule_createdby](#BKMK_lk_appmodule_createdby)
- [lk_appmodule_createdonbehalfby](#BKMK_lk_appmodule_createdonbehalfby)


### <a name="BKMK_organization_appmodule"></a> organization_appmodule

See organization Table [organization_appmodule](organization.md#BKMK_organization_appmodule) One-To-Many relationship.

### <a name="BKMK_lk_appmodule_modifiedby"></a> lk_appmodule_modifiedby

See systemuser Table [lk_appmodule_modifiedby](systemuser.md#BKMK_lk_appmodule_modifiedby) One-To-Many relationship.

### <a name="BKMK_publisher_appmodule"></a> publisher_appmodule

See publisher Table [publisher_appmodule](publisher.md#BKMK_publisher_appmodule) One-To-Many relationship.

### <a name="BKMK_lk_appmodule_modifiedonbehalfby"></a> lk_appmodule_modifiedonbehalfby

See systemuser Table [lk_appmodule_modifiedonbehalfby](systemuser.md#BKMK_lk_appmodule_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_appmodule_createdby"></a> lk_appmodule_createdby

See systemuser Table [lk_appmodule_createdby](systemuser.md#BKMK_lk_appmodule_createdby) One-To-Many relationship.

### <a name="BKMK_lk_appmodule_createdonbehalfby"></a> lk_appmodule_createdonbehalfby

See systemuser Table [lk_appmodule_createdonbehalfby](systemuser.md#BKMK_lk_appmodule_createdonbehalfby) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the AppModule table is the first table in the relationship. Listed by **SchemaName**.

- [appmoduleroles_association](#BKMK_appmoduleroles_association)
- [serviceplan_appmodule](#BKMK_serviceplan_appmodule)


### <a name="BKMK_appmoduleroles_association"></a> appmoduleroles_association

IntersectEntityName: appmoduleroles<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|appmoduleid|
|IsCustomizable|False|
|LogicalName|appmodule|
|NavigationPropertyName|appmoduleroles_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|role|
|IntersectAttribute|roleid|
|NavigationPropertyName|appmoduleroles_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |


### <a name="BKMK_serviceplan_appmodule"></a> serviceplan_appmodule

See serviceplan Table [serviceplan_appmodule](serviceplan.md#BKMK_serviceplan_appmodule) Many-To-Many Relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.appmodule?text=appmodule EntityType" />