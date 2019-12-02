---
title: "Optimize custom assembly development | MicrosoftDocs"
description: "Consider merging separate plug-ins/custom workflow activities into a single custom assembly to improve performance and maintainability and move plug-ins/custom workflow activities into multiple custom assemblies if an assembly size is near the sandbox assembly size constraints."
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
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Optimize assembly development

**Category**: Performance, Maintainability, Design

**Impact potential**: Low

<a name='symptoms'></a>

## Symptoms

When developing custom assemblies, there are a couple of considerations to take in:

1. Multiple different custom assemblies
    - Increased maintainability complexity
    - Potential increase plug-in execution length

2. Sandbox assembly size constraint is 16 MB in Common Data Service.

<a name='guidance'></a>

## Guidance

> [!NOTE]
> Further Guidance clarification is under development regarding specific details in optimizing assembly development, such as, how to merge separate plug-ins into a single custom assembly and suggestions to minimize the assembly size.

### Consolidate Plug-ins or Custom Workflow Activities into a Single Assembly

Plug-ins and custom workflow activities developed for a Common Data Service solution should exist with others in a single Visual Studio project. Consider merging separate plug-ins/custom workflow activities into a single Visual Studio project/assembly unless the plug-ins fall into the following exceptions:

1. A plug-in/custom workflow activity needs to be selectively deployed to one environment but not to others.

2. The physical assembly size is near or greater than 16 MB for a Common Data Service instance.


### Move Plug-ins/Custom Workflow Activities into Multiple Assemblies

Power Apps and Dynamics 365 (online) has an assembly size constraint of 16 MB which cannot be changed. If your assembly size is nearing 16 MB, consider moving plug-in/custom workflow activities into multiple assemblies.

<a name='problem'></a>

## Problematic patterns

### Multiple assemblies
Having multiple assemblies has a couple of areas that can be impacted:

1. Performance - each assembly has a lifecycle that is managed by Common Data Service.  This includes loading, caching, and unloading the assemblies.  Having more than one assembly causes more work to be done on the server, loading and caching an assembly, and could affect the overall plug-in/custom workflow activity execution length.

2. Maintainability - having more than one plug-in/custom workflow activity Visual Studio project leads to more complex application lifecycle management (ALM). It increases the risk and the amount of time when updating/patching the appropriate project for a specific plug-in/custom workflow activity, packaging the plug-ins/custom workflow activities within a solution, and managing plug-ins/custom workflow activities within a deployment.

### Assembly larger than 16 MB
You will not be able to register a custom assembly within Common Data Service that is larger than 16 MB.

<a name='additional'></a>

## Additional information

Quite often, developers create a new Visual Studio project for each plug-in/custom workflow activity.  In turn, this causes a separate assembly to be generated for each plug-in/custom workflow activity.

<a name='seealso'></a>

### See also

[Event Framework](../../event-framework.md)<br />
[Use plug-ins to extend business processes](../../plug-ins.md)<br />
