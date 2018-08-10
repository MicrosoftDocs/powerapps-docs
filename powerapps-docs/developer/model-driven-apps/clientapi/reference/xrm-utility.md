---
title: "Xrm.Utility (Client API reference)| MicrosoftDocs"
ms.date: 11/10/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: c044f7b8-7803-45fb-b99c-df01800c3b2a
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Xrm.Utility (Client API reference)



Provides a container for useful methods.

## Methods 

|Method | Description | 
| ------------- |-------------| 
|[closeProgressIndicator](xrm-utility/closeProgressIndicator.md) |[!INCLUDE[./xrm-utility/includes/closeProgressIndicator-description.md](./xrm-utility/includes/closeProgressIndicator-description.md)]|
|[getAllowedStatusTransitions](xrm-utility/getAllowedStatusTransitions.md) |[!INCLUDE[./xrm-utility/includes/getAllowedStatusTransitions-description.md](./xrm-utility/includes/getAllowedStatusTransitions-description.md)]|
|[getEntityMetadata](xrm-utility/getEntityMetadata.md) |[!INCLUDE[./xrm-utility/includes/getEntityMetadata-description.md](./xrm-utility/includes/getEntityMetadata-description.md)]|
|[getGlobalContext](xrm-utility/getGlobalContext.md) |[!INCLUDE[./xrm-utility/includes/getGlobalContext-description.md](./xrm-utility/includes/getGlobalContext-description.md)]|
|[getLearningPathAttributeName](xrm-utility/getLearningPathAttributeName.md) |[!INCLUDE[./xrm-utility/includes/getLearningPathAttributeName-description.md](./xrm-utility/includes/getLearningPathAttributeName-description.md)]|
|[getResourceString](xrm-utility/getResourceString.md) |[!INCLUDE[./xrm-utility/includes/getResourceString-description.md](./xrm-utility/includes/getResourceString-description.md)]|
|[invokeProcessAction](xrm-utility/invokeProcessAction.md) |[!INCLUDE[./xrm-utility/includes/invokeProcessAction-description.md](./xrm-utility/includes/invokeProcessAction-description.md)]|
|[lookupObjects](xrm-utility/lookupObjects.md) |[!INCLUDE[./xrm-utility/includes/lookupObjects-description.md](./xrm-utility/includes/lookupObjects-description.md)]|
|[refreshParentGrid](xrm-utility/refreshParentGrid.md) |[!INCLUDE[./xrm-utility/includes/refreshParentGrid-description.md](./xrm-utility/includes/refreshParentGrid-description.md)]|
|[showProgressIndicator](xrm-utility/showProgressIndicator.md) |[!INCLUDE[./xrm-utility/includes/showProgressIndicator-description.md](./xrm-utility/includes/showProgressIndicator-description.md)]|

## Deprecated methods

The following table lists the new methods you should use instead of the deprecated methods in the **Xrm.Utility** namespace. These methods were deprecated in v9.0.

|Deprecated Method | New method to be used | 
| ------------- |-------------|
|[alertDialog](https://msdn.microsoft.com/library/jj602956.aspx#BKMK_alertDialog)|Xrm.Navigation.[openAlertDialog](Xrm-Navigation/openAlertDialog.md)|
|[confirmDialog](https://msdn.microsoft.com/library/jj602956.aspx#BKMK_confirmDialog)|Xrm.Navigation.[openConfirmDialog](Xrm-Navigation/openConfirmDialog.md)|
|[getBarcodeValue](https://msdn.microsoft.com/library/jj602956.aspx#BKMK_getBarcodeValue)|Xrm.Device.[getBarcodeValue](Xrm-Device/getBarcodeValue.md)|
|[getCurrentPosition](https://msdn.microsoft.com/library/jj602956.aspx#BKMK_getCurrentPosition)|Xrm.Device.[getCurrentPosition](Xrm-Device/getCurrentPosition.md)|
|[openEntityForm](https://msdn.microsoft.com/library/jj602956.aspx#BKMK_OpenEntityForm)|Xrm.Navigation.[openForm](Xrm-Navigation/openForm.md)|
|[openQuickCreate](https://msdn.microsoft.com/library/jj602956.aspx#BKMK_openQuickCreate)|Xrm.Navigation.[openForm](Xrm-Navigation/openForm.md)|
|[openWebResource](https://msdn.microsoft.com/library/jj602956.aspx#BKMK_OpenWebResource)|Xrm.Navigation.[openWebResource](Xrm-Navigation/openWebResource.md)|


### Related topics

[Client API execution context](../clientapi-execution-context.md)

[Client API Xrm object](../clientapi-xrm.md)

[Client API reference](../reference.md)

[Deprecated client APIs](/dynamics365/get-started/whats-new/customer-engagement/important-changes-coming#some-client-apis-are-deprecated)

