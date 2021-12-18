---
title: Portals as progressive web apps (PWAs) overview
description: Overview of a building a portal as a progressive web app.
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

# Overview of portals as progressive web apps (preview)
<!--note from editor: Renee pointed out that the original title implied that progressive web apps themselves were our preview feature, so I've changed it here and throughout to say that "portals as progressive web apps" is the feature.-->
> [!Important]
> - This is a preview feature.
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

You can enable your functional portal as a progressive web app (PWA), with native app–like<!--note from editor: Note the en dash here and in line 28.--> look and feel, by using Power Apps portals Studio.

With this preview feature, Power Apps portals now supports using progressive web app technology to provide multiplatform support to create an app that will work on all platforms (Android, iOS, Windows, and Chromebooks) and form factors (mobile, desktop, and tablet).<!--note from editor: Writing Style Guide doesn't like slashes used for "and". Just as a side note - WSG doesn't explicitly have "multiplatform" on its list of allowed "multi" words, but it uses the term on one of its pages so that's good enough for me.-->

PWAs are built for cross-platform interoperability through browser support that provides users a native app–like experience. PWAs bring a seamless experience for users across different web browsers. These apps can be installed from the browser or through app stores. This capability enables external and internal customers to use a portal as an app. They can also pin the app directly to the home screen on their mobile device.<!--note from editor: Edit okay? I wasn't sure whether "you" meant the maker or the user here. Also, how is pinning the app to the home screen different from installing it through the browser?-->

PWAs can be used for both online and offline scenarios. As a maker, you can choose to enable specific pages in your portal to be available offline (the content on these pages will be read-only).<!--note from editor: Suggested, to avoid a bit of a noun stack.-->

The following graphics illustrate the users' experience of adding a portal to their home screen by using the browser that installs the portal as a PWA.<!--note from editor: A reader with low vision wouldn't understand this experience just by reading the alt text. Can you make this a "complex" type image and flesh out a long description? Perhaps something like "A sequence of images, the first of which shows a portal open on a mobile device, the next shows the menu command Add to Home screen. The user is then prompted to install the app, and the last image shows the app with its custom background and branding, looking for all the world like a native mobile app." (Obviously it should be better than what I have here.)-->

:::image type="content" source="media/progressive-web-apps/portal-to-pwa.png" alt-text="Portal configured as a progressive web app." border="false":::

Users can also install the portal from their device's app store, if you created an app package and published the app to the app store for their device.<!--note from editor: Edit suggested.-->

> [!Note]
> Publishing your PWA to the iOS app store is currently not supported.

<!--note from editor: Both of the images on this page use "Rubicon", but I don't see it in the list of approved fictitious names on CELAweb. Is it the name of a sample app from sample data? If not, can you use the Contoso example to reshoot the images?-->
:::image type="content" source="media/progressive-web-apps/app-store.png" alt-text="Mobile device app store." border="false":::

## Next step

[Build progressive web apps](build-progressive-web-apps.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]