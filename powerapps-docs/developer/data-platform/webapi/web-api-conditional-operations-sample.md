---
title: "Web API Conditional Operations Sample (Microsoft Dataverse)| Microsoft Docs"
description: "This collection of samples demonstrate how to perform operations that are conditionally based upon the version of the table row contained on the Microsoft Dataverse server and/or currently maintained by the client."
ms.date: 09/02/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API Conditional Operations Sample

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This collection of samples demonstrate how to perform operations that are conditionally based upon the version of the table row contained on the Microsoft Dataverse server and/or currently maintained by the client. For more information, see [Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md). This sample is implemented as a separate project for the following languages:  
  
- [Web API Conditional Operations Sample (C#)](samples/webapiservice-conditional-operations.md)
- [Web API Conditional Operations Sample (Client-side JavaScript)](samples/conditional-operations-client-side-javascript.md)
 
The Dataverse Web API follows the conventions of the [OData v4.0](https://www.odata.org/documentation/) protocol, which uses [ETags](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part1-protocol/odata-v4.0-errata03-os-part1-protocol-complete.html#_Toc453752236) to implement resource version control. Web API conditional operations depend upon this versioning  mechanism.  
  
This topic explains the structure and content of the samples at a higher, language-neutral level. It details the HTTP requests and responses, and the associated program output, where applicable. Review the linked sample topics above to obtain language-specific implementations and related details about how to perform the operations described in this topic.  
  
## Demonstrates

This sample is divided into three principal sections, listed in the following table.   Each section contains a set of related Web API operations which are discussed in greater detail in the associated conceptual section of the topic [Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md) .  
  
|Code section|Associated conceptual topics|  
|------------------|----------------------------------|  
|[Section 0: Create sample records](#section-0-create-sample-records)|[Create a table row using the Web API](create-entity-web-api.md)|
|[Section 1: Conditional GET](#section-1-conditional-get)|[Conditional retrievals](perform-conditional-operations-using-web-api.md#conditional-retrievals)|
|[Section 2: Optimistic concurrency on delete and update](#section-2-optimistic-concurrency-on-delete-and-update)|[Apply optimistic concurrency](perform-conditional-operations-using-web-api.md#bkmk_Applyoptimisticconcurrency)<br />[Limit upsert operations](perform-conditional-operations-using-web-api.md#bkmk_limitUpsertOperations)|
|[Section 3: Delete sample records](#section-3-delete-sample-records)|[Basic delete](update-delete-entities-using-web-api.md#basic-delete)<br />[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)|
  
The following sections contain a brief discussion of the Dataverse Web API operations performed, along with the corresponding HTTP messages and associated console output which is the same for each language implementation. For brevity, less pertinent HTTP headers have been omitted. The URIs of the table rows will vary with the base organization address and the ID of the row assigned by your Dataverse server.  
  
<a name="bkmk_sampleData"></a>
   
## Section 0: Create sample records

The sample creates the following table row before the principal code sections are executed.  

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/accounts?$select=name,revenue,telephone1,description HTTP/1.1
Prefer: return=representation
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "name": "Contoso Ltd",
  "telephone1": "555-0000",
  "revenue": 5000000,
  "description": "Parent company of Contoso Pharmaceuticals, etc."
}
```

**Response:**

```http
HTTP/1.1 201 Created
Preference-Applied: return=representation
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,revenue,telephone1,description)/$entity",
  "@odata.etag": "W/\"72965013\"",
  "name": "Contoso Ltd",
  "revenue": 5000000.0,
  "telephone1": "555-0000",
  "description": "Parent company of Contoso Pharmaceuticals, etc.",
  "accountid": "59d88f5e-6629-ed11-9db1-0022482746b6",
  "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1"
}
```
  
**Console output:**

```
Created and retrieved the initial account, shown below:
{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,revenue,telephone1,description)/$entity",
  "@odata.etag": "W/\"72965013\"",
  "name": "Contoso Ltd",
  "revenue": 5000000.0,
  "telephone1": "555-0000",
  "description": "Parent company of Contoso Pharmaceuticals, etc.",
  "accountid": "59d88f5e-6629-ed11-9db1-0022482746b6",
  "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1"
}
```
  
<a name="bkmk_conditionalGet"></a>

## Section 1: Conditional GET

This section of the program demonstrates how to perform conditional retrievals in order to optimize network bandwidth and server processing while still maintaining the most current row state on the client. More information: [Conditional retrievals](perform-conditional-operations-using-web-api.md#bkmk_DetectIfChanged)  
  
1. Attempt to retrieve the account `Contoso Ltd.` only if it does *not* match the current version, identified by the initial ETag value that was returned when the account row was created. This condition is represented by the `If-None-Match` header.  
  
   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/accounts(59d88f5e-6629-ed11-9db1-0022482746b6)?$select=name,revenue,telephone1,description HTTP/1.1
   If-None-Match: W/"72965013"
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 304 NotModified
   ```
   
   **Console output:**  
   
   ```  
   Account record retrieved using ETag: W/"72965013"
   Expected outcome: Entity was not modified so nothing was returned.
   ```  

   The response value, `304 NotModified`, indicates that the current table row is the most current, so the server does *not* return the requested row in the response body.  
  
1. Update the account by modifying its primary telephone number property.  
  
   **Request:**

   ```http
   PUT [Organization Uri]/api/data/v9.2/accounts(59d88f5e-6629-ed11-9db1-0022482746b6)/telephone1 HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {"value": "555-0001"}
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```
   
   **Console output:**  
   
   ```  
   Modified account record retrieved using ETag: W/"72965013" 
   ```  
  
1. Re-attempt the same conditional GET operation, again using the original ETag value. This time the operation returns the requested data because the version on the server is different (and newer) than the version identified in the request. As in all table row retrievals, the response includes an ETag header that identifies the current version.  
  
   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/accounts(59d88f5e-6629-ed11-9db1-0022482746b6)?$select=name,revenue,telephone1,description HTTP/1.1
   If-None-Match: W/"72965013"
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   ETag: W/"72965025"
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,revenue,telephone1,description)/$entity",
   "@odata.etag": "W/\"72965025\"",
   "name": "Contoso Ltd",
   "revenue": 5000000.0,
   "telephone1": "555-0001",
   "description": "Parent company of Contoso Pharmaceuticals, etc.",
   "accountid": "59d88f5e-6629-ed11-9db1-0022482746b6",
   "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1"
   }
   ```
   
   **Console output:**  
   
   ```
   Modified account record retrieved using ETag: W/"72965013"
   Notice the updated ETag value and telephone number
   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,revenue,telephone1,description)/$entity",
   "@odata.etag": "W/\"72965025\"",
   "name": "Contoso Ltd",
   "revenue": 5000000.0,
   "telephone1": "555-0001",
   "description": "Parent company of Contoso Pharmaceuticals, etc.",
   "accountid": "59d88f5e-6629-ed11-9db1-0022482746b6",
   "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1"
   }
   ```  
  
<a name="bkmk_optimisiticConcurrency"></a>
  
## Section 2: Optimistic concurrency on delete and update
 
This section of the program demonstrates how to perform conditional delete and update operations.  The most common use for such operations is in implementing an optimistic concurrency approach to row processing in a multi-user environment. More information: [Apply optimistic concurrency](perform-conditional-operations-using-web-api.md#bkmk_Applyoptimisticconcurrency)  
  
1. Attempt to delete original account if and only if it matches the original version (ETag value).  This condition is represented by the `If-Match` header.  This operation fails because the account row was updated in the previous section, so as a result, its version was updated on the server.  
  
   **Request:**

   ```http
   DELETE [Organization Uri]/api/data/v9.2/accounts(59d88f5e-6629-ed11-9db1-0022482746b6) HTTP/1.1
   If-Match: W/"72965013"
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 412 PreconditionFailed
   OData-Version: 4.0

   {
   "error": {
      "code": "0x80060882",
      "message": "The version of the existing record doesn't match the RowVersion property provided."
    }
   }
   ```
   
   **Console output:**  
   
   ```  
   Attempting to delete the account using the original ETag value
   Expected Error: The version of the existing record doesn't match the RowVersion property provided.
         Account not deleted using ETag 'W/"72965013"', status code: 'PreconditionFailed'.
   ```  
  
1. Attempt to update the account if and only if it matches the original ETag value.  Again, this condition is represented by the `If-Match` header and the operation fails for the same reason.  
  
   **Request:**

   ```http
   PATCH [Organization Uri]/api/data/v9.2/accounts(59d88f5e-6629-ed11-9db1-0022482746b6) HTTP/1.1
   If-Match: W/"72965013"
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "telephone1": "555-0002",
   "revenue": 6000000
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 412 PreconditionFailed
   OData-Version: 4.0

   {
   "error": {
      "code": "0x80060882",
      "message": "The version of the existing record doesn't match the RowVersion property provided."
    }
   }
   ```
   
   **Console output:**  
   
   ```  
   Attempting to update the account using the original ETag value
   Expected Error: The version of the existing record doesn't match the RowVersion property provided.
         Account not updated using ETag 'W/"72965013"', status code: 'PreconditionFailed'.
   ```  
  
1. Re-attempt an update, but instead use the current ETag value obtained from the last row retrieval in the previous section.  
  
   **Request:**

   ```http
   PATCH [Organization Uri]/api/data/v9.2/accounts(59d88f5e-6629-ed11-9db1-0022482746b6) HTTP/1.1
   If-Match: W/"72965025"
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "telephone1": "555-0003",
   "revenue": 6000000
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/accounts(59d88f5e-6629-ed11-9db1-0022482746b6)
   ```
   
   **Console output:**  

   ```
   Attempting to update the account using the current ETag value

   Account successfully updated using ETag: W/"72965025". 
   ```  
  
1. Confirm the update succeeded by retrieving and outputting the current account state.  This uses a basic `GET` request.  
  
   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/accounts(59d88f5e-6629-ed11-9db1-0022482746b6)?$select=name,revenue,telephone1,description HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   ETag: W/"72965035"
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,revenue,telephone1,description)/$entity",
   "@odata.etag": "W/\"72965035\"",
   "name": "Contoso Ltd",
   "revenue": 6000000.0,
   "telephone1": "555-0003",
   "description": "Parent company of Contoso Pharmaceuticals, etc.",
   "accountid": "59d88f5e-6629-ed11-9db1-0022482746b6",
   "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1"
   }
   ```
   
   **Console output:**  
   
   ```
   Below is the final state of the account
   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,revenue,telephone1,description)/$entity",
   "@odata.etag": "W/\"72965035\"",
   "name": "Contoso Ltd",
   "revenue": 6000000.0,
   "telephone1": "555-0003",
   "description": "Parent company of Contoso Pharmaceuticals, etc.",
   "accountid": "59d88f5e-6629-ed11-9db1-0022482746b6",
   "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1"
   }
   ```

## Section 3: Delete sample records

This section simply deletes the record created in [Section 0: Create sample records](#section-0-create-sample-records). It uses a `$batch` request.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/$batch HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

--batch_98e0fdc2-a298-4f42-85a8-da0536140b78
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 115

DELETE /api/data/v9.2/accounts(59d88f5e-6629-ed11-9db1-0022482746b6) HTTP/1.1


--batch_98e0fdc2-a298-4f42-85a8-da0536140b78--

```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_7bf5a9a8-5b97-4fb0-9243-668f3113e6eb
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_7bf5a9a8-5b97-4fb0-9243-668f3113e6eb--

```

**Console output:**

```
Deleting created records.
```
  
### See also

[Use the Dataverse Web API](overview.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)<br />
[Web API Conditional Operations Sample (C#)](samples/webapiservice-conditional-operations.md)<br />
[Web API Conditional Operations Sample (Client-side JavaScript)](samples/conditional-operations-client-side-javascript.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
