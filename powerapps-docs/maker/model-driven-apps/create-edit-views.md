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

<a name="BKMK_CreatingAndEditingViews"></a>   

With Power Apps apps, use views to define how a list of rows for a specific table is displayed in the application. A view defines:

- The columns to display
- How wide each column should be
- How the list of rows should be sorted by default
- What default filters should be applied to restrict which rows will appear in the list

A drop-down list of views is frequently displayed in the application so that people have options for different views of table data.

The rows that are visible in individual views are displayed in a list, sometimes called a grid, which frequently provides options so that people can change the default sorting, column widths, and filters to more easily see the data that's important to them. Views also define the data source for charts that are used in the application.  
  
## Types of Views  
  
There are three types of views: *personal*, *system*, and *public*.

This topic is about how system administrators and system customizers work with system and public views. 
  
### Personal views  
  
 You and anyone else who has at least User level access to actions for the Saved View table can also create personal views. As system administrator, you can modify the access level for each action in the security role to control the depth to which people can create, read, write, delete, assign, or share personal views.

Personal views are owned by individuals and, because of their default User level access, they are visible only to that person or anyone else they choose to share their personal views with. You can create personal views by saving a query that you define by using Advanced Find or by using the Save Filters as New Views and Save Filters to Current View options in the list of views. These views are typically included at the bottom in lists of system or public views that are available in the application. While you can create a new personal view based on a system or public view, you cannot create a system or public view based on a personal view.
  
### System views
As a system administrator or system customizer, you can edit system views. System views are special views the application depends on, which exist for system tables or are automatically created when you create custom tables. These views have specific purposes and some additional capabilities. 


|System Views  |Description  |
|---------|---------|
|Quick Find     | The default view used when searches are performed using Quick Find. This view also defines which columns are searched when using search capabilities of Quick Find and Lookup views.        |
|Advanced Find     |  The default view used to display results when using Advanced Find. This view also defines the columns used by default when new custom public views or personal views are created without defining a view to use as a template.       |
|Associated     |  The default view that lists the related tables for a row.       |
|Lookup     | The view you see when you select a row to set for a lookup column.        |

These views are not shown in the view selector and you can't use them in sublists in a form or as a list in a dashboard. You cannot delete or deactivate these views. More information: [Remove views](remove-views.md)

System views are owned by the organization so that everyone can see them. For example, everyone has organization-level access to read rows for the View (savedquery) table. These views are associated with specific tables and are visible within the solution explorer. You can include these views in solutions because they are associated with the table. Unified Interface optimizes for performance by caching system views and does not support running plugins on the savedquery table.

### Public views

Public views are general purpose views that you can customize as you see fit. These views are available in the view selector and you can use them in sub-grids in a form or as a list in a dashboard. Some public views exist by default for system tables and for any custom table. For example, when you create a new custom table, it will have the following combination of public and system views.


|Name  |Type  |
|---------|---------|
|Active *table plural name*     |  Public       |
|Inactive *table plural name*    |  Public       |
|Quick Find Active *table plural name*     | Quick Find        |
|*table name* Advanced Find View     | Advanced Find        |
|*table name* Associated View     |  Associated       |
|*table name* Lookup View     | Lookup        |

You can create custom public views. You can delete any custom public views you create in an unmanaged solution. You cannot delete any system-defined public views. Custom public views added by importing a managed solution may have managed properties set that can prevent them from being deleted, except by uninstalling the managed solution.

## Places where you can access the view editor to create or edit views

- Power Apps site: To access the view designer, select **Dataverse** > **Tables**, select a table, and then select the **View** tab. Open an existing view or create a new one. More information: [Create or edit a view](./create-edit-views-app-designer.md)
- App Designer: If you're working in an app, you may want to use the App Designer, which provides a simple and intuitive UI with drag-and-drop capabilities for created views. More information: [Tutorial: Create and edit public or system views by using the app designer](create-edit-views-app-designer.md)
- Solution explorer: If you're already experienced with Dynamics 365, you may want to use the solution explorer. More information: [Navigate to advanced app making and customization areas](advanced-navigation.md#solution-explorer)
 
## Customize views

As a system customizer you can customize the views through controls by making grids (lists) editable and compatible for Unified Interface. The following controls are used:

- Editable Grid: Allows users to do rich in-line editing directly from grids and sub-grids whether they're using a web app, tablet, or phone. More information: [Make grids editable using the Editable Grid custom control](make-grids-lists-editable-custom-control.md)
- Read Only Grid: Provides users an optimal viewing and interaction experience for any screen size or orientation such as mobiles and tablets by using responsive design principles. More information: [Specify properties for Unified Interface apps](specify-properties-for-unified-interface-apps.md)



## Next steps

[Create or edit views](./create-edit-views-app-designer.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]