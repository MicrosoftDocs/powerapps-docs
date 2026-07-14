---
title: Join Tables Using FetchXml Queries
description: Learn how to use FetchXml to join tables when you retrieve data from Microsoft Dataverse. Explore relationship types, link-entity options, and advanced join techniques.
ms.date: 03/13/2026
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
---
# Join tables using FetchXML

As described in [Query data using FetchXml](overview.md), start your query by selecting a table using the [entity element](reference/entity.md).

Use the [link-entity element](reference/link-entity.md) to describe the data from related tables that you want to return with your query. Use the following attributes:


| Attribute | Short description *[Find more details in the link-entity element reference](reference/link-entity.md)* |
|---------|---------|
| `name` | [!INCLUDE [link-entity-name-description](reference/includes/link-entity-name-description.md)] |
| `from` | [!INCLUDE [link-entity-from-description](reference/includes/link-entity-from-description.md)] |
| `to` | [!INCLUDE [link-entity-to-description](reference/includes/link-entity-to-description.md)] |
| `link-type` | The type of link to use. The default value is `inner`, which restricts results to rows with matching values in both tables.<br />Other valid values are:<br />- `outer`<br />- `any`<br />- `not any`<br />- `all`<br />- `not all`<br />- `exists`<br />- `in`<br />- `matchfirstrowusingcrossapply`<br />[Learn about link-type options](reference/link-entity.md#link-type-options).|
| `alias` | Represents the name of the related table in the results. |
| `intersect` | Indicates that the `link-entity` is used to join tables and doesn't return any columns.|

## Basic example

The following query returns up to five records from the [account](../reference/entities/account.md) and [contact](../reference/entities/contact.md) tables based on the [PrimaryContactId lookup column](../reference/entities/account.md#BKMK_PrimaryContactId) in the account record:

```xml
<fetch top='5'>
   <entity name='account'>
      <attribute name='name' />
      <link-entity name='contact'
         from='contactid'
         to='primarycontactid'
         link-type='inner'
         alias='contact'>
         <attribute name='fullname' />
      </link-entity>
   </entity>
</fetch>
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

## Limitations

You can add up to 15 `link-entity` elements to a query. Each `link-entity` adds a JOIN to the query and increases the time it takes to execute the query. This limit protects performance. If you add more than 15 `link-entity` elements to a query, you get this error message:

> Code: `0x8004430D`  
> Number: `-2147204339`  
> Message: `Number of link entities in query exceeded maximum limit.`  

## Child elements

Within the `link-entity` element, you can add child elements just like on the parent element to:

- [Select columns](select-columns.md) from the related table.
- [Filter rows](filter-rows.md) from the related table.
- Join another related table.

## Many-to-one relationships

The [basic example](#basic-example) shows a many-to-one relationship where many account records can refer to one contact record. You define this information in the [Account account_primary_contact many-to-one relationship](../reference/entities/account.md#BKMK_account_primary_contact), which has the following values:


|Property|Value|Comment|
|---------|---------|---------|
|`SchemaName`|`account_primary_contact`|Unique name of the relationship. |
|`ReferencedEntity`|`contact`|The referenced table. The *one* in many-to-one.|
|`ReferencedAttribute`|`contactid`|The primary key of the referenced table.|
|`ReferencingEntity`|`account`|The table with a lookup column referencing the other table. The *many* in many-to-one.|
|`ReferencingAttribute`|`primarycontactid`|The name of the lookup column.|
|`RelationshipType`|`OneToManyRelationship`|A one-to-many relationship when viewed from the *referenced* (one) table.<br />A many-to-one relationship when viewed from the *referencing* (many) table.|

### Retrieve relationship information

If you use tools like [XrmToolBox](../community-tools.md#xrmtoolbox) [FetchXML Builder](https://fetchxmlbuilder.com/) or [Power Platform ToolBox](https://www.powerplatformtoolbox.com/) [FetchXML Studio](https://www.powerplatformtoolbox.com/tools/e64db554-5dc9-4cc5-a712-832307d00777), you can see how these tools allow you to select the relationship to set the appropriate `name`, `from`, and `to` attribute values.

You can also use other tools and APIs to look up relationship data for the appropriate `name`, `from`, and `to` attribute values. To learn how to retrieve this data, see:

- [Browse table definitions in your environment](../browse-your-metadata.md)
- [Query schema definitions](../query-schema-definitions.md)

## One-to-many relationships

Many-to-one and one-to-many relationships are like two sides of the same coin. The relationship exists between the tables, so the way you use it depends on which table is the base table for your query.

You can retrieve the same data as the previous example from the contact table using the same relationship, but from the side of the contact table. Use the data from the same [Contact account_primary_contact one-to-many relationship](../reference/entities/contact.md#BKMK_account_primary_contact), but adjust the values for the different view of the relationship.

```xml
<fetch top='5'>
   <entity name='contact'>
      <attribute name='fullname' />
      <link-entity name='account'
         from='primarycontactid'
         to='contactid'
         alias='account'>
         <attribute name='name' />
      </link-entity>
   </entity>
</fetch>
```

The following table shows the [link-entity](reference/link-entity.md) attribute values in this example:


|Attribute|Value|Description|
|---------|---------|---------|
|`name`|`account`|The logical name of the *referencing* table|
|`from`|`primarycontactid`|The name of the lookup column in the *referencing* account table|
|`to`|`contactid`|The primary key of the *referenced* contact table|
|`alias`|`account`|A value is recommended for the `link-entity` with a one-to-many relationship. If you don't provide an alias, the system generates a default alias. In this example, if you don't provide an alias, the data is returned with a column named `account1.name`.|
|`link-type`|Not set|When you don't set a value, it defaults to `inner`|

The results include the same records and data as the previous query that uses the many-to-one relationship. The difference is that the *parent entity* is now `contact` instead of `account`.

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

Many-to-many relationships rely on an *intersect table*. An intersect table typically has just four columns, but only two of them are important. The two important columns correspond to the primary key columns of the participating tables.

For example, the `TeamMembership` intersect table supports the [teammembership_association many-to-many relationship](../reference/entities/team.md#BKMK_teammembership_association) between [SystemUser](../reference/entities/systemuser.md) and [Team](../reference/entities/team.md) tables. By using this relationship, users can join multiple teams, and teams can have multiple users. `TeamMembership` has these columns: `systemuserid` and `teamid`.

To retrieve information about users and the teams they belong to by using the `teammembership_association` many-to-many relationship, use this fetchXML query:

```xml
<fetch top='2'>
   <entity name='systemuser'>
      <attribute name='fullname' />
      <link-entity name='teammembership'
         from='systemuserid'
         to='systemuserid'
         intersect='true' >
         <link-entity name='team'
            from='teamid'
            to='teamid'
            link-type='inner'
            alias='team'>
            <attribute name='name' />
         </link-entity>
      </link-entity>
   </entity>
</fetch>
```

There are two nested link-entities.

- The first one connects `systemuser` to the `teammembership` intersect table where `systemuserid` = `systemuserid`.
- The second one connects `teammembership` intersect table to `team` where `teamid` = `teamid`.

The results look like:

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

You can specify `from` and `to` attributes by using columns that aren't part of a defined relationship.

For example, this query finds pairs of records where the [Name column](../reference/entities/account.md#BKMK_Name) of an [account](../reference/entities/account.md) record matches the [FullName column](../reference/entities/contact.md#BKMK_FullName) of a [contact](../reference/entities/contact.md) record regardless of whether they reference each other in any of the lookup columns.

``` xml
<fetch>
   <entity name='account'>
     <attribute name='name' />
     <link-entity name='contact'
       from='fullname'
       to='name'
       link-type='inner'
       alias='contact'>
       <attribute name='fullname' />
     </link-entity>
   </entity>
 </fetch>
```

> [!NOTE]
> Make sure the columns you specify in the `from` and `to` attributes are the same type, even if they're not involved in a relationship. If you use columns of different types, the query needs a type conversion, which can affect performance and might fail for some column values.

You can't use the following [column types](../../../maker/data-platform/types-of-fields.md) in `from` and `to` attributes:

- **File**
- **Image**
- **MultiSelect Field**
- [**PartyList**](../../../maker/data-platform/types-of-fields.md#different-types-of-lookups)

You can use these column types in `from` and `to` attributes, but they might result in poor performance:

- Columns of the **Multiple Lines of Text** type
- Columns of the **Single Line of Text** type with a maximum length larger than 850
- [**Formula**](../../../maker/data-platform/formula-columns.md) columns
- [**Calculated**](../../../maker/data-platform/define-calculated-fields.md) columns
- [**Logical**](../entity-attribute-metadata.md#logical-columns) columns



## Find records not in a set

You can use FetchXML to create a query that returns records that aren't in a set by using a *left outer join*. A left outer join returns each row that satisfies the join of the first input with the second input. It also returns any rows from the first input that have no matching rows in the second input. The non-matching rows in the second input are returned as null values.

You can perform a left outer join in FetchXML by using the `entityname` attribute in a [condition element](reference/condition.md). The `entityname` attribute is valid in conditions, filters, and nested filters. [Learn more about filters on link-entity](filter-rows.md#filters-on-link-entity).


For example, the following query returns all account records with no contacts.

```xml
<fetch>
   <entity name='account'>
      <attribute name='name' />
      <order attribute='name' />
      <link-entity name='contact'
         from='parentcustomerid'
         to='accountid'
         link-type='outer'
         alias='contact' />
      <filter type='and'>
         <condition entityname='contact'
            attribute='parentcustomerid'
            operator='null' />
      </filter>
   </entity>
</fetch>
```

## Use advanced link types

The following link entity types don't directly correspond to T-SQL [JOIN operator](/sql/relational-databases/performance/joins) types and use [subqueries](/sql/relational-databases/performance/subqueries) instead. These types provide more advanced capabilities you can use to improve query performance and define more complex queries.

|Name|Description|
|---------|---------|
|`exists`|[!INCLUDE [link-type-exists-description](reference/includes/link-type-exists-description.md)]|
|`in`|[!INCLUDE [link-type-in-description](reference/includes/link-type-in-description.md)]|
|`matchfirstrowusingcrossapply`|[!INCLUDE [link-type-matchfirstrowusingcrossapply-description](reference/includes/link-type-matchfirstrowusingcrossapply-description.md)]|

### Use `exists` or `in` link types

The `exists` and `in` link types are variants of the `inner` link type. They use different conditions ([EXISTS](/sql/t-sql/language-elements/exists-transact-sql) and [IN](/sql/t-sql/language-elements/in-transact-sql) respectively) in the `where` clause so that the query doesn't return multiple copies of the parent row. Neither of these link types returns the column values of the link entity rows.

#### `exists`

These FetchXML and SQL examples show the patterns applied with `exists`.

##### [FetchXML](#tab/fetchxml)

``` xml
<fetch>
   <entity name='contact'>
      <attribute name='fullname' />
      <link-entity name='account'
         from='primarycontactid'
         to='contactid'
         link-type='exists'>
         <filter type='and'>
            <condition attribute='statecode'
               operator='eq'
               value='1' />
         </filter>
      </link-entity>
   </entity>
</fetch>
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

#### `in`

These FetchXML and SQL examples show the patterns applied with `in`.

##### [FetchXML](#tab/fetchxml)

``` xml
<fetch>
   <entity name='contact'>
      <attribute name='fullname' />
      <link-entity name='account'
         from='primarycontactid'
         to='contactid'
         link-type='in'>
         <filter type='and'>
            <condition attribute='statecode'
               operator='eq'
               value='1' />
         </filter>
      </link-entity>
   </entity>
</fetch>
```

##### [SQL](#tab/sql)

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

Using `exists` or `in` link types can reduce the size of intermediate or final query results. This reduction is especially helpful when many matching linked rows exist for the same parent rows, or when multiple link entities are used with the same parent. By using `exists` or `in` link types, you can improve the performance of the query compared to the `inner` link type because the query doesn't need to return a Cartesian product containing all possible permutations of rows from different linked entities for each parent row.

By using these link types, Dataverse might only need to find the first matching linked entity row for each parent row. This approach is more efficient than finding all matching rows in the linked entity in an `inner` join.

### Use `matchfirstrowusingcrossapply` link type

This link type produces a [CROSS APPLY](/sql/t-sql/queries/from-transact-sql#using-apply) operator with a subquery using `top 1` following this pattern:

#### [FetchXml](#tab/fetchxml)

``` xml
<fetch>
   <entity name='contact'>
      <attribute name='fullname' />
      <link-entity name='account'
         from='primarycontactid'
         to='contactid'
         link-type='matchfirstrowusingcrossapply'>
         <attribute name='accountid' />
         <attribute name='name' />
      </link-entity>
   </entity>
</fetch>
```

##### [SQL](#tab/sql)

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

The `matchfirstrowusingcrossapply` link type is equivalent to the `inner` type except it only returns the parent row at most once. The parent row is returned only if there are matching rows in the linked entity but, unlike `in` and `exists` types, it **does** return column values from one of the matching rows in the linked entity. Use this type when only a single example of a matching row from the linked entity is sufficient and results don't need multiple copies of the parent row.

#### Related table property and attribute names are inconsistent

When you use the `matchfirstrowusingcrossapply` link type, the names of the properties returned by using Web API or the SDK [Entity.Attributes collection](/dotnet/api/microsoft.xrm.sdk.entity.attributes) `Keys` values for the related table columns differ from other types of joins. Usually, these names follow the `<tablealias>.<logicalname>` format. However, for the `matchfirstrowusingcrossapply` link type, the [SchemaName](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.schemaname) values are used without the table alias prefix.

By using the previous query example with any other link type, you can expect the properties or keys to have these names:

- `fullname`
- `contactid`
- `account1.accountid`
- `account1.name`

But by using the `matchfirstrowusingcrossapply` link type, the properties or keys have these names:

- `fullname`
- `contactid`
- `AccountId`
- `Name`


## Next steps

Learn how to order rows.

> [!div class="nextstepaction"]
> [Order rows](order-rows.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
