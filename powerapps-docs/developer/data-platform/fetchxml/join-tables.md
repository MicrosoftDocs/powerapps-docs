---
title: Join tables using FetchXml
description: Learn how to use FetchXml to join tables when you retrieve data from Microsoft Dataverse.
ms.date: 01/30/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Join tables using FetchXml

As described in [Query data using FetchXml](overview.md), start your query by selecting a table using the [entity element](reference/entity.md).

Use the [link-entity element](reference/link-entity.md) to describe the data from related tables to return with your query with the following attributes:


|Attribute|Short Description [Find more details in the link-entity element reference](reference/link-entity.md)|
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

If you use the [XrmToolbox](../community-tools.md#xrmtoolbox) [FetchXmlBuilder](https://fetchxmlbuilder.com/), you can see how this tool allows you to select the relationship to set the appropriate `name`, `from`, and `to` attribute values.

You can also use other tools and APIs to look up relationship data for the appropriate `name`, `from`, and `to` attribute values to use. For more information see:

- [Browse table definitions in your environment](../browse-your-metadata.md)
- [Query schema definitions](../query-schema-definitions.md)


## One-to-many relationships

Many-to-one and one-to-many relationships are like looking at two sides of a coin. The relationship exists between the tables, so the way you use it depends on which table is the base table for your query.

You can retrieve the same data as the previous example from the contact table using the same relationship, except from the side of the contact table. Use the data from the [Contact account_primary_contact one-to-many relationship](../reference/entities/contact.md#BKMK_account_primary_contact), but adjust the values for the different view of the relationship.

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
|`link-type`|Not set|When no value is set, it will default to `inner`|

The results look like this:

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

<!-- 
TODO: Is the intersect='true' attribute required? What benefit does it provide? 
As far as I can see, it isn't required, but provides a flag to indicate that no attributes are expected to be included from the table.
-->

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

It is possible to specify `to` and `from` attributes using columns that are not involved in a relationship.

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
> - It is important that the columns specified in the `to` and `from` attributes are the same type even if they are not involved in a relationship. Using columns of different types will require a type conversion that may have performance impact and may fail for some column values.

The following [column types](../../../maker/data-platform//types-of-fields) cannot be used in `to` and `from` attributes:
- **File**
- **Image**
- **MultiSelect Field**
- [**PartyList**](../../../maker/data-platform/types-of-fields#different-types-of-lookups) lookups

Some columns can be used in `to` and `from` attributes but may result in poor performance:
- Columns of the **Multiple Lines of Text** type
- Columns of the **Single Line of Text** type with a maximum length larger than 850
- [**Formula**](../../../maker/data-platform/formula-columns) columns
- [**Calculated**](../../../maker/data-platform/define-calculated-fields) columns
- [**Logical**](../entity-attribute-metadata#logical-columns) columns

## Find records not in a set

<!-- Summarizes this article: https://learn.microsoft.com/power-apps/developer/data-platform/use-fetchxml-left-outer-join-query-records-not-in -->

You can use FetchXml to create a query to return records that are not in a set using a *left outer join*. A left outer join returns each row that satisfies the join of the first input with the second input. It also returns any rows from the first input that had no matching rows in the second input. The non-matching rows in the second input are returned as null values.

You can perform a left outer join in FetchXML by using the `entityname` attribute as a condition operator. The `entityname` attribute is valid in conditions, filters, and nested filters. [Learn more about filters on link-entity](filter-rows.md#filters-on-link-entity).


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

## Limitations

You can add up to 15 `link-entity` elements to a query. Each link-entity adds a JOIN to the query and increases the time to execute the query. This limit is to protect performance. If you add more than 15 link-entity elements to a query you will get this error:

> Code: `0x8004430D`  
> Number: `-2147204339`  
> Message: `Number of link entities in query exceeded maximum limit.`  

## Child elements

Within the `link-entity` element you can add child elements just like on the parent element to:

- [Select columns](select-columns.md) from the related table
- [Filter rows](filter-rows.md) from the related table
- Join another related table


## Next steps

Learn how to order rows.

> [!div class="nextstepaction"]
> [Order rows](order-rows.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
