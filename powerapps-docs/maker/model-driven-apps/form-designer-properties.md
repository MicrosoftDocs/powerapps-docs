---
title: "Properties available in the form designer | MicrosoftDocs"
description: Manage component properties using the form designer.
ms.custom: ""
ms.date: 08/26/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
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

# Properties available in the form designer

Located on the right-pane of the model-driven form designer, the property pane lets you quickly view and update the properties of any element selected from the preview or the tree view. 

> [!div class="mx-imgBorder"] 
> ![Form designer property pane](media/form-designer-property-pane.png "Form designer property pane")

## Form properties

|Name  |Description  |
|---------|---------|
|**Title**     | Enter a name that will be meaningful to people. This name will be shown to people when they use the form. If they can use multiple forms configured for the table they will use this name to differentiate between available forms. <br /> This property is required.        |
|**Description**     |  Enter a description that explains how this form is different from other main forms. This description is only shown in the list of forms for a table in the solution explorer.        |
|**Max Width**     | Set a maximum width (in pixels) to limit the width of the form. The default value is 1900. <br /> This property is required.       |
|**Show image**      | Show the tables’s **Primary Image** if it has one set. This setting will enable showing the image column in the header of this form. <br /> See Enable or disable table options for more information about table options.         |


## Tab properties

|Area   |Name  |Description  |
|---------|---------|---------|
|**Display options**      | **Tab label**      | The localizable label for the tab visible to users. <br /> This property is required.         |
| **Display options**      |  **Name**     |  The unique name for the tab that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores. <br />This property is required.      |
| **Display options**      |  **Expand this tab by default**      |  The tab state can toggle between expanded or collapsed using form scripts or by people selecting the label. Choose the default state for the tab.       |
| **Display options**      | **Hide tab**     | When selected, tab is hidden by default and can be shown using code.       |
| **Display options**      | **Hide on phone**     |  For a condensed version of this form on phone screens, tabs can be hidden.     |
| **Formatting**   | **Layout**     |  Tabs may have up to three columns. Use these options to set the number of tabs and what percentage of the total width they should fill.      |


## Section properties

|Area   |Name  |Description  |
|---------|---------|---------|
|**Display options**      | **Section label**    | The localizable label for the section visible to users. <br /> This property is required.      |
|**Display options**      | **Name**    | The unique name for the section that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores. <br /> This property is required.        |
|**Display options**      | **Hide label**   |  When selected, the section label is hidden.  |
|**Display options**      | **Lock section**    | Lock this section to keep it from being removed.      |
|**Display options**      | **Hide section**     | When selected, section is hidden by default and can be shown using code.      |
|**Display options**      | **Hide on phone**     |  For a condensed version of this form on phone screens, sections can be hidden.     |
|**Formatting**     |  **Columns**    |  Specify up to four columns to be in the section.      |

## Column properties

|Area  |Name  |Description  |
|---------|---------|---------|
|**Display options**     | **Column label**    | By default the label will match the display name of the column. You can override that name for the form by entering a different label here.       |
|**Display options**     |  **Column name**    | The name of the column. This comes from the column properties on the table and is read-only.     |
|**Display options**     | **Hide label**     | When selected, the column label is hidden.      |
|**Display options**     | **Read-only column**    | When selected, the column value is not editable.      |
|**Display options**     |  **Lock column**   |  Lock this column to keep it from being removed.     |
|**Display options**     |  **Hide column**     | When selected, column is hidden by default and can be shown using code.      |
|**Display options**     |  **Hide on phone**    | For a condensed version of this form on phone screens, columns can be hidden.         |
|**Formatting**     | **Column width**      |  When the section containing the columns has more than one column you can set the column to occupy up to the number of columns that the section has.       |

## See also
[Overview of the model-driven form designer](form-designer-overview.md)  
[Create, edit, or configure forms using the form designer](create-and-edit-forms.md)  
[Add, configure, move, or delete columns on a form](add-move-or-delete-fields-on-form.md)  
[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)  
[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  
[Add, configure, move, or delete tabs on a form](add-move-or-delete-tabs-on-form.md)  
[Configure header properties in the form designer](form-designer-header-properties.md)  
[Add and configure a sub-grid component on a form](form-designer-add-configure-subgrid.md)  
[Add and configure a quick view component on a form](form-designer-add-configure-quickview.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit columns](../data-platform/create-edit-field-portal.md)  


[!INCLUDE[footer-include](../../includes/footer-banner.md)]