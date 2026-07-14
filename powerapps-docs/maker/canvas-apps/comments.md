---
title: Add comments when you're building a canvas app
description: Learn how to add comments while you’re building a canvas app in Power Apps Studio.
author: mkaur
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 03/01/2023
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Add comments when you're building a canvas app

Easily add comments when you’re building a canvas app in [Power Apps Studio](power-apps-studio.md). Use comments to help your team review the app and provide feedback, or provide additional information on implementation details in your app. To allow other makers to add comments, make sure to share the app with them.

You can add comments to different components or pages.

:::image type="content" source="media/comments/comments-canvas-apps.png" alt-text="Screenshot showing where you can add comments in Power Apps." lightbox="media/comments/comments-canvas-apps.png":::

Legend

1. **Tree view**: Select a screen from the tree view and right-click to add a **New comment**.
2. **Component**: In the canvas area, right-click on a component to add a **New comment**.
3. **App actions**: Select **Comments** > **New** and then add your comments.

## Use @mention in comments to tag someone for feedback

Connect with other makers in your organization as you collaborate on creating your app. You can tag people in the comments by using **@**+ their name.

If you tag a maker that doesn’t have access to your app, then you're prompted to share the app with them.

:::image type="content" source="media/comments/comments-access.png" alt-text="Screenshot showing the maker who doesn't have access.":::

When someone tags you in a comment, you receive an email that lets you know which app you're tagged in and the person who tagged you. It also includes the comment text and a direct link to that comment.

:::image type="content" source="media/comments/comments-email.png" alt-text="Screenshot showing an example email when you're tagged in a comment.":::

## Edit or delete a comment

You can edit your comments or remove existing comments from appearing in the app.

In the **Comments** pane, next to a comment, select **...**, and then select **Edit comment** or **Delete comment**.

## Resolve a comment

Comments are commonly questions, feedback, or ideas that are important context to live alongside your app. But they might not be active discussions anymore. You can resolve a comment or reopen a resolved comment thread to better track the active comments.  

1. In the **Comments** pane, next to a comment, select **...**, and then select **Resolve comment**.
1. The comment thread appears as **Resolved**.
1. Select one to remove the comment:

   :::image type="icon" source="media/comments/reopen-thread-button.png"::: **Reopen a thread**.

   :::image type="icon" source="media/comments/delete-thread-button.png"::: **Delete a thread**.

## Limitations

1. The numbers of users who can access an app in edit mode is limited. If you have an app open and tag someone, the user receives an email notification. The user must wait for you to exit the app in order to see the comment and resolve it.
2. Comments aren't supported when you're working on an app using Git.
3. @mention isn't supported for SharePoint custom Power Apps. Learn more  in [Customize a form for a SharePoint list](/sharepoint/dev/business-apps/power-apps/get-started/create-your-first-custom-form).
