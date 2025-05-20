---
title: Use Copilot case summary in model-driven apps
description: Learn how to view copilot case summary in model-driven apps.
author: gandhamm
ms.author: mgandham
ms.reviewer: gandhamm
ms.topic: how-to
ms.collection: 
ms.date: 04/11/2025
ms.custom: bap-template 
---

# Use Copilot case summary in model-driven apps

Copilot case summaries help users quickly understand the context of a case and resolve customer issues more efficiently. The case summary includes key information such as the case title, customer, subject, product, priority, case type, and description.

## View case summary card

Copilot case summary is enabled by default for all model-driven apps that use the **incident** table. When you open a case record, the case summary card appears. The card is collapsed by default. When you expand the card, Copilot generates and displays the case summary.

Based on the case form configured, users see the summary either on the top of the case form or within the form.
> [!NOTE]
> Users won't see case summary cards on case forms 
> - By default, if their organization has opted out of the automatic enablement of Copilot feature.
> - If case summary is disabled in the experience profile.

- Users can see the case form displayed on the top of all case forms except **Case for Interactive experience**, **Enhanced full case form**, **Case**, and **Case for Multisession experience** forms. Users can copy the summary, refresh it, regenerate the summary, and provide feedback.

   :::image type="content" source="media/copilot-case-summary.png" alt-text="Screenshot that shows the Copilot case summary on a model driven app.":::

- Users can see the case form displayed within the case form for **Case for Interactive experience**, **Enhanced full case form**, **Case**, and **Case for Multisession experience** forms. Users can copy the summary, translate the summary into multiple languages, refresh it, regenerate the summary, and provide feedback.

    :::image type="content" source="media/copilot-case-summary-default.png" alt-text="Screenshot that shows the default Copilot case summary on a model driven app.":::

- If [custom record summary](/dynamics365/customer-service/administer/copilot-enable-custom-record-summaries) is enabled, users see the custom record displayed on top of the form by default. 
