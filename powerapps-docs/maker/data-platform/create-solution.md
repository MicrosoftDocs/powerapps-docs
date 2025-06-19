---
title: "Create a solution in Power Apps | MicrosoftDocs"
description: "Learn how to create a solution in Power Apps"
ms.custom: ""
ms.date: 06/11/2025
ms.reviewer: ""
ms.topic: "how-to"
author: "Mattp123"
ms.assetid: e21a4876-08b4-417a-a644-c577a27c5cf1
caps.latest.revision: 12
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Create a solution

To locate and work with just the components you’ve customized, create a solution and do all your customization there. Then, always remember to work in the context of the custom solution as you add, edit, and create components. This makes it easy to export your solution so that it can be backed up or imported to another environment. 

> [!NOTE]
> For information about implementing healthy application lifecycle management (ALM) using solutions, see the [Power Platform ALM guide](/power-platform/alm).
  
To create a solution:   
1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left navigation. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
  
2.  Select **New solution** and then complete the required columns for the solution.
  
    |Field|Description|  
    |-----------|-----------------|  
    |**Display Name**|The name shown in the list of solutions. You can change this later.|  
    |**Name**|The unique name of the solution. Must only contain letters, numbers, and underscores. The name is generated from the allowed characters from the value you enter in the **Display Name** column. You can edit this before you save the solution, but after you save the solution, you can’t change it.|  
    |**Publisher**|You can select the default publisher or create a new publisher. We recommend that you create a publisher for your organization to use consistently across your environments where you'll use the solution. See [Solution publisher](#solution-publisher) later in this article. |  
    |**Version**|Enter a number for the version of your solution. This is only important if you export your solution. The version number is included in the file name when you export the solution.|  
  
3.  Select **Save**.  
  
 After you save the solution, you might wish to add information to columns that aren’t required. These steps are optional. Use the **Description** column to describe the solution and choose an HTML web resource as a **Configuration Page** for the solution. The configuration page is typically used by independent software vendors (ISVs) who distribute solutions. When this is set, a new **Configuration** node appears below the **Information** node to display this web resource. Developers use this page to include instructions or controls to allow you to set configuration data or launch their solution.  
  
<a name="BKMK_AddSolutionComponents"></a>

## Add solution components

After you create your solution, it won’t contain any solution components. You can create new components to be added to the solution or add existing components to your new solution.
 
### Create components in a solution

You can use the **New** command to create different types of components. Selecting **New** takes you to a different create experience depending on the component type that you choose. After you finish creating the component, it's added to the solution.
 
> [!div class="mx-imgBorder"]  
> ![Create new component in a solution.](media/solution-new-component.PNG "Create new component in a solution")  
 
### Add an existing component to a solution
 
With solutions that are unmanaged and not the default one, you can use the **Add existing** command to bring in components that aren’t already in the solution.  
 
> [!div class="mx-imgBorder"]  
> ![Add existing component to a solution.](media/solution-add-existing-component.PNG "Add existing component to a solution")  

> [!NOTE]
> The list of existing components will be different depending on the version and solutions imported in your environment. 
  
When you add an existing table, the best practice is to only add the table assets that were updated in your solution. With solution segmentation, you export solution updates with selected table assets, such as table columns, forms, and views, rather than entire tables with all the assets. This avoids unnecessary layers that hinder other solutions from being effective and unnecessary dependencies on other solutions. The system automatically selects **Include all objects** if the table is unmanaged, and **Include table metadata** if there's an unmanaged layer on the table. The system also preselects the table assets that are unmanaged or have unmanaged customizations automatically you can select the **Select objects** link to review that selection before select **Add* to complete the process. More information: [Create a segmented solution with table assets](#create-a-segmented-solution-with-table-assets)

Many of the customizations you’ll want to do involve tables. You can use the **table** filter to show a list of all the tables in the current solution that can be customized in some way. Once you drill into a table, you can see the components that are part of the table as shown with the account table in the following screenshot. 
   
> [!div class="mx-imgBorder"]  
> ![Demo solution showing expanded account table.](media/solution-entity-account.png "Demo solution showing expanded account table")  
  
## Publish changes 

When you make unmanaged changes in an environment, some components, such as forms, tables, model-driven apps, site maps, and views are saved in an unpublished state. The publish action promotes these changes to an active state and makes them available to end users and for export. 
 
### Publish your customizations

1.  Select **Solutions** from the left navigation. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

2.  Select the solution that you want to publish to open it.

3.  From the list of commands, select **Publish all customizations**.  

![Publish all customizations.](media/publish-all-customizations.PNG "Publish all customizations")  
  
> [!IMPORTANT]
>  Preparing customizations may take some time. If you see a message that the browser page has become unresponsive, wait for the page to become responsive, and don't close it.  

## Solution publisher

Every app you create or customization you make is part of a solution. Every solution has a publisher. You specify the publisher when you create a solution. 

The solution publisher indicates who developed the app. For this reason, you should create a solution publisher that is meaningful. You can view the solution publisher for a solution by selecting **Settings** from the **Solutions** area in Power Apps. For more information about the solution publisher, see [Solution publisher](/power-platform/alm/solution-concepts-alm#solution-publisher) in the Power Platform ALM guide.

> [!NOTE]
> The **Common Data Services Default Solution** is associated with the **Microsoft Dataverse Default Publisher**. The default customization prefix will be randomly assigned for this publisher, for example it could be `cr8a3`. This means that the name of every new item of metadata created for your organization will have this prepended to the names used to uniquely identify the items.

### Create a solution publisher

1.	In [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
2.	On the command bar, select **New solution**, in the right pane select the **Publisher** drop down list, and then select **+ Publisher**. 
    > [!div class="mx-imgBorder"] 
    > <img src="media/create-new-pubisher.png" alt="Create a new publisher" height="738" width="400">
3.	In the **New Publisher** form, enter the required and optional information: 
   - **Display Name**. Enter the display name for the publisher. 
   - **Name**. Enter the unique name for the publisher. 
   - **Prefix**. Enter the publisher prefix you want. 
   -	**Option Value Prefix**. This column generates a number based on the publisher prefix. This number is used when you add options to choices and provides an indicator of which solution was used to add the option. 
   - **Contact Details**. Optionally, you can add contact and address information.
4. Select **Save and Close**.

> [!NOTE]
> Don't use _upgrade as part of the solution name.  _upgrade is an internal reserved word for the solution [upgrade  process](/power-apps/maker/data-platform/update-solutions#apply-the-upgrade-or-update-in-the-target-environment). 

### Change a solution publisher

You can change a solution publisher for an unmanaged solution by following these steps:
1.	In [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions**, select **…** next to the solution you want, and then select **Settings**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
2.	In the **Solution settings** pane, select **Edit publisher**. 
3.	Edit the **Display name** and **Prefix** columns to the values you want. The **Option Value Prefix** column generates a number based on the publisher prefix. This number is used when you add options to choices and provides an indicator of which solution was used to add the option. 
4.	In addition to the prefix, you can also change the solution publisher display name, contact information, and address in the **Contact Details** section. 
5.	Select **Save and Close**.

## Create a segmented solution

Use solution segmentation so that you only include table components that are updated when you distribute solution updates. More information: [Use segmented solutions](/power-platform/alm/segmented-solutions-alm) in the Power Platform ALM guide

### Create a segmented solution with table assets

To create a segmented solution, start with creating an unmanaged solution and add only the components that you've updated. The wizard-like setup takes you step by step through the process of adding table assets. 

For example, imagine that you've created a new custom table that doesn't exist in any other environment named *Custom table* and also added a new column named *topten* for the account table. To create a segmented solution, follow these steps. 
  
1. Go to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and then select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
  
2.  Select **New solution** and create a solution. Enter information in the required columns. Select **Create**.  
  
3.  Open the solution you created. On the command bar, select **Add Existing**, and then select **Entity**.  
  
4.  In the **Add existing entities** pane, select one or more tables you want to add to the solution. For example, select **Account** and **Custom table**. Select **Next**.  

5.  In the **Select Entities** pane, you can choose from the assets to include: 
    - **Include all components**. This option includes all components *and* metadata associated with the table. It can include other tables or table components such as business process flows, reports, connections, and queues. 
    - **Include entity metadata**. This option includes *only* the metadata associated with the table. Metadata includes the table attributes, such as auditing, duplicate detection, or change tracking. 
    - **Select components**. This option lets you individually select each component that’s associated with the table, such as columns, relationships, business rules, views, forms, and charts. 
    - Don't include any components. 

      For this example, because *Custom table* has never been imported into the target environment, next to **Custom table** select **Include all components**. Under **Account**, choose **Select components**.  
      > [!div class="mx-imgBorder"] 
      > ![Add existing tables.](media/add-existing-entities1.png)
  
6.  Since only the *topten* custom column is new to the account  table, select **Top Ten**, and then select **Add**.  
     > [!div class="mx-imgBorder"] 
     > ![Select table components.](media/add-existing-entities2.png)

7. Select **Add** to add the components to the solution. 

### Create a segmented solution using solution explorer

The following illustrations provide an example of creating a segmented solution by choosing table assets from the `Account`, `Case`, and `Contact` tables.  

> [!NOTE]
> The case table is included with some Dynamics 365 applications, such as Dynamics 365 Customer Service. 
  
Start by opening an unmanaged solution you created. Choose the **table** component.  

 > [!div class="mx-imgBorder"] 
 > ![Add existing resources.](media/solution-segmentation-add-existing-resources-admin.png "Add existing resources.")  
  
 Then, select the solution components.  
  
 ![Select solution's components.](media/solution-segmentation-select-components-admin.png "Select solution's components.")  
  
Follow the wizard. In Step 1, starting in alphabetical order, select the assets for the first table, the `Account` table, as shown here.  
  
 ![Start the wizard.](media/solution-segmentation-wizard-starts-admin.png "Start the wizard.")  
  
 Open the **Fields** tab and select the **Account Number** column.  
  
 ![Select the Account table assets.](media/solution-segmentation-select-account-assets-admin.png "Select the Account table assets.")  
  
 In Step 2, for the **Case** table, add all assets.  
  
 ![Select the Case table assets.](media/solution-segmentation-select-case-assets-admin.png "Select the Case table assets.")  
  
 In Step 3, add the **Anniversary** column for the **Contact** table.  
  
 ![Select the Contact table assets.](media/solution-segmentation-select-contact-assets-admin.png "Select the Contact table assets.")  
  
 As a result, the segmented solution that’s created contains three tables, `Account`, `Case`, and `Contact`. Each table contains only the assets that were chosen.  
  
 > [!div class="mx-imgBorder"] 
 > ![Solution with tables.](media/solution-segmentation-solution-entities-admin.png "Solution with tables.")

## Delete a solution

Because there are two different types of solutions, managed and unmanaged, the behavior for deleting each type of solution is different.

The solution you want to delete might have components that have dependencies on other components. These dependencies must be removed before you can delete the component. More information: [View dependencies for a component in Power Apps](view-component-dependencies.md)

### Delete a managed solution

Deleting a managed solution removes (uninstalls) *all* the components within the solution. Additionally, *all* associated data are also deleted.

> [!CAUTION]
> Because all components within the solution and all associated data is deleted, use caution when you delete a managed solution.

### Delete an unmanaged solution

Deleting an unmanaged solution deletes the solution container but doesn't delete any of the unmanaged components within. Any data associated also remains. Each unmanaged component must be individually deleted to remove all components within the unmanaged solution.

### Delete a managed or unmanaged solution

> [!CAUTION]
> Before you delete a solution, make sure you understand the consequences. Once a solution is deleted it can't be restored. More information: [Delete a managed solution](#delete-a-managed-solution) and [Delete an unmanaged solution](#delete-an-unmanaged-solution)

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Select **Solutions** on the left navigation pane, and then select (don't open) the solution you want to delete in the **Solutions** list.
1. Select **Delete** on the command bar.

## Limitations

- Solution size is limited to 95 MB.
- Number of solutions is limited by Microsoft Dataverse capacity.
- Number of objects in a solution is limited by Dataverse capacity.

### See also

 [Use solutions](./solutions-overview.md) <br />
[For developers: Create, export, or import an unmanaged solution](/power-platform/alm/solution-api#create-export-or-import-an-unmanaged-solution)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
