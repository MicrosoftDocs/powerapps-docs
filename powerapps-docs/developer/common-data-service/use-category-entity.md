---
title: "Use the Category entity (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about categorizing the entity records using category entity." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Use the Category entity

Categorizing entity records in Common Data Service (CDS) for Apps helps you tag the records so that you can easily search them. Use the  `Category` entity to create and manage a hierarchical structure of categories in CDS for Apps, and then associate entity records to one or more categories.  
  
 A category can have multiple child categories, but a child category can have only one parent category. Deleting a parent `Category` record automatically deletes all its child records and entity associations. You define a parent category for a category using the `Category.ParentCategoryId` attribute.  
  
 Use the `Category.SequenceNumber` attribute to programmatically define the display order for categories in the hierarchy.  When you a add a new category using the web client, it is automatically added after the last category in the hierarchy. You can also use the `Category.CategoryNumber` attribute to programmatically set or update a number for category to help you easily distinguish a group of categories. Category number can be set to any value programmatically, but is automatically set when you create a category using the web client based on the auto-numbering prefix specified by the administrator for categories in the web client (**Settings** > **Administration** > **Auto-Numbering** > **Categories** tab).  
  
 You can associate `Category` records with system and custom entity records by using relationships and connections. A category record can be associated with different entity records. For example, you can programmatically associate a `Category` record with an `Account`, `Contact` and `Incident` records.   

