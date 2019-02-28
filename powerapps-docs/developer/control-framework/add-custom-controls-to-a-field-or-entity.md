---
title: Add Custom Controls to a field or entity in Model-driven Apps | Microsoft Docs
description: Process to import custom controls
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
---

# Add Custom Controls to a field or entity in model-driven Apps

Custom controls let you transform fields that traditionally contain text into visualizations. Similarly, you can use custom controls to transform datasets, such as a view, to display in a more visual rendering rather than a list of records. Custom controls can appear as visualizations on forms, dashboards, views, and homepage grids. 

## Add a custom control to a field

Following the steps in this procedure will change the default label and text box field of the **Budget Amount** field to the slider custom control on the Opportunity entity. You can use similar steps to replace an existing field with a custom control or configure a custom control for a custom field.

1. Open solution explorer.

2. Expand **Entities**, expand the entity that you want, such as the **Opportunity** entity, select **Forms**, and then open a form such as the **Main** form.

3. In the form editor, double-click the field where you want to add a custom control, such as the **Budget Amount** field on the opportunity main form. Alternatively, you can create a custom field.

4. On the **Field Properties** page, select the **Controls** tab, and then select **Add Control**.

5. On the Add Control page, select the control that you want, such as the **Linear Slider** control, and then select **Add**.

6. Choose the client where you want the control to appear.

   - **Web**. To make the custom control available from any web browser, select the Web option next to the control. Notice that setting the Web option includes rendering the control in web browsers on PCs, Macs, and mobile devices.

   - **Phone**. To make the custom control available on phones running Dynamics 365 for phones, select the Phone option next to the control.

   - **Tablet**. To make the custom control available on tablet devices running Dynamics 365 for tablets, select the Tablet option next to the control.
7. Select the pencil icon next to **Min**, **Max**, and **Step**, set the property option, and then select **OK**.  
  
   - **Min**. Set the minimum accepted value. You can bind a static value that you enter or bind the value to an existing field. In this example **Bind to static value** is **Currency** and the minimum value that can be entered is *zero*.  
  
       - **Bind to a static value**. Select the data type, such as a whole number (Whole.None), currency, floating point (FP), or decimal. Next, enter a number that represents the minimum accepted value for the field.  
  
       - **Bind to values on a field**. Select a field from the list that will be used as the minimum accepted value.  
  
   - **Max**. Set the maximum accepted value for the field. Similar to the Min value, you can bind a static value that you enter or bind the value to an existing field as described earlier. In this example, **Bind to static value** is **Currency** and the maximum value that can be entered is **1 billion**.  
  
   - **Step**. This represents the unit to increment or decrement when adding to or subtracting from  the current value. For example, for budget amount you can select 100 dollar increments\decrements.  
  
   - **Hide Default Control**. Selecting this option hides the control so neither the control or the data is displayed in any of the clients that don't support the custom control.   
  
8. Select **OK**, to close the Field Properties page.  
  
9. To activate the customization, on the entity form select **Save**, and then select **Publish**.  
  
10. Select **Save and Close** to close the form editor.  
  
## See the custom control in action  

 Open a record that includes the field with the custom control, such as the Opportunity form from the previous example, and view how the field is changed. The field is now rendered as a slider control instead of the text field.  
 
> [!div class="nextstepaction"]
> [Debug controls](debugging-custom-controls.md)
