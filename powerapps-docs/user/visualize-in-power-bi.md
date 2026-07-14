---
title: "Visualize your data in a view quickly with Power BI service| MicrosoftDocs"
description: Visualize your data in a view quickly with Power BI service.
author: shwetamurkute

ms.component: pa-user
ms.topic: how-to
ms.date: 10/19/2023
ms.subservice: end-user
ms.author: smurkute
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
contributors:
- RichdiMSFT 
---

# Visualize data in a view with Power BI service

Create reports in the Power BI service using the data that's in a view of your model-driven app. Power BI automatically generates the visuals for you, so you can start exploring the data with just a few clicks.

If you're new to Power BI reports and need more information, see [Reports in Power BI](/power-bi/consumer/end-user-reports).

If you're using Power BI Desktop, you can also [create a report using data from Dataverse in Power BI Desktop](/powerapps/maker/data-platform/data-platform-powerbi-connector).

> [!NOTE]
> Your administrator needs to turn on the **Enable Power BI quick report visualization on a table** feature setting, to use the capabilities that are covered in this topic. For more information, see [Manage feature settings](/power-platform/admin/settings-features).

   > [!div class="mx-imgBorder"]
   > ![Enabled Power BI report visualization on a table](media/powerbi-image1.png)

## Visualize in Power BI

1. In your model-driven app, select a table and then on the command bar, select **Visualize this view**.

   > [!div class="mx-imgBorder"]
   > ![Graphical user interface  text  application  email Description automatically generated](media/powerbi-image2.png)

2. Power BI-generates visuals of the data in your view, based on the view definition. That is, the filters acting on the view are automatically applied to the Power BI visualization. A subset of columns that are part of the view are used to auto-generate the Power BI visuals.

   > [!div class="mx-imgBorder"]
   > ![Graphical user interface  application Description automatically generated](media/powerbi-image3.png)

   The full set of view columns are available in the Power BI report to be used to change the data you see in the report.

   > [!div class="mx-imgBorder"]
   > ![Graphical user interface  application  Word Description automatically generated](media/powerbi-image4.png)

For more information on how you can interact with this visualization, see [Visualize your data quickly from Power Apps and Dynamics 365 apps (preview)](/power-bi/create-reports/dynamics-quick-create-report).

## Licensing considerations

Anyone can use the **Visualize this view** feature to explore the data in a view, but to use the full edit experience, publish reports, access reports that others have published, or delete reports, you need a Power BI Pro license. If you don't currently have a Pro license, you can [buy a Power BI Pro license or start a free trial](/power-bi/fundamentals/service-self-service-signup-purchase-for-power-bi).

## Known issues and limitations

- The first time you visualize the data in a view, creating the dataset and report can take some time. We're working to improve this performance experience.

- This feature isn't supported for the **Activities** table due to a limitation in generating charts.

- This feature isn't supported for guest users in a tenant.

- If you're building your app for mobile, Power BI dashboards aren't a recommended choice to visualize data. Power BI dashboards are suited for larger screens, and the small screens and form factor of mobile devices can cause usability issues with scroll bars, filters, and more.
