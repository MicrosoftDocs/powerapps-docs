---
title: Known issues in PowerApps Portals | Microsoft Docs
description: Learn about the known issues in PowerApps Portals 
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/18/2019
ms.author: shjais
ms.reviewer:
---

# Known issues

[!include[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

## General issues

- The **Modified Date** for the app might be incorrect because these are pre-provisioned apps and could have been provisioned earlier.

- The owner of the portal is not displayed correctly. It is displayed as System.

- If you are reusing the URL of a recently deleted portal to create a new portal, it will have some delay for runtime to setup. This is because the purge of previous resources would still be in progress and may take from 30 minutes to 1 hour for the new portal to setup on azure.

- When switching an environment in PowerApps, the portals within an environment may not show up immediately in **Apps** or **Recent Apps** list. This happens particularly on environments that are created in a different region than their tenant. The workaround is to use browser refresh or wait for some time for portal to show up in the apps list.

- When you reset your portal successfully from PowerApps Portals admin center, the following error is displayed: "The portal you are trying to access doesn't belong to the tenant you are currently logged into. Please log out and log in to the correct tenant.". You can visit the PowerApps home page and create a new portal. 

## Portal designer issues

-   When you select text in the text box, the font size of the selected text is not displayed in the formatting toolbar.

- The padding of columns in a section is not same as rendered on the website. The padding is adjusted according to the content inside the sections.

- Canvas does not load content in Chinese language.

- Webpage using the **Page with side navigation** template displays only the link of the pages which existed during the webpage creation. You can update the links on the left side of the page by changing the page template to another template and then back to **Page with side navigation**.

- When you delete a webpage, canvas does not reflect the updated menu until the next refresh of canvas.

- When creating a child page from a rewrite page (unsupported pages in portal designer), you must choose the template manually from the properties pane to render the page.

- If the page name is large and not displayed completely in the **Pages** pane, the **Ellipsis** button (...) is not displayed. You must right-click the page name to see the page options.

- If you have added a deactivated content snippet on a page, it will be displayed in the portal designer. But, the deactivated content snippet will be hidden on the actual website.

- Few components' placeholder like web links, Power BI, chart, and so on are not editable. But you can still edit the text on the same. The changes on placeholders will not be saved.

- Information and related actions on canvas, like component name, in portal designer are supported only in English.

- Color picker and its related strings are supported only in English.

- A few template pages on the Employee Self Service portal are not able to render correct breadcrumb.

- A few Dynamics 365 Portal templates do not have menu items as per their hierarchy of pages. However, if you create new pages, the menu items are created accordingly.
