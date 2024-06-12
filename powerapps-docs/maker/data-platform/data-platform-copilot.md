---
title: Improve copilot responses from Microsoft Dataverse
description: Overview about how to improve copilot responses from Microsoft Dataverse.
author: mattp123
ms.topic: overview
ms.collection: bap-ai-copilot
ms.date: 09/08/2023
ms.reviewer: matp
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
searchScope:
  - "Power Apps"
---
# Improve copilot responses from Microsoft Dataverse

Users across your organization expect copilots to answer questions about data they access and use every day, which drives your business and improves productivity for tasks. Getting accurate and highly relevant answers to questions about enterprise data in copilots is more important than ever as your users interact with copilots powered by Microsoft Copilot Studio, Power Apps, Teams, and Microsoft Copilot for Microsoft 365.

Copilot experiences in Dynamics 365 apps, apps in Power Apps, or Microsoft Copilot for Microsoft 365, provide users with the ability to ask natural language questions about their data stored in Dataverse. Many of the questions can easily be answered and copilot uses Dataverse for questions about the data. However, copilot currently doesn't support directly creating, updating, or deleting table data. More information: [Known limitations](../model-driven-apps/add-ai-copilot.md#known-limitations)

## Prerequisites for using copilot with Dataverse

The copilot for app users in model-driven apps feature isn't enabled by default. Administrators must manually enable this feature for their environments in Power Platform admin center. More information: [Turn on copilot and generative AI features](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)

## Improve results for Dataverse using knowledge sources in Microsoft Copilot Studio

Knowledge in Microsoft Copilot Studio allows you to add enterprise data from various sources including Power Platform, Dynamics 365 data, and external systems. By adding a knowledge source, your copilots provide relevant information and insights for your end users. Knowledge with Dataverse data can be added to a Copilot in Microsoft Copilot Studio. 

As a maker, you know the shape of your data and how your users ask questions for your organization and company. To improve the quality of the results, you help ground the copilot with definitions that require a much more complex configuration than just a simple rephrase of a question. With Dataverse as a knowledge source in Copilot Studio, you tune your copilot to understand domain knowledge using synonyms for columns in a table and you can add phrases with definitions that help tune your copilot to understand how users ask questions. For example, if your users ask a question like “What are my closed leads” and the results are based on a column that doesn't include *closed* or a status that doesn't have *closed* in the definition the results could be imprecise. If your company defines a closed lead as status not qualified or canceled, you can add a glossary term that defines "closed leads" to mean "lead status isn't qualified or canceled."  This helps copilot understand how your users ask questions that aren't easily mapped to a table or column in your data. Learn more about configuring and using [Dataverse tables in Microsoft Copilot Studio with knowledge](/microsoft-copilot-studio/knowledge-add-existing-copilot#dataverse).

## Improve answers for a specific record in an app using a copilot

With copilot chat in Power Apps model-driven apps and Dynamics 365 Sales, users can improve results by picking the record they want to use with record picker. Record picker helps users get better answers when the results return records across different tables or return records that aren't what they expected. Type "/" to open the record picker and continue typing the name of the record. More information: [Record picker to select object of the question](../../user/use-copilot-model-driven-apps.md#record-picker-to-select-object-of-the-question)

## See also

[Copilot in Power Apps overview](../canvas-apps/ai-overview.md)

[FAQ for Copilot in model-driven apps](../common/faqs-copilot-model-driven-app.md)

[FAQ about using AI responsibly in Power Apps](../common/responsible-ai-overview.md)
