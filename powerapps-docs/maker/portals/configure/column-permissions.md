---
title: Configure column permissions for portals
description: Configure column permissions for use with the portals Web API. 
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 01/31/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - neerajnandwana-msft
---

# Configure column permissions

[Table permissions](assign-entity-permissions.md) are used to apply security in portals to individual Dataverse table records. You can add **column permissions** to individual table columns. Column permissions are an optional configuration that are associated with [web roles](create-web-roles.md).

> [!NOTE]
> Column permissions are currently only applicable for [portal Web API](../web-api-overview.md) features.

Web roles can have any number of table permissions and column permissions. If web role has multiple column permissions, then all column permissions are applied to the selected web role.

When evaluating the permissions, table permissions are evaluated first. If a user has access to table then respective table's column permissions will be applied. If the user doesn't have access to table, then any column permissions configuration will be ignored.

When no column permissions are defined, then corresponding table permissions will apply to all columns.

> [!Important]
> This feature requires the following versions for starter portal package and portal host:
> - Portal host version 9.4.1.x or later.
> - Starter portal package version 9.3.2201.x or later.

## Add column permissions to a web role

1. Open the [Portal Management app](configure-portal.md).

1. Go to **Portals** > **Web Roles** and open the web role that you want to add column permissions.

1. Under **Related**, select **Column Permission Profiles**.

1. Select **Add Existing Column Permission Profiles** to add an existing column permission to a web role.

1. Browse for a column permission profile or select **New Column Permission Profiles** to create a new column permission profile record.

    :::image type="content" source="media/column-permissions/column-permission-profiles.png" alt-text="Adding column permission profiles.":::

## Attributes and relationships

:::image type="content" source="media/column-permissions/manage-column-permission.png" alt-text="Managing column permissions.":::

The following table explains the table permission attributes.

| **Name** | **Description** |
|-------------------------|-------------------------|
| Profile Name | The descriptive name of the record. This field is required. |
| Table Name | The logical name of the table that column is to be secured. This field is required. |
| Website | The associated website. This field is required. |
| All Column Permissions | This setting will allow users to limit table permission access scope. It's a multiple selection field. For example, the table permission allows the user to **Create**, **Read** all columns. Using this setting, you can further limit to only read permissions for all columns.</br></br>Available permissions:<ul><li>Create</li><li>Read</li><li>Update</li></ul></br>This configuration is useful when you want a specific web role to be able to read all contact fields but allow updates to the first name, and last name columns. You have to select **Read** option for the **All Column Permissions** setting and create column permission records for the first name, and last name columns with read and update permissions. |
| Column Permissions | The associated column permissions. This allows users to define specific permissions for table columns. Columns not defined here will follow the **All Column Permissions** setting. |
| Web Roles | The associated web roles. |

## Examples

In this example, we have the contact table with the columns; *JobTitle* and *Salary*.

The following table demonstrates the result of applying different column and table permissions to the contact table and the additional columns.

| **Table Permission** | **Site Setting**<br><em>**Webapi/contact/enabled**</em> | **Site Setting**<br><em>**Webapi/contact/fields**</em> | **Column Permission** | **Scenario** |
|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
| Contact (Create, Read, Update) | TRUE |  |  | User will not have any permissions to the columns. |
| Contact (Create, Read, Update) | FALSE |  |  | User will not have any permissions to the columns. |
| Contact (&lt;none&gt;) | TRUE | * | **All Column Permissions:** Create, Read, Update</br>**Column Permissions:** &lt;none&gt; | User will not have any permissions to the columns. |
| Contact (Create, Read, Update) | TRUE | * |  | User will have Create, Read, Update permissions on all contact table columns. |
| Contact (Create, Read, Update) | TRUE |  | **All Column Permissions:** Create, Read, Update</br>**Column Permissions:** &lt;none&gt; | User will not have any permissions to the columns. |
| Contact (Create, Read, Update) | TRUE | * | **All Column Permissions:** &lt;none&gt;</br>**Column Permissions:**</br><ul></br><li>**JobTitle:** Read</li></br></ul> | User will have Read on JobTitle and Create, Read, Update on all the other columns. |
| Contact (Create, Read, Update) | TRUE | * | **All Column Permissions:** Read</br>**Column Permissions:**</br><ul></br><li>**JobTitle:** Create, Read, Update</li></br></ul> | User will have Create, Read, Update on JobTitle and only Read on all the other columns. |
| Contact (Create, Read, Update) | TRUE | JobTitle, Salary |  | User will have Create, Read, Update on JobTitle and Salary. |
| Contact (Create, Read, Update) | TRUE | JobTitle, Salary | **All Column Permissions:** Create, Read, Update</br>**Column Permissions:** &lt;none&gt; | User will have Create, Read, Update on JobTitle and Salary, no permission on other columns. |
| Contact (Create, Read, Update) | TRUE | JobTitle, Salary | **All Column Permissions:** &lt;none&gt;</br>**Column Permissions:**</br><ul></br><li>**JobTitle:** Create, Read, Update</li></br><li>**Salary:** Create, Read, Update</li></br></ul> | User will have Create, Read, Update on JobTitle and Salary. |
| Contact (Create, Read, Update) | TRUE | JobTitle | **All Column Permissions:** &lt;none&gt;</br>**Column Permissions:**</br><ul></br><li>**JobTitle:** Create, Read, Update</li></br><li>**Salary:** Create, Read, Update</li></br></ul> | User will have Create, Read, Update on JobTitle and no permission on Salary. |
| Contact (Create, Read, Update) | TRUE | JobTitle, Salary | **All Column Permissions:** &lt;none&gt;</br>**Column Permissions:**</br><ul></br><li>**JobTitle:** Create, Read, Update</li></br><li>**Salary:** Read</li></br></ul> | User will have Create, Read, Update on JobTitle, and Read on Salary. |

### See also

[Assign table permissions](assign-entity-permissions.md)</br>
[Create web roles for portals](create-web-roles.md)</br>
[Portals Web API overview](../web-api-overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
