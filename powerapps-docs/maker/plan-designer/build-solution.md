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

Start building a solution based on the objects Plan desigher proposes based on your business problem.

To follow this article, you need to create a plan and save it. Learn more about creating a plan in [Create a plan](create-plan.md).

:::image type="content" source="media/build-your-solution/save-plan.png" alt-text="Screenshot of the Plan designer interface that shows the Save tables option." lightbox="media/build-your-solution/save-plan.png":::

After your plan is saved to solution, you can create apps like canvas apps, model-driven apps, Power Automate flows, and Copilot Studio agents based on the solution proposal from Plan designer.

:::image type="content" source="media/create-a-plan/create-objects.png" alt-text="Create your solution":::

## Create objects

1. Select **Create** to create the selected object.

    :::image type="content" source="media/build-your-solution/create-app-tiles.png" alt-text="Select create to create the object." lightbox="media/create-app-tiles/save-plan.png":::

2. When you select **Create** on one of these tiles, here's what happens:

    - **Canvas app**: Opens Power Apps Studio with a data-connected app that starts for you. The app includes responsive screens to view and edit data for each recommended table, and a welcome screen to navigate the app.Learn more about customizing  screens in the [Add and navigate screens](/power-apps/maker/canvas-apps/add-screen-context-variables#welcome-screen). Before using the app, [save and publish it](../canvas-apps/save-publish-app.md). 

    - **Model-driven app**: Opens the modern app designer with data tables already added. Save and publish the model-driven app to start using it.

    - **Power Automate flor**: Opens Power Automate with a prefilled prompt based on the business problem, user story, flow description, and data sources. Save and publish the flow to use it.
    
    - **Copilot Studio Agents**: Opens Microsoft Copilot Studio (MCS), where you finish creating your agent and then publish it. An agente is an AI-powered assistant that simplifies workflows, enhances productivity, and automates repetitive tasks. The plan designer includes agents as part of its technologies it recommends. The agent created by the plan is autofitted with the following informatoin:

        - **Name**: Name of the Agent  

        - **Description**: Details the purpose of the Agent  
   :::image type="content" source="media/build-your-solution/image6.png" alt-text="Screenshot of the Agent description field in Microsoft Copilot Studio.":::

        - **Instructions**: Provides a set of actions for the Agent to take  
           :::image type="content" source="media/build-your-solution/image7.png" alt-text="Screenshot of the Agent instructions field in Microsoft Copilot Studio.":::

        - **Knowledge**: All tables created by the plan are added to the Agent as  knowledge sources  
           :::image type="content" source="media/build-your-solution/image8.png" alt-text="Screenshot of the knowledge sources section in Microsoft Copilot Studio.":::

        Review the instructions and update the agent as needed for your scenario. For example, you may need to add a trigger or an action to the agent.

        Test your agent before publishing. 

        Learn more about Copilot Studio:

        - [Agent flows overview](/microsoft-copilot-studio/flows-overview)  
        - [Add actions to custom agents](/microsoft-copilot-studio/advanced-plugin-actions)  
        - [Test your agent](/microsoft-copilot-studio/authoring-test-bot?tabs=webApp)  
        - [Key concepts – Publish and deploy your agent](/microsoft-copilot-studio/publication-fundamentals-publish-channels)  
        - [Key concepts - Analytics](/microsoft-copilot-studio/analytics-overview)  

## Replace with an existing app

You can use existing apps in your plan. This saves time, reduces redundancy, and keeps your solutions consistent.

When new apps are proosed, you can replace them existing apps.

On the app tile, select **Replace** and choose an existing app.

:::image type="content" source="media/build-your-solution/replace-app.png" alt-text="Replace existing app":::


