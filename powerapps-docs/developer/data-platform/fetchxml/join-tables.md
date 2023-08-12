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


## Child elements

Within the `link-entity` element you can add child elements just like on the parent element to:

- [Select columns](select-columns.md) from the related table
- [Filter rows](filter-rows.md) from the related table
- Join another related table

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


## One-to-many relationships

## Many-to-many relationships

## No relationship

TODO: Describe how FetchXml can be used to create queries on match values where no relationship exists.

## Limitations

You can add up to 15 link-entity elements to a query. Each link-entity adds a JOIN to the query and increases the time to execute the query. This limit is to protect performance. If you add more than 15 link-entity elements to a query you will get this error: [TODO]


## Next steps

Learn how to order rows.

> [!div class="nextstepaction"]
> [Order rows](order-rows.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]