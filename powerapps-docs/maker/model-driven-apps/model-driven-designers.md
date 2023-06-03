---
title: "Model-driven-designers | MicrosoftDocs"
description: "Model-driven app designers"
ms.collection: get-started
ms.date: 09/27/2021
ms.reviewer: ""

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
    - "powerapps"
author: "matp"
ms.assetid: 
caps.latest.revision: 1
ms.subservice: 
ms.author: "matp"
tags: 
search.audienceType: 
  - maker

---
# Meet the model-driven app designers

In order to fully develop a model-driven app, multiple designers are required at different stages in the development process.

Broadly speaking, app development breaks down into the following stages:

- Data model development
- App development
- Data security

Assets created, such as tables, cloud flows, or model-driven apps, have the capacity to be held inside [solutions](model-driven-app-glossary.md#solution) to enable secure [application lifecycle management](model-driven-app-glossary.md#application-lifecycle-management).

This article focuses on the first two stages. For more information about data security, go to [Security in Microsoft Dataverse](/power-platform/admin/wp-security)

>[!NOTE]
> It isn't necessary to use all the editors to create a model-driven app.  As a minimum, concentrate on the table column editor, form designer, and view designer in addition to adding any required relationships. Then use the app designer to pull the components of the app together.

## Data-model development

The value of model-driven apps centers around having a strong, secure, reusable data-model. Once the data-model is in place, the process of developing the app is straightforward.

### The table designer, and related designers

Development of the data-model starts with using the table designer.  A table is a significant artifact of a model-driven app. There is a table designer, which defines the table structure, and includes access to the other designers for relationships, views, forms, and so on.

The table designer is shown below.
:::image type="content" source="media/table-designer.png" alt-text="Sample model-driven app":::

The following table describes the designers, what they do, and provides links about how to open them.

|Editor|Description|Link|
|--------------|---------------|---------------|
|**Table designer**|Tables hold record metadata in columns for a wide range of data types such as text, email, image, currency, and more. Many standard tables are available. You can customize a non-system standard table. You can also create a new custom table from scratch.<br>The table designer is effectively an entry point to the other designers, such as view and form.  In many cases, the designers are native to the table designer and in others a new browser tab opens where editing can take place.<br>The columns area of the table designer allows the developer to define the table columns.|[Create a custom table](../../maker/data-platform/data-platform-create-entity.md)
|**Relationships**|Part of the table designer. Relationships are fundamental to the operation of any model-driven app.  Without them all tables are isolated.  |[Create a relationship](../../maker/data-platform/data-platform-entity-lookup.md)
|**Business rule designer**| A separate designer accessed via the table designer. Business rules apply rules or recommendation logic to a form to set column requirements, hide columns, validate data, and more. App designers use a simple interface to implement and maintain fast-changing and commonly used rules.|[Create a business rule for a table](../../maker/data-platform/data-platform-create-business-rule.md)
|**View designer**|Part of the table designer. Views are tied to the table and present table data in columns by selecting, positioning, and filtering them.|[Create a view](create-edit-views-app-designer.md)  
|**Form designer**|A separate designer accessed via the table designer. Forms allow users to interact with data held in table records.|[Create a form](create-and-edit-forms.md)
|**Dashboard designer**|A separate designer accessed via the table designer. Used to create and edit dashboards presenting different data visualizations, such as embedded Power BI reports, data charts, and views.|[Create a dashboard](create-edit-dashboards.md)
|**Chart designer**|A separate designer used to create table charts.|[Create a system chart](create-edit-system-chart.md)
|**Business process flow designer**|Business process flows walk users through a standard business process. <br>While they are a part of the solution, they are created using Power Automate.|[Create a business process flow](/power-automate/create-business-process-flow)

## Business logic development

Business logic can be introduced in the form of business rules and business process flows.

In addition, Power Automate cloud flows can be used in a model-driven app that leverage cloud flow functionality, which can access hundreds of data connectors, not just Dataverse.

[Learn more about using Power Automate with Dataverse ](/power-automate/dataverse/overview)

## App designer

The app designer is the tool that is used to create the app and to configure the tables used in the app. It is important to understand that the quality of the app has much less to do with the edits performed at this stage than those using the other designers.

Makers can choose the views, forms, charts, and dashboards relevant to the app in development.

[Create an app using the app designer](create-model-driven-app.md)

<!-- :::image type="content" source="media/app-designer-form-component-properties.png" alt-text="App designer":::

When you create a model driven app for the first time a developer will need to create a **Sitemap** using the relevant designer.


## Sitemap designer

The site map designer allows a developer to choose the tables used in the app and arrange them into Areas (1), Groups (2) and Subareas (3).  These are then further configured using the app designer.

   :::image type="content" source="media/site-map-designer-demo.png" alt-text="Site map designer":::

[Learn about configuring a site map](create-site-map-app.md)  -->

## Next steps

[Steps to building a model-driven app](app-building-steps.md)

[Build your first model-driven app](build-first-model-driven-app.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
