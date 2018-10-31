---
title: "Execute batch operations using the Web API (Common Data Service for Apps)| Microsoft Docs"
description: "Batch operation lets you group multiple operations in a single HTTP request. Read how to execute batch operations using the Web API"
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 799b2346-bda1-4a26-a330-79d0927a7743
caps.latest.revision: 11
author: "brandonsimons" # GitHub ID
ms.author: "jdaly"
manager: "amyla"
---
# Execute batch operations using the Web API

You can group multiple operations into a single HTTP request using a batch operation.  
  
<a name="bkmk_Whentousebatchrequests"></a>

## When to use batch requests

The value that batch requests provide is that they can include change sets, which provide a way to bundle a number of operations that either succeed or fail as a group. Compared to other operations that can be performed using the web API, they are more difficult to compose without some object model that includes serialization of objects or a deeper understanding of the HTTP protocol because the request body is essentially a text document that must match very specific requirements.  
  
Remember that associated entities can be created in a single operation more easily than using a batch request. Batch requests are best used when performing operations on entities that aren’t associated with each other when all the operations must be performed in a single transactional operation.  
  
Also, the responses returned are essentially text documents rather than objects that can easily be parsed into JSON. You’ll need to parse the text in the response or locate a helper library to access the data in the response.  
 
>[!NOTE]
>  Batch requests can contain up to 100 individual requests and cannot contain other batch requests.  
  
<a name="bkmk_BatchRequests"></a> 

## Batch requests

Use a POST request to submit a batch operation that contains multiple requests. A batch request can include GET requests and change sets. To use the transactional capabilities of batch requests, only operations that will change data can be included within a change set. GET requests must not be included in the change set.  
  
The POST request containing the batch must have a Content-Type header with a value set to multipart/mixed with a boundary set to include the identifier of the batch using this pattern:  
  
```  
--batch_<unique identifier>  
```  
  
The unique identifier doesn’t need to be a GUID, but should be unique. Each item within the batch must be preceded by the batch identifier with a Content-Type and Content-Transfer-Encoding header like the following:  
  
```  
--batch_WKQS9Yui9r  
Content-Type: application/http  
Content-Transfer-Encoding:binary  
```  
  
The end of the batch must contain a termination indicator like the following:  
  
```  
--batch_WKQS9Yui9r--  
```  
  
>[!NOTE]
>  The odata.continue-on-error preference is not supported by the web API. Any error that occurs in the batch will stop the processing of the remainder of the batch.  
  
<a name="bkmk_ChangeSets"></a>

## Change sets

When multiple operations are contained in a change set, all the operations are considered atomic, which means that if any one of the operations fail, any completed operations will be rolled back. Like a batch request, change sets must have a Content-Type header with value set to multipart/mixed with a boundary set to include the identifier of the change set using this pattern:  
  
```  
--changeset_<unique identifier>  
```  
  
The unique identifier doesn’t need to be a GUID, but should be unique. Each item within the change set must be preceded by the change set identifier with a Content-Type and Content-Transfer-Encoding header like the following:  
  
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
POST[Organization URI]/api/data/v9.0/$batch HTTP/1.1  
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
  
POST[Organization URI]/api/data/v9.0/tasks HTTP/1.1  
Content-Type: application/json;type=entry  
  
{"subject":"Task 1 in batch","regardingobjectid_account_task@odata.bind":"[Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-000000000001)"}  
--changeset_BBB456  
Content-Type: application/http  
Content-Transfer-Encoding:binary  
Content-ID: 2  
  
POST[Organization URI]/api/data/v9.0/tasks HTTP/1.1  
Content-Type: application/json;type=entry  
  
{"subject":"Task 2 in batch","regardingobjectid_account_task@odata.bind":"[Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-000000000001)"}  
--changeset_BBB456--  
  
--batch_AAA123  
Content-Type: application/http  
Content-Transfer-Encoding:binary  
  
GET[Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-000000000001)/Account_Tasks?$select=subject HTTP/1.1  
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
Location:[Organization URI]/api/data/v9.0/tasks(a59c24f3-fafc-e411-80dd-00155d2a68cb)  
OData-EntityId:[Organization URI]/api/data/v9.0/tasks(a59c24f3-fafc-e411-80dd-00155d2a68cb)  
  
--changesetresponse_ff83b4f1-ab48-430c-b81c-926a2c596abc  
Content-Type: application/http  
Content-Transfer-Encoding: binary  
Content-ID: 2  
  
HTTP/1.1 204 No Content  
OData-Version: 4.0  
Location:[Organization URI]/api/data/v9.0/tasks(a69c24f3-fafc-e411-80dd-00155d2a68cb)  
OData-EntityId:[Organization URI]/api/data/v9.0/tasks(a69c24f3-fafc-e411-80dd-00155d2a68cb)  
  
--changesetresponse_ff83b4f1-ab48-430c-b81c-926a2c596abc--  
--batchresponse_c1bd45c1-dd81-470d-b897-e965846aad2f  
Content-Type: application/http  
Content-Transfer-Encoding: binary  
  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
  "@odata.context":"[Organization URI]/api/data/v9.0/$metadata#tasks(subject)","value":[  
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
  
GET[Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-000000000001)?$select=name,telephone1,emailaddress1,shippingmethodcode,customersizecode,accountratingcode,followemail,donotemail,donotphone,statuscode HTTP/1.1  
Accept: application/json  
Prefer: odata.include-annotations="*"
  
--batch_AAA123-- 
```
For more information about preference headers, see[Header Prefer](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part1-protocol/odata-v4.0-errata03-os-part1-protocol-complete.html#_Toc453752234).

### See also

[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Create an entity using the Web API](create-entity-web-api.md)<br />
[Retrieve an entity using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete entities using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate entities using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)
