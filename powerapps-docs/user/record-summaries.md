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
The **Row summary** feature in model-driven apps provides users with a concise, AI-generated overview of key details about a record (row). Displayed within the **AI assistance** area at the top of main forms, the summary helps users quickly understand essential information without manually scanning through fields, related records, or activity timelines. Summaries are presented in either a paragraph or bullet point format, ensuring clarity and ease of consumption.

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

### Viewing the record summary
- When a [table has been configured to display summaries](../maker/data-platform/configure-form-row-summary.md#create-a-row-summary), the record summary will appear in the **AI assistance** area at the top of the main form.
- The summary content is dynamically generated and presented in a clear paragraph or bullet point format, emphasizing key details about the record.

> [!NOTE]
> Record summaries only appear after a new record has been successfully saved. For unsaved records, the summary area remains hidden.

:::image type="content" source="media/row_summary_expanded.png" alt-text="Screenshot that shows a row summary card in the AI assistance area on a form.":::

### Expanding and collapsing the summary
- Users can **expand** or **collapse** the summary section as needed. The system remembers the expanded/collapsed state for each user across sessions per device, ensuring a consistent experience when revisiting records.
- Summaries are currently expanded by default. 

:::image type="content" source="media/row_summary_collapsed.png" alt-text="Screenshot that shows a collapsed row summary.":::

### Acting on the summary
- **Copy**: Users can select the **Copy** button to copy the summary content directly to their clipboard for easy sharing or documentation.
- **Refresh**: Users can select the **Refresh** button to regenerate the summary content, ensuring the displayed information reflects the latest updates to the record.

### Providing feedback
- To improve the usefulness of summaries, users are encouraged to rate the feature using the **thumbs up** or **thumbs down** icons.
- This feedback mechanism helps refine summary generation, ensuring future summaries better meet user expectations and needs.

### Related information

[Manage feature settings](/power-platform/admin/settings-features)  
[Configuring summaries for tables](../maker/data-platform/configure-form-row-summary.md#create-a-row-summary)  
