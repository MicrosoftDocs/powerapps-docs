---
title: "Import solutions | MicrosoftDocs"
description: "Learn how to import a solution in Power Apps"
ms.custom: ""
ms.date: 07/21/2023
ms.reviewer: ""
ms.topic: "article"
author: "Mattp123"
ms.assetid: 56363ea3-ea76-4311-9b7a-b71675e446fb
caps.latest.revision: 57
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Import solutions

You can manually import solutions using the steps in this article. You must import only those solutions that you've obtained from a trusted source.
 
> [!NOTE]
> - The create privilege is required to import a component. Although, the System Customizer security role has create privilege on most components that are commonly imported, by default it doesn't have create privilege on the **Plug-In Assembly** table. The System Administrator security role has this privilege.
> - When you import a managed solution, all component changes will be brought into the environment in a published state. However, when you import an unmanaged solution, the changes are imported in a draft state so you must publish them to make them active. 
> - To implement healthy application lifecycle management (ALM) in your organization, consider using a source control system to store and collaborate on your solutions, and automate the solution import process. More information: [ALM basics](/power-platform/alm/basics-alm) in the Power Platform ALM guide.

When you import an **unmanaged** solution:
- You add all the components of that solution into your environment and can't delete the components by deleting the solution. Deleting the unmanaged solution deletes only the solution container.
- That contains customized components, the existing customizations to the component will be overwritten after the unmanaged solution import. You can’t undo this.

To import a solution:

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left navigation. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)] 
  
1. On the command bar, select **Import**.  

    > [!div class="mx-imgBorder"]  
    > ![Import solution.](media/solution-import.png "Import solution") 
  
1. On the **Import a solution** page, select **Browse** to locate the compressed (.zip or .cab) file that contains the solution you want to import.

1. Select **Next**.  
  
1. Information about the solution is displayed. By default, in the **Advanced settings** section, if plugin steps (also known as SDK message processing steps) and flows exist in the solution, they'll be imported. Clear the **Enable Plugin steps and flows included in the solution** option if you want them to import in an inactive state.

1. If your solution contains [connection references](create-connection-reference.md), you are prompted to select the connections you want. If a connection doesn't already exist, create a new one. Select **Next**.

1. If your solution contains [environment variables](EnvironmentVariables.md), you'll be prompted to enter values. You won't see this screen if value(s) are already present in your solution or the target environment. 

1. If missing dependencies are detected in the target environment, a list of the dependencies is presented. In environments where the required package version is available for import in the target environment, a link to resolve the dependency is presented. Selecting the link takes you to the Power Platform admin center where you can install the application update. After the application update is completed, you can start the solution import again.

1. Select **Import**.

Your solution imports in the background and may take a few moments.  
  
 If you have imported any changes that require publishing, you must publish customizations before they're available.
  
 If the import isn’t successful, you'll see a notification on the solutions page showing any errors or warnings that were captured. Select **Download Log File** to capture details about what caused the import to fail. The most common cause for an import to fail is that the solution didn't contain some required components.  

When you download the log file, you'll find an XML file that you can open using Office Excel to view the contents.

> [!NOTE]
> You can view the details of all solution operations including solution import with the [solution history](solution-history.md) feature. To view these operations, select **See history** on the solutions page.
  
## Troubleshooting solution import

For known issues and information about how to troubleshoot working with solutions, go to [Manage apps and solutions](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/unmanaged-active-layer-created-after-solution-import) in the Power Apps Troubleshooting documentation.

### See also

[Update solutions](update-solutions.md) <br />
[Export solutions](export-solutions.md) <br />
[Publish changes](create-solution.md#publish-changes) <br />
[For developers: Create, export, or import an unmanaged solution](/power-platform/alm/solution-api#create-export-or-import-an-unmanaged-solution)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
