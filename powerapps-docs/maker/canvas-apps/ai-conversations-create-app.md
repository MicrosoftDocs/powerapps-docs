---
title: Build apps through conversation with Copilot 
description: Build apps easily with AI in Microsoft Power Apps. Describe the information you want to collect, track, or show in your app, and Copilot creates Dataverse tables and guides you through the process.
author: mduelae
ms.topic: how-to
ms.collection:
  - bap-ai-copilot
  - get started
ms.reviewer:
ms.date: 4/16/2025
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

Create apps without writing code or designing screens. With Copilot in Power Apps, you can use natural language to describe what you want your app to do, and AI does the rest.

Copilot is a feature in Power Apps that helps you build apps with AI assistance. You can access Copilot from the Power Apps home screen. Type what kind of information you want to collect, track, or show in your app, and Copilot generates one or more Microsoft Dataverse tables that you can use to build your canvas app.

## Prerequisites

- Ensure you meet the prerequisites and region availability in [Copilot in Power Apps overview (preview)](ai-overview.md).
- Depending on where your environment is hosted, you might need to allow data movement across regions. Learn more in [Copilots and generative AI features that are available when you enable data movement across regions](/power-platform/admin/geographical-availability-copilot#copilots-and-generative-ai-features-that-are-available-when-you-enable-data-movement-across-regions).
- Include a Dataverse database in your environment. Learn more in [Add a Microsoft Dataverse database](/power-platform/admin/create-database).
- Confirm that this feature is available in your region. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).
- The system customizer security role in the environment.

## Create an app with Copilot

To show you how Copilot works, let's create an app to track housekeeping tasks for a hotel.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Type your prompt in the text box such as the example prompt shown below.

    ```copilot-prompt
    Hotel housekeeping
    ```
   :::image type="content" source="media/artificial-intelligence/create-app-using-ai-1.png" alt-text="Screenshot of the Power Apps home page, with the Copilot input text box highlighted." lightbox="media/artificial-intelligence/create-app-using-ai-1.png":::

Copilot creates one or more Dataverse tables with data that includes typical hotel housekeeping tasks.

> [!IMPORTANT]
> If you don't have the right permissions and access to Dataverse in the environment you're working in, an alert asks you to create the app in your own environment. Confirm that the table and app can be created in your environment to proceed. If you don't have a personal developer environment, a new one is created for you automatically. Learn more in [Get your developer environment (preview)](../maker-create-environment.md).

## Review the table

Copilot generates tables and relationships based on your description. Review them and make any changes you need to before you go on to create your app.

### Review the tables for your app

Copilot shows you the tables and relationships that it generated based on your description.

:::image type="content" source="media/artificial-intelligence/data-workspace-copilot.png" alt-text="Screenshot of Dataverse tables and relationships for a hotel housekeeping app, with numbered annotations.":::

Legend:

1. **Edit**: Edit or create more tables in your canvas. Learn more in [Create and edit tables](../data-platform/create-edit-entities-portal.md).

1. **Copilot text box**: [Ask Copilot to modify the table](#use-copilot-to-make-changes) or create more tables for you.

1. **View prompt**: View examples of things that you can ask Copilot to do.

1. **Save and open app**: Save your tables and create your app. To start over, select **Back**.


## Use Copilot to make changes

If you want to change something, enter in the Copilot panel a brief description of the change you want to make. Copilot does it for you.

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
