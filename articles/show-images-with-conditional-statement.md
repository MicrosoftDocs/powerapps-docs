<properties
	pageTitle="Show images and use a checkbox with a conditional statement in PowerApps | Microsoft PowerApps"
	description="Add media and configure images and checkboxes in your PowerApp"
	services=""
	suite="powerapps"
	documentationCenter=""
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/24/2015"
   ms.author="mandia"/>

# Show images using a conditional statement
Use a conditional statement to display or hide an image.

You add a .jpeg image and include a checkbox with a conditional statement. If the checkbox is enabled, it displays certain text in a label. If it's unchecked, the checkbox displays different text in the same label.

You can use this feature in your PowerApps for different scenarios. For example, there is a product image in your PowerApp. When your users select the checkbox for the product image, additional information is displayed, like the price, or quantity in stock, maybe colors available, and so on.


### Prerequisites
- Install [PowerApps](http://aka.ms/powerappsinstall) and sign-in with your work or organization account.
- Create a new PowerApp or open an existing PowerApp.
- To familiarize yourself with configuring controls in PowerApps, step through the [configure a control](get-started-test-drive.md#configure-a-control).
- These steps use the [CreateFirstApp.zip](http://pwrappssamples.blob.core.windows.net/samples/CreateFirstApp.zip) as sample input data, which includes .jpeg images. The zip file also includes an XML file that can be converted to Excel. You can download and use this sample data, or import your own. 

## Add an image
1. On the **File** tab, select **Media**, and then select **Images**.
2. Select the **Upload** folder, browse to the CreateFirstApp folder, select the .jpeg file that you want to use, and then select **Open**. For example, select the *Jacket_8_PaleMarigold* image.  

	Your Media should look similar to the following:  
	![][8]  
3. Go back to the app designer. 
4. On the **Insert** tab, select **Image**. An image control is automatically added to the screen:  
![][1]  
5. On the **Content** tab, and select **Image**. In the scroll list, select *Jacket_8_PaleMarigold*. The image displays in the control:  
![][5]  


## Add a checkbox to change the label
1. On the **Insert** tab, select **Controls**, and then select **Checkbox**.
2. Rename the checkbox to **MyCheckbox**, and set its **Text** property to **More details**:  
![][6]  
3. Move the checkbox below your image. Your screen looks similar to the following:  
![][2]  
4. On the **Insert** tab, add a label, and set its **Text** property to the following function:  
```If(MyCheckbox!Value = true, "100% cotton. Additional sizes and colors available.", "Fall Jacket")```  

	![][4]  
5. Move the label anywhere you like on the screen. Preview the screen: ![][3]. Check and uncheck the checkbox. When it's checked, the "100% cotton. Additional sizes and colors available." text is displayed in your label. When not checked, "Fall Jacket"  is displayed.

Now, let's get creative with the image control. When **MyCheckbox** is enabled, show the picture. If **MyCheckbox** is not enabled, don't show the picture. To do this:

1. Select the image control.
2. In the Function Bar, select **Visible** and set it's function to the following:  
```If(MyCheckbox!Value = true, true, false)```  

	![][7]  
3. Preview your app: ![][3]. Check and uncheck the checkbox. When it's checked, the picture is displayed. When not checked, the picture is not displayed.

> [AZURE.TIP] Instead of a label, try using a [listbox](add-list-box-drop-down-list-radio-button.md) to display sizes or colors available.


## Tips and Tricks
- At anytime, you can select the preview button (![][3]) to see what you created and test it.
- When designing your app, you can re-size the controls and move them around using click-and-drag.
- Press **ESC** or select the **X** to close the preview window.

## What you learned

In this topic, you:

- Uploaded images to Media in your PowerApp. 
- Added an image, added a checkbox, and added a label.
- Using the label, you used an Excel-like function to display different text depending if the checkbox was enabled or cleared. This is known as a conditional statement.
- Used the **Visible** property of the image control to hide and show the picture, depending if the checkbox is checked or unchecked, another conditional statement.


[1]: ./media/show-images-with-conditional-statement/image.png
[2]: ./media/show-images-with-conditional-statement/checkbox.png
[3]: ./media/show-images-with-conditional-statement/preview.png
[4]: ./media/show-images-with-conditional-statement/textfunction.png
[5]: ./media/show-images-with-conditional-statement/imagewithpicture.png
[6]: ./media/show-images-with-conditional-statement/mycheckbox.png
[7]: ./media/show-images-with-conditional-statement/visible.png
[8]: ./media/show-images-with-conditional-statement/media.png