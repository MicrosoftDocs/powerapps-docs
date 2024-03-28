---
title: Join tables using FetchXml
description: Learn how to use FetchXml to join tables when you retrieve data from Microsoft Dataverse.
ms.date: 03/22/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - dmitmikh
 - dasussMS
 - apahwa-lab
 - DonaldlaGithub
---
# Join tables using FetchXml

As described in [Query data using FetchXml](overview.md), start your query by selecting a table using the [entity element](reference/entity.md).

Use the [link-entity element](reference/link-entity.md) to describe the data from related tables to return with your query with the following attributes:


|Attribute|Short Description *[Find more details in the link-entity element reference](reference/link-entity.md)*|
|---------|---------|
|`name`|[!INCLUDE [link-entity-name-description](reference/includes/link-entity-name-description.md)]|
|`from`|[!INCLUDE [link-entity-from-description](reference/includes/link-entity-from-description.md)]|
|`to`|[!INCLUDE [link-entity-to-description](reference/includes/link-entity-to-description.md)]|
|`link-type`|The type of link use. Default behavior is `inner`, which restricts results to rows with matching values in both tables.<br />Other valid values are:<br />- `outer`<br />- `any`<br />- `not any`<br />- `all`<br />- `not all`<br />- `exists`<br />- `in`<br />- `matchfirstrowusingcrossapply`<br />[Learn about link-type options](reference/link-entity.md#link-type-options)|
|`alias`|Represents the name of the related table in the results. |
|`intersect`|Indicates that the `link-entity` is used to join tables and not return any columns|

For example, the following query returns up to 5 records from the [account](../reference/entities/account.md) and [contact](../reference/entities/contact.md) tables based on the [PrimaryContactId lookup column](../reference/entities/account.md#BKMK_PrimaryContactId) in the account record:

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

You can add up to 15 `link-entity` elements to a query. Each link-entity adds a JOIN to the query and increases the time to execute the query. This limit is to protect performance. If you add more than 15 link-entity elements to a query, you get this error:

> Code: `0x8004430D`  
> Number: `-2147204339`  
> Message: `Number of link entities in query exceeded maximum limit.`  

## Child elements

Within the `link-entity` element you can add child elements just like on the parent element to:

- [Select columns](select-columns.md) from the related table
- [Filter rows](filter-rows.md) from the related table
- Join another related table

## Many-to-one relationships

The previous example is a many-to-one relationship where many account records can refer to a one contact record. This information is defined in the [Account account_primary_contact many-to-one relationship](../reference/entities/account.md#BKMK_account_primary_contact), which has the following values:


|Property|Value|Comment|
|---------|---------|---------|
|`SchemaName`|`account_primary_contact`|Unique Name of the relationship. |
|`ReferencedEntity`|`contact`|The referenced table. The *one* in many-to-one.|
|`ReferencedAttribute`|`contactid`|The primary key of the referenced table.|
|`ReferencingEntity`|`account`|The table with a lookup column referencing the other table. The *many* in many-to-one.|
|`ReferencingAttribute`|`primarycontactid`|The name of the lookup column.|
|`RelationshipType`|`OneToManyRelationship`|A one-to-many relationship when viewed from the *referenced* (one) table.<br />A many-to-one relationship when viewed from the *referencing* (many) table|

### Retrieve relationship information

If you use the [XrmToolBox](../community-tools.md#xrmtoolbox) [FetchXML Builder](https://fetchxmlbuilder.com/), you can see how this tool allows you to select the relationship to set the appropriate `name`, `from`, and `to` attribute values.

You can also use other tools and APIs to look up relationship data for the appropriate `name`, `from`, and `to` attribute values to use. Learn how to retrieve this data:

- [Browse table definitions in your environment](../browse-your-metadata.md)
- [Query schema definitions](../query-schema-definitions.md)

## One-to-many relationships

Many-to-one and one-to-many relationships are like looking at two sides of a coin. The relationship exists between the tables, so the way you use it depends on which table is the base table for your query.

You can retrieve the same data as the previous example from the contact table using the same relationship, except from the side of the contact table. Use the data from the same [Contact account_primary_contact one-to-many relationship](../reference/entities/contact.md#BKMK_account_primary_contact), but adjust the values for the different view of the relationship.

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
|`alias`|`account`|A value is recommended for the `link-entity` with a one-to-many relationship. If an alias isn't provided, a default alias is generated. In this example, if no alias is provided, the data is returned with a column named `account1.name`.|
|`link-type`|Not set|When no value is set, it defaults to `inner`|

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

Many-to-many relationships depend on an *intersect table*. An intersect table typically has just four columns, but only two of them are important. The two important columns match the primary key columns of the participating tables.

For example, the `TeamMembership` intersect table supports the [teammembership_association many-to-many relationship](../reference/entities/team.md#BKMK_teammembership_association) between [SystemUser](../reference/entities/systemuser.md) and [Team](../reference/entities/team.md) tables. It allows users to join multiple teams, and teams to have multiple users. `TeamMembership` has these columns: `systemuserid`, `teamid`.

If you want to retrieve information about users and the teams they belong to using the `teammembership_association` many-to-many relationship, you can use this fetchXML query:

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

It's possible to specify `from` and `to` attributes using columns that aren't part of a defined relationship.

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
> It is important that the columns specified in the `from` and `to` attributes are the same type even if they are not involved in a relationship. Using columns of different types will require a type conversion that may have performance impact and may fail for some column values.

The following [column types](../../../maker/data-platform/types-of-fields.md) can't be used in `from` and `to` attributes:

- **File**
- **Image**
- **MultiSelect Field**
- [**PartyList**](../../../maker/data-platform/types-of-fields.md#different-types-of-lookups)

Some columns can be used in `from` and `to` attributes but might result in poor performance:

- Columns of the **Multiple Lines of Text** type
- Columns of the **Single Line of Text** type with a maximum length larger than 850
- [**Formula**](../../../maker/data-platform/formula-columns.md) columns
- [**Calculated**](../../../maker/data-platform/define-calculated-fields.md) columns
- [**Logical**](../entity-attribute-metadata.md#logical-columns) columns



## Find records not in a set

You can use FetchXml to create a query to return records that aren't in a set using a *left outer join*. A left outer join returns each row that satisfies the join of the first input with the second input. It also returns any rows from the first input that had no matching rows in the second input. The non-matching rows in the second input are returned as null values.

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

The following link entity types don't directly correspond to T-SQL [JOIN operator](/sql/relational-databases/performance/joins) types and use [subqueries](/sql/relational-databases/performance/subqueries) instead. These types provides more advanced capabilities you can use to improve query performance and define more complex queries.

|Name|Description|
|---------|---------|
|`exists`|[!INCLUDE [link-type-exists-description](reference/includes/link-type-exists-description.md)]|
|`in`|[!INCLUDE [link-type-in-description](reference/includes/link-type-in-description.md)]|
|`matchfirstrowusingcrossapply`|[!INCLUDE [link-type-matchfirstrowusingcrossapply-description](reference/includes/link-type-matchfirstrowusingcrossapply-description.md)]|

### Use `exists` or `in` link types

`exists` and `in` are variants of `inner` that use different conditions ([EXISTS](/sql/t-sql/language-elements/exists-transact-sql) and [IN](/sql/t-sql/language-elements/in-transact-sql) respectively) in the `where` clause so that multiple copies of the parent row aren't returned in the results. Neither of these types return the column values of the link entity rows.

#### `exists`

These FetchXml and SQL examples show the patterns applied with `exists`.

##### [FetchXml](#tab/fetchxml)

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

These FetchXml and SQL examples show the patterns applied with `in`.

##### [FetchXml](#tab/fetchxml)

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

Using `exists` or `in` link types can reduce the size of intermediate or final query results, especially when many matching linked rows exist for the same parent rows, or when multiple link entities are used with the same parent  Using `exists` or `in` link types can improve performance of the query compared to the `inner` type because it doesn't require returning a Cartesian product containing all possible permutations of rows from different linked entities for each parent row.

These link types might also allow Dataverse to only find the first matching linked entity row for each parent row, which is more efficient than finding all matching rows in the linked entity in an `inner` join.

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

The `matchfirstrowusingcrossapply` link type is equivalent to the `inner` type except it only returns the parent row at most once. The parent row is returned only if there are matching rows in the linked entity but, unlike `in` and `exists` types, it **does** return column values from one of the matching rows in the linked entity. Use this when only a single example of a matching row from the linked entity is sufficient and multiple copies of the parent row in the results aren't necessary.

#### Related table property/attribute names are inconsistent

When using the `matchfirstrowusingcrossapply` link type, the names of the properties returned using Web API, or the SDK [Entity.Attributes collection](/dotnet/api/microsoft.xrm.sdk.entity.attributes) `Keys` values for the related table columns are different than other types of joins. Usually, these will follow the `<tablealias>.<logicalname>` format. However, for the `matchfirstrowusingcrossapply` link type, the [SchemaName](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.schemaname) values are used without the table alias prefix.

Using the previous query example with any other link-type, you can expect the properties or keys to have these names:

- `fullname`
- `contactid`
- `account1.accountid`
- `account1.name`

But with the `matchfirstrowusingcrossapply` link type, the properties or keys have these names:

- `fullname`
- `contactid`
- `AccountId`
- `Name`


## Next steps

Learn how to order rows.

> [!div class="nextstepaction"]
> [Order rows](order-rows.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
