---
title: "Tables and metadata in Microsoft Dataverse | MicrosoftDocs"
description: "Learn about tables and metadata in Microsoft Dataverse"
ms.custom: ""
ms.date: 10/02/2024
ms.reviewer: ""
ms.topic: "overview"
author: "Mattp123"
ms.assetid: 88b18946-474c-4c94-8e4c-27532f930757
caps.latest.revision: 28
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Tables and metadata in Microsoft Dataverse

Microsoft Dataverse is designed so that you can quickly and easily create a data model for your application. Normally, you shouldn't have to concern yourself with some of the details about metadata that this article introduces. But if you want to develop a deeper understanding about how apps that use Dataverse work or you're evaluating what is possible, understanding the metadata used by Dataverse can provide you with insight.

*Metadata* means data about data. Dataverse provides a flexible platform for you because it's relatively easy to edit the definitions of the data that the environment will use. In Dataverse, the metadata is a collection of tables. Tables describe the kinds of data stored in the database. Table metadata is what controls the kinds of records you can create and what kind of actions can be performed on them. When you use the customization tools to create or edit tables, columns, and table relationships, you're editing this metadata. 
  
Different clients people use to interact with the data in your environment depend on the table metadata and adapt as you customize the metadata. But these clients also depend on other data to control what visual elements to display, any custom logic to apply, and how to apply security. This system data is also stored within tables but the tables themselves aren't available for customization.

You can learn about standard tables, attributes, and table relationships included by default in Dataverse by reviewing the [entity reference](../../developer/data-platform/reference/about-entity-reference.md).

> [!TIP]
> The designers available to edit metadata don't show all the details found in the metadata. You can install a model-driven app called the **Metadata Browser**, which will allow you to view all the tables and metadata properties that are found in the system. More information: [Browse table definitions in your environment](../../developer/data-platform/browse-your-metadata.md).
  
## Create new metadata or use existing metadata?

Dataverse comes with standard tables that support core business application capabilities. For example, data about your customers or potential customers is intended to be stored using the account or contact tables.  
  
Each of these tables also contains many columns that represent common data that the system might need to store for the respective table.  
  
For most organizations it's to your advantage to use the standard tables and attributes for the purposes they were provided. 
  
If you install a solution, you can expect that the solution developer leveraged the standard tables and attributes. Creating a new custom table that replaces a system table or attribute will mean that any solutions available might not work for your organization.  
  
For these reasons, we recommend that you look for and use the provided standard tables, columns, and table relationships when they make sense for your organization. If they don't make sense and can't be edited to match your need, you should evaluate if creating a new table, column, or table relationships is required. 

Remember that you can change the display name of a table so that it matches the nomenclature your organization uses. For example, it's common for people to change the display name of the Account table to *Company* or the name of the Contact table to *Individual*. This can be done to tables or attributes without changing the behavior of the table. For more information about renaming tables, see [Change the name of a table](edit-entities.md#change-the-name-of-a-table).
  
You can't delete standard tables, columns, or table relationships. They're considered part of the system solution and every Dataverse environment is expected to have them. If you want to hide a standard table, change the security role privileges for your organization to remove the read privilege for that table. This removes the table from most parts of the application. If there's a system column that you don't need, remove it from the form and any views that use it. Change the **Searchable** value in the column and table relationship definitions so that they don't appear in advanced find. 

## Limitations on creating metadata items  

There's a limit to the number of tables you can create. Admins can view information about the number of tables and percent used towards the maximum in the legacy **Resources In Use** page. Go to Power Platform admin center (admin.powerplatform.com) select **Manage** > **Environments**, and open the environment you want. Select **Settings**, expand **Resources** select  **All legacy settings**. In the legacy settings, select **Administration** > **Resources In Use**.
  
Within each table there's also an upper limit on the number of columns you can create. This limit is based on the technical limitations on the amount of data that can be stored in a row of a Dataverse table and isn't viewable. It's difficult to provide a specific number because each type of column can use a different amount of space. The upper limit depends on the total space used by all the columns for the table.  
  
Most people don't create enough custom columns to reach the limit, but if you find yourself planning to add hundreds of custom columns to a table, you should consider if this is the best design. Do all the columns you plan to add describe properties for a row for that table? Do you really expect that people using your environment will be able to manage a form that includes such a high number of columns? The number of columns you add to a form increase the amount of data that has to be transferred each time a row is edited and will affect the performance of the system. Take these factors into consideration when you're adding custom columns to a table.  
  
Choice columns provide a set of options that are displayed in a drop-down control on a form or in picklist control when using advanced find. Your environment can support thousands of options within a choice column, but you shouldn't consider this as the upper limit. Usability studies show that people have trouble using a system where a drop-down control provides large numbers of options. Use choice columns to define categories for data. Don't use choice  columns to select categories that actually represent separate items of data. For example, rather than maintain a choice  column that stores each of hundreds of possible manufacturers of a type of equipment, consider creating a table that stores references to each manufacturer and use a lookup column instead of a choice.  
  
### Next steps

[Create or edit tables (row types)](./data-platform-create-entity.md)<br />
[Create and edit relationships between tables](create-edit-entity-relationships.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
