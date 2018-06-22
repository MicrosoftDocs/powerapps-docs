---
title: "formContext.ui.quickForms (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
description: "Learn about working with processes in Customer Engagement using client API."
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: a04043de-3497-433a-ae73-4101806dd931
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# formContext.ui.quickForms (Client API reference)

[!INCLUDE[](../../../includes/cc_applies_to_update_9_0_0.md)]

Provides methods to access all the quick view controls and its constituent controls on the Customer Engagement forms when using the new form rendering engine (also called "turbo forms"). A quick view control is a quick view form added to a main form in Customer Engagement that enables you to view information about a related entity record within the main form. Data in constituent controls in a quick view control cannot be edited.

The **quickForms** collection provides access to all the quick view controls on a form, and supports all the standard methods of the collections. See [Collections](collections.md)) for information about the collection methods. 

You can retrieve a quick view control in the **quickForms** collection by using the [get](collections/get.md) method by specifying either the index value (integer) or name (string) of the quick view control as the argument:

`quickViewControl = formContext.ui.quickForms.get(arg)`


## Quick form control Methods

|Name|Description|
|--|--|
|[getControl](formcontext-ui-quickForms/getControlType.md)|[!INCLUDE[formcontext-ui-quickForms/includes/getControl-description.md](formcontext-ui-quickForms/includes/getControl-description.md)]|
|[getControlType](formcontext-ui-quickForms/getControlType.md)|[!INCLUDE[formcontext-ui-quickForms/includes/getControlType-description.md](formcontext-ui-quickForms/includes/getControlType-description.md)]|
|[getDisabled](formcontext-ui-quickForms/getDisabled.md)|[!INCLUDE[formcontext-ui-quickForms/includes/getDisabled-description.md](formcontext-ui-quickForms/includes/getDisabled-description.md)]|
|[getLabel](formcontext-ui-quickForms/getLabel.md)|[!INCLUDE[formcontext-ui-quickForms/includes/getLabel-description.md](formcontext-ui-quickForms/includes/getLabel-description.md)]|
|[getName](formcontext-ui-quickForms/getName.md)|[!INCLUDE[formcontext-ui-quickForms/includes/getName-description.md](formcontext-ui-quickForms/includes/getName-description.md)]|
|[getParent](formcontext-ui-quickForms/getParent.md)|[!INCLUDE[formcontext-ui-quickForms/includes/getParent-description.md](formcontext-ui-quickForms/includes/getParent-description.md)]|
|[getVisible](formcontext-ui-quickForms/getVisible.md)|[!INCLUDE[formcontext-ui-quickForms/includes/getVisible-description.md](formcontext-ui-quickForms/includes/getVisible-description.md)]|
|[isLoaded](formcontext-ui-quickForms/isLoaded.md)|[!INCLUDE[formcontext-ui-quickForms/includes/isLoaded-description.md](formcontext-ui-quickForms/includes/isLoaded-description.md)]|
|[refresh](formcontext-ui-quickForms/refresh.md)|[!INCLUDE[formcontext-ui-quickForms/includes/refresh-description.md](formcontext-ui-quickForms/includes/refresh-description.md)]|
|[setDisabled](formcontext-ui-quickForms/setDisabled.md)|[!INCLUDE[formcontext-ui-quickForms/includes/setDisabled-description.md](formcontext-ui-quickForms/includes/setDisabled-description.md)]|
|[setFocus](formcontext-ui-quickForms/setFocus.md)|[!INCLUDE[formcontext-ui-quickForms/includes/setFocus-description.md](formcontext-ui-quickForms/includes/setFocus-description.md)]|
|[setLabel](formcontext-ui-quickForms/setLabel.md)|[!INCLUDE[formcontext-ui-quickForms/includes/setLabel-description.md](formcontext-ui-quickForms/includes/setLabel-description.md)]|
|[setVisible](formcontext-ui-quickForms/setVisible.md)|[!INCLUDE[formcontext-ui-quickForms/includes/setVisible-description.md](formcontext-ui-quickForms/includes/setVisible-description.md)]|


### Related topics

[formContext.ui](formContext-ui.md)