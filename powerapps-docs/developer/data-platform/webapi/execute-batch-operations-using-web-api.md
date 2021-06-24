---
title: "Execute batch operations using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Batch operation lets you group multiple operations in a single HTTP request. Read how to execute batch operations using the Web API"
ms.custom: ""
ms.date: 05/04/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 799b2346-bda1-4a26-a330-79d0927a7743
caps.latest.revision: 11
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

# Execute batch operations using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can group multiple operations into a single HTTP request using a batch operation. These operations will be performed sequentially in the order they are specified.
  
<a name="bkmk_Whentousebatchrequests"></a>

## When to use batch requests

The value that batch requests provide is that they can include change sets, which provide a way to bundle a number of operations that either succeed or fail as a group. Compared to other operations that can be performed using the web API, they are more difficult to compose without some object model that includes serialization of objects or a deeper understanding of the HTTP protocol because the request body is essentially a text document that must match very specific requirements.  
  
Remember that associated entities can be created in a single operation more easily than using a batch request. Batch requests are best used when performing operations on entities that aren't associated with each other when all the operations must be performed in a single transactional operation.  
  
Also, the responses returned are essentially text documents rather than objects that can easily be parsed into JSON. You'll need to parse the text in the response or locate a helper library to access the data in the response.  
 
>[!NOTE]
>  Batch requests can contain up to 1000 individual requests and cannot contain other batch requests.
>
>  URLs for `GET` requests sent with a batch are limited to 32768 characters.

  
<a name="bkmk_BatchRequests"></a> 

## Batch requests

Use a POST request to submit a batch operation that contains multiple requests. A batch request can include GET requests and change sets. To use the transactional capabilities of batch requests, only operations that will change data can be included within a change set. GET requests must not be included in the change set.  
  
The POST request containing the batch must have a Content-Type header with a value set to multipart/mixed with a boundary set to include the identifier of the batch using this pattern:  
  
```  
--batch_<unique identifier>
```  
  
The unique identifier doesn't need to be a GUID, but should be unique. Each item within the batch must be preceded by the batch identifier with a Content-Type and Content-Transfer-Encoding header like the following:  
  
```  
--batch_WKQS9Yui9r
Content-Type: application/http
Content-Transfer-Encoding:binary
```  
  
The end of the batch must contain a termination indicator like the following:  
  
```  
--batch_WKQS9Yui9r--
```   
  
<a name="bkmk_ChangeSets"></a>

## Change sets

When multiple operations are contained in a change set, all the operations are considered atomic, which means that if any one of the operations fail, any completed operations will be rolled back. Like a batch request, change sets must have a Content-Type header with value set to multipart/mixed with a boundary set to include the identifier of the change set using this pattern:  
  
```  
--changeset_<unique identifier>
```  
  
The unique identifier doesn't need to be a GUID, but should be unique. Each item within the change set must be preceded by the change set identifier with a Content-Type and Content-Transfer-Encoding header like the following:  
  
```  
--changeset_BBB456
Content-Type: application/http
Content-Transfer-Encoding:binary
```  
  
Change sets can also include a Content-ID header with a unique value. This value, when prefixed with `$`, represents a variable that contains the Uri for any entity created in that operation. For example, when you set the value of 1, you can refer to that entity using `$1` later in your change set.  
  
The end of the change set must contain a termination indicator like the following:  
  
```  
--changeset_BBB456--
```  
  
<a name="bkmk_Example"></a>

## Example

The following example includes a batch with a unique identifier of AAA123 and a change set with a unique identifier of BBB456.  
  
Within the change set, two tasks are created using POST and associated with an existing account with accountid = 00000000-0000-0000-000000000001.  
  
Finally, a GET request is included outside the change set to return all six tasks associated with the account, including the two that were created in the batch request.  
  
 **Request**

```http 
POST[Organization URI]/api/data/v9.1/$batch HTTP/1.1
Content-Type: multipart/mixed;boundary=batch_AAA123
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0

--batch_AAA123
Content-Type: multipart/mixed;boundary=changeset_BBB456

--changeset_BBB456
Content-Type: application/http
Content-Transfer-Encoding:binary
Content-ID: 1

POST[Organization URI]/api/data/v9.1/tasks HTTP/1.1
Content-Type: application/json;type=entry

{"subject":"Task 1 in batch","regardingobjectid_account_task@odata.bind":"[Organization URI]/api/data/v9.1/accounts(00000000-0000-0000-000000000001)"}
--changeset_BBB456
Content-Type: application/http
Content-Transfer-Encoding:binary
Content-ID: 2

POST[Organization URI]/api/data/v9.1/tasks HTTP/1.1
Content-Type: application/json;type=entry

{"subject":"Task 2 in batch","regardingobjectid_account_task@odata.bind":"[Organization URI]/api/data/v9.1/accounts(00000000-0000-0000-000000000001)"}
--changeset_BBB456--

--batch_AAA123
Content-Type: application/http
Content-Transfer-Encoding:binary

GET[Organization URI]/api/data/v9.1/accounts(00000000-0000-0000-000000000001)/Account_Tasks?$select=subject HTTP/1.1
Accept: application/json

--batch_AAA123--
```  
  
 **Response**

```http
--batchresponse_c1bd45c1-dd81-470d-b897-e965846aad2f
Content-Type: multipart/mixed; boundary=changesetresponse_ff83b4f1-ab48-430c-b81c-926a2c596abc

--changesetresponse_ff83b4f1-ab48-430c-b81c-926a2c596abc
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

HTTP/1.1 204 No Content
OData-Version: 4.0
Location:[Organization URI]/api/data/v9.1/tasks(a59c24f3-fafc-e411-80dd-00155d2a68cb)
OData-EntityId:[Organization URI]/api/data/v9.1/tasks(a59c24f3-fafc-e411-80dd-00155d2a68cb)

--changesetresponse_ff83b4f1-ab48-430c-b81c-926a2c596abc
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

HTTP/1.1 204 No Content
OData-Version: 4.0
Location:[Organization URI]/api/data/v9.1/tasks(a69c24f3-fafc-e411-80dd-00155d2a68cb)
OData-EntityId:[Organization URI]/api/data/v9.1/tasks(a69c24f3-fafc-e411-80dd-00155d2a68cb)

--changesetresponse_ff83b4f1-ab48-430c-b81c-926a2c596abc--
--batchresponse_c1bd45c1-dd81-470d-b897-e965846aad2f
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
  "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#tasks(subject)","value":[
    {
      "@odata.etag":"W/\"474122\"","subject":"Task Created with Test Account","activityid":"919c24f3-fafc-e411-80dd-00155d2a68cb"
    },{
      "@odata.etag":"W/\"474125\"","subject":"Task 1","activityid":"a29c24f3-fafc-e411-80dd-00155d2a68cb"
    },{
      "@odata.etag":"W/\"474128\"","subject":"Task 2","activityid":"a39c24f3-fafc-e411-80dd-00155d2a68cb"
    },{
      "@odata.etag":"W/\"474131\"","subject":"Task 3","activityid":"a49c24f3-fafc-e411-80dd-00155d2a68cb"
    },{
      "@odata.etag":"W/\"474134\"","subject":"Task 1 in batch","activityid":"a59c24f3-fafc-e411-80dd-00155d2a68cb"
    },{
      "@odata.etag":"W/\"474137\"","subject":"Task 2 in batch","activityid":"a69c24f3-fafc-e411-80dd-00155d2a68cb"
    }
  ]
}
--batchresponse_c1bd45c1-dd81-470d-b897-e965846aad2f--
```  
Include `odata.include-annotations` preference header with the `GET` requests and set its value to "*" to specify that all annotations related to the properties be returned.

```HTTP
--batch_AAA123
Content-Type: application/http
Content-Transfer-Encoding:binary

GET[Organization URI]/api/data/v9.1/accounts(00000000-0000-0000-000000000001)?$select=name,telephone1,emailaddress1,shippingmethodcode,customersizecode,accountratingcode,followemail,donotemail,donotphone,statuscode HTTP/1.1
Accept: application/json
Prefer: odata.include-annotations="*"

--batch_AAA123--
```
For more information about preference headers, see [Header Prefer](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part1-protocol/odata-v4.0-errata03-os-part1-protocol-complete.html#_Toc453752234).

## Reference URIs in an operation

You can use `$parameter` such as `$1`, `$2`, etc to reference URIs returned for new entities created earlier in the same changeset in a batch request. For more information see the OData v4.0 specification: [11.7.3.1 Referencing Requests in a Change Set](http://docs.oasis-open.org/odata/odata/v4.0/os/part1-protocol/odata-v4.0-os-part1-protocol.html#_Toc372793752).

This section shows various examples on how `$parameter` can be used in the request body of a batch operation to reference URIs.

### Reference URIs in request body

The below example shows how two URI references can be used in a single operation.

**Request**

```http
POST [Organization URI]/api/data/v9.1/$batch HTTP/1.1
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

POST [Organization URI]/api/data/v9.1/leads HTTP/1.1
Content-Type: application/json

{
    "firstname":"aaa",
    "lastname":"bbb"
}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

POST [Organization URI]/api/data/v9.1/contacts HTTP/1.1
Content-Type: application/json

{"@odata.type":"Microsoft.Dynamics.CRM.contact","firstname":"Oncall Contact-1111"}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 3

POST [Organization URI]/api/data/v9.1/accounts HTTP/1.1
Content-Type: application/json

{
    "name":"IcM Account",
    "originatingleadid@odata.bind":"$1",
    "primarycontactid@odata.bind":"$2"
}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab--
--batch_AAA123--
```

**Response**

```http
200 OK

--batchresponse_3cace264-86ea-40fe-83d3-954b336c0f4a
Content-Type: multipart/mixed; boundary=changesetresponse_1a5db8a1-ec98-42c4-81f6-6bc6adcfa4bc

--changesetresponse_1a5db8a1-ec98-42c4-81f6-6bc6adcfa4bc
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.1/leads(425195a4-7a75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.1/leads(425195a4-7a75-e911-a97a-000d3a34a1bd)

--changesetresponse_1a5db8a1-ec98-42c4-81f6-6bc6adcfa4bc
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.1/contacts(495195a4-7a75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.1/contacts(495195a4-7a75-e911-a97a-000d3a34a1bd)

--changesetresponse_1a5db8a1-ec98-42c4-81f6-6bc6adcfa4bc
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 3

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.1/accounts(4f5195a4-7a75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.1/accounts(4f5195a4-7a75-e911-a97a-000d3a34a1bd)

--changesetresponse_1a5db8a1-ec98-42c4-81f6-6bc6adcfa4bc--
--batchresponse_3cace264-86ea-40fe-83d3-954b336c0f4a--
```

### Reference URI in request URL

The example given below shows how you can reference a URI using `$1` in the URL of a subsequent request.

**Request**

```http
POST [Organization URI]/api/data/v9.1/$batch HTTP/1.1
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

POST [Organization URI]/api/data/v9.1/contacts HTTP/1.1
Content-Type: application/json

{
  "@odata.type":"Microsoft.Dynamics.CRM.contact",
  "firstname":"Contact",
  "lastname":"AAAAAA"
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

**Response**

```http
200 OK

--batchresponse_2cb48f48-39a8-41ea-aa52-132fa8ab3c2d
Content-Type: multipart/mixed; boundary=changesetresponse_d7528170-3ef3-41bd-be8e-eac971a8d9d4

--changesetresponse_d7528170-3ef3-41bd-be8e-eac971a8d9d4
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

HTTP/1.1 204 No Content
OData-Version: 4.0
Location:[Organization URI]/api/data/v9.1/contacts(f8ea5d2c-8c75-e911-a97a-000d3a34a1bd)
OData-EntityId:[Organization URI]/api/data/v9.1/contacts(f8ea5d2c-8c75-e911-a97a-000d3a34a1bd)


--changesetresponse_d7528170-3ef3-41bd-be8e-eac971a8d9d4
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

HTTP/1.1 204 No Content
OData-Version: 4.0


--changesetresponse_d7528170-3ef3-41bd-be8e-eac971a8d9d4--
--batchresponse_2cb48f48-39a8-41ea-aa52-132fa8ab3c2d--
```

### Reference URIs in URL and request body using @odata.id

The example given below shows how to link a Contact entity record to an Account entity record. The URI of Account entity record is referenced as `$1` and URI of Contact entity record is referenced as `$2`.

**Request**

```http
POST [Organization URI]/api/data/v9.1/$batch HTTP/1.1
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

POST [Organization URI]/api/data/v9.1/accounts HTTP/1.1
Content-Type: application/json

{"@odata.type":"Microsoft.Dynamics.CRM.account","name":"IcM Account"}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type:application/http
Content-Transfer-Encoding:binary
Content-ID:2

POST [Organization URI]/api/data/v9.1/contacts HTTP/1.1
Content-Type:application/json

{"@odata.type":"Microsoft.Dynamics.CRM.contact","firstname":"Oncall Contact"}

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

**Response**

```http
200 OK

--batchresponse_0740a25c-d8e1-41a5-9202-1b50a297864c
Content-Type: multipart/mixed; boundary=changesetresponse_19ca0da8-d8bb-4273-a3f7-fe0d0fadfe5f

--changesetresponse_19ca0da8-d8bb-4273-a3f7-fe0d0fadfe5f
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

HTTP/1.1 204 No Content
OData-Version: 4.0
Location:[Organization URI]/api/data/v9.1/accounts(3dcf8c02-8c75-e911-a97a-000d3a34a1bd)
OData-EntityId:[Organization URI]/api/data/v9.1/accounts(3dcf8c02-8c75-e911-a97a-000d3a34a1bd)

--changesetresponse_19ca0da8-d8bb-4273-a3f7-fe0d0fadfe5f
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

HTTP/1.1 204 No Content
OData-Version: 4.0
Location:[Organization URI]/api/data/v9.1/contacts(43cf8c02-8c75-e911-a97a-000d3a34a1bd)
OData-EntityId:[Organization URI]/api/data/v9.1/contacts(43cf8c02-8c75-e911-a97a-000d3a34a1bd)

--changesetresponse_19ca0da8-d8bb-4273-a3f7-fe0d0fadfe5f
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 3

HTTP/1.1 204 No Content
OData-Version: 4.0

--changesetresponse_19ca0da8-d8bb-4273-a3f7-fe0d0fadfe5f--
--batchresponse_0740a25c-d8e1-41a5-9202-1b50a297864c--
```

### Reference URIs in URL and navigation properties

The example given below shows how to use the Organization URI of a Contact record and link it to an Account record using the `primarycontactid` single-valued navigation property. The URI of the Account entity record is referenced as `$1` and the URI of Contact entity record is referenced as `$2` in the `PATCH` request.

**Request**

```http
POST [Organization URI]/api/data/v9.1/$batch HTTP/1.1
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

POST [Organization URI]/api/data/v9.1/accounts HTTP/1.1
Content-Type: application/json

{"@odata.type":"Microsoft.Dynamics.CRM.account","name":"IcM Account"}

--changeset_dd81ccab-11ce-4d57-b91d-12c4e25c3cab
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

POST [Organization URI]/api/data/v9.1/contacts HTTP/1.1
Content-Type: application/json

{
  "@odata.type":"Microsoft.Dynamics.CRM.contact",
  "firstname":"Oncall Contact"
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
**Response**

```http
200 OK

--batchresponse_9595d3ae-48f6-414f-a3aa-a3a33559859e
Content-Type: multipart/mixed; boundary=changesetresponse_0c1567a5-ad0d-48fa-b81d-e6db05cad01c

--changesetresponse_0c1567a5-ad0d-48fa-b81d-e6db05cad01c
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.1/accounts(6cd81853-7b75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.1/accounts(6cd81853-7b75-e911-a97a-000d3a34a1bd)

--changesetresponse_0c1567a5-ad0d-48fa-b81d-e6db05cad01c
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.1/contacts(6ed81853-7b75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.1/contacts(6ed81853-7b75-e911-a97a-000d3a34a1bd)

--changesetresponse_0c1567a5-ad0d-48fa-b81d-e6db05cad01c
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 3

HTTP/1.1 204 No Content
OData-Version: 4.0
Location: [Organization URI]/api/data/v9.1/accounts(6cd81853-7b75-e911-a97a-000d3a34a1bd)
OData-EntityId: [Organization URI]/api/data/v9.1/accounts(6cd81853-7b75-e911-a97a-000d3a34a1bd)

--changesetresponse_0c1567a5-ad0d-48fa-b81d-e6db05cad01c--
--batchresponse_9595d3ae-48f6-414f-a3aa-a3a33559859e--
```

> [!NOTE]
> Referencing a Content-ID before it has been declared in the request body will return the error **HTTP 400** Bad request.
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
> POST [Organization URI]/api/data/v9.1/phonecalls HTTP/1.1
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
> POST [Organization URI]/api/data/v9.1/accounts HTTP/1.1
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
> **Response**
> 
> ```http
> HTTP 400 Bad Request
> Content-ID Reference: '$1' does not exist in the batch context.
> ```

### See also

[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Create a table using the Web API](create-entity-web-api.md)<br />
[Retrieve a table using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete tables using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate tables using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
