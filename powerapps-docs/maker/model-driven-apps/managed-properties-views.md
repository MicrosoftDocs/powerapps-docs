---
title: "Model-driven app managed properties for views with Power Apps | MicrosoftDocs"
description: "Learn how to set managed properties for a view"
ms.custom: ""
ms.date: 06/12/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: a9014576-8fb2-4f28-b8bb-5d2d49d76e12
caps.latest.revision: 25
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Model-driven app managed properties for views

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

<a name="BKMK_ManagedProperties"></a>   
 
 If you create a custom public view in Power Apps that you want to include in a managed solution that you will distribute, you have the option to limit the ability of anyone who is installing your solution from customizing the view.  
  
 By default, most views have their **Customizable** managed property set to true so that people can customize them. Unless you have a very good reason to change this, we recommend you allow people to customize views in your app.  
  
## Set managed properties for a view  
  
1.  Open [solution explorer](advanced-navigation.md#solution-explorer), expand **Entities**, select the table that you want, and then select **Views**.  
  
2.  Select a custom public view.  
  
3.  On the menu bar, select **More Actions** > **Managed properties**.  

    > [!div class="mx-imgBorder"] 
    > ![managed properties menu.](media/managed-properties.png)
  
4.  Set the **Customizable** or **Can Be Deleted** options to **True** or **False**.  

    > [!div class="mx-imgBorder"] 
    > ![Set managed properties.](media/set-managed-properties.png)
  
> [!NOTE]
> The setting does not take effect until you export a solution that contains the view as a managed solution and install it in a different environment.  

## Next steps
[Understand views](create-edit-views.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]