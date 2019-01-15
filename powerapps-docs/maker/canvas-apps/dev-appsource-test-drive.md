---
title: Let customers test drive your canvas app on AppSource | Microsoft Docs
description: Use AppSource to share a canvas app with customers, and generate leads for your business.
author: linhtranms
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 05/08/2017
ms.author: litran
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Let customers test drive your canvas app on AppSource

Are you passionate about building canvas apps in PowerApps? Do you want to share a canvas app with customers? [AppSource.com](https://appsource.microsoft.com) supports PowerApps Test Drive solutions as a way for you to share apps with customers and generate leads for your business.

## What is a Test Drive solution?

A Test Drive solution enables your customers to try out a real app, without signing up for a PowerApps plan or installing any applications. Customers just sign into AppSource.com using their Azure Active Directory (AAD) account and run the app in a web browser. Without Test Drive, customers can only read about your app or watch a video that describes it. With Test Drive, customers get a better idea of what your solution is and what functionality your app has. And they have the experience of actually using the app. Customers won't be able to look under the hood to see how your app is built, so your intellectual property is protected. We collect and share lead information for users that launch your Test Drive app to help you grow your business.

Here is the example of an [app listing](https://go.microsoft.com/fwlink/?linkid=848867) on AppSource.com:

![Sample AppSource listing ](./media/dev-appsource-test-drive/sample-app-source-listing.png)

Selecting the **Free Trial** link from the app listing above launches the associated PowerApps Test Drive app directly within the user's browser:

![Sample App Web Player](./media/dev-appsource-test-drive/sample-app-web-player.png)

## How do I build a Test Drive solution?
Building an app for a Test Drive solution is just like building any app in PowerApps, but you use embedded data instead of external data connections. Using embedded data reduces the barrier of deploying the app to your customer, so there is zero friction for them to try it out. The full solution that you ultimately distribute to customers typically includes data connections, but embedded data works well for a Test Drive solution.

PowerApps natively supports building apps with embedded data, so you just need sample data for your app to use. This data should be captured in an Excel file as one or more tables. In PowerApps, you then pull the data from the Excel tables into the app and work with it there, rather than through an external connection. The three-step process below shows you how to pull data in and use that data in your app.

### Step 1: Import data into the app
Assume you have an Excel file with two tables: **SiteInspector** and **SitePhotos**.

![Excel tables to import](./media/dev-appsource-test-drive/excel-file.png)

Import these two tables into PowerApps by using the option **Add static data to your app**.

![Add static data to your app](./media/dev-appsource-test-drive/static-data.png)

You now have the tables as data sources in your app.

![Excel tables as imported data sources](./media/dev-appsource-test-drive/data-sources.png)

### Step 2: Handling read-only and read-write scenarios
The data you imported is *static*, therefore read-only. If your app is read-only (i.e. it only displays data to the user), reference the tables directly in the app. For example, if you want to access the **Title** field in the **SiteInspector** table, use **SiteInspector.Title** in your formula.

If your app is read-write, first pull the data from each table into a *collection*, which is a tabular data structure in PowerApps. Then work with the collection rather than the table. To pull data from the **SiteInspector** and **SitePhotos** tables into the **SiteInspectorCollect** and **SitePhotosCollect** collections:

```powerapps-dot
ClearCollect( SiteInspectorCollect, SiteInspector ); 
ClearCollect( SitePhotosCollect, SitePhotos )
```

The formula clears both collections, then collects data from each table into the appropriate collection:

* Call this formula somewhere in your app to load the data.
* View all collections in your app by navigating to **File** > **Collections**.
* For more information, see [Create and update a collection in your app](../canvas-apps/create-update-collection.md).

Now if you want to access the **Title** field, use **SiteInspectorCollect.Title** in your formula.

### Step 3: Add, update, and delete data in your app
You've seen how to read data directly and from a collection; now we'll show you how to add, update, and delete data in a collection:

**To add a row to a collection**, use [Collect( DataSource, Item, ... )](../canvas-apps/functions/function-clear-collect-clearcollect.md):

```powerapps-dot
Collect( SiteInspectorCollect,
    {
        ID: Value( Max( SiteInspectorCollect, ID ) + 1 ),
        Title: TitleText.Text,
        SubTitle: SubTitleText.Text,
        Description: DescriptionText.Text
    }
)
```

**To update a row in a collection**, use [UpdateIf( DataSource, Condition1, ChangeRecord1 [, Condition2, ChangeRecord2, ...] )](../canvas-apps/functions/function-update-updateif.md):

```powerapps-dot
UpdateIf( SiteInspectorCollect,
    ID = record.ID,
    {
        Title: TitleEditText.Text,
        SubTitle: SubTitleEditText.Text,
        Description: DescriptionEditText.Text
    }
)
```

**To delete a row from a collection**, use [RemoveIf( DataSource, Condition [, ...] )](../canvas-apps/functions/function-remove-removeif.md):

```powerapps-dot
RemoveIf( SiteInspectorCollect, ID = record.ID )
```

> [!NOTE]
> Collections hold data only while the app is running; any changes are discarded when the app is closed.

In summary, you can create a version of your app with embedded data, which simulates the experience of your app connecting to external data. After the data is embedded, you will be ready to publish this app as a Test Drive solution on  AppSource.com.

## How do I list my Test Drive solution on AppSource.com?
Now that your app is ready, it's time to publish it to AppSource.com. In order to start this process, please complete the [application form](https://powerapps.microsoft.com/partners/get-listed/) on PowerApps.com.

Once you apply you will receive an email with instructions on how to submit your app to be published on AppSource.com. The onboarding documentation that captures the full end-to-end process can also be downloaded [here](https://go.microsoft.com/fwlink/?linkid=851031).

