---
title: Known issues
description: Learn about the known issues in Power Apps portals 
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.author: sandhan
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
    - GitanjaliSingh33msft
    - sandhangitmsft
    - dileepsinghmicrosoft
---

# Known issues

## General issues

- You receive the following error message when configuring or using table fields:

    ***Field Name**: You have exceeded the maximum number of X characters in this field.*

    This can happen if the referenced field for the table exceeds characters limit mentioned in the error. To increase this limit, go to your Dynamics 365 instance > **Settings** > **Customization** > **Customize this system** > **Components** > **Entities**. Select applicable table and then select the field. Increase the **Maximum Length** field value for the field to a higher value. Allowed values: 1 through 1,048,576.

    Fields where limit may need to be increased:

    | Table | Field Display Name |
    | - | - |
    | Basic Form | Settings (adx_settings) |
    | Enity List | View (adx_views) |
    | Enity Form Metadata | Subgrid Setting (adx_subgrid_settings) |
    | Web Page | Copy (adx_copy) |

- Rich-text for notes in timeline isn't fully supported by Power Apps portals because there's no rich-text editor equivalent control available in portals. For more information, go to [notes created with rich-text editor](configure-notes.md?#notes-created-with-rich-text-editor). If you want, you can [disable the rich-text editor for notes in timeline](../model-driven-apps/set-up-timeline-control.md#enable-or-disable-rich-text-editor-for-notes-in-timeline) for the Microsoft Dataverse model-driven app.

- The **Modified Date** for the app might be incorrect because these apps are pre-provisioned apps and could have been provisioned earlier.

- When you create an environment along with the starter portal, the owner of the portal isn't displayed correctly. It's displayed as System.

- If you're reusing the URL of a recently deleted portal to create a new portal, it will have some delay for runtime to setup. This experience happens because the purge of previous resources would still be in progress and may take from 30 minutes to 1 hour for the new portal to setup on Azure. The portal will also not be available for editing during this time and may show errors when launched in studio for editing.

- When switching an environment in Power Apps, the portals within an environment may not show up immediately in **Apps** or **Recent Apps** list. This experience happens particularly on environments that are created in a different region than their tenant. The workaround is to use browser refresh or wait for some time for portal to show up in the apps list.

- If you keep the portal settings pane open in Power Apps home page while resetting the portal from Power Apps portals admin center, a user will see the "Something went wrong" error message in the portal settings pane, as portal isn't available.

- In certain cases, when you create a portal, the styles aren't applied properly to the portal, and the website is displayed without the styles when opened through **Browse website**. This behavior rarely happens and styles can be recovered by restarting the portal from Power Apps portals admin center.

## Power Apps portals Studio issues

- If a portal has page hierarchy of more than three levels, the pages from fourth level onwards aren't displayed in Power Apps portals Studio.

- The selected text font size will only be displayed if there's a font size defined specifically for that text. If it's part of the standard HTML tags such as p, H1, H2, H3, and so on, Power Apps portals Studio won't display the font size.

- Webpage using the **Page with side navigation** template displays only the link of the pages that existed during the webpage creation. You can update the links on the left side of the page by changing the page template to another template and then back to **Page with side navigation**.

- When you delete a webpage, canvas doesn't reflect the updated menu until the next refresh of canvas.

- Color picker and its related strings are supported only in English.

- A few template pages on the Employee Self Service portal aren't able to render correct breadcrumb.

- A few Power Apps portals templates, especially bound to customer engagement apps (such as Dynamics 365 Sales and Dynamics 365 Customer Service), don't have default menu items as per their hierarchy of pages. The reason is that there isn't page order available in all or few of the webpages. Any portal without the display order of webpages will have this issue.

- An error message is displayed when the page content (page copy) exceeds its limit of 65536 characters and page summary exceed its default limit of 2000 characters.

- Navigation menu is only visible on the canvas with a resolution of minimum width of 1600 px.

- An image uploaded on a page becomes the child of the page. If you delete the page, and use the image on another page, the image won't render on Power Apps portals Studio and website.

- Form rendering isn't currently supported in Power Apps portals Studio. When you add a form, you must select **Browse website** to open the website and verify the form.

- On a text or a section background, if you change the color to **No color**, Power Apps portals Studio doesn't remove the related attributes such as background color or font color, instead make the values null.

- In the following scenarios Power Apps portals Studio stops to load and shows the "Sorry, there's a disconnect" error:
    - If the Home page is deleted or disabled for a portal.
    - If a page template related to the Home page or any page is disabled or deleted.

- Power Apps portals Studio will be unable to load source code of those content snippets that don't have a language assigned in Dataverse.

- In some instances, the changes for header and footer, either through WYSIWYG experience of Power Apps portals Studio or through the code editor, won't be reflected immediately.

- If a webpage is assigned the Search template in Power Apps portals Studio, it will show a page with the loader. For this scenario to work, you'll have to create an appropriate site marker for that page.

- The Default studio template also shows up as an option in page template while creating a new page once it's used in Power Apps portals Studio. Also, this template is only inserted in English language and it doesn't support localization based on default Dataverse or portal language.

- A list rendered as a calendar control or map isn't configurable through Power Apps portals Studio.

- The Partial URL field in page properties doesn't accept special characters and it breaks the rendering in the canvas for some time.

- Upload CSS might fail in scenarios where CSS file name contains special characters or space in the file name.

- Unpublished webpages don't render in canvas of Power Apps portals Studio.

- While using Power Apps portals Studio, if your portal base language is different than the browser's language, the new webpages created using the Default studio template will have dummy content inserted in browser's language instead of portal language.

- Only CSS applied at the root page is displayed in the **Theme** pane. Although if you try uploading a CSS file with a same name as any other CSS file available in the portal, Power Apps portals Studio asks you to replace that file.

- Power Apps portals Studio is currently not supported on Safari in Mac operating system and has the following issues:
    - The selection of component isn't correct and hovering on a component provides incorrect target indication.
    - Two or three column sections don't render properly in Power Apps portals Studio but works fine on the website.

### See also

[Microsoft Learn: Power App portal maintenance and troubleshooting](/learn/modules/portals-maintenance-troubleshooting/)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]