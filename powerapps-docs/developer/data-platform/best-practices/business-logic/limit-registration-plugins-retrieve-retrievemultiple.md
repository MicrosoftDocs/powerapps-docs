---
title: "Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages | MicrosoftDocs"
description: "Adding synchronous plug-in logic to the Retrieve and RetrieveMultiple message events can cause slowness."
suite: powerapps
author: sakaralems
ms.author: sakarale
ms.reviewer: pehecke
ms.topic: article
ms.date: 03/02/2026
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---
# Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages

**Category**: Performance

**Impact potential**: Medium

<a name='symptoms'></a>

## Symptoms

Adding synchronous plug-in logic to the `Retrieve` and `RetrieveMultiple` message events can result in:

- Unresponsive model-driven apps
- Slow client interactions
- The browser stops responding

<a name='guidance'></a>

## Guidance

Evaluate the design of solutions that include plug-ins registered for the `Retrieve` and `RetrieveMultiple` messages. In general, don't register plug-ins for these messages because they can slow down the requests to return an entity record or records from various entry points. However, it might be appropriate for the design of your application. An example of a common application is the injection of more filter criteria to a specific existing query. This approach allows a solution to compensate for what can't be done in the user interface for views. The view designer supports only a certain depth of complexity. To go beyond that depth, you must employ other options to augment the results or the query.

If it's an appropriate solution, follow these tips to minimize the impact to the environment:

- Include conditions in the plug-in code to quickly check if the targeted logic needs to be performed. If it doesn't, return quickly, refraining from executing unnecessary extra steps that delay returning the data to the caller.

- Avoid including long running tasks, especially nondeterministic tasks, such as the invocation of external service calls or complex queries to Dataverse.

- Limit or avoid querying for more data from Microsoft Dataverse.

### Virtual entities

Developers typically call `Retrieve` and `RetrieveMultiple` within plug-ins to get data from external sources. You can display the data from external sources within Power Apps or use it to work with and manipulate existing data. By using Dataverse [virtual tables](../../../../maker/data-platform/create-edit-virtual-entities.md), you can integrate data that resides in external systems by seamlessly representing that data as tables in Power Apps, without replicating data and often without custom coding.

### Retrieve caution

Dataverse triggers at least two `Retrieve` messages for each entity form load. One retrieve contains limited attributes, which can vary by entity, and subsequent calls include more attributes. If you expect a single action to occur during the loading of a form, then don't rely strictly on the trigger of a `Retrieve` message.

<a name='additional'></a>

## Additional information

The `Retrieve` and `RetrieveMultiple` messages are two of the most frequently processed messages. The system triggers the `Retrieve` message when you open an entity form or access an entity by using the `Retrieve` operation in one of the service endpoints. Various actions in the application and service endpoints trigger `RetrieveMultiple`. For example, when the user interface populates a grid, it triggers `RetrieveMultiple`. Adding synchronous plug-in logic to these message events can cause slowness.

<a name='seealso'></a>

### See also

[Performance Optimizations for Microsoft Dynamics CRM Online](/dynamics/s-e/)<br />
[Create and edit virtual entities that contain data from an external data source](../../../../maker/data-platform/create-edit-virtual-entities.md)<br />


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
