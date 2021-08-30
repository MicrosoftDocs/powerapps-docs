---
title: "Creating side panes using client API in model-driven apps" 
description: Learn how to create side panes in model-driven apps using client API.
ms.date: 08/31/2021
ms.reviewer: "nabuthuk"
ms.service: powerapps
ms.subservice: mda-developer
ms.topic: "article"
author: "aorth"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - maker
  - developer
search.app: 
  - "PowerApps"
  - D365CE
---

# Preview: Creating side panes using client API

[!INCLUDE [cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

Developers can create and manage app side panes within a model-driven app using the [Xrm.App.sidePanes](reference/xrm-app-sidepanes.md) API which represents the collection of side panes. Calling the [createPane](reference/Xrm-App/Xrm-App-sidePanes/createPane.md) method adds a new pane that allows navigation to any model-driven app form or custom page. Pages within the side pane must fit within the minimum width of 300px and resize to larger widths based on the pane width.  

You always need to use the [navigateTo](reference/Xrm-Navigation/navigateTo.md) method while using the [sidePanes (Client API reference)](reference/xrm-app-sidepanes.md) for displaying records and views in the side pane.

The order of tabs in the side pane is based on the order created and placed in two groups. The top group contains the panes that are not closeable by a user, and the bottom group has user closeable panes. The non-closeable group is typically defined at the start of the app, while the closeable group generally is added based on user actions within the app.

You can use a platform-provided header with the title and close button or a custom header.

> [!IMPORTANT]
> - This is a preview feature, and isn't available in all regions.
> - [!INCLUDE[cc_preview_features_definition](../../../includes/cc-preview-features-definition.md)]

Side pane icons support badging indicating the user that a change needs attention.  The badge supports three modes, including a simple dot, a count, or an image.  By default, a badge is cleared when the user switches to the pane. You can control when the badge is cleared.

## Enable side panes feature

To use the side panes feature, you need to enable the `EnableAppSidePaneEarlyAccess` app setting in a model-driven app.

1. Sign in to your model-driven app.
1. Select the app where you want to use this feature.
1. Select **F12** button on your keyboard to open the browser console.
1. In the browser console, copy the code below. Enter your app's unique name in the `AppUniqueName` parameter. Press **Enter**.   

   ```javascript
   fetch(window.origin + "/api/data/v9.1/SaveSettingValue()",{
    method: "POST", 
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({AppUniqueName: "Your app unique name", SettingName:"EnableAppSidePaneEarlyAccess", Value: "true"})
      });
   ```
1. Now sign in to [Power Apps](https://make.powerapps.com).
1. Select **Solutions** in the left navigation pane. Select **New solution**. Enter the details and then select **Create**. 
1. Open the solution that you have created. Select **Add** > **App** > **Model-driven app**. From the list of apps, select the model-driven app where you want to see the notifications feature.
1. Select **Publish all customizations**. Refresh the model-driven app, and you should see a **Bell** icon on the top-right corner.

> [!TIP]
> The logical name of your model-driven app can be found in the solution explorer under the **Name** column. 


## Examples

### Showing default view in the side pane

The following examples show how to display a default view of the table in the side pane. This example shows how to open reservation list and product list in the app side pane as non-closeable panes.

> [!div class="mx-imgBorder"] 
> ![Example 1](../media/app-side-panes-example-1.png "Example 1")

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
> ![Example 2](../media/app-side-panes-example-2.png "Example 2")

### Showing a table record

This example shows how to display a record in the side pane. This example opens a reservation record by hiding the default header and with custom width.

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
> ![Open record](../media/app-side-panes-opening-record.png "Open record")

### Managing side panes

Apart from creating side panes and showing records or views within the side pane, you can also do other things using the API method. 

- You can use the `state` method to collapse the side pane programmatically:

  `Xrm.App.sidePanes.state = 0;`

- You can use the `state` method to collapse the side pane programmatically:

  `Xrm.App.sidePanes.state = 1;`

- You can also change the properties by retrieving the selected pane:

  `var lastPane = Xrm.App.sidePanes.getSelectedPane();
   lastPane.width = 400;`

- You can retrieve a specific pane using the `paneId` parameter:

  `var reservationPane = Xrm.App.sidePanes.getPane("ReservationList");
   reservationPane.close();`

- You can also enable the badge property on a pane:

  `Xrm.App.sidePanes.getSelectedPane().badge = 1;`


### Related topics

[sidePanes (Client API reference)](reference/xrm-app-sidepanes.md)