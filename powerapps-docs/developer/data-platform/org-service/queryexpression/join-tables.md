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

> [!NOTE]
> This property is read-only. You can set `LinkEntity` instances to this collection using object initialization or using the [QueryExpression.AddLink method](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.addlink).
>
> You can also use [System.Collections.ObjectModel.Collection&lt;T&gt; methods](/dotnet/api/system.collections.objectmodel.collection-1?view=net-8.0) the `LinkEntities` property inherits.


|Property|Description|
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkFromEntityName>|The logical name of the entity that you are linking from.<br /> For a `LinkEntity` that isn't nested, this is the same value as the [QueryExpression.EntityName property](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.entityname).<br /> For a `LinkEntity` that is included in a [LinkEntity.LinkEntities collection](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkEntities), this is the value of the [LinkEntity.LinkToEntityName](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkToEntityName). |
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkToEntityName>|The logical name of the entity that you are linking to.|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkFromAttributeName>|The logical name of the attribute of the entity that you are linking from. This is the name of the lookup column for the relationship.|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkToAttributeName>|The logical name of the attribute of the entity that you are linking to. This is the name of the primary key column for the table named in the <xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkToEntityName> property |
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.JoinOperator>|The join operator. The default is `Inner`, which restricts results to rows with matching values in both tables.<br />Other valid values are:<br />- `All`<br />- `Any`<br />- `Exists`<br />- `In`<br />- `LeftOuter`<br />- `MatchFirstRowUsingCrossApply`<br />- `Natural`<br />- `NotAll`<br />- `NotAny`|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.EntityAlias>|The alias for the table.|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.Columns>|The columns to include for the table. Add these to the joined table using a <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> as described in [Select columns using QueryExpression](select-columns.md)|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkCriteria>|The complex condition and logical filter expressions that filter the results of the query. [Learn how to filter rows using QueryExpression](filter-rows.md)|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkEntities>|The collection of links between entities that can included nested links. |

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

The results look like this:

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

## AddLink methods

You can compose the entire query in the object initialization as shown, but we recommend using the [QueryExpression.AddLink](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.addlink) and [LinkEntity.AddLink](/dotnet/api/microsoft.xrm.sdk.query.linkentity.addlink) methods. These methods return a reference to the link created so that you can easily access and modify the query within the collection. For example, if you compose the query this way using the [QueryExpression.AddLink method](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.addlink):

```csharp
var query = new QueryExpression("account")
{
      TopCount = 5,
      ColumnSet = new ColumnSet("name"),
};

// Link to primary contact
LinkEntity linkedPrimaryContact = query.AddLink(
      linkToEntityName: "contact",
      linkFromAttributeName: "primarycontactid",
      linkToAttributeName: "contactid",
      joinOperator: JoinOperator.Inner);

linkedPrimaryContact.EntityAlias = "contact";
linkedPrimaryContact.Columns = new ColumnSet("fullname");
```

You can then use then extend the query using the [LinkEntity.AddLink method](/dotnet/api/microsoft.xrm.sdk.query.linkentity.addlink) to include information about the owning user for the contact linked via the `linkedPrimaryContact` `LinkEntity` instance:

```csharp
// Link to contact owning user
LinkEntity linkedContactOwner = linkedPrimaryContact.AddLink(
      linkToEntityName: "systemuser",
      linkFromAttributeName: "owninguser",
      linkToAttributeName: "systemuserid",
      joinOperator: JoinOperator.Inner);

linkedContactOwner.EntityAlias = "owner";
linkedContactOwner.Columns = new ColumnSet("fullname");
```

## Limitations

You can add up to 15 [LinkEntity](xref:Microsoft.Xrm.Sdk.Query.LinkEntity) instances to a query. Each `LinkEntity` adds a JOIN to the query and increases the time to execute the query. This limit is to protect performance. If you add more than 15 `LinkEntity` to the [QueryExpression.LinkEntities](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.LinkEntities) you will get this runtime error:

> Code: `0x8004430D`  
> Number: `-2147204339`  
> Message: `Number of link entities in query exceeded maximum limit.`

## Many-to-one relationships

The previous example is a many-to-one relationship where many account records can refer to a one contact record. This information is defined in the [Account account_primary_contact many-to-one relationship](../../reference/entities/account.md#BKMK_account_primary_contact), which has the following values:


|Property|Value|Comment|
|---------|---------|---------|
|`SchemaName`|`account_primary_contact`|Unique Name of the relationship. |
|`ReferencedEntity`|`contact`|The referenced table. The *one* in many-to-one. `linkToEntityName` in the previous example.|
|`ReferencedAttribute`|`contactid`|The primary key of the referenced table. `linkToAttributeName` in the previous example.|
|`ReferencingEntity`|`account`|The table with a lookup column referencing the other table. The *many* in many-to-one. `LinkFromEntityName` in the previous example.|
|`ReferencingAttribute`|`primarycontactid`|The name of the lookup column. `linkFromAttributeName` in the previous example.|
|`RelationshipType`|`OneToManyRelationship`|A one-to-many relationship when viewed from the *referenced* (one) table.<br />A many-to-one relationship when viewed from the *referencing* (many) table|

### Retrieve relationship information

You can also use other tools and APIs to look up relationship data for the appropriate `linkToEntityName`, `linkToAttributeName`, `LinkFromEntityName` and `linkFromAttributeName` values to use. For more information see:

- [Browse table definitions in your environment](../browse-your-metadata.md)
- [Query schema definitions](../query-schema-definitions.md)


## One-to-many relationships

Many-to-one and one-to-many relationships are like looking at two sides of a coin. The relationship exists between the tables, so the way you use it depends on which table is the base table for your query.

> [!NOTE]
> If your base table contains the lookup column, it is a many-to-one relationship. Otherwise, it is a one-to-many relationship.

You can retrieve the same data as the previous example from the `contact` table using the same relationship, except from the side of the `contact` table. Use the data from the same [Contact account_primary_contact one-to-many relationship](../../reference/entities/contact.md#BKMK_account_primary_contact), but adjust the values for the different view of the relationship.

```csharp
var query = new QueryExpression("contact")
{
      TopCount = 5,
      ColumnSet = new ColumnSet("fullname"),
};

// Link to related account
var linkedPrimaryContact = query.AddLink(
      linkToEntityName: "account",
      linkFromAttributeName: "contactid",
      linkToAttributeName: "primarycontactid",
      joinOperator: JoinOperator.Inner);

linkedPrimaryContact.EntityAlias = "account";
linkedPrimaryContact.Columns = new ColumnSet("name");
```

For a one-to-many relationship, use these relationship values:

|Property|Relationship Value|Comment|
|---------|---------|---------|
|`LinkFromEntityName`|`ReferencedEntity`|The referenced table. The *one* in many-to-one. `contact` in the one-to-many example.|
|`linkToEntityName`|`ReferencingEntity`|The table with a lookup column referencing the other table. The *many* in many-to-one. `account` in the one-to-many example.|
|`linkFromAttributeName`|`ReferencedAttribute`|The primary key of the referenced table. `contactid` in the one-to-many example.|
|`linkToAttributeName`|`ReferencingAttribute`|The name of the lookup column. `primarycontactid` in the one-to-many example.|

The results include the same records and data as the previous query using the many-to-one relationship, except the *'parent entity'* is now `contact` instead of `account`.

```text
 -----------------------------------------------------------------
 | fullname                   | account.name                     |
 -----------------------------------------------------------------
 | Susanna Stubberod (sample) | Litware, Inc. (sample)           |
 -----------------------------------------------------------------
 | Nancy Anderson (sample)    | Adventure Works (sample)         |
 -----------------------------------------------------------------
 | Maria Campbell (sample)    | Fabrikam, Inc. (sample)          |
 -----------------------------------------------------------------
 | Sidney Higa (sample)       | Blue Yonder Airlines (sample)    |
 -----------------------------------------------------------------
 | Scott Konersmann (sample)  | City Power & Light (sample)      |
 -----------------------------------------------------------------
```

## Many-to-many relationships

Many-to-many relationships depend on an *intersect table*.  An intersect table typically has just four columns, but only two of them are important. The two important columns match the primary key columns of the participating tables.

For example, the `TeamMembership` intersect table supports the [teammembership_association many-to-many relationship](../../reference/entities/team.md#BKMK_teammembership_association) between [SystemUser](../../reference/entities/systemuser.md) and [Team](../../reference/entities/team.md) tables. It allows users to join multiple teams, and teams to have multiple users. `TeamMembership` has these columns: `systemuserid`, `teamid`.

If you want to retrieve information about users and the teams they belong to using the `teammembership_association` many-to-many relationship, you can use this [QueryExpression](/dotnet/api/microsoft.xrm.sdk.query.queryexpression) query:

```csharp
var query = new QueryExpression("systemuser")
{
      TopCount = 2,
      ColumnSet = new ColumnSet("fullname"),
};

LinkEntity linkedTeamMemberShip = query.AddLink(
      linkToEntityName: "teammembership",
      linkFromAttributeName: "systemuserid",
      linkToAttributeName: "systemuserid");

LinkEntity linkedTeam = linkedTeamMemberShip.AddLink(
      linkToEntityName: "team",
      linkFromAttributeName: "teamid",
      linkToAttributeName: "teamid");

linkedTeam.EntityAlias = "team";
linkedTeam.Columns = new ColumnSet("name");
```

There are two [LinkEntity](xref:Microsoft.Xrm.Sdk.Query.LinkEntity) instances.

- The first one connects `systemuser` to the `teammembership` intersect table where `systemuserid` = `systemuserid`.
- The second one connects `teammembership` intersect table to team where `teamid` = `teamid`.

The results should look something like:

```text
 --------------------------------------
 | fullname             | team.name   |
 --------------------------------------
 | FirstName LastName   | org26ed931d |
 --------------------------------------
 | # PpdfCDSClient      | org26ed931d |
 --------------------------------------
```

## No relationship

## Find records not in a set

## Use advanced link types?

## Next steps