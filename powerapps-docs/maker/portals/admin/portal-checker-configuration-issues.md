---
title: Portal checker configuration issues
description: Learn about Portal Checker diagnostics results for configuration issues.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 11/14/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - dileepsinghmicrosoft
    - ProfessorKendrick
---

# Portal checker configuration issues

In this article, you'll learn about Portal Checker diagnostics results related to configuration issues, and how to resolve common issues or problems.

## Anonymous access to basic forms, lists, and advanced form steps

The following issues relate to configuration of [table permissions](../configure/entity-permissions-studio.md) on Dataverse-enabled components.

### Anonymous access to basic/advanced forms and lists

Basic forms, Advanced forms, and lists in portals can be excluded from enforcing table permissions by not selecting the **Enable Table Permission** checkbox while creating or modifying these controls as explained in [Securing lists](../configure/securing-lists.md) and [Secure your forms](../configure/entity-forms.md#secure-your-forms).

This method is useful for quickly testing your configurations during development of a portal, but not securing Lists and Forms on a portal can have unintended consequences including unauthorized access to data. We don't advise this method to be used outside a secure dev or test environment.

To fix this issue for List/Basic forms:

1. Open the [Portal Management app](../configure/configure-portal.md).

1. On the left pane, select **List** or **Basic forms** as appropriate.

1. Find the record mentioned in the Portal Checker rule.

1. Update the property "Enable Table Permissions" for [Lists](../configure/securing-lists.md) or [Basic forms](../configure/entity-forms.md#secure-your-forms).

To fix this issue for Advanced forms:

> [!IMPORTANT]
> Portal Checker rule doesn't mention Advanced form steps that might have a similar configuration.

1. Open the [Portal Management app](../configure/configure-portal.md).

1. On the left pane, select **Advanced form**.

1. Open each advanced form and go to **Advanced Form Steps**.

1. Go through each step, and update the **Enable Table Permission** property to be enabled.

Once these changes are made, appropriate table permissions would need to be created and assigned to appropriate web roles to ensure that all users can access these components.

> [!NOTE]
> This method of disabling **Table Permissions** will be deprecated soon. Therefore, it shouldn't be used. Use proper [table permissions](../configure/entity-permissions-studio.md), and web role setup to provide access to users for any data instead. More information: [Table permission changes for forms and lists on new portals](../important-changes-deprecations.md#table-permission-changes-for-forms-and-lists-on-new-portals)

### Anonymous access available to OData feed

> [!NOTE]
> Starting with release [9.3.7.x](/power-platform/released-versions/portals/portalupdate1), lists on all portals (new or existing) that have [OData feeds](../configure/list-odata-feeds.md) enabled will require appropriate [table permissions](../configure/entity-permissions-studio.md) setup for the feed on these lists to work.

List components in portals can be enabled for OData feed by enabling [OData feeds](../configure/list-odata-feeds.md) on lists. 

To find anonymous OData feeds enabled on your portal:

1. Go to '{Portal Url}/_odata' (for example, `https://contoso.powerappsportals.com/_odata`) in InPrivate mode without authenticating to the portal.

1. In the UI, you'll see a list of all OData feeds enabled on your portal.

    ![Enabled OData feeds](media/portal-checker-analysis/enabled-odata-feeds.png "Enabled OData feeds")

    > [!NOTE]
    > The list of OData feeds on this page might be available anonymously depending on your security configuration. The next steps will help you verify the anonymous access of these feeds.

1. Go to each OData feed by browsing to the URL format {Portal URL}/_odata/{collection href value} (for example, `https://contoso.powerappsportals.com/_odata/accounts`) where the collection href value is highlighted below.

    ![Browse to OData feed](media/portal-checker-analysis/browse-to-enabled-odata-feeds.png "Browse to OData feed")

1. If the OData field is available anonymously, it will return the data with an HTTP 200 response. If the feed isn't enabled anonymously, it will return an HTTP 403 response with a message “Access to OData, with the entity set name of '{table set name}', has been denied.”


<!-- Not sure what the following sentence means. Please review. -->


If you've unintentionally enabled anonymous access to an OData feed on your site, it could be because of one of these possibilities:

- By not securing the list on which the OData feed is enabled as described in [Securing lists](../configure/securing-lists.md).

  - To fix this problem, secure the list as described in [Securing lists](../configure/securing-lists.md), and use appropriate table permissions and web roles to provide access to users.

  - You can also find the lists that aren't secured through Portal Checker as described in the above mentioned article.

- By securing lists, creating appropriate table permissions to the tables used in lists, and assigning those table permissions to an anonymous web role.

  - To fix this problem, check that the table permissions assigned to the **Anonymous** web role are updated to ensure that only intended data is made available anonymously.

## Cyclic parent webpage

This issue occurs when a [webpage](../configure/web-page.md) references itself as a parent page. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the webpages [listed](portal-checker.md#identifying-web-pages-listed-in-diagnostic-results) in the Portal Checker diagnostic results.
1. Update the **Parent Page** field to point to a valid webpage record that isn't referencing itself.

## List of tables with CMS security check failed

To fix this issue, ensure that your table has a proper search page.

## List of tables with search result having invalid URL

To fix this issue, ensure that your table has appropriate security permissions.

## Loading static resources (CSS/JS) asynchronously

When working on portal implementation, it's important to understand that you completely manage the HTML of the page. That means that standard web development practices should be followed to ensure that your webpage's client-side performance isn't affected.

One of the most common causes of performance issues on webpages is loading numerous static resources (CSS/JS) synchronously on the page. In portals, whenever you associate a web file directly to the home page, it creates a dependency in the generated HTML. This means that a web file is always loaded along with the home page. Synchronous loading of a large number of CSS/JS files can lead to long client-side processing time for your webpages.

To avoid this, do the following:

1. If a web file isn't needed on the home page, make sure its parent page isn't set to home, and follow the steps described in the section above to load it on demand.
1. While loading a JavaScript file on demand on any page, use the `<async>` or `<defer>` HTML attribute to load the file asynchronously.
1. While loading a CSS file on demand, you can use the `<preload>` HTML attribute (https://www.w3.org/TR/preload/) or JavaScript-based approach since preload isn't supported on all browsers yet.

## Parent page of an active webpage is inactive

This issue occurs when a parent [webpage](../configure/web-page.md) record is inactive. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the webpage [listed](portal-checker.md#identifying-web-pages-listed-in-diagnostic-results) in the Portal Checker diagnostic results.
1. Select the **Parent Page** record to navigate to the record.
1. Select **Activate** from the command bar.

## Portal is inaccessible

This issue may occur when the authentication certificate for the site needs to be renewed.

When a portal is created, a new authentication key is generated. The portal uses this authentication key to connect to the Microsoft Dataverse environment. When the authentication key is expired, portal users will see a message that the portal is inaccessible. 

To fix this issue, [renew the authentication key](manage-auth-key.md#renew-authentication-key) for this site. 

## Published state configuration

The following issues relate to the [publishing states](../configure/publishing-states.md).

### Published state isn't available for this website

To fix this issue, ensure that the publishing state **Published** is available and active.

### Published state isn't visible

To fix this issue, ensure that the publishing state **Published** has the **isVisible** checkbox selected.

## Site markers

The following issues relate to site markers.

### Home site marker configuration

The following issues relate to site markers and the home [webpage](../configure/web-page.md).

#### An active Home site marker isn't available for this portal

This issue occurs when the **Home** site marker isn't available in your portal configuration. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Create a new site marker with the following values:
    - **Name**: Home
    - **Website**: Select the website of your portal host.
    - **Page**: Select the webpage record that is set as the homepage of your portal.

#### The Home site marker isn't pointing to any webpage

This issue occurs when the **Home** site marker is available but isn't pointing to any webpage. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Find the **Home** site marker record.
1. Update the **Page** field to point to an active home page of your portal.

#### The Home site marker is pointing to a deactivated webpage

This issue occurs when the **Home** site marker is available, but is pointing to a deactivated webpage. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Find the **Home** site marker record.
1. Update the **Page** field to point to an active home page of your portal.

#### The Home site marker isn't pointing to a home page of the portal

This issue occurs when the **Home** site marker is available, but is pointing to a webpage that isn't a home page of your portal. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Find the **Home** site marker record.
1. Update the **Page** field to point to an active home page of your portal.

### Profile site marker configuration

The following issues relate to site marker configuration to the profile page.

#### An active Profile site marker isn't available for this portal

This issue occurs when the **Profile** site marker isn't available in your portal configuration. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Create a new site marker with the following values: 
    - **Name**: Profile
    - **Website**: Select the website of your portal host.
    - **Page**: Select the webpage record that is set as the profile page of your portal.

#### The Profile site marker isn't pointing to any webpage

This issue occurs when the **Profile** site marker is available but isn't pointing to any webpage. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Find the **Profile** site marker record.
1. Update the **Page** field to point to an active profile page of your portal.

#### The Profile site marker is pointing to a deactivated webpage

This issue occurs when the **Profile** site marker is available, but is pointing to a deactivated webpage. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Find the **Profile** site marker record.
1. Update the **Page** field to point to an active profile page of your portal.

### Page Not Found site marker configuration

The following issues relate to site marker configuration to the **Page Not Found** webpage.

#### An active Page Not Found site marker isn't available for this portal

This issue occurs when the **Page Not Found** site marker isn't available in your portal configuration. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Create a new site marker with the following values: 
    - **Name**: Page Not Found
    - **Website**: Select the website of your portal host.
    - **Page**: Select the webpage record that is set as the Page Not Found page of your portal.

#### The Page Not Found site marker isn't pointing to any webpage

This issue occurs when the **Page Not Found** site marker is available but isn't pointing to any webpage. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Find the **Page Not Found** site marker record.
1. Update the **Page** field to point to an active Page Not Found page of your portal.

#### The Page Not Found site marker is pointing to a deactivated webpage

This issue occurs when the **Page Not Found** site marker is available, but is pointing to a deactivated webpage. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Find the **Page Not Found** site marker record.
1. Update the **Page** field to point to an active Page Not Found page of your portal.

### Access Denied site marker configuration

The following issues relate to site marker configuration to the **Access Denied** page.

#### An active Access Denied site marker isn't available for this portal

This issue occurs when the **Access Denied** site marker isn't available in your portal configuration. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Create a new site marker with the following values: 
    - **Name**: Access Denied
    - **Website**: Select the website of your portal host.
    - **Page**: Select the webpage record that is set as the Access Denied page of your portal.

#### The Access Denied site marker isn't pointing to any webpage

This issue occurs when the **Access Denied** site marker is available but isn't pointing to any webpage. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Find the **Access Denied** site marker record.
1. Update the **Page** field to point to an active Access Denied page of your portal.

#### The Access Denied site marker is pointing to a deactivated webpage

This issue occurs when the **Access Denied** site marker is available, but is pointing to a deactivated webpage (root or content page can be deactivated). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. Find the **Access Denied** site marker record.
1. Update the **Page** field to point to an active Access Denied page of your portal.

### Search site marker availability

The following issues relate to site marker configuration to the site search page.

#### An active Search site marker isn't available for this portal

This issue occurs when the **Search** site marker isn't available in your portal configuration. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Site Markers**.
1. If a site marker named **Search** is available and deactivated, activate it.
1. If not available, create a new site marker with following values:
    - **Name**: Search
    - **Website**: Select the website of your portal host.
    - **Page**: Select the webpage record that is set as the search page of your portal.
1. Select **Save & Close**.

## Web files

The following are issues when configuring [web files](../configure/web-files.md).

### Web file isn't active

To fix this issue, ensure that the web file is in the active state.

### The partial URL of a web file is misconfigured

To fix this issue, ensure that the partial URL is the file name with Home as the root page.

### Web file doesn't have a file attachment

To fix this issue, add the corresponding CSS file in the notes section of the web file.

### File attachment doesn't have content

To fix this issue, add the CSS file with its entire contents in the notes section of the web file.

### MIME type of file isn't text/CSS

To fix this issue, ensure that there are no plug-ins or flows that override the MIME type of the CSS files.

## Webpages

The following issues relate to [webpages](../configure/web-page.md).

### Webpage associated a localized content page as a parent webpage  

This issue occurs when a [webpage](../configure/web-page.md) record has its **Parent Webpage** associated to a [language content page](../configure/enable-multiple-language-support.md#create-content-in-multiple-languages). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the webpages [listed](portal-checker.md#identifying-web-pages-listed-in-diagnostic-results) in the Portal Checker diagnostic results.
1. Update the **Parent Page** field to point to a valid webpage record that isn't a content page.

### Webpage belongs to different website

This issue occurs when a parent [webpage](../configure/web-page.md) is associated with a different [website](../configure/websites.md) than a child webpage. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the webpages (either parent webpage or children webpages) [listed](portal-checker.md#identifying-web-pages-listed-in-diagnostic-results) in the Portal Checker diagnostic results.
1. Update the **Web site** field to point to the appropriate website.

### Webpage doesn't have a publishing state

This issue occurs when a [webpage](../configure/web-page.md) record doesn't have a corresponding [publishing state](../configure/publishing-states.md). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the webpages [listed](portal-checker.md#identifying-web-pages-listed-in-diagnostic-results) in the Portal Checker diagnostic results.
1. Update the **Publishing State** field to point to a publishing state record. 

### Webpage has a page template that belongs to a different website

This issue occurs when a [page template](../configure/page-templates.md) is associated with a different [website](../configure/websites.md). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the webpages [listed](portal-checker.md#identifying-web-pages-listed-in-diagnostic-results) in the Portal Checker diagnostic results.
1. Update the **Web site** field to point to the appropriate website.
1. Alternatively, update the **Page Template** to point to a page template in the same website.

### Webpage has a publishing state that belongs to a different website

This issue occurs when a [publishing state](../configure/publishing-states.md) is associated with a different [website](../configure/websites.md). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the webpages [listed](portal-checker.md#identifying-web-pages-listed-in-diagnostic-results) in the Portal Checker diagnostic results.
1. Update the **Publishing State** field to point to a publishing state record in the same website. 

### Webpage is trying to use an inactive page template

This issue occurs when the [page template](../configure/page-templates.md) record is inactive. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the webpages [listed](portal-checker.md#identifying-web-pages-listed-in-diagnostic-results) in the Portal Checker diagnostic results.
1. Select the **Page Template** record to navigate to the record.
1. Select **Activate** from the command bar.
1. Alternatively, update the **Page Template** to point to an active page template in the webpage.

### Webpage needs at least one active localized language content page

This issue occurs when the [webpage](../configure/web-page.md) doesn't have at least one [language content page](../configure/enable-multiple-language-support.md#create-content-in-multiple-languages). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the webpages [listed](portal-checker.md#identifying-web-pages-listed-in-diagnostic-results) in the Portal Checker diagnostic results.
1. Scroll down to the **Localized Content** section.
1. Select **+ New Web Page** to create a new language content page.

   > [!Note]
   > The configuration fields on the home page of a content page are not inherited to the existing content pages. They are used only in creation of new content pages. You must update the content page configurations individually.

### Webpage publishing is hidden

This issue occurs when the [publishing state](../configure/publishing-states.md) **IsVisible** field isn't checked. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the webpages [listed](portal-checker.md#identifying-web-pages-listed-in-diagnostic-results) in the Portal Checker diagnostic results.
1. Select the **Publishing State** record to navigate to the record.
1. Select the **IsVisible** field and make sure that it's checked (set to true).

### Webpage without a page template

This issue occurs when a [webpage](../configure/web-page.md) record doesn't have a corresponding [page template](../configure/page-templates.md). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the webpage [listed](portal-checker.md#identifying-web-pages-listed-in-diagnostic-results) in the Portal Checker diagnostic results.
1. Update the **Page Template** field to point to an active page template record.

## See also

[Run Portal Checker](portal-checker.md)
