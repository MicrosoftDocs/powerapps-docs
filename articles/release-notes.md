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

# Release notes for PowerApps #

## Release 2.0.419 ##

1.  **For apps created from data, the field used for sorting and searching is not automatically configured.** 

	To configure, you will need to manually edit the **Items** formula for the gallery.  See steps 9 and 10 under under [Create an app from SharePoint](app-from-sharepoint.md#create-an-app).

2. **Co-authoring is not supported.  One author at a time please.**

	It’s possible to corrupt your app or over-write others’ changes if two or more people are working on the same app at the same time.  Close the app before having someone else edit it.

3. **In the [Form control](control-form-detail.md), custom cards cannot be used to change data.**

	The stock custom card is missing the **Update** property, required for writing back changes.  To workaround this, 
	- With the form control selected, insert a card through the right hand pane based on an the field you want to work with.  
	- Unlock the card, as described in [Understanding data cards](working-with-cards.md#unlock-a-card.md).
	- Remove or rearrange controls within the card as you see fit, just as you would with the custom card.   

4. **For apps created from data, only the first 500 records of a data source can be worked with.**

	In general, PowerApps works with any size data source by delegating operations to the data source.  For operations that cannot be delegated, PowerApps will give a warning at authoring time and operate only on the first 500 records of the data source.  See the [Filter function](function-filter.md) article for more details on delegation.  

	In this release, delegation does not support **Filter** and **Sort** functions used together nor does it support the **In** operator.  These are features that are used by apps created from data, and so, these apps are limited to the first 500 records.  To partially workaround this issue, you can remove one or both of the Filter and Sort functions from the gallery **Items** property.

5. **Card gallery is deprecated.**

	Existing app that use this feature will continue to run for the time being.  However, you cannot insert a new one.  Please move to the new [**Form** control](control-form-detail.md).

  
	

	







