---
title: "Create apps, data, and plans together"
description: Learn how the Power Apps new workspace simplifies app creation by generating plans, data models, and apps in parallel. Build smarter, faster, and seamlessly.
author: mduelae
ms.author: mkaur
ms.reviewer: mkaur
ms.date: 10/21/2025
ms.topic: concept-article
---

# Create apps, data, and plans together

The new workspace experience in Power Apps combines plans, data models, and apps in a single design surface, enabling you to design the app, data model, and requirements together. It reduces context switching and keeps you focused. Key capabilities:

- **Design everything together**: Create the app, plan, and data model in a single, seamless process
- **Build faster with AI**: Iterate and prototype through chat, from idea to a working app
- **One-click app generation**: Modern web apps created from your requirements and data

## Prerequisites

- Copilot must be enabled in the tenant and environment. Learn more: [Copilot in Power Apps overview](maker/canvas-apps/ai-overview.md)

- This capability is only available in the US region and in English only. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).


## Turn on new experience

Follow these these step to enable the new experience in Power Apps:

1. Sign in to [Power Apps](https://make.preview.powerapps.com/).
1. On the top right, select **Try new workspace (Preview)**.
:::image type="content" source="media/new-powerapps-experience/power-apps-new-workspace-toggle.png" alt-text="Screenshot of the Power Apps workspace showing the Try new workspace (Preview) toggle enabled and a tutorial pop-up explaining the feature.":::

### Turn off preview

To turn off the new experience and go back to generally avaiable defualt experience using [plans](maker/plan-designer/plan-designer.md), in the lower left select **Preview** > **Default homepage**.

## Create an app

1. Sign in to [Power Apps](https://make.preview.powerapps.com/).

   > [!IMPORTANT]
   > Make sure to turn on [Try new workspace (Preview)](new-powerapps-experience.md#turn-on-new-experience). 


1. Enter your prompt in the text box and then select **Enter**.  

    :::image type="content" source="media/new-powerapps-experience/power-apps-prompt-textbox.png" alt-text="Screenshot of Power Apps showing a prompt input box for the new experience." lightbox="media/new-powerapps-experience/power-apps-prompt-textbox.png":::

1. As the agents go to work and assets begin to load in the new workspace. You'll see the plan, the data model, and the app preview generating. 
 
   :::image type="content" source="media/new-powerapps-experience/powerapps-data-model-app-preview.png" alt-text="Screenshot of the Power Apps new workspace showing AI agents generating the plan, data model, and app preview simultaneously." lightbox="media/new-powerapps-experience/powerapps-data-model-app-preview.png":::

1. Data starts as in-memory draft tables. You may iterate on your data model and app without committing to any data source for rapid prototyping. And when you are ready to publish your data, you can choose between publishing as Dataverse tables or as SharePoint lists.

1. The initial save action stores the app, tables, and plan together in the preferred solution.

## Working in the new workspace

The new workspace has a single unified chat that allows you to work with powerful agents and keep context as you pivot focus between your app, plan, and data. You can switch focus using the pivots above the work surface or pop out a navigation menu to allow you to move between proposed objects at a more granular level. Each focus area has specific tools available to it above the work surface, like expanding/collapsing plan cards in Plan focus or choosing between visual preview, code view, or split view in the app focus. You can see all of the agents contributing to your generated solution. Finally you can save, publish, and share the generated objects (see more in the section below).
