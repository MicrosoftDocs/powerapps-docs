---
title: Improve FetchXML request performance | Microsoft Docs
description: "Learn how developers can improve FetchXML request performance when using Microsoft Dataverse."
author: NHelgren
manager: annbe
ms.service: powerapps
ms.topic: article
ms.date: 06/08/2021
ms.subservice: dataverse-developer
ms.author: nhelgren
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Improve FetchXML request performance

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

You can use the `LateMaterialize` option in FetchXML requests to break up such
requests into smaller, more usable segments, which can improve the performance of long-running FetchXML requests.

> [!NOTE]
> Performance improvements depend on the data distribution for each
> participating table and linked table. Late materialization might not always
> provide a performance benefit. It's best used if you're experiencing
> performance issues with your existing fetch request.

Executing a traditional fetch for a given number of the top table records will pull all
the columns in the select list that meet the filter criteria. Let's say you're
pulling the top 500 records on a table that has 100 columns and 100,000 rows
that meet the filter criteria. This request can cause issues in two ways:

- The 99,500 rows will pull all columns, even though you only need to populate
  the select list for 500 rows when returning to the client.

- The query optimizer can generate an arbitrary order when retrieving the child
  columns, resulting in a data order you don't want.

When you use `LateMaterialize`, you create a fetch that will:

- First pull only the primary ID of the top number of records specified.

- Select only the columns of data needed based on the primary IDs that were
  retrieved&mdash;for example, where only five columns are needed for display in the form.

By pulling only the needed data after the primary IDs are collected, the
retrieval is much faster because data that's not needed for the current operation is
excluded.

This is most beneficial when:

- The table you're querying has one or more links to other tables for column data.

- The table contains many columns.

- The table contains logical columns.

## Syntax

```xml
<fetch version="1.0" output-format="xml-platform" latematerialize="true"
 mapping="logical" distinct="true">

  <entity name="[entity]">​
    <attribute name="[attribute]" />
​
    <link-entity name="[entity]" from="[linked entity]" to="[linked entityid]"
                 link-type="outer" alias="[alias]">​
      <attribute name="[name of linked entity column]" />​
    </link-entity>
​
    <filter type=[filter type]>​
      <condition attribute="[column]" operator="[operator]" value="[value]"/> ​
    </filter>​
  </entity>
​
</fetch>
```

## Sample

```XML
<fetch version="1.0" output-format="xml-platform" latematerialize="true"
       mapping="logical" distinct="true">

  <entity name="account">​
    <attribute name="accountnumber" />​
    <attribute name="createdby" />​
    <attribute name="ownerid" />​

    <link-entity name="account" from="accountid" to="parentaccountid"
                 link-type="outer" alias="oaccount">​
      <attribute name="createdby" />
​
      <link-entity name="account" from="accountid" to="accountid" link-type="outer"
                 alias="oaccount1">​
        <attribute name="createdby" />​
        <attribute name="accountid" />​
        <attribute name="name" />​
      </link-entity>​
    </link-entity>​

    <link-entity name="account" from="accountid" to="accountid" link-type="outer"
                 alias="oaccount2"/>
​
    <filter type='and'>​
      <condition attribute="statecode" operator="eq" value="2"/> ​
    </filter>​
  </entity>​

</fetch>
```

## FetchXML support for query hints

Microsoft SQL Server supports a number of query hints to optimize queries. The FetchXML language
supports query hints and can pass these query options to SQL Server.

> [!IMPORTANT]
> The query hints feature is recommended to be used only by
> developers who fully understand how FetchXML is translated to SQL. This is to
> ensure that developers using this feature avoid inadvertent performance
> regression.

### Syntax

```xml
<fetch version='1.0' aggregate='true' output-format='xml - platform'
mapping='logical' options='OptimizeForUnknown,DisableRowGoal,Recompile'>

  <entity name='account'>

    <attribute name='accountid' aggregate='countcolumn' alias='countAll'/>
    <filter type='and'>
      <condition attribute='statecode' operator='eq' value='0' />
    </filter>

    <filter type='or'>
      <condition attribute='name' operator='like' value='%Test%' />
      <condition attribute='accountnumber' operator='like' value='%Test%' />
      <condition attribute='emailaddress1' operator='like' value='%Test%' />
      <condition attribute='telephone1' operator='like' value='%Test%' />
    </filter>

  </entity>
</fetch>
```

### Supported query options

The supported FetchXML query hints are listed in the following table. The table also shows the translation of FetchXML query hints into SQL Server query hints.

| FetchXML hint | SQL Server hint |
| --- | --- |
|OptimizeForUnknown | Optimize for unknown |
|ForceOrder | Force Order |
|Recompile | recompile |
|DisableRowGoal | DISABLE_OPTIMIZER_ROWGOAL |
|EnableOptimizerHotfixes | ENABLE_QUERY_OPTIMIZER_HOTFIXES' |
|LoopJoin | Loop Join |
|MergeJoin | Merge Join |
|HashJoin | Hash Join |
|NO_PERFORMANCE_SPOOL | NO_PERFORMANCE_SPOOL |
|ENABLE_HIST_AMENDMENT_FOR_ASC_KEYS | ENABLE_HIST_AMENDMENT_FOR_ASC_KEYS |

### See also

[Use FetchXML to construct a query](use-fetchxml-construct-query.md)  
[Hints (Transact-SQL) - Query](/sql/t-sql/queries/hints-transact-sql-query)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]