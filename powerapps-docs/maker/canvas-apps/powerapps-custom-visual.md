---
title: PowerApps custom visual for Power BI | Microsoft Docs
description: Embed an app that uses the same data source and can be filtered like other report items 
services: powerapps
suite: powerapps
documentationcenter: na
author: mgblythe
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: tutorial
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/15/2018
ms.author: mblythe
---

# PowerApps custom visual for Power BI

Power BI enables data insights and better decision-making, while PowerApps enables everyone to build and use apps that connect to business data. Using the PowerApps custom visual, you can pass context-aware data to a PowerApps app, which updates in real time as you make changes to your report. Now, your app users can derive business insights and take actions from right within their Power BI reports and dashboards.

# Using the PowerApps custom visual

Let's look at the steps required to use the PowerApps custom visual in your Power BI report. You can also go through a simple [step-by-step tutorial](embed-powerapps-powerbi.md) and check out out our [video](https://aka.ms/powerappscustomvisualvideo).

1. Get the custom visual from [AppSource](https://appsource.microsoft.com/product/power-bi-visuals/WA104381378?tab=Overview) or directly import it in the Power BI service.

    ![Custom visual in marketplace](./media/powerapps-custom-visual/powerapps-store.png) 

1. Add the PowerApps visual to your report and set the data fields associated with it.

    ![Select report data](./media/powerapps-custom-visual/add-visual-set-data.png)

1. Now, you have the option to create a new app or use an existing app. 

    ![New or existing app](./media/powerapps-custom-visual/create-new-or-choose-app.png)
    
    If you choose to use an existing app, the visual prompts you to open the app in PowerApps. The visual then sets up the required components in your app so that Power BI can send data to PowerApps.

    If you create a new app, PowerApps creates a simple app with the required components already set up.

    ![New app](./media/powerapps-custom-visual/new-app.png)

1. Now in PowerApps Studio, you can use the data fields you set in step 2. The PowerBIIntegration object acts like any other PowerApps read-only data source or collection. You can use the object to populate any control, or join and filter with other data sources.

    ![Custom formula](./media/powerapps-custom-visual/custom-formula.png)

    The formula I used here to join Power BI data with my Customer data source is: `LookUp(Customer,Customer\_x0020\_Name=First(PowerBIIntegration.Data).Customer\_Name)`

 The Power BI report and the instance of PowerApps Studio that was launched share a live data connection. While they are both open, you can filter or change the data in your report to see the updated data reflect immediately in your app in PowerApps Studio.

1. After you have completed building or making changes to your app, save and publish the app in PowerApps to see your app in the Power BI report.

    > [!Note] 
    > If you are editing an existing app, the current version of visual will not reload the app when a newer version in published from PowerApps. You will have to save your report and reload the browser page to see the latest version of the app.

1. Once you are satisfied with your changes, make sure to share the PowerApps app with users of your report and then save your report.

    If you want to again edit the app, click or tap **More options** and then select **Edit** from the PowerApps visual.

1. And with that, you have created a report in which your users can take actions as they gain insights from your data.

    ![Working report](./media/powerapps-custom-visual/working-report.gif)

    If you need to makes changes to an app, open the report in edit mode, click or tap **More options** (**. . .**) on the PowerApps visual and select **Edit**.

    ![Edit app](./media/powerapps-custom-visual/edit-app.png)

## Limitations of the PowerApps custom visual

The PowerApps custom visual is currently available in preview and has some limitations as listed below. We want to gather your feedback and address some of these limitations before we make the visual generally available:

- You cannot create or modify apps when using the PowerApps custom visual in Power BI desktop, Internet Explorer, or Mozilla Firefox. We recommend that you first publish your report to the Power BI service. Then use Microsoft Edge or Google Chrome to create new apps and make changes to apps.
- If your PowerApps visual has been configured with an app, and you publish a newer version of the app from PowerApps Studio, the open report will not reload the app automatically. You must reload your report to get the latest version of the app.
- If you change the data fields associated with the visual, you must edit the app from the Power BI service to make sure that the changes are propagated to PowerApps. If you don't do this, you will see unexpected behavior in the app.
- The PowerApps custom visual cannot trigger a refresh of the Power BI report or Power BI data source. If you write back data from the app to the same data source as the report, your changes won't be reflected immediately. Changes are reflected on the next scheduled refresh.
- The PowerApps custom visual cannot filter the data or send any data back to the report.
- You will need to share the PowerApps app separately from your report. Learn about [sharing apps in PowerApps](share-app.md).
- PowerApps custom visual is currently not supported on Power BI mobile app.

Please join the conversation in the [PowerApps community](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1) as we would love to hear from you about how you are using this capability and what you would like to see added in the future.



