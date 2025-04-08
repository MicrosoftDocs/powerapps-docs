---
title: Use Copilot case summary in model-driven apps
description: Learn how to view copilot case summary in model-driven apps.
author: gandhamm
ms.author: mgandham
ms.reviewer: gandhamm
ms.topic: conceptual e.
ms.collection: .
ms.date: 04/08/2025
ms.custom: bap-template 
---

# Use Copilot case summary in model-driven apps

Copilot case summaries help you quickly understand the context of a case and resolve customer issues more efficiently. The case summary includes key information such as the case title, customer, subject, product, priority, case type, and description.

## Key considerations

- Copilot case summaries are enabled by default in model-driven apps that use the **incident** table. However, this feature must be enabled by the administrator for the summary to appear in Customer Service workspace and Customer Service Hub. Learn more in [Enable case summaries](/dynamics365/contact-center/administer/copilot-enable-summary#enable-case-summaries).
- Copilot case summary is available by default on the all out-of-the-box and custom forms associated with the **incident** table except the following forms:
   - Case for interactive experience
   - Enhanced full case form
   - Case
   - Case for Multisession experience
- If case summary is already enabled for the forms in your model-driven app, we recommend that the administrator disable the case summary card on the form to avoid duplication.

## View case summary

Navigate to a case record in your model-driven app. The case summary appears as a card on the case form. When you open a case, the case summary card is collapsed by default so that your screen isn't cluttered with information. Select the card to expand the summary.

You can copy the summary, refresh it, regenerate the summary, and provide feedback.

:::image type="content" source="media/copilot-case-summary.png" alt-text="Screenshot that shows the Copilot case summary on a model driven app.":::