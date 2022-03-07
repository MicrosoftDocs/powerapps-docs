---
title: Use search pane (preview)
description: Learn how to use the Search pane inside Power Apps Studio to find text.
author: TashasEv
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/16/2022
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

# Use search pane (preview)

[This article is pre-release documentation and is subject to change.]

You can now use the search pane to locate objects across your app like media files, variables, collections, data sources and more. You can also use the search pane to find repeated instances of strings in formulas. For example, using the search pane, you can look for each instance of `HoverColor` to determine the setting for that property in other areas of your app. You can use the search pane to learn more about what is being used by your app where, along with being able to go right to results to make necessary updates.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]
> - This feature is being rolled out and depending on your region, it may not be available for your tenant yet.

## Prerequisites

- [Sign up](../signup-for-powerapps.md) for Power Apps.
- [Create an app](get-started-test-drive.md) or [open an existing app](edit-app.md) in Power Apps.
- Learn how to [configure a control](add-configure-controls.md).
- Create a [new app](data-platform-create-app.md), or open an [existing app](edit-app.md) in Power Apps.

## Enable the search pane

The search pane is enabled on the new apps by default. However, you need to manually enable it on existing apps.

To enable search pane on existing apps:

1. Open a [new](data-platform-create-app.md) or an [existing](edit-app.md) app in Power Apps Studio.

1. Select **Settings** at the top.

1. Select **Upcoming features**.

1. Under the **Preview** tab, select **Search** to turn this feature on.

    :::image type="content" source="media/search/enable-search.png" alt-text="Search feature listed under the preview section of upcoming features in settings.":::

    Search pane is enabled:

    :::image type="content" source="media/search/search-pane.png" alt-text="Search pane visible inside Power Apps Studio.":::

## Open search pane

You can open the search pane using the Search icon, or shortcut keys. To use the shortcut keys, press **Ctrl+F** when your cursor is outside the formula bar. When inside the formula bar, press **Ctrl+Shift+F* to open search pane.

> [!NOTE]
> Pressing **Ctrl+F** inside the formula bar will open the [Find and Replace](formula-bar-find-replace.md) capability inside the formula bar.

## Using the Search pane

When working with search, you have options to help you filter and refine your search. We'll look at these options.

## Filter

1.  Add text or characters to search for into the provided input area.

2.  Select the filter icon on the righthand side of the provided input area.

![A screenshot of the top of the Search pane highlighting the filter results dropdown to the far right of the text input area ](media/search/image4.png)

3.  Select one or more categories on the right to filter your search results. By default, "All" is selected and results from all categories will be shown.

![A screenshot of the expanded category filter dropdown  highlighting that you can select multiple categories and include refiners such as Match case  Match whole word  and regular expressions](media/search/image5.png)

## Refine your search

Below the filter categories, you can also refine your search results using the options under **More search options**:

![A screenshot of the expanded category filter dropdown highlighting the section labeled  quot](media/search/More search options&quot.png " and includes refiners such as Match case, Match whole word, and regular expressions")

- **Match case** returns only matches with the specified case.  
    In the example below, instances of Snow will appear as a match, but snow would not.

![A screenshot of the expanded category filter dropdown  highlighting the Match case search option below the filter categories](media/search/image7.png)

- **Match Whole Word** returns only exact matches of the entire sequence of characters.  
    In the example below, "Snow" returns only 2 results although "Snow" appears within names many times across app objects.

![A screenshot of the expanded category filter dropdown  highlighting the Match whole word search option in the second position below the filter categories](media/search/image8.png)

- **Use regular expression (RegEx)** returns only matches conforming to the regular expression specified within the input area. See [regular-expression syntax](https://docs.microsoft.com/en-us/previous-versions/1400241x(v=vs.100)) for an introduction to the syntax.   
    In the example below, using the Regular Expression search capability with *Snowboarding( Mountain\| Dashboard)* returns matches for*Snowboarding* when it appears together with either*Mountain* or*Dashboard* as shown below.

![A screenshot of the expanded category filter dropdown  highlighting the Use regular expression search option in the final position below the filter categories ](media/search/image9.png)

# Working with Search results

Selecting search results in different areas of the Search pane will behave differently depending on the context of the result. In broad terms, there are two major types of search results in the pane: **definitions** and **instances**. Definitions describe the object being referred to in your app, usually in a formula. Instances are the individual formula references where you refer to the object.

In the Search pane there are several category headers which you can use to navigate through the results in addition to filtering as shown above. The Variables, Collections, Data, Media, Flows, and Components categories all refer to **definitions.** When you select results under these category headers, you'll be taken either to the appropriate definition screen backstage (such as for Variables and Collections) or to the appropriate pane where that object was added to your app (such as for Data, Media, Flows, and Components).

The Screens category is based on the structure of the screens pivot under the Tree View. Here you will find **instances**: search results which are directly tied to an individual App, Screen, or Control property in the formula bar. When you select a result under the Screens category, you'll be taken to that specific formula bar reference and the related control will be selected if applicable.

Here we'll explore each search result type.

## Variables

![A screenshot of the Search pane highlighting results under the Variables category header with both global and context variable results  The searched term is highlighted within the results ](media/search/image10.png)

Selecting either a Global or Context Variable under the Variables header will navigate to the information screen backstage for that variable.

**Global Variable:**

![A screenshot of the backstage area showing details for the selected Global Variable Search result  the Global tab is highlighted and the search term is highlighted in multiple places on the screen ](media/search/image11.png)

**Context Variable:**

![A screenshot of the backstage area showing details for the selected context variable search result  The relevant screen tab for the context variable is highlighted and the search term is highlighted on the screen ](media/search/image12.png)

## Collections

![A screenshot of the Search pane highlighting results under the Collections category header  The searched term is highlighted within the results ](media/search/image13.png)

Selecting a collection under the Collections header will navigate you to the information screen backstage for that collection.

![A screenshot of the backstage area showing details for the selected collection search result  The relevant collection tab is highlighted ](media/search/image14.png)

## Data

![A screenshot of the Search pane highlighting results under the Data category header  The searched term is highlighted within the results ](media/search/image15.png)

Selecting a result under the Data header will open the Data Pane and pre-populate the search input for that pane with the selected result text to help further refine the pane results.

![A screenshot of the Data pane with the selected search result copied to the search input text area and showing the filtered list of data sources returning a single result matching the input text  ](media/search/image16.png)

## Media

![A screenshot of the Search pane highlighting results under the Media category header  The searched term is highlighted within the results ](media/search/image17.png)

Selecting a result under the Media header will open the Media Pane and pre-populate the search input for that pane with the selected result text to help further refine the pane results.

![A screenshot of the Media pane with the selected search result copied to the search input text area and showing the filtered list of Images with a single result with a name matching the input text  ](media/search/image18.png)

## Flows

![A screenshot of the Search pane highlighting results under the Flows category header  The searched term is highlighted within the results ](media/search/image19.png)

This header will only appear if you have enabled the Power Automate Pane (Preview) feature under Settings. Selecting a result here will open the Power Automate Pane and pre-populate the search input for that pane with the selected result text to help further refine the pane results. [Learn more about the Power Automate Pane here.](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/working-with-flows)

![A screenshot of the Power Automate pane with the selected search result copied to the search input text area and showing the filtered list of flows returning a single result matching the input text  ](media/search/image20.png)

## Components

![A screenshot of the Search pane highlighting results under the Components category header  The searched term is highlighted within the results ](media/search/image21.png)

Selecting a result under the Components header will navigate you to the Components pivot in the Tree View Pane and pre-populate the search input for that pane with the selected result text to help further refine the pane results.

![A screenshot of the Tree view pane on the components pivot with the selected search result copied to the search input text area  A filtered result list returning a single component result matching the input text  ](media/search/image22.png)

## Screens

![A screenshot of the Search pane highlighting results under the Screens category header  There is a hierarchy of results shown for App  screens  their associated controls  and the matching entries in associated properties in formulas  The searched term is highlighted within the results ](media/search/image23.png)

Selecting a result under the Screen header will select the appropriate control or screen on the canvas for the result and open the property for the result in the formula bar. The selected result will also be highlighted in the formula bar.

![A screenshot of the OnStart property of the app showing an associated formula in the formula bar which has the search text highlighted](media/search/image24.png)

# Refreshing the Search results

If you make changes within the app, you'll need to refresh the results pane to see the change reflected in your search results.

![A screenshot of the top of the search pane highlighting the refresh button underneath the search text input area ](media/search/image25.png)

# Clearing the Search term

Search terms and results are kept until you no longer need them. To clear the search term and results, select the 'X' on the right hand side of the input area.

![A screenshot of the top of the search pane highlighting the   39](media/search/X&#39.png " button to the right of the search text input area.")

# Limitations

The Search pane is limited to returning up to 2000 results. You'll receive a notification if you've exceeded that amount of results with a prompt to refine your search.

![A screenshot of the top of the search pane highlighting a message under the search term input area which says  quot](media/search/2000+ results found. Try narrowing your search&quot.png)
