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

## Running Solution Checker on large solutions fail

Larger solutions, such as the Default Solution, will fail during the export of the solution process for Solution Checker.  Solution Checker has a 10-minute timeout while exporting the solution selected for processing.  Solution Checker will retry three times before it fails to process the job.  It may take over 30-minutes before you receive the failure notification. 

To address this issue, create multiple, smaller, solutions.  To minimize false positives, ensure to add dependant customizations.  When creating a solution and adding these components, include:
- When adding plug-ins, include the SDK Message Processing Steps for the plug-in.
- When adding entity forms, include the JavaScript web resources attached to the form events.  
- When adding JavaScript web resources, include any dependent JavaScript web resources.
- When adding HTML web resources, include any dependent scripts that are defined within the HTML web resource.
- When adding custom workflows, include the assembly used within the workflow.

## Upgrading Solution Checker solution fails

If you have Solution Checker version lower than 1.0.0.45, it is recommended to Delete the solution and Install it again, due to schema changes.  Upgrades tend to fail when solutions have been analyzed and many Analysis Jobs or Analysis Results have been created.

If you want to keep the past results from Solution Checker, export the results from a previous run or export all Solution Checker data using [Export data to Excel](../../user/export-data-excel.md) to export the data from the following entities:

- Analysis Component
- Analysis Job
- Analysis Result
- Analysis Result Detail

### Delete Solution Checker

To delete the Solution Checker solution:

1. As a System Administrator or as a System Customizaer, open up your PowerApps portal by going to https://web.powerapps.com/environments
2. Click on **Solutions**
3. Select **PowerApps Checker** and click on **Delete**

### Add Solution Checker

To add Solution Checker back to your CDS instance:

1. As a System Administrator or as a System Customizaer, open up your PowerApps portal by going to https://web.powerapps.com/environments
2. Click on **Solutions**
3. Click on **Solution Checker** and **Install**

## Solution Checker will not process patched solutions

If a solution has had a patch applied to it, Solution Checker will fail to export the solution for analysis. The development team is actively working on a solution to this issue.  Until the solution has been released, you will need to create a new solution with all the necessary components you'd like to have analyzed.

## HTML web resource violations that contain JavaScript will have a different Line Number 

When HTML web resources are processed within Solution Checker, the HTML web resource is processed separately than the JavaScript within the HTML web resource. Due to this, the line number of the violation found within `<script>` of the HTML web resource will not be the same of the HTML page.

## See also
[Best practices and guidance for the Common Data Service for Apps](../../developer/common-data-service/best-practices/index.md)<br />
[Best practices and guidance for model-driven apps](../../developer/model-driven-apps/best-practices/index.md)<br />