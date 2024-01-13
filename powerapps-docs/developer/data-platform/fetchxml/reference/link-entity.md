---
title: link-entity element
description: Use this element to join tables with the containing entity or link-entity element.
author: pnghub
ms.author: gned
ms.reviewer: jdaly
ms.date: 08/31/2023
ms.topic: reference
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# link-entity element

[!INCLUDE [link-entity-description](includes/link-entity-description.md)]

[Learn how to join tables using FetchXml](../join-tables.md).

## Examples

The following examples show using `link-entity` with different types of relationships.

### Many-to-one relationship

This query returns data from the [account](../../reference/entities/account.md) and [contact](../../reference/entities/contact.md) tables based on the [PrimaryContactId lookup column](../../reference/entities/account.md#BKMK_PrimaryContactId) in the account record:

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

### One-to-many relationship

This query returns data from the [contact](../../reference/entities/contact.md) and [account](../../reference/entities/account.md) tables based on the [Contact account_primary_contact one-to-many relationship](../../reference/entities/contact.md#BKMK_account_primary_contact).

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

### Many-to-many relationship

This query returns data from the [SystemUser](../../reference/entities/systemuser.md) and [Team](../../reference/entities/team.md) tables using the [teammembership_association many-to-many relationship](../../reference/entities/team.md#BKMK_teammembership_association).

```xml
<fetch>
  <entity name='systemuser'>
    <attribute name='fullname' />
    <link-entity name='teammembership'
      from='systemuserid'
      to='systemuserid' >
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

## Attributes

|Name|Required?|Description|
|---------|---------|---------|
|`name`|Yes|[!INCLUDE [link-entity-name-description](includes/link-entity-name-description.md)]|
|`to`|No|[!INCLUDE [link-entity-to-description](includes/link-entity-to-description.md)][While not technically required, this attribute is usually used.](../join-tables.md#using-to-and-from-attributes)|
|`from`|No|[!INCLUDE [link-entity-name-from-description](includes/link-entity-from-description.md)][While not technically required, this attribute is usually used.](../join-tables.md#using-to-and-from-attributes)|
|`alias`|No|[!INCLUDE [link-entity-name-alias-description](includes/link-entity-alias-description.md)]|
|`link-type`|No|[!INCLUDE [link-entity-name-link-type-description](includes/link-entity-link-type-description.md)]|
|`intersect`|No|[!INCLUDE [link-entity-name-intersect-description](includes/link-entity-intersect-description.md)]|
|`enableprefiltering`|No|[!INCLUDE [link-entity-name-enableprefiltering-description](includes/link-entity-enableprefiltering-description.md)]|
|`prefilterparametername`|No|[!INCLUDE [link-entity-name-prefilterparametername-description](includes/link-entity-prefilterparametername-description.md)]|

### link-type options

Use `link-type` to apply filters on the records returned. The following table describes the valid `link-type` values

|Name|Description|
|---------|---------|
|`inner`|Default. Restricts results to rows with matching values in both tables.|
|`outer`|Includes results from the parent element that don't have a matching value.|
|`any`|A [Filter Link Type](#filter-link-types). Restricts results to parent rows with matching rows in the linked entity.|
|`not any`|A [Filter Link Type](#filter-link-types). Restricts results to parent rows with no matching rows in the linked entity.|
|`all`|A [Filter Link Type](#filter-link-types). Restricts results to parent rows where every row in the link entity with matching `from` column value satisfies the additional filters defined for this link entity. This includes parent rows which have no link entity rows with matching `from` values at all.|
|`not all`|A [Filter Link Type](#filter-link-types).  Restricts results to parent rows where at least one row in the link entity with matching `from` column value does not satisfy the additional filters defined for this link entity.|
|`exists`|Restricts results to rows with matching values in both tables using an `exists` condition in the `where` clause following this pattern:<br/>`exists (select linkEntity.Id from linkEntity where parentEntity.LinkTo = linkEntity.LinkFrom <additional filters>)`. This link type does not allow selecting columns values from the link entity and will only return the parent row once when multiple matching link entity rows exist. This is equivalent to the `inner` type except for only returning the parent row at most once and not returning column value of the link entity rows.|
|`in`|Restricts results to rows with matching values in both tables using an `in` condition in the `where` clause following this pattern:<br/>`parentEntity.LinkTo in (select linkEntity.LinkFrom from linkEntity <additional filters>)`. This link type does not allow selecting columns values from the link entity and will only return the parent row once when multiple matching link entity rows exist. This is equivalent to the `inner` type except for only returning the parent row at most once and not returning column value of the link entity rows.|
|`matchfirstrowusingcrossapply`|Includes results from the parent element that don't have a matching value. When multiple matching link entity rows exist for a given parent row, the parent row will only be returned once and the column values will be included only for one of the matching link entity rows. This is useful when an example of a link entity row is needed but finding the column values for all of them is not required. This is equivalent to the `outer` type except for only finding one link entity row at most.|

#### Filter Link Types

Link entities using these types must be defined inside of a [filter element](reference/filter.md) and are interpreted as child conditions following the behavior defined by the `type` attribute of the parent `filter`.

These link entities always return the parent row at most once even if multiple matching rows exist in the link entity. They do not allow returning column values from the link entity rows.

## Parent elements

|Name|Description|
|---------|---------|
|[entity](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[link-entity](link-entity.md)|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|

## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[all-attributes element](all-attributes.md)|0 or 1|[!INCLUDE [all-attributes-description](includes/all-attributes-description.md)]|
|[attribute element](attribute.md)|0 or many|[!INCLUDE [attribute-description](includes/attribute-description.md)]|
|[order element](order.md)|0 or many|[!INCLUDE [order-description](includes/order-description.md)]|
|[link-entity element](link-entity.md)|0 or many|[!INCLUDE [link-entity-description](includes/link-entity-description.md)]|
|[filter element](filter.md)|0 or 1|[!INCLUDE [filter-description](includes/filter-description.md)]|

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
