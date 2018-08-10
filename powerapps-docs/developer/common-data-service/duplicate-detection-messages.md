---
title: "Duplicate detection messages (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use the BulkDetectDuplicatesRequest or RetrieveDuplicatesRequest messages to detect duplicates." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Duplicate detection messages

Use the messages listed in the following table to detect duplicates in Common Data Service for Apps.  


|                                                                                                                                                                                                                   Message                                                                                                                                                                                                                   |                                      Web API Operation                                       |                         SDK Assembly                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| Detects duplicates for a specified entity type based on query criteria and store them as instances of a duplicate record entity type in the CDS for Apps database.<br /><br /> The query expression that describes the records on which to run the duplicate detection job is specified in the <xref:Microsoft.Crm.Sdk.Messages.BulkDetectDuplicatesRequest.Query> property of this request. | <xref href="Microsoft.Dynamics.CRM.BulkDetectDuplicates?text=BulkDetectDuplicates Action" /> | <xref:Microsoft.Crm.Sdk.Messages.BulkDetectDuplicatesRequest> |
|                                                                                                         Detects and retrieves duplicates for a specified record.<br /><br /> The matching entity type is specified in the <xref:Microsoft.Crm.Sdk.Messages.RetrieveDuplicatesRequest.MatchingEntityName> property of this request.                                                                                                          |  <xref href="Microsoft.Dynamics.CRM.RetrieveDuplicates?text=RetrieveDuplicates Function" />  |  <xref:Microsoft.Crm.Sdk.Messages.RetrieveDuplicatesRequest>  |

### See also  
 [Enable and disable duplicate detection](enable-disable-duplicate-detection.md)  
 [Running Duplicate Detection](run-duplicate-detection.md)   
 [Duplicate Rule entities](duplicaterule-entities.md)<br />
