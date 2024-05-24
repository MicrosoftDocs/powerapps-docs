---
title: Filter rows using QueryExpression
description: Learn how to use QueryExpression to filter rows when you retrieve data from Microsoft Dataverse.
ms.date: 05/12/2024
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

To set conditions on the rows of data to return, set the [QueryExpression.Criteria](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.criteria) or [LinkEntity.LinkCriteria](/dotnet/api/microsoft.xrm.sdk.query.linkentity.linkcriteria) properties to an instance of the [FilterExpression class](/dotnet/api/microsoft.xrm.sdk.query.filterexpression).

To set the conditions, add one or more [ConditionExpression class](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression) instances to the [FilterExpression.Conditions collection](/dotnet/api/microsoft.xrm.sdk.query.filterexpression.conditions).

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

The previous query can also be represented using `ConditionOperator.In`, with a single `ConditionExpression`. This condition is created using the [ConditionExpression(String, ConditionOperator, Object[]) constructor](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.-ctor#microsoft-xrm-sdk-query-conditionexpression-ctor(system-string-system-string-microsoft-xrm-sdk-query-conditionoperator-system-object())) that sets multiple values to compare to `address1_city`.

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
    values: new object[] {6,20})
```

## Filters on LinkEntity

When you use the [LinkEntity.LinkCriteria property](/dotnet/api/microsoft.xrm.sdk.query.linkentity.linkcriteria) to apply a filter, the filter will be applied with the join unless you configure the filter to be applied in the `QueryExpression.Criteria`. 

When the [LinkEntity.JoinOperator property](/dotnet/api/microsoft.xrm.sdk.query.linkentity.joinoperator) uses `JoinOperator.LeftOuter`, you might want the filter to be applied in the `QueryExpression.Criteria` by setting the [ConditionExpression.EntityName property](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.entityname) value. If you're using the [LinkEntity.EntityAlias property](/dotnet/api/microsoft.xrm.sdk.query.linkentity.entityalias), use that value to set the `ConditionExpression.EntityName` property. Otherwise, set the `ConditionExpression.EntityName` property to the [LinkEntity.LinkFromEntityName property](/dotnet/api/microsoft.xrm.sdk.query.linkentity.linkfromentityname) value. [Learn more about finding records not in a set using ](join-tables.md#find-records-not-in-a-set)

For example, the following query returns contacts without a [parent account](../../reference/entities/contact.md#BKMK_ParentCustomerId), or a parent account without a [fax](../../reference/entities/account.md#BKMK_Fax).

```csharp
QueryExpression query = new("contact") { 
     ColumnSet = new ColumnSet("fullname"),
     Criteria = new FilterExpression(LogicalOperator.And) { 
         Conditions = { 
            new ConditionExpression(){ 
                AttributeName = "fax",
                EntityName = "a",
                Operator = ConditionOperator.Null
            }
         }
     },
     LinkEntities = { 
        new LinkEntity(
            linkFromEntityName:"contact",
            linkToEntityName:"account",
            linkFromAttributeName:"parentcustomerid",
            linkToAttributeName:"accountid",
            joinOperator: JoinOperator.LeftOuter){
           EntityAlias = "a"
        }
    }
};
```

## Filter on column values in the same row

You can create filters that compare columns on values in the same row using by setting the [ConditionExpression.CompareColumns property](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.comparecolumns) using constructors like [ConditionExpression(String, String, ConditionOperator, Boolean, Object)](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression.-ctor#microsoft-xrm-sdk-query-conditionexpression-ctor(system-string-system-string-microsoft-xrm-sdk-query-conditionoperator-system-boolean-system-object)) that allow you to set this using the `compareColumns` parameter. When `CompareColumns` is true, the value represents the name of the other column.

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

- You can only use these [ConditionOperator enum](/dotnet/api/microsoft.xrm.sdk.query.conditionoperator) operators:

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

To filter on values in related records without returning those values, use the `FilterExpression.AnyAllFilterLinkEntity` property with a [LinkEntity](/dotnet/api/microsoft.xrm.sdk.query.linkentity) instance where the [LinkEntity.JoinOperator](/dotnet/api/microsoft.xrm.sdk.query.linkentity.joinoperator) uses one of the following [JoinOperator enum](/dotnet/api/microsoft.xrm.sdk.query.joinoperator) members:

|Name|Description|
|---------|---------|
|`Any`|Restricts results to parent rows with any matching rows in the linked entity.|
|`NotAny`|Restricts results to parent rows with no matching rows in the linked entity.|
|`All`|Restricts results to parent rows where rows with matching `from` column value exist in the link entity but **none of those matching rows** satisfy the additional filters defined for this link entity. You need to **invert** the additional filters to find parent rows where **every** matching link entity row satisfies some additional criteria.|
|`NotAll`|Restricts results to parent rows with any matching rows in the linked entity. This link type is equivalent to `any` despite the name.|

When you use these `JoinOperator` member values with a `LinkEntity` specified by the  `FilterExpression.AnyAllFilterLinkEntity`, these filters are child conditions following the behavior defined by the `FilterExpression.FilterOperator` (And/Or).

Filters using these `JoinOperator` member values return the parent row at most once even if multiple matching rows exist in the `LinkEntity`. Any columns specified in the [LinkEntity.Columns property](/dotnet/api/microsoft.xrm.sdk.query.linkentity.columns) will be ignored.

### Examples of filters on values in related records

The following examples demonstrate filtering on values of related records. These examples include the equivalent SQL statements to help explain the behavior.

#### Or filter with `JoinOperator.Any`

This query uses a `FilterExpression` with the `FilterOperator` property set to `LogicalOperator.Or` and a `AnyAllFilterLinkEntity` property set with a `LinkEntity` that has the `JoinOperator` property set to `JoinOperator.Any`. This query will return [contact](../../reference/entities/contact.md) records that are _either_:

- Referenced by the [PrimaryContactId lookup column](../../reference/entities/account.md#BKMK_PrimaryContactId) of at least one [account](../../reference/entities/account.md) record that has its [Name column](../../reference/entities/account.md#BKMK_Name) equal to 'Contoso',
- _or_
- Have the [Contact.StateCode column](../../reference/entities/contact.md#BKMK_StateCode) set to 1 : **Inactive**:

#### [QueryExpression](#tab/qe)

``` csharp
var query = new QueryExpression("contact")
{
    ColumnSet = new ColumnSet("fullname"),
    Criteria = new FilterExpression(filterOperator: LogicalOperator.Or)
    {
        AnyAllFilterLinkEntity = new LinkEntity(
            linkFromEntityName: "contact",
            linkToEntityName: "account",
            linkFromAttributeName: "contactid",
            linkToAttributeName: "primarycontactid",
            joinOperator: JoinOperator.Any)
        {
            LinkCriteria = new FilterExpression(filterOperator: LogicalOperator.And)
            {
                Conditions = {
                    new ConditionExpression(
                        attributeName: "name",
                        conditionOperator: ConditionOperator.Equal,
                        value: "Contoso")
                }
            }
        },
        Conditions = {
            new ConditionExpression(
                attributeName:"statecode",
                conditionOperator: ConditionOperator.Equal,
                value: 1)
        }
    }
};
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

#### `JoinOperator.NotAny`

This query uses `JoinOperator.NotAny` to return records from the [contact](../../reference/entities/contact.md) table that are **not** referenced by the [PrimaryContactId lookup column](../../reference/entities/account.md#BKMK_PrimaryContactId) of any [account](../../reference/entities/account.md) record that has its [Name column](../../reference/entities/account.md#BKMK_Name) equal to 'Contoso'. The contact record might still be referenced by account records with _other_ `name` column values.

#### [QueryExpression](#tab/qe)

``` csharp
var query = new QueryExpression("contact")
{
      ColumnSet = new ColumnSet("fullname"),
      Criteria = new FilterExpression(filterOperator: LogicalOperator.And)
      {
         AnyAllFilterLinkEntity = new LinkEntity(
            linkFromEntityName: "contact",
            linkToEntityName: "account",
            linkFromAttributeName: "contactid",
            linkToAttributeName: "primarycontactid",
            joinOperator: JoinOperator.NotAny)
         {
            LinkCriteria = new FilterExpression(filterOperator: LogicalOperator.And)
            {
                  Conditions = {
                     new ConditionExpression(
                        attributeName: "name",
                        conditionOperator: ConditionOperator.Equal,
                        value: "Contoso")
                  }
            }
         }
      }
};
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

#### `JoinOperator.NotAll`

> [!NOTE]
> The meaning of `JoinOperator.All` and `JoinOperator.NotAll` is the opposite of what the names might imply, and they are typically used with inverted filters:
>
> - `JoinOperator.NotAll` is equivalent to `JoinOperator.Any` and returns parent records that have related table records matching the filters.
> - `JoinOperator.All` returns parent records when some related entity records with a matching `LinkFromAttributeName` column value exist but **none** of those link entity rows satisfy the additional filters defined inside of the `LinkEntity`.

This query uses `JoinOperator.NotAll` to to return records from the [contact](../../reference/entities/contact.md) table that are referenced by the [PrimaryContactId lookup column](../../reference/entities/account.md#BKMK_PrimaryContactId) of at least one [account](../../reference/entities/account.md) record that has its [Name column](../../reference/entities/account.md#BKMK_Name) equal to 'Contoso':

#### [QueryExpression](#tab/qe)

```csharp
var query = new QueryExpression("contact")
{
    ColumnSet = new ColumnSet("fullname"),
    Criteria = new FilterExpression(filterOperator: LogicalOperator.And)
    {
        AnyAllFilterLinkEntity = new LinkEntity(
            linkFromEntityName: "contact",
            linkToEntityName: "account",
            linkFromAttributeName: "contactid",
            linkToAttributeName: "primarycontactid",
            joinOperator: JoinOperator.NotAll)
        {
            LinkCriteria = new FilterExpression(filterOperator: LogicalOperator.And)
            {
                Conditions = {
                    new ConditionExpression(
                        attributeName: "name",
                        conditionOperator: ConditionOperator.Equal,
                        value: "Contoso")
                }
            }
        }
    }
};
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

#### `JoinOperator.All`

This query uses `JoinOperator.All` to return records from the [contact](../../reference/entities/contact.md) table that **are** referenced by the [PrimaryContactId lookup column](../../reference/entities/account.md#BKMK_PrimaryContactId) of **some** [account](../../reference/entities/account.md) record, but **none** of those _account_ records have their [Name column](../../reference/entities/account.md#BKMK_Name) equal to 'Contoso':

#### [QueryExpression](#tab/qe)

```csharp
var query = new QueryExpression("contact")
{
    ColumnSet = new ColumnSet("fullname"),
    Criteria = new FilterExpression(filterOperator: LogicalOperator.And)
    {
        AnyAllFilterLinkEntity = new LinkEntity(
            linkFromEntityName: "contact",
            linkToEntityName: "account",
            linkFromAttributeName: "contactid",
            linkToAttributeName: "primarycontactid",
            joinOperator: JoinOperator.All)
        {
            LinkCriteria = new FilterExpression(filterOperator: LogicalOperator.And)
            {
                Conditions = {
                    new ConditionExpression(
                        attributeName: "name",
                        conditionOperator: ConditionOperator.Equal,
                        value: "Contoso")
                }
            }
        }
    }
};
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

You can include no more than 500 total [ConditionExpression](/dotnet/api/microsoft.xrm.sdk.query.conditionexpression)  and [LinkEntity](/dotnet/api/microsoft.xrm.sdk.query.linkentity) instances in a query. Otherwise, you see this error:

> Name: `TooManyConditionsInQuery`<br />
> Code: `0x8004430C`<br />
> Number: `-2147204340`<br />
> Message: `Number of conditions in query exceeded maximum limit.`

You need to reduce the number of conditions to execute the query. You might be able to reduce the number of conditions by using the `ConditionOperator.In` that can be used with numbers, unique identifiers, and strings up to 850 characters.


## Next steps

Learn how to page results.

> [!div class="nextstepaction"]
> [Page results](page-results.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]