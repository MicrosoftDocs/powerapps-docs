---
title: "Diagnose solutions | MicrosoftDocs"
description: "Use tools to run analysis of potential issues with solutions and solution objects."
author: caburk
ms.author: caburk
ms.reviewer: matp
manager: kvivek
ms.date: 07/08/2021
ms.service: powerapps
ms.topic: overview
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Tools available to diagnose solutions

There are two tools available for diagnosing solutions in Power Apps.
- [Object checker](#object-checker)
- [Solution checker](#solution-checker)

## Object checker

Object checker and solution checker are similar and share much of the same infrastructure. However, object checker runs *live diagnostics on the database* and can analyze issues based on the metadata and layering of a given solution object - regardless of which solution(s) the object is in. Therefore, object checker is better suited for troubleshooting application lifecycle (ALM) related issues in test and production environments. More information: [Use object checker to diagnose a solution component](object-checker.md)

## Solution checker

Solution checker runs offline analysis on a single solution file. Solution checker requires the solution be exported before you can run a solution diagnostic. Solution checker is best suited for development environments or analyzing a solution prior to committing it to a source control repository. More information: [Use solution checker to validate your model-driven apps in Power Apps](use-powerapps-checker.md)

### See also
[Debug a model-driven app with Monitor](../monitor-modelapps.md)