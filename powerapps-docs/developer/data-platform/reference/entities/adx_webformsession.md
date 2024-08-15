---
title: "Multistep Form Session (adx_webformsession)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Multistep Form Session (adx_webformsession)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Multistep Form Session (adx_webformsession)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Serves as a mechanism to log the occurrence of an incomplete multistep form entry for a given user so they can return and complete it later.

**Added by**: Power Pages Runtime Core Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /adx_webformsessions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /adx_webformsessions(*adx_webformsessionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Restore||Use <xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/>where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName> = Restore|
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /adx_webformsessions(*adx_webformsessionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /adx_webformsessions<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /adx_webformsessions(*adx_webformsessionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /adx_webformsessions(*adx_webformsessionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|adx_webformsessions|
|DisplayCollectionName|Multistep Form Sessions|
|DisplayName|Multistep Form Session|
|EntitySetName|adx_webformsessions|
|IsBPFEntity|False|
|LogicalCollectionName|adx_webformsessions|
|LogicalName|adx_webformsession|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|adx_webformsessionid|
|PrimaryNameAttribute|adx_name|
|SchemaName|adx_webformsession|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [adx_anonymousidentification](#BKMK_adx_anonymousidentification)
- [adx_contact](#BKMK_adx_contact)
- [adx_currentstepindex](#BKMK_adx_currentstepindex)
- [adx_name](#BKMK_adx_name)
- [adx_primaryrecordentitykeyname](#BKMK_adx_primaryrecordentitykeyname)
- [adx_primaryrecordentitylogicalname](#BKMK_adx_primaryrecordentitylogicalname)
- [adx_primaryrecordid](#BKMK_adx_primaryrecordid)
- [adx_stephistory](#BKMK_adx_stephistory)
- [adx_systemuser](#BKMK_adx_systemuser)
- [adx_userhostaddress](#BKMK_adx_userhostaddress)
- [adx_useridentityname](#BKMK_adx_useridentityname)
- [adx_webformsessionId](#BKMK_adx_webformsessionId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [mspp_webformid](#BKMK_mspp_webformid)
- [mspp_webformstepid](#BKMK_mspp_webformstepid)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_adx_anonymousidentification"></a> adx_anonymousidentification

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Anonymous Identification|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_anonymousidentification|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_contact"></a> adx_contact

|Property|Value|
|--------|-----|
|Description|Unique identifier for Contact associated with Multistep Form Session.|
|DisplayName|Contact|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_contact|
|RequiredLevel|Recommended|
|Targets|contact|
|Type|Lookup|


### <a name="BKMK_adx_currentstepindex"></a> adx_currentstepindex

|Property|Value|
|--------|-----|
|Description|The index of the current step the user last visited.|
|DisplayName|Current Step Index|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_currentstepindex|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|Recommended|
|Type|Integer|


### <a name="BKMK_adx_name"></a> adx_name

|Property|Value|
|--------|-----|
|Description|Type the name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_name|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_primaryrecordentitykeyname"></a> adx_primaryrecordentitykeyname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Primary Record Entity Primary Key Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_primaryrecordentitykeyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_primaryrecordentitylogicalname"></a> adx_primaryrecordentitylogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Primary Record Table name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_primaryrecordentitylogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_primaryrecordid"></a> adx_primaryrecordid

|Property|Value|
|--------|-----|
|Description|Shows the ID of the primary record created by the multistep form.  Used to retrieve the appropriate session record.|
|DisplayName|Primary Record ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_primaryrecordid|
|MaxLength|38|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_stephistory"></a> adx_stephistory

|Property|Value|
|--------|-----|
|Description|History of steps in JSON|
|DisplayName|Step History|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_stephistory|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_adx_systemuser"></a> adx_systemuser

|Property|Value|
|--------|-----|
|Description|Unique identifier for User associated with Multistep Form Session.|
|DisplayName|System User|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_systemuser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_adx_userhostaddress"></a> adx_userhostaddress

|Property|Value|
|--------|-----|
|Description||
|DisplayName|User Host Address|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_userhostaddress|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_useridentityname"></a> adx_useridentityname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|User Identity Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_useridentityname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_webformsessionId"></a> adx_webformsessionId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Multistep Form Session|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|adx_webformsessionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Shows the sequence number of the import that created this record.|
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


### <a name="BKMK_mspp_webformid"></a> mspp_webformid

**Added by**: Power Pages Runtime Extensions Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for Web Form associated with Web Form Session.|
|DisplayName|Multistep Form|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webformid|
|RequiredLevel|None|
|Targets|powerpagecomponent|
|Type|Lookup|


### <a name="BKMK_mspp_webformstepid"></a> mspp_webformstepid

**Added by**: Power Pages Runtime Extensions Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Multistep Form Session|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_webformstepid|
|RequiredLevel|None|
|Targets|powerpagecomponent|
|Type|Lookup|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was migrated. The date and time are displayed in the time zone selected in the solution options.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Shows the status of the multistep form session.|
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

|Property|Value|
|--------|-----|
|Description|Select the Multistep Form Session's status.
|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Shows the time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [adx_contactName](#BKMK_adx_contactName)
- [adx_contactYomiName](#BKMK_adx_contactYomiName)
- [adx_systemuserName](#BKMK_adx_systemuserName)
- [adx_systemuserYomiName](#BKMK_adx_systemuserYomiName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [mspp_webformidName](#BKMK_mspp_webformidName)
- [mspp_webformstepidName](#BKMK_mspp_webformstepidName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_adx_contactName"></a> adx_contactName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_contactname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_contactYomiName"></a> adx_contactYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_contactyominame|
|MaxLength|450|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_systemuserName"></a> adx_systemuserName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_systemusername|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_systemuserYomiName"></a> adx_systemuserYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_systemuseryominame|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Added by**: Active Solution Solution

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


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in the solution options.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Added by**: Active Solution Solution

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


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was updated. The date and time are displayed in the time zone selected in the solution options.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record on behalf of another user.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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


### <a name="BKMK_mspp_webformidName"></a> mspp_webformidName

**Added by**: Power Pages Runtime Extensions Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_webformidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_mspp_webformstepidName"></a> mspp_webformstepidName

**Added by**: Power Pages Runtime Extensions Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_webformstepidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Shows the organization.|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Added by**: Active Solution Solution

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


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version Number|
|DisplayName|Version Number|
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

- [adx_webformsession_SyncErrors](#BKMK_adx_webformsession_SyncErrors)
- [adx_webformsession_AsyncOperations](#BKMK_adx_webformsession_AsyncOperations)
- [adx_webformsession_MailboxTrackingFolders](#BKMK_adx_webformsession_MailboxTrackingFolders)
- [adx_webformsession_ProcessSession](#BKMK_adx_webformsession_ProcessSession)
- [adx_webformsession_BulkDeleteFailures](#BKMK_adx_webformsession_BulkDeleteFailures)
- [adx_webformsession_PrincipalObjectAttributeAccesses](#BKMK_adx_webformsession_PrincipalObjectAttributeAccesses)


### <a name="BKMK_adx_webformsession_SyncErrors"></a> adx_webformsession_SyncErrors

**Added by**: System Solution Solution

Same as the [adx_webformsession_SyncErrors](syncerror.md#BKMK_adx_webformsession_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_webformsession_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_webformsession_AsyncOperations"></a> adx_webformsession_AsyncOperations

**Added by**: System Solution Solution

Same as the [adx_webformsession_AsyncOperations](asyncoperation.md#BKMK_adx_webformsession_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_webformsession_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_webformsession_MailboxTrackingFolders"></a> adx_webformsession_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [adx_webformsession_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_adx_webformsession_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_webformsession_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_webformsession_ProcessSession"></a> adx_webformsession_ProcessSession

**Added by**: System Solution Solution

Same as the [adx_webformsession_ProcessSession](processsession.md#BKMK_adx_webformsession_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_webformsession_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_webformsession_BulkDeleteFailures"></a> adx_webformsession_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [adx_webformsession_BulkDeleteFailures](bulkdeletefailure.md#BKMK_adx_webformsession_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_webformsession_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_webformsession_PrincipalObjectAttributeAccesses"></a> adx_webformsession_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [adx_webformsession_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_adx_webformsession_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_webformsession_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_adx_webformsession_createdby](#BKMK_lk_adx_webformsession_createdby)
- [lk_adx_webformsession_createdonbehalfby](#BKMK_lk_adx_webformsession_createdonbehalfby)
- [lk_adx_webformsession_modifiedby](#BKMK_lk_adx_webformsession_modifiedby)
- [lk_adx_webformsession_modifiedonbehalfby](#BKMK_lk_adx_webformsession_modifiedonbehalfby)
- [organization_adx_webformsession](#BKMK_organization_adx_webformsession)
- [adx_webformsession_contact](#BKMK_adx_webformsession_contact)
- [adx_webformsession_systemuser](#BKMK_adx_webformsession_systemuser)
- [powerpagecomponent_mspp_webformid_adx_webformsession](#BKMK_powerpagecomponent_mspp_webformid_adx_webformsession)
- [powerpagecomponent_mspp_webformstepid_adx_webformsession](#BKMK_powerpagecomponent_mspp_webformstepid_adx_webformsession)


### <a name="BKMK_lk_adx_webformsession_createdby"></a> lk_adx_webformsession_createdby

**Added by**: System Solution Solution

See the [lk_adx_webformsession_createdby](systemuser.md#BKMK_lk_adx_webformsession_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_adx_webformsession_createdonbehalfby"></a> lk_adx_webformsession_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_adx_webformsession_createdonbehalfby](systemuser.md#BKMK_lk_adx_webformsession_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_adx_webformsession_modifiedby"></a> lk_adx_webformsession_modifiedby

**Added by**: System Solution Solution

See the [lk_adx_webformsession_modifiedby](systemuser.md#BKMK_lk_adx_webformsession_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_adx_webformsession_modifiedonbehalfby"></a> lk_adx_webformsession_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_adx_webformsession_modifiedonbehalfby](systemuser.md#BKMK_lk_adx_webformsession_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_organization_adx_webformsession"></a> organization_adx_webformsession

**Added by**: System Solution Solution

See the [organization_adx_webformsession](organization.md#BKMK_organization_adx_webformsession) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_adx_webformsession_contact"></a> adx_webformsession_contact

**Added by**: System Solution Solution

See the [adx_webformsession_contact](contact.md#BKMK_adx_webformsession_contact) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_adx_webformsession_systemuser"></a> adx_webformsession_systemuser

**Added by**: System Solution Solution

See the [adx_webformsession_systemuser](systemuser.md#BKMK_adx_webformsession_systemuser) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_powerpagecomponent_mspp_webformid_adx_webformsession"></a> powerpagecomponent_mspp_webformid_adx_webformsession

**Added by**: Power Pages Core Base Solution

See the [powerpagecomponent_mspp_webformid_adx_webformsession](powerpagecomponent.md#BKMK_powerpagecomponent_mspp_webformid_adx_webformsession) one-to-many relationship for the [powerpagecomponent](powerpagecomponent.md) table/entity.

### <a name="BKMK_powerpagecomponent_mspp_webformstepid_adx_webformsession"></a> powerpagecomponent_mspp_webformstepid_adx_webformsession

**Added by**: Power Pages Core Base Solution

See the [powerpagecomponent_mspp_webformstepid_adx_webformsession](powerpagecomponent.md#BKMK_powerpagecomponent_mspp_webformstepid_adx_webformsession) one-to-many relationship for the [powerpagecomponent](powerpagecomponent.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.adx_webformsession?text=adx_webformsession EntityType" />