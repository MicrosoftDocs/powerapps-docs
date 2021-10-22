---
title: Portals as Progressive Web Apps
description: Configure a portal as a Progressive Web App.
author: ankitavish
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/21/2021
ms.subservice: portals
ms.author: avishwakarma
ms.reviewer: ndoelman
contributors:
    - ankitavish
    - tapanm-msft
    - nickdoelman
---

# Overview

Progressive Web Apps (PWA) are built for cross-platform interoperability through browser support that provides users a native app-like experience. PWA brings a seamless experience for users across different <u>web</u> browsers.

With PWA, you can now pin Power Apps portals as an app to the home screen on a mobile device or install it from the app store. This capability enables external and internal customers to use portals as an app for both online and offline scenarios. As a maker, you can choose to enable specific pages in a portal for read-only offline availability.

The following graphics illustrates the end-user experience when adding the portal on a home screen using the browser that installs the portal as a PWA.

:::image type="content" source="media/progressive-web-apps/portal-to-pwa.png" alt-text="Alt text that describes the content of the image." border="false":::

Users can also install the portal from the store if you choose to create an app package and publish the app to the device store.

:::image type="content" source="media/progressive-web-apps/app-store.png" alt-text="Alt text that describes the content of the image." border="false":::

## Prerequisites

- Your portal package version must be [9.2.2103.1 or later](/power-platform/released-versions/portals) to use this feature.

- For browser support, refer to [supported web browsers for Power Apps portals](supported-web-browsers.md).

## Enable your portal as a PWA

To configure your portal as PWA, use Power Apps portals Studio. With this feature, we've added new settings for PWA configuration using the portals Studio. You can enable, disable PWA capability, customize PWA settings, and get started with the process of creating app package for your portal to publish to the respective device store.

1. Sign in to [Power Apps Preview](https://make.preview.powerapps.com/).

1. Select **Apps** from the left-pane.

1. Select your portal from the list of apps.

1. Select **Edit**.

1. In portals Studio, select **Progressive web app**.

    :::image type="content" source="media/progressive-web-apps/portalstudio-pwa.png" alt-text="Alt text that describes the content of the image." border="false":::

1. Select **Enable PWA** to turn on the PWA capability for your portal.

## Customize PWA settings

You can change the PWA app name, starting page, color, and more using the customization option. To customize PWA settings for your portal:

1. In portals Studio, select **Progressive web app**.

1. Select **Customize PWA** under **Customization**.

1. Update following PWA settings for your portal.

| **Setting** | **Description** |
|-------------------------|-------------------------|
| Title | Name of the portal's PWA that will show up on the mobile device and in the app store. |
| Description | Description for the portal's PWA that will show up on the mobile device and in the app store. |
| Starting page of the app | Start page for the portal when opened through PWA. |
| Splashscreen background | Background color for the splash screen when loading PWA. |
| App icon | Icon for the app that will show up on the mobile device and in the app store.</br>**NOTE:** Icon size must be 512x512 pixel. |

## Manage offline behavior

PWA offers support for a graceful navigation experience when the device being used is offline, disconnected from the internet. With the PWA capability for portals, you can choose the pages within portals that will have this read-only offline capability, and a graceful error page for the rest of the portal capability that isn't enabled for offline access.

### Offline pages for portal

To configure offline pages for the portal using PWA:

1. In portals Studio, select **Progressive web app**.

1. Select **Customize PWA**.

1. Select **Manage offline pages** under **Offline behavior**.

1. Select the pages that you want to enable for offline access using PWA.

> [!NOTE]
> Ensure you consider the storage limitations for the end-user devices when configuring offline access for pages using PWA. Storage requirement for PWA access exceeding the available storage on a device will result in the entire portal to be unavailable for offline access using PWA. We recommend that you test the offline access, and only cache the most important pages that must be available offline. Also, offline pages can only show information. Pages that allow form submissions or run queries won't work for offline access.

### Setup offline error page

When the device is offline, the page you configure as the offline error page shows up to the end-users if they try to access pages that aren't enabled for offline access using the previous setting.

To setup the offline error page:

1. In portals Studio, select **Progressive web app**.

1. Under **Customization**, select **Offline message page**.

1. Customize the page like any other portals page.

1. Change page template to suite your business needs.

:::image type="content" source="media/progressive-web-apps/edit-webpage.png" alt-text="Alt text that describes the content of the image." border="false":::

> [!NOTE]
> You can't change the Title, and the Partial URL ("*/default-offline-page*") for offline page. A default offline page will be rendered to end users if the offline page is missing.

### Browse your portal in offline mode

After you've enabled offline pages, you can now use a mobile device in offline mode and browse through different pages enabled for offline access.

To get started with offline browsing:

1. Browse to your portal using a web browser on your mobile device in online mode.

1. Select **Add to Home screen**, or a similar option. For example, on Android device, the option might be **+ Add to**, and then, **App screen**.

:::image type="content" source="media/progressive-web-apps/add-to-home.png" alt-text="Alt text that describes the content of the image." border="false":::

> [!NOTE]
> This action downloads portal pages enabled for offline browsing, and may take a while depending on the network bandwidth, and the selected pages for offline browsing.

1. Enable offline mode in your mobile device.

1. Open your portal from the home screen. You'll see a notification on the top reminding the browsing session being in offline mode, and if you select any pages that aren't enabled for offline browsing, the default error page appears.

## Create and configure app package

You can create an app package for your portal's PWA and publish the package to different app stores such as Microsoft Windows Store and Google Play Android Store

To create app package, select **Create app package** under **App package** in **Progressive web app** in portals Studio.

:::image type="content" source="media/progressive-web-apps/open-pwa-builder.png" alt-text="Alt text that describes the content of the image." border="false":::

You'll be taken to [PWA builder](https://www.pwabuilder.com/) where you can create app package for various app stores.

Package created from pwabuilder contains:

- .apk file to test the app

- .aab file which can be published in app store.

- Step by step document to publish app.

For Android platform, you can also update the android certificate using the option **Update android certificate**.

:::image type="content" source="media/progressive-web-apps/image13.png" alt-text="Alt text that describes the content of the image." border="false":::

Update the title and the SHA-256 certificate fingerprint to update digital asset links file (assetlinks.json) that proves ownership of your PWA.

## Advanced configuration

PWA capability for portals uses the following configuration that can be updated using the Portal Management app.

> [!NOTE]
> We recommend that you use Power Apps portals Studio to work with PWA feature instead of customizations using Portal Management app.

| **Type** | **Name** | **Description** | **Value** |
|-------------------------|-------------------------|-------------------------|-------------------------|
| Site Setting | PWAFeature | Site setting to enable PWA for the portal | { "status": "enable" }<br /></br>{ "status": "disable" } |
| Web file | PWAManifestjson.en-US.json | Manifest file of PWA is stored as this JSON web file. | This web file contains all customization related properties of PWA (such as, app name, splash screen color). |
| Site marker | Default Offline Page | This site marker defines which page to show when end user is offline. By default, it'll be pointed to default offline page. | "Default Offline Page" |


[!INCLUDE[footer-include](../../includes/footer-banner.md)]