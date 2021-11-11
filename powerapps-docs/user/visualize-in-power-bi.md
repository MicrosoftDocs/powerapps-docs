---
title: "Visualize your data in a view quickly with Power BI servic| MicrosoftDocs"
description: Visualize your data in a view quickly with Power BI servic.
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 11/11/2021
ms.subservice: end-user
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Visualize your data in a view quickly with Power BI service (preview)


[This topic is pre-release documentation and is subject to change.]

You can create reports quickly in the Power BI service starting with the data in a view in a model-driven app. Power BI automatically generates the visuals for you, so you can explore your data with just a few clicks.

New to creating in Power BI? Try reading [Reports in Power BI](https://docs.microsoft.com/en-us/power-bi/consumer/end-user-reports) for some quick background information.

If you use Power BI Desktop, you can also [create a report using data from Dataverse in Power BI Desktop](https://docs.microsoft.com/en-us/powerapps/maker/data-platform/data-platform-powerbi-connector).

*IMPORTANT: All the capabilities listed below are available on model-driven apps that have the setting **Enable Power BI quick report visualization on a table (Preview)** enabled.*

![Graphical user interface  text  application Description automatically generated](media/image1.png)

## Visualize in Power BI

In a model-driven app, on a table's homepage grid, select Visualize this view from the list of commands at the top of the page.

![Graphical user interface  text  application  email Description automatically generated](media/image2.png)

You can see a Power BI-generated visualization of the data in the view, based on the view definition. That is, the filters acting on the view are automatically applied to the Power BI visualization. A subset of columns that are part of the view are used to auto-generate the Power BI visuals

![Graphical user interface  application Description automatically generated](media/image3.png)

The full set of view columns are available in the Power BI report to be used to change the data you see in the report.

![Graphical user interface  application  Word Description automatically generated](media/image4.png)

For more information on how you can interact with this visualization please see: Visualize your data quickly from Power Apps and Dynamics 365 apps (Preview) *&lt;Link to be provided by Amanda Rivera&gt;*

## Licensing considerations

Anyone can use the **Visualize this view** feature to explore the data in a view, but to enter the full edit experience, publish reports, access reports that others have published, or delete reports, you need a Power BI Pro license. If you don't currently have a Pro license, you can [buy a Power BI Pro license or start a free trial](https://docs.microsoft.com/en-us/power-bi/fundamentals/service-self-service-signup-purchase-for-power-bi).

## Known issues and limitations

-   The first time you visualize the data in a view, creating the dataset and report can take some time. We're working to improve the end-to-end performance of this experience.

-   Columns are indicated by their logical names rather than the display name. We're working on updating this experience, so the columns' display names are in the Power BI report.

-   This feature isn't supported for guest users in a tenant.
