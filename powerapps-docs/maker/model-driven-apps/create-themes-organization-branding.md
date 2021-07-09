---
title: "Change the color scheme or add a logo to match your brand  | MicrosoftDocs"
description: Learn how to change the color scheme for your app with Power Apps
ms.custom: ""
ms.date: 01/12/2021
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
author: "Mattp123"
ms.assetid: 21a166a0-d25e-4260-a1e4-2ddc528787c2
caps.latest.revision: 17
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Use a theme to create a custom look for your app

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can create a custom look and feel (a theme), for your app by making changes to the default colors and visual elements provided in the uncustomized system. For example, you can create your personal product branding by adding a company logo and providing table-specific coloring. A theme can be created by using the **Themes** area, without requiring a developer to write code. You can create, clone, change, or delete themes that are used in your environment. 

> [!NOTE]
> You can define multiple themes, but only one can be active in the system and is identified as the default theme. To make a theme active, you publish it.
  
<a name="UseThemes"></a>   
## Use themes to enhance the user interface and create your product branding

 Theming is used to enhance the app user interface, not drastically alter it. The theme colors are applied globally throughout your model-driven apps. For example, you can enhance the following visual elements in the UI:  
  
- Change navigation colors to create product branding.
  
- Adjust accent colors, such as hover or selection colors.
  
- Provide table-specific coloring.
    
- Logo. (Use an existing or add a new image file as a web resource.)
  
- Logo tooltip.
  
- Navigation bar color.  
  
- Title text color.  
  
- Selected link color.  
  
- Hover link color.  
  
- Legacy accent color (primary background for process controls).
  
- Default color for tables.
  
- Default custom tables color.
  
- Control fill color.
  
- Control border color. 
  
<a name="Solution"></a>   
## Solution awareness

Themes aren't solution aware. The changes made for an organization's theme aren’t included in  solutions exported from the organization. The data is stored in the theme table that can be exported and re-imported in another environment. The imported theme must be published to take effect.  
  
<a name="CloneAlter"></a>   
## Copy and alter the existing theme

 The easiest and quickest way to create a new theme is to clone and alter an existing theme, then save, preview and publish it.
 
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Settings** ![Settings icon.](../model-driven-apps/media/powerapps-gear.png) (upper right), and then select **Advanced settings**.
1. Select **Customizations**, and then select **Themes**.
1. Under **All themes**, select the theme you want to clone, such as the **CRM Default Theme**. Select **Clone** on the command bar.
1. Replace an existing UI item's hexadecimal number, such as the **Title Text Color**, with the hexadecimal value that represents the color you want.

For example, the **CRM Default Theme** was cloned and changed using mostly varying shades of green color. The following screenshots show the new colors for navigation and highlighting. A custom logo was also added that will appear in the upper left corner of an app.  
 
 > [!div class="mx-imgBorder"] 
 > ![Gentle green theme colors for navigation bar.](media/theme-gentle-green.png "Gentle green theme colors for navigation bar")

 > [!div class="mx-imgBorder"] 
 > ![Gentle green theme colors for UI elements.](media/theme-gentle-green2.png "Gentle green theme colors for UI elements")  
  
 The following image shows an app account view with the new colors and logo.

 > [!div class="mx-imgBorder"] 
 > ![Gentle green theme account grid.](media/themes-gentle-green-account-grid.png "Gentle green theme account grid")  

> [!IMPORTANT]
> Logos that are too large won't display. The image used in the example is 156 pixels wide x 48 pixels height.

<a name="Publish"></a>   
## Preview and publish a theme  
 To preview and publish a theme, do the following steps:  
  
1. Create a **New** theme from scratch or **Clone** an existing one.  
1. **Preview** the new theme. To exit the preview mode, choose **Exit Preview** on the command bar.  
1. Publish the theme. Select **Publish Theme** on the command bar to make it the active (default) theme in the environment.  
  
 The following screenshot shows the buttons on the command bar for preview and publishing.  
  
 ![Use preview buttons to enter&#47;exit the preview mode.](media/themes-preview-buttons.PNG "Use preview buttons to enter/exit the preview mode")  
  
<a name="BestPracticies"></a>   
## Best practices

 Following are the recommendations for designing theme contrasts and choosing colors.  
  
### Theme contrast

 We recommend the following approach to providing contrast colors:  
  
-   Carefully choose the contrasting colors. The Microsoft Dataverse out-of-the-box default theme has the correct contrast ratios to ensure optimal usability. Use similar contrast ratios for your new themes.  
  
-   For high contrast mode, use the default color settings.  
  
### Theme colors

 We recommend that you don’t use a large number of different colors. Although you can set a different color for every table, we recommend one of two patterns:  
  
-   Make all tables in neutral colors and highlight the key tables.  
  
-   Use the same color for similar tables or related tables, such as queue and queue item, or product catalog tables. Keep the total number of groups low.  
  
<a name="Considerations"></a>   
## Custom theme considerations

 You should consider the following when planning on using custom themes:  
  
-   Most updated user interface (UI) areas will be displayed in the custom theme colors.  
  
-   Even though the theme colors are applied globally throughout the application, some legacy UI areas, such as gradient buttons, will retain the default colors.  
  
-   Certain areas must use dark or light colors to contrast with the default icon colors. The icon color isn’t customizable.  
  
-   A table can’t be displayed in different colors under different Sitemap nodes.  
  
-   The Sitemap nodes colors aren’t customizable.  
  
## See also  
         
 [Video: Themes](https://go.microsoft.com/fwlink/p/?LinkId=529568) <br />
 [Query and edit an organization theme](/dynamics365/customer-engagement/developer/customize-dev/query-and-edit-an-organization-theme)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]