---
title: Structure Dataverse data with nested categories in Microsoft Dataverse # Intent and product brand in a unique string of 43-59 chars including spaces
description: Discover how to structure the table rows using the Category table. # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 05/04/2021
ms.reviewer: "pehecke"

ms.topic: "article"
author: JimDaly #TODO: NoOwner
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---
# Structure Dataverse data with nested categories

Categorizing rows in Microsoft Dataverse helps you tag the rows so that you can easily search them. Use the  `Category` table to create and manage a hierarchical structure of categories in Dataverse, and then associate rows to one or more categories.  
  
A category can have multiple child categories, but a child category can have only one parent category. Deleting a parent `Category` row automatically deletes all its child rows and table associations. You define a parent category for a category using the `Category.ParentCategoryId` column.  
  
 Use the `Category.SequenceNumber` column to programmatically define the display order for categories in the hierarchy.  When you add a new category using the web client, it is automatically added after the last category in the hierarchy. You can also use the `Category.CategoryNumber` column to programmatically set or update a number for category to help you easily distinguish a group of categories. Category number can be set to any value programmatically, but is automatically set when you create a category using the web client based on the auto-numbering prefix specified by the administrator for categories in the web client (**Settings** > **Administration** > **Auto-Numbering** > **Categories** tab).  
  
 You can associate `Category` rows with system and custom table rows by using relationships and connections. A category row can be associated with different rows. For example, you can programmatically associate a `Category` row with an `Account`, `Contact` and `Incident` rows.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
