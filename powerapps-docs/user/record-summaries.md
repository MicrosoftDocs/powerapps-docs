---
title: Use row summaries in model-driven apps 
description: Learn how to access and utilize AI-generated row summaries in main forms.
ms.date: 01/16/2025
ms.topic: article
ms.component: pa-user
ms.subservice: end-user
author: JasonGre
ms.author: JasonGre
ms.reviewer: smurkute
ms.collection: 
    - bap-ai-copilot 
search.audienceType: 
  - enduser
contributors:
---

# Use row summaries in model-driven apps
The **Row summary** feature in model-driven apps provides users with a concise, AI-generated overview of key details about a record (row). Summaries helps users quickly understand essential information without requiring you to manually scanning through fields, related records, or activity timelines. They are presented in either a paragraph or bullet point format, ensuring clarity and ease of consumption.

Summaries can be accessed in two ways:
- From the **Insights bar** at the top of main forms. 
- From view pages using the inline **Summary** action in the grid, which opens the summary for a record in a modal popup.

The feature enhances user efficiency by delivering context-rich insights directly within the form. Users can interact with summaries to copy content, regenerate updated information, and provide feedback on their relevance, improving both usability and accuracy.

> [!IMPORTANT]
> - This feature is in public preview for Dynamics 365 apps.
>   - Preview features aren’t meant for production use and might have restricted functionality.
>   - Preview features are available before an official release so that customers can get early access and provide feedback.

## Prerequisite
Copilot assistance is available for all model-driven apps where the [AI insight cards](/power-platform/admin/settings-features#ai-insight-cards-preview) toggle is turned on. 

## Limitations
Summaries are only currently supported in the English language.

## Feature details

### Accessing record summaries
You can view the record summary from either a form or a view when a [table has been configured to display summaries](../maker/data-platform/configure-form-row-summary.md#create-a-row-summary).

- **Forms**: When viewing a record in a main form, the summary appears in the Insights bar at the top of the main form.
  :::image type="content" source="media/row_summary_expanded.png" alt-text="Screenshot that shows a row summary card in the Insights bar on a form.":::

  [!NOTE] Record summaries only appear after a new record has been successfully saved. For unsaved records, the summary area remains hidden. 

- **Views**: When browsing records in a view, select the inline Summary action next to a record to open the summary in a modal popup.
  //Add image

### Interacting with summaries 
- **Copy**: Select the Copy button to copy the summary content directly to your clipboard for easy sharing or documentation. 
- **Feedback**: Use the thumbs up or thumbs down icons to rate the usefulness of the summary. This feedback helps improve future summary generation, ensuring future summaries better meet user expectations and needs.
- **Refresh** (forms only): Select the Refresh button to regenerate the summary content, ensuring it reflects the latest updates to the record. 
- **Expand/Collapse** (forms only): In forms, the Insights bar is collapsed by default, but shows a one-line peek of the summary. You can expand the Insights bar to see more details.
  :::image type="content" source="media/row_summary_collapsed.png" alt-text="Screenshot that shows a collapsed row summary."::: 

### Related information

[Manage feature settings](/power-platform/admin/settings-features)  
[Configuring summaries for tables](../maker/data-platform/configure-form-row-summary.md#create-a-row-summary)  
