---
title: Filter rows using FetchXml
description: Learn how to use FetchXml to filter rows when you retrieve data from Microsoft Dataverse.
ms.date: 08/31/2023
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Filter rows using FetchXml

Use the [filter element](reference/filter.md) within an [entity](reference/entity.md), [link-entity](reference/link-entity.md), or another `filter` element to set conditions on the rows of data to return.

Add one or more [condition elements](reference/condition.md) to the filter to set the conditions. The containing `filter` `type` attribute determines whether all (`and`) or any (`or`) of the conditions must be met. The default is `and`. By nesting filter elements you can create complex filter criteria that combine criteria evaluated using `and` or `or`.

Each `condition` has an `operator` attribute to evaluate a row column value. There are many [operator conditions](reference/operators.md) for you to choose from.

For example, the following query returns account records where `address1_city` equals 'Redmond'. It uses `<filter type='and'>`.

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

This query returns account records where `address1_city` equals 'Redmond', 'Seattle', or 'Bellevue'. It uses `<filter type='or'>` with three [condition elements](reference/condition.md).

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

The previous query can also be represented using the `in` operator with a single `condition` element. This condition contains multiple [value elements](reference/value.md) to specify the values to compare to `address1_city`.

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

Operators can require no parameters, a single parameter, or multiple parameters. This determines how you set the value to evaluate.

### No parameters

Some operators don't require any parameters.
For example, you can use the `eq-userid` operator to evaluate any unique identifier to determine if it matches the calling user's ID.

```xml
<condition attribute='ownerid' operator='eq-userid' />
```

### Single parameter

When an operator requires a single parameter, use the `value` attribute to set the value to evaluate.
For example, you can use the `eq` operator to evaluate the `statecode` choice column value of a record by setting the `value` attribute.

```xml
<condition attribute='statecode' operator='eq' value='0' />
```

### Multiple parameters

When an operator requires multiple parameters, use the [value element](reference/value.md) to specify the values to evaluate.
For example, you can use the `between` operator to evaluate a number to determine if it is between a set of values.

```xml
<condition attribute="numberofemployees" operator="between">
  <value>6</value>
  <value>20</value>
</condition>
```

## Filters on link-entity

When you apply a `filter` within a [link-entity](reference/link-entity.md), the filter will be applied with the join unless you configure the filter to occur *after* the join.

When the [link-entity](reference/link-entity.md) `link-type` attribute value is `outer`, you may want the filter to be applied after the join by setting the [condition](reference/condition.md) `entityname` attribute value. If you are using a [link-entity](reference/link-entity.md) `alias`, use the `alias` value to set the `entityname` attribute. Otherwise, set the `entityname` attribute value to the [link-entity](reference/link-entity.md) `name` attribute value.

<!-- 
TODO Example
Why would you want the filter to be applied after the join?
 -->

## Filter on column values in the same row

You can create filters that compare columns on values in the same row using the `valueof` attribute. For example, if you want to find any contact records where the `firstname` column value matches the `lastname` column value, you can use this query:

```xml
<fetch>
  <entity name='contact' >
    <attribute name='firstname' />
    <filter>
      <condition attribute='firstname' operator='eq' valueof='lastname'/>
    </filter>
  </entity>
</fetch>
```

## Limitations on column comparison filters

There are limitations on these kinds of filters:

- Filter can only use these [operators](reference/operators.md): `eq`, `ne`, `gt`, `ge`, `lt`, `le`.
- Only two columns may be compared at a time
- Extended condition operations aren't supported. For example: `valueof='amount'+ 100`
- The columns must be the same type. For example: You can't compare a string value with an number value.


## Returning distinct results

Use the [fetch element](reference/fetch.md) `distinct` attribute to require the query to exclude any duplicate values in the results.

If you use the `distinct` attribute, you must add at least one order element to have consistent paging.

## Limit the number of rows

To limit the number of rows returned, use the [fetch element](reference/fetch.md) `top` attribute. You can set this to a value up to 5,000 because that is the maximum number of rows that can be returned.  The `top` attribute isn't used to get paged results.

## Next steps

Learn how to page results.

> [!div class="nextstepaction"]
> [Page results](page-results.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]