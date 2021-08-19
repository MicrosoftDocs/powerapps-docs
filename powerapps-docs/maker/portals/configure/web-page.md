---
title: Manage web pages
description: Learn how to manage web pages in a portal.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/19/2021
ms.subservice: portals
ms.author: sandhan
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - sandhangitmsft
---

# Manage web pages

A web page represents a particular URL in a portals website, and is one of the core tables of the portals content management system. Through parent and child relationships to other web pages, this basic forms the hierarchy of a website (i.e., its site map).

Web pages also form the basis for including other, specialized table types in the portal site map – web files, shortcuts, forums, advanced forms, and blogs are all situated in the portal site map through – and thus derive their URLs from – a relationship to a parent web page.

## Manage web pages

Web pages can be created, edited, and deleted from the Power Apps portals Studio. However, advanced customization can be performed from the Portal Management app.  

1. Open the [Portal Management app](configure-portal.md).

2. Go to **Portals** > **Web Pages**.

3. To edit an existing web page, select the web page name.

4. Enter appropriate values in the fields.

5. Select **Save & Close**.

### Web page attributes

The table below explains many of the standard web page attributes used by portals. It is important to note that the way in which many of the content/display-oriented attributes are rendered is controlled by the page template used, and thus by the portal developer.


|        Name         |                                                                                                                                                                                                                                                                                                                                   Description                                                                                                                                                                                                                                                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        Name         |                                                                                                                                                                                                                                                     The descriptive name of the table. This value will be used as the page title in most templates, particularly if a Title value is not provided. This field is required.                                                                                                                                                                                                                                                     |
|       Website       |                                                                                                                                                                                                                                                                                                        The Website to which the table belongs. This field is required.                                                                                                                                                                                                                                                                                                         |
|     Parent Page     |                                                                                                                                                                                                                                                      The parent web page of the table, in the website content hierarchy. <br>All web pages should have a parent page except for the single root (Home) page of a website.                                                                                                                                                                                                                                                      |
|     Partial URL     | The URL path segment used to build the portal URL of this page. <br>The single root (Home) page of your website – the single page that has no associated Parent Page – must have a Partial URL value of /.<br>Partial URL values are used as URL path segments. As such, they should not contain illegal URL path characters, such as ?, #, !, %. Since portals URLs are generated by joining together Partial URL values with slashes (/), they should also not generally contain slashes. Recommended practice would be to restrict Partial URL values to letters, numbers, and hyphens or underscores. For example: press-releases, Users_Guide, product1. |
|    Page Template    |                                                                                                                                                                                                                                                                                             The Page Template to be used to render this page on the portal. This field is required.                                                                                                                                                                                                                                                                                             |
|  Publishing State   |                                                                                                                                                 The current publishing workflow state of the page, which may dictate whether or not the page is visible on the site. The most common use of this feature is to provide published/draft control over content.<br>Users with content management permissions may be granted the ability to use Preview Mode, which allows these users to see (preview) unpublished content.                                                                                                                                                  |
|    Display Date     |                                                                                                                                                                                                         This attribute is a date/time value that can be used by a template, purely for display purposes. It has no functional implications, but can be useful for things like, for example, manually specifying a published date on a press release or news item page.                                                                                                                                                                                                          |
|    Release Date     |                                                                                                             Controls a date/time after which the page will be visible on the portal. If the current date/time is prior to this date, this page will not be visible. (The exception to this is that users with content management permissions may be granted the ability to use Preview Mode, which allows these users to see (preview) unreleased content.) This is useful for controlling the release of time-sensitive content, like news or press releases.                                                                                                              |
|   Expiration Date   |                                                                                                                                                                Controls a date/time prior to which the page will be visible on the portal. If the current date/time is after this date, this page will not be visible. (The exception to this is that users with content management permissions may be granted the ability to use Preview Mode, which allows these users to see (preview) expired content.)                                                                                                                                                                 |
|      Advanced Form       |                                                                                                                                                                                                                                                                                                                   The Advanced Form to be displayed on this page.                                                                                                                                                                                                                                                                                                                    |
|        Title        |                                                                                                                                                                   An optional title for the page. If this field is provided, this value will be used on the portal, instead of the Name field. This is useful in the case that you want a different title to appear on the portal, while having the Name be useful for content authors and users.                                                                                                                                                                   |
|       Summary       |                                                                                                                                                                                                                                                      A short description for the page, this value will generally be used to add a description of the page to portal navigational elements that render a link to the page.                                                                                                                                                                                                                                                       |
|        Copy         |                                                                                                                                                                                                                                                                                                                    The main HTML content field of the page.                                                                                                                                                                                                                                                                                                                     |
| Hidden from Sitemap |                                                                                                                                                                                                        Controls whether or not the page is visible has part of the portal site map. If this value is checked, the page will still be available on the site at its URL, and can be linked to, but standard navigational elements (menus, etc.) will not include the page.                                                                                                                                                                                                        |
|       Author        |                                                                                                                                                                                                                                  A Contact record representing the author of the page. This value is generally used for administrative purposes, but this information could be rendered on a portal, if the page's Page Template supports it.                                                                                                                                                                                                                                   |
|    Display Order    |                                                                                                                                                                                       An integer value indicating the order in which the page will be placed, relative to other tables with the same Parent Page. This controls the ordering of pages and other site map tables when, for example, a list of links to the child tables of a given page are rendered on the portal.                                                                                                                                                                                        |
|     Navigation      |                                                                       A Web Link Set record. This is used by the WebLinkNavigationPage.aspx Page Template to render a list of navigation links on the left hand side of the page. Create a Page Template in CRM and specify the Rewrite Url property as ~/Pages/WebLinkNavigationPage.aspx. Set the Web Page's Page Template to this template record. This is typically done to the parent page only and all child pages will automatically receive the same list of links of its parent. The current page will have its corresponding link highlighted.                                                                        |
|   Enable Tracking (Deprecated)  |                                                                                                                                                                                                                                              If enabled, every request for this page will be logged. A Web Page Log record will be created with the date & time, IP Address, and the contact record if the user is authenticated. Web page tracking is deprecated. For more information, go to [Web page tracking FAQ](../admin/portal-checker-analysis.md#web-page-tracking-enabled).                                                                                                                                                                                                                                               |
|                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Enable page comments

Page comments provides users with the ability to view and post comments on a web page. By default this feature is disabled and can be enabled on a page by page basis.

> [!NOTE]
> Comments are available for pages that use **Full page** or **Page** as a template.

1. Open the [Portal Management app](configure-portal.md).

2. Go to **Portals** > **Web Pages**.

3. Select the web page on which you need to enable comments.

4. From the **Comment Policy** list, select the required comment policy:
   - **Inherit**: The comment policy of the parent page will be used. This is the default setting.
   - **Open**: Submissions from all users, anonymous and authenticated, are allowed and displayed immediately.
   - **Open to Authenticated Users**: Only submissions from authenticated users are allowed and they are displayed immediately.
   - **Moderated**: Submissions from all users, anonymous or authenticated, are allowed. The submissions will not be displayed until a moderator approves them.
   - **Closed**: Existing submissions are displayed, but no new submissions are allowed.
   - **None**: User submissions are disabled. No submissions can be made or viewed.

5. Save the changes.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]