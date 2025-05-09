---
title: Subgrid properties for model-driven app main forms in Power Apps | MicrosoftDocs
description: Understand the Sub-Grid properties for main forms
Keywords: Main form; Sub-Grid properties; Dynamics 365
author: Mattp123
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.subservice: mda-maker
ms.author: matp
ms.date: 09/26/2022
ms.topic: article
ms.assetid: 82892cd3-3436-4677-b96b-f2ccd0a4f078
search.audienceType: 
  - maker
---
# Subgrid properties for model-driven app main forms (classic)

This article describes the classic form editor.

We recommend that you use the **modern form designer** to create and edit subgrids for model-driven app forms. More information: [Add and configure a subgrid component on a form](form-designer-add-configure-subgrid.md)

A subgrid exists within a main form and let app users view data within a Dataverse table, typically related to the record currently being reviewed.

:::image type="content" source="media/sub-grid-form.png" alt-text="Form sub-grid":::

A subgrid on a form can be configured using the classic form designer to display a list of records or a chart. Select **Show Chart Only** on the **Display** tab to show a chart instead of a list.

  > [!div class="mx-imgBorder"] 
  > ![sub-grid properties for show chart only.](media/sub-grid-properties.png "sub-grid properties for show chart only")

These are the properties available to configure when using a subgrid component on a form using the classic form designer.

|Tab|Property|Description|  
|---------|--------------|-----------------|  
|**Display**|**Name**|**Required**: The unique name for the subgrid that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores.|  
||**Label**|**Required**: The localizable label for the subgrid visible to users.|  
||**Display label on the Form**|Whether the label should be displayed on the form. This is required if you enable **Display Search Box**. You can also choose to have the panel header color.|  
||**Records**|Choose from two options:<br /><br /> - **Only Related Records**: Subgrid will display only records related to the current record.<br />- **All Record Types**: Subgrid will display records filtered only by the default view or, if the view selector is enabled, any views the user chooses.<br /><br /> The option you choose will affect the behavior of the show list control. More information: [Show list behavior](#show-list-behavior) |  
||**Table**|Depending on the option you choose for **Records**, this list displays either:<br /><br /> - **Only Related Records**: A list of tables that are related to this table with the name of the lookup column on that table, which defines the relationship in parentheses.<br />- **All Record Types**: A list of all tables.|  
||**Default View**|Choose the view that will be applied by default. If you do not enable any other views using the **View Selector** property. This will be the only view.<br /><br /> Use the **Edit** button to open the default view for editing. Use the **New** button to create a new view to use for this subgrid.|  
||**Display Search Box**|Display the search box. When this option is chosen the **Display Label on the Form** option is required.|  
||**Display Index**|Only forms using the [Classic forms](main-form-presentations.md#classic-forms) support display index.<br /><br /> Select this check box if you want the alphabetical index to be available with the list. This lets you jump to records starting with a particular letter or number.|  
||**View Selector**|You have three options:<br /><br /> - **Off**: Only the default view can be used.<br />- **Show All Views**: Allow people to choose any view.<br />- **Show Selected Views**: Use the Ctrl key with your cursor to select which of the available views to show.|  
||**Default Chart**|Select which chart to show if **Show Chart Only** is selected.|  
||**Show Chart Only**|Rather than a list of records a chart will be displayed.|  
||**Display Chart Selection**|If **Show Chart Only** is selected, allow people to choose different charts.|  
||**Availability**|Specify whether the section should be available on phone.|
|**Formatting**|**Layout**|**Select the number of columns the control occupies**.<br /><br /> When the section containing the subgrid has more than one column, you can set the column to occupy up to the number of columns that the section has.|  
||**Number of rows**| Determines how many records are shown on a page of a subgrid.|  
||**Use available space**| Note: This property only works with the legacy web client. It has no effect on Unified Interface. <br/><br/> If **Automatically expand to use available space** is chosen, the form will allow space for two records and will expand the space as the number of records increases. If the number exceeds the **Number of Records**, users can navigate to additional pages to view the records.<br /><br /> If **Automatically expand to use available space** is not chosen, the form will provide space for the number of records defined by **Number of rows** and users can navigate to additional pages to view any additional records.|  
|**Controls**|**Controls**|Choose to add controls and select the radio button to have them for Web, Phone, or Tablet.|
  
 In forms using the [classic forms](main-form-presentations.md#classic-forms), actions performed on a subgrid were available in the ribbon. Developers can customize the behavior of these actions or add additional actions by customizing the ribbon.  
  
 In forms using the [current forms](main-form-presentations.md#main-form-presentation-options) actions for subgrids are placed near the subgrid, making them easier to access. However the command bar does not allow for custom actions to be added. Developers can edit the ribbon to modify the actions for the remaining three actions: show list, add record, and delete record.  
  

## Show list behavior

When displaying a list in forms with the [current forms](main-form-presentations.md#main-form-presentation-options), each subgrid displays the **Open View** button ![Open view button.](media/crm-itpro-cust-openview.PNG "Open view button") in the top-right when the table is also displayed as one of the tables included in the navigation area of the form editor. Choosing this button will open the view. The behavior will change depending on the option chosen for the **Records** property.  
  
 When you select **Only Related Records** the view will open using one of the associated views in the same window. To return to the form, use the back button or choose the current record primary name value in the navigation bar.  
  
 When you select **All Record Types** the view will open in a new window.  

## Add record behavior  
 When displaying a list in forms with the [current forms](main-form-presentations.md#main-form-presentation-options), each subgrid displays the **Add record** button ![Add button.](media/crm-itpro-cust-subgridadd.PNG "Add button") in the top-right side of the subgrid. Choosing this button will allow you to add a record. This behavior will change depending on the option chosen for the **Records** property and if the lookup is for activity records.  
  
 When you select **Only Related Records** the default behavior is the behavior to add existing records. People see an in-line lookup to search for an existing record first. This helps prevent creating duplicate records.  If they can't find an existing record, they can choose the **New** option. When a new record is created any of the column mappings defined in the relationship will be applied. More information: [Map table columns](../data-platform/map-entity-fields.md)   
  
 When you select **All Record Types** the default behavior is to add a new record. The quick create form will be shown if the target table has one. If not, the default table main form is shown.  
  
 If the subgrid displays activities, people will first need to choose the type of activity and then they will see the "add new record" behavior.  
  
## Delete record behavior  
 When you select a record in a subgrid the **Delete** button ![Sublist delete icon.](media/crm-itpro-cust-subgriddelete.PNG "Sublist delete icon") appears on the right side of the record. The behavior of this delete action is different depending on the type of relationship with the current table.  
  
 When the subgrid uses a 1:N (one-to-many) relationship, the normal record delete behavior is to show a confirmation dialog before deleting the record.  
  
 When the subgrid uses a N:N (many-to-many) relationship, the record in the relationship (or intersect) table relating to two records is deleted without a confirmation and the record will no longer be displayed in the subgrid. But the record that was displayed is not deleted.  

## Next steps

[Use the Main form and its components](use-main-form-and-components.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
