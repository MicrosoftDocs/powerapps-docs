---
title: "Modern theme overrides | MicrosoftDocs"
description: Learn how to change the colors of the app header with the New look.
ms.custom: ""
ms.date: 10/11/2023
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
author: "jasongre"
ms.assetid: 21a166a0-d25e-4260-a1e4-2ddc528787c2
caps.latest.revision: 17
ms.subservice: mda-maker
ms.author: "jasongre"
search.audienceType: 
  - maker
---

# Modern theme overrides

Model-driven apps with the [modern, refreshed look](../../user/model-fluent.design.md) provide updated styling aligned to the Microsoft Fluent 2 design system. Because this modern refreshed look comes with a new theming system, [classic theming](create-themes-organization-branding.md) is not honored. In this article, you will learn about the styling overrides available with the modern, refreshed look and how to implement them for your organization.  

## Modify the app header colors 
With the modern, refreshed look enabled, you can modify the colors used by the app header to align with your personal or organizational branding. To accomplish this, you will  encapsulate your desired colors into an XML resource, use an app setting to point to this web resource, and then verify the color changes match your expectation.  

### Create an XML resource with your app header colors
The first step to modifying the app header styling is to create an XML file with your various color selections and add it as a web resource. 

The following styling options for the app header are available: 
-  **Background** – The background color of the app header. This element must be defined for any changes to take effect. 
-  **Foreground** – The text color of the app header. If this is not specified, the system will attempt to calculate an appropriate color that has sufficient contrast to the provided background color. 
-  **BackgroundHover** – The background color of buttons on the app header when they are hovered over. If no value is specified, the system will calculate a color based on the background color. 
-  **ForegroundHover** – The text color of buttons on the app header when they are hovered over. If no value is specified, the system will attempt to calculate an appropriate color that has sufficient contrast to the backgroundHover color. 
-  **BackgroundPressed** – The background color of buttons on the app header when they are pressed.  The defaulting logic is the same as backgroundHover. 
-  **ForegroundPressed** – The text color of buttons on the app header when they are pressed.  The defaulting logic is the same as foregroundHover.
-  **BackgroundSelected** – The background color of buttons on the app header when they are selected.  The defaulting logic is the same as backgroundHover.
-  **ForegroundSelected** – The text color of buttons on the app header when they are selected.  The defaulting logic is the same as backgroundHover.

Your XML file should be formatted as follows: 

     <AppHeaderColors
     // Required color
     background=”000000”
     
     // Optional colors
     />

As an example, this XML specifies a green background color for the app header with white text, with darker background colors for the various button interaction states. For optimal usability, we recommend specifying different color values for each state.  

     <AppHeaderColors 
        //Required color
        background="#12783F" 
     
        //Optional colors
        foreground="#FFFFFF" 
        backgroundHover="#165A31" 
        foregroundHover="#FFFFFF"
        backgroundPressed=”#0F1C12”
        foregroundPressed="#FFFFFF"
        backgroundSelected="#153D23" 
        foregroundSelected="#FFFFFF"
     />

### Apply custom app header colors to apps in your environment 
After you’ve selected your colors and created the XML resource, follow these steps to enable this app header styling for all the apps in your environment that have the “New look” enabled. 

1.	Create a new solution.
2.	Select **Add existing > More > Setting**.
3.	Search for **Override**.
4.	Select **Override app header colors**.
5.	Select **Add** to add it to the solution.
6.	Select **Override app header colors** from the solution explorer.
7.	Update **Setting environment value** to the name of your web resource.
8.	Select **Save**.
9.	**Publish all customizations**.

With the example colors above, the header should look like this after  refreshing or playing the app.  
:::image type="content" source="media/greenAppHeader-Oct2023.png" alt-text="Green app header in a model-driven app" lightbox="media/greenAppHeader-Oct2023.png":::

### Verifying new app header colors
After publishing your new app header colors, you will want to validate the app header visuals, including all the button states, to ensure everything appears as you expect and there are sufficient contrast ratios for accessibility. You should verify the following: 
-  The desired colors are shown for the app header at rest and for each button interaction state. 
-  There is a minimum of a 4.5:1 contrast ratio between foreground and background colors for the rest state and each button interaction state. 

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
