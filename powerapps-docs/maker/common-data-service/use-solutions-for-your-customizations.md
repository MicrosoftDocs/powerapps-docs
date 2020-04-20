---
title: "Use a solution to customize Power Apps | MicrosoftDocs"
description: "Learn how to customize Power Apps"
ms.custom: ""
ms.date: 02/20/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: f993c4ed-1fc3-4e47-bef1-d38695ddb11a
caps.latest.revision: 57
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Use a solution to customize
We recommend that you create a solution to manage your customizations. With a custom solution, you can easily find just the solution components you’ve customized, consistently apply your solution publisher prefix, and export your solution for distribution to other environments.  

If you don’t use a custom solution, you'll be working in a default solution in the unmanaged layer. There are two default solutions in every Common Data Service environment:  
- Common Data Service Default Solution. This is a base solution that is available for makers to use by default for their customizations in an environment. The Common Data Service Default Solution is useful when you want to evaluate or learn Power Apps.  
- Default Solution. This is a special solution that contains all components in the system. The default solution is useful for discovering all of the components and configurations in your system.  

## Why you shouldn’t use the default solutions to manage customizations
There are a few reasons why you shouldn’t create apps and make customizations in either of the default solutions:  
- The Default Solution contains all components and customizations from all solutions in the environment. 
- By default, all enabled users in an environment can create apps and customize components in the Common Data Services Default Solution. 
- It is difficult to locate or identify the customizations you have made in the environment using either default solution. 
- Using either default solution, when creating components will also use the default publisher assigned to it. This may result in the wrong publisher prefix being applied to some components. 
- The Default Solution can’t be exported. Therefore, you can’t distribute the Default Solution to another environment. 

<!-- Notice that if you have installed or imported other applications or solutions, additional solutions may be available in the solutions list. 

By default,  when you build or customize a model-driven app, you work with the solution called Common Data Services Default Solution. You can open the Common Data Services Default Solution to view and edit the components that are contained in it. To do this, follow these steps.
 
1.  On the left navigation pane select **Solutions**.

2.  In the list of solutions, select **Common Data Services Default Solution**.
  
> [!TIP]
>  If you plan to distribute the applications your make, consider changing the publisher customization prefix. More information: [Solution publisher prefix](change-solution-publisher-prefix.md).  -->
  
<a name="BKMK_PrivacyNotice"></a>   

## Privacy notices  
 [!INCLUDE[cc_privacy_crm_gcc_solution_import](../../includes/cc-privacy-crm-gcc-solution-import.md)]  
  
 [!INCLUDE[cc_privacy_crm_customizations](../../includes/cc-privacy-crm-customizations.md)]  
  
### See also  
[Create a solution](create-solution.md) <br />
[Understand model-driven app components](../model-driven-apps/model-driven-app-components.md)


