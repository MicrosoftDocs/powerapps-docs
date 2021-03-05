---
title: "Solutions in Power Apps | MicrosoftDocs"
description: "Provides an overview of solutions in Power Apps"
ms.custom: ""
ms.date: 09/15/2020
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
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

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Solutions are used to transport apps and components from one environment to another or to apply a set of customizations to existing apps. A solution can contain one or more apps as well as other components such as site maps, tables, processes, web resources, choices, flows, and more.

Solutions are the mechanism for implementing application lifecycle management (ALM) in Power Apps and other Power Platform products, such as Power Automate. For detailed information about the solution concepts and how solutions are used for application lifecycle management, see [Overview of ALM with Microsoft Power Platform](/power-platform/alm/overview-alm) in the Power Platform ALM guide.

This section will focus on the **manual** tasks that app makers need to perform while working with solutions in Power Apps.

## Get started: solution concepts

Before you work with solutions, it's important that you get acquainted with the following solution concepts:
- Two types of solutions (managed and unmanaged)
- Solution components
- Lifecycle of a solution (create, update, upgrade, and patch a solution)
- Solution publisher
- Solution and solution component dependencies

For detailed information, see [Solution concepts](/power-platform/alm/solution-concepts-alm) in the Power Platform ALM guide.

## Default solutions

Power Apps provides you the following default [unmanaged](/power-platform/alm/solution-concepts-alm) solutions:

- **Common Data Service Default Solution**. This solution is available for makers to use by default for their customizations in an environment. The Common Data Service Default Solution is useful when you want to evaluate or learn Power Apps. However, we recommend that app makers work in their own unmanaged solutions. 
- **Default Solution**. This is a special solution that contains all components in the system. The default solution is useful for discovering all the components and configurations in your system.

However, we recommend that you create a solution to manage your customizations. More information: [Use a solution to customize](/power-platform/alm/use-solutions-for-your-customizations) in the Power Platform ALM guide.

<!--  
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
The application or runtime behavior is what you actually see in your environment. The default system solution plus any managed solutions, plus any unmanaged customizations you have applied. --> 

## Managed properties
You can control which of your managed solution components are customizable by using managed properties. We recommend that you set managed properties so that your managed components can’t be modified. This helps protect your solution from modifications that may cause it to break after it's imported into another environment, such as test or production. 

More information: [Managed properties in the Power Platform](/power-platform/alm/managed-properties-alm)

## Work with solutions in Power Apps

 Within Power Apps, you can view a list of solutions by selecting **Solutions** in the left navigation. You can perform these solution tasks: 
- **New solution**: To locate and work with just the components you’ve customized, create a solution and do all your customization there. Then, you can easily distribute your solution to other environments. More information: [Create a solution](create-solution.md) 
- **Import**: Import a solution into your environment. More information: [Import solutions](import-update-export-solutions.md) 
- **Open AppSource**: [Microsoft AppSource](https://appsource.microsoft.com/) is where you can go to get solutions tailored to your industry that work with the products you already use. 
- **Publish all customizations**: Publish all active customizations in your environment. 
- **Switch to classic**: Open the classic solution explorer. 
- **See history**: View details about solution operations over time, such as import, export, and uninstall. More information: [View the history of a solution](solution-history.md)

    > [!div class="mx-imgBorder"]
    > ![Solutions area](media/solutions-area-tasks.png)

From the **Solutions** area, select a solution to view all of its components. 
 
> [!div class="mx-imgBorder"]  
> ![Demo solution with all components](media/solution-all-items-list.PNG "Demo solution with all components")   
 
 You can browse through all the components in a solution by scrolling through the items. If there are more then 100 items in the list you can select **Load the next 100 items** to see more. 
 
> [!div class="mx-imgBorder"]  
> ![Load more components](media/load-more.PNG "Load more components")  

 ## Search and filter in a solution
  You can also search for a specific component by its name. 
 
> [!div class="mx-imgBorder"]  
> ![Search component](media/solution-search-box.png "Search component")  
 
 Or filter all items in the list by the component type.
  
> [!div class="mx-imgBorder"]  
> ![Filter component by type](media/solution-filter.PNG "Filter component by type")  
 

 ## Contextual commands
 As you select each component, the actions available in the command bar will change depending on the type of the component you have selected and if the solution is the default or a managed one. 
 
> [!div class="mx-imgBorder"]  
> ![Component specific commands](media/component-commands.png "Component specific commands")  
 
 When you don't select any component, the command bar will show actions applied to the solution itself. 
 
> [!div class="mx-imgBorder"]  
> ![Solution specific commands](media/solution-commands.PNG "Solution specific commands")  
 
With solutions that are unmanaged or the default one, you can use the **New** or **Add Existing** command to create or add different types of components. More information: [Add solution components](create-solution.md#add-solution-components)
 
> [!NOTE]
> You can't add components to a managed solution. When you try to, you’ll see the following message:<br/>
`"You cannot directly edit the components within a managed solution. You’ll need to add it to another unmanaged solution that you’ve created to customize the component. The component might not be customizable."`


## Known limitations

The following limitations apply to the use of canvas apps, flows, and custom connectors in solutions. 

- Canvas app instant flows must be created from an app already in a solution. Adding this type of flow from outside solutions is blocked.
  - The app and flow will not currently be connected in the target environment after deployment. First associate valid connections with the flow and activate the flow. Then edit the app and re-associate the flow to the button.
-	Canvas apps won't display in the classic solution explorer. Use the modern experience. There are no plans for them to be added to classic solution explorer. 
- Flows created from solutions will not be displayed in the "Team Flows" list. They must be accessed through a solution. 
- You can’t add an instant flow into a solution when the following are true:
   - The flow was created outside of a solution.
   - The flow trigger is set to manual.
- Flows triggered from Microsoft 365 applications such as Excel are not available in solutions.
- Flows in solutions don't support delegated authentication. For example, access to a flow is not automatically granted based on having access to the SharePoint list the flow was created from.
- Custom connectors created outside solutions cannot be added to solutions at this time.

For details about customizing the individual components in a solution, see the following topics:  
  
-   For table, table relationships, column and message customizations, see [Metadata](create-edit-metadata.md).  
  
-   For table forms, see [Forms](../model-driven-apps/create-design-forms.md).  
  
-   For processes, see [Processes](../model-driven-apps/guide-staff-through-common-tasks-processes.md).  
  
-   For business rules, see [Business Rules](../model-driven-apps/create-business-rules-recommendations-apply-logic-form.md).
 
 
### Next steps  
[Create a solution](create-solution.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]