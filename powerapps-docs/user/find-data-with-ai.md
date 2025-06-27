---
title: Find data in a view with AI
description: Learn how to find, filter, and sort data in a view using AI
ms.date: 05/22/2025
ms.reviewer: smurkute
ms.topic: "how-to"
author: clromano
ms.subservice: end-user
ms.author: clromano
contributors: 
ms.service: powerapps
search.audienceType: 
  - enduser
---

# Find data in a view with AI

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Users can find, filter, and sort their data quickly with natural language, bypassing complicated advanced filters. If your administrator has turned on **Natural Language Grid and View Search**, then the natural language search box will be visible.

### Natural language search

Using smart grid natural language search, you can ask data-related questions with natural language. For instance, requesting “cases with high priority with overdue follow-up by date” will filter your view to display only those relevant cases.

:::image type="content" source="./media/smart_grid_search.png" alt-text="A screenshot of the natural language search box on grid page":::

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

### Supported features

- Filtering of record
- Sorting
- Text search

### Known limitations

The following capabilities aren't supported:

- Query aggregation
- Query grouping
- Adding columns

### Considerations

- After executing a query, review the generated filter tags to ensure that the filter conditions were correctly interpreted from your natural language query. If any part of your query is missing from the filter tags, the results weren't filtered by that condition.
- If Copilot doesn't produce the desired results, consider modifying your query by:
  - Referring to data columns by their names as they appear in the grid header
  - Separating multiple conditions with commas or periods
- Search strings with two words or fewer will do a text search (previous functionality).  To do a Copilot search, use more than two words.  To perform a text search for more than two words, enclose the search term in single or double quotes.
