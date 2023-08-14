---
title: Join tables using FetchXml
description: Learn how to use FetchXml to join tables when you retrieve data from Microsoft Dataverse.
ms.date: 08/31/2023
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

Use the [link-entity element](reference/link-entity.md) to describe the data from related tables to return with your query. For example, the following query returns data from the [account](../reference/entities/account.md) and [contact](../reference/entities/contact.md) tables based on the [PrimaryContactId lookup column](../reference/entities/account.md#BKMK_PrimaryContactId) in the account record:

```xml
<fetch>
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
 | Contoso Pharmaceuticals (sample) | Robert Lyon (sample)       |
 -----------------------------------------------------------------
 | Alpine Ski House (sample)        | Paul Cannon (sample)       |
 -----------------------------------------------------------------
 | A. Datum Corporation (sample)    | Rene Valdes (sample)       |
 -----------------------------------------------------------------
 | Coho Winery (sample)             | Jim Glynn (sample)         |
 -----------------------------------------------------------------
```

## Required attribute values

When you add the `link-entity` element, you must set these attribute values:


|Attribute|Description|
|---------|---------|
|`name`|[!INCLUDE [link-entity-name-description](reference/includes/link-entity-name-description.md)]<br />In this case, `contact`.|
|`from`|[!INCLUDE [link-entity-from-description](reference/includes/link-entity-from-description.md)]<br />In this case, `contactid`.|
|`to`|[!INCLUDE [link-entity-from-description](reference/includes/link-entity-from-description.md)]<br />In this case, `primarycontactid`.|


## Optional attribute values

The following attribute values are set in the previous example, but they have default values.

|Attribute|Description|
|---------|---------|
|`link-type`|[!INCLUDE [link-entity-link-type-description](reference/includes/link-entity-link-type-description.md)]|
|`alias`|[!INCLUDE [link-entity-alias-description](reference/includes/link-entity-alias-description.md)]|


## Many-to-one relationships

The previous example is a many-to-one relationship where many account records can refer to a one contact record. This information is defined in the [Account account_primary_contact many-to-one relationship](../reference/entities/account.md#BKMK_account_primary_contact), which has the following values:


|Property|Value|Comment|
|---------|---------|---------|
|`SchemaName`|`account_primary_contact`|Unique Name of the relationship|
|`ReferencedEntity`|`contact`|The referenced table. The *one* in many-to-one.|
|`ReferencedAttribute`|`contactid`|The primary key of the referenced table.|
|`ReferencingEntity`|`account`|The table with a lookup column referencing the other table. The *many* in many-to-one.|
|`ReferencingAttribute`|`primarycontactid`|The name of the lookup column.|
|`RelationshipType`|`OneToManyRelationship`|A one-to-many relationship when viewed from the *referenced* (one) table.<br />A many-to-one relationship when viewed from the *referencing* (many) table|

### Retrieve relationship information

If you use the [XrmToolbox](../community-tools.md#xrmtoolbox) [FetchXmlBuilder](https://fetchxmlbuilder.com/), you can see how this tool allows you to select the relationship to set the appropriate `name`, `from`, and `to` attribute values.

You can also use other tools and APIs to look up the appropriate `name`, `from`, and `to` attribute values to use. For more information see:

- [Browse table definitions in your environment](../browse-your-metadata.md)
- [Query schema definitions](../query-schema-definitions.md)


## One-to-many relationships

Many-to-one and one-to-many relationships are like looking at two sides of a coin. The relationship exists between the tables, so the way you use it depends on which table is the base table for your query.

You can retrieve the same data as the previous example from the contact table using the same relationship, except from the side of the contact table. Use the data from the [Contact account_primary_contact one-to-many relationship](../reference/entities/contact.md#BKMK_account_primary_contact), but adjust the values for the different view of the relationship.

```xml
<fetch>
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
 | Robert Lyon (sample)       | Contoso Pharmaceuticals (sample) |
 -----------------------------------------------------------------
 | Paul Cannon (sample)       | Alpine Ski House (sample)        |
 -----------------------------------------------------------------
 | Rene Valdes (sample)       | A. Datum Corporation (sample)    |
 -----------------------------------------------------------------
 | Jim Glynn (sample)         | Coho Winery (sample)             |
 -----------------------------------------------------------------
```

In this example:

- The `name` value is the logical name of the *referencing* table: `account`.
- The `from` value is the name of the lookup column in the *referencing* account table: `primarycontactid`.
- The `to` value is the primary key of the *referenced* contact table: `contactid`.
- The `alias` attribute is recommended for the `link-entity` with a one-to-many relationship. If an alias isn't provided, a default alias is generated.
- The `link-type` attribute isn't included. It will default to `inner`.

## Many-to-many relationships

Many-to-Many relationships depend on an intersect table.  An intersect table typically has just four columns, but only two of them are important in this case. All intersect tables have two columns that match the primary key columns of the participating tables, except that there is no unique constraint.

For example, the `TeamMembership` table supports the  [teammembership_association many-to-many relationship](../reference/entities/team.md#BKMK_teammembership_association) between [SystemUser](../reference/entities/systemuser.md) and [Team](../reference/entities/team.md) tables. It allows users to join multiple teams, and teams to have multiple users. `TeamMembership` has these columns: `systemuserid`, `teamid`.

If you want to retrieve information about users and the teams they belong to using the `teammembership_association` many-to-many relationship, you use this fetchXML:

```xml
<fetch>
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


There are two nested link-entities.

- The first one connects `systemuser` to the `teammembership` intersect table where `systemuserid` = `systemuserid`.
- The second one connects `teammembership` intersect table to team where `teamid` = `teamid`.

<!-- TODO: Is the intersect='true' attribute required? What benefit does it provide? -->

## No relationship

TODO:

- Describe how FetchXml can be used to create queries on match values where no relationship exists.
- Do we support this? https://jonasr.app/my-state-contacts/ claims "not unsupported"..
- Does this introduce other considerations?

## Limitations

You can add up to 15 `link-entity` elements to a query. Each link-entity adds a JOIN to the query and increases the time to execute the query. This limit is to protect performance. If you add more than 15 link-entity elements to a query you will get this error:

> Error Code: `0x8004430D`  
> Error Number: `-2147204339`  
> Error Message: `Number of link entities in query exceeded maximum limit.`  

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