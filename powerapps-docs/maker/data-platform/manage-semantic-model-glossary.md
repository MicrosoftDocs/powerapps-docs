---
title: Manage semantic model glossary entries
description: Learn how to add and edit glossary entries in the Dataverse semantic model to help agents and Copilot experiences understand your organization's terminology. Intended for Power Apps makers and Dataverse administrators.
ms.topic: how-to
ms.date: 11/17/2026
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: matp
reviewer: Mattp123
ai-usage: ai-generated
---
# Manage semantic model glossary entries

The glossary lets you add business vocabulary that system signals can't infer automatically. Use glossary definitions to clarify the terminology used in your Dataverse tables, so agents better understand user questions and respond more accurately.

## Open the glossary

Use the same environment and permissions described in [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md#prerequisites).

1. Sign in to [Power Apps](https://make.powerapps.com) and select the environment where your semantic model is provisioned.
2. Open the semantic models page and select the model you want to update.
3. Select **Glossary**. In the new semantic model experience, you can also select **Go to Glossary** on **Overview**.

Glossary changes apply only to the selected semantic model. If several apps or agents share it, those experiences use the same glossary.

## Add a glossary entry

> [!IMPORTANT]
> You can't delete system-defined glossary entries, but you can edit them to update the term or definition.

1. In **Glossary**, select **Add term**.
2. Enter both required fields:
   - **Term**. The domain-specific word or acronym, such as "VP."
   - **Definition**. Enter a clear description of what the term means in your organization, such as "VP" refers to the Vice President value in the "JobTitle" column of the "Contact" table.

3. Select **Add term** to save. The panel closes and a success message confirms that the term was added.

> [!TIP]
> Write definitions as if you're explaining the term to someone unfamiliar with your organization. Precise definitions reduce the chance that agents interpret a term differently across different queries.

The entry is saved separately from pending signal or table-source configuration. Changes are picked up during regeneration. To request an earlier run instead of waiting for the scheduled cycle, see [Regenerate the semantic model](regenerate-semantic-model.md). Regeneration must complete before you check the updated model.

## Edit an existing glossary entry

You can update an entry's term and definition as your organization's terminology evolves. The editor doesn't have a separate synonyms field; include relevant alternative names in the definition.

1. In **Glossary**, locate the entry you want to update. Search matches term names and definitions.
2. Select the entry's **Edit** action.
3. Update **Term** or **Definition**. Both fields must contain text.
4. Select **Save Changes**. Saving is available only when you change the term or definition.

> [!NOTE]
> Saving an entry confirms the glossary update, not completion of semantic model regeneration. Request a manual regeneration if you need an earlier run.

## Edit a system-defined glossary entry

Some glossary entries are created automatically by the system as part of the out-of-box semantic model. These entries appear alongside your custom entries in the glossary. You can edit them to better reflect your organization's terminology, but you can't delete them.

Use the same **Edit** action and **Term** and **Definition** fields as for a custom entry. The **Delete** action is disabled for system-defined entries.

## Delete a custom glossary entry

Delete entries that no longer describe your business vocabulary. You can't delete system-defined entries.

1. In **Glossary**, locate the custom entry.
2. Select its **Delete** action.
3. In the confirmation dialog, select **Delete term**.

After a successful deletion, the list refreshes and a success message confirms that the term was deleted. If an add, edit, or delete operation fails, review the error message before retrying.

## Related articles

- [Dataverse semantic model overview](semantic-model-overview.md)
- [Fine-tune semantic model signals](fine-tune-semantic-model-signals.md)
- [Regenerate semantic model](regenerate-semantic-model.md)
- [Dataverse semantic model frequently asked questions](semantic-model-faq.md)