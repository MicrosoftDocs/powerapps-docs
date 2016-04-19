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

# Table relationships via lookup field

In many cases, tables need to have relationships between each other. For example, in the standard tables we provide, Account table represents an organization which may do business with your organization, Contact table represents a person, and there is a relationship between Account and Contact that an account needs to have a contact so that we know who to contact regarding to a particular account. Such relationship is modeled as lookup field in PowerApps data platform.

## Understanding relationships

Relationship is used to describe the case where you need to correlate records from multiple tables together to enable your scenarios. A single relationship is set up between two tables. You can have multiple relationships to the same or different tables, who may have other relationships for themselves.

Following are some of the most common relationship types:

1. Normal relationship: this is a relationship from one table A to another table B. This is the most common case and it's supported by PowerApps.
2. Self relationship: this is a relationship from one table to itself. This is supported by PowerApps.
3. One-to-one relationship: this is a relationship where one record in table A can have no more than one matching record in table B, and vice versa. This is supported by PowerApps.
4. One-to-many relationship: this is a relationship where one record in table A can have many matching records in table B, but a record in table B can have only one matching record in table A. This is the most common case and it's supported by PowerApps.
5. Many-to-many relationship: this is a relationship where one record in table A can have many matching records in table B, and vice versa. This is not supported by PowerApps.

## Lookup field

PowerApps data platform supports table relationships via lookup field. A lookup field is essentially a field in a table with data type specified as **Lookup**. It points to some other table which you need the relationship with.

To create a lookup field, following are the steps:

1. Login to [PowerApps portal]() with your organization's account.
2. Click the **Manage** tab on the left hand navigation pane. Then Click **Tables** to navigate to the table management page.
3. Find the table you need. You can search for it in the search bar on the top.
4. Click the table to navigate to the fields page where it will show all the fields of the table.
5. Click the **Add field** button. This will add a new row to the bottom of the fields grid where you can enter the field information.
6. Specify the field name and display name.
7. For type, choose **Lookup**.
8. In the **Table to lookup to** dropdown list, select the table you want this field to lookup to.
9. Click the **Save** button to commit the change.

## Using lookup field in PowerApps

You can use a lookup field when building an app in PowerApps with the following formula.

```
Waiting for response from Greg.
```

## Deleting a record with lookup field

Once table A has a lookup field to table B, it impacts the record delete behavior in the following way:

1. You can delete any record in table A without any restriction.
2. When deleting a record in table B, if this record matches one or multiple records in table A, you need to delete all the match records in table A first.