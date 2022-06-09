---
title: Use the Search pane (preview)
description: Learn how to use the Search pane inside Power Apps Studio to find text.
author: TashasEv
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 06/09/2022
ms.subservice: canvas-maker
ms.author: tashas
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - TashasEv
---

# Use the Search pane (preview)

[This article is pre-release documentation and is subject to change.]

You can now use the Search pane to locate objects across your app like media files, variables, collections, data sources and more. You can also use the Search pane to find repeated instances of strings in formulas. For example, using the Search pane, you can look for each instance of `HoverColor` to determine the setting for that property in other areas of your app. You can use the Search pane to learn more about what is being used by your app where, along with being able to go right to results to make necessary updates. In addition, you can use the replace capability to update one or more instances of text, variables, collections, and formula references.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]
> - This feature is being rolled out and depending on your region, it may not be available for your tenant yet.

## Prerequisites

- [Sign up](../signup-for-powerapps.md) for Power Apps.
- [Create an app](get-started-test-drive.md) or [open an existing app](edit-app.md) in Power Apps.
- Learn how to [configure a control](add-configure-controls.md).
- Create a [new app](data-platform-create-app.md), or open an [existing app](edit-app.md) in Power Apps.

## Enable Search pane

The Search pane is enabled on the new apps by default. However, you need to manually enable it on existing apps.

To enable the Search pane on existing apps:

1. Open a [new](data-platform-create-app.md) or an [existing](edit-app.md) app in Power Apps Studio.

1. Select **Settings** at the top.

1. Select **Upcoming features**.

1. Under the **Preview** tab, select **Search** to turn on this feature.

    :::image type="content" source="media/search/enable-search.png" alt-text="Search feature listed under the preview section of upcoming features in settings.":::

    The Search pane is enabled:

    :::image type="content" source="media/search/search-pane.png" alt-text="Search pane visible inside Power Apps Studio.":::

## Open the Search pane

You can open the Search pane using the Search icon, or shortcut keys. To use the shortcut keys, press **Ctrl+F** when your cursor is outside the formula bar. When inside the formula bar, press **Ctrl+Shift+F** to open the Search pane.

You can also open the Search pane directly to the Replace functionality by pressing **Ctrl+H** when your cursor is outside the formula bar. When inside the formula bar, press **Ctrl+Shift+H** will open the Search pane directly to the Replace functionality.

> [!NOTE]
> Pressing **Ctrl+F** or **Ctrl+H** inside the formula bar will open the [Find and Replace](formula-bar-find-replace.md) capability inside the formula bar.

## Filter search results

You can filter search results through the selection of one or more categories. These categories help you focus the search by narrowing down the areas within the app&mdash;such as screens, media, collections, and so on.

To use filter option and select the required categories, use the filter option next to the search box. The default selection is **All**,  searching across all categories within the open app.

The following example shows the search results filtered for the search term "Snow" with the selected categories of **Variables** and **Collections**:

:::image type="content" source="media/search/filter.png" alt-text="Filter option selected on the Search pane.":::

## Refine your search

You can use more search options to further refine search. These options are available inside the filter option named **More search options** (below the **Categories** section).

:::image type="content" source="media/search/more-search-options.png" alt-text="More search options under categories in the filter option.":::

- **Match case** - returns search results that only match with the specified case.

    In the below example, instances of "Snow" (upper case) will appear as a match, but "snow" (lower case) wouldn't.

    :::image type="content" source="media/search/match-case.png" alt-text="An example of matching the case for search results with results for upper case keyword.":::

- **Match Whole Word** - returns search results for exact matches of the entire sequence of characters.

    In the below example, "Snow" returns only a few results although "Snow" appears within names many times across all app objects.

    :::image type="content" source="media/search/match-whole-words.png" alt-text="An example of matching the whole word in search result that limits search for the exact word only.":::

- **Use regular expression (RegEx)** - returns search results for matches conforming to the [regular expression](/deployedge/edge-learnmore-regex) specified within the input area.

    In the below example, using the Regular Expression search capability with `Snowboarding( Mountain | Dashboard)` formula returns matches for "Snowboarding" when it appears together with either "Mountain" or "Dashboard".

    :::image type="content" source="media/search/regex.png" alt-text="An example of matching regular expression syntax while searching for text.":::

## Work with search results

Selecting search results in different areas of the Search pane will behave differently depending on the context of the result. The search results can be classified under two broad categories&mdash;**Definitions** and **Instances**.

- **Definitions** describe the object being referred to in your app, usually in a formula. Instances are the individual formula references where you refer to the object.

    There are several category headers inside the Search pane that you can use to navigate through the results. Categories such as **Variables**, **Collections**, **Data**, **Media**, **Flows**, and **Components** are referred as **definitions**.

    Selecting the results under such definition category headers takes you to the appropriate definition screen backstage (such as for Variables and Collections), or to the appropriate pane where that object is available in your app (such as Data, Media, Flows, and Components).

- **Instances** describe the search results that are tied to an individual app, screen, or control property in the formula bar. All these results are tied to the **Screens** category based on the structure found inside the **Tree View**. When you select a result under this **Screens** category, you'll be taken to that specific formula bar reference or the related control as applicable.

### Variables

Selecting a global or a context variable under the **Variables** header in the search results will take you to the information screen backstage for the selection.

As shown below, you're taken to the definition of the global or context variable depending on your selection from the search results available.

Search result:

:::image type="content" source="media/search/variables.png" alt-text="Global and context variables available in search result.":::

Depending on the selected global or context variable, you're taken to the backstage for the selected type of variable.

Global variable selected:

:::image type="content" source="media/search/global-variable.png" alt-text="Selecting a global variable takes you to the backstage of the selected global variables.":::

Context variable selected:

:::image type="content" source="media/search/local-variable.png" alt-text="Selecting a context variable takes you to the backstage of the selected context variables.":::

### Collections

Selecting a collection under the **Collections** header will take you to the information screen backstage for that collection.

:::image type="content" source="media/search/collections.png" alt-text="Collections selected from search results showing the relevant collection details.":::

### Data

Selecting a result under the **Data** header opens the **Data** pane, and pre-populates the search input for that pane with the selected result text.

:::image type="content" source="media/search/data.png" alt-text="Data selected from search results showing the relevant data connection details.":::

### Media

Selecting a result under the **Media** header opens the **Media** and pre-populates the search input for that pane with the selected result text.

:::image type="content" source="media/search/media.png" alt-text="Media selected from search results showing the relevant media details.":::

### Flows

**Flows** header only appears if you've enabled the [Power Automate pane (preview)](working-with-flows.md). Selecting a result here opens the Power Automate pane, and pre-populates the search input with the selected result text.

:::image type="content" source="media/search/flows.png" alt-text="Flow selected from search results showing the relevant flow details.":::

### Components

Selecting a result under the **Components** header takes you to the components section in the **Tree view** pane, and pre-populates the search input for that pane with the selected result text.

:::image type="content" source="media/search/components.png" alt-text="Component selected from search results showing the relevant component details.":::

### Screens

Selecting a result under the **Screen** header selects the appropriate control or screen on the canvas, and opens the property for the result in the formula bar. The selected result also gets highlighted in the formula bar.

:::image type="content" source="media/search/screens.png" alt-text="Screens selected from search results showing the relevant screen details.":::

## Refreshing the search results

If you make changes within the app, you'll need to refresh the results pane to see the change reflected in your search results.

:::image type="content" source="media/search/refresh.png" alt-text="Use the Refresh button to refresh the search results based on changes inside the app elements.":::

## Clear the search term

Search terms and results are kept until you no longer need them. To clear the search term and results, select the **X** sign on the right hand side of the input area.

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

## Replace

You can replace one or more instances of certain types of search results, including variable and collection names and any formula text including strings and other formula references.

Once you perform a search, the replace pivot shows the list of search results which are eligible for replacing.

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

### Work with replaceable results

All replaceable results are selected by default. You can refine the list of results to replace by deselecting individual results or entire categories by selecting the checkbox beside the result or category heading. 

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

You can also filter the result list to only show selected categories of results.

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

As you refine the list of results to replace, the replace button at the bottom of the panel keeps track of the number of replacements to be made. If all items are selected, the button reads, "Replace all" with the total count of all replaceable items.

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

If you've selected results from the list, the button is updated to read, "Replace selected" with the total count of selected items.

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

You can also interact with individual results in the results list directly to perform replacements by selecting the ellipsis to the right of each individual result in the result list.

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

### Replacing Variables results

Performing a replacement for results in the Variables category replaces the variable name at the definition level, meaning all instances of the matching variable name will be replaced across the entire app. You can also view the variable details backstage to review the usage before making the replacement.

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

### Replacing Collections results

Similar to variables, replacing a result in the Collections category replaces the collection name at the definition level, replacing all matching instances of the collection name across the app. You can view collection details backstage prior to making the replacement.

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

### Replacing Screens results

The Screens category shows individual replaceable results following the structure in the Tree View, allowing you to replace text in formulas, formula references, and control names. Replacements made in the Screens category only replace the single instance of the selected matching result, allowing you to choose to pick and choose what you'd like to replace. You can also review the formula match before making the replacement.

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

### Completing the replacement and undoing replacements

Once you have refined your selection to the items you'd like to replace, selecting the button prompts you to confirm the operation.

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

Confirming the operation performs the replacement and a notification indicates whether the replacement was successful. The replacement operation may fail if a control name is already in use or unsupported characters are included.

:::image type="content" source="media/search/clear.png" alt-text="Use the clear button to clear the search terms.":::

After the replacement is complete, you can undo the replacement by using the undo button or by selecting **Ctrl+Z**.

## Limitations

The Search pane is limited to returning a maximum of 2000 results. A notification appears if you exceed this limit.

:::image type="content" source="media/search/max-results.png" alt-text="Maximum number of results reached.":::

### See also

[Use Find and Replace in the formula bar](formula-bar-find-replace.md)
