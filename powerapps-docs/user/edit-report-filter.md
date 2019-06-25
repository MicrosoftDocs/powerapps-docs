---
title: Edit the default filter of a report| Microsoft Docs
description: Edit the default filter of a report
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 06/25/2019
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
Edit the default filter of a report

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]

If you’ve created a custom report outside of the system, you can easily add it to PowerApps.

1. In the site map, choose Reports. 

2. Choose a report and on the commbar bar, select **Edit Default Filter**.
  
3. Modify the filter criteria.  
  
    The criteria are grouped by record types that you can use in the filter, such as **Accounts** or **Contacts**.  
  
   ### To edit an existing row
   1. Select the query relational operator and select an operator, or Select the underlined value and enter a new value.  
  
   2.Select the query relational operator, and select an operator.  
  
   To add a criteria row:  

   1.  Select **Select**, and specify the field to filter on.  

   2.  Select the query relational operator, and select an operator.  

   3.  Select **Enter Value**, and enter a value to filter on. For some values, you can select the **Select or change the values for this field** button ![Ellipsis button](../basics/media/ellipsis-button.gif "Ellipsis button") to open the **Select Values** dialog box and select the value you want.  

   ### To group criteria
   You must select two or more rows for the same record type. For example, **Sales Stage** and **Est. Revenue** are both field values in the **Opportunity** record  type and two rows that specify filter criteria for these fields can be grouped.  However, rows with field values from different record types, such as **Account** and **Opportunity** record types, cannot be grouped.  

   1.  For each row you want to group, in detailed mode, click or tap the **Options menu** button ![arrow&#95;down&#95;black](../basics/media/arrow-down-black.gif "arrow_down_black") for that row, and then click or tap **Select Row**.  

   2.  On the Filter toolbar, select **Group AND** or **Group OR**.  

   3.  To remove a row from a group, click or tap the **Options menu** button ![arrow&#95;down&#95;black](../basics/media/arrow-down-black.gif "arrow_down_black") for that row, and then click or tap **Delete**.  

   4.  To select a group, click or tap the **Options menu** button ![arrow&#95;down&#95;black](../basics/media/arrow-down-black.gif "arrow_down_black") for that group, and then click or tap **Select Group**.  

   5.  To add a criteria clause to a group, click or tap the **Options menu** button ![arrow&#95;down&#95;black](../basics/media/arrow-down-black.gif "arrow_down_black") for that group, click or tap **Add Clause**, and then select the field,  query relational operator, and value.  

   6.  To unselect a group that has been previously selected, click the **Options menu** button ![arrow&#95;down&#95;black](../basics/media/arrow-down-black.gif "arrow_down_black") for that group, and then click or tap **Deselect Group**.  

   7.  To ungroup a group, click or tap the **Options menu** button ![arrow&#95;down&#95;black](../basics/media/arrow-down-black.gif "arrow_down_black") for that group, and then click or tap **Ungroup**.  

   8.  To change a **Group AN**D group to a  Group OR group, or a **Group OR** group to a **Group AND** group, click the **Options menu** button ![arrow&#95;down&#95;black](../basics/media/arrow-down-black.gif "arrow_down_black") for that group, and then click or tap **Change to OR** or **Change to AND**.  

   > [!TIP]
   > - To clear all criteria and start over, on the Filter toolbar, click or tap **Clear**, and then click or tap **Confirm**.  
   >   -   To delete a row, click or tap the **Options menu** button ![arrow&#95;down&#95;black](../basics/media/arrow-down-black.gif "arrow_down_black") for that row, and then click or tap **Delete**.  

   ### Save the filter  
5. Click or tap **Save Default Filter**.  
