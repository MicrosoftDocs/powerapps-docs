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
|`to`|Yes|[!INCLUDE [link-entity-to-description](includes/link-entity-to-description.md)]|
|`from`|Yes|[!INCLUDE [link-entity-name-from-description](includes/link-entity-from-description.md)]|
|`alias`|No|[!INCLUDE [link-entity-name-alias-description](includes/link-entity-alias-description.md)]|
|`link-type`|No|[!INCLUDE [link-entity-name-link-type-description](includes/link-entity-link-type-description.md)]|
|`intersect`|No|[!INCLUDE [link-entity-name-intersect-description](includes/link-entity-intersect-description.md)]|
|`forceseek`|No|[!INCLUDE [link-entity-name-forceseek-description](includes/link-entity-forceseek-description.md)]|
|`enableprefiltering`|No|[!INCLUDE [link-entity-name-enableprefiltering-description](includes/link-entity-enableprefiltering-description.md)]|
|`prefilterparametername`|No|[!INCLUDE [link-entity-name-prefilterparametername-description](includes/link-entity-prefilterparametername-description.md)]|

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
