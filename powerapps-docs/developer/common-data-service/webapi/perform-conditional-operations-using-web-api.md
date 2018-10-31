---
title: "Perform conditional operations using the Web API (Common Data Service for Apps)| Microsoft Docs"
description: "Read how to create conditions that decide whether and how to perform certain operations using the Web API"
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 771002b0-825a-462d-bbf0-1aeba4b726c8
caps.latest.revision: 16
author: "brandonsimons" # GitHub ID
ms.author: "jdaly"
manager: "amyla"
---
# Perform conditional operations using the Web API

CDS for Apps provides support for a set of conditional operations that rely upon the standard HTTP resource versioning mechanism known as *ETags*.  
  
<a name="bkmk_ETags"></a>
  
## ETags

The HTTP protocol defines an *entity tag*, or [ETag](https://msdn.microsoft.com/en-us/library/dd541486.aspx) for short, for identifying specific versions of a resource. ETags are opaque identifiers whose exact values are implementation dependent. ETag values occur in two varieties: strong and weak validation. Strong validation indicates that a unique resource, identified by a specific URI, will be identical on the binary level if its corresponding ETag value is unchanged. Weak validation only guarantees that the resource representation is semantically equivalent for the same ETag value.  
  
Common Data Service for Apps generates a weakly validating `@odata.etag` property for every entity instance, and this property is automatically returned with each retrieved entity record. For more information, see [Retrieve an entity using the Web API](retrieve-entity-using-web-api.md).  
  
<a name="bkmk_ifMatchHeaders"></a>
 
## If-Match and If-None-Match headers

Use [If-Match](https://tools.ietf.org/html/rfc7232#section-3.1) and [If-None-Match](https://tools.ietf.org/html/rfc7232#section-3.2) headers with ETag values to check whether the current version of a resource matches the one last retrieved, matches any previous version or matches no version.  These comparisons form the basis of conditional operation support. Common Data Service for Apps provides ETags to support conditional retrievals, optimistic concurrency, and limited upsert operations.
 
Queries which expand collection-valued navigation properties may return cached data for those properties that doesn’t reflect recent changes. It is recommended to use `If-None-Match` header with value `null` to override browser caching. See [HTTP Headers](compose-http-requests-handle-errors.md#bkmk_headers) for more details. Use `If-None-Match` header with a specific ETag value to ensure that only changed data is returned.
  
> [!WARNING]
> Client code should not give any meaning to the specific value of an ETag, nor to any apparent relationship between ETags beyond equality or inequality. For example, an ETag value for a more recent version of a resource is not guaranteed to be greater than the ETag value for an earlier version. Also, the algorithm used to generate new ETag values may change without notice between releases of a service.  
  
<a name="bkmk_DetectIfChanged"></a>

## Conditional retrievals

Etags enable you to optimize record retrievals whenever you access the same record multiple times. If you have previously retrieved a record, you can pass the ETag value with the `If-None-Match` header to request data to be retrieved only if it has changed since the last time it was retrieved. If the data has changed, the request returns an HTTP status of 200 (OK) with the latest data in the body of the request. If the data hasn’t changed, the HTTP status code 304 (Not Modified) is returned to indicate that the entity hasn’t been modified. The following example message pair returns data for an account entity with the `accountid` equal to `00000000-0000-0000-0000-000000000001` when the data hasn’t changed since it was last retrieved.  

> [!NOTE]
> Conditional retrieval works only for entities that have optimistic concurrency enabled. Check if an entity has optimistic concurrency enabled using the Web API request shown below. Entities that have optimistic concurrency enabled will have <xref href="Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsOptimisticConcurrencyEnabled?text=EntityMetadata.IsOptimisticConcurrencyEnabled" /> property set to `true`.

> ```HTTP
> GET [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='<Entity Logical Name>')?$select=IsOptimisticConcurrencyEnabled
> ```
<!-- TODO:
> For more information about optimistic concurrency, see [Reduce potential data loss using optimistic concurrency](../org-service/reduce-potential-data-loss-using-optimistic-concurrency.md).   -->

 **Request**  
```http  
GET [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)?$select=accountcategorycode,accountnumber,creditonhold,createdon,numberofemployees,name,revenue   HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
If-None-Match: W/"468026"  
```  
  
 **Response**  
```json  
HTTP/1.1 304 Not Modified  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
```  
  
<a name="bkmk_limitUpsertOperations"></a>
  
## Limit upsert operations

An upsert ordinarily operates by creating an entity if it doesn’t exist; otherwise, it updates an existing entity. However, ETags can be used to further constrain upserts to either prevent creates or to prevent updates.  
  
<a name="bkmk_preventCreateOnUpsert"></a>
 
### Prevent create in upsert

If you are updating data and there is some possibility that the entity was deleted intentionally, you will not want to re-create the entity. To prevent this, add an `If-Match` header to the request with a value of "`*`".  
  
 **Request**  
```http  
PATCH [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
If-Match: "*"  
  
{  
    "name": "Updated Sample Account ",  
    "creditonhold": true,  
    "address1_latitude": 47.639583,  
    "description": "This is the updated description of the sample account",  
    "revenue": 6000000,  
    "accountcategorycode": 2  
}  
```  
  
 **Response**  
 If the entity is found, you’ll get a normal response with status 204 (No Content). When the entity is not found, you’ll get the following response with status 404 (Not Found).  
  
```json  
HTTP/1.1 404 Not Found  
OData-Version: 4.0  
Content-Type: application/json; odata.metadata=minimal  
  
{  
 "error": {  
  "code": "",  
  "message": "account With Id = 00000000-0000-0000-0000-000000000001 Does Not Exist",  
  "innererror": {  
   "message": "account With Id = 00000000-0000-0000-0000-000000000001 Does Not Exist",  
   "type": "System.ServiceModel.FaultException`1[[Microsoft.Xrm.Sdk.OrganizationServiceFault, Microsoft.Xrm.Sdk, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35]]",  
   "stacktrace": <stack trace removed for brevity>  
  }  
 }  
}  
```  
  
<a name="bkmk_preventUpdateInUpsert"></a>
  
### Prevent update in upsert

If you’re inserting data, there is some possibility that a record with the same `id` value already exists in the system and you may not want to update it. To prevent this, add an `If-None-Match` header to the request with a value of "`*`".  
  
 **Request**  
```http  
PATCH [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
If-None-Match: "*"  
  
{  
    "name": "Updated Sample Account ",  
    "creditonhold": true,  
    "address1_latitude": 47.639583,  
    "description": "This is the updated description of the sample account",  
    "revenue": 6000000,  
    "accountcategorycode": 2  
}  
```  
  
 **Response**  
 If the entity isn’t found, you will get a normal response with status 204 (No Content). When the entity is found, you’ll get the following response with status 412 (Precondition Failed).  
  
```json  
HTTP/1.1 412 Precondition Failed  
OData-Version: 4.0  
Content-Type: application/json; odata.metadata=minimal  
  
{  
  "error":{  
   "code":"",  
   "message":"A record with matching key values already exists.",  
   "innererror":{  
    "message":"Cannot insert duplicate key.",  
    "type":"System.ServiceModel.FaultException`1[[Microsoft.Xrm.Sdk.OrganizationServiceFault, Microsoft.Xrm.Sdk, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35]]",  
    "stacktrace":<stack trace removed for brevity>  
    }  
  }  
}  
```  
  
<a name="bkmk_Applyoptimisticconcurrency"></a>

## Apply optimistic concurrency

You can use optimistic concurrency to detect whether an entity has been modified since it was last retrieved. If the entity you intend to update or delete has changed on the server since you retrieved it, you may not want to complete the update or delete operation. By applying the pattern shown here you can detect this situation, retrieve the most recent version of the entity, and apply any necessary criteria to re-evaluate whether to try the operation again.  
  
<a name="bkmk_Applyoptimisticconcurrencyondelete"></a>

### Apply optimistic concurrency on delete

The following delete request for an account with `accountid` of`00000000-0000-0000-0000-000000000001` fails because the ETag value sent with the `If-Match` header is different from the current value. If the value had matched, a 204 (No Content) status is expected.  
  
 **Request**

```http  
DELETE [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
If-Match: W/"470867"  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response**

```json  
HTTP/1.1 412 Precondition Failed  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
  "error":{  
    "code":"","message":"The version of the existing record doesn't match the RowVersion property provided.",  
    "innererror":{  
      "message":"The version of the existing record doesn't match the RowVersion property provided.",  
      "type":"System.ServiceModel.FaultException`1[[Microsoft.Xrm.Sdk.OrganizationServiceFault, Microsoft.Xrm.Sdk, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35]]",  
"stacktrace":"  <stack trace details omitted for brevity>  
    }  
  }  
}  
```  
  
<a name="bkmk_Applyoptimisticconcurrencyonupdate"></a>

### Apply optimistic concurrency on update

The following update request for an account with `accountid` of `00000000-0000-0000-0000-000000000001` fails because the ETag value sent with the `If-Match` header is different from the current value. If the value had matched, a 204 (No Content) status is expected.  
  
 **Request**

```http  
PATCH [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
If-Match: W/"470867"  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{"name":"Updated Account Name"}  
```  
  
 **Response**

```json  
HTTP/1.1 412 Precondition Failed  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
  "error":{  
    "code":"","message":"The version of the existing record doesn't match the RowVersion property provided.",  
    "innererror":{  
      "message":"The version of the existing record doesn't match the RowVersion property provided.",  
      "type":"System.ServiceModel.FaultException`1[[Microsoft.Xrm.Sdk.OrganizationServiceFault, Microsoft.Xrm.Sdk, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35]]",  
"stacktrace":"  <stack trace details omitted for brevity>  
    }  
  }  
}  
```  
  
### See also

[Web API Conditional Operations Sample (C#)](samples/conditional-operations-csharp.md)<br />
[Web API Conditional Operations Sample (Client-side JavaScript)](samples/conditional-operations-client-side-javascript.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Create an entity using the Web API](create-entity-web-api.md)<br />
[Retrieve an entity using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete entities using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate entities using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)
