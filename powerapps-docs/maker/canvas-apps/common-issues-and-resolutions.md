---
title: Common issues and resolutions for Power Apps
description: A list of common issues and resolutions within Power Apps.
author: KumarVivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 06/07/2021
ms.subservice: troubleshoot
ms.author: kvivek
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - mduelae
---
# Common issues and resolutions for Power Apps

This article lists some common issues that you might encounter while using Power Apps. Where applicable, workarounds are provided.

> [!NOTE]
> - For help with performance problems in canvas apps, read the topics under the canvas apps [performance and optimization](execution-phases-data-flow.md) section.
> - If you're having trouble accessing or starting Power Apps, read [troubleshooting startup issues](../../troubleshooting-startup-issues.md) section for help.

## General Troubleshooting
If you're running into issues using Power Apps, try these common troubleshooting steps first.
* Check that the browser you're using is up to date. For more information, see [System requirements, limits, and configuration values for canvas apps](limits-and-config.md).
* Try with your browser's InPrivate, Incognito, or Guest mode.
* Try with a different supported browser.
* Disable all browser extensions and add-ons.
* Try with another device, if possible.

## Known Issues

   
1. **Problems with canvas app screen sizes** (April 27, 2021)

   Starting with Power Apps 3.21032, screens in some apps may be displaying unexpected dimensions or are not visible entirely. Check the affected screens' Height and Width properties and make sure they are set to an appropriate value, such as the default (`Max(App.Height, App.MinScreenHeight)` for Height, `Max(App.Width, App.MinScreenWidth)` for Width). A fix has already been deployed for screens that have a blank Height or Width. If you're still experiencing issues with the size of screens or the controls on them, the app may have been saved or auto-saved into the error state. Such apps can be restored to an earlier version via the portal, and the deployed fix will be applied the next time the app is opened for editing.
   
1. **Problems changing dimensions/orientation of SharePoint forms** (April 27, 2021)

   We are aware of issues affecting the "Screen size + orientation" settings for custom SharePoint forms. If you're having trouble with these settings, you can use the "Custom" size to work around the issue. First, reset the setting by selecting "Small" size, then toggle Orientation to Portrait and then back to Landscape. Then select "Custom" and enter a desired screen size. For reference, the preset values are Width: 270, Height: 480 for the Small Portrait size, and Width: 720, Height: 480 for Small Landscape size.
   
1. **SQL data sources no longer add a "[dbo]" prefix to the data source name** (April 27, 2021)

   This change was an intentional as the prefix did not serve any practical purpose. Existing data sources will not be affected, but any newly added SQL data sources will not include the prefix. If you need to update a large number of formulas in one of your apps, the [Power Apps Source File Pack and Unpack Utility](https://powerapps.microsoft.com/en-us/blog/source-code-files-for-canvas-apps/) can be used to do a global search-and-replace.
   
   Starting in version 3.21054, we will automatically update broken legacy name references to the new data source name after readding the data source.
   
1. **Black box covering part of embedded canvas app** (June 11, 2020)
   When using embedded canvas apps such as SharePoint forms, SharePoint web parts, and model driven forms, users many see a black box when scrolling covering part of the app. This issue happens with chromium-based browsers starting with version 83. There is not a workaround at this time. The team is actively investigating to find a fix and workaround. **A workaround in Power Apps was deployed in the week of 6/21/2020. In addition, the issue is fixed for Microsoft Edge based on Chromium with version 85.**
   
1. **Problems downloading attachments in SharePoint custom forms** (May 22, 2020)
   When using the attachment control to download an attachment, the click won't have any response when using Google Chrome version 83 or the new Microsoft Edge version 83 browser. As a workaround, change to use the default SharePoint form or use another browser. The team is actively working to fix this issue. **Fix has been deployed in the week of 6/8/2020**
   
1. **Problems downloading attachments in embedded Power Apps** (May 22, 2020)
  When using the attachment control to download an attachment, the click won't have any response when using Google Chrome version 83 or the new Microsoft Edge version 83 browser. As a workaround, use another browser. The team is actively working to fix this issue.
  
1. **Camera images when imported via Microsoft Edge are flipped** (January 20, 2020)

    When using the camera and the legacy Microsoft Edge browser, the image may be flipped. This is due to legacy Microsoft Edge browser defect. To mitigate this issue, use the new Microsoft Edge or a different browser.
    
1. **Camera images do not contain meta-data information** (January 20, 2020)

    When using the camera control, the image does not contain meta-data information. This is due to a limitation of how we take images with the camera. To mitigate this, use the [Add Picture control](controls/control-add-picture.md).

1. **Images added from iOS do not contain meta-data information** (January 20, 2020)

    When using the Add Picture control on iOS, images imported by using the camera or gallery do not contain meta-data.  


1. **Scrolling in flexible-height galleries** (Nov. 27, 2018)

    If you run into a limitation when you scroll with your finger, lift it and start to scroll again.


1. **Republishing apps** (Aug. 2, 2018)

    If you haven't updated your app in several months, republish it to sync with the most recent version of Power Apps, which includes performance improvements and other fixes.

1. <a name="out-of-memory"></a>**Browser running out of memory** (July 23, 2018)

    If you run out of memory while using Power Apps, please consider downloading a 64-bit version of Chrome, Microsoft Edge, or Internet Explorer.

1. **Launching a website from an embedded app** (May 10, 2018)

    Internet Explorer and Microsoft Edge browsers might block the launch of a URL or website that’s in protected mode or a lower security zone than the website in which the app is loaded. To resolve this issue, [change the security and privacy settings](https://support.microsoft.com/help/17479/windows-internet-explorer-11-change-security-privacy-settings) for your browser.

1. **Combo box controls in galleries** (May 3, 2018)

    When you use a **Combo box** control inside a gallery, its selections are not maintained when the user scrolls the gallery. This is not an issue if you use a **Combo box** control inside a gallery that doesn't scroll. A workaround is not currently available.

1. **Copying and pasting screens across apps** (April 4, 2018)

    Copying and pasting screens across apps is not currently supported. To work around this, add a new screen to your target app, copy the controls from the screen in your source app, and then paste them into the screen of your target app.

1. **Changing the layout of SharePoint forms** (March 7, 2018)

    While customizing a SharePoint list form in certain languages, if you try to change the layout from portrait (default) to landscape, the app may show multiple errors (yellow triangles in controls). To resolve these errors and retain the landscape layout, click **Undo**.

1. **Data Table control**

    If you copy and paste a **Data Table** control for which the **Items** property is set to a formula that contains a **Filter** function, the formula for the **Items** property on the new **Data Table** control ends up with field names that contain a **_1** suffix. This makes the field names invalid and results in no data showing up in the data table. To work around this issue, before you copy the control, confirm that the **Filter** function doesn't reference any field in the data source that has the same name as a column in the **Data Table** control. If it does, rename the column in the **Data Table** control. Alternatively, remove the **_1** suffix from the invalid field names so they match the names in the table.


1. **"Empty" gallery when opening an app**

    If you generate an app automatically from data, save the app, and then reopen it, the browse gallery might not immediately show any data. To resolve this issue, type at least one character in the search box, and then delete the text that you typed. The gallery will then show data as expected.

1. **Custom connectors and Microsoft Dataverse**

    If an app created using Power Apps build 2.0.540 or earlier relies on a database in the Dataverse and at least one custom connector in a different environment, you’ll need to deploy the connector to the same environment as the database and update the app to use the new connector. Otherwise, a dialog box will notify users that the API was not found. For more information, see the [overview of environments](/power-platform/admin/environments-overview).

1. **Column names with spaces**

    If you're using a SharePoint list or an Excel table in which a column name contains a space, Power Apps will replace it with **"\_x0020\_"**. For example, **"Column Name"** in SharePoint or Excel will appear as **"Column_x0020_Name"** in Power Apps when displayed in the data layout or used in a formula.

1. **Changing a flow in a shared app**

    If you add a flow to an app, share it, and then add a service or change a connection in the flow, you must remove the flow from the shared app, readd the flow, and reshare the app. Otherwise, users who trigger the flow will get an authentication failure.

1. **Scanning a barcode**

    For information about limitations and best practices when you use a **Barcode** control, see [Scan a barcode](./controls/control-new-barcode-scanner.md).

1. **Changing a Title field in a table**

    If you change the Title field for a table that other tables reference through one or more lookups, an error will occur when you try to save the change. To work around this issue, remove any lookups to the table for which you want to change the Title field, make the change, and then recreate the lookups. For more information about lookups, see [Build a relationship between tables](../data-platform/data-platform-entity-lookup.md).

1. **Apps that connect to on-premises SharePoint**

    If you share an app that relies on connections that aren’t automatically shared (for example, an on-premises SharePoint site), users who open the app in a browser will see a dialog box with no text when they click or tap **Sign in**. To close the dialog box, click or tap the close (X) icon in the upper-right corner. The dialog box doesn’t appear if you open the app in Power Apps Studio or Power Apps Mobile. For more information about shared connections, see [Share app resources](share-app-resources.md).

1. **When Power Apps generates an app from data, the field used for sorting and searching isn't automatically configured**.

   To configure this field, edit the **[Items](controls/properties-core.md)** formula for the gallery, as the sections for filtering and sorting in [Add a gallery](add-gallery.md) describe.

1. **For apps that are created from data, only the first 500 records of a data source can be accessed**.

     In general, Power Apps works with any size data source by delegating operations to the data source. For operations that can't be delegated, Power Apps will give a warning at authoring time and operate on only the first 500 records of the data source.  More information: See the [Filter function](functions/function-filter-lookup.md).

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

1. **Camera usage may be temporarily disabled if memory is low**.

     If your mobile device is low on memory, the camera is temporarily disabled to avoid crashing the device.

1. **Office 365 Video connector isn't supported**.

1. **Card gallery is deprecated**.

     Existing apps that use this feature will continue to run for the time being, but you can't add a card gallery. Replace card galleries with the new **[Edit form](controls/control-form-detail.md)** and **[Display form](controls/control-form-detail.md)** controls.
  
1. **Sign-in issue on certain Android mobile devices when using authenticator** (August 21, 2019)

    In certain devices and scenarios, you may experience sign-in failures when using authenticator. This is due to the OEM limiting this functionality. More information: [ADALError: BROKER_AUTHENTICATOR_NOT_RESPONDING](https://github.com/AzureAD/azure-activedirectory-library-for-android/wiki/ADALError:-BROKER_AUTHENTICATOR_NOT_RESPONDING).  


1. **Camera issue on Android mobile devices** (Jan. 1, 2019)

    If the camera control stops working on an Android device, republish your app, and reopen it on the device. The camera control was updated in response to a change in the Android operating system, and your app will benefit from the update when you republish.

1. **Multiple media controls in Power Apps Mobile** (Aug. 2, 2018)

    Power Apps Mobile runs on various types of devices, and some of them have limitations that are specific to that platform:

    - You can play videos in multiple **Video** controls at the same time on all platforms except for iPhone devices.
    - You can record audio with multiple **Microphone** controls at the same time on all platforms except for the web player.

 1. **Running an app on Windows 8.1**

    If you install [this update for Windows 8.1](/security-updates/SecurityBulletins/2016/ms16-118), you can't run apps that you open in Power Apps Studio on that operating system. However, you can still run apps that you open in [powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) or using Power Apps Mobile.
    
   
 1. **Camera control on a Windows Phone**

    An app that contains a camera control might crash if you open the app on a Windows Phone that's running build 10.0.10586.107. To avoid this problem, upgrade to the most recent build (for example, by running the [Upgrade Advisor](https://www.microsoft.com/store/p/upgrade-advisor/9nblggh0f5g4)).

  
## Power Apps for Windows

1. **Power Apps mobile app for Windows platform doesn't support Dropbox connector.** (December 15, 2020)
<br> A pop-up dialog will show the following message in this situation: <br>
  `We can’t connect to the service you need right now. Check your network connection or try again later`
<br> When this happens, consider using web player on Windows platform.

1. **AAD Conditional access with the policy "Require device to be marked as compliant" does not work in Power Apps for Windows** (July 30, 2020)
   When setting the conditional access policy "Require device to be marked as compliant" in Azure Active Directory, users will face login errors with the message "The application contains sensitive information and can only be accessed from devices or client applications that meet your enterprise management compliance policy" and won't be able to access their Power Apps. As a workaround, use your browser.

1. **`Connection.Connected` returns the wrong value during OnStart in Power Apps for Windows** (July 21, 2020)
   While offline, formula `Connection.Connected` may wrongly return **true** immediately after starting an app in the Windows app. As a workaround, delay when the logic depending on it is executed by using a **Timer** control. 
   
1. **Drawing with mouse or touch input is not smooth in Power Apps for Windows** (Sep. 24, 2018)

    The pen control only has partial support for drawing using mouse or touch input in the Windows app. Strokes might be intermittent. For smooth drawing, use a pen or run the app in a browser.
    
1. **Camera controls in Power Apps for Windows app**

   Power Apps for Windows app may crash if you open an app that uses a camera control. To avoid this problem, use the web player on the Windows platform. Also, multiple cameras aren't supported.
   
1. **Improve data source experience and Microsoft Dataverse views setting is not supported on Power Apps for Windows.** More information: [Microsoft Dataverse and the improve data source experience](use-native-cds-connector.md#how-do-i-upgrade)

## Next steps

If your issue isn't listed in this article, you can [search for more support resources](https://powerapps.microsoft.com/support), or contact [Microsoft support](https://admin.powerplatform.microsoft.com/support). More information: [Get Help + Support](/power-platform/admin/get-help-support)



### See also

[Understand canvas apps execution phases and data call flow](execution-phases-data-flow.md) <br>
[Possible sources of slow performance for canvas apps](slow-performance-sources.md) <br>
[Common canvas app performance issues and resolutions](common-performance-issue-resolutions.md) <br>
[Tips and best practices to improve canvas apps performance](performance-tips.md) <br>
[Troubleshooting startup issues for Power Apps](../../troubleshooting-startup-issues.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
