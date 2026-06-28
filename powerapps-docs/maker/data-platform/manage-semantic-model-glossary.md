---
title: Manage semantic model glossary entries (preview)
description: Learn how to add and edit glossary entries in the Dataverse semantic model to help agents and Copilot experiences understand your organization's terminology. Intended for Power Apps makers and Dataverse administrators.
ms.topic: how-to
ms.date: 06/17/2026
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: mkaur
reviewer: Mattp123
---
# Manage semantic model glossary entries (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

The glossary lets you add business vocabulary that system signals can't infer automatically. Use glossary definitions to clarify the terminology used in your Dataverse tables, so agents better understand user questions and respond more accurately.

[!INCLUDE [cc-preview-features-definition](../../../shared/preview-includes/preview-note-pp.md)]

## Add a glossary entry

> [!IMPORTANT]
> You can't delete system-defined glossary entries, but you can edit them to update the term or definition.

1. Sign in to [Power Apps](https://make.powerapps.com) and select the environment where your semantic model is provisioned.
1. From the semantic model overview, go to **Glossary**.
1. Select **Add item**. 
1. Enter the following:  
   - **Term**. The domain-specific word or acronym, such as "VP."
   - **Definition**. Enter a clear description of what the term means in your organization, such as "VP" refers to the Vice President value in the "JobTitle" column of the "Contact" table.

1. Select **Add term** to save.

> [!TIP]
> Write definitions as if you're explaining the term to someone unfamiliar with your organization. Precise definitions reduce the chance that agents interpret a term differently across different queries.

After saving, the entry is available to the semantic model. Changes are picked up during the next regeneration cycle. To make the entry available immediately, trigger a manual regeneration - see [Regenerate semantic model](regenerate-semantic-model.md).

## Edit an existing glossary entry

You can update any glossary entry you created to refine its term, definition, or synonyms as your organization's terminology evolves.

1. In the **Glossary** section of the semantic model, locate the entry you want to update. Use search to filter by term name if needed.
1. Select the entry to open it.
1. Update the **Term**, **Definition**, or **Synonyms** as needed.
1. Save your changes.

> [!NOTE]
> Edits to glossary entries take effect during the next regeneration. Trigger a manual regeneration if you need the change reflected immediately.

## Edit a system-defined glossary entry

Some glossary entries are created automatically by the system as part of the out-of-box semantic model. These entries appear alongside your custom entries in the glossary. You can edit them to better reflect your organization's terminology, but you can't delete them.

1. Go to **Glossary** and search for the term you want to edit.
1. Select the entry, and then select **Edit**.
1. Update the term, definition, or synonyms you want.
1. Select **Save changes**.

## Related articles

- [Dataverse semantic model overview](semantic-model-overview.md)
- [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md)
- [Regenerate semantic model](regenerate-semantic-model.md)
- [Dataverse semantic model frequently asked questions (preview)](semantic-model-faq.md)