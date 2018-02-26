---
title: Understand what developers can do with model apps| Microsoft Docs
description: Learn how developers can do with model apps as well as things they don't need to do.
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 02/26/2018
ms.author: jdaly
---
# Understand what developers can do with model apps

As a developer working with the PowerApps platform it is important for you to understand what you can do and what this means about where and when you will write code.

## Distribute your apps on AppSource

If you are an ISV, you can sell the model-driven applications you create using [AppSource](https://appsource.microsoft.com). With AppSource you can promote your app and offer customers the opportunity to try it, buy it, or contact you for more information. When people find your apps on AppSource they will know that it has passed a review of a set of criteria to ensure they will have a good experience with it.

Your apps will be distributed as solutions or as packages containing one or more solutions and other assets. If your app requires multiple solutions or other assets, you will use the *Package Deployer* to create an installable package containing your application so that it can be deployed to the customers environment when they want to try or buy your application.

More information: 
- [Tools and resources for developers](model-apps-developers.md#tools-and-resources-for-developers)
- [Introduction to solutions](introduction-solutions.md)
- [Publish your app on AppSource](/dynamics365/customer-engagement/developer/publish-app-appsource)

## Achieve many requirements without code

The PowerApps platform is designed so that people with a wide range of skills can extend it to build functionality that they need. This allows for rapid application development to meet the needs for change as the business requirements change.

![Diagram showing simple to sophisticated extensions](../media/dev-model-apps/simple-to-sophisticated.png)

This diagram illustrates how the combination of canvas and model apps can be used together by people with a wide range of skills.

As a developer, you need to understand the best way to meet a requirement may not involve writing code. In fact, you should consider writing code as a last resort when no other method will work. To understand what must be done in code you need to understand what can be done without code.

### Declarative development
Declarative development means that rather than writing code to build some functionality, you will use designers included in the application to create and modify metadata that will tell the platform what to do.

Model apps provide designers to achieve the following:


|Task  |Description  |
|---------|---------|
|Schema modification|You will usually use the solution explorer tools to create entities to store data. Use these same tools to create attributes on entities and relationships between them.<br />More information: [Customization Guide: Customize entities, relationships, and fields](/dynamics365/customer-engagement/customize/customize-entities-relationships-fields)<br /><br />There are also a complete set of metadata APIs that allow you to perform the same operations with code if you need to.<br />More information: [Metadata Services](use-web-services.md#metadata-services)<br />|
|Security Model|An extensible security model protects the data model to apply role, record and field level, as well as hierarchical security. All other aspects of the Common Data Service for Apps platform and user experience are driven by the data and security model. In this way, users only see and have access to the data and actions they need. <br />More information: <br />[Administrator Guide: Manage security, users, and teams](/dynamics365/customer-engagement/admin/manage-security-users-and-teams)<br />[Customization Guide: Manage access to apps by using security roles](/dynamics365/customer-engagement/customize/manage-access-apps-security-roles)<br />[Developer Guide: Security model of Customer Engagement](/dynamics365/customer-engagement/developer/security-dev/security-model)|
|Business logic|There are several different kinds of process designers that can apply business logic both on the server and on the client.<br />One of these options is *custom actions* which creates a new message you can use with code.<br />More information:  [Customization Guide: Create custom business logic through processes](/dynamics365/customer-engagement/customize/guide-staff-through-common-tasks-processes)<br /><br />If the designers cannot meet your requirement, as a developer you have other options. <br />More Information: <br />[Use Custom Actions](use-web-services.md#use-custom-actions)<br />[Apply Business Logic with code](apply-business-logic-with-code.md)|
|Custom app experiences|Model apps are experiences that are tailored for specific groups of users. You create them using the app designer. With an app, you define which entities are included in the app together with specific dashboards, forms, views, charts and business processes. Each app contains a subset of the available entities and can be further limited to only be available to members of security roles you define. If a user participates in multiple roles within an organization, they can choose to run the app which is tailored for the work they are doing.<br />More information: [Customization Guide: Design custom business apps by using the app designer](/dynamics365/customer-engagement/customize/design-custom-business-apps-using-app-designer)|
|Custom themes, forms, charts, and dashboards|Use designers to apply all the changes to the way the application looks and the assets available for users to work with. <br />More information in the [Customization Guide](/dynamics365/customer-engagement/customize/): <br />[Create a theme](/dynamics365/customer-engagement/customize/change-color-scheme-add-logo-match-organizations-brand)<br />[Create and design forms](/dynamics365/customer-engagement/customize/create-design-forms)<br />[Understand views (lists)](/dynamics365/customer-engagement/customize/create-edit-views)<br />[Create or edit dashboards](/dynamics365/customer-engagement/customize/create-edit-dashboards)<br />[Create or edit a system chart](/dynamics365/customer-engagement/customize/create-edit-system-chart)|

## Integrate your apps with Office 365

Office 365 provides so many additional options to work with your model app. With your app people will be able to:
- Integrate with Exchange and Outlook for email tracking, scheduling, and task management.
- Initiate instant messaging and phone calls with Skype for Business.
- Use Power BI to analyze data.
- Edit data with Excel.
- Take rich contextual notes with OneNote.
- Create personalized documents as a team with automatic document generation and real-time co-authoring.
- Manage contextual documents across SharePoint, Office 365 Groups, and OneDrive for Business.
- Get relevant content with Office Delve based on what they're working on and who they're working with.

More Information: [Administrator Guide: Add Office 365 Online services](/dynamics365/customer-engagement/admin/add-office-365-online-services)

## Provide Cross-platform mobile applications

Mobile model apps download metadata about your data model, security configuration, business processes and rules, transforming the out-of-the-box experience into a customized mobile app for your model app.

More information: [Phones and tablets : Overview of Dynamics 365 for phones and tablets](/dynamics365/customer-engagement/mobile-app/overview)

Canvas apps also provide highly tailored mobile experiences that can be rapidly created without code.
More information: [Quickstart: Run a canvas-based app on a mobile device](../run-app-client.md)

## Provide Business intelligence

People using your application will be able to gain insight into your business and proactively anticipate business needs. They will be able to use Power BI, interactive dashboards and reports, advanced visualizations, and natural language Q&A. People will have visibility into business performance with at-a-glance dashboards and contextual charts inside your business application.

More information : [Reporting and Analytics Guide for Dynamics 365 Customer Engagement](/dynamics365/customer-engagement/analytics/reporting-analytics-with-dynamics-365)

## Support multiple languages and currencies

The model apps you create are ready for international use. You can export all the text that appears in the user interface of your application, have it localized and then import it back in with the localized text. When users select a different language as their preference, they can use the app with their language preferences applied. If your customers business supports multiple currencies, you can configure the app to support them.

More information: 

- [Administrator Guide: Regional and other business management settings](/dynamics365/customer-engagement/admin/regional-other-business-management-settings)
- [Developer Guide: Create solutions that support multiple languages](/dynamics365/customer-engagement/developer/create-solutions-support-multiple-languages)


## Compose modular solutions

Model apps are included within solutions, but not every solution contains a model app. You can use the solution framework to compose individual modules that can provide layers of shared functionality that is used by multiple model apps. This provides a flexible way to distribute and maintain functionality that you provide.

More information: [Modular solutions](introduction-solutions.md#modular-solutions)

## Use web development skills with Web Resources

There is a virtual folder called `webresources` within each Common Data Service for Apps instance where you can upload HTML, JS, CSS, and image files and access each of them by name in your browser. These files can refer to each other using relative path names. This provides all the building blocks you need to make web applications using files that are processed within the authenticated session of your browser. Using only client-side code with AJAX techniques, you can create rich applications that can run within a browser window or within an IFrame in a form or dashboard. 

Most commonly, you will use JavaScript web resources to add event handler functions to forms and commands.

More information:
- [Developer Guide: Client scripting in Customer Engagement using JavaScript](/dynamics365/customer-engagement/developer/clientapi/client-scripting)
- [Developer Guide: Web resources for Customer Engagement](/dynamics365/customer-engagement/developer/web-resources)

## Customize Commands

The commands that appear within a form or list command bar are customizable. 
- You can define *display rules* that are evaluated when the form or list loads to determine whether a command or group of commands are visible.
- You can define *enable rules* that control whether a command is enabled based on various conditions such as the currently selected item in the UI.
- You must define an *action* for each command to tell it what to do when selected. A command can open a URL or execute a function defined within a JavaScript web resource.

Custom commands are positioned based on any existing commands. You must compose a *custom action* that defines what change to apply to the existing set of commands. There is no designer provided for commands. Fortunately, the community has provided tools. The [Ribbon Workbench](http://www.develop1.net/public/rwb/ribbonworkbench.aspx) provides a graphical interface and is the most commonly used tool to customize commands.

More information: [Developer Guide: Customize commands and the ribbon](/dynamics365/customer-engagement/developer/customize-dev/customize-commands-ribbon)

