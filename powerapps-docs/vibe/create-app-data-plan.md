---
title: "Create Apps, Data, and Plans With Power Apps Vibe"
description: Learn how Power Apps vibe simplifies app creation by generating plans, data models, and apps in parallel. Build modern web apps faster with AI assistance.
author: mduelae
ms.author: mkaur
ms.reviewer: mkaur
ms.date: 01/29/2026
ms.topic: concept-article
ms.custom: vibe
---

# Create apps, data, and plans together using vibe (preview)


[This article is prerelease documentation and is subject to change.]

The new vibe experience in Power Apps combines plans, data models, and apps in a single design surface. This integrated approach minimizes distractions and keeps you focused on building solutions efficiently.

Key capabilities

- **Design everything together**: Build apps, plans, and data models together in a single, cohesive process.
- **Build faster with AI**: Quickly move from ideas to working prototypes with conversational chat.
- **Instant app creation**: Generate modern web apps directly from your requirements and data with one click.


> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.


## Create an app

1. Sign in to [https://vibe.powerapps.com](https://vibe.powerapps.com/).

1. Enter your prompt in the text box. **Plan** mode is the default mode, which means it starts with a plan that includes potential clarifying questions before building the app. You can also select **Start dictation** and use your voice to turn speech into text.

    > [!TIP]
    > To skip planning and start creating apps, select **Plan** again to turn it off.

    :::image type="content" source="media/create-app-data-plan/prompt-text-box.png" alt-text="Screenshot of prompt input box where you enter a description to create an app." lightbox="media/create-app-data-plan/prompt-text-box.png":::


1. In **Plan** mode, the agent shows you a proposed plan to review before generating the app. It might also ask follow-up questions to clarify your requirements.
 
1. When the plan looks good, select **Accept this plan and create app** > **Submit** to start generating your app. 

1. The agent starts working and loads assets. When it's finished, you have a generated app, data model (if applicable), and a plan (if applicable). You can then make any necessary edits.
    
1. The first save stores the app, tables, and plan together in your selected solution, while your data remains in draft tables (in memory). If you don't see a **Save** button in the top right of the screen, your app is autosaved automatically. 


## Review and refine your generated app and data model

The new workspace uses a unified chat experience that keeps context as you switch between **Plan**, **Data**, and **App**. It speeds up development by letting you preview the app visually, inspect the code, and make changes without leaving the workspace.

:::image type="content" source="media/create-app-data-plan/plan-data-app-menu-options.png" alt-text="Screenshot of the Plan, Data, and App menu options in the workspace.":::

A list of next actions appears above the chat area to suggest relevant next steps.

:::image type="content" source="media/create-app-data-plan/edit-app.png" alt-text="Screenshot of suggested next actions above the chat area for editing generated app components." lightbox="media/create-app-data-plan/edit-app.png":::

If you submit a request and then decide to cancel it, select the stop button.

:::image type="content" source="media/create-app-data-plan/cancel-chat.png" alt-text="Screenshot of the stop button used to cancel a chat request in Power Apps vibe.":::

## Focus area

Each focus area displays its specific tools above the work surface. For instance, when you select the **App** focus area, you see these options:

:::image type="content" source="media/create-app-data-plan/app-menu-options.png" alt-text="Screenshot of the menu options available in the workspace.":::

Legend:

1. **App**: When selected, this focus area displays menu options specific to the app.
1. **Preview**: View a live preview of the app.
1. **Code**: Access and review the app’s code.
1. **Split**: See both the code and the app preview side by side.
1. **Toggle inline edits**: Select any area in the app and edit its text directly.
1. **Refresh preview**: Reload the app preview to see the latest changes.
1. **Select preview screen size**: Choose **Desktop**, **Tablet**, or **Mobile** to see how your app renders across screen sizes and orientations.
1. **Play**: Run the app to test behavior and interactions. Use the drop-down to show a QR code, then scan it to open the app on your mobile device in a browser.


## Edit the generated app

When generation finishes, the visual preview appears in focus on the work surface.

You can interact with the app directly, using the navigation items and buttons to see how they function and respond.

To inspect the code, switch to **Code** view or **Split** view. Expand the **src** folder to see subfolders and files, and select any file to view the generated code.

When you modify the app, plan, or data, the agent analyzes your changes to see if updates are needed elsewhere in the solution. If so, the agent automatically applies updates and summarizes them in the chat.

### Edit the app using chat

Use the chat input on the work surface to ask questions or request changes to the generated app. For example: "What does this button do?" or "Change theme to blue."

- **Plan mode**: To discuss potential changes with the agent before applying them, select **Plan** in the chat box. The agent proposes a plan for your review. Once you accept it, the agent executes the plan and makes the necessary edits. When the edits are complete, **Plan** mode turns off automatically.

- **Questions**: If you ask a question, the agent provides an explanatory response.
- **Change requests**: If you request a change, the agent evaluates the request, outlines an implementation plan, and then applies it.
- **Unsupported changes**: If the agent can't implement the change directly, you receive step-by-step guidance or instructions for retrying the request.

### Edit the app using inline actions

Use inline actions to edit the style of your app.

 1. Select the option to toggle inline edits.
 1. Select the item you want to edit. The element is outlined and labeled with the corresponding code object so you know exactly what you're editing.

    Depending on the element type, a properties pane or inline controls appear for typography, styling, or layout. Adjust values like font, color, or spacing directly in the pane.

    > [!TIP]
    > If multiple elements share the same style, a single change applies across the group. For example, changing a button color inside a card updates all buttons in that card group.
 
    Inline edits update the associated code directly without involving the AI agent.

    You can also open inline chat on a selected element and request a change like **Make this button primary blue**. The element's context is passed automatically, so you don't need to describe it in the prompt.

1. When you're done, review the result in the visual preview. If needed, switch to **Code** view or **Split** view to inspect the generated files.


### Keyboard shortcuts for inline actions

Use keyboard shortcuts to open and close inline edit actions while editing your app.

- **Hold and release Alt** to toggle the inline edit gesture.
- **Press Esc** to dismiss the inline edit gesture.

## Edit the generated data model

Select **Data** to review and refine your data model. The data view displays all proposed tables, their relationships, and sample data to help you understand the schema and how the generated app uses the data. The tables exist in memory only and aren't published to a data source until you explicitly publish them. You can modify them until they meet your business needs. For more information, see [Create and edit tables using Power Apps](../maker/data-platform/create-edit-entities-portal.md).


:::image type="content" source="media/create-app-data-plan/edit-data-model-details.png" alt-text="Screenshot of the data model editor showing tables, relationships, and sample data." lightbox="media/create-app-data-plan/edit-data-model-details.png":::

Legend

1. **Data**: Edit the data model directly in this view.
1. **Add table**: Add a draft or existing table.
1. **Create relationships**:  Creates a table relationship between two tables.
1. **Data view**: View the data workspace experience where you create tables, configure table relationships, and can view a diagram of your data.
1. **Remove**: Deletes the table and all associated table rows.


### Edit data using chat

Use the chat to ask questions or request changes to the proposed fields, tables, and relationships.

You can also ask for more sample data to enrich your dataset for the app.
The agent analyzes your requests and makes the necessary updates.

Some actions might not be supported through agent chat. For more information, see the [limitations](create-app-data-plan.md#known-limitations) section in the article.

### Edit data using inline actions

Add new or existing tables, or make targeted changes to relationships, tables, and sample data directly within the data workspace.

1. To edit data, select the relationship line or the ellipsis (...) next to the table you want to modify.
1. Select **Remove** to remove relationships or tables from the data model, or make specific edits as needed.

    :::image type="content" source="media/create-app-data-plan/edit-data-relationships.png" alt-text="Edit data relationships":::

### Add a data table

1. Select **Add table** in the command bar to include a new or existing table in your data model.
1. Choose **Draft table** to create a new in-memory table from scratch, or select **Existing Dataverse table** to add data you already have.

    :::image type="content" source="media/create-app-data-plan/add-tables.png" alt-text="Add more data tables":::

> [!NOTE]
> You can also add SharePoint data. For more information, [Add a SharePoint list in Power Apps vibe](add-data-source-sharepoint-lists.md).

### Add and edit relationship

1. Select **Add relationship** in the command bar to add a new relationship between two tables.

1. To edit a relationship, select the relationship line between two tables and select **Edit** from the dropdown menu. Change the relationship type or add a lookup column. You can also perform advanced edits like changing the logical names used in the relationship.

1. Some relationship configurations currently aren't supported. For more information, see [Known limitations](create-app-data-plan.md#known-limitations).

### Remove a data table

1. Select the table you want to remove.
1. Select **Remove** in the command bar.

   - If you remove a draft table, you delete it along with all its rows.
   - If you remove an existing Dataverse table, the table and its data remain in the original source; you only remove the reference from your solution.

### View and edit data in a table

1. Select **View data** from the command bar.
   :::image type="content" source="media/create-app-data-plan/view-edit-data.png" alt-text="View and edit data"::: 
1. In this view, you can add, remove, or modify columns and rows as needed.

### Row ownership

To change the ownership type to **User**, **Team**, or **Organization**, use one of the following methods:

1. Select **View options**, and then select **Row ownership**.

   :::image type="content" source="media/create-app-data-plan/edit-row-ownership.png" alt-text="Edit the row ownership":::

1. Select **View data** on the command bar, select a row, and then select **Row ownership**.

   :::image type="content" source="media/create-app-data-plan/edit-row-ownership-detailed-view.png" alt-text="Edit the row relationship from the detailed view":::

### Edit the data table properties

1. Select the table you want to edit. Then, select **View data** in the command bar.
1. Select **Properties** to update the table’s display name, plural name, description, and other details.

 :::image type="content" source="media/create-app-data-plan/edit-table-properties.png" alt-text="Edit table properties":::



## Application lifecycle management (ALM) capabilities

The following [ALM](/power-platform/alm/overview-alm) features are supported: 

- **Save**: For new apps created after April 9, 2026, AutoSave is turned on by default. You don't need to manually select save. For apps created before this date, manual saving is still required. To save your progress, select **Save** in the command bar at any time. This action saves all edits to every solution object in your preferred solution.
  
- **Publish data**: To publish draft tables, select **Publish draft tables** from the data card’s context menu when you're ready to make a table available for production. You can choose Dataverse as the target data source. Once published, any apps using these draft tables automatically update to use the published versions.

- **Publishing app**: When you're ready to release your app for production, select **Publish** in the app’s command bar. If your app uses any draft tables, you're prompted to publish those tables as well.

- **Share the app**: To share your app with others, select **Share** and add the accounts of users you want to grant access to. You can also share with Microsoft Entra ID security-enabled groups. Distribution lists and nonsecurity Microsoft 365 Groups aren't supported. 

  > [!NOTE]
  > Group sharing only works in production environments. Developer environments don't support group-level permissions.

## Choose a data source and publish

1. When you're ready to publish, select **Publish**.

1. Your Dataverse tables are published in the same environment. 

## Known limitations

The new Power Apps experience has the following limitations:

- You can't access or edit apps created in the new authoring experience outside of the new authoring experience.
- If you export an app and edit it outside the new authoring experience (for example, in VS Code), redeploying via PAC CLI creates a new app, and it disconnects from the original plan.
- Currently, you can only have one app per plan; multiple apps within a single plan aren't supported.
- You can't open preexisting plans in the new experience.
- Canvas and model-driven apps aren't supported; you can't recommend, open, or edit these app types in the new authoring experience.
- Existing tables aren't automatically recommended during data model proposal; you can manually add existing tables to your plan.
- Editing existing Dataverse tables via chat isn't currently supported; you can make changes to these tables through the data editor manually.
- Direct code edits in **Code** view or **Split** view aren't supported; you can't modify code directly in these views.


## Share your feedback 

- **Feedback on generated content**: Use the thumbs up or thumbs down icons in the chat pane to rate the generated content. For more details, select **Tell us why** to provide specific feedback.

- **Feedback on the overall experience**: Select **Give feedback** in the command bar to share your thoughts about the overall experience. Choose a feedback category and enter your comments in the provided field.
 :::image type="content" source="media/create-app-data-plan/give-feedback.png" alt-text="Provide feedback":::

## See also

[FAQ for the Power Apps vibe experience (preview)](../maker/common/faq-vibe.md)
