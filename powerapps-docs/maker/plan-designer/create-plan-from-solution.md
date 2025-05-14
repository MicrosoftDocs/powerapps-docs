---  
title: Create a plan for your solution using Plan designer  
description: Learn how to use Plan designer to create a detailed plan for your existing solution, including business problems, user requirements, data models, and technology stacks.  
author: szlo  
contributors:  
ms.topic: how-to  
ms.date: 05/01/2025  
ms.author: mkaur  
ms.reviewer: mkaur  
---  

# Create a plan from a solution

Use Plan designer to create a plan for your existing solution. Plan designer generates a detailed document that describes your solution. The plan covers the business problem, user requirements like user roles and stories, the data model, and technologies like apps and flows. This feature saves time when you're trying to understand a solution's content and helps makers improve an existing solution.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. In the navigation pane, select **Solutions**.
1. Select **Create plan from a solution**. Or, from the list of solutions, select a solution, and then select **Commands** > **Create a plan**.

    :::image type="content" source="media/create-a-plan-from-a-solution/create-plan-from-solution.png" alt-text="Screenshot of creating a plan from a solution.":::

1. Select **Select solution** and then choose a solution.
    
    > [!NOTE]  
    > The solution must have at least one app and one associated table.  

1. Select **Create plan**.

    :::image type="content" source="media/create-a-plan-from-a-solution/create-plan-1.png" alt-text="Screenshot of the interface for selecting a solution and creating a plan.":::

1. When the plan is created, save it. For an unmanaged solution, the plan is saved in the same solution. For a managed solution, the plan is saved in a new unmanaged solution by default.

    :::image type="content" source="media/create-a-plan-from-a-solution/save-existing-plan.png" alt-text="Screenshot of the saved plan interface for unmanaged and managed solutions.":::

## Known limitations

- A solution needs at least one app and one associated table to create a plan.
- The plan recognizes apps, flows, and tables in a solution. Other objects, like sites and agents, are out of scope.
- To create a plan from an existing solution, publish the apps in the solution and then publish the solution.

## Related information

[Create a plan using Plan designer](create-plan.md)