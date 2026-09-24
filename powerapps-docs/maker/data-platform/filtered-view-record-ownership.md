---
title: Filtered record ownership
description: Learn how to
ms.component: pa-admin
ms.date: 09/24/2026
ms.topic: concept-article
author: paulliew
ms.subservice: dataverse-maker
ms.author: paulliew
ms.reviewer: ellenwehrle
search.audienceType: 
  - maker
---
# Filtered record ownership (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

Row-level security for filtered record ownership of Dataverse tables allows privileges to be defined based on filtered views of columns. For example, privileges can be set where the column **City** has values such as **Redmond**, **Seattle**, or **Bellevue**. Security roles can be created, and data access is granted based on these filter privileges, allowing users to create or read records based on the value of the **City** column. CRUD (create, read, update, delete) calls are filtered and secured to records that were granted based on these filtered views, according to the user's assigned security roles.

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

Filtered record ownership of Dataverse tables doesn't include record ownership. This means that records can't be owned by an individual. Since there's no record owner, these records can't be shared or assigned to an individual. When you create the filtered, record ownership table, the system creates a global **All records** CRUD privilege and gives it to the system administrator security role.

## How does filtered record ownership work?

Row-level security with filtered view privileges in your data models is an important feature that restricts data access for certain users based on filter conditions of column values. It's crucial to understand that row-level security can't be configured to restrict access to model objects, such as tables, columns, or views. With Dataverse, row-level security filtered privilege allows you to define filters within roles to limit data access at the row level. This means that users can only read and update rows that they have permission to within the Dataverse form. Row-level security filtered privilege restricts data access for users with **Create, Read, Write, Delete, Append,** and **Append to** table privileges.

Row-level security features are essential for controlling access to specific rows within your data models, ensuring that users only see the data they are permitted to see. This level of granular access control enhances data confidentiality by allowing you to manage data access at a very detailed level.

Here's an overview of the procedures you need to complete.

1. [Create a table with filtered record ownership](#create-a-filtered-record-ownership-table).
1. [Create a filter](#create-filters).
1. [Create a record filter](#create-a-record-filter).
1. [Create an entity record filter](#create-an-entity-record-filter).
1. [Create a security role](#create-and-assign-a-security-role) (or use an existing security role) and grant filter privileges.
1. [Assign a security role](#create-and-assign-a-security-role) with filtered privileges to the user.

## Prerequisites

To create and assign the security roles required for this feature you need the system administrator security role.

## Create a filtered record ownership table

1. Go to [Power Apps](https://make.powerapps.com).

1. Select your environment.

1. Go to **Solutions**, open the solution you want or create a new one.

1. Select **New table** on the command bar, and then select **Table (advanced properties).**

1. Enter a table **Display name**.

1. From the **Record ownership** list, select **Filtered (preview)**.

1. Select **Save**.

Test your filter by entering some rows in the table you just created. For example, the following image shows some rows added to the table.

:::image type="content" source="media/filtered-view-record-ownership/table-sample-data-rows.png" alt-text="Screenshot of a table with sample data rows entered, showing the Record ownership dropdown set to Filtered (preview)." lightbox="media/filtered-view-record-ownership/table-sample-data-rows.png":::

## Create filters

To control data access to the filtered record ownership tables, create filters. These filters set the condition for which rows are accessed and returned from the database. Use [**FetchXml**](/power-apps/developer/data-platform/fetchxml/overview?form=MG0AV3) to create the filters.

You can also create filters by using **Edit the view with advanced filter queries** on the table view form.

1. Open your model-driven app for editing.​

1. Open a table where you want to create filtered view record ownership, such as **Accounts**.

1. Select **Filters** on the top right-hand corner of the action bar.​

1. Update the filters or remove them from the screen.
1. Select **+ Add** to add a new filter, such as *City* equals *Redmond* added here.​
   :::image type="content" source="media/filtered-view-record-ownership/edit-filters-dialog-city-redmond.png" alt-text="Screenshot of the Edit filters dialog showing a filter where City equals Redmond, with options to add more filters or download FetchXML." lightbox="media/filtered-view-record-ownership/edit-filters-dialog-city-redmond.png":::
1. Continue to **+ Add** more filters as needed.
1. Select **Download FetchXML** when you're done with selecting all the fields and operators.​
1. Open the **Notepad** app and open the downloaded **FetchXML**.

## Create a record filter

A Record filter is a security predicate for filtered record ownership table. It's used to grant permission to the table in a security role. The record filter determines which rows in a database table a user is allowed to access.

1. Go to [Power Apps](https://make.powerapps.com).
1. Select your environment.
1. Go to **Solutions** and create a new solution or open an existing solution.
1. Select **+ New**.
1. Select **More** and **Other**.
1. Select **Record Filter**.
1. Enter a Unique Name with a prefix, such as new_*filter name*.
1. Enter a **Display name**, such as *City of Redmond*.
1. Return to your Notepad session, which has the **FetchXML**​.
1. Copy the **FetchXML** and paste it in the FetchXML box.
1. Select **Save & close**.

## Create an entity record filter

*Entity record filter* is the list of record filters that is associated to the table. There can be multiple record filters for each table. For example, where **City** equals *Redmond*, and another one for **City** in *Kirkland*, or *Sammamish*, or other city. Each of these record filters can be activated by creating their respective entity record filter entry. To prevent locking out access to the records on a filtered record ownership table, a **All** **Records** entity record filter is provided by the system and is automatically granted to system administrator.

1. Return to your Solution.
1. Select **+ New**.
1. Select **More** and **Other**.
1. Select **EntityRecordFilter**.
1. Enter a **Name**, such as *City of Redmond*.
1. Select the **Record Filter**, such as *City of Redmond*.
1. Enter the **Related Entity**, the logical name of the table, such as account.
1. Select **Save & close**.​

:::image type="content" source="media/filtered-view-record-ownership/entity-record-filter-list-view.png" alt-text="Screenshot of the Entity Record Filter list view with the New button highlighted." lightbox="media/filtered-view-record-ownership/entity-record-filter-list-view.png":::

## Create and assign a security role

All activated entity record filter security predicates for a table can be granted by an admin to a security role. Roles can be assigned to the **Create, Read, Write, Delete, Append** and **Append to** privileges.

For example, granting the **Redmond rows** record filter permission the **Read** privilege.

:::image type="content" source="media/filtered-view-record-ownership/security-role-read-privilege.png" alt-text="Screenshot of the security role configuration showing the Redmond rows filter granted to the Read privilege." lightbox="media/filtered-view-record-ownership/security-role-read-privilege.png":::

Then assign the role to users or teams.

:::image type="content" source="media/filtered-view-record-ownership/manage-security-roles-dialog.png" alt-text="Screenshot of the Manage security roles dialog for assigning roles to a user." lightbox="media/filtered-view-record-ownership/manage-security-roles-dialog.png":::

For more information about creating and assigning security roles, see [create/edit security role](/power-platform/admin/create-edit-security-role) and  [assign a security to a user](/power-platform/admin/assign-security-roles)

## Example filtered view record ownership implementation

A user with assigned security role to read Redmond rows accesses the form and can see rows from *City of Redmond*.

:::image type="content" source="media/filtered-view-record-ownership/filtered-table-redmond-records.png" alt-text="Screenshot of the filtered table view showing only Redmond city records visible to the user." lightbox="media/filtered-view-record-ownership/filtered-table-redmond-records.png":::

A Power Platform admin can see all records because the admin has global **All records** permission on the Read privilege.

:::image type="content" source="media/filtered-view-record-ownership/admin-all-records-table-view.png" alt-text="Screenshot of the filtered table view showing all records visible to the administrator." lightbox="media/filtered-view-record-ownership/admin-all-records-table-view.png":::

## Frequently asked questions

### What are some common use cases for this filter row-level security?

Common use cases include granting data access to a different user persona, for example an accounting clerk can access to certain Departments and/or locations, while the accounting manager can have access to all Departments.

### Is there a record owner for a filtered record ownership table?

No, there is no record owner. It has the Created by field to track who created the record, but the record isn't owned by anyone. Permission to record is granted via security role privileges.

### Can filtered record ownership table's records be shared and/or assigned?

No, since there is no record owner on the record, the record cannot be shared and/or assigned to an individual.

### Does filter permissions affect query performance?

Yes. Every query applies filter permissions. An efficient data model and filter design should mitigate performance problems.

### Can I use filter permissions in my existing user or organization record ownership tables?

Yes. You can create record filters for existing user or organization owned record ownership tables.

### Can I use filter permissions to external virtual tables?

Not currently.

### Can I change my organization record ownership table to filtered record ownership?

No. After you create a table, you can't change its record ownership type.

## Limitations

### Dataverse Search returns results for primary table

For filter queries that involve a link-entity relationship, such as Account linked to Contact, Dataverse Search returns results from the primary table only and doesn't include values from the linked table.

## Related articles

[Create and edit tables using the table designer](../canvas-apps/create-edit-tables.md)   
[Filtered record ownership by using code](../../developer/data-platform/filtered-record-ownership.md)
