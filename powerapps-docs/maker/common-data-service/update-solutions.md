---
title: "Import, update and upgrade a solution | MicrosoftDocs"
description: "Learn how to import, update and upgrade a solution in Power Apps"
ms.custom: ""
ms.date: 01/24/2020
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
ms.assetid: 
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Import, update, and upgrade a solution  
[!INCLUDE [applies-to-on-premises](../includes/applies-to-on-premises.md)] [Import, update, and export solutions](/powerapps/maker/common-data-service/import-update-export-solutions)

This topic describes how to import, update, and upgrade a solution. 
  
## Import a solution
You can import solutions manually using the steps below. Only import solutions that you've obtained from a trusted source. Customizations might include code that can send data to external sources. 

1. [!INCLUDE[proc_settings_solutions](../includes/proc-settings-solutions.md)]  

2. In the solutions list menu, choose **Import**.  

3. In the **Import Solution** dialog, **Select Solution Package** step browse to the compressed (.zip or .cab) file that contains the solution you want to import.  

4. Choose **Next**.  

5. You can view information about the solution before you choose **Import**.  

6. You may need to wait a few moments while the solution import completes. If it is successful, you can view the results and choose **Close**.  

   If you have imported any changes that require publishing, you must publish customizations before they will be available. 

   If the import isn’t successful, you will see a report showing any errors or warnings that were captured. You can choose **Download Log File** to capture details about what caused the import to fail. The most common cause for a solution import to fail is that the solution did not contain some required solution components.  

   When you download the log file, you will find an XML file that you can open using [!INCLUDE[pn_MS_Excel_Full](../includes/pn-ms-excel-full.md)] and view the contents.  

> [!NOTE]
>  You can’t edit an active routing rule set. Therefore, if you’re importing a solution that includes an active routing rule set into an organization where the rule already exists with the same ID, the solution import will fail. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Create rules to automatically route cases](../../../customer-service/create-rules-automatically-route-cases.md)  

<a name="BKMK_UpdateSolutions"></a>   

## Update or upgrade a solution  
There are times when you may wish to install an update to an existing managed solution. The procedure is similar to installing a new managed solution, except you will get some different options. If you are updating a solution you got from someone else, you should get guidance from the solution publisher about which options you should choose.  

1. [!INCLUDE[proc_settings_solutions](../includes/proc-settings-solutions.md)]  

2. In the solutions list menu choose **Import**.  

3. In the **Import Solution** dialog, **Select Solution Package** step browse to the compressed (.zip or .cab) file that contains the solution you want to update.  

4. Choose **Next**.  

5. You can view information about the solution before you choose **Next**. This page will display a yellow bar saying **This solution package contains an update for a solution that is already installed**.  

6. You will have the following Solution Action options:  
   - **Upgrade (recommended)**
        This option upgrades your solution to the latest version and rolls up all previous patches in one step.  Any components associated to the previous solution version that are not in the newer solution version will be deleted. This option is the recommended option as it will ensure that your resulting configuration state is consistent with the importing solution including removal of components that are no longer part of the solution.
        
   - **Stage for Upgrade**
        This option upgrades your solution to the higher version, but defers the deletion of the previous version and any related partches until you apply a solution upgrade later.  This option should only be selected if you want to have both the old and new solutions installed in the system concurrently so that you can do some data migration before you complete the solution upgrade which will delete the old solution and any components that are not included in the new solution.
        
   - **Update (not recommended)**
        This option replaces your solution with this version.  Components that are not in the newer solution will not be deleted and will remain in the system.  This option is not recommended as your destination environment will differ in configuration from your source environment and could cause issues that are difficult to reproduce and diagnose.
        
7. You will have the following customization options:

   - **Maintain customizations (recommended)**  

        Selecting this option will maintain any unmanaged customizations performed on components but also implies that some of the updates included in this solution will not take effect.  

   - **Overwrite Customizations (not recommended)**  

        Selecting this option will overwrite or remove any unmanaged customizations previously performed on components included in this solution. This option does not affect components that support merge behavior (forms, sitemap, ribbon, app modules).  Components that have other managed solutions on top of the existing solution you are replacing do also still remain on top and are not affected by this option.  

8. You will have the following option available to enable for Post Import Actions:
   - **Enable any SDK message processing steps included in the solution**  
        Selecting this option will enable plugins and workflows that are included in the solution.
        
9. Choose **Next**.  

10. You may need to wait a few moments while the solution import completes. If it is successful, you can view the results and choose **Close**.  

   If you have imported any changes that require publishing, you must publish customizations before they will be available. 

**Completing Solution Upgrade**
If you chose to stage for upgrade, or if the system had an issue completing an upgrade, you will see that you have the original solution still installed in your system as well as a new solution that has the same solution name as the base solution suffixed with \_Upgrade.  To complete the upgrade simply select the base solution in the solution list and click **Apply Solution Upgrade**.  This will uninstall all previous patches and the base solution then rename the \_Upgrade solution to be the same name as the previous base solution.  Any components that were in the original solution and patches that are not present in the \_Upgrade solution will be deleted as part of this process.


### See also
[Export solutions](export-solutions.md) <br />
[Distribute solutions and patches](use-segmented-solutions-patches-simplify-updates.md) <br />
[Import solutions](import-update-export-solutions.md)