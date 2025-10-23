---
title: "Create apps, data, and plans together"
description: Learn how the Power Apps new workspace simplifies app creation by generating plans, data models, and apps in parallel. Build smarter and faster.
author: mduelae
ms.author: mkaur
ms.reviewer: mkaur
ms.date: 10/21/2025
ms.topic: concept-article
---

# Create apps, data, and plans together

The new workspace experience in Power Apps combines plans, data models, and apps in a single design surface, enabling you to design the app, data model, and requirements together. It reduces context switching and keeps you focused. 

Key capabilities:

- **Design everything together**: Create the app, plan, and data model in a single, seamless process
- **Build faster with AI**: Iterate and prototype through chat, from idea to a working app
- **One-click app generation**: Modern web apps are created from your requirements and data

## Prerequisites

- Copilot must be enabled in the tenant and environment. Learn more: [Copilot in Power Apps overview](maker/canvas-apps/ai-overview.md).

- This capability is available only in the US region and in English only. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).


## Turn on the new experience

Follow these steps to enable the new experience in Power Apps:

1. Sign in to [Power Apps](https://make.preview.powerapps.com/).
1. In the top right, select **Try new workspace (Preview)**.
:::image type="content" source="media/new-powerapps-experience/turn-on-new-experience.png" alt-text="Screenshot of the Power Apps workspace showing the Try new workspace (Preview) toggle enabled and a tutorial pop-up explaining the feature.":::

### Turn off preview

To turn off the new experience and use the default experience using [plans](maker/plan-designer/plan-designer.md), in the lower left, select **Preview** > **Default homepage**.

## Create an app

1. Sign in to [Power Apps](https://make.preview.powerapps.com/).

   > [!IMPORTANT]
   > Make sure to turn on [Try new workspace (Preview)](new-powerapps-experience.md#turn-on-new-experience). 


1. Enter your prompt in the text box, and then select **Enter**.  

    :::image type="content" source="media/new-powerapps-experience/power-apps-prompt-textbox.png" alt-text="Screenshot of Power Apps showing a prompt input box for the new experience." lightbox="media/new-powerapps-experience/power-apps-prompt-textbox.png":::

1. Agents start working and assets load. You’ll see the plan, data model, and app preview generate. 
 
   :::image type="content" source="media/new-powerapps-experience/powerapps-data-model-app-preview.png" alt-text="Screenshot of the Power Apps new workspace showing AI agents generating the plan, data model, and app preview simultaneously." lightbox="media/new-powerapps-experience/powerapps-data-model-app-preview.png":::


1. After the plan, data, and app are generated, choose **Save** in the top‑right corner. The first save stores the app, tables, and plan together in your selected solution, while your data remains in in‑memory draft tables. This lets you iterate on the data model and app quickly without committing to a data source. When you publish the app, you then select the data source.


## Review and refine your generated app and data model

The new workspace uses a single, unified chat that keeps context as you switch between **Plan**, **Data**, and **App**. It speeds up development by letting you preview the app visually, inspect and edit code, and make inline changes—all without leaving the workspace

:::image type="content" source="media/new-powerapps-experience/plan-data-app-menu-options.png" alt-text="view plan, data, and app ":::

Each focus area shows its own tools above the work surface. In **App** focus, for example, you can choose visual preview, code view, or split view.

:::image type="content" source="media/new-powerapps-experience/app-menu-options.png" alt-text="Menu option in the App area":::


## Edit the generated app

When generation finishes, the visual preview appears in focus on the work surface.

You can explore the app directly on the work surface interact with the generated navigation items and buttons to see what’s produced and how it behaves.

To inspect the code, switch to Code view or Split view. Expand the src folder to reveal the subfolders and files that make up the app, and select any file to view the generated code.

### Edit using chat

Use the chat input on the work surface to ask questions or request changes to the generated app. For example: “What does this button do?” or “Change theme to blue.”

- If you ask a question, the agent provides an explanatory response.
- If you request a change, the agent evaluates the request, outlines an implementation plan, and then applies it.
- If the agent cannot implement the change directly, you will receive step‑by‑step guidance or instructions for retrying the request.

### Edit using inline actions

You can make pinpoint adjustments to the styling of your app using inline actions. 

 1. Select the option to toggle inline edits.
 1. Select the item you want to edit. The element is outlined and labeled with the corresponding code object so you know exactly what you’re editing.
    Depending on the element type, a properties pane or inline controls appear for typography, styling, or layout. Adjust values like font, color, or spacing directly in the pane. If multiple elements share the same style, a single change can apply across the group for example, changing a button color inside a card updates all buttons in that card group.
 
    Inline edits update the associated code directly without an AI agent involved.

    When an element is selected, open inline chat and request a change like “Make this button primary blue”. The selected element’s context is passed automatically, so you don’t have to describe it in the prompt. This is equivalent to typing the same request in the main chat but faster.

1. After editing, review the result in the visual preview; if needed, switch to Code view or Split view to inspect the generated files.

## Edit the generated plan

Focus on the plan by switching to the Plan pivot in the new workspace. Here you’ll find the generated user roles and requirements, the proposed tables for your data model, and the recommended technologies to complete your solution.

### Edit using chat

1. Open the chat on the work surface.
1. Ask questions or request changes for example, “Update the manager role,” “Add a requirement for offline access,” or “Remove the Power BI report”.
1. The agent analyzes your request and applies updates to the plan.

### Edit via inline actions

You can also make targeted edits directly inline. 

#### Edit user requirements

- Select the area you want to change and start typing, or select the **Edit** button to add new roles and requirements.
- Use inline chat while an area is selected to provide context for the agent. This saves you from describing the specific element.

#### Edit data model  -----Left off here

1. In the data model area, select the ellipsis for the specific table you'd like to edit. Alternatively, you can select to view the data workspace, save the proposed tables, or chat with the agents to pass in specific context about the edit you're requesting.

#### Edit technology

> In the technology area, select the ellipsis beside any recommended technology to remove it from the plan. You can also add new technologies or chat with the agent with specific context for the change you're requesting.

## Editing the generated data model

1. Focus on the data model by switching to the Data pivot in the workspace. Here you can see all the proposed data for the solution, the relationships between tables, and sample data to help you understand the proposed schema and to illustrate how the data is used in the generated app. These tables are in-memory and are not published yet to any data source, you will have all the flexibility to iterate on them so they can meet your business requirements.

### Edit using chat

  Ask questions and make changes to the proposed data via the chat—just ask for updates to the proposed fields, tables, and relationships. Ask for more sample data to get a rich data set for your proposed app. The agents will analyze your request and make the necessary updates.

  Note: not all actions are supported via the agent chat. See Known limitations for more details.

### Edit via inline actions

Add new or existing tables, and also remove or make targeted edits to relationships, tables, and sample data. Select the relationship line or the ellipsis of the table you'd like to edit. From here you can remove the relationship or table from the data model or make edits.

### Add table

Select **Add table** button from the command bar to add a new or existing table to your data model. Select Draft table if you want to create a new in-memory table from scratch. Select Existing Dataverse table or Existing SharePoint list if you want to bring your existing data to this solution.

### Add and edit relationship

1. Select **Add relationship** button from the command bar to add a new relationship between two tables.

1. To edit a relationship, select the relationship line between two tables and select edit from the dropdown menu. Here you can change the relationship type or add a lookup column. You can also perform advanced edits like changing the logical names used in the relationship.

1. Some relationship configurations are currently not supported. See Known limitations for more details.

### Remove

To remove a table from your solution, first select a table from the canvas, then select **Remove** from the command bar. When a Draft table is selected, this will delete the table and all associated table rows. When an existing Dataverse table or SharePoint list is selected, Remove doesn't delete the table and associate rows.

### View data

Select **View data** from the command bar or the context menu available under the ellipsis for the table you would like to edit. Here you can add, remove, and edit columns and rows of data.

### Row ownership

Edit row ownership from the context menu or data view drawer. Select the row ownership option from either location to change the ownership type to User or Team or Organization.

### Properties

Edit table properties from the context menu or data view drawer.

When you make changes to the app, plan, or data, the agent performs an analysis to determine whether updates are needed to the other parts of the solution. If changes are required, the agent proactively makes them and outlines the changes made in the chat.

## ALM capabilities

**Save**: Auto-save is not supported yet. Select Save in the command bar at any time to save the progress of your solution. Selecting save will save all edits to all solution objects to your preferred solution.

**Publish**:

- **Publishing data**: Select **Publish draft tables** from the context menu of data card when you're ready to commit your table for production use. Choose between Dataverse or SharePoint as a target data source. Once the draft tables are published, the apps using the draft tables are automatically updated to use the published tables as well.

- **Publishing app**: Select **Publish** button on the command bar of the app when you're ready to publish the app for production use. If there's any draft table being used by the app, you're prompted to publish those draft tables as well.

**Share the app:** You can share your app with others for them to use. Select the **Share** button and add the accounts you'd like to be able to run the created app.

## Provide feedback

Share your feedback about the generated content or the experience at any time by using either the thumbs icons in the chat pane or the feedback icon in the command bar.

- **Provide feedback using thumbs:** to provide feedback about the generated content, use the thumbs in the chat pane. Provide additional details by selecting "Tell us why."

- **Provide feedback about the experience:** to provide feedback about the overall experience, use the Feedback icon in the command bar. Select the category of feedback you want to provide and then share the details in the provided input.

## Known limitations

- The new workspace can only be used in one browser tab at a time. Working in multiple browser tabs may result in unexpected behavior.

- Only one app will be recommended/allowed in the new workspace per solution at this time

- Individual components of a generated solution cannot be saved individually at this time

- Pre-existing plans can't be opened in OWS

- Canvas and model apps aren't recommended

- You can't open or edit canvas and model apps in OWS

- <span class="mark">Apps created can be shared with users, but cannot be shared with additional co-owners at this time</span>

- Existing tables aren't automatically recommended during data model proposal. Makers need to manually add the existing tables to be included in their solution.

- Editing existing Dataverse tables and SharePoint lists via chat isn't supported yet.

- Inline editing on SharePoint lists isn't supported yet. Makers can select **Edit in new tab** to edit the SharePoint list from the SharePoint site. Some relationship configurations currently aren't supported, including many-to-many relationship between any table, many-to-one relationship between existing table and new table, and any relationship between existing tables across different data sources (for example, relationship between SharePoint list and Dataverse table).

- Previously created Code apps are only editable from OWS

- Code view/Split view doesn't support direct edits of code at this time.

  - <span class="mark">^ this means that code apps in the apps list/home page might have edit disabled in the context menu – makers will have to open the plan to edit the app</span>

  - If you export a code app and edit it outside of OWS (in VS Code for example), you might not be able to further edit it in OWS if you re-import it.

  - Undo is only available by asking in the chat.

  - Proposed technologies (apart from code apps) can't be directly created from the plan at this time.



## Choose a data source and publish

1. When you’re ready to publish, on the top right select **Publish**.

1. Select a data source to publish and store the draft tables in your app and then select **Publish**.

    :::image type="content" source="media/new-powerapps-experience/save-and-select-data-source.png" alt-text="Select a data source":::