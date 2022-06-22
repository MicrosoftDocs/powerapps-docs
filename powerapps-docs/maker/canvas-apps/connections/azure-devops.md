---
title: Connect to Azure DevOps from Power Apps
description: See how to connect to Azure DevOps projects, display the queries and work items.
author: lancedMicrosoft
ms.topic: reference
ms.custom: canvas
ms.date: 03/17/2022
ms.subservice: canvas-maker
ms.author: lanced
ms.reviewer: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - lancedmicrosoft
---

# Connect to Azure DevOps from Power Apps

Power Apps connector for [Azure DevOps](/connectors/visualstudioteamservices/) allows you to work with Azure DevOps instance. You can view Azure DevOps queries, choose work items based on different work item types, view or edit details all from inside a canvas app that connects to Azure DevOps.

> [!TIP]
> For a complete list of all actions, see [Azure DevOps connector actions](/connectors/visualstudioteamservices/#actions).

In this article, you'll create a canvas app that connects to Azure DevOps to retrieve the list of queries, and work with work items within the project.

## Prerequisites

- You'll need a Power Apps license. If you don't have a license, use a [30-day trial](../../signup-for-powerapps.md), or sign up for a [developer plan](../../developer-plan.md) for non-production use.
- If you're new to Power Apps, familiarize yourself with Power Apps basics by [generating an app](../get-started-test-drive.md) and then customizing that app's [controls](../add-configure-controls.md), [gallery](../add-gallery.md), [forms](../working-with-forms.md), and [cards](../working-with-cards.md).
- You'll need a [blank canvas app](../create-blank-app.md) that we'll use to connect to Azure DevOps.
- You'll need an [Azure DevOps](/azure/devops/user-guide/what-is-azure-devops) instance that has an organization, a project, and a shared query, and a few sample work items to edit using the app that you'll create in this article.
- The Azure DevOps instance that you use must be enabled for **Third-party application access via OAuth**. To configure this setting, see [Manage access policies for Azure DevOps](/azure/devops/organizations/accounts/change-application-access-policies#manage-a-policy).

## Step 1. Add Azure DevOps data source

To connect to Azure DevOps, [edit](../edit-app.md) the [blank canvas app](../create-blank-app.md), and add **Azure DevOps** data source.

:::image type="content" source="media/azure-devops/add-data-source.png" alt-text="Connect to Azure DevOps.":::

If you don't have an Azure DevOps connection already, select **Connect** and follow the prompts to provide your details, and then allow the app to connect.

## Step 2. List shared queries

In this section, we'll use the [ListQueriesInFolder](/connectors/visualstudioteamservices/#list-queries-within-folder) action for the Azure DevOps connector to list the available queries.

1. From the left pane, select **Insert** > **Layout** > **Blank vertical gallery**.

1. Enter the following formula for the **Items** property of the gallery, replacing the example parameter values as appropriate.

    ```powerapps-dot
    AzureDevOps.ListQueriesInFolder("Sample-project","Fabrikam-Inc","Shared Queries").value
    ```

    :::image type="content" source="media/azure-devops/list-queries-in-folder.png" alt-text="List queries in folder using formula added to Items property of the vertical gallery.":::

    This formula uses the [ListQueriesInFolder](/connectors/visualstudioteamservices/#list-queries-within-folder) action with the following parameter values:
    - **Project Name** - Name of the project in Azure DevOps. "Sample-project" in this example.
    - **Organization Name** - Name of your organization in Azure DevOps. "Fabrikam-Inc" in this example.
    - **Folder Path** - The folder path to look for queries. "Shared Queries" in this example.

    > [!NOTE]
    > If you see the following error in the above formula, [enable third-party app access using OAuth](/azure/devops/organizations/accounts/change-application-access-policies#manage-a-policy) in your Azure DevOps organization, and try again.
    > 
    > "AzureDevOps.ListQueriesInFolder failed:{"status":401,"message":"TF400813:The user 'GUID' is not authorized to access this resource."

1. Select the **Layout** for the gallery to **Title and subtitle**.

1. Choose the fields as **Name** and **Path** for the title and subtitles.

    :::image type="content" source="media/azure-devops/query-list-fields.png" alt-text="Gallery fields for listing queries.":::

## Step 3. List work items

Now we'll use [GetQueryResultsV2](/connectors/visualstudioteamservices/#get-query-results) action for the Azure DevOps connector to list all work items for the selected query.

1. Insert another blank vertical gallery, and place it on the right-side of the existing gallery.

1. Enter the following formula for the **Items** property of the gallery, replacing the example parameter values as appropriate.

    ```powerapps-dot
    AzureDevOps.GetQueryResultsV2("Sample-project",Gallery2.Selected.Id,"Fabrikam-Inc").value
    ```

    :::image type="content" source="media/azure-devops/get-query-results.png" alt-text="Get query results from existing gallery based on the query selected.":::
    
    This formula uses the [GetQueryResultsV2](/connectors/visualstudioteamservices/#get-query-results) action with the project name, query ID, and the organization name. The query ID in this example (`Gallery2.Selected.Id`) refers to the query selected from the list of queries available through the gallery added earlier. Replace the gallery name as appropriate.

1. Select the **Layout** as **Title, subtitle, and body**.

1. Choose the fields as **'System.Title'**, **'System.WorkItemType'**, and **'System.Description'** for the title, subtitle and body fields.

    :::image type="content" source="media/azure-devops/workitem-fields.png" alt-text="Show work item fields of title, work item type, and description.":::

    > [!NOTE]
    > In order to render the fields correctly, ensure the fields that you want to use in Power Apps are added to the selected Azure DevOps query through **Column options**.

## Step 4. Edit work items

So far, the app shows a list of all queries, and then the list of work items for the selected query. Now we'll add an edit form that allows changing and saving the selected fields of a work item back to Azure DevOps.

For this purpose, we'll use the [UpdateWorkItem](/connectors/visualstudioteamservices/#update-a-work-item) action for the Azure DevOps connector.

1. Rearrange the two galleries on screen to make room for the edit form that we'll add by moving both galleries to the left of the screen.

1. Add **Edit form** to the screen, and move it to the right side of the galleries.

    :::image type="content" source="media/azure-devops/add-edit-form.png" alt-text="Add edit form.":::

1. Set the **DataSource** property of the edit form to `Gallery2.AllItems`.

    This formula sets the **DataSource** property to all items from the gallery configured [earlier](#step-3-list-work-items) to list all work items.

1. Set the **Item** property of the edit form to `Gallery2.Selected`.

    This formula sets the **Item** property for the edit form to the work item that's selected in the list of work items.

1. Select **Edit fields** from the properties pane on the right-side of the screen.

1. Select **...** (ellipsis) > **Add custom card**.

    :::image type="content" source="media/azure-devops/add-custom-card.png" alt-text="Add custom card.":::

1. Rearrange the data card within the edit form at the top.

    :::image type="content" source="media/azure-devops/custom-card-top.png" alt-text="Custom card moved to the top section inside the edit form.":::

1. Keeping the custom card selected, insert a **Text input** control. Once selected, the control is added inside the custom card.

1. Increase the size of the text input control.

    :::image type="content" source="media/azure-devops/text-input-inside-custom-card.png" alt-text="Text input control inside custom card.":::

1. Set the **Default** property of the text input control to `ThisItem.'System.Title'`.

    :::image type="content" source="media/azure-devops/title-custom-card.png" alt-text="Text input control referring to title of the work item.":::

    This formula sets the default text inside the text input control to the **Title** field from the selected Azure DevOps work item.

    > [!TIP]
    > If your Azure DevOps project uses **Description** field with HTML or rich text, you can also use the [Rich text editor](../controls/control-richtexteditor.md) input control instead of the [Text input](../controls/control-text-input.md) control. Using the **Rich text editor** control in this case also helps resolve any issues such as the description being displayed with HTML code instead of plain or rich text.

1. Repeat the previous steps to add another custom card, with a text input control inside with the **Default** property set to `ThisItem.'System.Description'`.

    This formula sets the default text inside the text input control to the **Description** field from the selected Azure DevOps work item.

1. Rearrange the data cards inside the edit form to create space where we'll add the save icon.

1. Select the edit form, and then select **Insert** > **Icons** > **Save**.

1. Make a copy of the icon by pressing **Ctrl+C** and **Ctrl+V**.

1. Rearrange the save icons next to the data cards for title and description.

    :::image type="content" source="media/azure-devops/save-icons.png" alt-text="Save icons for saving data card text input values.":::

1. Set the **OnSelect** properties for both icons to the following formulas, for title and description.

    - Title:

        ```powerapps-dot
        AzureDevOps.UpdateWorkItem(Gallery2.Selected.'System.Id',"Fabrikam-Inc",{project:"Sample-project",type:Gallery2.Selected.'System.WorkItemType',title:TextInput2.Text})
        ```

    - Description:

        ```powerapps-dot
        AzureDevOps.UpdateWorkItem(Gallery2.Selected.'System.Id',"Fabrikam-Inc",{project:"Sample-project",type:Gallery2.Selected.'System.WorkItemType',description:TextInput3.Text})
        ```

    The formulas for the save icon uses the [UpdateWorkItem](/connectors/visualstudioteamservices/#update-a-work-item) action. The formula uses the work item selected in the work item gallery, and updates the property of "text" or "description" with the value updated through the given text input controls. In the above example, "TextInput2" for "title" and "TextInput3" for "description".

    > [!NOTE]
    > Ensure the formula uses lower case for field names. For example, when referring to "Description" field, use `description:TextInput3.Text` instead of `Description:TextInput3.Text`. Incorrect casing might result in the error "400 Required parameter: 'workItem' missing for requested operation: 'UpdateWorkItem'".

1. [Save and publish](../save-publish-app.md) the app.

## Next steps

Play the app. Select a query from the list of queries. And then, choose a work item that you want to update the title or description of. Make a change, and then select the save button. The changes are saved to the Azure DevOps work item. Switch to another query and switch back to see the changes show inside the app.

Similarly, customize the app further or create an app with additional data cards on forms. You can also use display form instead of edit form to just show data inside different data cards. When using display form, ensure you use the [Text label](../controls/control-text-box.md) control to display text. When using rich text or HTML format (such as the **Description** field in Azure DevOps), use the [HTML text](../controls/control-html-text.md) control. For more information about customizing that app, see [controls](../add-configure-controls.md), [gallery](../add-gallery.md), [forms](../working-with-forms.md), and [cards](../working-with-cards.md).

### See also

[Working with dynamic schema data sources in Power Apps (experimental)](../working-with-dynamic-schema.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
