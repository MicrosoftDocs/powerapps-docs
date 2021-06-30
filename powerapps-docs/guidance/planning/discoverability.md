---
title: Deploying a Power Apps project - Discoverability | Microsoft Docs
description: Get your app into the hands of your users by making it available for production use. Then, explore various ways to make your app discoverable.
author: taiki-yoshida
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.author: tayoshi
ms.reviewer: kathyos

---

# Making apps discoverable

Congratulations! You made your first app, and it's tested and ready to go!

However, making the first version of your app isn't the end of the Power Apps journey.
You need to get your app into the hands of your users by making it available for production use.

After you launch the app, you'll want to make sure it's working well and meeting your objectives. In the majority of cases, you can expect to get requests for new features or fixes, or you'll need to accommodate a business process that has changed.

In this section, you'll learn how to:

- [Deploy your app](#publishing-and-sharing-the-app) and [help users discover it](#featured-apps).

- Get [feedback and usage information](feedback-telemetry.md) to help refine your app.

## Publishing and sharing the app

As soon as your app is ready to use, you need to publish and share it.

Follow the instructions for your app type.

:::row:::
    :::column:::
        **Model-driven apps**

        -   [Publishing a model-driven
    app](../../maker/model-driven-apps/validate-app.md)

        -   [Sharing a model-driven
    app](../../maker/model-driven-apps/share-model-driven-app.md)


    :::column-end:::
    :::column:::
        **Canvas apps**

        -   [Publishing a canvas
    app](../../maker/canvas-apps/save-publish-app.md)

        -   [Sharing a canvas
    app](../../maker/canvas-apps/share-app.md)

    :::column-end:::
:::row-end:::

After you publish and share the app, it's important to make sure it's
discoverable so that people will start using it. There are several ways
to make apps discoverable, as described in the following sections.

## Featured apps

![Featured apps list](media/featured-apps.png "Featured apps list")

The [Featured Apps](https://powerapps.microsoft.com/blog/powerapps-discoverability-in-the-enterprise/) list
is a good way to showcase your app if it was meant to be used
by the entire company&mdash;for example, for employee search or company news.

For information about how to use PowerShell scripts with Power Apps to set up Featured
Apps, see [PowerShell support for Power Apps](/power-platform/admin/powerapps-powershell#power-apps-cmdlets-for-administrators-preview)

## QR codes

QR codes are the fastest way to get users to install apps on their
mobile devices. An iOS device natively recognizes QR codes when the camera is used. Android users can
hold the Home button while using the camera to recognize QR codes.

Bing has a QR code generator where you can paste in a URL and it
will instantly generate a QR code image for you. Right-click the
QR code image, copy it, and then paste it into your communications as you advertize your app.

![The Bing QR code generator](media/qr-codes.png "The Bing QR code generator")

## Deep linking

Deep linking from one app to another is a great way of letting users know about
apps that are related to their work. Users can launch an app and then move to relevant apps, without having to
exit the first app, return to the player, and search for another app. Deep linking is
faster and makes the experience more immersive.

To deep link, you can use the [Launch and Param functions](../../maker/canvas-apps/functions/function-param.md) in Power Apps.
More information: [Deep Linking in PowerApps](https://powerapps.microsoft.com/blog/powerapps-deep-linking/)

## Microsoft Teams

You can embed your app as one of the tabs inside of Teams.
This is a great way of increasing user satisfaction if this app is to be used in
scenarios that require going back and forth between Teams and the existing
process.

![A screenshot of an app embedded in Teams](media/add-app-as-tab.png "A screenshot of an app embedded in Teams")

More information: [Embed an app in Teams](../../teams/embed-teams-app.md)

## Tie-ins to existing web apps and portals

Embedding links to the apps from existing websites and portals is also a good
way to give your app exposure.

Using the Param() function to pass on information from the websites and portals
can minimize the need for users to fill in data from whichever website or page they've
come from. This function can be used to fill in some data or take actions from it
automatically.

## SharePoint embedding

Apps can also be embedded directly into modern SharePoint pages. Not only
does this aid discovery of the app, but the content and the app can be easily
changed independent of each other.

More information: [Use the Power Apps web part](https://support.microsoft.com/en-us/office/use-the-power-apps-web-part-6285f05e-e441-408a-99d7-aa688195cd1c)<!--note from editor: This link doesn't work if you remove "en-us" (which we usually do). Just FYI.-->

## Microsoft Search in Bing integration

With Microsoft Search in Bing, you can create a bookmark for your enterprise and
embed apps directly in your search results.

An administrator configures the Bing search engine so that when signed-in
employees in certain groups or locales&mdash;or using certain devices&mdash;search for
specific terms, they'll get the app in a pane at the top of their
search results.

> [!div class="nextstepaction"]
> [Next step: Collect feedback and telemetry](feedback-telemetry.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]