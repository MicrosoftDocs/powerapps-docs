---
title: Model-driven app common column properties in Power Apps | MicrosoftDocs
description: Understand how to view the common column properties for a main form.
Keywords: Main form; Common column properties; Dynamics 365
author: Mattp123
ms.subservice: mda-maker
ms.author: matp
manager: kvivek
ms.date: 02/25/2020
ms.service: powerapps
ms.topic: conceptual
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: 2b91ee28-7f09-435e-9fae-5225aa698e22
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Model-driven app common column properties

Common properties of table columns for a model-driven app can be viewed using the Power Apps portal or the Power Apps solution explorer. The Power Apps portal provides an easy way to create and edit table columns with the Microsoft Dataverse.

The portal enables configuring the most common options, but certain options can only be set using solution explorer.

In addition to configuring aspects of the Dataverse column, such as its type and whether or not it is required, it is possible to configure aspects of how the column is used in the context of a [form](model-driven-app-glossary.md#form).  This approach allows for different forms to permit users to have different interactions with the data column.

## Common column properties in Power Apps portal

1. From the Power Apps portal found at [make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Data** > **Tables** and select the table that has the columns you want to view.

> [!note]
> Many customisations to a table take place within [solutions](../model-driven-apps/model-driven-app-glossary.md#solution).  To update a table within a solution first navigate to your **solution**, then select the **table** followed by the **views** tab.

2. Select the column that you want to view.

    > [!div class="mx-imgBorder"]
    > <img src="media/common-field-prop-powerapps.png" alt="Common column properties in Power Apps portal" height="658" width="300">

The following table describes the common properties of columns. Certain types of columns have special properties. These are described in [Create and edit columns for Dataverse](../data-platform/create-edit-field-portal.md).

 |Property|Description|
 |--|--|
 |**Display Name**|The text to be displayed for the column in the user interface.|
 |**Name**|The unique name across your environment. A name will be generated based on the display name that has been entered, however this can be edited before saving. Once a column is created the name cannot be changed as it may be referenced in your applications or code. The name will have the customization prefix for the **Dataverse Default Publisher** prepended to it.|
 |**Data type**|Controls how values are stored as well as how they are formatted in some applications. Once a column is saved, it is not possible to change the data type with the exception of converting text columns to autonumber columns.|
 |**Required**| A row can't be saved without data in this column. |
 |**Searchable**| This column appears in Advanced Find and is available when customizing views. |
 |**Calculated or Rollup**| Use to automate manual calculations. Use values, dates, or text.|
 |**Advanced Options**| Add a description, and specify a maximum length and IME mode for the column.

There are many different types of columns, but it is only possible to create some of them. For more information about all types of columns, see [Types of columns and column data types](../data-platform/types-of-fields.md). Additional options depending on the choice of **Data type**.

## Common column properties in solution explorer

In addition to using the Power Apps Portal columns can also be reviewed using the solution explorer.

[!INCLUDE [cc_navigate-solution-from-powerapps-portal](../../includes/cc_navigate-solution-from-powerapps-portal.md)]

### Navigate to a column for a table using the solution explorer

To update the column the following steps need to be performed.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
1. On the left navigation pane, expand **Data**, and then select **Tables**.
    > [!note]
    > Many customisations to a table take place within [solutions](../model-driven-apps/model-driven-app-glossary.md#solution).  To update a form within a solution first navigate to your **Solution**, then select the **Table** followed by the **Forms** tab.

1. Select a table, such as the account table.

1. Select three dots in the command menu and select **switch to classic**.

1. Select **switch to classic**.  The table will open using the classic experience.
    >[!note]
    >In the solution explorer tables are known as entities and columns are known as fields.

1. Select the column where an updated experience is required.
1. Select **change properties** from the top menu or simply double click the field.

   ![Common column properties in solution explorer.](media/common-field-properties.png "Common form data column properties in solution explorer")

1. Make the necessary property changes (see the classic editor field properties options) then select **OK**.
1. **Save** and **Publish** the form.

## Field properties within the classic editor

There are 6 tabs shown for a field.  Display, Formating, Details, Events, Business Rules and Components.
  
The following table describes properties that all columns have. Certain types of columns have special properties. These are described in [Special column properties](special-field-properties-legacy.md).  
  
|Tab|Property|Description|  
|---------|--------------|-----------------|  
|**Display**|**Label**|**Required**: By default the label will match the display name of the column. The name for the form can be overridden by entering a different label here.|  
||**Display label on the form**|This contains the option not to display the label at all.|  
||**Field Behavior**|Specify the column level behavior using the check boxes.|  
||**Locking**|This will prevent the column from being removed from the form accidentally. This will prevent any configuration applied to the column, such as event handlers, from being cleared if the column were removed. To remove this column a customizer would need to clear this setting first.|  
||**Visibility**|Showing the column is optional and can be controlled using scripts. More information: [Visibility options](visibility-options-legacy.md)|  
||**Availability**|Choose if you want the tab to be available on the phone.|
|**Formatting**|**Select the number of fields the control occupies**|When the section containing the columns has more than one column this can set the column to occupy up to the number of columns that the section has.|  
|**Details**|**Display Name**, **Name**, and **Description**|These read-only columns are for reference. Click the **Edit** button for convenient access to the column definition if you want to edit it.<br /><br /> Each instance of a column in the form has a name property so that they can be referenced in form scripts, but this name is managed by the application. The first instance of the column is the name of the column specified when it was created. More information: [Create and edit columns](../data-platform/create-edit-fields.md)<br /><br /> For each additional time that a column is included in a form, the name appends a number starting with 1 to the end. So if the column name is 'new_cost', the first instance is 'new_cost', the second is 'new_cost1', and so on for each instance of the column in the form.<br /><br />**Note:** The column **Description** value provides tooltip text for the column when people place their cursor over it.|  
|**Events**|**Form Libraries**|Specify any JavaScript web resources that will be used in the column `OnChange` event handler.<br /><br />|  
||**Event Handlers**|Configure the functions from the form libraries that should be called for the column `OnChange` event. More information: [Configure Event Handlers](configure-event-handlers-legacy.md)|  
|**Business Rules**|**Business Rules**|View and manage any business rules that reference this column. More information: [Create business rules and recommendations](create-business-rules-recommendations-apply-logic-form.md)|  
|**Controls**|**Controls**|Add controls and specify their availability on Web, Phone and Tablet .|  

## Editing form level column properties

In some scenarios it is desirable to be able to render a data column within a form field in one form in a way that differs to the way in which it is presented in another form.  This allows the user experience to be tailored to the individual using the form.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. On the left navigation pane, expand **Data**, and then select **Tables**.
> [!note]
> Many customisations to a table take place within [solutions](../model-driven-apps/model-driven-app-glossary.md#solution).  To update a form within a solution first navigate to your **Solution**, then select the **Table** followed by the **Forms** tab.

3. Select a table, such as the account table, and then select the **Forms** tab.

4. Select the form where customisations are required.

5. Select **switch to classic**.  The form will open using the classic experience.
6. Select the form field where an updated experience is required.
7. Select **change properties** from the top menu or simply double click the field.

  ![Common column properties in solution explorer.](media/common-field-properties.png "Common form data column properties in solution explorer")

8. Make the necessary changes then select **OK**.
9. **Save** and **Publish** the form.

## Next steps

[Overview of special column properties](special-field-properties-legacy.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]