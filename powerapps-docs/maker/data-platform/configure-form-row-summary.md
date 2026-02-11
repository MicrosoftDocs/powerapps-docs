---
title: "Configure a row summary for a model-driven app"
description: "Learn how to configure a row summary for a model-driven app forms and views that uses AI to let your users view key information about a record."
ms.date: 02/11/2026
ms.update-cycle: 180-days
ms.subservice: dataverse-maker
ms.topic: how-to
author: Mattp123
ms.author: damialajogun
ms.reviewer: matp
contributors: jasongre
ms.collection: bap-ai-copilot
ms.custom: ignite-2024
ms.service: powerapps
---
# Configure a row summary for a model-driven app (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Write a custom prompt to specify which columns should be included in a Copilot‑generated row summary. These summaries appear in a consistent, dedicated experience, either surfaced in a collapsible summary bar at the top of a main form or accessed directly for individual rows from views, giving users quick access to the most important information for a record.

Records are often comprised of dozens of fields spread across multiple tables, views, forms, tabs, and sections, making it time‑consuming for users to locate and understand the information that matters most. By highlighting key fields and insights in an at‑a‑glance summary, makers can help users quickly orient themselves, regardless of where they encounter the record.

<!-- PM verifying this functionality: The customizable record summary can also include hyperlinks to related information, making it easy to navigate deeper or share concise, meaningful summaries with colleagues using collaboration tools like Microsoft Teams. -->

:::image type="content" source="media/ai-row-summary-runtime.png" alt-text="Row summary on a main form":::

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Prerequisite for configuring a row summary

To enable and use this feature, the following criterion is required:

- A Power Platform administrator has enabled the AI insight cards environment setting. More information: [Manage feature settings](/power-platform/admin/settings-features)

## Create a row summary

Row summaries can be configured for most tables and appear on main forms and views. 

> [!NOTE]
>
> - When you configure the row summary, it applies to all views and main forms for the table.
> - Some Dynamics 365 apps tables, such as Case, Lead, and Opportunity, provide their own summaries via the Dynamics 365 Customer Service and Dynamics 365 Sales applications. To avoid conflicts, the row summary feature isn't available for these tables. You can find more information about the summaries for these tables and the options for configuring or disabling these summaries by reading about the [Customer Service summary](/dynamics365/customer-service/administer/copilot-map-custom-fields) and [Sales summary](\/dynamics365/sales/copilot-summarize-records) features. These out-of-the-box summaries are currently only accessible from main forms (not views).  

1. Sign in to Power Apps (make.powerapps.com) select **Tables** on the left navigation pane, and then open the table where you want to configure a row summary. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Under **Customizations**, select **Row summary**.
   - If **Row summary** is disabled, hover over the words to find out the reason. For example, the table must have at least one row of data for the summary option to be enabled.   
1. In the **Prompt** box, add the columns that you want included in the summary by selecting **Add** or by typing */*. You can also specify formatting for the summary, such as make it a bulleted list or a paragraph, as well as how to ensure the summary is generated in the user's preferred language. More information: [Write a good prompt for the row summary](#write-a-good-prompt-for-the-row-summary) 
   :::image type="content" source="media/row-summary-main-form-example.png" alt-text="Columns added for main form summary " lightbox="media/row-summary-main-form-example.png":::
1. Select **Test prompt** to display a preview of the summary.
   The most recently edited row in the table is used to generate a test response.
1. Once you're satisfied with the columns and response from the test, select **Apply to main forms**.

> [!IMPORTANT]
> Any user who needs to view summaries configured through the Dynamics 365 Customer Service app must be assigned the `prvReadLanguageLocale` privilege through a security role.

## Determine which main forms include a row summary

After you apply a row summary, the summary displays on all main forms for the table. To view the forms that include a row summary, in Power Apps, select **Tables** on the left navigation pane, and then under **Data experiences** select **Forms**.

All forms with the row summary applied have a form AI icon next to the form name. Hovering over the icon displays "The row summary is applied to all main from for the *table name* table, and appears in every model-driven app that uses this form."
:::image type="content" source="media/ai-row-summary-indicator2.png" alt-text="Main form AI icon indicating that the form includes a row summary" lightbox="media/ai-row-summary-indicator2.png":::

## Write a good prompt for the row summary

Writing a custom prompt gives you the ability to instruct the AI model to perform a specific task. By carefully crafting a prompt, you can generate a response that suits your specific business need. Here are some tips to consider when writing a prompt:

- Provide a list of the columns you want to include in the summary. Alternatively, you might wish to provide a list of columns that you want to exclude from the summary.
- Specify any formatting preferences, such as write the summary as a bulleted list.
- Include the appropriate input and instruction if your users work in multiple languages and you want the summary to respect the user’s preferred language; otherwise, the summary will be generated in the language of the summary prompt itself, regardless of the user’s language settings. To configure:
   - Include the **LanguageCode** input in the prompt.
   - Add the instruction to the prompt: **"You must respond in language \<LanguageCode\>."**
   - If Copilot doesn't support the user's language, the summary is generated in English.
   - This language instruction is added by default for newly configured summaries, but must be *manually added for any pre-existing summaries* that were created before this behavior was introduced.  
- For information about how to craft effective prompts, download the [AI Builder prompt engineering guide](https://aka.ms/promptguide).

### Prompt example for a row summary

Here are examples to use when building a row summary prompt.

*Summarize Account record in a way that is easy to understand for a sales manager. Make sure to include all important information, including main ideas and important details, while keeping the order of the content logical. Remove any repetitive elements to make the summary as concise as possible without losing the original text’s integrity. If the original text is too short to condense, present it as the summary.*

*Don't include the title in the summary. Create the summary in two paragraphs. For the first paragraph, use the instructions under the header Data. For the second paragraph, use the data under the header Activity. Leave a blank line between the two paragraphs. Don't include the titles Data & Activity in the paragraphs.*

*Data:*

*Show the below values as bullet points using markdown text and bold the values. Make the primary contact a navigation link to the contact record. The link must not include query string parameters in it.*

*Account.Annual Revenue, Account.Category, Account.Industry, Account.Ownership*

*Activity:*

*Generate a summary paragraph using the following customer communication fields identifying top 2 key information and top 2 important actions to take.*

*Account.Regarding (Phone Call).Subject, Account.Regarding (Email).Subject*

*You must respond in language LanguageCode*

## Edit a row summary

To edit a row summary, open the table, and then under **Customizations** select **Row summary (applied)**. Follow the steps similar in [Create a row summary](#create-a-row-summary) to make and apply changes.

## Hide a row summary 

1. In Power Apps, select **Tables** on the left navigation pane, and open the table where you want to edit a row summary.
1. Under **Customizations**, select **Row summary**.
1. Unselect the **Show row summary** option at the top right of the modal. 
   :::image type="content" source="media/hide-form-row-summary.png" alt-text="Hide all main form row summaries":::

> [!NOTE]
> If you're trying to hide the default summary for case, lead, and opportunity, which are provided via the Dynamics 365 Customer Service and Dynamics 365 Sales applications, go to these articles to learn more about options for configuring and/or disabling these summaries:
>
> - Case: [Customer Service summary](/dynamics365/customer-service/administer/copilot-map-custom-fields)
> - Lead and opportunity: [Sales summary](/dynamics365/sales/copilot-summarize-records) features.

## Adding summaries to solutions

Row summaries are solution-aware and can be added to a solution to facilitate moving between environments. To add a summary to a solution, follow these steps: 

1. In Power Apps, select **Solutions** on the left navigation pane, and open the desired solution. 
1. Select **Add existing > More > Other > AI Skill Config**.
1. Select the rows corresponding to the tables you created summaries for, and then select **Add**. 

> [!IMPORTANT]
> - Don't add AI Skill Config table rows with an owner of *System* to your solutions. These don't correspond to row summaries you have created and might cause solution import to fail.  

## Related information

[FAQ for prompts and text generation capabilities](/ai-builder/faqs-text-generation)
