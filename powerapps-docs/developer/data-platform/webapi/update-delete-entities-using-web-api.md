---
title: "Update and delete table rows using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Read how to perform update and delete operations on tables using the Web API"
ms.custom: ""
ms.date: 05/03/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 694889fd-2b85-43a0-97bc-1e760695db31
caps.latest.revision: 17
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Update and delete table rows using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Operations to modify data are a core part of the Web API. In addition to a simple update and delete, you can perform operations on single table columns (entity attributes) and compose *upsert* requests that will either update or insert data depending on whether it exists.  
  
<a name="bkmk_update"></a>

## Basic update

Update operations use the HTTP `PATCH` verb. Pass a JSON object containing the properties you want to update to the URI that represents the entity. A response with a status of 204 will be returned if the update is successful.  
  
The `If-Match: *` header helps ensure you don't create a new record by accidentally performing an upsert operation. More information: [Prevent create in upsert](perform-conditional-operations-using-web-api.md#prevent-create-in-upsert).
  
> [!IMPORTANT]
>  When updating an entity, only include the properties you are changing in the request body. Simply updating the properties of an entity that you previously retrieved, and including that JSON in your request, will update each property even though the value is the same. This can cause system events that can trigger business logic that expects that the values have changed. This can cause properties to appear to have been updated in auditing data when in fact they haven’t actually changed.

> [!NOTE] 
> The definition for attributes includes a `RequiredLevel` property. When this is set to `SystemRequired`, you cannot set these attributes to a null value. More information: [Attribute requirement level](../entity-attribute-metadata.md#column-requirement-level)

This example updates an existing account record with the `accountid` value of 00000000-0000-0000-0000-000000000001.  
  
 **Request**

```http
PATCH [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
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
  
 **Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
  
```  
  
> [!NOTE]
>  See [Associate and disassociate tables on update](associate-disassociate-entities-using-web-api.md#associate-and-disassociate-table-rows-on-update) for information about associating and disassociating entities on update.  
  
<a name="bkmk_updateWithDataReturned"></a>

## Update with data returned
  
To retrieve data from an entity you are updating you can compose your `PATCH` request so that data from the created record will be returned with a status of 200 (OK).  To get this result, you must use the `return=representation` preference in the request headers.  
  
 To control which properties are returned, append the `$select` query option to the URL to the entity set.  The `$expand` query option will be ignored if used.  
  
 This example updates an account entity and returns the requested data in the response.  
  
 **Request**

```http
PATCH [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)?$select=name,creditonhold,address1_latitude,description,revenue,accountcategorycode,createdon HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
Prefer: return=representation
If-Match: * 
  
{"name":"Updated Sample Account"}  
```  
  
 **Response** 
 
```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
Preference-Applied: return=representation  
OData-Version: 4.0  
  
{  
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#accounts/$entity",  
    "@odata.etag": "W/\"536537\"",  
    "accountid": "00000000-0000-0000-0000-000000000001",  
    "accountcategorycode": 1,  
    "description": "This is the description of the sample account",  
    "address1_latitude": 47.63958,  
    "creditonhold": false,  
    "name": "Updated Sample Account",  
    "createdon": "2016-09-28T23:14:00Z",  
    "revenue": 5000000.0000,  
    "_transactioncurrencyid_value": "048dddaa-6f7f-e611-80d3-00155db5e0b6"  
}  
  
```  
  
<a name="bkmk_updateSingleProperty"></a> 
  
## Update a single property value  

When you want to update only a single property value use a PUT request with the property name appended to the Uri of the entity.  
  
 The following example updates the name property of an existing account entity with the `accountid` value of 00000000-0000-0000-0000-000000000001.  
  
 **Request**  

```http
PUT [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)/name HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{"value": "Updated Sample Account Name"}  
```  
  
 **Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
  
```  
  
<a name="bkmk_deleteSingleProperty"></a>

## Delete a single property value

To delete the value of a single property use a DELETE request with the property name appended to the Uri of the entity.  
  
The following example deletes the value of the `description` property of an account entity with the `accountid` value of 00000000-0000-0000-0000-000000000001.  
  
 **Request**

```http
DELETE [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001)/description HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
  
```  
  
> [!NOTE]
>  This can’t be used with a single-valued navigation property to disassociate two entities. For an alternative approach, see [Remove a reference to a table](associate-disassociate-entities-using-web-api.md#bkmk_Removeareferencetoarow).  
  
<a name="bkmk_upsert"></a>

## Upsert a table

An *upsert* operation is exactly like an update. It uses a `PATCH` request and uses a URI to reference a specific entity. The difference is that if the entity doesn’t exist it will be created. If it already exists, it will be updated. Normally when creating a new entity you will let the system assign a unique identifier. This is a best practice. But if you need to create a record with a specific `id` value, an `upsert` operation provides a way to do this. This can be valuable in situation where you are synchronizing data in different systems.  
  
Sometimes there are situations where you want to perform an `upsert`, but you want to prevent one of the potential default actions: either create or update. You can accomplish this through the addition of `If-Match` or `If-None-Match` headers. For more information, see [Limit upsert operations](perform-conditional-operations-using-web-api.md#bkmk_limitUpsertOperations).  
  
<a name="bkmk_delete"></a>
  
## Basic delete

A delete operation is very straightforward. Use the DELETE verb with the URI of the entity you want to delete. This example message deletes an account entity with the primary key `accountid` value equal to 00000000-0000-0000-0000-000000000001.  
  
 **Request**

```http
DELETE [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response**

 If the entity exists, you’ll get a normal response with status 204 to indicate the delete was successful. If the entity isn’t found, you’ll get a response with status 404.  
  
```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```  

<a name="bkmk_duplicate"></a>

## Check for duplicate records

See [Detect duplicates during Update operation using the Web API](manage-duplicate-detection-create-update.md#bkmk_update) for more information on how to check for duplicate records during Update operation.

## Update and delete documents in storage partitions

If you are updating or deleting entity data stored in partitions be sure to specify the partition key when accessing that data.

More information: [Access table data faster using storage partitions](azure-storage-partitioning.md)

### See also

[Web API Basic Operations Sample (C#)](samples/cdswebapiservice-basic-operations.md)<br />
[Web API Basic Operations Sample (Client-side JavaScript)](samples/basic-operations-client-side-javascript.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Create a table using the Web API](create-entity-web-api.md)<br />
[Retrieve a table using the Web API](retrieve-entity-using-web-api.md)<br />
[Associate and disassociate tables using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
