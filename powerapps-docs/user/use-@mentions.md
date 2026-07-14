---
title: Use @mention to collaborate with your team using Notes
description: Learn how to use @mention to collaborate with your team using Notes.
author: shwetamurkute
ms.component: pa-user
ms.topic: overview
ms.date: 03/20/2025
ms.subservice: end-user
ms.author: smurkute
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
ms.contributors:
- srihas
---

# Use @mention to collaborate with your team using Notes

Collaborate effortlessly by mentioning your coworkers in Notes on the timeline.

The administrator must enable the [**@mention people when in rich text editor to add and notify user settings**](/power-platform/admin/settings-collaboration#end-user-experiences) in Power Platform admin center and [enable in-app notifications](../developer/model-driven-apps/clientapi/send-in-app-notifications.md?tabs=clientapi#enable-the-in-app-notification-feature) for the app for this capability to be available. 

> [!Important]
> Users must have the Read privilege for the **msdyn_postconfig** entity, as well as the Share privilege for the entity for which they use @mentions (for example, account, contact, case, and so forth).

## @mention a user in Notes

1. Open a row and go to the activity timeline on the page.
1. Add a note by selecting _Enter a note_.
1. In the **Description** field, enter **@** and the first few letters of the person’s first name to see a list of options.
1. Select the name you want.

   If the user doesn't already have permission to view the row and you have the Share privilege for the row, you're asked to provide basic read permission for the row you're adding a note on.

## Notifications

1. The notification bell icon indicates a new notification when you're @mentioned in a note.
1. Open the notification center and select the notification to navigate to the record on which you were mentioned.
