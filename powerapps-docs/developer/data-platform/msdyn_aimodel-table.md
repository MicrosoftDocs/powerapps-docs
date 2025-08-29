---
title: "AI Model table"
description: "Learn about the capabilities of the AI Model table."
ms.date: 08/29/2025
ms.reviewer: jdaly
ms.topic: article
author: MKBajwa-PM
ms.author: mbajwa
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - ColinBe
---
# AI Model table

The [AI Model (msdyn_AIModel) table](reference/entities/msdyn_aimodel.md) represents machine learning models used to provide AI-driven capabilities such as predictions, classifications, and recommendations. This table is essential for anyone who wants to integrate AI models into their business applications. It provides metadata and configuration details for each AI model, enabling automation, retraining, and inference scheduling.

The Web API exposes the [msdyn_aimodel EntityType](xref:Microsoft.Dynamics.CRM.msdyn_aimodel).

## Columns

AI Model table has the following writable columns:

<!-- Writable columns are usually the most interesting ones -->

|Name|Type|Description|
|---|---|---|
|`msdyn_ActiveRunConfigurationId`|Lookup| Unique identifier for the current active run configuration id associated with AIModel.|
|`msdyn_AIModelCatalog`|Lookup|Lookup to AI Model Catalog, which organizes and categorizes AI models for easier management and discovery.|
|`msdyn_AIModelId`|Uniqueidentifier|Unique identifier for the AI Model.|
|`msdyn_ModelCreationContext`|Memo|Contains metadata about the context in which the model was created, such as the data sources, parameters, and environment.|
|`msdyn_Name`|String|The name of the AI Model.|
|`msdyn_RetrainWorkflowId`|Lookup|Unique identifier for Retrain Process associated with AI Model, which can updates the model with new data to improve accuracy over time.|
|`msdyn_ScheduleInferenceWorkflowId`|Lookup|Unique identifier for the Schedule Inference Process associated with the AI Model. This process automates the execution of predictions at scheduled intervals.|
|`msdyn_ShareWithOrganizationOnCreate`|Boolean|Indicates whether the AI Model should be shared with the organization upon creation.|
|`msdyn_TemplateId`|Lookup|Unique identifier for [AI Template](reference/entities/msdyn_aitemplate.md) associated with AIModel. Templates define the structure and expected inputs/outputs of the model.|
|`OwnerId`|Owner|The owner of the AI Model record.|
|`statecode`|State|Status of the AI Model.|
|`statuscode`|Status|Reason for the status of the AI Model.|

### Retrieve AI Model data

### [SDK for .NET](#tab/sdk)

```csharp
var query = new QueryExpression("msdyn_aimodel")
{
    ColumnSet = new ColumnSet("msdyn_name", "msdyn_aimodelid")
};

var results = service.RetrieveMultiple(query);

foreach (var entity in results.Entities)
{
    Console.WriteLine($"Model Name: {entity["msdyn_name"]}, ID: {entity["msdyn_aimodelid"]}");
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

## Actions

AI Model table supports the following actions:

|Name|Description|
|---|---|
|[AddToFeedbackLoop](xref:Microsoft.Dynamics.CRM.AddToFeedbackLoop)|Adds a feedback loop item to a model to improve its performance based on user input.|
|[BatchPrediction](xref:Microsoft.Dynamics.CRM.BatchPrediction)|Runs batch prediction on an AI Model.|
|[Predict](xref:Microsoft.Dynamics.CRM.Predict)|Uses the AI Model to make a real-time prediction.|
|[PredictByReference](xref:Microsoft.Dynamics.CRM.PredictByReference)|Run real-time prediction with reference to record to predict on.|
|[PredictionSchema](xref:Microsoft.Dynamics.CRM.PredictionSchema)|Retrieves the schema used for predictions, including input and output fields.|
|[SchedulePrediction](xref:Microsoft.Dynamics.CRM.SchedulePrediction)|Schedules a prediction job to run at specified intervals.|
|[ScheduleRetrain](xref:Microsoft.Dynamics.CRM.ScheduleRetrain)|Schedules retraining of an AI Model.|
|[UnschedulePrediction](xref:Microsoft.Dynamics.CRM.UnschedulePrediction)|Cancels a scheduled batch prediction job.|


## Predict action

The Predict action allows you to use an AI Model to generate predictions based on input data. This is typically used in real-time scenarios where immediate insights are needed, such as predicting customer churn or recommending next best actions.

### [SDK for .NET](#tab/sdk)

```csharp
// Create the input parameters for the Predict action
var inputParameters = new ParameterCollection
{
    { "version", "2.0" },
    {
        "requestv2", new Dictionary<string, object>
        {
            { "@odata.type", "#Microsoft.Dynamics.CRM.expando" },
            { "pai_sex", 1 },
            { "pai_age", 10 },
            {
                "patient", new Dictionary<string, object>
                {
                    { "@odata.type", "#Microsoft.Dynamics.CRM.expando" },
                    { "firstname", "John" },
                    { "lastname", "Smith" }
                }
            }
        }
    }
};

// Create the OrganizationRequest for the Predict action
var predictRequest = new OrganizationRequest("Microsoft.Dynamics.CRM.Predict")
{
    Parameters = inputParameters
};

// Set the target AI Model ID
predictRequest["Target"] = new EntityReference("msdyn_aimodel", new Guid("your-ai-model-id"));

// Execute the request
var response = service.Execute(predictRequest);

Console.WriteLine("Prediction Result:");
Console.WriteLine(response.Results);
```

### [Web API](#tab/webapi)

**Request**:
```http
POST msdyn_aimodels([AI Model ID])/Microsoft.Dynamics.CRM.Predict

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
    "responsev2": {
        "@odata.type": "#Microsoft.Dynamics.CRM.expando",
        "operationStatus": "Success",
        "predictionOutput": {
            "@odata.type": "#Microsoft.Dynamics.CRM.expando",
            "Prediction": true,
            "Likelihood": 0.7423451,
            "Explanation": "[{\"attributeName\": \"aib_thalach\", \"entityName\": \"aib_heartdisease\", \"weight\": 1.1121130981531835}, {\"attributeName\": \"aib_exang\", \"entityName\":\"aib_heartdisease\", \"weight\": 0.04764715190587494}, {\"attributeName\": \"aib_chol\", \"entityName\": \"aib_heartdisease\", \"weight\": 0.013412023876486838}]"
        }
    }
}
```

---
