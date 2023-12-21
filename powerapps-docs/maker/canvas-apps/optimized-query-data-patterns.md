---
title: Optimized query data patterns in Power Apps  
description: Optimized query data patterns in Power Apps.
author: lancedMicrosoft
ms.subservice: canvas-developer
ms.topic: article
ms.date: 12/01/2023
ms.author: lanced
ms.reviewer: mkaur
search.audienceType:
  - maker
contributors:
  - lancedMicrosoft
  - mduelae
  
---

# Optimized query data patterns
The simplest and fastest data query pattern is:

1. A single table or view
2. Prefiltered on the server to what you need
3. Columns are indexed correctly for the expected queries
 
When you design your app, you need to think about how to query the data quickly. The best way to query data is to use a single table or view that has all the information you need, and filter it on the server before you display it in your app. You also need to make sure that the columns you use to filter or sort the data are indexed properly. This makes your app faster and smoother.

For example, suppose you have a gallery that shows a list of customers and their salespersons. If you store the customer and salesperson information in separate tables, you need to use lookups to get the salesperson name for each customer. This slows down your app because it needs to run many queries to the other table. A better way is to create a view that combines the customer and salesperson information in one table, and use that view as the data source for your gallery. Then your app only needs to run one query to get all the data it needs.

There's a trade-off between query speed and data normalization. Data normalization means that you store the data only once, and avoid duplication. This helps to keep the data consistent and accurate. However, sometimes you need to duplicate some data to make the queries faster and easier. You need to balance these two goals in your app design and table structure. Otherwise your app will be slow and laggy because it needs to do numerous work to filter and join the data from different tables.

## Use server-side views
Views are probably the most common tool to help balance these goals.  They present a single table structure for queries, prefilter data for what you need in the query, and enable lookups and joins to other tables. Because the filters, lookups and joins for the view are computed on the server, both the payload and client-side compute are minimized. 

## Avoid too many lookups on a gallery
A gallery can display many records from a data source. But sometimes, you need to show additional information from another data source that is related to the original one. For example, you have a gallery that shows a list of customers, and you want to show the name of the salesperson who is assigned to each customer. The salesperson’s name is stored in a different data source than the customer’s information. To show the salesperson’s name, you need to use a lookup function that finds the matching record in the other data source. This expands the original table with the lookup values.

However, expanding the table can be very slow if you have many records and many lookups. For each record in the gallery, the app needs to run a separate query to the other data source and get the lookup value. This means that the app may need to run many queries for each record, which can take a long time and affect the app performance. This anti-pattern is sometimes known as “N squared, (n^2)" or an "N+1" problem.

## Use StartsWith or Filter
Power Fx provides several ways to search data. In general, use an expression that leverages an index like **StartsWith** or **Filter** instead of one that reads the entire table like **In**. The In operator is fine for in-memory collections or if the external data source table is very small.

## Consider duplicating data 
Sometimes data is slow to access in a query because it is stored in a different location or format. To make the query faster, you can copy the slow data and store it locally in a table that is fast and easy to query. However, this means that the local data may not be the most updated version of the original data. Then run another process to update the local data periodically. This process can be a Power Automate flow, a plugin, a stored procedure, or any other method that can move data from one place to another.

The frequency requirement of updating the local data depends on your business needs. How fresh does the data need to be for your app? For example, suppose you work for Contoso, a company that sells bicycles. The list of available bicycles is stored in a Products database that you can access through an API in a custom connector. But say the API call is slow, and so you decide to copy the product data and store it locally in a table. Then you create a view that combines your table with other relevant data for your app. You also create a Power Automate flow that runs every day and updates your table with the latest product data from the API. Then your app can query the local data faster, and the data is only one day old at most.

Duplicating data is a common type of technique in enterprise-grade applications to ensure good performance. You can use Dataverse plugins, stored procedures, or data movement to duplicate data into a single table that is optimized for querying. The key question is: how up to date must this data be? If you can afford some delay, you can use this technique to speed up your app.

## Suggestions

To achieve this goal, consider the following questions and suggestions:

1. How important is it for a customer to see the data value in a gallery or data grid? Would it be acceptable to first select a record and then show the data in a form?
2. Can a view do the prework necessary to see data in the right format?
3. Are you using an "IN" operator where a "StartsWith" will work? 
4. How current does your data need to be? Is there a data duplication strategy you can use to get your query to work over a single table by default?