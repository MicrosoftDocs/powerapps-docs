---
title: "Use object checker in solutions | MicrosoftDocs"
description: "Use object checker to run live analysis of potential issues with objects in your solution."
Keywords: object checker, checker, solution checker, solution issue
author: caburk
ms.author: caburk
ms.reviewer: matp
manager: kvivek
ms.date: 07/08/2021
ms.service: powerapps
ms.topic: conceptual
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Use object checker to diagnose a solution component

Object checker runs real-time diagnostics on component objects within your solution. If issues are detected, a recommendation is returned that describes how to fix the issue. This might include documentation, instructions, or a click-able action that can fix the issue for you.

## Difference between object checker and solution checker

Object checker and solution checker are similar and share much of the same infrastructure. However, object checker runs *live diagnostics on the database* and can analyze issues based on the metadata and layering of a given solution object - regardless of which solution(s) the object is in. Therefore, object checker is better suited for troubleshooting application lifecycle (ALM) related issues in test and production environments.

Solution checker runs offline analysis on a single solution file and requires the solution to be exported. Solution checker is better suited for development environments or analyzing a solution prior to committing it to a source control repository.

## Example issues object checker detects

- Active layer hiding customizations.
- Malformed or corrupted metadata.

## Use object checker

1. Open a solution that contains the problematic object. You may run object checker within either managed and unmanaged solutions.
1. Select a single object, such as a model-driven app or a site map.
1. On the command bar, select **...** > **Object checker** > **Run**.
   :::image type="content" source="media/object-checker-run.png" alt-text="Run object checker":::

1. On the command bar, select **...** > **Object checker** > **View results**
   :::image type="content" source="media/object-checker-view-results.png" alt-text="View object checker results":::

1. The results are displayed in the right pane. If issues are detected, follow the prompt to resolve the issue.

## Current limitations

Object checker is currently only supported for model-driven apps and site map components. <!-- This is a framework that will grow to support other object types and additional rules over time. -->


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
