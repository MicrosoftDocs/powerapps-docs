---
title: Define data for your model-driven app in Power Apps | MicrosoftDocs
description: "Understand how to define data for your model-driven app"
Keywords: data, table, columns, relationship, attributes, model-driven app
ms.custom: intro-internal
author: Mattp123
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.subservice: mda-maker
ms.author: matp
manager: kvivek
ms.date: 06/27/2018
ms.service: powerapps
ms.topic: conceptual
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Define data for your model-driven app

Model-driven apps behave according to the nature of the data model that underpins them. This manifests itself to app users through [views](model-driven-app-glossary.md#view) of data housed within [tables](model-driven-app-glossary.md#table) and the [forms](model-driven-app-glossary.md#form) used to enter data into [records](model-driven-app-glossary.md#record) based on those tables.

In addition to editing table views and forms, [charts](model-driven-app-glossary.md#chart) and [dashboards](model-driven-app-glossary.md#dashboard) are also defined at the level of the table.

Finally, [business rules](model-driven-app-glossary.md#business-rule) allow organizations to ensure consistent business logic is applied to table records.

While it is possible to create a table without a business rule, chart or dashboard, it is not possible to design a meaningful one without a view or a form.

Finally, while [business process flows](model-driven-app-glossary.md#business-process-flow) are highly relevant to tables and the app user experience, they are not authored at the level of the table. Business process flows are created and managed using Power Automate.

The process of designing an app using the [app designer](model-driven-app-glossary.md#app-designer) in most instances comes **after** the data model has been prepared. However, an iterative approach is possible using the platform.

## How to define a data model

The data model for a model-driven app is defined in [Microsoft Dataverse](../data-platform/data-platform-intro.md). Power Apps model-driven apps can only be defined using Dataverse.

The apps data-model is defined using the following components: *table*, *column*, and *relationship*.  Once these have been created, then the forms and views can be developed further to meet the needs of the organization.

For detailed information about working with these components in Dataverse to define data for your model-driven app, go to the following articles:

|Component |Article|Note|
|-----|----|-----|
|Table| [Work with tables](../data-platform/entity-overview.md)|
|Column| [Work with columns](../data-platform/fields-overview.md)|
|Relationships| [Work with relationships](../data-platform/relationships-overview.md)|
|Business rule| [Create a business rule](create-business-rules-recommendations-apply-logic-form.md)
|Chart| [Create a chart](add-chart-to-form.md)
|Dashboard| [Build a dashboard](create-edit-dashboards.md)
|Business process flow|[Create a business process flow](/power-automate/create-business-process-flow)|Uses Power Automate designer|

## Next steps

[Learn about common column properties](../../maker/model-driven-apps/common-field-properties-legacy.md)

[Learn about configuring tables](../../maker/data-platform/entity-overview.md)

[Learn about creating and designing forms](../../maker/model-driven-apps/create-design-forms.md)

[Discover out more about views here](../../maker/model-driven-apps/create-edit-views.md)

[Build your first app](app-building-steps.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]