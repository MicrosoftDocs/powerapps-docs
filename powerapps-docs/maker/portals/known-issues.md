---
title: Known issues in Power Apps portals | Microsoft Docs
description: Learn about the known issues in Power Apps portals 
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 01/17/2020
ms.author: tapanm
ms.reviewer:
---

# Known issues


## General issues

- Due to ongoing compatibility issues between the updated Yahoo YDN OAuth provider endpoint and Power Apps portals, users are temporarily unable to authenticate with [Yahoo identity provider](./configure/configure-oauth2-settings.md#yahoo-ydn-app-settings).

- The **Modified Date** for the app might be incorrect because these are pre-provisioned apps and could have been provisioned earlier.

- When you create an environment along with the starter portal, the owner of the portal is not displayed correctly. It is displayed as System.

- If you are reusing the URL of a recently deleted portal to create a new portal, it will have some delay for runtime to setup. This is because the purge of previous resources would still be in progress and may take from 30 minutes to 1 hour for the new portal to setup on Azure. The portal will also not be available for editing during this time and may show errors when launched in studio for editing.

- When switching an environment in Power Apps, the portals within an environment may not show up immediately in **Apps** or **Recent Apps** list. This happens particularly on environments that are created in a different region than their tenant. The workaround is to use browser refresh or wait for some time for portal to show up in the apps list.

- If you keep the portal settings pane open in Power Apps home page while resetting the portal from Power Apps Portals admin center, a user will see the "Something went wrong" error message in the portal settings pane, as portal is not available.

- In certain cases, when you create a portal, the styles are not applied properly to the portal, and the website is displayed without the styles when opened through **Browse website**. This rarely happens and styles can be recovered by restarting the portal from Power Apps Portals admin center.

## Power Apps portals Studio issues

- If a portal has page hierarchy of more than three levels, the pages from fourth level onwards are not displayed in Power Apps portals Studio.

- The selected text font size will only be displayed if there is a font size defined specifically for that text. If it is part of the standard HTML tags such as p, H1, H2, H3, an so on, Power Apps portals Studio will not display the font size.

- Webpage using the **Page with side navigation** template displays only the link of the pages which existed during the webpage creation. You can update the links on the left side of the page by changing the page template to another template and then back to **Page with side navigation**.

- When you delete a webpage, canvas does not reflect the updated menu until the next refresh of canvas.

- Color picker and its related strings are supported only in English.

- A few template pages on the Employee Self Service portal are not able to render correct breadcrumb.

- A few Power Apps portals templates, especially bound to model-driven apps in Dynamics 365, do not have default menu items as per their hierarchy of pages. The reason is that there is not page order available in all or few of the webpages. Any portal without the display order of webpages will have this issue.

- An error message is displayed when the page content (page copy) exceeds its limit of 65536 characters and page summary exceed its default limit of 2000 characters.

- Navigation menu is only visible on the canvas with a resolution of minimum width of 1600px.

- An image uploaded on a page becomes the child of the page. If you delete the page, and use the image on another page, the image will not render on Power Apps portals Studio and website.

- Form rendering is not currently supported in Power Apps portals Studio. When you add a form, you must select **Browse website** to open the website and verify the form.

- On a text or a section background, if you change the color to **No color**, Power Apps portals Studio does not remove the related attributes such as background color or font color, instead make the values null.

- In the following scenarios Power Apps portals Studio ceases to load and shows the "Sorry, there's a disconnect" error:
    - If the Home page is deleted or disabled for a portal.
    - If a page template related to the Home page or any page is disabled or deleted.

- Power Apps portals Studio will be unable to load source code of those content snippets which do not have a language assigned in Common Data Service.

- In some instances the changes for header and footer, either through WYSIWYG experience of Power Apps portals Studio or through the code editor, will not be reflected immediately.

- If a webpage is assigned the Search template in Power Apps portals Studio, it will show a simple page with loader. For this to work, you will have to create an appropriate site marker for that page.

- The Default studio template also shows up as an option in page template while creating a new page once it is used in Power Apps portals Studio. Also, this template is only inserted in English language and it does not support localization based on default Common Data Service or portal language.

- A list rendered as a calendar control or map is not configurable through Power Apps portals Studio.

- The Partial URL field in page properties does not accept special characters and it breaks the rendering in the canvas for some time. 

- Upload CSS might fail in scenarios where CSS file name contains special characters or space in the file name.

- Unpublished webpages do not render in canvas of Power Apps portals Studio.

- While using Power Apps portals Studio, if your portal base language is different than the browser's language, the new webpages created using the Default studio template will have dummy content inserted in browser's language instead of portal language.

- Only CSS applied at the root page is displayed in the **Theme** pane. Although, if you try uploading a CSS file with a same name as any other CSS file available in the portal, Power Apps portals Studio asks you to replace that file.

- Power Apps portals Studio is currently not supported on Safari in Mac operating system and has the following issues:
    - The selection of component is not correct and hovering on a component provides incorrect target indication.
    - Two or three column sections do not render properly in Power Apps portals Studio but works fine on the website.

