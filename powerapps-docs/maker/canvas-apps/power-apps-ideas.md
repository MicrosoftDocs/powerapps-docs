---
title: Power Apps Ideas
description: Learn about using Power Apps Ideas natural language to transform into Power Fx formulas.
author: norliu
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.date: 07/06/2021
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

# Power Apps Ideas


We know [Power
Fx](https://docs.microsoft.com/en-us/power-platform/power-fx/overview) is a
powerful, low-code language to help makers stitch app components together. Yet
we hear from our makers that it is not easy to write a formula. It takes time to
learn and effort to tune. Power Apps Ideas are created to help customers ease
the formula authoring experience by leveraging the power of AI models. It can
now be used to transform natural language to a Power Fx formula.

So instead of figuring out how to write the following

Sort(Search('Contacts', TextSearchBox1.Text, "fullname"), 'Created On',
Descending)

You can type in “search Contacts with 'Full Name' in TextSearchBox1 and sort
results by 'Created On' latest on top”

![](media/power-apps-ideas44f789d262c409ced446b89716845f26.gif)

Todo: limitations

Walkthrough with the northwind example. Step by step guidance.

## Transforming natural language to Power Fx formula

This feature currently supports only Gallery and Data table controls on their
Items property and was mainly trained for the Dataverse connector. So if you
have a gallery binding to a Dataverse table, and you’re about to write a formula
for its Items property, you can check out the Power Apps Ideas.

To begin, let’s take a look at a simple app to see how we use the Power Apps
Ideas to help building formulas.

You can follow steps mentioned in [Create a canvas app from Microsoft Dataverse
- Power Apps \| Microsoft
Docs](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/data-platform-create-app)
to generate that simple app using Accounts table from Dataverse.

1.  Select **BrowseGallery1,** which is bound to the Accounts table.

2.  Navigate to the right pane, pick “Ideas” tab.

3.  You will see a big textbox with a few default examples.

4.  You can either click on one of the default suggestions to check how it
    works, or start to type in your own query in plain English.

![](media/power-apps-ideas5a38b18a9ba3c7df7df56f6a9f20d595.png)

>   Graphical user interface, application, table Description automatically
>   generated

1.  When typing, try to be precise about the table names, column names and
    conditions you want to use. e.g. “search Accounts whose 'Account Name'
    contains TextSearchBox1”, “show Accounts whose ‘Created On’ is earlier than
    7 days ago”. After done typing, hit Enter button or click on the blank space
    of that tab. See [limitations](#limitations) of the feature now.

2.  You will see one or a few formula suggestions coming out. Let’s use the
    example above “search Accounts whose 'Account Name' contains
    TextSearchBox1”. You will see there’s one formula suggestion popped out. And
    it includes 2 part

    1.  **Accounts** where the text in **TextSearchBox1** appears in **name**.
        This is trying to explain what the suggested formula is doing so it is
        easier for users who are not familiar with Power Fx to understand the
        result. And bolded parts are for components used in the app.

    2.  Search('Accounts', TextSearchBox1.Text, "name"). This is the actual
        formula suggestion.

        ![Graphical user interface, text, application, letter, email Description automatically generated](media/power-apps-ideas1de9402e4c46341e1b8e4d9a2fd9b801.png)

3.  By clicking on the result, you will see the formula populating in your
    formula bar, and it will automatically run for you so you can check the
    result in your app to decide whether to keep it or abort.

## Limitations

-   Region and language support: Now it will only be visible for environments in
    NAM region and browser default language is English.

-   Controls: this feature supports only **Gallery** and **Data table**
    controls, on their Items property.

-   Functions: Works best on Search(), Filter(), Sort(), SortByColumns(),
    FirstN(), LastN(). We’ll continue to add support of more functions as we go.

-   Data types: We support Text, Date time, Numbers now, but not Lookup, Choice,
    Choices, Yes/No, File and Image.

-   How natural it is:

    -   the model does understand some commonly used expressions in natural
        language, e.g. it can translate from “latest on top”, “big to small” to
        a descending order and “oldest on top”, “small to big” to ascending
        order.

    -   However, it needs you to be precise about table, column, control names.
        E.G if you say “search Accounts with name in textbox”, it might not give
        you good result because there’s no linkage build on the model to
        understand “name” maps to “Account Name” column and textbox maps to
        TextSearchBox1.

    -   It also doesn’t understand business related verbs, e.g. if you want to
        show Accounts that are created in the last month, you might not get good
        result, because the model doesn’t understand “created” means “Created
        On” column.

    -   We’re keep improving the model to make it be able to accomplish more
        complex tasks and support more functions, properties. If you have a wish
        list, please submit ideas from [Power Apps Ideas - Power Platform
        Community
        (microsoft.com)](https://powerusers.microsoft.com/t5/Power-Apps-Ideas/idb-p/PowerAppsIdeas)

## Reporting abuses

Microsoft is committed to develop and deploying AI technologies in a responsible
manner. If you find any inappropriate or absurd results generated by Power Apps
Ideas, click the [Report it now](https://msrc.microsoft.com/report/abuse) link
in the bottom of the ideas pane to help us improve the AI model.

Make sure to select Threat type as URL and Incident Type as Responsible AI as
showed by following screenshot so we can try our best to respond in time.

![Graphical user interface, text, application, email Description automatically generated](media/power-apps-ideas24c9a36873a9ec5d6cf2a17243380369.png)

### See also

[Formula reference](formula-reference.md)
