---
title: "Update and delete table rows using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Read how to perform update and delete operations on tables using the Web API"
ms.date: 08/01/2022
author: divka78
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
---

# Update and delete table rows using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Operations to modify data are a core part of the Web API. In addition to a simple update and delete, you can perform operations on single table columns (entity attributes) and compose *upsert* requests that will either update or insert data depending on whether it exists.  
  
<a name="bkmk_update"></a>

## Basic update

Update operations use the HTTP `PATCH` verb. Pass a JSON object containing the properties you want to update to the URI that represents the record. A response with a status of `204 No Content` will be returned if the update is successful.  
  
The `If-Match: *` header ensures you don't create a new record by accidentally performing an upsert operation. More information: [Prevent create in upsert](perform-conditional-operations-using-web-api.md#prevent-create-in-upsert).
  
> [!IMPORTANT]
> When updating an entity, only include the properties you are changing in the request body. Simply updating the properties of an entity that you previously retrieved, and including that JSON in your request, will update each property even though the value is the same. This can cause system events that can trigger business logic that expects that the values have changed. This can cause properties to appear to have been updated in auditing data when in fact they haven't actually changed.

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
>  See [Using single-valued navigation properties](associate-disassociate-entities-using-web-api.md#using-single-valued-navigation-properties) for information about associating and disassociating entities on update.  
  
<a name="bkmk_updateWithDataReturned"></a>

## Update with data returned
  
To retrieve data from an entity you are updating you can compose your `PATCH` request so that data from the created record will be returned with a status of 200 (OK).  To get this result, you must use the `Prefer: return=representation` request header.  
  
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

To delete the value of a single property use a `DELETE` request with the property name appended to the Uri of the entity.  
  
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
>  This can't be used with a single-valued navigation property to disassociate two entities. For an alternative approach, see [Disassociate with a single-valued navigation property](associate-disassociate-entities-using-web-api.md#disassociate-with-a-single-valued-navigation-property) .  
  
<a name="bkmk_upsert"></a>

## Upsert a table row

An *upsert* operation is similar to an update. It uses a `PATCH` request and uses a URI to reference a specific record. The difference is that if the record doesn't exist it will be created. If it already exists, it will be updated.

Upsert is valuable when synchronizing data between external systems. The external system may not contain a reference to the primary key of the Dataverse table, so you can configure alternate keys for the Dataverse table using values from the external system that uniquely identify the record on both systems. More information: [Define alternate keys to reference rows](../../../maker/data-platform/define-alternate-keys-reference-records.md)

You can see any alternate keys that are defined for a table in the annotations for the entity type in the $metadata service document. More information: [Alternate Keys](web-api-entitytypes.md#alternate-keys).

In the following example, there is a table with the name `sample_thing` that has an alternate key that refers to two columns: `sample_key1` and `sample_key2` which are both defined to store integer values.

**Request**

```http
PATCH [Organization URI]/api/data/v9.2/sample_things(sample_key1=1,sample_key2=1) HTTP/1.1
Accept: application/json 
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Content-Type: application/json

{
    "sample_name": "1:1"
}
```

For both create or update operations you will get the same response. Notice how the `OData-EntityId` response header uses the key values rather than the GUID primary key identifier for the record. 

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.2/sample_things(sample_key1=1,sample_key2=1)
```

Because the response it the same, you cannot know whether the operation represented a `Create` or `Update`.

If you need to know, you can use the `Prefer: return=representation` request header. Whith this header you will get a `201 Created` response when a record is created and a `200 OK` reponse when the record is updated. This adds an additional `Retrieve` operation which has an impact on performance. If you use the `Prefer: return=representation` request header, make sure that your `$select` includes the minimal amount of data, preferably only the primary key column. More information: [Update with data returned](#update-with-data-returned) and [Create with data returned](create-entity-web-api.md#create-with-data-returned).

When using alternate keys, you should not include the alternate key values in the body of the request.

- When an upsert represents an `Update`, these alternate key values will be ignored. You cannot update alternate key values while using them to identify the record.
- When an upsert represents a `Create`, the key values in the URL will be set for the record if they are not present in the body. So there is no need to include them in the body of the request.

More information: [Use Upsert to Create or Update a record](../use-upsert-insert-update-record.md)

> [!NOTE]
> Normally when creating a new record you will let the system assign a GUID value for the primary key. This is a best practice because the system generates keys that are optimized for the index and this improves performance. But if you need to create a record with a specific primary key value, such as when the key GUID value is generated by an external system, the `upsert` operation provides a way to do this.

### Prevent create or update with upsert

Sometimes there are situations where you want to perform an `upsert`, but you want to prevent one of the potential operations: either create or update. You can accomplish this through the addition of `If-Match` or `If-None-Match` headers. For more information, see [Limit upsert operations](perform-conditional-operations-using-web-api.md#bkmk_limitUpsertOperations). 
  
<a name="bkmk_delete"></a>
  
## Basic delete

A delete operation is very straightforward. Use the `DELETE` verb with the URI of the entity you want to delete. This example message deletes an account entity with the primary key `accountid` value equal to 00000000-0000-0000-0000-000000000001.  
  
 **Request**

```http
DELETE [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response**

 If the entity exists, you'll get a normal response with status 204 to indicate the delete was successful. If the entity isn't found, you'll get a response with status 404.  
  
```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```  

<a name="bkmk_duplicate"></a>

## Check for duplicate records

See [Detect duplicates during Update operation using the Web API](manage-duplicate-detection-create-update.md#bkmk_update) for more information on how to check for duplicate records during an update operation.

## Update and delete documents in storage partitions

If you are updating or deleting entity data stored in partitions be sure to specify the partition key when accessing that data.

More information: [Access table data faster using storage partitions](azure-storage-partitioning.md)

### See also

[Web API Basic Operations Sample (C#)](samples/webapiservice-basic-operations.md)<br />
[Web API Basic Operations Sample (Client-side JavaScript)](samples/basic-operations-client-side-javascript.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Create a table row using the Web API](create-entity-web-api.md)<br />
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />
[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
