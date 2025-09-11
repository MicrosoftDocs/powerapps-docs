---
title: "Code interpreter for developers"
description: "Learn how developers can use code interpreter enabled prompts."
ms.date: 09/11/2025
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
> A common scenario for this code interpreter enabled prompts is to generate UI experiences for model-driven applications using PCF components. Refer to the [Code interpreter PCF component sample](code-interpreter-pcf-sample.md) for an example.

## Enable code interpreter for the environment

Code interpreter must be enabled for each environment before you can use it. The default setting is **Off**. [Learn how to enable code interpreter using the Power Platform Admin center](/microsoft-copilot-studio/code-interpreter-for-prompts#administration-of-code-interpreter)

Developers can use the Power Platform [Environment Management Settings](/rest/api/power-platform/environmentmanagement/environment-management-settings) APIs to read or set the `CopilotStudio_CodeInterpreter` boolean property to enable code interpreter for an environment.

## Code interpreter enabled prompts

Every prompt created using Microsoft Copilot Studio or AI Builder creates a new record in the Dataverse [AI Model (msdyn_AIModel) table](reference/entities/msdyn_aimodel.md). You need the ID of the row when you invoke the `Predict` message.

You can't create a prompt by creating a new row in the `msdyn_AIModel`. Prompts are created updated using the [AIModelPublish](/power-apps/developer/data-platform/webapi/reference/aimodelpublish) message. This public message is for internal use only. You must use the UI to create code interpreter enabled prompts. You must also make sure that each prompt is enabled for code interpreter. How you do this is slightly different depending on the UI. See these instructions:

- [Enable code interpreter in Power Apps AI Hub](/microsoft-copilot-studio/code-interpreter-for-prompts#enable-code-interpreter-in-power-apps-ai-hub)
- [Enable code interpreter in prompt tool within a Copilot Studio agent](/microsoft-copilot-studio/code-interpreter-for-prompts#enable-code-interpreter-in-prompt-tool-within-an-agent)

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

- The ID of the `msdyn_AIModel` record. How you set this depends on whether you use the SDK for .NET or Web API.
- The data that contains the parameters that the prompt is configured to accept. This is passed as a parameter named `requestv2`. [Learn more about the `requestv2` parameter](#requestv2-parameter)
- The `version` parameter. The value is always `"2.0"`.

#### `requestv2` parameter

This parameter is configured as an *open type*. [Learn more about how to use open types in general](use-open-types.md#how-to-use-open-types)

An open type is a dictionary that contains keys and values. The values can also be dictionaries, so it is possible to send complex, hierarchical data to an open type parameter.

### [SDK for .NET](#tab/sdk)

With the SDK for .NET, use the [Entity class](/dotnet/api/microsoft.xrm.sdk.entity) and set the [Attributes](/dotnet/api/microsoft.xrm.sdk.entity.attributes) collection with the values.  The key difference in this scenario is that the `Entity` instance doesn't have a [LogicalName](/dotnet/api/microsoft.xrm.sdk.entity.logicalname) set, so it doesn't refer to a specific Dataverse table.

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

As explained in [Use Entity as a dictionary](use-open-types.md?tabs=webapi#use-entity-as-a-dictionary), set the `requestv2` property with a dictionary that includes an `@odata.type` property set to `"Microsoft.Dynamics.CRM.expando"`.  This indicates the value is an open type.

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
                    "base64_content": "[Sales_Proposal.pdf base64 content]",
                    "content_type": "application/pdf",
                    "file_name": "Sales_Proposal.pdf"
                }
            ],
            "structuredOutput": {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "mimetype": "text/markdown",
                "text": "# Sales Proposal\n\nSales proposal for Example record Example 2.\n\n[Download the proposal PDF here](Sales_Proposal.pdf)"
            },
            "artifacts":{
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "Sales_Proposal": {
                    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                    "artifactName": "Sales_Proposal.pdf",
                    "mimeType": "application/pdf",
                    "base64Content": "[Sales_Proposal.pdf base64 content]"
        }
      }
    }
  }
}
```

---

### Processing the response

The [PredictResponse complex type](/power-apps/developer/data-platform/webapi/reference/predictresponse) contains the response from the `Predict` message in web API. The SDK for .NET has similar response properties.

| Property | Type | Description |
|----------|------|-------------|
|`overrideHttpStatusCode`|String|In case the prediction is not completed, 202 will indicate that a polling is necessary.|
|`overrideLocation`|String| The location of the polling (do a GET on this to poll for the result).|
|`overrideRetryAfter`|String|Suggestion on when to try polling.|
|`response`|String|This property should always be null.|
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
| `finishReason` | string | Reason generation stopped. |
| `code` | string | Python Source code or placeholder describing executed code. |
| `signature` | string | a Base64‑encoded, versioned metadata and integrity token |
| `logs` | string | Execution log output (if provided). |
| `codeThinking` | object | Empty/internal placeholder object. |
| `files` | array of objects | Generated file artifacts with name, content type, and base64 content. |
| `structuredOutput` | object | Canonical form of main output (`text` + `mimetype`). |
| `artifacts` | object | Map of artifact identifiers to metadata & base64 content. |
