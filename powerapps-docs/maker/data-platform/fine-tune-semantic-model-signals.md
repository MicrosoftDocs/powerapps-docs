---
title: Create and configure Dataverse semantic models
description: Learn how to create a Dataverse semantic model, configure table sources and signals, and review generated context for agents and Copilot experiences.
ms.topic: how-to
ms.date: 11/17/2026
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: matp
reviewer: Mattp123
ai-usage: ai-generated
---

# Create and configure Dataverse semantic models

This article explains how to create and configure Dataverse semantic models, choose their table sources, and fine-tune the signals available to agents and Copilot experiences.

> [!NOTE]
> The **creation** and **Add or remove a table** steps in this article apply to the **New semantic model experience**, where available.

## Prerequisites

- A Dataverse environment with **Work IQ** enabled by a Power Platform administrator. For more information, see [Manage participation in Business Applications in Work IQ](/power-platform/admin/business-applications-work-iq/manage-participation#environment-features-for-work-iq).
- The semantic model has completed its initial generation. More information: [How the semantic model works](semantic-model-overview.md#how-the-semantic-model-works)
- Dataverse version with Dynamics 365 apps enabled must be 9.2.26103.00144 or later version.
- AIPlatformExtensions Solution must be 1.0.0.373 or later version.
- You need either of the following security roles to manage the semantic model:
   - System Administrator -or-
   - Dataverse Search, Semantic Model *and* Environment Maker.

> [!IMPORTANT]
> After Dataverse Intelligence is first enabled, an initial sync runs automatically and can take up to two hours to complete. During this initial sync, the semantic model page displays a generating state. Wait until the initial sync is finished before proceeding.
> The **new semantic model experience** is enabled by default. Use it to take advantage of its enhanced capabilities. However, you can turn it off at any time to switch back to the previous experience.

## Select a semantic model

The semantic models page is the central hub for managing semantic models in your environment. Select the model associated with the app or agent you want to configure.

1. Sign in to [Power Apps](https://make.powerapps.com), and open the environment where Dataverse Intelligence is enabled.
2. In the left navigation pane, select **More**, and if not in the **More** list, select **Discover all**, and then select **Semantic models** under **AI** section.
4. Select a semantic model from the list to view its overview, configure its table sources and signals, or manage its glossary.

The list shows the following columns for each semantic model:

| Column | Description |
| --- | --- |
| Name | The identifier of the semantic model. The name reflects the source that provisioned it. More information: [Naming conventions](#naming-conventions)  |
| Description | Describes what the model helps agents do. Select a model to add or edit a description. |
| Associated apps or agents | Apps or agents that have access to this semantic model. |
| Creator | The original creator of the model. |
| Date Created | The date when the model was created. |

A custom model with no associated app or agent displays **CUSTOM** in **Associated apps or agents**. You can currently use custom models through direct API and action calls. Creating one doesn't automatically connect it to an app or agent. For API guidance, see [Manage Dataverse semantic models](../../developer/data-platform/ask/manage-semantic-models.md) and [Ask questions by using a semantic model](../../developer/data-platform/ask/ask-semantic-model.md).

> [!TIP]
> Pin the **Semantic model** page to the left navigation pane for quick access.

## Naming conventions

Semantic models are named based on the source that provisioned them. Use the name to identify which experience a semantic model belongs to.

| Source | Name format | Associated apps or agents |
| --- | --- | --- |
| [Add Dataverse tables as a knowledge source](/microsoft-copilot-studio/knowledge-add-dataverse) | User-configured Dataverse knowledge name | custom agent name (user configurable) |
| [Add Microsoft Copilot for app users in model-driven apps](/power-apps/maker/model-driven-apps/add-microsoft-365-copilot) -or-<br /> [Dataverse data in Microsoft Copilot](data-platform-data-copilot.md) | `M365_Secondary_model_<App_name>` | Connected app display name (user configurable) |
| [Set up Sales agent in Microsoft Copilot](/microsoft-sales-copilot/set-up-sales-chat) -or-<br /> [Copilot in Dynamics 365 Sales overview](/dynamics365/sales/copilot-overview#chat-in-natural-language-or-use-predefined-prompts) | `SalesSpecificQnA` | Copilot in Dynamics 365 Sales |

> [!NOTE]
> Changes you make to a semantic model, including signal settings, table-level controls, and glossary entries, only apply to that specific semantic model. They don't affect other semantic models in your environment. If multiple apps or agents share the same semantic model (for example, Sales Agent and Copilot in Dynamics 365 Sales both use `SalesSpecificQnA`), changes to that model apply to all experiences associated with it.

## Manage the semantic model

The model's **Overview** tab shows three areas:

- **Signals**. Review the generated signal count and turn model-wide signal types on or off.
- **Table sources**. Review the number of tables in the model. Select **Configure table sources** to change the table selection and per-table signals.
- **Glossary**. Review the term count. Select **Go to Glossary** to add or edit business vocabulary.

Use **Configure** to edit the model's description, model-wide signals, and table sources. A saved model's name is read-only. Descriptions can contain up to 1,000 characters.

Select **Save** to apply all pending configuration changes to the semantic model. The changes take effect immediately. Saving configuration and regenerating the model are separate operations. For details, see [Regenerate the semantic model](regenerate-semantic-model.md).

You can control semantic models at multiple levels:

| Control level | Scope |
| --- | --- |
| Signal-type level | Enable or disable a signal type across all tables in the selected model. |
| Table level | Add or remove a table from the selected model, or change which signals it contributes. |
| Item level | Enable or disable a generated view or relationship within a table. |

> [!IMPORTANT]
> Generated summaries, views, and relationships are read-only. You can control which signals contribute to the model to improve relevance and exclude unnecessary information, but you can't directly edit the generated content. Use the glossary to add business definitions and context that automatic extraction might not capture.

## Create a custom semantic model (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Create a model when you need a table selection or purpose that isn't covered by an existing model.

[!INCLUDE [preview-note-business-applications-work-iq](~/../shared-content/shared/preview-includes/preview-note-business-applications-work-iq.md)]

1. On the semantic models page, select **Create model**.
2. Enter a **Model name** of up to 100 characters and, optionally, a **Description** of up to 1,000 characters. Model names must be unique in the environment.
3. Under **Manage signals**, choose the signal types to generate by default for tables in this model. **Sample table rows** is turned off at the model level by default.
4. Under **Configure table sources**, find the tables you need in **All tables** and select **Add table**. Include at least one table.
5. Select a table to adjust its per-table signal settings.
6. Select **Save**.

After creation, the model opens on **Configure**. Generated summaries, views, and relationships appear after the tables are saved and generation completes.

> [!NOTE]
> If a message says the model was created but its signal settings couldn't be saved, stay on the created model's **Configure** page, review the pending signal settings, and select **Save** if changes remain. If you leave or refresh the page, recheck **Manage signals** and **Table signals** because unsaved choices might be lost. Don't create a second model to retry the signal settings.

## Enable or disable a signal type

Model-wide settings apply across all tables in the selected semantic model.

1. Open the model and select **Configure**.
2. Under **Manage signals**, turn the relevant signal **On** or **Off**.
3. Select **Save**.

You can also change model-wide signals in the **Signals** area on **Overview**. The available signal types can differ by environment.

## Add or remove a table

Choose tables relevant to the questions the model should support. Removing a table from the model doesn't delete the Dataverse table.

1. Open the model and select **Configure**.
2. Under **Configure table sources**, select **All tables** to find an available table, or **Included in model** to review the current selection.
3. Search for the table display name and select the table.
4. Select **Add table** or **Remove table**, as appropriate.
5. Select **Save**.

Keep at least one table in the model. **Remove all** clears the pending table selection; it doesn't delete tables or the model, and you must add a table before saving.

To keep a table in the model but exclude a signal type for that table, select the table, open **Table signals**, and turn the signal off. A signal turned off in **Manage signals** can't be enabled for an individual table until it's enabled at the model level.

> [!IMPORTANT]
> Table selection and signal settings define the context of the semantic model. They don't override or replace Dataverse security roles, table-, column-, or record-level access controls, or application-level configurations.

## Enable or disable a specific table item

Views and relationships within a table can be individually disabled when they contain outdated, incorrect, or misleading data that negatively affects agent responses.

1. Open the model, select **Configure**, and select an included table.
2. Open **Views** or **Relationships** to review the generated items. Use **Summary** to review the generated table summary.
3. Turn the relevant view or relationship **On** or **Off**.
4. Select **Save**.

If an item control is unavailable, first enable its signal type in **Manage signals** and in the table's **Table signals** section. For a newly added table, save the table selection and wait for generation before reviewing its generated items.

## Add and manage glossary entries

The glossary lets you add business vocabulary that system signals can't infer automatically. Use glossary definitions to clarify the terminology used in your Dataverse tables, so agents better understand user questions and respond more accurately. For more information, see [Manage semantic model glossary entries](manage-semantic-model-glossary.md).

## Trigger a manual regeneration

The semantic model automatically regenerates every 12 hours. To request an earlier run after saving configuration or changing Dataverse metadata, select **Regenerate**. Regeneration is asynchronous; selecting the command doesn't mean the updated model is ready. For more information, see [Regenerate the semantic model](regenerate-semantic-model.md).

## Enable sample data rows

The **Sample table rows** signal is turned off by default. When available and enabled, it uses a selection of row values to give agents context about the table's content.

1. In **Overview**, or in **Configure** under **Manage signals**, turn **Sample table rows** on.
2. If the regeneration dialog appears, select **Save & regenerate** to save the settings and request regeneration.
3. If you select **Skip for now**, select **Save** separately to persist your changes. Regeneration is still required before sample rows are available to agents.

## Delete a custom semantic model (preview)

Before deleting a custom model, check which applications or API callers use it. Deletion can't be undone.

1. Return to the semantic models list.
2. Open the model's **More options** menu and select **Delete**, if available.
3. Confirm the deletion.

> [!NOTE]
> The **Delete** action appears for custom models only in the new experience. If deletion reports an error, refresh the list to check whether the model still exists before trying again.

## Add semantic model to a solution
Semantic models are solution-aware, which means you can package them into solutions for application lifecycle management (ALM). This capability allows you to move semantic model configuration between environments as part of your deployment process.

To add a semantic model to a solution:
1. Sign in to [Power Apps](https://make.powerapps.com) and select your environment.
2. Ensure the version of each skill you want to move is active.
3. Go to **Solutions** and open an existing solution or create a new one.
4. Select **Add existing** > **More** > **Other** > **DVTableSearch** from the top navigation bar.
5. Choose the semantic model you want to add to your solution, and then select **Add**.


## Related articles

- [Dataverse semantic model overview](semantic-model-overview.md)
- [Manage semantic model glossary entries](manage-semantic-model-glossary.md)
- [Regenerate semantic model](regenerate-semantic-model.md)
- [Dataverse semantic model frequently asked questions](semantic-model-faq.md)
