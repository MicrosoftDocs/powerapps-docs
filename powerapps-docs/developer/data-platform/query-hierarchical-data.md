---
title: "Query hierarchical data (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how you can use the query condition operators to query tables with explicit hierarchical relationships." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/26/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Query hierarchical data

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

You can define specific self-referencing one-to-many table relationships as hierarchical. You can write queries that return related data in these hierarchies.  
  
You can take advantage of new query condition operators to query tables with explicit hierarchical relationships. These operators only apply for the table relationship specifically defined as a hierarchical relationship. You can use new condition operators to retrieve this hierarchical data when you query using <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> or <xref:Microsoft.Xrm.Sdk.Query.FetchExpression>.  
  
<a name="BKMK_ConditionOperators"></a>

## Condition operators for hierarchical data

 Use the following operators to set conditions when querying hierarchical data.  
  
|FetchXML|ConditionOperator|Description|  
|--------------|-----------------------|-----------------|  
|`above`|`Above`|Returns all records in referenced record's hierarchical ancestry line.|  
|`eq-or-above`|`AboveOrEqual`|Returns the referenced record and all records above it in the hierarchy.|  
|`under`|`Under`|Returns all child records below the referenced record in the hierarchy|  
|`eq-or-under`|`UnderOrEqual`|Returns the referenced record and all child records below it in the hierarchy|  
|`not-under`|`NotUnder`|Returns all records not below the referenced record in the hierarchy|  
|`eq-useroruserhierarchy`|`OwnedByMeOrMyReports`|When hierarchical security models are used, Equals current user or user's reporting hierarchy|  
|`eq-useroruserhierarchyandteams`|`OwnedByMeOrMyReportsAndTeams`|When hierarchical security models are used, Equals current user and user's teams, or user's reporting hierarchy and their teams|  
  
### Recursion limits when querying hierarchical data

 Because querying hierarchical data can be resource intensive, there is a default limit of 100 recursions allowed conditions for hierarchical queries using the `Above`, `AboveOrEqual`, `Under`, `UnderOrEqual`, and `NotUnder` condition operators.  
  
 `OwnedByMeOrMyReports` and `OwnedByMeOrMyReportsAndTeams` are hierarchical security condition operators that depend on the **Hierarchy Depth** setting that can be found in **Settings** > **Security** > **Hierarchy Security**. The value of this setting is stored in the `Organization.MaxDepthForHierarchicalSecurityModel` column.  
  
<a name="BKMK_ChildCountAggregate"></a>

## Retrieve the number of hierarchically related child records

 Use the `rowaggregate` column in a FetchXML based query to retrieve the number of hierarchically related child records. When this value is set to `CountChildren` a value that includes the total number of child records for the record is included in the <xref:Microsoft.Xrm.Sdk.EntityCollection>. For example, the following query will include an `AccountChildren` aggregate value representing the number of child account records in the hierarchical relationship where the `{0}` parameter represents the `AccountId` of the parent record.  
  
```xml  
<fetch distinct='false' no-lock='false' mapping='logical'>  
  <entity name='account'>  
    <attribute name='name' />  
    <attribute name='accountid' />  
    <attribute name='accountid' rowaggregate='CountChildren' alias='AccountChildren'/>  
    <filter type='and'>  
      <condition attribute='accountid' operator='under' value='{0}' />  
    </filter>  
  </entity>  
</fetch>  
  
```  
  
> [!NOTE]
> The aggregate value returned represents all the child records, including any that the user may not have access to read.  
  
### See Also

[Work with Quick Find’s search item limit](quick-find-limit.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]