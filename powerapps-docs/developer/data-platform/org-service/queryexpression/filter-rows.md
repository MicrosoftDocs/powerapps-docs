---
title: Filter rows using QueryExpression
description: Learn how to use QueryExpression to filter rows when you retrieve data from Microsoft Dataverse.
ms.date: 03/18/2024
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Filter rows using QueryExpression

<!-- 
Related: Seems you can filter on 'child column' values, those columns which have the naming convention:
<lookupname>name and have AttributeOf = lookupname
There is a 'emitVirtualAttributes' parameter for pac modelbuilder
https://github.com/microsoft/powerplatform-vscode/issues/509
 -->

To set conditions on the rows of data to return, set the [QueryExpression.Criteria](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.criteria) or [LinkEntity.LinkCriteria](/dotnet/api/microsoft.xrm.sdk.query.linkentity.linkcriteria) properties to an instance of the [FilterExpression class](/dotnet/api/microsoft.xrm.sdk.query.filterexpression).

To set the conditions, add one or more [ConditionExpression class](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression) instances to the [FilterExpression.Conditions property](/dotnet/api/microsoft.xrm.sdk.query.filterexpression.conditions).

The [FilterExpression.FilterOperator property](/dotnet/api/microsoft.xrm.sdk.query.filterexpression.filteroperator) uses the [LogicalOperator enum](/dotnet/api/microsoft.xrm.sdk.query.logicaloperator) value to specify whether *all* (`And`) or *any* (`Or`) of the conditions must be met. The default is `And`.

Use the [FilterExpression.Filters property](/dotnet/api/microsoft.xrm.sdk.query.filterexpression.filters) to add additional filter criteria that can be combined using `And` or `Or`.

For each condition, set the [ConditionExpression.Operator property](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.operator) to one of the [ConditionOperator enum](/dotnet/api/microsoft.xrm.sdk.query.conditionoperator) members to specify how to evaluate a row column value.

For example, the following query returns account records where `address1_city` equals 'Redmond'. It uses `LogicalOperator.And` with `ConditionOperator.Equal`.

```csharp
QueryExpression query = new("account")
{
   TopCount = 5,
   ColumnSet = new ColumnSet("name"),
   Criteria = new FilterExpression(LogicalOperator.And)
   {
      Conditions = {
         new ConditionExpression(
            attributeName:"address1_city",
            conditionOperator: ConditionOperator.Equal,
            value:"Redmond")
      }
   }
};
```

This query returns account records where `address1_city` equals 'Redmond', 'Seattle', or 'Bellevue'. It uses `LogicalOperator.Or` with three `ConditionExpression` instances created using the [ConditionExpression(String, String, ConditionOperator, Object) constructor](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.-ctor#microsoft-xrm-sdk-query-conditionexpression-ctor(system-string-system-string-microsoft-xrm-sdk-query-conditionoperator-system-object)) that each use `ConditionOperator.Equal`.

```csharp
QueryExpression query = new("account")
{
   TopCount = 5,
   ColumnSet = new ColumnSet("name"),
   Criteria = new FilterExpression(LogicalOperator.Or)
   {
      Conditions = {
         new ConditionExpression(
            attributeName:"address1_city",
            conditionOperator: ConditionOperator.Equal,
            value:"Redmond"),
         new ConditionExpression(
            attributeName:"address1_city",
            conditionOperator: ConditionOperator.Equal,
            value:"Seattle"),
         new ConditionExpression(
            attributeName:"address1_city",
            conditionOperator: ConditionOperator.Equal,
            value:"Bellevue")
      }
   }
};
```

The previous query can also be represented using `ConditionOperator.In`, with a single `ConditionExpression`. This condition is created using the [ConditionExpression(String, ConditionOperator, Object[]) constructor](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.-ctor?view=dataverse-sdk-latest#microsoft-xrm-sdk-query-conditionexpression-ctor(system-string-system-string-microsoft-xrm-sdk-query-conditionoperator-system-object())) that sets multiple values to compare to `address1_city`.

```csharp
QueryExpression query = new("account")
{
   TopCount = 5,
   ColumnSet = new ColumnSet("name"),
   Criteria = new FilterExpression(LogicalOperator.Or)
   {
      Conditions = {
         new ConditionExpression(
            attributeName:"address1_city",
            conditionOperator: ConditionOperator.In,
            values: new string[] { "Redmond", "Seattle", "Bellevue" })
      }
   }
};
```

## Operator parameters

Operators can require no parameters, a single parameter, or multiple parameters. The operator determines how you set the value to evaluate.

### No parameters

Some operators don't require any parameter values.

For example, you can use the [ConditionExpression(String, ConditionOperator) constructor](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.-ctor#microsoft-xrm-sdk-query-conditionexpression-ctor(system-string-microsoft-xrm-sdk-query-conditionoperator)) with  `ConditionOperator.EqualUserId` to evaluate any unique identifier to determine if it matches the calling user's ID.

```csharp
new ConditionExpression(
   attributeName:"ownerid",
   conditionOperator: ConditionOperator.EqualUserId)
```

### Single parameter

When an operator requires a single parameter, use the  [ConditionExpression(String, ConditionOperator, Object) constructor](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.-ctor#microsoft-xrm-sdk-query-conditionexpression-ctor(system-string-microsoft-xrm-sdk-query-conditionoperator-system-object)) to specify the `value` parameter to the value to evaluate.

For example, you can use `ConditionOperator.Equal` to evaluate the `statecode` choice column value of a record.

```csharp
new ConditionExpression(
    attributeName:"statecode",
    conditionOperator: ConditionOperator.Equal,
    value: 0)
```

### Multiple parameters

When an operator requires multiple parameters, use the [ConditionExpression(String, ConditionOperator, Object[]) constructor](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.-ctor#microsoft-xrm-sdk-query-conditionexpression-ctor(system-string-microsoft-xrm-sdk-query-conditionoperator-system-object())) `values` parameter to specify the values to evaluate.

For example, you can use `ConditionOperator.Between` to evaluate a number to determine if it is between a set of values.

```csharp
new ConditionExpression(
    attributeName:"numberofemployees",
    conditionOperator: ConditionOperator.Between,
    values: new object[] {6,20 })
```

## Filters on link-entity

When you use the [LinkEntity.LinkCriteria property](/dotnet/api/microsoft.xrm.sdk.query.linkentity.linkcriteria) to apply a filter, the filter will be applied with the join unless you configure the filter *after* the join.

When the [LinkEntity.JoinOperator property](/dotnet/api/microsoft.xrm.sdk.query.linkentity.joinoperator) uses `JoinOperator.LeftOuter`, you might want the filter to be applied after the join by setting the [ConditionExpression.EntityName property](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.entityname) value. If you're using the [LinkEntity.EntityAlias property](/dotnet/api/microsoft.xrm.sdk.query.linkentity.entityalias), use that value to set the `ConditionExpression.EntityName` property. Otherwise, set the `ConditionExpression.EntityName` property to the [LinkEntity.LinkFromEntityName property](/dotnet/api/microsoft.xrm.sdk.query.linkentity.linkfromentityname) value.


## Filter on column values in the same row

You can create filters that compare columns on values in the same row using by setting the [ConditionExpression.CompareColumns property](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.comparecolumns) using constructors like [ConditionExpression(String, String, ConditionOperator, Boolean, Object)](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.-ctor#microsoft-xrm-sdk-query-conditionexpression-ctor(system-string-system-string-microsoft-xrm-sdk-query-conditionoperator-system-boolean-system-object)) that allow you to set this using the `compareColumns` parameter.

For example, if you want to find any contact records where the `firstname` column value matches the `lastname` column value, you can use this query:

```csharp
QueryExpression query = new("contact")
{
      ColumnSet = new ColumnSet("firstname"),
      Criteria = new FilterExpression(LogicalOperator.And)
      {
         Conditions = {
            new ConditionExpression(
                  attributeName:"firstname",
                  conditionOperator: ConditionOperator.Equal,
                  compareColumns: true, 
                  value: "lastname")
         }
      }
};
```

### Limitations on column comparison filters

There are limitations on these kinds of filters:

- [ConditionExpression.Operator](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.operator) can only use these [ConditionOperator enum](/dotnet/api/microsoft.xrm.sdk.query.conditionoperator) members:

  |Operator |Description|
  |---------|---------|
  |`Equal`|   The two values are equal.|
  |`NotEqual`| The two values are not equal. |
  |`GreaterThan`|The value is greater than the compared value. |
  |`GreaterEqual`|The value is greater than or equal to the compared value.|
  |`LessThan`|The value is less than the compared value. |
  |`LessEqual`|The value is less than or equal to the compared value. |

- Only two columns can be compared at a time
- Extended condition operations aren't supported. For example: `value: "amount" + 100`
- The columns must be the same type. For example: You can't compare a string value with a number value

## Filter on values in related records

<!-- TODO: Continue from here -->

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