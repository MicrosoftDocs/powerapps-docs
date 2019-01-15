---
title: Common issues and resolutions for PowerApps | Microsoft Docs
description: A list of common issues and resolutions within PowerApps.
author: AFTOwen
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 11/09/2018
ms.author: anneta
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Common issues and resolutions for PowerApps

This article lists some common issues that you might encounter while using PowerApps. Where applicable, workarounds are provided.

## Added after February 2018

1. **Camera issue on Android mobile devices** (Jan. 1, 2019)

    If the camera control stops working on an Android device, republish your app, and reopen it on the device. The camera control was updated in response to a change in the Android operating system, and your app will benefit from the update when you republish.

1. **Scrolling in flexible-height galleries** (Nov. 27, 2018)

    If you run into a limitation when you scroll with your finger, lift it and start to scroll again.

1. **Drawing with mouse or touch input is not smooth in PowerApps for Windows** (Sep. 24, 2018)

    The pen control only has partial support for drawing using mouse or touch input in the Windows app. Strokes might be intermittent. For smooth drawing, use a pen or run the app in a browser.

1. **Multiple media controls in PowerApps Mobile** (Aug. 2, 2018)

    PowerApps Mobile runs on various types of devices, and some of them have limitations that are specific to that platform:

    - You can play videos in multiple **Video** controls at the same time on all platforms except for iPhone devices.
    - You can record audio with multiple **Microphone** controls at the same time on all platforms except for the web player.

1. **Republishing apps** (Aug. 2, 2018)

    If you haven't updated your app in several months, republish it to sync with the most recent version of PowerApps, which includes performance improvements and other fixes.

1. <a name="out-of-memory"></a>**Browser running out of memory** (July 23, 2018)

    If you run out of memory while using PowerApps, please consider downloading a 64-bit version of Chrome, Microsoft Edge, or Internet Explorer.

1. **Launching a website from an embedded app** (May 10, 2018)

    Internet Explorer and Microsoft Edge browsers might block the launch of a URL or website that’s in protected mode or a lower security zone than the website in which the app is loaded. To resolve this issue, [change the security and privacy settings](https://support.microsoft.com/en-us/help/17479/windows-internet-explorer-11-change-security-privacy-settings) for your browser.

1. **Combo box controls in galleries** (May 3, 2018)

    When you use a **Combo box** control inside a gallery, its selections are not maintained when the user scrolls the gallery. This is not an issue if you use a **Combo box** control inside a gallery that doesn't scroll. A workaround is not currently available.

1. **Using a custom image as an app icon** (April 11, 2018)

    In PowerApps Studio for Windows version 3.18043, you cannot upload a custom image to use as an app icon. To work around this issue, use [PowerApps Studio for web](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to upload a custom image. Alternatively, you can use one of the icons included with PowerApps Studio for Windows and customize the background color.

1. **Copying and pasting screens across apps** (April 4, 2018)

    Copying and pasting screens across apps is not currently supported. To work around this, add a new screen to your target app, copy the controls from the screen in your source app, and then paste them into the screen of your target app.

1. **Changing the layout of SharePoint forms** (March 7, 2018)

    While customizing a SharePoint list form in certain languages, if you try to change the layout from portrait (default) to landscape, the app may show multiple errors (yellow triangles in controls). To resolve these errors and retain the landscape layout, click **Undo**.

## Added in or before February 2018

1. **Data Table control**

    If you copy and paste a **Data Table** control for which the **Items** property is set to a formula that contains a **Filter** function, the formula for the **Items** property on the new **Data Table** control ends up with field names that contain a **_1** suffix. This makes the field names invalid and results in no data showing up in the data table. To work around this issue, before you copy the control, confirm that the **Filter** function doesn't reference any field in the data source that has the same name as a column in the **Data Table** control. If it does, rename the column in the **Data Table** control. Alternatively, remove the **_1** suffix from the invalid field names so they match the names in the entity.

1. **Camera controls in PowerApps Studio for Windows**

    PowerApps Studio for Windows may crash if you add a camera control or open an app that uses a camera control. To avoid this problem, use [PowerApps Studio for web](create-app-browser.md) when adding or using a camera control.

1. **Release 2.0.700 on Android devices**

    If you install release 2.0.700 on an Android device and then can't open apps (or an app stops responding), uninstall PowerApps, restart the device, and then reinstall PowerApps.

1. **"Empty" gallery when opening an app**

    If you generate an app automatically from data, save the app, and then reopen it, the browse gallery might not immediately show any data. To resolve this issue, type at least one character in the search box, and then delete the text that you typed. The gallery will then show data as expected.

1. **Upgrading PowerApps on Windows 8.1**

    If you install PowerApps on a computer that’s running Windows 8 or Windows 8.1, keep the Windows Store app open and active, use the Settings charm to check for updates, and then install them.

1. **Custom connectors and the Common Data Service**

    If an app created using PowerApps build 2.0.540 or earlier relies on a database in the Common Data Service and at least one custom connector in a different environment, you’ll need to deploy the connector to the same environment as the database and update the app to use the new connector. Otherwise, a dialog box will notify users that the API was not found. For more information, see the [overview of environments](../../administrator/environments-overview.md).

1. **Running an app on Windows 8.1**

    If you install [this update for Windows 8.1](https://technet.microsoft.com/library/security/ms16-118), you can't run apps that you open in PowerApps Studio on that operating system. However, you can still run apps that you open in [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) or using PowerApps Mobile.

1. **Column names with spaces**

    If you're using a SharePoint list or an Excel table in which a column name contains a space, PowerApps will replace it with **"\_x0020\_"**. For example, **"Column Name"** in SharePoint or Excel will appear as **"Column_x0020_Name"** in PowerApps when displayed in the data layout or used in a formula.

1. **Changing a flow in a shared app**

    If you add a flow to an app, share it, and then add a service or change a connection in the flow, you must remove the flow from the shared app, re-add the flow, and reshare the app. Otherwise, users who trigger the flow will get an authentication failure.

1. **Using a localized version**.

    If you're running release 2.0.531 on Windows 8.1, you can't type in a **Text input** control if the device is set to a language that requires an IME window.

1. **Camera control on a Windows Phone**

    An app that contains a camera control might crash if you open the app on a Windows Phone that's running build 10.0.10586.107. To avoid this problem, upgrade to the most recent build (for example, by running the [Upgrade Advisor](https://www.microsoft.com/store/p/upgrade-advisor/9nblggh0f5g4)).

1. **Opening an app from a template**.

    If you're running release 2.0.500 or older, an error message appears when you try to create an app from a template. You must upgrade to be able to use this feature.

    If you're running release 2.0.510 or later, an warning might appear when you try to create an app from a template. However, you can close the message and create the app.

1. **Scanning a barcode**

    For information about limitations and best practices when you use a **Barcode** control, see [Scan a barcode](scan-barcode.md).

1. **Creating and modifying apps in a browser**

    You can do many, but not all, of the same things in PowerApps Studio for web as you can in PowerApps Studio for Windows. For more information, see [Create an app in a browser](create-app-browser.md).

1. **Changing a Title field in an entity**

    If you change the Title field for an entity that other entities reference through one or more lookups, an error will occur when you try to save the change. To work around this issue, remove any lookups to the entity for which you want to change the Title field, make the change, and then recreate the lookups. For more information about lookups, see [Build a relationship between entities](../common-data-service/data-platform-entity-lookup.md).

1. **Apps that connect to on-premises SharePoint**

    If you share an app that relies on connections that aren’t automatically shared (for example, an on-premises SharePoint site), users who open the app in a browser will see a dialog box with no text when they click or tap **Sign in**. To close the dialog box, click or tap the close (X) icon in the upper-right corner. The dialog box doesn’t appear if you open the app in PowerApps Studio or PowerApps Mobile. For more information about shared connections, see [Share app resources](share-app-resources.md).

1. **When PowerApps generates an app from data, the field used for sorting and searching isn't automatically configured**.

   To configure this field, edit the **[Items](controls/properties-core.md)** formula for the gallery, as the sections for filtering and sorting in [Add a gallery](add-gallery.md) describe.

1. **For apps that are created from data, only the first 500 records of a data source can be accessed**.

     In general, PowerApps works with any size data source by delegating operations to the data source. For operations that can't be delegated, PowerApps will give a warning at authoring time and operate on only the first 500 records of the data source.  See the [Filter function](functions/function-filter-lookup.md) article for more details about delegation.

1. **Excel data must be formatted as a table**.

     For information about limitations when you use Excel as a data source, see [Cloud-storage connections](connections/cloud-storage-blob-connections.md#known-limitations).

1. **SharePoint custom lists are supported but not libraries, some types of list columns, or columns that support multiple values or selections**.

     For more information, see [SharePoint Online](connections/connection-sharepoint-online.md#known-issues).

1. **Co-authoring isn't supported. One author at a time, please**.

     You can corrupt an app or over-write others’ changes if more than one person modifies the same app at the same time. Close the app before someone else edits it.

1. **It can sometimes take a moment before a newly shared app can be used**.

     In some cases, a newly shared app won't be immediately available. Wait a few moments, and it should become available.

1. **In the [Form control](controls/control-form-detail.md), you can't change data by using a custom card**.

     The stock custom card is missing the **[Update](controls/control-card.md)** property, which is required to write back changes. To work around this:

    * Select the form control, and insert a card by using the right-hand pane based on the field that you want the card to show.  
    * Unlock the card, as described in [Understanding data cards](working-with-cards.md#unlock-a-card).
    * Remove or rearrange controls within the card as you see fit, just as you would with the custom card.

1. **An app that's running on Android 5.0, Nexus 6 with Webview versions v48 or v49 may crash**.

     Users can fix this problem by updating to a lower version of Webview (3x) or update to Android 6.0.

1. **Camera usage may be temporarily disabled if memory is low**.

     If your mobile device is low on memory, the camera is temporarily disabled to avoid crashing the device.

1. **Office 365 Video connector isn't supported**.

1. **Card gallery is deprecated**.

     Existing apps that use this feature will continue to run for the time being, but you can't add a card gallery. Please replace card galleries with the new **[Edit form](controls/control-form-detail.md)** and **[Display form](controls/control-form-detail.md)** controls.
