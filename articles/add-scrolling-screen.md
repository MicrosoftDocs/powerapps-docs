<properties
	pageTitle="Add a scrolling screen | Microsoft PowerApps"
	description=""
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="aftowen"
	manager="dwrede"
	editor=""
	tags=""/>
<tags
	ms.service="powerapps"
	ms.devlang="na"
	ms.topic="article"
	ms.tgt_pltfrm="na"
	ms.workload="na"
	ms.date="11/18/2015"
	ms.author="anneta"/>

# Add a scrolling screen in PowerApps #
Create a screen that users can scroll to show more types of content than the screen can show at a time. For example, you might want to juxtapose multiple charts, videos, or other kinds of data from different sources on the same screen while keeping each element big enough to see clearly. If you add controls to multiple sections, the relative position of each element is maintained, even if the screen orientation changes between portrait and landscape.  

[What are PowerApps?](http://www.powerapps.com)

**Prerequisites**
- [Install PowerApps](http://aka.ms/installpowerapps)
- Learn how to [configure a control](get-started-test-drive.md#configure-a-control) in PowerApps

## Create a scrolling screen, and add an element
1. Open PowerApps, and then do one of the following:

	- [Add a screen](add-screen-context-variables.md) to a PowerApp.

	![Option to add a screen to a PowerApp](./media/add-scrolling-screen/add-screen.png)

	- Create a PowerApp from scratch. (Select **New** in the **File** menu, and then select **Get started** under **Start from scratch**.)

	![Option to create an app from scratch](./media/add-scrolling-screen/blank-app.png)

1. On the **Home** tab, select **Layouts**, and then select the option to add an infinite scrolling canvas.

	![Option to add an infinite scrolling canvas](./media/add-scrolling-screen/add-canvas.png)

	The canvas is added to the screen.

	![A screen with an infinite scrolling canvas, as it appears by default](./media/add-scrolling-screen/default-canvas.png)

1. Select **Insert a visual**, select **Charts** on the **Insert** tab, and then select **Column Chart**.

	![The option to add a column chart](./media/add-scrolling-screen/add-chart.png)

	A column chart appears in the first card on the screen.

	![Default column chart](./media/add-scrolling-screen/default-chart.png)

1. On the **Insert** tab, select **Text** and then select **Pen**.

	![Option to add a pen control](./media/add-scrolling-screen/add-pen.png)

1. Move the pen control below the chart, and resize the pen control to cover the bottom of the card.

	![Move and resize the pen control](./media/add-scrolling-screen/move-resize-pen.png)

## Add a section ##

1. Near the bottom of the screen, select **Add section**.

	![Option to add a section](./media/add-scrolling-screen/add-section.png)

	A card is added to the screen

	![A new card below the default section](./media/add-scrolling-screen/new-card.png)

1. With the card still selected, add a line chart, which is too big to appear on the screen with the other controls.

	![A line chart added to the new card](./media/add-scrolling-screen/add-line-chart.png)

1. Press F5 to display the app in Preview, and then scroll to display the new chart.

	![Preview shows line chart](./media/add-scrolling-screen/line-chart-preview.png)
