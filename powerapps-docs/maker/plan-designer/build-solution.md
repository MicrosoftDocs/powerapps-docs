---  
title: Build Your Solution With canvas apps, model-driven Apps, flows, and agents  
description: Learn how to build business solutions using canvas apps, model-driven apps, Power Automate flows, and Copilot Studio agents. Incorporate existing apps into your plans for efficiency and consistency.  
author: mduelae  
contributors:  
ms.topic: conceptual  
ms.date: 05/19/2025  
ms.author: mkaur  
ms.reviewer: mkaur  
---  

# Build a solution from a plan

Build a solution based on the objects the Plan designer suggests for your business problem.

To follow this article, create and save a plan. Learn more in [create a plan](create-plan.md).

:::image type="content" source="media/build-your-solution/save-plan.png" alt-text="Screenshot of the Plan designer interface showing the Save tables option." lightbox="media/build-your-solution/save-plan.png":::

After you save a plan in a solution, create apps like canvas apps, model-driven apps, Power Automate flows, and Copilot Studio agents based on the solution proposal from the Plan designer.

:::image type="content" source="media/create-a-plan/create-objects.png" alt-text="Screenshot of the interface to create a solution.":::

## Create objects

1. Select **Create**.

    :::image type="content" source="media/build-your-solution/create-app-tiles.png" alt-text="Screenshot of the Create button. The Create button is selected in the app tiles interface." lightbox="media/build-your-solution/create-app-tiles.png":::

1. When you select **Create** on one of these tiles, these objects are created:

    - **Canvas app**: Opens Power Apps Studio with a data-connected app that starts for you. The app has responsive screens to view and edit data for each recommended table, and a welcome screen to navigate the app. Learn more about customizing screens in [Add and navigate screens](/power-apps/maker/canvas-apps/add-screen-context-variables#welcome-screen). Before you use the app, [save and publish it](../canvas-apps/save-publish-app.md). 

    - **Model-driven app**: Opens the modern app designer with data tables already added. Before you use the app, save and publish it.

    - **Power Pages site**: Opens [Power Pages design stuido(/power-pages/getting-started/use-design-studio)) with the initial setup, including layout design, domain configuration, and pages tailored to your goals. Use the studio to develop your website. Learn more in [Overview of designing and building sites](/power-pages/configure/design-build-overview). To create a Power Pages site, you need the [System administrator](/power-pages/admin/admin-roles#system-administrator) role in the environment.
        - Save and publish the site before you use it. Save the site to the same solution as the plan for healthy application lifecycle management (ALM).
        - When you save a plan in a new solution, make sure to select the **Set this as your preferred solution in this environment** option to save the subsequent items created in this solution by default.
        :::image type="content" source="media/build-your-solution/power-pages-save-option.png" alt-text="Sceenshot of saving plan to preferred solution in a environment":::
 
    - **Power Automate flow**: Opens Power Automate with a prefilled prompt based on the business problem, user story, flow description, and data sources. To use the flow, save and publish it.
    
        - **Copilot Studio agents**: Opens Microsoft Copilot Studio (MCS), where you finish creating your agent and then publish it. An agent is an AI-powered assistant that simplifies workflows, boosts productivity, and automates repetitive tasks. The Plan designer includes agents as part of its recommended technologies. The plan prefills the agent with the following information:

        - **Name**: Name of the agent.
        - **Description**: Purpose of the agent.
        - **Instructions**: Set of actions for the agent to take.
        - **Knowledge**: All tables created by the plan are added to the agent as knowledge sources.

        Review the instructions and update the agent as needed for your scenario. For example, add a trigger or an action to the agent. Test the agent to make sure it works as expected before you publish it.

        Learn more about Microsoft Copilot Studio.

         - [Agent flows overview](/microsoft-copilot-studio/flows-overview)
         - [Add actions to custom agents](/microsoft-copilot-studio/advanced-plugin-actions)
         - [Test your agent](/microsoft-copilot-studio/authoring-test-bot?tabs=webApp)
         - [Key concepts – Publish and deploy your agent](/microsoft-copilot-studio/publication-fundamentals-publish-channels)
         - [Key concepts - Analytics](/microsoft-copilot-studio/analytics-overview)  

## Use existing apps

When Plan designer proposes apps, replace a proposed app with an existing app or add an existing app to the plan. This approach helps if you already developed apps and want to use them in a new business solution. It saves time, reduces redundancy, and keeps your solutions consistent.

- To replace an app proposed in the plan, select **Replace** on the app tile you want to replace, and then select an app.

    :::image type="content" source="media/build-your-solution/replace-app.png" alt-text="Screenshot of the Replace option on an app tile.":::


- To add an existing app that isn't related to the proposed scenarios, select **Add technology**, and then select an app.

    :::image type="content" source="media/build-your-solution/add-technology.png" alt-text="Screenshot showing how to add an existing app to the plan.":::

    Existing apps you add to the plan aren't included in a new solution. Use the solution view to see all solutions related to the plan.

## Next steps

[Manage your solution](manage-solution.md)
