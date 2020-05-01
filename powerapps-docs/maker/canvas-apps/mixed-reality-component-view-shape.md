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
# Create and view predefined 3D shapes in mixed reality

You can use the **View shape in MR** component in your app to let users see a simple cube might fit within a specified space. 

The component creates a button in your app. When app users click the button, it overlays a cube onto the live camera feed of the device. You set up the dimensions of the cube when you edit the component in Power Apps.


To use the component, you need to [enable the mixed reality (MR) features for each app](#enable-the-mixed-reality-features-for-each-app) that you want to use it in. 

Make sure to also [review the prerequisites for using MR components](mixed-reality-overview.md#prerequisites).

>[!TIP]
>The MR controls work best in well-lit environments with flat-textured surfaces.  
>When establishing tracking, point the device at the surface you would like to track and slowly pan the device from right to left in broad arm motions.  
>If tracking fails, exit and enter the MR view to reset the tracking and try again.

## Use the component

Insert the component into your app as you normally would for any other button control or component.

With an app open for editing in the Power Apps https://create.powerapps.com studio:

1. Open the **Insert** tab.
2. Expand **Mixed reality**.
3. Select the component **View shape in MR** to place it in the center of the app screen, or drag and drop it to position it anywhere on the screen.

  ![](./media/augmented-view-shape/augmented-view-shape.png)

You can modify the component with a number of properties.

### Properties

The following properties can be defined and configured in the component's **View shape in MR** pane on the **Properties** and **Advanced** tabs. 

![](./media/augmented-view-shape/augmented-view-shape-properties.png)

Note that some properties are only available in the **Advanced** tab on the **View in MR** pane.

Property | Description | Type | Location
- | - | - | -
Text | Label for the button | String | Properties (also in **Advanced**)
Display type | Whether the button shows just an icon, text, or both | Drop-down selection | Properties (also in **Advanced**)
Shape width | Width of the cube. | Integer | **Properties** (also in **Advanced**)
Shape height | Height of the cube. | Integer | **Properties** (also in **Advanced**)
Shape depth | The three-dimensional depth of the cube. | Integer | **Properties** (also in **Advanced**)
Unit of measurement | The measurement unit used for the width, height, and depth fields. | Drop-down selection | **Properties** (also in **Advanced**)
Visible | Whether the component is shown or not. | Boolean | **Properties** (also in **Advanced**)
Position | X is the horizontal position of the component on the app screen. 0 is the leftmost edge of the screen. <br/>Y is the vertical position of the component on the app screen. 0 is the topmost edge of the screen. | Pixels | **Properties** (also in **Advanced** as individual X and Y values)
Size | Width and height of the component in pixels. | Pixels | **Properties** (also in **Advanced** as individual width and height values)
Padding top, bottom, left, right | How much padding between the associated edge and the label inside the button. | Pixels | **Properties** (also in **Advanced**)
Font options | Font and styling that should be used for the button's text. | String | **Properties** (also in **Advanced**)
Disabled options | How the button should appear if it's set to a disabled state, where the app user will not be able to interact with it. | **Properties** (also in **Advanced**)
OnChange | Defines what happens when an event occurs within the component | Formula | **Advanced**
FillColor | Color of the button | RGBA or HTML hexadecimal color codes | **Advanced**
Tooltip | Descriptive text that appears when a user navigates to the component. | String | **Advanced**
DisplayMode | The mode to use for data cards and controls within the component. `DisplayMode.Edit` allows users to edit the component's forms and controls, `DisplayMode.View` sets the component to read only | String | **Advanced**
TabIndex | Order in which items on the app screen be tabbed between. | Integer | **Advanced**


## Other augmented reality controls
- View 3D models with the **[View in 3D](mixed-reality-component-view-3d.md)** component.
- View 3D models in the real world with the **[View in mixed reality](mixed-reality-component-view-mr.md)** component.
- Take measurements and create 3D volumes with the **[Measure in mixed reality](mixed-reality-component-measure-distance.md)** component.

