---
title: Component library
description: Learn about working with a library of reusable components for canvas apps.
author: hemantgaur
ms.service: powerapps
ms.topic: article
ms.date: 07/01/2021
ms.author: hemantg
ms.reviewer: tapanm
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - hemantgaur
  - tapanm-msft
---

# Component library

> [!IMPORTANT]
> This feature is still in public preview. For more information, see [Experimental and preview features](./working-with-experimental-preview.md).

In the [overview](create-component.md) article for creating components, you are introduced to components inside canvas app. As you create components inside an app, you can also create a library of components that can be reused. By creating a component library, app makers easily share and update one or more components with other makers.

Component libraries are containers of component definitions that make it easy to:

- Discover and search components.
- Publish updates.
- Notify app makers of available component updates. 

> [!NOTE]
> Component libraries are the recommended way to reuse components across apps. When using a component library, an app maintains dependencies on the components it uses. The app maker will be alerted when the updates to dependent components become available. Hence, all new reusable components should be created within the component libraries instead. An earlier Power Apps feature that allowed [importing components from one canvas app to another](create-component.md?#import-and-export-components) is retired.

## Difference between an app and a component library

A component library provides a centralized and managed repository of components for reusability. 

The **Insert** pane on the left navigation defaults to a components tab if you create a component library. When you create an app, this view shows screens instead of components. 

The screens inside a component library are available for testing only. It provides library creators a way to quickly test the created components on an actual screen and also validate the update behavior as components are enhanced over time. To use the components from the component library, you must create an app that uses the component library.

You can preview component library components using the screens inside the library with the play option. When you select the component tab, the play option is disabled. The component library doesn't display when using Power Apps Mobile.

> [!NOTE]
> The component library discussed in this article is different from the Power Apps component framework that enables developers and makers to create code components for model-driven and canvas apps. For more information, go to [Power Apps component framework overview](../../developer/component-framework/overview.md).

## Working with component library

You can create a new component library or edit an existing component library from the same interface. Browse to [make.powerapps.com](https://make.powerapps.com), select **Apps**, and then select **Component Libraries**:

![Create or edit component library.](./media/component-library/create-edit-component-library.png "Create or edit component library")

## Create an example component library

The steps to create components inside a component library are the same as creating components inside an app. You'll create a component library and then reuse the steps for creating components from [components overview example](create-component.md#create-an-example-component). Then you'll use the component library to provide the reusable components in a new app.

1. Sign in to [make.powerapps.com](https://make.powerapps.com).

1. Select **Apps** in the left navigation, select **Component Libraries**, and then select **New component library**.

1. Name the component library as *Menu components*; you can also provide a different name of your choice.

1. Follow the steps to create components from [components overview example](create-component.md#create-an-example-component). You don't have to open Power Apps Studio or create a new blank app, since you already have created a new component library. Start with step 2. 

    After following the steps to create components, follow the next set of steps to also [add components to a screen](create-component.md#add-component-to-a-screen) and the steps to [create output property](create-component.md#create-and-use-output-property). 

1. After you complete the components creation and testing, save the component library by selecting the **File** menu and then selecting **Save**. 

    You also have an option to save a **version note**. A version note is useful to retrieve versions of a component library and for upgrading the components used in apps from this component library.

    ![Version note when saving component library.](./media/component-library/save-component-libray-version-note.png "Version note when saving component library")

    > [!TIP]
    > A version note is useful when reviewing versions of a component library and for the app makers using your component library to review changes and update apps consuming these components as needed. Go to [update a component library](component-library.md?#update-a-component-library) for more details.   

1. A saved component library can be published. Only published component library updates are available for apps that consume a component library. Select **Publish** to publish the component library version:

    ![Publish component library version.](./media/component-library/publish-component-library.png "Publish component library version")

## Import from a component library

After you create a component library and publish, apps can consume the components from this component library by importing the library. You can also [share a component library](component-library.md#component-library-permissions).

To import from a component library, edit an existing app or create a new app. After the app opens in canvas app studio, select **Insert** or the **+** on the left navigation. Then select **Get more components** to list the component libraries available in the current environment:

![Get more components.](./media/component-library/get-more-components.png "Get more components")

You'll see the list of component libraries available in the current environment on the right side of the screen. Select an individual component from a component library. Or use **Select all** to import all of the components from the library at once:

![Import components.](./media/component-library/components.png "Import components")

> [!NOTE]
> If a maker doesn't see the component library listed in the import section, ensure the component library is shared with the maker. For more details, go to [component library permissions](component-library.md#component-library-permissions). 

Notice you can select and import more than one component and across different component libraries. 

Components available inside the app are listed under the **Custom** category in the list of components in the **Insert** pane. Components available from imported component libraries are listed under the **Library components** category:

![Insert components to the app.](./media/component-library/insert-components.png "Insert components to the app")

## Update a component library

You can modify an existing component library and save any changes with additional version notes. However, the updated component library version must be published for use in existing apps that use the component library. The [example component library](component-library.md#create-an-example-component-library) steps above explain how to publish a component library after saving it.

Makers of other apps are notified of updated components being available. The notification appears when makers edit the apps in canvas app studio. They can choose to update the components:

![Update available.](./media/component-library/update-available.png "Update available")

Select **Review**, and you'll see the option to update the component:

![Update component.](./media/component-library/update-components.png "Update component")

Notice that the version note you added when publishing the component library version shows up here. 

Select **Update** to update the components.

## Component library permissions

Sharing a component library works the same way you share a canvas app. When you share a component library, you allow others to reuse the component library. Once shared, others can edit the component library and import components from this shared component library for creating and editing apps. If shared as a co-owner, a user can use, edit, and share a component library but not delete or change the owner.

## Known limitations

- [Known limitations](create-component.md#known-limitations) applicable to components also applies to component libraries.
- You can't import components using a component library from locally saved component library files. If you try to import a locally saved component library using **File** > **Save As** > **This Computer** and download the component library file as an app, following error message appears: 

    ![Import component library file.](./media/component-library/import-component-library-file.png "Import component library file")

- You can't add existing component libraries to a [solution](add-app-solution.md). However, you can create new component libraries for solutions using add component library flow.

- If you import a component from a component library, you can't edit it inside the consuming app. If you select **Edit component**, you'll see an option to create a copy of the component inside the current app for you to make changes: 

    ![Edit library component.](./media/component-library/edit-library-component.png "Edit library component")

    If you select **Create a copy**, the component is copied to the local app. The local copy of the component appears under the **Custom** category in the **Insert** pane. This local copy of the component won't receive updates if a new version of the originating component library is published later.
    
- When a component is added to an app from the component library and the theme of the app is updated, the component becomes a local app component and is no longer associated with the master component in the component library.

## Next steps

Learn [behavior formulas](component-behavior.md) for canvas apps.

### See also

Canvas app [components overview](create-component.md) and working with components in an app.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]