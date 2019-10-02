---
title: "Check for analysis status | Microsoft Docs"
description: "Learn how to form a GET request using the PowerApps checker web API to check the status of an analysis request job."
ms.custom: ""
ms.date: 06/04/2019
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 6e2abe2d-2205-4d15-9e0f-5975ccc0484e
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

# Check for analysis status

[!INCLUDE [cc-beta-prerelease-disclaimer](../../../../includes/cc-beta-prerelease-disclaimer.md)]

A URL is returned as part of the `Location` header in response to a request to the `analyze` API. It is to be used to query via HTTP `GET` for the analysis job's status. When the analysis job is finished the response body will include the URL or list of URLs in which the results output can be downloaded. Keep calling this URI until an HTTP status code of 200 is returned. While the job is still running, an HTTP status code of 202 will be returned with the `Location` header containing this same URI that was returned from `analyze`. Once a 200 response is returned, the `resultFileUris` property will include the single or list of downloadable locations of the output, which is contained in a zip file. A [Static Analysis Results Interchange Format (SARIF)](https://sarifweb.azurewebsites.net) V2 formatted file is included within this zip download that is a `JSON` formatted file containing the results of the analysis. The response body will contain an `IssueSummary` object that contains a summary of the count of issues found.

> [!NOTE]
>  It is recommended to wait between 15 to 60 seconds between status checks. Analysis usually takes between 1 to 5 minutes to run.<br />
>  This API does require an OAuth token that must be a token for the same client application that initiated the analysis job.

<a name="bkmk_headers"></a>

## Headers

|Name|Type|Expected value|Required?|
|---|---|---|---|
|Authorization|string|The OAuth 1 bearer token with AAD Application ID claim.|yes|
|x-ms-tenant-id|GUID|The ID of the tenant for the application.|yes|
|x-ms-correlation-id|GUID|The identifier for the analysis run. You should provide the same Id for the entire execution (upload, analyze, status)|yes|

<a name="bkmk_responses"></a>

## Expected responses

|HTTP status code|Scenario|Result|
|---|---|---|
|200|One or more results were found|See the example below. One result will be returned.|
|202|Still processing|See the example below. One result will be returned.|
|403|Forbidden|The requestor is not the same as the originator of the request for analysis.|
|404|Not found|Unable to find the analysis request with the reference provided in the URL.|

### Expected response headers

|Name|Type|Expected value|Required?|
|---|---|---|---|
|Location|uri|URI to use in querying for the current status and to obtain the results|yes|

### Expected response body

The following table outlines the structure of the response for each request (HTTP 200 or 202 response only).

|Property|Type|Expected value|Required?|
|---|---|---|---|
|privacyPolicy|string|The URI of the privacy policy.|Yes|
|progress|int|A value ranging from 0-100 percentage complete, where 10 means that processing is approximately 10% complete.|Yes|
|runCorrelationId|GUID|The request identifier that is included in each request. This can be used to correlate to the request, if needed.|Yes|
|status|string|`InProgress` is returned when the job is still being processed. `Failed` is returned when there was a catastrophic issue processing the job on the server. There should be more details in the error property. `Finished` is returned when the job has completed successfully without issues. `FinishedWithErrors` is returned when the job has completed successfully, however, one or more rules failed to complete without error. This is purely a signal for you to know that the report may not be complete. Microsoft is aware of these issues in the backend and will work to get things diagnosed and addressed.|Yes|
|resultFileUris|array of strings|A list of URIs that allow for direct download of the output. There should be one per file that was included in the original analyze API call.|No. This is only included when processing has completed.|
|issueSummary|IssueSummary|Properties listed below|No. This is only included when processing has completed.|
|issueSummary.criticalIssueCount|int|Count of issues identified having a critical severity in the result|Yes|
|issueSummary.highIssueCount|int|Count of issues identified having a high severity in the result|Yes|
|issueSummary.mediumIssueCount|int|Count of issues identified having a medium severity in the result|Yes|
|issueSummary.lowIssueCount|int|Count of issues identified having a low severity in the result|Yes|
|issueSummary.informationalIssueCount|int|Count of issues identified having an informational severity in the result|Yes|

<a name="bkmk_checkStatusDone"></a>

## Example: status check when done

This example issues a status check call with the result being a completion.

**Request**

```http
GET [Geographical URI]/api/status/9E378E56-6F35-41E9-BF8B-C0CC88E2B832&api-version=1.0
Accept: application/json
Content-Type: application/json; charset=utf-8
x-ms-correlation-id: 9E378E56-6F35-41E9-BF8B-C0CC88E2B832
x-ms-tenant-id: F2E60E49-CB87-4C24-8D4F-908813B22506
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
    "privacyPolicy":"https://go.microsoft.com/fwlink/?LinkID=310140",
    "progress":100,
    "resultFileUris":["https://fakeblob.blob.core.windows.net/report-files/mySolution.zip?sv=2017-11-09&sr=b&sig=xyz&se=2019-06-11T20%3A27%3A59Z&sp=rd"],"runCorrelationId":"9E378E56-6F35-41E9-BF8B-C0CC88E2B832","status":"Finished","issueSummary":
    {
        "informationalIssueCount":0,
        "lowIssueCount":0,
        "mediumIssueCount":302,
        "highIssueCount":30,
        "criticalIssueCount":0
    }
}
```


### See also

[Use the PowerApps checker web API](overview.md)<br />
[Retrieve the list of rulesets](retrieve-rulesets.md)<br />
[Retrieve the list of rules](retrieve-rules.md)<br />
[Upload a file](upload-file.md)<br />
[Invoke analysis](analyze.md)<br />
