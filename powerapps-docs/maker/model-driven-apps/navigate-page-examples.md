---
title: "Navigating to and from a custom page in your model-driven app (preview)" 
description: ""
ms.custom: ""
ms.date: 07/21/2021
ms.reviewer: ""
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: "how-to"
author: "aorth"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Navigating to and from a custom page (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This topic provides examples of navigating from a model-driven app page using the Client API to a custom page. It also includes examples of navigating from a custom page to other custom pages or a model page.

outlines the steps to use the Client API to open a custom page as a full page, dialog, or pane.  It provides examples of **custom** as a pageType value in [navigateTo (Client API reference)](../../developer/model-driven-apps/clientapi/reference/xrm-navigation/navigateto.md).

  > [!IMPORTANT]
  > - This is a preview feature, and isn't available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]


## Navigating from a custom page

Custom Page Fx [Navigate function](../canvas-apps/functions/function-navigate.md) has been updated to allow navigating to either model pages or custom pages.  These functions only apply when the custom page is running within a model-driven app.  During custom page authoring or previewing in canvas designer, these functions have no effect.

Navigate examples that use an entity must have it added as a Datasource in the page.

### Navigate to another custom page
A custom page can navigate to another custom page by passing the custom page display name as the first parameter.

```powerappsfl
Navigate( '<custom page>'  )
```

### Navigate to the default view for an entity
When Navigate is passed an entity as the first argument, it will open the user's default view page.

```powerappsfl
Navigate( Accounts )
```

### Navigate to a specific system view for an entity
When Navigate is passed an entity's Views enum, it will  open the specific system view for the entity.

```powerappsfl
Navigate( 'Accounts (Views)'.'My Active Accounts' )
```

### Navigate to the default form for an entity
When Navigate is passed a CDS record as the first argument, it will open the default entity form with the record.

```powerappsfl
Navigate( Gallery1.Selected )
```

### Navigate to the default form for an entity in create mode

When Navigate is passed a CDS record created from Defaults, it will open the default entity form with the table record as new record.  Defaults function takes an entity name to create the record.

```powerappsfl
Navigate( Defaults( Accounts ) )
```

### Navigate back to the prior page or close a dialog

When Back function is called in a custom page, it will close the current page and return to the priority model or custom page in the model-driven app.  If the custom page has multiple screens then see [Navigation advanced examples for custom page](navigate-page-advanced-examples.md) for advanced guidance.

```powerappsfl
Back( )
```


## Related topics

[Model-driven app custom page overview](model-app-page-overview.md)

[Add a custom page to your model-driven app](add-page-to-model-app.md)

[Navigating to and from a custom page using client API](../../developer/model-driven-apps/clientapi/navigate-to-custom-page-examples.md)

[navigateTo (Client API reference)](../../developer/model-driven-apps/clientapi/reference/xrm-navigation/navigateto.md)

[Navigate function (Power Apps expression function)](../canvas-apps/functions/function-navigate.md) 