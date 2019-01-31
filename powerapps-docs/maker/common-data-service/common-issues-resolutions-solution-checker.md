---
title: "Common issues and resolutions for Solution Checker | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: " A list of common issues and resolutions within Solution Checker"
keywords: ""
ms.date: 01/28/2019
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: caa4e3f2-9700-49b8-87ed-8a68e8878b02
author: jowells1 # GitHub ID
ms.author: jowells # MSFT alias of Microsoft employees only
manager: austinj # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Common issues and resolutions for Solution Checker

This article lists some common issues that you might encounter while using Solution Checker. Where applicable, workarounds are provided.

<!-- Using this article as the template: https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/common-issues-and-resolutions -->

## Checks fail due to PowerApps Checker version installed
Solution Checker is a component of the PowerApps Checker solution.  If you have a PowerApps Checker version lower than 1.0.0.47, solution checks will fail to complete successfully. You should upgrade your PowerApps Checker version from the Dynamics 365 Administration portal. 

However, if you have a PowerApps Checker version lower than 1.0.0.45 installed, it is recommended to delete the solution and install it again. Due to recent schema changes, upgrade of PowerApps Checker from versions lower than 1.0.0.45 may fail.

If you want to keep the past results from Solution Checker, export the results from a previous run or export all Solution Checker data using [Export data to Excel](../../user/export-data-excel.md) to export the data from the following entities:

- Analysis Component
- Analysis Job
- Analysis Result
- Analysis Result Detail

### Delete PowerApps Checker

To delete the PowerApps Checker solution:

1. As a System Administrator or as a System Customizer, open up your PowerApps portal by going to https://web.powerapps.com/environments
2. Click on **Solutions**
3. Select **PowerApps Checker** and click on **Delete**

### Add PowerApps Checker

To add PowerApps Checker back to your CDS instance:

1. As a System Administrator or as a System Customizer, open up your PowerApps portal by going to https://web.powerapps.com/environments
2. Click on **Solutions**
3. Click on **Solution Checker** and **Install**

## Checks on large solutions fail

Solution Checker has a 10-minute timeout for exporting a solution from the Common Data Service (CDS) for Apps environment. Large solutions, like the Default Solution, may fail to get exported within this time, and the check will not complete successfully. Solution Checker will retry three times before it fails to process the job, so it may take over 30-minutes before you receive a failure notification.
To address this issue, check or create smaller solutions to be analysed. To minimize false positives, ensure to add dependant customizations. When creating a solution and adding these components, include:

- When adding plug-ins, include the SDK Message Processing Steps for the plug-in.
- When adding entity forms, include the JavaScript web resources attached to the form events.  
- When adding JavaScript web resources, include any dependent JavaScript web resources.
- When adding HTML web resources, include any dependent scripts that are defined within the HTML web resource.
- When adding custom workflows, include the assembly used within the workflow.

## Solution Checker will not process patched solutions

If a solution has had a [patch](https://docs.microsoft.com/powerapps/developer/common-data-service/create-patches-simplify-solution-updates) applied, Solution Checker will fail to export the solution for analysis. When a solution has had a patch applied, the original solution becomes locked and it can’t be changed or exported, as long as there are dependent patches that exist in the organization that identify the solution as the parent solution.

To address this issue, all patches to that solution could be merged into a new version of the solution. This unlocks the solution and allows the solution to be exported from the system. 

## Line number references for issues in HTML resources with embedded JavaScript are not correct 

When HTML web resources are processed within Solution Checker, the HTML web resource is processed separately than the JavaScript within the HTML web resource. Due to this, the line number of the violation found within `<script>` of the HTML web resource will not be correct.

## JS1001 syntax issue for web resources

ECMAScript 6 (2015) or later versions are not currently supported. When Solution Checker analyzes JavaScript using ECMAScript 6 or later, a JS1001 syntax issue for the web resource is reported.  

## See also
[Best practices and guidance for the Common Data Service for Apps](../../developer/common-data-service/best-practices/index.md)<br />
[Best practices and guidance for model-driven apps](../../developer/model-driven-apps/best-practices/index.md)<br />
