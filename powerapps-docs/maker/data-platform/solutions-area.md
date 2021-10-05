---
title: "Solutions  | MicrosoftDocs"
description: "Use the solutions area to view the objects and components in a solution"
keywords: 
ms.date: 08/26/2021
ms.service: powerapps
ms.custom: 
ms.topic: article
ms.assetid: 
author: Mattp123
ms.subservice: dataverse-maker
ms.author: matp
manager: kvivek
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 
topic-status: Drafting
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Solution view

The modern solution view makes it easier for you to work with solution objects and subcomponents in your solutions.

## Solution view overview

1. Panes - The left navigation pane consists of the following areas:
   - **Overview**. Provides details about the solution, such as display name, name, created on date, version, managed or unmanaged, publisher, description, and whether the solution is a patch. Also, solution health information and solution actions available on the command bar such as export, clone, apply upgrade, and translations.
   - **Objects**. Presents a tree view of all objects within the solution. Select an object from the objects list (4) to view or edit it.
   - **History**.  Presents the solution operations completed on the solution. An operation can be a solution import, export, or uninstall. The solution history displays information such as solution version, solution publisher, type of operation, operation start and end time, and operation result status.
2. Tree view. From the **Object** pane, the tree view displays a list that you can browse to find an object to open it or one of the object’s subcomponents.
3. Command bar. Contextual command bar to perform actions on the solution, objects, or subcomponents.
4. Objects list. Displays information and components that can be viewed and/or opened for editing of the selected object from the **Objects** pane. Add existing objects and subcomponents or create new ones for unmanaged solutions.
5. Search. Use to filter the list of subcomponents for the object that's currently selected. Filter on any of the subcomponent's properties. For example, filter on only **Lookup** data types or whether a column is **Required** by entering those strings in the **Search** box.

   :::image type="content" source="media/solutions-area-solution.png" alt-text="Solutions area displaying the objects pane":::

## Disable modern solution view

By default, the modern solution view is enabled. To disable, switch **Solution preview on** to off, from the **Solutions** area.

:::image type="content" source="media/enable-solution-preview.png" alt-text="Turn on solution preview"::: 

### See also
[View the history of a solution](solution-history.md) <br />
[View dependencies for a component](view-component-dependencies.md) <br />
[Create a solution](create-solution.md)