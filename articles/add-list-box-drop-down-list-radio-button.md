<properties
	pageTitle="Add a listbox, drop-down list, and radio button controls in PowerApps | Microsoft Azure"
	description=""
	services="power-apps"
	documentationCenter="" 
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="power-apps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="" 
   ms.date="09/24/2015"
   ms.author="mandia"/>


# Add a list box, drop-down list, or radio button control

PowerApps includes multi-select options, including a listbox, drop-down list, and radio button controls. In this topic, we add these controls and use a Table to build the lists. When an item is selected in the list, it updates other controls.

### Prerequisites 

- Install PowerApps. Create a new app or open an existing app in PowerApps.
- To familiarize yourself with PowerApps and creating apps, step through the [Test Drive](get-started-test-drive.md ). It walks you through performing some key tasks.


## Add a listbox

1. On the **Insert** tab, select **Controls**, and then select **ListBox**:  
![][2]  
2. Rename the listbox to **MyListBox**:  
![][3]  
3. Set its **Items** property to the following function:  
```Table({Shape:"circle"}, {Shape:"triangle"}, {Shape:"rectangle"})```  

	![][4]  
3. On the **Insert** tab, select **Shapes**, select the **circle**, and move it under the listbox:  
![][5]  

4. Add a triangle and a rectangle, and then arrange the shapes in a row under the listbox:  
![][6]  

5. Set the **Visible** property of the following shapes to the following functions:  

	Shape | Set function to | Screen shot
--- | --- | ---
circle | ```If("circle" in MyListbox!SelectedItems!Value, true)``` | ![][7] 
triangle | ```If("triangle" in MyListbox!SelectedItems!Value, true)``` | ![][8] 
rectangle | ```If("rectangle" in MyListbox!SelectedItems!Value, true)``` | ![][9] 

6. Preview ![][1] what you've created. Select the different shapes in the listbox. Only the shape or shapes you select appear. Press ESC to go back to your screen. 

In these steps, you use the Table function to create a list of items in a listbox. Depending on what you choose in the list box, different shapes are displayed. You can apply this to other elements within your business. For example, you can use a listbox to display product images, product descriptions, and so on. 


## Add a drop-down list and a radio button control

> [AZURE.NOTE] The following steps apply to radio button controls and drop-down lists. Both controls are created the same way. 

1. On the **Insert** tab, select **Controls**, select **Radio**, and then rename the radio control to **Choices**:  
![][10]  

	![][11]  

2. Set the radio control **Items** property to the following function:  
```Table({Color:"red"}, {Color:"green"}, {Color:"blue"})```

	![][12]  

	If needed, resize the control to show all the options. 

3. On the Insert tab, select **Shapes**, and select the circle. Set the **Fill** property of the circle to the following function:  
```If(Choices!Selected!Value = "red", RGBA(192, 0, 0, 1), Choices!Selected!Value = "green", RGBA(0, 176, 80, 1), Choices!Selected!Value = "blue", RGBA(0, 32, 96, 1))```  

	![][13]  

	In this function, you enter different color values based on which radio button you choose.

5. Move the circle under the radio control. You setup should look similar to the following:  
![][14]  
6. Preview ![][1] what you've created. Select the different radio buttons to change the color of the circle. Press ESC to go back to your screen. 

In these steps, you used a Table to create the items in the radio button control. When you click an item within the control, the property of another control (the circle) changes. 


## Tips and Tricks
- You can also use different data sources to populate the items within these controls. For example, you can use an Excel table as a data source. Then display the Excel data in a list box, and so on.
- At anytime, you can select the preview button (![][1]) to see what you created and test it.
- When designing your app, you can re-size the controls and move them around using click-and-drag.
- Press **ESC** to close the preview window. 

## What you learned

In this topic, you:

- Added radio buttons and a listbox to the app.
- Using the Table function, you populated the items within the lists.
- You used Excel-like functions to update properties on other controls. For example, if a list item or radio button is selected, a shape changes color or is displayed in the app. 


[1]: ./media/add-list-box-drop-down-list-radio-button/preview.png
[2]: ./media/add-list-box-drop-down-list-radio-button/listbox.png
[3]: ./media/add-list-box-drop-down-list-radio-button/renamelistbox.png
[4]: ./media/add-list-box-drop-down-list-radio-button/itemslistbox.png
[5]: ./media/add-list-box-drop-down-list-radio-button/circle.png
[6]: ./media/add-list-box-drop-down-list-radio-button/allshapes.png
[7]: ./media/add-list-box-drop-down-list-radio-button/visiblecircle.png
[8]: ./media/add-list-box-drop-down-list-radio-button/visibletriangle.png
[9]: ./media/add-list-box-drop-down-list-radio-button/visiblerectangle.png
[10]: ./media/add-list-box-drop-down-list-radio-button/radiobutton.png
[11]: ./media/add-list-box-drop-down-list-radio-button/renameradio.png
[12]: ./media/add-list-box-drop-down-list-radio-button/itemsradio.png
[13]: ./media/add-list-box-drop-down-list-radio-button/fillradio.png
[14]: ./media/add-list-box-drop-down-list-radio-button/radiocircle.png
