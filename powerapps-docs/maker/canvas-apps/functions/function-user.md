---
title: User function | Microsoft Docs
description: Reference information, including syntax, for the User function in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 11/07/2016
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# User function in PowerApps
Returns information about the current user.

## Description
The **User** function returns a [record](../working-with-tables.md#records) of information about the current user:

| Property | Description |
| --- | --- |
| **User().Email** |Email address of the current user. |
| **User().FullName** |Full name of the current user, including first and last names. |
| **User().Image** |Image of the current user. This will be an image URL of the form "blob:*identifier*". Set the **[Image](../controls/properties-visual.md)** property of the **[Image](../controls/control-image.md)** control to this value to display the image in the app. |

> [!NOTE]
> The information returned is for the current PowerApps user.  It will match the "Account" information that is displayed in the PowerApps players and studio, which can be found outside of any authored apps.  This may not match the current user's information in Office 365 or other services.

## Syntax
**User**()

## Examples
The current PowerApps user has the following information:

* Full Name: **"John Doe"**
* Email address: **"john.doe@contoso.com"**
* Image: ![](media/function-user/john-doe-picture.png) 

|       Formula       |                                                                    Description                                                                    |                                                 Result                                                  |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
|     **User()**      |                                             Record of all information for the current PowerApps user.                                             |    { FullName:&nbsp;"John Doe", Email:&nbsp;"john.doe@contoso.com", Image:&nbsp;"blob:1234...5678" }    |
|  **User().Email**   |                                                 The email address of the current PowerApps user.                                                  |                                         "john.doe@contoso.com"                                          |
| **User().FullName** |                                                   The full name of the current PowerApps user.                                                    |                                               "John Doe"                                                |
|  **User().Image**   | The image URL for the current PowerApps user.  Set the **Image** property of the **Image** control to this value to display the image in the app. | "blob:1234...5678"<br><br>With **ImageControl.Image**:<br>![](media/function-user/john-doe-picture.png) |

