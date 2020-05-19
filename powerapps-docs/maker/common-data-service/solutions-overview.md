---
title: "Work with solutions in Power Apps | MicrosoftDocs"
description: "Learn how solutions are distributed"
ms.custom: ""
ms.date: 05/19/2020
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
   
# Solutions overview  

In Power Apps, solutions are leveraged to transport apps and components from one environment to another or to apply a set of customizations to existing apps. A solution can contain one or more apps as well as other components such as site maps, entities, processes, web resources, option sets, and more.  You can get a solution from [AppSource](https://appsource.microsoft.com/) or from an independent software vendor (ISV).
  
More information: [Solutions concepts](/power-platform/alm/solution-concepts-alm)
  
> [!NOTE]
>  If you’re an ISV creating an app that you will distribute, you’ll need to use solutions. For more information about using solutions, see [Developer Guide: Introduction to solutions](/powerapps/developer/common-data-service/introduction-solutions).  -->
  
## Unmanaged and managed solutions
There are two types of solutions: *managed* and *unmanaged*. A managed solution is a completed solution that is intended to be distributed and installed.

- You cannot edit the components of a managed solution.
- You cannot export a managed solution.
- You can add unmanaged customizations to components of a managed solution. When you do this, you create a dependency between your unmanaged customizations and the managed solution. When a dependency exists, the managed solution cannot be uninstalled until you remove the dependency.
- When a managed solution is deleted (uninstalled), all the customizations and extensions included with it are removed.

> [!IMPORTANT]
> When you uninstall a managed solution, the following data is lost: data stored in custom entities that are part of the managed solution and data stored in custom attributes that are part of the managed solution on other entities that are not part of the managed solution.

An unmanaged solution is one that is still under development or isn't intended to be distributed. 

- While a solution is unmanaged, you can continue to add and remove components to it.
- You can export an unmanaged solution to transport unmanaged customizations from one environment to another.
- When an unmanaged solution is deleted, only the solution container of any customizations included in it is deleted. All the unmanaged customizations remain in effect and belong to the default solution.
- When the unmanaged solution is complete and you want to distribute it, export it as a managed solution.

> [!NOTE]
>  You cannot import a managed solution into the same environment that contains the originating unmanaged solution. To test a managed solution, you need a separate environment to import it into.

## The default solutions


## Solution dependencies  
Because of the way that managed solutions are layered, some managed solutions can be dependent on solution components in other managed solutions. Some solution publishers will take advantage of this to build solutions that are modular. You may need to install a “base” managed solution first and then you can install a second managed solution that will further customize the components in the base managed solution. The second managed solution depends on solution components that are part of the first solution.  
  
The system tracks these dependencies between solutions. If you try to install a solution that requires a base solution that isn’t installed, you won’t be able to install the solution. You will get a message saying that the solution requires another solution to be installed first. Similarly, because of the dependencies, you can’t uninstall the base solution while a solution that depends on it is still installed. You have to uninstall the dependent solution before you can uninstall the base solution.  


<!-- Move this to ALM guide  ## View and edit solution components
A component represents something that you can potentially customize. Anything that can be included in a solution is a component. To view the components included in a solution, open the solution you want. The components are listed in the **Components** list. Notice that you can't edit components contained in a managed solution. 

> [!div class="mx-imgBorder"] 
> ![Components in solution](media/components-in-solution.png "Components in solution") 

To view a list of component types that can be added to any solution, see [ComponentType Options](../../developer/common-data-service/reference/entities/solutioncomponent.md#componenttype-options). 

For more information about solutions, see these articles: 
- [Solutions concepts](/power-platform/alm/solution-concepts-alm)
- [Solution layers](/power-platform/alm/solution-layers-alm)
- [Understand how managed solutions are merged](/power-platform/alm/how-managed-solutions-merged)
- [Use a solution to customize](/power-platform/alm/use-solutions-for-your-customizations)
- [Managed properties](/power-platform/alm/managed-properties-alm)
- [Use segmented solutions](/power-platform/alm/segmented-solutions-alm)
- [Update a solution](/power-platform/alm/update-solutions-alm)


Some components are nested within other components. For example, an entity contains forms, views, charts, fields, entity relationships, messages, and business rules. Each of those components requires an entity to exist. A field can’t exist outside of an entity. We say that the field is dependent on the entity.   
  
 Some components are nested within other components. For example, an entity contains forms, views, charts, fields, entity relationships, messages, and business rules. Each of those components requires an entity to exist. A field can’t exist outside of an entity. We say that the field is dependent on the entity. There are actually twice as many types of components as shown in the preceding list, but most of them are not nested within other components and not visible in the application.  
  
 The purpose of having components is to keep track of any limitations on what can be customized using managed properties and all the dependencies so that it can be exported, imported, and (in managed solutions) deleted without leaving anything behind.  -->

<!--  
<a name="BKMK_ManagedAndUnmanagedSolutions"></a>   

## Managed and unmanaged solutions  
There are **managed** and **unmanaged** solutions. A **managed** solution can't be modified and can be uninstalled after it is imported. All the components of that solution are deleted by uninstalling the solution.  
  
When you import an **unmanaged** solution, you add all the components of that solution into your environment. You can’t delete the components by uninstalling the solution.  
  
When you import an **unmanaged** solution that contains components that you have already customized, your customizations will be overwritten by the customizations in the imported unmanaged solution. You can’t undo this.  
  
> [!IMPORTANT]
>  Install an unmanaged solution only if you want to add all the components to your environment and overwrite any existing customizations.  
  
Even if you don’t plan on distributing your apps or customizations, you should create and use an unmanaged solution to have a separate view that only includes those parts of the application that you have customized. Whenever you customize something, just add it to the unmanaged solution that you created.  
  
To create a **managed** solution, you choose the **As managed** option when you export the solution. When you create a managed solution, you can’t import it back into the same environment you used to create it. You can only import it into a different environment.  
  
<a name="BKMK_HowSolutionsAreApplied"></a>   

### How solutions are applied  
All solutions are evaluated as layers to determine what your app will actually do. The following diagram shows how managed and unmanaged solutions are evaluated and how changes in them will appear in your environment.  
  
![Solution layering](media/solution-layering.png "Solution layering")  
  
Starting from the bottom and working up to top:  
  
**System Solution**  
The system solution is like a managed solution that every environment has. The system solution is the definition of all the out-of-the box components in the system.  
  
**Managed Solutions**  
Managed solutions can modify the system solution components and add new components. If multiple managed solutions are installed, the first one installed is below the managed solution installed later. This means that the second solution installed can customize the one installed before it. When two managed solutions have conflicting definitions, the general rule is "Last one wins." If you uninstall a managed solution, the managed solution below it takes effect. If you uninstall all managed solution, the default behavior defined within the system solution is applied.  
  
**Unmanaged Customizations**  
Unmanaged customizations are any change you have made to your environment through an unmanaged solution. The system solution defines what you can or can't customize by using managed properties. Publishers of managed solutions have the same ability to limit your ability to customize solution components that they add in their solution. You can customize any of the solution components that do not have managed properties that prevent you from customizing them.  
  
**Application Behavior**  
The application or runtime behavior is what you actually see in your environment. The default system solution plus any managed solutions, plus any unmanaged customizations you have applied.  
  
<a name="BKMK_ManagedProperties"></a>   

## Managed properties  
Some components can’t be customized. These components in the system solution have metadata that prevents you from customizing them. These are called **managed properties**. The publisher of a managed solution can also set the managed properties to prevent you from customizing their solution in ways they don’t want you to.  
  
<a name="BKMK_Dependencies"></a>   
 
## Solution publisher 

The **Common Data Services Default Solution** is associated with the **Common Data Service Default Publisher**. The default customization prefix will be randomly assigned for this publisher, for example it could be `cr8a3`. This means that the name of every new item of metadata created for your organization will have this prepended to the names used to uniquely identify the items. 

We recommend that you change the solution publisher prefix so that it will be more meaningful. More information: [Change the solution publisher prefix](change-solution-publisher-prefix.md) -->
  
### Next steps  
[Use solutions in Power Apps](use-solution-explorer.md) <br/>

 
