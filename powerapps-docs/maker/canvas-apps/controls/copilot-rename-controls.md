---
title: Rename controls with Copilot (preview)
description: Rename controls in bulk for canvas apps with AI in Microsoft Power Apps.
author: mamali-ms
ms.topic: how-to
ms.collection:
  - bap-ai-copilot
  - get started
ms.reviewer: mkaur
ms.date: 11/13/2024
ms.subservice: canvas-maker
ms.author: mamali
search.audienceType:
  - maker
contributors:
  - mduelae
ms.custom:
  - canvas
  - ignite-2024
ai-usage: ai-assisted
---

# Rename controls in canvas apps with Copilot (preview)

[This article is prerelease documentation and is subject to change.]

Canvas apps often contain numerous controls, so it's important to name them meaningfully for better maintenance and collaboration. With the new **Proactive control rename** feature, Copilot assists by suggesting appropriate names for controls. Makers can review the suggestions and apply the changes to multiple controls at once. When a control’s name is updated, the change is reflected across all its references.

Currently, the most frequently renamed and supported controls are:

- Labels
- Buttons

Additional support for more controls will be incorporated based on feedback from preview.

> [!IMPORTANT]
>
> - This is a preview feature.
> - This is available in English only.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

## Prerequisites

Ensure you meet the prerequisites and region availability in [Copilot in Power Apps overview (preview)](../ai-overview.md#availability).

By default, **Proactive control rename** setting is enabled for new apps.

To use this feature for existing apps, follow these steps:

1. Open your [canvas app for editing](../edit-app.md) in Power Apps Studio. On the command bar, select **Settings** > **Updates**.
1. On the **Preview** tab, find and turn on the **Proactive control rename** setting.
1. On the **New** tab, find and turn on the **New analysis engine** setting.


## Rename controls

When you rename a control like the **Button** control, Copilot suggests names for other **Button** controls based on their properties.

1. Open your [canvas app for editing](../edit-app.md) in Power Apps Studio.

1. In the **Tree view**, select a control and then select **More options** (...).

1. Select **Rename** and type a new name for the control and then press Enter.

 > [!NOTE]
 > When you  manually rename a control, Copilot will only appear if there are additional controls on the same screen that can be renamed.

1. Copilot appears with suggestions to rename other controls that are the same type. 

    :::image type="content" source="media/rename-controls/rename-control-copilot-appears.png" alt-text="Copilot appears with suggestions to rename controls":::

1. Select **View Suggestions**.

1. Review the suggested names and unselect any item that you don't want to rename.
:::image type="content" source="media/rename-controls/rename-control-unselect-rename.png" alt-text="Unselect a suggested renaming of a control":::

1. When you're done, select **Rename** to apply the changes. <br>If a formula references a control, the control's name is automatically updated in the formula.

    :::image type="content" source="media/rename-controls/rename-control-copilot-suggestions.png" alt-text="Suggested names from Copilot":::


## Best practices and recommendations

To get the best results from Copilot, use this feature after setting the **Text** property of a control. For example, Copilot won't suggest names for a button with the default Text property value **Button** or an invalid **Text** property value like **If()**.

If you still don't get the desired results, send us your feedback.

When you manually rename a control, use standard and relevant names and naming patterns so Copilot can reference them while suggesting renames. Avoid using special characters and spaces. For example, renaming a **Button** to **collectResponse** provides better renaming suggestions for other buttons compared to using a name like **collect_1**.

## Limitations

- Only the **Label** and **Button** controls are supported.
- When you rename a label manually, Copilot appears only if there are other labels under the same screen that can be renamed.
- Only controls with a valid **Text** property are considered for renaming by Copilot. 
- The **Text** property can be a **Text** literal or a formula returning **Text** type.
- Only controls with nondefault **Text** property are considered for renaming. For instance, **Text** property value must not be the default value such as **Button** or **Text**.

## See also

[FAQ for rename controls in canvas apps with Copilot](../../common/faq-rename-control.md)
