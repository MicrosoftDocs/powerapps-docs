---
title: FAQ about finding data in a view with AI
description: This FAQ provides information about the AI technology used to find data in a view with natural language with key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
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
# FAQ about finding data in a view with AI

These frequently asked questions (FAQ) describe the AI impact of finding data in a view with AI in model-driven apps.

## What is finding data in a view with AI?

Finding data in a view with AI lets users search and filter a grid or view in a model-driven app by typing a natural-language question or request instead of building a filter manually. The feature interprets the request and applies the matching filter conditions to the view.

## What can you do with finding data in a view with AI?

Users can type a natural-language request, such as asking for records that match a condition described in everyday language, and the feature translates that request into filter conditions applied to the current view. This feature complements visualizing data in a view with Copilot, which generates charts from the data in a view.

## What is the intended use of finding data in a view with AI?

The intended use of this feature is to help users find the records they're looking for more quickly, without needing to know how to construct filter conditions manually or without remembering the exact column names used in a view.

## How was finding data in a view with AI evaluated? What metrics are used to measure performance?

We evaluate this feature by measuring how accurately natural-language requests are translated into the intended filter conditions, and whether the resulting view reflects the data the user was looking for. We also evaluate the feature for satisfying Microsoft's responsible AI principles.

## What are the limitations of finding data in a view with AI? How can users minimize the impact of the limitations when using the system?

Natural-language requests can be ambiguous, and the feature might interpret a request differently than the user intended, especially for complex or compound conditions. Users should review the filter conditions applied to the view after a request to confirm the results match their intent. They can refine their request or adjust the filter manually if needed.

## What operational factors and settings allow for effective and responsible use of finding data in a view with AI?

Users get the most reliable results by phrasing requests clearly and in terms of the data shown in the view, and by reviewing the resulting filtered view before relying on it for reporting or decision-making.

## Related articles

- [Find data in a view with AI](../../user/find-data-with-ai.md)
- [Visualize data in a view with Copilot](../../user/visualize-data-in-copilot.md)
- [FAQ about Copilot visualizations on a view (preview)](faq-visualize-view.md)
- [Legal terms](https://go.microsoft.com/fwlink/?linkid=2173149)
