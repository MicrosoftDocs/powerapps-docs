---
title: Configure column permissions for portals
description: Configure column permissions for use with the portals Web API. 
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 06/14/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - neerajnandwana-msft
---

# Configure column permissions

In portals, [table permissions](assign-entity-permissions.md) are used to apply security to individual Dataverse table records. You can add column permissions to individual table columns. Column permissions are an optional configuration that you associate with [web roles](create-web-roles.md).

> [!NOTE]
> Column permissions are currently only applicable for [portal Web API](../web-api-overview.md) features.

Web roles can have any number of table permissions and column permissions. If a web role has multiple column permissions, all column permissions are applied to the selected web role.

When permissions are evaluated, table permissions are evaluated first. If a user has access to a table, the table's column permissions will be applied. If the user doesn't have access to the table, any configured column permissions will be ignored.

When no column permissions are defined, the corresponding table permissions will apply to all columns.

> [!Important]
> This feature requires the following versions for starter portal package and portal host:
> - Portal host version 9.4.1.*x* or later.
> - Starter portal package version 9.3.2201.*x* or later.

## Add column permissions to a web role

1. Open the [Portal Management app](configure-portal.md).

1. Go to **Portals** > **Web Roles** and open the web role that you want to add column permissions.

1. Under **Related**, select **Column Permission Profiles**.

1. Do one of the following:

   1. To add an existing column permission to the web role, select **Add Existing Column Permission Profiles**, and then browse to the record you want.

   1. To create a new column permission profile record, select **New Column Permission Profiles**.

    :::image type="content" source="media/column-permissions/column-permission-profiles.png" alt-text="Adding column permission profiles.":::

## Attributes and relationships

:::image type="content" source="media/column-permissions/manage-column-permission.png" alt-text="Managing column permissions.":::

The following table explains the table permission attributes.

| **Name** | **Description** |
|-------------------------|-------------------------|
| Profile Name | The descriptive name of the table record. This field is required. |
| Table Name | The logical name of the table in which the column is to be secured. This field is required. |
| Website | The associated website. This field is required. |
| All Column Permissions | Available permissions:<ul><li>Create</li><li>Read</li><li>Update</li></ul>This setting allows users to limit the scope of table permission access. It's a multiple selection field.<br><br>For example, the table permissions might allow a user Create and Read permissions on all columns. Using this setting, you can further limit users to only Read permissions for all columns.</br></br>In another example, you might want a specific web role to be able to read all contact fields but you also want to allow the web role to update the first name and last name columns. In this case, you select the **Read** option for the **All Column Permissions** setting, and create column permission profiles for the First Name and Last Name columns with Read and Update permissions. |
| Column Permissions | The associated column permissions. This allows users to define specific permissions for table columns. Columns that aren't defined here will follow the **All Column Permissions** setting. |
| Web Roles | The associated web roles. |

## Examples

In this example, we have a contact table with the columns **JobTitle** and **Salary**.

The following table shows the result of applying different column and table permissions to the contact table and the additional columns.

| **Scenario** | **Table permission** | **Site  setting**<br><em>**Webapi/contact/enabled**</em> | **Site setting**<br><em>**Webapi/contact/fields**</em> | **Column permission** | 
|-|-|-|-|-|
| The user won't have any permissions to the columns. | Contact (Create, Read, Update) | TRUE |  |  |  
| The user won't have any permissions to the columns. | Contact (Create, Read, Update) | FALSE |  |  | 
| The user won't have any permissions to the columns. | Contact (&lt;none&gt;) | TRUE | * | **All Column Permissions:** Create, Read, Update</br>**Column Permissions:** &lt;none&gt; |
| The user will have Create, Read, and Update permissions on all *contact* table columns. | Contact (Create, Read, Update) | TRUE | * |  |
| The user won't have any permissions to the columns. | Contact (Create, Read, Update) | TRUE |  | **All Column Permissions:** Create, Read, Update</br>**Column Permissions:** &lt;none&gt; |
| The user will have Read on *JobTitle* and Create, Read, and Update on all the other columns. | Contact (Create, Read, Update) | TRUE | * | **All Column Permissions:** &lt;none&gt;</br>**Column Permissions:**</br><ul></br><li>**JobTitle:** Read</li></br></ul> | |
| The user will have Create, Read, and Update on *JobTitle* and only Read on all the other columns.| Contact (Create, Read, Update) | TRUE | * | **All Column Permissions:** Read</br>**Column Permissions:**</br><ul></br><li>**JobTitle:** Create, Read, Update</li></br></ul>  |
| The user will have Create, Read, and Update on *JobTitle* and *Salary.* | Contact (Create, Read, Update) | TRUE | JobTitle, Salary |  |  
| The user will have Create, Read, and Update on *JobTitle* and *Salary*, no permission on other columns. | Contact (Create, Read, Update) | TRUE | JobTitle, Salary | **All Column Permissions:** Create, Read, Update</br>**Column Permissions:** &lt;none&gt; |  
| The user will have Create, Read, and Update on *JobTitle* and *Salary*. | Contact (Create, Read, Update) | TRUE | JobTitle, Salary | **All Column Permissions:** &lt;none&gt;</br>**Column Permissions:**</br><ul></br><li>**JobTitle:** Create, Read, Update</li></br><li>**Salary:** Create, Read, Update</li></br></ul> |
| The user will have Create, Read, and Update on *JobTitle* and no permission on *Salary*.| Contact (Create, Read, Update) | TRUE | JobTitle | **All Column Permissions:** &lt;none&gt;</br>**Column Permissions:**</br><ul></br><li>**JobTitle:** Create, Read, Update</li></br><li>**Salary:** Create, Read, Update</li></br></ul>  |
| The user will have Create, Read, and Update on *JobTitle* and Read on *Salary*. | Contact (Create, Read, Update) | TRUE | JobTitle, Salary | **All Column Permissions:** &lt;none&gt;</br>**Column Permissions:**</br><ul></br><li>**JobTitle:** Create, Read, Update</li></br><li>**Salary:** Read</li></br></ul> |

### See also

[Assign table permissions](assign-entity-permissions.md)</br>
[Create web roles for portals](create-web-roles.md)</br>
[Portals Web API overview](../web-api-overview.md)

