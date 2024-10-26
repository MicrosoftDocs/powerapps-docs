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

# Rename controls in canvas apps with Copilot

A typical Canvas Power App includes hundreds of controls. Naming them in a relevant way is important for maintainability and coauthoring.

Copilot can take away the time spent in renaming each control manually, by suggesting and applying relevant control renames for multiple controls at once. The rename also propagates to all other references of the control.

Following controls are currently supported:
- Labels
- Buttons

## Prerequisites

- To enable this Copilot feature for existing apps, enable control rename app setting. Go to Settings, click Updates, Preview, and then turn on Proactive control rename toggle to true. Feature will be enabled by default for new apps. 
- Ensure New Analysis Engine app setting is enabled in your app. Go to Settings, click Updates, New, and then turn on New analysis engine toggle to true.

## Rename controls

1. Rename a control (currently only label or a button) manually in tree View.

![Manually rename a control.](./media/1-rename-manually.png)

2. Copilot nudge will appear near tree view if it has renaming suggestions for other controls of same type under that Screen.

![Copilot shows up](./media/2-copilot-shows-up.png)

3. Clicking on Copilot will open a preview of rename suggestions.

![rename suggestions](./media/3-click-to-see-rename-suggestions.png)

4. Review suggestions and click Rename. Controls will be updated with renames at once. Any formulas referencing the controls will be auto updated with new names.

![apply all renames](./media/4-apply-all-renames.png)

5. Alternatively, you can unselect any rename suggestions if so desired and then click Rename.

![optional unselect](./media/optional-unselect-if-needed.png)

## Limitations

- This feature is currently supported for labels and buttons only.
- When you rename a label manually, Copilot will appear only if there are other labels under the same Screen that can be renamed.
- Only controls with valid Text property will be considered for rename. Text property can be a Text literal or a formula returning Text type.
- Only controls with non-default Text property will be considered for rename. For instance, Text property value must not be the default value like "Button" or "Text".

## Best Practices
To get the most out of this feature:

- Use this feature after Text property of controls has been set to ensure quality results from Copilot. For example, a button with default Text property value "Button" or invalid Text property value If() will not be considered for rename. And if you still can't get the desired results, send us your feedback.
- Use standard and relevant name and naming pattern when manually renaming a control so Copilot can reference it while suggesting renames. Avoid use of special characters and space. For example, renaming a button to "collectResponse" will provide better renaming suggestions for other buttons than "collect_1"
