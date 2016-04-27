<properties
    pageTitle="Release notes for PowerApps | Microsoft PowerApps"
    description="Release nots"
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
    ms.date="04/13/2016"
    ms.author="gregli"/>

# Release notes for PowerApps release 2.0.410#

## PowerApps.com ##

1. 	**Use apps directly on the web!**

	Now you can find and use PowerApps on any device with a web browser.

2.  **A new home screen at PowerApps.com.**

	Features include:
	- Quick access to your apps
	- Sample apps you can check out to get started
	- Documentation to learn more
	
3.	**A fresh new look for finding and managing your apps, connections, and notifications.**

4.	**Improvements to sharing experience.**

	Users can now reshare apps and share apps with their organization.

## PowerApps Mobile ##

1. 	**PowerApps Android is now available!**

	Look for PowerApps in the [Andriod store](http://aka.ms/powerappsandroid).

2. 	**PowerApps for iOS has a new look for finding and opening apps.**
	
	Update your app or install anew from the [Apple store](http://aka.ms/powerappsios).

3. **Single sign on for services on Microsoft services on Azure Active Directory.**

	Sign in to PowerApps and you have access to your information on Office 365 without further authentication.

3. **Simplified first run experience and sign-in on mobile.**

4. **Usability improvements to mobile clients.**

	We've added hamburger navigation and an app context menu.

## PowerApps Studio for Windows ##

1. **Streamlined "New" page.**

	- An updated “new” screen with more useful options for quickly getting to what you need.
	- An improved create from data flow that includes better breadcrumbs and navigation
	- Now you can see your most recently used SharePoint sites when creating an app from SharePoint Online, for those users who don’t have their SharePoint URLs memorized by heart

3. **New guided product tour.**

	A product tour to help new users get acquainted with the most important parts of the authoring experience.

1. **Contextual help links.**

	We've made it much easier for you to find help in the product and connect with others through our communnity.

3. **New [Edit form](control-form-detail.md) and [Display form](control-form-detail.md) controls. As a result, an improved app from data.** 

	Creating an app over data just became a whole lot easier.  With these new controls, and their associated cards and functions, you can create a basic data view and edit app without needing to manually call [**Patch**](function-patch.md), [**Validate**](function-validate.md), and other low level functions.

	These controls also offer a new configuration pane, where you can turn on and off fields and pick your desired card for each field.

	Check out [Understand data forms](working-with-data-forms.md) for more details.

1. **Data source delegation of [Filter](function-filter-lookup.md) and [Sort](function-sort.md) improve performance and support large numbers of records.**

	Up until now, all Filter and Sort operations were handled on the device, requiring the time consuming and bandwidth choking fetch of all the data.  With this release, in certain situations, these operations can be delegated to the data source making your apps more responsive and able to handle a large number of records.  You can read more about it on the [Filter](function-filter-lookup.md) and [Sort](function-sort.md) pages.

	Delegation is limited to certain situations.  Apps created from data do not qualify.  See Known limitations later in this article for more details.  We will be expanding the scenarios in which delegation can be used.

	To take advantage of this new capability, the [**Gallery**](control-gallery.md) control now supports paging.  As the user reaches the end of a list of data, the control knows to fetch more from the service, seamlessly.

1. **Improvements to the [PDF viewer](control-pdf-viewer.md) control: searching and scrolling.**

	The PDF viewer control now supports full text search across the document.  

	We have also added smooth scrolling between pages.  No longer do you need to move page by page.

1. **Meta data refresh.**

	No longer do you need to delete and re-add a connection in order to update your meta data.  One click and you are done.

1. **New SharePoint site most recently used list.**

	Building a bunch of apps for the same SharePoint site?  Making that easier, we now keep track of SharePoint sites you have recently used and make those easy for you to select again.   

1. **Performance and data-handling improvements, along with many other usability and bug fixes, throughout!**

## Known limitations ##

1.  **For apps created from data, the field used for sorting and searching is not automatically configured.** 

	To configure, you will need to manually edit the **Items** formula for the gallery.  See steps 9 and 10 under [Create an app from SharePoint](app-from-sharepoint.md#create-an-app).

2. **Co-authoring is not supported.  One author at a time please.**

	It’s possible to corrupt your app or over-write others’ changes if two or more people are working on the same app at the same time.  Close the app before having someone else edit it.

3. **In the [Form control](control-form-detail.md), custom cards cannot be used to change data.**

	The stock custom card is missing the **Update** property, required for writing back changes.  To workaround this, 
	- With the form control selected, insert a card through the right hand pane based on an the field you want to work with.  
	- Unlock the card, as described in [Understanding data cards](working-with-cards.md#unlock-a-card.md).
	- Remove or rearrange controls within the card as you see fit, just as you would with the custom card.   

4. **For apps created from data, only the first 500 records of a data source can be worked with.**

	In general, PowerApps works with any size data source by delegating operations to the data source.  For operations that cannot be delegated, PowerApps will give a warning at authoring time and operate only on the first 500 records of the data source.  See the [Filter function](function-filter-lookup.md) article for more details on delegation.  

	In this release, delegation does not support **Filter** and **Sort** functions used together nor does it support the **In** operator.  These are features that are used by apps created from data, and so, these apps are limited to the first 500 records.  To partially workaround this issue, you can remove one or both of the Filter and Sort functions from the gallery **Items** property.

5. **Card gallery is deprecated.**

	Existing app that use this feature will continue to run for the time being.  However, you cannot insert a new one.  Please move to the new [**Form** control](control-form-detail.md).

5. **Apps running on Android 5.0, Nexus 6 with Webview versions v48 or v49 may crash.**

	Users can fix this problem by updating to a lower version of webview (3x) or update to Android 6.0.

6. **Camera usage on a device may be temporarily disabled if memory is low.**

	If your mobile is low on memory, rather than crashing, we will temporarily disable the camera. 

8. **It can sometimes take a moment before a newly shared app can be used.**

	In some cases, a newly shared app will not be immeidately available.  Wait a few moments and it should become available.

9. **Sharing an app for editing does not also share the Flows.**

	The Flows must be shared seperately.  They can still be run, just not edited.

   


  
	

	







