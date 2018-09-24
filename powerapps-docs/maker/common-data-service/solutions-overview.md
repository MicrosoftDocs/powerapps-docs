---
title: "Work with solutions in PowerApps | MicrosoftDocs"
description: "Learn how solutions are distributed"
ms.custom: ""
ms.date: 06/21/2018
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
ms.assetid: ece68f5f-ad40-4bfa-975a-3e5bafb854aa
caps.latest.revision: 55
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

<a name="BKMK_Solutions"></a>   
# Solutions overview  

 Solutions exist so that a model-driven app can be purchased, shared, or otherwise transported from one organization to another. You can get solutions from [AppSource](https://appsource.microsoft.com/) or from an independent software vendor (ISV). A solution is a file that you can import in to an environment as an app or to apply a set of customizations to an existing app.  
  
More information: [Whitepaper: Patterns and Principles for Solution Builders](http://go.microsoft.com/fwlink/p/?LinkID=533946)  
  
> [!NOTE]
>  If you’re an ISV creating an app that you will distribute, you’ll need to use solutions. For more information about using solutions, see [Package and distribute extensions using solutions](https://msdn.microsoft.com/library/gg334530.aspx).  
  
 If you are just interested in creating PowerApps apps for organizational use or customizing Dynamics 365, here is what you need to know about solutions:  
  
-   Creating solutions is optional. You can build or customize apps in your PowerApps environment directly without ever creating a solution.  
  
-   When you customize the PowerApps environment directly, you work with a special solution called the **Common Data Services Default Solution**. This solution contains all the components in your system.  
  
-   You can export your default solution to create a backup of the customizations you have defined in your organization. This is good to have in a worst case scenario.  
  
<a name="BKMK_SolutionComponents"></a>   
### Solution components  
 A solution component represents something that you can potentially customize. Anything that can be included in a solution is a solution component. The following is a list of solution components that you can view in a solution:  
  
-   Application Ribbon  

-   App 
  
-   Article Template  
  
-   Business Rule  
  
-   Chart  
  
-   Connection Role  
  
-   Contract Template  
 
-   Custom Control
  
-   Dashboard  
  
-   Email Template  
  
-   Entity  
  
-   Entity Relationship  
  
-   Field  
  
-   Field Security Profile  
  
-   Form  
  
-   Mail Merge Template  
  
-   Message  
  
-   Option Set  
  
-   Plug-in Assembly  
  
-   Process  
  
-   Sdk Message Processing Step  
  
-   Security Role  
  
-   Service Endpoint  
  
-   Site Map  

-   Virtual Entity Data Provider

-   Virtual Entity Data Source
  
-   Web Resource  
  
 Most solution components are nested within other solution components. For example, an entity contains forms, views, charts, fields, entity relationships, messages, and business rules. Each of those solution components requires an entity to exist. A field can’t exist outside of an entity. We say that the field is dependent on the entity. There are actually twice as many types of solution components as shown in the preceding list, but most of them are not visible in the application.  
  
 The purpose of having solution components is to keep track of any limitations on what can be customized using Managed properties and all the solution dependencies so that it can be exported, imported, and (in managed solutions) deleted without leaving anything behind.  
  
<a name="BKMK_ManagedAndUnmanagedSolutions"></a>   
### Managed and unmanaged solutions  
 A **managed** solution can be uninstalled after it is imported. All the components of that solution are removed by uninstalling the solution.  
  
 When you import an **unmanaged** solution, you add all the components of that solution into your default solution. You can’t remove the components by uninstalling the solution.  
  
 When you import an **unmanaged** solution that contains solution components that you have already customized, your customizations will be overwritten by the customizations in the unmanaged solution. You can’t undo this.  
  
> [!IMPORTANT]
>  Install an unmanaged solution only if you want to add all the components to your default solution and overwrite any existing customizations.  
  
 Even if you don’t plan on distributing your solution, you might want to create and use an unmanaged solution to have a separate view that only includes those parts of the application that you have customized. Whenever you customize something, just add it to the unmanaged solution that you created.  
  
 You can only export your Default Solution as an unmanaged solution.  
  
 To create a **managed** solution, you choose the managed solution option when you export the solution. If you create a managed solution, you can’t import it back into the same organization you used to create it. You can only import it into a different organization.  
  
<a name="BKMK_HowSolutionsAreApplied"></a>   
### How solutions are applied  
 All solutions are evaluated as layers to determine what your app will actually do. The following diagram shows how managed and unmanaged solutions are evaluated and how changes in them will appear in your organization.  
  
 ![Solution layering](media/solution-layering.png "Solution layering")  
  
 Starting from the bottom and working up to top:  
  
 **System Solution**  
 The system solution is like a managed solution that every organization has. The system solution is the definition of all the out-of-the box components in the system.  
  
 **Managed Solutions**  
 Managed solutions can modify the system solution components and add new components. If multiple managed solutions are installed, the first one installed is below the managed solution installed later. This means that the second solution installed can customize the one installed before it. When two managed solutions have conflicting definitions, the general rule is “Last one wins”. If you uninstall a managed solution, the managed solution below it takes effect. If you uninstall all managed solution, the default behavior defined within the system solution is applied.  
  
 **Unmanaged Customizations**  
 Unmanaged customizations are any change you have made to your organization through an unmanaged solution. The system solution defines what you can or can't customize by using managed properties. Publishers of managed solutions have the same ability to limit your ability to customize solution components that they add in their solution. You can customize any of the solution components that do not have managed properties that prevent you from customization them.  
  
 **Application Behavior**  
 This is what you actually see in your organization. The default system solution plus any managed solutions, plus any unmanaged customizations you have applied.  
  
<a name="BKMK_ManagedProperties"></a>   
### Managed properties  
 Some components can’t be customized. These components in the system solution have metadata that prevents you from customizing them. These are called **managed properties**. The publisher of a managed solution can also set the managed properties to prevent you from customizing their solution in ways they don’t want you to.  
  
<a name="BKMK_Dependencies"></a>   
### Solution dependencies  
 Because of the way that managed solutions are layered some managed solutions can be dependent on solution components in other managed solutions. Some solution publishers will take advantage of this to build solutions that modular. You may need to install a “base” managed solution first and then you can install a second managed that will further customize the components in the base managed solution. The second managed solution depends on solution components that are part of the first solution.  
  
 The system tracks these dependencies between solutions. If you try to install a solution that requires a base solution that isn’t installed, you won’t be able to install the solution. You will get a message saying that the solution requires another solution to be installed first. Similarly, because of the dependencies, you can’t uninstall the base solution while a solution that depends on it is still installed. You have to uninstall the dependent solution before you can uninstall the base solution.  
  
  
## Next steps  
[Import, update, and export solutions](import-update-export-solutions.md) <br/>
[Navigate to a specific solution](navigate-specific-solution.md)
 
