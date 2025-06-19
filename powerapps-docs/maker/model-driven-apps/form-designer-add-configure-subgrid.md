---
title: "Add and configure a subgrid component on a form | MicrosoftDocs"
description: Learn how to add a subgrid on a model-driven app form
ms.custom: ""
ms.date: 09/20/2024
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: how-to
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
ms.subservice: mda-maker
ms.author: "matp"
tags: 
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
---
# Add and configure a subgrid component on a form

A form that displays the details of a table record can use a subgrid component to display a read-only list of related or unrelated records in a tabular format. From the subgrid, app users can create new rows or open an existing row to edit. Makers add and configure a subgrid component using the form designer.

:::image type="content" source="media/read-only-subgrid.png" alt-text="Subgrid component on a model-driven app form":::

This article explains how makers can add a subgrid component to a model-driven app form. To learn how to add an editable grid to a model-driven app form, go to [Make model-driven app views editable using the editable grid control](make-grids-lists-editable-custom-control.md).

## Add a subgrid component

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and select the environment you want.  
1. Select **Solutions** in the left navigation pane, and then open the solution that contains the table you want.
1. Select **Tables**, and then open the table that you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select the **Forms** area, and then open the form you want to edit.
1. In the form designer, select **Component** on the command bar.
1. Drag a **1-column section** on the left **Components** pane onto the form.
1. With the **New Section** selected, select **Subgrid** from the left **Components** pane.
1. On the **Select subgrid views** pane:
   - Typically app users want to view related records. When **Show related records** is selected, only tables with a relationship are displayed.
   - Select the **Table** you want.
   - Select the **Default view** from the table. When an existing view isn't suitable for the app, [create or edit a view](create-edit-views.md) for the table.
1. Select **Done**.
1. Select **Save**, and then select **Publish**.

## Configure a subgrid component

These are the properties available to configure when using a subgrid component on a form using the form designer.

|Area   |Name  |Description  |
|---------|---------|---------|
| **Display options** | **Label** | The localizable label for the subgrid visible to users. <br /><br />This property is required.|
| **Display options** |  **Name** |  The unique name for the subgrid that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores. <br /><br />This property is required. |
| **Display options** | **Hide label**  | The label can be hidden on the form.  |
| **Display options** | **Hide on phone** |  The subgrid can be hidden to render a condensed version of the form on phone screens. |
| **Display options** | **Show related records** |  When selected, the subgrid displays only records related to the current record that is displayed on the form. <br /><br />The **Table** drop-down list is also filtered to only list tables that are related to the current table. |
| **Display options** | **Table** |  The table whose records you want to display in the subgrid. <br /><br />When **Show related records** is selected, the list of tables is filtered to show only tables that are related to the current table. In addition to the table name, the name of the lookup column is also displayed in parentheses. |
| **Display options** | **Default view** |  The view of the table selected in the **Table** property that will be used to get and display the list of records in the subgrid. |
| **Display options** | **Team template**  | Note: This option is only available with the user table when the **Default view** is **Associated Record Team Members**. When available, sets the team template to use for the subgrid. More information: [Create a team template to control access](/power-platform/admin/create-team-template-add-entity-form) |
| **Display options** | **Allow users to change view** |  When selected, app users can change from the **Default view** to another view of the table selected in the **Table** property. |
| **Display options** | **Show all views** |  When selected, app users can change from the **Default view** to all other views of the table selected in the **Table** property. <br /><br />This property is only available when **Allow users to change view** is selected. |
| **Display options** | **Hide search box**  | When selected, the **Search** box won't appear on the upper right of the subgrid.  |
| **Display options** | **Selected views** |  A list of views of the table selected in the **Table** property that app users can change from the **Default view**. <br /><br />This property is only available when **Allow users to change view** is selected and **Show all views** is cleared. |
| **Display options** | **Default chart**  | Select which chart to show if **Show chart only** is selected.  |
| **Display options** | **Show chart only**  | Rather than a list of records a chart is displayed.  |
| **Display options** | **Allow users to change chart**  | When **Show chart only** is selected, app users can change the chart displayed in the subgrid.  |
| **Display options** | **Maximum number of rows**  | Determines the maximum number of records to display in the subgrid. The minimum number of rows displayed is 2 and the maximum is 250.  |
| **Display options** | **Use available space** | Note: This property only works with the legacy web client. It has no effect on Unified Interface. <br/><br/>Determines whether the form allows space for two records and will expand the space as the number of records increases. If the number exceeds the **Maximum number of rows**, people can navigate to additional pages to view the records. If **Use available space** isn't chosen the form provides space for the number of records defined by **Maximum number of rows** and people can navigate to additional pages to view any additional records.  |
| **Formatting**  | **Component width**  | When the section containing the subgrid has more than one column, you can set the column to occupy up to the number of columns that the section has.  |

## See also

[Overview of the model-driven form designer](form-designer-overview.md)  

[Create, edit, or configure forms using the form designer](create-and-edit-forms.md)  

[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)  

[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
