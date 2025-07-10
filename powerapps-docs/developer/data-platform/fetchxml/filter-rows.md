---
title: Filter rows using FetchXml
description: Learn how to use FetchXml to filter rows when you retrieve data from Microsoft Dataverse.
ms.date: 04/01/2024
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
 - rappen
---
# Filter rows using FetchXml

To set conditions on the rows of data to return, use the [filter element](reference/filter.md) within an [entity](reference/entity.md), [link-entity](reference/link-entity.md), or another `filter` element.

To set the conditions, add one or more [condition elements](reference/condition.md) to the filter. The containing `filter` `type` attribute determines whether *all* (`and`) or *any* (`or`) of the conditions must be met. The default is `and`. By nesting filter elements you can create complex filter criteria that combine criteria evaluated using `and` or `or`.

Each `condition` has an `operator` attribute to evaluate a row column value. There are many [condition operator values](reference/operators.md) for you to choose from.

For example, the following query returns account records where `address1_city` equals 'Redmond'. It uses `<filter type='and'>` with the [eq operator](reference/operators.md#eq).

```xml
<fetch>
   <entity name='account'>
      <attribute name='name' />
      <filter type='and'>
         <condition attribute='address1_city'
            operator='eq'
            value='Redmond' />
      </filter>
   </entity>
</fetch>
```

This query returns account records where `address1_city` equals 'Redmond', 'Seattle', or 'Bellevue'. It uses `<filter type='or'>` with three [condition elements](reference/condition.md) that each use the [eq operator](reference/operators.md#eq).

```xml
<fetch>
   <entity name='account'>
      <attribute name='name' />
      <attribute name='address1_city' />
      <filter type='or'>
         <condition attribute='address1_city'
            operator='eq'
            value='Redmond' />
         <condition attribute='address1_city'
            operator='eq'
            value='Seattle' />
         <condition attribute='address1_city'
            operator='eq'
            value='Bellevue' />
      </filter>
   </entity>
</fetch>
```

The previous query can also be represented using the [in operator](reference/operators.md#in) with a single `condition` element. This condition contains multiple [value elements](reference/value.md) to specify the values to compare to `address1_city`.

```xml
<fetch>
   <entity name='account'>
      <attribute name='name' />
      <attribute name='address1_city' />
      <filter type='and'>
         <condition attribute='address1_city'
            operator='in'>
            <value>Redmond</value>
            <value>Seattle</value>
            <value>Bellevue</value>
         </condition>
      </filter>
   </entity>
</fetch>
```

## Operator parameters

Operators can require no parameters, a single parameter, or multiple parameters. The operator determines how you set the value to evaluate.

### No parameters

Some operators don't require any parameters.
For example, you can use the [eq-userid operator](reference/operators.md#eq-userid) to evaluate any unique identifier to determine if it matches the calling user's ID.

```xml
<condition attribute='ownerid'
   operator='eq-userid' />
```

### Single parameter

When an operator requires a single parameter, use the `value` attribute to set the value to evaluate.
For example, you can use the [eq operator](reference/operators.md#eq) to evaluate the `statecode` choice column value of a record by setting the `value` attribute.

```xml
<condition attribute='statecode'
   operator='eq'
   value='0' />
```

### Multiple parameters

When an operator requires multiple parameters, use the [value element](reference/value.md) to specify the values to evaluate.
For example, you can use the [between operator](reference/operators.md#between) to evaluate a number to determine if it is between a set of values.

```xml
<condition attribute="numberofemployees"
   operator="between">
   <value>6</value>
   <value>20</value>
</condition>
```

## Filters on link-entity

When you apply a [filter](reference/filter.md) within a [link-entity](reference/link-entity.md), the filter will be applied with the join unless you configure the filter to occur *after* the join.

When the [link-entity](reference/link-entity.md) `link-type` attribute value is `outer`, you might want the filter to be applied after the join by setting the [condition](reference/condition.md) `entityname` attribute value. If you're using a [link-entity](reference/link-entity.md) `alias`, use the `alias` value to set the `entityname` attribute. Otherwise, set the `entityname` attribute value to the [link-entity](reference/link-entity.md) `name` attribute value.

For example, the following query returns contacts without a [parent account](../reference/entities/contact.md#BKMK_ParentCustomerId), or a parent account without a [fax](../reference/entities/account.md#BKMK_Fax).

```xml
<fetch>
  <entity name='contact'>
    <attribute name='fullname' />
    <filter>
      <condition entityname='a'
        attribute='fax'
        operator='null' />
    </filter>
    <link-entity name='account'
      from='accountid'
      to='parentcustomerid'
      link-type='outer'
      alias='a' />
  </entity>
</fetch>
```

## Filter on column values in the same row

You can create filters that compare columns on values in the same row using the `valueof` attribute. For example, if you want to find any contact records where the `firstname` column value matches the `lastname` column value, you can use this query:

```xml
<fetch>
   <entity name='contact' >
      <attribute name='firstname' />
      <filter>
         <condition attribute='firstname'
            operator='eq'
            valueof='lastname' />
      </filter>
   </entity>
</fetch>
```

### Cross table column comparisons

With FetchXML only, you can compare field values in related tables. The following example returns rows where the contact `fullname` column matches the account `name` column.

```xml
<fetch>
   <entity name='contact'>
      <attribute name='contactid' />
      <attribute name='fullname' />
      <filter type='and'>
         <condition attribute='fullname'
            operator='eq'
            valueof='acct.name' />
      </filter>
      <link-entity name='account'
         from='accountid'
         to='parentcustomerid'
         link-type='outer'
         alias='acct'>
         <attribute name='name' />
      </link-entity>
   </entity>
</fetch>
```

The [link-entity element](reference/link-entity.md) must use an `alias` attribute and the value of the `valueof` parameter must reference that alias and the column name in the related table.


### Limitations on column comparison filters

There are limitations on these kinds of filters:

- [Condition](reference/condition.md) can only use these [operators](reference/operators.md):

  |Operator |Description|
  |---------|---------|
  |[eq](reference/operators.md#eq)|[!INCLUDE [operator-eq-description](reference/includes/operator-eq-description.md)]|
  |[ne](reference/operators.md#ne)|[!INCLUDE [operator-ne-description](reference/includes/operator-ne-description.md)]|
  |[gt](reference/operators.md#gt)|[!INCLUDE [operator-gt-description](reference/includes/operator-gt-description.md)]|
  |[ge](reference/operators.md#ge)|[!INCLUDE [operator-ge-description](reference/includes/operator-ge-description.md)]|
  |[lt](reference/operators.md#lt)|[!INCLUDE [operator-lt-description](reference/includes/operator-lt-description.md)]|
  |[le](reference/operators.md#le)|[!INCLUDE [operator-le-description](reference/includes/operator-le-description.md)]|

- Only two columns can be compared at a time
- Extended condition operations aren't supported. For example: `valueof='amount'+ 100`
- The columns must be the same type. For example: You can't compare a string value with a number value

## Filter on values in related records

To filter on values in related records without returning those values, use a [link-entity element](reference/link-entity.md) within the [filter element](reference/filter.md) with one of the following `link-type` attributes:

<!-- Don't want first column to have line breaks -->
|Name&nbsp;&nbsp;&nbsp;&nbsp;|Description|
|---------|---------|
|`any`|[!INCLUDE [link-type-any-description](reference/includes/link-type-any-description.md)]|
|`not any`|[!INCLUDE [link-type-not-any-description](reference/includes/link-type-not-any-description.md)]|
|`all`|[!INCLUDE [link-type-all-description](reference/includes/link-type-all-description.md)]|
|`not all`|[!INCLUDE [link-type-not-all-description](reference/includes/link-type-not-all-description.md)]|

When you use these link types inside of a [filter element](reference/filter.md), these filters are child conditions following the behavior defined by the `type` attribute of the parent `filter`.

Filters using these types return the parent row at most once even if multiple matching rows exist in the link entity. They don't allow returning column values from the link entity rows.

### Examples of filters on values in related records

The following examples demonstrate filtering on values of related records. These examples include the equivalent SQL statements to help explain the behavior.

#### Or filter with `link-type` `any`

This query uses a `filter` of type `or` with a child `link-entity` of type `any` to return records in [contact](../reference/entities/contact.md) that:
- _either_ are referenced by the [PrimaryContactId lookup column](../reference/entities/account.md#BKMK_PrimaryContactId) of at least one [account](../reference/entities/account.md) record that has its [Name column](../reference/entities/account.md#BKMK_Name) equal to 'Contoso',
- _or_ have the [Contact.StateCode picklist column](../reference/entities/contact.md#BKMK_StateCode) set to 1 : **Inactive**:

#### [FetchXml](#tab/fetchxml)

``` xml
<fetch>
   <entity name='contact'>
      <attribute name='fullname' />
      <filter type='or'>
         <link-entity name='account'
            from='primarycontactid'
            to='contactid'
            link-type='any'>
            <filter type='and'>
               <condition attribute='name'
                  operator='eq'
                  value='Contoso' />
            </filter>
         </link-entity>
         <condition attribute='statecode'
            operator='eq'
            value='1' />
      </filter>
   </entity>
</fetch>
```

#### [SQL](#tab/sql)

``` sql
select 
    "contact0".fullname as "fullname" 
from Contact as "contact0" 
where "contact0".statecode = 1
    or exists (
        select "account1".primarycontactid
        from Account as "account1"
        where "account1".name = N'Contoso'
            and "contact0".contactid = "account1".primarycontactid)
```

---

#### `link-type` `not any`

This query uses the `not any` link type to return records from the [contact](../reference/entities/contact.md) table that is **not** referenced by the [PrimaryContactId lookup column](../reference/entities/account.md#BKMK_PrimaryContactId) of any [account](../reference/entities/account.md) record that has its [Name column](../reference/entities/account.md#BKMK_Name) equal to 'Contoso'. The _contact_ record might still be referenced by _account_ records with **other** _Name column_ values.

#### [FetchXml](#tab/fetchxml)

``` xml
<fetch>
   <entity name='contact'>
      <attribute name='fullname' />
      <filter type='and'>
         <link-entity name='account'
            from='primarycontactid'
            to='contactid'
            link-type='not any'>
            <filter type='and'>
               <condition attribute='name'
                  operator='eq'
                  value='Contoso' />
            </filter>
         </link-entity>
      </filter>
   </entity>
</fetch>
```

#### [SQL](#tab/sql)

``` sql
select 
    "contact0".fullname as "fullname" 
from Contact as "contact0" 
where not exists (
    select "account1".primarycontactid
    from Account as "account1"
    where "account1".name = N'Contoso' and "contact0".contactid = "account1".primarycontactid)
```

---

#### `link-type` `not all`

> [!NOTE]
> The meaning of `all` and `not all` link types is the opposite of what the names might imply, and they are typically used with inverted filters:
>
> - A link entity of type `not all` is equivalent to `any` and returns parent records that have link entity records matching the filters.
> - A link entity of type `all` returns parent records when some link entity records with a matching `from` column value exist but **none** of those link entity rows satisfy the additional filters defined inside of the [link-entity element](reference/link-entity.md).

This query uses a `link-entity` of type `not all` to return records from the [contact](../reference/entities/contact.md) table that are referenced by the [PrimaryContactId lookup column](../reference/entities/account.md#BKMK_PrimaryContactId) of at least one [account](../reference/entities/account.md) record that has its [Name column](../reference/entities/account.md#BKMK_Name) equal to 'Contoso':

#### [FetchXml](#tab/fetchxml)

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
               <condition attribute='name'
                  operator='eq'
                  value='Contoso' />
            </filter>
         </link-entity>
      </filter>
   </entity>
</fetch>
```

#### [SQL](#tab/sql)

``` sql
select 
    "contact0".fullname as "fullname" 
from Contact as "contact0" 
where exists (
    select "account1".primarycontactid
    from  Account as "account1"
    where "account1".name = N'Contoso'
        and "contact0".contactid = "account1".primarycontactid)
```

---

#### `link-type` `all`

This query uses a `link-entity` of type `all` to return records from the [contact](../reference/entities/contact.md) table that **are** referenced by the [PrimaryContactId lookup column](../reference/entities/account.md#BKMK_PrimaryContactId) of **some** [account](../reference/entities/account.md) record, but **none** of those _account_ records have their [Name column](../reference/entities/account.md#BKMK_Name) equal to 'Contoso':

#### [FetchXml](#tab/fetchxml)

``` xml
<fetch>
   <entity name='contact'>
      <attribute name='fullname' />
      <filter type='and'>
         <link-entity name='account'
            from='primarycontactid'
            to='contactid'
            link-type='all'>
            <filter type='and'>
               <condition attribute='name'
                  operator='eq'
                  value='Contoso' />
            </filter>
         </link-entity>
      </filter>
   </entity>
</fetch>
```

#### [SQL](#tab/sql)

``` sql
select 
    "contact0".fullname as "fullname" 
from Contact as "contact0" 
where exists (
    select "account1".primarycontactid
    from Account as "account1"
    where "contact0".contactid = "account1".primarycontactid
) and not exists (
    select "account1".primarycontactid
    from Account as "account1"
    where "account1".name = N'Contoso'
        and "contact0".contactid = "account1".primarycontactid)
```

---

## Condition limits

You can include no more than 500 total [condition](reference/condition.md) and  [link-entity](reference/link-entity.md) elements in a FetchXml query. Otherwise, you see this error:

> Name: `TooManyConditionsInQuery`<br />
> Code: `0x8004430C`<br />
> Number: `-2147204340`<br />
> Message: `Number of conditions in query exceeded maximum limit.`

You need to reduce the number of conditions to execute the query. You might be able to reduce the number of conditions by using the [in operator](reference/operators.md#in) that can be used with numbers, unique identifiers, and strings up to 850 characters.


## Next steps

Learn how to page results.

> [!div class="nextstepaction"]
> [Page results](page-results.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
