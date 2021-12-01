---
title: "formContext.data.process (Client API reference) in model-driven apps| MicrosoftDocs"
description: "Learn about working with processes in model-driven apps using client API."
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 32e8d1d0-4093-4588-a517-2930eec34dce
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# formContext.data.process (Client API reference)



Provides events, methods, and objects to interact with the business process flow data on a form. See [formContext.ui.process (Client API reference)](formContext-ui-process.md) for methods to interact with the business process flow control on the form.

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]


## Process events and event handler methods

Use the following events and event handler methods to write scripts for business process flows.

|Event | Event handler methods|
|--|--|
|[OnPreProcessStatusChange](events/onpreprocessstatuschange.md)|[addOnPreProcessStatusChange](formContext-data-process/eventhandlers/addOnPreProcessStatusChange.md)<br/>[removeOnPreProcessStatusChange](formContext-data-process/eventhandlers/removeOnPreProcessStatusChange.md)|
|[OnProcessStatusChange](events/onprocessstatuschange.md)|[addOnProcessStatusChange](formContext-data-process/eventhandlers/addOnProcessStatusChange.md)<br/>[removeOnProcessStatusChange](formContext-data-process/eventhandlers/removeOnProcessStatusChange.md)|
|[OnStageChange](events/OnStageChange.md)|[addOnStageChange](formContext-data-process/eventhandlers/addOnStageChange.md)<br/>[removeOnStageChange](formContext-data-process/eventhandlers/removeOnStageChange.md)|
|[OnStageSelected](events/OnStageSelected.md)|[addOnStageSelected](formContext-data-process/eventhandlers/addOnStageSelected.md)<br/>[removeOnStageSelected](formContext-data-process/eventhandlers/removeOnStageSelected.md)|

## Active Process methods

Use these methods to retrieve information about the active process and set a different process as the active process.

|Name | Description |
|--|--|
|[getActiveProcess](formcontext-data-process/activeprocess/getActiveProcess.md)|[!INCLUDE[formcontext-data-process/activeprocess/includes/getActiveProcess-description.md](formcontext-data-process/activeprocess/includes/getActiveProcess-description.md)]|
|[setActiveProcess](formcontext-data-process/activeprocess/setActiveProcess.md)|[!INCLUDE[formcontext-data-process/activeprocess/includes/setActiveProcess-description.md](formcontext-data-process/activeprocess/includes/setActiveProcess-description.md)]|

## Process methods 

A process contains the data for a business process flow. Use the methods to access properties of the process.

|Name | Description |
|--|--|
|[getId](formcontext-data-process/process/getId.md)|[!INCLUDE[formcontext-data-process/process/includes/getId-description.md](formcontext-data-process/process/includes/getId-description.md)]|
|[getName](formcontext-data-process/process/getName.md)|[!INCLUDE[formcontext-data-process/process/includes/getName-description.md](formcontext-data-process/process/includes/getName-description.md)]|
|[getStages](formcontext-data-process/process/getStages.md)|[!INCLUDE[formcontext-data-process/process/includes/getStages-description.md](formcontext-data-process/process/includes/getStages-description.md)]|
|[isRendered](formcontext-data-process/process/isRendered.md)|[!INCLUDE[formcontext-data-process/process/includes/isRendered-description.md](formcontext-data-process/process/includes/isRendered-description.md)]|


## ProcessInstance methods

Use these methods to retrieve information about all the process instances for a record and to set a process instance as the active instance.

|Name | Description |
|--|--|
|[getProcessInstances](formContext-data-process/getProcessInstances.md)|[!INCLUDE[formcontext-data-process/includes/getProcessInstances-description.md](formcontext-data-process/includes/getProcessInstances-description.md)]|
|[setActiveProcessInstance](formContext-data-process/setActiveProcessInstance.md)|[!INCLUDE[formcontext-data-process/includes/setActiveProcessInstance-description.md](formcontext-data-process/includes/setActiveProcessInstance-description.md)]|


## Instance methods 

A process instance contains the data for an instance of the business process flow. Use the methods to access properties of the process instance.

|Name | Description |
|--|--|
|[getInstanceId](formcontext-data-process/instance/getInstanceId.md)|[!INCLUDE[formcontext-data-process/instance/includes/getInstanceId-description.md](formcontext-data-process/instance/includes/getInstanceId-description.md)]|
|[getInstanceName](formcontext-data-process/instance/getInstanceName.md)|[!INCLUDE[formcontext-data-process/instance/includes/getInstanceName-description.md](formcontext-data-process/instance/includes/getInstanceName-description.md)]|
|[getStatus](formcontext-data-process/instance/getStatus.md)|[!INCLUDE[formcontext-data-process/instance/includes/getStatus-description.md](formcontext-data-process/instance/includes/getStatus-description.md)]|
|[setStatus](formcontext-data-process/instance/setStatus.md)|[!INCLUDE[formcontext-data-process/instance/includes/setStatus-description.md](formcontext-data-process/instance/includes/setStatus-description.md)]|

## Active Stage methods

Use these methods to retrieve information about the active stage and set a different stage as the active stage.

|Name | Description |
|--|--|
|[getActiveStage](formcontext-data-process/activestage/getActiveStage.md)|[!INCLUDE[formcontext-data-process/activestage/includes/getActiveStage-description.md](formcontext-data-process/activestage/includes/getActiveStage-description.md)]|
|[setActiveStage](formcontext-data-process/activestage/setActiveStage.md)|[!INCLUDE[formcontext-data-process/activestage/includes/setActiveStage-description.md](formcontext-data-process/activestage/includes/setActiveStage-description.md)]|

## Stage methods 

A stage contains the data for a stage in a business process flow. Use the methods to access properties of the stage.

|Name | Description|
|--|--|
|[getCategory](formcontext-data-process/stage/getCategory.md)|[!INCLUDE[formcontext-data-process/stage/includes/getCategory-description.md](formcontext-data-process/stage/includes/getCategory-description.md)]|
|[getEntityName](formcontext-data-process/stage/getEntityName.md)|[!INCLUDE[formcontext-data-process/stage/includes/getEntityName-description.md](formcontext-data-process/stage/includes/getEntityName-description.md)]|
|[getId](formcontext-data-process/stage/getId.md)|[!INCLUDE[formcontext-data-process/stage/includes/getId-description.md](formcontext-data-process/stage/includes/getId-description.md)]|
|[getName](formcontext-data-process/stage/getName.md)|[!INCLUDE[formcontext-data-process/stage/includes/getName-description.md](formcontext-data-process/stage/includes/getName-description.md)]|
|[getNavigationBehavior](formcontext-data-process/stage/getNavigationBehavior.md)|[!INCLUDE[formcontext-data-process/stage/includes/getNavigationBehavior-description.md](formcontext-data-process/stage/includes/getNavigationBehavior-description.md)]|
|[getStatus](formcontext-data-process/stage/getStatus.md)|[!INCLUDE[formcontext-data-process/stage/includes/getStatus-description.md](formcontext-data-process/stage/includes/getStatus-description.md)]|
|[getSteps](formcontext-data-process/stage/getSteps.md)|[!INCLUDE[formcontext-data-process/stage/includes/getSteps-description.md](formcontext-data-process/stage/includes/getSteps-description.md)]|

## Step methods

A step contains the data for a step in a stage in a business process flow. Use the methods to access properties of the step.

|Name | Description|
|--|--|
|[getAttribute](formcontext-data-process/step/getAttribute.md)|[!INCLUDE[formcontext-data-process/step/includes/getAttribute-description.md](formcontext-data-process/step/includes/getAttribute-description.md)]|
|[getName](formcontext-data-process/step/getName.md)|[!INCLUDE[formcontext-data-process/step/includes/getName-description.md](formcontext-data-process/step/includes/getName-description.md)]|
|[getProgress](formcontext-data-process/step/getProgress.md)|[!INCLUDE[formcontext-data-process/step/includes/getProgress-description.md](formcontext-data-process/step/includes/getProgress-description.md)]|
|[isRequired](formcontext-data-process/step/isRequired.md)|[!INCLUDE[formcontext-data-process/step/includes/isRequired-description.md](formcontext-data-process/step/includes/isRequired-description.md)]|
|[setProgress](formcontext-data-process/step/setProgress.md)|[!INCLUDE[formcontext-data-process/step/includes/setProgress-description.md](formcontext-data-process/step/includes/setProgress-description.md)]|

## Navigation methods

Use these methods to move to next and previous stages. Both these methods will cause the OnStageChange event to occur.

|Name | Description|
|--|--|
|[moveNext](formContext-data-process/navigation/moveNext.md)|[!INCLUDE[formcontext-data-process/navigation/includes/moveNext-description.md](formcontext-data-process/navigation/includes/moveNext-description.md)]|
|[movePrevious](formContext-data-process/navigation/movePrevious.md)|[!INCLUDE[formcontext-data-process/navigation/includes/movePrevious-description.md](formcontext-data-process/navigation/includes/movePrevious-description.md)]|

## Other useful methods

Use these methods to find information about the stages in the active path, enabled processes, and selected stage.

|Name | Description|
|--|--|
|[getActivePath](formContext-data-process/activepath/getActivePath.md)|[!INCLUDE[formcontext-data-process/activepath/includes/getActivePath-description.md](formcontext-data-process/activepath/includes/getActivePath-description.md)]|
|[getEnabledProcesses](formContext-data-process/getEnabledProcesses.md)|[!INCLUDE[formcontext-data-process/includes/getEnabledProcesses-description.md](formcontext-data-process/includes/getEnabledProcesses-description.md)]|
|[getSelectedStage](formContext-data-process/getSelectedStage.md)|[!INCLUDE[formcontext-data-process/includes/getSelectedStage-description.md](formcontext-data-process/includes/getSelectedStage-description.md)]|

### Related topics

[formContext.ui.process (Client API reference)](formContext-ui-process.md)

[Understand Xrm object model](../understand-clientapi-object-model.md)

[Controls (Client API reference)](controls.md)






[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]