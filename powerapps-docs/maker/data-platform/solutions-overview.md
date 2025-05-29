---
title: Solutions in Power Apps
description: Provides an overview of solutions in Power Apps
ms.date: 05/29/2025
ms.reviewer: matp
ms.topic: overview
author: "Mattp123"
ms.assetid: ece68f5f-ad40-4bfa-975a-3e5bafb854aa
caps.latest.revision: 55
ms.subservice: dataverse-maker
ms.author: "caburk"
search.audienceType: 
  - maker
contributors: v-aangie
---
   
# Solutions in Power Apps overview  

Solutions are used to transport apps and components from one environment to another or to apply a set of customizations to existing apps. A solution can contain one or more apps as well as other components such as site maps, tables, processes, web resources, choices, flows, and more.

Solutions are the mechanism for implementing application lifecycle management (ALM) in Power Apps and other Power Platform products, such as Power Automate. 

> [!NOTE]
> To learn more about the solution concepts and how solutions are used for application lifecycle management, go to [Overview of ALM with Microsoft Power Platform](/power-platform/alm/overview-alm) in the Power Platform ALM guide.

This section focuses on the **manual** tasks that app makers need to perform while working with solutions in Power Apps.

## Get started: solution concepts

Before you work with solutions, it's important that you get acquainted with the following solution concepts:

- Two types of solutions (managed and unmanaged)
- Solution components
- Lifecycle of a solution (create, update, upgrade, and patch a solution)
- Solution publisher
- Solution and solution component dependencies

To learn more, go to [Solution concepts](/power-platform/alm/solution-concepts-alm) in the Power Platform ALM guide.

## Default solutions

Power Apps provides you with the following default [unmanaged](/power-platform/alm/solution-concepts-alm) solutions:

- **Common Data Service Default Solution**. This solution is available for makers to use by default for their customizations in an environment. The Common Data Service Default Solution is useful when you want to evaluate or learn Power Apps. However, we recommend that app makers work in their own unmanaged solutions. 
- **Default Solution**. This is a special solution that contains all components in the system. The default solution is useful for discovering all the components and configurations in your system.

However, we recommend that you create a solution to manage your customizations. More information: [Use a solution to customize](/power-platform/alm/use-solutions-for-your-customizations) in the Power Platform ALM guide.

## Managed properties

You can control which of your managed solution components are customizable by using managed properties. We recommend that you set managed properties so that your managed components can’t be modified. This helps protect your solution from modifications that might cause it to break after it's imported into another environment, such as test or production. 

More information: [Managed properties in the Power Platform](/power-platform/alm/managed-properties-alm)

## Work with solutions in Power Apps

 Within Power Apps, you can view a list of solutions by selecting **Solutions** in the left navigation. You can perform these solution tasks:

- **New solution**: To locate and work with just the components you’ve customized, create a solution and do all your customization there. Then, you can easily distribute your solution to other environments. More information: [Create a solution](create-solution.md) 
- **Import solution**: Import a solution into your environment. More information: [Import solutions](import-update-export-solutions.md) 
- **Open AppSource**: [Microsoft AppSource](https://appsource.microsoft.com/) is where you can go to get solutions tailored to your industry that work with the products you already use. 
- **Publish all customizations**: Publish all active customizations in your environment.
- **Set preferred solution**: Set your [preferred solution](preferred-solution.md) where all solution components are created in.
- **See history**: View details about solution operations over time, such as import, export, and uninstall. More information: [View the history of a solution](solution-history.md)
- **Connect to Git**: Source control integration allows development teams to sync solutions and solution objects across one or more Dataverse environments using an Azure DevOps Git repository. More information: [Overview of Git integration in Power Platform](/power-platform/alm/git-integration-overview)
- **Switch to classic**: Open the classic solution explorer.

When you select a solution, additional tasks become available in the command bar. These tasks include:

- **Edit**: Edit the solution properties, such as adding or removing solution components.
- **Delete**. Delete the selected solution.
- **Create a plan**. Use Plan designer to create a plan for your existing solution. Plan designer generates a detailed document that describes your solution. The plan covers the business problem, user requirements like user roles and stories, the data model, and technologies like apps. This feature saves time when you're trying to understand a solution's content and helps makers improve an existing solution. More information: [Create a plan from a solution](../plan-designer/create-plan-from-solution.md)
- **Export solution**: Export the solution to a file that can be imported into another environment. More information: [Export solutions](import-update-export-solutions.md#export-a-solution)
- **Deploy**. Use pipelines in Power Platform to deploy solutions to test and production environments. More information: [Overview of pipelines in Power Platform](/power-platform/alm/pipelines)
- **Solution checker**: Appears when you select a solution. Run or review results of [solution checker](use-powerapps-checker.md) for this solution.
- **Show dependencies**: Appears when you select a solution. [View solution dependencies](view-component-dependencies.md) for solutions that would block uninstall of this solution.
- **Set preferred solution**. Use the selected solution as your preferred solution. The preferred solution is where, if not already working in the context of a solution, all your solution components are maintained. More information: [Preferred solution](preferred-solution.md)
- **See history**. View details about solution operations over time, such as import, export, and uninstall. More information: [View the history of a solution](solution-history.md)
- **Publish to Catalog**: Publishes the solution to the catalog, making it available for other makers in your organization to use. This is useful for sharing solutions that you want others to be able to import and use in their environments. More information: [Catalog in Power Platform](catalog-overview.md)
- **Apply Upgrade**: Appears when you select a solution. [Apply a pending upgrade](update-solutions.md#apply-the-upgrade-or-update-in-the-target-environment) that has been initiated for a managed solution.

From the **Solutions** area, select a solution to view all of its objects.

:::image type="content" source="media/solution-all-items-list.png" alt-text="Example solution with all objects.":::

Browse through all the objects in a solution by scrolling through the items. If there are more than 100 items in the list, you can select **Load the next 100 items** to see more.

:::image type="content" source="media/load-more.png" alt-text="Load next 100 items.":::

Columns can be sorted and filtered by selecting the column header.

Column headers include:

- **Managed**: The solution object is from a managed solution. You can inspect the object by selecting the item and then select **Advanced** > **See solution layers**.
- **Customizable**: The component is available to be customized.
- **Customized**: This indicates that the object is an unmanaged object, or a managed object with an unmanaged customization layer.  You can use this column to quickly locate the unmanaged changes you have for components in the solution.
- **Owner**: If the solution object supports user and team ownership, the current owner is displayed.
- **Status**: If the solution object supports state management (on/off, enabled/disabled, active/inactive), the status is displayed.

> [!TIP]
> You can quickly locate all solution objects that are unmanaged or have unmanaged customizations by selecting the default solution and filtering on the **Customized** column.

## Search and filter in a solution

Search for a specific component by its name.
 
> [!div class="mx-imgBorder"]  
> ![Search component.](media/solution-search-box.png "Search component")  
 
 Or filter all items in the list by the component type.
  
> [!div class="mx-imgBorder"]  
> ![Filter component by type.](media/solution-filter.PNG "Filter component by type")  

 ## Contextual commands

 As you select each component, the actions available in the command bar changes depending on the type of the component you have selected and if the solution is the default or a managed one. 

> [!div class="mx-imgBorder"]  
> ![Component specific commands.](media/component-commands.png "Component specific commands")  

 When you don't select any component, the command bar shows actions applied to the solution itself. 
 
> [!div class="mx-imgBorder"]  
> ![Solution specific commands.](media/solution-commands.PNG "Solution specific commands")  

With solutions that are unmanaged or the default one, you can use the **New** or **Add Existing** command to create or add different types of components. More information: [Add solution components](create-solution.md#add-solution-components)

> [!NOTE]
> You can't add components to a managed solution. When you try to, you’ll get the following message:<br/>
`"You cannot directly edit the components within a managed solution. You’ll need to add it to another unmanaged solution that you’ve created to customize the component. The component might not be customizable."`

## Additional privileges required

Some components might require certain Dataverse privileges for users to run the component when the component is imported into the environment from a  solution.

### Flows

To use or run a flow from a canvas app that is included in a solution, you must have permissions to that flow through someone sharing ownership or run permissions. When an app in a solution is shared with a set of users, the flows must also be explicitly shared.

More information: [Security roles and privileges](/power-platform/admin/security-roles-privileges)

## Use pipelines in Power Platform to deploy solutions

Easily deploy solutions to test and production environments using pipelines in Power Platform. Once pipelines are in place, makers can initiate in-product deployments with a few clicks. Makers do so directly within their development environments. More information: [Overview of pipelines in Power Platform](/power-platform/alm/pipelines)

## Known limitations

The following limitations apply to the use of canvas apps, flows, and custom connectors in solutions.

- If you encounter a canvas app publishing error: **the app has connections to flows that are no longer in the environment**, remove any deleted flows from the app. Then save and publish the app.  
- Canvas apps shared with **Everyone** that go through environment backup and environment restore operations aren't shared with **Everyone** in the restored environment. Notice that the canvas app can be shared with a security group, and the app in the restored environment is shared with that security group.  
  
To learn more about customizing the individual components in a solution, go to the following articles:  
  
- For table, table relationships, column and message customizations, go to [Metadata](create-edit-metadata.md).  
- For table forms, go to [Forms](../model-driven-apps/create-design-forms.md).  
- For processes, go to [Processes](../model-driven-apps/guide-staff-through-common-tasks-processes.md).  
- For business rules, go to [Business Rules](../model-driven-apps/create-business-rules-recommendations-apply-logic-form.md).

## Troubleshooting solutions

For known issues and information about how to troubleshoot working with solutions, go to [Manage apps and solutions](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/unmanaged-active-layer-created-after-solution-import) in the Power Apps Troubleshooting documentation.

## Next step

[Create a solution](create-solution.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
