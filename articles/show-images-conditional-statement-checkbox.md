<properties
	pageTitle="Show images and use a checkbox with a conditional statement in PowerApps | Microsoft Azure"
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
   ms.date="09/21/2015"
   ms.author="mandia"/>


# Show an image and use a conditional statement in a checkbox
Use a checkbox with a conditional statement for a JPEG image.

You add a .jpeg image and include a checkbox with a conditional statement. If the checkbox is enabled, it displays certain text in a label. If it's unchecked, the checkbox displays different text in the same label. 

You can use this feature in your PowerApps apps for different scenarios. For example, there is a product image in your PowerApps app. When your users select the checkbox for the product image, additional information is displayed, like the price, or quantity in stock, maybe colors available, and so on.


### Prerequisites 
- Install PowerApps. Create a new app or open an existing app in PowerApps.
- To familiarize yourself with PowerApps and creating apps, step through the [Test Drive](get-started-test-drive.md ). It walks you through performing some key tasks.
- These steps use the [CreateFirstApp](https://gallery.technet.microsoft.com/Sample-data-for-Create-c77790e7) as sample input data, which includes .jpg images. You can use this sample data, or import your own.


## Add an image
1. On the **Insert** tab, select **Image**. An image control is automatically added to the screen:  
![][1]  
2. On the **Data** tab, select **Image**, and then select **Add an image file**. 
3. Browse to the CreateFirstApp folder, select the .jpeg file that you want to use, and then select **Open**. The image displays in the control:  
![][5]  


## Add a checkbox
1. On the **Insert** tab, select **Controls**, and then select **Checkbox**. 
2. Rename the checkbox to **MyCheckbox**, and set its **Text** property to **Pick me**:  
![][6]  
3. Move the checkbox below your image. Your screen looks similar to the following:  
![][2]  
4. On the **Insert** tab, add a label, and set its **Text** property to the following function:  
```If(MyCheckbox!Value = true, "Great choice!", "Great for fall")```  

	![][4]  
5. Move the label anywhere you like on the screen. Preview ![][3] the screen. Check and uncheck the checkbox. When it's checked, the "Great Choice" text is displayed in your label. When not checked, "Great for fall" is displayed.

## Tips and Tricks
- At anytime, you can select the Preview button (![][3]) to see what you created and test it.
- When designing your app, you can re-size the controls and move them around using click-and-drag.
- Press **ESC** to close the preview window. 

## What you learned

In this topic, you:

- Added an image, added a checkbox, and added a label.
- Using the label, you used an Excel-like function to display different text depending if the checkbox was enabled or cleared. This is known as a conditional statement.


[1]: ./media/show-images-conditional-statement-checkbox/image.png
[2]: ./media/show-images-conditional-statement-checkbox/checkbox.png
[3]: ./media/show-images-conditional-statement-checkbox/preview.png
[4]: ./media/show-images-conditional-statement-checkbox/textfunction.png
[5]: ./media/show-images-conditional-statement-checkbox/imagewithpicture.png
[6]: ./media/show-images-conditional-statement-checkbox/mycheckbox.png
