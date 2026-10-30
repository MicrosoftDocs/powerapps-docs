---
title: "Perform Conditional Operations Using the Dataverse Web API"
description: "Learn how to use ETags with the Dataverse Web API to perform conditional retrievals, limit upsert operations, and apply optimistic concurrency."
ms.date: 10/29/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Perform conditional operations by using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Microsoft Dataverse supports conditional operations that use the standard HTTP resource versioning mechanism known as *ETags*. Use conditional operations by using the Web API to optimize record retrievals, limit upsert operations, and apply optimistic concurrency to prevent overwriting changes made by others.  
  
<a name="bkmk_ETags"></a>
  
## ETags and resource versioning

The HTTP protocol defines an *entity tag*, or [ETag](/openspecs/windows_protocols/ms-odata/c4d715eb-10f6-47fa-9ccc-2ebf926558a6) for short, for identifying specific versions of a resource. ETags are opaque identifiers whose exact values depend on the implementation. ETag values occur in two varieties: strong and weak validation. Strong validation indicates that a unique resource, identified by a specific URI, is identical on the binary level if its corresponding ETag value is unchanged. Weak validation only guarantees that the resource representation is semantically equivalent for the same ETag value.
  
Dataverse generates a weakly validating `@odata.etag` property for every entity instance, and it automatically returns this property with each retrieved entity record. For more information, see [Retrieve a table row using the Web API](retrieve-table-row.md).
  
<a name="bkmk_ifMatchHeaders"></a>
 
## If-Match and If-None-Match headers

Use the [If-Match](https://www.rfc-editor.org/rfc/rfc7232.html#section-3.1) and [If-None-Match](https://www.rfc-editor.org/rfc/rfc7232.html#section-3.2) headers with ETag values to check whether the current version of a resource matches the one you last retrieved, matches any previous version, or matches no version. These comparisons form the basis of conditional operation support. Dataverse provides ETags to support conditional retrievals, optimistic concurrency, and limited upsert operations.
  
> [!WARNING]
> Client code shouldn't give any meaning to the specific value of an ETag, nor to any apparent relationship between ETags beyond equality or inequality. For example, an ETag value for a more recent version of a resource isn't guaranteed to be greater than the ETag value for an earlier version. Also, the algorithm used to generate new ETag values might change without notice between releases of a service.  
  
<a name="bkmk_DetectIfChanged"></a>

## Conditional retrievals

Etags help you optimize record retrievals when you access the same record multiple times. If you previously retrieved a record, pass the ETag value with the `If-None-Match` header to request data only if it changed since the last time you retrieved it. If the data changed, the request returns an HTTP status of `200 OK` with the latest data in the body of the request. If the data is unchanged, the request returns the HTTP status code `304 Not Modified` to indicate that the record isn't modified.

The following example message pair returns data for an account record with the `accountid` equal to `00000000-0000-0000-0000-000000000001` when the data hasn't changed since you last retrieved it and the Etag value was `W/"468026"`.

 **Request:**

```http  
GET [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001)?$select=accountcategorycode,accountnumber,creditonhold,createdon,numberofemployees,name,revenue   HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
If-None-Match: W/"468026"  
```  
  
 **Response:**

```http  
HTTP/1.1 304 Not Modified  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
```  

The following sections describe limitations to using conditional retrievals.

### Table must have optimistic concurrency enabled

Check if a table has optimistic concurrency enabled by using the following Web API request. Tables that have optimistic concurrency enabled have the [EntityMetadata.IsOptimisticConcurrencyEnabled](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsOptimisticConcurrencyEnabled) property set to `true`. Use this URL to retrieve the value:

```http
GET [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='<Entity Logical Name>')?$select=IsOptimisticConcurrencyEnabled
```

This example retrieves the value from the contact table:

 **Request:**

```http  
GET [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='contact')?$select=IsOptimisticConcurrencyEnabled  HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response:**

```http  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0

{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#EntityDefinitions(IsOptimisticConcurrencyEnabled)/$entity",
   "MetadataId": "608861bc-50a4-4c5f-a02c-21fe1943e2cf",
   "IsOptimisticConcurrencyEnabled": true
}
```  

### Query must not include $expand

The Etag can only detect if the single record that you're retrieving changed. When you use `$expand` in your query, you might return more records, and it isn't possible to detect whether any of those records changed. If the query includes `$expand`, the request never returns `304 Not Modified`.

### Query must not include annotations

When you include the `Prefer: odata.include-annotations` header in a `GET` request, the server never returns `304 Not Modified`. The values of annotations can refer to values from related records. These records might have changed, and the server can't detect this change, so it would be incorrect to indicate that nothing changed.


  
<a name="bkmk_limitUpsertOperations"></a>
  
## Limit upsert operations

An upsert operation creates a record if it doesn't exist; otherwise, it updates an existing record. However, you can use ETags to further constrain upserts to either prevent creates or prevent updates.  
  
<a name="bkmk_preventCreateOnUpsert"></a>
 
### Prevent create in upsert

If you're updating data and there's a possibility that the record was deleted intentionally, you might not want to re-create the record. To prevent this condition, add an `If-Match` header to the request with a value of `*`.
  
 **Request:**

```http  
PATCH [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
If-Match: *  
  
{  
    "name": "Updated Sample Account ",  
    "creditonhold": true,  
    "address1_latitude": 47.639583,  
    "description": "This is the updated description of the sample account",  
    "revenue": 6000000,  
    "accountcategorycode": 2  
}  
```  
  
 **Response:**

 If the server finds the record, you get a normal response with status `204 No Content`. If the server doesn't find the record, you get the following response with status `404 Not Found`.  
  
```http  
HTTP/1.1 404 Not Found  
OData-Version: 4.0  
Content-Type: application/json; odata.metadata=minimal  
  
{  
 "error": {  
  "code": "",  
  "message": "account With Id = 00000000-0000-0000-0000-000000000001 Does Not Exist"
 }  
}  
```  
  
<a name="bkmk_preventUpdateInUpsert"></a>
  
### Prevent update in upsert

If you're inserting data, a record with the same `id` value might already exist in the system. You might not want to update this existing record. To prevent updating the record, add an `If-None-Match` header to the request with a value of "*".
  
 **Request:**

```http
PATCH [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
If-None-Match: *  
  
{  
    "name": "Updated Sample Account ",  
    "creditonhold": true,  
    "address1_latitude": 47.639583,  
    "description": "This is the updated description of the sample account",  
    "revenue": 6000000,  
    "accountcategorycode": 2  
}  
```  
  
 **Response:**  
 If the record isn't found, you receive a normal response with status `204 No Content`. If the record is found, you receive the following response with status `412 Precondition Failed`.  
  
```http  
HTTP/1.1 412 Precondition Failed  
OData-Version: 4.0  
Content-Type: application/json; odata.metadata=minimal  
  
{  
  "error":{  
   "code":"",  
   "message":"A record with matching key values already exists."
  }  
}  
```  
  
<a name="bkmk_Applyoptimisticconcurrency"></a>

## Apply optimistic concurrency

Use optimistic concurrency to detect whether a record was modified since you last retrieved it. If the record you intend to update or delete changed on the server since you retrieved it, you might not want to complete the update or delete operation. By using the following pattern, you can detect this situation, retrieve the most recent version of the record, and apply any necessary criteria to reevaluate whether to try the operation again.  
  
<a name="bkmk_Applyoptimisticconcurrencyondelete"></a>

### Apply optimistic concurrency on delete

The following delete request for an account with `accountid` of `00000000-0000-0000-0000-000000000001` fails because the ETag value sent with the `If-Match` header is different from the current value. If the value matched, you receive a `204 No Content` status.
  
 **Request:**

```http  
DELETE [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
If-Match: W/"470867"  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response:**

```json  
HTTP/1.1 412 Precondition Failed  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
  "error":{  
    "code":"","message":"The version of the existing record doesn't match the RowVersion property provided." 
  }  
}  
```  
  
<a name="bkmk_Applyoptimisticconcurrencyonupdate"></a>

### Apply optimistic concurrency on update

The following update request for an account with `accountid` of `00000000-0000-0000-0000-000000000001` fails because the ETag value sent with the `If-Match` header is different from the current value. If the value matched, you receive a `204 No Content` status.  
  
 **Request:**

```http  
PATCH [Organization URI]/api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
If-Match: W/"470867"  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{"name":"Updated Account Name"}  
```  
  
 **Response:**

```json  
HTTP/1.1 412 Precondition Failed  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
  "error":{  
    "code":"","message":"The version of the existing record doesn't match the RowVersion property provided."
  }  
}  
```  
  
### See also

[Web API Conditional Operations Sample (PowerShell)](samples/conditional-operations-powershell.md)<br />
[Web API Conditional Operations Sample (C#)](samples/webapiservice-conditional-operations.md)<br />
[Web API Conditional Operations Sample (Client-side JavaScript)](samples/conditional-operations-client-side-javascript.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
