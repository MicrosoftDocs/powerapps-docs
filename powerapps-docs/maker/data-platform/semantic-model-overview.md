---
title: Overview of Dataverse semantic model
description: Learn what the Dataverse semantic model is, how its building blocks work together, and which Copilot and agent experiences it powers — for Power Apps makers and Dataverse administrators.
ms.topic: overview
ms.date: 11/17/2026
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: matp
reviewer: Mattp123
ai-usage: ai-generated
---

# Overview of Dataverse semantic model

The Dataverse semantic model gives AI agents and Copilot experiences a shared, business-aware understanding of your Dataverse data. Rather than reasoning from raw column and table names alone, agents that consume the semantic model understand what your data *means*.

The platform automatically provisions semantic models for supported Copilot experiences over Dataverse data. Makers and administrators can then fine-tune each model's table sources and signals, and add domain-specific glossary terms for business language that automatic extraction can't infer.

You can also create a custom model for a specific purpose. Custom models are currently usable through direct API and action calls; creation doesn't automatically associate a model with an app or agent. See [Create a custom semantic model (preview)](fine-tune-semantic-model-signals.md#create-a-custom-semantic-model-preview).

## Building blocks of the semantic model

The semantic model combines three building blocks to give agents a complete picture of your Dataverse data: data scope with semantic indexing, system-inferred signals, and a human-curated glossary. Together, they allow agents to understand not just what your data contains, but what it means.

### Data scope with semantic indexing

The data scope defines the set of Dataverse tables covered by the semantic model. Semantic indexing is applied over those tables, forming the foundation for agent reasoning within a particular scenario. In the new experience, use **Configure** to add or remove table sources, then choose which signals each included table contributes.

### System-inferred signals

The semantic model automatically extracts signals from metadata that already exists in your Dataverse environment: table and column descriptions, table relationships, views, forms, and optionally sample data rows. The model uses this context to build semantic understanding. Available signal controls can differ by environment.

You can fine-tune which signals are included and exclude those that introduce noise or are no longer relevant. For details, see [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md).

### Glossary

The glossary allows makers to add domain-specific terms, acronyms, synonyms, and definitions that system signals can't infer. If your organization uses coined abbreviations or business-specific terminology that agents misinterpret, glossary entries close those gaps directly. For details, see [Manage semantic model glossary entries](manage-semantic-model-glossary.md).

## Why use the semantic model

The semantic model provides context that helps agents interpret your business data:

- *Business context* - Table summaries, relationships, and glossary definitions help agents interpret intent beyond schema names.
- *Focused scope* - A relevant table selection and signal configuration help reduce ambiguity in the model's context.
- *Reduced setup time* — The model automatically extracts semantic knowledge from your existing Dataverse environment. As your schema evolves, the model updates on a scheduled basis.
- *Shared context across agents* - When multiple agents reference the same semantic model, they use the same configured signals and glossary. Responses can still vary with the question and the caller's Dataverse privileges.

## How the semantic model works

Once [Dataverse intelligence](./data-platform-intelligence.md) is enabled, the semantic model is provisioned automatically. It reads metadata from your Dataverse environment and extracts the following signals:

| Signal | What is captured |
|---|---|
| Table relationships | How records across tables are associated, such as one-to-many and many-to-many relationships. |
| Views | Public views with join conditions and sub-grid views that define which records and columns are relevant for a scenario. |
| Forms summaries | Context summarized from forms and form fields. |
| Table summaries | Context generated from table descriptions, column headers, and column descriptions. |
| Sample data rows | Representative rows showing what data looks like in each column. |

> [!NOTE]
> Sample data rows are turned off by default. System views - including Quick Find, Advanced Find, Associated, and Lookup views - and personal views are excluded from signal extraction. Polymorphic relationships aren't available to configure.

The semantic model regenerates automatically every 12 hours to reflect schema changes. You can also request a manual regeneration. Save configuration changes before requesting regeneration, and wait for the run to complete before checking the generated context. Initial generation can take up to two hours, and incremental changes typically take up to 30 minutes. For details, see [Regenerate the semantic model](regenerate-semantic-model.md).

## Copilot experiences that use the semantic model

The semantic model is automatically provisioned and consumed by the following Copilot and agent experiences when they are set up over Dataverse data:

- *Copilot in Power Apps* — Available in model-driven apps. For setup information, see [Add Microsoft Copilot for app users in model-driven apps](../model-driven-apps/add-microsoft-365-copilot.md).
- *Microsoft Copilot with Dataverse* — Connects Microsoft Copilot to your Dataverse data. For setup information, see [Dataverse data in Microsoft Copilot](./data-platform-data-copilot.md).
- *Sales Agent in Microsoft 365* — Uses Dataverse data to power sales scenarios. For setup information, see [Set up Sales agent in Microsoft Copilot](/microsoft-sales-copilot/set-up-sales-chat).
- *Microsoft Copilot Studio agents over Dataverse data* — Agents built in Copilot Studio that use Dataverse tables as a knowledge source. For setup information, see [Add Dataverse tables as a knowledge source](/microsoft-copilot-studio/knowledge-add-dataverse).

## Known limitations

The following limitations currently apply:

- New experience availability. Custom model creation and the **Configure** interface are available only in environments where the new semantic model experience is enabled and its version requirements are met. For steps, see [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md). For programmatic model creation, see [Manage Dataverse semantic models](../../developer/data-platform/ask/manage-semantic-models.md).
- No ALM support. The semantic model currently doesn't support environment copy or move operations. After any environment copy or move, turn Dataverse Intelligence off and back on in the Power Platform Admin Center to force a restart.

For additional questions about the semantic model, see [Dataverse semantic model FAQ](semantic-model-faq.md).

## Related content

- [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md)
- [Manage semantic model glossary entries](manage-semantic-model-glossary.md)
- [Regenerate the semantic model](regenerate-semantic-model.md)
- [Dataverse semantic model FAQ](semantic-model-faq.md)
