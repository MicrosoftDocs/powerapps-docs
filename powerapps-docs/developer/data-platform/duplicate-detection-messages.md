---
title: "Duplicate detection messages (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use the BulkDetectDuplicatesRequest or RetrieveDuplicatesRequest messages to detect duplicates." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/26/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Duplicate detection messages

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Use the messages listed in the following table to detect duplicates in Microsoft Dataverse.  


|                                                                                                                                                                                                                   Message                                                                                                                                                                                                                   |                                      Web API Operation                                       |                         SDK Assembly                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| Detects duplicates for a specified table type based on query criteria and store them as instances of a duplicate record table type in the Dataverse database.<br /><br /> The query expression that describes the records on which to run the duplicate detection job is specified in the <xref:Microsoft.Crm.Sdk.Messages.BulkDetectDuplicatesRequest.Query> property of this request. | <xref href="Microsoft.Dynamics.CRM.BulkDetectDuplicates?text=BulkDetectDuplicates Action" /> | <xref:Microsoft.Crm.Sdk.Messages.BulkDetectDuplicatesRequest> |
|                                                                                                         Detects and retrieves duplicates for a specified record.<br /><br /> The matching table type is specified in the <xref:Microsoft.Crm.Sdk.Messages.RetrieveDuplicatesRequest.MatchingEntityName> property of this request.                                                                                                          |  <xref href="Microsoft.Dynamics.CRM.RetrieveDuplicates?text=RetrieveDuplicates Function" />  |  <xref:Microsoft.Crm.Sdk.Messages.RetrieveDuplicatesRequest>  |

### See also

 [Enable and disable duplicate detection](enable-disable-duplicate-detection.md)  
 [Running duplicate detection](run-duplicate-detection.md)   
 [Duplicate rule tables](duplicaterule-entities.md)<br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]