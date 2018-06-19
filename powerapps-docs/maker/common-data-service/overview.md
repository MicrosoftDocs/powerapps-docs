---
title: "Customization Guide (Dynamics 365 Customer Engagement) | MicrosoftDocs"
ms.custom: ""
ms.date: 06/18/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: e9810433-224b-4bde-851a-e581cf5fb8a4
caps.latest.revision: 21
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
---

# Customization Guide for Dynamics 365 Customer Engagement

The way your organization works is unique. Some organizations have well-defined business processes that they apply using PowerApps apps. Others aren’t happy with their current business processes and use PowerApps to apply new data and processes to their business. Whatever situation you find yourself in, you’ll find a lot of customization capabilities in PowerApps so that it can work for your organization.  
  
 Of course you’re eager to get started, but please take a few minutes to read the content in this section. This will introduce you to important terms, give you some background about why things are done a certain way, and help you avoid potential problems in the future.  

## What is metadata and why should you care?  
 In the past, you may have customized business applications by editing the source code. This created complications because each organization had unique changes and it was very difficult, or extremely expensive, to upgrade. Then application developers started exposing application programming interfaces (APIs) so that other developers could interact with the application and add their own logic without touching the source code. This was moderately better because it means developers can extend the application without changing it. But it still requires a developer to write code.  
  
 Today, modern business applications use a metadata-driven architecture so that people can customize the application without writing code. Metadata means “data about data” and it defines the structure of the data stored in the system. With this metadata, an application knows about any changes to the data structure and this enables the application to adapt as the data structure changes. Since the metadata is known, additional capabilities can be included that are tied to the metadata.  
  
 When you customize you app using the customization tools in PowerApps, you’re adding or updating the metadata or data used by features that depend on the metadata. Because we know the kinds of data used to customize apps, we can take this data into account and add new features to PowerApps without breaking your app. This way you should always be able to apply an update rollup or upgrade to the latest version and enjoy the best new features.  
  
> **Customize or Configure?**   
> Most people say they want to customize the application, so we use the word “customize” to describe changing the system to make it work the way you want. Some people prefer to use the word “configure” because it suggests that no code was required to make changes. Call it whatever you like, we just want to make it clear that you don’t need to be a developer to customize or create PowerApps apps.  
  
PowerApps provides a set of web services and APIs that allow developers to write code. When code is written using supported methods you can expect that it will continue to work when you upgrade your organization.  
  
<a name="BKMK_SupportedCust"></a>   
## What kinds of customizations are supported?  
 We expect that you can do most of your customization with the tools in the application. Everything you do by using those tools is supported by Microsoft because they apply changes to the metadata or data that depends on the metadata.  
  
 If the customization tools don’t meet your needs, you can install a solution provided by a third party or hire a developer to code your customizations. Either way, it’s good for you to understand supported customizations. If you need to invest in a solution that requires code, you should make sure that the code is written using only supported APIs. This helps you protect your investment in both the apps and any solutions you get.  
  
 Developers who extend PowerApps apps have a responsibility to follow rules and best practices documented in the SDK: [Best practices for developing with Dynamics 365 Customer Engagement](https://docs.microsoft.com/dynamics365/customer-engagement/developer/best-practices-sdk). The SDK documents the APIs available to developers and provides guidance about how to best use them. Microsoft supports only the APIs and practices that are documented in the SDK. You may find something on the Internet that describes how you can solve a problem, but if it doesn’t leverage APIs documented in the SDK, it isn’t supported by Microsoft. Before you have a developer apply a change you should verify whether it uses supported methods.  
  
 If developers use the APIs and best practices described in the SDK we can be sure to test whether any of the changes we make to PowerApps has the potential to break existing customizations. Our goal is that code customizations written using supported methods will continue to work when new versions or updates to PowerApps  are released. You benefit because you can upgrade to new versions with improved features without having developers change their code each time.  
  
 If we detect that a change in a new version of PowerApps will cause a supported customization to break, we will document what is affected and how people can change their code to fix it.  
  
<a name="BKMK_Unsupported"></a>   
## What kinds of customizations aren’t supported?  
 Just because certain APIs and programming practices aren’t supported by Microsoft doesn’t mean that they don’t work. “Unsupported by Microsoft” means exactly what it says: you can’t get support about these APIs or programming practices from Microsoft. We don’t test them and we don’t know if something we change will break them. We can’t predict what will happen if someone changes code in our application.  
  
 The developer who uses unsupported APIs and programming practices assumes the responsibility to support their code. They will need to test their code to make sure it works.  
  
 If you choose to use unsupported customizations in your PowerApps environment you should be sure to document what was done and have a strategy to remove those customizations before you contact Microsoft Technical Support. If you need help with unsupported customizations, contact the developer or organization who prepared the customizations.  
  
<a name="BKMK_CommonUnsupportedCustomizations"></a>   
### Common unsupported customization practices  
 The following is a list of common customization practices that aren’t supported. This is not a complete list. More information: [Supported extensions for Dynamics 365: Unsupported customizations](https://docs.microsoft.com/dynamics365/customer-engagement/developer/supported-extensions#Unsupported). 
 
**Interacting with the web application Document Object Model (DOM) elements using JavaScript**  
 Any JavaScript libraries used anywhere in the application must only interact with the documented APIs. When JavaScript developers work with applications they frequently access DOM elements using specific names. Because PowerApps apps are web applications these techniques work, but they are likely to break during an update because the names of the elements they reference are subject to change at any time. We reserve the right to make any changes necessary in the application and this frequently means changing how the page is constructed. Adding any changes that depend on the current structure of the page means that you’ll need to invest in testing and perhaps changing the custom code in these scripts each time you apply an update to your application.  
  
 jQuery is a very common library used by JavaScript developers. Most of the benefit of using jQuery is that it simplifies a developer’s ability to access and create DOM elements, which is exactly what we do not support in the PowerApps application pages. jQuery is recommended when developers are creating custom user interfaces with HTML web resources, but within the PowerApps application pages, the supported APIs do not require jQuery to be used.  
  
 **Using any undocumented internal objects or methods using JavaScript**  
PowerApps uses many JavaScript objects within pages. A JavaScript developer can discover these objects by debugging a page and then access and reuse these objects. We reserve the right to make any changes necessary to these objects, including removing them or changing the names of the methods. If a script references these objects, the script will break if they are not found.  <a name="BKMK_Metadata"></a>   
 
<a name="BKMK_CombineCustomizations"></a>   
## Combine customization capabilities  
 Each of the topics in this guide describe individual customization capabilities in considerable depth. But it’s important to keep in mind that the solutions to meeting your business requirements will frequently use one of the capabilities together with one or more other capabilities.  
  
<a name="BKMK_ChooseTheRightCustomization"></a>   
### Choose the right customization capability for the job  
 The law of instrument states “If all you have is a hammer, everything looks like a nail.” With all the different customization capabilities available in PowerApps it’s easy to become familiar with one of them and seek to use it to solve every problem. As you evaluate the business problems you want to solve, think about the end result you want to achieve and then work backwards to how you can get there.  
 
<a name="BKMK_changesinperformance"></a>   
## Changes that affect PowerApps environment performance  
 Importing solutions and applying customizations that change metadata can affect PowerApps environment performance. Actions that can interfere with normal system operation include:  
  
-   Add, remove, or change entities, alternate keys, attributes, or relationships.   
  
-   Import solutions
  
-   Publishing customizations 
  
If you’re applying these changes to a production system, we recommend that you schedule these operations when it is least disruptive to users.   
  
  
## Next Steps  
[Overview of building a model-driven app](../model-driven-apps/model-driven-app-overview.md)
