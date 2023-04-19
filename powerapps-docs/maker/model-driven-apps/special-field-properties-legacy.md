---
title: Model-driven app special column properties for main forms in Power Apps | MicrosoftDocs
description: Understand the special column properties for main forms
Keywords: Main forms; Special column properties; Dynamics 365
author: Mattp123
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.subservice: mda-maker
ms.author: matp
ms.date: 06/06/2018
ms.topic: overview
ms.assetid: 6ad7e43c-b6a1-48c4-9dfb-ed830142a841
search.audienceType: 
  - maker
---
# Overview of model-driven app special column properties

 All columns have the properties listed in [Common column properties](common-field-properties-legacy.md), but certain columns have additional properties, such as this entitlement column that can be opened from the main form for the case table.  

![special-properties-dialog.](media/special-properties.png)

> [!NOTE]
> This article describes properties for the classic experience. For information about lookup column properties in the modern for designer, go to [Configure a lookup component on a form](form-designer-add-configure-lookup.md).
  
<a name="BKMK_LookupFieldProperties"></a>  

## Lookup column properties  
  
> [!NOTE]
> The options described in the table below are available only for single-table lookup columns.  
  
|Section|Property|Description|  
|-------------|--------------|-----------------|  
|**Related Records Filtering**|**Only show records where**|When this is enabled, the records that display when users search for a record will have additional filtering applied. This helps provide more relevant searches when setting the value of the lookup.<br /><br /> By default, this is turned off.<br /><br /> The relationship combinations that are possible when you filter related records are listed in the table following this one.<br /><br /> The first list is populated with all the potential relationships you can use to filter this lookup. Select one.<br /><br /> The second list is then populated with all relationships that connect the related table (selected in first list) to the target table. Select one.<br /><br /> Select the **Allow users to turn off filter** check box to give users the option to turn off the filter you define here.<br /><br /> When users select the **Look Up More Records** option while setting the value for a lookup, they see this dialog box.<br /><br /> ![look-up-more-records.](media/crm-ua-v-8-1-look-up-more-records.png) <br /><br /> If you’ve selected the **Allow users to turn off filter** option while configuring the lookup column, users will see the check box to turn off the filter.  This makes it possible for them to see a wider range of records. If you want to make sure that users only see a limited range of records defined by this filter, clear the  **Allow users to turn off filter** check box.|  
|**Additional Properties**|**Display Search Box in lookup dialog**|You can choose not to display the search box in the lookup dialog.|  
||**Default View**|This view is used to filter the results of the inline search and set the default view shown in the lookup dialog when users select the **Look Up More Records** option.<br /><br /> The default view also controls which columns are included in the inline lookup.<br /><br /> For lookups that only allow selection of a single table type, the columns displayed in the inline lookup are set to be the first two columns included in the default view. In this example, **Main Phone** and **Email** are the first two columns in the default view configured for an account lookup.<br /><br /> For system lookups that allow for multiple table types, the first two columns of the table lookup view are shown.|  
||**View Selector**|You can choose from three options:<br /><br /> -   **Off**: Don’t allow users to choose a different view.<br />-   **Show All Views**: All views are available.<br />-   **Show Selected Views**: When you choose this option you can use the Ctrl key and your cursor to choose which views to show. The Lookup view for the table can’t be de-selected.|  
  
### Possible relationship combinations
  
|First list relationship|Second list relationship|Available?|
|-----------------------------|------------------------------|----------------|
|N:1|1:N|Yes|
|N:1|N:1|Yes|
|N:1|N:N|Yes|
|1:N|1:N|Yes|
|1:N|N:1|No|
|1:N|N:N|No|
|N:N|1:N|Yes|
|N:N|N:1|No|
|N:N|N:N|No|
  
<a name="BKMK_TwoOptionProperties"></a>   

### Yes/No column properties  
 On the formatting tab, Yes/No columns have the following formatting choices:  
  
- **Two radio buttons**: Two labeled controls with labels. Only one may be selected.  
  
- **Checkbox**: A single checkbox to set the true value, otherwise false.  
  
- **List**: A drop-down list containing both values.  
  
<a name="BKMK_MultipleLinesOfTextProperties"></a>   

### Multiple lines of text column properties

Multiple lines of text and single line of text columns that use the `Text Area` format have a **Record Layout** property. With this property you can specify a value for **Number of Records** or select **Automatically expand to use available space**.  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
