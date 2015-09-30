<properties
	pageTitle="Show images and use a checkbox with a conditional statement in KratosApps | Microsoft Azure"
	description=""
	services=""
	documentationCenter=""
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="na"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na" 
   ms.date="09/30/2015"
   ms.author="mandia"/>


# Show an image and use a conditional statement in a checkbox
Use a checkbox with a conditional statement for a JPEG image.

You add a .jpeg image and include a checkbox with a conditional statement. If the checkbox is enabled, it displays certain text in a label. If it's unchecked, the checkbox displays different text in the same label.

You can use this feature in your KratosApps apps for different scenarios. For example, there is a product image in your KratosApps app. When your users select the checkbox for the product image, additional information is displayed, like the price, or quantity in stock, maybe colors available, and so on.


### Prerequisites
- Install KratosApps. Create a new app or open an existing app in KratosApps.
- To familiarize yourself with KratosApps and creating apps, step through the [Test Drive](get-started-test-drive.md ). It walks you through performing some key tasks.
- These steps use the [CreateFirstApp](https://gallery.technet.microsoft.com/Sample-data-for-Create-c77790e7) as sample input data, which includes .jpg images. You can use this sample data, or import your own.


## Add an image
1. On the **Insert** tab, select **Image**. An image control is automatically added to the screen:  
![][1]  
2. On the **Data** tab, select **Image**, and then select **Add an image file**.
3. Browse to the CreateFirstApp folder, select the .jpeg file that you want to use, and then select **Open**. The image displays in the control:  
![][5]  


## Add a checkbox to change the label
1. On the **Insert** tab, select **Controls**, and then select **Checkbox**.
2. Rename the checkbox to **MyCheckbox**, and set its **Text** property to **Pick me**:  
![][6]  
3. Move the checkbox below your image. Your screen looks similar to the following:  
![][2]  
4. On the **Insert** tab, add a label, and set its **Text** property to the following function:  
```If(MyCheckbox!Value = true, "Great choice!", "Great for fall")```  

	![][4]  
5. Move the label anywhere you like on the screen. Preview ![][3] the screen. Check and uncheck the checkbox. When it's checked, the "Great Choice" text is displayed in your label. When not checked, "Great for fall" is displayed.

Now, let's get creative with the image control. When **MyCheckbox** is enabled, show the picture. If **MyCheckbox** is not enabled, don't show the picture. To do this:

1. Select the image control.
2. In the Function Bar, select **Visible** and set it's function to the following:  
```If(MyCheckbox!Value = true, true, false)```  

	![][7]  
3. Preview ![][3] the screen. Check and uncheck the checkbox. When it's checked, the picture is displayed. When not checked, the picture is not displayed.

You can also add another checkbox named **ShowPicCheckbox** with the "Show picture" text. If you do this, set the **Visible** property of the image control to the following function:

```If(ShowPicCheckbox!Value = true, true, false)```

![][8]
Preview ![][3] the screen. Check and uncheck the "Show picture" checkbox. When it's checked, the picture is displayed. When not checked, the picture is not displayed.



## Tips and Tricks
- At anytime, you can select the preview button (![][3]) to see what you created and test it.
- When designing your app, you can re-size the controls and move them around using click-and-drag.
- Press **ESC** to close the preview window.

## What you learned

In this topic, you:

- Added an image, added a checkbox, and added a label.
- Using the label, you used an Excel-like function to display different text depending if the checkbox was enabled or cleared. This is known as a conditional statement.
- Used the **Visible** property of the image control to hide and show the picture, depending if the checkbox is checked or unchecked.


[1]: ./media/show-images-conditional-statement-checkbox/image.png
[2]: ./media/show-images-conditional-statement-checkbox/checkbox.png
[3]: ./media/show-images-conditional-statement-checkbox/preview.png
[4]: ./media/show-images-conditional-statement-checkbox/textfunction.png
[5]: ./media/show-images-conditional-statement-checkbox/imagewithpicture.png
[6]: ./media/show-images-conditional-statement-checkbox/mycheckbox.png
[7]: ./media/show-images-conditional-statement-checkbox/visible.png
[8]: ./media/show-images-conditional-statement-checkbox/showpicture.png
