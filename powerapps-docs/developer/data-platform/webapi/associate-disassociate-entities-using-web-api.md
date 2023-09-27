---
title: "Associate and disassociate table rows using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "How to relate and unrelate records using the Web API"
ms.date: 08/15/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Associate and disassociate table rows using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can associate individual records in table rows with other records using relationships that exist between the table definitions. In OData the relationships are expressed as navigation properties.

You can discover which navigation properties exist in the $metadata service document. See [Web API Navigation Properties](web-api-navigation-properties.md). For existing Dataverse tables, see the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex?text=Web API EntityType Reference>, for each entity type, see the listed single-valued and collection-valued navigation properties.

The following table describes the three types of relationships between tables in Dataverse.

|Type|Description|Example|
|---------|---------|---------|
|One-to-Many|One record can have many records associated with it.|An <xref:Microsoft.Dynamics.CRM.account?text=account> record can have many <xref:Microsoft.Dynamics.CRM.contact?text=contact> records in the `contact_customer_accounts` *collection-valued navigation property*.|
|Many-to-One|Many records can be associated with one record.<br/><br/>Many-to-One is the mirror image of a One-to-Many relationship. There is just one relationship.|Multiple <xref:Microsoft.Dynamics.CRM.contact?text=contact> records can be associated to a single <xref:Microsoft.Dynamics.CRM.account?text=account> record using the `parentcustomerid_account` *single-valued navigation property*.|
|Many-to-Many|Many records can be associated with many records.|Each <xref:Microsoft.Dynamics.CRM.role?text=security role (role)> may include references to the definition of a <xref:Microsoft.Dynamics.CRM.systemuser?text=systemuser>.<br />Both of these tables has a `systemuserroles_association` *collection-valued navigation property*.|

## Using single-valued navigation properties

For existing records on the *many* side of a one-to-many or many-to-one relationship, you can associate the record by setting a Uri reference to the other record. The easiest and most common way to do this is by appending the `@odata.bind` annotation to the name of the single-valued navigation property and then setting the value as the Uri to the other record in a `PATCH` request.

### Associate with a single-valued navigation property

For example, to associate a <xref:Microsoft.Dynamics.CRM.contact?text=contact> record to an <xref:Microsoft.Dynamics.CRM.account?text=account> using the `parentcustomerid_account` single-valued navigation property:

**Request:**

```http
PATCH [Organization Uri]/api/data/v9.2/contacts(cf9eaaef-f718-ed11-b83e-00224837179f) HTTP/1.1
If-Match: *
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "parentcustomerid_account@odata.bind": "accounts(ce9eaaef-f718-ed11-b83e-00224837179f)"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/contacts(cf9eaaef-f718-ed11-b83e-00224837179f)
```

As described in [Associate table rows on create](create-entity-web-api.md#associate-table-rows-on-create), new records can also be associated with existing records in the same way.

### Disassociate with a single-valued navigation property

If you want to disassociate, you can simply set the value to null.

**Request:**

```http
PATCH [Organization Uri]/api/data/v9.2/contacts(cf9eaaef-f718-ed11-b83e-00224837179f) HTTP/1.1
If-Match: *
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "parentcustomerid_account@odata.bind": null
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/contacts(cf9eaaef-f718-ed11-b83e-00224837179f)
```

When disassociating in this manner, you don't need to include the `@odata.bind` annotation. You can simply use the name of the single-valued navigation property:

**Request:**

```http
PATCH [Organization Uri]/api/data/v9.2/contacts(cf9eaaef-f718-ed11-b83e-00224837179f) HTTP/1.1
If-Match: *
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "parentcustomerid_account": null
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/contacts(cf9eaaef-f718-ed11-b83e-00224837179f)
```

More information: [Basic update](update-delete-entities-using-web-api.md#basic-update)

### Other methods

There are other ways to achieve the same results described above with single-valued navigation properties.

You can use the following `PUT` request to set the value of the `parentcustomerid_account` single-valued navigation property:

**Request:**

```http
PUT [Organization Uri]/api/data/v9.2/contacts(cf9eaaef-f718-ed11-b83e-00224837179f)/parentcustomerid_account/$ref HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "@odata.id": "[Organization URI]/api/data/v9.2/accounts(ce9eaaef-f718-ed11-b83e-00224837179f)"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

> [!NOTE]
> Note: You must use an absolute URL when setting the value for `@odata.id`.

To remove the reference, you can also use this `DELETE` request:

**Request:**

```http
DELETE [Organization Uri]/api/data/v9.2/contacts(cf9eaaef-f718-ed11-b83e-00224837179f)/parentcustomerid_account/$ref HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

## Using collection-valued navigation properties

With OData, both sides of a many-to-many relationship will have collection-valued navigation properties. For one-to-many and many-to-one relationships, the table one the 'One' side will have a collection-valued navigation property. There is no difference how you work with any of these types of relationships while using collection-valued navigation properties. This section will describe how to work with collection-valued navigation properties with any type of relationship.

## Add a record to a collection

The following example shows how to add a <xref:Microsoft.Dynamics.CRM.contact?text=contact> record to the <xref:Microsoft.Dynamics.CRM.account?text=account> `contact_customer_accounts` collection which is part of a one-to-many relationship.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/accounts(ce9eaaef-f718-ed11-b83e-00224837179f)/contact_customer_accounts/$ref HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "@odata.id": "[Organization URI]/api/data/v9.2/contacts(cf9eaaef-f718-ed11-b83e-00224837179f)"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

The following example shows how to add a <xref:Microsoft.Dynamics.CRM.role?text=role> record to the <xref:Microsoft.Dynamics.CRM.systemuser?text=systemuser> `systemuserroles_association` collection which is a many-to-many relationship.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/systemusers(34dcbaf5-f718-ed11-b83e-00224837179f)/systemuserroles_association/$ref HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "@odata.id": "[Organization URI]/api/data/v9.2/roles(886b280c-6396-4d56-a0a3-2c1b0a50ceb0)"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

## Remove a record from a collection

The following example shows how to remove a <xref:Microsoft.Dynamics.CRM.contact?text=contact> record to the <xref:Microsoft.Dynamics.CRM.account?text=account> `contact_customer_accounts` collection where the contact `contactid` value is `cf9eaaef-f718-ed11-b83e-00224837179f`.

**Request:**

```http
DELETE [Organization Uri]/api/data/v9.2/accounts(ce9eaaef-f718-ed11-b83e-00224837179f)/contact_customer_accounts(cf9eaaef-f718-ed11-b83e-00224837179f)/$ref HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

The following also works:

**Request:**

```http
DELETE [Organization Uri]/api/data/v9.2/accounts(ce9eaaef-f718-ed11-b83e-00224837179f)/contact_customer_accounts/$ref?$id=[Organization URI]/api/data/v9.2/contacts(cf9eaaef-f718-ed11-b83e-00224837179f) HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

<!-- 

The code snippet in the following section doesn't work, so removing this section until the correct request can be added.

<a name="bkmk_Associaterowsonupdate_multi"></a>

## Associate table rows on update using collection-valued navigation property

The following example shows how to associate multiple existing [ActivityParty](../reference/entities/activityparty.md) with an [Email](../reference/entities/email.md) using collection-valued navigation property `email_activity_parties`.

> [!NOTE]
> Associating multiple tables with a table on update is a special scenario that is possible only with <xref:Microsoft.Dynamics.CRM.activityparty?text=activityparty EntityType>.

**Request:**

```HTTP
PUT [Organization URI]/api/data/v9.0/emails(2479d20d-3a39-e711-8145-e0071b6a2001)/email_activity_parties
Content-Type: application/json  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0

{
   "value": [
      {
         "partyid_contact@odata.bind":"contacts(a30d4045-fc46-e711-8115-e0071b66df51)",
         "participationtypemask":3
         
      },
      {
         "partyid_contact@odata.bind":"contacts(1dcdda07-3a39-e711-8145-e0071b6a2001)",
         "participationtypemask":2
         
      }
      ]
}
```

**Response:**

```HTTP
HTTP/1.1 204 No Content  
OData-Version: 4.0 
``` -->

### See also

 [Web API Basic Operations Sample (C#)](samples/webapiservice-basic-operations.md)<br />
 [Web API Basic Operations Sample (Client-side JavaScript)](samples/basic-operations-client-side-javascript.md)<br />
 [Perform operations using the Web API](perform-operations-web-api.md)<br />
 [Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
 [Query Data using the Web API](query-data-web-api.md)<br />
 [Create a table row using the Web API](create-entity-web-api.md)<br />
 [Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />
 [Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)<br />
 [Use Web API functions](use-web-api-functions.md)<br />
 [Use Web API actions](use-web-api-actions.md)<br />
 [Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
 [Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
 [Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
