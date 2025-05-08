---  
title: Create a plan for your solution using plan Designer  
description: Learn how to use Plan Designer to create a detailed plan for your existing solution, including business problems, user requirements, data models, and technology stacks.  
author: mduelae  
contributors:  
ms.topic: conceptual  
ms.date: 05/01/2025  
ms.author: mkaur  
ms.reviewer: mkaur  
---  

# Create a plan from a solution

Use Plan Designer to create a plan for your existing solution. Plan Designer generates a detailed document describing your solution. The plan includes a business problem, user requirements such as user roles and stories, a data model, and technologies like apps and flows. This feature saves time spent deciphering a solution's content and helps makers improve an existing solution.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. In the left navigation pane, select **Solutions**.
1. Select **Create plan from a solution**, or from the list of solutions, select a solution and then select **Commands** > **Create a plan**.

    :::image type="content" source="media/create-a-plan-from-a-solution/create-plan-from-solution.png" alt-text="Screenshot of the solutions page with the Create plan from a solution option highlighted.":::

1. Select **Select solution** and then choose a solution.
    
    > [!NOTE]  
    > The solution must have at least one app and one associated table.  

1. Select **Create plan**.

    :::image type="content" source="media/create-a-plan-from-a-solution/create-plan-1.png" alt-text="Screenshot of the interface for selecting a solution and creating a plan.":::

1. Save the plan after it's created. For an unmanaged solution, the plan is saved in the same solution. For a managed solution, the plan is saved by default in a new unmanaged solution.

    :::image type="content" source="media/create-a-plan-from-a-solution/save-existing-plan.png" alt-text="Screenshot of the saved plan interface for unmanaged and managed solutions.":::

## Known limitations

- A solution needs at least one app and one associated table to create a plan successfully.
- The plan recognizes apps, flows, and tables in a solution. Other objects, like sites and agents, are out of scope.
- To create a plan from an existing solution, you must publish the apps in the solution and publish the solution.

## Related information

[Create a plan using Plan designer](create-plan.md)