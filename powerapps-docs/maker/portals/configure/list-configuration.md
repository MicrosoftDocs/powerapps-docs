---
title: List configuration
description: Learn how to configure lists on a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 05/27/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---

# List configuration

You can easily enable and configure actions (create, edit, delete, and so on) for records in a list. It's also possible to override default labels, sizes, and other attributes so that the list will be displayed exactly the way you want.

These settings are found on the **Options** tab in the **Grid Configuration** section of the list configuration in the [Portal Management app](configure-portal.md). By default, only **Basic Settings** are shown. Select **Advanced Settings** to see more settings.

:::image type="content" source="media/lists/configure-entitylist.png" alt-text="Configure a list."::: 

**Attributes**

|Name                   |Description|
|---------------------------|-----------|
|**Basic Settings**         |   |
| View Actions              |Use to add action buttons for actions that are applicable for the table set and will appear above the grid. The available actions are: <ul><li>Create</li> <li>Download</li></ul> Selecting one of these options displays a configuration area for that action.|
| Items Actions             |Use to add action buttons for actions that are applicable for an individual record and will appear for each row in the grid, provided the appropriate privilege has been granted by Table Permissions. The actions generally available are:<ul><li>Details</li><li>Edit</li><li>Delete</li><li>Workflow</li><li>Activate</li><li>Deactivate</li></ul> Selecting one of these options displays a configuration area for that action. See below for details about each action. Furthermore, certain tables have special actions that are available to them on a per-table basis:<ul><li>Calculate Value of Opportunity (opportunity)</li><li>Cancel Case action (incident)</li><li>Close (resolve) Case action (incident)</li><li>Convert Quote to Order (quote)</li><li>Convert Order to Invoice (sales order)</li><li>Generate Quote from Opportunity (opportunity)</li><li>Lose Opportunity action (opportunity)</li><li>Win Opportunity action (opportunity)</li><li>Reopen Case action (incident)</li><li>Set Opportunity on Hold (opportunity)</li></ul>|
| Override Column Attributes|Use to override display settings for individual columns in the grid.<ul><li>Attribute: Logical name of the column you want to override</li><li>Display Name: New column title to override the default</li><li>Width: Width (in either percent or pixels) of the column to override the default. See also Grid Column Width Style</li></ul> To override settings on a column, select **+ Column** and fill in the details.|
|**Advanced Settings**      |  |
| Loading Message           |Overrides the default HTML message that appears while the grid is loading.|
| Error Message             |Overrides the default HTML message that appears when an error occurs while loading the grid.|
| Access Denied Message     |Overrides the default HTML message that appears when a user doesn't have sufficient Table Permissions to view the list.|
| Empty Message             |Overrides the HTML message that appears when the grid contains no data.|
| Details Form Dialog       |Controls the settings for the dialog box that appears when a user activates the Details action.|
| Edit Form Dialog          |Controls the settings for the dialog box that appears when a user activates the Edit action.|
| Create Form Dialog        |Controls the settings for the dialog box that appears when a user activates the Create action.|
| Delete Dialog             |Controls the settings for the dialog box that appears when a user activates the Delete action.|
| Error Dialog              |Controls the settings for the dialog box that appears when an error occurs during any action.|
| CSS Class                 |Specify a CSS class or classes that will be applied to the HTML element that contains the entire grid area, including the grid and action buttons.|
| Grid CSS Class            |Specify a CSS class or classes that will be applied to the list's HTML \<table\> element.|
| Grid Column Width Style   |Configures whether the **Width** values in the Override Column Attributes are specified in **Pixels** or **Percent**.|

**General action settings**

In general, Table actions have settings that can be configured. In all cases, this is to give you more options in terms of customization, and the fields aren't required. Simply adding the action will allow the action to be taken on the portal, provided the appropriate privilege has been granted by Table Permissions.

Generally, you can configure the corresponding dialog box for each action, which will appear only if you select **Confirmation Required**.


| Name                   | Description                                                                                                                                                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Basic Settings**         |                                                                                                                                                                                                                               |
| Confirmation Required? | Determines whether a confirmation will prompt the user to confirm when the action is selected.                                                                                                                                 |
| **Advanced Settings**      |                                                                                                                                                                                                                               |
| Confirmation           | Overrides the confirmation HTML message displayed when the user activates the action.                                                                                                                                         |
| Button Label           | Overrides the HTML label for this action displayed in the list row.                                                                                                                                                    |
| Button Tooltip         | Overrides the tooltip text that appears when the user points to the button for this action displayed in the list row.                                                                                           |
| Button CSS Class       | Adds a CSS class to the button.                                                                                                                                                      |
| Redirect to Webpage    | Some actions (not all) allow a redirect upon completion of the action. Highly recommended for the Delete action, optional in most other cases, you can choose a webpage to redirect to when the action is completed. |
| Redirect URL           | An alternative to the **Redirect to Webpage** option&mdash;allows redirecting to a specific URL.                                                                                                                                   |

**General dialog box advanced settings**

|**Name**                 |**Description**                                                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Title                    | Overrides the HTML that appears in the title bar of the dialog box.|                                                                         
| Primary Button Text      | Overrides the HTML that appears in the Primary (Delete) button on the dialog box.                                                         |
| Close Button Text        | Overrides the HTML that appears in the Close (Cancel) button on the dialog box.                                                           |
| Dismiss Button Sr Text   | Overrides the screen reader text associated with the dialog box's Dismiss button.                                                           |
| Size                     | Specifies the size of the Delete dialog box. The Options are Default, Large, and Small. The default size is Default. |
| CSS Class                | Specify a CSS class or classes that will be applied to the resulting dialog box.                                                            |
| Tile CSS Class           | Specify a CSS class or classes that will be applied to the resulting dialog box's title bar.                                                |
| Primary Button CSS Class | Specify a CSS class or classes that will be applied to the dialog box's Primary (Delete) button.                                          |
| Close Button CSS Class   | Specify a CSS class or classes that will be applied to the dialog box's Close (Cancel) button.                                            |

**Create action settings**

Enabling a **Create Action** renders a button above the list that, when selected, opens a dialog box with a basic form that the user can use to create a new record, provided the Create privilege has been granted by Table Permissions.

| Name               | Description                          |
|--------------------|--------------------------------------|
| **Basic Settings**     |                                                                                                                                                                       |
| Basic Form     | Specifies the basic form that will be used to create the new record. The drop-down list will include all basic forms that are configured for the table type of the list. <br>**Note**: If the table type of the list has no basic forms, the drop-down list will appear empty. If no basic form is supplied for the Create action, it will be ignored and the button won't be rendered on the list. |
| **Advanced Settings**          |                                                                                                                                                                       |
| Button Label                                                                                                                                                                                                                 | Overrides the HTML label displayed in the Create action button above the list.                                                                                        |
| Button Tooltip                                                                                                                                                                                                               | Overrides the tooltip text that appears when the user points to the Create action button.                                                                         |

**Create Form dialog box advanced settings**

|**Name**               |**Description**                                                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Loading Message        | Overrides the message that appears while the dialog box is loading.                                                                                  |
| Title                  | Overrides the HTML that appears in the title bar of the dialog box.                                                                                  |
| Dismiss Button Sr Text | Overrides the screen reader text associated with the dialog box's Dismiss button.                                                                   |
| Size                   | Specifies the size of the Create Form dialog box. The Options are Default, Large, and Small. The default size is Large. |
| CSS Class              | Specify a CSS class or classes that will be applied to the resulting dialog box.                                                                    |
| Title CSS Class        | Specify a CSS class or classes that will be applied to the resulting dialog box's title bar.                                                        |

**Download action settings**

Enabling a **Download Action** renders a button above the list that, when selected, downloads the data from the list to an [!INCLUDE[pn-excel-short](../../../includes/pn-excel-short.md)] (.xlsx) file.

| Name              | Description                                                                                        |
|-------------------|----------------------------------------------------------------------------------------------------|
| **Basic Settings**    |                                                                                                    |
| None              |                                                                                                    |
| **Advanced Settings** |                                                                                                    |
| Button Label      | Overrides the HTML label displayed in the Download action button above the list.            |
| Button Tooltip    | Overrides the tooltip text that appears when the user points to the Download action button. |

**Details action settings**

Enabling a **Details Action** allows a user to view a read-only basic form of a selected row in the list.


|                 Name                  |                                                                                                                                                                                                                      Description                                                                                                                                                                                                                      |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          **Basic Settings**           |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|              Basic Form              | Specifies the basic form that will be used to view the details of the selected table. The drop-down list will include all basic forms that are configured for the table type of the list. <br> **Note**: If the table type of the list has no basic forms, the drop-down list will appear empty. If no basic form is supplied for the Details action, it will be ignored and the button won't be rendered in the list. |
|         **Advanced Settings**         |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Record ID Parameter Name |                                                                    Specifies the name of the Query String parameter that will be used to select the table to view in the selected basic form. This should match the value in that basic form's Record ID Parameter Name. The default value for this field, both here and in basic form configuration, is **id**.                                                                     |
|             Button Label              |                                                                                                                                                                                      Overrides the HTML label for this action displayed in the list row.                                                                                                                                                                                       |
|            Button tooltip             |                                                                                                                                                             Overrides the tooltip text that appears when the user points to the button for this action displayed in the list row.                                                                                                                                                              |

**Details dialog box advanced settings**

|**Name**               |**Description**                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Loading Message        | Overrides the HTML that appears when the dialog box is loading.                                                                             |
| Title                  | Overrides the HTML that appears in the title bar of the dialog box.                                                                         |
| Dismiss Button Sr Text | Overrides the screen reader text associated with the dialog box's Dismiss button.                                                           |
| Size                   | Specifies the size of the Details dialog box. The Options are Default, Large, and Small. The default size is Large. |
| CSS Class              | Specify a CSS class or classes that will be applied to the resulting dialog box.                                                            |
| Title CSS Class        | Specify a CSS class or classes that will be applied to the resulting dialog box's title bar.                                                |

**Edit action settings**

Enabling an **Edit Action** allows a user to view an editable basic form that is data-bound to the record of the selected row from the list, provided the Write privilege has been granted by Table Permissions.


|                 Name                  |                                                                                                                                                                                                             Description                                                                                                                                                                                                             |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          **Basic Settings**           |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|              Basic Form              | Specifies the basic form that will be used to edit the selected table. The drop-down list will include all basic forms that are configured for the table type of the list. <br> **Note**: If the table type of the list has no basic forms, the drop-down list will appear empty. If no basic form is supplied for the Edit action, it will be ignored and the button won't be rendered in the list. |
|         **Advanced Settings**         |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Record ID Parameter Name |                                                           Specifies the name of the Query String parameter that will be used to select the table to edit in the selected basic form. This should match the value in that basic form's Record ID Parameter Name. The default value for this field, both here and in basic form configuration, is **id**.                                                            |
|             Button Label              |                                                                                                                                                                             Overrides the HTML label for this action displayed in the list row.                                                                                                                                                                              |
|            Button Tooltip             |                                                                                                                                                    Overrides the tooltip text that appears when the user points to the button for this action displayed in the list row.                                                                                                                                                     |

**Edit form dialog box advanced settings**

|**Name**               |**Description**                                                                                                                   |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Loading Message        | Overrides the HTML that appears when the dialog box is loading.                                                                       |
| Title                  | Overrides the HTML that appears in the title bar of the dialog box.                                                                   |
| Dismiss Button Sr Text | Overrides the screen reader text associated with the dialog box's Dismiss button.                                                     |
| Size                   | Specifies the size of the Edit dialog box. The Options are Default, Large, and Small. The default size is Large. |
| CSS Class              | Specify a CSS class or classes that will be applied to the resulting dialog box.                                                      |
| Title CSS Class        | Specify a CSS class or classes that will be applied to the resulting dialog box's title bar.                                          |

**Delete action settings**

Enabling a **Delete Action** allows a user to permanently delete the record of the selected row from the list, provided the Delete privilege has been granted by Table Permissions.

| Name              | Description                                                                                                                         |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Basic Settings**    |                                                                                                                                     |
| none              |                                                                                                                                     |
| **Advanced Settings** |                                                                                                                                     |
| Confirmation      | Overrides the confirmation HTML message displayed when the user activates the Delete action.                                        |
| Button Label      | Overrides the HTML label for this action displayed in the list row.                                                          |
| Button Tooltip    | Overrides the tooltip text that appears when the user points to the button for this action displayed in the list row. |

**Delete dialog box (advanced) settings**

|**Name**                 |**Description**                                                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Title                    | Overrides the HTML that appears in the title bar of the dialog box.                                                                         |
| Primary Button Text      | Overrides the HTML that appears in the Primary (Delete) button on the dialog box.                                                         |
| Close Button Text        | Overrides the HTML that appears in the Close (Cancel) button on the dialog box.                                                           |
| Dismiss Button Sr Text   | Overrides the screen reader text associated with the dialog box's Dismiss button.                                                           |
| Size                     | Specifies the size of the Delete dialog box. The Options are Default, Large, and Small. The default size is Default. |
| CSS Class                | Specify a CSS class or classes that will be applied to the resulting dialog box.                                                            |
| Title CSS Class          | Specify a CSS class or classes that will be applied to the resulting dialog box's title bar.                                                |
| Primary Button CSS Class | Specify a CSS class or classes that will be applied to the dialog box's Primary (Delete) button.                                          |
| Close Button CSS Class   | Specify a CSS class or classes that will be applied to the dialog box's Close (Cancel) button.                                            |

**Workflow action settings**

Enabling a **Workflow action** allows a user to run an on-demand workflow against the record of the selected row from the list. You may add any number of Workflow actions to the list.


|         Name          |                                                                                                                                                           Description                                                                                                                                                           |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Basic Settings**   |                                                                                                                                                                                                                                                                                                                                 |
|       Workflow        | Specifies the on-demand workflow that will run when the user activates this action. <br> **Note**: If the table type of the list has no workflows, the drop-down list will appear empty. If no workflow is supplied for the Workflow action, it will be ignored and the button won't be rendered in the list. |
|     Button Label      |                                                                                                                 Sets the HTML label for this action displayed in the list row. This setting is required.                                                                                                                 |
| **Advanced Settings** |                                                                                                                                                                                                                                                                                                                                 |
|    Button Tooltip     |                                                                                                  Overrides the tooltip text that appears when the user points to the button for this action displayed in the list row.                                                                                                   |

### See also

- [Work with lists](entity-lists.md)
- [Display multiple Dataverse records using lists](/learn/modules/portals-access-data-platform/2-entity-lists)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)
