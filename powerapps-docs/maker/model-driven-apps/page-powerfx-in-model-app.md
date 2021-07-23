---
title: "Use PowerFx in custom page for your model-driven app (preview)" 
description: ""
ms.custom: ""
ms.date: 07/06/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "aorth"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Use PowerFx in a custom page for your model-driven app (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This article outlines how the common Microsoft Power Fx functions works within a custom page. Power Fx formulas in a custom page can be different from Power Fx in a standalone canvas app. This is because custom pages are a component within the model-driven app.

  > [!IMPORTANT]
  > - This is a preview feature, and isn't available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

## Add notifications to a custom page

A notification can be shown to the user in a custom page by calling the [Notify function](../canvas-apps/functions/function-showerror.md).  When the notification messages appear, they're docked above the default page to stay visible until disabled. If a timeout interval is provided, the notification message will disappear after the timeout interval. It is recommended to avoid using a timeout interval of 10, as this is no longer considered as a timeout interval. More information: [Notify function](../canvas-apps/functions/function-showerror.md).

```powerappsfl
Notify( "Custom page notification message" )
```

> [!div class="mx-imgBorder"]
> ![Custom page notify information message bar](media/page-powerfx-in-model-app/custom-page-notify-information.png "Custom page notify information message bar")

```powerappsfl
Notify( "Custom page notify warning message", NotificationType.Warning )
```

> [!div class="mx-imgBorder"]
> ![Custom page notify warning message bar](media/page-powerfx-in-model-app/custom-page-notify-warning.png "Custom page notify warning message bar")

## Navigating to a custom page

This section provides examples of navigating from a model-driven app form to a custom page, navigating from a custom page to other custom pages or model-driven app form using Power Fx.

### Navigating from a custom page

The [Navigate function](../canvas-apps/functions/function-navigate.md) allows the users to navigate either from model-driven app forms or custom pages.  This function is only applicable when the custom page is running within a model-driven app.  During custom page authoring or previewing in canvas designer, this function have no effect.

Examples that use a table should be added as a data source in the page.

### Navigate to another custom page

To navigate from one custom page to another, pass the display name of the custom page as the first parameter.

```powerappsfl
Navigate( '<custom page>'  )
```

### Navigate to the default view of the table

To navigate to the default view of the table, passed table name as the first argument.

```powerappsfl
Navigate( Accounts )
```

### Navigate to specific system view of the table

To navigate to a specific system view of the table,pass the table's Views enum.

```powerappsfl
Navigate( 'Accounts (Views)'.'My Active Accounts' )
```

### Navigate to the default form of the table

To navigate to the default form of the table, pass the record as the first argument.

```powerappsfl
Navigate( Gallery1.Selected )
```

### Navigate to the default form of the table in create mode

To navigate to the default form of the table in create mode, pass a Dataverse record created from the [Defaults](../canvas-apps/functions/function-defaults.md) function. This will open the default form with the record as a new record. The **Defaults** function takes the table name to create the record.

```powerappsfl
Navigate( Defaults( Accounts ) )
```

### Navigate back to the prior page or close a dialog

To navigate back to the last page or to close a dialog, the [Back](../canvas-apps/functions/function-navigate.md) function is called in a custom page. The **Back** function closes the current page and returns to the last model-driven app or custom page in the model-driven app. If the custom page has multiple screens, see the article [Navigation advanced examples for custom page](#navigating-back-when-custom-page-has-multiple-screens).

```powerappsfl
Back( )
```

### Navigating back when custom page has multiple screens

The default configuration for a custom page is to have one screen. In this case the **Back** function call will close the custom page unless the custom page is the last in the page stack in model-driven app. The last page is kept open.

An app maker can enable multiple screens in a custom page. These should be considered like full page controls within the custom page which can be stacked. Opening a custom page has no means of specifying the screen to use.  When a custom page contains multiple screens the maker is responsible for managing the screen stacking.  Calling the **Navigate** function to a screen will add to the screen stack with the custom page.  Each **Back** function call will remove a screen from the screen stack.  When there is only one screen on the screen stack, the custom page is closed.

### See also

[Navigating to and from a custom page using client API](../../developer/model-driven-apps/clientapi/navigate-to-custom-page-examples.md)

[Model-driven app custom page overview](model-app-page-overview.md)

[Navigating a custom page](page-powerfx-in-model-app.md#navigating-a-custom-page)