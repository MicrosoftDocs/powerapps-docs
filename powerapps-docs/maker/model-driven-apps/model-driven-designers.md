---
title: "Model-driven-designers | MicrosoftDocs"
description: "Model-driven app designers"
ms.custom: intro-internal
ms.date: 09/27/2021
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
    - "powerapps"
author: ""
ms.assetid: 
caps.latest.revision: 1
ms.subservice: 
ms.author: ""
manager: ""
tags: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps

---
# Meet the Model-driven app designers

## Introduction

In order to fully develop a model-driven app multiple designers will be required at different stages in the development process.

Broadly speaking app development breaks down into the following stages

- data model development
- app development
- data security

All of the assets created whether they be tables, cloud flows or model-driven apps have the capacity to be held inside [solutions](model-driven-app-glossary.md#solution) to enable secure [application lifecycle management](model-driven-app-glossary.md#application-lifecycle-management).

This article focuses on the first two stages, however you can [learn more about security and security roles here](https://docs.microsoft.com/en-us/power-platform/admin/wp-security)

>[!NOTE]
> It is not necessary to use all the editors to create a model driven app.  As a minimum, concentrate on the table column editor, form designer and view designer in addition to adding any required relationships and using the app designer to pull the app together.

## Data-model development

The value proposition of model-driven apps centers around having a strong, secure, reusable data-model.

Once the data-model is in place the process of developing the app is relatively straightforward.

### The table designer, and related designers

Development of the data-model starts with using the table designer, however a table is a much more significant artifact than meets the eye.

To this end there is a master table designer which defines the table structure, and sub designers which include matters such as relationships, forms and views.

The table designer presents itself as shown below.
:::image type="content" source="media/table-designer.png" alt-text="Sample model-driven app":::

The following table describes the designers, what they do, and provide links as to how to get to them.

|Editor|Description|Link|
|--------------|---------------|---------------|
|**Table designer**|Tables are hold record metadata in **columns** in a wide range of data types such as Text, Email, Image, Currency and many more. Many standard tables are available. You can **customize** a non-system standard table. You can also create a new custom table from scratch.<br>The table designer is effectively a portal to the other designers, such as view and form.  In many cases the designers are native to the table designer and in others a fresh window will open where editing can take place.<br>The columns area of the table designer allows the developer to define the table columns.|[Create a custom table](../../maker/data-platform/data-platform-create-entity) 
|**Relationships**|Whilst this is not a full designer, relationships are fundamental to the operation of any model driven app.  Without them all tables are isolated|[Create a relationship](../../maker/data-platform/data-platform-entity-lookup)
|**Business rule designer**|Accessed via the table designer. Business rules apply rules or recommendation logic to a form to set column requirements, hide columns, validate data, and more. App designers use a simple interface to implement and maintain fast-changing and commonly used rules.|[Create a business rule for a table](../../maker/data-platform/data-platform-create-business-rule)
|**View designer**|Part of the table designer.  Views are tied to the table and present table data in columns by selecting, positioning and filtering them|[Create a view](create-edit-views-app-designer.md)  
|**Form designer**|Part of the table designer. Forms allow users to interact with data held in table records|[Create a form](create-and-edit-forms)
|**Dashboard designer**|A separated designer used to create dashboards presenting different data charts|[Create a dashboard](create-edit-dashboards.md)
|**Chart designer**|A separated designer used to create table charts|[Create a system chart](create-edit-system-chart)
|**Business process flow designer**|Business process flows walk users through a standard business process. <br>Whilst they are a part of the solution they are created using Power Automate.|[Create a business process flow](https://docs.microsoft.com/en-us/power-automate/create-business-process-flow)

## Business logic Development

Business logic can be introduced in the form of business rules and process flows.

In addition to this Power Automate cloud flows can be introduced in order to leverage both it's functionality in addition to the fact that it can access hundreds of data connectors, not just Dataverse.

[Learn more about using Power Automate with Dataverse ](https://docs.microsoft.com/en-us/power-automate/dataverse/overview)

## App designer

The App designer is the tool that is used to create the app and to configure the tables introduced by the **Sitemap designer**.  It is important to understand that the quality of the app has much less to do with the edits performed at this stage than those using the other designers.

Developers can choose the views, forms, charts and dashboards relevant to the app in development.

   :::image type="content" source="media/app-designer-form-component-properties.png" alt-text="App designer":::

When creating a model driven app for the first time a developer will need to create a **Sitemap** using the relevant designer.

[Create an app using the app designer](create-edit-app.md)

## Sitemap designer

The site map designer allows a developer to choose the tables used in the app and arrange them into Areas (1), Groups (2) and Subareas (3).  These are then further configured using the app designer.

   :::image type="content" source="media/site-map-designer-demo.png" alt-text="Site map designer":::

[Configure a site map](create-site-map-app.md)

## Next steps

[Build your first model-driven app](build-first-model-driven-app.md)

[Understanding the benefits of the model-driven approach](app-value-proposition.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]