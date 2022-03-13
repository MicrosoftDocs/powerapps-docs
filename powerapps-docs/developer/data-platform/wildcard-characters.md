---
title: "Use wildcard characters in conditions for string values in Microsoft Dataverse (PowerApps) | Microsoft Docs" 
description: "You can use wildcard characters when querying for conditions using string values." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 03/13/2022
ms.reviewer: "jdaly"
ms.topic: "article"
author: "mayadumesh" # GitHub ID Temp owner
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use wildcard characters in conditions for string values

You can use wildcard characters when you construct queries using conditions on string values with the following operators:

# [FetchXml](#tab/fetchxml)

`like`<br/>
`not-like`<br/>
`begins-with`<br/>
`not-begin-with`<br/>
`ends-with`<br/>
`not-end-with`<br/>


# [QueryExpression](#tab/queryexpression)

`Like`<br/>
`NotLike`<br/>
`BeginsWith`<br/>
`DoesNotBeginWith`<br/>
`EndsWith`<br/>
`DoesNotEndWith`<br/>

# [Web API](#tab/webapi)

`contains`<br/>
`not contains`<br/>
`startswith`<br/>
`not startswith`<br/>
`endswith`<br/>
`notendswith`<br/>



[!INCLUDE[footer-include](../../includes/footer-banner.md)]