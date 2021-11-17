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

App interface design includes working with table [views](model-driven-app-glossary.md#view) and [forms](model-driven-app-glossary.md#form).  

There are two experiences available when you build apps. The first, and more recent experience, involves the creation of [pages](model-driven-app-glossary.md#page).  The second experience involves building an app in a more deliberate fashion.

In both experiences the same thing is created, a model-driven app with a [site-map](model-driven-app-glossary.md#site-map) associated with it that describes the navigation experience within the app.

Additionally, app interface design can include changing the command bar menu in an app.

This article mentions the classic approach to developing apps. This includes the creation of apps in addition to working with forms, views, and other elements.

## Model-driven app design

Here's an overview of the model-driven app design process.

Designing a model-driven app requires a range of skills. There are many [design tools](model-driven-designers.md) that enable a model-driven app to be created. At times the app maker plays the role of a database designer, a user experience customizer, and even a process designer.

Model-driven apps are essentially a selection of Dataverse [components](model-driven-app-glossary.md#component) (tables, charts, dashboards) that work alongside each other to achieve a business outcome. These components are delivered in conjunction with the Dataverse [security roles](model-driven-app-glossary.md#security-role) to create a user experience that meets the needs of members of different parts of an organization.

This means that the same app can be used by colleagues in different departments. In some cases, users will only want to review data and may only have interest in specific areas in order to complete their daily objectives.

The design of tables and table columns is covered under a documentation dedicated to this topic. [Learn more about creating Dataverse tables](../../maker/data-platform/entity-overview.md).

## App interface design resources

The following table describes the resources in this section.

|Title|Detail|Link|
|-----|------|----|
|Use the modern app designer|An overview of the most recent experience for building model-driven apps.|[Learn more](app-designer-overview.md)|
|Use the classic app designer|How to create an app using the classic method.|[Learn more](create-edit-app.md)|
|Working with views|How to create or edit table views.|[Learn more](create-edit-views.md)|
|Working with forms|How to create or edit forms.|[Learn more](create-design-forms.md)|
|Use custom pages with model-driven apps|How to understand and work with custom pages.|[Learn more](model-app-page-overview.md)|
|Customize app commands|Discover how to customize the command bar menu located near the top of a model-driven app.|[Learn more](command-designer-overview.md)
|Using the classic designers|Use the classic method of creating model-driven apps.|[Learn more](design-custom-business-apps-using-app-designer.md)

### See also

[Learn more about Dataverse security roles](https://docs.microsoft.com/power-platform/admin/security-roles-privileges)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]