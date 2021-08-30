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

Developers can add and manage app side panes within a model-driven app using [Xrm.App.sidePanes](reference/xrm-app-sidepanes.md) API which represents the collection of side panes. Calling [createPane](reference/Xrm-App/Xrm-App-sidePanes/createPane.md) adds a new pane item which allows navigation to any model-driven app form or custom page. Pages within the pane must fit within the minimal width of 300px and support resize to larger widths based on the pane width.  

The order of tabs in the app side pane is based on the order created and placed in two groups. The top group contains the panes not closeable by a user and the bottom group will contain user closeable panes. The non-closeable group is typically defined at the start of the app while the closeable group is typically added based on user actions within the app.
A maker can use a platform provided header that has the title and close button or can use a custom header.

> [!IMPORTANT]
> - This is a preview feature, and isn't available in all regions.
> - [!INCLUDE[cc_preview_features_definition](../../../includes/cc-preview-features-definition.md)]

App side pane icons support badging to indicate to a user that there is a change needing attention.  The badge supports three modes including a simple dot, a count, or an image.  By default, a badge is cleared when the user switches to the pane but this can be disabled if the maker wants to control when the badge is cleared.

## Enable side panes feature

To use the side panes feature, you need enable the `EnableAppSidePaneEarlyAccess` app setting in model-driven app.

1. Sign in to your model-driven app.
1. Select the app where you want to use this feature.
1. Select **F12** button on your keyboard to open the browser console.
1. In the browser console, copy the code below. Enter your app unique name in the `AppUniqueName` parameter. Press **Enter**.   

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
1. Select **Publish all customizations**. Refresh the model-driven app, you should see a **Bell** icon on the top-right corner.

> [!TIP]
> The logical name of your model-driven app can be found in the solution explorer under the **Name** column. 


## Examples

### Showing default view in side pane

The following examples shows how to show a default view of the table in the side pane. This example shows how to open reservation list and product list in the app side pane as non-closeable panes.

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

This example shows howe to display a record in the side pane. This example opens a reservation record by hiding the default header and with custom width.

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

Apart from creating side panes and showing records or view within the side pane, you can also do other thins using the API method. 

- You can use the `state` method to programmatically collapse the side pane:

  `Xrm.App.sidePanes.state = 0;`

- You can use the `state` method to programmatically collapse the side pane:

  `Xrm.App.sidePanes.state = 1;`

- You can also change the properties by retrieving the selected pane:

  `var lastPane = Xrm.App.sidePanes.getSelectedPane();
   lastPane.width = 400;`

- You can retrieve a specific pane using the paneId parameter:

  `var reservationPane = Xrm.App.sidePanes.getPane("ReservationList");
   reservationPane.close();`

- You can also enable the badge property on a pane:

  `Xrm.App.sidePanes.getSelectedPane().badge = 1;`


### Related topics

[sidePanes (Client API reference)](reference/xrm-app-sidepanes.md)