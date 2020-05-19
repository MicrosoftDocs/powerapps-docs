---
title: "Use solutions in Power Apps | MicrosoftDocs"
description: "Learn how to use solution to create or customize apps"
ms.custom: ""
ms.date: 05/19/2020
ms.reviewer: matp
ms.service: powerapps
ms.topic: "article"
author: "caburk"
ms.assetid: 72bacfbb-96a3-4daa-88ff-11bdaaac9a3d
caps.latest.revision: 57
ms.author: "caburk"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Use solutions in Power Apps

 Within Power Apps, you can view a list of solutions by selecting **Solutions** in the left navigation. 

Additionally, you can perform these tasks: 
- **New solution**: To locate and work with just the components you’ve customized, create a solution and do all your customization there. Then, you can easily distribute your solution to other environments. More information: [Create a solution](create-solution.md) 
- **Import**: Import a solution into your environment. More information: [Import solutions](import-update-export-solutions.md) 
- **Open AppSource**: [Microsoft AppSource](https://appsource.microsoft.com/) is where you can go to get solutions tailored to your industry that work with the products you already use. 
- **Publish all customizations**: Publish all active customizations in your environment. 
- **Switch to classic**: Open the classic solution explorer. 
- **See history**: View details about solution operations over time, such as import, export, and uninstall. More information: [View the history of a solution](solution-history.md)

![Solutions area](media/solutions-area-tasks.png)

## Open and work in a solution.
From the **Solutions** area, select a solution to view all of its components. 
 
> [!div class="mx-imgBorder"]  
> ![Demo solution with all components](media/solution-all-items-list.PNG "Demo solution with all components")   
 You can browse through all the components in a solution by scrolling through the items. If there are more then 100 items in the list you can select **Load the next 100 items** to see more. 
 
> [!div class="mx-imgBorder"]  
> ![Load more components](media/load-more.PNG "Load more components")  

 ### Search and filter in a solution
  You can also search for a specific component by its name. 
 
> [!div class="mx-imgBorder"]  
> ![Search component](media/solution-search-box.png "Search component")  
 
 Or filter all items in the list by the component type.
  
> [!div class="mx-imgBorder"]  
> ![Filter component by type](media/solution-filter.PNG "Filter component by type")  
 

 ### Contextual commands
 As you select each component, the actions available in the command bar will change depending on the type of the component you have selected and if the solution is the default or a managed one. 
 
> [!div class="mx-imgBorder"]  
> ![Component specific commands](media/component-commands.png "Component specific commands")  
 
 When you don't select any component, the command bar will show actions applied to the solution itself. 
 
> [!div class="mx-imgBorder"]  
> ![Solution specific commands](media/solution-commands.PNG "Solution specific commands")  
 
 ### Create components in a solution
 With solutions that are unmanaged or the default one, you can use the **New** command to create different types of components. This takes you to a different create experience depending on the component type that you choose. After you finish creating the component, it will be added to the solution. 
 
> [!div class="mx-imgBorder"]  
> ![Create new component in a solution](media/solution-new-component.PNG "Create new component in a solution")  
 
 ### Add an existing component to a solution
 
 With solutions that are unmanaged and not the default one, you can use the **Add existing** command to bring in components that aren’t already in the solution.  
 
> [!div class="mx-imgBorder"]  
> ![Add existing component to a solution](media/solution-add-existing-component.PNG "Add existing component to a solution")  
  
 With solutions that are managed, only certain commands are available and you’ll see the message "You cannot directly edit the components within a managed solution." You’ll need to add it to another unmanaged solution that you’ve created to customize the component. The component might not be customizable. More information: [Managed properties](/power-platform/alm/managed-properties-alm)

When you add an existing entity, rather than select **Include all components** or **Include entity metadata**, use the **Select components** option to only add the entity components that have been updated. With solution segmentation, you export solution updates with selected entity assets, such as entity fields, forms, and views, rather than entire entities with all the assets. [Create a segmented solution with entity assets](use-segmented-solutions-patches-simplify-updates.md#create-a-segmented-solution-with-entity-assets)

 Many of the customizations you’ll want to do will involve entities. You can use the **Entity** filter to show a list of all the entities in the current solution that can be customized in some way. Once you drill into an entity, you can see the components that are part of the entity as shown with the account entity in the following screenshot. 
   
> [!div class="mx-imgBorder"]  
> ![Demo solution showing expanded account entity](media/solution-entity-account.png "Demo solution showing expanded account entity")  

## Known limitations

The following limitations apply to the use of canvas apps, flows, and custom connectors in solutions. 

- Connections require authentication and consent, which requires an interactive user session and therefore cannot be transported via solutions. After importing your solution, play the app to authenticate connections. You can also create the connections in the target environment prior to importing the solution. 
- Canvas app button triggered flows must be created from an app already in a solution. Adding this type of flow from outside solutions is blocked.
  - The app and flow will not currently be connected in the target environment post deployment. First associate valid connections with the flow and activate the flow. Then edit the app and re-associate the flow to the button.
-	Canvas apps shared as co-owner to an Azure Active Directory (AAD) security group can't be added to solutions. Unshare the app before adding it to a solution.
-	Canvas apps won't display in the classic solution explorer. Use the modern experience. There are no plans for them to be added to classic solution explorer. 
- Database operations such as backup, restore, and copy are not supported for canvas apps and flows. These operations can corrupt canvas apps and flows.
- Deleting a managed solution does not rollback to a different canvas app version. Instead, all versions of the app are deleted.
- Importing a solution containing a flow will not automatically create or associate required connections. The flow must be edited to fix the connections.
  - If using managed solutions, this creates an active customization in the unmanaged layer. Therefore subsequent solution updates to the flow will not be reflected. 
- Flows created from solutions will not be displayed in the "Team Flows" list. They must be accessed through a solution. 
- Button triggered flows are not available in solutions.
- Flows triggered from Microsoft 365 applications such as Excel are not available in solutions.
- Flows that connect to SharePoint are not available in solutions.
- Flows in solutions don't support delegated authentication. For example, access to a flow is not automatically granted based on having access to the SharePoint list the flow was created from.
- Custom connectors created outside solutions cannot be added to solutions at this time.


 For details about customizing the individual components in a solution, see the following topics:  
  
-   For entity, entity relationships, field and message customizations, see [Metadata](create-edit-metadata.md).  
  
-   For entity forms see [Forms](../model-driven-apps/create-design-forms.md).  
  
-   For processes, see [Processes](../model-driven-apps/guide-staff-through-common-tasks-processes.md).  
  
-   For business rules, see [Business Rules](../model-driven-apps/create-business-rules-recommendations-apply-logic-form.md).  
