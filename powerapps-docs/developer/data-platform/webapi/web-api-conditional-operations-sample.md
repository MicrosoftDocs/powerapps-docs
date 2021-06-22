---
title: "Web API Conditional Operations Sample (Microsoft Dataverse)| Microsoft Docs"
description: "This collection of samples demonstrate how to perform operations that are conditionally based upon the version of the table row contained on the Microsoft Dataverse server and/or currently maintained by the client."
ms.custom: ""
ms.date: 06/17/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: f2e5d22b-93fe-43b7-af15-3e281f3b3084
caps.latest.revision: 13
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Web API Conditional Operations Sample

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This collection of samples demonstrate how to perform operations that are conditionally based upon the version of the table row contained on the Microsoft Dataverse server and/or currently maintained by the client. For more information, see [Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md). This sample is implemented as a separate project for the following languages:  
  
 [Web API Conditional Operations Sample (C#)](samples/cdswebapiservice-conditional-operations.md)  
 
 The Dataverse Web API follows the conventions of the [OData v4.0](https://www.odata.org/documentation/) protocol, which uses [ETags](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part1-protocol/odata-v4.0-errata03-os-part1-protocol-complete.html#_Toc453752236) to implement resource version control. Web API conditional operations depend upon this versioning  mechanism.  
  
 This topic explains the structure and content of the samples at a higher, language-neutral level. It details the HTTP requests and responses, and the associated program output, where applicable. Review the linked sample topics above to obtain language-specific implementations and related details about how to perform the operations described in this topic.  
  
## Demonstrates

 This sample is divided into three principal sections, listed in the following table.   Each section contains a set of related Web API operations which are discussed in greater detail in the associated conceptual section of the topic [Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md) .  
  
|Code section|Associated conceptual topics|  
|------------------|----------------------------------|  
|[Conditional GET](#bkmk_conditionalGet)|[Conditional retrievals](perform-conditional-operations-using-web-api.md#bkmk_DetectIfChanged)|  
|[Optimistic concurrency on delete and update](#bkmk_optimisiticConcurrency)|[Apply optimistic concurrency](perform-conditional-operations-using-web-api.md#bkmk_Applyoptimisticconcurrency)|  
|[Controlling upsert operations](#bkmk_controllingUpsert)|[Limit upsert operations](perform-conditional-operations-using-web-api.md#bkmk_limitUpsertOperations)|  
  
 The following sections contain a brief discussion of the Dataverse Web API operations performed, along with the corresponding HTTP messages and associated console output which is the same for each language implementation. For brevity, less pertinent HTTP headers have been omitted. The URIs of the table rows will vary with the base organization address and the ID of the row assigned by your Dataverse server.  
  
<a name="bkmk_sampleData"></a>
   
## Sample data

 The sample creates the following table row before the principal code sections are executed.  
  
|Entity type|Client-assigned properties|Server-assigned properties|  
|-----------------|---------------------------------|---------------------------------|  
|<xref:Microsoft.Dynamics.CRM.account>|Name: `Contoso Ltd.` <br />Revenue: `5000000`<br />Telephone: `555-0000`<br />Description: `Parent company of Contoso Pharmaceuticals, etc.`|ID:  `14e151db-9b4f-e611-80e0-00155da84c08`<br />Initial Etag:  `W/"628448"`|  
  
<a name="bkmk_conditionalGet"></a>

## Conditional GET

 This section of the program demonstrates how to perform conditional retrievals in order to optimize network bandwidth and server processing while still maintaining the most current row state on the client. More information:[Conditional retrievals](perform-conditional-operations-using-web-api.md#bkmk_DetectIfChanged)  
  
1.  Attempt to retrieve the account `Contoso Ltd.` only if it does *not* match the current version, identified by the initial ETag value that was returned when the account row was created. This condition is represented by the `If-None-Match` header.  
  
 **Request**  
  
   ```http  
   GET https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08)?$select=name,revenue,telephone1,description HTTP/1.1  
   If-None-Match: W/"628448"  
   OData-MaxVersion: 4.0  
   OData-Version: 4.0  
   Accept: application/json  

   ```  
  
 **Response**  
  
   ```http  
   HTTP/1.1 304 Not Modified  
   ```  
  
 **Console output**  
  
   ```  
   Instance retrieved using ETag: W/"628448"  
   Expected outcome: Entity was not modified so nothing was returned.  
   ```  

   The response value, `304 Not Modified`, indicates that the current table row is the most current, so the server does *not* return the requested row in the response body.  
  
2.  Update the account by modifying its primary telephone number property.  
  
 **Request**  
  
   ```http
   PUT https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08)/telephone1 HTTP/1.1  
   OData-MaxVersion: 4.0  
   OData-Version: 4.0  
   Accept: application/json  
   Content-Type: application/json  
   {  
      "value": "555-0001"  
   }  
   ```  
  
 **Response**  
  
   ```http
   HTTP/1.1 204 No Content  
   ```  
  
 **Console output**  
  
   ```  
   Account telephone number updated.  
   ```  
  
3.  Re-attempt the same conditional GET operation, again using the original ETag value. This time the operation returns the requested data because the version on the server is different (and newer) than the version identified in the request. As in all table row retrievals, the response includes an ETag header that identifies the current version.  
  
 **Request**  
  
   ```http
   GET https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08)?$select=name,revenue,telephone1,description HTTP/1.1  
   If-None-Match: W/"628448"  
   OData-MaxVersion: 4.0  
   OData-Version: 4.0  
   Accept: application/json  
   ```  
  
 **Response**  
  
   ```http
   HTTP/1.1 200 OK  
   Content-Type: application/json; odata.metadata=minimal  
   ETag: W/"628460"  
   {  
      "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,revenue,telephone1,description)/$entity",  
      "@odata.etag":"W/\"628460\"",  
      "name":"Contoso Ltd",  
      "revenue":5000000.0000,  
      "telephone1":"555-0001",  
      "description":"Parent company of Contoso Pharmaceuticals, etc.",  
      "accountid":"14e151db-9b4f-e611-80e0-00155da84c08",  
      "_transactioncurrencyid_value":"0d4ed62e-95f7-e511-80d1-00155da84c03"  
   }  
   ```  
  
 **Console output**  
  
   ```
   Instance retrieved using ETag: W/"628448"  
   {  
      "@odata.context": "https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,revenue,telephone1,description)/$entity",  
      "@odata.etag": "W/\"628460\"",  
      "name": "Contoso Ltd",  
      "revenue": 5000000.0,  
      "telephone1": "555-0001",  
      "description": "Parent company of Contoso Pharmaceuticals, etc.",  
      "accountid": "14e151db-9b4f-e611-80e0-00155da84c08",  
      "_transactioncurrencyid_value": "0d4ed62e-95f7-e511-80d1-00155da84c03"  
   }  
  
   ```  
  
<a name="bkmk_optimisiticConcurrency"></a>
  
## Optimistic concurrency on delete and update
 
 This section of the program demonstrates how to perform conditional delete and update operations.  The most common use for such operations is in implementing an optimistic concurrency approach to row processing in a multi-user environment. More information:[Apply optimistic concurrency](perform-conditional-operations-using-web-api.md#bkmk_Applyoptimisticconcurrency)  
  
1.  Attempt to delete original account if and only if it matches the original version (ETag value).  This condition is represented by the `If-Match` header.  This operation fails because the account row was updated in the previous section, so as a result, its version was updated on the server.  
  
 **Request**  
  
   ```http
   DELETE https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08) HTTP/1.1  
   If-Match: W/"628448"  
   OData-MaxVersion: 4.0  
   OData-Version: 4.0  
   Accept: application/json  
   ```  
  
 **Response**  
  
   ```http  
    HTTP/1.1 412 Precondition Failed  
    Content-Type: application/json; odata.metadata=minimal  
    OData-Version: 4.0  
    {  
      "error":{  
        "code":"","message":"The version of the existing record doesn't match the RowVersion property provided.", . . .  
        }  
    }  
   ```  
  
 **Console output**  
  
   ```  
   Expected Error: The version of the existing record doesn't match the property provided.  
         Account not deleted using ETag 'W/"628448"', status code: '412'.  
   ```  
  
2.  Attempt to update the account if and only if it matches the original ETag value.  Again, this condition is represented by the `If-Match` header and the operation fails for the same reason.  
  
 **Request**  
  
   ```http  
    PATCH https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08) HTTP/1.1  
    If-Match: W/"628448"  
    OData-MaxVersion: 4.0  
    OData-Version: 4.0  
    Accept: application/json  
    Content-Type: application/json; charset=utf-8  
    {  
      "telephone1": "555-0002",  
      "revenue": 6000000  
    }    
   ```  
  
 **Response**  
  
   ```http  
    HTTP/1.1 412 Precondition Failed  
    Content-Type: application/json; odata.metadata=minimal  
    OData-Version: 4.0  
    {  
      "error":{  
        "code":"","message":"The version of the existing record doesn't match the RowVersion property provided.", . . .   
      }  
    }    
   ```  
  
 **Console output**  
  
   ```  
    Expected Error: The version of the existing record doesn't match the property provided.  
            Account not updated using ETag 'W/"628448"', status code: '412'.  
   ```  
  
3.  Re-attempt an update, but instead use the current ETag value obtained from the last row retrieval in the previous section.  
  
 **Request**  
  
   ```http
    PATCH https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08) HTTP/1.1  
    If-Match: W/"628460"  
    OData-MaxVersion: 4.0  
    OData-Version: 4.0  
    Accept: application/json  
    {  
      "telephone1": "555-0003",  
      "revenue": 6000000  
    }  
   ```  
  
 **Response**  
  
   ```http
    HTTP/1.1 204 No Content  
   ```  
  
 **Console output**  
  
   ```  
    Account successfully updated using ETag: W/"628460", status code: '204'.  
   ```  
  
4.  Confirm the update succeeded by retrieving and outputting the current account state.  This uses a basic GET request.  
  
 **Request**  
  
   ```http 
    GET https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08)?$select=name,revenue,telephone1,description HTTP/1.1  
    OData-MaxVersion: 4.0  
    OData-Version: 4.0  
    Accept: application/json  
   ```  
  
 **Response**  
  
   ```http
    HTTP/1.1 200 OK  
    Content-Type: application/json; odata.metadata=minimal  
    ETag: W/"628461"  
    OData-Version: 4.0  
    {  
      "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,revenue,telephone1,description)/$entity",  
      "@odata.etag":"W/\"628461\"",  
      "name":"Contoso Ltd",  
      "revenue":6000000.0000,  
      "telephone1":"555-0003",  
      "description":"Parent company of Contoso Pharmaceuticals, etc.",  
      "accountid":"14e151db-9b4f-e611-80e0-00155da84c08",  
      "_transactioncurrencyid_value":"0d4ed62e-95f7-e511-80d1-00155da84c03"  
    }  
   ```  
  
 **Console output**  
  
   ```
    {  
      "@odata.context": "https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,revenue,telephone1,description)/$entity",  
      "@odata.etag": "W/\"628461\"",  
      "name": "Contoso Ltd",  
      "revenue": 6000000.0,  
      "telephone1": "555-0003",  
      "description": "Parent company of Contoso Pharmaceuticals, etc.",  
      "accountid": "14e151db-9b4f-e611-80e0-00155da84c08",  
      "_transactioncurrencyid_value": "0d4ed62e-95f7-e511-80d1-00155da84c03"  
    }  
   ```  
  
<a name="bkmk_controllingUpsert"></a>

## Controlling upsert operations

 This section of the program demonstrates how to perform conditional `PATCH` operations, limiting upsert operations to perform as either update-only or insert-only operations. More information:[Limit upsert operations](perform-conditional-operations-using-web-api.md#bkmk_limitUpsertOperations)  
  
1.  Attempt to insert, without updating, the primary telephone and revenue properties for this account. The `If-None-Match` header with the value of  `*` represents this upsert condition. This operation fails because this account row still exists on the server (unless it was concurrently deleted by another user or process).  
  
 **Request**  
  
   ```http
    PATCH https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08) HTTP/1.1  
    If-None-Match: *  
    OData-MaxVersion: 4.0  
    OData-Version: 4.0  
    Accept: application/json  
    Content-Type: application/json; charset=utf-8  
    {  
      "telephone1": "555-0004",  
      "revenue": 7500000  
    }  
   ```  
  
 **Response**  
  
   ```http
    HTTP/1.1 412 Precondition Failed  
    Content-Type: application/json; odata.metadata=minimal  
    OData-Version: 4.0  
    {  
      "error":{  
        "code":"","message":"A record with matching key values already exists.", . . .  
      }  
    }  
   ```  
  
 **Console output**  
  
   ```   
    Expected Error: A record with matching key values already exists.  
            Account not updated using ETag 'W/"628448", status code: '412'.    
   ```  
  
2.  Attempt to perform the same update operation without creation. To accomplish this, the conditional `If-Match` header is used with a value of `*`.  This operation succeeds because the row exists on the server.  
  
 **Request**  
  
   ```http
    PATCH https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08) HTTP/1.1  
    If-Match: *  
    OData-MaxVersion: 4.0  
    OData-Version: 4.0  
    Accept: application/json  
    Content-Type: application/json; charset=utf-8  
    {  
      "telephone1": "555-0005",  
      "revenue": 7500000  
    }  
   ```  
  
 **Response**  
  
   ```http
    HTTP/1.1 204 No Content  
   ```  
  
 **Console output**  
  
   ```  
    Account updated using If-Match '*'  
   ```  
  
3.  Retrieve and output the current account state with a basic `GET` request. Note that the returned ETag value has changed to reflect the new, updated version of the account row.  
  
 **Request**  
  
   ```http  
    GET https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08)?$select=name,revenue,telephone1,description HTTP/1.1  
    OData-MaxVersion: 4.0  
    OData-Version: 4.0  
    Accept: application/json    
   ```  
  
 **Response**  
  
   ```http  
    HTTP/1.1 200 OK  
    Content-Type: application/json; odata.metadata=minimal  
    ETag: W/"628463"  
    OData-Version: 4.0  
    {  
      "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,revenue,telephone1,description)/$entity",  
      "@odata.etag":"W/\"628463\"",  
      "name":"Contoso Ltd","revenue":7500000.0000,  
      "telephone1":"555-0005",  
      "description":"Parent company of Contoso Pharmaceuticals, etc.",  
      "accountid":"14e151db-9b4f-e611-80e0-00155da84c08",  
      "_transactioncurrencyid_value":"0d4ed62e-95f7-e511-80d1-00155da84c03"  
    }    
   ```  
  
 **Console output**  
  
   ```http    
    {  
      "@odata.context": "https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,revenue,telephone1,description)/$entity",  
      "@odata.etag": "W/\"628463\"",  
      "name": "Contoso Ltd",  
      "revenue": 7500000.0,  
      "telephone1": "555-0005",  
      "description": "Parent company of Contoso Pharmaceuticals, etc.",  
      "accountid": "14e151db-9b4f-e611-80e0-00155da84c08",  
      "_transactioncurrencyid_value": "0d4ed62e-95f7-e511-80d1-00155da84c03"  
    }    
   ```  
  
4.  Delete the account with a basic `DELETE`.  
  
 **Request**  
  
   ```http    
    DELETE https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08) HTTP/1.1  
    OData-MaxVersion: 4.0  
    OData-Version: 4.0  
    Accept: application/json    
   ```  
  
 **Response**  
  
   ```http
    HTTP/1.1 204 No Content  
   ```  
  
 **Console output**  
  
   ```  
    Account was deleted.  
   ```  
  
5.  Just as in step 2, attempt to update the account if it exists.  Again, this condition is represented by the `If-Match` header with a value of `*`.  This operation fails because this table row was just deleted. However, if this `If-Match` header was absent, then the resulting basic upsert operation should successfully create a new row.  
  
 **Request**  
  
   ```http  
    PATCH https://[Organization URI]/api/data/v9.0/accounts(14e151db-9b4f-e611-80e0-00155da84c08) HTTP/1.1  
    If-Match: *  
    OData-MaxVersion: 4.0  
    OData-Version: 4.0  
    Accept: application/json  
    Content-Type: application/json; charset=utf-8  
    {  
      "telephone1": "555-0006",  
      "revenue": 7500000  
    }    
   ```  
  
 **Response**  
  
   ```http    
    HTTP/1.1 404 Not Found  
    Content-Type: application/json; odata.metadata=minimal  
    OData-Version: 4.0  
    {  
      "error":{  
        "code":"","message":"account With Id = 14e151db-9b4f-e611-80e0-00155da84c08 Does Not Exist", . . .  
      }  
    }    
   ```  
  
 **Console output**  
  
   ```    
    Expected Error: Account with Id = 14e151db-9b4f-e611-80e0-00155da84c08 does not exist.  
    Account not updated because it does not exist, status code: '404'.    
   ```  
  
 There is no need to cleanup sample data because the one account row was already deleted in step 4.  
  
### See also

[Use the Dataverse Web API](overview.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)<br />
[Web API Conditional Operations Sample (C#)](samples/cdswebapiservice-conditional-operations.md)   

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]