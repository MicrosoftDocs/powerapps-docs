---
title: "Read and update environment settings (Microsoft Dataverse)" 
description: "Change environment settings in the organization table." 
ms.date: 06/10/2025
ms.topic: article
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Read and update environment settings

Many settings for the environment are stored as columns in the [Organization table](reference/entities/organization.md).

The organization table has a single row and the [OrganizationId](reference/entities/organization.md#BKMK_OrganizationId) primary key value is the same **Organization ID** value visible in the [Power Platform admin center](https://admin.powerplatform.microsoft.com/). [Find your environment and organization ID](/power-platform/admin/determine-org-id-name#find-your-environment-and-organization-id)

The `WhoAmI` message response returns the `OrganizationId` property. Use the `organizationid` value to retrieve the single row of the organization table. See [SDK for .NET WhoAmIRequest Class](/dotnet/api/microsoft.crm.sdk.messages.whoamirequest) and [Web API WhoAmI function](/power-apps/developer/data-platform/webapi/reference/whoami).

## Supported settings

The documentation for any feature with settings must document the settings they support changing. Not every column is documented. Only settings described in feature documentation are supported to set.

For example, the following columns are supported because they're mentioned in the feature documentation:

|Setting|Link to documentation|
|---------|---------|
|[AuditSettings](reference/entities/organization.md#BKMK_AuditSettings)<br />[IsAuditEnabled](reference/entities/organization.md#BKMK_IsAuditEnabled)<br />[AuditRetentionPeriodV2](reference/entities/organization.md#BKMK_AuditRetentionPeriodV2)<br />[IsUserAccessAuditEnabled](reference/entities/organization.md#BKMK_IsUserAccessAuditEnabled)<br />[UserAccessAuditingInterval](reference/entities/organization.md#BKMK_UserAccessAuditingInterval)|[Configure auditing](auditing/configure.md)|
|[ExpireSubscriptionsInDays](reference/entities/organization.md#BKMK_ExpireSubscriptionsInDays)|[Cache Schema data](cache-schema-data.md)|
|[MaxUploadFileSize](reference/entities/organization.md#BKMK_MaxUploadFileSize)<br />[BlockedAttachments](reference/entities/organization.md#BKMK_BlockedAttachments)<br />[BlockedMimeTypes](reference/entities/organization.md#BKMK_BlockedMimeTypes)<br />[AllowedMimeTypes](reference/entities/organization.md#BKMK_AllowedMimeTypes)|[Files and images overview](files-images-overview.md)|
|[PluginTraceLogSetting](reference/entities/organization.md#BKMK_PluginTraceLogSetting)|[Tracing and logging](logging-tracing.md)|
|[QuickFindRecordLimitEnabled](reference/entities/organization.md#BKMK_QuickFindRecordLimitEnabled)|[About quick find queries](quick-find.md)|
|[ShareToPreviousOwnerOnAssign](reference/entities/organization.md#BKMK_ShareToPreviousOwnerOnAssign)|[Sharing and assigning](security-sharing-assigning.md)|
|[ExpireChangeTrackingInDays](reference/entities/organization.md#BKMK_ExpireChangeTrackingInDays)|[Use change tracking to synchronize data with external systems](use-change-tracking-synchronize-data-external-systems.md)|
|[IsExternalSearchIndexEnabled](reference/entities/organization.md#BKMK_IsExternalSearchIndexEnabled)|[Search for Dataverse records](search/overview.md)|

> [!NOTE]
> This list is not comprehensive. Look in the documentation for the feature you are working with for the settings that feature supports changing.


## Unsupported settings

Some columns are explicitly not supported to update directly. For example, you shouldn't try to update the [OrgDbOrgSettings](reference/entities/organization.md#BKMK_OrgDbOrgSettings) column directly. This string column contains multiple XML elements that control behavior for multiple features. If you update this value incorrectly, features that depend on these settings could break. Always use the tools described in [Environment database settings](/power-platform/admin/environment-database-settings) to change the values of this column.



## Read-only settings

Some settings are available to retrieve but can't be set. These columns have false values for both [AttributeMetadata.IsValidForCreate](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.isvalidforcreate) and [AttributeMetadata.IsValidForUpdate](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.isvalidforupdate). You can view the list of read-only columns here: [Organization table Read-only columns/attributes](reference/entities/organization.md#read-only-columnsattributes).

> [!NOTE]
> As with every kind of table, if you try to set a read-only column, the operation does not throw an error. The value you provide to update a read-only column is ignored.

Settings that can be updated are listed here [Organization table Writable columns/attributes](reference/entities/organization.md#writable-columnsattributes). Keep in mind that being writable doesn't mean that [updating the setting is supported](#supported-settings).

## Deprecated settings

Some columns represent deprecated settings. You should look at the descriptions of the column in the list of [Organization table Writable columns/attributes](reference/entities/organization.md#writable-columnsattributes) to determine whether the setting still represents the way to modify the environment behavior. For example, the following columns are deprecated:

- [CurrentBulkOperationNumber](reference/entities/organization.md#BKMK_CurrentBulkOperationNumber)
- [CurrentCampaignNumber](reference/entities/organization.md#BKMK_CurrentCampaignNumber)
- [CurrentCaseNumber](reference/entities/organization.md#BKMK_CurrentCaseNumber)
- [CurrentCategoryNumber](reference/entities/organization.md#BKMK_CurrentCategoryNumber)
- [CurrentContractNumber](reference/entities/organization.md#BKMK_CurrentContractNumber)
- [CurrentInvoiceNumber](reference/entities/organization.md#BKMK_CurrentInvoiceNumber)
- [CurrentKaNumber](reference/entities/organization.md#BKMK_CurrentKaNumber)
- [CurrentKbNumber](reference/entities/organization.md#BKMK_CurrentKbNumber)
- [CurrentOrderNumber](reference/entities/organization.md#BKMK_CurrentOrderNumber)
- [CurrentQuoteNumber](reference/entities/organization.md#BKMK_CurrentQuoteNumber)
- [MicrosoftFlowEnvironment](reference/entities/organization.md#BKMK_MicrosoftFlowEnvironment)


## Use PAC CLI to retrieve and update settings

You can retrieve and update column values for the organization table row using the SDK for .NET and Web API as you would for any Dataverse table. You can also use the [Microsoft Power Platform CLI](/power-platform/developer/cli/introduction).

The PAC CLI includes these commands:

 - [pac env list-settings](/power-platform/developer/cli/reference/env#pac-env-list-settings): Returns environment settings stored in the organization table.
 - [pac env update-settings](/power-platform/developer/cli/reference/env#pac-env-update-settings): Enables updating a single organization table column value.

 When you use the `pac env update-settings` command, make sure to only update columns that can be updated. If you use this command to set a [read-only column](#read-only-settings), the command will incorrectly report that the change was applied successfully because no error occurred.

