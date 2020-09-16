---
title: Power Apps and Teams integration - Known issues and limitations | Microsoft Docs
description: Provides an overview of known issues and limitations when using Power Apps with Microsoft Teams.
author: tapanm-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/14/2020
ms.author: mabolan
ms.reviewer: tapanm
---
# Known issues and limitations

This article provides details about the known issues and limitations of the Power Apps and Teams integration capabilities when using [**Project Oakdale environments**](/power-platform/admin/about-teams-environment).

## Component library

[Component library](../maker/canvas-apps/component-library.md) isn't supported currently. This support is coming soon.

## Government Community Cloud (GCC)

Project Oakdale currently isn't available in [Power Apps Government Community Cloud (GCC)](/power-platform/admin/powerapps-us-government).

## Localization

Localization of [Power Apps Studio](understand-power-apps-studio.md) isn't supported. Support for additional languages is coming soon.

## Responsive containers

The new responsive containers that make it easier to create responsive canvas apps for teams is coming soon.

## Sharing

You can't share apps or data outside of a team currently. This capability is coming soon as a new **Share with your colleagues** experience.

![Share with your colleagus](media/share-with-colleagues.png "Share with your colleagues")

## Studio

### Studio and Table designer synchronization

Power Apps Studio doesn't reflect the changes to tables after:

1. Renaming tables.
1. Adding relationships within the inline [Table designer](understand-power-apps-studio.md#table-designer).

To see the new changes, refresh Power Apps Studio.

### Controls

The following controls aren't supported:

- [Forms Pro survey (preview)](/forms-pro/embed-survey-powerapps)
- AR controls
- [Video control](../maker/canvas-apps/controls/control-audio-video.md)

### Studio version

It's currently not possible to change your Studio version.

### Image and date in Table designer

You can't create an image and a date in [Table designer](understand-power-apps-studio.md#table-designer). To create an image and a date in Table designer, use the experience with [build hub](create-table.md) to work with tables.

## Theme

Power Apps Studio and apps currently don't support **Dark theme**.
