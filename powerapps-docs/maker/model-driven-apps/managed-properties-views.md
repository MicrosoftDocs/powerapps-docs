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
 
 If a custom public view has been created for a table in Power Apps and this is included in a managed solution there is the option to limit the ability of anyone who is installing the solution from customizing the view.

 In addition to this there are also high level options that can be applied to the table that apply to all views.  
  
 By default, most views have their **Customizable** managed property set to true so that people can customize them. Unless there is a very good reason to change this, it is recommend to allow people to customize views in the table.  
  
## Set managed properties for all views  

1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

2.  Select **Solutions**, open the solution required. Select **Tables**, then select the table required.

3.  Select the three dots either next to the table or in the top menu, then select **managed properties**.

:::image type="content" source="media/table-managed-properties-navigation.png" alt-text="Selecting managed properties":::

4.  There are a range of options relevant to the current table to either prevent any customizations or to prevent the creation of new views.

:::image type="content" source="media/table-managed-properties.png" alt-text="Managed properties options":::

5.  Make any necessary changes and when finished, select **Done**.  
  
> [!NOTE]
> The setting does not take effect until the solution is exported from the development environment and imported as a managed solution into a new environment.

## Set managed properties for a view (classic)

With this approach the ability for the view to be amended can be set at the level of the individual view.
  
1.  Open [solution explorer](advanced-navigation.md#solution-explorer), expand **Entities**, select the table required, and then select **Views**.  
  
2.  Select a custom public view.  
  
3.  On the menu bar, select **More Actions** > **Managed properties**.  

    > [!div class="mx-imgBorder"] 
    > ![managed properties menu.](media/managed-properties.png)
  
4.  Set the **Customizable** or **Can Be Deleted** options to **True** or **False**.  

    > [!div class="mx-imgBorder"] 
    > ![Set managed properties.](media/set-managed-properties.png)

## Next steps

[Specifying a default view](specify-default-views.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]