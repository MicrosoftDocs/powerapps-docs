---
title: "Build tools tasks| Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "PowerApps build tools are a collection of PowerApps specific Azure DevOps build tasks that eliminate the need to manually download  tools and scripts to manage the application lifecycle of PowerApps. This topic describes the tasks that are available. " # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/21/2019
ms.reviewer: "Dean-Haas"
ms.service: powerapps
ms.topic: "article"
author: "mikkelsen2000" # GitHub ID
ms.author: "pemikkel" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Build tools tasks

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Several types of build tasks are available as part of the PowerApps build tools to help automate your application lifecycle, using Azure DevOps.
  
## Helper task

The PowerApps tools installer is required to be the first task in any build and release pipeline. This task installs a set of PowerApps specific tools required by the agent to run the PowerApps build tasks. This task does not require any additional configuration.

## Quality check

The PowerApps checker task runs a static analysis check on your solution(s) against a set of best-practice rules to identify any problematic patterns that you might inadvertently have introduced when building your solution.

| **Parameters** | **Description** |
| --- | --- |
| PowerApps checker service  |   Select the service endpoint for PowerApps checker. The service   endpoint is defined under **Service Connections** in **Project Settings**.  **NOTE:** The service connection type that must be used for this specific task only is ‘PowerApps Checker,’ which is a service principals connection. More information on how to configure Service Principals before you can use the  task is available [here](https://aka.ms/buildtoolsconnection).  |
| Location of file to analyze  | Specify whether to reference a local file or a reference file from a Sas url. 
| Local files to analyze/Sas uri for file to analyze |  Specify the path and file name of the zip files to analyze.   Wildcards can be used. For example, **\*.zip   for all zip files in all sub folders. You can choose to specify the files   directly or reference a File from a Sas uri.   |
|  Rule set |   Specify which ruleset to apply. The following two rulesets are available:  **Solution Checker:** This is the same ruleset that is run from the [Maker Portal](https://make.powerapps.com/).    **AppSource:** This is the extended ruleset that is used to certify an application before it can be published to [AppSource](https://appsource.microsoft.com/en-US/).   |

## Solution tasks

This set of tasks perform actions against solutions, and includes the following tasks:

### PowerApps import solution

The import solution imports a solution into a target environment.

| **Parameters** | **Description** |
|----|----|
| PowerApps environment URL  | The service endpoint for the target environment that you want to import the solution to. For example, *https://powerappsbuildtools.crm.dynamics.com*.  Service endpoints can be defined under **Service Connections** in **Project Settings**. |
| Solution input file  | The path and file name of the solution.zip file to import into the target environment. For example: *$(Build.ArtifactStagingDirectory)\$(SolutionName).zip*.
 |
> [!NOTE] 
> Variables give you a convenient way to get key bits of data into various parts of your pipeline. A comprehensive list of predefined variables is available [here](https://docs.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml).

### PowerApps export solution

The export solution task exports a solution from a source environment.

| **Parameters** | **Description** |
|----------|-------------|
| PowerApps environment URL | The service endpoint for the source environment that you want to export the solution from.  Defined under **Service Connections -> Generic Service Connection** in **Project Settings**. |
| Solution name | The name of the solution to export. Always use the solution ‘Name’. Not the ‘Display Name’. |
| Solution output file | The path and file name of the solution.zip file to export the source environment to. For example: *$(Build.ArtifactStagingDirectory)\$(SolutionName).zip*. |

> [!NOTE] 
> Variables give you a convenient way to get key bits of data into various parts of your pipeline. A comprehensive list of predefined variables is available here.
 
### PowerApps unpack solution

The unpack solution task takes a compressed solution file and decomposes it into multiple XML files and other files so that these files can be more easily managed by a source control system.

| **Parameters** | **Description** |
|------------|---------|
| Solution input file | The path and file name of the solution.zip file to unpack. |
| Target folder to unpack solution | The path and target folder you want to unpack the solution into. |
| Type of solution | The type of solution you want to unpack:  **Unmanaged** (recommended): *Only the unmanaged solution should be unpacked to your repo*, **Managed**, **Both** |


### PowerApps pack solution

Packs a solution represented in source control into a solution.zip file that can be imported into an environment.

| **Parameters** | **Description** |
|------------|---------|
| Solution output file | The path and file name of the solution.zip file to pack the solution into. |
| Source folder of solution to pack | The path and source folder of the solution  to pack. |
| Type of solution | The type of solution you want to pack:  **Unmanaged** (recommended):, **Managed**, **Both** |

### Publish customizations

The publish customizations task publishes all customizations in an environment.

| **Parameters** | **Description** |
|------------|---------|
| PowerApps environment URL | The service endpoint for the environment in which you want to publish customizations.  Defined under **Service Connections** in **Project Settings**. |

### PowerApps set solution version 

The set solution version task updates the version of a solution.

| **Parameters** | **Description** |
|---------------------------|----|
| PowerApps environment URL  | The service endpoint for the environment where you want to deploy the package.  Defined under **Service Connections** in **Project Settings**. |
| Solution name  | The name of the solution you want to set the Version Number for |
| Solution Version Number | Version number to set, using format `major.minor.build.revision` e.g. **1.0.0.1** |

### PowerApps deploy package

The deploy package task deploys a package to an environment. Deploying a package as opposed to a single solution file provides an option to deploy multiple solutions, data, and code into an environment.

| **Parameters** | **Description** |
|---------------------------|----|
| PowerApps environment URL  | The service endpoint for the target environment that holds the solution you want to update.  Defined under **Service Connections** in **Project Settings**. |

## Environment management tasks

Environment management tasks are used to automate common environment management functions, and includes the following tasks:

### PowerApps create environment

The create environment task creates an environment.

> [!NOTE]
> A new environment can only be provisioned if your license or capacity allows for the creation of additional environments.

| **Parameters** | **Description** |
|---------|-----------|
| Deployment Region | The Region that the environment should be deployed into. |
| Instance Type | The type of instance to deploy. Options are Sandbox or Production. |
| Base Language | The base language in the environment. |
| Domain Name | This is the environment specific string that forms part of the URL. For example, for an environment with the following URL: *https://powerappsbuildtasks.crm.dynamics.com*, the domain name would be ‘powerappsbuildtasks’.  NOTE: If you are entering a domain name that is already in use – the task will append a numeric value to the URL, starting with 0. For the example above, the URL could become *https://powerappsbuildtasks0.crm.dynamics.com*. |
| Friendly name | The friendly name of the environment. |

### PowerApps delete environment

The delete environment task deletes an environment.

| **Parameters** | **Description** |
|---------|-----------|
| PowerApps environment URL  | The service endpoint for the environment you want to delete.  Defined under **Service Connections** in **Project Settings**. |

### PowerApps backup environment

The backup environment task backs up an environment. 

| **Parameters** | **Description** |
|---------|-----------|
| PowerApps environment URL  | The service endpoint for the environment you want to backup.  Defined under **Service Connections** in **Project Settings**. |
| Backup label  | The label you want to assign to the  backup.  |

### PowerApps copy environment

The copy environment task copies an environment to a target environment. Two types of copy are available: full and minimal. Full copies both data and solution metadata (customizations), whereas minimal only copies solution metadata but not the actual data.

> [!NOTE]
> This task is only available for D365 CE environments.  

| **Parameters** | **Description** |
|---------|-----------|
| PowerApps source environment URL  | The service endpoint for the environment you want to copy from.  Defined under **Service Connections** in **Project Settings**. |
| PowerApps target environment URL  | The service endpoint for the environment you want to copy to.  Defined under **Service Connections** in **Project Settings**. |
