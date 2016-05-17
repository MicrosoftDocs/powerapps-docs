<properties
	pageTitle="Show the current user details or information in PowerApps | Microsoft PowerApps"
	description="Insert the User function to display the name and email address of the signed-in user in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter=""
	authors="MandiOhlinger"
	manager="erikre"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="05/03/2016"
   ms.author="mandia"/>

# Get the signed-in user details
The User feature can show the full name, email address, and picture associated with the current signed-in user. You can use this information to automatically fill in a form.

For example, you can use this feature to:

- Create a sign-up "sheet" for users to attend training, volunteer for events, check-in at a kiosk, and more.
- Display the full name on a Human Resources app.
- Automatically enter an email address when contacting your Help Desk.

Basically, you can use this anywhere users would benefit from an automatically-populated form or automatically-populated labels.

&nbsp;

[AZURE.INCLUDE [app-customization-requirements](../includes/app-customization-requirements.md)]

## Add User
In these steps, we're going to display the image, full name, and email address of the current signed-in user.

1.	On the **Insert** tab, select **Image**:  
![][2]
2. Set the **[Image](properties/properties-visual.md)** property to ```User().Image```:  
![][3]
3. On the **Insert** tab, select **Text**, and select **Text box**:  
![][4]
4.	Set the **[Text](properties/properties-core.md)** property to ```User().FullName```:  
![][6]  
When you do this, the label is automatically populated with your full name. Move the label so it's below the image control, similar to the following:  
![][5]
5. Add another text box, and set its **[Text](properties/properties-core.md)** property to ```User().Email```:  
![][8]  
When you do this, the label is automatically populated with your email address. Move the label so it's below the first label, similar to the following:  
![][7]

Now, let's see what you've created. Select the Preview button ![][9]. When you view the screen, you get an idea of what your app looks like; and it shows the picture, full name, and email address of the signed-in user.

## Tips and Tricks
- At anytime, you can select the preview button (![][9]) to see what you created and test it.
- When designing your app, you can re-size the controls and move them around using click-and-drag.
- Press **ESC** to close the preview window.
- **Save** your work using the **File** menu, or press **Ctrl** + **S**.

## What you learned

In this topic, you:

- Used the Insert menu to add an image and text boxes to your app.
- You used Excel-like functions to display some user properties.
- With the User() function, you accessed some information specific to the signed-in user, including the user's full name and the user's email address.
- Saw that when you configure a property, like the Text property, the labels are automatically updated.


[2]: ./media/show-current-user/insertimage.png
[3]: ./media/show-current-user/imageproperty.png
[4]: ./media/show-current-user/insertlabel.png
[5]: ./media/show-current-user/label.png
[6]: ./media/show-current-user/textproperty.png
[7]: ./media/show-current-user/secondlabel.png
[8]: ./media/show-current-user/email.png
[9]: ./media/show-current-user/preview.png
