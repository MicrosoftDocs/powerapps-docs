---
title: Create and manage page templates
description: Learn how to create and manage page templates in Power Apps portals.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2020
ms.subservice: portals
ms.author: sandhan
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - sandhangitmsft
---

# Create and manage page templates

While web pages are nodes in your portal's sitemap which represent content accessible to portal users, page templates represent the actual .aspx pages which provide a means to maintain a consistent look and feel throughout your entire website. Page templates are built using ASP.NET pages, master pages, cascading style sheets (CSS), user controls, and server controls.

When creating a new web page for the site, whether through front-side publishing or through the portal interface, you must select a page template which will present the page's content to users of the portal.

The difference between web pages and page templates is perhaps best understood as the difference between an exact URL and an actual .aspx page which acts as a blueprint for displaying content. Each webpage represent a specific URL in your site, which users can navigate to. When a user navigates to a URL, the content associated with that URL is displayed. However, a webpage contains no information on how that content is displayed.  This is determined by the page template, which is the actual .aspx page which generates the HTML that the user sees.

When you create a new webpage, you must choose a page template from a list of existing templates. Several Page templates are included with each of the start portals. When using these portals as a base for your own website, these templates will come in handy as a basic means of demonstrating the functionality of the portal. However, a portal developer will be necessary to significantly change the layout of these pages. In most cases, the “Page” page template will be the page template to use as it is general purpose: a web page using this template will have its content displayed, as well as a list of child pages presented as navigation items.

## Manage page templates

Creating a new Page Template is only necessary when creating a brand new .aspx page to display content on your website, a portal developer’s task. In fact, for the purposing of simply customizing the layout of your site, a portal developer can largely just modify existing .aspx pages.

1. Open the [Portal Management app](configure-portal.md).

2. Go to **Portals** > **Page Templates**.

3. To create a new page template, select **New**.

4. To edit an existing page template, select the page template name.

5. Enter appropriate values in the fields.

6. Select **Save & Close**.

### Page template attributes

|Name |Description |
|-----|--------|
|Name    |Name of the template used for reference.   |
|Website   |The associated website.   |
|Type   |The type of the template, which controls how the template will determine what to render.<ul><li>**Rewrite**: Will use the Rewrite URL field to render a given ASP.NET template.</li><li>**Web Template**: Will use the Web Template field to render a given Web Template.</li></ul>   |
|Rewrite URL   |Path of the physical ASP.NET .aspx page (or other resource, such as .ashx) which will be rendering the content.<br> This field is displayed only if **Rewrite URL** is selected from the **Type** list. |
|Web Template   |A reference to a web template to that will be used to render this template.<br>This field is displayed only if **Web Template** is selected from the **Type** list.  |
|Is Default   |If 'Yes' then the template will be the default assigned to the dropdown in the client-side editing tools.   |
|Table Name   |The page table type that this template expects to render. This will be use by the front-side editing system to present only appropriate template choices to content authors.<br>Usually, this will be Web Page (adx_webpage), but may be another portal table, such as Forum, Forum Thread, Blog, or Blog Post.   |
|Description  |A description of this template, for the benefit of front-side editing users. |
|||



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]