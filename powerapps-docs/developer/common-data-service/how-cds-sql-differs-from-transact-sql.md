---
title: "How Common Data Service SQL Differs from Transact-SQL | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn what subset of the Transact-SQL language is supported by the Common Data Service SQL endpoint." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/01/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# How Common Data Service SQL differs from Transact-SQL

This article describes the differences between Common Data Service SQL and Transact-SQL.  
  
## Inheritance and Relationships Support  

 Common Data Service SQL works directly with conceptual entity schemas and supports conceptual model features such as inheritance and relationships.  
  
 When working with inheritance, it is often useful to select instances of a subtype from a collection of supertype instances. The [oftype](oftype-entity-sql.md) operator in Common Data Service SQL (similar to `oftype` in C# Sequences) provides this capability.  
  
## Support for Collections  

 Common Data Service SQL treats collections as first-class entities. For example:  
  
- Collection expressions are valid in a `from` clause.  
  
- `in` and `exists` subqueries have been generalized to allow any collections.  
  
     A subquery is one kind of collection. `e1 in e2` and `exists(e)` are the Common Data Service SQL constructs to perform these operations.  
  
- Set operations, such as `union`, `intersect`, and `except`, now operate on collections.  
  
- Joins operate on collections.  
  
## Support for Expressions  

 Transact-SQL has subqueries (tables) and expressions (rows and columns).  
  
 To support collections and nested collections, Common Data Service SQL makes everything an expression. Common Data Service SQL is more composable than Transact-SQL—every expression can be used anywhere. Query expressions always result in collections of the projected types and can be used anywhere a collection expression is allowed. For information about Transact-SQL expressions that are not supported in Common Data Service SQL, see [Unsupported Expressions](unsupported-expressions-entity-sql.md).  
  
 The following are all valid Common Data Service SQL queries:  
  
```sql  
1+2 *3  
"abc"  
row(1 as a, 2 as b)  
{ 1, 3, 5}
e1 union all e2  
set(e1)  
```  
  
## Uniform Treatment of Subqueries  

 Given its emphasis on tables, Transact-SQL performs contextual interpretation of subqueries. For example, a subquery in the `from` clause is considered to be a multiset (table). But the same subquery used in the `select` clause is considered to be a scalar subquery. Similarly, a subquery used on the left side of an `in` operator is considered to be a scalar subquery, while the right side is expected to be a multiset subquery.  
  
 Common Data Service SQL eliminates these differences. An expression has a uniform interpretation that does not depend on the context in which it is used. Common Data Service SQL considers all subqueries to be multiset subqueries. If a scalar value is desired from the subquery, Common Data Service SQL provides the `anyelement` operator that operates on a collection (in this case, the subquery), and extracts a singleton value from the collection.  
  
### Avoiding Implicit Coercions for Subqueries  

 A related side effect of uniform treatment of subqueries is implicit conversion of subqueries to scalar values. Specifically, in Transact-SQL, a multiset of rows (with a single field) is implicitly converted into a scalar value whose data type is that of the field.  
  
 Common Data Service SQL does not support this implicit coercion. Common Data Service SQL provides the `ANYELEMENT` operator to extract a singleton value from a collection, and a `select value` clause to avoid creating a row-wrapper during a query expression.  
  
## Select Value: Avoiding the Implicit Row Wrapper  

 The select clause in a Transact-SQL subquery implicitly creates a row wrapper around the items in the clause. This implies that we cannot create collections of scalars or objects. Transact-SQL allows an implicit coercion between a `rowtype` with one field and a singleton value of the same data type.  
  
 Common Data Service SQL provides the `select value` clause to skip the implicit row construction. Only one item may be specified in a `select value` clause. When such a clause is used, no row wrapper is constructed around the items in the `select` clause, and a collection of the desired shape may be produced, for example, `select value a`.  
  
 Common Data Service SQL also provides the row constructor to construct arbitrary rows. `select` takes one or more elements in the projection and results in a data record with fields:  
  
 `select a, b, c`  
  
## Left Correlation and Aliasing  

 In Transact-SQL, expressions in a given scope (a single clause like `select` or `from`) cannot reference expressions defined earlier in the same scope. Some dialects of SQL (including Transact-SQL) do support limited forms of these in the `from` clause.  
  
 Common Data Service SQL generalizes left correlations in the `from` clause, and treats them uniformly. Expressions in the `from` clause can reference earlier definitions (definitions to the left) in the same clause without the need for additional syntax.  
  
 Common Data Service SQL also imposes additional restrictions on queries involving `group by` clauses. Expressions in the `select` clause and `having` clause of such queries may only refer to the `group by` keys via their aliases. The following construct is valid in Transact-SQL but are not in Common Data Service SQL:  
  
```sql  
SELECT t.x + t.y FROM T AS t group BY t.x + t.y
```  
  
 To do this in Common Data Service SQL:  
  
```sql  
SELET k FROM T AS t GROUP BY (t.x + t.y) AS k
```  
  
## Referencing Columns (Properties) of Tables (Collections)  

 All column references in Common Data Service SQL must be qualified with the table alias. The following construct (assuming that `a` is a valid column of table `T`) is valid in Transact-SQL but not in Common Data Service SQL.  
  
```sql  
SELECT a FROM T
```  
  
 The Common Data Service SQL form is  
  
```sql  
SELECT t.a AS A FROM T AS t
```  
  
 The table aliases are optional in the `from` clause. The name of the table is used as the implicit alias. Common Data Service SQL allows the following form as well:  
  
```sql  
SELET Tab.a FROM Tab
```  
  
## Navigation Through Objects  

 Transact-SQL uses the "." notation for referencing columns of (a row of) a table. Common Data Service SQL extends this notation (borrowed from programming languages) to support navigation through properties of an object.  
  
 For example, if `p` is an expression of type Person, the following is the Common Data Service SQL syntax for referencing the city of the address of this person.  
  
```sql  
p.Address.City
```  
  
## No Support for \*  

 Transact-SQL supports the unqualified \* syntax as an alias for the entire row, and the qualified \* syntax (t.\*) as a shortcut for the fields of that table. In addition, Transact-SQL allows for a special count(\*) aggregate, which includes nulls.  
  
 Common Data Service SQL does not support the * construct. Transact-SQL queries of the form `select * from T` and `select T1.* from T1, T2...` can be expressed in Common Data Service SQL as `select value t from T as t` and `select value t1 from T1 as t1, T2 as t2...`, respectively. Additionally, these constructs handle inheritance (value substitutability), while the `select *` variants are restricted to top-level properties of the declared type.  
  
 Common Data Service SQL does not support the `count(*)` aggregate. Use `count(0)` instead.  
  
## Changes to Group By  

 Common Data Service SQL supports aliasing of `group by` keys. Expressions in the `select` clause and `having` clause must refer to the `group by` keys via these aliases. For example, this Common Data Service SQL syntax:  
  
```sql  
SELECT k1, count(t.a), sum(t.a)
FROM T AS t
GROUP BY t.b + t.c AS k1
```  
  
 ...is equivalent to the following Transact-SQL:  
  
```sql  
SELECT b + c, count(*), sum(a)
FROM T
GROUP BY b + c
```  
  
## Collection-Based Aggregates  

 Common Data Service SQL supports two kinds of aggregates.  
  
 Collection-based aggregates operate on collections and produce the aggregated result. These can appear anywhere in the query, and do not require a `group by` clause. For example:  
  
```sql  
SELECT t.a AS a, count({1,2,3}) AS b FROM T AS t
```  
  
 Common Data Service SQL also supports SQL-style aggregates. For example:  
  
```sql  
SELECT a, sum(t.b) FROM T AS t GROUP BY t.a AS a
```  
  
## ORDER BY Clause Usage  

Transact-SQL allows `ORDER BY` clauses to be specified only in the topmost `SELECT .. FROM .. WHERE` block. In Common Data Service SQL, you can use a nested `ORDER BY` expression and it can be placed anywhere in the query, but ordering in a nested query is not preserved.  
  
```sql  
-- The following query will order the results by the last name  
SELECT C1.FirstName, C1.LastName  
        FROM AdventureWorks.Contact AS C1
        ORDER BY C1.LastName  
```  
  
```sql  
-- In the following query ordering of the nested query is ignored.  
SELECT C2.FirstName, C2.LastName  
    FROM (SELECT C1.FirstName, C1.LastName  
        FROM AdventureWorks.Contact as C1  
        ORDER BY C1.LastName) as C2  
```  
  
## Identifiers  

 In Transact-SQL, identifier comparison is based on the collation of the current database. In Common Data Service SQL, identifiers are always case insensitive and accent sensitive (that is, Common Data Service SQL distinguishes between accented and unaccented characters; for example, 'a' is not equal to 'ấ'). Common Data Service SQL treats versions of letters that appear the same but are from different code pages as different characters. For more information, see [Input Character Set](input-character-set-entity-sql.md).  
  
## Transact-SQL Functionality Not Available in Common Data Service SQL  

 The following Transact-SQL functionality is not available in Common Data Service SQL.  
  
 DML  
 Common Data Service SQL currently provides no support for DML statements (insert, update, delete).  
  
 DDL  
 Common Data Service SQL provides no support for DDL in the current version.  
  
 Imperative Programming  
 Common Data Service SQL provides no support for imperative programming, unlike Transact-SQL. Use a programming language instead.  
  
 Grouping Functions  
 Common Data Service SQL does not yet provide support for grouping functions (for example, CUBE, ROLLUP, and GROUPING_SET).  
  
 Analytic Functions  
 Common Data Service SQL does not (yet) provide support for analytic functions.  
  
 Built-in Functions, Operators  
 Common Data Service SQL supports a subset of Transact-SQL's built in functions and operators. These operators and functions are likely to be supported by the major store providers. Common Data Service SQL uses the store-specific functions declared in a provider manifest. Additionally, the Entity Framework allows you to declare built-in and user-defined existing store functions, for Common Data Service SQL to use.  
  
 Hints  
 Common Data Service SQL does not provide mechanisms for query hints.  
  
 Batching Query Results  
 Common Data Service SQL does not support batching query results. For example, the following is valid Transact-SQL (sending as a batch):  
  
```sql  
SELECT * FROM products;
SELECT * FROM catagories;
```  
  
 However, the equivalent Common Data Service SQL is not supported:  
  
```sql  
SELECT value p FROM Products AS p;
SELECT value c FROM Categories AS c;
```  
  
 Common Data Service SQL only supports one result-producing query statement per command.  
  
## See also

- [Common Data Service SQL Overview](entity-sql-overview.md)
- [Unsupported Expressions](unsupported-expressions-entity-sql.md)