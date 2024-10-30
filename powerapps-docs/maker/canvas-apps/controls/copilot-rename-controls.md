---
title: Rename controls with Copilot (preview)
description: Rename controls in bulk for canvas apps with AI in Microsoft Power Apps.
author: mamali-ms
ms.topic: conceptual
ms.collection:
  - bap-ai-copilot
  - get started
ms.reviewer: mkaur
ms.date: 11/8/2024
ms.subservice: canvas-maker
ms.author: mamali
search.audienceType:
  - maker
contributors:
  - mduelae
ms.custom:
  - canvas
ai-usage: ai-assisted
---

# Rename controls in canvas apps with Copilot (preview)

[This article is prerelease documentation and is subject to change.]

Most canvas apps contain numerous controls, so it's crucial to name them meaningfully for better maintainability and collaboration. When you turn on the **Proactive control rename** feature, Copilot can help by suggesting and applying relevant names to multiple controls at once, ensuring these names are updated across all references.

Currently, the following controls are supported:

- Labels
- Buttons


To ensure quality results from Copilot, use this feature after setting the Text property of controls. For example, a button with the default Text property value **Button** or an invalid **Text** property value like If() will not be considered for renaming.

If you still don't get the desired results, please send us your feedback.

When manually renaming a control, use standard and relevant names and naming patterns so Copilot can reference them while suggesting renames. Avoid using special characters and spaces. For example, renaming a button to **collectResponse** will provide better renaming suggestions for other buttons than **collect_1**.

## Prerequisites

By default, **Proactive control rename** setting is enabled for new apps.

To use this feauture for existing apps, follow these steps:

1. Open your [canvas app for editing](edit-app.md) in Power Apps Studio. On the command bar, select **Settings** > **Updates**.
1. On the **Preview** tab, find and turn on the **Proactive control rename** setting.
1. On the **New** tab, find and turn on the **New analysis engine** settting.





## Rename controls

When you rename a control such as the **Button** control, Copilot will suggest names for other **Button** controls based on the control properties.

1. Open your [canvas app for editing](edit-app.md) in Power Apps Studio.

1. In the **Tree view**, select a control and then select **More options** (...).

1. Select **Rename** and type a new name for the control and then press Enter.

1. Copilot will appear with suggestions to rename other controls that are the same type.

    :::image type="content" source="media/rename-controls/rename-control-copilot-appears.png" alt-text="Copilot appears with suggestions to rename controls":::

1. Select **View Suggestions** to see Copilot's suggestions.

1. Review the suggested names and unselect any item that you don't want to rename.
:::image type="content" source="media/rename-controls/rename-control-unselect-rename.png" alt-text="Unselect a suggested renaming of a control":::

1. When you done, select **Rename** to apply the changes. <br>If a formula references a control, it will automatically update with the control's new name.

    :::image type="content" source="media/rename-controls/rename-control-copilot-suggestions.png" alt-text="Suggested names from Copilot":::


## Limitations

- Only the **Label** and **Button** controls are suppported.
- When you rename a label manually, Copilot will appear only if there are other labels under the same screen that can be renamed.
- Only controls with valid **Text** property are considered for renaming by Copilot. 
- **Text** property can be a **Text** literal or a formula returning **Text** type.
- Only controls with non-default **Text** property are considered for renaming. For instance, Text property value must not be the default value such as **Button** or **Text**.
