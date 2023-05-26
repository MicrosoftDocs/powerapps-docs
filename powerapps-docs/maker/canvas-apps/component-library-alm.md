---
title: Component library application lifecycle management (ALM)
description: Learn about the application lifecycle management (ALM) with component libraries
author: jorisdg
ms.subservice: canvas-developer
ms.topic: article
ms.date: 06/10/2022
ms.author: jorisde
ms.reviewer: mkaur
search.audienceType:
  - maker
contributors:
  - jorisdg
  - mduelae
---

# Component library application lifecycle management (ALM)

A [component library](component-library.md) is a special type of canvas app that can contain one or more canvas components. These library components can then be used by all the other canvas apps in the environment. This capability enables you to create reusable shared components across all apps in an environment, unlike [app-level components](create-component.md#components-in-canvas-apps) that are restricted to one app.

To use a component from a component library, you have to first import the component into the canvas app. Once imported, you can then add the component to any app screen. Any updates in the component definition from the component library will prompt you to review and incorporate the change [on demand](component-library.md#method-2-proactive-check-for-updates) or when the [app is opened for editing](component-library.md#method-1-component-update-notification-on-app-edit). Component libraries and dependent apps can also be moved to another environment using standard [Microsoft Dataverse solutions](/power-platform/alm/solution-concepts-alm).

> [!NOTE]
> In this article, the term "import" refers to importing a component from a component library to an app, and shouldn't be confused with importing a solution into Dataverse.

When a component from a component library is imported into a canvas app, that component's definition is copied into the definition of the canvas app. Once a component definition has been imported, the app is "self-contained" as far as that component definition is concerned. The app maker can choose to [edit the component](component-library.md#library-component-customization), and create  local instances of the component within the app. At this point there's no direct link to the component library from where the component originated. This self-containment characteristic also applies if the canvas app is then migrated to a different environment where the component library isn't present.
You can continue to create instances of the imported component definition within the apps in the target environment, and the apps can still be published and played. No new updates will be prompted or received in the consuming app in this case.

In order to maintain the relationship from the app to the component library, ensure that you use the component library to make any changes to the component, instead of editing the component within the consuming app.

## Canvas apps and component libraries solution support

Consistent with the other solution object dependencies, if a canvas app imports a canvas component from a component library, it will have a dependency on that component library. In order to move an app to the new environment, you'll need to either package the component library inside the same solution or install it as a pre-requisite. App to component library dependency is maintained in the target environment. At a later point, when a component library with the updated component is imported using a solution into the target environment, existing apps will get the new component definitions using the regular [component update flow](component-library.md#update-a-component-library).

### Creating and exporting component library in a solution

You can either create a component library directly from within the solution, or add it to an existing solution.

:::image type="content" source="media/component-library-alm/new-add-existing-library-solution.png" alt-text="Add an existing component library to a solution, or a new one.":::

When a component library is saved in an environment that has Dataverse available, component library is automatically added to the default solution. A unique logical name is generated for the component library with the **Default CDS Publisher** prefix. This behavior is to ensure that the solution system is aware of its presence, and can link the dependencies from the apps that use the component library's logical name.

> [!NOTE]
> Component libraries created before the rollout of the component library ALM feature need to be edited, published, and the editor must be closed explicitly before they're enabled for the ALM capabilities. You can check the component library ALM readiness by its presence in the default solution.

:::image type="content" source="media/component-library-alm/check-default-solution.png" alt-text="Check default solution for your component library presence.":::

Component libraries inside a solution also support **Allow customizations** managed properties that govern the behavior of the component library in the target environment.

:::image type="content" source="media/component-library-alm/allow-customizations.png" alt-text="Allow customizations managed property for component library.":::

If you turn off this setting, and export the solution to a target environment, you won't be able to edit the component library.

:::image type="content" source="media/component-library-alm/edit-disabled.png" alt-text="You can't edit the component library that doesn't allow customizations.":::

### Component library dependencies

Apps that use components from the component library will be marked as dependent in the solutions infrastructure. This behavior applies to all apps that are added to any Dataverse solution in a given environment. You can still create apps outside of solutions, but those apps won't have any solution dependencies. You can later add these apps to solutions to make them part of the solution ALM.

:::image type="content" source="media/component-library-alm/dependencies.gif" alt-text="Animation that shows a canvas app in a solution using the component from the component library in the same solution and the dependencies for both.":::

If you import a solution that only has an app that uses a component from a component library, but excludes the component library, you'll see the following message:

"Import failed due to missing dependencies for \<app name\>".

In this case, you can choose to install the component library solution first, or bundle the component library with the solution that contains the canvas app. Either of the steps would ensure the app will have the dependency created in the target environment.

When the library is updated and a newer component version is imported through the solutions, the app will get a notification and receive the updates when the [app is opened for editing](component-library.md#method-1-component-update-notification-on-app-edit).

> [!NOTE]
> If the component library managed property **Allow customizations** is turned off, the component library can't be edited in the target environment.

Dependencies are calculated based on the latest published state of an app. If you restore an older version of the app that doesn't use a library component, the dependency will be removed from the app, and the solution. Importing a component into an app from a component library without actually using it also creates a dependency since the unused library component remains available within the app for a future use.

> [!TIP]
> Editing a component from a component library inside the consuming app creates a local copy. At this point, the library component is still available for use through the **Insert** pane. In order to remove the dependency completely, delete the component from **Insert** > **Library components** > **...** (ellipsis) > **Remove from app**.

## Best practices and troubleshooting

- Limit the number of components in a library to 20 to get optimal performance. Plan and create multiple component libraries in advance as the number of components in them will likely grow over time. This approach will also reduce the solution payload as apps are moved across the environment.

- There's a delay from when the component library is published to when it's available to the application, and can take up to 5 minutes.

- If the app isn't able to receive the update from the library component in the target environment where the solution is installed, check using the below actions:


    - Changes made to a component library in a target environment reside at the top layer of a component. Subsequently, these customizations define the runtime behavior of the component. To remove these unmanaged customizations, see [Remove an unmanaged layer](../data-platform/solution-layers.md#remove-an-unmanaged-layer).
    - Determine the component library logical name from the solution view. Use the default solution if library isn't explicitly added to solution.
    - Download app using the library component to local computer using **File** > **Save as** > **This computer**. Rename the downloaded file to have a .zip extension, and unzip the package. Open the **Properties.json** file, and then search for the keyword "LibraryDependencies". You should see a matching library logical name.
    - If you're consuming the solution, check that the canvas app has properly identified the component libraries as [solution dependencies](/power-platform/alm/solution-concepts-alm#solution-dependencies). If the solution doesn't properly identify the component libraries as solution dependencies, that means the app dependency to the component library link hasn't been created properly. In that case, check with the solution provider to resolve the issue.
    - If you're the solution publisher, check that the component libraries are saved with the library logical name in the solution, and that it's same as the one referenced in the component library .msapp package.

- Solution export always exports the latest version of the component library. Hence, always update the apps with the latest component version before exporting them through solutions. This action ensures that the apps have the same component version as available in the latest version of the component library. Apps and library are considered to be synchronized with each other when they're moved to a target environment for the first time; and hence, you're not prompted for any update being available when editing the app.

### See also

- [Canvas components](create-component.md)
- [Component library](component-library.md)
- [Map input fields of a component](map-component-input-fields.md)
- [Add multimedia to a component](component-multimedia.md)
- [Behavior formulas for components](component-behavior.md)
- [Power Apps component framework](../../developer/component-framework/component-framework-for-canvas-apps.md) 
- [Add canvas components to a custom page in a model-driven app](../model-driven-apps/page-canvas-components.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
