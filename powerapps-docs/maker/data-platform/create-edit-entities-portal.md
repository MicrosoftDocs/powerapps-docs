---
title: "Create and edit tables using Power Apps | MicrosoftDocs"
description: "Understand how to create and edit tables using Power Apps."
author: "Mattp123"
ms.date: 02/28/2024
ms.reviewer: ""
ms.topic: "how-to"
ms.subservice: dataverse-maker
ms.author: "matp"
ms.collection: bap-ai-copilot
---
# Create and edit tables using Power Apps

[Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) provides an easy way to view, create, and edit tables for Microsoft Dataverse.

## View tables

Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Tables** on the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

Filter the tables that are displayed using the following tabs:

 |View|Description|
 |--|--|
 |**Recommended**|Displays only the standard tables. Standard tables are tables included with Power Apps or Dynamics 365 apps. |
 |**Custom**|Displays only custom tables. Custom tables are created by you and other app makers. |
 |**All**| Displays all the tables. |

:::image type="content" source="media/view-entities-portal.png" alt-text="View tables in Power Apps":::

You can also select a column heading from the table view, and then select **Filter by** to display tables by a certain property, such as **Type**, **Managed**, or **Tags**.

## Create a table

There are several ways to create a new table:

- [Add columns and data](#add-columns-and-data)
- [Describe the new table](#describe-the-new-table)
- [Set advanced properties](#set-advanced-properties)
- [Create with external data](#create-with-external-data)
- [Create a virtual table](#create-a-virtual-table)

### Add columns and data

Create a table by entering the data rows and columns you want.

1. From the **Tables** area, on the command bar select **New table** > **Add columns and data**.
1. When you're finished, select **Create**.

More information: [Table designer](#table-designer)

### Describe the new table

Create a table with the help of AI Copilot.

> [!NOTE]
> To use this feature, note the following requirements:
>
> - Copilot must be enabled for the environment. By default, Copilot is enabled. More information:  [Manage feature settings](/power-platform/admin/settings-features#copilot-preview)
> - This feature is available in English, Dutch, French, German, Italian, Japanese, Portuguese (Brazil), and Spanish. Depending on where your environment is hosted, you might need to enable data movement across regions. For more information go to [Copilots and generative AI features that are available when you enable data movement across regions](/power-platform/admin/geographical-availability-copilot#copilots-and-generative-ai-features-that-are-available-when-you-enable-data-movement-across-regions).

1. From the **Tables** area, on the command bar select **New table** > **Describe the new table**.
1. Describe the table with the assistance of Copilot. More information: [Review the table](../canvas-apps/ai-conversations-create-app.md#step-2-review-the-table-for-your-app)
1. When you're finished, select **Create**.

### Set advanced properties

Start with a blank table and enter the table properties, such as name, and description. Expand **Advanced options** to set more properties, such as track changes and audit changes.

From the **Tables** area, on the command bar select **New table** > **Set advanced properties**. This opens the **New table** properties panel.

:::image type="content" source="media/new-entity-panel.png" alt-text="Create a new table pane.":::

Enter data for the following properties.

|Property |Description|
|--|--|
|**Display name**|This is the singular name for the table that is shown in the app. This can be changed later.|
|**Plural display name**|This is the plural name for the table that is shown in the app. This can be changed later.|
|**Description**|Provide a meaningful description of the purpose of the table.|

Select **Enable Attachments** to append notes and files to records for this table.

Select the **Primary column** tab if you want to change the **Display name** or **Description** of the primary column. The primary column is used by lookup fields when establishing relationships with other tables.

> [!IMPORTANT]
> After you save the table, the **Primary column** display name and description can't be changed.

#### Advanced options

Select **Advanced options** to display additional properties that are optional for a table.

|Property |Description|
|--|--|
| **Schema name**  | By default, the schema name is automatically created for you based on the display name, but you can change it. The schema name can't contain spaces and includes the customization prefix for the Dataverse solution publisher. You can't change this after the table is saved.  |
|**Type**  | Select the type of table. Use standard for most tables. [Activity tables](/power-apps/maker/data-platform/types-of-entities#activity-tables) are a special table that can only be owned by a user or team, but can't be owned by an organization. [Virtual tables](create-edit-virtual-entities.md) require the table be populated with data from an external source. [Elastic tables](create-edit-elastic-tables.md) should be considered when your business scenario entails very large data volumes with high throughput, storage, and low latency requirements.  |
|**Record ownership**|Switch the table type to Activity table to create tables that can manage tasks. The type of **Ownership** defines who can perform operations on a record.|
| **Choose a table image**  | You can choose whether to display an image for the table. This image is displayed in Power Apps in some design areas. Notice that the image doesn't appear in apps using the table. To display images in apps, use the image column. More information: [Image columns](types-of-fields.md#image-columns) |
| **Color** | Set a color to be used for the table in model-driven apps.  |
|**Apply duplicate detection rules**   | If duplicate detection is enabled for your organization, enabling this allows you to create duplicate detection rules for this table.  |
|**Track changes**   | Enables data synchronization in a performant way by detecting what data has changed since the data was initially extracted or last synchronized.  This option must be enabled for certain features such as Azure Synapse Link for Dataverse. |
| **Provide custom help**  | When selected, set a **Help URL** to control what page users see when they select the help button in the application. Use this to provide guidance specific to your company processes for the table.  |
| **Audit changes to its data**  | When auditing is enabled for your organization, this allows for changes to table records to be captured over time. When you enable auditing for a table, auditing is also enabled on all its fields. You can select or clear fields that you want to enable auditing on.  |
| **Leverage quick create form if available**  |After you've created and published a Quick Create Form for this table, people have the option to create a new record using the Create button in the navigation pane. More information: [Create and design model-driven app forms](../model-driven-apps/create-design-forms.md)  <br /> When this is enabled for a custom activity table, the custom activity is visible in the group of activity entities when people use the **Create** button in the navigation pane. However, because activities don't support quick create forms, the main form is used when the custom table icon is selected.  |
|**Creating a new activity**  | Associate activities to records for this table.  |
| **Doing a mail merge**  | App users can use this table with mail merge.   |
|**Setting up SharePoint document management**   | After other tasks have been performed to enable document management for your organization, enabling this feature allows for this table to participate in integration with SharePoint.  |
| **Can have connections**  | Use the connections feature to show how records for this table have connections to records of other tables that also have connections enabled.  |
| **Can have a contact email**  | Send emails using an email address stored in one of the fields for this table. If a **Single Line of Text** column with format set to email doesn't already exist for this table, a new one is created when you enable sending email.  |
| **Have an access team**| Create team templates for this table.  |
| **Can be linked to feedback**  | Let app users write feedback for any table record, or rate table records within a defined rating range. More information: [Configure a table for feedback/ratings](configure-entity-feedback.md)  |
|**Appear in search results**   | Enable so that table records can be included in search results when using an app.  |
|**Can be taken offline** | Makes data in this table available while the Power Apps application isn't connected to a network.  |
|**Can be added to a queue**| Use the table with queues. Queues improve routing and sharing of work by making records for this table available in a central place that everyone can access. |

Select **Save** to continue, this closes the **New table** panel and display the [table hub](#edit-table-components-using-the-table-hub).

### Create with external data

Use an Excel file/CSV file or SharePoint list to populate a table with your data, which uses copilot to assist with the table generation.

> [!NOTE]
> [Generally available](/power-platform/admin/general-availability-deployment) copilot features are enabled by default and can't be turned off. To disable them, a tenant admin must [contact support](/power-platform/admin/get-help-support).

1. From the **Tables** area, on the command bar select **New table** > **Create with external data**, and then select either **File (Excel, .CSV)** or **SharePoint list**.
   # [File (Excel, .CSV)](#tab/excel)

   1. Select from device or drag and drop your Excel file onto the **Upload an Excel file** page.
   1. The data from the Excel file is displayed as a Dataverse table. Select a column header > **Edit column** to make changes, such as the column name or data type.
   1. When you're finished, select **Create**.

   For more information about how AI is used with this feature, go to [FAQ for Excel to table and app](../common/faqs-excel-to-table-app.md).

   # [SharePoint list (preview)](#tab/sharepoint)

   > [!IMPORTANT]
   > - This is a preview feature.
   > - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
   > - For SharePoint columns not supported, go to [SharePoint columns not used in Dataverse table generation](#sharepoint-columns-not-used-in-dataverse-table-generation).

   1. If you agree to the terms, select **Continue**.
   1. Select the SharePoint site you want from the following options:

      - **Enter the SharePoint URL** for the SharePoint site that has the list you want, such as `https://microsoft.sharepoint.com/teams/ContosoSite`, and then select **Connect**.
      - Select the SharePoint site with the list you want under **Recent sites**.
      - Alternatively, you can create a new connection to a SharePoint site by selecting **...** > **Add a new connection** on the left pane.

   1. Under **Select a list**, select the list you want, and then select **Next**.
   1. The table preview appears. Select from the following options:

      - Select **Edit table properties** if you want to change the table name and description that are generated for you.
      - Select **Row ownership** if you want to change the table row ownership to either user\group or organization owned. More information: [Table ownership](types-of-entities.md#table-ownership)
   1. Select **Create** to create the table.

   For more information about how AI is used with this feature, go to [FAQ for SharePoint list to table and app](../common/faqs-sharepoint-list-to-table-app.md).
---

#### SharePoint columns not used in Dataverse table generation

The following columns aren’t included when generating a Dataverse table from a SharePoint list because the respective data types aren’t supported with Dataverse:

- Image
- Task outcome
- External data
- Managed metadata
- Attachment (single)
- Multiple attachments / images
- SharePoint list system columns
- Symbol at column level (currency, prefix, postfix) in numbers
- Unique values

### Create a virtual table

A virtual table is a custom table in Microsoft Dataverse that has columns containing data from an external data source, such as Azure SQL Database or SharePoint.

1. From the **Tables** area, on the command bar select **New table** > **Create a virtual table**.
1. Follow the **New table from external data** wizard to create the virtual table. More information: [Create the virtual table](create-virtual-tables-using-connectors.md#create-the-virtual-table)

## Edit a table

While [viewing tables](#view-tables), select the table you want to edit, and then select **Properties** from the command bar if you want to edit the table properties.

:::image type="content" source="media/entity-settings-portal.png" alt-text="Edit table properties":::

### Edit table components using the table hub

To edit form components, open the table to display the table hub. The table hub displays the table components described in the following sections.

:::image type="content" source="media/table-hub.png" alt-text="Table hub" lightbox="media/table-hub.png":::

#### Table properties

Displays a few common properties for the table. Select **Properties** on the command bar to edit the table properties.

#### Schema

From the Schema area, select from the following table components to open the area where you can view and open existing components or create a new one.

- Columns. More information: [Create and edit columns](create-edit-fields.md)
- Relationships. See [Create and edit relationships between tables](create-edit-entity-relationships.md)
- Keys. More information: [Define alternate keys to reference rows](define-alternate-keys-reference-records.md)

#### Data experiences

From the **Data experiences** area select from the following table components to open the area where you can view and open existing components or create a new one.

- Forms. More information: [Create and design forms](../model-driven-apps/create-design-forms.md)
- Views. More information: [Create or edit a view](../model-driven-apps/create-edit-views.md)
- Charts. More information: [Create a system chart](../model-driven-apps/create-edit-system-chart.md)
- Dashboards. More information: [Create or edit dashboards](../model-driven-apps/create-edit-dashboards.md)

#### Customizations

From the Customizations area, select from the following table components to open the area where you can view and open existing components or create a new one.

- Business rules. More information: [Create business rules and recommendations to apply logic in a form](../model-driven-apps/create-business-rules-recommendations-apply-logic-form.md)
- Commands. More information: [Customize the command bar using command designer](../model-driven-apps/use-command-designer.md)

#### Table columns and data

View and create table record data for the table. Select the number of columns, such as **+17 more**, to select columns to display in the columns and data view.

:::image type="content" source="media/select-columns-to-display.png" alt-text="Select additional columns to display in the columns and data view":::

#### Table designer

From the table hub, select **Edit** to open the table designer. The table designer lets you make extensive changes to a table including editing or adding new records and columns, editing table properties, or creating a model-driven app based on the table.

:::image type="content" source="media/table-hub.gif" alt-text="Table hub video":::

#### Update forms and views

From the table hub, select **Update forms and views** to add selected columns to forms and views in this table without having to edit them in the form and view designers. More information: [Update forms and views using table designer](update-forms-and-views.md)

## Delete a table

As someone with the system administrator security role, you can delete custom tables that aren't part of a managed solution.  

> [!WARNING]
>  When you delete a custom table, the database tables that store data for that table are deleted and all data they contain is lost. Any associated records that have a parental relationship to the custom table are also deleted. For more information about parental relationships, see [Create and edit relationships between tables](create-edit-entity-relationships.md).  
> 
> The only way to recover data from a table that was deleted is to restore the database from a point before the table was deleted. More information: [Backup and restore instances](/dynamics365/customer-engagement/admin/backup-restore-instances)

While [viewing tables](#view-tables), select the table, and then select **Delete** from the menu.

If the table has dependencies that prevent it from being deleted you see an error message. To identify and remove any dependencies, you need to use the solution explorer. More information [Identify table dependencies](create-edit-entities-solution-explorer.md#identify-table-dependencies)

### See also

[Build apps through conversation (preview)](../canvas-apps/ai-conversations-create-app.md)

[Create a custom table using code](../../developer/data-platform/org-service/create-custom-entity.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
