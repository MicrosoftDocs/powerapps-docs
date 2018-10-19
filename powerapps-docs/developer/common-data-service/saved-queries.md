---
title: "Saved queries (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how saved queries augment the search environment in CDS for Apps." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Saved queries

Saved queries are business entities that define the parameters and criteria of a Common Data Service (CDS) for Apps environment search. Saved queries support cross-entity searches. There are two entities available for queries against the Common Data Service (CDS) for Apps environment.  
  
- A *user query*, called a saved view in the application, is owned by an individual user, can be assigned and shared with other users, and can be viewed by other users depending on the query's access privileges. This is appropriate for frequently used queries that span entity types and queries that perform aggregation. 

- A *saved query*, called a view in the application, is owned by an organization making it visible to all users in the organization. Saved queries (views) are used for both views defined for an entity and for filters and templates for Dynamics 365 for Outlook.  
  
 A query in the form of a FetchXML statement is constructed and then assigned to the `UserQuery.FetchXml` attribute. This query can be executed by using the <xref:Microsoft.Crm.Sdk.Messages.ExecuteByIdUserQueryRequest> message.  
  
 You can see the user query (saved view) in the Advanced Find section of the PowerApps application and also in the **View** drop-down list for an entity.  You can export the value of the `UserQuery.FetchXml` attribute by using the **Download Fetch XML** button in the **Advanced Find** dialog box.  
  


<!-- 

Need PM owner for query questions

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/userquery-saved-view-entity 

This topic needs to be adapted to describe the concept of saved queries, both user-queries and systemviews

It should cover using these messages 

ExecuteByIdUserQuery 
ExecuteByIdSavedQuery

or is an entity-operations- topic enough?

And support the Web API content here:
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/webapi/retrieve-and-execute-predefined-queries

-->