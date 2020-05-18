---
title: Use mixed reality components in Power Apps (Preview)
description: Use augmented reality features in Power Apps to view and manipulate 3D models and 2D images in the real world, take measurements, and create and view 3D digital shapes.
author: iaanw
manager: shellyha
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 5/4/2020
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Add mixed reality components to your canvas app (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../../includes/cc-beta-prerelease-disclaimer.md)]

You can add a number of mixed reality (MR) components to your canvas app to support multiple 3D and mixed reality scenarios.

Components are groups of controls that can answer the need for a specific scenario. For example, you can use these MR components to:

- View and manipulate 3D content
- Overlay 3D content and 2D images onto the feed from the camera
- Measure distance, area, and volume using your device with MR
- Identify spaces in the real world through an MR overlay

You can read more about components and how to build your own in [Power Apps component framework docs](/powerapps/developer/component-framework/custom-controls-overview).

> [!NOTE]
> Mixed reality components are currently an experimental preview feature that is only available in [https://preview.create.powerapps.com](https://preview.create.powerapps.com) on a [Power Apps Preview Program environment](/power-platform/admin/preview-environments).

The following pre-built components can be used for mixed reality scenarios:

- [View in 3D](mixed-reality-component-view-3d.md)
- [View in mixed reality](mixed-reality-component-view-mr.md)
- [Measure in mixed reality](mixed-reality-component-measure-distance.md)
- [View shape in mixed reality](mixed-reality-component-view-shape.md)

## Prerequisites

1. [Enable the mixed reality features for each app](#enable-the-mixed-reality-features-for-each-app).
2. You'll need a mixed reality-capable device. Any [ARCore capable device](https://developers.google.com/ar/discover/supported-devices) is supported, as are [certain Apple iOS devices](https://www.apple.com/augmented-reality/).
3. Use a [Power Apps Preview Program environment](/power-platform/admin/preview-environments).

### Enable the mixed reality features for each app

For each app you create, you need to enable the mixed reality features:

1. Open the app for editing in the Power Apps studio at [https://preview.create.powerapps.com](https://preview.create.powerapps.com).

2. Select **File** from the top menu.

    ![](./media/augmented-overview/augmented-overview-file.png)

3. Go to the **Settings** tab, select **Advanced settings**, and scroll down to find the **Mixed reality features** option. Set the option to **On**.

    ![](./media/augmented-overview/augmented-enable-mixed-reality.png)

4. Return to editing your app by selecting the back arrow icon

    ![](./media/augmented-overview/augmented-overview-back.png)

5. Open the **Insert** pane to see the mixed reality components under **Media** and **Mixed Reality**.

    ![](./media/augmented-overview/augmented-overview-insert-all.png)

## Next steps

Start installing the components in your apps:

- View 3D content with the **[View in 3D](mixed-reality-component-view-3d.md)** component.
- View images and 3D content in the real world with the **[View in mixed reality](mixed-reality-component-view-mr.md)** component.
- Measure distance, area, and volume with the **[Measure in mixed reality](mixed-reality-component-measure-distance.md)** component.
- Create and view predefined 3D shapes with the **[View shape in mixed reality](mixed-reality-component-view-shape.md)** component
