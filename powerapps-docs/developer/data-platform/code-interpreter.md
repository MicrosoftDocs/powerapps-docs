---
title: "Code interpreter for developers"
description: "Learn how developers can use code interpreter enabled prompts."
ms.date: 09/11/2025
ms.reviewer: jdaly
ms.topic: article
author: rapraj
ms.author: rapraj
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - ColinBe
---
# Code interpreter for developers

As described in [Use code interpreter to generate and execute Python code](/microsoft-copilot-studio/code-interpreter-for-prompts), code interpreter provides a way for agents to execute python code for data analysis, Word, Excel, PowerPoint, and PDF processing, and visualizations. Refer to that article to understand:

- Licensing requirements and supported regions
- General code interpreter capabilities
- How to enable code interpreter for a prompt
- How to use code interpreter capabilities with a prompt

This article describes how developers can use the Dataverse `Predict` message to pass parameters to code interpreter enabled prompts and process the responses.  

> [!NOTE]
> A common scenario for this code interpreter enabled prompts is to generate UI experiences for model-driven applications using PCF components. Refer to the [Code interpreter PCF component sample](code-interpreter-pcf-sample.md) for an example.

## Enable code interpreter for the environment

Code interpreter must be enabled for each environment before you can use it. The default setting is **Off**. [Learn how to enable code interpreter using the Power Platform Admin center](/microsoft-copilot-studio/code-interpreter-for-prompts#administration-of-code-interpreter)

Developers can use the Power Platform [Environment Management Settings](/rest/api/power-platform/environmentmanagement/environment-management-settings) APIs to read or set the `CopilotStudio_CodeInterpreter` boolean property to enable code interpreter for an environment.

## Code interpreter enabled prompts
