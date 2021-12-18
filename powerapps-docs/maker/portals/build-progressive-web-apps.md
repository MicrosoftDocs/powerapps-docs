---
title: Build progressive web apps
description: Configure a portal as a progressive web app.
author: ankitavish
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/30/2021
ms.subservice: portals
ms.author: avishwakarma
ms.reviewer: ndoelman
contributors:
    - ankitavish
    - tapanm-msft
    - nickdoelman
---

# Build a portal as a progressive web app (preview)
<!--note from editor: H1 edit is suggested, to differentiate it from the Edge article.-->
> [!Important]
> - This is a preview feature.
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

## Prerequisites

- Your portal package version must be [9.2.2103.1 or later](/power-platform/released-versions/portals) to use this feature.

- For browser support, refer to [supported web browsers for Power Apps portals](supported-web-browsers.md).

## Enable your portal as a progressive web app

Use Power Apps portals Studio to configure your progressive web app (PWA). You can enable or disable PWA capability, customize PWA settings, and prepare to create an app package to publish to respective device stores if you choose.

1. Sign in to [Power Apps Preview](https://make.preview.powerapps.com/).

1. On the left pane, select **Apps**.

1. From the list of apps, select your portal.

1. Select **Edit**.

1. In portals Studio, select **Progressive web app**.

    :::image type="content" source="media/progressive-web-apps/portalstudio-pwa.png" alt-text="Progressive web app icon in portals Studio." border="false":::

1. Select **Enable PWA**.

    :::image type="content" source="media/progressive-web-apps/enable-pwa.png" alt-text="Enable PWA capability from portals Studio." :::

## Brand your app

You can create your own branded PWA by using the customization options to change the app name, starting page, color, and more.<!--note from editor: Suggested.-->

> [!Note]
> On iOS devices, icons for the PWA will be shown as thumbnails and the customized splash screen won't be displayed.
<!--note from editor: The "To <do this thing>" procedure headings are only needed if you have multiple procedures within a section or you're combining conceptual and procedural information within the section. You've already dedicated separate H2s and H3s to each procedure, so you don't need those "To..." headings.-->
1. In portals Studio, select **Progressive web app**.

1. Under **Customization**, select **Customize PWA**.

1. Update the following PWA settings for your portal.
    
    | **Setting** | **Description** |
    |-------------------------|-------------------------|
    | Title | The name of the portal PWA<!--note from editor: WSG doesn't like the possessive for Microsoft product, service, or feature names. I interpret that to apply here.--> that will appear on the mobile device and in the app store. |
    | Description | The description of the portal PWA that will appear on the mobile device and in the app store. |
    | Starting page of the app | The start page for the portal when it's opened through the PWA. |
    | Splash screen background | The background color for the splash screen when the PWA is loaded. |
    | App icon | The icon for the app that will appear on the mobile device and in the app store.<br>**Note:** The icon size must be 512 &times; 512 pixels.<!--note from editor: If it has to be PNG format, maybe mention it here?--> |
    
    :::image type="content" source="media/progressive-web-apps/customize-pwa.png" alt-text="Customizing PWA settings such as title, description, and color." :::
    
    > [!NOTE]
    > After customizing the PWA, select **Browse website** to clear the cache. This will cause changes to be reflected instantly.

## Manage offline behavior

PWA offers support for a smooth navigation experience when the device being used is offline or disconnected from the internet. You can choose the pages within your portal that will be available offline (read-only), and a message page for the rest of the portal capabilities that haven't been enabled for offline access.<!--note from editor: Edits suggested.-->

### Configure offline pages for the portal PWA

1. In portals Studio, select **Progressive web app**.

1. Select **Customize PWA**.

1. Under **Offline behavior**, select **Manage offline pages**.

    :::image type="content" source="media/progressive-web-apps/offline-behavior.png" alt-text="Selecting pages for offline mode." :::

1. Select the pages that you want to enable users to access when they use the PWA offline.<!--note from editor: Suggested. -->

    :::image type="content" source="media/progressive-web-apps/manage-offline.png" alt-text="Managing offline pages." :::

> [!NOTE]
> When configuring offline access for PWA pages, be sure to<!--note from editor: Edit suggested. If you don't like, it should be "Ensure that you consider..."--> consider the storage limitations for user devices. When the storage requirement for offline PWA access exceeds the available storage on the device, the entire portal will be unavailable for offline access. We recommend that you test the user experience of offline access and only cache the pages that will be most helpful and important to your users. Remember that offline pages can only show information; pages that contain forms to fill out or run queries won't work while offline.<!--note from editor: Edits suggested.  -->

### Set up an offline message page

When a device is offline, the page you configure as the offline message page appears when users try to access pages that haven't been enabled for offline access.<!--note from editor: Edits suggested. I don't know what "using the previous setting" meant here. -->

1. In portals Studio, select **Progressive web app**.

1. Under **Customization**, select **Offline message page**.

    :::image type="content" source="media/progressive-web-apps/offline-message.png" alt-text="Configuring the offline message page." :::

1. Customize the page as you would any other portals page.

1. Change the page template to suit your business needs.

    :::image type="content" source="media/progressive-web-apps/edit-webpage.png" alt-text="Customizing the offline message page in portals Studio." border="false" :::

> [!NOTE]
> You can't change the **Title** or **Partial URL** ("*/default-offline-page*") fields for the offline page. A default offline page will be shown to users if the offline page is missing.

> [!TIP]
> After configuring the offline PWA experience, select **Browse website** to clear the cache. This will cause changes to be reflected instantly.<!--note from editor: Suggest pulling this out of the note to make it stand alone a bit better.-->

### Test your portal in offline mode<!--note from editor: Edit suggested. If this section actually is related to the guidance in the note on line 95, maybe we can add a link to this section in that note?-->

After you've enabled offline pages, you can now use a mobile device in offline mode and browse through different pages that have been enabled for offline access.

1. Browse to your portal by using a web browser on your mobile device in online mode.

1. Select **Add to Home screen** or a similar option. For example, on an Android device, the option might be **+ Add to** > **App screen**.

    :::image type="content" source="media/progressive-web-apps/add-to-home.png" alt-text="Adding the PWA to the home page on a mobile device." border="false":::

    > [!NOTE]
    > This action downloads portal pages that have been enabled for offline browsing. This might take a while, depending on network bandwidth and the size of the pages that were selected for offline browsing.<!--note from editor: Edit okay? Note that WSG prefers "might" over "may" in a case like this.-->

1. Enable offline mode in your mobile device.

1. Open your portal from the home screen. You'll see a notification at the top reminding you that you're browsing in offline mode. If you select any pages that haven't been enabled for offline browsing, the offline message appears.<!--note from editor: Edit okay? I assume it won't necessarily be the default offline message, if you've customized your own in the previous section.-->

    :::image type="content" source="media/progressive-web-apps/pwa-offline.png" alt-text="Read-only page in offline mode for a PWA app.":::   :::image type="content" source="media/progressive-web-apps/not-connected.png" alt-text="Not connected to the internet page in PWA app." :::

## Distribute your app

### Distribute your app by using a browser

After<!--note from editor: Via WSG.--> your portal is enabled as a PWA, your users can pin Power Apps portals as an app to the home screen on their device. This is supported on all platforms (Android, iOS, and Windows<!--note from editor: Should this include Chromebook, to be parallel with the list in progressive-web-apps.md?-->) in addition to all form factors (mobile, desktop, and tablet).

### Distribute your app through an app store

You can create an app package for your portal PWA and publish the package to different app stores such as Microsoft Store and Google Play.<!--note from editor: Would it be helpful to move the note about "Publishing your PWA to the iOS app store is currently not supported" here from progressive-web-apps.md?-->

To create an app package, go to portals Studio. Under **App package**, select **Create app package**.

:::image type="content" source="media/progressive-web-apps/open-pwa-builder.png" alt-text="Opening PWA Builder to create an app package in portals Studio." border="false":::

You'll be taken to [the PWA Builder website](https://www.pwabuilder.com/) where you can create an app package for various app stores. The package you create by using PWA Builder contains:

- An app package for the PWA to be used in its respective app store.

- A step-by-step document about publishing the app.<!--note from editor: I assume this is a document for the user? Otherwise it doesn't belong in this list. I'm not sure the list makes much sense anyway.I confess, it confuses me mightily. -->

For more details, go to the [PWA resource hub](https://blog.pwabuilder.com/).

#### Additional considerations for Android<!--note from editor: I realize this new heading is now an orphaned H4, but I think something needs to separate this section from the previous content. Obviously it's tracking with the UI; it would be nice to have a bit more info in here to put this in context. -->

For the Android platform, you can also update the Android certificate with the **Update android certificate** option.

:::image type="content" source="media/progressive-web-apps/update-android.png" alt-text="Menu item in portals Studio to update the Android certificate." border="false":::

Update the title and the SHA-256 certificate fingerprint to update the digital asset links file (assetlinks.json) that proves ownership of your PWA.

:::image type="content" source="media/progressive-web-apps/android-certificate.png" alt-text="Updating the Android certificate details.":::

## Advanced configuration

The PWA capability for portals uses the following configurations that you can update by using the Portal Management app.

> [!NOTE]
> We recommend that you use Power Apps portals Studio to work with PWA features instead of customizing them by using Portal Management.<!--note from editor: Is this what this note is saying? Not sure why this section is even included.-->

| **Type** | **Name** | **Description** | **Value**<!--note from editor: Are the quotation marks in this column literal? If not, maybe bold or monospace would be a better way to indicate the literal strings.--> |
|-------------------------|-------------------------|-------------------------|-------------------------|
| Site Setting | PWAFeature | Site setting to enable PWA for the portal | { "status": "enable" }<br /></br>{ "status": "disable" } |
| Web file | PWAManifestjson.en-US.json | The PWA manifest file is stored as this JSON web file. | This web file contains all customization-related properties of the PWA (such as app name and splash screen color). |
| Site marker | Default Offline Page | This site marker defines which page to show when the user is offline. By default, it points to the default offline page. | "Default Offline Page" |

### See also

[Overview of portals as progressive web apps](progressive-web-apps.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]