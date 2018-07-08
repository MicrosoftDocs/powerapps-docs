---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Retrieve an entity

## Retrieve with related records

```csharp
Guid accountToRetrieveId = new Guid("a976763a-ba1c-e811-a954-000d3af451d6");

var relationshipQueryCollection = new RelationshipQueryCollection();

var relatedTasks = new QueryExpression("task");
relatedTasks.ColumnSet = new ColumnSet("subject", "description");
var taskRelationship = new Relationship("Account_Tasks");
relationshipQueryCollection.Add(taskRelationship, relatedTasks);


var relatedContacts = new QueryExpression("contact");
relatedContacts.ColumnSet = new ColumnSet("fullname", "emailaddress1");
var contactRelationship = new Relationship("account_primary_contact");
relationshipQueryCollection.Add(contactRelationship, relatedContacts);

var request = new RetrieveRequest()
{
    ColumnSet = new ColumnSet(true),
    RelatedEntitiesQuery = relationshipQueryCollection,
    Target = new EntityReference("account", accountToRetrieveId)
};

RetrieveResponse response = (RetrieveResponse)svc.Execute(request);

Account retrievedEntity = (Account)response.Entity;
```