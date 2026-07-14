---
title: "Perform conditional operations using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Read how to create conditions that decide whether and how to perform certain operations using the Web API"
ms.date: 04/06/2022
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Perform conditional operations using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Microsoft Dataverse provides support for a set of conditional operations that rely upon the standard HTTP resource versioning mechanism known as *ETags*.  
  
<a name="bkmk_ETags"></a>
  
## ETags

The HTTP protocol defines an *entity tag*, or [ETag](/openspecs/windows_protocols/ms-odata/c4d715eb-10f6-47fa-9ccc-2ebf926558a6) for short, for identifying specific versions of a resource. ETags are opaque identifiers whose exact values are implementation dependent. ETag values occur in two varieties: strong and weak validation. Strong validation indicates that a unique resource, identified by a specific URI, are identical on the binary level if its corresponding ETag value is unchanged. Weak validation only guarantees that the resource representation is semantically equivalent for the same ETag value.
  
Dataverse generates a weakly validating `@odata.etag` property for every entity instance, and this property is automatically returned with each retrieved entity record. For more information, see [Retrieve a table row using the Web API](retrieve-entity-using-web-api.md).
  
<a name="bkmk_ifMatchHeaders"></a>
 
## If-Match and If-None-Match headers

Use [If-Match](https://tools.ietf.org/html/rfc7232#section-3.1) and [If-None-Match](https://tools.ietf.org/html/rfc7232#section-3.2) headers with ETag values to check whether the current version of a resource matches the one last retrieved, matches any previous version, or matches no version. These comparisons form the basis of conditional operation support. Dataverse provides ETags to support conditional retrievals, optimistic concurrency, and limited upsert operations.
  
> [!WARNING]
> Client code should not give any meaning to the specific value of an ETag, nor to any apparent relationship between ETags beyond equality or inequality. For example, an ETag value for a more recent version of a resource is not guaranteed to be greater than the ETag value for an earlier version. Also, the algorithm used to generate new ETag values may change without notice between releases of a service.  
  
<a name="bkmk_DetectIfChanged"></a>

## Conditional retrievals

Etags enable you to optimize record retrievals whenever you access the same record multiple times. If you previously retrieved a record, you can pass the ETag value with the `If-None-Match` header to request data to be retrieved only if it changed since the last time it was retrieved. If the data changed, the request returns an HTTP status of `200 OK` with the latest data in the body of the request. If the data is unchanged, the HTTP status code `304 Not Modified` is returned to indicate that the record hasn't been modified.

The following example message pair returns data for an account record with the `accountid` equal to `00000000-0000-0000-0000-000000000001` when the data hasn't changed since it was last retrieved when the Etag value was `W/"468026"`

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

Check if an table has optimistic concurrency enabled using the following Web API request. Tables that have optimistic concurrency enabled have [EntityMetadata.IsOptimisticConcurrencyEnabled](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsOptimisticConcurrencyEnabled) property set to `true`.

```http
GET [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='<Entity Logical Name>')?$select=IsOptimisticConcurrencyEnabled
```

### Query must not include $expand

The Etag can only detect if the single record that is being retrieved changed. When you use `$expand` in your query, more records might be returned and it isn't possible to detect whether or not any of those records changed. If the query includes `$expand`, `304 Not Modified` is never returned.

### Query must not include annotations

When the `Prefer: odata.include-annotations` header is included with a `GET` request, `304 Not Modified` is never returned. The values of annotations can refer to values from related records. These records might have changed and this change couldn't be detected, so it would be incorrect to indicate that nothing changed.


  
<a name="bkmk_limitUpsertOperations"></a>
  
## Limit upsert operations

An upsert ordinarily operates by creating a record if it doesn't exist; otherwise, it updates an existing record. However, ETags can be used to further constrain upserts to either prevent creates or to prevent updates.  
  
<a name="bkmk_preventCreateOnUpsert"></a>
 
### Prevent create in upsert

If you're updating data and there's some possibility that the record was deleted intentionally, you won't want to re-create the record. To prevent this, add an `If-Match` header to the request with a value of `*`.
  
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

 If the record is found, you get a normal response with status `204 No Content`. When the record isn't found, you get the following response with status `404 Not Found`.  
  
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

If you're inserting data, there's some possibility that a record with the same `id` value already exists in the system and you might not want to update it. To prevent this, add an `If-None-Match` header to the request with a value of "*".
  
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
 If the record isn't found, you'll get a normal response with status `204 No Content`. When the record is found, you get the following response with status `412 Precondition Failed`.  
  
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

You can use optimistic concurrency to detect whether a record was modified since it was last retrieved. If the record you intend to update or delete has changed on the server since you retrieved it, you might not want to complete the update or delete operation. By applying the pattern shown here you can detect this situation, retrieve the most recent version of the record, and apply any necessary criteria to reevaluate whether to try the operation again.  
  
<a name="bkmk_Applyoptimisticconcurrencyondelete"></a>

### Apply optimistic concurrency on delete

The following delete request for an account with `accountid` of`00000000-0000-0000-0000-000000000001` fails because the ETag value sent with the `If-Match` header is different from the current value. If the value matched, a `204 No Content` status is expected.
  
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

The following update request for an account with `accountid` of `00000000-0000-0000-0000-000000000001` fails because the ETag value sent with the `If-Match` header is different from the current value. If the value matched, a `204 No Content` status is expected.  
  
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

[Web API Conditional Operations Sample (C#)](samples/webapiservice-conditional-operations.md)<br />
[Web API Conditional Operations Sample (Client-side JavaScript)](samples/conditional-operations-client-side-javascript.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query/overview.md)<br />
[Create a table row using the Web API](create-entity-web-api.md)<br />
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
