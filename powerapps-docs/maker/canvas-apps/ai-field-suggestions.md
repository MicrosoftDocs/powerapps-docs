---
title: How to use field suggestions by Copilot in Power Apps Studio
description: Use field suggestions by Copilot in Power Apps Studio.
author: norliu
ms.topic: conceptual
ms.custom: canvas
ms.collection: 
    - bap-ai-copilot
    - get started
ms.reviewer: mkaur
ms.date: 5/7/2024
ms.subservice: canvas-maker
ms.author: norliu
search.audienceType: 
  - maker
contributors:
  - mduelae
  - norliu
---

# Use field suggestions by Copilot

Use field suggestions by Copilot to select the best fields to display when you link a data source to a control in a canvas app. Instead of using the default fields that Power Apps selects, makers can view up to 10 suggestions from Copilot. The field suggestions are based on the data schema and the context of the app. An app maker can review the suggestions and make adjustments as needed, saving time and improving the quality of the app.

## Prerequisites

- Prerequisites for Copilot in Power Apps features: [Copilot in Power Apps overview (preview)](ai-overview.md)
- See if this feature is available in your region: [Product availability report](https://releaseplans.microsoft.com/en-US/availability-reports/?report=productgeoreport)
- Learn how to turn on Copilots in your region: [Turn on copilots and generative AI features](/power-platform/admin/geographical-availability-copilot)

## Use field suggestions

Field suggestions by Copilot work when you bind a data source to one of the following controls: 

- Gallery
- Form (modern)
- Table (modern)
- Edit form (classic)
- Display  form (classic)
- Data table (classic)

Supported data sources:

- Dataverse
- Structured query language (SQL)
- SharePoint list

When you select a data source for a control, Copilot analyzes the data schema and recommends up to 10 fields that are relevant and meaningful for your app. If you have more than 10 required fields, Copilot merges the AI suggestions together with the required fields so you don't get an error when you submit a form. You can view the suggestions in the **Fields** pane and preview how it looks in your app. You can also adjust the orders, remove fields, and add more fields from the data source. When you're done, apply the changes and view the results in your app.


## See also
- [FAQs for field suggestions by Copilot](../common/faq-field-suggestions.md)