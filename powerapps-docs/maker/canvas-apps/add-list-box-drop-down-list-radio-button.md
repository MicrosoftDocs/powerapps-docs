---
title: Add a list box, a drop-down list, or radio buttons to a canvas app | Microsoft Docs
description: In Power Apps, create or configure multi-select options in a canvas app
author: chmoncay
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
# Add a list box, a drop-down list, a combo box, or radio buttons to a canvas app

Show a single column of data (for example, from a multi-column table) in a canvas app so that users can select one or more items in a list.

- Add a list box to allow users to select more than one option.
- Add a drop-down list or combo box to take up less space on a screen.
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

## Add an item to an existing list

1. Add a **[Button](control-button.md)** control and name it **btnReset**.

   Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
   
2. Set **[OnChange](properties-core.md)** property on **btnReset** to this formula:
   <br>`ClearCollect(MyItems, {value: "circle"},{value: "triangle"},{value: "rectangle"})`
   
3. Set the **[Text](properties-core.md)** property on **btnReset** to 
   <br>`"Reset"`

4. Add a **List box** control named **lbItems**, and set its **Items** property to this expression:
   <br/> `MyItems`

5. While holding down the Alt key, press the Reset button.

> [!NOTE]
> The list box should populate with the items from the MyItems collection.

6. Arrange the list box and button so they're lined up vertically:

[1]: ./media/add-list-box-drop-down-list-radio-button/listboxbutton.png

7. Add a **[Text Input](control-text-input.md)** control and name it **txtAdd**.

8. Set **[Text](properties-core.md)** property on **txtAdd** to
   <br>`""`

9. Add a **[Button](control-button.md)** control and name it **btnAdd**.

10. Set the **[Text](properties-core.md)** property on **btnAdd** to
   <br>`"Add"`

11. Set **[OnChange](properties-core.md)** property on **btnAdd** to this formula:
   <br>`Collect(MyItems,{value: txtAdd.Text}); Reset(txtAdd)`

> [!NOTE]
> The collect function will add the text from the text input as an item in the collection.
> The reset function will reset the text input back to it's default state.

12. Arrange **txtAdd** and **btnAdd* so they're lined up vertically underneath **lbItems** and **btnReset**

[1]: ./media/add-list-box-drop-down-list-radio-button/allcontrolsbeforeadd.png

13. Preview the app by pressing F5.

14. Add a text value to **txtAdd** text input control.

[1]: ./media/add-list-box-drop-down-list-radio-button/allcontrolstextentered.png

15. Press the Add button.

> [!NOTE]
> The list box should populate with the items from the MyItems collection.

### (Optional) Remove an item from an existing list

1. Add a **[Button](control-button.md)** control and name it **btnDelete**.

2. Set the **[Text](properties-core.md)** property on **btnDelete** to
   <br>`"Delete"`

3. Set **[OnChange](properties-core.md)** property on **btnDelete** to this formula:
   <br>`Remove(MyItems, lbItems.Selected)`

4. Arrange **btnDelete** so it's lined up vertically underneath **btnReset**

[1]: ./media/add-list-box-drop-down-list-radio-button/allcontrolsdeletebutton.png

5. Preview the app by pressing F5.

6. Press the Reset button to reset the list box.

7. Press an item in the list box to select it.

[1]: ./media/add-list-box-drop-down-list-radio-button/allcontrolsdeleteselected.png

8. Press the Delete button to delete item.

[1]: ./media/add-list-box-drop-down-list-radio-button/allcontrolsafterdelete.png


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
