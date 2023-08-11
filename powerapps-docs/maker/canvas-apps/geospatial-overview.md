---
title: Add geospatial controls to canvas apps
description: Add geospatial controls to your canvas apps to see interactive maps with dynamic routing and get address autosuggestion
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
contributors:
  - mduelae
  - anuitz
---

# Add geospatial controls to your canvas apps

Add interactive maps with dynamic routing and address lookup to your canvas apps using geospatial controls.

Use the following prebuilt controls for geospatial applications:

- [Interactive map](geospatial-component-map.md)
- [Address input](geospatial-component-input-address.md)

The map control runs with limited features available by default. You can enable additional map control features and support for the address input control [by turning on full support in the Power Platform admin center](#prerequisites-for-full-support). Refer to the [table at the bottom of the page](#privacy-and-security-considerations) for more details on data usage in limited and full support.

## Prerequisites for full support

Before you can use geospatial features in your apps, your Power Platform administrator has a couple of tasks to complete:

1. Enable geospatial features in the Power Platform admin center for the environment you intend to use. The geospatial features require their own terms of service, which your admin must review and agree to.
2. Make sure the geospatial controls aren't blocked by the environment's data loss prevention policies.

  >[!IMPORTANT]
  > Geospatial controls are not available in [Power Apps US Government](/power-platform/admin/powerapps-us-government).

### Enable geospatial features for the environment

If you don't have administrative access to the Power Platform admin center, ask your admin to enable geospatial features for you. You can similarly follow these steps to disable geospatial features.

1. Open the [Power Platform admin center](https://admin.powerplatform.microsoft.com).
1. On the **Environments** tab, select the environment you want to use for your apps, and then select **Settings**.

    :::image type="content" source="./media/geospatial/ppac-environment.png" alt-text="A screenshot of the Power Platform admin center, with an environment selected.":::

1. Expand **Product**, and then select **Features**.

    :::image type="content" source="./media/geospatial/ppac-settings.png" alt-text="A screenshot of the Power Platform admin center, with the environment Product Features setting selected.":::

1. Under **Map and address services**, turn on the **Full** toggle. You can use the toggles in this section to similarly turn on and off limited support as well.

    :::image type="content" source="./media/geospatial/geo-admin-flag.png" alt-text="A screenshot of the Power Platform admin center, with the default Limited and Full support toggle settings in view. The Limited toggle is on and the Full toggle is off.":::
1. Read the terms of service. Select **I agree to the terms of service**, and then select **Enable**.

    >[!IMPORTANT]
    >
    >The terms of service must be agreed to before you can use all geospatial features in your apps.
    >
    >Mapping capabilities are provided by a third party. Microsoft shares address and location queries, but not customer or user names, with the provider. Requests are sent securely over HTTPS or aren't exposed to the public Internet.

1. Select **Save**.

### Review the environment's data loss prevention policies

Geospatial controls use the Spatial Services connector to fetch map tiles and to look up and geocode addresses. Your Power Platform admin must make sure data loss prevention policies that apply to that connector don’t conflict with the policies that affect the controls. [Learn more about data loss prevention policies for Power Platform](/power-platform/admin/prevent-data-loss).


## Privacy and security considerations

- Power Apps doesn’t link search queries to any user or tenant when shared with TomTom, and the shared search queries can’t be used to identify individuals or tenants.
- Azure Maps doesn't store the request information sent by you. For more information about Azure Maps compliance, see [Azure global compliance](https://azure.microsoft.com/blog/new-azure-maps-make-identifying-local-compliance-options-easy/)
- Requests sent between TomTom and Azure Maps are not exposed over the public Internet.
- Requests sent between apps you create with the geospatial controls and Azure Maps are sent over HTTPS.
- The following table describes the user data that Power Apps sends to Azure Maps, Bing Maps, and TomTom on full support:

    | Control | Feature | Data |  Purpose | Sent to Azure Maps | Sent to Bing Maps | Sent to TomTom | User identifiers or tracking data sent | Enabled in Full Support | Enabled in Limited Support |
    | ------- | ------- | ---- | ------------------ | ----------------- | -------------- | ------- | ------ | ------ | ------ |
    | Map | Show map tiles | Coordinates in and around the map view | To show the map tiles in the map view. | Yes | No | Yes | No | Yes | Yes |
    | Map | Show pins and shapes from coordinates | Pin and shape coordinates | Feature does not require sending coordinate data. | No | No | No | No | Yes | Yes |
    | Map | Show pins and route waypoints | Pins and route waypoint addresses | To translate addresses to latitude/longitude coordinates, and show them on the map. | No | Yes | Yes | No | Yes | No |
    | Map | Show routes | Route waypoint coordinates | To calculate routes between waypoints. | Yes | No | Yes | No | Yes | No |
    | Address Input | Address Search | Address search query string | To show address search results. | No | Yes | Yes | No | Yes | No |
    | Address Input | Address Search | Current device location | To bias address search results around the device location. | No | Yes | Yes | No | Yes | No |

### Next steps

Add the controls to your apps:

- Visualize and interpret location data with the **[Interactive map](geospatial-component-map.md)** control.
- See dynamic address suggestions as you type with the **[Address input](geospatial-component-input-address.md)** control.

### See also

[Create an app that uses the address input and map controls](how-to/mobile-apps-address-map.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
