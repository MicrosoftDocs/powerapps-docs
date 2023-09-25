---
title: Connect to Azure DevOps from Power Apps
description: See how to connect to Azure DevOps projects, display the queries and work items.
author: lancedMicrosoft
ms.topic: reference
ms.custom: canvas
ms.date: 03/17/2022
ms.subservice: canvas-maker
ms.author: lanced
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
---

# Connect to Azure DevOps from Power Apps

Power Apps connector for [Azure DevOps](/connectors/visualstudioteamservices/) allows you to work with Azure DevOps instance. You can view Azure DevOps queries, select work items based on different work item types, and view, or edit details all from inside a canvas app that connects to Azure DevOps.

> [!TIP]
> For a complete list of all actions, see [Azure DevOps connector actions](/connectors/visualstudioteamservices/#actions).

In this article, you'll create a canvas app that connects to Azure DevOps to retrieve the list of queries, and work with work items within the project.

## Prerequisites

- You need a Power Apps license. If you don't have a license, use a [30-day trial](../../signup-for-powerapps.md), or sign up for a [developer plan](../../developer-plan.md) for non-production use.
- If you're new to Power Apps, familiarize yourself with Power Apps basics by [generating an app](../get-started-test-drive.md) and then customizing that app's [controls](../add-configure-controls.md), [gallery](../add-gallery.md), [forms](../working-with-forms.md), and [cards](../working-with-cards.md).
- You need a [blank canvas app](../create-blank-app.md) to use to connect to Azure DevOps.
- You need an [Azure DevOps](/azure/devops/user-guide/what-is-azure-devops) instance that has an organization, a project, and a shared query that has few sample work items to edit using the app that you'll create in this article.
- The Azure DevOps instance that must be enabled for **Third-party application access via OAuth**. To configure this setting, see [Manage access policies for Azure DevOps](/azure/devops/organizations/accounts/change-application-access-policies#manage-a-policy).

## Step 1 - Add Azure DevOps data source

To connect to Azure DevOps, [edit](../edit-app.md) the [blank canvas app](../create-blank-app.md), and add **Azure DevOps** data source.

> [!div class="mx-imgBorder"]
>![Connect to Azure DevOps.](./media/azure-devops/add-data-source.png "Connect to Azure DevOps")

If you don't have an Azure DevOps connection already, select **Connect** and follow the prompts to provide your details, and then allow the app to connect.

## Step 2 - List shared queries

In this section, we'll use the [ListQueriesInFolder](/connectors/visualstudioteamservices/#list-queries-within-folder) action for the Azure DevOps connector to list the available queries.

1. From the left pane, select **Insert** > **Layout** > **Blank vertical gallery**.

1. Enter the following formula for the **Items** property of the gallery, replacing the example parameter values as appropriate.

    ```powerapps-dot
    AzureDevOps.ListQueriesInFolder("Project","Organization","Folder").value
    ```


> [!div class="mx-imgBorder"]
>![List queries in folder using formula added to Items property of the vertical gallery.](./media/azure-devops/list-queries-in-folder.png "List queries in folder using formula added to Items property of the vertical gallery.")

If the example uses the variables "Project", "Organization", and "Folder" and the actual values are in the text boxes below the formula bar (highlighted). You can find your Project and Organization values from the URL used to connect to Azure Dev Ops.  The Folder will usually be "Shared Queries" or "My Queries".

> [!div class="mx-imgBorder"]
>![Locate the project and organization name for your Azure Dev Ops instance.](./media/azure-devops/find-azuredevops-project-name.png "Locate the project and organization name for your Azure Dev Ops instance.")

If you get the following error in the above formula, [enable third-party app access using OAuth](/azure/devops/organizations/accounts/change-application-access-policies#manage-a-policy) in your Azure DevOps organization, and try again.<br>
"AzureDevOps.ListQueriesInFolder failed:{"status":401,"message":"TF400813:The user 'GUID' isn't authorized to access this resource."}

1. Select the **Layout** for the gallery to **Title and subtitle**.

1. Choose the fields appropriate for Azure Dev Ops as **Name** and **FolderOptions** for the title and subtitles.

> [!div class="mx-imgBorder"]
>![Gallery fields for listing queries.](./media/azure-devops/query-list-fields.png "Gallery fields for listing queries")

## Step 3 - List work items

Now we use [GetQueryResultsV2](/connectors/visualstudioteamservices/#get-query-results) action for the Azure DevOps connector to list all work items for the selected query. This binds the gallery to the data source.

1. Insert another blank vertical gallery, and place it on the right-side of the existing gallery.

1. Enter the following formula for the **Items** property of the gallery, replacing the example parameter values as appropriate.  Substitute your Project and Organization names as appropriate.

    ```powerapps-dot
    AzureDevOps.GetQueryResultsV2("Project", Text(Gallery1.Selected.Id),"Organization").value
    ```

> [!div class="mx-imgBorder"]
>![Get query results from existing gallery based on the query selected..](./media/azure-devops/get-query-results.png "Get query results from existing gallery based on the query selected.")

This formula uses the [GetQueryResultsV2](/connectors/visualstudioteamservices/#get-query-results) action with the project name, query ID, and the organization name. The query ID in this example (`Gallery2.Selected.Id`) refers to the query selected from the list of queries available through the gallery added earlier. Replace the gallery name as appropriate.


### Adding untyped return values to your gallery
The returned result of **GetQueryResultsV2** is dynamic. And the values are therefore untyped as well.    

> [!div class="mx-imgBorder"]
> ![Show work item fields of title, work item type.](./media/azure-devops/dynamic-return-results-message.png "Get query results from existing gallery based on the query selected.")

However you can access some of the values.  Azure Dev Ops returns a basic set of values for all items that are typed.  Select the data card in the gallery and insert two text label.  Set the text property of the labels as follows:

```powerapps-dot
    ThisItem.Value.'System.WorkItemType'
    ThisItem.Value.'System.Title'
```

## Step 4 - Display work items

The app shows a list of all queries, and the list of work items for the selected query. Now we can add an edit form that we'll use to simply display data.

1. Arrange the two galleries on screen to make room for the edit form that we add by moving both galleries to the left of the screen.

1. Add **Edit form** to the screen, and move it to the right side of the galleries.

  > [!div class="mx-imgBorder"]
  > ![Add edit form.](./media/azure-devops/add-edit-form.png "Add edit form.")


1. Set the **DataSource** property of the edit form to `AzureDevOps.GetQueryResultsV2("Project", Text(Gallery1.Selected.Id),"Organization").value`.  Substitute your Project and Organization names as appropriate.


1. Set the **Item** property of the edit form to `Gallery2.Selected`.

    This formula sets the **Item** property for the edit form to the work item that's selected in the list of work items.

1. Select **Edit fields** from the properties pane on the right-side of the screen.

1. Select **...** (ellipsis) > **Add a custom card**.

    ![Add a custom card.](./media/azure-devops/add-custom-card.png "Add a custom card")

 
2. Rearrange the data card within the edit form at the top.

    :::image type="content" source="media/azure-devops/custom-card-top.png" alt-text="Custom card moved to the top section inside the edit form.":::

3. Keeping the custom card selected, insert a **Text input** control. Once selected, the control is added inside the custom card.

4. Increase the size of the text input control.

> [!div class="mx-imgBorder"]
>![Text input control inside custom card.](./media/azure-devops/text-input-inside-custom-card.png "Text input control inside custom card.")


5. Set the **Default** property of the text input control to `Text(ThisItem.Value.'System.Title')`. The Text function 'types' the return as Text.  

> [!div class="mx-imgBorder"]
> ![This is text input control referring to title of the work item.](./media/azure-devops/title-custom-card.png "Text input control referring to title of the work item.")

  This formula sets the default text inside the text input control to the **Title** field from the selected Azure DevOps work item.

> [!TIP]
> If your Azure DevOps project uses **Description** field with HTML or rich text, you can also use the [Rich text editor](../controls/control-richtexteditor.md) input control instead of the [Text input](../controls/control-text-input.md) or label controls. Using the **Rich text editor** control in this case also helps resolve any issues such as the description being displayed with HTML code instead of plain or rich text.

6. Repeat the previous steps to add another custom card, with a text input control inside with the **Default** property set to `Text(ThisItem.Value.'System.State')`.

    This formula sets the default text inside the text input control to the **State** field from the selected Azure DevOps work item.

7. Rearrange the data cards inside the edit form to create space where we'll add the save icon.

### Adding untyped and dynamic return values to your forms
So far we have been using the Edit form which simplifies the data access story by providing a common DataSource and Item property which all of the data cards in the form can work with.  If you use the Edit form, to access the untyped values make sure you set **both** the data source and the item properties as follows: (Substituting in your values for Organization and Project.)

 ```powerapps-dot
    AzureDevOps.GetWorkItemDetails(Gallery2.Selected.Value.'System.Id',Organization, Project, Gallery2.Selected.Value.'System.WorkItemType')
  ```
Note that "WorkItemType" is a text property passed in (e.g., "Feature") that allows you to pivot from items like Features and Work Items. The set of fields for these items vary from each other - which is why the return type from this call is dynamic. 

To access specific values you can still access the common values the same way (e.g.,`Text(ThisItem.Value.'System.Id')` ). However, you may also access them in the more general dynamic response this way: `Text(ThisItem.fields.System_Id)`. These dynamic values names aren't generally documented.  The easiest way to see the correct names for these fields - including the non-standard fields is to open the monitor tool and look at the data response. In this case, to the `GetWorkItemDetails` call.  (See image below.)

If you aren't using an Edit form, but rather simply a container, then you can access these values with a formula like the following: (Which accesses a custom team field.)

```powerapps-dot
Text(AzureDevOps.GetWorkItemDetails(Gallery2.Selected.Value.'System.Id',Organization, Project, Gallery2.Selected.Value.'System.WorkItemType').fields.One_custom_CustomField1)
```

> [!div class="mx-imgBorder"]
> ![Text input control that refers to title of the work item.](./media/azure-devops/monitor-workitem-details.png "Text input control referring to title of the work item.")


## Next steps

Play the app. Select a query from the list of queries. And then, choose a work item that you want to update the title or description of. Make a change, and then select the save button. The changes are saved to the Azure DevOps work item. Switch to another query and switch back to see the changes show inside the app.

Similarly, customize the app further or create an app with additional data cards on forms. You can also use display form instead of edit form to just show data inside different data cards. When using display form, ensure you use the [Text label](../controls/control-text-box.md) control to display text. When using rich text or HTML format (such as the **Description** field in Azure DevOps), use the [HTML text](../controls/control-html-text.md) control. For more information about customizing that app, see [controls](../add-configure-controls.md), [gallery](../add-gallery.md), [forms](../working-with-forms.md), and [cards](../working-with-cards.md).

### See also

[Working with dynamic schema data sources in Power Apps (experimental)](../working-with-dynamic-schema.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
