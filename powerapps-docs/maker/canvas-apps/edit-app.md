---
title: Edit a canvas app | Microsoft Docs
description: Step-by-step instructions for editing canvas apps and session-locking scenarios in Power Apps.
author: emcoope-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 04/30/2020
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Edit a canvas app in Power Apps

Edit any canvas app that you built, that you own, or for which you have **Co-owner** permissions. You can edit an app in Power Apps Studio. If you try to edit an app that's open for editing elsewhere, a message tells you whether you already have it open or another user does.

## Edit an app

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

1. Select **Apps** in the left navigation pane.

    ![List of apps](./media/edit-app/file-apps.png "List of apps")

1. Select an app.

1. Select **Edit** from top menu. You can also use "**...**" (More Commands) for the app and then select **Edit** from the drop-down menu.

    ![Edit an app](./media/edit-app/edit-app.png "Edit an app")

If you don't see the app that you want to edit, verify that you've selected the correct environment.

![Select environment](./media/edit-app/select-environment.png "Select environment")

## Collaborate on an app

Anybody who has **Can edit** permission for an app can edit it, but only one person can edit an app at a time. If you try to edit an app that someone else is already editing, this message appears. You can't proceed until the other person closes the app (or that person's session times out).

![App open by another user](./media/edit-app/applock-otheruser.png "App open by another user")

In addition, this message appears if you open an app for editing and then try to open it on another device or in another browser window. You can override the previous session, but you might lose any changes that you haven't saved.

![App already open for editing by same user](./media/edit-app/applock-selfuser.png "App already open for editing by same user")

## Next Steps

Learn more about how to add a [screen](add-screen-context-variables.md), a [control](add-configure-controls.md) or a [data connection](add-data-connection.md).
