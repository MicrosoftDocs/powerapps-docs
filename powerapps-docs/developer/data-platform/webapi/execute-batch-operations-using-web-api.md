---
title: "Execute batch operations using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Batch operation lets you group multiple operations in a single HTTP request. Read how to execute batch operations using the Web API"
ms.date: 01/14/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Execute batch operations using the Web API

You can group multiple operations into a single HTTP request using a batch operation. These operations will be performed sequentially in the order they're specified. The order of the responses will match the order of the requests in the batch operation.

The format to send `$batch` requests is defined in this section of the OData specification: [11.7 Batch Requests](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part1-protocol/odata-v4.0-errata03-os-part1-protocol-complete.html#_Toc453752313). The content in this article summarizes the specification requirements and provides Dataverse specific information and examples.
  
<a name="bkmk_Whentousebatchrequests"></a>

## When to use batch requests

Batch requests provide two capabilities that can be used together:

- You can send requests for multiple operations with a single HTTP request.

   - Batch requests can contain up to 1000 individual requests and can't contain other batch requests.
   - This is equivalent to the `ExecuteMultiple` message available in the SDK for .NET. More information: [Execute multiple requests using the Organization service](../org-service/execute-multiple-requests.md)

- You can group requests for operations together so that they're included as a single transaction using [Change sets](#change-sets).

   - You may want to create, update, or delete a set of related records in a way that guarantees that all the operations succeed or fail as a group.
   - This is equivalent to the `ExecuteTransaction` message available in the SDK for .NET. More information: [Execute messages in a single database transaction](../org-service/use-executetransaction.md)
   
   > [!NOTE]
   > Remember that associated entities can be created in a single operation more easily than using a batch request. More information:  [Create related table rows in one operation](create-entity-web-api.md#create-related-table-rows-in-one-operation)


Batch requests are also sometimes used to sent `GET` requests where the length of the URL may exceed the maximum allowed URL length. This is because the URL for the request is included in the body of the message where a longer URL, up to 64 KB (65,536 characters), is allowed. Sending complex queries using FetchXml can result in long URLs. More information: [Use FetchXML within a batch request](use-fetchxml-web-api.md#use-fetchxml-within-a-batch-request)

Compared to other operations that can be performed using the Web API, batch requests are more difficult to compose. The raw request and response bodies are essentially a text document that must match specific requirements. To access the data in a response, you'll need to parse the text in the response or locate a helper library to access the data in the response.  See [.NET helper methods](#net-helper-methods).

  
<a name="bkmk_BatchRequests"></a>

## Batch requests

Use a `POST` request to submit a batch operation that contains multiple requests.
  
The `POST` request containing the batch must have a [Content-Type](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Type) header with a value set to `multipart/mixed` with a `boundary` set to include the identifier of the batch using this pattern:  
  
```
POST [Organization Uri]/api/data/v9.2/$batch HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: multipart/mixed; boundary="batch_<unique identifier>"
```  
  
The unique identifier doesn't need to be a GUID, but should be unique.

Each item within the batch must be preceded by the batch identifier with a `Content-Type` and [Content-Transfer-Encoding](https://www.w3.org/Protocols/rfc1341/5_Content-Transfer-Encoding.html) header like the following example:  
  
```  
--batch_<unique identifier>
Content-Type: application/http
Content-Transfer-Encoding: binary
```  
  
The end of the batch request must contain a termination indicator like the following example:  
  
```  
--batch_<unique identifier>--
```

The following is an example of a batch request without change sets. This example:
- Creates three task records associated with an account with `accountid` equal to `00000000-0000-0000-0000-000000000001`.
- Retrieves the task records associated with the account.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/$batch HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: multipart/mixed; boundary="batch_80dd1615-2a10-428a-bb6f-0e559792721f"

--batch_80dd1615-2a10-428a-bb6f-0e559792721f
Content-Type: application/http
Content-Transfer-Encoding: binary

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Task 1 in batch",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--batch_80dd1615-2a10-428a-bb6f-0e559792721f
Content-Type: application/http
Content-Transfer-Encoding: binary

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Task 2 in batch",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--batch_80dd1615-2a10-428a-bb6f-0e559792721f
Content-Type: application/http
Content-Transfer-Encoding: binary

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Task 3 in batch",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--batch_80dd1615-2a10-428a-bb6f-0e559792721f
Content-Type: application/http
Content-Transfer-Encoding: binary

GET /api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001)/Account_Tasks?$select=subject HTTP/1.1


--batch_80dd1615-2a10-428a-bb6f-0e559792721f--

```

## Batch responses

When successful, the batch response will return HTTP Status `200 OK`, and each item in the response will be separated by a `Guid` unique identifier value that isn't the same as the batch request value.

```http
--batchresponse_<unique identifier>
Content-Type: application/http
Content-Transfer-Encoding: binary
```

The end of the batch response will contain a termination indicator like the following example:  
  
```http
--batchresponse_<unique identifier>--
```

The following is the response to the batch request example above.

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_01346794-f2e2-4d45-8cc2-f97e09fe8916
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization Uri]/api/data/v9.2/tasks(d31ba648-c592-ed11-aad1-000d3a993550)
OData-EntityId: [Organization Uri]/api/data/v9.2/tasks(d31ba648-c592-ed11-aad1-000d3a993550)


--batchresponse_01346794-f2e2-4d45-8cc2-f97e09fe8916
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization Uri]/api/data/v9.2/tasks(d41ba648-c592-ed11-aad1-000d3a993550)
OData-EntityId: [Organization Uri]/api/data/v9.2/tasks(d41ba648-c592-ed11-aad1-000d3a993550)


--batchresponse_01346794-f2e2-4d45-8cc2-f97e09fe8916
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization Uri]/api/data/v9.2/tasks(d51ba648-c592-ed11-aad1-000d3a993550)
OData-EntityId: [Organization Uri]/api/data/v9.2/tasks(d51ba648-c592-ed11-aad1-000d3a993550)


--batchresponse_01346794-f2e2-4d45-8cc2-f97e09fe8916
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal; odata.streaming=true
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#tasks(subject)",
  "value": [
    {
      "@odata.etag": "W/\"77180907\"",
      "subject": "Task 1 in batch",
      "activityid": "d31ba648-c592-ed11-aad1-000d3a993550"
    },
    {
      "@odata.etag": "W/\"77180910\"",
      "subject": "Task 2 in batch",
      "activityid": "d41ba648-c592-ed11-aad1-000d3a993550"
    },
    {
      "@odata.etag": "W/\"77180913\"",
      "subject": "Task 3 in batch",
      "activityid": "d51ba648-c592-ed11-aad1-000d3a993550"
    }
  ]
}
--batchresponse_01346794-f2e2-4d45-8cc2-f97e09fe8916--

```


<a name="bkmk_ChangeSets"></a>

## Change sets

In addition to individual requests, a batch request can include change sets. When multiple operations are contained in a change set, all the operations are considered *atomic*. This means that if any one of the operations fails, any completed operations will be rolled back.

> [!NOTE]
> `GET` request are not allowed within change sets. A `GET` operation should not change data, therefore they don't belong within a change set.


Like a batch request, change sets must have a `Content-Type` header with value set to `multipart/mixed` with a `boundary` set to include the identifier of the change set using this pattern:  
  
```
Content-Type: multipart/mixed; boundary="changeset_<unique identifier>"
```  
  
The unique identifier doesn't need to be a GUID, but should be unique. Each item within the change set must be preceded by the change set identifier with a `Content-Type` and `Content-Transfer-Encoding` header like the following:  
  
```  
--changeset_<unique identifier>
Content-Type: application/http
Content-Transfer-Encoding: binary
```  
  
Change sets can also include a `Content-ID` header with a unique value. This value, when prefixed with `$`, represents a variable that contains the Uri for any entity created in that operation. For example, when you set the value of `1`, you can refer to that entity using `$1` later in your change set. More information: [Reference URIs in an operation](#reference-uris-in-an-operation)
  
The end of the change set must contain a termination indicator like the following:  
  
```  
--changeset_<unique identifier>--
```  

The following example shows the use of a change set to:
- Group the creation of three tasks associated with an account with `accountid` value `00000000-0000-0000-0000-000000000001`.
- Retrieve the accounts created using a GET request outside of the changeset.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/$batch HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: multipart/mixed; boundary="batch_22975cad-7f57-410d-be15-6363209367ea"

--batch_22975cad-7f57-410d-be15-6363209367ea
Content-Type: multipart/mixed; boundary="changeset_246e6bfe-89a4-4c77-b293-7a433f082e8a"

--changeset_246e6bfe-89a4-4c77-b293-7a433f082e8a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Task 1 in batch",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--changeset_246e6bfe-89a4-4c77-b293-7a433f082e8a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Task 2 in batch",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--changeset_246e6bfe-89a4-4c77-b293-7a433f082e8a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 3

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Task 3 in batch",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--changeset_246e6bfe-89a4-4c77-b293-7a433f082e8a--

--batch_22975cad-7f57-410d-be15-6363209367ea
Content-Type: application/http
Content-Transfer-Encoding: binary

GET /api/data/v9.2/accounts(00000000-0000-0000-0000-000000000001)/Account_Tasks?$select=subject HTTP/1.1


--batch_22975cad-7f57-410d-be15-6363209367ea--

```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_f27ef42d-51b0-4685-bac9-f468f844de2f
Content-Type: multipart/mixed; boundary=changesetresponse_64cc3fff-023a-45b0-b29d-df21583ffa15

--changesetresponse_64cc3fff-023a-45b0-b29d-df21583ffa15
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization Uri]/api/data/v9.2/tasks(e73ffc82-e292-ed11-aad1-000d3a9933c9)
OData-EntityId: [Organization Uri]/api/data/v9.2/tasks(e73ffc82-e292-ed11-aad1-000d3a9933c9)


--changesetresponse_64cc3fff-023a-45b0-b29d-df21583ffa15
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization Uri]/api/data/v9.2/tasks(e83ffc82-e292-ed11-aad1-000d3a9933c9)
OData-EntityId: [Organization Uri]/api/data/v9.2/tasks(e83ffc82-e292-ed11-aad1-000d3a9933c9)


--changesetresponse_64cc3fff-023a-45b0-b29d-df21583ffa15
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 3

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization Uri]/api/data/v9.2/tasks(e93ffc82-e292-ed11-aad1-000d3a9933c9)
OData-EntityId: [Organization Uri]/api/data/v9.2/tasks(e93ffc82-e292-ed11-aad1-000d3a9933c9)


--changesetresponse_64cc3fff-023a-45b0-b29d-df21583ffa15--
--batchresponse_f27ef42d-51b0-4685-bac9-f468f844de2f
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal; odata.streaming=true
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#tasks(subject)",
  "value": [
    {
      "@odata.etag": "W/\"77181173\"",
      "subject": "Task 1 in batch",
      "activityid": "e73ffc82-e292-ed11-aad1-000d3a9933c9"
    },
    {
      "@odata.etag": "W/\"77181176\"",
      "subject": "Task 2 in batch",
      "activityid": "e83ffc82-e292-ed11-aad1-000d3a9933c9"
    },
    {
      "@odata.etag": "W/\"77181179\"",
      "subject": "Task 3 in batch",
      "activityid": "e93ffc82-e292-ed11-aad1-000d3a9933c9"
    }
  ]
}
--batchresponse_f27ef42d-51b0-4685-bac9-f468f844de2f--

```

### Reference URIs in an operation

Within changesets you can use `$parameter` such as `$1`, `$2`, etc. to reference URIs returned for new entities created earlier in the same changeset. For more information, see the OData v4.0 specification: [11.7.3.1 Referencing Requests in a Change Set](http://docs.oasis-open.org/odata/odata/v4.0/os/part1-protocol/odata-v4.0-os-part1-protocol.html#_Toc372793752).

This section shows various examples on how `$parameter` can be used in the request body of a batch operation to reference URIs.

#### Reference URIs in request body

The below example shows how two URI references can be used in a single operation.

**Request:**

```http
POST [Organization URI]/api/data/v9.2/$batch HTTP/1.1
Content-Type:  multipart/mixed;boundary=batch_AAA123
Accept:  application/json
OData-MaxVersion:  4.0
OData-Version:  4.0

--batch_AAA123
Content-Type: multipart/mixed; boundary=changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

POST [Organization URI]/api/data/v9.2/leads HTTP/1.1
Content-Type: application/json

{
    "firstname":"first name",
    "lastname":"last name"
}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

POST [Organization URI]/api/data/v9.2/contacts HTTP/1.1
Content-Type: application/json

{"firstname":"first name"}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 3

POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1
Content-Type: application/json

{
    "name":"IcM Account",
    "originatingleadid@odata.bind":"$1",
    "primarycontactid@odata.bind":"$2"
}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab--
--batch_AAA123--
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_3cace264-86ea-40fe-83d3-954b336c0f4a
Content-Type: multipart/mixed; boundary=changesetresponse_1a5db8a1-ec98-42c4-81f6-6bc6adcfa4bc

--changesetresponse_1a5db8a1-ec98-42c4-81f6-6bc6adcfa4bc
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.2/leads(425195a4-7a75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.2/leads(425195a4-7a75-e911-a97a-000d3a34a1bd)

--changesetresponse_1a5db8a1-ec98-42c4-81f6-6bc6adcfa4bc
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.2/contacts(495195a4-7a75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.2/contacts(495195a4-7a75-e911-a97a-000d3a34a1bd)

--changesetresponse_1a5db8a1-ec98-42c4-81f6-6bc6adcfa4bc
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 3

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.2/accounts(4f5195a4-7a75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.2/accounts(4f5195a4-7a75-e911-a97a-000d3a34a1bd)

--changesetresponse_1a5db8a1-ec98-42c4-81f6-6bc6adcfa4bc--
--batchresponse_3cace264-86ea-40fe-83d3-954b336c0f4a--
```

#### Reference URI in request URL

The example given below shows how you can reference a URI using `$1` in the URL of a subsequent request.

**Request:**

```http
POST [Organization URI]/api/data/v9.2/$batch HTTP/1.1
Content-Type:  multipart/mixed;boundary=batch_AAA123
Accept:  application/json
OData-MaxVersion:  4.0
OData-Version:  4.0

--batch_AAA123
Content-Type: multipart/mixed; boundary=changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

POST [Organization URI]/api/data/v9.2/contacts HTTP/1.1
Content-Type: application/json

{
  "firstname":"First Name",
  "lastname":"Last name"
}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Transfer-Encoding: binary
Content-Type: application/http
Content-ID: 2

PUT $1/lastname HTTP/1.1
Content-Type: application/json

{
  "value":"BBBBB"
}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab--
--batch_AAA123--
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_2cb48f48-39a8-41ea-aa52-132fa8ab3c2d
Content-Type: multipart/mixed; boundary=changesetresponse_d7528170-3ef3-41bd-be8e-eac971a8d9d4

--changesetresponse_d7528170-3ef3-41bd-be8e-eac971a8d9d4
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

HTTP/1.1 204 No Content
OData-Version: 4.0
Location:[Organization URI]/api/data/v9.2/contacts(f8ea5d2c-8c75-e911-a97a-000d3a34a1bd)
OData-EntityId:[Organization URI]/api/data/v9.2/contacts(f8ea5d2c-8c75-e911-a97a-000d3a34a1bd)


--changesetresponse_d7528170-3ef3-41bd-be8e-eac971a8d9d4
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

HTTP/1.1 204 No Content
OData-Version: 4.0


--changesetresponse_d7528170-3ef3-41bd-be8e-eac971a8d9d4--
--batchresponse_2cb48f48-39a8-41ea-aa52-132fa8ab3c2d--
```

#### Reference URIs in URL and request body using @odata.id

The example given below shows how to link a Contact entity record to an Account entity record. The URI of Account entity record is referenced as `$1` and URI of Contact entity record is referenced as `$2`.

**Request:**

```http
POST [Organization URI]/api/data/v9.2/$batch HTTP/1.1
Content-Type:multipart/mixed;boundary=batch_AAA123
Accept:application/json
OData-MaxVersion:4.0
OData-Version:4.0

--batch_AAA123
Content-Type: multipart/mixed; boundary=changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type:application/http
Content-Transfer-Encoding:binary
Content-ID:1

POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1
Content-Type: application/json

{ "name":"Account Name"}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type:application/http
Content-Transfer-Encoding:binary
Content-ID:2

POST [Organization URI]/api/data/v9.2/contacts HTTP/1.1
Content-Type:application/json

{ "firstname":"Contact first name"}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type:application/http
Content-Transfer-Encoding:binary
Content-ID:3

PUT $1/primarycontactid/$ref HTTP/1.1
Content-Type:application/json

{"@odata.id":"$2"}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab--
--batch_AAA123--
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_0740a25c-d8e1-41a5-9202-1b50a297864c
Content-Type: multipart/mixed; boundary=changesetresponse_19ca0da8-d8bb-4273-a3f7-fe0d0fadfe5f

--changesetresponse_19ca0da8-d8bb-4273-a3f7-fe0d0fadfe5f
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

HTTP/1.1 204 No Content
OData-Version: 4.0
Location:[Organization URI]/api/data/v9.2/accounts(3dcf8c02-8c75-e911-a97a-000d3a34a1bd)
OData-EntityId:[Organization URI]/api/data/v9.2/accounts(3dcf8c02-8c75-e911-a97a-000d3a34a1bd)

--changesetresponse_19ca0da8-d8bb-4273-a3f7-fe0d0fadfe5f
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

HTTP/1.1 204 No Content
OData-Version: 4.0
Location:[Organization URI]/api/data/v9.2/contacts(43cf8c02-8c75-e911-a97a-000d3a34a1bd)
OData-EntityId:[Organization URI]/api/data/v9.2/contacts(43cf8c02-8c75-e911-a97a-000d3a34a1bd)

--changesetresponse_19ca0da8-d8bb-4273-a3f7-fe0d0fadfe5f
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 3

HTTP/1.1 204 No Content
OData-Version: 4.0

--changesetresponse_19ca0da8-d8bb-4273-a3f7-fe0d0fadfe5f--
--batchresponse_0740a25c-d8e1-41a5-9202-1b50a297864c--
```

#### Reference URIs in URL and navigation properties

The example given below shows how to use the Organization URI of a Contact record and link it to an Account record using the `primarycontactid` single-valued navigation property. The URI of the Account entity record is referenced as `$1` and the URI of Contact entity record is referenced as `$2` in the `PATCH` request.

**Request:**

```http
POST [Organization URI]/api/data/v9.2/$batch HTTP/1.1
Content-Type:multipart/mixed;boundary=batch_AAA123
Accept:application/json
OData-MaxVersion:4.0
OData-Version:4.0

--batch_AAA123
Content-Type: multipart/mixed; boundary=changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1
Content-Type: application/json

{ "name":"Account name"}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

POST [Organization URI]/api/data/v9.2/contacts HTTP/1.1
Content-Type: application/json

{
  "firstname":"Contact first name"
}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 3

PATCH $1 HTTP/1.1
Content-Type: application/json

{
  "primarycontactid@odata.bind":"$2"
}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab--
--batch_AAA123--
```
**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_9595d3ae-48f6-414f-a3aa-a3a33559859e
Content-Type: multipart/mixed; boundary=changesetresponse_0c1567a5-ad0d-48fa-b81d-e6db05cad01c

--changesetresponse_0c1567a5-ad0d-48fa-b81d-e6db05cad01c
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.2/accounts(6cd81853-7b75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.2/accounts(6cd81853-7b75-e911-a97a-000d3a34a1bd)

--changesetresponse_0c1567a5-ad0d-48fa-b81d-e6db05cad01c
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.2/contacts(6ed81853-7b75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.2/contacts(6ed81853-7b75-e911-a97a-000d3a34a1bd)

--changesetresponse_0c1567a5-ad0d-48fa-b81d-e6db05cad01c
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 3

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.2/accounts(6cd81853-7b75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.2/accounts(6cd81853-7b75-e911-a97a-000d3a34a1bd)

--changesetresponse_0c1567a5-ad0d-48fa-b81d-e6db05cad01c--
--batchresponse_9595d3ae-48f6-414f-a3aa-a3a33559859e--
```

> [!NOTE]
> Referencing a `Content-ID` before it has been declared in the request body will return the error **HTTP 400** Bad request.
>
> The example given below shows a request body that can cause this error.
> 
> **Request body**
> 
> ```http
> --batch_AAA123
> Content-Type: multipart/mixed; boundary=changeset_BBB456
> 
> --changeset_BBB456
> Content-Type: application/http
> Content-Transfer-Encoding:binary
> Content-ID: 2
> 
> POST [Organization URI]/api/data/v9.2/phonecalls HTTP/1.1
> Content-Type: application/json;type=entry
> 
> {
>     "phonenumber":"911",
>     "regardingobjectid_account_phonecall@odata.bind" : "$1"
> }
> 
> --changeset_BBB456
> Content-Type: application/http
> Content-Transfer-Encoding:binary
> Content-ID: 1
> 
> POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1
> Content-Type: application/json;type=entry
> 
> {
>     "name":"QQQQ",
>     "revenue": 1.50
> }
> 
> --changeset_BBB456--
> --batch_AAA123--
> ```
>
> **Response:**
> 
> ```http
> HTTP 400 Bad Request
> Content-ID Reference: '$1' does not exist in the batch context.
> ```

<a name="bkmk_handling_errors"></a>

## Handling errors

When an error occurs for a request within a batch, the error for that request will be returned for the batch request and more requests won't be processed.

You can use the `Prefer: odata.continue-on-error` request header to specify that more requests be processed when errors occur. The batch request will return `200 OK` and individual response errors will be returned in the batch response body.

More information: [OData Specification: 8.2.8.3 Preference odata.continue-on-error](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html#_Toc406398236)

<a name="bkmk_Example"></a>

### Example

The following example attempts to create three task records associated with an account with `accountid` equal to `00000000-0000-0000-0000-000000000001`, but the length of the `subject` property for the first task is too long.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/$batch HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: multipart/mixed; boundary="batch_431faf5a-f979-4ee6-a374-d242f8962d41"
Content-Length: 1335

--batch_431faf5a-f979-4ee6-a374-d242f8962d41
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 436

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Subject is too long xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--batch_431faf5a-f979-4ee6-a374-d242f8962d41
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 250

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Task 2 in batch",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--batch_431faf5a-f979-4ee6-a374-d242f8962d41
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 250

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Task 3 in batch",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--batch_431faf5a-f979-4ee6-a374-d242f8962d41--

```

Without setting the `Prefer: odata.continue-on-error` request header, the batch fails on the first request in the batch. The batch error represents the error of the first failing request.

**Response:**

```http
HTTP/1.1 400 BadRequest
OData-Version: 4.0

--batchresponse_156da4b8-cd2c-4862-a911-4aaab97c001a
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 400 Bad Request
REQ_ID: 5ecd1cb3-1730-4ffc-909c-d44c22270026
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{"error":{"code":"0x80044331","message":"A validation error occurred.  The length of the 'subject' attribute of the 'task' entity exceeded the maximum allowed length of '200'."}}
--batchresponse_156da4b8-cd2c-4862-a911-4aaab97c001a--

```

When the `Prefer: odata.continue-on-error` request header is applied to the batch request, the batch request succeeds with a status of `200 OK` and the failure of the first request is returned as part of the body.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/$batch HTTP/1.1
Prefer: odata.continue-on-error
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: multipart/mixed; boundary="batch_662d4610-7f12-4895-ac4a-3fdf77cc10a1"
Content-Length: 1338

--batch_662d4610-7f12-4895-ac4a-3fdf77cc10a1
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 439

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Subject is too long xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--batch_662d4610-7f12-4895-ac4a-3fdf77cc10a1
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 250

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Task 2 in batch",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--batch_662d4610-7f12-4895-ac4a-3fdf77cc10a1
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 250

POST /api/data/v9.2/tasks HTTP/1.1
Content-Type: application/json; type=entry

{
  "subject": "Task 3 in batch",
  "regardingobjectid_account_task@odata.bind": "accounts(00000000-0000-0000-0000-000000000001)"
}
--batch_662d4610-7f12-4895-ac4a-3fdf77cc10a1--

```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_f44bd09d-573f-4a30-bca0-2e500ee7e139
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 400 Bad Request
REQ_ID: de4c5227-4a28-4ebd-8ced-3392ece1697b
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{"error":{"code":"0x80044331","message":"A validation error occurred.  The length of the 'subject' attribute of the 'task' entity exceeded the maximum allowed length of '200'."}}
--batchresponse_f44bd09d-573f-4a30-bca0-2e500ee7e139
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization Uri]/api/data/v9.2/tasks(aed2ae8b-3c94-ed11-aad1-000d3a9933c9)
OData-EntityId: [Organization Uri]/api/data/v9.2/tasks(aed2ae8b-3c94-ed11-aad1-000d3a9933c9)


--batchresponse_f44bd09d-573f-4a30-bca0-2e500ee7e139
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization Uri]/api/data/v9.2/tasks(b181a991-3c94-ed11-aad1-000d3a9933c9)
OData-EntityId: [Organization Uri]/api/data/v9.2/tasks(b181a991-3c94-ed11-aad1-000d3a9933c9)


--batchresponse_f44bd09d-573f-4a30-bca0-2e500ee7e139--

```

## .NET helper methods

The [WebAPIService class library (C#)](samples/webapiservice.md) is a sample helper class library project used for Web API samples written in .NET. It demonstrates one way that common patterns used with Web API can be reused.

> [!NOTE]
> This sample library is a helper that is used by all the Dataverse C# Web API samples, but it is not an SDK. It is tested only to confirm that the samples that use it run successfully. This sample code is provided 'as-is' with no warranty for reuse.

This library includes classes for creating batch requests and processing responses.  For example, variations on following code were used to generate many of the HTTP request and response examples in this article.

```csharp
using PowerApps.Samples;
using PowerApps.Samples.Batch;

static async Task Main()
{
    Config config = App.InitializeApp();

    var service = new Service(config);

    JObject account = new()
    {
        {"name","test account" }
    };

    EntityReference accountRef = await service.Create("accounts", account);

    List<HttpRequestMessage> createRequests = new() {
        new CreateRequest("tasks",new JObject(){
            {"subject","Task 2 in batch" },
            {"regardingobjectid_account_task@odata.bind", accountRef.Path }
        }),
        new CreateRequest("tasks",new JObject(){
            {"subject","Task 2 in batch" },
            {"regardingobjectid_account_task@odata.bind", accountRef.Path }
        }),
        new CreateRequest("tasks",new JObject(){
            {"subject","Task 3 in batch" },
            {"regardingobjectid_account_task@odata.bind", accountRef.Path }
        })
    };

    BatchRequest batchRequest = new(service.BaseAddress)
    {
        Requests = createRequests,
        ContinueOnError = true
    };

    var batchResponse = await service.SendAsync<BatchResponse>(batchRequest);

    batchResponse.HttpResponseMessages.ForEach(response => {

        string path = response.As<CreateResponse>().EntityReference.Path;
        Console.WriteLine($"Task created at: {path}");
        
    });
}
```

**output**

```
Task created at: tasks(6743adfa-4a94-ed11-aad1-000d3a9933c9)
Task created at: tasks(6843adfa-4a94-ed11-aad1-000d3a9933c9)
Task created at: tasks(6943adfa-4a94-ed11-aad1-000d3a9933c9)
```

Within this library, there are some methods that you may find useful in your .NET code.

More information:

 - [WebAPIService Batch](samples/webapiservice.md#batch)
 - [Web API Data operations Samples (C#)](web-api-samples-csharp.md)

### .NET HttpRequestMessage to HttpMessageContent example

In .NET, you must send batch requests as <xref:System.Net.Http.MultipartContent> that is a collection of <xref:System.Net.Http.HttpContent>. `HttpMessageContent` inherits from `HttpContent`. The [WebAPIService class library (C#)](samples/webapiservice.md) [BatchRequest class](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/C%23-NETx/WebAPIService/Batch/BatchRequest.cs) uses the following private static `ToMessageContent` method to convert <xref:System.Net.Http.HttpRequestMessage> to `HttpMessageContent` that can be added to `MultipartContent`.

```csharp
/// <summary>
/// Converts a HttpRequestMessage to HttpMessageContent
/// </summary>
/// <param name="request">The HttpRequestMessage to convert.</param>
/// <returns>HttpMessageContent with the correct headers.</returns>
private HttpMessageContent ToMessageContent(HttpRequestMessage request)
{

    //Relative URI is not allowed with MultipartContent
    request.RequestUri = new Uri(
        baseUri: ServiceBaseAddress,
        relativeUri: request.RequestUri.ToString());

    if (request.Content != null)
    {
        if (request.Content.Headers.Contains("Content-Type"))
        {
            request.Content.Headers.Remove("Content-Type");
        }
        request.Content.Headers.Add("Content-Type", "application/json;type=entry");
    }

    HttpMessageContent messageContent = new(request);

    if (messageContent.Headers.Contains("Content-Type"))
    {
        messageContent.Headers.Remove("Content-Type");
    }
    messageContent.Headers.Add("Content-Type", "application/http");
    messageContent.Headers.Add("Content-Transfer-Encoding", "binary");

    return messageContent;

}
```

### .NET Parse batch response example

The [WebAPIService class library (C#)](samples/webapiservice.md) [BatchResponse class](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/C%23-NETx/WebAPIService/Batch/BatchResponse.cs) uses the following private static `ParseMultipartContent` method to parse the body of a batch response into a `List` of [HttpResponseMessage](xref:System.Net.Http.HttpResponseMessage) that can be processed like individual responses.

```csharp
/// <summary>
/// Processes the Multi-part content returned from the batch into a list of responses.
/// </summary>
/// <param name="content">The Content of the response.</param>
/// <returns></returns>
private static async Task<List<HttpResponseMessage>> ParseMultipartContent(HttpContent content)
{
   MultipartMemoryStreamProvider batchResponseContent = await content.ReadAsMultipartAsync();

   List<HttpResponseMessage> responses = new();

   if (batchResponseContent?.Contents != null)
   {
         batchResponseContent.Contents.ToList().ForEach(async httpContent =>
         {

            //This is true for changesets
            if (httpContent.IsMimeMultipartContent())
            {
               //Recursive call
               responses.AddRange(await ParseMultipartContent(httpContent));
            }

            //This is for individual responses outside of a change set.
            else
            {
               //Must change Content-Type for ReadAsHttpResponseMessageAsync method to work.
               httpContent.Headers.Remove("Content-Type");
               httpContent.Headers.Add("Content-Type", "application/http;msgtype=response");

               HttpResponseMessage httpResponseMessage = await httpContent.ReadAsHttpResponseMessageAsync();

               if (httpResponseMessage != null)
               {
                     responses.Add(httpResponseMessage);
               }
            }
         });
   }

   return responses;
}
```

### See also

[Perform operations using the Web API](perform-operations-web-api.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
