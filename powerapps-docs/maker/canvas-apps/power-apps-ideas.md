---
title: Power Apps Ideas overview (Preview)
description: Over view of Power Apps Ideas
author: norliu
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.date: 09/17/2021
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

# Power Apps Ideas overview (Preview)

[This article is pre-release documentation and is subject to change.]

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

[Power Fx](/power-platform/power-fx/overview) is a powerful, low-code language to help makers stitch app components together. However, sometimes it's not easy to write a formula. It takes time to learn and effort to tune. Power Apps Ideas is created to help customers ease the formula authoring experience by using the power of AI models.

You'll find an Ideas pane on the right side of your canvas app, next to Properties and Advanced tabs. You can select or create a Gallery or Data table that is bound to a Dataverse table and start to type in ideas in natural language. Select **Get Ideas** after done and in a few seconds, formula suggestions will be ready for you to pick from.

For example, instead of figuring out how to write the following formula:

```powerapps-dot
Sort(Search('Contacts', TextSearchBox1.Text, "fullname"), 'Created On', Descending)
```

You can type in `search Contacts with 'Full Name' in TextSearchBox1 and sort results by 'Created On' latest on top`.

![Power Apps Ideas demo.](media/power-apps-ideas/power-apps-ideas-demo.gif "Animation that shows how Power Apps Ideas work")

## Use Power Apps Ideas in your app

There are two methods to benefit from Power Apps Ideas in your app.

### Method 1: Transforming natural language to Power Fx formulas

You can enter your requirements in plain natural language (such as English (en-us)), and Power Apps transforms your requirement to Power Fx formula. For details, go to [Tutorial: Transforming natural language to Power Fx formulas (Preview)](power-apps-ideas-transform.md).

> [!NOTE]
> This capability only works on the **Items** property of [Gallery](controls/control-gallery.md) and [Data table](controls/control-data-table.md) controls. See [limitations](#limitations), [supported/unsupported capabilities](#supported-and-unsupported-capabilities), and [supported functions](#supported-power-fx-functions) later for more information.

### Method 2: Train with examples

When the formula doesn’t meet your needs, or there’s no formula suggestion, you can try to provide more examples for the model to learn so it could try to provide you a better suggestion. For details, go to [Tutorial: Train with examples](power-apps-ideas-train-examples.md).

> [!NOTE]
> We're improving the model to make it better and to accomplish more complex tasks, support more functions, controls, and properties. If you have a wish list, submit ideas through [Power Apps Ideas - Power Platform Community](https://powerusers.microsoft.com/t5/Power-Apps-Ideas/idb-p/PowerAppsIdeas).

## Limitations

During this experimental release, Power Apps Ideas has the following limitations:

- Regions and language: Currently available in environments created inside United States, with English (en-us) set as the browser's default language.
- Controls: Supports generating formulas for **Gallery** and **Data table** controls&mdash;on their **Items** property. Can recognize control value of TextInput, Dropdown, DatePicker, Slider, Toggle, Checkbox, Radio as input.
- Data sources: Currently Ideas only supports **Dataverse** tables and won't generate any suggestions if your Gallery or Data table isn't bound to a Dataverse table.
- Functions: Works best on `Search()`, `Filter()`, `Sort()`, `SortByColumns()`, `FirstN()`, and `LastN()`. And also a list of basic functions for the conditions. See [Supported Power Fx functions](#supported-power-fx-functions). We’ll continue to add support for more functions.
- Data types: Supports Text, Whole Number, Date and Time, Date Only, Decimal Number. Not supported: Lookup, Choice, Choices, Yes/No, File and Image.
- This feature's model understands some commonly used expressions in natural  language. For example, it can translate from `latest on top`, `big to small` to a descending order and `oldest on top`, `small to big` to ascending order. However, it needs you to be precise about table, column, and control names. <br> For example, if you enter `search Accounts with name in textbox`, it might not give you good results because there’s no linkage built on the model to understand that “name” maps to the “Account Name” column and "textbox" maps to "TextSearchBox1". <br> 
- This feature doesn’t understand business-related verbs. For example, if you want to show accounts that are created in the last month, you might not get good results, because the model doesn’t understand that “created” refers to the “Created On” column.

## Supported and unsupported capabilities

The following capabilities are supported:

- Converting a single date field in a table to a different format
- Converting a single text field in a table to a different format
- Works only for label text in a gallery
- All available languages and data connectors as supported by Power Apps regions

The following capabilities are not supported:

- Number manipulation
- Manipulating text from multiple columns
- Scenarios that include:
    - Branching
    - If/else patterns (function [If](functions/function-if.md))

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
      [DateDiff](functions/function-date-time.md)
   :::column-end:::
   :::column span="":::
      [DateTimeValue](functions/function-datevalue-timevalue.md)
   :::column-end:::
   :::column span="":::
      [DateValue](functions/function-datevalue-timevalue.md)
   :::column-end:::
   :::column span="":::
      [Day](functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::
:::row:::
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
   :::column span="":::
      [Hour](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [IsBlank](functions/function-isblank-isempty.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [IsEmpty](functions/function-isblank-isempty.md)
   :::column-end:::
   :::column span="":::
      [LastN](functions/function-first-last.md)
   :::column-end:::
   :::column span="":::
      [Minute](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Month](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Now](functions/function-now-today-istoday.md)
   :::column-end:::
   :::column span="":::
      [Search](functions/function-filter-lookup.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Second](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Sort](functions/function-sort.md)
   :::column-end:::
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
:::row-end:::
:::row:::
   :::column span="":::
      [Today](functions/function-now-today-istoday.md)
   :::column-end:::
   :::column span="":::
      [Weekday](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Year](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
   :::column-end:::
   :::column span="":::
   :::column-end:::
   :::column span="":::
   :::column-end:::
:::row-end:::

## Reporting abuses

Microsoft is committed to developing and deploying AI technologies in a responsible manner. If you find any inappropriate or absurd results generated by Power Apps
Ideas, select the [Report it now](https://msrc.microsoft.com/report/abuse) link at the bottom of the Ideas pane to help us improve the AI model. Make sure to select Threat type as URL and Incident type as Responsible AI as shown in the following screenshot so we can try our best to respond in time.

![Reporting abuses](media/power-apps-ideas/report.png "Reporting abuses")

## Next steps

- [Tutorial - Transforming natural language to Power Fx formulas (Preview)](power-apps-ideas-transform.md)
- [Tutorial - Use Power Apps Ideas in your app](power-apps-ideas-tutorial.md)

### See also

[Formula reference](formula-reference.md)
