---
title: Regenerate semantic model (preview)
description: Keep your Dataverse semantic model current by understanding automatic regeneration cycles and triggering manual regeneration after schema changes or ALM actions.
ms.topic: how-to
ms.date: 06/17/2026
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: mkaur
reviewer: Mattp123
---

# Regenerate the semantic model (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

The Microsoft Dataverse semantic model automatically regenerates every 12 hours. If you want changes to take effect immediately - such as updates to signal settings, or Dataverse metadata changes like adding or updating views and column descriptions - trigger a manual regeneration instead of waiting for the next scheduled run.

[!INCLUDE [cc-preview-features-definition](../../../shared/preview-includes/preview-note-pp.md)]

## Trigger a manual regeneration

From the semantic model overview, select **Regenerate**. The button grays out while the regeneration job is queued and running. 

After regeneration completes, the overview page refreshes and shows the updated timestamp next to the Regenerate button.

> [!NOTE]
>
> - Regeneration runs across all semantic models in the environment.
> - Only changes made before selecting Regenerate are captured in that run. Any changes made after are picked up in the next cycle. Use the Last regeneration timestamp to confirm which changes are reflected in the current model.

## Related articles

- [Overview of Dataverse semantic model (preview)](semantic-model-overview.md)
- [Fine-tune semantic model signals (preview)](fine-tune-semantic-model-signals.md)
- [Manage semantic model glossary entries (preview)](manage-semantic-model-glossary.md)
- [Dataverse semantic model frequently asked questions (preview)](semantic-model-faq.md)