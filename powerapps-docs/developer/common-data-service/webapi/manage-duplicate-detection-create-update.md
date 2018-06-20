---
title: "Manage duplicate detection for create and update operations using the Web API | Microsoft Docs"
description: "Read how to detect duplicates using MSCRM.SuppressDuplicateDetection header and Common Data Service for Apps Web API"
ms.custom: ""
ms.date: 06/15/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: AE107774-4545-44B4-94C8-A0271EFA7876
caps.latest.revision: 11
author: "SushantSikka"
ms.author: "susikka"
manager: "amyla"
---

# Manage duplicate detection for create and update operations using the Web API

Common Data Service for Apps Web API allows you to detect duplicate records of an existing record in order to maintain integrity of data. 

## Detect duplicate during Create operation

Use `MSCRM.SuppressDuplicateDetection` header during `POST` request, to detect creation of a duplicate record of an existing record. The value assigned to `MSCRM.SuppressDuplicateDetection` header determines whether the Create or Update operation can be completed:

- `true` – Create or update the record, if a duplicate is found.
- `false` – Do not create or update the record, if a duplicate is found.

> [!NOTE]
> Passing of the `CalculateMatchCodeSynchronously` optional parameter is not required. The match codes used to detect duplicates are calculated synchronously regardless of the value passed in this parameter.

Use preference header `MSCRM.SuppressDuplicateDetection` and set its value to `false` in the Web API request.

> [!NOTE]
>  Make sure there are appropriate duplicate detection rules in place. Common Data Service for Apps includes default duplicate detection rules for accounts, contacts, and leads, but not for other types of records. If you want the system to detect duplicates for other record types, you’ll need to create a new rule. For information on how to create a duplicate detection rule, see [Set up duplicate detection rules to keep your data clean](../../../administrator/set-up-duplicate-detection-rules-keep-data-clean.md).

<a name="bkmk_create"></a>

###  Example: Detect duplicates during Create operation using the Web API

The following example shows how to detect duplicates during `Create` and `Update` operations using `MSCRM.SuppressDuplicateDetection` header in Web API request.

**Request**
```http
POST [Organization URI]/org1/api/data/v9.0/leads HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
MSCRM.SuppressDuplicateDetection: false

{
	"firstname":"Monte",
	"lastname":"Orton",
	"emailaddress1":"monteorton@example.com"
}
```
If a lead record with the same `emailaddress1` attribute already exists, the following Response is returned.

**Response**
```json
HTTP/1.1 500 Internal Server Error  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0

{
    "error": {
        "code": "0x80040333",
        "message": "A record was not created or updated because a duplicate of the current record already exists.",
        "innererror": {
            "message": "A record was not created or updated because a duplicate of the current record already exists.",
            "type": "Microsoft.Crm.CrmException",
            [ Stack Trace and internal exception details ommitted for brevity]
        }
    }
}
```
Assign value `true` to `MSCRM.SuppressDuplicateDetection` header to allow creation of a duplicate record.

<a name="bkmk_update"></a>

## Detect duplicates during Update operation

Set the value of `MSCRM.SuppressDuplicateDetection` header to `false` in your `PATCH` request to avoid creation of a duplicate record during Update operation. By default, duplicate detection is suppressed when you are updating records using the Web API.

The example shown below attempts to update an existing lead entity record which includes the same value of `emailaddress1` attribute as an existing record.

**Request**
```http
PATCH [Organization URI]/api/data/v9.0/leads(c4567bb6-47a3-e711-811b-e0071b6ac1b1) HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
MSCRM.SuppressDuplicateDetection: false

{
	"firstname":"Monte",
	"lastname":"Orton",
	"emailaddress1":"monteorton@example.com"
}
```  

**Response**
```json  
HTTP/1.1 500 Internal Server Error  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0

{
    "error": {
        "code": "0x80040333",
        "message": "A record was not created or updated because a duplicate of the current record already exists.",
        "innererror": {
            "message": "A record was not created or updated because a duplicate of the current record already exists.",
            "type": "Microsoft.Crm.CrmException",
            [ Stack Trace and internal exception details ommitted for brevity]
        }
    }
}
```

### See Also

<!-- TODO:
[Run duplicate detection](../run-duplicate-detection.md)<br />
[Duplicate detection messages](../duplicate-detection-messages.md) -->