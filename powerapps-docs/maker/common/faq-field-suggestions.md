---
title: FAQs for field suggestions by Copilot
description: These FAQs provide information about the AI technology that uses to get field suggestions by Copilot, along with key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
ms.date: 9/04/2024
ms.custom: 
  - responsible-ai-faqs
ms.topic: faq
author: norliu
ms.author: norliu
ms.reviewer: mkaur
contributors:
- Mattp123
ms.collection: 
    - bap-ai-copilot 
---

# FAQs for field suggestions by Copilot

These frequently asked questions (FAQs) describe the AI impact of field suggestions by Copilot in Power Apps.

## What is field suggestions by Copilot?

In Power Apps Studio, when a maker connects a gallery or form to a data table, Power Apps automatically selects certain system-generated key columns, such as ID, created on, or modified on. These columns might not be relevant to the app users. Moreover, makers have to manually select each field, which can be a tedious process for large data tables. With field suggestions, Copilot can recommend relevant columns to the gallery or form when the developer binds it to data using the table’s metadata. This feature can save makers time in field configuration, thereby accelerating the app building process.

## What are the system’s capabilities?

At the time, a maker first binds to or changes data source of a gallery or form to a data table, Copilot will automatically suggest up to 10 of the most relevant fields. A maker must approve the suggestions for it to take effect. Makers can adjust the results easily as they change fields today.

Supported controls:

- Gallery
- Form (classic)
- Form (modern)
- Table (modern)
- Supported views and forms (model-driven apps)
- Quick view form
- Quick create form
- New view

Supported data sources:

- Dataverse
- SQL
- SharePoint list

## What is the system’s intended use?

The system is intended to help makers save time in app editing by preloading and selecting the most relevant fields when data source change happens. 

## How was field suggestions by Copilot evaluated? What metrics are used to measure performance?

We evaluate the feature both qualitatively and quantitatively. To assess the quality of the feature, we're conducting user studies with makers to gather their feedback on their experiences, thoughts about the feature's quality, and suggestions for improvement. Additionally, we're monitoring telemetry data to track the number of makers who tried the feature, the success rate of the feature, and the ratio of positive to negative feedback. Before releasing the Copilot feature, we conducted extensive testing to ensure its functionality. If you encounter any issues with the content generated, provide feedback. Your feedback is used to enhance Microsoft's products and services. Your organization's IT admins have access to your feedback data for management purposes. For more information, read the [Privacy Statement](https://go.microsoft.com/fwlink/?linkid=2182930%22%20%5Ct%20%22_blank).

## What are the limitations of field suggestions by Copilot? How can users minimize the impact of field suggestions by Copilot limitations when using the system?

-	Copilot will only use the table’s metadata to make recommendations, it doesn’t allow maker to provide natural language input to specify what columns they want. If you think this is critical, send us feedback.
-	This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
-	This capability is in the process of rolling out and might not be available in your region yet.
-	This capability may be subject to usage limits or capacity throttling.
-	Your environment must be in the United States region.
-	This feature doesn’t support non-English language input.
-	This feature only supports limited controls and actions as listed in the [intended use](faq-field-suggestions.md#what-is-the-systems-intended-use) section. - Microsoft is actively working on expanding the scope of this feature and support more actions incrementally.

## What operational factors and settings allow for effective and responsible use of the system?

Copilot will only read your table’s metadata (so table name, description, column name, description, column’s data type) to make recommendations and select fields. To yield the best quality, it’s strongly recommended that when you create your data source, use meaningful names and descriptions for both the table and the columns.

## See also

[Use field suggestions by Copilot](../canvas-apps/ai-field-suggestions.md)

[Column suggestions by Copilot](../model-driven-apps/create-and-edit-forms.md#column-suggestions-by-copilot)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
