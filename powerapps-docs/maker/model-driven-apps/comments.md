---
title: Add comments in model-driven apps with Power Apps
description: Comments help app makers collaborate better when working together. 
author: Mattp123
ms.author: "emcoope"
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: how-to
ms.date: 03/28/2023
ms.custom: template-how-to
---
# Add comments in the model-driven app designer

Comments are notes that are associated with items in your app. Use comments to help your team review the app and provide feedback, or provide additional information on implementation details in your app.  

In the app designer, the anchors, which are what comments attach to, are all of the pages in the pages pane, and any of the items in the **Navigation** pane. This lets you add comments to items such as areas, groups, pages, tables, and dashboards. Comments are stored in a table in Microsoft Dataverse in the default solution.

## Add a comment to a page

1. Open a model-driven app for edit using the app designer.
1. Select an item in the **Pages** pane.
1. Select **Comments** on the command bar. This opens the comments pane for the selected component. You can also open the comments pane by selecting the comment count indicator for existing comments to an item in the left pane.
   :::image type="content" source="media/comments-feature2.png" alt-text="Comments feature in app designer":::
1. Select **New** to create a new comment and type the comment message in the box. Or, type into the **Reply** box to respond to an existing comment. Select <img src = "media/post-comment-button.png" alt = "Post your comment button" width = "25" height = "25"> **Post reply** or press Ctrl + Enter to post your comment.

## Edit or delete a comment

You can edit your comments or remove existing comments from appearing in the app.

In the **Comments** pane, next to a comment, select **...**, and then select **Edit comment** or **Delete comment**.

## Resolve a comment

Comments are commonly questions, feedback, or ideas that are important context to live alongside your app. But, they may not be active discussions anymore. You can resolve, or reopen a resolved, comment thread to better track the active comments.  

1. In the **Comments** pane, next to a comment, select **...**, and then select **Resolve comment**.
1. The comment thread appears as **Resolved**.
1. To reopen select <img src = "media/reopen-thread-button.png" alt = "reopen comment thread button" width = "20" height = "20"> **Reopen thread** or <img src = "media/delete-thread-button.png" alt = "Delete comment thread button" width = "20" height = "20"> **Delete thread** to remove the comment.

## Moving comments between environments

Comments in model-driven apps can't be exported or imported as solution components because they contain user collaboration data. You can, however export the **Comment** table to Excel and then import the Excel file into the environment you want. More information: [Export data](../data-platform/data-platform-import-export.md#export-data)

## Next steps

[Discover who's working on an app](copresence.md) <br />
[Coauthoring in model-driven apps (preview)](coauthoring.md)