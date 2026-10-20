---
title: FAQ about row summaries in model-driven apps
description: This FAQ provides information about the AI technology used in the row summaries feature with key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
ms.date: 09/17/2026
ms.custom: 
  - responsible-ai-faqs
ms.topic: faq
author: jasongre
ms.author: jasongre 
ms.reviewer: matp
ms.collection: 
    - bap-ai-copilot 
---
# FAQ about row summaries in model-driven apps

These frequently asked questions (FAQ) describe the AI impact of row summaries in model-driven apps.

## What are row summaries?

Row summaries are AI-generated summaries of a record's data shown on a form in a model-driven app. The feature reads the data on the current record and generates a short, natural-language summary that highlights key information, so users can understand a record without reading through every field.

## What can you do with row summaries?

Users can view an AI-generated summary of a record directly on its form. Makers can configure which forms show a row summary, edit the default AI-generated prompt that controls what the summary emphasizes, and hide row summaries from specific forms.

## What is the intended use of row summaries?

The intended use of row summaries is to help users quickly understand the content of a record without having to read every field and every related item on the form, especially for records with a large number of fields or a long history of activity.

## How were row summaries evaluated? What metrics are used to measure performance?

Row summaries rely on AI Builder to execute summary prompts. For more information about how AI Builder models are tested and evaluated for responsible AI, see [Responsible AI FAQs for AI Builder](/ai-builder/responsible-ai-overview).

## What are the limitations of row summaries? How can users minimize the impact of the limitations when using the system?

The current limitations of row summaries include:

- Row summaries can't currently perform calculations.
- Row summaries can't currently reference dates in relative terms, such as "yesterday" or "next week."
- Row summaries can't include links to related records.
- Columns calculated by using a formula aren't included in the summary.
- Row summaries don't include metadata about a record, such as who created or last modified it.
- Formatting, such as bold text or bullet points, isn't currently supported in the generated summary.

Treat the row summary as a helpful starting point for understanding a record. Review the record's fields and related data directly before making important decisions based on that data.

## What operational factors and settings allow for effective and responsible use of row summaries?

The **AI insight cards** environment setting that enables row summaries is on by default. Makers still need to configure and turn on summary prompts on individual tables so that row summaries appear on the corresponding forms and views. When configuring a summary prompt, makers should review the default prompt and adjust it as needed so that the generated summary emphasizes the information most relevant to the people using that form.

## Related articles

- [Use row summaries in model-driven apps](../../user/record-summaries.md)
- [Configure row summaries on a form](../data-platform/configure-form-row-summary.md)
- [Legal terms](https://go.microsoft.com/fwlink/?linkid=2173149)
