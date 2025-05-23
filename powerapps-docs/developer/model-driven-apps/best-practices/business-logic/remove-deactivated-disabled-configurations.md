---
title: "Remove deactivated or disabled customizations "
description: "Deactivated or disabled customizations should be removed from a solution to improve solution management and to decrease the risk of utilizing or managing an outdated component."
suite: powerapps
author: MitiJ
ms.author: mijosh
ms.reviewer: jdaly
ms.topic: article
ms.date: 1/15/2019
ms.subservice: mda-developer
search.audienceType: 
  - developer
---
# Remove deactivated or disabled customizations

**Category**: Maintainability, Supportability

**Impact potential**: Low

<a name='symptoms'></a>

## Symptoms

Deactivated or disabled customizations should be removed from a solution to improve solution management and to decrease the risk of utilizing or managing an outdated component.

<a name='guidance'></a>

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

## Guidance

Ensure that each solution component that is deactivated, or disabled, has been done so intentionally.  If so and will no longer be utilized, consider removing it from the solution to prevent confusion for users and system customizers. These components include:

- SDK Message Processing Steps
- Processes
- Record Creation and Update Rules
- SLAs

As well as table components such as:

- Forms
- Views
- Business Rules

![Deactivated Processes.](../media/deactivated-processes.png)

<a name='seealso'></a>

### See also

[Apply custom business logic with business rules and flows in model-driven apps](../../../../maker/model-driven-apps/guide-staff-through-common-tasks-processes.md)<br />
[Events in forms and grids in model-driven apps](../../clientapi/events-forms-grids.md)<br/>

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
