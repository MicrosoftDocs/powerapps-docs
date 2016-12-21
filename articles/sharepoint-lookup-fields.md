<properties
	pageTitle="Create relationships between SharePoint lists via lookup field | Microsoft PowerApps"
	description="Create relationships between SharePoint lists by using lookup fields."
	services="powerapps"
	documentationCenter="na"
	authors="RickSaling"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="12/21/2016"
   ms.author="ricksal"/>

# Linking SharePoint lists with lookup fields

Data in one SharePoint list often relates to data in another list. For example, you might have a **Customers** list and an **Orders** list, and the **Orders** list might have a lookup relation to the **Customers** list to show which customer placed the order. You can use a lookup field in the **Orders** list to show data from the **Customers** list for the customer who placed the order.

## Summary
What do lookups mean in PowerApps, and why are they important?

Data in an enterprise is large and complex. Every entity that your app is using is likely to have relationships with other entities. For example, an order can show information about the product that was ordered, by linking to a list of products.

Lookups are the primary way such business data comes together.
Lookups make it possible to link the current entity to all the related entities needed f context. For an order, lookups can bring all the information needed about a product such as product pictures, specifications, manufacturer details, etc.

This tutorial shows how lookups work with SharePoint lists. SharePoint provides three types of lookups:

* Choice
* Lookup to another list
* Person or group


We’ll review the specifics of each and use them in an app that we’ll create right in PowerApps. We'll also show how to enable lookups using more than one field.

## Create the lists in SharePoint

### The schema used in this example

This example links two SharePoint custom lists together, **Assets** and **RepairShop**.

The **Assets** list is used to track hardware equipment in a team. Since hardware gets broken from time to time, we use the **RepairShop** list to track the local shops we can contact to get it fixed.

The **Assets** list has a lookup field pointing to a *RepairShop*, so you have to first create the **RepairShop** so that each row in the **Assets** list has something to point to. You use the ContactEmail field to identify the shop, and you may wish to define other fields as well.

Next you create the **Assets** list. You define three columns in **Assets**:
* one of type *lookup* and which points to an email address in the **RepairShop** list.
* one called *AssetType*, of type *choice*, and you populate the choice values when you define the column.
* finally one called *CurrentOwner*, of type *Person or Group*.

You most likely would define additional columns, depending on the information you need to track.

The schema looks something like this:

![](./media/sharepoint-lookup-fields/sharepoint-schema.png)

### Populate the lookup list with data

On your SharePoint site, first enter sample data into the **RepairShop** list.

This ensures that when you create **Assets** entries, there will be **RepairShop** entries available to fill into the *Assets.RepairShop* lookup field.

## Create an app from the main list
Now you create an app that uses these lists.
To build the app, do the following steps:

* Open PowerApps Studio.

	(New to PowerApps? [Sign up for free](https://powerapps.microsoft.com)  using your organizational email address and follow the instructions to download PowerApps Studio from the Windows store)

* In PowerApps Studio, click or tap New --> ”SharePoint”
![](./media/sharepoint-lookup-fields/create-app.png)

* Choose your SharePoint site from the **Recent sites** list or enter your site's url directly into the text box. Click or tap **GO**.
![](./media/sharepoint-lookup-fields/choose-sharepoint-site.png)

* Choose the main list from your SharePoint site, in this example, **Assets**. Click or tap **Connect**.
![](./media/sharepoint-lookup-fields/choose-main-list.png)


## Add data to your main list
Now that the app is generated, let’s run the app and take a look at how the view details screen looks for the three lookup fields.

* Click or tap F5 or the "run triangle" on the upper right of the Studio tool bar.

* Enter an *AssetName*.

* Click or tap the **AssetType** dropdown arrow. Choose one of the entries. Note that the values displayed were those you entered when you created this column.
![](./media/sharepoint-lookup-fields/fill-asset-type.png)

* Click or tap the **RepairShop** dropdown arrow. Choose one of the entries.
![](./media/sharepoint-lookup-fields/fill-repair-shop.png)

* Click or tap the **CurrentOwner** dropdown arrow. Choose one of the entries or enter someone directly.
![](./media/sharepoint-lookup-fields/choose-current-owner.png)

* Enter a **Title** and click the check mark in the upper right corner of the app.

* You can repeat this procedure to enter as many items in your list as you want.

* Press *escape* to return to the Studio designer. To save your app, press **File** and **Save as**.

![AZURE.INCLUE](./includes/app-testing.md)

## Multiple fields in Lookups

PowerApps supports using multiple fields from your lookup data source.

For example, let’s assume your data source contains a lookup field to your employee list, and in your company there are multiple people with the same first and last name.  So that users of your app can properly distinguish between “Anne Smith” from accounting and “Anne Smith” from engineering you can configure your lookup to show more than one field.

Multiple field support is available for both SharePoint and Microsoft Common Data Model today with more connector support on the way.

The existing app allows you to lookup **CurrentOwner** by email address. Lets change it to allow you to look the owner up by **DisplayName** and **Department**.

* Open your app in the Studio designer.

* Click or tap on the **EditScreen** in the left panel.
![](./media/sharepoint-lookup-fields/choose-edit-screen.png)

* Click or tap the **CurrentOwner** field, then click or tap **Advanced**, and finally click or tap **Unlock to change properties**.
![](./media/sharepoint-lookup-fields/enable-edits.png)


* Change **Value1** to *DisplayName*.
![](./media/sharepoint-lookup-fields/change-value1.png)

* Change **Value2** to *Department*.
![](./media/sharepoint-lookup-fields/change-value2.png)

* Now run the app, and start typing a name into the **CurrentOwner** text box. Note that names and departments will appear in the dropdown list, enabling you to use both fields to choose.
![](./media/sharepoint-lookup-fields/multi-field-lookup.png)


## For more information ##
- [Introducing support for lookups and a new sample app](https://powerapps.microsoft.com/en-us/blog/support-for-lookups/)
- [Performance, Refresh button, ForAll, and multiple field lookups](https://powerapps.microsoft.com/en-us/blog/performance-refresh-forall-multiple-field-lookups-531/)
- [Generate an app by using a Common Data Service database](data-platform-create-app.md)
- [Create an app from scratch using a Common Data Service database](data-platform-create-app-scratch.md)
