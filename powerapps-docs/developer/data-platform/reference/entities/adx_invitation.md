---
title: "Invitation (adx_invitation)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Invitation (adx_invitation)  table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Invitation (adx_invitation)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Send invitations to existing contacts or email addresses and assign them to web roles upon redemption.

**Added by**: Power Pages Runtime Core Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /adx_invitations(*adx_invitationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /adx_invitations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /adx_invitations(*adx_invitationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Restore||Use <xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/>where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName> = Restore|
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /adx_invitations(*adx_invitationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /adx_invitations<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /adx_invitations(*adx_invitationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /adx_invitations(*adx_invitationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|adx_invitations|
|DisplayCollectionName|Invitations|
|DisplayName|Invitation|
|EntitySetName|adx_invitations|
|IsBPFEntity|False|
|LogicalCollectionName|adx_invitations|
|LogicalName|adx_invitation|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|adx_invitationid|
|PrimaryNameAttribute|adx_name|
|SchemaName|adx_invitation|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [adx_assignToAccount](#BKMK_adx_assignToAccount)
- [adx_expiryDate](#BKMK_adx_expiryDate)
- [adx_invitationCode](#BKMK_adx_invitationCode)
- [adx_invitationId](#BKMK_adx_invitationId)
- [adx_inviteContact](#BKMK_adx_inviteContact)
- [adx_invitercontact](#BKMK_adx_invitercontact)
- [adx_maximumRedemptions](#BKMK_adx_maximumRedemptions)
- [adx_name](#BKMK_adx_name)
- [adx_redeemedContact](#BKMK_adx_redeemedContact)
- [adx_redemptions](#BKMK_adx_redemptions)
- [adx_redemptionWorkflow](#BKMK_adx_redemptionWorkflow)
- [adx_type](#BKMK_adx_type)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_adx_assignToAccount"></a> adx_assignToAccount

|Property|Value|
|--------|-----|
|Description|An account record to assign the redeemed contact to.|
|DisplayName|Assign To Account|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_assigntoaccount|
|RequiredLevel|None|
|Targets|account|
|Type|Lookup|


### <a name="BKMK_adx_expiryDate"></a> adx_expiryDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|The date the invitation is no longer valid for redemption.|
|DisplayName|Expiry Date|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_expirydate|
|RequiredLevel|Recommended|
|Type|DateTime|


### <a name="BKMK_adx_invitationCode"></a> adx_invitationCode

|Property|Value|
|--------|-----|
|Description|Shows the user who is redeeming the invitation.|
|DisplayName|Invitation Code|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_invitationcode|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_invitationId"></a> adx_invitationId

|Property|Value|
|--------|-----|
|Description|Shows the entity instance.|
|DisplayName|Invitation|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|adx_invitationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_adx_inviteContact"></a> adx_inviteContact

|Property|Value|
|--------|-----|
|Description|The contact to send an invitation to.|
|DisplayName|Invite Contact|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_invitecontact|
|RequiredLevel|None|
|Targets|contact|
|Type|Lookup|


### <a name="BKMK_adx_invitercontact"></a> adx_invitercontact

|Property|Value|
|--------|-----|
|Description|The contact that invited.|
|DisplayName|Inviter|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_invitercontact|
|RequiredLevel|None|
|Targets|contact|
|Type|Lookup|


### <a name="BKMK_adx_maximumRedemptions"></a> adx_maximumRedemptions

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Maximum Redemptions|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_maximumredemptions|
|MaxValue|2147483647|
|MinValue|1|
|RequiredLevel|None|
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
|MaxLength|200|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_adx_redeemedContact"></a> adx_redeemedContact

|Property|Value|
|--------|-----|
|Description|The contact associated with the redemption of this invitation.|
|DisplayName|Redeemed Contact|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_redeemedcontact|
|RequiredLevel|None|
|Targets|contact|
|Type|Lookup|


### <a name="BKMK_adx_redemptions"></a> adx_redemptions

|Property|Value|
|--------|-----|
|Description|The current number of times this invitation has been redeemed.|
|DisplayName|Redemptions|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_redemptions|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_adx_redemptionWorkflow"></a> adx_redemptionWorkflow

|Property|Value|
|--------|-----|
|Description|A workflow to execute on the redeeming contact.|
|DisplayName|Redemption Workflow|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_redemptionworkflow|
|RequiredLevel|None|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_adx_type"></a> adx_type

|Property|Value|
|--------|-----|
|Description|The type of invitation.|
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|adx_type|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### adx_type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|756150000|Single||
|756150001|Group||



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


### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

**Added by**: Power Pages Runtime Extensions Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Website|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mspp_websiteid|
|RequiredLevel|None|
|Targets|powerpagesite|
|Type|Lookup|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OwnerId"></a> OwnerId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Enter the user who is assigned to manage the record. This field is updated every time the record is assigned to a different user.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Invitation|
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
|Description|Select the invitation's status.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|New|0|
|2|Inactive|1|
|756150000|Sent|0|
|756150001|Redeemed|0|



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

- [adx_assignToAccountName](#BKMK_adx_assignToAccountName)
- [adx_assignToAccountYomiName](#BKMK_adx_assignToAccountYomiName)
- [adx_inviteContactName](#BKMK_adx_inviteContactName)
- [adx_inviteContactYomiName](#BKMK_adx_inviteContactYomiName)
- [adx_invitercontactName](#BKMK_adx_invitercontactName)
- [adx_invitercontactYomiName](#BKMK_adx_invitercontactYomiName)
- [adx_redeemedContactName](#BKMK_adx_redeemedContactName)
- [adx_redeemedContactYomiName](#BKMK_adx_redeemedContactYomiName)
- [adx_redemptionWorkflowName](#BKMK_adx_redemptionWorkflowName)
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
- [mspp_websiteidName](#BKMK_mspp_websiteidName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_adx_assignToAccountName"></a> adx_assignToAccountName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_assigntoaccountname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_assignToAccountYomiName"></a> adx_assignToAccountYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_assigntoaccountyominame|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_inviteContactName"></a> adx_inviteContactName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_invitecontactname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_inviteContactYomiName"></a> adx_inviteContactYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_invitecontactyominame|
|MaxLength|450|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_invitercontactName"></a> adx_invitercontactName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_invitercontactname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_invitercontactYomiName"></a> adx_invitercontactYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_invitercontactyominame|
|MaxLength|450|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_redeemedContactName"></a> adx_redeemedContactName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_redeemedcontactname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_redeemedContactYomiName"></a> adx_redeemedContactYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_redeemedcontactyominame|
|MaxLength|450|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_adx_redemptionWorkflowName"></a> adx_redemptionWorkflowName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|adx_redemptionworkflowname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Added by**: Active Solution Solution

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
|Description|Shows the date and time when the record was created.|
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
|Description|Shows who last updated the record.|
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
|Description|Shows the date and time when the record was modified.|
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


### <a name="BKMK_mspp_websiteidName"></a> mspp_websiteidName

**Added by**: Power Pages Runtime Extensions Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mspp_websiteidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Yomi name of the owner|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Shows the business unit that owns the record.|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunitname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


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

- [adx_invitation_ActivityPointers](#BKMK_adx_invitation_ActivityPointers)
- [adx_invitation_chats](#BKMK_adx_invitation_chats)
- [adx_invitation_SyncErrors](#BKMK_adx_invitation_SyncErrors)
- [adx_invitation_DuplicateMatchingRecord](#BKMK_adx_invitation_DuplicateMatchingRecord)
- [adx_invitation_DuplicateBaseRecord](#BKMK_adx_invitation_DuplicateBaseRecord)
- [adx_invitation_AsyncOperations](#BKMK_adx_invitation_AsyncOperations)
- [adx_invitation_MailboxTrackingFolders](#BKMK_adx_invitation_MailboxTrackingFolders)
- [adx_invitation_ProcessSession](#BKMK_adx_invitation_ProcessSession)
- [adx_invitation_BulkDeleteFailures](#BKMK_adx_invitation_BulkDeleteFailures)
- [adx_invitation_PrincipalObjectAttributeAccesses](#BKMK_adx_invitation_PrincipalObjectAttributeAccesses)
- [adx_invitation_Appointments](#BKMK_adx_invitation_Appointments)
- [adx_invitation_Emails](#BKMK_adx_invitation_Emails)
- [adx_invitation_Faxes](#BKMK_adx_invitation_Faxes)
- [adx_invitation_Letters](#BKMK_adx_invitation_Letters)
- [adx_invitation_PhoneCalls](#BKMK_adx_invitation_PhoneCalls)
- [adx_invitation_Tasks](#BKMK_adx_invitation_Tasks)
- [adx_invitation_RecurringAppointmentMasters](#BKMK_adx_invitation_RecurringAppointmentMasters)
- [adx_invitation_SocialActivities](#BKMK_adx_invitation_SocialActivities)
- [adx_invitation_connections1](#BKMK_adx_invitation_connections1)
- [adx_invitation_connections2](#BKMK_adx_invitation_connections2)
- [adx_invitation_Annotations](#BKMK_adx_invitation_Annotations)
- [adx_invitation_adx_inviteredemptions](#BKMK_adx_invitation_adx_inviteredemptions)
- [adx_invitation_adx_portalcomments](#BKMK_adx_invitation_adx_portalcomments)


### <a name="BKMK_adx_invitation_ActivityPointers"></a> adx_invitation_ActivityPointers

**Added by**: System Solution Solution

Same as the [adx_invitation_ActivityPointers](activitypointer.md#BKMK_adx_invitation_ActivityPointers) many-to-one relationship for the [activitypointer](activitypointer.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_ActivityPointers|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_invitation_chats"></a> adx_invitation_chats

**Added by**: Activities Patch Solution

Same as the [adx_invitation_chats](chat.md#BKMK_adx_invitation_chats) many-to-one relationship for the [chat](chat.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|chat|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_chats|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_invitation_SyncErrors"></a> adx_invitation_SyncErrors

**Added by**: System Solution Solution

Same as the [adx_invitation_SyncErrors](syncerror.md#BKMK_adx_invitation_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_invitation_DuplicateMatchingRecord"></a> adx_invitation_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [adx_invitation_DuplicateMatchingRecord](duplicaterecord.md#BKMK_adx_invitation_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_invitation_DuplicateBaseRecord"></a> adx_invitation_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [adx_invitation_DuplicateBaseRecord](duplicaterecord.md#BKMK_adx_invitation_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_invitation_AsyncOperations"></a> adx_invitation_AsyncOperations

**Added by**: System Solution Solution

Same as the [adx_invitation_AsyncOperations](asyncoperation.md#BKMK_adx_invitation_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_invitation_MailboxTrackingFolders"></a> adx_invitation_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [adx_invitation_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_adx_invitation_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_invitation_ProcessSession"></a> adx_invitation_ProcessSession

**Added by**: System Solution Solution

Same as the [adx_invitation_ProcessSession](processsession.md#BKMK_adx_invitation_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_invitation_BulkDeleteFailures"></a> adx_invitation_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [adx_invitation_BulkDeleteFailures](bulkdeletefailure.md#BKMK_adx_invitation_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_invitation_PrincipalObjectAttributeAccesses"></a> adx_invitation_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [adx_invitation_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_adx_invitation_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_invitation_Appointments"></a> adx_invitation_Appointments

**Added by**: System Solution Solution

Same as the [adx_invitation_Appointments](appointment.md#BKMK_adx_invitation_Appointments) many-to-one relationship for the [appointment](appointment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_Appointments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_invitation_Emails"></a> adx_invitation_Emails

**Added by**: System Solution Solution

Same as the [adx_invitation_Emails](email.md#BKMK_adx_invitation_Emails) many-to-one relationship for the [email](email.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_Emails|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_invitation_Faxes"></a> adx_invitation_Faxes

**Added by**: System Solution Solution

Same as the [adx_invitation_Faxes](fax.md#BKMK_adx_invitation_Faxes) many-to-one relationship for the [fax](fax.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_Faxes|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_invitation_Letters"></a> adx_invitation_Letters

**Added by**: System Solution Solution

Same as the [adx_invitation_Letters](letter.md#BKMK_adx_invitation_Letters) many-to-one relationship for the [letter](letter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_Letters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_invitation_PhoneCalls"></a> adx_invitation_PhoneCalls

**Added by**: System Solution Solution

Same as the [adx_invitation_PhoneCalls](phonecall.md#BKMK_adx_invitation_PhoneCalls) many-to-one relationship for the [phonecall](phonecall.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_PhoneCalls|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_invitation_Tasks"></a> adx_invitation_Tasks

**Added by**: System Solution Solution

Same as the [adx_invitation_Tasks](task.md#BKMK_adx_invitation_Tasks) many-to-one relationship for the [task](task.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_Tasks|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_invitation_RecurringAppointmentMasters"></a> adx_invitation_RecurringAppointmentMasters

**Added by**: System Solution Solution

Same as the [adx_invitation_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_adx_invitation_RecurringAppointmentMasters) many-to-one relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_RecurringAppointmentMasters|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_invitation_SocialActivities"></a> adx_invitation_SocialActivities

**Added by**: System Solution Solution

Same as the [adx_invitation_SocialActivities](socialactivity.md#BKMK_adx_invitation_SocialActivities) many-to-one relationship for the [socialactivity](socialactivity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_SocialActivities|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_invitation_connections1"></a> adx_invitation_connections1

**Added by**: System Solution Solution

Same as the [adx_invitation_connections1](connection.md#BKMK_adx_invitation_connections1) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_invitation_connections2"></a> adx_invitation_connections2

**Added by**: System Solution Solution

Same as the [adx_invitation_connections2](connection.md#BKMK_adx_invitation_connections2) many-to-one relationship for the [connection](connection.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_adx_invitation_Annotations"></a> adx_invitation_Annotations

**Added by**: System Solution Solution

Same as the [adx_invitation_Annotations](annotation.md#BKMK_adx_invitation_Annotations) many-to-one relationship for the [annotation](annotation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_Annotations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_invitation_adx_inviteredemptions"></a> adx_invitation_adx_inviteredemptions

**Added by**: Active Solution Solution

Same as the [adx_invitation_adx_inviteredemptions](adx_inviteredemption.md#BKMK_adx_invitation_adx_inviteredemptions) many-to-one relationship for the [adx_inviteredemption](adx_inviteredemption.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|adx_inviteredemption|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_adx_inviteredemptions|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_adx_invitation_adx_portalcomments"></a> adx_invitation_adx_portalcomments

**Added by**: Active Solution Solution

Same as the [adx_invitation_adx_portalcomments](adx_portalcomment.md#BKMK_adx_invitation_adx_portalcomments) many-to-one relationship for the [adx_portalcomment](adx_portalcomment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|adx_portalcomment|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|adx_invitation_adx_portalcomments|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_adx_invitation_createdby](#BKMK_lk_adx_invitation_createdby)
- [lk_adx_invitation_createdonbehalfby](#BKMK_lk_adx_invitation_createdonbehalfby)
- [lk_adx_invitation_modifiedby](#BKMK_lk_adx_invitation_modifiedby)
- [lk_adx_invitation_modifiedonbehalfby](#BKMK_lk_adx_invitation_modifiedonbehalfby)
- [user_adx_invitation](#BKMK_user_adx_invitation)
- [team_adx_invitation](#BKMK_team_adx_invitation)
- [business_unit_adx_invitation](#BKMK_business_unit_adx_invitation)
- [adx_invitation_assigntoaccount](#BKMK_adx_invitation_assigntoaccount)
- [adx_invitation_invitecontact](#BKMK_adx_invitation_invitecontact)
- [adx_invitation_invitercontact](#BKMK_adx_invitation_invitercontact)
- [adx_invitation_redeemedContact](#BKMK_adx_invitation_redeemedContact)
- [adx_invitation_redemptionworkflow](#BKMK_adx_invitation_redemptionworkflow)
- [powerpagesite_mspp_websiteid_adx_invitation](#BKMK_powerpagesite_mspp_websiteid_adx_invitation)


### <a name="BKMK_lk_adx_invitation_createdby"></a> lk_adx_invitation_createdby

**Added by**: System Solution Solution

See the [lk_adx_invitation_createdby](systemuser.md#BKMK_lk_adx_invitation_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_adx_invitation_createdonbehalfby"></a> lk_adx_invitation_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_adx_invitation_createdonbehalfby](systemuser.md#BKMK_lk_adx_invitation_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_adx_invitation_modifiedby"></a> lk_adx_invitation_modifiedby

**Added by**: System Solution Solution

See the [lk_adx_invitation_modifiedby](systemuser.md#BKMK_lk_adx_invitation_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_adx_invitation_modifiedonbehalfby"></a> lk_adx_invitation_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_adx_invitation_modifiedonbehalfby](systemuser.md#BKMK_lk_adx_invitation_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_adx_invitation"></a> user_adx_invitation

**Added by**: System Solution Solution

See the [user_adx_invitation](systemuser.md#BKMK_user_adx_invitation) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_adx_invitation"></a> team_adx_invitation

**Added by**: System Solution Solution

See the [team_adx_invitation](team.md#BKMK_team_adx_invitation) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_adx_invitation"></a> business_unit_adx_invitation

**Added by**: System Solution Solution

See the [business_unit_adx_invitation](businessunit.md#BKMK_business_unit_adx_invitation) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_adx_invitation_assigntoaccount"></a> adx_invitation_assigntoaccount

**Added by**: System Solution Solution

See the [adx_invitation_assigntoaccount](account.md#BKMK_adx_invitation_assigntoaccount) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_adx_invitation_invitecontact"></a> adx_invitation_invitecontact

**Added by**: System Solution Solution

See the [adx_invitation_invitecontact](contact.md#BKMK_adx_invitation_invitecontact) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_adx_invitation_invitercontact"></a> adx_invitation_invitercontact

**Added by**: System Solution Solution

See the [adx_invitation_invitercontact](contact.md#BKMK_adx_invitation_invitercontact) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_adx_invitation_redeemedContact"></a> adx_invitation_redeemedContact

**Added by**: System Solution Solution

See the [adx_invitation_redeemedContact](contact.md#BKMK_adx_invitation_redeemedContact) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_adx_invitation_redemptionworkflow"></a> adx_invitation_redemptionworkflow

**Added by**: System Solution Solution

See the [adx_invitation_redemptionworkflow](workflow.md#BKMK_adx_invitation_redemptionworkflow) one-to-many relationship for the [workflow](workflow.md) table/entity.

### <a name="BKMK_powerpagesite_mspp_websiteid_adx_invitation"></a> powerpagesite_mspp_websiteid_adx_invitation

**Added by**: Power Pages Core Base Solution

See the [powerpagesite_mspp_websiteid_adx_invitation](powerpagesite.md#BKMK_powerpagesite_mspp_websiteid_adx_invitation) one-to-many relationship for the [powerpagesite](powerpagesite.md) table/entity.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the adx_invitation table is the first table in the relationship. Listed by **SchemaName**.

- [adx_invitation_invitecontacts](#BKMK_adx_invitation_invitecontacts)
- [adx_invitation_redeemedcontacts](#BKMK_adx_invitation_redeemedcontacts)
- [adx_invitation_mspp_webrole_powerpagecomponent](#BKMK_adx_invitation_mspp_webrole_powerpagecomponent)


### <a name="BKMK_adx_invitation_invitecontacts"></a> adx_invitation_invitecontacts

IntersectEntityName: adx_invitation_invitecontacts<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|adx_invitationid|
|IsCustomizable|True|
|LogicalName|adx_invitation|
|NavigationPropertyName|adx_invitation_invitecontacts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 20000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|contact|
|IntersectAttribute|contactid|
|NavigationPropertyName|adx_invitation_invitecontacts|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Invite Contacts<br />Order: 10000|


### <a name="BKMK_adx_invitation_redeemedcontacts"></a> adx_invitation_redeemedcontacts

IntersectEntityName: adx_invitation_redeemedcontacts<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|adx_invitationid|
|IsCustomizable|True|
|LogicalName|adx_invitation|
|NavigationPropertyName|adx_invitation_redeemedcontacts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: Redeemed Invitations<br />Order: 20000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|contact|
|IntersectAttribute|contactid|
|NavigationPropertyName|adx_invitation_redeemedcontacts|
|AssociatedMenuConfiguration|Behavior: UseLabel<br />Group: Details<br />Label: Redeemed Contacts<br />Order: 10000|


### <a name="BKMK_adx_invitation_mspp_webrole_powerpagecomponent"></a> adx_invitation_mspp_webrole_powerpagecomponent

IntersectEntityName: adx_invitation_mspp_webrole_powerpagecomponent<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|adx_invitationid|
|IsCustomizable|True|
|LogicalName|adx_invitation|
|NavigationPropertyName|adx_invitation_mspp_webrole_powerpagecomponent|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 20000|

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|powerpagecomponent|
|IntersectAttribute|powerpagecomponentid|
|NavigationPropertyName|adx_invitation_mspp_webrole_powerpagecomponent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: Assign To Web Roles<br />Order: 10000|


### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.adx_invitation?text=adx_invitation EntityType" />