---
title: "Invoke analysis | Microsoft Docs"
description: "Read how to form a POST request using the PowerApps checker web API to initiate the analysis request job"
ms.custom: ""
ms.date: 06/04/2019
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: a2c771f4-7eb6-4445-af2d-f775619ac3e8
caps.latest.revision: 21
author: "mhuguet" # GitHub ID
ms.author: "mhuguet"
ms.reviewer: ""
manager: "maustinjones"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Invoke analysis

Initiating an analysis job is done by submitting a `POST` request to the `analyze` route. Analysis can be a long running process, which is usually longer than a minute, so the API does some basic validation, initiates the request on the backend by submitting a job, and responds with a status code of 202 and a `Location` header or with the apprioriate error details. The `Location` header value is a URL that can be used to check on the status of the request and to obtain the URL(s) of the result(s). There are various options through the POST action to taylor the job based on your criteria, such as the list of rules or rulesets, files to exclude from the analysis, etc. You can initiate using the following _/api/analyze?api-version=1.0_.


> [!NOTE]
>  It is recommended to wait between 15 to 60 seconds between status checks. Analysis usually takes between 1 to 5 minutes to run.

> [!NOTE]
>  This endpoint does require an OAuth token.

<a name="bkmk_headers"></a>

## Headers
|Name|Type|Expected value|Required?|
|--|--|--|--|
|Authorization|string|OAuth 1 bearer token with AAD Application Id claim|yes|
|x-ms-tenant-id|guid|ID of the tenant for the application|yes|
|x-ms-correlation-id|guid|Identifier for the analysis run. You should provide the same Id for the entire execution (upload, analyze, status)|yes|
|Accept|object|application/json, application/x-ms-sarif-v2|yes|
|Accept-Language|string|language code or codes, e.g.- en-US. The default is en-US. If multiple are provided, the first will be the primary, however, all translations (if the language is supported) will be included.|no

<a name="bkmk_body"></a>

## Body

### Commonly used options:

|Property|Type|Expected value|Required?|
|--|--|--|--|
|sasUriList|array of strings|List of URIs that provides the service access to download a single solution, a zip file containing multiple solution files, or a package|Yes|
|ruleSets|array of custom|0 or more|No|
|ruleSets.id|guid|Id of the ruleset, which can be found by querying the ruleset API.|No, but this is usually what you would want to use. You must use either this or ruleCodes.|
|ruleCodes.code|string|Id of the desired rule, which can be found by querying the ruleset and rule APIs.|No. You must use either this or ruleSets.|
|fileExclusions|array of strings|List of file names or file name patterns to exclude. Support exists for using "*" as a wildcard in the beginning and/or end of a file name, e.g._\*jquery.dll_ and _\*jquery\*_.|No|

<a name="bkmk_responses"></a>

## Expected responses
|HTTP status code|Scenario|Result|
|--|--|--|
|202|Request for analysis was accepted and the status check URI was returned in the `Location` header|No result body
|400|A non zip file was sent, incorrect parameters, or a file was included with a virus|No result body|
|409|A request with a duplicate x-ms-correlation-id header value was sent|No result body|

### Expected response headers
|Name|Type|Expected value|Required?|
|--|--|--|--|
|Location|Uri|URL to use in querying for the current status and to obtain the results|yes|

<a name="bkmk_analyzeExample"></a>

## Example: initiate an analysis

This is an example of initiating an analysis job with the _AppSource Certification_ ruleset, a single file, and excluding files that contain the text _jquery_ and _json_ in the name.

**Request**
```http
POST [Geographical URI]/api/analyze?api-version=1.0
Accept: application/json
Content-Type: application/json; charset=utf-8
x-ms-correlation-id: 9E378E56-6F35-41E9-BF8B-C0CC88E2B832

{
    "ruleSets": [{
        "id": "0ad12346-e108-40b8-a956-9a8f95ea18c9"
    }],
    "sasUriList": ["https://testenvfakelocation.blob.core.windows.net/mySolution.zip"],
    "fileExclusions": ["*jquery*", "*json*"]
}
```

**Response**
```http
HTTP/1.1 202 Accepted
Content-Type: application/json; charset=utf-8
Location: [Geographical URI]/api/status/9E378E56-6F35-41E9-BF8B-C0CC88E2B832&api-version=1.0
```

### See also

[Use the PowerApps checker web API](overview.md)<br />
[Retrieve the list of rulesets](retrieve-rulesets.md)<br />
[Retrieve the list of rules](retrieve-rules.md)<br />
[Upload a file](upload-file.md)<br />
[Check for analysis status](check-status.md)<br />