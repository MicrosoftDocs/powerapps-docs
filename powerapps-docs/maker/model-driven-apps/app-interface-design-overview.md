---
title: "Model-driven app interface design overview | MicrosoftDocs"
description: "An overview of the elements that influence the app design interface"
ms.custom: intro-internal
ms.date: 11/16/2021
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
    - "powerapps"
author: "v-roryneary"
ms.assetid: 
caps.latest.revision: 1
ms.subservice: 
ms.author: v-roryneary
manager: ""
tags: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps

---

# Model-driven app interface design overview

## Introduction

In this section we will explore how to work with table [views](model-driven-app-glossary.md#view) and [forms](model-driven-app-glossary.md#form) in some detail.  

We will discover that there are 2 experiences available when building apps.  The first, and more recent experience, involves the creation of [pages](model-driven-app-glossary.md#page).  The second experience involves building an app in a more deliberate fashion.

In both cases the same product is created, a model-driven app with a [site-map](model-driven-app-glossary.md#site-map) associated with it that describes the navigation experience within the app.

Additionally, we will discover a method of changing the command bar menu in our apps.  Finally we retain details on the classic approach to developing apps.  This describes the creation of apps in addition to working with forms, views and other elements.

Before we do this a reminder of the model-driven app design process may be helpful.

## Model-driven app design recap

Designing a model-driven app requires a range of skills and there are a number of [design tools](model-driven-designers.md) that enable them to be created.  At times the developer plays the role of a **database designer**, a user experience **customizer** and even a **process designer**.

Model-driven apps are essentially a selection of Dataverse [components](model-driven-app-glossary.md#component) (tables, charts, dashboards) that work alongside each other to achieve a business outcome.  These components are delivered in conjunction with the Dataverse [security roles](model-driven-app-glossary.md#security-role) to create a user experience that meets the needs of members of different parts of an organization.

This means that the same app can be used by a colleagues different departments.  In some cases users will only wish to review data and may only have interest in specific areas in order to complete their daily objectives.

The design of tables and table columns is specifically covered under a documentation dedicated to this topic.  [Learn more about creating Dataverse tables](../../maker/data-platform/entity-overview.md).

## App interface design resources

The following table describes the resources in this section.

|Title|Detail|Link|
|-----|------|----|
|Use the modern app designer|An overview of the most recent experience for building model-driven apps|[Learn more](app-designer-overview.md)|
|Use the classic app designer|How to create an app using the classic method|[Learn more](create-edit-app.md)|
|Working with views|How to create or edit table views|[Learn more](create-edit-views.md)|
|Working with forms|How to create or edit forms|[Learn more](create-design-forms.md)|
|Use custom pages with model-driven apps|How to understand and work with custom pages|[Learn more](model-app-page-overview.md)|
|Customize app commands|Discover how to ensure that the customize the menu in the top rail of a model driven app|[Learn more](command-designer-overview.md)
|Using the classic designers|Discover the classic method of creating model-driven apps|[Learn more](design-custom-business-apps-using-app-designer.md)

### See also

[Learn more about Dataverse security roles](https://docs.microsoft.com/power-platform/admin/security-roles-privileges)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]