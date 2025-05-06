---  
title: Build Your Solution With Canvas Apps, Model-Driven Apps, Flows, and Agents  
description: Learn how to build business solutions using canvas apps, model-driven apps, Power Automate flows, and Copilot Studio agents. Incorporate existing apps into your plans for efficiency and consistency.  
author: mduelae  
contributors:  
ms.topic: conceptual  
ms.date: 05/01/2025  
ms.author: mkaur  
ms.reviewer: mkaur  
---  

# Build a solution from a plan

To follow this article, you need to create a plan and save the plan to a solution. Learn more about creating a plan in [Create a plan](create-plan.md).

Once your plan is saved to solution.

Create apps like canvas apps, model-driven apps, Power Automate flows, and Copilot Studio agents based on the solution proposal from Plan designer.

Before creating an object, create a plan and save the tables.

:::image type="content" source="media/build-your-solution/image1.png" alt-text="Screenshot of the Plan designer interface that shows the Save tables option.":::  



## Create canvas apps

After you save your tables, select **Create** for a canvas app.

:::image type="content" source="media/build-your-solution/image2.png" alt-text="Screenshot of the **Create** button on a canvas app in Power Apps.":::

Selecting **Create** for a canvas app opens Power Apps Studio with a data-connected app that starts for you. The app includes responsive screens to view and edit data for each recommended table, and a welcome screen to navigate the app. Learn more about customizing these screens in the [modern templates documentation](/power-apps/maker/canvas-apps/add-screen-context-variables#welcome-screen).

Save and publish the canvas app to use it.

## Create model-driven apps

After saving your tables, select **Create** in the model-driven app.

The modern app designer opens with the tables already added. Save and publish the model-driven app to start using it.

:::image type="content" source="media/build-your-solution/image3.png" alt-text="Screenshot of the modern app designer that shows tables already added.":::

## Create Power Automate flows

After saving your tables, select **Create** on the Power Automate flow card.

Selecting **Create** for the flow launches Power Automate with a prefilled prompt based on the business problem, user story, flow description, and data sources. Save and publish the flow to use it.

:::image type="content" source="media/build-your-solution/image4.png" alt-text="Screenshot of the Power Automate flow creation interface.":::

## Create Copilot Studio agents

A Copilot Studio agent is an AI-powered assistant that simplifies workflows, enhances productivity, and automates repetitive tasks. The plan designer includes agents as part of its technology stack.

Save your tables, then select **Create** on the Copilot Studio Agent card.

:::image type="content" source="media/build-your-solution/image5.png" alt-text="Screenshot of the Copilot Studio Agent card with the Create button highlighted.":::

Microsoft Copilot Studio (MCS) opens, letting you finish creating your agent and publish it. The agent created by the plan is autofitted with the following:

1. Name – Name of the Agent  
   :::image type="content" source="media/build-your-solution/image6.png" alt-text="Screenshot of the Agent name field in Microsoft Copilot Studio.":::

1. Description – Details the purpose of the Agent  
   :::image type="content" source="media/build-your-solution/image6.png" alt-text="Screenshot of the Agent description field in Microsoft Copilot Studio.":::

1. Instructions – Provides a set of actions for the Agent to take  
   :::image type="content" source="media/build-your-solution/image7.png" alt-text="Screenshot of the Agent instructions field in Microsoft Copilot Studio.":::

1. Knowledge – All tables created by the plan are added to the Agent as knowledge sources  
   :::image type="content" source="media/build-your-solution/image8.png" alt-text="Screenshot of the knowledge sources section in Microsoft Copilot Studio.":::

It is highly recommended to review the instructions and update the Agent as needed for your scenario. For example, you may need to add a trigger or an action to the Agent.

Test your Agent before publishing. Please see resources below for more information.

### Related content

[Agent flows overview](/microsoft-copilot-studio/flows-overview)  
[Add actions to custom agents](/microsoft-copilot-studio/advanced-plugin-actions)  
[Test your agent](/microsoft-copilot-studio/authoring-test-bot?tabs=webApp)  
[Key concepts – Publish and deploy your agent](/microsoft-copilot-studio/publication-fundamentals-publish-channels)  
[Key concepts - Analytics](/microsoft-copilot-studio/analytics-overview)  

## Create a plan with existing apps

Makers can incorporate existing apps into their plans. This is particularly beneficial for users who have already developed apps and want to include them in new business solutions without starting from scratch. By using existing apps, makers can save time, reduce redundancy, and ensure consistency across their solutions.

Once the Solution Agent proposes new apps, you can include your existing apps to the plan.

1. Replace proposed apps with existing apps.

   If you have an existing app that solves the same business problem as the proposed app, replace it with the existing app. In the app tile, select **choose existing**.

   :::image type="content" source="media/build-your-solution/image9.png" alt-text="Screenshot of a computer showing the option to choose an existing app.":::

2. Add existing apps to your existing plan.

   If your existing app is unrelated to the scenarios already added, in the document view, select “+Add”.

   :::image type="content" source="media/build-your-solution/image10.png" alt-text="Screenshot of a computer showing the option to add an existing app.":::

Existing apps added to the plan will not be added to a new solution. You can use the solution view to see all the solutions related to the plan.

:::image type="content" source="media/build-your-solution/image11.png" alt-text="Screenshot of a computer showing the solution view for the plan.":::