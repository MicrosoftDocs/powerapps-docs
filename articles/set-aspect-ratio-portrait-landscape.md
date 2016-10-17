<properties
	pageTitle="Change screen size and orientation | Microsoft PowerApps"
	description="Step-by-step instructions for changing settings such as the screen size and orientation"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="lonu"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/16/2016"
   ms.author="lonu"/>

# Change screen size and orientation in PowerApps #
Customize an app by changing its screen size and orientation.

## Prerequisites ##
1. Create an app, or open one for editing.
1. On the **File** menu, click or tap **App settings**.

## Change screen size and orientation ##
1. Under **App settings**, click or tap **Screen size + orientation**.

	![Option to change the screen size and orientation of an app](./media/set-aspect-ratio-portrait-landscape/size-orientation.png)

1. In the **Orientation** list, click or tap **Portrait** or **Landscape**.

1. (Tablet apps only) Under **Aspect ratio**, click or tap the ratio that matches the target device for this app.

	![Change the aspect ratio of a tablet app](./media/set-aspect-ratio-portrait-landscape/aspect-tablet.png)

1. Under **Lock aspect ratio**, specify either **On** or **Off**.

	If you lock the aspect ratio, the app will retain the appropriate aspect ratio for a phone. If the app is running on another kind of device, the app will display incorrectly and may show unwanted results. If you unlock the aspect ratio, the app will adjust to the aspect ratio of the device on which it's running.

1. Under **Lock orientation**, specify either **On** or **Off**.

	If you lock the app's orientation, the app will retain the orientation that you specify. If the app is running on a device for which the screen is in a different orientation, the app will display incorrectly and may show unwanted results. If you unlock the app's orientation, it will adjust to the screen orientation of the device on which it's running.

1. Select **Apply** to save your changes.

## Next step #
On the **File** menu, select **Save** to republish your app with the new settings.
