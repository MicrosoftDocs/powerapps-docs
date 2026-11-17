---
title: Dataverse semantic model frequently asked questions
description: Answers to common questions about the Dataverse semantic model for Power Apps makers and Dataverse administrators.
ms.topic: faq
ms.date: 11/17/2026
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: mkaur
reviewer: Mattp123
ai-usage: ai-generated
---

# Dataverse semantic model frequently asked questions

This article answers common questions about the Microsoft Dataverse semantic model that gives AI agents and Copilot experiences a shared, business-aware understanding of your Dataverse data.

## Why don't I see Create model or Configure?

These controls belong to the new semantic model experience. Where the **New semantic model experience** switch is available, it's on by default. If you turned it off, turn it back on from the semantic models page. The preference is remembered for your account in the browser, not for the whole environment.

The experience also depends on the environment's Dataverse and installed solution versions and whether it's enabled for that environment. Turning on Dataverse intelligence alone doesn't establish that the new experience is available.

**Create model** requires Dataverse intelligence to be enabled and initial provisioning to complete successfully without a provisioning status error. The earlier experience uses **Configuration** instead of **Configure**.

See [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md) for the new experience's steps and prerequisites.

## Why can't I turn on a signal for one table or view?

A model-wide signal setting takes precedence over per-table settings. In **Configure**, turn the signal on under **Manage signals**, then turn it on for the included table under **Table signals**. To manage individual views or relationships, the corresponding signal must be enabled at both levels.

An excluded table's signal controls aren't available until you add the table to the model. For a newly added table, save the table selection and wait for generation before reviewing its generated summaries, views, or relationships.

## Does removing a table delete my Dataverse data?

No. **Remove table** changes the pending table selection for the semantic model; it doesn't delete the Dataverse table. Select **Save** to persist the selection. Keep at least one table in the model.

Model configuration isn't a substitute for Dataverse access controls. Continue to manage permissions through Dataverse security roles and table, column, and record access.

## Why are some views from a table not visible in the semantic model?

Only public views with join conditions and sub-grid views are included in the semantic model. These view types are excluded:

- System views. This includes Quick Find, Advanced Find, Associated, and Lookup views.
- Personal views.

If a view you expect to see is missing, it's most likely one of these excluded types.

For more information about how views contribute to the semantic model, see [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md).

## Why does the semantic model show a Regenerating status?

The **Regenerating** status appears when a manual regeneration is triggered or the scheduled 12-hour regeneration cycle is running. **Regenerate** is unavailable while a request or regeneration is in progress. A success message that says regeneration started confirms acceptance of the request, not completion.

Wait for the job to complete. The overview page refreshes and displays the updated timestamp when regeneration finishes.

> [!NOTE]
> If the **Regenerating** status appears stuck for more than 24 hours, turn Dataverse Intelligence off and back on in the Power Platform admin center to force a restart.

## How is the semantic model consumed by agents and Copilot experiences?

The semantic model is automatically consumed by the following experiences:

- Copilot in Power Apps
- Microsoft Copilot with Dataverse
- Sales Agent in Microsoft 365
- Microsoft Copilot Studio agents over Dataverse data

Agents reference the semantic model associated with their app or knowledge source to understand and reason over your Dataverse data.

## Why is the semantic model not appearing for my agent or Copilot experience?

Semantic models are available only when the Copilot experience is consuming Dataverse data with semantic indexing enabled. For Microsoft Copilot experiences specifically, you must enable Microsoft Copilot in model-driven apps in the app settings.
:::image type="content" source="media/semantic-model-faq/copilot-model-driven-app-setting.png" alt-text="Copilot enabled for model-driven app setting":::

For an overview of which experiences automatically use the semantic model, see [Dataverse semantic model overview](semantic-model-overview.md).


## Why can't I delete a glossary entry that was created by the system?

System-defined glossary entries are part of a solution provided by Microsoft and can't be deleted. You can edit them to update the term or definition to better reflect your organization's terminology.

For instructions on editing glossary entries, see [Manage semantic model glossary entries](manage-semantic-model-glossary.md).

## What does Secondary_model mean in the name of a Microsoft 365-enabled semantic model?

`Secondary_model` is a naming convention that indicates the semantic model isn't ALM-compatible. If you see this term in a model name, the model doesn't carry over when you copy or move the environment.

## How long does it take for the semantic model to reflect a newly created or updated view?

The semantic model automatically regenerates every 12 hours. To request an earlier run, save any pending model configuration, and then select **Regenerate**. The updated context isn't available until regeneration completes.

Regeneration time depends on the volume of changes:

| Scenario | Approximate generation time |
|---|---|
| Initial generation | Up to 2 hours |
| Incremental changes | Up to 30 minutes |

For steps to trigger a manual regeneration, see [Regenerate semantic model](regenerate-semantic-model.md).

## Related articles

- [Dataverse semantic model overview](semantic-model-overview.md)
- [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md)
- [Manage semantic model glossary entries](manage-semantic-model-glossary.md)
- [Regenerate semantic model](regenerate-semantic-model.md)
