---
title: Integrate Power Apps, Power Automate, and Power BI with SharePoint Online
description: In this series of tutorials, we'll explore how to build out a basic canvas app for project management based on SharePoint lists and three key technologies that integrate with SharePoint Online - Power Apps, Power Automate, and Power BI.
author: NickWaggoner
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 06/18/2020
ms.subservice: canvas-maker
ms.author: niwaggon
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - navjotm
  - wimcoor
---
# Integrate Power Apps, Power Automate, and Power BI with SharePoint Online
Do you have SharePoint Online and want to better automate and streamline your business processes? Have you worked with Power Apps, Power Automate, or Power BI, but you're not sure how to use them with SharePoint Online? You've come to the right place! This series of tutorials explores how to build out a basic canvas app for project management based on SharePoint lists and three key technologies that integrate with SharePoint Online: Power Apps, Power Automate, and Power BI. These technologies work together, making it easy to *measure* your business, *act* on the results, and *automate* your workflows. When you're done with this series, you will have a cool scenario like the following:

![Diagram of completed scenario.](./media/sharepoint-scenario-intro/composite-with-background.png)

## Business scenario
In this series of tutorials, the company Contoso has a SharePoint Online site where they manage the lifecycle of projects, from request, to approval, to development, to final review. A *project requestor*, such as a department head, requests an IT project by adding an item to a SharePoint list. A *project approver*, such as an IT manager, reviews the project, and then approves it or rejects it. If approved, the project is assigned to a *project manager*, and additional detail is added to a second list through the same app. A *business analyst* reviews current and completed projects using a Power BI report embedded in SharePoint.  Power Automate is used to send approval email and respond to Power BI alerts.

## Getting started quickly
The scenario we present in this series of tutorials is simple compared to a full-blown project management and analysis app, but it still takes some time to complete all the tasks. If you just want a quick introduction to using Power Apps, Power Automate, and Power BI with SharePoint, check out the following articles:

* **Power Apps**: [Create an app from within SharePoint using Power Apps](app-from-sharepoint.md#create-an-app-from-within-sharepoint-online) and [Create an app to manage data in a SharePoint list](app-from-sharepoint.md)
* **Power Automate**: [Wait for approval in Power Automate](/flow/wait-for-approvals)
* **Power BI**: [Embed with report web part in SharePoint Online](/power-bi/service-embed-report-spo)

When you're done, we hope you'll be back to check out this full scenario.

Even within the scenario, you can focus on the tasks that interest you, and complete the tasks as you have time. After you set up SharePoint lists in task 1, you can work through tasks 2-5 in any order; then tasks 6-8 are sequential. Lastly, we have included two finished apps and a Power BI Desktop report as part of the [download package](https://aka.ms/o4ia0f) for this scenario. You can look at these and learn by example even if you don't go through all the steps in each task.

## Prerequisites
To complete the scenario, you need the following subscriptions and desktop tools. The Office 365 Business Premium subscription includes Power Apps and Power Automate.

| **Subscription or tool** | **Link** |
| --- | --- |
| Office 365 Business Premium subscription |[Trial subscription](https://signup.microsoft.com/Signup?OfferId=467eab54-127b-42d3-b046-3844b860bebf&dl=O365_BUSINESS_PREMIUM&ali=1) |
| Power BI Pro subscription |[Trial subscription](https://powerbi.microsoft.com/get-started/) (click **TRY FREE**) |
| Power BI Desktop |[Free download](https://powerbi.microsoft.com/get-started/) (click **DOWNLOAD FREE**) |

Ideally, you have basic familiarity with each technology, but you can still complete the scenario if you're new to some of these technologies. Use the following content to get up to speed:

* [Get started with SharePoint](https://support.office.com/article/Get-started-with-SharePoint-909ec2f0-05c8-4e92-8ad3-3f8b0b6cf261)
* [Power Apps Guided Learning](/learn/browse/?products=powerapps&resource_type=learning+path)
* [Power Automate Guided Learning](/flow/guided-learning/)
* [Power BI Guided Learning](/power-bi/guided-learning/)

## Next steps
The next step in this tutorial series is to [set up the SharePoint Online lists](sharepoint-scenario-setup.md) that we use throughout the series.

### See also

- [SharePoint integration scenarios](sharepoint/scenarios-intro.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]