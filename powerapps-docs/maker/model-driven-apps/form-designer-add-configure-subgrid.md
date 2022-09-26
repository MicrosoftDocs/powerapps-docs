---
title: "Add and configure a subgrid component on a form | MicrosoftDocs"
description: Learn how to add a subgrid on a model-driven app form
ms.custom: ""
ms.date: 05/03/2022
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
tags: 
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Add and configure a subgrid component on a form

A form that displays the details of a table record can use a subgrid component to display a list of related or unrelated records in a tabular format. Makers can add and configure a subgrid component using the form designer.

## Add a subgrid component

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  
2. Expand **Data**, select **Tables**, select the table that you want, select the **Forms** area, and then edit the form you want.
   
   > [!note]
   > Customizations to a table should take place within a [solution](../model-driven-apps/model-driven-app-glossary.md#solution). To update a table within a solution, open your solution from the **Solutions** area, select the table, select the **Forms** area, and then edit the form you want.

3. Select **+Component** on the command bar. This can also be selected from the left pane.
4. Drag a **1 column section** from the layout area of the components menu onto the form.
5. Select **Subgrid** from the **Related Data** area of the components menu.

6. On the **Select subgrid views** pane:
   - Typically app users want to view related records. When **Show related records** is selected, only tables with a relationship are displayed.
   - Select the **Table** you want.
   - Select the **Default view** from the table. When an existing view is not suitable for the app, [create or edit a view](create-edit-views.md) for the table.
7. Select **Done**.
8. Select **Save**, and then select **Publish**.

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
| **Display options** | **Use available space** | *[Not supported in Unified Interface]*<br/>Determines whether the form will allow space for two records and will expand the space as the number of records increases. If the number exceeds the **Maximum number of rows**, people can navigate to additional pages to view the records. If **Use available space** is not chosen the form will provide space for the number of records defined by **Maximum number of rows** and people can navigate to additional pages to view any additional records.  |
| **Formatting**  | **Component width**  | When the section containing the subgrid has more than one column, you can set the column to occupy up to the number of columns that the section has.  |

## See also

[Overview of the model-driven form designer](form-designer-overview.md)  
[Create, edit, or configure forms using the form designer](create-and-edit-forms.md)  
[Add, configure, move, or delete columns on a form](add-move-or-delete-fields-on-form.md)  
[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)  
[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  
[Add, configure, move, or delete tabs on a form](add-move-or-delete-tabs-on-form.md)  
[Configure header properties in the form designer](form-designer-header-properties.md)  
[Add and configure a quick view component on a form](form-designer-add-configure-quickview.md)  
[Configure a lookup component on a form](form-designer-add-configure-lookup.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit columns](../data-platform/create-edit-field-portal.md)  


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
