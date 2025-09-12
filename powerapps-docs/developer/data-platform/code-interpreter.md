---
title: "Code interpreter for developers"
description: "Learn how developers can use code interpreter enabled prompts."
ms.date: 09/15/2025
ms.reviewer: jdaly
ms.topic: article
author: rapraj
ms.author: rapraj
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - ColinBe
---
# Code interpreter for developers

As described in [Use code interpreter to generate and execute Python code](/microsoft-copilot-studio/code-interpreter-for-prompts), code interpreter provides a way for agents to execute python code for data analysis, Word, Excel, PowerPoint, and PDF processing, and visualizations. Refer to that article to understand:

- Licensing requirements and supported regions
- General code interpreter capabilities
- How to enable code interpreter for a prompt
- How to use code interpreter capabilities with a prompt

This article describes how developers can use the Dataverse `Predict` message to pass parameters to code interpreter enabled prompts and process the responses.  

> [!NOTE]
> A common scenario for code interpreter enabled prompts is to generate UI experiences for model-driven applications using Power Apps Component (PCF) components. Refer to the [Code interpreter PCF component sample](code-interpreter-pcf-sample.md) for an example.

## Enable code interpreter for the environment

Code interpreter must be enabled for each environment before you can use it. The default setting is **Off**. [Learn how to enable code interpreter using the Power Platform Admin center](/microsoft-copilot-studio/code-interpreter-for-prompts#administration-of-code-interpreter)

Developers can use the Power Platform [Environment Management Settings](/rest/api/power-platform/environmentmanagement/environment-management-settings) APIs to read or set the `CopilotStudio_CodeInterpreter` boolean property to enable code interpreter for an environment.

## Code interpreter enabled prompts

Every prompt created using Microsoft Copilot Studio or AI Builder creates a new record in the Dataverse [AI Model (msdyn_AIModel) table](reference/entities/msdyn_aimodel.md). You need the ID of the row when you invoke the `Predict` message.

You can't create a prompt by creating a new row in the `msdyn_AIModel`. Prompts are created updated using the [AIModelPublish](/power-apps/developer/data-platform/webapi/reference/aimodelpublish) message. This public message is for internal use only. You must use the UI to create code interpreter enabled prompts. You must also make sure that each prompt is enabled for code interpreter. Enabling a prompt is slightly different depending on whether you edit the prompt in Power Apps or Copilot Studio. See these instructions:

- [Power Apps](/microsoft-copilot-studio/code-interpreter-for-prompts#enable-code-interpreter-in-power-apps-ai-hub)
- [Copilot Studio](/microsoft-copilot-studio/code-interpreter-for-prompts#enable-code-interpreter-in-prompt-tool-within-an-agent)

You can query the `msdyn_AIModel` table using the `msdyn_Name` column value to identify code interpreter enabled prompts by name. The `msdyn_AIModel` doesn't have a property you can use to filter only those prompts that are code interpreter enabled.

### Retrieve AI Model data

Use queries like the following to retrieve data from the `msdyn_AIModel` table.

### [SDK for .NET](#tab/sdk)

```csharp
static RetrieveAIModelsExample (IOrganizationService service)
{
 var query = new QueryExpression("msdyn_aimodel")
 {
     ColumnSet = new ColumnSet("msdyn_name", "msdyn_aimodelid")
 };
 
 var results = service.RetrieveMultiple(query);
 
 foreach (var entity in results.Entities)
 {
     Console.WriteLine($"Model Name: {entity["msdyn_name"]}, ID: {entity["msdyn_aimodelid"]}");
 }
}
```

### [Web API](#tab/webapi)

**Request**:

```http
GET [Organization URI]/api/data/v9.2/msdyn_aimodels?$select=msdyn_name,msdyn_aimodelid
```

**Response**:

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
 "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#msdyn_aimodels(msdyn_name,msdyn_aimodelid,modifiedon)",
   "value": [
  {
   "@odata.etag": "W/\"5080532\"",
   "msdyn_aimodelid": "a0440df3-2656-e911-8194-000d3a6cd5a5",
   "msdyn_name": "BusinessCard model"
  },
  {
   "@odata.etag": "W/\"5080568\"",
   "modifiedon": "2025-08-28T18:17:39Z",
   "msdyn_aimodelid": "046ab801-2756-e911-8194-000d3a6cd5a5",
   "msdyn_name": "ObjectDetectionProposal model"
  }
}
```

---

## Predict message

The `Predict` message is available in both the Dataverse SDK for .NET and Web API.

### Sending the request

Regardless of how you send the request, the `Predict` message requires three parameters:

- The ID of the `msdyn_AIModel` record. How you set this value depends on whether you use the SDK for .NET or Web API.
- The data that contains the parameters that the prompt is configured to accept. This is passed as a parameter named `requestv2`. [Learn more about the `requestv2` parameter](#requestv2-parameter)
- The `version` parameter. The value is always `"2.0"`.

#### `requestv2` parameter

This parameter is configured as an *open type*. [Learn more about how to use open types in general](use-open-types.md#how-to-use-open-types)

An open type is a dictionary that contains keys and values. The values can also be dictionaries, so it's possible to send complex, hierarchical data to an open type parameter.

### [SDK for .NET](#tab/sdk)

With the SDK for .NET, use the [Entity class](/dotnet/api/microsoft.xrm.sdk.entity) and set the [Attributes](/dotnet/api/microsoft.xrm.sdk.entity.attributes) collection with the values. The key difference in this scenario is that the `Entity` instance doesn't have a [LogicalName](/dotnet/api/microsoft.xrm.sdk.entity.logicalname) set, so it doesn't refer to a specific Dataverse table.

In the following `PredictActionExample` sample method, the `Predict` action is invoked using the [OrganizationRequest class](/dotnet/api/microsoft.xrm.sdk.organizationrequest) as described in [Use messages with the SDK for .NET](org-service/use-messages.md). Alternatively, you can generate a pair of typed `PredictRequest` and `PredictResponse` classes. [Learn how to generate early-bound classes for the SDK for .NET](org-service/generate-early-bound-classes.md)

It also shows how to set the `Target` parameter with an [EntityReference](/dotnet/api/microsoft.xrm.sdk.entityreference) that refers to the `msdyn_AIModel` record using the ID.

```csharp
static PredictActionExample (IOrganizationService service, Guid yourAiModelId)
{
 // Create the nested 'patient' entity
 var patientEntity = new Entity
 {
     Attributes =
     {
         { "firstname", "John" },
         { "lastname", "Smith" }
     }
 };
 
 // Create the main 'requestv2' entity
 var requestV2Entity = new Entity
 {
     Attributes =
     {
         { "pai_sex", 1 },
         { "pai_age", 10 },
         { "patient", patientEntity }
     }
 };
 
 // Create the Predict action request
 var predictRequest = new OrganizationRequest("Predict")
 {
     Parameters = new ParameterCollection
     {
         { "version", "2.0" },
         { "requestv2", requestV2Entity },
         { "Target", new EntityReference("msdyn_aimodel", new Guid(yourAiModelId)) }
     }
 };
 
 // Execute the request
 var response = service.Execute(predictRequest);
 
 Console.WriteLine("Prediction Result:");
 Console.WriteLine(response.Results);
}
```

### [Web API](#tab/webapi)

The [Predict Action](/power-apps/developer/data-platform/webapi/reference/predict) is bound to the [msdyn_aimodel entity type](/power-apps/developer/data-platform/webapi/reference/msdyn_aimodel). When you use [actions bound to a table](webapi/use-web-api-actions.md#actions-bound-to-a-table), you pass the reference in the URL and invoke the action using the fully qualified name: `Microsoft.Dynamics.CRM.Predict`.

As explained in [Use Entity as a dictionary](use-open-types.md?tabs=webapi#use-entity-as-a-dictionary), set the `requestv2` property with a dictionary that includes an `@odata.type` property set to `"Microsoft.Dynamics.CRM.expando"`. This indicates the value is an open type.

Notice how this example uses two nested open dictionaries.

**Request**:

```http
POST msdyn_aimodels([AI Model ID])/Microsoft.Dynamics.CRM.Predict
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0

{
    "version": "2.0",
    "requestv2": {
        "@odata.type": "#Microsoft.Dynamics.CRM.expando",
        "pai_sex": 1,
        "pai_age": 10,
        "patient": {
            "@odata.type": "#Microsoft.Dynamics.CRM.expando",
            "firstname": "John",
            "lastname": "Smith"
        }
    }
}
```

**Response**:

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.PredictResponse",
    "response": null,
    "overrideHttpStatusCode": null,
    "overrideLocation": null,
    "overrideRetryAfter": null,
    "responsev2": {
        "@odata.type": "#Microsoft.Dynamics.CRM.expando",
        "operationStatus": "Success",
        "predictionOutput": {
            "@odata.type": "#Microsoft.Dynamics.CRM.expando",
            "text":"<content returned from code execution>",
            "mimetype":"text/markdown",
            "textMimeType":"text/markdown",
            "finishReason":"stop",
            "code":"<Python code that was executed to generate the content>",
            "signature":"<a Base64‑encoded, versioned metadata and integrity token >",
            "logs": "<Output of the steps executed by the python code>"
            "codeThinking":{
                "@odata.type": "#Microsoft.Dynamics.CRM.expando"
            },
            "files@odata.type": "#Collection(Microsoft.Dynamics.CRM.crmbaseentity)",
            "files": [
                {
                    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                    "base64_content": "[Example_Document.pdf base64 content]",
                    "content_type": "application/pdf",
                    "file_name": "Example_Document.pdf"
                }
            ],
            "structuredOutput": {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "mimetype": "text/markdown",
                "text": "# Example Document\n\nExample document for Example record Example 2.\n\n[Download the PDF document here](Example_Document.pdf)"
            },
            "artifacts":{
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "Example_Document": {
                    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                    "artifactName": "Example_Document.pdf",
                    "mimeType": "application/pdf",
                    "base64Content": "[Example_Document.pdf base64 content]"
        }
      }
    }
  }
}
```

---

### Processing the response

The [PredictResponse complex type](/power-apps/developer/data-platform/webapi/reference/predictresponse) contains the response from the `Predict` message in web API. The SDK for .NET has similar response properties. Refer to the previous Web API response example for details.

| Property | Type | Description |
|----------|------|-------------|
|`overrideHttpStatusCode`|String|In case the prediction isn't completed, 202 indicates that a polling is necessary, otherwise null.|
|`overrideLocation`|String| Null except when `overrideHttpStatusCode` isn't null. The location of the polling. Sent a GET request to this location to poll for the result.|
|`overrideRetryAfter`|String|Null except when `overrideHttpStatusCode` isn't null. Suggestion on when to try polling.|
|`response`|String|This property is obsolete since the introduction of the `responsev2` property and should always be null.|
|`responsev2`| Entity/expando | See [PredictResponse responsev2 properties](#predictresponse-responsev2-properties)|

#### PredictResponse responsev2 properties

The `responsev2` property has two properties:

- `operationStatus`: A string value showing whether the operation succeeded. Expected value is `Success`.
- `predictionOutput`: A dictionary with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `text` | string | Primary generated content. Content depends on the type of value returned by the prompt. |
| `mimetype` | string | Text [MIME type](https://developer.mozilla.org/docs/Web/HTTP/Guides/MIME_types/Common_types). |
| `textMimeType` | string | Duplicate/confirming [MIME type](https://developer.mozilla.org/docs/Web/HTTP/Guides/MIME_types/Common_types)|
| `finishReason` | string | The reason the reasoning finished. This is usually `stop`. |
| `code` | string | Python Source code or placeholder describing executed code. |
| `signature` | string | a Base64‑encoded, versioned metadata and integrity token |
| `logs` | string | Python code execution log output (if provided). |
| `codeThinking` | object | Empty/internal placeholder object. |
| `files` | array of objects | Generated file artifacts with `file_name`, `content_type`, and `base64_content` properties. |
| `structuredOutput` | object | Canonical form of main output with `mimetype` and `text` properties. |
| `artifacts` | object | Map of artifact identifiers to metadata & base64 content. This object contains properties specific to the output and these properties are objects that have the following properties:  `artifactName`, `mimeType`, and `base64Content` |

## Troubleshooting

The following are some errors you might encounter while using the Predict action with code interpreter enabled prompts.

### Insufficient capacity

When you don't have any remaining AI Builder capacity, you'll get this `403 Forbidden` `EntitlementNotAvailable` error:

```json
{ 
   "error": { 
       "code": "0x80048d06", 
       "message": "{\"operationStatus\":\"Error\",\"error\":{\"type\":\"Error\",\"code\":\"EntitlementNotAvailable\",\"innerErrors\":[{\"scope\":\"Generic\",\"target\":null,\"code\":\"NoCapacity\",\"type\":\"Error\",\"message\":\"No capacity was found.\"}]},\"predictionId\":null}" 
   } 
}
```

A PCF control that encounters this error displays this message: **Access denied. You don't have permission to use this model.**

The resolution to this error is to purchase more AI Builder capacity. [Learn more about how to get entitlement to AI Builder credits](/ai-builder/credit-management#get-entitlement-to-ai-builder-credits)

### Max concurrency calls reached

When you're sending too many requests concurrently per environment or tenant, you'll get this `500 Internal Server Error` `MaxConcurrentPlexCallsReachedException` error:

```json
{ 
   "error": { 
       "code": "0x80048d0a", 
       "message": "{\"operationStatus\":\"Error\",\"error\":{\"type\":\"Error\",\"code\":\"Unknown\",\"message\":\"Unhandled exception: Microsoft.PowerAI.MiddleEarth.HttpService.CodeInterpreter.Exceptions.MaxConcurrentPlexCallsReachedException\"},\"predictionId\":null}" 
   } 
}
```

A PCF control that encounters this error displays this message: **Server error. Please try again later or contact administrator.**

The resolution of this error is to send fewer requests. Wait a short time and try again. There's no `RetryAfter` response header to recommend how long you should wait.
