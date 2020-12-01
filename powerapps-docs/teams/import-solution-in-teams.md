---
title: Import a solution into Dataverse for Teams | Microsoft Docs
description: Explains how to import a Dataverse solution into Dataverse for Teams.
author: wimcoor
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/09/2020
ms.author: wimcoor
ms.reviewer: matp
---
#  Import a Dataverse solution into Dataverse for Teams

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse for Teams provides a way to transport the customizations you make in Microsoft Dataverse into Dataverse for Teams. The process involves three main steps:

1. First, create a solution in a Dataverse environment. 
1. Next, export the solution from the Dataverse environment.
1. Finally, import the solution in Dataverse for Teams.

## Create a solution in Dataverse 
The first step to move your customizations is to create a solution in Dataverse. Include only components that are fully supported for Dataverse for Teams. Solutions that included components that are not supported by Dataverse for Teams won’t import. Only the following custom components can be imported into Dataverse for Teams:

* Canvas apps 
* Tables 
* Flows 
* Bots 
* Connection references 
* Environment variables 

> [!NOTE]
> Only include items that you or your team have created. Solutions that contain any of the standard Dataverse or Dynamics 365 tables, such as account or contact, won’t import.

For information about the differences between Dataverse for Teams and Dataverse see [How are Dataverse for Teams and Dataverse different?](data-platform-compare.md)

For information about how to create a solution with Dataverse, see [Create a solution](../maker/common-data-service/create-solution.md). 

## Export the solution form Dataverse

Typically, you want to export your solution as managed. However, if your goal is to transport your customizations to Dataverse for Teams and continue your development from there, export your solution as an unmanaged solution. More information: [Export solutions](../maker/common-data-service/export-solutions.md) 

## Import the solution into Dataverse for Teams
1. Select the **Build** tab of the team where you want to import the solution.
1. Select **See all**, and then on the command bar, select **Import**.
1. On the **Import a solution** pane, select **Browse**.

    :::image type="content" source="media/teams-import-solution.png" alt-text="Select Browse":::
1. Locate the compressed (.zip or .cab) file that contains the solution you want to import, select **Open**, and then select **Next**. 
1. Information about the solution is displayed. Depending on the components in the solution, you may be prompted for additional information before you select **Next**.
   - If your solution contains connection references, you’ll be prompted to select the connections you want. If a connection does not already exist, create a new one. 
   - If your solution contains environment variables, you will be prompted to enter values. You will not see this screen if values are already present in your solution or the target environment.
1. Select **Import**.

Your solution imports in the background and may take multiple minutes. A notification appears on the **Build** tab as the solution is imported.

:::image type="content" source="media/teams-import-staus.png" alt-text="Currently importing solution message ":::
After the import completes, a success or failure notification is displayed.
 
The location of your solution components is different depending on whether you imported a managed or unmanaged solution:
* With a managed solution, all your customizations appear on the **Build** tab under **Installed apps** using the name of the solution.
* With an unmanaged solution, all your customizations appear on the **Build** tab under **Built by this team**.

## Troubleshooting import failures

If the import isn’t successful, you’ll see a notification on the solutions page that displays error or warnings messages that were captured. Select **Download Log File** to capture details about what caused the import to fail. The most common cause for an import to fail is that the solution did not contain some required components.

When you download the log file, you will find an XML file in your browser's default download folder that you can open using Office Excel to view the contents.

## Known issue

When you are working with a new Dataverse for Teams environment, the **Import** command is missing because the **See all** link **Build** tab is not displayed for that environment.  

To work around this issue, create and save an app in the environment. When an item exists in the environment the **See all** link is available and you will be able to browse to the **Build** tab.

### See also

[Export solutions](../maker/common-data-service/export-solutions.md)
