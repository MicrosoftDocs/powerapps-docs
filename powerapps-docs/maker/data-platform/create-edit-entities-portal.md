---
title: "Create and edit tables using Power Apps | MicrosoftDocs"
description: "Understand how to create and edit tables using Power Apps portal"
author: "Mattp123"
ms.date: 07/25/2023
ms.reviewer: ""
ms.topic: "how-to"
ms.subservice: dataverse-maker
ms.author: "matp"
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

Watch this video for a quick overview about how to create a table:
> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWEEuM]

While [viewing tables](#view-tables), on the menu bar select **New table**. This opens the **New table** panel.

:::image type="content" source="media/new-entity-panel.png" alt-text="Create a new table pane.":::

Enter data for the following properties.

|Property |Description|
|--|--|
|**Display name**|This is the singular name for the table that will be shown in the app. This can be changed later.|
|**Plural display name**|This is the plural name for the table that will be shown in the app. This can be changed later.|
|**Description**|Provide a meaningful description of the purpose of the table.|

Select **Enable Attachments** to append notes and files to records for this table.

Select the **Primary column** tab if you want to change the **Display name** or **Description** of the primary column. The primary column is used by lookup fields when establishing relationships with other tables.

> [!IMPORTANT]
> After you save the table, the **Primary column** display name and description can't be changed.

### Advanced options

Select **Advanced options** to display additional properties that are optional for a table.

|Property |Description|
|--|--|
| **Schema name**  | By default, the schema name is automatically created for you based on the display name, but you can change it. The schema name can't contain spaces and includes the customization prefix for the Dataverse solution publisher. You can't change this after the table is saved.  |
|**Type**  | Select the type of table. Use standard for most tables. [Activity tables](/power-apps/maker/data-platform/types-of-entities#activity-tables) are a special table that can only be owned by a user or team, but can’t be owned by an organization. [Virtual tables](create-edit-virtual-entities.md) require the table be populated with data from an external source. [Elastic tables](create-edit-elastic-tables.md) should be considered when your business scenario entails very large data volumes with high throughput, storage, and low latency requirements.  |
|**Record ownership**|Switch the table type to Activity table to create tables that can manage tasks. The type of **Ownership** defines who can perform operations on a record.|
| **Choose a table image**  | You can choose whether to display an image for the table. This image is displayed in Power Apps in some design areas. Notice that the image doesn't appear in apps using the table. To display images in apps, use the image column. More information: [Image columns](types-of-fields.md#image-columns) |
| **Color** | Set a color to be used for the table in model-driven apps.  |
|**Apply duplicate detection rules**   | If duplicate detection is enabled for your organization, enabling this allows you to create duplicate detection rules for this table.  |
|**Track changes**   | Enables data synchronization in a performant way by detecting what data has changed since the data was initially extracted or last synchronized.  This option must be enabled for certain features such as Azure Synapse Link for Dataverse. |
| **Provide custom help**  | When selected, set a **Help URL** to control what page users will see when they select the help button in the application. Use this to provide guidance specific to your company processes for the table.  |
| **Audit changes to its data**  | When auditing is enabled for your organization, this allows for changes to table records to be captured over time. When you enable auditing for a table, auditing is also enabled on all its fields. You can select or clear fields that you want to enable auditing on.  |
| **Leverage quick create form if available**  |After you've created and published a Quick Create Form for this table, people will have the option to create a new record using the Create button in the navigation pane. More information: [Create and design model-driven app forms](../model-driven-apps/create-design-forms.md)  <br /> When this is enabled for a custom activity table, the custom activity will be visible in the group of activity entities when people use the **Create** button in the navigation pane. However, because activities don’t support quick create forms, the main form will be used when the custom table icon is selected.  |
|**Creating a new activity**  | Associate activities to records for this table.  |
| **Doing a mail merge**  | App users can use this table with mail merge.   |
|**Setting up SharePoint document management**   | After other tasks have been performed to enable document management for your organization, enabling this feature allows for this table to participate in integration with SharePoint.  |
| **Can have connections**  | Use the connections feature to show how records for this table have connections to records of other tables that also have connections enabled.  |
| **Can have a contact email**  | Send emails using an email address stored in one of the fields for this table. If a **Single Line of Text** column with format set to email doesn’t already exist for this table, a new one will be created when you enable sending email.  |
| **Have an access team**| Create team templates for this table.  |
| **Can be linked to feedback**  | Let app users write feedback for any table record, or rate table records within a defined rating range. More information: [Configure a table for feedback/ratings](configure-entity-feedback.md)  |
|**Appear in search results**   | Enable so that table records can be included in search results when using an app.  |
|**Can be taken offline** | Makes data in this table available while the Power Apps application isn't connected to a network.  |
|**Can be added to a queue**| Use the table with queues. Queues improve routing and sharing of work by making records for this table available in a central place that everyone can access. |

Select **Save** to continue, this will close the **New table** panel and display the [table hub](#edit-table-components-using-the-table-hub).

## Edit a table

While [viewing tables](#view-tables), select the table you want to edit, and then select **Properties** from the command bar if you want to edit the table properties.

:::image type="content" source="media/entity-settings-portal.png" alt-text="Edit table properties":::

### Edit table components using the table hub

To edit form components, open the table to display the table hub. The table hub displays the table components described in the following sections.

:::image type="content" source="media/table-hub.png" alt-text="Table hub" lightbox="media/table-hub.png":::

#### Table properties

Displays a few common properties for the table. Select **Properties** on the command bar to edit the table properties.

#### Schema

From the **Schema** area select from the following table components to open the area where you can view and open existing components or create a new one.

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

From the **Customizations** area select from the following table components to open the area where you can view and open existing components or create a new one.

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

As someone with the system administrator security role, you can delete custom tables that aren’t part of a managed solution.  

> [!WARNING]
>  When you delete a custom table, the database tables that store data for that table are deleted and all data they contain is lost. Any associated records that have a parental relationship to the custom table are also deleted. For more information about parental relationships, see [Create and edit relationships between tables](create-edit-entity-relationships.md).  
> 
> The only way to recover data from a table that was deleted is to restore the database from a point before the table was deleted. More information: [Backup and restore instances](/dynamics365/customer-engagement/admin/backup-restore-instances)

While [viewing tables](#view-tables), select the table, and then select **Delete** from the menu.

If the table has dependencies that prevent it from being deleted you'll see an error message. To identify and remove any dependencies, you'll need to use the solution explorer. More information [Identify table dependencies](create-edit-entities-solution-explorer.md#identify-table-dependencies)

### See also

[Create a custom table using code](../../developer/data-platform/org-service/create-custom-entity.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
