---
title: Use solution checker to validate your apps in PowerApps | Microsoft Docs
description: Tutorial with step-by-step instructions for creating and configuring an entity to use with a PowerApps app.
author: Mattp123
manager: kvivek
ms.service: powerapps
ms.component: cds
ms.topic: article
ms.date: 10/26/2018
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Use solution checker to validate your apps in PowerApps

Solution checker is a Microsoft solution that helps app makers follow best practices when customizing and extending solutions that use the Common Data Service (CDS) for Apps platform. Using best practice rulesets for solution development, solution checker analyzes a solutions’ components within an environment, and generates a report of potential issues or violations. 

The solution checker analyzes these solution components. 
- CDS for Apps plug-ins
- CDS for Apps custom workflow activities 
- CDS for Apps web resources (HTML and JavaScript)
- CDS for Apps configurations, such as SDK message steps 

## Install the solution checker
The solution checker solution can be installed from [Microsoft AppSource](https://appsource.microsoft.com/). It's compatible with PowerApps apps built with CDS for Apps and Dynamics 365 for Customer Engagement, version 9.0 or later versions.

### Components created with the solution checker
When you install the solution checker these solution specific components are created. 
- Entities: The entities that are created are required to store the results of solution analysis and the status of analysis jobs in your environment.
   - Analysis Component
   - Analysis Job
   - Analysis Result
- System job: A system job is created so admins can remove solution analysis data from the environment. The jobs contain a configuration value, currently set to 60 days, which can be overridden by an administrator. 
   - Analysis results cleanup job  
- User Principle: A user is created automatically that allows the solution checker to authenticate with your CDS for Apps environment. The user is required to export the solution for analysis, and the subsequent storing of the analysis results to the solution checker entities in your environment. The solution checker user is an application user and does not consume a license.


## Run the solution checker
After you have installed the solution checker in your environment, the solution checker menu will be made available in the **Solutions** area in the PowerApps portal. 

1. Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. Select **Solutions**, and then select the unmanaged solution that you want to analyze.
3. Select the **Solution checker** menu option. 
    If the **Solution checker** menu option is not available after you select a solution, it means the solution checker has not been installed. To verify, view the solutions in the **Solutions** list. 
4.	Select **Run**. Note the following.
    - The solution checker can take a few minutes to complete the analysis. 
    - During this time you will notice a **Running…** state in the **Solution check** column of the **Solution** list. 
    - You receive an email notification and a notification in the **Notifications** area of the PowerApps site when the check is completed.  
7.	View the report when the check is completed.


## Solution checker states
When you install the solution checker in your environment, the **Solution check** column becomes available in the **Solutions** list. This column displays the solution analysis states for a solution. 

|State  |Description  |
|---------|---------|
|Hasn’t been run    | The solution has never been analyzed.        |
|Running     | The solution is being analyzed.       |
|Couldn’t be completed     |  Solution analysis was requested but the analysis did not complete successfully.       |
|Results as of *date and time*   | Solution analysis completed and results are available for download.      |
| Couldn’t be completed. Result as of *date and time*     | The latest analysis request did not complete successfully. The last successful results can be downloaded.         |
|Checked by Microsoft     | This is Microsoft managed solution. Solution analysis is not permitted on these solutions.         |
|Checked by Publisher     |  This is a third party managed solution. Currently, solution analysis is not available for these solutions.        |


## Reviewing the solution checker report
When a check is completed, the analysis report will be available for download in CSV format. The report contains several columns that assist you in identifying the impact, type, and location of issues in your solution. A link to detailed guidance about how to resolve the issue is also provided. 


|Report field |Description  |Applies to component   |
|---------|---------|---------|
|Issue     |   The title of the issue identified in the solution.      | All        |
|Category     | The categorization of the issue identified, such as **Performance**, **Usage**, or **Supportability**.      |  All       |
|Impact     | Represents the potential impact of the issue identified. Available impact types are **High**, **Medium**, **Low**, **Informational**.         |  All       |
|Component     |  The solution component where the issue was idenitifed.        |   All      |
|Location     |  The location and/or source file of the component where the issue that was identified occured, such as the assembly or JavaScript file name.        |  All       |
|Line  #     |  The line number reference of the issue in the impacted web resource component.       |  Web resources       |
|Scope     |  The global or function container for the issue in the impacted web resource component.       |   Web resources       |
|Module     | Module name where the issue identified in the assembly was detected.     |   Plug-in or custom workflow activity      |
|Type     | Type of the issue idenitifed in the assembly.        | Plug-in or custom workflow activity        |
|Member     |  Member of the issue idenitifed in the assembly.      | Plug-in or custom workflow activity        |
|Statement     | The code statement or configuration which resulted in the issue.        |  All       |
|Issue details     | Details about the issue that include high level resolution steps.         |  All       |
|Guidance     |  Link to article detailing the issue, impact, and recommended resolution. actions.       |  All       |


## Best practice rules used by solution checker

|Column1  |Column2  |
|---------|---------|
|Row1     |         |
|Row2     |         |
|Row3     |         |
|Row4     |         |
|Row5     |         |
|Row6     |         |
|Row7     |         |
|Row8     |         |
|Row9     |         |
|Row10     |         |
|Row11     |         |
|Row12     |         |
|Row13     |         |
|Row14     |         |
|Row15     |         |
|Row16     |         |
|Row17     |         |
|Row18     |         |
|Row19     |         |
|Row20     |         |
|Row21     |         |
|Row22     |         |
|Row23     |         |
|Row24     |         |
|Row25     |         |
|Row26     |         |
|Row27     |         |
|Row28     |         |
|Row29     |         |
|Row30     |         |
|Row31     |         |
|Row32     |         |
|Row33     |         |
|Row34     |         |
|Row35     |         |
|Row36     |         |
|Row37     |         |
|Row38     |         |
|Row39     |         |
|Row40     |         |
|Row41     |         |
|Row42     |         |
|Row43     |         |
|Row44     |         |


## See also
[Guidance and best practices for building PowerApps solutions](https://docs.microsoft.com/dynamics365/customer-engagement/guidance/)
