---
title: Create a component library for canvas apps | Microsoft Docs
description: Library of reusable components for canvas apps
author: yifwang
ms.service: powerapps
ms.topic: article
ms.date: 02/20/2020
ms.author: yifwang
ms.reviewer: tapanm
search.audienceType:
  - maker
search.app:
  - PowerApps
---

# Component library

> [!IMPORTANT]
> This feature is still in public preview. For more information, see [Experimental and preview features](working-with-experimental.md).

In the [overview](create-component.md) article for creating components, you are introduced to components inside canvas app. As you create components inside an app, you can also create a library of components that can be reused. By creating a component library, app makers easily share and update one or more components with other makers.

Component libraries are containers of component definitions that make it easy to:

- Discover and search components.
- Publish updates across environments.
- Notify app makers of available component updates. 

> [!NOTE]
> Component libraries are the recommended way to reuse components across apps. When using component library, an app maintains dependencies on the components it uses. The app maker will be alerted when the updates to dependent components become available. Hence, all new reusable components should be created within the component libraries instead. An earlier Power Apps feature that allowed [importing components from one canvas app to another](create-component.md?#import-and-export-components) will be deprecated.

## Difference between an app and a component library

A component library provides a centralized and managed repository of components for reusability. 

**Insert** pane on left navigation defaults to components tab if you create a component library. When you create an app, this view shows screens instead of components. 

The screens inside a component library are available for testing only. It provides library creators a way to quickly test the created components on actual screen and also validate the update behavior as components are enhanced over time. To use the components from component library, you must create an app that uses component library.

You can preview component library components using the screens inside the library with the play option. When you select component tab, the play option is disabled. Component library doesn't display when using Power Apps mobile.

> [!NOTE]
> Component library discussed in this article is different from the Power Apps component framework that enables developers and makers to create code components for model-driven and canvas apps. For more information, read [Power Apps component framework overview](https://docs.microsoft.com/powerapps/developer/component-framework/overview).

## Working with component library

You can create a new component library or edit an existing component library from the same interface. Browse to [make.powerapps.com](https://make.powerapps.com), select **Apps**, and then select **Component Libraries**:

![Create or edit component library](./media/component-library/create-edit-component-library.png)

## Create an example component library

The steps to create components inside a component library are same as creating components inside an app. You'll create a component library. And then reuse the steps for creating components from [components overview example](create-component.md#create-an-example-component). And then you'll use the component library to provide the reusable components in a new app.

1. Sign in to [make.powerapps.com](https://make.powerapps.com).

1. select **Apps** in left navigation, select **Component Libraries**, and then select **New component library**.

1. Name the component library as *Menu components*; you can also provide a different name of your choice.

1. Follow the steps to create components from [components overview example](create-component.md#create-an-example-component). You don't have to open Power Apps Studio or create a new blank app, since you already have created a new component library. Start with step 2. 

    After following steps to create components, follow next set of steps to also [add components to a screen](create-component.md#add-component-to-a-screen) the steps to [create output property](create-component.md#create-and-use-output-property). 

1. After you completed the components creation and testing, save the component library by selecting **File** menu and then selecting **Save**. 

    You also have an option to save a **Version note**. Version note is useful to retrieve versions of a component library. And when upgrading the components used in apps from this component library.

    ![Version note when saving component library](./media/component-library/save-component-libray-version-note.png)

    > [!TIP]
    > Version note is useful when reviewing versions of a component library and for the app makers using your component library to review changes and update apps consuming these components as needed. Read [update a component library](component-library.md?#update-a-component-library) for more details.   

1. Saved component library can be published. Only published component library updates are available for apps that consume a component library. Select **Publish** to publish the component library version:

    ![Publish component library version](./media/component-library/publish-component-library.png)

## Import from a component library

After you create a component library and publish, apps can consume the components from this component library by importing the library. You can also [share a component library](component-library.md#component-library-permissions).

To import from a component library, edit an existing app or create a new app. After app opens in canvas app studio, select **Insert** or the **+** on the left navigation. And then select **Get more components** to list the component libraries available in current environment:

![Get more components](./media/component-library/get-more-components.png)

You'll see the list of component libraries available in current environment on right side of the screen. Select an individual component from a component library. Or use **Select all** to import all of the components from the library at once:

![Import components](./media/component-library/components.png)

> [!NOTE]
> If maker doesn't see the component library listed in import section, ensure the component library is shared with the maker. For more details, read [component library permissions](component-library.md#component-library-permissions). 

Notice you can select and import more than one component and across different component libraries. 

Components available inside the app are listed under **Custom** category in list of components in the **Insert** pane. Components available from imported component libraries are listed under **Library components** category:

![Insert components to the app](./media/component-library/insert-components.png)

## Update a component library

You can modify existing component library and save any changes with additional version notes. However, the updated component library version must be published for use in existing apps that use the component library. [Example component library](component-library.md#create-an-example-component-library) steps above explain how to publish a component library after saving it.

Makers of other apps are notified of updated components being available. The notification appears when makers edit the apps in canvas app studio. And can choose to update the components:

![Update available](./media/component-library/update-available.png)

Select **Review**, and you'll see the option to update the component:

![Update component](./media/component-library/update-components.png)

Notice the version note you added when publishing component library version shows up here. 

Select **Update** to update the components.

## Component library permissions

Sharing a component library works the same way you share a canvas app. When you share a component library, you allow others to reuse the component library. Once shared, others can edit the component library and import components from this shared component library for creating and editing apps. If shared as co-owner, user can use, edit, share component library but not delete or change owner.

## Known limitations

- [Known limitations](create-component.md#known-limitations) applicable to components also applies to component library.
- You can't import components using component library from locally saved component library file. If you try to import a locally saved component library using **File** -> **Save As** -> **This Computer** and download the component library file as an app, following error message appears: 

    ![Import component library file](./media/component-library/import-component-library-file.png)

- You can't add existing component libraries to a [solution](add-app-solution.md). However, you can create new component libraries for solutions using add component library flow.

- If you import a component from a component library, you can't edit it inside the consuming app. If you select **Edit component**, you'll see an option to create a copy of the component inside current app for you to make changes: 

    ![Edit library component](./media/component-library/edit-library-component.png)

    If you select **Create a copy**, the component is copied to the local app. The local copy of the component appears under the **Custom** category in the **Insert** pane. This local copy of the component won't receive updates if a new version of the originating component library is published later.
    
- When a component is added to an app from the component library and the theme of the app is updated, the component becomes a local app component and is no longer associated to the master component in the component library.

## Next steps

Learn [behavior formulas](component-behavior.md) for canvas app.

### See also

Read canvas app [components overview](create-component.md) and working with components in an app.
