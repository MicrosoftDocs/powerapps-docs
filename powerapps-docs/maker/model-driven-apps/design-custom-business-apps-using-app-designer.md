---
title: "Design model-driven apps by using the app designer | MicrosoftDocs"
description: Learn how to design model-driven apps
ms.custom: intro-internal
ms.date: 06/27/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - PowerApps
ms.assetid: aa6aca00-f95a-4f06-bec4-18b427b4618c
ms.subservice: mda-maker
ms.author: matp
manager: kvivek
author: Mattp123
caps.latest.revision: 17
topic-status: Drafting
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Design model-driven apps using the classic app designer

With Power Apps, model-driven apps are comprised of components such as [tables](model-driven-app-glossary.md#table), [forms](model-driven-app-glossary.md#form), [views](model-driven-app-glossary.md#view), [dashboards](model-driven-app-glossary.md#dashboard) and [business process flows](model-driven-app-glossary.md#business-process-flow).  

As the model-driven apps have evolved so too have the ways in which the various elements are edited.  This article describes the method of creating an app using the classic app designer.

> [!TIP]
> Use the modern app designer to build your apps. More information: [Create a model-driven app using the app designer](create-model-driven-app.md)
  
The [app designer](model-driven-app-glossary.md#app-designer) helps all these components to be brought together quickly. Its tile-based information structure and simplified interface make the process of building an app much easier, and apps that are specific to business roles and functions can be brought together without having to write any code.  
  
Each app that you create can have its own [site map](model-driven-app-glossary.md#site-map) with the integrated and easy-to-use site map designer.  Just drag and drop [areas](model-driven-app-glossary.md#area), [group](model-driven-app-glossary.md#group), and [subareas](model-driven-app-glossary.md#subarea) to the canvas. Components that you select in the site map are also added as tables in the app designer.  
  
[Tables](model-driven-app-glossary.md#table) can be added and removed as necessary, and also add other components.  
  
Once [components](model-driven-app-glossary.md#component) have been added, the app can be validated to confirm that all components have been added correctly.
  
The following table shows the steps required to create an app and assumes that all the necessary [tables](model-driven-app-glossary.md#table), [forms](model-driven-app-glossary.md#form), [views](model-driven-app-glossary.md#view), [dashboards](model-driven-app-glossary.md#dashboard) and [relationships](model-driven-app-glossary.md#relationship) have been created within the environment in advance.
  
|Step|Description|Related topics|  
|----------|-----------------|--------------------|  
|![Step 1.](media/walkthrough-green-1.png "Step 1")|Define app properties.|[Create or edit an app](create-edit-app.md)|  
|![Step 2.](media/walkthrough-green-2.png "Step 2")|Define navigation for an app using the site map designer.|[Create a site map for an app](create-site-map-app.md)|  
|![Step 3.](media/walkthrough-green-3.png "Step 3")|Apps are composed of components like dashboards, tables, business process flows, forms, views, and charts. Include the required ones in your app by using the app designer.|[Add or edit app components](add-edit-app-components.md)|  
|![Step 4.](media/walkthrough-green-4.png "Step 4")|Check the app for any required components that have not been added. After all required components are added make the app available for use. |[Validate and publish an app](validate-app.md)|  
|![Step 5.](media/walkthrough-green-5.png "Step 5")|Give users access to the data within the apps created by using security roles.|[Share a model-driven app](./share-model-driven-app.md)|  
  
## Supported web browsers

For information about the supported web browsers to use with the app designer and site map designer, see [Supported web browsers and mobile devices](/power-platform/admin/supported-web-browsers-and-mobile-devices).  
  
### Next steps

 [Build your first model-driven app from scratch](./build-first-model-driven-app.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]