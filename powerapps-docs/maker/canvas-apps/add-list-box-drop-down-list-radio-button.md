---
title: Add a list box, a drop-down list, or radio buttons to a canvas app
description: In Power Apps, create or configure multi-select options in a canvas app.
author: fikaradz
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/24/2018
ms.author: fikaradz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Add a list box, a drop-down list, or radio buttons to a canvas app

Show a single column of data (for example, from a multi-column table) in a canvas app so that users can select one or more items in a list.

- Add a list box to allow users to select more than one option.
- Add a drop-down list to take up less space on a screen.
- Add a set of radio buttons for a particular design effect.

This topic focuses on lists boxes and radio buttons, but the same principles apply to drop-down lists.

[!INCLUDE [app-customization-requirements](../../includes/app-customization-requirements.md)]

## Create a simple list

1. Add a **List box** control named **MyListBox**, and set its **Items** property to this expression:

    ```["circle","triangle","rectangle"]```  <br/>

    Your designer looks similar to the following:

    ![Screen with list box control][4]

4. On the **Insert** tab, select **Icons**, select the circle, and move it under **MyListBox**:

    ![Add icon][5]  

5. Add a triangle and a rectangle, and then arrange the shapes in a row under **MyListBox**:

    ![Add shapes][6]  

6. Set the **[Visible](controls/properties-core.md)** property of the following shapes to the following functions:  

   | Shape | Set Visible function to |
   | --- | --- |
   | circle |```If("circle" in MyListBox.SelectedItems.Value, true)``` |
   | triangle |```If("triangle" in MyListBox.SelectedItems.Value, true)``` |
   | rectangle |```If("rectangle" in MyListBox.SelectedItems.Value, true)``` |

7. While holding down the Alt key, select one or more shapes in **MyListBox**.

    Only the shape or shapes that you select appear.

In these steps, you used an expression to create a list of items. You can apply this to other elements within your business. For example, you can use a **Drop down** control to display product images, product descriptions, and so on.

## Add radio buttons
1. On the **Home** tab, select **New Screen**, and then select **Blank**.

2. On the **Insert** tab, select **Controls**, and then select **Radio**.

    ![Add Radio button][10]  

3. Rename the **Radio** control to **Choices**, and set its **[Items](controls/properties-core.md)** property to this formula:  
   ```["red","green","blue"]```  <br/>

    ![Rename control][12]  

    If needed, resize the control to show all the options.

4. On the **Insert** tab, select **Icons**, and then select the circle.

5. Set the **[Fill](controls/properties-color-border.md)** property of the circle to the following function:  
   ```If(Choices.Selected.Value = "red", Red, Choices.Selected.Value = "green", Green, Choices.Selected.Value = "blue", Blue)```  

    In this formula, the circle changes its color depending on which radio button you choose.

6. Move the circle under the **Radio** control, as in this example:

    ![Move circle under the Radio control][14]  

7. While holding down the Alt key, select a different radio button to change the color of the circle.

[1]: ./media/add-list-box-drop-down-list-radio-button/preview.png
[2]: ./media/add-list-box-drop-down-list-radio-button/listbox.png
[3]: ./media/add-list-box-drop-down-list-radio-button/renamelistbox.png
[4]: ./media/add-list-box-drop-down-list-radio-button/itemslistbox.png
[5]: ./media/add-list-box-drop-down-list-radio-button/circle.png
[6]: ./media/add-list-box-drop-down-list-radio-button/allshapes.png
[10]: ./media/add-list-box-drop-down-list-radio-button/radiobutton.png
[12]: ./media/add-list-box-drop-down-list-radio-button/itemsradio.png
[14]: ./media/add-list-box-drop-down-list-radio-button/radiocircle.png
[15]: ./media/add-list-box-drop-down-list-radio-button/dropdown.png


[!INCLUDE[footer-include](../../includes/footer-banner.md)]