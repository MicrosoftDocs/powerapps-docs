<properties
	pageTitle="Create or Edit apps in a browser | Microsoft PowerApps"
	description="Create or Edit apps in a browser."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="sarafankit"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="07/28/2016"
   ms.author="ankitsar"/>

# Create or Edit apps in a browser #

**Note** PowerApps Studio for web is in preview and has certain limitations. You can also create and edit apps by [installing PowerApps Studio for Windows](https://web.powerapps.com/#/downloads) on a computer that's running Windows 8.1 or Windows 10.

Learn how to get with started with PowerApps Studio for web to create and edit apps in a browser. 

## Prerequisites ##
- [Sign up](signup-for-powerapps.md) for PowerApps.
- Microsoft Edge, Google Chrome or Internet Explorer 11 on Windows or Mac

## Launching  PowerApps Studio for web ##
1. Sign-in to [powerapps.com](http://go.microsoft.com/fwlink/p/?LinkId=708209)

1. In the left navigation bar, select **New app** (near the bottom left edge of screen).

	![New app on navigation bar](./media/create-app-browser/left-nav.png)

1. In the pop-up, select the second option for **PowerApps Studio for web**.

	![Select PowerApps Studio for web](./media/create-app-browser/launch-web-authoring.png)

1. **PowerApps Studio for web** will launch in a new tab in your browser, you will get the same experiences as the **PowerApps Studio for Windows**. 

## Next steps ##
- [Automatically generate an app](get-started-create-from-data.md) that's designed specifically for your data.
- Learn how to [add a control and set its properties](add-configure-controls.md).
- Unleash your creativity by [creating an app from scratch](get-started-create-from-blank.md).

## Known Issues/Limitations ##
1. **Creating an app from a template**
	
	You can't currently [create an app from a template](get-started-test-drive.md) in a browser. You will have to use PowerApps Studio for Windows to create an app from a template. 

1. **[Acceleration](functions/signals.md)** and **[Compass](functions/signals.md)** functions do not return real values during authoring, they will always return zero values. The functions will return real signals in a published app.

1. **[Export](controls/control-export-import.md)** and **[Import](controls/control-export-import.md)** controls do not work while authoring, they will behave correctly in a published app.

1. **[Creating connections](add-manage-connections,md)** to data sources requiring service authentication is currently not supported, you can use existing connections from PowerApps Studio for web. You can [create such connections](add-manage-connections.md) using [powerapps.com](http://go.microsoft.com/fwlink/p/?LinkId=708209).

1. **Adding or modifying Flows**
	
	Currently it is not possible to [add new or modify existing Flows](using-logic-flows.md) in your app. You must use PowerApps Studio for Windows to add or modify Flows in your apps. 

1. **Support for Undo/Redo**
	
	PowerApps Studio for web does not supports undo/redo of user actions. If you need to revert any changes, you will have to do them manually.

1. **Copying controls across two sessions**
	
	You cannot copy controls from one session of PowerApps Studio for web to another session of PowerApps Studio for web
