---
title: "Use Power Fx in custom page for your model-driven app" 
description: "This article outlines how the common Microsoft Power Fx functions work within a custom page."
ms.custom: ""
ms.date: 01/22/2025
ms.reviewer: ""
ms.subservice: mda-maker
ms.topic: how-to
author: "aorth"
ms.author: "matp"
search.audienceType: 
  - maker
---
# Use Power Fx in a custom page for your model-driven app

This article outlines how the common [Microsoft Power Fx](../canvas-apps/formula-reference.md) functions work differently between a standalone canvas apps and a custom page. Functions work differently because a custom page is a component within the model-driven app. Other Microsoft Power Fx formulas continue to behave in the same way.

> [!IMPORTANT]
> Custom pages are a new feature with significant product changes and currently have a number of known limitations outlined in [Custom Page Known Issues](model-app-page-issues.md).

## Add notifications to a custom page

A notification can be shown to the user in a custom page by calling the [Notify function](../canvas-apps/functions/function-showerror.md). When the notification messages appear, they're docked above the default page to stay visible until disabled. If a time-out interval is provided, the notification message disappears after the time out interval. We recommend that you don't use a time-out interval of 10, as this is no longer considered as a time-out interval. More information: [Notify function](../canvas-apps/functions/function-showerror.md).

```power-fx
Notify( "Custom page notification message" )
```

> [!div class="mx-imgBorder"]
> ![Custom page notify information message bar](media/page-powerfx-in-model-app/custom-page-notify-information.png "Custom page notify information message bar")

```power-fx
Notify( "Custom page notify warning message", NotificationType.Warning )
```

> [!div class="mx-imgBorder"]
> ![Custom page notify warning message bar](media/page-powerfx-in-model-app/custom-page-notify-warning.png "Custom page notify warning message bar")

## Navigating to a custom page

This section provides examples of navigating from a model-driven app form to a custom page, navigating from a custom page to other custom pages or model-driven app form using Power Fx.

### Navigating from a custom page

The [Navigate function](../canvas-apps/functions/function-navigate.md) allows users to navigate either from model-driven app forms or custom pages. This function is only applicable when the custom page is running within a model-driven app. During custom page authoring or previewing in Power Apps Studio, this function has no effect.

### Navigate to another custom page

To navigate from one custom page to another, pass the display name of the custom page as the first parameter.

```power-fx
Navigate( CustomPage2  )
```

### Navigate to the default view of the table

To navigate to the default view of the table, pass table name as the first parameter.

```power-fx
Navigate( Accounts )
```

> [!IMPORTANT]
> Make sure you add the accounts Microsoft Dataverse table to the custom page before publishing and testing.

### Navigate to specific system view of the table

To navigate to a specific system view of the table, pass the GUID of the view.

```power-fx
Navigate( 'Accounts (Views)'.'My Active Accounts' )
```

### Navigate to the default form of the table

To navigate to the default form of the table, pass the record as the first parameter.

```power-fx
Navigate( Gallery1.Selected )
```

### Navigate to a specific form of a table

To pass a Dataverse record to a specific form, pass the form name in the second parameter's `Page` attribute.

```power-fx
Navigate( 
  AccountGallery.Selected, 
  { Page: 'Accounts (Forms)'.Account  } )
```

### Navigate to a specific custom page with a record input

To pass a Dataverse record to a specific custom page, pass the custom page name in the second parameter's `Page` attribute.

```power-fx
Navigate( 
  AccountGallery.Selected, 
  { Page: 'Account Record Page'  } )
```

In the target custom page, the record is retrieved using `Param` function to get the `etn` and `id` values.

Here's an example of loading the record into an `EditForm` control.

```power-fx
AccountEditForm.DataSource = Accounts
AccountEditForm.Item = 
  LookUp( Accounts, accountid = GUID( Param("id") ) )
```

### Navigate to the default form of the table in create mode

To navigate to the default form of the table in create mode, pass a Dataverse record created from the [Defaults](../canvas-apps/functions/function-defaults.md) function. Defaults opens the default form with the record as a new record. The `Defaults` function takes the table name to create the record.

```power-fx
Navigate( Defaults( Accounts ) )
```

### Navigate to the default form of the table in create mode with field defaulted

To navigate to a new record with some fields defaulted, use the `Patch` function to set fields on the default record for the table.

```power-fx
Navigate(
	Patch(
		Defaults(Accounts), { 'Account Name': "My company", Phone: "555-3423" } ) 
  )
```

### Navigate back to the prior page or close a dialog

To navigate back to the last page or to close a dialog, the [Back](../canvas-apps/functions/function-navigate.md) function is called in a custom page. The `Back` function closes the current page and returns to the last model-driven app or custom page in the model-driven app. If the custom page has multiple screens, go to the article [Navigating back when custom page has multiple screens](#navigating-back-when-custom-page-has-multiple-screens).

```power-fx
Back()
```

### Navigating back when custom page has multiple screens

The default configuration for a custom page is to have one screen. In this case, the `Back` function call closes the custom page unless the custom page is the last in the page stack in model-driven app. The last page is kept open.

An app maker can enable multiple screens in a custom page. These should be considered like full page controls within the custom page that can be stacked. Opening a custom page has no means of specifying the screen to use. When a custom page contains multiple screens, the maker is responsible for managing the screen stacking. Calling the `Navigate` function to a screen adds to the screen stack with the custom page. Each `Back` function call removes a screen from the screen stack. When there's only one screen on the screen stack, the custom page is closed.

### Enabling multiple screens

By default a custom page uses a single screen to encourage separation of the app into a screen per page. Single screen can be switched by enabling **Settings** > **Display** > **Enable multiple screens**.

> [!div class="mx-imgBorder"]
> ![Custom page enable multiple screens](media/page-powerfx-in-model-app/custom-page-enable-multiple-screens.png "Custom page enable multiple screens")

### Known issues

- The `Navigate` function doesn't have support for opening a model-driven app or custom page to a dialog. All navigation from a custom page opens inline.
- Navigate function doesn't support opening:
   - A dashboard collection or a specific dashboard.
   - A specific model-driven app form.
- A custom page can only open into the current session’s current app tab in a multi-session model-driven app.

### See also

[Navigating to a custom page using client API](../../developer/model-driven-apps/clientapi/navigate-to-custom-page-examples.md)

[Model-driven app custom page overview](model-app-page-overview.md)
