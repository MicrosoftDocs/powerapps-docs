---
title: Add geospatial controls to canvas apps
description: Add geospatial controls to your canvas apps to view 3D objects and 2D images in the real world using mixed-reality features in Power Apps. 
author: anuitz
ms.service: powerapps
ms.topic: overview
ms.custom: canvas, ce06122020
ms.date: 03/3/2022
ms.reviewer: mkaur
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - anuitz
---

# Add geospatial controls to your canvas apps

Add interactive maps with dynamic routing and address lookup to your canvas apps using geospatial controls.

Use the following prebuilt controls for geospatial applications:

- [Interactive map](geospatial-component-map.md)
- [Address input](geospatial-component-input-address.md)

## Prerequisites

Before you can use geospatial features in your apps, your Power Platform administrator has a couple of tasks to complete:

1. Enable geospatial features in the Power Platform admin center for the environment you intend to use. The geospatial features require their own terms of service, which your admin must review and agree to.
2. Make sure the geospatial controls aren't blocked by the environment's data loss prevention policies.

>[!IMPORTANT]
>Your app must be connected to the **Organizations** data source to use geospatial controls. The data source is included whenever you insert a geospatial control in an app. If you manually delete it, you'll need to connect it again.
>
>1. With the geospatial control selected, open the **Data** tab, and then select **Add data**.
>2. Search for and select **Organizations**.

### Enable geospatial features for the environment

If you don't have administrative access to the Power Platform admin center, ask your admin to enable geospatial features for you.

1. Open the [Power Platform admin center](https://admin.powerplatform.microsoft.com).
1. On the **Environments** tab, select the environment you want to use for your apps, and then select **Settings**.

    :::image type="content" source="./media/geospatial/ppac-environment.png" alt-text="A screenshot of the Power Platform admin center, with an environment selected.":::

1. Expand **Product**, and then select **Features**.

    :::image type="content" source="./media/geospatial/ppac-settings.png" alt-text="A screenshot of the Power Platform admin center, with the environment Product Features setting selected.":::

1. Turn on the **Geospatial services** toggle.
1. Read the terms of service. Select **I agree to the terms of service**, and then select **Enable**.

    >[!IMPORTANT]
    >
    >The terms of service must be agreed to before you can use geospatial features in your apps.
    >
    >Mapping capabilities are provided by a third party. Microsoft shares address and location queries, but not customer or user names, with the provider. Requests are sent securely over HTTPS or aren't exposed to the public Internet.

1. Select **Save**.



### Review the environment's data loss prevention policies

Geospatial controls use the Microsoft Dataverse and Spatial Services connectors to fetch map tiles and to look up and geocode addresses. Your Power Platform admin must make sure data loss prevention policies that apply to those connectors don't conflict with policies that affect the controls.

Your admin should confirm that the Microsoft Dataverse and Spatial Services connectors are classified under the same data group, typically **Business**. [Learn more about data loss prevention policies for Power Platform](/power-platform/admin/prevent-data-loss).

### Next steps

Add the controls to your apps:

- Visualize and interpret location data with the **[Interactive map](geospatial-component-map.md)** control.
- See dynamic address suggestions as you type with the **[Address input](geospatial-component-input-address.md)** control.

### See also

[Create an app that uses mobile sensors](how-to/mobile-sensors.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
