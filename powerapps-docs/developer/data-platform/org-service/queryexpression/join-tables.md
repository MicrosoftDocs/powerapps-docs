---
title: Join tables using QueryExpression
description: Learn how to use QueryExpression to join tables when you retrieve data from Microsoft Dataverse.
ms.date: 05/12/2024
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
- Which column values to base the join on
- Which columns of those records to return
- Any filters to apply with the join

> [!NOTE]
> The `LinkEntities` property is read-only. You can set `LinkEntity` instances to this collection using object initialization or using the [QueryExpression.AddLink method](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.addlink).
>
> You can also use [System.Collections.ObjectModel.Collection&lt;T&gt; methods](/dotnet/api/system.collections.objectmodel.collection-1#methods) the `LinkEntities` property inherits.

## LinkEntity properties

The following table provides details about the [LinkEntity properties](/dotnet/api/microsoft.xrm.sdk.query.linkentity#properties):

|Property|Description|
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkFromEntityName>|The logical name of the entity that you're linking from.<br /> For a `LinkEntity` that isn't nested, use the same value as the [QueryExpression.EntityName property](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.entityname).<br /> For a `LinkEntity` that is nested in a [LinkEntity.LinkEntities collection](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkEntities), use the value of the [LinkEntity.LinkToEntityName](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkToEntityName) from the parent link entity. |
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkToEntityName>|The logical name of the entity that you're linking to.|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkFromAttributeName>|The logical name of the attribute of the entity that you're linking from.|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkToAttributeName>|The logical name of the attribute of the entity that you're linking to. |
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.JoinOperator>|The join operator. Use a value of one of the [JoinOperator enum](xref:Microsoft.Xrm.Sdk.Query.JoinOperator) members. The default value is `Inner`, which restricts results to rows with matching values in both tables.<br />Other valid values are:<br />- `LeftOuter` Includes results from the parent row that don't have a matching value.<br />- `Natural` Only one value of the two joined columns is returned if an equal-join operation is performed and the two values are identical.<br />These members considered [advanced JoinOperators](#use-advanced-joinoperators):<br />- `Exists`<br />- `In`<br />- `MatchFirstRowUsingCrossApply`<br />These members are used to [filter on values in related records](filter-rows.md#filter-on-values-in-related-records):<br />- `All`<br />- `Any`<br />- `NotAll`<br />- `NotAny`|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.EntityAlias>|The alias for the table.|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.Columns>|The columns to include for the table. Add these columns to the joined table using a <xref:Microsoft.Xrm.Sdk.Query.ColumnSet>. [Learn to select columns using QueryExpression](select-columns.md)|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkCriteria>|The complex condition and logical filter expressions that filter the results of the query. [Learn how to filter rows using QueryExpression](filter-rows.md)|
|<xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkEntities>|The collection of links between entities that can include nested links. [Up to 15 total links can be included in a query](#limitations) |

> [!NOTE]
> The meaning of the [LinkEntity.LinkFromAttributeName](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkFromAttributeName) and [LinkEntity.LinkToAttributeName](xref:Microsoft.Xrm.Sdk.Query.LinkEntity.LinkToAttributeName) properties are the opposite of the corresponding `from` and `to` attributes in FetchXml. [Learn more about using `from` and `to` attributes with FetchXml](../../fetchxml/reference/link-entity.md#using-from-and-to-attributes)

### LinkEntity example

The following query returns up to five records from the [account](../../reference/entities/account.md) and [contact](../../reference/entities/contact.md) tables based on the [PrimaryContactId lookup column](../../reference/entities/account.md#BKMK_PrimaryContactId) in the account record. This represents a [many-to-one relationship](#many-to-one-relationships):

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

You can compose the entire query using object initialization as shown, but we recommend using the [QueryExpression.AddLink](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.addlink) and [LinkEntity.AddLink](/dotnet/api/microsoft.xrm.sdk.query.linkentity.addlink) methods. These methods return a reference to the link created so that you can easily access and modify the query within the collection. For example, if you compose the query this way using the [QueryExpression.AddLink method](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.addlink):

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

linkedPrimaryContact.EntityAlias = "primarycontact";
linkedPrimaryContact.Columns = new ColumnSet("fullname");
```

You can extend the query using the [LinkEntity.AddLink method](/dotnet/api/microsoft.xrm.sdk.query.linkentity.addlink) to include information about the owning user for the contact linked via the `linkedPrimaryContact` `LinkEntity` instance:

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

This way you can more easily access the different parts of the query to make adjustments.


## Limitations

You can add up to 15 [LinkEntity](xref:Microsoft.Xrm.Sdk.Query.LinkEntity) instances to a query. Each `LinkEntity` adds a JOIN to the query and increases the time to execute the query. This limit is to protect performance. If you add more than 15 `LinkEntity` instances to the [QueryExpression.LinkEntities](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.LinkEntities), you get this runtime error:

> Name: `TooManyLinkEntitiesInQuery`
> Code: `0x8004430D`  
> Number: `-2147204339`  
> Message: `Number of link entities in query exceeded maximum limit.`

## Many-to-one relationships

The [previous example](#linkentity-example) is a many-to-one relationship where many account records can refer to a one contact record. This information is defined in the [Account account_primary_contact many-to-one relationship](../../reference/entities/account.md#BKMK_account_primary_contact), which has the following values:


|Property|Value|Comment|
|---------|---------|---------|
|`SchemaName`|`account_primary_contact`|Unique Name of the relationship. |
|`ReferencedEntity`|`contact`|The referenced table. The *one* in many-to-one. `LinkToEntityName` in the previous example.|
|`ReferencedAttribute`|`contactid`|The primary key of the referenced table. `LinkToAttributeName` in the previous example.|
|`ReferencingEntity`|`account`|The table with a lookup column referencing the other table. The *many* in many-to-one. `LinkFromEntityName` in the previous example.|
|`ReferencingAttribute`|`primarycontactid`|The name of the lookup column. `LinkFromAttributeName` in the previous example.|
|`RelationshipType`|`OneToManyRelationship`|A one-to-many relationship when viewed from the *referenced* (one) `contact` table.<br />A many-to-one relationship when viewed from the *referencing* (many) `account` table|

### Retrieve relationship information

You can use other tools and APIs to look up relationship data for the appropriate `LinkToEntityName`, `LinkToAttributeName`, `LinkFromEntityName`, and `LinkFromAttributeName` values to use. For more information, see:

- [Browse table definitions in your environment](../../browse-your-metadata.md)
- [Query schema definitions](../../query-schema-definitions.md)

### Many-to-one relationship example

The following table shows the relationship values to use for a many-to-one relationship:

|Property|Relationship Value|Comment|
|---------|---------|---------|
|`LinkFromEntityName`|`ReferencingEntity`|The referenced table. The *many* in many-to-one. `account` in the many-to-one example. There's no parameter for this property in the [AddLink methods](#addlink-methods) because it can be derived from the `QueryExpression.EntityName` or `LinkEntity.LinkToEntityName` properties. |
|`LinkToEntityName`|`ReferencedEntity`|The table with a primary key the other table references. The *one* in many-to-one. `contact` in the many-to-one example.|
|`LinkFromAttributeName`|`ReferencingAttribute`|The name of the lookup column. `primarycontactid` in the many-to-one example.|
|`LinkToAttributeName`|`ReferencedAttribute`| The primary key of the referenced table. `contactid` in the many-to-one example.|


## One-to-many relationships

Many-to-one and one-to-many relationships are like looking at two sides of a coin. The relationship exists between the tables, so the way you use it depends on which table is the base table for your query.

> [!NOTE]
> If your base table contains the lookup column, it is a many-to-one relationship. Otherwise, it is a one-to-many relationship.

You can retrieve the same data as the [previous example](#linkentity-example) from the [contact](../../reference/entities/contact.md) table using the same relationship, except from the side of the `contact` table. Use the data from the same [Contact account_primary_contact one-to-many relationship](../../reference/entities/contact.md#BKMK_account_primary_contact), but adjust the values for the different view of the relationship.

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
|`LinkFromEntityName`|`ReferencedEntity`|The referenced table. The *one* in many-to-one. `contact` in the one-to-many example. There's no parameter for this property in the [AddLink methods](#addlink-methods) because it can be derived from the `QueryExpression.EntityName` or `LinkEntity.LinkToEntityName` properties. |
|`LinkToEntityName`|`ReferencingEntity`|The table with a lookup column referencing the other table. The *many* in many-to-one. `account` in the one-to-many example.|
|`LinkFromAttributeName`|`ReferencedAttribute`|The primary key of the referenced table. `contactid` in the one-to-many example.|
|`LinkToAttributeName`|`ReferencingAttribute`|The name of the lookup column. `primarycontactid` in the one-to-many example.|

The results include the same records and data as the [previous example](#linkentity-example) using the many-to-one relationship, except now the *'parent entity'* is now `contact` instead of `account`.

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

Many-to-many relationships depend on an *intersect table*. An intersect table typically has just four columns, but only two of them are important. The two important columns match the primary key columns of the participating tables.

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

- `linkedTeamMemberShip` connects `systemuser` to the `teammembership` intersect table where `systemuserid` = `systemuserid`.
- `linkedTeam` connects `teammembership` intersect table to team where `teamid` = `teamid`.

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

It's possible to specify `LinkFromAttributeName` and `LinkToAttributeName` properties using columns that aren't part of a defined relationship.

For example, this query finds pairs of records where the [Name column](../../reference/entities/account.md#BKMK_Name) of an [account](../../reference/entities/account.md) record matches the [FullName column](../../reference/entities/contact.md#BKMK_FullName) of a [contact](../../reference/entities/contact.md) record regardless of whether they reference each other in any of the lookup columns.

```csharp
var query = new QueryExpression("account")
{
      ColumnSet = new ColumnSet("name"),
};

LinkEntity linkedContact = query.AddLink(
      linkToEntityName: "contact", 
      linkFromAttributeName: "name", 
      linkToAttributeName: "fullname");
linkedContact.EntityAlias = "contact";
linkedContact.Columns = new ColumnSet("fullname");
```

> [!NOTE]
> It is important that the columns specified in the `LinkFromAttributeName` and `LinkToAttributeName` properties are the same type even if they are not involved in a relationship. Using columns of different types will require a type conversion that might have performance impact and might fail for some column values.

The following [column types](../../../../maker/data-platform/types-of-fields.md) can't be used in `LinkFromAttributeName` and `LinkToAttributeName` properties:

- **File**
- **Image**
- **MultiSelect Field**
- [**PartyList**](../../../../maker/data-platform/types-of-fields.md#different-types-of-lookups)

Some columns can be used in `LinkFromAttributeName` and `LinkToAttributeName` properties but might result in poor performance:

- Columns of the **Multiple Lines of Text** type
- Columns of the **Single Line of Text** type with a maximum length larger than 850
- [**Formula**](../../../../maker/data-platform/formula-columns.md) columns
- [**Calculated**](../../../../maker/data-platform/define-calculated-fields.md) columns
- [**Logical**](../../entity-attribute-metadata.md#logical-columns) columns


## Find records not in a set

You can use [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) to create a query to return records that aren't in a set using a *left outer join*. A left outer join returns each row that satisfies the join of the first input with the second input. It also returns any rows from the first input that had no matching rows in the second input. The nonmatching rows in the second input are returned as null values.

You can perform a left outer join in `QueryExpression` by using the [ConditionExpression.EntityName property](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.entityname). The `EntityName` property is valid in conditions, filters, and nested filters. [Learn more about filters on LinkEntity](filter-rows.md#filters-on-linkentity)


For example, the following query returns all account records with no contacts.

```csharp
var query = new QueryExpression(entityName: "account");
query.ColumnSet.AddColumn("name");
query.AddOrder(
      attributeName: "name", 
      orderType: OrderType.Descending);
query.Criteria.AddCondition(
      entityName: "contact",
      attributeName: "parentcustomerid",
      conditionOperator: ConditionOperator.Null);

LinkEntity linkedContact = query.AddLink(
      linkToEntityName: "contact",
      linkFromAttributeName: "accountid",
      linkToAttributeName: "parentcustomerid",
      joinOperator: JoinOperator.LeftOuter);
linkedContact.EntityAlias = "contact";
linkedContact.Columns.AddColumn("fullname");
```

## Use advanced JoinOperators

The following [JoinOperator members](/dotnet/api/microsoft.xrm.sdk.query.joinoperator) don't directly correspond to T-SQL [JOIN operator](/sql/relational-databases/performance/joins) types and use [subqueries](/sql/relational-databases/performance/subqueries) instead. These types provides more advanced capabilities you can use to improve query performance and define more complex queries.

|Name|Description|
|---------|---------|
|`Exists`|A variant of `Inner` that can provide performance benefits. Uses an [EXISTS](/sql/t-sql/language-elements/exists-transact-sql) condition in the `where` clause. Use `Exists` when multiple copies of the parent row aren't necessary in the results. [Learn more about `Exists` and `In`.](#use-joinoperatorexists-or-joinoperatorin)|
|`In`|A variant of `Inner` that can provide performance benefits. Uses an [IN](/sql/t-sql/language-elements/in-transact-sql) condition in the where clause. Use `In` when multiple copies of the parent row aren't necessary in the results. [Learn more about `Exists` and `In`.](#use-joinoperatorexists-or-joinoperatorin)|
|`MatchFirstRowUsingCrossApply`|A variant of `Inner` that can provide performance benefits. Use this type when only a single example of a matching row from the linked entity is sufficient and multiple copies of the parent row in the results aren't necessary. [Learn more about using `MatchFirstRowUsingCrossApply`](#use-joinoperatormatchfirstrowusingcrossapply)|

### Use `JoinOperator.Exists` or `JoinOperator.In`

`Exists` and `In` are variants of `Inner` that use different conditions ([EXISTS](/sql/t-sql/language-elements/exists-transact-sql) and [IN](/sql/t-sql/language-elements/in-transact-sql) respectively) in the `where` clause so that multiple copies of the parent row aren't returned in the results. Both `Exists` and `In` don't return the column values of the related entity rows.

Using `JoinOperator.Exists` or `JoinOperator.In` can reduce the size of intermediate or final query results, especially when many matching linked rows exist for the same parent rows, or when multiple link entities are used with the same parent. Using `JoinOperator.Exists` or `JoinOperator.In` can improve performance of the query compared to `JoinOperator.Inner` because it doesn't require returning a Cartesian product containing all possible permutations of rows from different linked entities for each parent row.

These `JoinOperator` members might also allow Dataverse to only find the first matching linked entity row for each parent row that is more efficient than finding all matching rows in the linked entity with `JoinOperator.Inner`.

#### `JoinOperator.Exists` example

These [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) and SQL examples show the patterns applied with `JoinOperator.Exists`.

##### [QueryExpression](#tab/qe)

```csharp
QueryExpression query = new("contact");
query.ColumnSet.AddColumn("fullname");

LinkEntity linkedAccount = query.AddLink(
      linkToEntityName: "account",
      linkFromAttributeName: "contactid",
      linkToAttributeName: "primarycontactid",
      joinOperator: JoinOperator.Exists);

linkedAccount.EntityAlias = "account";

linkedAccount.LinkCriteria.AddCondition(
      entityName:"account", 
      attributeName: "statecode", 
      conditionOperator: ConditionOperator.Equal,
      values: 1);
```

##### [SQL](#tab/sql)

``` sql
select 
    "contact0".fullname as "fullname" 
from Contact as "contact0" 
where exists (
    select "account1".primarycontactid
    from Account as "account1"
    where "account1".statecode = 1
        and "contact0".contactid = "account1".primarycontactid)
```

---

#### `JoinOperator.In` example

These [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) and SQL examples show the patterns applied with `JoinOperator.In`.

##### [QueryExpression](#tab/qe)

```csharp
QueryExpression query = new("contact");
query.ColumnSet.AddColumn("fullname");

LinkEntity linkedAccount = query.AddLink(
      linkToEntityName: "account",
      linkFromAttributeName: "contactid",
      linkToAttributeName: "primarycontactid",
      joinOperator: JoinOperator.In);

linkedAccount.EntityAlias = "account";

linkedAccount.LinkCriteria.AddCondition(
      entityName: "account",
      attributeName: "statecode",
      conditionOperator: ConditionOperator.Equal,
      values: 1);
```

#### [SQL](#tab/sql)

``` sql
select 
    "contact0".fullname as "fullname" 
from Contact as "contact0" 
where "contact0".contactid in (
    select "account1".primarycontactid
    from Account as "account1"
    where "account1".statecode = 1)
```

---

### Use `JoinOperator.MatchFirstRowUsingCrossApply`

`JoinOperator.MatchFirstRowUsingCrossApply` produces a [CROSS APPLY](/sql/t-sql/queries/from-transact-sql#using-apply) operator with a subquery using `top 1` following this pattern:

#### [QueryExpression](#tab/qe)

```csharp
QueryExpression query = new("contact");
query.ColumnSet.AddColumn("fullname");

LinkEntity linkedAccount = query.AddLink(
      linkToEntityName: "account",
      linkFromAttributeName: "contactid",
      linkToAttributeName: "primarycontactid",
      joinOperator: JoinOperator.MatchFirstRowUsingCrossApply);

linkedAccount.EntityAlias = "account";
linkedAccount.Columns = new ColumnSet("accountid", "name");
```

#### [SQL](#tab/sql)

``` sql
select 
    "contact0".fullname as "fullname",
    "account1".accountid as "accountid",
    "account1".name as "name" 
from Contact as "contact0"
cross apply (
    select top 1
        "account1".accountid as "accountid",
        "account1".name as "name"
    from Account as "account1"
    where "contact0".contactid = "account1".primarycontactid
  ) "account1"
```

---

This is equivalent to `JoinOperator.LeftOuter` except it only returns the parent row at most once. Unlike `JoinOperator.In` and `JoinOperator.Exists`, it returns column values from one of the matching rows in the related table when matching rows exist, but the parent row is returned even if there are no matching rows in the related table. Use this when only a single example of a matching row from the related table is sufficient and multiple copies of the parent row in the results aren't necessary.

## Next steps

Learn how to order rows.

> [!div class="nextstepaction"]
> [Order rows](order-rows.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]