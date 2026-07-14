---
title: Order rows using QueryExpression
description: Learn how to use QueryExpression to order rows when you retrieve data from Microsoft Dataverse.
ms.date: 05/12/2024
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Order rows using QueryExpression

To specify the sort order for the rows in tables, use the [QueryExpression.Orders](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.orders) or [LinkEntity.Orders](/dotnet/api/microsoft.xrm.sdk.query.linkentity.orders) properties.

> [!NOTE]
> The `Orders` property is read-only. You can set [OrderExpression](/dotnet/api/microsoft.xrm.sdk.query.orderexpression) instances to this collection using object initialization or using the [QueryExpression.AddOrder method](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.addorder). 
>
> `LinkEntity` doesn't have an `AddOrder` method. You can use [System.Collections.ObjectModel.Collection&lt;T&gt; methods](/dotnet/api/system.collections.objectmodel.collection-1#methods) the `Orders` property inherits.

The default sort order is [OrderType](/dotnet/api/microsoft.xrm.sdk.query.ordertype).`Ascending`.

The following query returns [account](../../reference/entities/account.md) records in ascending order by `createdon`, `name`, and `accountnumber` values.

```csharp
var query = new QueryExpression(entityName: "account") { 
    ColumnSet = new ColumnSet("name", "accountnumber", "createdon"),
    Orders = {
        { 
            new OrderExpression(
                attributeName: "createdon", 
                orderType: OrderType.Ascending) 
        },
        {
            new OrderExpression(
                attributeName: "name",
                orderType: OrderType.Ascending)
        },
        {
            new OrderExpression(
                attributeName: "accountnumber",
                orderType: OrderType.Ascending)
        },
    }
};
```

This same query can be composed using the [QueryExpression.AddOrder method](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.addorder):

```csharp
var query = new QueryExpression(entityName: "account") { 
    ColumnSet = new ColumnSet("name", "accountnumber", "createdon")
};
query.AddOrder(attributeName: "createdon", orderType: OrderType.Ascending);
query.AddOrder(attributeName: "name", orderType: OrderType.Ascending);
query.AddOrder(attributeName: "accountnumber", orderType: OrderType.Ascending);
```


The order of the elements determines how the ordering is applied. To have ordering applied using `accountnumber`, add that order first:

```csharp
query.AddOrder(attributeName: "accountnumber", orderType: OrderType.Ascending);
query.AddOrder(attributeName: "createdon", orderType: OrderType.Ascending);
query.AddOrder(attributeName: "name", orderType: OrderType.Ascending);
```


## Descending order

If you want to use *descending* order, use `OrderType.Descending`. The following example returns account records with the most recently created records at the top.

```csharp
var query = new QueryExpression(entityName: "account") { 
    ColumnSet = new ColumnSet("name", "createdon")
};
query.AddOrder(attributeName: "createdon", orderType: OrderType.Descending);
```

## Process LinkEntity orders first

Dataverse always orders columns specified by [LinkEntity.Orders](/dotnet/api/microsoft.xrm.sdk.query.linkentity.orders) after [QueryExpression.Orders](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.orders).

The following example shows a conventional ordering pattern for both `LinkEntity` and `QueryExpression` columns.

```csharp
var query = new QueryExpression(entityName: "account")
{
    ColumnSet = new ColumnSet("name", "accountnumber", "createdon"),
    LinkEntities = {
        new LinkEntity(
            linkFromEntityName:"account",
            linkToEntityName:"account",
            linkFromAttributeName: "parentaccountid",
            linkToAttributeName:"accountid",
            joinOperator: JoinOperator.Inner){
             EntityAlias = "parentaccount",
             Columns = new ColumnSet("name"),
             Orders = {
                {
                    new OrderExpression(
                        attributeName:"name",
                        orderType: OrderType.Ascending)
                }
            }
        }
    },
    Orders = {
                {
                    new OrderExpression(
                        attributeName:"name",
                        orderType: OrderType.Ascending)
                }
    }
};
```

In this case, the results are ordered using following attributes:

- First => `account.name`
- Last => `parentaccountname.name`


To ensure the `LinkEntity` order is applied first, move the `OrderExpression` from the `LinkEntity.Orders` to the `QueryExpression.Orders` above the other `OrderExpression`, and use the [OrderExpression.EntityName](/dotnet/api/microsoft.xrm.sdk.query.orderexpression.entityname) to refer to the [LinkEntity.EntityAlias](/dotnet/api/microsoft.xrm.sdk.query.linkentity.entityalias) value.


```csharp
var query = new QueryExpression(entityName: "account")
{
    ColumnSet = new ColumnSet("name", "accountnumber", "createdon"),
    LinkEntities = {
        new LinkEntity(
            linkFromEntityName:"account",
            linkToEntityName:"account",
            linkFromAttributeName: "parentaccountid",
            linkToAttributeName:"accountid",
            joinOperator: JoinOperator.Inner){
             EntityAlias = "parentaccount",
             Columns = new ColumnSet("name")
        }
    },
    Orders = {
                {
                    new OrderExpression(
                        attributeName:"name",
                        orderType: OrderType.Ascending){
                        // LinkEntity.EntityAlias value
                        EntityName = "parentaccount"
                    }
                },
                {
                    new OrderExpression(
                        // QueryExpression Columns name
                        attributeName:"name",
                        orderType: OrderType.Ascending)
                }
    }
};
```

Now, the results are ordered using the following attributes:

- First => `parentaccount.name`
- Last => `account.name`

## Ordering lookup and choice columns

The data contained by most column types is relatively simple and you can perform sorting operations that make sense. Lookup and choice columns are more complex because the data stored in the database isn't meaningful out of context.

### Lookup Columns

When you order using lookup columns, the results are sorted using the primary name field for the related table. The database stores a GUID value. The [formatted value](../entity-operations-query-data.md#formatted-values-are-returned-for-some-columns) returned is the corresponding primary name field.

### Choice Columns

Choice column values are also sorted using the [formatted value](../entity-operations-query-data.md#formatted-values-are-returned-for-some-columns) rather than the values stored in the database. Data for these columns are stored as integers. The formatted value is a localized label based on the user's language.

> [!NOTE]
> Since choice sorting is based on the localized label of the users's language, expect different ordering for the results set if the user's language differs.

<!-- ## Ordering and paging -->
[!INCLUDE [cc-ordering-paging](../../includes/cc-ordering-paging.md)]

## Next steps

Learn how to filter rows.

> [!div class="nextstepaction"]
> [Filter rows](filter-rows.md)
