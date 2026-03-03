---
title: "Properties available in the form designer"
description: Manage component properties available to you when using the form designer.
ms.custom: ""
ms.date: 03/02/2026
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: article
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
# Properties available in the form designer

Located on the right-pane of the model-driven form designer, the property pane lets an app maker quickly view and update the properties of any element selected from the preview or the tree view.

:::image type="content" source="media/form-designer-property-pane.png" alt-text="Form designer property pane.":::

## Form properties

|Name  |Description  |
|---------|---------|
|**Display Name**     | Enter a name that is meaningful to people. This name is shown to people when they use the form. If app users can use multiple forms configured for the table, they use this name to differentiate between available forms. <br /> This property is required.        |
|**Description**     |  Enter a description that explains how this form is different from other main forms. This description is only shown in the list of forms for a table in the solution explorer.        |
|**Max Width**     | Set a maximum width (in pixels) to limit the width of the form. The default value is 1900. <br /> This property is required.       |
|**Show image**      | Show the tables’s **Primary Image** if it has one set. This setting will enable showing the image column in the header of this form. <br /> See Enable or disable table options for more information about table options.         |

## Tab properties

|Area   |Name  |Description  |
|---------|---------|---------|
|**Display options**      | **Label**      | The localizable label for the tab visible to users. <br /> This property is required.         |
| **Display options**      |  **Name**     |  The unique name for the tab that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores. <br />This property is required.      |
| **Display options**      |  **Expand this tab by default**      |  The tab state can toggle between expanded or collapsed using form scripts or by people selecting the label. Choose the default state for the tab.       |
| **Display options**      | **Hide tab**     | When selected, tab is hidden by default and can be shown using code.       |
| **Display options**      | **Hide on phone**     |  For a condensed version of this form on phone screens, tabs can be hidden.     |
| **Formatting**   | **Layout**     |  Tabs can have up to three columns. Use these options to set the number of tabs and what percentage of the total width they should fill.      |

## Section properties

|Area   |Name  |Description  |
|---------|---------|---------|
|**Display options**      | **Label**    | The localizable label for the section visible to users. <br /> This property is required.      |
|**Display options**      | **Name**    | The unique name for the section that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores. <br /> This property is required.        |
|**Display options**      | **Hide label**   |  When selected, the section label is hidden.  |
|**Display options**      | **Lock**    | Lock this section to keep it from being removed.      |
|**Display options**      | **Hide**     | When selected, section is hidden by default and can be shown using code.      |
|**Display options**      | **Hide on phone**     |  For a condensed version of this form on phone screens, sections can be hidden.     |
|**Formatting**     |  **Columns**    |  Specify up to four columns to be in the section.      |

## Column properties

|Area  |Name  |Description  |
|---------|---------|---------|
|**Display options**     | **Label**  | The localizable label for the column that displays the name of the column.     |
|**Display options**     | **Hide label**     | When selected, the column label is hidden.      |
|**Display options**     | **Read-only**    | When selected, the column value is not editable.      |
|**Display options**     |  **Lock**   |  Lock this column to keep it from being removed.     |
|**Display options**     |  **Hide**     | When selected, column is hidden by default and can be shown using code.      |
|**Display options**     |  **Hide on phone**    | For a condensed version of this form on phone screens, columns can be hidden.         |
|**Formatting**     | **Form field width**      |  Columns, or form fields, exist within sections and sections can be divided into columns. When the section containing the record columns has more than one column, the number of section columns that the record column can occupy can be set with the maximum being the total number of section columns specified in the section properties.       |

## See also

[Overview of the model-driven form designer](form-designer-overview.md)  
[Create, edit, or configure forms using the form designer](create-and-edit-forms.md)  
[Add, configure, move, or delete columns on a form](add-move-or-delete-fields-on-form.md)  
[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)  
[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  
[Add, configure, move, or delete tabs on a form](add-move-or-delete-tabs-on-form.md)  
[Configure header properties in the form designer](form-designer-header-properties.md)  
[Add and configure a subgrid component on a form](form-designer-add-configure-subgrid.md)  
[Add and configure a quick view component on a form](form-designer-add-configure-quickview.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit columns](../data-platform/create-edit-field-portal.md)  


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
