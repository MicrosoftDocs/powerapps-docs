---
title: "Saved queries (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how saved queries augment the search environment in CDS for Apps." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Saved queries

Saved queries are business entities that define the parameters and criteria of a Common Data Service (CDS) for Apps environment search. Saved queries support cross-entity searches. There are two entities available for queries against the Common Data Service (CDS) for Apps environment.  
  
- A *user query*, called a saved view in the application, is owned by an individual user, can be assigned and shared with other users, and can be viewed by other users depending on the query's access privileges. This is appropriate for frequently used queries that span entity types and queries that perform aggregation. More information: [UserQuery entity](reference/entities/userquery.md) 

- A *saved query*, called a view in the application, is owned by an organization making it visible to all users in the organization. Saved queries (views) are used for both views defined for an entity and for filters and templates for Dynamics 365 for Outlook. More information: [SavedQuery entity](reference/entities/savedquery.md) 
  
 A query in the form of a FetchXML statement is constructed and then assigned to the `UserQuery.FetchXml` attribute. This query can be executed by using the <xref:Microsoft.Crm.Sdk.Messages.ExecuteByIdUserQueryRequest> message.  
  
 You can see the user query in the **Advanced Find** section of the model-driven app and also in the **View** drop-down list for an entity.  You can export the value of the `UserQuery.FetchXml` attribute by using the **Download Fetch XML** button in the **Advanced Find** dialog box.  
  
## Use Web API to execute saved queries

To know about executing user query and saved query using Web API, see [Retrieve and execute predefined queries](webapi/retrieve-and-execute-predefined-queries.md)

## Use Organization service to execute saved queries

You can use the <xref:Microsoft.Crm.Sdk.Messages.ExecuteByIdUserQueryRequest> and <xref:Microsoft.Crm.Sdk.Messages.ExecuteByIdSavedQueryRequest> messages to execute user query and saved query respectively.
