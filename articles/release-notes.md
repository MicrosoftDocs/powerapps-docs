<properties
    pageTitle="Release notes for PowerApps | Microsoft PowerApps"
    description="Release notes"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="gregli-msft"
    manager="erikre"
    editor=""
    tags=""/>
<tags
    ms.service="powerapps"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="na"
    ms.date="04/27/2016"
    ms.author="gregli"/>

# Release notes for PowerApps release 2.0.410#

## PowerApps.com ##
1. 	**Use apps directly on the web!**

	You can find and use PowerApps on any device that has a web browser.

2.  **A new home screen at PowerApps.com.**

	Features include:
	- Quick access to your apps
	- Sample apps that you can check out to get started
	- Documentation to learn more

3.	**A fresh new look for finding and managing your apps, connections, and notifications.**

4.	**Improvements to the sharing experience.**

	Users can now reshare apps and share apps with their organization.

## PowerApps Mobile ##
1. 	**PowerApps is now available for Android!**

	Look for PowerApps in the [Android store](http://aka.ms/powerappsandroid).

2. 	**PowerApps has a new look for finding and opening apps on devices that run iOS.**

	Update your app or install anew from the [Apple store](http://aka.ms/powerappsios).

3. **Simplified sign-in and first-run experiences.**

4. **Usability improvements.**

	We've added hamburger navigation and an app context menu.

## PowerApps Studio ##

1. **Streamlined page for starting to create an app.**

	- More useful options for quickly getting to what you need.
	- An improved flow, including better breadcrumbs and navigation, when you create an app from data.
	- Now you can see your most recently used SharePoint sites when you create an app from SharePoint Online, for those users who don’t memorize their SharePoint URLs.

3. **New guided product tour.**

	A quick tour of the most important parts of the authoring experience to help new users get acquainted.

1. **Contextual help links.**

	We've made it much easier for you to find help in the product and connect with others through our community.

3. **New [Edit form](controls/control-form-detail.md) and [Display form](controls/control-form-detail.md) controls. As a result, better apps generated from data.**

	Creating an app over data just got a whole lot easier.  With these controls and their associated cards and functions, you can create a basic app to view and edit data without needing to manually call **[Patch](functions/function-patch.md)**, **[Validate](functions/function-validate.md)**, and other low-level functions.

	These controls also offer a new configuration pane, where you can turn on and off fields and change the card for each field.

	Check out [Understand data forms](working-with-forms.md) for more details.

1. **Data-source delegation of [Filter](functions/function-filter-lookup.md) and [Sort](functions/function-sort.md) improves performance and supports large numbers of records.**

	Until now, all Filter and Sort operations were handled on the device, which required the time-consuming and bandwidth-choking fetch of all the data.  With this release, in certain situations, these operations can be delegated to the data source, which makes your apps more responsive and able to handle a large number of records.  You can read more about it on the [Filter](functions/function-filter-lookup.md) and [Sort](functions/function-sort.md) pages.

	Delegation is limited to certain situations. Apps created from data don't qualify.  See [Known limitations](#known-limitations) later in this article for more details.  We will expand the scenarios in which delegation can be used.

	To take advantage of this new capability, the **[Gallery](controls/control-gallery.md)** control now supports paging.  As the user reaches the end of a list of data, the control fetches more from the data source, seamlessly.

1. **Search and scroll in the [PDF viewer](controls/control-pdf-viewer.md) control.**

	The PDF viewer control now supports full-text search across the document, and we've added smooth scrolling between pages. No longer do you need to move page by page.

1. **More connectors.**

	We continue to add connectors. [Check out the list](connections-list.md) for the latest.

1. **Metadata refresh.**

	Update your metadata with a single click or tap (instead of deleting a connection and adding it again).

1. **A list of your most recently used SharePoint sites.**

	Building a bunch of apps for the same SharePoint site? To make that easier, we track SharePoint sites that you've recently used so that you can easily select them again.   

1. **Performance and data-handling improvements, along with many other usability and bug fixes throughout!**

## Connections ##

With this release, we [support a wide assortment of connections](connections-list.md) including:

- SharePoint
- Office 365
- Dynamics CRM
- SQL
- OneDrive for Business
- Dropbox
- Google Drive
- Slack
- Twilio
- Yammer
- Twitter
- and many more

## Known limitations ##
1. **On Apple iPhone 6 Plus devices, an incorrect icon appears for PowerApps.**

	An update has been submitted and should appear soon.

1.  **For apps created from data, the field used for sorting and searching isn't automatically configured.**

	To configure this field, edit the **[Items](properties/properties-core.md)** formula for the gallery, as the sections for filtering and sorting in [Add a gallery](add-gallery.md) describe.

2. **Co-authoring isn't supported. One author at a time, please.**

	You can corrupt an app or over-write others’ changes if more than one person modifies the same app at the same time. Close the app before someone else edits it.

3. **In the [Form control](controls/control-form-detail.md), you can't change data by using a custom card.**

	The stock custom card is missing the **[Update](controls/control-card.md)** property, which is required to write back changes. To work around this:
	- Select the form control, and insert a card by using the right-hand pane based on the field that you want the card to show.  
	- Unlock the card, as described in [Understanding data cards](working-with-cards.md#unlock-a-card).
	- Remove or rearrange controls within the card as you see fit, just as you would with the custom card.   

4. **For apps that are created from data, only the first 500 records of a data source can be accessed.**

	In general, PowerApps works with any size data source by delegating operations to the data source. For operations that can't be delegated, PowerApps will give a warning at authoring time and operate on only the first 500 records of the data source.  See the [Filter function](functions/function-filter-lookup.md) article for more details about delegation.  

	In this release, delegation doesn't support **[Filter](functions/function-filter-lookup.md)** and **[Sort](functions/function-sort.md)** functions used together, nor does it support the **[In](functions/operators.md#in-and-exactin-operators)** operator.  These features are used by apps that are created from data, so these apps are limited to the first 500 records. To partially work around this issue, you can remove one or both of the Filter and Sort functions from the gallery's **[Items](properties/properties-core.md)** property.

5. **Card gallery is deprecated.**

	Existing apps that use this feature will continue to run for the time being, but you can't add a card gallery. Please replace card galleries with the new **[Edit form](controls/control-form-detail.md)** and **[Display form](controls/control-form-detail.md)** controls.

5. **An app that's running on Android 5.0, Nexus 6 with Webview versions v48 or v49 may crash.**

	Users can fix this problem by updating to a lower version of Webview (3x) or update to Android 6.0.

6. **Camera usage may be temporarily disabled if memory is low.**

	If your mobile device is low on memory, the camera is temporarily disabled to avoid crashing the device.

8. **It can sometimes take a moment before a newly shared app can be used.**

	In some cases, a newly shared app won't be immediately available.  Wait a few moments, and it should become available.

9. **Sharing an app for editing doesn't also share the flows.**

	You must share the flows separately so that others can edit them, not just run them.
