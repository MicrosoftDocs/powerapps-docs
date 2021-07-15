---
title: "Add canvas components to a custom page for your model-driven app" 
description: ""
ms.custom: ""
ms.date: 07/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "hemantg"
ms.assetid: b4098c96-bce1-4f57-804f-8694e6254e81
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Add canvas components to a custom page for your model-driven app 

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This topic outlines the use of canvas components using canvas component libray for a custom page. 

  > [!IMPORTANT]
  > - This is a preview feature, and may not be available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

  > [!NOTE]
  > Custom page currently supports only a [limited set of controls](https://review.docs.microsoft.com/en-us/powerapps/maker/model-driven-apps/design-page-for-model-app?branch=pr-en-us-4627#supported-controls-in-custom-page) and only these  supported controls should be used to create canvas components for the custom page. 


Canvas components provides app makers an ability to create custom components in a low code fashion. These components can not only then be reused across custom pages and applications but also can be centrally updated, packaged and moved in the Dataverse solutions. See [Create a component for canvas apps](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/create-component) for more details on how to create a component. Since custom page authoring is limited to only one page, canvas components can only be authored inside a [component library](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/component-library). This is different from the standalone canvas apps which additionally has ability to create components at the app level.

## Create a canvas component using component library 
You can create a new [component library]/powerapps/maker/canvas-apps/component-library) or edit an existing one either from the Solutions area or Maker portal.  Browse to [make.powerapps.com](https://make.powerapps.com), select **Apps**, and then select **Component Libraries**:



![Create or edit component library.](../canvas-apps/media/component-library/create-edit-component-library.png "Create or edit component library")


## Create canvas component for use in custom page 
Components can now be created inside component library. Note that only the [supported set of controls](/powerapps/maker/model-driven-apps/design-page-for-model-app#supported-controls-in-custom-page) should be used to create components for custom page. You can enable the modern controls in the canvas component library settings for use in custom pages. 

   > ![Settings dialog for enabling modern controls](media/add-component-to-model-app/lib-setting-for-modern-controls.png "Settings dialog for enabling modern controls")


## Upcoming changes to canvas component for custom pages

* Code component support for the canvas libraries

## Known issues

* Custom page and canvas libraries do not maintain the reference when moved via solution across environments. 
## Related topics

[Model-driven app custom page overview](model-app-page-overview.md)

[Add a custom page to your model-driven app](add-page-to-model-app.md)

[Using PowerFx in custom page](page-powerfx-in-model-app.md)

[Overview of Power Apps connectors](../canvas-apps/connections-list.md)

[Add data connection in canvas designer](../canvas-apps/add-data-connection.md)
