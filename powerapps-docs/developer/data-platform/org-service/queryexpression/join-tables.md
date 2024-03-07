---
title: Join tables using QueryExpression
description: Learn how to use QueryExpression to join tables when you retrieve data from Microsoft Dataverse.
ms.date: 02/29/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Join tables using QueryExpression

Use the [QueryExpression.LinkEntities](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.LinkEntities) property to describe the data from related tables to return with your query. This property contains a collection of [LinkEntity](xref:Microsoft.Xrm.Sdk.Query.LinkEntity) instances that describe:

- Which related table rows to return
- Which columns of those records to return
- Any filters to apply with the join


|Property|Description|
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkFromEntityName>|The logical name of the entity that you are linking from.|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkToEntityName>|The logical name of the entity that you are linking to.|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkFromAttributeName>|The logical name of the attribute of the entity that you are linking from.|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkToAttributeName>|The logical name of the attribute of the entity that you are linking to.|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.JoinOperator>|The join operator. The default is `Inner`, which restricts results to rows with matching values in both tables.<br />Other valid values are:<br />- All<br />- Any<br />- Exists<br />- In<br />- LeftOuter<br />- MatchFirstRowUsingCrossApply<br />- Natural<br />- NotAll<br />- NotAny|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.EntityAlias>|The alias for the table.|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.Columns>|The columns to include for the table. Add these to the joined table using a <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> as described in [Select columns using QueryExpression](select-columns.md)|

<!-- 
TODO: Add detailed remarks in the [JoinOperator Enum](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.JoinOperator) article to explain each of the types like is done for FetchXML at https://learn.microsoft.com/en-us/power-apps/developer/data-platform/fetchxml/reference/link-entity#link-type-options 
-->


For example, the following query returns up to 5 records from the [account](../../reference/entities/account.md) and [contact](../../reference/entities/contact.md) tables based on the [PrimaryContactId lookup column](../../reference/entities/account.md#BKMK_PrimaryContactId) in the account record:

```csharp
QueryExpression query = new("account")
{
      TopCount = 5,
      ColumnSet = new ColumnSet("name"),
      LinkEntities = {
            new LinkEntity()
            {
                  LinkFromEntityName = "account",
                  LinkToEntityName = "contact",
                  LinkFromAttributeName = "primarycontactid",
                  LinkToAttributeName = "contactid",
                  JoinOperator = JoinOperator.Inner,
                  EntityAlias = "contact",
                  Columns = new ColumnSet("fullname")
            }
      }
};
```

Or you may prefer to compose the query this way using the [LinkEntity(String, String, String, String, JoinOperator) constructor](/dotnet/api/microsoft.xrm.sdk.query.linkentity.-ctor#microsoft-xrm-sdk-query-linkentity-ctor(system-string-system-string-system-string-system-string-microsoft-xrm-sdk-query-joinoperator)) with the  [LinkEntities.Add method](xref:System.Collections.ObjectModel.Collection%601.Add%2A) inherited from <xref:System.Collections.ObjectModel.Collection%601?displayProperty=fullName>:

```csharp
QueryExpression query = new();
query.EntityName = "account";
query.TopCount = 5;
query.ColumnSet = new ColumnSet("name");

LinkEntity primaryContact = new("account", "contact", "primarycontactid", "contactid", JoinOperator.Inner)
{
      EntityAlias = "contact",
      Columns = new ColumnSet("fullname")
};

query.LinkEntities.Add(primaryContact);
```

Either way the results are the same and might look like this:

```text
-----------------------------------------------------------------
 | name                             | contact.fullname           |
 -----------------------------------------------------------------
 | Litware, Inc. (sample)           | Susanna Stubberod (sample) |
 -----------------------------------------------------------------
 | Adventure Works (sample)         | Nancy Anderson (sample)    |
 -----------------------------------------------------------------
 | Fabrikam, Inc. (sample)          | Maria Campbell (sample)    |
 -----------------------------------------------------------------
 | Blue Yonder Airlines (sample)    | Sidney Higa (sample)       |
 -----------------------------------------------------------------
 | City Power & Light (sample)      | Scott Konersmann (sample)  |
 -----------------------------------------------------------------
```



## Limitations

You can add up to 15 [LinkEntity](xref:Microsoft.Xrm.Sdk.Query.LinkEntity) instances to a query. Each `LinkEntity` adds a JOIN to the query and increases the time to execute the query. This limit is to protect performance. If you add more than 15 `LinkEntity` to the [QueryExpression.LinkEntities](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.LinkEntities) you will get this runtime error:

> Code: `0x8004430D`  
> Number: `-2147204339`  
> Message: `Number of link entities in query exceeded maximum limit.`  

## Child elements

## Many-to-one relationships

## One-to-many relationships

## Many-to-many relationships

## No relationship

## Find records not in a set

## Use advanced link types?

## Next steps