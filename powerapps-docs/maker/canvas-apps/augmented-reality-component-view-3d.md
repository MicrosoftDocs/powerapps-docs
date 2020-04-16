---
title: 
description: 
author: iaanw
manager: shellha
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 3/19/2020
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# View 3D objects in canvas and model-driven apps

Add 3D models to your canvas and model-driven apps built in Power Apps. Use the **View in 3D** component to rotate the shape and zoom into the model with simple gestures.

You can display a single 3D object, or you can let the user see [multiple objects by connecting the component to the **Gallery** control](#define-the-location-for-3d-objects).

![](./media/augmented-3d/augmented-3d-viewer.png)

>[!IMPORTANT]
>Your 3D objects must be in the .glb file format.  
>You can use the [AR Import Tool](/dynamics365/mixed-reality/import-tool/) to convert from a variety of industry 3D formats into .glb.


To use the component, you need to [enable the mixed reality features for each app](#enable-the-mixed-reality-features-for-each-app) that you want to use it in.


## Properties

The following properties can be defined and configured in the **View in 3D** component's **View in 3D** pane on the **Properties** and **Advanced** tabs. 

![](./media/augmented-3d/augmented-3d-viewer-controls.png)

Note that some properties are only available in the **Advanced** tab on the **View in 3D** pane.

Property | Description | Type | Location
- | - | - | -
Source | Data source that identifies the .glb file to display. <br/>Within **model-driven apps**, the **View in 3D** component is bound to a *SingleLine.URL* field property. This means that you can only add the component to a *SingleLine.URL* field on the form. An example is the **Website** field on the **Account** entity. <br/>Within **canvas apps**, the **View in 3D** component supports loading models from publically accessible, CORS-compliant URLs, base64-encoded models, and as attachments or media content accessed through data connectors. | Not applicable | Properties (also in **Advanced** as **Src**)
Background fill | Set the background color for the component. | Color picker | Properties (also in **Advanced** as **BackgroundFill**, where it accepts RGBA or HTML hexadecimal color codes)
OnChange |  | Boolean | Advanced
Tooltip | Descriptive text that appears when a user navigates to the map component. | String | Advanced
DisplayMode | | String | Advanced
Height | Height of the component in pixels. | Pixels | Advanced
TabIndex | Order in which items on the app screen be tabbed between. | Integer | Advanced
Visible | Whether the component is shown or not. | Boolean | Advanced
Width | Width of the component in pixels. | Pixels | Advanced
X | Horizontal position of the component on the app screen. 0 is the leftmost edge of the screen. | Pixels | Advanced
Y | Vertical position of the component on the app screen. 0 is the topmost edge of the screen. | Pixels | Advanced


## Define the location for 3D objects


## Other augmented reality controls
- [View in augmented reality](augmented-reality-component-view-ar.md)
- [Measure in augmented reality - distance](augmented-reality-component-measure-distance.md)
- [Measure in augmented reality - advanced](augmented-reality-component-measure-advanced.md)
- [View shape in augmented reality](augmented-reality-component-view-shape.md)

## Next steps
Explore [example AR apps](augmented-reality-example-apps.md) and see what sorts of scenarios AR controls can help solve
