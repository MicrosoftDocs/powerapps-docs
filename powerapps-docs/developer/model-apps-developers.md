---
title: Model apps for developers| Microsoft Docs
description: Learn how developers can add value to model apps.
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
ms.date: 02/20/2018
ms.author: jdaly
---
# Model apps for developers

Model apps offers businesses, partners, independent software vendors (ISVs), and systems integrators (SIs) a powerful platform for building line-of-business apps. These days there is little time to write a lot of custom code to deliver solutions. To meet requirements for business applications you need a framework that provides the agility and flexibility to rapidly adapt to changes and get user acceptance and adoption. 

Business apps typically model and track connections between various types of business data (people, places, and things). Unlike canvas apps, model apps provide for declarative development of relational business applications with flexible data models and web services. In addition to the declarative app capabilities, model apps can be extended and integrated with external systems through a set of web services as well as capabiliites to include client-side logic using JavaScript.

## How are model apps different from canvas apps?

While canvas apps can connect to data in the Common Data Service (CDS), model apps are part of the new CDS that includes the core capabilities of Dynamics 365 Customer Engagement. Like canvas apps, no code is required to create a model app. Each CDS instance includes a web application that provides a user interface for the app you configure. When you create a model app, you choose which entities to expose in your app and what the navigation experience will be. You will also configure what lists are available and design forms people will use to view and edit data. Users can access your app using their browser or through apps for their phone or tablet.
<!-- Look for new content in this repo -->
More information: [Create or edit an app by using the app designer](/dynamics365/customer-engagement/customize/create-edit-app)

For developers, one of the most important capabilities is to define an app and all the supporting components into a *solution* file that you can export. You can then import the solution file into a different environment to move all the functionality of your model app to that environment. 

The solution framework is the key to many of the benefits for developers creating model apps. Think of a solution as both the way you define a software project, like a Visual Studio project, and as how you will distribute your software, like an installer. 

More information: [Introduction to solutions](introduction-solutions.md)

Because the new CDS in this preview release is an instance of Dynamics 365 Customer Engagement, you will find more information for developers in the 
 [Developer Guide for Dynamics 365 Customer Engagement](/dynamics365/customer-engagement/developer/developer-guide).

## What can you do?

Let's look at what you can do with model apps.

## Distribute your apps on AppSource

If you are an ISV, you can sell the model apps you create using [AppSource](https://appsource.microsoft.com). With AppSource you can promote your app and offer customers the opportunity to try it, buy it, or contact you for more information. When people find your apps on AppSource they will know that it has passed a review of a set of criteria to ensure they will have a good experience with it. Each model app is included within a solution.

More information: [Publish your app on AppSource](/dynamics365/customer-engagement/developer/publish-app-appsource)

## Create modular solution libraries

Line of business applications are frequently delivered as modules for specific industries or groups of users. Each of these apps frequently include similar functionality. Developers need flexibility in how they compose what they ship.

The solution framework allows you to create a discrete set of components that provide a set of functionalities that can include entities, security roles, business logic, apps and more. Each solution can be installed and uninstalled to return the customer’s deployment to its original state. Each solution you create runs on top of the system solution and can access the capabilities of that underlying solution.

You can also build solutions that run on top of other solutions to create a set of functionalities that can be shared by different model apps. In this way, you can build and maintain a common solution library as a module to support multiple solutions. This solution does not need to include a definition of a model app. This way customers only need to install the solution that is right for them and you don’t need to include the same shared functionality in every solution. If you need to push out an update to a solution library that supports multiple solutions, you only need to update the common solution library.

Customers, SIs, and other ISVs can then build solutions on top of your solutions to achieve the specific customizations they require.

More information: [Organize your solutions](/dynamics365/customer-engagement/developer/organize-solutions)

## Extend data and security models

Solutions can include entities and security roles. Model apps enable you to extend the Common Data Model (CDM) of the CDS to meet the data storage and tracking needs of your business app. The data model is protected by an extensible security model to apply role, record and field level, as well as hierarchical security. All other aspects of the CDS platform and user experience are driven by the data and security model you define. In this way, users only see and have access to the data and actions you choose.

Customers of your app can also add their own data elements and security to work seamlessly on top of the data model used by your app. Other ISVs or SIs can build solutions on top of yours, just as yours is built on top of the standard CDS data and security model.

More information: [Model your business data](/dynamics365/customer-engagement/developer/model-business-data) and  [Security model of Customer Engagement](/dynamics365/customer-engagement/developer/security-dev/security-model)

## Support multiple languages and currencies

The apps you create are ready for international use. You can export all the text that appears in the user interface of your app, have it localized and then import it back in with the localized text. When users select a different language as their preference, they can use the app with their language preferences applied. If your customers business supports multiple currencies, you can configure the app to support them.

More information: [Work with an international audience](/dynamics365/customer-engagement/customize/work-with-international-audience) and [Regional and other business management settings](/dynamics365/customer-engagement/admin/regional-other-business-management-settings)

## Add custom business logic

Solutions can include business logic. Defining and enforcing consistent business processes is one of the main reasons people use model applications. You can use model applications to define and enforce consistent business processes and rules for your app. Customers that use your app can modify or extend your default app business logic without writing code. You can write code to define business logic that will respond to events raised by the system. Any data operation performed against the data in your app can have the same rules applied regardless of which app people are using.

More information: 
 - [Create custom business logic through processes](/dynamics365/customer-engagement/customize/guide-staff-through-common-tasks-processes)
 - [Extend Dynamics 365 Customer Engagement on the server](/dynamics365/customer-engagement/developer/extend-dynamics-365-server)

## Integrate your apps with Office 365

Office 365 provides so many additional options to work with your app. With your app people will be able to:
- Integrate with Exchange and Outlook for email tracking, scheduling and task management.
- Initiate instant messaging and phone calls with Skype for Business.
- Use Power BI to analyze data.
- Edit data with Excel.
- Take rich contextual notes with OneNote.
- Create personalized documents as a team with automatic document generation and real-time co-authoring.
- Manage contextual documents across SharePoint, Office 365 Groups, and OneDrive for Business.
- Get relevant content with Office Delve based on what they're working on and who they're working with.

More information: [Add Office 365 Online services](/dynamics365/customer-engagement/admin/add-office-365-online-services)

## Use Cross-platform mobile applications

Model mobile apps download metadata about your data model, security configuration, business processes and rules, transforming the out-of-the-box experience into a customized mobile app for your app.

More information [User Guide (Dynamics 365 for phones and tablets)](/dynamics365/customer-engagement/mobile-app/dynamics-365-phones-tablets-users-guide)

## Use business intelligence

People using your app will be able to gain insight into your business and proactively anticipate business needs. They will be able to use Power BI, interactive dashboards and reports, advanced visualizations, and natural language Q&A. People will have visibility into business performance with at-a-glance dashboards and contextual charts inside your business app.

More information: [Reporting and Analytics Guide for Dynamics 365 Customer Engagement](/dynamics365/customer-engagement/analytics/reporting-analytics-with-dynamics-365)

## Extend with code

While low code or no code customizations are preferred, the web services built into the CDS used by model apps allow developers familiar with standards-based web technologies to extend and integrate their business applications built on CDS using HTML, JavaScript, and CSS, and the .NET Framework. The CDS exposes the same end user and administrative capabilities you've seen in the UI through a RESTful web service API built on open standards including OAuth 2.0 and OData v4. Because the CDS embraces web standards, external systems can integrate with your business app built on the CDS using their platform and languages of choice.

More information: [Programming models for Dynamics 365 Customer Engagement](/dynamics365/customer-engagement/developer/programming-models)

## Get Started

As a developer, you probably want to just start looking at the APIs and understand how you write code for model apps using CDS. Slow down.

Remember that all the benefits you gain by using model apps comes from the integrated platform that model apps are built upon. Rather than building an app with code, you will build your app using the app tools which will consume and append to the underlying metadata that drives the platform. Most of the time, you won’t need to or want to define your app using code.

Instead, you will use code to extend the business logic or app behavior when the robust configuration options to customize the app are not sufficient to meet requirements. To avoid writing unnecessary code, you should first understand whether you can achieve the requirement without it. If you find a gap, you can write code to fill that gap rather than attempt to replace existing functionality with code you must write and maintain.

The first step for any developer is to understand how to build and extend model applications without code.

<!-- <continue on to introduce learning path for developers in a separate topic> -->

