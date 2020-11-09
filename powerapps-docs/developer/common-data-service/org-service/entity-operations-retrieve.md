---
title: "Retrieve an table using the Organization Service (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes options available when retrieving a row programmatically" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 11/09/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Retrieve an table using the Organization Service

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

You will typically retrieve a row based on the results of a query and the query results should include a unique identifier for the table row.

> [!NOTE]
> In the following examples the `accountid` variable represents the <xref:System.Guid> identifier for an account table row.

You have some options to define the data returned when you retrieve an table row. You will use the <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class to define which column values you require.


> [!IMPORTANT]
> When retrieving table rows you should only request the columns values you need by setting the specific columns using the <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class constructor. Although <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> class constructor provides an overload that accepts a boolean `allColumns` parameter, you should not use this in production code. More information: [Do not retrieve Entity all columns via query APIs](/dynamics365/customer-engagement/guidance/data/retrieve-specific-columns-entity-via-query-apis)

If you need to return related table rows you can include a query with your retrieve request to define which related rows to return.


## Basic Retrieve

You can retrieve individual rows using either the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*> method or by setting the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest.Target> property of the  <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> class to a reference row and use the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method.

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
> - [Retrieve with related rows](#retrieve-with-related-rows)
> - [Retrieve with an alternate key](#retrieve-with-an-alternate-key)


## Retrieve with related rows

When you retrieve an individual row you can also include a query to include related rows by setting the  <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest.RelatedEntitiesQuery> property of the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest>.

You can define a query using any of the classes derived from <xref:Microsoft.Xrm.Sdk.Query.QueryBase> and associate it with a specific table relationship. Add a collection of pairs of queries and relationships to the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest.RelatedEntitiesQuery> property using a <xref:Microsoft.Xrm.Sdk.RelationshipQueryCollection>.

The following example includes  `task` and `contact` rows related to the `account` table row that is being retrieved.

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

If you have configured an table to use an alternate key, you can use this alternate key to define an <xref:Microsoft.Xrm.Sdk.EntityReference> and pass this value as the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest>.<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest.Target> property.

For example, if you define the `account` `accountnumber` column to be an alternate key, you can retrieve an account using the value of that column.


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

If your alternate key is a composite of several columns, you would define a <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection>. The following example is for an account table that has an alternate key that includes both the `accountnumber` and `sic` columns.

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

[Create tables using the Organization Service](entity-operations-create.md)<br />
[Update and Delete tables using the Organization Service](entity-operations-update-delete.md)<br />
[Associate and disassociate tablea using the Organization Service](entity-operations-associate-disassociate.md)<br />
