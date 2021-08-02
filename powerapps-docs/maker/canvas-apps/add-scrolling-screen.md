---
title: Add a scrolling screen to a canvas app
description: In Power Apps, create a screen that users can scroll to show more types of content than the screen can show at a time in a canvas app.
author: emcoope-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/25/2016
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - emcoope-msft
---
# Add a scrolling screen to a canvas app

In a canvas app, create a screen that users can scroll to show different items. For example, create a phone app that shows data in several charts, which users can display if they scroll.

When you add multiple controls in a section, the controls maintain their relative positions within that section, regardless if it's a phone app or a tablet app. Note that the screen size and orientation may determine how the sections are arranged.  

[!INCLUDE [app-customization-requirements](../../includes/app-customization-requirements.md)]

## Create a scrolling screen

1. On the **Home** tab, click or tap **New screen**:

    ![Option to add a screen to an app][1]

2. On the **Home** tab, click or tap **Layouts**, and then click or tap the option to add an infinite scrolling canvas:  
   
    ![Option to add an infinite scrolling canvas][2]
   
    The canvas is added:  
   
    ![A screen with an infinite scrolling canvas, as it appears by default][3]

## Add elements
Now, let's add some controls to the canvas to see how the scrolling screen works.

1. In the canvas you added, click or tap **Add an item from the Insert tab**.
   
    ![Add an item from the Insert tab][4]
2. On the **Insert** tab, click or tap **Charts**, and then click or tap **Column Chart**.
   
    ![The option to add a column chart][5]
   
    A column chart appears in the first card on the screen:  
   
    ![Default column chart][7]
3. On the **Insert** tab, click or tap **Text**, and then click or tap **Pen input**:  
   
    ![Option to add a pen control][8]
4. Move the pen control below the chart, and resize the pen control to cover the bottom of the card:  
   
    ![Move and resize the pen control][9]

## Add a section
Now, let's add another card with another control.

1. Near the bottom of the screen, click or tap **Add section**:  
   
    ![Option to add a section][10]
   
    A new card is added to the screen:  
   
    ![A new card below the default section][11]
2. With the card still selected, go to the **Insert** tab, click or tap **Charts**, and then click or tap **Line chart**.
   
    The new chart is too big to appear on the screen with the other controls:  
   
    ![A line chart added to the bottom of the new card][12]
3. Open Preview mode by pressing F5 (or by clicking or tapping the play icon near the upper-right corner).
   
    ![Open Preview mode.](./media/add-scrolling-screen/open-preview.png)
4. Scroll down to display the new line chart.  
   
    ![Preview shows the line chart][13]

[1]: ./media/add-scrolling-screen/add-screen.png
[2]: ./media/add-scrolling-screen/add-canvas.png
[3]: ./media/add-scrolling-screen/default-canvas.png
[4]: ./media/add-scrolling-screen/insert-visual.png
[5]: ./media/add-scrolling-screen/add-chart.png
[7]: ./media/add-scrolling-screen/default-chart.png
[8]: ./media/add-scrolling-screen/add-pen.png
[9]: ./media/add-scrolling-screen/move-resize-pen.png
[10]: ./media/add-scrolling-screen/add-section.png
[11]: ./media/add-scrolling-screen/new-card.png
[12]: ./media/add-scrolling-screen/add-line-chart.png
[13]: ./media/add-scrolling-screen/line-chart-preview.png


[!INCLUDE[footer-include](../../includes/footer-banner.md)]