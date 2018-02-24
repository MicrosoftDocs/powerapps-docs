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

PowerApps offers users, businesses, partners, independent software vendors (ISVs), and systems integrators (SIs) a powerful platform for building line-of-business apps. The new addition to PowerApps in this release are model apps built using the new Common Data Service (CDS). The new CDS now contains the core functionality of the Dynamics 365 Customer Engagement family of applications. With model apps, you can build apps that use the same extensibility capabilities as those applications, or extend those applications.

> [!NOTE]
> Because the new CDS in this preview release is an instance of Dynamics 365 Customer Engagement, you will find more complete information for developers in the 
 [Developer Guide for Dynamics 365 Customer Engagement](/dynamics365/customer-engagement/developer/developer-guide). This topic will provide an overview with links to more information.

## Progress from simple to sophisticated

![Diagram showing the simple to sophisticated progression](../media/dev-model-apps/simple-to-sophisticated.png)

Canvas apps let power users to create the task-focused apps they need connected to a wide range of data sources, including the new Common Data Service (CDS). 

Model apps provide the way to step up into sophisticated enterprise applications where events that occur within the CDS can trigger logic that can leverage  declarative processes, call custom code, or integrate with external data.

## Declarative development

Model apps provide for declarative development of metadata-driven relational business applications with flexible data models and web services. This means you will usually build model applications without writing code by customizing the application using customization tools provided rather than by writing code.

This approach allows for customers who use your apps or SIs who deploy your apps to adapt them to meet the requirements for each business without having to write code.

### Schema designers

You can add or modify the entities in the system and how they are related to each other. You can create new fields and define how they should behave.

### Business Logic

You can use the Process designers to apply business logic that is evaluated and invoked on the server or on the client.

## Developing with code

While declarative development can address most requirements, there will always be some requirements that are better addressed using code. The CDS enables this in several ways:

### Web services for data operations

Every data operation performed by the application can be done via web services. There are two main web services:
- **Web API**: An OData v4 RESTful web service
    - Recommended for use from external systems written on any language or platform.
    - Frequently used by client-side JavaScript
- **Organization Service**: A WCF service supported by .NET SDK assemblies
    - Required for use in plug-ins

Both services use OAuth 2.0 for authentication

### Plug-ins for server events

You can write .NET assemblies and register them for specific events that occur within the CDS. These assemblies will accept contextual data about the events that occur and you can do the following:
 - Determine that the operation should not complete and cancel it with an error
 - Enrich or modify the data in the operation.
 - Perform additional operations using the organization service.
 - Invoke processes on external system via integration with Azure Service bus or a web hook

These event handlers can respond synchronously or asynchronously. Asynchronous responses for events are added to a queue and performed in a deferred manner to improve overall system performance.

### Web resources

There is a virtual folder called `webresources` within each CDS instance where you can upload HTML, JS, CSS, and image files and access each of them by name in your browser. These files can refer to each other using relative path names. This gives  all the building blocks you need to make web applications using files that are processed within the authenticated session of your browser. Using only client-side code with AJAX techniques, you can create rich applications that can run within a browser window or within an IFrame in a form or dashboard.

### JavaScript for client events

You can write event handler functions using JavaScript for specified form events such as the value of a field in a form changing or a form being saved. Each event is passed contextual data about the events which includes an object model with methods you can call to perform actions within the context of the event. Some things you can do include the following:
 - Cancel the operation
 - Hide or display UI elements depending on rules
 - Display notifications to the user
 - Perform additional data operations using the Web API

JavaScript can also be used to perform operations when custom commands are added to the application.

### Web services for metadata

Both the Web API and Organization Service provide Metadata APIs. You can use these to extend the metadata model with code, but generally you should use the designers. 

The most common scenario is to read metadata so that the logic you apply in code can adapt to how environment has been customized.


## Web services for deployment

, the web services built into the CDS used by model apps allow developers familiar with standards-based web technologies to extend and integrate their business applications built on CDS using HTML, JavaScript, and CSS, and the .NET Framework. The CDS exposes the same end user and administrative capabilities you've seen in the UI through a RESTful web service API built on open standards including OAuth 2.0 and OData v4. Because the CDS embraces web standards, external systems can integrate with your business app built on the CDS using their platform and languages of choice.

More information: [Programming models for Dynamics 365 Customer Engagement](/dynamics365/customer-engagement/developer/programming-models)

## How are model apps different from canvas apps?

While canvas apps can connect to data in the Common Data Service (CDS) as well as other sources, model apps are part of the new CDS that includes the core capabilities of the Dynamics 365 Customer Engagement family of applications. 




Like canvas apps, no code is required to create a model app. Each CDS instance includes a web application that provides a user interface for the app you configure. When you create a model app, you choose which CDS entities to expose in your app and what the navigation experience will be. You will also configure what common lists are available and design forms everyone will use to view and edit data. Users can access your app using their browser or through apps for their phone or tablet.
<!-- Look for new content in this repo -->
More information: [Create or edit an app by using the app designer](/dynamics365/customer-engagement/customize/create-edit-app)

### Transport your model app in a solution file
For developers, one of the most important capabilities is to define a model app and all the supporting components into a *solution* file that you can export. You can then import the solution file into a different environment to move all the functionality of your model app to that environment. 

The solution framework is the key to many of the benefits for developers creating model apps. Think of a solution as both the way you define a software project, like a Visual Studio project, and as how you will distribute your software, like an installer.  When a team of developers work together to create a model app, the components of the solution can be disassembled and checked into your source code repository and then re-assembled so that the functionality included in the solution can be added to another environment or distributed to customers. 

More information: [Introduction to solutions](introduction-solutions.md)



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



## Get Started

As a developer, you probably want to just start looking at the APIs and understand how you write code for model apps using CDS. Slow down.

Remember that all the benefits you gain by using model apps comes from the integrated platform that model apps are built upon. Rather than building an app with code, you will build your app using the app tools which will consume and append to the underlying metadata that drives the platform. Most of the time, you won’t need to or want to define your app using code.

Instead, you will use code to extend the business logic or app behavior when the robust configuration options to customize the app are not sufficient to meet requirements. To avoid writing unnecessary code, you should first understand whether you can achieve the requirement without it. If you find a gap, you can write code to fill that gap rather than attempt to replace existing functionality with code you must write and maintain.

The first step for any developer is to understand how to build and extend model applications without code.

<!-- <continue on to introduce learning path for developers in a separate topic> -->

