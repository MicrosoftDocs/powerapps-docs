---
title: "Solutions  | MicrosoftDocs"
description: "Use the solutions area to view the objects and components in a solution"
keywords: 
ms.date: 11/07/2024
ms.custom: 
ms.topic: article
ms.assetid: 
author: Mattp123
ms.subservice: dataverse-maker
ms.author: swatim
ms.reviewer: matp
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 
topic-status: Drafting
search.audienceType: 
  - maker
---
# Solution view

The modern solution view makes it easier for you to work with solution objects and subcomponents in your solutions.

## Open solution view

To open the solution view, sign in to Power Apps (make.powerapps.com) on the left navigation pane, select **Solutions**, and then open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)] 

The solution objects and available actions are displayed.

1. Panes - The left navigation pane consists of the following areas:
   - **Overview**. Provides details about the solution, such as display name, name, created on date, version, managed or unmanaged, publisher, description, and whether the solution is a patch. Also, solution health information and solution actions available on the command bar such as export, clone, apply upgrade, and translations.
   - **Objects**. Presents a tree view of all objects within the solution. Select an object from the objects list (4) to view or edit it.
   - **History**.  Presents the solution operations completed on the solution. An operation can be a solution import, export, or uninstall. The solution history displays information such as solution version, solution publisher, type of operation, operation start and end time, and operation result status.
   - **Pipelines**. Deploy solutions using pipelines in Power Platform. More information: [Set up pipelines in Power Platform](/power-platform/alm/set-up-pipelines)
   - **Source control** (not shown in image). Connect to Git to source your Power Platform solution objects in an Azure DevOps Git repo. More information: [Overview of Dataverse Git integration](/power-platform/alm/git-integration/overview)
2. Tree view. From the **Object** pane, the tree view displays a list that you can browse to find an object to open it or one of the object’s subcomponents. Search for objects and subcomponents that are in the solution.
3. Command bar. Contextual command bar to perform actions on the solution, objects, or subcomponents.
4. Objects. Displays information and solution components that can be viewed and/or opened for editing of the selected object from the **Objects** pane. Add existing objects and subcomponents or create new ones for unmanaged solutions. More information: [Objects list](#objects-list)
5. Search. Use to filter the list of subcomponents for the object that's currently selected. Filter on any subcomponent property. For example, filter on only **Lookup** data types or whether a column is **Required** by entering those strings in the **Search** box.

:::image type="content" source="media/solutions-area-solution.png" alt-text="Solutions area displaying the objects pane" lightbox="media/solutions-area-solution.png":::

## Objects list

The **Objects** list in solution view has the following columns:

- **Display name**. The friendly name of the solution object.
- **Name**. The unique or logical name of the solution object that includes the solution publisher prefix.
- **Type**. Solution object type, such as a table, web resource, model-driven app, canvas app, and so on.
- **Managed**. Indicates whether the solution object is managed or unmanaged. Managed solutions aren't typically customizable.
- **Customized**. Unmanaged solution components are customized while managed solution objects typically shouldn't be. If a managed solution object is customized, you can remove the customization. More information: [View solution layers for a component](solution-layers.md#view-the-solution-layers-for-a-component)
- **Last modified**. The date the solution object was last changed.

### See also

[View the history of a solution](solution-history.md) <br />
[View dependencies for a component](view-component-dependencies.md) <br />
[Create a solution](create-solution.md)
