---
title: "Create N:N (many-to-many) entity relationships in Common Data Service for Apps using solution explorer | MicrosoftDocs"
description: "Learn how to create many-to-may relationships"
ms.custom: ""
ms.date: 05/29/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create N:N (many-to-many) entity relationships in Common Data Service for Apps using solution explorer

Solution explorer provides one way to create and edit N:N (many-to-many) for Common Data Service for Apps.

The [PowerApps portal](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) enables configuring the most common options, but certain options can only be set using solution explorer. More information:
- [Create Many-to-many (N:N) entity relationships](create-edit-nn-relationships.md)
- [Create Many-to-many entity relationships in Common Data Service for Apps using PowerApps portal](create-edit-nn-relationships-portal.md)

  
## Open solution explorer

Part of the name of any custom relationship you create is the customization prefix. This is set based on the solution publisher for the solution you’re working in. If you care about the customization prefix, make sure that you are working in an unmanaged solution where the customization prefix is the one you want for this entity. More information: [Change the solution publisher prefix](change-solution-publisher-prefix.md) 

[!INCLUDE [cc_navigate-solution-from-powerapps-portal](../../includes/cc_navigate-solution-from-powerapps-portal.md)]

## View entity relationships

In solution explorer, expand **Entities** an select an entity. Within that entity, select  **N:N Relationships**.

![View N:N entity relationships](media/view-nn-entity-relationships-solution-explorer.png)

## Create relationships

While [viewing entity relationships](#view-entity-relationships), select **New Many-to-Many Relationship** from the command bar.

> [!NOTE]
> If the command is not available, the entity is not eligible to create a custom relationship.

![New many-to-many relationship form](media/new-nn-entity-relationship-form-solution-explorer.png)

In the **Other Entity** group, in the **Entity Name** field, choose the entity that you want to create the relationship with. This will populate the **Name** and **Relationship Entity Name** fields in the **Relationship Definition** group.

You can click ![Save entity relationship button](media/save-entity-icon-solution-explorer.png) to save the entity and continue editing. More information: [Edit relationships](#edit-relationships)

> [!NOTE]
> If either the **Name** or **Relationship Entity Name** values already exist in the system you will get an error when you save. Edit the values so that they are unique and try again.

## Edit relationships

While [viewing entity relationships](#view-entity-relationships), select the entity you want to edit. 

> [!NOTE]
> The publisher of a managed solution can prevent customizations of relationships that are part of their solution.

The following entity relationship properties can be edited after the relationship is created.

> [!IMPORTANT]
> After you edit these properties you must publish customizations before they will take effect in model-driven apps.

### Edit Display options

For both the **Current Entity** and the **Other Entity**, you can edit the display option fields which control how the related entities are displayed for model-driven apps.

|Field|Description|
|--|--|
|**Display Option**|How the related entity list should be displayed. More information: [Display Options](#display-options)|
|**Custom Label**|Specify the localizable text to be used instead of the plural name when you select **Use Custom Label** as the **Display Option** .|
|**Display Area**|Select one of the available groupings to display this list. The available options are: **Details** (for the *Common* group), **Marketing**, **Sales**, and **Service**. |
|**Display Order**|Controls where the navigation item will be included within the selected display area. The range of allowed numbers begins with 10,000. Navigation pane items with a lower value appear above other relationships with a higher value.|

<!-- TODO: Not sure whether Display Area or Display Order are still used anymore. Might only be used in the Outlook client?-->

#### Display Options

These are the available display options:

|Option|Description|
|--|--|
|**Do not Display**|Do not display the related entities for this relationship.|
|**Use Custom Label**|When this option is chosen, the **Custom Label** field is enabled so that you can specify the localizable text to be used instead of the plural name.|
|**Use Plural Name**|Use the plural display name defined for the related entity.|

### Searchable

You can hide the relationship from **Advanced Find** in model-driven apps by setting the **Searchable** field to **No**.

## Delete relationships

While [viewing entity relationships](#view-entity-relationships), select the entity relationship you want to delete and click the ![Delete command](media/delete.gif) command.

Deleteing the relationship will delete the relationship entity created. All data connecting entities using the relationship will be lost.

### See also

[Create Many-to-many (N:N) entity relationships](create-edit-nn-relationships.md)<br />
[Create Many-to-many entity relationships in Common Data Service for Apps using PowerApps portal](create-edit-nn-relationships-portal.md)<br />
[Create and edit 1:N (one-to-many) or N:1 (many-to-one) entity relationships](create-edit-1n-relationships.md)
