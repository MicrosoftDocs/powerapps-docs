---
title: "Retrieve an entity using the Organization Service (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes options available when retrieving a record programmatically" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Retrieve an entity using the Organization Service

You will typically retrieve a record based on the results of a query and the query results should include a unique identifier for the entity record.

> [!NOTE]
> In the following examples the `accountid` variable represents the <xref:System.Guid> identifier for an account entity record.

You have some options to define the data returned when you retrieve an entity record. You will use the <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class to define which attribute values you require.


> [!IMPORTANT]
> When retrieving entity records you should only request the attributes values you need by setting the specific attributes using the <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class constructor. Although <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class constructor provides an overload that accepts a boolean `allColumns` parameter, you should not use this in production code. More information: [Do not retrieve Entity all columns via query APIs](/dynamics365/customer-engagement/guidance/data/retrieve-specific-columns-entity-via-query-apis)

If you need to return related entity records you can include a query with your retrieve request to define which related records to return.


## Basic Retrieve

You can retrieve individual records using either the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*> method or by setting the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest.Target> property of the  <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> class to a reference record and use the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method.

This example shows using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*> method.

```csharp
Entity entity = svc.Retrieve("account", accountid, new ColumnSet("name"));
Console.WriteLine("account name: {0}", entity["name"]);
```

This example shows using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> and <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> classes with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method.

```csharp
RetrieveRequest request = new RetrieveRequest()
{
  ColumnSet = new ColumnSet("name"),
  Target = new EntityReference("account", accountid)
};
var response = (RetrieveResponse)svc.Execute(request);
Entity entity = response.Entity;
Console.WriteLine("account name: {0}", entity["name"]);
```

> [!NOTE]
> Most of the time you should use the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*> method.
>
> Use <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method for special circumstances as described below. 
> More information: 
> - [Retrieve with related records](#retrieve-with-related-records)
> - [Retrieve with an alternate key](#retrieve-with-an-alternate-key)


## Retrieve with related records

When you retrieve an individual record you can also include a query to include related records by setting the  <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest.RelatedEntitiesQuery> property of the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest>.

You can define a query using any of the classes derived from <xref:Microsoft.Xrm.Sdk.Query.QueryBase> and associate it with a specific entity relationship. Add a collection of pairs of queries and relationships to the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest.RelatedEntitiesQuery> property using a <xref:Microsoft.Xrm.Sdk.RelationshipQueryCollection>.

The following example includes  `task` and `contact` records related to the `account` entity record that is being retrieved.

```csharp

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
  Target = new EntityReference("account", accountid)
};

RetrieveResponse response = (RetrieveResponse)svc.Execute(request);

Entity retrievedAccount = response.Entity;

Console.WriteLine("Account Name: {0}",retrievedAccount["name"]);

var tasks = retrievedAccount.RelatedEntities[new Relationship("Account_Tasks")];

Console.WriteLine("Tasks:");
tasks.Entities.ToList().ForEach(x => {
  Console.WriteLine(" Task Subject: {0}",x["subject"]);
});

Entity primaryContact = retrievedAccount
  .RelatedEntities[new Relationship("account_primary_contact")]
  .Entities.FirstOrDefault();

Console.WriteLine("Primary Contact Fullname: {0}",primaryContact["fullname"]);
```
The results of the sample could look like the following:

```
Account Name: City Power & Light (sample)
Tasks:
 Task Subject: Task 1
 Task Subject: Task 2
Primary Contact Fullname: Scott Konersmann (sample)
```

More information: [Query data using the Organization service](entity-operations-query-data.md)


## Retrieve with an alternate key

If you have configured an entity to use an alternate key, you can use this alternate key to define an <xref:Microsoft.Xrm.Sdk.EntityReference> and pass this value as the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest>.<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest.Target> property.

For example, if you define the `account` `accountnumber` attribute to be an alternate key, you can retrieve an account using the value of that attribute.


```csharp
RetrieveRequest request = new RetrieveRequest()
{
ColumnSet = new ColumnSet("name"),
Target = new EntityReference("account", "accountnumber", "0001")
};
var response = (RetrieveResponse)svc.Execute(request);
Entity entity = response.Entity;

Console.WriteLine(entity["name"]);
```

If your alternate key is a composite of several attributes, you would define a <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection>. The following example is for an account entity that has an alternate key that includes both the `accountnumber` and `sic` attributes.

```csharp
var keyCollection = new KeyAttributeCollection();
keyCollection.Add("accountnumber", "0001");
keyCollection.Add("sic", "7372");

RetrieveRequest request = new RetrieveRequest()
{
ColumnSet = new ColumnSet("name"),
Target = new EntityReference("account", keyCollection)
};
var response = (RetrieveResponse)svc.Execute(request);
Entity entity = response.Entity;

Console.WriteLine(entity["name"]);
```
> [!NOTE]
> Alternate keys are usually used only for data integration scenarios


## Access Formatted values

The method to access formatted values on a retrieve operation is the same you will use when accessing them in the results of a query. More information: [Access formatted values](entity-operations-query-data.md#access-formatted-values)

<!-- TODO Move the information about accessing formatted values here, where the topic is shorter rather than the query topic which is longer -->

### See also

[Create entities using the Organization Service](entity-operations-create.md)<br />
[Update and Delete entities using the Organization Service](entity-operations-update-delete.md)<br />
[Associate and disassociate entities using the Organization Service](entity-operations-associate-disassociate.md)<br />
