---
title: "Create and edit entities using Power Apps portal | MicrosoftDocs"
description: "Learn how to create and edit entities using Power Apps portal"
ms.custom: ""
ms.date: 05/30/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
author: "Mattp123"
ms.assetid: fa04f99d-a5f9-48cb-8bfb-f0f50718ccee
caps.latest.revision: 41
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create and edit entities using Power Apps portal

The [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) provides an easy way to create and edit entities for  Common Data Service.

The portal enables configuring the most common options, but certain options can only be set using solution explorer. More information: 
- [Create and edit entities in Common Data Service](create-edit-entities.md)
- [Create and edit entities using solution explorer](create-edit-entities-solution-explorer.md)

## View entities

1. From the [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Data** > **Entities**.

![View entities](media/view-entities-portal.png)

You can filter the entities you see using the following views in a list: 

![Entity views](media/entity-views-portal.png)

 |View|Description|
 |--|--|
 |**All**| Shows all the entities|
 |**Managed**| Shows only managed and standard entities|
 |**Custom**|Shows only custom entities|
 |**Default**|Shows only the standard entities |

You can also select **Group** to group entities by the **Tags** applied to them.

## Create an entity

While [viewing entities](#view-entities), in the menu bar select **New entity**. This will open the New entity panel.

![New entity Panel](media/new-entity-panel.png)

Enter data for the following fields

|Field|Description|
|--|--|
|**Display name**|This is the singular name for the entity that will be shown in the app. This can be changed later.|
|**Plural display name**|This is the plural name for the entity that will be shown in the app. This can be changed later.|
|**Name**|This field is pre-populated based on the **Display name** you enter. It includes the customization prefix for the Common Data Service solution publisher. You cannot change this after the entity is saved.|
|**Primary Name**|This is the only field visible at this point.| Edit it if you want to change the **Display Name**or **Name** of the field.
|**Display name**|This is the main user-friendly text identifier for your record (typically a name or a number). The value of this field is shown to users when they need to select from a list of records.
|**Name**|This field is pre-populated based on the **Display name** you enter. It includes the customization prefix for the Common Data Service solution publisher. You cannot change this after the entity is saved.|

Select **Enable Attachments** to append notes and files to records for this entity.

Select **More settings**. These settings are optional for an entity.

|Field|Description|
|--|--|
|**Description**|Provide a meaningful description of the purpose of the entity.|
|**Entity type and ownership**|Switch the entity type to Activity Entity to create entities that can manage tasks. The type of **Ownership** defines who can perform operations on a record.|
|**Collaboration**|Enable features to help users to more easily work together on this entity.|
|**Create and Update Settings**|You can enable quick create forms, giving your app a streamlined data entry experience. Duplicate detection lets you set duplicate detection policies and create duplicate detection rules. Change tracking provides a way to keep data synchronized in a performant way.|
|**Dynamics 365 for Outlook**|Configure how this entity appears in Outlook.|

Select **Create** to continue, this will close the **New entity** panel and display the list of fields.

The **Primary Name** field of the entity is displayed in the list of fields. Select the **Primary Name** field to edit it if you want to change the **Display Name**or **Name** of the field. The default values are shown below:

![Primary Name panel](media/primary-name-panel.png)

## Edit an entity

While [viewing entities](#view-entities), select the entity you want to edit.

Select **Settings** from the menu if you want to edit the **Display name**, **Plural display name** or **Description** for the entity.

![Entity Settings](media/entity-settings-portal.png)

For other items choose from the tabs.

### Fields

See [Create and edit fields](create-edit-fields.md)

### Relationships

See [Create and edit relationships between entities](create-edit-entity-relationships.md)

### Business rules

See [Create business rules and recommendations to apply logic in a form](../model-driven-apps/create-business-rules-recommendations-apply-logic-form.md)

### Views

See [Create or edit a view](../model-driven-apps/create-edit-views.md)

### Forms

See [Create and design forms](../model-driven-apps/create-design-forms.md)

### Dashboards

See [Create or edit dashboards](../model-driven-apps/create-edit-dashboards.md)

### Charts

See [Create a system chart](../model-driven-apps/create-edit-system-chart.md)

### Keys

See [Define alternate keys to reference records](define-alternate-keys-reference-records.md)

### Data

View the data in the entity.
Use the **Select view** menu to choose from available views for the entity or to show all fields.

![Select view](media/entity-data-select-view.png)

Use the **Next Page** and **Previous Page** commands at the bottom of the form to see more data.

## Delete an entity

As someone with the system administrator security role, you can delete custom entities that aren’t part of a managed solution.  
  
> [!IMPORTANT]
>  When you delete a custom entity, the database tables that store data for that entity are deleted and all data they contain is lost. Any associated records that have a parental relationship to the custom entity are also deleted. For more information about parental relationships, see [Create and edit relationships between entities](create-edit-entity-relationships.md).  
  
> [!NOTE]
> The only way to recover data from an entity that was deleted is to restore the database from a point before the entity was deleted. More information: [Backup and restore instances](/dynamics365/customer-engagement/admin/backup-restore-instances)

While [viewing entities](#view-entities), select the entity and select **Delete entity** from the menu.

![Delete an entity using the Power Apps portal](media/delete-entity-powerapps-portal.png)

If the entity has dependencies that prevent it from being deleted you will see an error message. To identify and remove any dependencies, you will need to use the solution explorer. More information [Identify entity dependencies](create-edit-entities-solution-explorer.md#identify-entity-dependencies)

### See also

[Create and edit entities in Common Data Service](create-edit-entities.md)<br />
[Create and edit entities using solution explorer](create-edit-entities-solution-explorer.md)


