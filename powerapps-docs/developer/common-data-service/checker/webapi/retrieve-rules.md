---
title: "Retrieve the list of rules | Microsoft Docs"
description: "Learn how to form a GET request using the PowerApps checker web API to retrieve the list of rules available."
ms.custom: ""
ms.date: 06/04/2019
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: a8dc3019-c49e-48e4-a646-8a3a3fecd3a6
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

# Retrieve the list of rules

[!INCLUDE [cc-beta-prerelease-disclaimer](../../../../includes/cc-beta-prerelease-disclaimer.md)]

Rules are grouped together using a ruleset. A rule can be in no ruleset, or multiple rulesets. Use a `GET` request to obtain a list of all rules available, rules in a ruleset, or rulesets by calling the API `[Geographical URI]/api/rule`. There are a few variations to calling this API, however, the most common usage is to retrieve the list of rules for a specific ruleset.

> [!NOTE]
>  This API does not require an OAuth token, but can accept one if provided.

<a name="bkmk_headers"></a>

## Headers

|Name|Type|Expected value|Required?|
|---|---|---|---|
|Accept-Language|string|The language code (e.g., en-US). The default is en-US.|no

<a name="bkmk_params"></a>

## Parameters

|Name|Type|Expected value|Required?|
|---|---|---|---|
|ruleset|string|The name or ID of the ruleset or a list of ruleset IDs, or names separated by a comma or semicolon (e.g., "Solution Checker").|no|
|includeMessageFormats|bool|When set to `true`, the list of possible message variations are included in the results of the language(s) requests, if available. This is useful for translations into multiple languages. If not needed, then do not provide this parameter or provide `false` as the value as this parameter will increase the size of the response and can increase processing time.|no|

<a name="bkmk_responses"></a>

## Expected responses

|HTTP status code|Scenario|Result|
|---|---|---|
|200|One or more results were found|See the example below. One or more results may be returned.|
|204|No results were found|No results in the response body.|

### Expected response body

The following table outlines the structure of the response for each request (HTTP 200 response only).

|Property|Type|Expected value|Required?|
|---|---|---|---|
|code|string|The identifier of the rule, sometimes referred to as the Rule ID.|Yes|
|summary|string|A summary of the the rule.|Yes|
|description|string|More detailed description of the rule.|Yes|
|guidanceUrl|URI|The URL in which to find published guidance. There may be some cases where there is not a dedicated supporting guidance article.|Yes|
|include|boolean|Signals to the service that the rule is to be included in the analysis. This will be `true` for this API.|No|
|messageTemplates|array|This property value is included only when `includeMessageFormats` is `true`.|No|
|messageTemplates.ruleId|string| Returns the same ID value as the `code` property.|Yes|
|messageTemplates.messageTemplateId|string| An identifier used in the Static Analysis Results Interchange Format (SARIF) report to signal an issue message variation for the rule.|Yes|
|messageTemplates.messageTemplate|string|The text of the message variation for the issue scenario that the rule reports. This is a format string that may contain tokens in which  arguments provided in the SARIF report can be used to construct a detailed message.|Yes|

<a name="bkmk_retrieveForRuleset"></a>

## Example: retrieve rules for a ruleset in another language

This example returns data for all of the rules in the *Solution Checker* ruleset in the French language. If the desired language is English, then just remove the Accept-Language header.

**Request**

```http
GET [Geographical URI]/api/rule?ruleset=083A2EF5-7E0E-4754-9D88-9455142DC08B&api-version=1.0
x-ms-correlation-id: 9E378E56-6F35-41E9-BF8B-C0CC88E2B832
Accept: application/json
Content-Type: application/json; charset=utf-8
Accept-Language: fr
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

[
    {
        "description": "Ne pas implémenter d’activités de workflow Microsoft Dynamics CRM 4.0",
        "guidanceUrl": "https://go.microsoft.com/fwlink/?LinkID=398563&error=il-avoid-crm4-wf&client=PAChecker",
        "include": true,
        "code": "il-avoid-crm4-wf",
        "summary": "Ne pas implémenter d’activités de workflow Microsoft Dynamics CRM 4.0",
        "howToFix": {
            "summary": ""
        }
    },
    {
        "description": "Utiliser InvalidPluginExecutionException dans des plug-ins et activités de workflow",
        "guidanceUrl": "https://go.microsoft.com/fwlink/?LinkID=398563&error=il-use-standard-exception&client=PAChecker",
        "include": true,
        "code": "il-use-standard-exception",
        "summary": "Utiliser InvalidPluginExecutionException dans des plug-ins et activités de workflow",
        "howToFix": {
            "summary": ""
        }
    },
...
]
```

<a name="bkmk_retrieveAll"></a>

## Example: retrieve all

This example returns data for all of the rules available.

**Request**

```http
GET [Geographical URI]/api/rule?api-version=1.0
Accept: application/json
Content-Type: application/json; charset=utf-8
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

[
    {
        "description": "Retrieve specific columns for an entity via query APIs",
        "guidanceUrl": "https://go.microsoft.com/fwlink/?LinkID=398563&error=il-specify-column&client=PAChecker",
        "include": true,
        "code": "il-specify-column",
        "summary": "Retrieve specific columns for an entity via query APIs",
        "howToFix": {
            "summary": ""
        }
    },
    {
        "description": "Do not duplicate plug-in step registration",
        "guidanceUrl": "https://go.microsoft.com/fwlink/?LinkID=398563&error=meta-remove-dup-reg&client=PAChecker",
        "include": true,
        "code": "meta-remove-dup-reg",
        "summary": "Do not duplicate plug-in step registration",
        "howToFix": {
            "summary": ""
        }
    },
...
]
```

<a name="bkmk_retrieveForRuleset"></a>

## Example: retrieve for a ruleset with message formats

This example returns data for all of the rules in the *Solution Checker* ruleset in the French language. If the desired language is English, then just remove the Accept-Language header.

**Request**

```http
GET [Geographical URI]/api/rule?ruleset=083A2EF5-7E0E-4754-9D88-9455142DC08B&includeMessageFormats=true&api-version=1.0
Accept: application/json
Content-Type: application/json; charset=utf-8
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

[
    {
        "description": "Do not implement Microsoft Dynamics CRM 4.0 workflow activities",
        "guidanceUrl": "https://go.microsoft.com/fwlink/?LinkID=398563&error=il-avoid-crm4-wf&client=PAChecker",
        "include": true,
        "code": "il-avoid-crm4-wf",
        "summary": "Do not implement Microsoft Dynamics CRM 4.0 workflow activities",
        "howToFix": {
            "summary": ""
        },
        "messageTemplates": [
            {
                "ruleId": "il-avoid-crm4-wf",
                "messageTemplateId": "message1",
                "messageTemplate": "Update the {0} class to derive from System.Workflow.Activities.CodeActivity, refactor Execute method implementation, and remove Microsoft.Crm.Workflow.CrmWorkflowActivityAttribute from type"
            },
            {
                "ruleId": "il-avoid-crm4-wf",
                "messageTemplateId": "message2",
                "messageTemplate": "Change the {0} property's type from {1} to {2} Argument &lt;T&gt; type"
            },
            {
                "ruleId": "il-avoid-crm4-wf",
                "messageTemplateId": "message3",
                "messageTemplate": "Replace the Microsoft.Crm.Workflow.Crm{0}Attribute with Microsoft.Xrm.Sdk.Workflow.{0}Attribute"
            },
            {
                "ruleId": "il-avoid-crm4-wf",
                "messageTemplateId": "message4",
                "messageTemplate": "Remove the {0} System.Workflow.ComponentModel.DependencyProperty type field"
            }
        ]
    },
    {
        "description": "Use InvalidPluginExecutionException in plug-ins and workflow activities",
        "guidanceUrl": "https://go.microsoft.com/fwlink/?LinkID=398563&error=il-use-standard-exception&client=PAChecker",
        "include": true,
        "code": "il-use-standard-exception",
        "summary": "Use InvalidPluginExecutionException in plug-ins and workflow activities",
        "howToFix": {
            "summary": ""
        },
        "messageTemplates": [
            {
                "ruleId": "il-use-standard-exception",
                "messageTemplateId": "message1",
                "messageTemplate": "An unguarded throw of type {0} was detected. Refactor this code to either throw an exception of type InvalidPluginExecutionException or guard against thrown exceptions of other types."
            },
            {
                "ruleId": "il-use-standard-exception",
                "messageTemplateId": "message2",
                "messageTemplate": "An unguarded rethrow of type {0} was detected. Refactor this code to either throw an exception of type InvalidPluginExecutionException or guard against thrown exceptions of other types."
            }
        ]
    },
...
]
```

### See also

[Use the PowerApps checker web API](overview.md)<br />
[Retrieve the list of rulesets](retrieve-rulesets.md)<br />
[Upload a file](upload-file.md)<br />
[Invoke analysis](analyze.md)<br />
[Check for analysis status](check-status.md)<br />