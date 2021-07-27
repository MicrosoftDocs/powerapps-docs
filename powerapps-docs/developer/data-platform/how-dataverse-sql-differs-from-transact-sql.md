---
title: "How Dataverse SQL Differs from Transact-SQL | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn what subset of the Transact-SQL language is supported by the Dataverse SQL endpoint." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 12/16/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# How Dataverse SQL differs from Transact-SQL (Preview)

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This article describes the differences between Dataverse SQL and Transact-SQL. Dataverse SQL is a subset of Transact-SQL.

## Data types

In a SQL database, each column, local variable, expression, and parameter has a related data type. A data type is an attribute that specifies the type of data that the object can hold: integer data, character data, monetary data, date and time data, binary strings, and so on.

More information: [Data types (Transact-SQL)](/sql/t-sql/data-types/data-types-transact-sql)

### [Supported](#tab/supported)

- bigint
- bit
- char
- datetime
- decimal
- float
- int
- money
- nchar
- numeric
- nvarchar*
- real
- smalldatetime
- smallint
- smallmoney
- tinyint
- uniqueidentifier
- varchar*
- picklist
- lookup
- primarykey
- customer
- owner
- state
- status
- multiselectpicklist

### [Not supported](#tab/not-supported)

- binary
- image
- ntext
- nvarchar(max)
- sql_variant
- text
- timestamp
- varbinary
- varchar(max)
- virtual
- partylist
- HierarchyId
- managedproperty
- file
- xml

---

## Statements

A SQL statement is an atomic unit of work and either completely succeeds or completely fails. A SQL statement is a set of instruction that consists of identifiers, parameters, variables, names, data types, and SQL reserved words that compiles successfully. 

More information: [Transact-SQL statements](/sql/t-sql/statements/statements)

### [Supported](#tab/supported)

- DQL
  - SELECT column
  - SELECT expression
  - SELECT STAR
  - SELECT distinct
  - SELECT TOP
  - SELECT SET Variable
  - All JOIN types
  - All WHERE conditions
  - All nested queries (SELECT, FROM, WHERE)
  - Union
  - [GROUP BY](#select-group-by)/Having
- General
  - IF THEN ELSE
  - DECLARE variable

### [Not supported](#tab/not-supported)

- DDL
- DML
- TCL
- SCS
- DCL
- Stored Procedure
- DQL
  - Pivot
  - DQL XML function
  - DQL JSON function
  - CUBE and ROLLUP
  - Duplicate columns
  - Without unique column name and alias
- General
  - WHILE LOOP

---

## Functions

Learn about the categories of built-in functions you can use with Dataverse environments through the SQL endpoint.

More information: [What are the SQL database functions?](/sql/t-sql/functions/functions)

### [Supported](#tab/supported)

- Aggregate
- Collation
- Configuration
- Conversion
- Data type
  - DATALENGTH
- Date & time
- Mathematical
- Logical
- [Metadata](#metadata-functions)
- String
- [System](#system-functions)

### [Not supported](#tab/not-supported)

- ODBC Scalar
- Analytic
- Cryptographic
- Cursor
- Data type
  - IDENT_CURRENT
  - IDENT_INCR
  - IDENT_SEED
  - IDENTITY(Function)
  - SQL_VARIANT_PROPERTY
- JSON
- Ranking
- Replication
- Rowset
- Security
- System Statistical
- Text & Image
- Trigger

---

### System functions

The following system functions perform operations on and return information about values, objects, and settings in the Dataverse environment.

More information: [System Functions (Transact-SQL)](/sql/t-sql/functions/system-functions-transact-sql)

#### [Supported](#tab/supported)

- @@ROWCOUNT
- FORMATMESSAGE
- GETANSINULL
- ISNULL
- ISNUMERIC
- NEWID
- NEWSEQUENTIALID
- ROWCOUNT_BIG

#### [Not supported](#tab/not-supported)

- $PARTITION
- @@ERROR
- @@IDENTITY
- @@PACK_RECEIVED
- @@TRANCOUNT
- BINARY_CHECKSUM
- CHECKSUM
- CONNECTIONPROPERTY
- CONTEXT_INFO
- CURRENT_REQUEST_ID
- CURRENT_TRANSACTION_ID
- DECOMPRESS
- ERROR_LINE
- ERROR_MESSAGE
- ERROR_NUMBER
- ERROR_PROCEDURE
- ERROR_SEVERITY
- ERROR_STATE
- GET_FILESTREAM_TRANSACTION_CONTEXT
- HOST_ID
- HOST_NAME
- MIN_ACTIVE_ROWVERSION
- SESSION_CONTEXT
- SESSION_ID
- XACT_STATE

---

### Metadata functions

The following scalar functions return information about the environment and environment objects.

More information: [Metadata Functions (Transact-SQL)](/sql/t-sql/functions/metadata-functions-transact-sql)

#### [Supported](#tab/supported)

No metadata functions are supported at this time.

#### [Not supported](#tab/not-supported)

- @@PROCID
- APP_NAME
- APPLOCK_MODE
- APPLOCK_TEST
- ASSEMBLYPROPERTY
- COL_LENGTH
- COL_NAME
- COLUMNPROPERTY
- DATABASEPROPERTYEX
- DB_ID
- DB_NAME
- FILE_ID
- FILE_IDEX
- FILE_NAME
- FILEGROUP_ID
- FILEGROUP_NAME
- FILEGROUPPROPERTY
- FILEPROPERTY
- FULLTEXTCATALOGPROPERTY
- FULLTEXTSERVICEPROPERTY
- INDEX_COL  
- INDEXKEY_PROPERTY  
- INDEXPROPERTY  
- NEXT VALUE FOR
- OBJECT_DEFINITION
- OBJECT_ID
- OBJECT_NAME
- OBJECT_SCHEMA_NAME
- OBJECTPROPERTY
- OBJECTPROPERTYEX
- ORIGINAL_DB_NAME
- PARSENAME
- SCHEMA_ID
- SCHEMA_NAME
- SCOPE_IDENTITY
- SERVERPROPERTY
- STATS_DATE
- TYPE_ID
- TYPE_NAME
- TYPEPROPERTY
- VERSION

---

## Language elements

The Dataverse SQL endpoint supports the following language elements.

More information: [Language Elements (Transact-SQL)](/sql/t-sql/language-elements/language-elements-transact-sql)

### [Supported](#tab/supported)

- Expressions
- [General](#language-elements-general)
- Variables

### [Not supported](#tab/not-supported)

- Control-of-Flow
- Transactions

---

### Language elements General

#### [Supported](#tab/supported)

- [Reserved Keywords](/sql/t-sql/language-elements/reserved-keywords-transact-sql)
- [Syntax Conventions](/sql/t-sql/language-elements/transact-sql-syntax-conventions-transact-sql)
- -- (Comment)
- Slash Star (Block Comment)
- NULL and UNKNOWN
- Backslash (Line Continuation)
- GO

#### [Not supported](#tab/not-supported)

- EXECUTE
- PRINT
- RAISERROR
- CHECKPOINT
- KILL
- KILL QUERY NOTIFICATION SUBSCRIPTION
- KILL STATS JOB
- RECONFIGURE
- SHUTDOWN
- USE

---

## Queries

Use these statements to query data from the Dataverse SQL endpoint.

More information: [Queries](/sql/t-sql/queries/queries)

### General

#### [Supported](#tab/supported)

- Search Condition
- TOP

#### [Not supported](#tab/not-supported)

- AT TIME ZONE
- OPTION Clause
- OUTPUT Clause
- PREDICT
- READTEXT
- Table Value Constructor
- UPDATETEXT
- WITH common_table_expression
- WRITETEXT

---

### SELECT

Retrieves rows from a Dataverse environment and enables the selection of one or many rows or columns from one or many tables.

#### [Supported](#tab/supported)

- General (SELECT and SELECT Clause)
- [GROUP BY](#select-group-by)
- HAVING
- ORDER BY

#### [Not supported](#tab/not-supported)

- FOR
- INTO
- OVER

---

#### SELECT GROUP BY

##### [Supported](#tab/supported)

- GROUP BY column-expression [ ,...n ]

##### [Not supported](#tab/not-supported)

- GROUP BY ROLLUP
- GROUP BY CUBE ( )
- GROUP BY GROUPING SETS ( )
- GROUP BY ()
- GROUP BY [ ALL ] column-expression [ ,...n ]
- WITH (DISTRIBUTED_AGG)

---

### FROM plus JOIN, APPLY, PIVOT

#### [Supported](#tab/supported)

- JOIN
- APPLY

#### [Not supported](#tab/not-supported)

- PIVOT
- UNPIVOT

---

### WHERE

#### [Supported](#tab/supported)

- WHERE
- MATCH

#### [Not supported](#tab/not-supported)

---

### Hints

Hints are not supported.

### Predicates

#### [Supported](#tab/supported)

- CONTAINS
- IS NULL

#### [Not supported](#tab/not-supported)

- FREETEXT

---

### See also

[Use SQL to query data](dataverse-sql-query.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]