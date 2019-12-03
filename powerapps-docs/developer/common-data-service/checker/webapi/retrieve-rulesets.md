---
title: "Retrieve the list of rulesets | Microsoft Docs"
description: "Read how to form a GET request using the Power Apps checker web API to retrieve the list of rulesets available."
ms.custom: ""
ms.date: 06/04/2019
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 23c9391c-1697-47a3-a8f2-eedd5c862874
caps.latest.revision: 21
author: "mhuguet" # GitHub ID
ms.author: "mhuguet"
ms.reviewer: "pehecke"
manager: "maustinjones"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Retrieve the list of rulesets

[!INCLUDE [cc-beta-prerelease-disclaimer](../../../../includes/cc-beta-prerelease-disclaimer.md)]

Rules are grouped together using a ruleset. Rulesets can have one or more rules with no limit. A rule can be in no ruleset, or multiple rulesets. Use a `GET` request to obtain a list of all rulesets available by calling the API, [Geographical URI]/api/ruleset.

> [!NOTE]
>  This API does not require an OAuth token, but can accept one if provided.

<a name="bkmk_responses"></a>

## Expected responses

|HTTP status code|Scenario|Result|
|---|---|---|
|200|One or more results were found|See example below. One or more results may be returned.|
|204|No results were found|No results response body is returned.|

### Expected response body

The following table outlines the structure of the response for each request (HTTP 200 response only).

|Property|Type|Expected value|Required?|
|---|---|---|---|
|id|Guid|Identifier of the ruleset|Yes|
|name|string|Friendly name of the ruleset|Yes|

<a name="bkmk_retrieve"></a>

## Example: retrieve all rulesets

This example returns data for all of the rulesets available.

**Request**

```http
GET [Geographical URI]/api/ruleset?api-version=1.0
Accept: application/json
x-ms-correlation-id: 9E378E56-6F35-41E9-BF8B-C0CC88E2B832
Content-Type: application/json; charset=utf-8
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

[
    {
        "id": "083a2ef5-7e0e-4754-9d88-9455142dc08b",
        "name": "AppSource Certification"
    },
    {
        "id": "0ad12346-e108-40b8-a956-9a8f95ea18c9",
        "name": "Solution Checker"
    }
]
```

### See also

[Use the Power Apps checker web API](overview.md)<br />
[Retrieve the list of rules](retrieve-rules.md)<br />
[Upload a file](upload-file.md)<br />
[Invoke analysis](analyze.md)<br />
[Check for analysis status](check-status.md)<br />