---
title: Portal Checker performance
description: Learn about Portal Checker diagnostics results related to performance.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 05/26/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - dileepsinghmicrosoft
    - ProfessorKendrick
---

# Portal Checker performance

In this article, you'll learn about Portal Checker diagnostics results related to performance issues, and how to resolve common issues or problems.

## Webpage tracking enabled

Enabling a portal webpage for page tracking can lead to performance issues in your portal. 

> [!IMPORTANT]
> This functionality has been retired for portals with version [9.3.4.x](../versions/version-9.3.4.x.md) or later. For more information, see the deprecation announcement published earlier: [Dynamics 365 Portals - Deprecated Features](https://blogs.msdn.microsoft.com/crm/2018/03/20/portal-capabilities-for-dynamics-365-deprecated-features/).

The Portal Checker tool will list all the webpages (both root and content page) that are enabled for page tracking. These pages should be disabled by following these steps:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. Go to **Advanced find**.
1. Search for all the webpages where the **Enable Tracking (Deprecated)** field is enabled (value is set to Yes).
1. Bulk edit all the pages and set this field to **No**.

You also can go to each page listed in the Portal Checker results and set the value of the **Enable Tracking (Deprecated)** field to **No** instead.

It's important to understand that if you're on Dynamics 365 Portals solution version 9.x, this field won't be displayed on the form and you might need to add it to the form first. 

## Web file tracking enabled

Enabling a portal web file for page tracking can lead to performance issues in your portal. 

> [!IMPORTANT]
> This functionality has been retired for portals with version [9.3.4.x](../versions/version-9.3.4.x.md) or later. For more information, see the deprecation announcement published earlier: [Dynamics 365 Portals - Deprecated Features](https://blogs.msdn.microsoft.com/crm/2018/03/20/portal-capabilities-for-dynamics-365-deprecated-features/).

The Portal Checker tool will list all the web files that are enabled for page tracking. These files should be disabled by following these steps:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. Go to **Advanced find**.
1. Search for all the web files where the **Enable Tracking (Deprecated)** field is enabled (value is set to Yes).
1. Bulk edit all the records and set this field to **No**.

You also can go to each file listed in the Portal Checker results and set the value of the **Enable Tracking (Deprecated)** field to **No**. If you're on portal solution version 9.x, this field won't be displayed on the form and you might need to add it to the form first. 

## Sign-in tracking enabled

Enabling portal sign-in tracking can lead to performance issues in your portal. 

> [!IMPORTANT]
> This functionality has been retired for portals with version [9.3.4.x](../versions/version-9.3.4.x.md) or later. For more information, see the deprecation announcement published earlier: [Dynamics 365 Portals - Deprecated Features](https://blogs.msdn.microsoft.com/crm/2018/03/20/portal-capabilities-for-dynamics-365-deprecated-features/).

The Portal Checker tool will check to see if sign-in tracking is enabled for your portal and show a failed check if it's enabled. Sign-in tracking should be disabled by following these steps:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. Go to **Portals** > **Site Settings**.
1. Search for the site setting `Authentication/LoginTrackingEnabled`.
1. Change the value of this site setting to **False** or delete the site setting.
1. Restart the portal. 

## Header output cache is disabled

Disabling header output cache on your portal can lead to performance issues in your portal during high load. More details about this functionality can be found at [Enable header and footer output caching on a portal](../configure/enable-header-footer-output-caching.md).

The Portal Checker tool will check to see if header output cache is disabled on your portal and show a failed check if it's disabled. To enable it:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. Go to **Portals** > **Site Settings**.
1. Search for the site setting `Header/OutputCache/Enabled`.
1. If the site setting is available, change the value to **True**. If the site setting isn't available, create a new site setting with this name and set its value to **True**.
1. Restart the portal. 

## Footer output cache is disabled

Disabling footer output cache on your portal can lead to performance issues in your portal during high load. More details about this functionality can be found at [Enable header and footer output caching on a portal](../configure/enable-header-footer-output-caching.md).

The Portal Checker tool will check to see if footer output cache is disabled on your portal and show a failed check if it's disabled. To enable it:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. Go to **Portals** > **Site Settings**.
1. Search for the site setting `Footer/OutputCache/Enabled`.
1. If the site setting is available, change the value to **True**. If the site setting isn't available, create a new site setting with this name and set its value to **True**.
1. Restart the portal. 

## Large number of web file records

The web file table is used by a portal to store any static files you want to use on your portal. The main use case of this table is to store static content of your website such as CSS, JavaScript, image files, and so on. However, having a large number of these files can cause slowness during the startup of your portal.

The Portal Checker tool will check for this scenario and provide you an indication if you have more than 500 active web files in your portal. If all of these files represent static content, you can take the following actions to mitigate this issue:

- Use an external file server like Azure Blob Storage or Azure Content Delivery Network to store these files and then reference these files on the appropriate pages either within the page or in an underlying template.

- If you can't move files outside, ensure that all the files aren't loaded along with the home page. A web file is loaded along with the home page if the parent page of that file is set to home. To avoid this scenario, do the following:

  1. Create a dummy webpage with no content and a blank template. This page would be used to create a direct path to your web files. 
  1. For all the web files that aren't needed on the home page, change the parent page to this dummy webpage. Once done, the full path to your web file would be `Portal URL/{dummy_webpage}/{web file}`.
  1. Reference your web file directly in the HTML of the page template or web template of the page where you want to use it. This will load your file on demand on that page. 

## Basic form lookup configuration 

Enabling a lookup to render as a dropdown mode in basic forms or advanced forms can lead to performance issues if the number of records shown in the dropdown list exceeds 200 and the records are changed frequently. Use this option for only static lookups, such as country and state lists, having a limited number of records.

When this option is enabled for lookups that can have a large number of records, it will slow the load time of the webpage on which the basic form is available. When this page is used by many users and loaded many times, it can slow the entire website by using website resources to render this page. For these situations, a full lookup experience should be used, or a custom HTML control that calls an AJAX endpoint (created using web templates) should be built for the wanted look and feel.

## Number of web roles

Web roles are used in portals to enable role-based access control. Typically, the number of web roles in a portal are limited as the number of different combinations of permissions would be limited as well. If the number of web roles exceeds 100 in your portal, it can cause performance issues that affect all pages of your portal. 

### See also

[Run Portal Checker](portal-checker.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
