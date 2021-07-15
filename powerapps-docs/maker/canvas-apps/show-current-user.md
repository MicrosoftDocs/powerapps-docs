---
title: Show information about a user in a canvas app
description: Learn about how to display the name and email address of the signed-in user in a canvas app.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/16/2016
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Show information about a user in a canvas app

In Power Apps, show the full name, the email address, and the picture that's associated with the user who's signed in to a canvas app. You can use this information, for example, to automatically fill in a form.

For example, you can use this feature to:

* Create a sign-up "sheet" for users to attend training, volunteer for events, check in at a kiosk, and more.
* Display the full name on a Human Resources app.
* Automatically enter an email address when contacting your helpdesk.

Basically, you can use this anywhere users would benefit from a form or labels that are populated automatically

[!INCLUDE [app-customization-requirements](../../includes/app-customization-requirements.md)]

## Show user details

1. On the **Insert** tab, click or tap **Media**, and then click or tap **Image**.
   
   ![Insert media][2]
2. Set the **[Image](controls/properties-visual.md)** property to this formula:
   <br>**User().Image**
   
    ![Image property][3]
3. On the **Insert** tab, click or tap **Text**, and then click or tap **Label**:  
   
    ![Text label][4]
4. Set the **[Text](controls/properties-core.md)** property to this formula:
   <br>**User().FullName**
   
   ![Text property with formula][6]
   
   When you do this, the label is automatically populated with your full name. Move the label so it's below the image control, similar to the following:
   
   ![Image of label][5]
5. Add another label, and set its **[Text](controls/properties-core.md)** property to this formula:
   <br>**User().Email**  
   
    ![Text property with user email][8]
   
    When you do this, the label is automatically populated with your email address. Move the label so it's below the first label, similar to the following:  
   
    ![Image with name and email][7]

[2]: ./media/show-current-user/add-image.png
[3]: ./media/show-current-user/imageproperty.png
[4]: ./media/show-current-user/insertlabel.png
[5]: ./media/show-current-user/label.png
[6]: ./media/show-current-user/textproperty.png
[7]: ./media/show-current-user/secondlabel.png
[8]: ./media/show-current-user/email.png
[9]: ./media/show-current-user/preview.png


[!INCLUDE[footer-include](../../includes/footer-banner.md)]