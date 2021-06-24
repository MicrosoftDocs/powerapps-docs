---
title: "Xrm.Utility (Client API reference)| MicrosoftDocs"
description: Provides container for useful methods.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Xrm.Utility (Client API reference)

Provides a container for useful methods.

## Methods 

|Method | Description | 
| ------------- |-------------| 
|[closeProgressIndicator](xrm-utility/closeProgressIndicator.md) |[!INCLUDE[./xrm-utility/includes/closeProgressIndicator-description.md](./xrm-utility/includes/closeProgressIndicator-description.md)]|
|[getAllowedStatusTransitions](xrm-utility/getAllowedStatusTransitions.md) |[!INCLUDE[./xrm-utility/includes/getAllowedStatusTransitions-description.md](./xrm-utility/includes/getAllowedStatusTransitions-description.md)]|
|[getEntityMetadata](xrm-utility/getEntityMetadata.md) |[!INCLUDE[./xrm-utility/includes/getEntityMetadata-description.md](./xrm-utility/includes/getEntityMetadata-description.md)]|
|[getEntityMainFormDescriptor](xrm-utility/getEntityMainFormDescriptor.md)|[!INCLUDE[./xrm-utility/includes/getEntityMainFormDescriptor-description.md](./xrm-utility/includes/getEntityMainFormDescriptor-description.md)]
|[getGlobalContext](xrm-utility/getGlobalContext.md) |[!INCLUDE[./xrm-utility/includes/getGlobalContext-description.md](./xrm-utility/includes/getGlobalContext-description.md)]|
|[getLearningPathAttributeName](xrm-utility/getLearningPathAttributeName.md) |[!INCLUDE[./xrm-utility/includes/getLearningPathAttributeName-description.md](./xrm-utility/includes/getLearningPathAttributeName-description.md)]|
|[getPageContext](xrm-utility/getPageContext.md) |[!INCLUDE[./xrm-utility/includes/getPageContext-description.md](./xrm-utility/includes/getPageContext-description.md)]|
|[getResourceString](xrm-utility/getResourceString.md) |[!INCLUDE[./xrm-utility/includes/getResourceString-description.md](./xrm-utility/includes/getResourceString-description.md)]|
|[invokeProcessAction](xrm-utility/invokeProcessAction.md) |[!INCLUDE[./xrm-utility/includes/invokeProcessAction-description.md](./xrm-utility/includes/invokeProcessAction-description.md)]|
|[lookupObjects](xrm-utility/lookupObjects.md) |[!INCLUDE[./xrm-utility/includes/lookupObjects-description.md](./xrm-utility/includes/lookupObjects-description.md)]|
|[refreshParentGrid](xrm-utility/refreshParentGrid.md) |[!INCLUDE[./xrm-utility/includes/refreshParentGrid-description.md](./xrm-utility/includes/refreshParentGrid-description.md)]|
|[showProgressIndicator](xrm-utility/showProgressIndicator.md) |[!INCLUDE[./xrm-utility/includes/showProgressIndicator-description.md](./xrm-utility/includes/showProgressIndicator-description.md)]|

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

## Deprecated methods

The following table lists the new methods you should use instead of the deprecated methods in the **Xrm.Utility** namespace. These methods were deprecated in v9.0.

|Deprecated Method | New method to be used | 
| ------------- |-------------|
|[alertDialog](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#BKMK_alertDialog)|Xrm.Navigation.[openAlertDialog](Xrm-Navigation/openAlertDialog.md)|
|[confirmDialog](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#BKMK_confirmDialog)|Xrm.Navigation.[openConfirmDialog](Xrm-Navigation/openConfirmDialog.md)|
|[getBarcodeValue](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#BKMK_getBarcodeValue)|Xrm.Device.[getBarcodeValue](Xrm-Device/getBarcodeValue.md)|
|[getCurrentPosition](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#BKMK_getCurrentPosition)|Xrm.Device.[getCurrentPosition](Xrm-Device/getCurrentPosition.md)|
|[openEntityForm](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#BKMK_OpenEntityForm)|Xrm.Navigation.[openForm](Xrm-Navigation/openForm.md)|
|[openQuickCreate](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#BKMK_openQuickCreate)|Xrm.Navigation.[openForm](Xrm-Navigation/openForm.md)|
|[openWebResource](/previous-versions/dynamicscrm-2016/developers-guide/jj602956(v=crm.8)#BKMK_OpenWebResource)|Xrm.Navigation.[openWebResource](Xrm-Navigation/openWebResource.md)|


### Related topics

[Client API execution context](../clientapi-execution-context.md)

[Client API Xrm object](../clientapi-xrm.md)

[Client API reference](../reference.md)

[Deprecated client APIs](/dynamics365/get-started/whats-new/customer-engagement/important-changes-coming#some-client-apis-are-deprecated)



[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]