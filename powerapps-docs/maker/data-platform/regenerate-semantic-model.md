---
title: Regenerate semantic model
description: Learn how to save Dataverse semantic model changes, request manual regeneration, and distinguish a regeneration request from a completed update.
ms.topic: how-to
ms.date: 11/17/2026
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: matp
reviewer: Mattp123
ai-usage: ai-generated
---

# Regenerate the semantic model

The Microsoft Dataverse semantic model automatically regenerates every 12 hours. To request an earlier run after changing signal settings or Dataverse metadata, trigger a manual regeneration instead of waiting for the scheduled cycle. Regeneration is asynchronous: requesting a run doesn't make the updated model available immediately.

## Trigger a manual regeneration

Open the model you want to review from the semantic models page in Power Apps. Use the environment and permissions described in [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md#prerequisites).

1. Save pending signal, description, or table-source changes by selecting **Save**. **Regenerate** isn't a save command.
2. Select **Regenerate** in the model's command bar. On a narrow screen, the command can appear in the overflow menu.
3. Wait while **Regenerating...** is displayed. The command is unavailable while a request or regeneration is in progress.
4. After the run completes, review **Last regeneration** and check the generated context on the model's configuration page. The timestamp is shown in local time.

A message that regeneration started successfully confirms that the request was accepted, not that generation has completed. If the request fails, review the error message; don't assume the model has been updated.

> [!NOTE]
>
> - Regeneration runs across all semantic models in the environment.
> - Save changes before selecting **Regenerate**. Unsaved edits aren't included in the request.
> - **Last regeneration** identifies the last successful run; it doesn't confirm that changes made after that run are reflected in the model.

## Regenerate after enabling sample rows

When you turn on **Sample table rows**, a dialog can offer **Save & regenerate**. Select it to save the settings before requesting regeneration. If saving fails, regeneration doesn't start.

**Skip for now** closes the dialog without saving or starting regeneration. Select **Save** separately if you want to keep the changed settings, then regenerate when ready. Sample rows aren't available to agents until the model is regenerated.

## Related articles

- [Overview of Dataverse semantic model](semantic-model-overview.md)
- [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md)
- [Manage semantic model glossary entries](manage-semantic-model-glossary.md)
- [Dataverse semantic model frequently asked questions](semantic-model-faq.md)