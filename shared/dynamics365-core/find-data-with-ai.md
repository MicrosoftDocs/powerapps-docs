[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Users can find, filter, and sort their data quickly with natural language, bypassing complicated advanced filters. If your administrator has turned on **Natural Language Grid and View Search**, then the natural language search box will be visible.

### Natural language search

Use smart grid natural language search to ask data-related questions in natural language. For example, request “cases with high priority with overdue follow-up by date” to filter your view and display only those relevant cases.

:::image type="content" source="/power-apps/user/media/smart_grid_search.png" alt-text="A screenshot of the natural language search box on grid page":::

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

### Supported features

- Filtering of record
- Sorting
- Text search

### Known limitations

These capabilities aren't supported:

- Query aggregation
- Query grouping
- Adding columns

### Considerations

- After you run a query, check the generated filter tags to make sure that the filter conditions were correctly interpreted from your natural language query. If any part of your query is missing from the filter tags, the results aren't filtered by that condition.
- If Copilot doesn't give the desired results, consider modifying your query by:
  - Refer to data columns by the names shown in the grid header.
  - Separate multiple conditions with commas or periods.
- If your search string has two words or fewer, Copilot does a text search. To do a Copilot search, use more than two words. To do a text search with more than two words, put the search term in single or double quotes.