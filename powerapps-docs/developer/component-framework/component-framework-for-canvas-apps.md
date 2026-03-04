---
title: Code components for canvas apps  | Microsoft Docs
description: Learn how to create code components using Power Apps component framework for canvas apps.
keywords:
author: anuitz
ms.author: anuitz
ms.date: 01/09/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: pcf
contributors:
 - JimDaly
---

# Code components for canvas apps

Professional developers can use Power Apps component framework to create code components that they can use in their canvas apps. For more information, see [Power Apps component framework overview](overview.md).

App makers can use Power Apps component framework to create, import, and add code components to canvas apps by using [Microsoft Power Platform CLI](get-powerapps-cli.md). Certain APIs might not be available in canvas apps. Check each API to determine where it's available.  

## Security considerations

> [!WARNING]
> Code components contain code that Microsoft didn't generate and can potentially access security tokens and data when rendered in Power Apps Studio. When adding code components to a canvas app, make sure that you get the code component solutions from a trusted source. This vulnerability doesn't exist when playing the canvas app.  

When you open a canvas app that contains code components in Power Apps Studio, a warning message about potentially unsafe code appears. Code components in the Power Apps Studio environment have access to security tokens, so only open components from trusted sources. Administrators and system customizers should review and validate all code components before importing those components in an environment and making them available for makers to use in their apps. The `Default` publisher appears when you import code components by using an unmanaged solution or when you use [pac pcf push](/power-platform/developer/cli/reference/pcf#pac-pcf-push) to install your code component.

![Safety warning.](media/canvas-app-safety-warning.png "Safety warning")  

## Prerequisites

- A Power Apps license is required. For more information, see [Power Apps component framework licensing](overview.md#licensing).
- System administrator privileges are required to enable the Power Apps component framework feature in the environment.

## Enable the Power Apps component framework feature

To add code components to an app, you need to enable the Power Apps component framework feature in each environment where you want to use them. By default, the Power Apps component feature is enabled for model-driven apps. To enable an environment to use code components inside its apps:

1. Sign in to [Power Apps](https://powerapps.microsoft.com/).

1. Select **Settings** ![Settings.](media/settings.png), and then select **Admin Center**.

    > [!div class="mx-imgBorder"]
    > ![Settings and Admin Center.](media/select-admin-center-from-settings.png "Settings and Admin Center")

1. On the left pane, select **Environments**, select the environment where you want to enable this feature, and then select **Settings**.

1. Expand **Product**, and select **Features**.

1. From the list of available features, turn on **Power Apps component framework for canvas apps**, and then select **Save**.

   > [!div class="mx-imgBorder"]
   > ![Enable Power Apps component framework.](media/enable-pcf-feature.png "Enable Power Apps component framework")

## Implementing code components

After you enable the Power Apps component framework feature in your environment, you can start implementing the logic for code components. For a step-by-step tutorial, see [Create your first code component](implementing-controls-using-typescript.md).

Check the [limitations](limitations.md) of code components in canvas apps before starting implementation.

## Add components to a canvas app

1. Go to Power Apps Studio.

1. Create a new canvas app, or edit an existing app to which you want to add the code component.

   > [!IMPORTANT]
   > Make sure you [imported](../../maker/data-platform/import-update-export-solutions.md) the solution .zip file containing the code components into Microsoft Dataverse.

1. On the left pane, select **Add** (**+**), and then select **Get more components**.

   > [!div class="mx-imgBorder"]
   > ![Insert components.](media/insert-code-components-using-get-more-components.png "Insert components")

1. Select the **Code** tab, select a component from the list, and then select **Import**.

    > [!div class="mx-imgBorder"]
    > ![Import a component.](media/insert-component-add-sample-component.png "Import a component")

1. On the left pane, select **+**, expand **Code components**, and then select the component to add it to the app.

   > [!div class="mx-imgBorder"]
   > ![Add a component.](media/add-sample-component-from-list.png "Add a component")

   > [!NOTE]
   > You can also add components by selecting **Insert** > **Custom** > **Import component**. This option is deprecated and will be removed in a future release, so use the flow described earlier.
   >

On the **Properties** tab, you see the code component properties.

> [!div class="mx-imgBorder"]
> ![Default code component properties pane.](media/property-pane-with-parameters.png "Default code components properties pane")

> [!NOTE]
> To re-import existing code components and make the properties available in the default **Properties** tab, update the code component's manifest version. The properties remain available on the **Advanced** properties tab.

## Delete a code component from a canvas app

1. Open the app where you added the code component.
1. On the left pane, select **Tree view**, and then select the screen where you added the code component.
1. Next to the component, select **More** (**...**), and then select **Delete**.

   > [!div class="mx-imgBorder"]
   > ![Delete a code component.](media/delete-code-component.png "Delete a code component")

1. Save the app to see the changes.

## Update existing code components

To see runtime changes after updating code components, change the `version` property in the manifest file. Change the version of the component whenever you make changes.

> [!NOTE]
> Power Apps Studio updates existing code components only when you close or reopen the app. When you reopen the app, it asks you to update the code components. Simply deleting or adding code components back into the app doesn't update the components. Publish all the customizations in the updated solution first, otherwise updates made to the code component don't appear.

### See also

[Power Apps component framework overview](overview.md)<br/>
[Create your first code component](implementing-controls-using-typescript.md)<br/>
[Learn Power Apps component framework](/training/paths/use-power-apps-component-framework)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
