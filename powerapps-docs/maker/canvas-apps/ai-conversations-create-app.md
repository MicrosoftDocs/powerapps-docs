---
title: Build apps through conversation with Copilot 
description: Build apps easily with AI in Microsoft Power Apps. Describe the information you want to collect, track, or show in your app, and Copilot creates Dataverse tables and guides you through the process.
author: mduelae
ms.topic: how-to
ms.collection:
  - bap-ai-copilot
  - get started
ms.reviewer:
ms.date: 01/12/2026
ms.update-cycle: 180-days
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType:
  - maker
contributors:
  - mduelae
ms.custom:
  - canvas
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-gen-desc
  - ai-seo-date:08/28/2024
  - copilot-scenario-highlight
ai-usage: ai-assisted
---

# Build apps through conversation with Copilot 

Create apps without writing code or designing screens. By using Copilot in Power Apps, you use natural language to describe what you want your app to do, and AI does the rest.

Copilot is a feature in Power Apps that helps you build apps with AI assistance. Access Copilot from the Power Apps home screen. Enter the type of information you want to collect, track, or show in your app, and Copilot generates one or more Microsoft Dataverse tables that you use to build your canvas app.

## Prerequisites

- Check the prerequisites and region availability in [Copilot in Power Apps overview (preview)](ai-overview.md).
- Depending on where your environment is hosted, you might need to enable data movement across regions. For more information, see [Copilots and generative AI features that are available when you enable data movement across regions](/power-platform/admin/geographical-availability-copilot#copilots-and-generative-ai-features-that-are-available-when-you-enable-data-movement-across-regions).
- Add a Dataverse database to your environment. For more information, see [Add a Microsoft Dataverse database](/power-platform/admin/create-database).
- Check if this feature is available in your region. For more information, see [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).
- Assign the system customizer security role in the environment.

## Create an app by using Copilot

Let's create an app to track housekeeping tasks for a hotel so you can see how Copilot works.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. On the left navigation pane, select **Create** > **Start with Copilot**.

1. Enter your prompt in the text box, like the example prompt in the following section.

    ```copilot-prompt
    Hotel housekeeping
    ```
1. Select table options, like multiple tables or one table, and then select **Generate**.
 
Copilot creates one or more Dataverse tables with data that includes typical hotel housekeeping tasks.

> [!IMPORTANT]
> If you don't have the right permissions or access to Dataverse in the environment you're working in, an alert asks you to create the app in your own environment. Make sure you can create the table and app in your environment to continue. If you don't have a personal developer environment, a new one is created for you automatically. For more information, see [Get your developer environment (preview)](../maker-create-environment.md).

## Review the table

Copilot generates tables and relationships based on your description. Review them and make any changes you need before you create your app.

### Review the tables for your app

Copilot shows you the tables and relationships it generates based on your description.

:::image type="content" source="media/artificial-intelligence/data-workspace-copilot.png" alt-text="Screenshot of Dataverse tables and relationships for a hotel housekeeping app, with numbered annotations.":::

Legend:

1. **Edit**: Edit or create more tables. Learn more in [Create and edit tables](../data-platform/create-edit-entities-portal.md).

1. **Copilot text box**: [Ask Copilot to modify the table](#use-copilot-to-make-changes) or create more tables for you.

1. **View prompt**: See examples of what you can ask Copilot to do.

1. **Save and open app**: Save your tables and create your app. To start over, select **Back**.


## Use Copilot to make changes

To change something, enter a brief description of the change in the Copilot panel. Copilot makes the change for you.

For example, ask Copilot to add columns to track cleaning start and end time.

1. In the Copilot text box, enter **Add columns to track start and end time**.

    Copilot adds two new columns called **Start Time** and **End Time**.

1. Continue editing the table as needed. For example, add room status, change room types, or set a priority level for each room.

1. When you're ready to create your app, select **Save and open app**.

## Related information

- [Copilot in Power Apps overview (preview)](ai-overview.md)
- [Add a Copilot control to a canvas app (preview)](add-ai-copilot.md)
- [Build apps through conversation (video)](https://youtu.be/A4cBqQjnIBg?feature=shared)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
