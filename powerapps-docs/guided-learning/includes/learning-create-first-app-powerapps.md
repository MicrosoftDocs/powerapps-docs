You're now familiar with all the parts of PowerApps and the options for creating apps, so it's time to actually build an app. For this topic, we'll generate a phone app from a SharePoint Online list, but you could use data from lots of other sources, including Excel, cloud services like Salesforce, and on-premises sources such as SQL Server.

## Connect to a data source
In web.powerapps.com, click or tap **Apps** near the left edge, and then click or tap **Create an app** in the banner.

In PowerApps, you can build an app from data, from a template, or from scratch. We're building a phone app for a SharePoint list, so under **SharePoint** click or tap **Phone layout**.

![Phone app from SharePoint list](./media/learning-create-first-app-powerapps/generate-sharepoint-phone.png)

Generated apps are always based on a single list or table (you can add more data to the app later). The next three screens take you through the process of connecting to the **Flooring Estimates** list in SharePoint Online.

![Connect to SharePoint Online list](./media/learning-create-first-app-powerapps/generate-connect-list.png)

After you click **Connect**, PowerApps starts to generate the app. PowerApps makes all sorts of inferences about your data so that it generates a useful app as a starting point.

## Explore the generated app
Success! Your new three screen app opens in PowerApps Studio. All apps generated from data have the same set of screens:

* The **browse** screen: where you browse, sort, filter, and refresh the data pulled in from the list, as well as add items by clicking the (+) icon.
* The **details** screen: where you view more detail about an item, and can choose to delete or edit the item.
* The **edit/create** screen: where you edit an existing item or create a new one.

In the left navigation bar, click or tap an icon in the upper-right corner to switch to the thumbnail view. 

![Toggle the views](./media/learning-create-first-app-powerapps/toggle-view.png)

Click or tap each thumbnail to view the controls on that screen.

![The generated app](./media/learning-create-first-app-powerapps/generate-finished-app.png)

Click or tap ![Start app preview arrow](./media/learning-create-first-app-powerapps/f5-arrow-sm.png) in the top right to run the app. If you navigate through the app, you see that it includes all the data from the list and provides a good default experience.

Wow, that was pretty easy! In a few minutes you learned how to connect to a data source, generate an app, and get acquainted with PowerApps Studio and the three app screens. In later sections, you'll see how to customize generated apps. In the next topic we review this section of the course and get you ready for future lessons.

