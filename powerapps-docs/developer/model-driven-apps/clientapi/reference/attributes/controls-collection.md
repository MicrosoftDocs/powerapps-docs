---
title: "Controls collection (Client API reference)| MicrosoftDocs"
description: "Learn about how to access controls associated with attributes."
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: d5f3c0c5-b267-42a8-82e8-8c4a1cda3752
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Controls collection (Client API reference)



Use the Controls collection to access controls associated with attributes. 

Because each attribute may be represented more than one time on the page, the controls collection provides access to all controls representing that attribute. If the attribute is represented by only one field in the page, the length of this collection will be 1. When you use the control getName method the name of the first control will be the same as the name of the attribute. The second instance of a control for that attribute will be **<attributeName>1**. The pattern **<attributeName>+N** will continue for each additional control added to the form for a specific attribute.

When a form displays a business process flow control in the header, additional controls will be added for each attribute that is displayed in the business process flow. These controls have a unique name like the following: **header_process_<attribute name>**.

When performing actions on controls that are tied to an attribute you should always consider that the control may be included on the page more than once and you should generally perform the same actions for each control for the attribute. You can do this by looping through the attribute controls collection and perform the actions on each control.

### Related topics

[attributes (Client API reference)](../attributes.md)


