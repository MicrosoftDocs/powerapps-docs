---
title: Use field groups for app creation | Microsoft Docs
description: Use field groups to standardize app creation across the database.
services: powerapps
documentationcenter: na
author: aneesmsft
manager: kfend
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/11/2017
ms.author: aneesa

---
# Use field groups
Field groups provide a way to group one or more fields of an entity. Field groups can help speed up and simplify the creation and maintenance of apps. A field group contains one or more fields, and a field can appear in any number of field groups. A field can't appear more than once in a field group.

Field groups are stored on an entity and shared across all apps that use the same entity. At any given time, many different apps may use the same entity and field groups of that entity. This centralization and sharing of field groups helps enforce consistency, because a field group will always display the same fields wherever it's used. This makes maintenance easy because a change to a field group is automatically reflected in all the places using that field group. Field groups help speed up the app authoring and customization process because an application author works with groups of fields, rather than individual fields.

## Default field groups
Common Data Service includes several default field groups on entities. These field groups are used in various places to help speed up and ease app creation and customization.

| Default field group name | Description |
| --- | --- |
| DefaultList |Used to display a list of records in a tabular format. |
| DefaultCard |Used to display a list of records in a card format. |
| DefaultDetails |Used to display the details of a single record in view and edit. |
| DefaultLookup |Used to display a lookup to select a record. |

## View a field group
1. Sign in to [powerapps.com](https://web.powerapps.com).
2. If you have access to more than one environment, ensure that you have the right environment selected using the environment picker in the top bar.
3. Expand the **Common Data Service** section, and click or tap **Entities** in the left navigation pane.
4. In the list of entities, click or tap the entity that you want to view the field group for.
5. In the header above the list of fields, click or tap **Field groups**. You now see all the field groups that currently exist for the entity.
6. In the list of field groups, click or tap the field group that you want to view the details for.
7. In the field group details, there are two lists side-by-side. One is titled **Entity fields** and lists all the fields for the entity. The other is titled **Field group fields** and lists the fields included in the field group.

## Modify a field group
1. View the field group that you want to modify.
2. To add a field, double-click a field name in the **Entity fields** list. You can also drag and drop fields from the **Entity fields** list to the **Field group fields** list.
3. To remove a field group, click the **X** next to the field name in the **Field group fields** list.
4. Click or tap the **Save** button.

> [!NOTE]
> Modifying field groups for [standard entities](guided-learning/manage-data.yml#step-2) isn't currently supported, but you can modify field groups for your custom entities.*

## Creating a field group
Default field groups are automatically created when you create an entity. Creating additional field groups isn't currently supported.

## Delete a field group
Deleting a field group isn't currently supported.

## View and edit field group data in Microsoft Excel
1. View the field groups for the entity that you want to examine the data for.
2. There is an Excel icon next to each field group. The Excel icon is enabled only if the field group has fields.
3. Click the Excel icon for the field group that you want to open in Excel. A workbook is generated containing the entity field list, the Excel Add-in, and a pointer to your environment.
4. Open the generated workbook that's provided by the browser.
5. After the workbook is open, enable editing. The Excel Add-in will then read the data into the workbook. For more information, see [Open entity data in Excel](data-platform-interactive-excel.md).

## Field group usage
The default field groups help speed up application authoring and customization. Some places where you can currently see field groups in action are:

* **Entity form control** - Entity form control uses the default field groups to display dynamic forms that help speed up the app authoring process, help enforce consistency, and also ease maintenance. For more details, see [Use the Entity Form control](entity-form-control.md).
* **Lookup control** - If one of the fields that you add on your screen is a reference to another linked entity, the field is rendered as a lookup control (picklist). When a user clicks the lookup control to select a record from the linked entity, the fields displayed are determined by the **DefaultLookup** field group on the linked entity. Only the first two fields of the **DefaultLookup** field group are used.
* **Creating an app** - When you generate an app by choosing the option to create an app from data, the screens for the entity that you select are automatically created. The **Display form** control on the **Display** screen and the **Edit form** control on the **Edit** screen use the **DefaultDetails** field group to determine which fields will be added by default to those screens.

