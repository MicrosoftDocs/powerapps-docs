---
title: Select the best fields to display with Copilot in Power Apps
description: Learn how to use field suggestions by Copilot, an AI feature in Power Apps, to select the best fields to display when you link a data source to a control in a canvas app.
author: norliu
ms.author: norliu
ms.date: 5/7/2024
ms.topic: conceptual
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

# Select the best fields to display with Copilot in Power Apps

Copilot is an AI feature in Power Apps that helps you select the best fields to display when you link a data source to a control in a canvas app. Instead of using the default fields that Power Apps selects, you can view up to 10 suggestions from Copilot. The field suggestions are based on the data schema and the context of the app. You can review the suggestions and make adjustments as needed, saving time and improving the quality of the app.

## Prerequisites

- Meet the prerequisites for Copilot in Power Apps features. Learn more in [Create conversational apps with Copilot in Power Apps](ai-overview.md).

- Make sure this feature is available in your region. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).

- Turn on Copilots in your region. Learn more in [Turn on copilots and generative AI features](/power-platform/admin/geographical-availability-copilot).

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

When you're done, apply the changes and view the results in your app.

## Related information

- [FAQs for field suggestions by Copilot](../common/faq-field-suggestions.md)
