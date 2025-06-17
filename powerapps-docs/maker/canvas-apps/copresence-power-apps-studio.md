---
title: Collaborate on canvas apps in Microsoft Power Apps Studio
description: Learn how to use copresence and coauthoring to view who's working on the same canvas app as you and edit it together in real time.
author: mkaur
ms.author: szlo
ms.date: 6/16/2025
ms.topic: how-to
ms.reviewer: mkaur
ms.subservice: canvas-maker
search.audienceType: 
  - maker
contributors:
  - mduelae
  - -szlo
ai-usage: ai-assisted
ms.custom:
  - ai-gen-diyeditor
  - canvas
---

# Collaborate on canvas apps in Power Apps Studio

Collaborate on canvas apps in Power Apps Studio using copresence and coauthoring. These features let you work with other makers in real time, improving productivity and teamwork.

- **Copresence** shows who else is working on the same app, but only one person can edit the app at a time. The first person who opens the app gets editing control

- **Coauthoring** lets multiple people edit the app at the same time and see each other's changes in real time.

## Use copresence to see who's working on the same app

When you open an app for editing in Power Apps Studio, indicators might show that other people are also working on the app. These indicators are part of the copresence feature.

The first person who opens the app gets editing control. If another person opens the app, a notification lets them know that someone else is editing the app, and they're viewing it in read-only mode. In read-only mode, you can't add new screens, edit control properties, or use the command bar. You can save a copy of the app.

The command bar shows the names and icons of other makers who are editing or viewing the app. The left navigation pane shows the app's structure and highlights which part of the app someone else is editing. You also get a notification to refresh the app when someone saves changes to the app.

:::image type="content" source="media/copresence/canvas-copresence.png" alt-text="Screenshot of copresence indicators in Power Apps Studio with annotations." lightbox="media/copresence/canvas-copresence.png":::

**Legend**:

1. The command bar shows the names and icons of other makers who are editing or viewing the app.
1. A **Read-only** warning appears if someone already has editing control elsewhere. You can select **Override** to become the main author and regain editing rights.
1. In **Tree view**, you see the app's structure and other people's profile pictures on the part of the app someone else is editing.

> [!TIP]
> If you're inactive for two hours while editing an app, Power Apps asks if you want to keep editing or switch to read-only mode. If you don't respond, the system puts you in read-only mode so other makers can become the editor.
>
> If autosave is on, your changes are automatically saved. If autosave isn't on, Power Apps notifies you that you're no longer editing and lets you save a copy of your changes.

## Use coauthoring to edit the same app together

Coauthoring lets multiple makers edit a canvas app at the same time. When you use coauthoring, you can tell where other makers are working on the app and view their changes in real time.

:::image type="content" source="media/copresence/coauthoring.png" alt-text="Screenshot of coauthoring indicators in Power Apps Studio with annotations." lightbox="media/copresence/coauthoring.png" :::

When multiple editors work on the app, their avatars show.

- The left navigation pane shows the app's structure in **Tree view** and shows which part of the app someone else is editing. For example, you might edit **Screen 1**, while someone else edits **Screen 2**.
- The area that another maker edits is highlighted and shows their initials. For example, someone else might edit a part of a form, which is highlighted for the first user.


> [!IMPORTANT]
> Multiple makers can select and edit a control at the same time. Be careful not to overwrite each other's changes.

### Turn on coauthoring

To use coauthoring, you need to turn it on for each app. When you turn on coauthoring, it overrides the copresence feature.

1. [Open your app for editing](edit-app.md) in Power Apps Studio.
1. Go to **Settings** > **Updates** > **New**.
1. In the searh box, type **coauthor**.
1. Turn on the **Coauthoring** toggle.

   :::image type="content" source="media/copresence/coauthor-settings.png" alt-text="Screenshot of coauthoring settings":::

### Limitations of coauthoring

- When more than one maker edits an app, the following actions aren't available:

  - Search
  - Save as
  - Open another or new app
  - Undo and redo
  - Switch authoring versions

- The maximum number of coauthors is 10, either in one session or across a total of 10 tabs, depending on which limit is reached first. Any other coauthors or tabs beyond 10 are in [copresence](copresence-power-apps-studio/md#use-copresence-to-see-whos-working-on-the-same-app) and can't edit the app or view real-time updates.

- The app language is locked to the locale of the first maker who opens the app for editing. Opening the same app in a different locale can lead to errors in formulas.

- Cut isn't available.

- Coauthoring is turned off in the [Monitor tool](../monitor-overview.md).

- You can encounter a problem with the following actions:

  - Renaming a control
  - Adding AI Builder components
  - Adding geospatial controls
  - Running a flow that another coauthor added, without refreshing the app first
  - Viewing errors from one author's actions on all other coauthors' screens
  - Copying and pasting
