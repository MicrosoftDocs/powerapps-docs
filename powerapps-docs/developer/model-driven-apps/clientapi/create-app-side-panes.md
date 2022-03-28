---
title: "Creating side panes by using a client API in model-driven apps" 
description: Learn how to create side panes in model-driven apps by using a client API.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.subservice: mda-developer
ms.topic: "article"
search.audienceType: 
  - maker
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---

# Creating side panes by using a client API (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

Developers can create and manage app side panes within a model-driven app by using the [Xrm.App.sidePanes](reference/xrm-app-sidepanes.md) API, which represents the collection of side panes. Calling the [createPane](reference/Xrm-App/Xrm-App-sidePanes/createPane.md) method adds a new pane that allows navigation to any model-driven app form or custom page. Pages displayed in the side pane must fit within the minimum width of 300 pixels and resize to larger widths based on the pane width.

Tabs are listed in the side pane in two groups&mdash;non-closable and closable. Within each group, the tabs are listed in the order they were created in. The top group contains the panes that a user can't close, and the bottom group has user-closable panes. The non-closable group is populated when the app is opened, whereas the closable group is added based on user actions within the app.

You can use a platform-provided header with the title and Close button, or you can use a custom header.

> [!IMPORTANT]
> - This is a preview feature, and isn't available in all regions.
> - [!INCLUDE[cc_preview_features_definition](../../../includes/cc-preview-features-definition.md)]

You can add a badge to the side pane to indicate to the user that a change needs attention. The badge supports three modes: a simple dot, a count, or an image. By default, the badge is cleared when the user switches to the pane. You can control when the badge is cleared.


## Examples

### Showing a default view in the side pane

The examples in this section show how to display the default view of a table in the app side pane. A reservation list and product list are opened as non-closable panes.

```javascript
Xrm.App.sidePanes.createPane({
    title: "Reservations",
    imageSrc: "WebResources/sample_reservation_icon",
    paneId: "ReservationList",
    canClose: false
}).then((pane) => {
    pane.navigate({
        pageType: "entitylist",
        entityName: "sample_reservation",
    })
});
```

> [!div class="mx-imgBorder"] 
> ![Screenshot showing a Reservations table with a list of active reservations, including name, equipment, and the start date of the reservation.](../media/app-side-panes-example-1.png "Example 1")

```javascript
Xrm.App.sidePanes.createPane({
    title: "Products",
    imageSrc: "WebResources/sample_product_icon",
    paneId: "ProductList",
    canClose: false
}).then((pane) => {
    pane.navigate({
        pageType: "entitylist",
        entityName: "sample_product",
    })
});
```

> [!div class="mx-imgBorder"] 
> ![Screenshot showing a Products table with a list of products that can be reserved.](../media/app-side-panes-example-2.png "Example 2")

### Showing a table row

This example shows how to display a row in the side pane. A reservation row is opened in a side pane where the default header is hidden and the width is customized to 600 pixels.

```javascript
Xrm.App.sidePanes.createPane({
    title: "Reservation: Ammar Peterson",
    imageSrc: "WebResources/sample_reservation_icon",
    hideHeader: true,
    canClose: true,
    width: 600
}).then((pane) => {
    pane.navigate({
        pageType: "entityrecord",
        entityName: "sample_reservation",
        entityId: "d4034340-4623-e811-a847-000d3a30c619",
    })
});
```

> [!div class="mx-imgBorder"] 
> ![Screenshot showing an Active Reservations list opened to an individual record.](../media/app-side-panes-opening-record.png "Open record")

### Managing side panes

In addition to creating side panes and showing rows or views within the side pane, you can also: 

- Use the `state` method to collapse the side pane programmatically:

  `Xrm.App.sidePanes.state = 0;`

- Use the `state` method to expand the side pane programmatically:

  `Xrm.App.sidePanes.state = 1;`

- Change properties by retrieving the selected pane:

  `var lastPane = Xrm.App.sidePanes.getSelectedPane();`  
  `lastPane.width = 400;`

- Retrieve a specific pane by using the `paneId` parameter:

  `var reservationPane = Xrm.App.sidePanes.getPane("ReservationList");`  
  `reservationPane.close();`

- Enable the badge property on a pane:

  `Xrm.App.sidePanes.getSelectedPane().badge = 1;`


### Related topics

[sidePanes (Client API reference)](reference/xrm-app-sidepanes.md)
