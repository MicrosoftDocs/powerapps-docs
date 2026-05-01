
Users can quickly find, filter, and sort their data by using natural language, so they don't need to use complicated advanced filters. If your administrator turns on **Natural Language Grid and View Search**, you see the natural language search box.

## Natural language search in apps

Use smart grid natural language search to ask data-related questions in natural language. For example, request “cases with high priority with overdue follow-up by date” to filter your view and display only those relevant cases.

:::image type="content" source="/power-apps/user/media/smart_grid_search.png" alt-text="A screenshot of the natural language search box on grid page":::

### Licensing requirements

Natural language grid and view search requires specific user licenses based on the product. If the user doesn't have the license, the feature is hidden. This license enforcement will gradually rollout following the feature's general availability.

- **Power Apps model-driven app**: The user must have a Power Apps premium license. For details, see the [Power Platform License Guide](https://go.microsoft.com/fwlink/?linkid=2085130).
- **Dynamics 365 model-driven app**: The user must have a Dynamics 365 enterprise or premium license as outlined in [Dynamics 365 License Guide](https://go.microsoft.com/fwlink/?LinkId=866544).

Usage might be subject to service limits or throttling. Microsoft reserves the right to update the limits.

### Admin control

The primary admin control for **Natural Language Grid and View Search** is moving to the Power Platform admin center under **Copilot** > **Settings** > **Power Apps** > **Data exploration**. Learn more in [Copilot hub](/power-platform/admin/copilot/copilot-hub). This is gradually rolling out over the next coming weeks.
 
**Natural language grid and view search** app setting (`NLGridSearchSetting`) previously available in [Power Platform admin center](/power-platform/admin/settings-features#natural-language-grid-and-view-search) **Environment** > **Settings** > **Product** > **Features** page is moving and you can configure this setting at the app level either by using [Manage model-driven app settings in the app designer](/power-apps/maker/model-driven-apps/app-properties) or [Updating a setting definition](/power-apps/maker/data-platform/create-edit-configure-settings#updating-a-setting-definition).

## Explore data with agents in Microsoft 365 Copilot (preview)

[!INCLUDE [preview-banner-section](~/../shared-content/shared/preview-includes/preview-banner-section.md)]

With Microsoft 365 Copilot you have the ability to bring app-based experiences to agents, the app experience can also use the AI assisted search in the grid view. 

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is being gradually rolled out across regions and might not be available yet in your region.

> [!NOTE]
> To use this capability, you need to [set up an apps agent in Microsoft 365 Copilot](/power-apps/maker/model-driven-apps/app-properties#upcoming).

When users interact with agents in M365 Copilot, the agents can search and retrieve data from apps view directly within the conversation. By using natural language, users can find, filter, and review app data without switching to the app experience.
Natural language search interprets the user's request and applies the appropriate filters, sorting, and text search against the underlying view data. The agent returns the results in Copilot chat, presented in a structured, tabular format that reflects the view data.
Users can continue to work with the returned results in the conversation, iterating with natural language to refine the output until it reflects the exact results they’re looking for.

:::image type="content" source="/power-apps/user/media/find-data-grid-in-copilot.png" alt-text="A screenshot showing how data can be fetched using agent in Microsoft 365 Copilot":::


## Supported features

- Filtering of records
- Sorting
- Text search

## Known limitations

These capabilities aren't supported:

- Query aggregation
- Query grouping
- Adding columns

## Considerations

- After you run a query, check the generated filter tags to make sure that the filter conditions were correctly interpreted from your natural language query. If any part of your query is missing from the filter tags, the results aren't filtered by that condition.
- If search doesn't give the desired results, consider modifying your query by:
  - Referring to data columns by the names shown in the grid header.
  - Separating multiple conditions with commas or periods.
- In model-driven app for grids, if your search string has two words or fewer, the search does a text search. To do a natural language search, use more than two words. To do a text search with more than two words, put the search term in single or double quotes. This behavior doesn't apply to Copilot chat.

