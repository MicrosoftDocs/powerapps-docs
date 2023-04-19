---
title: "Use object checker in solutions | MicrosoftDocs"
description: "Use object checker to run live analysis of potential issues with objects in your solution."
Keywords: object checker, checker, solution checker, solution issue
author: caburk
ms.author: caburk
ms.reviewer: matp
ms.date: 03/09/2023
ms.topic: how-to
search.audienceType: 
  - maker
---
# Use object checker to diagnose a solution component (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Object checker runs real-time diagnostics on component objects within your solution. If issues are detected, a recommendation is returned that describes how to fix the issue. This might include documentation, instructions, or a click-able action that can fix the issue for you.

## Example issues object checker detects

- Active layer hiding customizations.
- Malformed or corrupted metadata.

## Run object checker and view the results

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Solutions** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open a solution that contains the problematic object. You can run object checker within either managed and unmanaged solutions.
1. Select a single object, such as a model-driven app or a site map.
1. On the command bar, select **...** > **Object checker** > **Run**.
   :::image type="content" source="media/object-checker-run.png" alt-text="Run object checker":::

1. When object checker finishes, on the command bar, select **...** > **Object checker** > **View results**
   :::image type="content" source="media/object-checker-view-results.png" alt-text="View object checker results":::

1. The results are displayed in the right pane. If issues are detected, follow the prompt to resolve the issue.
1. Select **Close** to close the object checker results pane.

## Current limitations

Object checker currently only works with model-driven app and site map components.

### See also

[Tools available to diagnose solutions](diagnose-solutions.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
