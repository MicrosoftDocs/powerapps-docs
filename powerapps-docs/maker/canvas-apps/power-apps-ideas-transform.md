---
title: "Transform natural language to Power Fx formulas"
description: Learn how to use Power Apps Ideas to transform natural language into Power Fx formulas.
author: norliu

ms.topic: how-to
ms.custom: canvas
ms.date: 10/04/2022
ms.subservice: canvas-maker
ms.author: norliu
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - norliu
  - mduelae
---

# Transform natural language to Power Fx formulas 


Power Apps Ideas can generate ideas for formulas using the following controls on different properties:

- **Gallery**
- **Data table**
- **Text box**
- **Drop down**
- **Combo box**
- **Text label** 


Power Apps Ideas also supports Microsoft Dataverse, Microsoft Lists, SharePoint library, and Excel as connectors. So, if you're using one of the supported controls and want to write a formula for Gallery or Dropdown items, or for Label’s text content, color, or visibility, then check out Power Apps Ideas.

For example, instead of figuring out how to write the following formula ...

```power-fx
Filter('Table1', StartsWith('fullname', "Yvonne"))
```

... You can type `'name starts with Yvonne` instead.

To begin, let’s look at a simple app to see how you can use Power Apps Ideas to help write formulas.

You can follow the steps mentioned in [Create a canvas app from Microsoft Dataverse](data-platform-create-app.md) to generate that app using the **Accounts** table from Dataverse.

1. Select **BrowseGallery1,** which is bound to the **Accounts** table.

1. Select **Sort, filter, and search** on the ideas box. 

   :::image type="content" source="media/power-apps-ideas/sort-filter.png" alt-text="Sort, filter, and search.":::

1. Select one of the default suggestions to check how it works or start entering your own query in natural language such as English (en-us).

    :::image type="content" source="media/power-apps-ideas/sort-filter-ideas.png" alt-text="Suggested ideas for sorting and filtering.":::

1. When typing you can use the default query, modify it, or describe it in your own way.

1. You'll see one or more formula suggestions produced. Let’s use the example **search accounts where name in textinput**. You'll see two suggestions in the results. Each of those formula suggestions includes three parts:

    - **Accounts** where the text in **TextInput1** appears in **name**. This is trying to explain what the suggested formula is doing so that it's easier for users who aren't familiar with Power Fx to understand the result. The names of the components used in the app are shown in bold.
    
    - **Apply to: Items**: This suggests which property the formula will be applied to. As Power Apps controls have many properties, Ideas can identify which property a formula should be applied to.

    - The formula suggestion in this scenario is `Search('Accounts', TextInput1.Text, "name")`.

        :::image type="content" source="media/power-apps-ideas/Ideas_example_c7.png" alt-text="Suggested formula based on entered search scenario.":::

1. Select your preferred suggestion and then select **Apply**. In this case, let's select the first suggestion since it's the best fit. The formula gets updated automatically and runs so you can check the result in your app. You can then decide whether to keep the selected formula or modify it.

## More examples

Consider the following examples for inspiration while working with Power Apps Ideas.

| Scenario | Description | Ideas example |
| --- | --- | --- |
|**Sort your table** |Sort by a single column |sort accounts by Account Name|
| | |sort accounts by Account Name A-Z|
| | |sort accounts by Account Name Z-A|
| |Sort accounts by Account Name and Created On|
| | |sort accounts by Account Name A-Z and Created On latest on top|
| |Sort existing tables |sort Gallery3 by Account Name Z to A|
|**Filter or search table by some conditions**|A number condition|accounts with length of Account Name bigger than 10|
| |A date condition|accounts created a week ago, accounts modified last 3 days|
| |A text condition|accounts with name contains Karen|
| |A few conditions|accounts whose name contains Karen and created 7 days ago|
| |A choice value|inactive accounts|
| |Search table by user input|search accounts with name in textinput|
| |Find a single record|first record in accounts where name contains Karen|
| |Find records on the top or the bottom of the table|top 10 accounts|
| | |last 10 accounts|
|**Conditional formatting (apply to color and visible)** |A number condition|accounts with length of Account Name bigger than 10|
| |A date condition|red if created 7 days ago|
| |A text condition|blue if name contains Karen|
|**Text generation** |Numbers|count of gallery sum of slider1 and slider2|
||String|label4 and label5 Trim textinput1First 3 characters of TextInput1|



## Best practices

To get the best results, follow these tips when writing the plain natural language query in the Ideas pane.

- Leverage default queries to see what kind of scenarios are supported.
- Be precise in your query. Ideas can recognize controls such as tables and columns. However, if you don't get a suggestion, try using the full name of the assets you’re referencing. For example, use **TextInput1** when you have multiple text input controls in the app. This way the system knows which control you're referring to. 

## Limitations

> [!NOTE]
> We're improving the model so it can accomplish more complex tasks and support more functions, controls, and properties. If you have a wish list, submit your ideas through [Power Apps Ideas - Power Platform Community](https://ideas.powerapps.com/).

Power Apps Ideas currently has the following limitations:

- Regions and language: Currently available in environments created inside the United States, with English (en-us) set as the browser's default language.
- Recognizes control value of **TextInput**, **Dropdown**, **DatePicker**, **Slider**, **Toggle**, **Checkbox**, and **Radio** as input.

   | Controls | Properties | 
   | --- | --- |
   | **Gallery**, **Data table**, **Drop down**, **Combo box** | Items |
   | **Text Box**, **Label** | Text, Color, Visible |
   
- Data sources: Currently Ideas supports Dataverse tables, Microsoft Lists, and Excel sheets.
- Functions: See [Supported Power Fx functions](#supported-power-fx-functions). We’ll continue to add support for more functions.
- Data types: Supports Text, Whole Number, Date and Time, Date Only, Decimal Number, Choice, Choices, Yes/No Lookup. Not supported: File and Image.
- This feature's model understands some commonly used expressions in natural language. For example, it can translate from `latest on top`, `big to small` to a descending order and `oldest on top`, `small to big` to ascending order. And it can understand most of the context so even if you didn't specify the table names, it will make the best prediction based on the current table that is bound to the control.<br>  

## Supported Power Fx functions

Functions supported by the Power Apps Ideas feature:

:::row:::
   :::column span="":::
      [Abs](functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
      [Average](functions/function-aggregates.md)
   :::column-end:::
   :::column span="":::
      [Concat](functions/function-concatenate.md)
   :::column-end:::
   :::column span="":::
      [Countif](functions/function-table-counts.md)
   :::column-end:::
   :::column span="":::
      [Countrows](functions/function-table-counts.md)
   :::column-end:::
   :::column span="":::
      [Date](functions/function-date-time.md)
   :::column-end:::
:::row-end:::
:::row:::
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
   :::column span="":::
      [Distinct](functions/function-distinct.md)
   :::column-end:::
:::row-end:::
:::row:::
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
      [If](functions/function-if.md)
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
      [Lower](functions/function-lower-upper-proper.md)
   :::column-end:::
   :::column span="":::
      [Max](functions/function-aggregates.md)
   :::column-end:::
   :::column span="":::
      [Min](functions/function-aggregates.md)
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
      [Not](functions/function-logicals.md)
   :::column-end:::
   :::column span="":::
      [Now](functions/function-now-today-istoday.md)
   :::column-end:::
   :::column span="":::
      [Power](functions/function-numericals.md)
   :::column-end:::
   :::column span="":::
      [Proper](functions/function-lower-upper-proper.md)
   :::column-end:::
   :::column span="":::
      [Rand](functions/function-rand.md)
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      [Round](functions/function-round.md)
   :::column-end::: 
   :::column span="":::
      [RoundDown](functions/function-round.md)
   :::column-end:::
   :::column span="":::
      [RoundUp](functions/function-round.md)
   :::column-end:::
   :::column span="":::
      [Search](functions/function-filter-lookup.md)
   :::column-end:::
   :::column span="":::
      [Second](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Split](functions/function-split.md)
   :::column-end:::
:::row-end:::
:::row:::
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
      [Sum](functions/function-aggregates.md)
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
      [Trim](functions/function-trim.md)
   :::column-end:::
   :::column span="":::
      [TrimEnds](functions/function-trim.md)
   :::column-end:::
   :::column span="":::
      [Upper](functions/function-lower-upper-proper.md)
   :::column-end:::
   :::column span="":::
      [Weekday](functions/function-datetime-parts.md)
   :::column-end:::
   :::column span="":::
      [Year](functions/function-datetime-parts.md)
   :::column-end:::
:::row-end:::

## Give feedback to Microsoft

If you have feedback for this feature—for example, you find the formula suggestions inaccurate or you have suggestions or ideas to share with us—you can find the feedback card in the Ideas panel. By selecting Send feedback, you can enter your thoughts. (Don't include confidential or personal information in your feedback.) 


Microsoft is committed to developing and deploying AI technologies in a responsible manner. If you find any inappropriate or absurd results generated by Power Apps
Ideas, look in the same feedback card for a [Report it now](https://msrc.microsoft.com/report/abuse) link below the feedback box that can help us keep our AI model behaving in a responsible manner. For a timely response, select **Threat type** as "URL" and **Incident type** as "Responsible AI" as shown in the following screenshot.

:::image type="content" source="media/power-apps-ideas/ideas-feedback-channel.png" alt-text="Give us feedback.":::



### See also

- [Formula reference](formula-reference.md)
- [Power Apps Ideas overview](power-apps-ideas.md)
