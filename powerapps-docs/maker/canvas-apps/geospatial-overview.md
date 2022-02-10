---
title: Add Geospatial controls to apps made with Microsoft Power Apps
description: Geospatial controls let you view and manipulate 3D objects and images in the real world, in augmented reality. 
author: anuitz
ms.service: powerapps
ms.topic: overview
ms.custom: canvas, ce06122020
ms.reviewer: tapanm
ms.date: 02/09/2022
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


# Add geospatial controls to your app


You can add a number of geospatial controls to your canvas app to support scenarios that involve mapping locations and addresses.

Components are groups of controls that can answer the need for a specific scenario. You can read more about controls and how to build your own in [the Power Apps developer library](../../developer/component-framework/custom-controls-overview.md).

The following prebuilt controls can be used for geospatial and mapping scenarios:

- [Interactive map](geospatial-component-map.md)
- [Address input](geospatial-component-input-address.md)

## Prerequisites
1. An admin must [add a Microsoft Dataverse database](/power-platform/admin/create-database) to the environment.
3. An admin must [enable the geospatial features in the Power Platform admin center](#enable-the-geospatial-features-for-the-environment) for the environment. This requires reviewing and agreeing to specific terms of service.
3. An admin must [ensure the geospatial controls will not be blocked by the environment's data loss prevention policies](#review-the-environments-data-loss-prevention-policies).

    >[!IMPORTANT]
    >The controls require the default **Organizations** data source to be present. This data source is included whenever you insert the controls into an app, but if you manually delete it you'll need to add it before the controls will work:
    >
    >1. With the control selected, go to the **Data sources** tab on the side navigation menu.
    >2. In the search field, enter **Organizations**, and then select the data source that appears. This will add it to the control.

## Enable the geospatial features for the environment

Before you can use geospatial features in your apps, an admin must enable access to the features for the environment where you want to create your app.

The geospatial features require additional terms of use that must be reviewed and agreed to.

1. Open the [Power Platform admin center](https://admin.powerplatform.microsoft.com).

1. On the **Environments** tab, select the environment you want to use for your apps, and then select **Settings** from the top menu.

    ![Environment selected in the Power Platform admin center.](./media/geospatial/ppac-environment.png "Environment selected in the Power Platform admin center")

1. Expand **Product**, and then select **Features**.

    ![Screenshot of environment settings with Features selection highlighted.](./media/geospatial/ppac-settings.png "Screenshot of environment settings with Features selection highlighted")

1. Under **Geospatial services**, set the toggle switch to **On**. A terms of service notice will appear. Read through the terms of service, and if you agree, select the checkbox **I agree to the terms of service**, and then select **Enable**.

    :::image type="content" source="./media/geospatial/ppac-terms.png" alt-text="Screenshot of the terms of service.":::

    >[!IMPORTANT]
    >You must read and agree to the terms of service before you can use geospatial features. 

1. Select **Save** at the bottom of the settings page.

    ![Screenshot of the Save button.](./media/geospatial/ppac-save.png "Screenshot of the Save button")

## Review the environment's data loss prevention policies

The geospatial controls require the Microsoft Dataverse and Spatial Services connectors. This connector is used by the Power Apps Maps and Address Input controls to connect to Microsoft’s Azure Maps service. It is used to fetch map tiles and satellite imagery, geocode addresses, and search for addresses. Thus, it is required for the Interactive Map and Address Input controls to function.

For the controls to function properly, these connectors must not have conflicting data loss prevention policies. An admin must review the environment's data loss prevention policies and ensure that these connectors are classified under the same data group, typically the **Business** data group. [Learn more about data loss prevention policies for Power Platform](/power-platform/admin/prevent-data-loss).

## Privacy and security considerations

- Power Apps doesn’t link search queries to any user when shared with TomTom, and the shared search queries can’t be used to identify individuals.
- Azure Maps doesn't store the request information sent by you. For more information about Azure Maps compliance, see [Azure global compliance](https://azure.microsoft.com/blog/new-azure-maps-make-identifying-local-compliance-options-easy/)
- Requests sent between TomTom and Azure Maps are not exposed over the public Internet.
- Requests sent between apps you create with the geospatial controls and Azure Maps are sent over HTTPS.
- Power Apps doesn't send any user identifiers or tracking data to Azure Maps, Bing Maps, or TomTom.
- The following table describes the user data that Power Apps sends to Azure Maps, Bing Maps, and TomTom:

    | Control | Feature | Data | Sent to Azure Maps | Sent to Bing Maps | Sent to TomTom | Purpose |
    | ------- | ------- | ---- | ------------------ | ----------------- | -------------- | ------- |
    | Map | Show map tiles | Coordinates in and around the map view | Yes | No | Yes | To show the map tiles in the map view. |
    | Map | Show pins and route waypoints | Pins and route waypoint addresses | No | Yes | Yes | To translate addresses to latitude/longitude coordinates, and show them on the map. |
    | Map | Show routes | Route waypoint coordinates | Yes | No | Yes | To calculate routes between waypoints. |
    | Address Input | Address Search | Address search query string | No | Yes | Yes | To show address search results. |
    | Address Input | Address Search | Current device location | No | Yes | Yes | To bias address search results around the device location. |

## Next steps

Start installing the controls in your apps:

- Visualize and interpret location data with the **[Interactive map](geospatial-component-map.md)** control.
- See dynamic address suggestions as you type with the **[Address input](geospatial-component-input-address.md)** control.

### See also

[Create an app that uses mobile sensors](how-to/mobile-sensors.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
