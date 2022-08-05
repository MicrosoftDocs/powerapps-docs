---
title: Create a choice| Microsoft Docs
description: Step-by-step instructions for how to create a choice.
author: lancedMicrosoft
manager: tapanm
ms.component: cds
ms.topic: how-to
ms.date: 03/21/2018
ms.subservice: dataverse-maker
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Create a choice

Choice columns allow you to include dropdown lists of fixed values to a user within your app to ensure data consistency. Choice columns, were formerly referred to as option sets and are sometimes called picklists. Similar to tables, there are both standard choices or makers have the ability to create custom choice columns to use in apps.

Choices can be created while working from a solution in powerapps.com in a table in the table hub or on a table form in the form designer.

Choice columns can be single selection only (choice) or can allow multi-selection (choices). The following screenshot shows a multi-select choices column in a model-driven app. More information: [Create and edit choice columns overview](create-edit-global-option-sets.md)

:::image type="content" source="media/data-platform-cds-newoptionset/multi-select-choice.png" alt-text="A multi-select choices column displayed on a model-driven app main form":::

## Create a global choice within a solution

When you follow these steps to create a choice in a solution, you're creating a global choice that is single selection.

1. Sign into [powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select Solutions, and then open the solution you want.

1. On the command bar, select **New** > **Choice**.

1. In the **New choice** panel, enter the **Display name** for your column. The **Display name** is used when presenting this column to your users.

1. Create the options for your choice:
   - In the **Label** field, enter the label you want displayed for the choice option.
   - The **Value** number represents a unique value for the option and is not displayed in the choice column in an app. Notice there's a number generated for each **Value** automatically. We recommend that you not change this. Having a unique **Value** helps ensure that the value will be different from other option values that might be defined in other solutions and imported into your environment.
   - Select the color picker to the left of the **Label** if you want a color to appear for the option in model-driven app charts.

1. Select **+ New choice** to create additional options for the choice list. Repeat steps 4-5 until all the options you want are created.

1. Optionally, expand **Advanced options** to display the following properties:
   - **Name**. This is the unique name used by the system and is automatically generated based on the display name and solution publisher prefix. After a new choice column is saved you can't change this.
   - **External type name**: This value is used for virtual tables to map a value in an external data source to the choice column.
   - **Description**: Add an optional description for the choice.

   :::image type="content" source="media/data-platform-cds-newoptionset/choice-created-in-solution.png" alt-text="New choice properties pane.":::

1. Select **Save**.

## Create a choice in the form designer

You can create global or local choice columns in the form designer. More information: [Create a choice column](../model-driven-apps/add-move-or-delete-fields-on-form.md#create-a-choice-column)

## Create and edit global choices using solution explorer

Solution explorer provides one way to create and edit global choices for Dataverse.

> [!NOTE]
> [make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) is the best way to create and edit choice columns.

### Open solution explorer

Part of the name of any global choice  you create is the customization prefix. This is set based on the solution publisher for the solution you’re working in. If you care about the customization prefix, make sure that you are working in an unmanaged solution where the customization prefix is the one you want for this global choice . More information: [Change the solution publisher prefix](create-solution.md#solution-publisher) 

[!INCLUDE [cc_navigate-solution-from-powerapps-portal](../../includes/cc_navigate-solution-from-powerapps-portal.md)]

### View global choices

With solution explorer open, under **Components** select **Option Sets**.

![View global choices.](media/view-global-option-sets-solution-explorer.png)

> [!NOTE]
> Some system global choices are not customizable. These options may change with updates or new versions so we recommend you don’t use them unless you are certain that your requirements align with the way that Dataverse uses these values.

### Create a global choice 

> [!NOTE]
> You do not need to create a global choice  before you use it within a custom column. When you create a new choice  column you have the option to create a new global choice  or use an existing one. See [Choice column options](create-edit-field-solution-explorer.md#choice-column-options)

While viewing global choices, click **New** to open a form to define the global choice .

![Create global choice .](media/create-global-option-set-solution-explorer.png)

Type a **Display name** that will be visible to people with the system administrator or customizer role who will choose this global choice  when defining new columns that use it. This name will not be visible to people using your apps.

A **Name** column value will be generated for you based on the **Display name** you enter. It will include the customization prefix for the Solution publisher in the context of the solution you are working in. You can change the generated portion of the **Name** column value before you save.

Type a **Description** for the global choice . 

> [!TIP]
> Use the **Description** to explain the purpose of this global choice . This value is not visible to users of the application, it is for other people with the system administrator or customizer role who may want to know why this particular global choice  was created.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]