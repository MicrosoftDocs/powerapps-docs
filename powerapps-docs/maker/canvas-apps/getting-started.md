---
title: Complete guide to building canvas applications
description: Learn to build custom canvas apps in Power Apps without coding. Create business applications that connect to data sources, work across devices, and streamline workflows. Start building today.
author: mduelae

ms.topic: concept-article
ms.custom: canvas
ms.collection: get-started
ms.reviewer: 
ms.date: 04/15/2026
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
searchScope:
  - "Power Apps"
contributors:
  - mduelae
---
# What are canvas apps?

Canvas apps are custom business applications you can create in Microsoft Power Apps without writing code. Think of a canvas as a blank design surface where you can drag and drop components to build exactly the user interface you need. Whether you're creating a simple data entry form or a complex business workflow, canvas apps give you the flexibility to design solutions that work the way your business works.

With canvas apps, you can:

- Connect to [data from hundreds of sources](connections-list.md), including Microsoft 365, Dataverse, SharePoint, and other data sources
- Create responsive designs that work seamlessly across browsers and mobile devices
- Use AI-powered Copilot to build apps through natural language conversations
- Share your apps securely within your organization
- Embed apps directly in SharePoint, Power BI, and Microsoft Teams

This overview helps you understand how to get started building canvas apps and guide you through the key concepts for creating effective business solutions.


## Build an app

The following articles provide guidance on building apps:

- [Create a plan](../plan-designer/create-plan.md)
- [Create a blank canvas app from scratch](create-blank-app.md) 
- [Build apps through conversation with Copilot](ai-conversations-create-app.md)
- [Create a canvas app using Microsoft Dataverse](data-platform-create-app-scratch.md)
- [Create a canvas app with data from a list](app-from-sharepoint.md)
- [Create a canvas app based on Excel data](get-started-create-from-blank.md)


For more information on where makers can create apps, see [Get started with Power Apps](intro-maker-portal.md).

After you generate an app automatically, customize its default appearance and behavior based on your users' workflows. For example, change which types of data appear, how they're sorted, or whether users specify a number by typing it or adjusting a slider. Add and customize [screens](add-screen-context-variables.md), [galleries](customize-layout-sharepoint.md), [forms](customize-forms-sharepoint.md), and other controls.

After you generate and customize an app automatically, create an app from scratch based on [Dataverse](data-platform-create-app-scratch.md), [Excel](get-started-create-from-blank.md), or another data source. By working from the ground up, you get flexibility in app design, flow, and controls, and you can use a larger variety of data sources.

If you're new to Power Apps and want to turn your ideas into a working solution, start with [Planning a Power Apps project](../../guidance/planning/introduction.md).

## Connect to data

Canvas apps can connect to a wide variety of data sources. Choose the data source that best fits your scenario:

- **[Microsoft Dataverse](data-platform-create-app-scratch.md)** &ndash; Use Dataverse as your primary data store for business applications with built-in security, logic, and data management.
- **[SharePoint](app-from-sharepoint.md)** &ndash; Build apps on top of SharePoint lists to extend your existing collaboration workflows.
- **[Excel](get-started-create-from-blank.md)** &ndash; Create apps based on Excel workbooks stored in cloud storage like OneDrive or SharePoint.
- **[SQL Server and Azure SQL](/power-apps/maker/canvas-apps/connections/connection-azure-sqldatabase)** &ndash; Connect directly to SQL databases for enterprise data scenarios.
- **[Other connectors](connections-list.md)** &ndash; Browse hundreds of available connectors for services like Dynamics 365, Salesforce, and more.

For guidance on linking Power Apps data to Microsoft Fabric, see [Configure your environment and link to Microsoft Fabric](/power-apps/maker/data-platform/fabric-link-to-data-platform).

## Share and run an app

When you finish the app and save it to the cloud, [share it with others](share-app.md) in your organization. Specify which users or groups can run the app, and whether they can also customize and share it with more people in the organization.

Run your own apps, and any apps shared with you, on Windows, in a [web browser](../../user/run-app-browser.md), or on an [iOS or Android device](/powerapps/mobile/run-powerapps-on-mobile).

## Licensing and trials

To get started with Power Apps, you need the right license for your scenario:

- **Free trial** &ndash; If you don't have a license for Power Apps, you can [sign up for a free trial](../signup-for-powerapps.md). Trial licenses provide access to most Power Apps features for a limited time.
- **Trial extension** &ndash; If your trial is expiring, contact your admin or visit the [Power Platform admin center](https://admin.powerplatform.microsoft.com/) to explore extension options.
- **Developer environment** &ndash; If you don't have an organization account, establish a developer's account through the [Microsoft Developer Program](https://developer.microsoft.com/en-us/microsoft-365/dev-program).
- **Licensing overview** &ndash; For detailed plan comparisons, see the [Power Apps pricing page](https://powerapps.microsoft.com/pricing/).

## Troubleshoot common issues

If you encounter issues while building or running canvas apps, the following resources can help:

- **[Known issues for canvas apps](/power-apps/maker/canvas-apps/common-issues-and-resolutions)** &ndash; Solutions for common errors and known limitations.
- **[Performance optimization](/power-apps/maker/canvas-apps/performance-tips)** &ndash; Tips for improving app load times and responsiveness, including slow site performance.
- **[Formula reference](/power-platform/power-fx/formula-reference-canvas-apps)** &ndash; Complete reference for Power Fx formulas and functions used in canvas apps.
- **[Coding guidelines](../../guidance/coding-guidelines/overview.md)** &ndash; Best practices for maintaining clean, performant canvas app code.
- **[Dataverse troubleshooting](/troubleshoot/power-platform/dataverse/welcome-dataverse)** &ndash; Resolve issues with Dataverse connections, including mailbox configuration and solution imports.

If your issue isn't resolved through documentation, you can [create a support request](/power-platform/admin/get-help-support) through the Power Platform admin center.

## Learn more

- Want to turn your ideas into an app? Start with [Planning a Power Apps project](../../guidance/planning/introduction.md).
- Explore step-by-step, conceptual, and reference articles in the navigation pane on the left.
- Check out the [webinars and video gallery](https://powerusers.microsoft.com/t5/Webinars-and-Video-Gallery/bd-p/VideoGallery?featured=yes) to learn how to use Power Apps features and functions.

## Share your experience

* Read and post in the [Power Apps Community](https://aka.ms/powerapps-community), where anyone who uses Power Apps can post a question for others to answer. Before you post a question, search the community to see if your question is already answered.
* Submit an idea to improve Power Apps in the [Power Apps Ideas Forum](https://ideas.powerapps.com/).
* If you're a Power Apps admin for your organization, open a support ticket in the [Power Platform admin center](https://admin.powerplatform.microsoft.com/support).



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
