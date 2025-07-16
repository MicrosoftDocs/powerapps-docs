---
title: Add the Copilot control to the rich text editor
description: Learn how to make the Copilot control available in the rich text editor by modifying the editor configuration file.
author: udaykirang
ms.author: udag
ms.reviewer: udag
ms.topic: how-to
ms.date: 04/30/2025
ms.update-cycle: 180-days
ms.subservice: mda-maker
tags:
ms.collection: bap-ai-copilot
search.audienceType:
  - maker
ms.custom:
  - bap-template
  - ai-gen-docs-bap
  - ai-gen-desc
  - ai-seo-date:09/28/2023
---

# Add the Copilot control to the rich text editor

The Copilot control is available in the email form's rich text editor toolbar by default. You can add the Copilot control to the rich text editor in other forms by changing the editor's properties in its advanced configuration file.

## Prerequisites

[Have a configuration file for the rich text editor](rich-text-editor-control.md#customize-the-rich-text-editor-control) in the form where you want to add the Copilot control.

## Add the Copilot control

To add the Copilot control to the rich text editor toolbar in a form, you need to add a value that represents it to the `extraPlugins` and `toolbar` properties in the editor's advanced configuration file.

1. Open the editor's advanced configuration file.
1. Add the following values in the [`defaultSupportedProps` section](rich-text-editor-control.md#rich-text-editor-properties) of the file:

    - In the `extraPlugins` property, add `copilotrefinement`.
    - In the `toolbar` property, add `CopilotRefinement`.

    It should look something like the following example, where "&hellip;" represents values that aren't shown to save space:

    ```text
    "defaultSupportedProps": {
        ...
        "extraPlugins": "computedfont,...,copilotrefinement",
        ...
        "toolbar":[{ "items": ["CopyFormatting", ... ,"CopilotRefinement"]}]
    },
    ```

1. Save the file, and then publish the changes.

### See also

[Use Copilot in the email rich text editor](../model-driven-apps/use-copilot-email-assist.md)
