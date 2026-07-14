---
title: Stream control in Power Apps
description: Learn about the details, properties, and examples of the new stream control in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
ms.date: 5/21/2025
ms.subservice: canvas-maker
ms.author: yogupt


ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - yogeshgupta698
  
---
# Stream control (based on SharePoint) in Power Apps (preview)

[This article is pre-release document and is subject to change.]

The Stream control in Power Apps lets you embed Microsoft [Stream (on SharePoint)](/stream/streamnew/new-stream) videos directly in your canvas app. Adding a Stream video in your app makes a smooth integration of videos hosted on Microsoft Stream in your canvas app. It also improves the user experience.

## Prerequisites

To add a Stream video in your canvas app, follow these steps to get the embed URL of the video:

1. Open your [Stream (on SharePoint)](/stream/streamnew/new-stream) video.
1. Select **Share** > **Embed code**.
:::image type="content" source="media/embed-URL-image.png" alt-text="Microsoft Stream embed URL":::

1. Copy the URL starting from **https://** to the **UniqueId=** including the Unique ID numbers.
:::image type="content" source="media/sample-embed-code.png" alt-text="embed URL example":::

> [!IMPORTANT] 
> The Microsoft Stream control in Power Apps only supports URLs that follow the *.sharepoint.com pattern. If your SharePoint domain doesn't follow this pattern, the Stream control will show an invalid URL error.

## Add Stream control 

1. Open your app canvas app for [editing](../../edit-app.md).
1. On the [command bar](../../power-apps-studio.md#1--power-apps-studio-modern-command-bar), select **Insert** > **Media** > **Stream (preview)**.
1. In the **STREAM** pane, enter the **Stream URL** of the video. This is the embed URL from the [Prerequisites](new-stream-video-control.md#prerequisites) section of the article.
1. Customize the size of the embedded video player by setting the width and height properties of the control.


## Properties

**Stream URL (Required)** - The URL of the Stream video that you want to embed. This is the embed URL of the video. The URL should only have Unique ID. If URL detects other parameters, the control detects as invalid URL.
 
**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Mobile support for stream control
Stream control is now also supported on mobile. To comply with Apple's privacy policies, iOS users must follow these steps to enable cross-site tracking on Power Apps:

1. On iOS, select **Settings** > go to **Power Apps**.
1. Set the toggle for **Allow Cross-Website Tracking** to **On**.

## Limitations

1. Control properties such as auto start, auto play, and start from are coming soon.
1. Don't add more than four videos on a single canvas app screen because it can cause performance issues.
3. The last played state isn't preserved for a video that's in a gallery.
