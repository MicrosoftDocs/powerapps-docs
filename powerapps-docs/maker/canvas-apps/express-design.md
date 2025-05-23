---
title: Express design
description: Learn about using the express design features such as creating apps from an image or a Figma design.
author: norliu
ms.topic: article
ms.custom: canvas
ms.date: 05/24/2022
ms.subservice: canvas-maker
ms.author: norliu
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - norliu
  - mduelae
---

# Express design

Express design is a new way to quickly get started with Power Apps by instantly transforming your visual design into an app. With **Express design**, makers can quickly turn existing design artifacts—including paper forms, whiteboard sketches, or Figma files—directly into a working app.

Whether it’s handling the detailed adjustments required to generate pixel-perfect UI, or creating a new data source and setting the formulas to connect it to your app, Express design does the heavy lifting so you can jumpstart the app development process and build with ease and confidence.

:::image type="content" source="media/express-design/express-design-overview.png" alt-text="Express design overview.":::

Express design currently supports design artifacts in the form of an image or a Figma design file.

## Image to app

If you have a wireframe or a visual design that you want to convert into an app, you can use **Image to app** to quickly generate an app and connect it to data. Upload an image of your design and follow the steps in the guided interface to tag the components and set up your data. For more information, see [Create an app from an image (preview)](app-from-image.md).

:::image type="content" source="media/express-design/app-from-image.png" alt-text="Create an app from an image.":::

> [!div class="nextstepaction"]
> [Create an app from an image](app-from-image.md)

## Figma to app

If you’re looking to generate a pixel-perfect app with exact styles that match your designs, you can use the [Create Apps from Figma UI Kit](https://go.microsoft.com/fwlink/?linkid=2193981) to design your app in Figma. Then, use the **Figma to app** feature to convert your design file into app UI. From here, you can continue building in Power Apps Studio to add more advanced functionality, such as connecting to data. For more information, see [Create an app from Figma (preview)](figma/overview.md).

:::image type="content" source="media/express-design/app-from-figma.png" alt-text="Create an app from a Figma page or a frame.":::

> [!div class="nextstepaction"]
> [Create an app from Figma](figma/overview.md)

## Enable and disable

Express design features are generally available and turned on by default for your environment. You can use PowerShell command to turn the feature on or off.

The setting name:

**powerPlatform.powerApps.disableCreateFromFigma**
When this setting is true, users in the environment will not have the ability to use app from Figma. It is false by default.

**powerPlatform.powerApps.disableCreateFromImage**
When this setting is true, users in the environment will not have the ability to use app from Image. It is false by default.

```
# update the desired setting
$requestBody = [pscustomobject]@{
  powerPlatform = [pscustomobject]@{
    powerApps = [pscustomobject]@{
      disableCreateFromFigma = $True
    }
  }
}
Set-TenantSettings -RequestBody $requestBody
```

### See also

- [Create an app from an image](app-from-image.md)
- [Create an app from Figma (preview)](figma/overview.md)
- [Set-TenantSettings](/powershell/module/microsoft.powerapps.administration.powershell/set-tenantsettings)
