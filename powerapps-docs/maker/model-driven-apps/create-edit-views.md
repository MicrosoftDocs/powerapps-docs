---
title: "Create or edit a model-driven app view in Power Apps | MicrosoftDocs"
description: "Learn how to create or edit a view"
ms.custom: intro-internal
ms.date: 03/19/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: bd1d393d-16ea-40ac-8136-26643c37dd2a
caps.latest.revision: 25
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Understand model-driven app views

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Model-driven apps use views to define how a list of rows for a specific table is displayed in the application.

A view defines:

- The columns to display.
- The order of the columns.
- How wide each column should be.
- How the list of rows should be sorted by default.
- The default filters applied to restrict the rows that will appear.

Once the view has been made available in the app the user can switch between these.

:::image type="content" source="media/create-or-edit-model-driven-app-view/switch-views.gif" alt-text="Switch between views":::

When designing an app the developer decides on which of the public views to make available to app users. These decisions are typically based on the types of user such as sales, or marketing, that will be making use of the app.  

Views can be developed through the table designer or the app designer.

:::image type="content" source="media/configure-views.png" alt-text="Configure views in model-driven apps":::

## Types of views  
  
There are three types of views: *personal*, *system* and *public*.

- **Personal view** - Personal views are owned by individuals and only visible to that person unless they share their personal views with others.
- **System view** - As a system administrator or system customizer, you can edit system views. System views are special views the application depends on, which exist for system tables or are automatically created when you create custom tables. These views have specific purposes and some additional capabilities.
- **Public view** - Public views are general purpose views that you can customize as you see fit. They are important because all app users get to see and are available in the view selector.  It is possible to use them in sub-grids in a form or as a list in a dashboard.

## Views within model-driven apps

Users may wish to see data in relation to a table in a range of ways.  A drop-down list of views is frequently displayed in the application so these can be selected.

:::image type="content" source="media/my-views.png" alt-text="My Views in a model-driven app":::

Personal views are included above the list of system or public views that are available in the app. To make it easier for users to find the data that is important to them.

The rows that are visible in views are displayed in a list. Views  frequently provide options for users to change the default sorting, column widths and filters to more easily see the data that's important to them.

Views are not only used by users within model-driven apps, they can also be used to define the data source in for example charts that are used in the application.

### Personal views  

Personal views can be created by following these steps:

1. select **Create view** from the command bar in your model-driven app.
:::image type="content" source="media/create-view.png" alt-text="Create view in model-driven app":::
1. Define the [view filters](create-edit-view-filters.md)
1. Then select **Save**

> [!note]
>While you can create a new personal view based on a system or public view, you cannot create a system or public view based on a personal view.

Personal views can be created by users who have at least User level access to actions for the Saved View table.

As system administrator, you can modify the access level for each action in the security role to control the depth to which people can create, read, write, delete, assign, or share personal views.

### System views

|System Views  |Description  |
|---------|---------|
|Quick Find     | The default view used when searches are performed using Quick Find. This view also defines which columns are searched when using search capabilities of Quick Find and Lookup views.        |
|Advanced Find     |  The default view used to display results when using Advanced Find. This view also defines the columns used by default when new custom public views or personal views are created without defining a view to use as a template.       |
|Associated     |  The default view that lists the related tables for a row.       |
|Lookup     | The view you see when you select a row to set for a [lookup](../model-driven-apps/model-driven-app-glossary.md#lookup)  column.        |

These views are not shown in the view selector and you can't use them in sublists in a form or as a list in a dashboard. You cannot delete or deactivate these views. For more information on removing views see [Remove views](remove-views.md)

System views are owned by the organization so that everyone can see them. For example, everyone has organization-level access to read rows for the View (savedquery) table. These views are associated with specific tables and are visible within the solution explorer. You can include these views in solutions because they are associated with the table.

> [!note]
>System views are cached for performance optimization purposes and therefore plugins on the savedquery table are not supported.

### Public views

Some public views exist by default for system tables and for any custom table. For example, when you create a new custom table, it will have the following combination of public and system views.

|Name  |Type  |
|---------|---------|
|Active *table plural name*     |  Public       |
|Inactive *table plural name*    |  Public       |
|Quick Find Active *table plural name*     | Quick Find        |
|*table name* Advanced Find View     | Advanced Find        |
|*table name* Associated View     |  Associated       |
|*table name* Lookup View     | [Lookup](../model-driven-apps/model-driven-app-glossary.md#lookup)        |

You can create custom public views. You can delete any custom public views you create in an unmanaged solution.

You cannot delete any system-defined public views.

Custom public views added by a managed solution should only be deleted by uninstalling or updating the managed solution.

## How to access the view editor to create or edit views

- App Designer: If you're working in an app, you may want to use the App Designer, which provides a simple and intuitive user interface with drag-and-drop capabilities for created views. More information: [Tutorial: Create and edit public or system views by using the app designer](create-edit-views-app-designer.md)
- Solution explorer: If you're already experienced with Dynamics 365, you may want to use the solution explorer. For more information see [Navigate to advanced app making and customization areas](advanced-navigation.md#solution-explorer)

## Customize views

As a system customizer you can customize the views through controls by making grids (lists) editable.

The following controls are used:

- Editable Grid: Allows users to do rich in-line editing directly from grids and sub-grids whether they're using a web app, tablet, or phone. for more information see [Make grids editable using the Editable Grid custom control](make-grids-lists-editable-custom-control.md)
- Read Only Grid: Provides users an optimal viewing and interaction experience for any screen size or orientation such as mobiles and tablets by using responsive design principles. For more information see [Specify properties for Unified Interface apps](specify-properties-for-unified-interface-apps.md)

## Next steps

[Opening the view designer](./accessing-view-definitions.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
