---
title: Media control in cards for Power Apps
description: Learn about the properties and examples of the media control for cards in Power Apps.
author: anuitz
ms.topic: reference
ms.custom: 
ms.reviewer: mkaur
ms.date: 03/01/2023
ms.author: anuitz
search.audienceType:
  - maker
contributors:
  - mduelae
  - anuitz
---

# Media control in cards

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

Displays a media player for audio or video content. A video or audio file is specified by its Url and MimeType in the Sources tab. The media control supports publicly accessible and CORS-compliant URLs. On Web and Desktop versions of Teams, share links to any OneDrive or SharePoint backed video or audio link are also supported.

Use the [image control](image.md) for pictures.

## Properties

**[Sources](control-reference.md#s)** - The media content to play. Plays the first one specified by default.

**[Poster](control-reference.md#p)** – URL of an image to display before playing. Supports data URI in version 1.2+

**[Alt text](control-reference.md#a)** – Alternate text describing the audio or video.

**[Initially visible](control-reference.md#i)** – If false, this item will be removed from the visual tree.

**[Spacing](control-reference.md#s)** – Controls the amount of spacing between this control and the preceding control.

**[Divider](control-reference.md#d)** – When true, draw a separating line at the top of the control.

**[Height](control-reference.md#h)** – Specifies the height of the control.

**[Repeat for every](control-reference.md#r)** – The source of data that is used to show multiple instances of this control. Learn how to use [repeat for every](control-reference.md#r).

**[Show when](control-reference.md#s)** – Conditional layout expression.
