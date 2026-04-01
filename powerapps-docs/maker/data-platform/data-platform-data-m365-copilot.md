---
title: Dataverse data in Microsoft 365 Copilot
description: Understand how Microsoft Copilot searches and reasons over Microsoft Dataverse table data used by model-driven and canvas apps in Power Apps.
#customer intent: Learn about how Microsoft Copilot searches and reasons over Microsoft Dataverse table data.
author: paulliew
ms.author: paulliew
ms.reviewer: matp
ms.date: 04/01/2026
ms.topic: concept-article
ms.service: power-platform
ms.subservice: dataverse
---
# Dataverse data in Microsoft 365 Copilot

Dataverse is the data platform for Power Apps and Microsoft 365 Copilot can search and reason over Dataverse table data used by model-driven and canvas apps.

When your business data is stored in Dataverse tables, Microsoft 365 Copilot can retrieve relevant rows and related records and use them to answer questions or summarize information in natural language.

These are the supported experiences with Microsoft 365 Copilot and Dataverse:

- Microsoft 365 Copilot Chat (main chat): Ask questions across Dataverse data, summarize records, and identify trends using natural language.
- Power Apps (sidecar): Get help while working in model-driven or canvas apps—for example, find records, understand related data, and summarize what matters.
- Outlook: Draft and review customer emails with relevant Dataverse context, such as account details and open items.
- Microsoft Word: Turn Dataverse data into structured content like customer briefs, status updates, and summaries.

## How it works

At a high level, here's how Dataverse data n Microsoft 365 Copilot works:

1. You ask Copilot a question in a supported Microsoft 365 experience.
1. Copilot searches the Dataverse tables you have access to.
1. Copilot uses table relationships to bring in relevant related records, such as lookups columns.
1. Copilot returns a response grounded in Dataverse data, such as a summary, list, or explanation.

## Example prompts

- “Show me my highest-priority open cases.”
- “Summarize this account’s recent activity and open items.”
- “Which opportunities are at risk this month, and why?”
- “Draft a customer update email based on the latest case status.”
- “Create a one-page customer brief for this account.”

## Considerations

- Copilot only returns Dataverse data that the user is authorized to access.
- Results depend on data quality and how tables and relationships are modeled.
- Use clear, specific prompts SUCH AS table/entity, timeframe, and status, to get more precise answers.

These are to be added in the [What is Dataverse intelligence? - Power Apps \| Microsoft Learn](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-intelligence) 

Dataverse data in Microsoft 365 Copilot

Microsoft 365 Copilot can use Dataverse data to help users find information and take action with natural language across Microsoft 365 experiences.

Dataverse table data from Power Apps (model-driven and canvas apps) can be searched and reasoned over in Microsoft 365 Copilot. Copilot can find relevant rows and related records, interpret table relationships, and summarize or answer questions based on your data.

## Business skills

Business skills help makers and users interpret data, improve processes, and make decisions. Intelligence experiences can support key skills like problem framing, requirements discovery, communicating insights, and iterating with stakeholders.

## Related articles

[What is Dataverse intelligence?](/power-apps/maker/data-platform/data-platform-intelligence)
