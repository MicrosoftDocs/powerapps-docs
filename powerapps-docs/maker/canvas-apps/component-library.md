---
title: Create a component library for canvas apps | Microsoft Docs
description: Library of reusable components for canvas apps
author: yifwang
ms.service: powerapps
ms.topic: article
ms.date: 02/15/2020
ms.author: yifwang
ms.reviewer: tapanm
search.audienceType:
  - maker
search.app:
  - PowerApps
---

# Component library in canvas app

In the [overview](create-component) article for creating components, you are introduced to components inside canvas app. While you can create components inside an app and reuse them inside the same or any other app, you can also create a library of components that can be reused. This enables app makers to share and update components with other makers by creating component libraries. 

Component libraries are containers of component definitions that make it easy to discover and search for components, publish updates across environments, and notify app makers of available component updates. Data source references are also supported in components.

You can use components in gallery controls and forms. Components can also use collections. When you export an app with components that include related media files, the media files are exported with the control.

Solution awareness of canvas components and apps that use them is also enabled through component libraries. Migrating an app and its dependencies across environments is now possible through Common Data Service solutions. Canvas apps and component libraries are handled very similarly and modeled under the same 'CanvasApp' entity.

## Difference between an app and a component library

When you create a component library, the tree view on left navigation by default displays components. When you create an app, this view shows screens instead of components. 

The screens inside a component library are available for testing only. A component library cannot be used as an app even if you configure multiple screens. If you want to use components that you created inside a component library, you must create an app that uses the component library. And you can share this app with others like any other canvas app.

Components available inside the app are listed under **Custom** category in list of components inside tree view; whereas components available from imported component libraries are listed under **Library components** category:

![Insert components to the app](./media/component-library/insert-components.png)

As mentioned in [components overview](create-component.md), you cannot **preview** components from components section or the component library like the way you can preview an app using the play button on top right side of the Power Apps Studio. In order to experience the components, you must use components inside an app. Component library does not display when using Power Apps mobile.

## Working with component library

You can create a new component library or edit an existing component library from the same interface by browsing to make.powerapps.com and selecting **Component Libraries**:

![Create or edit component library](./media/component-library/create-edit-component-library.png)

## Create an example component library

The steps to create components inside a component library are same as creating components inside an app. In this example, you'll create a component library first and then reuse the steps for creating components from [components overview example](create-component.md#create-an-example-component). Once you create the required components and test the functionality using those steps, you'll use the component library to reuse the components in a new app.

1. Go to make.powerapps.com, select **Apps** in left navigation, select **Component Libraries** and then select **New component library**.

1. Follow the steps to create components from the [components overview example](create-component.md#create-an-example-component) topic.

1. After you completed the components creation and testing, save the component library. 

## Component library permissions

Sharing a component library works the same way you share a canvas app. When you share a component library, you are allowing others to reuse the component library. Once shared, others can edit the component library and import components from this shared component library for creating and editing apps.

