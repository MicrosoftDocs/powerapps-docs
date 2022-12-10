---
title: About lists
description: Learn how to add and configure lists to render a list of records on a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 05/27/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---

# About lists


[!INCLUDE[cc-pages-ga-banner](../../../includes/cc-pages-ga-banner.md)]

A list is a data-driven configuration that you use to add a webpage that will render a list of records without the need for a developer to surface the grid in the portal. By using lists, you can expose records for display on portals.

The grid supports sorting and will be paginated if the number of records is larger than the page size specified. If **Web Page for Details View** has been specified, each record will contain a link to the page, and the ID of the record will be appended to the query string along with the ID Query String Parameter Name. The list also supports multiple views. If more than one view has been specified, a drop-down list will be rendered to allow the user to switch between the various views.

The data can also be filtered by the current portal user, the current portal user's parent Customer account, and the current portal website. If a value exists for both filter conditions **Portal User Attribute** and **Account Attribute**, the portal will render a drop-down list to allow the user to view their own (My) data or their parent Customer account's data.

## Add a list to your portal

The list contains relationships to webpages and various properties to control the initialization of the list of records within the portal. The relationship to the webpage allows dynamic retrieval of the list definition for a given page node within the website. To view existing table views or to create new Table views, go to **Portals** > **Lists**.

Lists can also be added to a page using the [portals Studio](../add-list.md).

> [!Note]
> - A list must be associated with a webpage in a given website for the list to be viewable within the site.

The webpages associated with the list can be viewed by selecting the **Web Pages** link listed in the **Related** navigation links in the leftmost menu. When creating your list, the first step is to choose the table for which you want to render a list on the portal. You'll then choose one or more model-driven app views to render.

When creating or editing a webpage, you can specify a list in the lookup field provided on the Web Page form. The page template typically will be the Page template, but can be one of several other templates designed for content because the master templates contain the necessary logic to determine whether a list should be rendered.

## See Also

- [List attributes and relationships](list-attributes-relationionships.md)
- [Sort lists](sort-lists.md)
- [Add custom Javascript](add-custom-javascript-list.md)
- [List configuration](list-configuration.md)
- [Securing lists](securing-lists.md)
- [Adding a view details page](list-view-details.md)
- [List filter configuration](list-filter-configuration.md)
- [List map view](list-map-view.md)
- [List calendar view](list-calendar-view.md)
- [List OData feeds](list-odata-feeds.md)
- [Enhanced view filter for lists](list-enhanced-view-filter.md)
