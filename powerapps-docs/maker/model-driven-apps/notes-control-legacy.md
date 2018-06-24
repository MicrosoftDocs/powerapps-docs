---
title: "Set up the Notes control to access information about posts (Dynamics 365 Customer Engagement) | MicrosoftDocs"
ms.custom: ""
ms.date: 05/06/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: f10cdf1c-3540-439c-a171-27a10e72da45
caps.latest.revision: 63
ms.author: "matp"
manager: "kvivek"
---
# Set up the Notes control to access information about posts

 In PowerApps forms for certain system entities using the [Updated forms](main-form-presentations.md#updated-forms),  the Notes control provides the ability to access information about **Posts**, **Activities**, and **Notes**. For custom entities where you have enabled notes and activities, you will only see **Notes** and **Activities**. To include **Posts** you must enable them for the custom entity.  
  
## Enable posts for a custom entity  
  
1.  Go to **[Settings](advanced-navigation.md#settings)** > **Activity Feeds Configuration**. 
  
2.  Open the record for your custom entity.  
  
3.  Make sure that **Enable walls for this type of record form** is selected and save the record.  
  
4.  In the command bar, select **Activate**.  
  
5.  If you needed to enable walls, you need to publish the entity.  
  
 By default, for system entities the notes control is positioned in a social pane section in the center of a three column tab at the top of the form. It can appear in a form just one time. You can move or remove the notes control. To add it back, use the **Notes** button in the **Control** group of the **Insert** tab.  
  
 The following table describes the properties for the Notes control.  
  
|Tab|Property|Description|  
|---------|--------------|-----------------|  
|**Display**|**Label**|**Required**: Although the label is not displayed by default, a label is required.|  
||**Display Label on the form**|You can choose to display the label.|  
||**Lock the field on the form**|This will prevent the notes from being removed from the form accidentally.|  
||**Default tab**|Select which tab should be displayed by default. The options are:<br /><br /> - **Activities**<br />- **Posts**<br />- **Notes**|  
|**Formatting**|**Select the number of columns the control occupies**|When the section containing the notes control has more than one column you can set the field to occupy up to the number of columns that the section has.|  
||**Number of Rows**|Control the height of the notes control by selecting the number of rows the control occupies.|  
||**Automatically expand to use available space**|Instead of setting the height by a number of rows, you can allow the notes control height to expand to available space.|  
  
## Next steps
[Open the form editor](open-form-editor.md)
