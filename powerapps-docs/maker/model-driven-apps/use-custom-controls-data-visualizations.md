---
title: "Use custom controls for data visualizations in PowerApps | MicrosoftDocs"
description: "Learn how to use custom controls for fields"
ms.custom: ""
ms.date: 06/07/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: 0d6064cd-4d38-4fc2-a564-735cb453a4b2
caps.latest.revision: 8
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
---
# Tutorial: Use custom controls for data visualizations

In this tutorial you learn how to configure a custom control for a field. 

Custom controls let you transform fields that traditionally contain text into visualizations. Similarly, you can use custom controls to transform datasets, such as a view, to display in a more visual rendering rather than a list of records. Custom controls can appear as visualizations on forms, dashboards, views, and homepage grids. You can set one type of custom control to appear in the web browser client while having a different custom control appear in your Dynamics 365 phone or  tablet mobile apps. For example, you could use a number input custom control for a field in web browser clients and a slider custom control for the phone app. After the customization is published, users can fully interact with the control to change the value, such as by sliding the control when using the linear slider custom control. Changes are automatically saved when the form is closed just as they are when the user changes a traditional  field on a form.  
  
   ![Custom slider control](media/slider-control.PNG "Custom slider control")  
  
## Use a custom control to add visualizations to a field  
 Following the steps in this procedure will change the default label and text box field  of the **Budget Amount** field to the slider custom control on the Opportunity entity. You can use similar steps to replace an existing field with a custom control or configure a custom control for a custom field.  
  
1.  On the [PowerApps](https://web.powerapps.com) site, select **Model-driven** (lower left of the navigation pane).  

     ![Model-driven design mode](media/model-driven-switch.png)

2.  Expand **Data**, select **Entities**, select the entity that you want, and then select the **Forms** tab.  
  
2.  Open a form such as the **Main** form for the opportunity entity. 
  
3.  In the form editor, double-click the field where you want to add a custom control, such as the **Budget Amount** field on the opportunity main form. Alternatively, you can create a custom field. 
  
4.  On the **Field Properties** page, select the **Controls** tab, and then select **Add Control**.  
  
5.  On the Add Control page, select the control that you want, such as the **Linear Slider** control shown here, and then select **Add**.  
  
   ![Add linear slider control](media/add-slider.PNG "Add linear slider control")  
  
6.  Choose the client where you want the control to appear.  
  
    - **Web**. To make the custom control available from any web browser, select the **Web** option next to the control. Notice that setting the **Web** option includes rendering the control in web browsers on PCs, Macs, and mobile devices.  
  
    - **Phone**. To make the custom control available on phones running Dynamics 365 for phones, select the **Phone** option next to the control.  
  
    - **Tablet**. To make the custom control available on tablet devices running Dynamics 365 for tablets, select the **Tablet** option next to the control.  
  
   ![Choose the client apps to view the custom control](media/choose-client.png "Choose the client apps to view the custom control")  
  
7.  Select the ![Edit custom control property icon](media/ccf-pencil-icon.png "Edit custom control property icon") pencil icon next to **Min**, **Max**, and **Step**, set the property option described below, and then select **OK**.  
  
   ![Add custom control properties](media/ccf-add-properties.png "Add custom control properties")
  
   - **Min**. Set the minimum accepted value. You can bind a static value that you enter or bind the value to an existing field. In this example **Bind to static value** is **Currency** and the minimum value that can be entered is *zero*.  
  
       - **Bind to a static value**. Select the data type, such as a whole number (Whole.None), currency, floating point (FP), or decimal. Next, enter a number that represents the minimum accepted value for the field.  
  
       - **Bind to values on a field**. Select a field from the list that will be used as the minimum accepted value.  
  
   - **Max**. Set the maximum accepted value for the field. Similar to the Min value, you can bind a static value that you enter or bind the value to an existing field as described earlier. In this example, **Bind to static value** is **Currency** and the maximum value that can be entered is **1 billion**.  
  
   - **Step**. This represents the unit to increment or decrement when adding to or subtracting from  the current value. For example, for budget amount you can select 100 dollar increments\decrements.  
  
   - **Hide Default Control**. Selecting this option hides the control so neither the control or the data is displayed in any of the clients that don't support the custom control. Notice that  the classic Dynamics 365 web client doesn't support most custom controls. By default, this option is not selected and the classic Dynamics 365 web client displays the default, typically text based, control.  
  
       > [!NOTE]
       >  The default control is identified with **(default)** following the control name.  
       >   
       > ![Default control](media/default-control.png "Default control")  
  
8.  Select **OK**, to close the **Field Properties** page.  
  
9. To activate the customization, on the entity form select **Save**, and then select **Publish**.  
  
10. Select **Save and Close** to close the form editor.  
  
## See the custom control in action  
 Open a record that includes the field with the custom control, such as the opportunity form from the previous example, and view how the field is changed.  
  
   ![Slider control rendered on form](media/slider-control.PNG "Slider control rendered on form")  
  
 The field is now rendered as a slider control instead of the text field.  
  
## Next steps  
[Create and edit fields](../common-data-service/create-edit-fields.md)
