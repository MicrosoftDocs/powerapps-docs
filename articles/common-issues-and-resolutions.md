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
   ms.date="06/10/2016"
   ms.author="anneta"/>

# Common issues and resolutions #

## Recently added/changed ##
1. **Connections to SQL Server**

	You can connect to an on-premises SQL Server database if you upgrade to build 2.0.460. If you don't upgrade, you can connect to SQL Azure, but you'll be prompted to specify an authentication type. The connection will succeed regardless of whether you specify anything in that field.

1. **Windows 10 Insider builds**

	You can't open PowerApps on devices that are running Windows Insider builds 14361 through 14375, inclusive. The issue has been resolved, and the fix was first released in build 14376.

## Older ##
1.  **When PowerApps generates an app from data, the field used for sorting and searching isn't automatically configured**.

	To configure this field, edit the **[Items](controls/properties-core.md)** formula for the gallery, as the sections for filtering and sorting in [Add a gallery](add-gallery.md) describe.

1. **For apps that are created from data, only the first 500 records of a data source can be accessed**.

	In general, PowerApps works with any size data source by delegating operations to the data source. For operations that can't be delegated, PowerApps will give a warning at authoring time and operate on only the first 500 records of the data source.  See the [Filter function](functions/function-filter-lookup.md) article for more details about delegation.  

1. **Excel data must be formatted as a table**.

	If **Data type unsupported** or **Not formatted as a table** appears when you try to use an Excel connection in your app, [format the data as a table](https://support.office.com/en-us/article/Create-an-Excel-table-in-a-worksheet-E81AA349-B006-4F8A-9806-5AF9DF0AC664).

1. **SharePoint lists are supported but not libraries, some types of list columns, or columns that support multiple values or selections**.

	For more information, see [SharePoint Online](connection-sharepoint-online.md#known-issues).

1. **Co-authoring isn't supported. One author at a time, please** (as of release 2.0.410).

	You can corrupt an app or over-write others’ changes if more than one person modifies the same app at the same time. Close the app before someone else edits it.

1. **It can sometimes take a moment before a newly shared app can be used** (as of release 2.0.410).

	In some cases, a newly shared app won't be immediately available. Wait a few moments, and it should become available.

1. **In the [Form control](controls/control-form-detail.md), you can't change data by using a custom card** (as of release 2.0.410).

	The stock custom card is missing the **[Update](controls/control-card.md)** property, which is required to write back changes. To work around this:
	- Select the form control, and insert a card by using the right-hand pane based on the field that you want the card to show.  
	- Unlock the card, as described in [Understanding data cards](working-with-cards.md#unlock-a-card).
	- Remove or rearrange controls within the card as you see fit, just as you would with the custom card.   

1. **Card gallery is deprecated** (as of release 2.0.410).

	Existing apps that use this feature will continue to run for the time being, but you can't add a card gallery. Please replace card galleries with the new **[Edit form](controls/control-form-detail.md)** and **[Display form](controls/control-form-detail.md)** controls.

1. **Office 365 Video connector isn't supported**.

1. **An app that's running on Android 5.0, Nexus 6 with Webview versions v48 or v49 may crash** (as of release 2.0.410).

	Users can fix this problem by updating to a lower version of Webview (3x) or update to Android 6.0.

1. **Camera usage may be temporarily disabled if memory is low** (as of release 2.0.410).

	If your mobile device is low on memory, the camera is temporarily disabled to avoid crashing the device.
