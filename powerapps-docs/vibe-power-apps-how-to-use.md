---
title: "Create apps, data, and plans together"
description: Learn how the Power Apps new experience simplifies app creation by generating plans, data models, and apps in parallel. Build apps smarter and faster.
author: mduelae
ms.author: mkaur
ms.reviewer: mkaur
ms.date: 11/06/2025
ms.topic: concept-article
---

# Create apps, data, and plans together (preview)


[This article is prerelease documentation and is subject to change.]

The new experience in Power Apps combines plans, data models, and apps in a single design surface. This combination lets you design an app, data model, and requirements together. It reduces context switching and keeps you focused. 

Key capabilities

- **Design everything together**: Create apps, plans, and data models in a single, seamless process.
- **Build faster with AI**: Iterate and prototype through chat, from idea to a working app.
- **One-click app generation**: Modern web apps are created from your requirements and data.


> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.


## Create an app

1. Sign in to [Power Apps](https://make.preview.powerapps.com/).

   > [!IMPORTANT]
   > Make sure to turn on [Try new workspace (Preview)](vibe-power-apps-overview.md#turn-on-the-new-experience). 


1. Enter your prompt in the text box, and then select **Enter**.  

    :::image type="content" source="media/vibe-powerapps-experience/power-apps-prompt-text-box.png" alt-text="Screenshot of Power Apps showing a prompt input box for the new experience." lightbox="media/vibe-powerapps-experience/power-apps-prompt-text-box.png":::

1. Agents start working and assets load. You’ll see the plan, data model, and app preview generate. 
 
   :::image type="content" source="media/vibe-powerapps-experience/powerapps-data-model-app-preview.png" alt-text="Screenshot of the Power Apps new workspace showing AI agents generating the plan, data model, and app preview simultaneously." lightbox="media/vibe-powerapps-experience/powerapps-data-model-app-preview.png":::


1. After the plan, data, and app are generated, choose **Save** in the top-right corner. The first save stores the app, tables, and plan together in your selected solution, while your data remains in in-memory draft tables. This lets you iterate on the data model and app quickly without committing to a data source. When you publish the app, you then select the data source.


## Review and refine your generated app and data model

The new workspace uses a single, unified chat that keeps context as you switch between **Plan**, **Data**, and **App**. It speeds up development by letting you preview the app visually, inspect and edit code, and make inline changes all without leaving the workspace.

:::image type="content" source="media/vibe-powerapps-experience/plan-data-app-menu-options.png" alt-text="view plan, data, and app ":::

Each focus area displays its specific tools above the work surface. For instance, when the **App** focus area is selected, you will see these options:

:::image type="content" source="media/vibe-powerapps-experience/app-menu-options.png" alt-text="Menu option in the App area":::

Legend:

1. **App**: When selected, this focus area displays menu options specific to the app.
1. **Preview**: View a live preview of the app.
1. **Code**: Access and review the app’s code.
1. **Split**: See both the code and the app preview side by side.
1. **Refresh preview**: Reload the app preview to see the latest changes.


## Edit the generated app

When generation finishes, the visual preview appears in focus on the work surface.

Once generation is complete, the visual preview appears in focus on the work surface. You can interact with the app directly, using the navigation items and buttons to see how they function and respond.

To inspect the code, switch to **Code** view or **Split** view. Expand the **src** folder to see subfolders and files, then select any file to view the generated code.

When you modify the app, plan, or data, the agent analyzes your changes to see if updates are needed elsewhere in the solution. If so, updates are automatically applied and summarized in the chat.

### Edit the app using chat

Use the chat input on the work surface to ask questions or request changes to the generated app. For example: “What does this button do?” or “Change theme to blue.”

- If you ask a question, the agent provides an explanatory response.
- If you request a change, the agent evaluates the request, outlines an implementation plan, and then applies it.
- If the agent can't implement the change directly, you receive step-by-step guidance or instructions for retrying the request.

### Edit the app using inline actions

Use inline actions to edit the style of your app.

 1. Select the option to toggle inline edits.
 1. Select the item you want to edit. The element is outlined and labeled with the corresponding code object so you know exactly what you’re editing.
    Depending on the element type, a properties pane or inline controls appear for typography, styling, or layout. Adjust values like font, color, or spacing directly in the pane. If multiple elements share the same style, a single change can apply across the group for example, changing a button color inside a card updates all buttons in that card group.
 
    Inline edits update the associated code directly without an AI agent involved.

    When an element is selected, open inline chat and request a change like **Make this button primary blue**. The selected element’s context is passed automatically, so you don’t have to describe it in the prompt. This is equivalent to typing the same request in the main chat but faster.

1. When you're done, review the result in the visual preview; if needed, switch to **Code** view or **Split** view to inspect the generated files.

## Edit the generated plan

Select **Plan** to edit the plan. The plan shows generated user roles and requirements, the proposed tables for your data model, and the recommended technologies to complete your solution.

:::image type="content" source="media/vibe-powerapps-experience/edit-plan.png" alt-text="Edit the plan pivot":::

### Edit the plan using chat

Open the chat and enter your questions or request changes, such as:

- Update the manager role
- Add a requirement for offline access
- Remove the Power BI report

The agent analyzes your request and applies updates to the plan. You can also make targeted edits directly inline.

#### Edit user requirements

Select the area you want to change and start typing, or select the **Edit** button to add new roles and requirements. Use inline chat while an area is selected to provide context for the agent. This approach saves you from describing the specific element.

:::image type="content" source="media/vibe-powerapps-experience/edit-user-roles.png" alt-text="Select Edit to make edits to user roles":::

#### Edit data model 

In the **Data model** area, select the ellipsis for the specific table you’d like to edit.

:::image type="content" source="media/vibe-powerapps-experience/edit-data-model.png" alt-text="Edit a data table":::

You can select to view the data workspace, save the proposed tables, or chat with the agents to pass in specific context about the edit you’re requesting.

#### Edit technology

In the **Technology** area, select the ellipsis beside any recommended technology to remove it from the plan. You can also add new technologies or chat with the agent with specific context for the change you're requesting.

## Editing the generated data model

Select **Data** and review and refine your data. The data view displays all proposed tables, their relationships, and sample data, helping you understand the schema and how data's used in the generated app. The tables are currently in-memory only and haven't been published to any data source, giving you full flexibility to modify them until they meet your business needs.  For more information, see [Create and edit tables using Power Apps](maker/data-platform/create-edit-entities-portal.md)

:::image type="content" source="media/vibe-powerapps-experience/edit-data-model-details.png" alt-text="Edit the data for your app":::

Legend

1. Add table 
1. Create relationships
1. Data view
1. Remove


### Edit data using chat

Use the chat to ask questions or request changes to the proposed fields, tables, and relationships.

You can also ask for additional sample data to enrich your dataset for the app.
The agents will analyze your requests and make the necessary updates.

Some actions might not be supported through agent chat. For details review the [limitations](vibe-power-apps-how-to-use.md#known-limitations)


### Edit data using inline actions

Add new or existing tables, or make targeted changes to relationships, tables, and sample data directly within the workspace.

1. To edit, select the relationship line or the ellipsis (…) next to the table you want to modify.
1. Select **Remove** to remove relationships or tables from the data model, or make specific edits as needed.

    :::image type="content" source="media/vibe-powerapps-experience/edit-data-relationships.png" alt-text="Edit data relationships":::

### Add table

1. Select the **Add table** button in the command bar to include a new or existing table in your data model.
2. Choose **Draft table** to create a new in-memory table from scratch, or select **Existing Dataverse table** or **Existing SharePoint list** to add data you already have.

    :::image type="content" source="media/vibe-powerapps-experience/add-tables.png" alt-text="Add more data tables":::

### Add and edit relationship

1. Select **Add relationship** button from the command bar to add a new relationship between two tables.

1. To edit a relationship, select the relationship line between two tables and select edit from the dropdown menu. Here you can change the relationship type or add a lookup column. You can also perform advanced edits like changing the logical names used in the relationship.

1. Some relationship configurations currently aren't supported. See Known limitations for more details.

### Remove a table

1. Select the table you want to remove.
2. Select **Remove** in the command bar.

   - If you remove a draft table, it will be deleted along with all its rows.
   - If you remove an existing Dataverse table or SharePoint list, the table and its data remain in the original source; only the reference is removed from your solution.

### View and edit data

1. Select **View data** from the command bar.
   :::image type="content" source="media/vibe-powerapps-experience/view-edit-data.png" alt-text="View and edit data"::: 
1. In this view, you can add, remove, or modify columns and rows as needed.

### Row ownership

Follow one of these steps to change the ownership type to User, Team, or Organization:

- Select **View options** and then select **Row ownership**.

  :::image type="content" source="media/vibe-powerapps-experience/edit-row-ownership.png" alt-text="Edit the row ownership":::

- Select **View data** on the command bar, select a row, and then select **Row ownership**.

  :::image type="content" source="media/vibe-powerapps-experience/edit-row-ownership-detailed-view.png" alt-text="Edit the row relationship from the detailed view":::

### Edit table properties

1. Select the table you want to edit and then select **View data** in the command bar.
2. Select **Properties** to update the table’s display name, plural name, description, and other details.

 :::image type="content" source="maker/canvas-apps/media/tables/edit-table-properties.png" alt-text="Edit table properties":::


## Application lifecycle management (ALM) capabilities

The following [ALM](/power-platform/alm/overview-alm) features are supported: 

- **Save**: Auto-save isn't currently available. To save your progress, select **Save** in the command bar at any time. This action saves all edits to every solution object in your preferred solution.
- **Publish data**: To publish draft tables, select **Publish draft tables** from the data card’s context menu when you’re ready to make a table available for production. You can choose either Dataverse or SharePoint as the target data source. Once published, any apps using these draft tables will automatically update to use the published versions.

- **Publishing app**: When you’re ready to release your app for production, select **Publish** in the app’s command bar. If your app uses any draft tables, you’ll be prompted to publish those tables as well.

- **Share the app**: To share your app with others, select **Share** and add the accounts of users you want to grant access to run the app.


## Choose a data source and publish

1. When you’re ready to publish, on the top right select **Publish**.

1. Select a data source to publish and store the draft tables in your app and then select **Publish**.

    :::image type="content" source="media/vibe-powerapps-experience/save-and-select-data-source.png" alt-text="Select a data source":::

## Known limitations

The following are limitations of the new Power Apps experience:

- The new experience can only be used in one browser tab at a time. Using multiple tabs might cause unexpected behavior.

- Only one app is currently supported per solution.

- Individual components of a generated solution cannot be saved separately.

- Pre-existing plans cannot be opened in the new experience.

- Canvas and model-driven apps are not recommended or supported. You also can't open or edit canvas and model-driven apps in the new experience.

- Apps can be shared with users, but adding additional co-owners is not supported.

- Existing tables are not automatically suggested during data model creation. Makers must manually add any existing tables they want to include.

- Editing existing Dataverse tables and SharePoint lists via chat is not yet supported.

- Inline editing for SharePoint lists is not supported. To edit a SharePoint list, select **Edit in new tab** to open it on the SharePoint site.
- Some relationship configurations are not supported, including:
  - Many-to-many relationships between any tables
  - Many-to-one relationships between an existing table and a new table
  - Relationships between existing tables across different data sources (e.g., between a SharePoint list and a Dataverse table).

- Previously created code apps can only be edited in the new experience. 

- Code view and split view do not currently support direct code editing.
  - As a result, code apps in the app list or home page may have the edit option disabled in the context menu. Makers must open the plan to edit the app.
  - If you export a code app and edit it outside of OWS (such as in Visual Studio Code), you might not be able to edit it further in OWS after re-importing.

- Undo is only available by making a request in the chat.

- Technologies other than code apps cannot be created directly from the plan at this time.

## Share your feedback 

- **Feedback on generated content**: Use the thumbs up or thumbs down icons in the chat pane to rate the generated content. For more details, select **Tell us why** to provide specific feedback.

- **Feedback on the overall experience**: Select **Give feedback** in the command bar to share your thoughts about the overall experience. Choose a feedback category and enter your comments in the provided field.
 :::image type="content" source="media/vibe-powerapps-experience/give-feedback.png" alt-text="Provide feedback":::
