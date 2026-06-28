---
title: Overview of Dataverse semantic model (preview)
description: Learn what the Dataverse semantic model is, how its building blocks work together, and which Copilot and agent experiences it powers — for Power Apps makers and Dataverse administrators.
ms.topic: overview
ms.date: 06/17/2026
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: mkaur
reviewer: Mattp123
---

# Overview of Dataverse semantic model (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

The Dataverse semantic model gives AI agents and Copilot experiences a shared, business-aware understanding of your Dataverse data. Rather than reasoning from raw column and table names alone, agents that consume the semantic model understand what your data *means*.

The semantic model is automatically provisioned when Copilot experiences over Dataverse data are enabled, so there is no manual setup required to start. Makers and administrators can then fine-tune which signals feed into the model and add domain-specific glossary terms to cover business-specific language that automatic extraction can't infer.

[!INCLUDE [cc-preview-features-definition](../../../shared/preview-includes/preview-note-pp.md)]

## Building blocks of the semantic model

The semantic model combines three building blocks to give agents a complete picture of your Dataverse data: data scope with semantic indexing, system-inferred signals, and a human-curated glossary. Together, they allow agents to understand not just what your data contains, but what it means.

### Data scope with semantic indexing

The data scope defines the set of Dataverse tables covered by the semantic model. Semantic indexing is applied over those tables, forming the foundation for agent reasoning within a particular scenario. Only tables included in the data scope contribute to an agent's understanding of your data.

### System-inferred signals

The semantic model automatically extracts signals from metadata that already exists in your Dataverse environment - table relationships, views, forms, column description summaries, and optionally sample data rows. No additional data entry is required. The model reads what you already configured and uses it to build semantic understanding.

You can fine-tune which signals are included and exclude those that introduce noise or are no longer relevant. For details, see [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md).

### Glossary

The glossary allows makers to add domain-specific terms, acronyms, synonyms, and definitions that system signals can't infer. If your organization uses coined abbreviations or business-specific terminology that agents misinterpret, glossary entries close those gaps directly. For details, see [Manage semantic model glossary entries](manage-semantic-model-glossary.md).

## Why use the semantic model

The semantic model improves agent behavior in four ways:

- *Improved accuracy* — Agents interpret business intent rather than guessing from schema names alone, delivering more meaningful and relevant results.
- *Faster responses* — A well-scoped semantic model reduces ambiguity, so agents return answers more quickly and fluently.
- *Reduced setup time* — The model automatically extracts semantic knowledge from your existing Dataverse environment. As your schema evolves, the model updates on a scheduled basis.
- *Consistent answers across agents* — When multiple agents reference the same semantic model, they share the same understanding of your data and return consistent responses across experiences.

## How the semantic model works

Once [Dataverse intelligence](./data-platform-intelligence.md) is enabled, the semantic model is provisioned automatically. It reads metadata from your Dataverse environment and extracts the following signals:

| Signal | What is captured |
|---|---|
| Table relationships | How records across tables are associated, such as one-to-many and many-to-many relationships. |
| Views | Public views with join conditions and sub-grid views that define which records and columns are relevant for a scenario. |
| Forms | The display name of forms that define how records are presented to users. |
| Description summaries | Descriptions added to tables and columns that explain what they represent. |
| Sample data rows | Representative rows showing what data looks like in each column. |

> [!NOTE]
> Sample data rows are turned off by default. System views - including Quick Find, Advanced Find, Associated, and Lookup views - and personal views are excluded from signal extraction. For forms, only the display name is captured. Polymorphic relationship type isn't supported to configure.

The semantic model regenerates automatically every 12 hours to reflect schema changes. You can also trigger a manual regeneration at any time. Initial generation can take up to two hours, and incremental changes typically take up to 30 minutes. For details, see [Regenerate the semantic model](regenerate-semantic-model.md).

## Copilot experiences that use the semantic model

The semantic model is automatically provisioned and consumed by the following Copilot and agent experiences when they are set up over Dataverse data:

- *Copilot in Power Apps* — Available in model-driven apps. For setup information, see [Add Microsoft 365 Copilot for app users in model-driven apps](../model-driven-apps/add-microsoft-365-copilot.md).
- *Microsoft 365 Copilot with Dataverse* — Connects Microsoft 365 Copilot to your Dataverse data. For setup information, see [Dataverse data in Microsoft 365 Copilot](./data-platform-data-copilot.md).
- *Sales Agent in Microsoft 365* — Uses Dataverse data to power sales scenarios. For setup information, see [Set up Sales agent in Microsoft 365 Copilot](/microsoft-sales-copilot/set-up-sales-chat).
- *Microsoft Copilot Studio agents over Dataverse data* — Agents built in Copilot Studio that use Dataverse tables as a knowledge source. For setup information, see [Add Dataverse tables as a knowledge source](/microsoft-copilot-studio/knowledge-add-dataverse).

## Known limitations

The following limitations currently apply:

- No new model creation. You can't currently create a completely new semantic model.
- No ALM support. The semantic model currently doesn't support environment copy or move operations. After any environment copy or move, turn Dataverse Intelligence off and back on in the Power Platform Admin Center to force a restart.

For additional questions about the semantic model, see [Dataverse semantic model FAQ](semantic-model-faq.md).

## Related content

- [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md)
- [Manage semantic model glossary entries](manage-semantic-model-glossary.md)
- [Regenerate the semantic model](regenerate-semantic-model.md)
- [Dataverse semantic model FAQ](semantic-model-faq.md)
