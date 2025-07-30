---
title: "Don't duplicate plug-in step registration | MicrosoftDocs"
description: "Duplicate plug-in step registration causes the plug-in to fire multiple times on the same message/event."
suite: powerapps
author: jowells
ms.author: jowells
ms.reviewer: jdaly
ms.topic: article
ms.date: 1/15/2019
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
---
# Don't duplicate plug-in step registration

**Category**: Performance

**Impact potential**: High

<a name='symptoms'></a>

## Symptoms

Duplicate plug-in step registration causes the plug-in to fire multiple times on the same message/event. Duplicate plug-in step registration could lead to:

- Delayed processing of asynchronous jobs when registered as an asynchronous execution mode.
- Degraded user performance experience when registered as a synchronous execution mode. Experiences include:
   
   - Unresponsive model-driven apps
   - Slow client interactions
   - The browser stops responding

<a name='guidance'></a>

## Guidance

Ensure you're updating existing plug-in registration steps rather than deleting and re-creating them. Additionally, only create and update plug-in registration steps in a supported manner.

<a name='problem'></a>

## Problematic patterns

> [!WARNING]
> These patterns should be avoided.

Deleting and recreating a step in the source instance (test, dev, preprod) creates a duplicate step being registered in the target environment if that step was registered before.

![Duplicate Plug-in Step Registration.](../media/duplicate-plugin-registration-step.png)

Manually creating the `SDKMessageProcessingSteps` with a new GUID or updating the existing GUID within the `customizations.xml` file results in a duplicate step being registered. These types of tasks are unsupported as outlined in [When to edit the customizations file](/power-platform/alm/when-edit-customization-file).

<a name='additional'></a>

## Additional information

Duplicate plug-in step registration could cause SQL deadlocking when the events are registered on an update message. When issuing an update on a record, SQL creates a row lock on that record. If another transaction tries to update that same record, it has to wait until the lock is released before it's able to make the update. If a timeout occurs, the transaction is rolled back and the update isn't committed to the SQL database.

<a name='seealso'></a>

### See also

[Register a plug-in](../../register-plug-in.md)
[Deadlocking](/previous-versions/sql/sql-server-2008-r2/ms177433(v=sql.105))<br />


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
