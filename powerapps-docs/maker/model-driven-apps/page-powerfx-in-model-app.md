---
title: "Using PowerFx in custom page for your model-driven app (preview)" 
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
# Using PowerFx in a custom page for your model-driven app (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This article outlines how the common Power Fx functions work within a custom page. Power Fx formulas in a custom page can be different than Power Fx in a standalone canvas app. This is because custom pages are a component within the model-driven app.

  > [!IMPORTANT]
  > - This is a preview feature, and isn't available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

## Add custom page notifications

A custom page notification can be shown to the user by calling the [Notify function](../canvas-apps/functions/function-showerror.md) to make a page message bar appear.  When the notify messages appear, they're docked above the page default to stay visible until disabled. Unless a timeout interval is provided, the message will disappear after the timeout interval. Avoid using a timeout interval of 10, it is currently treated as no timeout.

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

## Navigating from a custom page

A custom page navigation uses the Navigate and Back functions.

### See also

[Model-driven app custom page overview](model-app-page-overview.md)

[Navigating to and from a custom page in your model-driven app](navigate-page-examples.md)