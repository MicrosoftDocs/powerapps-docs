---
title: "Modern theme overrides | MicrosoftDocs"
description: Learn how to change the colors of the app header with the new look.
ms.custom: ""
ms.date: 10/11/2023
ms.reviewer: "matp"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
author: "jasongre"
ms.subservice: mda-maker
ms.author: "jasongre"
search.audienceType: 
  - maker
---

# Theme overrides

Model-driven apps with the [modern, refreshed look for model-driven apps](../../user/modern-fluent-design.md) provide updated styling aligned to the Microsoft Fluent 2 design system. Because this modern refreshed look comes with a new theming system, [classic theming](create-themes-organization-branding.md) is not honored. In this article, you learn about the styling overrides available with the modern, refreshed look and how to implement them for your organization.  

## Modify the app header colors

With the modern, refreshed look enabled, you can modify the colors used by the app header to align with your personal or organizational branding. To accomplish this, you will  encapsulate your desired colors into an XML resource, use an app setting to point to this web resource, and then verify the color changes match your expectation.  

  > [!NOTE]
  > This functionality is available in build 9.4.23094 and later.

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

```xml
<AppHeaderColors
// Required color
background=”000000”

// Optional colors
/>
```

As an example, this XML specifies a green background color for the app header with white text, with darker background colors for the various button interaction states. For optimal usability, we recommend specifying different color values for each state.  

```xml
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
```

### Create the web resource

1. Sign into [Power Apps](https://make.powerapps.com/), select **Solutions** on the left navigation pane, and then create a **New solution**.

### Apply custom app header colors to apps in your environment 

After you’ve selected your colors and created the XML resource, follow these steps to enable this app header styling for all the apps in your environment that have the “New look” enabled.

1. Select **Solutions** on the left navigation pane, and then create a **New solution**.
1. Select **Add existing** > **More** > **Setting**.
1. Type *Override* in the **Search** box, select **Override app header color**, select **Next**, and then select **Add**.
1. In the solution, select **Override app header color**, and then select **Edit** on the command bar.
1. On the right **Edit Override ap header color** properties pane, update **Setting environment value** to the name of your web resource. 
1. Select **Save**.
1. **Publish all customizations**.

With the example colors above, the header should look like this after  refreshing or playing the app.  
:::image type="content" source="media/greenAppHeader-Oct2023.png" alt-text="Green app header in a model-driven app" lightbox="media/greenAppHeader-Oct2023.png"::: <!-- This media file is missing -->

### Verifying new app header colors

After publishing your new app header colors, you will want to validate the app header visuals, including all the button states, to ensure everything appears as you expect and there are sufficient contrast ratios for accessibility. You should verify the following: 
-  The desired colors are shown for the app header at rest and for each button interaction state. 
-  There is a minimum of a 4.5:1 contrast ratio between foreground and background colors for the rest state and each button interaction state.

## Related links
[Modern refreshed look](../../user/model-fluent.design.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
