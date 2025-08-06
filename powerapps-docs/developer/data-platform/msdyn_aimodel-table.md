---
title: "AI Model table"
description: "Learn about the capabilities of the AI Model table."
ms.date: 08/05/2025
ms.reviewer: jdaly
ms.topic: article
author: MKBajwa-PM
ms.author: mbajwa
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# AI Model table

The [AI Model (msdyn_AIModel) table](reference/entities/msdyn_aimodel.md)... TODO: explain what this table is for, why is it useful and why people should read more about it..

The Web API exposes the [msdyn_aimodel EntityType](xref:Microsoft.Dynamics.CRM.msdyn_aimodel).

## Columns

AI Model table has the following writable columns:

<!-- Writable columns are usually the most interesting ones -->

|Name|Type|Description|
|---|---|---|
|`msdyn_ActiveRunConfigurationId`|Lookup| Unique identifier for the active run configuration id associated with AIModel.  TODO: Explain why this look up has no `Targets` property value. Which kind of records does it point to?|
|`msdyn_AIModelCatalog`|Lookup|Lookup to AI Model Catalog this table was excluded in the reference but can be added back.|
|`msdyn_AIModelId`|Uniqueidentifier|Unique identifier for the AI Model|
|`msdyn_ModelCreationContext`|Memo|TODO: explain what this is, or not. Does it contain information of interest?|
|`msdyn_Name`|String|The name of the AI Model. TODO: Are these values unique? (I don't think so)|
|`msdyn_RetrainWorkflowId`|Lookup|Unique identifier for Retrain Process associated with AI Model. TODO: What is a Retrain process?|
|`msdyn_ScheduleInferenceWorkflowId`|Lookup|Unique identifier for Schedule Inference Process associated with AI Model.TODO: What is a Schedule Inference Process? |
|`msdyn_ShareWithOrganizationOnCreate`|Boolean|TODO add missing description?|
|`msdyn_TemplateId`|Lookup|Unique identifier for [AI Template](reference/entities/msdyn_aitemplate.md) associated with AIModel.|
|`OwnerId`|Owner|Owner Id|
|`statecode`|State|Status of the AI Model|
|`statuscode`|Status|Reason for the status of the AI Model|

### Retrieve AI Model data

TODO: Add some example queries here  I can help with these.

### [SDK for .NET](#tab/sdk)

```csharp
// Add .NET sample code using the SDK here
 ///I can help with these.
```

### [Web API](#tab/webapi)

**Request**:
```http
POST [Organization URI]/api/data/v9.2/
```

**Response**:
```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
  
}
```

---

## Actions

AI Model table supports the following actions:

|Name|Description|
|---|---|
|[AddToFeedbackLoop](xref:Microsoft.Dynamics.CRM.AddToFeedbackLoop)|API to add a feedback loop item to a model.|
|[BatchPrediction](xref:Microsoft.Dynamics.CRM.BatchPrediction)|Runs batch prediction on an AI Model.|
|[Predict](xref:Microsoft.Dynamics.CRM.Predict)|Uses AI to make a prediction.|
|[PredictByReference](xref:Microsoft.Dynamics.CRM.PredictByReference)|Run real time prediction with reference to record to predict on.|
|[PredictionSchema](xref:Microsoft.Dynamics.CRM.PredictionSchema)|Gets the prediction schema.|
|[SchedulePrediction](xref:Microsoft.Dynamics.CRM.SchedulePrediction)|Schedules a prediction for an AI model.|
|[ScheduleRetrain](xref:Microsoft.Dynamics.CRM.ScheduleRetrain)|Schedules retraining for an AI model.|
|[UnschedulePrediction](xref:Microsoft.Dynamics.CRM.UnschedulePrediction)|Unschedules batch prediction on an AI model.|


## Predict action

TODO Describe this action in more detail here

### [SDK for .NET](#tab/sdk)

```csharp
// Add .NET sample code using the SDK here
//  I can help with these.
```

### [Web API](#tab/webapi)

**Request**:
```http
POST [Organization URI]/api/data/v9.2/
 I can help with these.
```

**Response**:
```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
  
}
```

---