---
title: Create a Dataverse custom table  | Microsoft Docs
description: Learn how to create a custom table in Power Apps.
author: Mattp123
ms.component: cds
ms.topic: quickstart
ms.date: 07/20/2020
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---

# Create a Dataverse custom table

In Microsoft Dataverse, a *table* defines information that you want to track in the form of records, which typically include properties such as company name, location, products, email, and phone. You can then surface that data by developing an app that refers to the table. Power Apps offers standard "out-of-the-box" tables to cover typical scenarios within an organization (such as tracking appointments), but there might be times when you need to create custom tables to store data that's specific to your organization.

Watch this video for a quick overview about how to create a table:
> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWEEuM]

## Prerequisites

To create a table, you must have either a System Administrator or System Customizer security role within Dataverse.

## Create a table

1. Sign in to Power Apps at [https://make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. On the left navigation pane, select **Tables**.
1. On the command bar, select **New table** &gt; **Set advanced properties**.  

   Before you create a table, check out the [table reference](../../developer/data-platform/reference/about-entity-reference.md) for a description of available standard tables. These tables cover typical scenarios. If one of these tables meets your requirements as is or after minor changes, you can save time by starting with that table.

1. In the **New table** panel, enter the information for all required properties and the optional properties that you want. Required columns are designated with an asterisk (*) next to the column label. More information: [Dataverse table options](#dataverse-table-options).

## Dataverse table options

|Option  |Name  |Description  |Can be edited after table save  |
|---------|---------|---------|---------|
|Standard     | **Display name**      | This singular name for the table is shown in apps.     |   Yes   |
|Standard     |  **Plural name**    | This plural name for the table is shown in apps.    | Yes |
|Standard     |  **Primary column**    | Select the **Primary column** tab to display the primary column name and description fields. By default, every table contains a **Primary column**, which is used by lookup columns when establishing relationships with other tables. Typically the primary column stores the name or primary description of the data stored in the table. You can change the name and display name of the primary column before saving the table for the first time. Observe that the primary column also has its own **Name** box, which functions similarly to the table name described above. The primary name column name is autopopulated when a display name is entered using the same prefix as the table.  | No    |
|Standard     |  **Description**.     |   You can enter a description for your table if you wish. Descriptions are helpful when other people use this table.   |  Yes    |
|Standard     |  **Enable attachments**  |  Adds the attachments control to the table. The control is used to add or remove files and notes to records. Enabling this option lets users add files, such as document files from their computer or existing photos from a mobile device. By default, attached files can be up to 5 MB in size, but can be increased for the environment in the Power Platform admin center. More information: [System settings email tab](/power-platform/admin/system-settings-dialog-box-email-tab)<br /><br />Once this option is set, it can’t be changed after the table is created.   |  No  |
| Advanced   |  **Schema name**   |  Unique name that prepends the solution publisher prefix. By default, the schema name is automatically formed using the display name and publisher prefix. | No   |
|Advanced     |  **Type**    | By default, tables are created as **Standard**. Other table types are [Activity](types-of-entities.md#activity-tables), [Virtual](types-of-entities.md#virtual-tables), or [Elastic](types-of-entities.md#elastic-tables).       |   No      |
|Advanced     |  **Record ownership** |    The type of ownership defines who can perform operations on a row. **User or team** ownership allows the table records to contain data that relates to customers, such as accounts or contacts. Security can be defined according to the business unit for the user or team. **Organization** ownership table records contain data involving something that belongs to or that can be viewed by the whole organization. *Organization-owned table records can't be assigned or shared.*   |  No   |
|Advanced  |  **Choose table image**  |   Select an image file from a web resource. The image is displayed for table records created in apps.    |  Yes     |
|Advanced     |  **Color**    |  Select the color using the color picker or enter the hexadecimal number that represents the color.      |   Yes      |
|Advanced     | **Apply duplicate detection rules**   | Helps reduce duplicate records in the system. More information: [Set up duplicate detection rules to keep your data clean](/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)   |  Yes       |
|Advanced     |  **Track changes**   |  Provides a way to keep the data synchronized in an efficient manner by detecting what data has changed since the data was initially extracted or last synchronized. Certain features such as Azure Synapse Link for Dataverse require this setting enabled.  | No    |
|Advanced     | **Provide custom help**    | Lets you add a link to direct users from apps via the Help link to your help information such as a SharePoint site.     |  Yes       |
|Advanced     | **Audit changes to its data**     |  Auditing logs changes that are made to customer records in Dataverse. More information: [Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing)   |  Yes       |
|Advanced     |   **Leverage quick-create form if available**   | After you have created and published a quick create form for this table, people will have the option to create a new row using the **Create** button in the navigation pane. <br /> <br />When this is enabled for a custom activity table, the custom activity is visible in the group of activity tables when people use the **Create** button. However, because activities don’t support quick create forms, the main form is used when the custom table icon is selected.     | Yes    |
|Advanced   |  **Enable long term retention**   |  Dataverse supports custom retention policies to securely retain unlimited data long term in a cost-efficient way. More information: [Dataverse long term data retention overview](data-retention-overview.md)     |  Yes       |
|Advanced     |  **Creating a new activity**   |  Associate activities to records for this table.   |  No    |
|Advanced     |  **Doing a mail merge**    |  Allows people to use this table with mail merge.    |  Yes       |
|Advanced     |  **Setting up OneNote integration**    | When you turn on OneNote integration, you have the benefits of using OneNote to take or review customer notes from within your records. Requires SharePoint document management to be set up. More information: [Set up OneNote integration](/power-platform/admin/set-up-onenote-integration-in-dynamics-365)    |  Yes       |
|Advanced     |  **Setting up SharePoint integration**  |  Document management with SharePoint lets users manage common document types, such as Word, Excel, PowerPoint, OneNote, and create folders to save and manage those documents with Power Apps. More information: [Manage your documents using SharePoint](/power-platform/admin/manage-documents-using-sharepoint)   |         |
|Advanced     |  **Can have connections**  | Use the connections feature to show how records for this table have connections to records of other tables that also have connections enabled. Once enabled, this setting can't be disabled.     |   No   |
|Advanced     |  **Can have contact email**  | Send emails using an email address stored in one of the columns for this table. If a **Single Line** of **Text column** with format set to email doesn’t already exist for this table, a new one is created when you enable sending email. Once enabled, this setting can't be disabled.         |   No      |
|Advanced     |  **Have an access team**  |  Create team templates for this table.     |   Yes      |
|Advanced     |  **Can be linked to feedback**   |   Let customers write feedback for any table row, or rate table records within a defined rating range. More information: [Configure a table for feedback/ratings](configure-entity-feedback.md)      |   No      |
|Advanced     | **Appear in search results**   | Include records for this table so they can be queried via Dataverse search.        |  Yes       |
|Advanced     | **Can be taken offline**    |  Records for this table can be taken offline for mobile users. More information: [Mobile offline overview](/power-apps/mobile/mobile-offline-overview)  |  Yes       |
|Advanced     | **Can be added to queue**   | Use the table with queues. Queues improve routing and sharing of work by making records for this table available in a central place that everyone can access. Once enabled, this setting can't be disabled.         |   No      |



On the table details page, observe that the table is now being provisioned in the background. Once provisioning is completed, your table is saved and available for use in apps. Columns, relationships, and keys can be added to your table at any time (even while provisioning is still in progress), but views, forms, charts, dashboards, and business rules can only be added to the table after provisioning is completed.

## Next steps

In this article, you learned how to create a custom table. Next, learn how to define relationships between tables.

> [!div class="nextstepaction"]
> [Create a relationship](data-platform-entity-lookup.md)

## Privacy notice

With the Microsoft Power Apps common data model, Microsoft collects and stores custom table and column names in our diagnostic systems. We use this knowledge to improve the common data model for our customers. The table and column names that app Creators create help us understand scenarios that are common across the Microsoft Power Apps community and ascertain gaps in the service’s standard table coverage, such as schemas related to organizations. The data in the database tables associated with these tables isn't accessed or used by Microsoft or replicated outside of the region in which the database is provisioned. Note, however, that the custom table and column names may be replicated across regions and are deleted in accordance with our data retention policies. Microsoft is committed to your privacy as described further in our [Trust Center](https://www.microsoft.com/trustcenter/Privacy/default.aspx).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
