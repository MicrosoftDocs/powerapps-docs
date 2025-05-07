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

On the solutions page, select **Create plan from a solution**.

:::image type="content" source="media/create-a-plan-from-a-solution/image1.png" alt-text="Screenshot of the solutions page with the Create plan from a solution option highlighted.":::

Select the solution that you would like to create a plan for. 

> [!NOTE]  
> The solution must have at least 1 app and 1 associated table.  

After selecting your solution, select **Create plan**.

:::image type="content" source="media/create-a-plan-from-a-solution/image2.png" alt-text="Screenshot of the interface for selecting a solution and creating a plan.":::

After your plan is created, save the plan. For an unmanaged solution, the plan defaults to saving in the same solution. For a managed solution, the plan defaults to saving in a new unmanaged solution.

:::image type="content" source="media/create-a-plan-from-a-solution/image3.png" alt-text="Screenshot of the save plan interface for unmanaged and managed solutions.":::

Alternatively, you can select your solution in the solutions list and, in the overflow menu, select **Create a plan**.

:::image type="content" source="media/create-a-plan-from-a-solution/image4.png" alt-text="Screenshot of the overflow menu with the Create a plan option highlighted.":::

## Known limitations

1. A solution must have at least one app and one associated table to successfully create a plan.

2. The plan recognizes apps, flows, and tables in a solution. Other objects, such as sites and agents, are currently out of scope.

3. Publish the apps in your solution.

4. The solution must be published.

## Related information

[Create a plan using Plan designer](create-plan.md)