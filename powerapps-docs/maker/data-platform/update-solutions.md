---
title: "Update a solution | MicrosoftDocs"
description: "Learn how to update or upgrade a solution in Power Apps"
ms.custom: ""
ms.date: 01/18/2022
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
---

# Upgrade or update a solution  

There are times when you need to update an existing managed solution. To update the solution, follow these steps:

1. Open the unmanaged solution in your development environment and create new or add and remove the existing components that you want. 
2. Increment the version number when you export the solution as a managed solution. More information: [Understanding version numbers for updates](#understanding-version-numbers-for-updates) 

    > [!div class="mx-imgBorder"] 
    > ![Update solution version.](media/update-solution-version.png)
3. [Apply the upgrade or update in the target environment](#apply-the-upgrade-or-update-in-the-target-environment)

## Apply the upgrade or update in the target environment

The procedure to import the updated solution is similar to installing a new managed solution, except you will get some different options. If you are updating a solution you got from someone else, you should get guidance from the solution publisher about which options you should choose.  

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select the target environment you want, and then select **Solutions** from the left navigation. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)] 

2. On the command bar, select **Import**.  

3. On the **Select Solution Package** page, select **Browse** to locate the compressed (.zip or .cab) file that contains the solution you want to update.  

4. Select **Next**.  

5. This page displays a yellow bar indicating **This solution package contains an update for a solution that is already installed**. To upgrade the solution, select **Next**. To view additional options, expand **Advanced settings**, and then select from the following solution action options:  
   - **Upgrade**
        This is the default option and upgrades your solution to the latest version and rolls up all previous patches in one step.  Any components associated to the previous solution version that are not in the newer solution version will be deleted. This option will ensure that your resulting configuration state is consistent with the importing solution including removal of components that are no longer part of the solution.
        
   - **Stage for Upgrade**
        This option upgrades your solution to the higher version, but defers the deletion of the previous version and any related patches until you apply a solution upgrade later.  This option should only be selected if you want to have both the old and new solutions installed in the system concurrently so that you can do some data migration before you complete the solution upgrade. Applying the upgrade will delete the old solution and any components that are not included in the new solution.
        
   - **Update**
        This option replaces your solution with this version. Components that are not in the newer solution won't be deleted and will remain in the system. Be aware that the source and destination environment may differ if components were deleted in the source environment. This option has the best performance by typically finishing in less time than the upgrade methods.
        
8. Decide whether to enable the following option for post import actions:
   - **Enable plug-in steps and flows included in the solution**  
        Selecting this option will enable plug-ins and Power Automate flows that are included in the solution.
        
9. Select **Import**.  

   :::image type="content" source="media/import-solution-pane.png" alt-text="Import solution information and options.":::

10. You may need to wait a few moments while the solution import completes. If it's successful, you can view the results and select **Close**.  

   Managed customizations are always imported in a published state, so there is no need to publish customizations after import in this scenario.

**Completing Solution Upgrade**
If you chose to stage for upgrade, or if the system had an issue completing an upgrade, you will see that you have the original solution still installed in your system as well as a new solution that has the same solution name as the base solution suffixed with \_Upgrade.  To complete the upgrade, select the base solution in the solution list and select **Apply Solution Upgrade**.  This will uninstall all previous patches and the base solution then rename the \_Upgrade solution to be the same name as the previous base solution.  Any components that were in the original solution and patches that are not present in the \_Upgrade solution will be deleted as part of this process.

## Understanding version numbers for updates

A solution’s version has the following format: major.minor.build.revision. An update must have a higher major, minor, build, or revision number than the parent solution. For example, for a base solution version 3.1.5.7, a small update could be a version 3.1.5.8 or a slightly more significant update could have version 3.1.7.0. A substantially more significant update could be version 3.2.0.0.

## Removing a managed component from the target environment

There might be occasions when you want to remove a managed component from an environment. There are two different solution actions that you can perform that will remove a managed component from an environment.

- Upgrade the solution (recommended). In the development environment where the managed solution originated, update the solution so that it no longer includes the component. In other words, remove the component such as a column, chart, or form from the solution and then export it as managed. Then, when you import the managed solution into the target environment, choose the **Solution action** as **Upgrade**. This action removes the component (if there aren’t any other components that depend on it in the target environment).
- Delete the managed solution. This action removes all components in the solution. In the environment where the managed solution was imported, delete the managed solution that includes the managed component. You can do this from the **Solutions** area of Power Apps.
   > [!WARNING]
   > Deleting a managed solution deletes ALL the components that are in the managed solution as well as any related data. Always use caution before deleting a managed solution.


## Overwrite customizations option

The option to overwrite customizations is only available with the classic import experience and using the SDK APIs.

> [!IMPORTANT]
> Selecting the **Overwrite Customizations (not recommended)**  option will overwrite or remove any unmanaged customizations previously performed on components included in this solution. This option does not affect components that support merge behavior (forms, sitemap, ribbon, app modules).  Components that have other managed solutions on top of the existing solution you are replacing do also still remain on top and are not affected by this option.  

### See also
[Layering within a managed solution](/power-platform/alm/solution-layers-alm#layering-within-a-managed-solution)
[Add solution components](create-solution.md#add-solution-components) <br />
[Create solution patches](/power-platform/alm/update-solutions-alm#create-solution-patches) <br />
[For developers: Cloning, patching, and upgrading](/power-platform/alm/solution-api#cloning-patching-and-upgrading)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
