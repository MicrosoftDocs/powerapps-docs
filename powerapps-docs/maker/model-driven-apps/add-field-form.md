---
title: "Add a column to a model-driven app form in Power Apps | MicrosoftDocs"
description: Learn how to add a field to a model-driven app form
ms.custom: ""
ms.date: 05/04/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Mattp123"
ms.assetid: 29499887-6e7b-44a1-86a7-eaad33f3075d
caps.latest.revision: 30
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Add a column to a model-driven app form 

If a Power Apps form for a standard table doesn't meet your organization's business requirements, you can customize the form by changing existing columns or by adding new columns. While it might be simpler to edit the existing columns on a form, sometimes it's better to add a column to address a specific business scenario.

In this topic, you add a column on to a form.   
  
1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2.  Expand **Data**, select **Tables**, select the table that you want, and then select the **Forms** tab.  

3.  In the list, open a form with the type of **Main** to edit it.  
  
4.  In the form, click the section you want to add a column to, and then in the **Columns** pane, click the column you want added to the form.  
  
    > [!TIP]
    >  When you add an option set column on the form, the drop-down list that contains the option set values can only display two values. Users must scroll to see more values in the list. If you want to show more than two values without users having to scroll, add one or more **Spacer** controls below the option set column on the form. Each **Spacer** control provides a space for one additional option set value. For example, if you want to display four values in the drop-down list without scrolling, add two **Spacer** controls below the option set column on the form.  
  
5.  To publish customizations for the form that you're editing, with the form open, click **Publish**. 
  
6.  When you're done editing the form, click **Save and Close**.  
  
> [!IMPORTANT]
>  In Unified Interface, when you set column level security, we don’t recommend that you set read-only on a required column using column level security rules.  When the row is created, the save pipeline will ignore the read-only setting on the required column and will save the row. We recommend that you set the table to read-only using role-based security. This helps ensure there is no conflict when creating or saving a row.
  
  
> [!NOTE]
>  Publishing customizations can interfere with normal system operation. We recommend that you publish when it's least disruptive to users.

  
## Next steps  
 
 [Create and design forms](create-design-forms.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]