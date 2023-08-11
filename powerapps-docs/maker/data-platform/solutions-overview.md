---
title: "Solutions in Power Apps | MicrosoftDocs"
description: "Provides an overview of solutions in Power Apps"
ms.date: 05/04/2023
ms.reviewer: ""
ms.topic: overview
author: "Mattp123"
ms.assetid: ece68f5f-ad40-4bfa-975a-3e5bafb854aa
caps.latest.revision: 55
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
   
# Solutions overview  

Solutions are used to transport apps and components from one environment to another or to apply a set of customizations to existing apps. A solution can contain one or more apps as well as other components such as site maps, tables, processes, web resources, choices, flows, and more.

Solutions are the mechanism for implementing application lifecycle management (ALM) in Power Apps and other Power Platform products, such as Power Automate. 

> [!NOTE]
> For detailed information about the solution concepts and how solutions are used for application lifecycle management, see [Overview of ALM with Microsoft Power Platform](/power-platform/alm/overview-alm) in the Power Platform ALM guide.

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
    > ![Solutions area.](media/solutions-area-tasks.png)

From the **Solutions** area, select a solution to view all of its components. 
 
> [!div class="mx-imgBorder"]  
> ![Demo solution with all components.](media/solution-all-items-list.PNG "Demo solution with all components")   
 
 You can browse through all the components in a solution by scrolling through the items. If there are more then 100 items in the list you can select **Load the next 100 items** to see more. 
 
> [!div class="mx-imgBorder"]  
> ![Load more components.](media/load-more.PNG "Load more components")  

 ## Search and filter in a solution
  You can also search for a specific component by its name. 
 
> [!div class="mx-imgBorder"]  
> ![Search component.](media/solution-search-box.png "Search component")  
 
 Or filter all items in the list by the component type.
  
> [!div class="mx-imgBorder"]  
> ![Filter component by type.](media/solution-filter.PNG "Filter component by type")  
 

 ## Contextual commands

 As you select each component, the actions available in the command bar will change depending on the type of the component you have selected and if the solution is the default or a managed one. 
 
> [!div class="mx-imgBorder"]  
> ![Component specific commands.](media/component-commands.png "Component specific commands")  
 
 When you don't select any component, the command bar will show actions applied to the solution itself. 
 
> [!div class="mx-imgBorder"]  
> ![Solution specific commands.](media/solution-commands.PNG "Solution specific commands")  
 
With solutions that are unmanaged or the default one, you can use the **New** or **Add Existing** command to create or add different types of components. More information: [Add solution components](create-solution.md#add-solution-components)
 
> [!NOTE]
> You can't add components to a managed solution. When you try to, you’ll see the following message:<br/>
`"You cannot directly edit the components within a managed solution. You’ll need to add it to another unmanaged solution that you’ve created to customize the component. The component might not be customizable."`

## Additional privileges required

Some components may require certain Dataverse privileges for users to run the component when the component is imported into the environment from a  solution.

### Flows

To use or run a flow from a canvas app that is included in a solution, you must have permissions to that flow through someone sharing ownership or run permissions. When an app in a solution is shared with a set of users, the flows must also be explictly shared.

More information: [Security roles and privileges](/power-platform/admin/security-roles-privileges)

## Use pipelines in Power Platform to deploy solutions

Easily deploy solutions to test and production environments using pipelines in Power Platform. Once pipelines are in place, makers can initiate in-product deployments with a few clicks. Makers do so directly within their development environments. More information: [Overview of pipelines in Power Platform](/power-platform/alm/pipelines)

## Known limitations

The following limitations apply to the use of canvas apps, flows, and custom connectors in solutions. 

-	If you encounter a canvas app publishing error: **the app has connections to flows that are no longer in the environment**, remove any deleted flows from the app. Then save and publish the app.  
- Canvas apps shared with 'Everyone' that go through environment backup and environment restore operations aren't shared with 'Everyone' in the restored environment. Notice that, the canvas app can be shared with a security group and the app in the restored environment will be shared with that security group.  
- Canvas app instant flows must be created from an app already in a solution since adding this type of flow from outside solutions is blocked. 
   - Workaround for this limitation: Remove the trigger, replace with another trigger like recurrence, save the flow, add it into a solution, and then change the trigger as needed.
- Instant flows (flows that use a manual trigger) can't be added to a solution after the flow has been created. To include an instant flow in a solution, it must be created from the solution. To do this, from the solution select **New** > **Automation** > **Cloud flow** > **Instant**.
- The [Power Automate mobile app](/power-automate/mobile-manage-flows) does not currently support flows created in a solution. 
- The Flow action menu in [Power Apps Mobile](/powerapps/mobile/run-powerapps-on-mobile) and [Dynamics 365 for phones and tablets](/dynamics365/mobile-app/overview) does not currently support flows created in a solution. 
- Flows in solutions don't support delegated authorization. For example, access to a flow cannot be automatically granted based on having access to the SharePoint list the flow was created from. 
- Flows using [connectors](/connectors/connector-reference/) that are 'indexed' cannot be added into solutions. Indexing isn't supported for solution cloud flows yet. Indexing enables the quick retrieval of those flows to display in a menu or list. Indexed connectors include Power Automate instant (button) flows, Power Apps, Teams, SharePoint, Dynamics 365 Customer Voice, Microsoft Forms, legacy Dataverse connector, Dynamics 365, Excel Online, Microsoft Project, Azure IOT Central V2, and Project Online. 
   - Workarounds for this limitation: 
      - Edit the flow to remove the indexed connector triggers/actions, add it into a solution, and then change it back.
      - Create a new flow in a solution. 
- Flows triggered from Microsoft 365 applications such as Excel cannot see/show cloud flows in solutions since they use indexing.
      
For details about customizing the individual components in a solution, see the following topics:  
  
-   For table, table relationships, column and message customizations, see [Metadata](create-edit-metadata.md).  
  
-   For table forms, see [Forms](../model-driven-apps/create-design-forms.md).  
  
-   For processes, see [Processes](../model-driven-apps/guide-staff-through-common-tasks-processes.md).  
  
-   For business rules, see [Business Rules](../model-driven-apps/create-business-rules-recommendations-apply-logic-form.md).

## Troubleshooting solutions

For known issues and information about how to troubleshoot working with solutions, go to [Manage apps and solutions](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/unmanaged-active-layer-created-after-solution-import) in the Power Apps Troubleshooting documentation.

### Next steps

[Create a solution](create-solution.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
