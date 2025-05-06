---
title: "Model-driven app interface design overview | MicrosoftDocs"
description: "An overview of the elements that influence the app design interface"
ms.date: 04/22/2025
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: overview
applies_to: 
    - "powerapps"
author: "Mattp123"
ms.assetid: 
caps.latest.revision: 1
ms.subservice: mda-maker
ms.author: matp
tags: 
search.audienceType: 
  - maker
---
# Model-driven app interface design overview

Model-driven app interface design includes working with table [views](model-driven-app-glossary.md#view) and [forms](model-driven-app-glossary.md#form). To work with these components in your app, you create [pages](model-driven-app-glossary.md#page).

Creating pages in a model-driven app builds the app [site-map](model-driven-app-glossary.md#site-map) that describes the navigation experience within the app.

App interface design can include changing the command bar menu in an app.

This article mentions the classic approach to developing apps. This includes the creation of apps in addition to working with forms, views, and other elements.

## Model-driven app design

Here's an overview of the model-driven app design process.

Designing a model-driven app requires a range of skills. There are many [design tools](model-driven-designers.md) that enable a model-driven app to be created. At times the app maker plays the role of a database designer, a user experience customizer, and even a process designer.

Model-driven apps are essentially a selection of Microsoft Dataverse [components](model-driven-app-glossary.md#component) (tables, charts, dashboards) that work alongside each other to achieve a business outcome. These components are delivered in conjunction with the Dataverse [security roles](model-driven-app-glossary.md#security-role) to create a user experience that meets the needs of members of different parts of an organization.

This means that the same app can be used by colleagues in different departments. In some cases, users only want to review data and might only have interest in specific areas in order to complete their daily objectives.

The design of tables and table columns is covered under a documentation dedicated to this article. [Learn more about creating Dataverse tables](../../maker/data-platform/entity-overview.md).

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

### See also

[Learn more about Dataverse security roles](/power-platform/admin/security-roles-privileges)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
