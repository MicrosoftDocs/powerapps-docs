---
title: "Tables and metadata in Microsoft Dataverse | MicrosoftDocs"
description: "Learn about tables and metadata in Microsoft Dataverse"
ms.custom: ""
ms.date: 06/29/2022
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

Dataverse is designed so that you can quickly and easily create a data model for your application. Normally, you shouldn't have to concern yourself with some of the details about metadata that this topic will introduce. But if you want to develop a deeper understanding about how apps that use Dataverse work or you're evaluating what is possible, understanding the metadata used by Dataverse may provide you insight.

*Metadata* means data about data. Dataverse provides a flexible platform for you because it's relatively easy to edit the definitions of the data that the environment will use. In Dataverse, the metadata is a collection of tables. Tables describe the kinds of data stored in the database. Table metadata is what controls the kinds of records you can create and what kind of actions can be performed on them. When you use the customization tools to create or edit tables, columns, and table relationships, you're editing this metadata. 
  
Different clients people use to interact with the data in your environment depend on the table metadata and adapt as you customize the metadata. But these clients also depend on other data to control what visual elements to display, any custom logic to apply, and how to apply security. This system data is also stored within tables but the tables themselves aren't available for customization.

You can learn about standard tables, attributes, and table relationships included by default in Dataverse by reviewing the [entity reference](../../developer/data-platform/reference/about-entity-reference.md).

> [!TIP]
> The designers available to edit metadata cannot show all the details found in the metadata. You can install a model-driven app called the **Metadata Browser** which will allow you to view all the tables and metadata properties that are found in the system. More information: [Browse table definitions in your environment](../../developer/data-platform/browse-your-metadata.md).
  
<a name="BKMK_CreateNewOrUseExistingMetadata"></a>

## Create new metadata or use existing metadata?

Dataverse comes with many standard tables that support core business application capabilities. For example, data about your customers or potential customers is intended to be stored using the account or contact tables.  
  
Each of these tables also contains many columns that represent common data that the system may need to store for the respective table.  
  
For most organizations it's to your advantage to use the standard tables and attributes for the purposes they were provided. 
  
If you install a solution, you can expect that the solution developer has leveraged the standard tables and attributes. Creating a new custom table that replaces a system table or attribute will mean that any solutions available may not work for your organization.  
  
For these reasons, we recommend that you look for and use the provided standard tables, columns, and table relationships when they make sense for your organization. If they don't make sense and can't be edited to match your need, you should evaluate if creating a new table, column, or table relationships is required. 

Remember that you can change the display name of a table so that it matches the nomenclature your organization uses. For example, it's common for people to change the display name of the Account table to *Company* or the name of the Contact table to *Individual*. This can be done to tables or attributes without changing the behavior of the table. For more information about renaming tables, see [Change the name of a table](edit-entities.md#change-the-name-of-a-table).
  
You can't delete standard tables, columns, or table relationships. They're considered part of the system solution and every organization is expected to have them. If you want to hide a standard table, change the security role privileges for your organization to remove the read privilege for that table. This will remove the table from most parts of the application. If there's a system column that you don't need, remove it from the form and any views that use it. Change the **Searchable** value in the column and table relationship definitions so that they don't appear in advanced find. 
  
<a name="BKMK_LimitationsOnMetadata"></a>   

## Limitations on creating metadata items  

There's a limit to the number of tables you can create. You can find information about the maximum number in the **[Settings](../model-driven-apps/advanced-navigation.md#solution-explorer)** > **Administration** > **Resources In Use** page. 
  
Within each table there's an upper limit on the number of columns you can create. This limit is based on the technical limitations on the amount of data that can be stored in a row of a database table. It's difficult to provide a specific number because each type of column can use a different amount of space. The upper limit depends on the total space used by all the columns for the table.  
  
Most people don't create enough custom columns to reach the limit, but if you find yourself planning to add hundreds of custom columns to a table, you should consider if this is the best design. Do all the columns you plan to add describe properties for a row for that table? Do you really expect that people using your organization will be able to manage a form that includes such a high number of columns? The number of columns you add to a form increase the amount of data that has to be transferred each time a row is edited and will affect the performance of the system. Take these factors into consideration when you're adding custom columns to a table.  
  
Choice columns provide a set of options that will be displayed in a drop-down control on a form or in picklist control when using advanced find. Your environment can support thousands of options within an Option set, but you shouldn't consider this as the upper limit. Usability studies have shown that people have trouble using a system where a drop-down control provides large numbers of options. Use choice  column to define categories for data. Don't use choice  columns to select categories that actually represent separate items of data. For example, rather than maintain a choice  column that stores each of hundreds of possible manufacturers of a type of equipment, consider creating a table that stores references to each manufacturer and use a lookup column instead of a choice.  
  
### Next steps

[Create or edit tables (row types)](./data-platform-create-entity.md)<br />
[Create and edit relationships between tables](create-edit-entity-relationships.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
