---
title: Create a choice column
description: Step-by-step instructions for how to create a choice in Power Apps.
author: lancedMicrosoft
ms.component: cds
ms.topic: how-to
ms.date: 05/07/2025
ms.subservice: dataverse-maker
ms.author: lanced
search.audienceType: 
  - maker
---
# Create a choice

Choice columns allow you to include dropdown lists of fixed values to a user within your app to ensure data consistency. Choice columns, were formerly referred to as option sets and are sometimes called picklists. Similar to tables, there are both standard choices or makers have the ability to create custom choice columns to use in apps.

Choices can be created while working from a solution in powerapps.com or on a table form in the form designer.

Choice columns can be single selection only (choice) or can allow multi-selection (choices). The following screenshot shows a multi-select choices column in a model-driven app.

:::image type="content" source="media/data-platform-cds-newoptionset/multi-select-choice.png" alt-text="A multi-select choices column displayed on a model-driven app main form":::

Choices are either global or local. You can define a choice to use a set of options defined elsewhere (globally) which can be made available to other choice columns, or define a set of options only available within the choice column (locally). More information: [Create and edit choice columns overview](create-edit-global-option-sets.md)

## Create a global choice within a solution

1. Sign into [powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions**, and then open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. On the command bar, select **New** > **Choice**.
1. Enter the following properties:
   - **Display name**.  Enter the **Display name** for your column. The **Display name** is used when presenting this column to your users.
   - In the **Label** field, enter the label you want displayed for the choice option.
   - The **Value** number represents a unique value for the option and isn't displayed in the choice column in an app. Notice there's a number generated for each **Value** automatically. We recommend that you not change this. Having a unique **Value** helps ensure that the value will be different from other option values that might be defined in other solutions and imported into your environment.
   - Select the color picker to the left of the **Label** if you want a color to appear for the option in model-driven app charts.
   - **Additional properties**.
      - **Description**. Add a description for the option.
      - **External value**. This value is used for virtual tables to map a value in an external data source with this option.
      - **Hidden**. Hide the option from the choice column at runtime in apps.

1. Select **New choice** to create another option for the choice.
1. Repeat the previous step to until you have the options you want for the choice.
1. Expand **Advanced options** to display additional properties: 
   - **Name**. Unique name of the global choice including the solution publisher prefix.
   - **External type name**. This value is used for virtual tables to map a value in an external data source with this choice.
   - **Description**. Enter an optional description for the choice column.
1. Select **Save**.

> [!IMPORTANT]
> Global choices can't be directly added to an app. After you create a global choice column the options from the choice can be made available when you create a local choice column. Local choice columns are table specific and can then be used with forms and views in an app.

## Create a local choice to use in forms and views

Create a local choice column for a table that can be used in forms and views within a solution.

1. Sign into [powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions**, and then open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

1. Open the table where you want to create the local choice, and then on the command bar, select **New** > **Choice**.

1. In the **New column** panel, enter properties for the choice column.

### Configure properties for a local choice

- **Display name**.  Enter the **Display name** for your column. The **Display name** is used when presenting this column to your users.
- **Description**. Enter an optional description of the choice column.
- **Data type**. Select **Choice** > **Choice**. Select **Choice** > **Yes/No** if you want a two option single select choice field.
- **Behavior**. Select calculated to enable the column to be included in calculated columns to automate manual calculations.
- **Required**. Setting this to **Business required** makes it so a record can't be saved without data in this column.
- **Searchable**. When selected, this column appears in Advanced Find and is available when customizing views.
- **Selecting multiple choices is allowed**. Select this option if you want to create a choice where the user can select more than one option (multi-select).
- **Sync with global choice?**
   - **Yes**. Select this option if you want the local choice to have the ability to use options from a global choice. Then, you can also select an existing global choice to use the options from that global choice.
   - **No**. Select this option if you don't want the choice to have the ability to use options from a global choice.
   - **Sync this choice with**. When **Sync with global choice** is **Yes**, you can select an existing choice column. Then, the options configured for that choice can be used for this choice.
   - If you chose **No** to enable a global choice, create the options for your choice by selecting **Choices** or, if you chose **Yes**, select **Edit choice** to edit the sync choice options or **New choice** to add new options:
   - In the **Label** field, enter the label you want displayed for the choice option.
   - The **Value** number represents a unique value for the option and isn't displayed in the choice column in an app. Notice there's a number generated for each **Value** automatically. We recommend that you not change this. Having a unique **Value** helps ensure that the value will be different from other option values that might be defined in other solutions and imported into your environment.
   - Select the color picker to the left of the **Label** if you want a color to appear for the option in model-driven app charts.
- **Default choice**. Select one of the options you created as the default choice.
- **Schema name**. This is the unique name used by the system and is automatically generated based on the display name and solution publisher prefix. After a new choice column is saved, you can't change this.
- **Enable column security**. Select this to allow for securing the data in the column beyond the security defined for the table.
- **Enable auditing.** If auditing has been enabled in the environment, this column can be included in change tracking.
- **Appears in dashboard's global filter**. Select this option to allow column to be available as a filter in interactive dashboards.
- **Sortable**. Select this option to allow sorting of this column when used in interactive dashboards.

Select **Save**.

Now the local choice column appears in the form and view designers to add for the table.

## Create and edit global choices using solution explorer

For information about how to create and edit global choices using the classic solution explorer, go to [Create or edit a global option set (on-premises)](/dynamics365/customerengagement/on-premises/customize/create-edit-global-option-sets).
<!-- Solution explorer provides one way to create and edit global choices for Dataverse.

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
> Use the **Description** to explain the purpose of this global choice . This value is not visible to users of the application, it is for other people with the system administrator or customizer role who may want to know why this particular global choice  was created. -->

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
