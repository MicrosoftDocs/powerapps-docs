---
title: Configure a lookup component on a form"
description: Learn how to create a lookup for a form with Power Apps
ms.custom: ""
ms.date: 06/22/2026
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
# Configure a lookup component on a form  

Lookups help a user choose records from a **related** table. A lookup component is automatically added when a lookup column is added to a form.

For example, using a lookup component, you can open an account record that relates to a sales invoice record.

:::image type="content" source="media/form-designer-add-configure-lookup/lookup-matching-records.png" alt-text="Example of a lookup column for a teacher table":::

[Learn more about the lookup field user experience](../../user/lookup-field.md)

## Configure a lookup component

Makers configure a lookup component using the form designer.

1. While working in the form designer, select **New table** column. For **Data type**, select **Lookup** > **Lookup**.
1. Save the column to edit the properties. These properties are available to configure when using a lookup component on a form by using the form designer.

|Area  |Name  |Description  |
|---------|---------|---------|
| **Display options** | **Label** |  The label text that is displayed next to the lookup column. |
| **Display options**   | **Hide label**  | When enabled, the label isn’t displayed.  |
| **Display options**   | **Hide on phone**  | When enabled, the lookup column won’t display when running the app on a phone.  |
| **Display options**   | **Hide**  | Don’t display the lookup column. The lookup column can then be displayed using code.  |
| **Display options**   | **Lock**  | Make this column so that it can’t be removed by you or other makers until the **Lock** property is disabled.  |
| **Display options**   | **Read-only**  | When this property is enabled, users can’t change the value in the lookup column.  |
| **Display options**   | **Disable most recently used items**  | Disabling this option allows users to view recently used rows in the lookup dropdown list. Enabling this option disables the recent items.   |
| **Display options**   | **Use Main Form Dialog for Create**  | Enabling this option allows users to create rows in a pop out dialog for this lookup field, instead of closing the current form and navigating away.  |
| **Display options**   | **Use Main Form Dialog for Edit**  | Enabling this option allows users to edit rows in a pop out dialog for this lookup field, instead of closing the current form and navigating away.   |
| **Display options** | **Default view** |  The view of the table selected in the **Table** property that can be used to get and display the list of rows that app users can select in the lookup drop-down list. |
| **Display options** | **Allow users to change view** |  When selected, app users can change from the **Default view** to another view of the table. |
| **Display options** | **Show all views** |  When selected, app users can change from the **Default view** to all other views of the table selected in the **Table** property. <br /><br />This property is only available when **Allow users to change view** is selected. |
| **Display options** | **Selected views** |  A list of views of the table selected in the **Table** property that app users can change to from the **Default view**. <br /><br />This property is only available when **Allow users to change view** is selected and **Show all views** is unselected. |
| **Formatting**  | **Form field width**  | Determines the width in number of columns for the lookup column.  |
| **Filtering**  | **Filter by related rows**  | When this is enabled, you can filter this lookup based on a row related to both the current table and this lookup. The rows that display in this lookup when users search for a row will then have additional filtering applied. This helps provide more relevant searches when setting the value of the lookup. <br /><br />By default, this is turned off.  |
| **Filtering**  | **Relationship to current table** | This dropdown list defines the relationship from the table of the related row you want to filter by to the target lookup's table. <br /><br />The possible relationship combinations will be listed in the table following this one.  |
| **Filtering**  | **Relationship to this lookup’s table**  | This dropdown list defines the relationship from the table of the related row you want to filter by to the target lookup's table. <br /><br />For the possible relationship combinations, go to [Table relationships available for a lookup column](#possible-relationship-combinations-for-a-lookup-column).   |
| **Filtering**  | **Allow users to turn off filter**  | When this is enabled, users will have the option to turn off the filter you define here.  |
| **Components**  | **+Component** | Configure a control for the lookup column: <br/>- **[Form]( /power-apps/maker/model-driven-apps/form-component-control)**. Add the form component control that lets users edit related table records from the main form where the control resides. <br/> - Additional [lookup controls](#lookup-controls). Add additional functionality to the lookup column.
  |

### Lookup controls

There are a few lookup controls available with a lookup column. You might need to select **+ Component** > **Get more components** > **Add** to make the control available for your form.

- **Lookup (default)**. The default control when you create a lookup column. This control appears in the **Components** section when you add one of the other lookup controls. Select client type Web, Mobile, or Tablet. No other properties are available to configure. Add one of the following controls for extended functionality.
- **Lookup Control** (simple). Allows makers to disable the clickthrough behavior on the lookup column by disabling the **Lookup clickthrough** value. By default, lookup values in forms appear as hyperlinks, allowing users to open related records by selecting them so you might want to prevent users from navigating away from the current form.
- **Drawer Lookup Control**. This control is optimized for mobile and tablet and offers fewer clicks and a modern bottom sheet. It also allows makers to disable the clickthrough behavior on lookup fields by disabling the **Lookup clickthrough** value.
- **Look-up Control** (classic). This control has these two properties:
   - **Related Virtual Entity**. If there's a related table for the lookup that's a virtual table, you can bind to table column and add a static value.
   - **Virtual Entity Lookup View Id**. Add an identifier for the virtual table lookup view.

## Possible relationship combinations for a lookup column

|Relationship to current table (Related table > Current table) |Relationship to this lookup's table (Related table > Lookup's table) |Available?|
|-----------------------------|------------------------------|----------------|
|1:N|1:N|Yes|
|1:N|N:1|Yes|
|1:N|N:N|Yes|
|N:1|1:N|No|
|N:1|N:1|No|
|N:1|N:N|No|
|N:1|Self|Yes|
|N:N|1:N|No|
|N:N|N:1|No|
|N:N|N:N|No|
|N:N|Self|Yes|

## See also

[Overview of the model-driven form designer](form-designer-overview.md)  

[Table relationships](../data-platform/create-edit-entity-relationships.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
