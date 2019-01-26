---
title: Show details about the current user in a canvas app | Microsoft Docs
description: In PowerApps, display the name and email address of the signed-in user in a canvas app
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 10/16/2016
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Show information about a PowerApps user in a canvas app

In PowerApps, show the full name, the email address, and the picture that's associated with the user who's signed in to a canvas app. You can use this information, for example, to automatically fill in a form.

For example, you can use this feature to:

* Create a sign-up "sheet" for users to attend training, volunteer for events, check in at a kiosk, and more.
* Display the full name on a Human Resources app.
* Automatically enter an email address when contacting your helpdesk.

Basically, you can use this anywhere users would benefit from a form or labels that are populated automatically

[!INCLUDE [app-customization-requirements](../../includes/app-customization-requirements.md)]

## Show user details

1. On the **Insert** tab, click or tap **Media**, and then click or tap **Image**.
   
   ![][2]
2. Set the **[Image](controls/properties-visual.md)** property to this formula:
   <br>**User().Image**
   
    ![][3]
3. On the **Insert** tab, click or tap **Text**, and then click or tap **Label**:  
   
    ![][4]
4. Set the **[Text](controls/properties-core.md)** property to this formula:
   <br>**User().FullName**
   
   ![][6]
   
   When you do this, the label is automatically populated with your full name. Move the label so it's below the image control, similar to the following:
   
   ![][5]
5. Add another label, and set its **[Text](controls/properties-core.md)** property to this formula:
   <br>**User().Email**  
   
    ![][8]
   
    When you do this, the label is automatically populated with your email address. Move the label so it's below the first label, similar to the following:  
   
    ![][7]

[2]: ./media/show-current-user/add-image.png
[3]: ./media/show-current-user/imageproperty.png
[4]: ./media/show-current-user/insertlabel.png
[5]: ./media/show-current-user/label.png
[6]: ./media/show-current-user/textproperty.png
[7]: ./media/show-current-user/secondlabel.png
[8]: ./media/show-current-user/email.png
[9]: ./media/show-current-user/preview.png
