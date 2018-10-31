---
title: "Organize your solutions (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This document lists down some strategies to organize your solutions" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Organize your solutions

Before you create solutions, take some time to plan ahead. For example, think about how many solutions you want to release and whether the solutions will share components.  
  
 Also, determine how many Common Data Service for Apps organizations you’ll need to develop your line of solutions. You can use a single organization for most strategies described in this topic. However, if you decide to have only one organization and later realize that you need more, it can be challenging to change the solutions if people have already installed them. Using multiple organizations, although introducing more complexity, can provide better flexibility.  
  
<a name="BKMK_OptionsToModularize"></a>   
## Strategies to organize your solutions  
 The following are some strategies for creating solutions listed in order from simplest to most complex:  
  
-   [No custom solutions](organize-solutions.md#BKMK_NoCustomSolution)  
  
-   [Single solution](organize-solutions.md#BKMK_SingleSolution)  
  
-   [Multiple solutions](organize-solutions.md#BKMK_MultipleSolutions)  
  
-   [Multiple solutions with shared components](organize-solutions.md#BKMK_MultipleSolutionsSharedComponents)  
  
-   [Solution libraries](organize-solutions.md#BKMK_SolutionLibraries)  
  
<a name="BKMK_NoCustomSolution"></a> 
  
### No custom solutions  
 You don’t have to create solutions. You can customize CDS for Apps directly by using the default solution.  
  
 You can still export your default solution as an unmanaged solution to transport it between organizations.  
  
> [!TIP]
>  If you change the customization prefix for the default publisher to a value that matches a publisher you may want to create in the future, any new customizations that you create will include this customization prefix in the name. This way, if you use solutions, you can add the customizations that you created in your default solution to an unmanaged solution so they can have consistent names.  
  
<a name="BKMK_SingleSolution"></a>   
### Single solution  
 By creating a solution, you establish a working set of customizations. This makes it easier to find items that you have customized.  
  
 This approach is recommended when you only want to create a single managed solution. If you think you may have to split up the solution in the future, consider using multiple solutions.  
  
<a name="BKMK_MultipleSolutions"></a>   
### Multiple solutions  
 If you have two unrelated solutions that don’t share components, the most direct approach is to create two unmanaged solutions.  
  
> [!NOTE]
>  It is very common in solutions to modify the application ribbons or the Sitemap. If both of your solutions modify these solution components, they are shared components. See the following section to see how to work with shared components.  
  
<a name="BKMK_MultipleSolutionsSharedComponents"></a>   
### Multiple solutions with shared components  
 You may have multiple solutions that share components. You may have a certain set of common functionality within multiple solutions and that common functionality is compatible with any of the other functionality unique to each solution. For example, you may have a set of utility plug-ins that each solution uses yet each of the separate solutions do not share any other components.  
  
 In this case, each solution can be developed in a single organization. Some components can be included in more than one solution as long as any changes that were made to them are compatible with all other solutions that use them. It is important that all the solutions share the same solution publisher. If the solution publisher is not identical, organizations will not be able to install more than one of your solutions.  
  
<a name="BKMK_SolutionLibraries"></a> 
  
### Solution libraries  
 For an ISV with multiple solutions or a large enterprise deployment, many solution components will probably have to be shared. The best ways for solutions to share components is through solution libraries. Create a solution library by creating an unmanaged solution in a separate organization and then packaging those components into a managed solution. Install the managed solution into another organization and let developers reference these shared components.  
  
 The CDS for Apps Solutions Framework lets you build layers of solutions that depend on each other. Typically, you create a solution library representing a ”base” solution. Other solutions can be built on top of this base solution. This allows for cleaner separation of components. Development teams that are working on solution libraries and those working on the dependent solutions can develop at different paces. The dependent solutions must be created after the solution libraries are installed.  
  
 This requires that you create a prerequisite solution that customers must install before they can install a dependent solution. Developers working on the solution libraries can continue to work on them and update them as long as they don’t break any dependent solutions that require them.  
  
### See also  
 [Organize your team to develop solutions](organize-team-develop-solutions.md)   
 [Planning for Solution Development](/dynamics365/customer-engagement/developer/plan-solution-development)
