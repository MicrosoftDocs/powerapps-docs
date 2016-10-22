<properties
	pageTitle="Common issues and resolutions | Microsoft PowerApps"
	description="Read about PowerApps issues and resolutions"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="AFTOwen"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/22/2016"
   ms.author="anneta"/>

# Common issues and resolutions #

## Recently added/changed ##
1. **Camera control on a Windows Phone**

	An app that contains a camera control might crash if you open the app on a Windows Phone that's running build 10.0.10586.107. To avoid this problem, upgrade to the most recent build (for example, by running the [Upgrade Advisor](https://www.microsoft.com/en-us/store/p/upgrade-advisor/9nblggh0f5g4)). 

1. **Running an app on Windows 8.1**

	If you install [this update for Windows 8.1](https://technet.microsoft.com/library/security/ms16-118), you can't run apps that you open in PowerApps Studio on that operating system. However, you can still run apps that you open in  [powerapps.com](https://web.powerapps.com) or using PowerApps Mobile.

1. **Changing a flow in a shared app**

	If you add a flow to an app, share it, and then add a service or change a connection in the flow, you must remove the flow from the shared app, re-add the flow, and reshare the app. Otherwise, users who trigger the flow will get an authentication failure.

1. **Using a localized version**.

	If you're running release 2.0.531 on Windows 8.1, you can't type in a **Text input** control if the device is set to a language that requires an IME window.

## Older ##
1. **Opening an app from a template**.

	If you're running release 2.0.500 or older, an error message appears when you try to create an app from a template. You must upgrade to be able to use this feature.

	If you're running release 2.0.510 or later, an warning might appear when you try to create an app from a template. However, you can close the message and create the app.

1. **Scanning a barcode**

	For information about limitations and best practices when you use a **Barcode** control, see [Scan a barcode](scan-barcode.md).

1. **Creating and modifying apps in a browser**

	You can do many of the same things in PowerApps Studio for web as you can in PowerApps Studio for Windows. However, you can't, for example, create an app from a template. For more information, see [Create an app in a browser](create-app-browser.md).

1. **Changing a Title field in an entity**

	If you change the Title field for an entity that other entities reference through one or more lookups, an error will occur when you try to save the change. To work around this issue, remove any lookups to the entity for which you want to change the Title field, make the change, and then recreate the lookups. For more information about lookups, see [Build a relationship between entities](data-platform-entity-lookup.md).

1. **Apps that connect to on-premises SharePoint**

	If you share an app that relies on connections that aren’t automatically shared (for example, an on-premises SharePoint site), users who open the app in a browser will see a dialog box with no text when they click or tap **Sign in**. To close the dialog box, click or tap the close (X) icon in the upper-right corner. The dialog box doesn’t appear if you open the app in PowerApps Studio or PowerApps Mobile. For more information about shared connections, see [Share app resources](share-app-resources.md).

1.  **When PowerApps generates an app from data, the field used for sorting and searching isn't automatically configured**.

	To configure this field, edit the **[Items](controls/properties-core.md)** formula for the gallery, as the sections for filtering and sorting in [Add a gallery](add-gallery.md) describe.

1. **For apps that are created from data, only the first 500 records of a data source can be accessed**.

	In general, PowerApps works with any size data source by delegating operations to the data source. For operations that can't be delegated, PowerApps will give a warning at authoring time and operate on only the first 500 records of the data source.  See the [Filter function](functions/function-filter-lookup.md) article for more details about delegation.  

1. **Excel data must be formatted as a table**.

	For information about limitations when you use Excel as a data source, see [Cloud-storage connections](cloud-storage-blob-connections.md#known-limitations).

1. **SharePoint custom lists are supported but not libraries, some types of list columns, or columns that support multiple values or selections**.

	For more information, see [SharePoint Online](connection-sharepoint-online.md#known-issues).

1. **Co-authoring isn't supported. One author at a time, please**.

	You can corrupt an app or over-write others’ changes if more than one person modifies the same app at the same time. Close the app before someone else edits it.

1. **It can sometimes take a moment before a newly shared app can be used**.

	In some cases, a newly shared app won't be immediately available. Wait a few moments, and it should become available.

1. **In the [Form control](controls/control-form-detail.md), you can't change data by using a custom card**.

	The stock custom card is missing the **[Update](controls/control-card.md)** property, which is required to write back changes. To work around this:
	- Select the form control, and insert a card by using the right-hand pane based on the field that you want the card to show.  
	- Unlock the card, as described in [Understanding data cards](working-with-cards.md#unlock-a-card).
	- Remove or rearrange controls within the card as you see fit, just as you would with the custom card.   

1. **An app that's running on Android 5.0, Nexus 6 with Webview versions v48 or v49 may crash**.

	Users can fix this problem by updating to a lower version of Webview (3x) or update to Android 6.0.

1. **Camera usage may be temporarily disabled if memory is low**.

	If your mobile device is low on memory, the camera is temporarily disabled to avoid crashing the device.

1. **Office 365 Video connector isn't supported**.

1. **Card gallery is deprecated**.

	Existing apps that use this feature will continue to run for the time being, but you can't add a card gallery. Please replace card galleries with the new **[Edit form](controls/control-form-detail.md)** and **[Display form](controls/control-form-detail.md)** controls.
