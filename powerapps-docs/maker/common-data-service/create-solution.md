---
title: "Create a solution in Power Apps | MicrosoftDocs"
description: "Learn how to create a solution in Power Apps"
ms.custom: ""
ms.date: 05/19/2020
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "Mattp123"
ms.assetid: e21a4876-08b4-417a-a644-c577a27c5cf1
caps.latest.revision: 12
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Create a solution

To locate and work with just the components you’ve customized, create a solution and do all your customization there. Then, always remember to work in the context of the custom solution as you add, edit, and create components. This makes it easy to export your solution so that it can be backed up or imported to another environment. 

> [!NOTE]
> For information about implementing healthy application lifecycle management (ALM) using solutions, see the [Power Platform ALM guide](/power-platform/alm).
  
To create a solution:   
1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left navigation. 
  
2.  Select **New solution** and then complete the required fields for the solution.
  
    |Field|Description|  
    |-----------|-----------------|  
    |**Display Name**|The name shown in the list of solutions. You can change this later.|  
    |**Name**|The unique name of the solution. This is generated using the value you enter in the Display Name field. You can edit this before you save the solution, but after you save the solution, you can’t change it.|  
    |**Publisher**|You can select the default publisher or create a new publisher. We recommend that you create a publisher for your organization to use consistently across your environments where you will use the solution. See [Solution publisher](#solution-publisher) later in this article. |  
    |**Version**|Enter a number for the version of your solution. This is only important if you export your solution. The version number will be included in the file name when you export the solution.|  
  
3.  Select **Save**.  
  
 After you save the solution, you may wish to add information to fields that aren’t required. These steps are optional. Use the **Description** field to describe the solution and choose an HTML web resource as a **Configuration Page** for the solution. The configuration page is typically used by ISVs who distribute solutions. When this is set, a new **Configuration** node appears below the **Information** node to display this web resource. Developers will use this page to include instructions or controls to allow you to set configuration data or launch their solution.  
  
<a name="BKMK_AddSolutionComponents"></a>

## Add solution components

 After you’ve created your solution, it won’t contain any solution components. You can create new components to be added to the solution or add existing components to your new solution.
 
 ### Create components in a solution

 You can use the **New** command to create different types of components. This takes you to a different create experience depending on the component type that you choose. After you finish creating the component, it will be added to the solution. 
 
> [!div class="mx-imgBorder"]  
> ![Create new component in a solution](media/solution-new-component.PNG "Create new component in a solution")  
 
 ### Add an existing component to a solution
 
 With solutions that are unmanaged and not the default one, you can use the **Add existing** command to bring in components that aren’t already in the solution.  
 
> [!div class="mx-imgBorder"]  
> ![Add existing component to a solution](media/solution-add-existing-component.PNG "Add existing component to a solution")  

> [!NOTE]
> The list of existing components will be different depending on the version and solutions imported in your environment. 
  
When you add an existing entity, rather than select **Include all components** or **Include entity metadata**, use the **Select components** option to only add the entity components that have been updated. With solution segmentation, you export solution updates with selected entity assets, such as entity fields, forms, and views, rather than entire entities with all the assets. [Create a segmented solution with entity assets](#create-a-segmented-solution-with-entity-assets)

 Many of the customizations you’ll want to do will involve entities. You can use the **Entity** filter to show a list of all the entities in the current solution that can be customized in some way. Once you drill into an entity, you can see the components that are part of the entity as shown with the account entity in the following screenshot. 
   
> [!div class="mx-imgBorder"]  
> ![Demo solution showing expanded account entity](media/solution-entity-account.png "Demo solution showing expanded account entity")  
  
<!--
When you do this you may see a **Missing Required Components** dialog.  
   
 ![Add Required Components Dialog](media/crm-itpro-cust-addrequiredcomponents.PNG "Add Required Components Dialog")  
  
 This dialog alerts you that the solution component has dependencies on other solution components. If you select **No, do not include required components**, the solution may fail if you import it into another organization where all those required components do not exist. If the solution import succeeds, the behavior in the other solution may not be identical as the original organization because the components are configured differently than those in the source solution.  
  
When you select entity components, we recommend that you use solution segmentation so that you only include entity components that are new or updated when you distribute solution updates. With solution segmentation, you work in a solution with selected entity assets, such as entity fields, forms, and views, rather than entire entities with all the assets. More information: [Use segmented solutions](use-segmented-solutions-patches-simplify-updates.md)
  
 If you don’t intend to export the solution, or if you only intend to export it as an unmanaged solution and import it back into the same organization, it isn’t necessary to include required components. If you ever export the solution you’ll see another warning indicating that some required components are missing. If you are only going to import this solution back into the same organization, it is OK to disregard this warning. The steps to edit application navigation or the ribbon without using a third-party editing tool expect that you’ll export the solution back into the same organization.-->  

## Publish changes 

When you make unmanaged changes in an environment, some components, such as forms, entities, model-driven apps, site maps, and views are saved in an unpublished state. The publish action promotes these changes to an active state and makes them available to end users and for export. 
 
### Publish your customizations

1.  Select **Solutions** from the left navigation.

2.  Select the solution that you want to publish to open it.

3.  From the list of commands, select **Publish all customizations**.  

![Publish all customizations](media/publish-all-customizations.PNG "Publish all customizations")  
  
> [!IMPORTANT]
>  Preparing customizations may take some time. If you see a message that the browser page has become unresponsive, wait for the page to become responsive, and don't close it.  

## Solution publisher
Every app you create or customization you make is part of a solution. Every solution has a publisher. You specify the publisher when you create a solution. 

The solution publisher indicates who developed the app. For this reason, you should create a solution publisher that is meaningful. You can view the solution publisher for a solution by selecting **Settings** from the **Solutions** area in Power Apps. For more information about the solution publisher, see [Solution publisher](/power-platform/alm/solution-concepts-alm#solution-publisher) in the Power Platform ALM guide.

> [!NOTE]
> The **Common Data Services Default Solution** is associated with the **Common Data Service Default Publisher**. The default customization prefix will be randomly assigned for this publisher, for example it could be `cr8a3`. This means that the name of every new item of metadata created for your organization will have this prepended to the names used to uniquely identify the items.

### Create a solution publisher
1.	In the Power Apps portal, select **Solutions**. 
2.	On the command bar, select **New solution**, in the right pane select the **Publisher** drop down list, and then select **+ Publisher**. 
    > [!div class="mx-imgBorder"] 
    > <img src="media/create-new-pubisher.png" alt="Create a new publisher" height="738" width="400">
3.	In the **New Publisher** form, enter the required and optional information: 
   - **Display Name**. Enter the display name for the publisher. 
   - **Name**. Enter the unique name for the publisher. 
   - **Prefix**. Enter the publisher prefix you want. 
   -	**Option Value Prefix**. This field generates a number based on the publisher prefix. This number is used when you add options to option sets and provides an indicator of which solution was used to add the option. 
   - **Contact Details**. Optionally, you can add contact and address information.
4. Select **Save and Close**.

### Change a solution publisher
You can change a solution publisher for an unmanaged solution by following these steps:
1.	In the Power Apps portal, select **Solutions**, select **…** next to the solution you want, and then select **Settings**. 
2.	In the **Solution settings** pane, select **Edit publisher**. 
3.	Edit the **Display name** and **Prefix** fields to the values you want. The **Option Value Prefix** field generates a number based on the publisher prefix. This number is used when you add options to option sets and provides an indicator of which solution was used to add the option. 
4.	In addition to the prefix, you can also change the solution publisher display name, contact information, and address in the **Contact Details** section. 
5.	Select **Save and Close**.

## Create a segmented solution

Use solution segmentation so that you only include entity components that are updated when you distribute solution updates. More information: [Use segmented solutions](/power-platform/alm/segmented-solutions-alm) in the Power Platform ALM guide

### Create a segmented solution with entity assets 
 To create a segmented solution, start with creating an unmanaged solution and add only the components that you've updated. The wizard-like setup takes you step by step through the process of adding entity assets. 

For example, imagine that you've created a new custom entity that doesn't exist in any other environment named *Custom entity* and also added a new field named *topten* for the account entity. To create a segmented solution, follow these steps. 
  
1. Go to the Power Apps portal and then select **Solutions**.  
  
2.  Select **New solution** and create a solution. Enter information in the required fields. Select **Create**.  
  
3.  Open the solution you created. On the command bar, select **Add Existing**, and then select **Entity**.  
  
4.  In the **Add existing entities** pane, select one or more entities you want to add to the solution. For example, select **Account** and **Custom entity**. Select **Next**.  

5.  In the **Select entities** pane, you can choose from the assets to include: 
    - **Include all components**. This option includes all components *and* metadata associated with the entity. It can include other entities or entity components such as business process flows, reports, connections, and queues. 
    - **Include entity metadata**. This option includes *only* the metadata associated with the entity. Metadata includes the entity attributes, such as auditing, duplicate detection, or change tracking. 
    - **Select components**. This option lets you individually select each component that’s associated with the entity, such as fields, relationships, business rules, views, forms, and charts. 
    - Don't include any components. 

      For this example, because *Custom entity* has never been imported into the target environment, next to **Custom entity** select **Include all components**. Under **Account**, choose **Select components**.  
      > [!div class="mx-imgBorder"] 
      > ![Add existing entities](media/add-existing-entities1.png)
  
6.  Since only the *topten* custom field is new to the account  entity, select **Top Ten**, and then select **Add**.  
     > [!div class="mx-imgBorder"] 
     > ![Select entity components](media/add-existing-entities2.png)

7. Select **Add** to add the components to the solution. 

### Create a segmented solution using solution explorer  
The following illustrations provide an example of creating a segmented solution by choosing entity assets from the `Account`, `Case`, and `Contact` entities.  

> [!NOTE]
> The case entity is included with some Dynamics 365 applications, such as Dynamics 365 Customer Service. 
  
Start by opening an unmanaged solution you created. Choose the **Entity** component.  

 > [!div class="mx-imgBorder"] 
 > ![Add existing resources.](media/solution-segmentation-add-existing-resources-admin.png "Add existing resources.")  
  
 Then, select the solution components.  
  
 ![Select solution's components.](media/solution-segmentation-select-components-admin.png "Select solution's components.")  
  
 Follow the wizard. In Step 1, starting in alphabetical order, select the assets for the first entity, the `Account` entity, as shown here.  
  
 ![Start the wizard.](media/solution-segmentation-wizard-starts-admin.png "Start the wizard.")  
  
 Open the **Fields** tab and select the **Account Number** field.  
  
 ![Select the Account entity assets.](media/solution-segmentation-select-account-assets-admin.png "Select the Account entity assets.")  
  
 In Step 2, for the **Case** entity, add all assets.  
  
 ![Select the Case entity assets.](media/solution-segmentation-select-case-assets-admin.png "Select the Case entity assets.")  
  
 In Step 3, add the **Anniversary** field for the **Contact** entity.  
  
 ![Select the Contact entity assets.](media/solution-segmentation-select-contact-assets-admin.png "Select the Contact entity assets.")  
  
 As a result, the segmented solution that’s created contains three entities, `Account`, `Case`, and `Contact`. Each entity contains only the assets that were chosen.  
  
 > [!div class="mx-imgBorder"] 
 > ![Solution with entities.](media/solution-segmentation-solution-entities-admin.png "Solution with entities.")

### See also
 [Use solutions](use-solution-explorer.md)
