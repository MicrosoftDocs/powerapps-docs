---
title: Add a list box, a drop-down list, and radio buttons to a canvas app | Microsoft Docs
description: In PowerApps, create or configure multiselect options in a canvas app
author: lonu
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 10/23/2016
ms.author: lonu
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Add a list box, a drop-down list, or radio buttons to a canvas app in PowerApps

PowerApps includes multi-select and single-select options for canvas apps, including a list box, a drop-down list, and radio buttons. In this topic, we add these controls and use a **Table** formula to build the lists. When an item is selected in the list, it updates other controls.

[!INCLUDE [app-customization-requirements](../../includes/app-customization-requirements.md)]

## Add a list box

1. On the **Insert** tab, select **Controls**, and then select **List box**:  

    ![][2]  

2. Rename the **List box** control to **MyListBox**:  

    ![][3]

3. Set its **[Items](controls/properties-core.md)** property to the following expression:  
   ```["circle","triangle","rectangle"]```  <br/>

    Your designer looks similar to the following:

    ![][4]

4. On the **Insert** tab, select **Icons**, select the circle, and move it under the **List box** control:

    ![][5]  

5. Add a triangle and a rectangle, and then arrange the shapes in a row under the **List box** control:

    ![][6]  

6. Set the **[Visible](controls/properties-core.md)** property of the following shapes to the following functions:  

   | Shape | Set Visible function to |
   | --- | --- |
   | circle |```If("circle" in MyListBox.SelectedItems.Value, true)``` |
   | triangle |```If("triangle" in MyListBox.SelectedItems.Value, true)``` |
   | rectangle |```If("rectangle" in MyListBox.SelectedItems.Value, true)``` |

7. Preview what you've created ![][1]. Select the different shapes in the **List box** control. Only the shape or shapes that you select appear. Press Esc or select the **X** to go back to your screen.

In these steps, you used an expression to create a list of items in a **List box** control. Depending on what you choose in the **List box** control, different shapes are displayed. You can apply this to other elements within your business. For example, you can use a **List box** control to display product images, product descriptions, and so on.

## Add radio buttons
1. On the **Home** tab, select **New Screen**.

2. On the **Insert** tab, select **Controls**, and then select **Radio**.

    ![][10]  

3. Rename the **Radio** control to **Choices**, and set its **[Items](controls/properties-core.md)** property to this formula:  
   ```["red","green","blue"]```  <br/>

    ![][12]  

    If needed, resize the control to show all the options.

4. On the **Insert** tab, select **Icons**, and then select the circle.

5. Set the **[Fill](controls/properties-color-border.md)** property of the circle to the following function:  
   ```If(Choices.Selected.Value = "red", RGBA(192, 0, 0, 1), Choices.Selected.Value = "green", RGBA(0, 176, 80, 1), Choices.Selected.Value = "blue", RGBA(0, 32, 96, 1))```  

    In this formula, the circle changes its color depending on which radio button you choose.

6. Move the circle under the **Radio** control, as in this example:

    ![][14]  

7. Preview what you've created: ![][1]. Select a different radio button to change the color of the circle. Press Esc or select the **X** to go back to your screen.

## Add a drop-down list
1. Add a screen, and then add a **Drop down** control.

    ![][15]  

2. Rename the control to **DDChoices**, and set its **[Items](controls/properties-core.md)** property to this formula:<br>
   **["red","green","blue"]**

3. Add a circle, move it below the **Drop down** control, and set the circle's **[Fill](controls/properties-color-border.md)** property to this formula:  
   ```If(DDChoices.Selected.Value = "red", RGBA(192, 0, 0, 1), DDChoices.Selected.Value = "green", RGBA(0, 176, 80, 1), DDChoices.Selected.Value = "blue", RGBA(0, 32, 96, 1))```

4. Preview what you've created: ![][1]. Select the different options to change the color of the circle.

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
