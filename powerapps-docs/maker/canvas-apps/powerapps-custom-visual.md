---
title: Power Apps custom visual for Power BI | Microsoft Docs
description: Procedure and limitations for embedding a canvas app that uses the same data source and can be filtered like other report items in Power BI 
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 12/02/2019
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Power Apps custom visual for Power BI

Power BI enables data insights and better decision-making, while Power Apps enables everyone to build and use apps that connect to business data. Using the Power Apps custom visual, you can pass context-aware data to a canvas app, which updates in real time as you make changes to your report. Now, your app users can derive business insights and take actions from right within their Power BI reports and dashboards.

## Using the Power Apps custom visual

Let's look at the steps required to use the Power Apps custom visual in your Power BI report.

1. Power Apps custom visual is available by default in the Power BI service. If you are using Power BI Desktop and don’t see it, you must upgrade to the latest version of Power BI Desktop.

2. Add the Power Apps visual to your report, and set the data fields associated with it.

    ![Select report data](./media/powerapps-custom-visual/add-visual-set-data.png)

    You can choose an existing app or create one, but the report must be published to the Power BI service and opened in Microsoft Edge or Google Chrome.

3.  If you choose to create an app, you can choose in which environment to create it.

    ![New or existing app](./media/powerapps-custom-visual/create-new-or-choose-app.png)

    If you choose to use an existing app, the visual prompts you to open the app in Power Apps. The visual then sets up the required components in your app so that Power BI can send data to Power Apps.

    If you create a new app, Power Apps creates a simple app with the required components already set up.

    ![New app](./media/powerapps-custom-visual/new-app.png)

4. Now in Power Apps Studio, you can use the data fields you set in step 2. The `PowerBIIntegration` object acts like any other Power Apps read-only data source or collection. You can use the object to populate any control, or join and filter with other data sources.

    ![Custom formula](./media/powerapps-custom-visual/custom-formula.png)

    This formula joins Power BI data with the Customer data source: `LookUp(Customer,Customer_x0020_Name=First(PowerBIIntegration.Data).Customer_Name)`

   The Power BI report and the instance of Power Apps Studio that was launched share a live data connection. While they are both open, you can filter or change the data in your report to see the updated data reflect immediately in your app in Power Apps Studio.

5. After you have completed building or making changes to your app, save and publish the app in Power Apps to see your app in the Power BI report.

6. Once you are satisfied with your changes, make sure to share the Power Apps app with users of your report and then save your report.

7. And with that, you have created a report in which your users can take actions as they gain insights from your data.

    ![Working report](./media/powerapps-custom-visual/working-report.gif)

    If you need to makes changes to an app, open the report in edit mode, click or tap **More options** (**. . .**) on the Power Apps visual and select **Edit**.

    ![Edit app](./media/powerapps-custom-visual/edit-app.png)

## Limitations of the Power Apps custom visual

The following limitations apply to the Power Apps custom visual:

- If you change the data fields associated with the visual, you must edit the app from within the Power BI service by selecting the ellipsis (...) and then selecting **Edit**. Otherwise, the changes won't be propagated to Power Apps, and the app will behave in unexpected ways.
- The Power Apps custom visual can't trigger a refresh of Power BI reports and Power BI data sources from within Power BI Desktop. If you write back data from the app to the same data source as the report, your changes won't be reflected immediately in Power BI Desktop. Changes are reflected on the next scheduled refresh.
- The Power Apps custom visual can't filter the data or send any data back to the report.
- You'll need to share the Power Apps app separately from your report. Learn about [sharing apps in Power Apps](share-app.md).
- Power BI Report Server and the mobile app for Power BI do not support the Power Apps custom visual.
- Following limitations apply when using PowerBIIntegration.Refresh() function:
    - You must author the app from Power Apps custom visual in Power BI report for this function to be available.
    - You must use a source that supports [DirectQuery](https://docs.microsoft.com/power-bi/desktop-directquery-data-sources) and the data connection must be created using DirectQuery method.
- Power Apps in Power BI Desktop provides data to Power Apps Studio when creating apps but not while editing. Use Power BI Web to preview the data while editing apps.

> [!NOTE]
> We recommend that you first publish your report to the Power BI service and then create or modify apps.

## Browser support

The following table lists the browser supportability for view, create and modify actions of the Power Apps custom visual. Supported browsers and actions are identified by a check mark ( &check; ).

|Browser|View|Create|Modify
|-|-|-|-
|Microsoft Edge|&check;|&check;|&check;
|Internet Explorer 11|&check;
|Google Chrome|&check;|&check;|&check;
|Safari \*|&check;
|Mozilla Firefox
|All other browsers

\* In Safari, you must enable cross site tracking (**Preferences** > **Privacy**, and clear **Prevent cross site tracking**) to view Power Apps custom visual.

## Accessibility support

To navigate the Power Apps visual using the keyboard follow these steps:

1. Focus selection on the Power BI Report for the desired Power Apps visual.
2. Use the **Tab** key on the keyboard until the visual is highlighted.
3. Use the **Ctrl+Right** key on the keyboard to enter the visual.
3. Use the  **Tab** key on the keyboard until the desired component of the visual is selected.

For more information see: [Power BI Accessibility Documentation]( https://docs.microsoft.com/power-bi/desktop-accessibility)


## Next steps

* Go through a simple [step-by-step tutorial](embed-powerapps-powerbi.md).
* Check out our [video](https://aka.ms/powerappscustomvisualvideo).
