---
title: List map view
description: Learn how to enable a list to  render as a map on a portal.
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

# List Map view

On the **Map View** tab, you can enable the list to render as a map view of the data.

The map view is powered by [!INCLUDE[pn-bing](../../../includes/pn-bing.md)] maps with search functionality to find locations near an address. By populating your records with latitude and longitude coordinate values and specifying the necessary configuration options listed in this section, your records can be rendered as pushpins on a map. Any record that doesn't have a latitude or longitude value will be excluded from the search. The initial load of the page will display all records within the initial value of the Distance Values field (in miles or km, depending on the Distance Units specified) from the Default Center Latitude and Default Center Longitude coordinates. The view specified is ignored when Map view is used, and a distance query is applied to the dataset to return the mappable results.

> [!NOTE] 
> - This option is not supported in the German Sovereign Cloud environment. The Map view section will not be visible in this environment.
> - Only Bing maps are supported as the **Map type**.

### See also

- [Work with lists](entity-lists.md)
- [Display multiple Dataverse records using lists](/training/modules/portals-access-data-platform/2-entity-lists)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)
