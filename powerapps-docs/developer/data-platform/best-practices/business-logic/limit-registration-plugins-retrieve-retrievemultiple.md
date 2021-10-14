---
title: "Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages | MicrosoftDocs"
description: "Adding synchronous plug-in logic to the Retrieve and RetrieveMultiple message events can cause slowness."
services: ''
suite: powerapps
documentationcenter: na
author: jowells
manager: austinj
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 1/15/2019
ms.subservice: dataverse-developer
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

**Category**: Performance

**Impact potential**: Medium

<a name='symptoms'></a>

## Symptoms

Adding synchronous plug-in logic to the Retrieve and RetrieveMultiple message events can result in:

- Unresponsive model-driven apps
- Slow client interactions
- The browser stops responding

<a name='guidance'></a>

## Guidance

Evaluate the design of solutions that include plug-ins registered for the Retrieve and RetrieveMultiple messages.  In general, it is not recommended to register plug-ins for these messages due to the risks associated with slowing down the requests to return an entity record or records from various entry points.  However, it may be appropriate for the design of your application. An example of a common application would be the injection of additional filter criteria to a specific existing query. This allows a solution to compensate for what cannot be done in the user interface for views.  The view designer can only support a certain depth of complexity and then other options must be employed to augment the results or the query.

If it is an appropriate solution, then follow these tips to minimize the impact to the environment:

- Include conditions in the plug-in code to quickly check if the targeted logic needs to be performed. If it does not, then return quickly, refraining from executing unnecessary extra steps that will delay returning the data to the caller.

- Avoid including long running tasks, especially those that can be non-deterministic, such as the invocation of external service calls or complex queries to Dynamics 365.

- Limit or avoid querying for additional data from Microsoft Dataverse

### Virtual Entities

Most commonly Retrieve and RetrieveMultiple is called within plug-ins to retrieve data from external sources. The data from the external sources are rendered within Power Apps or used to work/manipulate existing data. Dynamics 365 (online), version 9.0 introduces a feature called [Virtual Entities](/dynamics365/customer-engagement/developer/virtual-entities/get-started-ve) which allows integration of data residing in external systems by seamlessly representing that data as entities in Power Apps, without replication of data and often without custom coding. Review the [Virtual Entities](/dynamics365/customer-engagement/developer/virtual-entities/get-started-ve) documentation for further information about the capabilities, limitations, and configuration.

### Retrieve Caution

Dataverse will trigger at least two Retrieve messages for each entity form load.  One retrieve contains limited attributes, which can vary by entity, and subsequent calls will include more attributes.  If you expect a single action to occur during the loading of a form, then do not rely strictly on the trigger of a Retrieve message.

<a name='additional'></a>

## Additional information

The `Retrieve` and `RetrieveMultiple` messages are two of the most frequently processed messages. The `Retrieve` message is triggered when opening up an entity form or when an entity is being accessed using the `Retrieve` operation in one of the service endpoints. `RetrieveMultiple` is triggered due to various actions in the application and service endpoints, for example, when populating a grid in the user interface.  Adding synchronous plug-in logic to these message events can cause slowness.

<a name='seealso'></a>

### See also

[Performance Optimizations for Microsoft Dynamics CRM Online](/dynamics/s-e/)<br />
[Create and edit virtual entities that contain data from an external data source](../../../../maker/data-platform/create-edit-virtual-entities.md)<br />


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]