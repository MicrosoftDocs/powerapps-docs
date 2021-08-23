---
title: Power Apps Ideas (Preview)
description: Learn about using Power Apps Ideas natural language to transform into Power Fx formulas.
author: norliu
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.date: 08/23/2021
ms.subservice: canvas-maker
ms.author: norliu
ms.reviewer: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - norliu
  - tapanm-msft
---

# Power Apps Ideas (Preview)

[This article is pre-release documentation and is subject to change.]

[Power Fx](/power-platform/power-fx/overview) is a powerful, low-code language to help makers stitch app components together. However, sometimes it's not easy to write a formula. It takes time to learn and effort to tune. Power Apps Ideas is created to help customers ease the formula authoring experience by using the power of AI models. It can
now be used to transform natural language to a Power Fx formula.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

For example, instead of figuring out how to write the following formula:

```powerapps-dot
Sort(Search('Contacts', TextSearchBox1.Text, "fullname"), 'Created On', Descending)
```

You can type in `search Contacts with 'Full Name' in TextSearchBox1 and sort results by 'Created On' latest on top`.

![Power Apps Ideas demo.](media/power-apps-ideas/power-apps-ideas-demo.gif "Animation that shows how Power Apps Ideas work")

## Using Power Apps Ideas in your app

To use Power Apps Ideas, you'll find an Ideas pane on the right side of your canvas app, next to Properties and Advanced. You can select or create a Gallery or Data table that is bound to a Dataverse table and start to type in ideas in natural language. Select **Get Ideas** after done and in a few seconds, formula suggestions will be ready for you to pick from.

## Transforming natural language to Power Fx formula

Power Apps Ideas feature currently supports only **Gallery** and **Data table** controls for the **Items** property, and it's trained for the **Microsoft Dataverse connector**. So if you've got a gallery that is bound to a Dataverse table, and you’re about to write a formula for its Items property, you can check out Power Apps Ideas.

To begin, let’s take a look at a simple app to see how we can use the Power Apps Ideas to help write formulas.

You can follow the steps mentioned in [Create a canvas app from Microsoft Dataverse](data-platform-create-app.md) to generate that app using Accounts table from Dataverse.

1. Select **BrowseGallery1,** which is bound to the Accounts table.

1. Go to the property pane on the right-side of the screen, and select the **Ideas** tab.

1. You'll see a large textbox with a few default examples.

1. Select one of the default suggestions to check how it works, or start to type in your own query in plain English.

    ![Get started with Power Apps Ideas.](media/power-apps-ideas/power-apps-ideas.png "Get started with Power Apps Ideas")

1. When typing, try to be precise about the table names, column names, and conditions you want to use. For example, `search Accounts whose 'Account Name' contains TextSearchBox1”, “show Accounts whose ‘Created On’ is earlier than 7 days ago”`. After done typing, hit the "Enter" key on the keyboard, or select anywhere outside the input box.

1. You'll see one or more formula suggestions produced. Let’s use the example above `search Accounts whose 'Account Name' contains TextSearchBox1`. You'll see that the formula suggestion produced includes two parts:

    1. **Accounts** where the text in **TextSearchBox1** appears in **name**. This is trying to explain what the suggested formula is doing&mdash;so that it's easier for users who aren't familiar with Power Fx to understand the result. The names of the components used in the app are shown in bold.

    1. `Search('Accounts', TextSearchBox1.Text, "name")` > This is the actual formula suggestion.

        ![Graphical user interface, text, application, letter, email Description automatically generated.](media/power-apps-ideas/ideas-example.png)

1. When you select any suggested idea for a formula, the formula gets updated automatically and runs so you can check the result in your app. You can then decide whether to keep the selected formula, or modify it.

## Best practices

To get the best results, here are some tips that you can follow when writing the plain English query in the Ideas pane.

- Enter the complete context in the query. For example, if you need to filter a table by some conditions, be precise about which table to filter, which column to filter by, and what conditions need to be met.
- Use IntelliSense as much as possible. IntelliSense could help the AI model recognize context, and understand data types better.
- Double quote the text string you want to filter or search for. This will help the model recognize the target string better and provide a more accurate formula suggestion.

## Limitations

During this experimental release, Power Apps Ideas has the following limitations:

- Regions and language: Currently available in environments created inside United States, with English (en-us) set as the browser's default language.
- Controls: Supports generating formulas for **Gallery** and **Data table** controls&mdash;on their **Items** property. Can recognize control value of TextInput, Dropdown, DatePicker, Slider, Toggle, Checkbox, Radio as input.
- Data sources: Currently Ideas only supports **Dataverse** tables and won't generate any suggestions if your Gallery or Data table isn't bound to a Dataverse table.
- Functions: Works best on `Search()`, `Filter()`, `Sort()`, `SortByColumns()`, `FirstN()`, and `LastN()`. And also a list of basic functions for the conditions. See [Supported Power Fx functions](#supported-power-fx-functions). We’ll continue to add support for more functions.
- Data types: Supports Text, Whole Number, Date and Time, Date Only, Decimal Number. Not supported: Lookup, Choice, Choices, Yes/No, File and Image.
- This feature's model understands some commonly used expressions in natural  language. For example, it can translate from `latest on top`, `big to small` to a descending order and `oldest on top`, `small to big` to ascending order. However, it needs you to be precise about table, column, and control names. <br> For example, if you enter `search Accounts with name in textbox`, it might not give you good results because there’s no linkage built on the model to understand that “name” maps to the “Account Name” column and "textbox" maps to "TextSearchBox1". <br> 
- This feature doesn’t understand business-related verbs. For example, if you want to show accounts that are created in the last month, you might not get good results, because the model doesn’t understand that “created” refers to the “Created On” column.

> [!NOTE]
> We're improving the model to make it better and to accomplish more complex tasks, support more functions, controls, and properties. If you have a wish list, submit ideas through [Power Apps Ideas - Power Platform Community](https://powerusers.microsoft.com/t5/Power-Apps-Ideas/idb-p/PowerAppsIdeas).

## Supported Power Fx functions

Functions supported by Power Apps Ideas feature:

:::row:::
   :::column span="":::
      [Date](functions/function-date-time.md)
   :::column-end:::
   :::column span="":::
      [DateAdd](functions/function-date-time.md)
   :::column-end:::
   :::column span="":::
      [DateDiff]((functions/function-date-time.md))
   :::column-end:::
   :::column span="":::
      [DateTimeValue](functions/function-datevalue-timevalue.md)
   :::column-end:::
   :::column span="":::
      [DateValue](functions/function-datevalue-timevalue.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Day](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Distinct](functions/function-distinct.md)
   :::column-end:::
   :::column span="":::
      [EndsWith](functions/function-startswith.md)
   :::column-end:::
   :::column span="":::
      [Filter](functions/function-filter-lookup.md)
   :::column-end:::
   :::column span="":::
      [FirstN](functions/function-first-last.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Hour](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [IsBlank](functions/function-isblank-isempty.md)
   :::column-end:::
   :::column span="":::
      [IsEmpty](functions/function-isblank-isempty.md)
   :::column-end:::
   :::column span="":::
      [LastN](functions/function-first-last.md)
   :::column-end:::
   :::column span="":::
      [Minute](functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Month](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Now](functions/function-now-today-istoday.md)
   :::column-end:::
   :::column span="":::
      [Search](functions/function-filter-lookup.md)
   :::column-end:::
   :::column span="":::
      [Second](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Sort](functions/function-sort.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [SortByColumns](functions/function-sort.md)
   :::column-end:::
   :::column span="":::
      [StartsWith](functions/function-startswith.md)
   :::column-end:::
   :::column span="":::
      [Time](functions/function-date-time.md)
   :::column-end:::
   :::column span="":::
      [TimeValue](functions/function-datevalue-timevalue.md)
   :::column-end:::
   :::column span="":::
      [Today](functions/function-now-today-istoday.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Weekday](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Year](functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::

## Reporting abuses

Microsoft is committed to developing and deploying AI technologies in a responsible manner. If you find any inappropriate or absurd results generated by Power Apps
Ideas, select the [Report it now](https://msrc.microsoft.com/report/abuse) link at the bottom of the Ideas pane to help us improve the AI model. Make sure to select Threat type as URL and Incident type as Responsible AI as shown in the following screenshot so we can try our best to respond in time.

![Reporting abuses.](media/power-apps-ideas/report.png "Reporting abuses")

### See also

[Formula reference](formula-reference.md)
