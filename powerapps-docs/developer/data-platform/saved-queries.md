---
title: "Saved queries (Microsoft Dataverse) | Microsoft Docs" 
description: "Learn how saved queries enhance the search capabilities of Microsoft Dataverse." 
ms.date: 03/22/2022
ms.reviewer: "pehecke"
ms.topic: "article"
author: "caburk" 
ms.subservice: dataverse-developer
ms.author: "jdaly"
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---
# Saved queries

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Saved queries are business tables that define the parameters and criteria of a Microsoft Dataverse environment search. Saved queries support cross-table searches. There are two tables available for queries against the Dataverse environment.  
  
- A *user query*, called a saved view in the application, is owned by an individual user, can be assigned and shared with other users, and can be viewed by other users depending on the query's access privileges. This is appropriate for frequently used queries that span table types and queries that perform aggregation. More information: [UserQuery table](reference/entities/userquery.md) 

- A *saved query*, called a view in the application, is owned by an organization making it visible to all users in the organization. Saved queries (views) are used for both views defined for a table and for filters and templates for Dynamics 365 for Outlook. More information: [SavedQuery table](reference/entities/savedquery.md) 
  
 A query in the form of a FetchXML statement is constructed and then assigned to the `UserQuery.FetchXml` column. This query can be executed by using the <xref:Microsoft.Crm.Sdk.Messages.ExecuteByIdUserQueryRequest> message.  
  
 You can see the user query in the **Advanced Find** section of the model-driven app and also in the **View** drop-down list for a table.  You can export the value of the `UserQuery.FetchXml` column by using the **Download Fetch XML** button in the **Advanced Find** dialog box.  
  
## Use Web API to execute saved queries

To know about executing user query and saved query using Web API, see [Retrieve and execute predefined queries](webapi/retrieve-and-execute-predefined-queries.md)

## Use SDK for .NET to execute saved queries

You can use the <xref:Microsoft.Crm.Sdk.Messages.ExecuteByIdUserQueryRequest> and <xref:Microsoft.Crm.Sdk.Messages.ExecuteByIdSavedQueryRequest> messages to execute user query and saved query respectively.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
