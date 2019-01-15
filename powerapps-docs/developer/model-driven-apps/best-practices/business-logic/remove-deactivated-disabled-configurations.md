---
title: "Remove deactivated or disabled customizations | MicrosoftDocs"
description: "Deactivated or disabled customizations should be removed from a solution to improve solution management and to decrease the risk of utilizing or managing an outdated component."
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
ms.date: 12/12/2018
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Remove deactivated or disabled customizations

**Category**: Maintainability, Supportability

**Impact potential**: Low

<a name='symptoms'></a>

## Symptoms

Deactivated or disabled customizations should be removed from a solution to improve solution management and to decrease the risk of utilizing or managing an outdated component.

<a name='guidance'></a>

## Guidance

Ensure that each solution component that is deactivated, or disabled, has been done so intentionally.  If so and will no longer be utilized, consider removing it from the solution to prevent confusion for users and system customizers. These components include:

- SDK Message Processing Steps
- Processes
- Record Creation and Update Rules
- SLAs

As well as Entity components such as:

- Forms
- Views
- Business Rules

![Deactivated Processes](../media/deactivated-processes.png)

<a name='seealso'></a>

### See also

[Create custom business logic through processes](/dynamics365/customer-engagement/customize/guide-staff-through-common-tasks-processes)<br />
[Events in forms and grids in Customer Engagement](/dynamics365/customer-engagement/developer/clientapi/events-forms-grids)<br />