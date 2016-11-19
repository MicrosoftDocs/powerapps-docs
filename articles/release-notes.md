<properties
    pageTitle="What's new in PowerApps | Microsoft PowerApps"
    description="Updates for each release of PowerApps, organized by build number"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="aftowen"
    manager="anneta"
    editor=""
    tags=""/>
<tags
    ms.service="powerapps"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="na"
    ms.date="11/18/2016"
    ms.author="anneta"/>

# What's new in PowerApps release 2.0.560-2.0.561 #
For information about known limitations, see [Common issues and resolutions](common-issues-and-resolutions.md).

1. **Support for universal links on iOS and Android devices**.

1. **Back button support on Windows Phone devices**.

	When you press the Back button, the app closes.

1. **Better experience when you delete an app**.

	When you delete an app from https://web.powerapps.com, the app is deleted when you reopen PowerApps Mobile or Dynamics 365.

1. **Support for context variables in delegable expressions**.

1. **Improved memory usage when you run an app**.

1. **Added AutoHeight property to the HTML text control**.

1. **Fixed a variety of bugs**, including in the Microphone, Ratings, Dropdown, and Camera controls.

## Release 2.0.542-2.0.545 ##

1. **Windows Phone 10**.

	A preview release of PowerApps Mobile is available for Windows Phone 10. For more information, see [Use PowerApps on a phone or a tablet](https://powerapps.microsoft.com/en-us/tutorials/run-app-client/).

1. **Bug fixes**.

## Release 2.0.540 ##
1. **Run apps in any of several languages**.

1. **Manage apps and data in specific environments**.

	For more information, see [Environments overview](environments-overview.md).

1. **Specify a description for each app that you create**.

	By adding descriptions, app creators help users find the best apps for their needs.

1. **Better support for the Back button on Android devices**.

	You're prompted to confirm whether you want to close the app.

1. **Bug fixes and other improvements in performance, diagnostics, connections in shared apps, and accessibility**.

	Apps open faster and are easier to use with a screen reader or just a keyboard. We've improved the dialog box in which you confirm or change connections when you open an app that someone shared with you. We've added a **Session details** option, which contains diagnostic information such as a session ID. We've made gallery layouts more accessible and made other improvements throughout the product.

## Release 2.0.531 ##

1. **Available in several languages in addition to English**.

1. **Select and rename controls more easily**.

	When you select a control, its name and the name or names of any parent controls appear in a "bread-crumb" element near the lower-left corner. You can open the **Rename** text box by double-clicking the name of a control at the top of the right-hand pane or by double-clicking the name of a screen in the left navigation bar.

1. **Find options on the toolbar more easily**.

1. **Show the Advanced view of control properties more easily**.

	 Review and update property values of the selected control in the **Advanced** tab of the right-hand pane.

1. **Refresh data in generated apps more easily**.

	When you automatically generate an app, the default browse screen contains a refresh button. Users can click or tap the button to display the most recent changes to the data from its source without closing the app.

1. **Show two display fields in lookup controls**.

1. **Update multiple records at once by using the Patch function**.

	Create or update more than one record at a time by specifying a table of base records and a table of change records as arguments for the **[Patch](function-patch.md)** function.

1. **Perform calculations and actions on a set of records by using the ForAll function**.

	The **[ForAll](function-forall.md)** function evaluates a formula for all records of a table. The formula can calculate a value and/or perform one or more actions, such as modifying data or working with a connection.

1. **Calculate exponential values by using the Power function**.

	The **[Power](function-numericals.md)** function returns a number raised to a power. This function is equivalent to the [^ operator](operators.md).

1. **Better sorting and filtering across sessions and devices**.

	If you sort or filter your list of apps on a mobile device, that setting is retained even if you close PowerApps. If you sort your list of apps by when you opened them most recently, the sort order is accurate even if you opened an app on a different device.

1. **Improved mechanism for providing feedback**.

	Instead of clicking or tapping the smile icon near the upper-right corner, create a ticket by clicking or tapping **Contact** on [our support page](https://powerapps.microsoft.com/support/) and then providing information about your question. You can also check the status of tickets that you've filed.

## Release 2.0.510-2.0.512 ##
Because of administrative details, different platforms show different build numbers, but 2.0.510, 2.0.511, and 2.0.512 were released at effectively the same time.

1. **Open apps in iOS 10**.

1. **Mark favorite apps on iOS and Android devices**.

	You can mark an app as a favorite and show only your favorite apps in the list of apps that you can run.

1. **Swipe down to refresh the list of apps on iOS and Android devices**.

1.	**Delay property for text-input controls**.

	If you set the **[OnChange](https://powerapps.microsoft.com/en-us/tutorials/properties-core/)** property for a **[Text input](control-text-input.md)** control to an action, that action occurs, by default, every time that the user types a character in the control. For example, a user might type seven letters in a search box, and the results will update every time the user adds a letter, which uses network bandwidth unnecessarily when a data source is searched. If you set the **DelayOutput** property for that control to **true**, the action doesn’t occur until the user types one or more characters and then stops typing in that control for a period of time.

1.	**Mathematical functions added**.

	- Calculate sine, cosine, tangent, and other trigonometric values.
	- Easily access the value of &pi;.
	- Convert between units of angle.
	- Calculate natural exponentiations and logarithms.

	For more information, see [Trigonometric functions](function-trig.md) and [Numerical functions](function-numericals.md).

## Release 2.0.500 ##
1. **Barcode scanner for UPC, Codabar, and other types of codes**.

	For step-by-step instructions and information about best practices and limitations, see [Scan a barcode](scan-barcode.md).

1. **App templates that showcase the Common Data Model**.

	Use a template to quickly create a phone app to manage cases or a tablet app to register contacts for a contest. These templates are based on standard entities in the Common Data Model.

1. **Bug fixes and performance improvements**.

## Release 2.0.490 ##
1. **Use the entities in the Microsoft Common Data Model to build apps**.

	Store organizational data in standard or custom entities, build and share apps based on those entities, and open the entities in Excel to easily view and edit the data. For more information, see [Understand entities](data-platform-intro.md).

1. **Connect to data in an on-premises SharePoint site**.

	Show and manage data in an on-premises SharePoint site by using a data gateway. For more information, see [Connect to SharePoint](connection-sharepoint-online.md).

1. **Get push notifications on your Android device when apps are shared with you**.

1. **Run apps using PowerApps Mobile on Android N**.

## Release 2.0.480 ##

1. **Create and modify an app in a browser**.

	You can create and modify apps by opening either PowerApps Studio or a browser such as Edge, Chrome, or Internet Explorer 11. For more information, see [Create an app in a browser](create-app-browser.md).

1. **Create an app from within a modern list in SharePoint**.

	For more information, see this [blog post](http://go.microsoft.com/fwlink/?LinkID=808680).

1. **Add or duplicate a screen**

	In the left navigation bar, you can click or tap the ellipsis for a thumbnail and then click or tap **New Screen** to add a screen or **Duplicate Screen** to copy the current screen. In either case, the new screen appears just below the current screen instead of at the bottom of the navigation bar.

## Release 2.0.471 ##
1. **Dates and times when you create an app automatically**.

	If you create an app automatically from a data source that includes date information, the app will show that information on **EditScreen1** in a **DatePicker** control by default. If the source also includes time information, it will appear in **Drop down** controls.

1. **New sample apps and templates**.

	You can open a sample app that demonstrates a scenario such as showcasing products, surveying employee engagement, checking out assets, and helping a new employee choose a health plan.

1. **Pass parameters while running an app in the browser using a query string**.

1. **Deprecated data sources from Project Siena**.

	If you created or updated an app in the beta 4 release of Project Siena to include data from any of these sources, that data will no longer appear if you run or edit the app in PowerApps:

	- on-premises SharePoint sites
	- Azure Mobile Services
	- REST services that weren't created by using a WADL file
	- RSS

	If you open the app for editing, an error icon will notify you which control or controls have properties that refer to a deprecated data source.

## Release 2.0.460 ##
1. **On-premises data**.

	Show and manage data in an on-premises SQL Server database by using an [on-premises data gateway](gateway-management.md).

1. **PowerApps on Firefox**.

	You can run apps in the most recent version of the Mozilla Firefox browser.

1. **SharePoint Update control**.

	This control has been deprecated in favor of the **[Edit Form](add-form.md)** control. An app that contains the **SharePoint Update** control will still open, but the control itself will no longer appear.

## Release 2.0.450 ##
1. **Add data while customizing a form**.

	With a form selected, tap the data source for the form (or **No data source selected**) in the right-hand pane, and then tap **Add a data source**.

1.	**App from data now fully delegated for SQL Azure and Salesforce connections**.

	When you create an app from data for a SQL Azure or Salesforce connection, the resulting app now delegates all operations to the service. It's now possible to work with large data sets with these generated apps.

	Instead of generating formulas based on **Filter** and **Sort** functions, we now generate formulas based on **Search** and **SortByColumns** functions.  These new functions are easier to delegate to a data service because they don't depend on an arbitrary formula.

1.	**New Search function**.

	Acting as a specialized **Filter** function, the **Search** function takes a single string to look for and a list of text columns to search within. This function also automatically returns all records if no search term is present, suitable for direct use with a search **Text input** control. For more information, see the **Search** function documentation, or take a look at the formulas generated when you create an app from data.

1.	**In operator now supports delegation**.

	Feel free to use this operator in **Filter** functions to accomplish the same effect as the **Search** function.

1. **Show PDF files that are protected by a password**.

	If you configure a **PDF Viewer** control to show a file that requires a password, each user must provide the password to view the file. To remove the password requirement, set the **Password** property of that control to the password for that file.

1. **Coordinated Universal Time in the DatePicker control**.

	By default, the **DatePicker** control interprets all date values in the local time zone. If your input is given as midnight in the Coordinated Universal Time (UTC), it would show a date one day off in certain time zones. For example, a **DatePicker** control shows Dec. 31, 2016, if you set its **DefaultDate** property to “2017-01-01T00:00:00Z” and you’re in the Pacific time zone (UTC-0800). To ensure that the control shows those values correctly, change its **DateTimeZone** property from **Local** to **UTC**.

## Release 2.0.440 ##

1. **Options pane**.

	We've consolidated the **Options** and **Quick Tools** panes, and the **Options** pane remains open all the time.

1. **Edit lookup control**.

	If you add and configure an **Edit Lookup** control in an **Edit form** control, users can add and update items in a SharePoint list that contains these types of columns:

	- Lookup
	- Person or Group
	- Managed Metadata

## Release 2.0.430 ##

1. **Update required for PowerApps Studio and PowerApps Mobile**.

	Due to an internal change, you must install this update to continue to create and edit apps in PowerApps Studio and run apps in PowerApps Mobile.

	For Windows 8 and Windows 8.1:

	1.	Open the app for the Windows Store.
	1.	Open the settings for that app.<br>For example, press the Windows key and the “c” key simultaneously, and then select **Settings**.
	1.	Select  **App updates**, and then select **Check for updates**.
	1.	In the screen that appears, select **Install** for PowerApps.

1. **Enhanced delegation for large data sets.**

	- **SortByColumns** now supports delegation.
	- **Sort**, **SortByColumns**, and **Filter** can now be composed together.
	- More support for delegation is on the way.

1. **Updates property added to the Edit form control.**

	The **[Edit form](controls/control-form-detail.md)** control now has an **[Updates](controls/control-form-detail.md)** property to access all the **[Update](controls/control-card.md)** properties of the cards within the form.

	You can use this property to pass form data to a REST API.

1. **Bug fixes for Video control.**

	Now works with YouTube.

1. **Single sign-on support for Microsoft services.**

	Single sign-on feature will automatically sign PowerApps users into their first party services that use Azure Active Directory authentication, such as SharePoint, Office 365, and Dynamics CRM.

1. **Added Edit lookup card.**

	As soon as you install this PowerApps update, **[Display form](controls/control-form-detail.md)** and **[Edit form](controls/control-form-detail.md)** controls will show lookup fields to other tables, but this data will be read-only. As soon as other changes occur in the SharePoint connector, you’ll be able to update these fields for data in SharePoint lists. (You won’t need to update PowerApps again to take advantage of this capability).

1. **Minimum/maximum values for numeric cards.**

	Numeric cards, such as those for ratings and percentages, reflect minimum and maximum values that you set (or that are set in the metadata for the data source).

1. **Default value for the DatePicker control.**

	You can configure a DatePicker control with a blank value as its default.

1. **Improvements to Display Form and Edit Form controls.**

	Form controls now show both a display name and the name of the field if they differ, and you can change the display name of a lookup control.

1. **On powerapps.com, show only those apps you own or were shared with you.**

1. **Bug fixes and performance improvements throughout the product.**

## Release 2.0.410 ##

### PowerApps.com ###
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

### PowerApps Mobile ###
1. 	**PowerApps is now available for Android!**

	Look for PowerApps in the [Android store](http://aka.ms/powerappsandroid).

2. 	**PowerApps has a new look for finding and opening apps on devices that run iOS.**

	Update your app or install anew from the [Apple store](http://aka.ms/powerappsios).

3. **Simplified sign-in and first-run experiences.**

4. **Usability improvements.**

	We've added hamburger navigation and an app context menu.

### PowerApps Studio ###

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

### Connections ###

This release supports these connections, among [many others](connections-list.md):

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
