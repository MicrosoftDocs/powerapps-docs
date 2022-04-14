---
title: Measure your space in mixed reality
description: Measure your space in mixed reality.
author: anuitz
ms.topic: overview
ms.custom: canvas
ms.reviewer: mduelae
ms.date: 04/14/2022
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - mduelae
  - anuitz
---

# Measure your space in mixed reality

Measure the distance, area, and volume of your physical space using your device camera.

To use the measurement feature, your app must enable the  [Measure in MR](mixed-reality-component-measure-distance.md) control for your canvas app.

## Prerequisites

Before you start taking measurements, follow these steps to enter basic information about your space.

1. Open your canvas app and select the **Measure in MR** button.
2. At the top select the drop-down list or select the list button.
 
   > [!div class="mx-imgBorder"]
   > ![Choose the item you want to meaaure.](./media/mr-measurement/measure-4.png)

3. On **the Measurement Inputs** screen, enter the required measurements.
   
   > [!div class="mx-imgBorder"]
   > ![Enter measurements](./media/mr-measurement/measurement-inputs-5.png)

4. When you're done, select the close button.

## Take a measurement

1. Open your canvas app and select the **Measure in MR** button.

2. Select the camera button and then follow the instructions on your screen

3. Keep moving your device until it vibrates, and white dots appear. The white dot with a circle is the starting point of your measurement.

4. Select the ![Measurement button](media/image8.png) button to start a new measurement. Follow these steps depending on the type of measurement:

    - **Distance:** Bring the dot to where you would like to end measurement and select the green checkmark button to finish.

    - **Area**: Outline the area you would like to measure by clicking the ![Icon Description automatically generated](media/image11.png) button to add points. Once you are done, bring the dot to where you began measuring and click the green check to finish measuring.

    - **Volume:** Outline the base of the volume you would like to measure by clicking the ![Icon Description automatically generated](media/image11.png) button to add points. Once you are done, bring the dot to where you began measuring to finish the base. Rotate your phone upwards to select the desired height of the volume and click the green check to finish measuring. ![A screenshot of a video game Description automatically generated with medium confidence](media/image15.jpeg) ![A picture containing text Description automatically generated](media/image16.jpeg) ![A picture containing diagram Description automatically generated](media/image17.png) ![](media/image18.png)

Some Power Apps may have Box Draw enabled, where volumes are restricted to rectangular prisms. Drawing is accomplished by selecting just four points: three to draw the base, and one for height.

![A screenshot of a cell phone Description automatically generated with medium confidence](media/image19.png) ![](media/image20.png) ![Diagram Description automatically generated](media/image21.jpeg) ![](media/image22.jpeg)

*Define length Define width Define height Finished volume*

- **Freeform:** Freeform allows distance, multi-segment, area, and volume all together. You can stop measuring by selecting the last point added. For example:

![Graphical user interface Description automatically generated with low confidence](media/image23.jpeg) ![A screenshot of a phone Description automatically generated with medium confidence](media/image24.jpeg)

A rectangle has been drawn on the floor. To decide to finish the area, keep your dot cursor at the last point you added. Click the green check to finish the measurement.

![](media/image25.jpeg) ![](media/image26.jpeg)

Alternatively, the same rectangle can be part of a volume measurement. Instead of selecting the same last point you added, rotate your phone upwards to select a height. Click the green check to finish the measurement.

Some Power Apps may have box draw enabled. In box draw, drawing in Freeform is limited to rectangular areas and volumes, similar to box draw for Volume measurements.

## Keeping track of your measurements

This feature has a useful log to show what measurements you've already taken.

1.  Tap either the measurement label at the top or the list button on the bottom to open the measurement log. Here you can see what kind of measurements you have, which measurements you have taken, and which you haven't.

2.  Tap the right arrow next to a measurement to see its details. Some things you can do here:

-   Tap one of the measurements' labels to remeasure or take a measurement out of the listed order.

-   Tap the trash can![Icon Description automatically generated](media/image27.png) icon to clear a measurement.

-   Click the ![](media/image28.png) or ![A picture containing icon Description automatically generated](media/image29.png) button to continue measuring where you left off.

*Tap to open menu Tap for details See measurement details*

## Button Guide

![](media/image33.png)![](media/image34.png) *Exit button*  
Leave the mixed reality experience to return to your Power App screen

![](media/image35.png) *Reset button*  
Remove the 3D model and enter placement mode to place the model again

![](media/image1.png) *Camera button*  
Screen capture the current view. These pictures may be used by your  
Power App and are not viewable while in the mixed reality experience.

#### ![](media/image2.png) Undo button

Undo the last chosen point to redo part of the measurement.

#### ![](media/image3.png) List button

Open a window that lists the details of the measurements.

#### ![A picture containing text Description automatically generated](media/image36.png) Submit button

Once you have finished measuring some or all measurements, you can press the submit button to close the mixed reality experience and send the measurement data to your app. Note that the button may be grayed out if no measurements were taken or a measurement is currently being taken.
