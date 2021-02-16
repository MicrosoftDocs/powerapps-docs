---
title: Analyze Portal Checker results, and resolutions to common issues found.
description: Learn about Portal Checker results, how to analyze them, and resolve issues or problems found by Portal Checker.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 02/08/2021
ms.author: nenandw
ms.reviewer: tapanm
---

# Analyze and resolve Portal Checker diagnostics results

In this article, you'll learn about the Portal Checker diagnostics results, and how to resolve them.

## Portal doesn't load and displays a generic error page (Server Error in "/" application) 

This issue can be caused by different kinds of reasons like when a portal isn't able to connect to the underlying Dataverse environment, Dataverse environment doesn't exist, or its URL has changed, when request to Dataverse environment is timed out, and so on. When you run the portal checker tool, it will try to determine the exact reason and will point you to the correct mitigation. 

Below is a list of most common causes and their corresponding mitigation steps:

### URL of the connected Dataverse environment has changed 

This happens when the URL of Dataverse environment is changed by a user after portal is provisioned against the organization. To fix this issue, update the Dynamics 365 URL:

1. Open [Power Apps Portals admin center](admin-overview.md).
2. Go to **Portal Actions** > **Update Dynamics 365 URL**. 

Once this action is successfully executed, your Dataverse environment URL will be updated and portal will start working.

### Dataverse environment connected to your portal is in administration mode

This issue occurs when the Dataverse environment is put in administration mode either when changing organization from production to sandbox mode or manually by an organization administrator.

If this is the cause, you can disable administration mode by doing actions listed [here](https://docs.microsoft.com/dynamics365/admin/manage-sandbox-instances#administration-mode). Once administration mode is disabled, portal will work fine.

### Authentication connection between Dataverse environment and portal is broken

This issue occurs when the authentication connection between Dynamic 365 organization and portal is broken because either Dataverse environment was restored from a backup or was deleted and recreated from a backup. To fix this issue:

1. Open [Power Apps Portals admin center](admin-overview.md).
2. In the **Portal Details** tab, select **Off** from the **Portal State** list.
3. Select **Update**.
4. Select **On** from the **Portal State** list.
5. Select **Update**. The portal restarts and can now make authentication connection.

In certain situations, especially if the organization ID has changed after the restore operation (or if you reprovisioned the organization), these mitigation steps won't work. In those situations, you can reset and reprovision the portal against the same instance. For information on how to reset a portal, see [Reset a portal](reset-portal.md).

### Request to Dataverse environment has timed out

This issue is typically a transient issue that can occur if the API requests to your Dataverse environment has timed out. This issue will automatically mitigate itself once the API requests starts working. To mitigate this issue, you can also try restarting the portal:

1. Open [Power Apps Portals admin center](admin-overview.md).
2. Go to **Portal Actions** > **Restart**.

If restarting the portal doesn't work and this issue is occurring for a long period of time, contact Microsoft support for help.

### Website binding not found

This issue occurs when the website binding records for portal are deleted from the underlying Dataverse environment and portal isn't able to create binding automatically. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
2. Go to **Portals** > **Website Bindings**.
3. Delete all the website binding records that are pointing to your portal. The **Sitename** field helps you to identify website binding records of your portal.
4. After you delete all website binding records, restart the portal.

Once you complete the above steps, your portal will restart and will recreate website binding record automatically.

There are situations in which portal won't be able to recreate website binding record automatically when the GUID of the website record available in your instance is different than the one created during default installation of portal. In this situation, do the following steps:

1. Delete all website binding records related to your portal.

2. Create a website binding record manually with following values:

      - **Name**: Can be any string
      - **Website**: Select the website record that you want to be rendered on portal
      - **Sitename**: Type in the hostname of your portal i.e Portal URL without `https://` in the beginning. If your Portal is using custom domain name, then use custom domain name here.
      - Leave all other fields blank.

3. Once website binding record is recreated, restart your portal from Power Apps Portals admin center.

### An unexpected error has occurred while trying to connect to your Dataverse environment

This situation can arise because of some unexpected issue. To mitigate in this situation, you can either try resetting or reprovisioning the portal. For information on how to reset a portal, see [Reset a portal](reset-portal.md).

If portal reset and reprovision doesn't solve this issue, contact Microsoft support for help.

## Portal isn't displaying updated data from Dataverse environment

Any data displayed on portal is rendered from the portal cache. This cache gets updated whenever data in Dataverse environment is updated. However, this process is asynchronous and can take upto 15 minutes. If the changes are made in the metadata entity of portal, for example, web pages, web files, content snippet, site setting, and so on, it's advised to clear cache manually or restart the portal from Power Apps Portals admin center. For information on how to clear cache, see [Clear the server-side cache for a portal](clear-server-side-cache.md). 

However, if you're seeing stale data for a long time in non-portal metadata entities, it can be because of variety of issues listed below:

### Entities not enabled for cache invalidation

If you're seeing stale data only for certain entities and not for everything, this can be because the Change Tracking metadata isn't enabled on that specific entity.

If you run the Portal checker (self-service diagnostic) tool, it will list down Object Type code of all the entities that are referenced on portal in entity list or entity forms and web forms and aren't enabled for change tracking. Browse your metadata by using the steps mentioned at [Browse the metadata for your organization](https://docs.microsoft.com/dynamics365/customerengagement/on-premises/developer/browse-your-metadata)

If you're experiencing stale data issue in any of these entities, you can enable change tracking by using Power Apps Portals admin center. UI or Dynamics 365 API. More information:  [Enable change tracking for an entity](https://docs.microsoft.com/dynamics365/customerengagement/on-premises/developer/use-change-tracking-synchronize-data-external-systems#enable-change-tracking-for-an-entity)

### Organization not enabled for change tracking

Apart from each entity being enabled for change tracking, organizations on a whole have to be enabled for change tracking as well. An organization is enabled for change tracking when a portal provisioning request is submitted. However, this can break if an organization is restored from an old database or reset. To fix this issue:

1. Open [Power Apps Portals admin center](admin-overview.md).
2. In the **Portal Details** tab, select **Off** from the **Portal State** list.
3. Select **Update**.
4. Select **On** from the **Portal State** list.
5. Select **Update**. The portal restarts and can now make the authentication connection.

### I'm getting "Page Not Found" error and the page content is different from the default Page Not Found site marker or web page.

You may see a *Page Not Found* error message that may appear different from the default error page content available by default on the **Page Not Found** site marker and web page.

![Page Not Found](media/page-not-found.png "Page Not Found")

This *Page Not Found* page is a system page and appears if: 

- The default **Page Not Found** site marker is configured incorrectly.
- The default **Page Not Found** site marker is deleted.
- The default **Page Not Found** web page is deleted.

To resolve this error, ensure that you have the default site marker named **Page Not Found** present and configured correctly. If the site marker is present and correctly configured, check if the **Page Not Found** web page is selected for the site marker or whether the **Page Not Found** web page is present or not.

For steps to create a site marker for **Page Not Found**, go to [An active Page Not Found site marker isn't available for this portal](#an-active-page-not-found-site-marker-isnt-available-for-this-portal).

For steps to check site marker configuration and ensure it points to the correct web page, go to [The Page Not Found site marker isn't pointing to any webpage](#the-page-not-found-site-marker-isnt-pointing-to-any-webpage).

For steps to change the site marker to point to the correct **Page Not Found** web page, go to [The Page Not Found site marker is pointing to a deactivated web page](#the-page-not-found-site-marker-is-pointing-to-a-deactivated-web-page).

## Web page tracking enabled

Enabling a portal web page for page tracking can lead to performance issues in your portal. This functionality is deprecated since January 2018 release of Dynamics 365 Portals. More information: [Dynamics 365 Portals: Deprecated Features](https://blogs.msdn.microsoft.com/crm/2018/03/20/portal-capabilities-for-dynamics-365-deprecated-features/)

The portal checker tool will list all the web pages (both root and content page) which are enabled for page tracking. These pages should be disabled by following these steps:

1. Open the [Portal Management app](../configure/configure-portal.md).
2. Go to Advanced find.
3. Search for all the web pages where **Enable Tracking (Deprecated)** field is enabled (value is set to Yes).
4. Bulk edit all the pages and set this field to **No**.

You can also go to each page listed in portal checker result and set the value of **Enable Tracking (Deprecated)** field to **No** instead.

It's important to understand that if you're on Dynamics 365 Portals solution version 9.x, this field won't be displayed on the form and you might need to add it to the form first. 

## Web file tracking enabled

Enabling a portal web file for page tracking can lead to performance issues in your portal. This functionality is deprecated since January 2018 release of Dynamics 365 Portals. More information: [Dynamics 365 Portals: Deprecated Features](https://blogs.msdn.microsoft.com/crm/2018/03/20/portal-capabilities-for-dynamics-365-deprecated-features/)

The portal checker tool will list all the web files that are enabled for page tracking. These files should be disabled by following these steps:

1. Open the [Portal Management app](../configure/configure-portal.md).
2. Go to Advanced find.
3. Search for all the web files where **Enable Tracking (Deprecated)** field is enabled (value is set to Yes).
4. Bulk edit all the records and set this field to **No**.

You can also go to each file listed in portal checker result and set the value of **Enable Tracking (Deprecated)** field to **No** instead. It's important to understand that if you're on Portal solution version 9.x, this field won't be displayed on the form and you might need to add it to the form first. 

## Login tracking enabled

Enabling a portal login tracking can lead to performance issues in your portal. This functionality is deprecated since January 2018 release of Dynamics 365 Portals. More information: [Dynamics 365 Portals: Deprecated Features](https://blogs.msdn.microsoft.com/crm/2018/03/20/portal-capabilities-for-dynamics-365-deprecated-features/)

The portal checker tool will check if login tracking is enabled for your portal and will show a failed check if it's enabled. Login tracking should be disabled by following these steps:

1.    Open the [Portal Management app](../configure/configure-portal.md).
2.    Go to **Portals** > **Site Settings**.
3.    Search for site setting named `Authentication/LoginTrackingEnabled`.
4.    Change the value of this site setting to **False** or delete the site setting.
5.    Restart the portal. 

## Header output cache is disabled

Disabling header output cache on your portal can lead to performance issues in your portal during high load. More details around this functionality can be found at: [Enable header and footer output caching on a portal](../configure/enable-header-footer-output-caching.md)

The portal checker tool will check if header output cache is disabled on your portal and will show a failed check if it's disabled. To enable it:

1.	Open the [Portal Management app](../configure/configure-portal.md).
2.	Go to **Portals** > **Site Settings**.
3.	Search for site setting named `Header/OutputCache/Enabled`.
4.	If the site setting is available, change the value of Site setting to **True**. If the site setting isn't available, create a new site setting with this name and set its value to **True**.
5.	Restart the portal. 

## Footer output cache is disabled

Disabling footer output cache on your portal can lead to performance issues in your portal during high load. More details around this functionality can be found at: [Enable header and footer output caching on a portal](../configure/enable-header-footer-output-caching.md)

The portal checker tool will check if footer output cache is disabled on your portal and will show a failed check if it's disabled. To enable it:

1.	Open the [Portal Management app](../configure/configure-portal.md).
2.	Go to **Portals** > **Site Settings**.
3.	Search for site setting named `Footer/OutputCache/Enabled`.
4.	If the site setting is available, change the value of Site setting to **True**. If the site setting isn't available, create a new site setting with this name and set its value to **True**.
5.	Restart the portal. 

## Large number of web file records

The web file entity is used by a portal to store any static files you want to use on your portal. Main use case of this entity is to store static content of your website like CSS, JavaScript, image files, and so on. However, having many such files can cause slowness during the startup of your portal.

The portal checker tool will check for this scenario and will provide you an indication if you've more than 500 active web files in your portal. If all of these files represent static content like CSS, JavaScript, image files, and so on, you can take following actions to mitigate this issue.

- Use an external file server like Azure blob storage or CDN to store these files and then reference these files on the appropriate pages either within the page or in underlying template.

- If you can't move files outside, ensure that all the files aren't loaded along with home page. A web file is loaded along with home page if the parent page of that file is set to home. To avoid this scenario, you can do the following steps:

  1. Create a dummy web page with no content and a blank template. This page would be used to create a direct path to your web files. 
  2. For all the web files that aren't needed on home page, change the parent page to this dummy webpage. Once done, full path to your web file would be `Portal URL/{dummy_webpage}/{web file}`
  3. Reference your web file directly in the HTML of the page template or web template of the page where you want to use it. This will load your file on demand on that page. 

## Loading static resources (css/js) asynchronously

When working on portal implementation, it's important to understand that you completely manage the HTML of the page. That means, the standard web development practices should be followed to ensure that your webpage's client side performance isn't affected.

One of the most common cause of performance issues on webpages is loading a lot of static resources (css/js) synchronously on the load of the page. Synchronous loading of large no of css/js files can lead to long client-side processing time for your webpages.

In portals, whenever you're associating a web file directly to the home page, it creates a dependency in the generated HTML. This means that web file always loaded along with the home page. If this web file is a css/js file, this would be loaded synchronously and can slow down your client-side processing time.

To avoid this, you can do the following steps:

1. If a web file isn't needed on the home page, make sure its parent page isn't set as home page and reuse the mechanism described above to load it on demand.
2. While loading a JavaScript file on demand on any page, use `<async>` or `<defer>` HTML attribute to load the file asynchronously.
3. While loading a CSS file on demand, you can use `<preload>` HTML attribute (https://www.w3.org/TR/preload/) or JavaScript based approach since preload isn't supported on all the browsers yet.

## Entity form lookup configuration 

Enabling a lookup to render as a drop-down mode in entity forms or web forms can be performance intensive if the number of records shown in the drop-down exceed 200 and are changed frequently. Use this option for only static lookups, such as country list and state list, having a limited number of records.

If this option is enabled for lookups that can have large number of records, it will slow down the load time of the webpage on which entity form is available. If this page is used by a lot of users and is loaded a lot of times, it can slow down the whole website and the website resources would be used to render this page. For these situations, full lookup experience should be used or a custom HTML control that calls an AJAX endpoint (created using web templates) should be built for the wanted look and feel.

## Number of web roles

Web roles are used in portals to enable role-based access control. Typically, the number of web roles in a portal are limited as the number of different combinations of permissions would be limited as well. If the number of web roles exceed 100 in your portal, it can cause performance issues that can affect all pages of your portal.

## An active Home site marker isn't available for this portal

This issue occurs when the **Home** site marker isn't available in your portal configuration. To fix this issue:

1.	Open the [Portal Management app](../configure/configure-portal.md).
2.	In the left pane, select **Site Markers**.
3.	Create a new site marker with following values:
    - **Name**: Home
    - **Website**: Select the website of your portal host.
    - **Page**: Select the webpage record that is set as the home page of your portal.

## The Home site marker isn't pointing to any webpage

This issue occurs when the **Home** site marker is available but isn't pointing to any webpage. To fix this issue:

1.    Open the [Portal Management app](../configure/configure-portal.md).
2.    In the left pane, select **Site Markers**.
3.    Find the **Home** site marker record.
4.    Update the **Page** field to point to an active home page of your portal.

## The Home site marker is pointing to a deactivated web page

This issue occurs when the **Home** site marker is available, but is pointing to a deactivated webpage. To fix this issue:

1.    Open the [Portal Management app](../configure/configure-portal.md).
2.    In the left pane, select **Site Markers**.
3.    Find the **Home** site marker record.
4.    Update the **Page** field to point to an active home page of your portal.

## The Home site marker isn't pointing to home page of the portal

This issue occurs when the **Home** site marker is available, but is pointing to a webpage that isn't a home page of your portal. To fix this issue:

1.    Open the [Portal Management app](../configure/configure-portal.md).
2.    In the left pane, select **Site Markers**.
3.    Find the **Home** site marker record.
4.    Update the **Page** field to point to an active home page of your portal.

## An active Profile site marker isn't available for this portal

This issue occurs when the **Profile** site marker isn't available in your portal configuration. To fix this issue:

1.	Open the [Portal Management app](../configure/configure-portal.md).
2.	In the left pane, select **Site Markers**.
3.	Create a new site marker with following values: 
    - **Name**: Profile
    - **Website**: Select the website of your portal host.
    - **Page**: Select the webpage record that is set as the profile page of your portal.

## The Profile site marker isn't pointing to any webpage

This issue occurs when the **Profile** site marker is available but isn't pointing to any webpage. To fix this issue:

1.    Open the [Portal Management app](../configure/configure-portal.md).
2.    In the left pane, select **Site Markers**.
3.    Find the **Profile** site marker record.
4.    Update the **Page** field to point to an active profile page of your portal.

## The Profile site marker is pointing to a deactivated web page

This issue occurs when the **Profile** site marker is available, but is pointing to a deactivated webpage. To fix this issue:

1.    Open the [Portal Management app](../configure/configure-portal.md).
2.    In the left pane, select **Site Markers**.
3.    Find the **Profile** site marker record.
4.    Update the **Page** field to point to an active profile page of your portal.

## An active Page Not Found site marker isn't available for this portal

This issue occurs when the **Page Not Found** site marker isn't available in your portal configuration. To fix this issue:

1.	Open the [Portal Management app](../configure/configure-portal.md).
2.	In the left pane, select **Site Markers**.
3.	Create a new site marker with following values: 
    - **Name**: Page Not Found
    - **Website**: Select the website of your portal host.
    - **Page**: Select the webpage record that is set as the Page Not Found page of your portal.

## The Page Not Found site marker isn't pointing to any webpage

This issue occurs when the **Page Not Found** site marker is available but isn't pointing to any webpage. To fix this issue:

1.    Open the [Portal Management app](../configure/configure-portal.md).
2.    In the left pane, select **Site Markers**.
3.    Find the **Page Not Found** site marker record.
4.    Update the **Page** field to point to an active Page Not Found page of your portal.

## The Page Not Found site marker is pointing to a deactivated web page

This issue occurs when the **Page Not Found** site marker is available, but is pointing to a deactivated webpage. To fix this issue:

1.    Open the [Portal Management app](../configure/configure-portal.md).
2.    In the left pane, select **Site Markers**.
3.    Find the **Page Not Found** site marker record.
4.    Update the **Page** field to point to an active Page Not Found page of your portal.

## An active Access Denied site marker isn't available for this portal

This issue occurs when the **Access Denied** site marker isn't available in your portal configuration. To fix this issue:

1.	Open the [Portal Management app](../configure/configure-portal.md).
2.	In the left pane, select **Site Markers**.
3.	Create a new site marker with following values: 
    - **Name**: Access Denied
    - **Website**: Select the website of your portal host.
    - **Page**: Select the webpage record that is set as the Access Denied page of your portal.

## The Access Denied site marker isn't pointing to any webpage

This issue occurs when the **Access Denied** site marker is available but isn't pointing to any webpage. To fix this issue:

1.    Open the [Portal Management app](../configure/configure-portal.md).
2.    In the left pane, select **Site Markers**.
3.    Find the **Access Denied** site marker record.
4.    Update the **Page** field to point to an active Access Denied page of your portal.

## The Access Denied site marker is pointing to a deactivated web page

This issue occurs when the **Access Denied** site marker is available, but is pointing to a deactivated webpage (root or content page can be deactivated). To fix this issue:

1.    Open the [Portal Management app](../configure/configure-portal.md).
2.    In the left pane, select **Site Markers**.
3.    Find the **Access Denied** site marker record.
4.    Update the **Page** field to point to an active Access Denied page of your portal.

## Profile web form isn't available for contact entity

Profile page is one of the common pages used in your portal for all profile related issues. This page shows a form that can be used by users to update their profile. Form used on this page comes from the **Profile Web Page** main form available in the Contact entity. This form is created in your Dataverse environment when portal is provisioned. This error is displayed when the **Profile** web form is either deleted or disabled in your portal. This form is mandatory and deleting or disabling this form can break the whole website displaying runtime error on portal. This is an irreparable state and requires portal to be reinstalled in the environment.

## Published state isn't available for this website

To fix this issue, ensure that the publishing state entity **Published** is available and active.

## Published state isn't visible

To fix this issue, ensure that the publishing state entity **Published** has the **isVisible** check box is selected.

## List of entities with search result having invalid URL

To fix this issue, ensure that your entity has appropriate security permission.

## List of entities with CMS security check failed

To fix this issue, ensure that your entity has proper search page.

## Web file isn't active

To fix this issue, ensure that the web file is in active state.

## The partial URL of web file is misconfigured

To fix this issue, ensure that the partial URL is the file name with Home as the root page.

## Web file doesn't have a file attachment

To fix this issue, add the corresponding CSS file in the notes section of the web file.

## File attachment doesn't have content

To fix this issue, add the CSS file with entire content in the notes section of the web file.

## MIME type of file isn't text/css

To fix this issue, ensure that there are no plugins or flows that override the MIME type of the CSS file(s).

### See also

[Run Portal Checker](portal-checker.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]