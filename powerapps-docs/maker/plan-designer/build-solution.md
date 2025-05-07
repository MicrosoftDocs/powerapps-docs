---  
title: Build Your Solution With canvas apps, model-driven Apps, flows, and agents  
description: Learn how to build business solutions using canvas apps, model-driven apps, Power Automate flows, and Copilot Studio agents. Incorporate existing apps into your plans for efficiency and consistency.  
author: mduelae  
contributors:  
ms.topic: conceptual  
ms.date: 05/01/2025  
ms.author: mkaur  
ms.reviewer: mkaur  
---  

# Build a solution from a plan

To follow this article, you need to create a plan and save it. Learn more about creating a plan in [Create a plan](create-plan.md).

After your plan is saved to solution, you can create apps like canvas apps, model-driven apps, Power Automate flows, and Copilot Studio agents based on the solution proposal from Plan designer.

:::image type="content" source="media/build-your-solution/save-plan.png" alt-text="Screenshot of the Plan designer interface that shows the Save tables option." lightbox="media/build-your-solution/save-plan.png":::

## Create canvas apps

On a canvas app tile, select **Create** to open Power Apps Studio with a data-connected app that starts for you. The app includes responsive screens to view and edit data for each recommended table, and a welcome screen to navigate the app. Learn more about customizing these screens in the [modern templates documentation](/power-apps/maker/canvas-apps/add-screen-context-variables#welcome-screen).


:::image type="content" source="media/build-your-solution/image2.png" alt-text="Screenshot of the **Create** button on a canvas app in Power Apps.":::


Before using the app, [save and publish it](../canvas-apps/save-publish-app.md).

## Create model-driven apps

Select **Create** in the model-driven app tile to open the modern app designer with data tables already added. Save and publish the model-driven app to start using it.

:::image type="content" source="media/build-your-solution/image3.png" alt-text="Screenshot of the modern app designer that shows tables already added.":::

## Create Power Automate flows

Select **Create** on the Power Automate flow tile to open Power Automate with a prefilled prompt based on the business problem, user story, flow description, and data sources. Save and publish the flow to use it.

:::image type="content" source="media/build-your-solution/image4.png" alt-text="Screenshot of the Power Automate flow creation interface.":::

## Create Copilot Studio agents

A Copilot Studio agent is an AI-powered assistant that simplifies workflows, enhances productivity, and automates repetitive tasks. The plan designer includes agents as part of its technologies it recommends.

Select **Create** on the Copilot Studio Agent tile.

:::image type="content" source="media/build-your-solution/image5.png" alt-text="Screenshot of the Copilot Studio Agent card with the Create button highlighted.":::

Microsoft Copilot Studio (MCS) opens, where you finish creating your agent and then publish it. The agent created by the plan is autofitted with the following informatoin:

- **Name**: Name of the Agent  

- **Description**: Details the purpose of the Agent  
   :::image type="content" source="media/build-your-solution/image6.png" alt-text="Screenshot of the Agent description field in Microsoft Copilot Studio.":::

- **Instructions**: Provides a set of actions for the Agent to take  
   :::image type="content" source="media/build-your-solution/image7.png" alt-text="Screenshot of the Agent instructions field in Microsoft Copilot Studio.":::

- **Knowledge**: All tables created by the plan are added to the Agent as knowledge sources  
   :::image type="content" source="media/build-your-solution/image8.png" alt-text="Screenshot of the knowledge sources section in Microsoft Copilot Studio.":::

Review the instructions and update the agent as needed for your scenario. For example, you may need to add a trigger or an action to the agent.

Test your agent before publishing. 

Learn more about Copilot Studio:

- [Agent flows overview](/microsoft-copilot-studio/flows-overview)  
- [Add actions to custom agents](/microsoft-copilot-studio/advanced-plugin-actions)  
- [Test your agent](/microsoft-copilot-studio/authoring-test-bot?tabs=webApp)  
- [Key concepts – Publish and deploy your agent](/microsoft-copilot-studio/publication-fundamentals-publish-channels)  
- [Key concepts - Analytics](/microsoft-copilot-studio/analytics-overview)  

## Create a plan with existing apps

You can incorporate existing apps into their plans. This is beneficial if you have  created apps and want to include them in new business solutions without starting from scratch. By using existing apps, you can save time, reduce redundancy, and ensure consistency across their solutions.

Once the **Solution Agent** proposes new apps, you can include existing apps to the plan.

1. In the app tile, select **Choose existing** to replace a proposed apps.

   :::image type="content" source="media/build-your-solution/image9.png" alt-text="Screenshot of a computer showing the option to choose an existing app.":::

2. Selec the app and then select **Add**.

   :::image type="content" source="media/build-your-solution/image10.png" alt-text="Screenshot of a computer showing the option to add an existing app.":::

The existing apps added to the plan will not be added to a new solution. Open the solution view to see all the solutions related to the plan.

:::image type="content" source="media/build-your-solution/image11.png" alt-text="Screenshot of a computer showing the solution view for the plan.":::