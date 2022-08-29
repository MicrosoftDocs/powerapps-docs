---
title: Overview of portals Web API
description: Learn how to use the portals Web API to create, read, update, and delete Microsoft Dataverse tables from your portals pages.
author: neerajnandwana-msft

ms.topic: overview
ms.custom: 
ms.date: 07/26/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - ProfessorKendrick
---

# Portals Web API overview

The portals Web API enables a richer user experience inside Power Apps portals pages. You can use the Web API to perform create, read, update, and delete operations across all Microsoft Dataverse tables from your portals pages. For example, you can create a new account, update a contact, or change the [table permissions](configure/assign-entity-permissions.md) for a product by using the portals Web API instead of the Portal Management app.

> [!NOTE] 
> You can also use portals Web API in Power Pages. More information: [What is Power Pages](/power-pages/introduction)

> [!IMPORTANT]
> - **Your portal version must be 9.3.3.x or later for this feature to work**.
> - The portals Web API is built for creating a rich user experience inside portal pages. It isn't optimized for third-party services or application integration.
> - Portals Web API operations are limited to tables related to data&mdash;for example, accounts, contacts, or your custom tables. Configuring table metadata or portal configuration table data&mdash;for example, configuring portals tables such as adx_contentsnippet, adx_entityform, or adx_entitylist&mdash;isn't supported with the portals Web API. For a complete list, go to [unsupported configuration tables](#unsupported-configuration-tables) later in this topic.
> - The portals Web API benefits from [server-side caching](admin/clear-server-side-cache.md), so subsequent calls to the Web API are faster than the initial calls. Note that clearing the portal server-side cache causes temporary performance degradation.
> - Portals Web API operations require a Power Apps portals license. For example, Web API calls made by anonymous users are counted towards page view capacity. Web API calls made by authenticated users (internal or external) are not counted towards page views, but require applicable licenses. More information: [Power Apps portals licensing FAQs](/power-platform/admin/powerapps-flow-licensing-faq#can-you-share-more-details-regarding-the-new-power-apps-portals-licensing)

## Web API operations

The portals Web API offers a subset of capabilities for Dataverse operations that you can do by using the Dataverse API. We've kept the API format as similar as possible to reduce the learning curve.

> [!NOTE]
> Web API operations are case-sensitive.

### Web API operations available in portals

- [Read records from a table](read-operations.md)
- [Create a record in a table](write-update-delete-operations.md#create-a-record-in-a-table)
- [Update and delete records in a table](write-update-delete-operations.md#update-and-delete-records-by-using-the-web-api) 
- [Associate and disassociate tables](write-update-delete-operations.md#associate-and-disassociate-tables-by-using-the-web-api)

## Site settings for the Web API

You must enable the site setting to enable the portals Web API for your portal. You can also configure the field-level Web API that determines the table fields that can or can't be modified with the portals Web API.

> [!NOTE]
> Use the table [logical name](../../developer/data-platform/entity-metadata.md) for these settings (for example **account**).

| Site setting name | Description|
| - |- |
| *Webapi/\<table name\>/enabled* | Enables or disables the Web API for \<table name\>. <br> **Default:** `False` <br> **Valid values:** `True`, `False` |
| *Webapi/\<table name\>/fields*  | Defines the comma-separated list of attributes that can be modified with the Web API. <br>  **Possible values:**  <br> - *All attributes:* `*` <br> - *Specific attributes:* `attr1,attr2,attr3` <br> **Note**:  The value must be either an asterisk (**\***) or a comma-separated list of field names. <br> **Important**: This is a mandatory site setting. When this setting is missing, you'll see the error "No fields defined for this entity." |
| *Webapi/error/innererror* | Enables or disables InnerError. <br> **Default:** `False` <br> **Valid values:** `True`, `False`

> [!NOTE]
> Site settings must be set to **Active** for changes to take effect.

For example, to expose the Web API for the Case table where authenticated
users are allowed to perform create, update, and delete operations on this entity, the site settings are shown in the following table.

| Site setting name | Site setting value|
| - |- |
| *Webapi/incident/enabled* | true |
| *Webapi/incident/fields* | attr1,attr2,attr3 |

## Security with the portals Web API

You can configure record-based security to individual records in portals by using [table permissions](configure/assign-entity-permissions.md). The portals Web API accesses table (entity) records and follows the table permissions given to users through the associated [web role](configure/create-web-roles.md).

You can configure [column permissions](configure/column-permissions.md) to further define privileges to individual columns within a table while using the portals Web API. 

![Portals Web API security.](media/web-api/portals-Webapi-security.png "Portals Web API security architecture")

## Authenticating portals Web API requests

You don't need to include an authentication code, because authentication and authorization are managed by the application session. All Web API calls must include a Cross-Site Request Forgery (CSRF) token.

## Using EntitySetName

When referring to Dataverse tables using the portals Web API in your code, you need to use the [EntitySetName](../../developer/data-platform/entity-metadata.md#table-names), for example, to access the **account** table, the code syntax will use the EntitySetName of **accounts**; `/_api/accounts()`.

> [!NOTE]
> Use the table logical name for [site settings](#site-settings-for-the-web-api) (for example, **account**).

You can determine the **EntitySetName** of specific tables by following these steps: 

1. Go to https://make.powerapps.com

1. Select the **Dataverse** tab from the side panel and select the table.

1. Select the **...** (Commands option) and then choose **Advanced**, **Tools**, and **Copy set name** to copy the **EntitySetName** of the table to your clipboard.

    :::image type="content" source="media/web-api/entitysetname.png" alt-text="How to locate EntitySetName of a Dataverse table.":::

## General Data Protection Regulation (GDPR)

All request headers will have a contact ID passed for auditing purposes. For an anonymous user, this will be passed as `null`.

If audit logging is enabled, a user can see all the audit events in the [Office 365 audit log](https://protection.office.com/unifiedauditlog).

![Office 365 audit log.](media/web-api/office365-security-compliance-audit-log.png)

More information:<br>[Enable and use activity logging](/power-platform/admin/enable-use-comprehensive-auditing)<br>[Export, configure, and view audit log records](/microsoft-365/compliance/export-view-audit-log-records)

## Unsupported configuration tables

Portals Web API can't be used for the following configuration tables:


:::row:::
:::column:::
	adx_contentaccesslevel
:::column-end:::
:::column:::
	adx_contentsnippet
:::column-end:::
:::column:::
	adx_entityform
:::row-end:::
:::row:::
:::column:::
	adx_entityformmetadata
:::column-end:::
:::column:::
	adx_entitylist
:::column-end:::
:::column:::
	adx_entitypermission
:::row-end:::
:::row:::
:::column:::
	adx_entitypermission_webrole
:::column-end:::
:::column:::
	adx_externalidentity
:::column-end:::
:::column:::
	adx_pagealert
:::row-end:::
:::row:::
:::column:::
	adx_pagenotification
:::column-end:::
:::column:::
	adx_pagetag
:::column-end:::
:::column:::
	adx_pagetag_webpage
:::row-end:::
:::row:::
:::column:::
	adx_pagetemplate
:::column-end:::
:::column:::
	adx_portallanguage
:::column-end:::
:::column:::
	adx_publishingstate
:::row-end:::
:::row:::
:::column:::
	adx_publishingstatetransitionrule
:::column-end:::
:::column:::
	adx_publishingstatetransitionrule_webrole
:::column-end:::
:::column:::
	adx_redirect
:::row-end:::
:::row:::
:::column:::
	adx_setting
:::column-end:::
:::column:::
	adx_shortcut
:::column-end:::
:::column:::
	adx_sitemarker
:::row-end:::
:::row:::
:::column:::
	adx_sitesetting
:::column-end:::
:::column:::
	adx_urlhistory
:::column-end:::
:::column:::
	adx_webfile
:::row-end:::
:::row:::
:::column:::
	adx_webfilelog
:::column-end:::
:::column:::
	adx_webform
:::column-end:::
:::column:::
	adx_webformmetadata
:::row-end:::
:::row:::
:::column:::
	adx_webformsession
:::column-end:::
:::column:::
	adx_webformstep
:::column-end:::
:::column:::
	adx_weblink
:::row-end:::
:::row:::
:::column:::
	adx_weblinkset
:::column-end:::
:::column:::
	adx_webnotificationentity
:::column-end:::
:::column:::
	adx_webnotificationurl
:::row-end:::
:::row:::
:::column:::
	adx_webpage
:::column-end:::
:::column:::
	adx_webpage_tag
:::column-end:::
:::column:::
	adx_webpageaccesscontrolrule
:::row-end:::
:::row:::
:::column:::
	adx_webpageaccesscontrolrule_webrole
:::column-end:::
:::column:::
	adx_webpagehistory
:::column-end:::
:::column:::
	adx_webpagelog
:::row-end:::
:::row:::
:::column:::
	adx_webrole_systemuser
:::column-end:::
:::column:::
	adx_website
:::column-end:::
:::column:::
	adx_website_list
:::row-end:::
:::row:::
:::column:::
	adx_website_sponsor
:::column-end:::
:::column:::
	adx_websiteaccess
:::column-end:::
:::column:::
	adx_websiteaccess_webrole
:::row-end:::
:::row:::
:::column:::
	adx_websitebinding
:::column-end:::
:::column:::
	adx_websitelanguage
:::column-end:::
:::column:::
	adx_webtemplate
:::row-end:::

## Next step

[Query data using portals Web API](read-operations.md)

### See also

[Compose HTTP requests and handle errors](web-api-http-requests-handle-errors.md)</br>
[Portals write, update and delete operations using the Web API](write-update-delete-operations.md)</br>
[Tutorial: Use portal Web API](webapi-tutorial.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
