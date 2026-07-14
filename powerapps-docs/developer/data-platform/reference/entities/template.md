---
title: "Email Template (Template) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Email Template (Template) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Email Template (Template) table/entity reference (Microsoft Dataverse)

Template for an email message that contains the standard attributes of an email message.

## Messages

The following table lists the messages for the Email Template (Template) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /templates(*templateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /templates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /templates(*templateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `InstantiateTemplate`<br />Event: False |<xref:Microsoft.Dynamics.CRM.InstantiateTemplate?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.InstantiateTemplateRequest>|
| `MakeAvailableToOrganizationReport`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.MakeAvailableToOrganizationReportRequest>|
| `MakeAvailableToOrganizationTemplate`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.MakeAvailableToOrganizationTemplateRequest>|
| `MakeUnavailableToOrganizationReport`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.MakeUnavailableToOrganizationReportRequest>|
| `MakeUnavailableToOrganizationTemplate`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.MakeUnavailableToOrganizationTemplateRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /templates(*templateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /templates<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SendEmail`<br />Event: True |<xref:Microsoft.Dynamics.CRM.SendEmail?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SendEmailRequest>|
| `SendFax`<br />Event: True |<xref:Microsoft.Dynamics.CRM.SendFax?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SendFaxRequest>|
| `SendTemplate`<br />Event: True |<xref:Microsoft.Dynamics.CRM.SendTemplate?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SendTemplateRequest>|
| `Update`<br />Event: True |`PATCH` /templates(*templateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /templates(*templateid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Email Template (Template) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Email Template** |
| **DisplayCollectionName** | **Email Templates** |
| **SchemaName** | `Template` |
| **CollectionSchemaName** | `Templates` |
| **EntitySetName** | `templates`|
| **LogicalName** | `template` |
| **LogicalCollectionName** | `templates` |
| **PrimaryIdAttribute** | `templateid` |
| **PrimaryNameAttribute** |`title` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Body](#BKMK_Body)
- [Description](#BKMK_Description)
- [EntityImage](#BKMK_EntityImage)
- [GenerationTypeCode](#BKMK_GenerationTypeCode)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsPersonal](#BKMK_IsPersonal)
- [LanguageCode](#BKMK_LanguageCode)
- [MimeType](#BKMK_MimeType)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PresentationXml](#BKMK_PresentationXml)
- [SafeHtml](#BKMK_SafeHtml)
- [Subject](#BKMK_Subject)
- [SubjectPresentationXml](#BKMK_SubjectPresentationXml)
- [SubjectSafeHtml](#BKMK_SubjectSafeHtml)
- [TemplateId](#BKMK_TemplateId)
- [TemplateTypeCode](#BKMK_TemplateTypeCode)
- [Title](#BKMK_Title)

### <a name="BKMK_Body"></a> Body

|Property|Value|
|---|---|
|Description|**Body text of the email template.**|
|DisplayName|**Body**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`body`|
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
|Description|**Description of the email template.**|
|DisplayName|**Description**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|---|---|
|Description|**Shows the default image for the record.**|
|DisplayName|**Default Image**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage`|
|RequiredLevel|None|
|Type|Image|
|CanStoreFullImage|False|
|IsPrimaryImage|True|
|MaxHeight|144|
|MaxSizeInKB|10240|
|MaxWidth|144|

### <a name="BKMK_GenerationTypeCode"></a> GenerationTypeCode

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Generation Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`generationtypecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

### <a name="BKMK_IsPersonal"></a> IsPersonal

|Property|Value|
|---|---|
|Description|**Information about whether the template is personal or is available to all users.**|
|DisplayName|**Viewable By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispersonal`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`template_ispersonal`|
|DefaultValue|True|
|True Label|Individual|
|False Label|Organization|

### <a name="BKMK_LanguageCode"></a> LanguageCode

|Property|Value|
|---|---|
|Description|**Language of the email template.**|
|DisplayName|**Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`languagecode`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_MimeType"></a> MimeType

|Property|Value|
|---|---|
|Description|**MIME type of the email template.**|
|DisplayName|**Mime Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mimetype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the template for the email activity.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_PresentationXml"></a> PresentationXml

|Property|Value|
|---|---|
|Description|**XML data for the body of the email template.**|
|DisplayName|**Presentation XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`presentationxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_SafeHtml"></a> SafeHtml

|Property|Value|
|---|---|
|Description|**Safe html of email template.**|
|DisplayName|**Safe HTML of email template**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`safehtml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Subject"></a> Subject

|Property|Value|
|---|---|
|Description|**Subject associated with the email template.**|
|DisplayName|**Subject**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subject`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_SubjectPresentationXml"></a> SubjectPresentationXml

|Property|Value|
|---|---|
|Description|**XML data for the subject of the email template.**|
|DisplayName|**Subject XML**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subjectpresentationxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_SubjectSafeHtml"></a> SubjectSafeHtml

|Property|Value|
|---|---|
|Description|**Safe html of email template subject.**|
|DisplayName|**Safe HTML of email template subject**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`subjectsafehtml`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_TemplateId"></a> TemplateId

|Property|Value|
|---|---|
|Description|**Unique identifier of the template.**|
|DisplayName|**Email Template**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`templateid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_TemplateTypeCode"></a> TemplateTypeCode

|Property|Value|
|---|---|
|Description|**Type of email template.**|
|DisplayName|**Template Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`templatetypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_Title"></a> Title

|Property|Value|
|---|---|
|Description|**Title of the template.**|
|DisplayName|**Title**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`title`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [IsManaged](#BKMK_IsManaged)
- [IsRecommended](#BKMK_IsRecommended)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OpenCount](#BKMK_OpenCount)
- [OpenRate](#BKMK_OpenRate)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ReplyCount](#BKMK_ReplyCount)
- [ReplyRate](#BKMK_ReplyRate)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TemplateIdUnique](#BKMK_TemplateIdUnique)
- [UsedCount](#BKMK_UsedCount)
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

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the email template.**|
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
|Description|**Date and time when the email template was created.**|
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
|Description|**Unique identifier of the delegate user who created the template.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_timestamp`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_url`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_IsRecommended"></a> IsRecommended

|Property|Value|
|---|---|
|Description|**Indicates if a template is recommended by Dynamics 365.**|
|DisplayName|**Recommended**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isrecommended`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`template_isrecommended`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the template.**|
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
|Description|**Date and time when the email template was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the template.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OpenCount"></a> OpenCount

|Property|Value|
|---|---|
|Description|**For internal use only. Shows the number of times emails that use this template have been opened.**|
|DisplayName|**Open Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`opencount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_OpenRate"></a> OpenRate

|Property|Value|
|---|---|
|Description|**Shows the open rate of this template. This is based on number of opens on followed emails that use this template.**|
|DisplayName|**Open Rate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`openrate`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description||
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
|Description||
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
|Description|**Unique identifier of the business unit that owns the template.**|
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
|Description|**Unique identifier of the team who owns the template.**|
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
|Description|**Unique identifier of the user who owns the template.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ReplyCount"></a> ReplyCount

|Property|Value|
|---|---|
|Description|**For internal use only. Shows the number of times emails that use this template have received replies.**|
|DisplayName|**Reply Count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`replycount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ReplyRate"></a> ReplyRate

|Property|Value|
|---|---|
|Description|**Shows the reply rate for this template. This is based on number of replies received on followed emails that use this template.**|
|DisplayName|**Reply Rate**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`replyrate`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

### <a name="BKMK_TemplateIdUnique"></a> TemplateIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`templateidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_UsedCount"></a> UsedCount

|Property|Value|
|---|---|
|Description|**Shows the number of sent emails that use this template.**|
|DisplayName|**Sent email count**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`usedcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the template.**|
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

- [business_unit_templates](#BKMK_business_unit_templates)
- [lk_templatebase_createdby](#BKMK_lk_templatebase_createdby)
- [lk_templatebase_createdonbehalfby](#BKMK_lk_templatebase_createdonbehalfby)
- [lk_templatebase_modifiedby](#BKMK_lk_templatebase_modifiedby)
- [lk_templatebase_modifiedonbehalfby](#BKMK_lk_templatebase_modifiedonbehalfby)
- [owner_templates](#BKMK_owner_templates)
- [system_user_email_templates](#BKMK_system_user_email_templates)
- [team_email_templates](#BKMK_team_email_templates)

### <a name="BKMK_business_unit_templates"></a> business_unit_templates

One-To-Many Relationship: [businessunit business_unit_templates](businessunit.md#BKMK_business_unit_templates)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_templatebase_createdby"></a> lk_templatebase_createdby

One-To-Many Relationship: [systemuser lk_templatebase_createdby](systemuser.md#BKMK_lk_templatebase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_templatebase_createdonbehalfby"></a> lk_templatebase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_templatebase_createdonbehalfby](systemuser.md#BKMK_lk_templatebase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_templatebase_modifiedby"></a> lk_templatebase_modifiedby

One-To-Many Relationship: [systemuser lk_templatebase_modifiedby](systemuser.md#BKMK_lk_templatebase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_templatebase_modifiedonbehalfby"></a> lk_templatebase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_templatebase_modifiedonbehalfby](systemuser.md#BKMK_lk_templatebase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_templates"></a> owner_templates

One-To-Many Relationship: [owner owner_templates](owner.md#BKMK_owner_templates)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_system_user_email_templates"></a> system_user_email_templates

One-To-Many Relationship: [systemuser system_user_email_templates](systemuser.md#BKMK_system_user_email_templates)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_email_templates"></a> team_email_templates

One-To-Many Relationship: [team team_email_templates](team.md#BKMK_team_email_templates)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [Email_EmailTemplate](#BKMK_Email_EmailTemplate)
- [template_activity_mime_attachments](#BKMK_template_activity_mime_attachments)
- [Template_AsyncOperations](#BKMK_Template_AsyncOperations)
- [Template_BulkDeleteFailures](#BKMK_Template_BulkDeleteFailures)
- [Template_Organization](#BKMK_Template_Organization)
- [Template_ProcessSessions](#BKMK_Template_ProcessSessions)
- [Template_SyncErrors](#BKMK_Template_SyncErrors)

### <a name="BKMK_Email_EmailTemplate"></a> Email_EmailTemplate

Many-To-One Relationship: [email Email_EmailTemplate](email.md#BKMK_Email_EmailTemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`templateid`|
|ReferencedEntityNavigationPropertyName|`Email_EmailTemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_template_activity_mime_attachments"></a> template_activity_mime_attachments

Many-To-One Relationship: [activitymimeattachment template_activity_mime_attachments](activitymimeattachment.md#BKMK_template_activity_mime_attachments)

|Property|Value|
|---|---|
|ReferencingEntity|`activitymimeattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`template_activity_mime_attachments`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Template_AsyncOperations"></a> Template_AsyncOperations

Many-To-One Relationship: [asyncoperation Template_AsyncOperations](asyncoperation.md#BKMK_Template_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Template_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Template_BulkDeleteFailures"></a> Template_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Template_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Template_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Template_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Template_Organization"></a> Template_Organization

Many-To-One Relationship: [organization Template_Organization](organization.md#BKMK_Template_Organization)

|Property|Value|
|---|---|
|ReferencingEntity|`organization`|
|ReferencingAttribute|`acknowledgementtemplateid`|
|ReferencedEntityNavigationPropertyName|`Template_Organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Template_ProcessSessions"></a> Template_ProcessSessions

Many-To-One Relationship: [processsession Template_ProcessSessions](processsession.md#BKMK_Template_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Template_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Template_SyncErrors"></a> Template_SyncErrors

Many-To-One Relationship: [syncerror Template_SyncErrors](syncerror.md#BKMK_Template_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Template_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.template?displayProperty=fullName>
