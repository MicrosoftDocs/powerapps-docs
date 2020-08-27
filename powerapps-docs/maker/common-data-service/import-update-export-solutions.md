---
title: "Import solutions | MicrosoftDocs"
description: "Learn how to import a solution in Power Apps"
ms.custom: ""
ms.date: 08/27/2020
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "Mattp123"
ms.assetid: 56363ea3-ea76-4311-9b7a-b71675e446fb
caps.latest.revision: 57
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Import solutions 

You can manually import solutions using the steps in this article. You must import only those solutions that you've obtained from a trusted source. Customizations might include code that can send data to external sources.   
 
> [!NOTE]
> - To import a solution that includes a plug-in assembly, the **Create** privilege on the **Plug-In Assembly** entity is required. By default, the System Administrator security role has this privilege, but the System Customizer security role doesn’t. 
> - When you import a managed solution, all component changes will be brought into the environment in a published state. However, when you import an unmanaged solution, the changes are imported in a draft state so you must publish them to make them active. 
> - To implement healthy application lifecycle management (ALM) in your organization, consider using a source control system to store and collaborate on your solutions, and automate the solution import process. More information: [ALM basics](/power-platform/alm/basics-alm) in the Power Platform ALM guide.

When you import an **unmanaged** solution:
- You add all the components of that solution into your environment and can't delete the components by deleting the solution. Deleting the unmanaged solution deletes only the solution container.
- That contains components you have already customized, your customizations will be overwritten by the customizations in the imported unmanaged solution. You can’t undo this.

To import a solution:

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left navigation.  
  
2. On the command bar, select **Import**.  

    > [!div class="mx-imgBorder"]  
    > ![Import solution](media/solution-import.png "Import solution") 
  
3. On the **Import a solution** page, select **Browse** to locate the compressed (.zip or .cab) file that contains the solution you want to import.
  
4. Select **Next**.  
  
5. Information about the solution is displayed. By default, in the **Advanced settings** section, if SDK messages and flows exist in the solution, they will be imported. Clear the option if you don’t want to import them, and then select **Import**.
  
6. You may need to wait a few moments while the import completes. View the results and then select **Close**.  
  
 If you have imported any changes that require publishing, you must publish customizations before they are available.
  
 If the import isn’t successful, you will see a report showing any errors or warnings that were captured. Select **Download Log File** to capture details about what caused the import to fail. The most common cause for an import to fail is that the solution did not contain some required components.  
  
 When you download the log file, you will find an XML file that you can open using Office Excel to view the contents.  
  
> [!NOTE]
> You can’t edit an active routing rule set. Therefore, if you’re importing a solution that includes an active routing rule set into an environment where the rule already exists with the same ID, the import will fail. More information: [Create rules to automatically route cases](https://docs.microsoft.com/dynamics365/customer-engagement/customer-service/create-rules-automatically-route-cases)  
  
<a name="BKMK_UpdateSolutions"></a>   

### See also
[Update solutions](update-solutions.md) <br />
[Export solutions](export-solutions.md) <br />
[Publish changes](create-solution.md#publish-changes) <br />
[For developers: Create, export, or import an unmanaged solution](/power-platform/alm/solution-api#create-export-or-import-an-unmanaged-solution)
