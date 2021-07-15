---
title: Display a full-sized image on a canvas app form
description: Learn about how to display a full-sized image on a canvas app form.
keywords: ""
ms.date: 11/09/2020
ms.service: powerapps
ms.custom: 
ms.topic: article
applies_to: 
  - "powerapps"
author: "Mattp123"
ms.assetid: 
ms.subservice: canvas-maker
ms.author: matp
manager: kvivek
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Display a full-sized image on a canvas app form
By default,	when an app user adds an image to display to a form in a canvas app, the image displayed is the thumbnail image. To display a full image for a canvas app, follow these steps: 
1. Open the canvas app in PowerApps Studio. 
2. Select **Insert**, and then select **Image**.
3. Select the image data card. 

    > [!div class="mx-imgBorder"] 
    > ![Image data card.](../canvas-apps/media/display-full-sized-image/image-data-card.png)

4. Under the **Advanced** tab set the **Data** field to the table that contains the image you want to display.
5.	Add **.Full** after the value for the image **Default** setting. 

    > [!div class="mx-imgBorder"] 
    > ![Image full size setting.](../canvas-apps/media/display-full-sized-image/image-full-setting.png)

6.	Select **Save**. 

### See also
[Show, edit, or add a record in a canvas app](add-form.md) <br />
[Image fields](../data-platform/types-of-fields.md#image-columns)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]