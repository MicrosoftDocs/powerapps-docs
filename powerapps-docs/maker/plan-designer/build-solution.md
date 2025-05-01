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

# Build your solution

You can create Applications (Canvas Apps and Model-driven Apps), Power Automate Flows, and Copilot Studio Agents from Plan Designer’s solution proposal.

Before creating an artifact item, select **Save tables**.

:::image type="content" source="media/build-your-solution/image1.png" alt-text="Screenshot of the Plan Designer interface showing the Save tables option.":::  

## Create canvas apps

After saving your tables, select **Create** on a canvas app card.

:::image type="content" source="media/build-your-solution/image2.png" alt-text="Screenshot of the Create button on a canvas app card in Power Apps.":::

Selecting **Create** for a canvas app launches Power Apps Studio with a data-connected app already started for you. This app includes responsive screens to view and edit data for each recommended table and a welcome screen to navigate the app. To learn more about customizing these screens, see the [modern templates documentation](/power-apps/maker/canvas-apps/add-screen-context-variables#welcome-screen). The canvas app can then be saved and published for use. 

## Create model-driven apps

After saving your tables, select **Create** on the model-driven app card.

The modern app designer opens with the tables already added. The model-driven app can then be saved and published for use.

:::image type="content" source="media/build-your-solution/image3.png" alt-text="Screenshot of the modern app designer with tables already added.":::

## Create Power Automate flows

After saving your tables, select **Create** on the Power Automate Flow card.

Selecting **Create** for Flow launches Power Automate with a pre-filled prompt based on the business problem, user story, flow description, and data sources. The Flow can then be saved and published for use.

:::image type="content" source="media/build-your-solution/image4.png" alt-text="Screenshot of the Power Automate Flow creation interface.":::

## Create Copilot Studio Agents

A Copilot Studio Agent is an AI-powered assistant designed to simplify workflows, enhance productivity, and automate repetitive tasks. Plan Designer now proposes Agents as part of its technology stack.

After saving your tables, click **Create** on the Copilot Studio Agent card.

:::image type="content" source="media/build-your-solution/image5.png" alt-text="Screenshot of the Copilot Studio Agent card with the Create button highlighted.":::

You will be navigated to Microsoft Copilot Studio (MCS) to finish creating your Agent and then publish your Agent. The Agent created by the Plan will be autofitted with the following:

1.  Name – Name of the Agent  
    :::image type="content" source="media/build-your-solution/image6.png" alt-text="Screenshot of the Agent name field in Microsoft Copilot Studio.":::

1.  Description – Details the purpose of the Agent  
    :::image type="content" source="media/build-your-solution/image6.png" alt-text="Screenshot of the Agent description field in Microsoft Copilot Studio.":::

1.  Instructions – Provides a set of actions for the Agent to take  
    :::image type="content" source="media/build-your-solution/image7.png" alt-text="Screenshot of the Agent instructions field in Microsoft Copilot Studio.":::

1.  Knowledge – All tables created by the plan are added to the Agent as knowledge sources  
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

   If you have an existing app that solves the same business problem as the proposed, you can replace it by the existing. In the app card, select choose existing.

   :::image type="content" source="media/build-your-solution/image9.png" alt-text="Screenshot of a computer AI-generated content may be incorrect.":::

2. Add existing apps to your existing plan.

   If your existing app is unrelated to the scenarios already added, in the document view, select “+Add”.

   :::image type="content" source="media/build-your-solution/image10.png" alt-text="Screenshot of a computer AI-generated content may be incorrect.":::

Existing apps added to the plan will not be added to a new solution. You can use the solution view to see all the solutions related to the plan.

:::image type="content" source="media/build-your-solution/image11.png" alt-text="Screenshot of a computer AI-generated content may be incorrect.":::