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
|`to`|No|[!INCLUDE [link-entity-to-description](includes/link-entity-to-description.md)] [While not technically required, this attribute is usually used.](../join-tables.md#using-to-and-from-attributes)|
|`from`|No|[!INCLUDE [link-entity-name-from-description](includes/link-entity-from-description.md)] [While not technically required, this attribute is usually used.](../join-tables.md#using-to-and-from-attributes)|
|`alias`|No|[!INCLUDE [link-entity-name-alias-description](includes/link-entity-alias-description.md)]|
|`link-type`|No|[!INCLUDE [link-entity-name-link-type-description](includes/link-entity-link-type-description.md)]|
|`intersect`|No|[!INCLUDE [link-entity-name-intersect-description](includes/link-entity-intersect-description.md)]|

### link-type options

Use `link-type` to apply filters on the records returned. The following table describes the valid `link-type` values

|Name|Description|
|---------|---------|
|`inner`|Default. Restricts results to rows with matching values in both tables.|
|`outer`|Includes results from the parent element that don't have a matching value.|
|`any`|A [Filter Link Type](#filter-link-types).[!INCLUDE [link-type-any-description](includes/link-type-any-description.md)] |
|`not any`|A [Filter Link Type](#filter-link-types). [!INCLUDE [link-type-not-any-description](includes/link-type-not-any-description.md)] |
|`all`|A [Filter Link Type](#filter-link-types). [!INCLUDE [link-type-all-description](includes/link-type-all-description.md)]|
|`not all`|A [Filter Link Type](#filter-link-types).[!INCLUDE [link-type-not-all-description](includes/link-type-not-all-description.md)]|
|`exists`|Restricts results to rows with matching values in both tables using an [EXISTS](/sql/t-sql/language-elements/exists-transact-sql) condition in the `where` clause following this pattern:<br/>`exists (select linkEntity.Id from linkEntity where parentEntity.LinkTo = linkEntity.LinkFrom <additional filters>)`<br/>This link type does not allow selecting columns values from the link entity and will only return the parent row once when multiple matching link entity rows exist. This is equivalent to the `inner` type except it only returns the parent row at most once and doesn't return column values of the link entity rows.|
|`in`|Restricts results to rows with matching values in both tables using an [IN](/sql/t-sql/language-elements/in-transact-sql) condition in the `where` clause following this pattern:<br/>`parentEntity.LinkTo in (select linkEntity.LinkFrom from linkEntity <additional filters>)`.<br/>When using this link type, you can't select column values from the link entity and the parent row is only returned once when multiple matching link entity rows exist. This is equivalent to the `inner` type except it only returns the parent row at most once and doesn't return the column values of the link entity rows.|
|`matchfirstrowusingcrossapply`|Includes results from the parent element that don't have a matching value. When multiple matching link entity rows exist for a given parent row, the parent row is only returned once and the column values are included for only one of the matching link entity rows. This is useful when an example of a link entity row is needed but finding the column values for all of them is not required. This is equivalent to the `outer` type except it only finds at most one link entity row.|

#### Filter Link Types

Use these types inside of a [filter element](filter.md). These filters are child conditions following the behavior defined by the `type` attribute of the parent `filter`.

Filters using these types return the parent row at most once even if multiple matching rows exist in the link entity. They do not allow returning column values from the link entity rows.

The following query using the `any` link type returns records from the [contact](../../reference/entities/contact.md) table that are referenced by the [PrimaryContactId lookup column](../../reference/entities/account.md#BKMK_PrimaryContactId) of at least one [account](../../reference/entities/account.md) record:

``` xml
<fetch>
  <entity name='contact'>
    <attribute name='fullname' />
    <filter type='and'>
      <link-entity name='account' 
       from='primarycontactid' 
       to='contactid' 
       link-type='any'>
      </link-entity>
    </filter>
  </entity>
</fetch>
```

This query uses a `filter` of type `or` with a child `link-entity` of type `any` to return records in [contact](../../reference/entities/contact.md) that _either_ are referenced by the [PrimaryContactId lookup column](../../reference/entities/account.md#BKMK_PrimaryContactId) of at least one [account](../../reference/entities/account.md) record _or_ have the [Contact.StateCode picklist column](../../reference/entities/contact.md#BKMK_StateCode) set to 1 : **Inactive**:

``` xml
<fetch>
  <entity name='contact'>
    <attribute name='fullname' />
    <filter type='or'>
      <link-entity name='account' 
       from='primarycontactid' 
       to='contactid' 
       link-type='any'>
      </link-entity>
      <condition attribute='statecode' operator='eq' value='1' />
    </filter>
  </entity>
</fetch>
```

This query uses a `link-entity` of type `not all` to return records from the [contact](../../reference/entities/contact.md) table that are referenced by the [PrimaryContactId lookup column](../../reference/entities/account.md#BKMK_PrimaryContactId) of at least one [account](../../reference/entities/account.md) record that has its [Name column](../../reference/entities/account.md#BKMK_Name) **not** equal to 'Contoso':

``` xml
<fetch>
  <entity name='contact'>
    <attribute name='fullname' />
    <filter type='and'>
      <link-entity name='account' 
       from='primarycontactid' 
       to='contactid' 
       link-type='not all'>
        <filter type='and'>
          <condition attribute='name' operator='eq' value='Contoso' />
        </filter>
      </link-entity>
    </filter>
  </entity>
</fetch>
```

<!-- TODO: Show FetchXML equivalent of OData Lambda operator examples
https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#lambda-operator-examples -->

## Parent elements

|Name|Description|
|---------|---------|
|[entity](entity.md)|[!INCLUDE [entity-description](includes/entity-description.md)]|
|[link-entity](link-entity.md)|Joins a table related to the [entity](entity.md) or [link-entity](link-entity.md) to return additional columns with the result.|

## Child elements

|Name|Occurrences|Description|
|---------|---------|---------|
|[all-attributes](all-attributes.md)|0 or 1|[!INCLUDE [all-attributes-description](includes/all-attributes-description.md)]|
|[attribute](attribute.md)|0 or many|[!INCLUDE [attribute-description](includes/attribute-description.md)]|
|[order](order.md)|0 or many|[!INCLUDE [order-description](includes/order-description.md)]|
|[link-entity](link-entity.md)|0 or many|Joins a table related to the [entity](entity.md) or [link-entity](link-entity.md) to return additional columns with the result.|
|[filter](filter.md)|0 or 1|[!INCLUDE [filter-description](includes/filter-description.md)]|

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
