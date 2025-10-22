---
title: Work in the new workspace
description: Learn to edit generated apps with visual previews, code views, and inline actions. Make precise changes or collaborate with agents for seamless updates.
author: mduelae
ms.author: mkaur
ms.reviewer: mkaur
ms.date: 10/22/2025
ms.topic: concept-article
ms.service: powerapps
ms.subservice: code-apps
---

The new workspace has a single unified chat that lets you work with powerful agents and keep context as you pivot focus between your app, plan, and data. Switch focus using the pivots above the work surface or pop out a navigation menu to move between proposed objects at a more granular level. Each focus area has specific tools available to it above the work surface, like expanding/collapsing plan cards in Plan focus or choosing between visual preview, code view, or split view in the app focus. You can see all of the agents contributing to your generated solution. Finally, you can save, publish, and share the generated objects (see more in the section below).

## Editing the generated app

Once the generation steps complete, you will see the visual app preview in focus on the work surface.

You can explore the app by interacting with it in the work surface just as you would with any app – you can click on the generated navigation items or buttons in the app to see what has been generated and how it behaves.

1. You can also explore the app through code by selecting code view or split view. Expanding the src folder will show you the subfolders and files which make up the app. Select a file to see the generated code.

### Edit via chat

 You can ask questions about or make edits to the generated app through the chat in the provided text input field. Examples are like: what does this button do? Or change theme to blue. Depending on whether you ask a question or request a change, you'll either see a response to the question or the agent thinking about the request, determining an implementation plan, and then implementing. NOTE: if the agent is unable to do the implementation plan itself, you may receive steps on how you can implement the change or guidance on how to retry the request.

### Edit via inline actions

 You can make pinpoint adjustments to the styling of your app via inline actions. To begin, select the option to toggle inline edits. Then, select the item on the work surface that you'd like to edit. You'll see the objects in the app get outlined with a label for what code object you're editing. Depending on the type of object selected on the canvas, you may see visual options to edit the typography, styling, or layout. The requested edit may also impact multiple objects on the screen if they share the same style. For example, select a button inside of a card and change the color, all buttons in the associated card group will also change color.

These types of edits directly change the associated code without AI involvement.

1. You can also use inline chat to ask for edits while giving the agent specific context for the object you're requesting to edit. Which is equivalent to you directly type in the chat but saves you the effort of specifying context.

## Editing the generated plan

1. Focus on the plan by switching to the Plan pivot in the new workspace. Here you will see the user roles and requirements generated for the solution, as well as the proposed tables for the data model. Finally, you will see proposed technologies to complete your solution.

### Edit via chat

    1. You can ask questions and make changes to the plan via the chat – just ask for updates to the user roles, requirements, tables, or technologies. The agent will analyze your request and make the necessary updates.

### Edit via inline actions

> You can also make targeted edits directly inline.

### Edit user requirements

> In the user requirements section, click in the area that you'd like to make a change and start typing. You can also select the edit button to manually add new roles and requirements. You can chat inline to give the agent specific context for the change you're requesting.

### Edit data model

1. In the data model area, select the ellipsis for the specific table you'd like to edit. Alternatively, you can select to view the data workspace, save the proposed tables, or chat with the agents to pass in specific context about the edit you're requesting.

### Edit technology

> In the technology area, select the ellipsis beside any recommended technology to remove it from the plan. You can also add new technologies or chat with the agent with specific context for the change you're requesting.

## Editing the generated data model

1. Focus on the data model by switching to the Data pivot in the workspace. Here you can see all the proposed data for the solution, the relationships between tables, and sample data to help you understand the proposed schema and to illustrate how the data is used in the generated app. These tables are in-memory and are not published yet to any data source, you will have all the flexibility to iterate on them so they can meet your business requirements.

### Edit via chat

    1. You can ask questions and make changes to the proposed data via the chat- just ask for updates to the proposed fields, tables, and relationships. You can even ask for more sample data to get a rich data set for your proposed app. The agents will analyze your request and make the necessary updates.

    1. Note: not all actions are supported via the agent chat yet. See Known limitations for more details.

### Edit via inline actions

> You can add new or existing tables, and also remove or make targeted edits to relationships, tables, and sample data. Select the relationship line or the ellipsis of the table you'd like to edit. From here you can remove the relationship or table from the data model or make edits.

### Add table

1. Select **Add table** button from the command bar to add a new or existing table to your data model. Select Draft table if you want to create a new in-memory table from scratch. Select Existing Dataverse table or Existing SharePoint list if you want to bring your existing data to this solution.

### Add and edit relationship

1. Select **Add relationship** button from the command bar to add a new relationship between two tables.

1. To edit a relationship, select the relationship line between two tables and select edit from the dropdown menu. Here you can change the relationship type or add a lookup column. You can also perform advanced edits like changing the logical names used in the relationship.

1. Some relationship configurations are currently not supported. See Known limitations for more details.

### Remove

1. To remove a table from your solution, first select a table from the canvas, then select **Remove** from the command bar. When a Draft table is selected, this will delete the table and all associated table rows. When an existing Dataverse table or SharePoint list is selected, Remove doesn't delete the table and associate rows.

### View data

> Select **View data** from the command bar or the context menu available under the ellipsis for the table you would like to edit. Here you can add, remove, and edit columns and rows of data.

### Row ownership

> You can edit row ownership from the context menu or data view drawer. Select the row ownership option from either location to change the ownership type to User or Team or Organization.

### Properties

1. You can edit table properties from the context menu or data view drawer.

1. When you make changes to the app, plan, or data, the agent will perform an analysis to determine whether updates are needed to the other parts of the solution. If changes are required, the agent will proactively make them and outline the changes made in the chat.

## ALM capabilities

- **Save**: Auto-save is not supported yet. Select Save in the command bar at any time to save the progress of your solution. Selecting save will save all edits to all solution objects to your preferred solution.

- **Publish**:

  - **Publishing data**: Select Publish draft tables from the context menu of data card when ready to commit your table for production use. Choose between Dataverse or SharePoint as a target data source. Once the draft tables are published, the apps using the draft tables will be automatically updated to use the published tables as well.

  - **Publishing app**: Select Publish button on the command bar of the app when you're ready to publish the app for production use. If there is any draft table being used by the app, you will be prompted to publish those draft tables as well.

- **Share the app:** You can share your app with others for them to use. Select the Share button and add the accounts you would like to be able to run the created app.

## Provide feedback

You can share your feedback about the generated content or the experience at any time by using either the thumbs icons in the chat pane or the feedback icon in the command bar.

- **Provide feedback using thumbs:** to provide feedback about the generated content, use the thumbs in the chat pane. You can provide additional details by selecting "Tell us why."

- **Provide feedback about the experience:** to provide feedback about the overall experience, use the Feedback icon in the command bar. Select the category of feedback you'd like to provide and then share the details in the provided input.

## Known limitations

- The new workspace can only be used in one browser tab at a time. Working in multiple browser tabs may result in unexpected behavior.

- Only one app will be recommended/allowed in the new workspace per solution at this time

- Individual components of a generated solution cannot be saved individually at this time

- Pre-existing plans can't be opened in OWS

- Canvas and model apps won't be recommended

- Canvas and model apps can't be opened or edited in OWS

- <span class="mark">Apps created can be shared with users, but cannot be shared with additional co-owners at this time</span>

- Existing tables won't be automatically recommended during data model proposal. Maker will need to manually add the existing tables to be included in their solution.

- Editing existing Dataverse tables and SharePoint lists via chat is not supported yet.

- Inline editing on SharePoint lists is not supported yet. Maker can select **Edit in new tab** to edit the SharePoint list from the SharePoint site. Some relationship configurations are currently not supported, including many-to-many relationship between any table, many-to-one relationship between existing table and new table, and any relationship between existing tables across different data sources (Ex: relationship between SharePoint list and Dataverse table).

- Previously created Code apps are only editable from OWS

- Code view/Split view doesn't support direct edits of code at this time

  - <span class="mark">^ this means that code apps in the apps list/home page might have edit disabled in the context menu – makers will have to open the plan to edit the app</span>

  - If you export a code app and edit it outside of OWS (in VS Code for example), you may not be able to further edit it in OWS if you re-import it

  - Undo is only available by asking in the chat

  - Proposed technologies (apart from code apps) cannot be directly created from the plan at this time.
