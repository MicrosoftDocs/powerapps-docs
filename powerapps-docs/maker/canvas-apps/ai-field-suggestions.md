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

Field suggestion by Copilot is a feature designed for app makers. It assists in selecting the most suitable fields to display in your app when linking a data source to a control. Instead of using the default fields chosen by Power Apps, you can view up to 10 suggestions from Copilot. The field suggestions are based on the data schema and your app's context. You can review the suggestions and adjust as you need, saving you time and improving the quality of your app. 

## Prerequisites

- Prerequisites for Copilot in Power Apps features: [Copilot in Power Apps overview (preview)](ai-overview.md)
- See if this feature is available in your region: [Product availability report](https://releaseplans.microsoft.com/en-US/availability-reports/?report=productgeoreport)
- Learn how to turn on Copilots in your region: [Turn on copilots and generative AI features](/power-platform/admin/geographical-availability-copilot)

## Use field suggestions

Field suggestions by Copilot works when you bind a data source to one of the following controls: 

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

When you select a data source for a control, Copilot will analyze the data schema and recommend up to 10 fields that are most relevant and meaningful for your app. If you have more than 10 required fields, Copilot will merge the AI suggestions together with required fields, so you won’t get an error for submitting a form. You can see the suggestions in the fields pane and preview how they will look in your app. You can adjust their orders, remove fields and also add more fields from the data source if you need to. When you are happy with the selection, you can apply the changes and see the results in your app.

## See also
- [FAQs for field suggestions by Copilot](../common/faq-field-suggestions.md)
