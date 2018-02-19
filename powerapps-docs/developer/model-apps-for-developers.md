---
title: Model apps for developers| Microsoft Docs
description: Describes the value proposition for model apps for developers.
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
ms.date: 08/15/2017
ms.author: jdaly
---
# Model apps for developers

PowerApps model apps offers customers, partners, independent software vendors (ISVs), and systems integrators (SIs) a powerful platform for building line-of-business apps. 

Business apps typically model and track connections between various types of business data (people, places, and things). Model apps provide for declarative development of relational business applications with flexible data models and web services. In addition to the declarative app capabilities, model apps can be extended and integrated with external systems through a set of web services and behaviors can be added to the client using a client API.

## What can you do?

These days there is little time to write a lot of custom code to deliver solutions. To meet requirements for business applications you need a framework that provides the agility and flexibility to rapidly adapt to changes and get user acceptance and adoption. 
Let's look at what you can do with model apps:

### Distribute your apps on AppSource

If you are an ISV, you can sell the model applications you create using AppSource. With AppSource you can promote your app and offer customers the opportunity to try it, buy it, or contact you for more information. When people find your apps on AppSource they will know that it has passed a review of a set of criteria to ensure they will have a good experience with it. Each app is included within a *solution*. 

<!-- <add more information link> -->

### Create modular solutions

The solution framework allows you to create a discrete set of components that provide a set of functionalities that can include entities, security roles, business logic, apps and more. Each solution can be installed and uninstalled to return the customer’s deployment to its original state. Each solution you create runs on top of the system solution and can access the capabilities of that underlying solution.
You can also build solutions that run on top of other solutions to create a set of functionalities that can be shared by different solutions. In this way, you can build and maintain a common module as a solution to support multiple solutions. This way customers only need to install the solution that is right for them and you don’t need to include the same shared functionality in every solution. If you need to push out an update to solution that supports multiple solutions, you only need to update the common module.
Customers, System Implementers, and other ISVs can then build solutions on top of your solutions to achieve the specific customizations they require.

<!-- <add more information link> -->

### Extend data and security models

Solutions can include entities and security roles. Model apps enable you to extend the Common Data Model (CDM) of the Common Data Service (CDS) to meet the data storage and tracking needs of your business app. The data model is protected by an extensible security model to apply role, record and field level, as well as hierarchical security. All other aspects of the CDS platform and user experience are driven by the data and security model you define. In this way, users only see and have access to the data and actions you choose.
Customers of your app can also add their own data elements and security to work seamlessly on top of the data model used by your app. Other ISVs or SIs can build solutions on top of yours, just as yours is built on top of the standard CDS data and security model.

<!-- <add more information link> -->

### Build the app users want

Solutions can include model apps. You can build an app experience that is tailored for specific groups of users using the app designer. With an app, you define which entities are included in the app experience together with specific dashboards, forms, views, charts and business processes. Each app contains a subset of the available entities and can be further limited to only be available to members of security roles you define. If a user participates in multiple roles within an organization, they can choose to run the app which is tailored for the work they are doing.

<!-- <add more information link> -->

### Support multiple languages and currencies

The apps you create are ready for international use. You can export all the text that appears in the user interface of your app, have it localized and then import it back in with the localized text. When users select a different language as their preference, they can use the app with their language preferences applied. If your customers business supports multiple currencies, you can configure the app to support them.

<!-- <add more information link> -->

### Let users build the apps they want

Users with no coding experience can rapidly and easily create their own canvas applications that connect to the same data your app uses to create applications that provide unique task focused experiences or integrate data from other sources.

<!-- <add more information link> -->

### Add custom business logic

Solutions can include business logic. Defining and enforcing consistent business processes is one of the main reasons people use model applications. You can use model applications to define and enforce consistent business processes and rules for your app. Customers that use your app can modify or extend your default app business logic without writing code. You can write code to define business logic that will respond to events raised by the system. Any data operation performed against the data in your app can have the same rules applied regardless of which app people are using.

<!-- <add more information link> -->

### Integrate your apps with Office 365

Office 365 provides so many additional options to work with your app. With your app people will be able to:
- Integrate with Exchange and Outlook for email tracking, scheduling and task management.
- Initiate instant messaging and phone calls with Skype for Business.
- Use Power BI to analyze data.
- Edit data with Excel.
- Take rich contextual notes with OneNote.
- Create personalized documents as a team with automatic document generation and real-time co-authoring.
- Manage contextual documents across SharePoint, Office 365 Groups, and OneDrive for Business.
- Get relevant content with Office Delve based on what they're working on and who they're working with.

<!-- <add more information link> -->

### Use Cross-platform mobile applications

Model mobile apps download metadata about your data model, security configuration, business processes and rules, transforming the out-of-the-box experience into a customized mobile app for your app.
Canvas mobile apps provide highly tailored experiences that can be rapidly created without code.

<!-- <add more information link> -->

### Use business intelligence

People using your app will be able to gain insight into your business and proactively anticipate business needs. They will be able to use Power BI, interactive dashboards and reports, advanced visualizations, and natural language Q&A. People will have visibility into business performance with at-a-glance dashboards and contextual charts inside your business app.

<!-- <add more information link> -->

### Extend with code

While low code or no code customizations are preferred, the web services built into the CDS used by model apps allow developers familiar with standards-based web technologies to extend and integrate their business applications built on CDS using HTML, JavaScript, and CSS, and the .NET Framework. The CDS exposes the same end user and administrative capabilities you've seen in the UI through a RESTful web service API built on open standards including OAuth 2.0 and OData v4. Because the CDS embraces web standards, external systems can integrate with your business app built on the CDS using their platform and languages of choice.

<!-- <add more information link> -->

## Get Started

As a developer, you probably want to just start looking at the APIs and understand how you write code for model apps using CDS. Slow down.
Remember that all the benefits you gain by using model apps comes from the integrated platform that model apps are built upon. Rather than building an app with code, you will build your app using the app tools which will consume and append to the underlying metadata that drives the platform. Most of the time, you won’t need to or want to define your app using code.
Instead, you will use code to extend the business logic or app behavior when the robust configuration options to customize the app are not sufficient to meet requirements. To avoid writing unnecessary code, you should first understand whether you can achieve the requirement without it. If you find a gap, you can write code to fill that gap rather than attempt to replace existing functionality with code you must write and maintain.
The first step for any developer is to understand how to build and extend model applications without code.

<!-- <continue on to introduce learning path for developers in a separate topic> -->

