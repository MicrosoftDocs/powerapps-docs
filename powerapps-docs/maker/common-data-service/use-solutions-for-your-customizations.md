---
title: "Use the default project to customize with PowerApps | MicrosoftDocs"
description: "Learn how to customize the default project"
ms.custom: ""
ms.date: 10/17/2018
ms.reviewer: ""
ms.service: "crm-online"
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

# Use the Common Data Services Default Solution  

> [!NOTE]
>  Projects are built on the [solution system](https://docs.microsoft.com/dynamics365/customer-engagement/developer/introduction-solutions) in the Dynamics platform. When using this functionality in PowerApps, you’ll see it described as a ‘project'. When using this functionality in Dynamics, you'll see it described as a 'solution'. 
  
 All PowerApps environments include the following projects.
-	Common Data Services Default Solution. This is a base project that is available for makers to use by default to for their customizations in an environment.
-	Default Solution. This is a special project that contains all customizations from all projects in an environment. 
-	Base Custom Controls Core. This project includes a core set of controls. Controls are used in user interface elements, such as fields, lists, and views. 

Notice that if you have installed or imported other applications or projects, additional projects may be available in the projects list. 

By default,  when you build or customize a model-driven app, you work with the project called Common Data Services Default Solution. You can open the Common Data Services Default Solution to view and edit the components that are contained in it. To do this, follow these steps.
 
1.  On the left navigation pane select **Projects**.

2.  In the list of projects, select **Common Data Services Default Solution**.
  
> [!TIP]
>  If you plan to distribute the applications your make, consider changing the publisher customization prefix. More information: [Project publisher prefix](change-solution-publisher-prefix.md).  
  
<a name="BKMK_PrivacyNotice"></a>   

## Privacy notices  
 [!INCLUDE[cc_privacy_crm_gcc_solution_import](../../includes/cc-privacy-crm-gcc-solution-import.md)]  
  
 [!INCLUDE[cc_privacy_crm_customizations](../../includes/cc-privacy-crm-customizations.md)]  
  
## See Also  
[Understand model-driven app components](../model-driven-apps/model-driven-app-components.md)
 <br/>
 [Whitepaper: Patterns and Principles for Solution Builders](http://go.microsoft.com/fwlink/p/?LinkID=533946)
