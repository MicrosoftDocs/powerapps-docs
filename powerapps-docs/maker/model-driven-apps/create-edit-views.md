---
title: "Create or edit a model-driven app view in Power Apps | MicrosoftDocs"
description: "Learn how to create or edit a view"
ms.collection: get-started
ms.date: 08/03/2022
ms.reviewer: ""
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
search.audienceType: 
  - maker
---
# Understand model-driven app views

Model-driven apps use views to define how a list of records for a specific table are displayed in the application.

A view defines:

- The columns to display.
- The order of the columns.
- How wide each column should be.
- How the list of records should be sorted by default.
- The default filters applied to restrict the records that will appear.

Once a view has been made available in the app, the user can select it.

:::image type="content" source="media/create-or-edit-model-driven-app-view/switch-views.gif" alt-text="Switch between views":::

When designing an app, the maker decides which of the public views to make available to app users. These decisions are typically based on the type of user, such as sales or marketing, that will use the app.  

Views can be developed through the table designer or the app designer.

:::image type="content" source="media/configure-views.png" alt-text="Configure views in model-driven apps":::

## Types of views  
  
There are three types of views: *personal*, *system*, and *public*.

- **Personal view** - Personal views are owned by individuals and only visible to that person unless they share their personal views with others.
- **System view** - As a system administrator or system customizer, you can edit system views. System views are special views the application depends on, which exist for system tables or are automatically created when you create custom tables. These views have specific purposes and some additional capabilities.
- **Public view** - Public views are general purpose views that you can customize as you see fit. They are important because all app users can access them, when they are made available, by using the view selector.  It is possible to use public views in subgrids in a form or as a list in a dashboard.

## Views within model-driven apps

Users may want to view data in relation to a table in a range of ways. A drop-down list of views is frequently displayed in the application so these can be selected.

:::image type="content" source="media/my-views.png" alt-text="My Views in a model-driven app":::

Personal views are included above the list of system or public views that are available in the app. This makes it easier for users to find the data that is important to them.

The records that are visible in views are displayed in a list. Views frequently provide options for users to change the default sorting, column widths, and filters to more easily find the data that's important to them.

Views are not only used by users within model-driven apps, they can also be used to define the data source in, for example,  charts that are used in the application.

### Personal views  

Personal views can be created by following these steps:

1. Select **Create view** from the command bar in your model-driven app.
   :::image type="content" source="media/create-view.png" alt-text="Create view in model-driven app":::
1. Define the [view filters](create-edit-view-filters.md).
1. Then select **Save**.

> [!Note]
> While you can create a new personal view based on a system or public view, you can't create a system or public view based on a personal view.

Personal views can be created by users who have at least User level access to actions for the Saved View table.

As system administrator, you can modify the access level for each action in the security role to control the depth to which people can create, read, write, delete, assign, or share personal views.

### System views

|System Views  |Description  |
|---------|---------|
|Quick Find     | The default view used when searches are performed using Quick Find. This view also defines which columns are searched when using search capabilities of Quick Find and Lookup views.        |
|Advanced Find     |  The default view used to display results when using Advanced Find. This view also defines the columns used by default when new custom public views or personal views are created without defining a view to use as a template.       |
|Associated     |  The default view that lists the related tables for a record.       |
|Lookup     | The view that is displayed when you select a record to set for a [lookup](../model-driven-apps/model-driven-app-glossary.md#lookup)  column.        |

These views are not shown in the view selector and you can't use them in sublists in a form or as a list in a dashboard. You can't delete or deactivate these views. For more information about removing views, go to [Remove views](remove-views.md).

System views are owned by the organization so that everyone can view them. For example, everyone has organization-level access to read records for the view (`savedquery`) table. These views are associated with specific tables and are visible within the solution explorer. You can include these views in solutions because they are associated with the table.

> [!Note]
> System views are cached for performance optimization purposes and therefore plugins on the `savedquery` table aren't supported.

### Public views

Some public views exist by default for system tables and for any custom table. For example, when you create a new custom table, it will have the following combination of public and system views.

|Name  |Type  |
|---------|---------|
|Active *table plural name*     |  Public       |
|Inactive *table plural name*    |  Public       |
|Quick Find Active *table plural name*     | Quick Find        |
|*Table name* Advanced Find View     | Advanced Find        |
|*Table name* Associated View     |  Associated       |
|*Table name* Lookup View     | [Lookup](../model-driven-apps/model-driven-app-glossary.md#lookup)        |

You can create custom public views. You can delete any custom public views you create in an unmanaged solution.

You can't delete any system-defined public views.

Custom public views added by a managed solution should only be deleted by uninstalling or updating the managed solution.

## How to access the view editor to create or edit views

- App Designer: If you're working in an app, you may want to use the app designer, which provides a simple and intuitive user interface with drag-and-drop capabilities for creating views. More information: [Tutorial: Create and edit public or system views by using the app designer](create-edit-views-app-designer.md)
- Solution explorer: If you're already experienced with Dynamics 365, you may want to use the solution explorer. For more information, go to [Navigate to advanced app making and customization areas](advanced-navigation.md#solution-explorer)

## Customize views

As a system customizer you can customize views and subgrids through controls by making them read-only or editable as well as display an alphabetic list at the bottom of views or subgrids (jump bar).

The following controls are available:

|Grid control name  |Read-only or editable?  |Description  |
|---------|---------|---------|
|**Power Apps grid control (Preview)**     |  Read-only or editable   | Currently in preview, this grid control includes accessibility enhancements and will become the default grid control used in views and subgrids. This control will eventually replace all other grid controls. More information: [Power Apps grid control (preview)](the-power-apps-grid-control.md)       |
|**Power Apps Read-Only Grid**     | Read-only    | Modern grid with accessibility enhancements released in October 2021 and became the default read-only grid experience in April 2022. More information: [Power Apps read-only grid control](power-apps-grid-control.md)       |
|**Editable Grid**  |  Editable only    | Legacy grid control. More information: [Make model-driven app views editable using the editable grid control](make-grids-lists-editable-custom-control.md)        |
|**Read-Only Grid**  | Read-only    |  Legacy grid control that is deprecated. More information: [ The legacy read-only grid in model-driven apps is deprecated](/power-platform/important-changes-coming#the-legacy-read-only-grid-in-model-driven-apps-is-deprecated)    |

## Next steps

[Opening the view designer](./accessing-view-definitions.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
