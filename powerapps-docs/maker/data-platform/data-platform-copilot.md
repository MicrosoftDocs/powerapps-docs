---
title: Improve copilot responses from Microsoft Dataverse
description: Find out how to get more precise and relevant answers from copilots that use your data in Microsoft Dataverse.
author: mattp123
ms.topic: overview
ms.collection: bap-ai-copilot
ms.date: 05/29/2025
ms.update-cycle: 180-days
ms.reviewer: matp
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
searchScope:
  - "Power Apps"
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-title
  - ai-gen-desc
  - ai-seo-date:
ai-usage: ai-assisted
---

# Improve copilot responses from Microsoft Dataverse

Copilot experiences in Dynamics 365 apps, apps in Power Apps, or Microsoft 365 Copilot allow users to ask natural language questions about data that's stored in Dataverse. Copilots help your users get insights and information from your enterprise data, which improves their productivity and decision-making. However, sometimes they might not get the answers they expect or need from copilots. This article shows you how to improve the accuracy and relevance of copilot answers by using Microsoft Copilot Studio and the record picker.

## Prerequisites for using copilots with Dataverse

By default, the Copilot feature for app users in model-driven apps is turned off. Admins must enable this feature for their environments in the Power Platform admin center. Learn more: [Turn on copilots and generative AI features](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)

## Improve results for Dataverse using knowledge sources in Copilot Studio

As a maker, you know how your data is structured and how your users ask questions about it. To improve the quality of the results, you can teach the copilot some domain knowledge, also known as *grounding*, using synonyms and phrases with definitions. This information helps the copilot understand how your users ask questions that don't match the names or values of the tables or columns in your data.

For example, if your users ask "What are my closed leads?" and the results depend on a column that doesn't include "closed" or a status that doesn't have "closed" in the definition, the results might be imprecise. If your company defines a closed lead as a status of not qualified or canceled, you can add a glossary term that defines "closed leads" as "lead status isn't qualified or canceled." This additional information helps the copilot understand your users' questions better.

Teach your copilot domain knowledge by adding a knowledge source in Copilot Studio to make its answers more relevant and informative for your users. You can add enterprise data from Power Platform, Dynamics 365, and external systems as knowledge sources. You can also add Dataverse data as a knowledge source. Learn more: [Add knowledge to a copilot](/microsoft-copilot-studio/knowledge-add-existing-copilot#dataverse)

## Improve answers for a specific record using a copilot in an app

In Power Apps model-driven apps and Dynamics 365 Sales, users can use the record picker to improve their results. The record picker lets you choose a record to use as the object of your question. This helps you get better answers when the results include records from different tables or records that aren't what you wanted.

To open the record picker, type `/`. Then type the name of the record you want. Learn more: [Use Copilot chat in model-driven apps](../../user/use-copilot-model-driven-apps.md#use-the-record-picker)

## Related information

- [Copilot in Power Apps overview](../canvas-apps/ai-overview.md)
- [FAQ for Copilot in model-driven apps](../common/faqs-copilot-model-driven-app.md)
- [FAQ about using AI responsibly in Power Apps](../common/responsible-ai-overview.md)
