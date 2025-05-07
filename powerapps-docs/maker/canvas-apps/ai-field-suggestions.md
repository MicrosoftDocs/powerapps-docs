---
title: Use field suggestions by Copilot
description: Learn how to use field suggestions by Copilot, an AI feature in Microsoft Power Apps, to select the best fields to display when you link a data source to a control in a canvas app.
author: norliu
ms.author: norliu
ms.date: 4/16/2025
ms.topic: article
ms.reviewer: mkaur
ms.subservice: canvas-maker
ms.collection:
  - bap-ai-copilot
  - get started
search.audienceType:
  - maker
contributors:
  - mduela
  - norliu
ai-usage: ai-assisted
ms.custom: 
  - ai-gen-diyeditor
  - canvas
---

# Use field suggestions by Copilot

Copilot is an AI feature in Microsoft Power Apps that helps you select the best fields to display when you link a data source to a control in a canvas app. Instead of using the default fields that Power Apps selects, you can view up to 10 suggestions from Copilot. The field suggestions are based on the data schema and the context of the app. You can review the suggestions and make adjustments as needed, saving time and improving the quality of the app.

## Prerequisites

Ensure you meet the prerequisites and region availability in [Copilot in Power Apps overview (preview)](ai-overview.md).

## Use field suggestions

Field suggestions by Copilot work when you bind a data source to one of the following controls:

- Gallery
- Form (modern)
- Table (modern)
- Edit form (classic)
- Display form (classic)
- Data table (classic)

You can bind these controls to one of the following data sources:

- Dataverse
- SQL Server
- SharePoint list

When you select a data source for a control, Copilot analyzes the data schema and recommends up to 10 fields that are relevant and meaningful for your app. If you have more than 10 required fields, Copilot combines the AI suggestions with the required fields so that you don't get an error when you submit a form.

You can view the suggestions in the **Fields** pane and preview how they look in your app. You can also adjust the order, remove fields, and add more fields from the data source.

:::image type="content" source="media/artificial-intelligence/fields-pane.png" alt-text="Screenshot that shows you where you can view the fields pane from the Properties pane.":::

When you're done, apply the changes and view the results in your app.

## Related information

- [FAQs for field suggestions by Copilot](../common/faq-field-suggestions.md)
