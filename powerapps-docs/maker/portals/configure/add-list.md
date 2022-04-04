---
title: Add a list
description: Learn how to add lists on a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 04/04/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---

# Add a list to your portal

The list contains relationships to webpages and various properties to control the initialization of the list of records within the portal. The relationship to the webpage allows dynamic retrieval of the list definition for a given page node within the website. To view existing Table views or to create new Table views, go to **Portals** > **Lists**.

> [!Note]
> - A list must be associated with a webpage in a given website for the list to be viewable within the site.

The webpages associated with the list can be viewed by selecting the **Web Pages** link listed in the **Related** navigation links in the leftmost menu. When creating your list, the first step is to choose the table for which you want to render a list on the portal. You'll then choose one or more model-driven app views to render.

When creating or editing a webpage, you can specify a list in the lookup field provided on the Web Page form. The page template typically will be the Page template, but can be one of several other templates designed for content because the master templates contain the necessary logic to determine whether a list should be rendered.

### See also

- [Microsoft Learn: Display multiple Dataverse records using lists](/learn/modules/portals-access-data-platform/2-entity-lists)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
