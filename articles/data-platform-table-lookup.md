<properties
	pageTitle="Table relationships via lookup field | Microsoft PowerApps"
	description="Build relationships between tables using lookup field."
	services="powerapps"
	documentationCenter="na"
	authors="guangyang"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/19/2016"
   ms.author="guayan"/>

# Table relationships via a lookup field

In many cases, tables need to have relationships with each other. For example, in the standard tables we provide, a record in the Account table represents an organization that might do business with your organization, and a record in the Contact table represents a person. There is a relationship between Account and Contact, because an account needs to have a contact so that we know who to contact regarding to a particular account. A relationship like this is modeled as a lookup field in the PowerApps data platform.

## Understanding relationships

A relationship is used to describe the case where you need to connect records from multiple tables together to enable your scenarios. A single relationship is set up between two tables. You can have multiple relationships to the same or different tables, which might have other relationships for themselves.

Some common relationship types are:

* **Normal**: This is a relationship from one table to another table. This is supported by PowerApps.
* **Self**: This is a relationship from one table to itself. This is supported by PowerApps.
* **One-to-one**: This is a relationship where one record in table A can have no more than one matching record in table B, and one record in table B can have no more than one matching record in table. This is supported by PowerApps.
* **One-to-many**: This is a relationship where one record in table A can have many matching records in table B, but a record in table B can have only one matching record in table A. This is supported by PowerApps.
* **Many-to-many**: This is a relationship where one record in table A can have many matching records in table B, and one record in table B can have many matching records in table. This is not supported by PowerApps.

## Lookup field

The PowerApps data platform supports table relationships via a lookup field. A lookup field is a field in a table with the data type specified as **Lookup**. It points to another table which you need the relationship with.

To create a lookup field:

1. Sign in to [PowerApps portal]() with your organization's account.
2. Click the **Manage** tab in the left navigation pane. Click **Tables** to navigate to the table management page.
3. Find the table you need. You can search for it in the search bar at the top.
4. Click the table to navigate to the fields page which will show all the fields of the table.
5. Click the **Add field** button. This will add a new row to the bottom of the fields grid where you can enter the field information.
6. Specify the field name and display name.
7. For the type, choose **Lookup**.
8. In the **Table to lookup to** list, select the table you want this field to serve as a lookup to.
9. Click the **Save** button to commit the change.

## Using a lookup field in PowerApps

You can use a lookup field when building an app in PowerApps.

```
Waiting for response from Greg.
```

## Deleting a record with lookup field

After table A has a lookup field to table B, it affects the record delete behavior in the following ways:

* You can delete any record in table A without restriction.
* When you a delete a record in table B, if this record matches one or multiple records in table A, you need to delete all the matched records in table A first.
