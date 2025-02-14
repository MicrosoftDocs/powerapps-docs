---
title: "Invitation (adx_invitation) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Invitation (adx_invitation) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Invitation (adx_invitation) table/entity reference (Microsoft Dataverse)

Send invitations to existing contacts or email addresses and assign them to web roles upon redemption.

## Messages

The following table lists the messages for the Invitation (adx_invitation) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /adx_invitations(*adx_invitationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /adx_invitations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /adx_invitations(*adx_invitationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /adx_invitations(*adx_invitationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /adx_invitations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /adx_invitations(*adx_invitationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /adx_invitations(*adx_invitationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /adx_invitations(*adx_invitationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Invitation (adx_invitation) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Invitation (adx_invitation) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Invitation** |
| **DisplayCollectionName** | **Invitations** |
| **SchemaName** | `adx_invitation` |
| **CollectionSchemaName** | `adx_invitations` |
| **EntitySetName** | `adx_invitations`|
| **LogicalName** | `adx_invitation` |
| **LogicalCollectionName** | `adx_invitations` |
| **PrimaryIdAttribute** | `adx_invitationid` |
| **PrimaryNameAttribute** |`adx_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

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
|---|---|
|Description|**An account record to assign the redeemed contact to.**|
|DisplayName|**Assign To Account**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_assigntoaccount`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account|

### <a name="BKMK_adx_expiryDate"></a> adx_expiryDate

|Property|Value|
|---|---|
|Description|**The date the invitation is no longer valid for redemption.**|
|DisplayName|**Expiry Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_expirydate`|
|RequiredLevel|Recommended|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_adx_invitationCode"></a> adx_invitationCode

|Property|Value|
|---|---|
|Description|**Shows the user who is redeeming the invitation.**|
|DisplayName|**Invitation Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_invitationcode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_adx_invitationId"></a> adx_invitationId

|Property|Value|
|---|---|
|Description|**Shows the entity instance.**|
|DisplayName|**Invitation**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`adx_invitationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_adx_inviteContact"></a> adx_inviteContact

|Property|Value|
|---|---|
|Description|**The contact to send an invitation to.**|
|DisplayName|**Invite Contact**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_invitecontact`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|contact|

### <a name="BKMK_adx_invitercontact"></a> adx_invitercontact

|Property|Value|
|---|---|
|Description|**The contact that invited.**|
|DisplayName|**Inviter**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_invitercontact`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|contact|

### <a name="BKMK_adx_maximumRedemptions"></a> adx_maximumRedemptions

|Property|Value|
|---|---|
|Description||
|DisplayName|**Maximum Redemptions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_maximumredemptions`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_adx_name"></a> adx_name

|Property|Value|
|---|---|
|Description|**Type the name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_adx_redeemedContact"></a> adx_redeemedContact

|Property|Value|
|---|---|
|Description|**The contact associated with the redemption of this invitation.**|
|DisplayName|**Redeemed Contact**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_redeemedcontact`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|contact|

### <a name="BKMK_adx_redemptions"></a> adx_redemptions

|Property|Value|
|---|---|
|Description|**The current number of times this invitation has been redeemed.**|
|DisplayName|**Redemptions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_redemptions`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_adx_redemptionWorkflow"></a> adx_redemptionWorkflow

|Property|Value|
|---|---|
|Description|**A workflow to execute on the redeeming contact.**|
|DisplayName|**Redemption Workflow**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_redemptionworkflow`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_adx_type"></a> adx_type

|Property|Value|
|---|---|
|Description|**The type of invitation.**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`adx_type`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`adx_invitation_adx_type`|

#### adx_type Choices/Options

|Value|Label|
|---|---|
|756150000|**Single**|
|756150001|**Group**|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Shows the sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_websiteid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|powerpagesite|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time that the record was migrated.**|
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

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user who is assigned to manage the record. This field is updated every time the record is assigned to a different user.**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Invitation**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`adx_invitation_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Select the invitation's status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`adx_invitation_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **New**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|
|756150000|Label: **Sent**<br />State:0<br />TransitionData: None|
|756150001|Label: **Redeemed**<br />State:0<br />TransitionData: None|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Shows the time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Shows who created the record.**|
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
|Description|**Shows the date and time when the record was created.**|
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
|Description|**Shows who created the record on behalf of another user.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
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
|Description|**Shows the date and time when the record was modified.**|
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
|Description|**Shows who last updated the record on behalf of another user.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description|**Yomi name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Shows the business unit that owns the record.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier for the team that owns the record.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [adx_invitation_assigntoaccount](#BKMK_adx_invitation_assigntoaccount)
- [adx_invitation_invitecontact](#BKMK_adx_invitation_invitecontact)
- [adx_invitation_invitercontact](#BKMK_adx_invitation_invitercontact)
- [adx_invitation_redeemedContact](#BKMK_adx_invitation_redeemedContact)
- [adx_invitation_redemptionworkflow](#BKMK_adx_invitation_redemptionworkflow)
- [business_unit_adx_invitation](#BKMK_business_unit_adx_invitation)
- [lk_adx_invitation_createdby](#BKMK_lk_adx_invitation_createdby)
- [lk_adx_invitation_createdonbehalfby](#BKMK_lk_adx_invitation_createdonbehalfby)
- [lk_adx_invitation_modifiedby](#BKMK_lk_adx_invitation_modifiedby)
- [lk_adx_invitation_modifiedonbehalfby](#BKMK_lk_adx_invitation_modifiedonbehalfby)
- [owner_adx_invitation](#BKMK_owner_adx_invitation)
- [powerpagesite_mspp_websiteid_adx_invitation](#BKMK_powerpagesite_mspp_websiteid_adx_invitation)
- [team_adx_invitation](#BKMK_team_adx_invitation)
- [user_adx_invitation](#BKMK_user_adx_invitation)

### <a name="BKMK_adx_invitation_assigntoaccount"></a> adx_invitation_assigntoaccount

One-To-Many Relationship: [account adx_invitation_assigntoaccount](account.md#BKMK_adx_invitation_assigntoaccount)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`adx_assigntoaccount`|
|ReferencingEntityNavigationPropertyName|`adx_assignToAccount`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_invitecontact"></a> adx_invitation_invitecontact

One-To-Many Relationship: [contact adx_invitation_invitecontact](contact.md#BKMK_adx_invitation_invitecontact)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`adx_invitecontact`|
|ReferencingEntityNavigationPropertyName|`adx_inviteContact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_invitercontact"></a> adx_invitation_invitercontact

One-To-Many Relationship: [contact adx_invitation_invitercontact](contact.md#BKMK_adx_invitation_invitercontact)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`adx_invitercontact`|
|ReferencingEntityNavigationPropertyName|`adx_invitercontact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_redeemedContact"></a> adx_invitation_redeemedContact

One-To-Many Relationship: [contact adx_invitation_redeemedContact](contact.md#BKMK_adx_invitation_redeemedContact)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`adx_redeemedcontact`|
|ReferencingEntityNavigationPropertyName|`adx_redeemedContact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_adx_invitation_redemptionworkflow"></a> adx_invitation_redemptionworkflow

One-To-Many Relationship: [workflow adx_invitation_redemptionworkflow](workflow.md#BKMK_adx_invitation_redemptionworkflow)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`adx_redemptionworkflow`|
|ReferencingEntityNavigationPropertyName|`adx_redemptionWorkflow`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_business_unit_adx_invitation"></a> business_unit_adx_invitation

One-To-Many Relationship: [businessunit business_unit_adx_invitation](businessunit.md#BKMK_business_unit_adx_invitation)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_adx_invitation_createdby"></a> lk_adx_invitation_createdby

One-To-Many Relationship: [systemuser lk_adx_invitation_createdby](systemuser.md#BKMK_lk_adx_invitation_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_adx_invitation_createdonbehalfby"></a> lk_adx_invitation_createdonbehalfby

One-To-Many Relationship: [systemuser lk_adx_invitation_createdonbehalfby](systemuser.md#BKMK_lk_adx_invitation_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_adx_invitation_modifiedby"></a> lk_adx_invitation_modifiedby

One-To-Many Relationship: [systemuser lk_adx_invitation_modifiedby](systemuser.md#BKMK_lk_adx_invitation_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_adx_invitation_modifiedonbehalfby"></a> lk_adx_invitation_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_adx_invitation_modifiedonbehalfby](systemuser.md#BKMK_lk_adx_invitation_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_adx_invitation"></a> owner_adx_invitation

One-To-Many Relationship: [owner owner_adx_invitation](owner.md#BKMK_owner_adx_invitation)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesite_mspp_websiteid_adx_invitation"></a> powerpagesite_mspp_websiteid_adx_invitation

One-To-Many Relationship: [powerpagesite powerpagesite_mspp_websiteid_adx_invitation](powerpagesite.md#BKMK_powerpagesite_mspp_websiteid_adx_invitation)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesite`|
|ReferencedAttribute|`powerpagesiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_websiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_adx_invitation"></a> team_adx_invitation

One-To-Many Relationship: [team team_adx_invitation](team.md#BKMK_team_adx_invitation)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_adx_invitation"></a> user_adx_invitation

One-To-Many Relationship: [systemuser user_adx_invitation](systemuser.md#BKMK_user_adx_invitation)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [adx_invitation_ActivityPointers](#BKMK_adx_invitation_ActivityPointers)
- [adx_invitation_adx_inviteredemptions](#BKMK_adx_invitation_adx_inviteredemptions)
- [adx_invitation_adx_portalcomments](#BKMK_adx_invitation_adx_portalcomments)
- [adx_invitation_Annotations](#BKMK_adx_invitation_Annotations)
- [adx_invitation_Appointments](#BKMK_adx_invitation_Appointments)
- [adx_invitation_AsyncOperations](#BKMK_adx_invitation_AsyncOperations)
- [adx_invitation_BulkDeleteFailures](#BKMK_adx_invitation_BulkDeleteFailures)
- [adx_invitation_chats](#BKMK_adx_invitation_chats)
- [adx_invitation_connections1](#BKMK_adx_invitation_connections1)
- [adx_invitation_connections2](#BKMK_adx_invitation_connections2)
- [adx_invitation_DuplicateBaseRecord](#BKMK_adx_invitation_DuplicateBaseRecord)
- [adx_invitation_DuplicateMatchingRecord](#BKMK_adx_invitation_DuplicateMatchingRecord)
- [adx_invitation_Emails](#BKMK_adx_invitation_Emails)
- [adx_invitation_Faxes](#BKMK_adx_invitation_Faxes)
- [adx_invitation_Letters](#BKMK_adx_invitation_Letters)
- [adx_invitation_MailboxTrackingFolders](#BKMK_adx_invitation_MailboxTrackingFolders)
- [adx_invitation_PhoneCalls](#BKMK_adx_invitation_PhoneCalls)
- [adx_invitation_PrincipalObjectAttributeAccesses](#BKMK_adx_invitation_PrincipalObjectAttributeAccesses)
- [adx_invitation_ProcessSession](#BKMK_adx_invitation_ProcessSession)
- [adx_invitation_RecurringAppointmentMasters](#BKMK_adx_invitation_RecurringAppointmentMasters)
- [adx_invitation_SocialActivities](#BKMK_adx_invitation_SocialActivities)
- [adx_invitation_SyncErrors](#BKMK_adx_invitation_SyncErrors)
- [adx_invitation_Tasks](#BKMK_adx_invitation_Tasks)

### <a name="BKMK_adx_invitation_ActivityPointers"></a> adx_invitation_ActivityPointers

Many-To-One Relationship: [activitypointer adx_invitation_ActivityPointers](activitypointer.md#BKMK_adx_invitation_ActivityPointers)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_ActivityPointers`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_adx_inviteredemptions"></a> adx_invitation_adx_inviteredemptions

Many-To-One Relationship: [adx_inviteredemption adx_invitation_adx_inviteredemptions](adx_inviteredemption.md#BKMK_adx_invitation_adx_inviteredemptions)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_adx_inviteredemptions`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_adx_portalcomments"></a> adx_invitation_adx_portalcomments

Many-To-One Relationship: [adx_portalcomment adx_invitation_adx_portalcomments](adx_portalcomment.md#BKMK_adx_invitation_adx_portalcomments)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_adx_portalcomments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_Annotations"></a> adx_invitation_Annotations

Many-To-One Relationship: [annotation adx_invitation_Annotations](annotation.md#BKMK_adx_invitation_Annotations)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_Annotations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_Appointments"></a> adx_invitation_Appointments

Many-To-One Relationship: [appointment adx_invitation_Appointments](appointment.md#BKMK_adx_invitation_Appointments)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_Appointments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_AsyncOperations"></a> adx_invitation_AsyncOperations

Many-To-One Relationship: [asyncoperation adx_invitation_AsyncOperations](asyncoperation.md#BKMK_adx_invitation_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_BulkDeleteFailures"></a> adx_invitation_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure adx_invitation_BulkDeleteFailures](bulkdeletefailure.md#BKMK_adx_invitation_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_chats"></a> adx_invitation_chats

Many-To-One Relationship: [chat adx_invitation_chats](chat.md#BKMK_adx_invitation_chats)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_chats`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_connections1"></a> adx_invitation_connections1

Many-To-One Relationship: [connection adx_invitation_connections1](connection.md#BKMK_adx_invitation_connections1)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record1id`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_connections1`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_connections2"></a> adx_invitation_connections2

Many-To-One Relationship: [connection adx_invitation_connections2](connection.md#BKMK_adx_invitation_connections2)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`record2id`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_connections2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_DuplicateBaseRecord"></a> adx_invitation_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord adx_invitation_DuplicateBaseRecord](duplicaterecord.md#BKMK_adx_invitation_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_DuplicateMatchingRecord"></a> adx_invitation_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord adx_invitation_DuplicateMatchingRecord](duplicaterecord.md#BKMK_adx_invitation_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_Emails"></a> adx_invitation_Emails

Many-To-One Relationship: [email adx_invitation_Emails](email.md#BKMK_adx_invitation_Emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_Emails`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_Faxes"></a> adx_invitation_Faxes

Many-To-One Relationship: [fax adx_invitation_Faxes](fax.md#BKMK_adx_invitation_Faxes)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_Faxes`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_Letters"></a> adx_invitation_Letters

Many-To-One Relationship: [letter adx_invitation_Letters](letter.md#BKMK_adx_invitation_Letters)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_Letters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_MailboxTrackingFolders"></a> adx_invitation_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder adx_invitation_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_adx_invitation_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_PhoneCalls"></a> adx_invitation_PhoneCalls

Many-To-One Relationship: [phonecall adx_invitation_PhoneCalls](phonecall.md#BKMK_adx_invitation_PhoneCalls)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_PhoneCalls`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_PrincipalObjectAttributeAccesses"></a> adx_invitation_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess adx_invitation_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_adx_invitation_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_ProcessSession"></a> adx_invitation_ProcessSession

Many-To-One Relationship: [processsession adx_invitation_ProcessSession](processsession.md#BKMK_adx_invitation_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_RecurringAppointmentMasters"></a> adx_invitation_RecurringAppointmentMasters

Many-To-One Relationship: [recurringappointmentmaster adx_invitation_RecurringAppointmentMasters](recurringappointmentmaster.md#BKMK_adx_invitation_RecurringAppointmentMasters)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_RecurringAppointmentMasters`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_SocialActivities"></a> adx_invitation_SocialActivities

Many-To-One Relationship: [socialactivity adx_invitation_SocialActivities](socialactivity.md#BKMK_adx_invitation_SocialActivities)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_SocialActivities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_SyncErrors"></a> adx_invitation_SyncErrors

Many-To-One Relationship: [syncerror adx_invitation_SyncErrors](syncerror.md#BKMK_adx_invitation_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_Tasks"></a> adx_invitation_Tasks

Many-To-One Relationship: [task adx_invitation_Tasks](task.md#BKMK_adx_invitation_Tasks)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_Tasks`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [adx_invitation_invitecontacts](#BKMK_adx_invitation_invitecontacts)
- [adx_invitation_mspp_webrole_powerpagecomponent](#BKMK_adx_invitation_mspp_webrole_powerpagecomponent)
- [adx_invitation_redeemedcontacts](#BKMK_adx_invitation_redeemedcontacts)

### <a name="BKMK_adx_invitation_invitecontacts"></a> adx_invitation_invitecontacts

See [contact adx_invitation_invitecontacts Many-To-Many Relationship](contact.md#BKMK_adx_invitation_invitecontacts)

|Property|Value|
|---|---|
|IntersectEntityName|`adx_invitation_invitecontacts`|
|IsCustomizable|True|
|SchemaName|`adx_invitation_invitecontacts`|
|IntersectAttribute|`adx_invitationid`|
|NavigationPropertyName|`adx_invitation_invitecontacts`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 20000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_mspp_webrole_powerpagecomponent"></a> adx_invitation_mspp_webrole_powerpagecomponent

See [powerpagecomponent adx_invitation_mspp_webrole_powerpagecomponent Many-To-Many Relationship](powerpagecomponent.md#BKMK_adx_invitation_mspp_webrole_powerpagecomponent)

|Property|Value|
|---|---|
|IntersectEntityName|`adx_invitation_mspp_webrole_powerpagecomponent`|
|IsCustomizable|True|
|SchemaName|`adx_invitation_mspp_webrole_powerpagecomponent`|
|IntersectAttribute|`adx_invitationid`|
|NavigationPropertyName|`adx_invitation_mspp_webrole_powerpagecomponent`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 20000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_invitation_redeemedcontacts"></a> adx_invitation_redeemedcontacts

See [contact adx_invitation_redeemedcontacts Many-To-Many Relationship](contact.md#BKMK_adx_invitation_redeemedcontacts)

|Property|Value|
|---|---|
|IntersectEntityName|`adx_invitation_redeemedcontacts`|
|IsCustomizable|True|
|SchemaName|`adx_invitation_redeemedcontacts`|
|IntersectAttribute|`adx_invitationid`|
|NavigationPropertyName|`adx_invitation_redeemedcontacts`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: Redeemed Invitations<br />MenuId: null<br />Order: 20000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.adx_invitation?displayProperty=fullName>
