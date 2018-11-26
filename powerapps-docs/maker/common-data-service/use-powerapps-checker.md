---
title: Use PowerApps checker to validate your apps in PowerApps | Microsoft Docs
description: Use the PowerApps checker to validate your solution.
author: Mattp123
manager: kvivek
ms.service: powerapps
ms.component: cds
ms.topic: article
ms.date: 11/26/2018
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Use PowerApps checker to validate your apps in PowerApps

To deliver on complex business requirements, model-driven app makers can often end up with highly advanced solutions that customize and extend the Common Data Service (CDS) for Apps platform. With advanced implementations comes an increased risk where performance, stability, and reliability issues become introduced, which can negatively impact end-user experience. Identifying and understanding how to resolve these issues can be complicated and time consuming. With the PowerApps checker feature, you can perform a rich static analysis check on your solutions against a set of best practice rules and quickly identify these problematic patterns. After the check completes, you receive a detailed report that lists the issues identified, the components and code affected, and links to documentation that describes how to resolve each issue.

The PowerApps checker analyzes these solution components. 
- CDS for Apps plug-ins
- CDS for Apps custom workflow activities 
- CDS for Apps web resources (HTML and JavaScript)
- CDS for Apps configurations, such as SDK message steps 

PowerApps checker works with unmanaged solutions that can be exported from an environment. PowerApps checker doesn't work with the following solutions. 
- The system default solutions (Default Solution and Common Data Services Default Solution).
- Solutions that contain JavaScript using ECMAScript 6 (2015) or later versions.

> [!NOTE]
> This feature is currently in preview and available only in the North America region. 
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]


## Install the PowerApps checker
The PowerApps checker becomes available in the Solutions area of PowerApps after you install the solution from [Microsoft AppSource](https://appsource.microsoft.com/). It's compatible with PowerApps apps built with CDS for Apps and Dynamics 365 for Customer Engagement, version 9.0 or later versions.

### Components created with the PowerApps checker
When you install the PowerApps checker these solution specific components are created. 
- Entities: The entities that are created are required to store the results of solution analysis and the status of analysis jobs in your environment.
   - Analysis Component
   - Analysis Job
   - Analysis Result
- System job: A system job is created so admins can remove solution analysis data from the environment. The job contains a configuration value, currently set to remove the solution analysis data after 60 days, which an administrator can override. 
- Security Roles: Two security roles, **Export Customizations**, and **Solution Checker** are created. These roles are required to export the solution for analysis, and storing the analysis results to the entities in your environment.
- User principle: The **PowerApps Advisor** user is created that allows the checker to authenticate with your CDS for Apps environment and assign the two security roles, Export Customizations and Solution Checker. The PowerApps Advisor is an application user and does not consume a license.

## Run the PowerApps checker
After you install the PowerApps checker in your environment, a **PowerApps checker** menu item is available when you select an unmanaged solution in the **Solutions** area of PowerApps. 

1. Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. In the left pane select **Solutions**. 
3. Next to the unmanaged solution that you want to anayze, select **...**, point to **PowerApps checker**, and then select **Run**. 

  <!--    ![Run solution checker command](media/run-solution-checker.png) -->

   - If the **PowerApps checker** menu option is not available after you select a solution, it could mean the PowerApps checker has not been installed. To verify, make sure that the **PowerApps Checker** solution is in the **Solutions** list. 

4.	The status pane located in the upper right of the **Solutions** page displays **PowerApps checker running**. Note the following.
    - The PowerApps checker can take a few minutes to complete the analysis. 
    - During this time you will notice a **Running…** state in the **Solution check** column of the **Solution** list. 
    - You receive an email notification and a notification in the **Notifications** area of the PowerApps site when the check is completed.  
7.	[View the report](#reviewing-the-solution-checker-report) when the check is completed.

## Cancel a check

After you submit a PowerApps check in your environment, the check can be cancelled through the status pane in the upper right area of the **Solutions** page. 

When you cancel a check, the solution check stops running and the solution check status returns to the previous state. 

## PowerApps checker states
When you install the PowerApps checker in your environment, the **Solution check** column becomes available in the **Solutions** list. This column displays the solution analysis states for a solution. 

|State  |Description  |
|---------|---------|
|Hasn’t been run    | The solution has never been analyzed.        |
|Running     | The solution is being analyzed.       |
|Couldn’t be completed     |  Solution analysis was requested but the analysis did not complete successfully.       |
|Results as of *date and time*   | Solution analysis completed and results are available for download.      |
| Couldn’t be completed. Result as of *date and time*     | The latest analysis request did not complete successfully. The last successful results can be downloaded.         |
|Checked by Microsoft     | This is Microsoft managed solution. Solution analysis is not permitted on these solutions.         |
|Checked by Publisher     |  This is a third party managed solution. Currently, solution analysis is not available for these solutions.        |


## Review the PowerApps checker report
When a solution check is completed, the analysis report becomes available for download from your web browser. The report is in CSV format and contains several columns that assist you in identifying the impact, type, and location of each issue detected in your solution. A link to detailed guidance about how to resolve the issue is also provided. 

1. In the left pane select **Solutions**.
2. Next to the unmanaged solution where you want to download the PowerApps checker report, select **...**, point to **PowerApps checker**, and then select **Download last results**.  
3. The PowerApps checker zip file is downloaded to the folder specified by your web browser.

Here's a summary of each column in the report.

|Report field |Description  |Applies to component   |
|---------|---------|---------|
|Issue     |   The title of the issue identified in the solution.      | All        |
|Category     | The categorization of the issue identified, such as **Performance**, **Usage**, or **Supportability**.      |  All       |
|Impact     | Represents the potential impact of the issue identified. Available impact types are **High**, **Medium**, **Low**, **Informational**.         |  All       |
|Component     |  The solution component where the issue was idenitifed.        |   All      |
|Location     |  The location and/or source file of the component where the issue that was identified occured, such as the assembly or JavaScript file name.        |  All       |
|Line  #     |  The line number reference of the issue in the impacted web resource component.       |  Web resources       |
|Module     | Module name where the issue identified in the assembly was detected.     |   Plug-in or custom workflow activity      |
|Type     | Type of the issue idenitifed in the assembly.        | Plug-in or custom workflow activity        |
|Member     |  Member of the issue idenitifed in the assembly.      | Plug-in or custom workflow activity        |
|Statement     | The code statement or configuration which resulted in the issue.        |  All       |
|Issue details     | Details about the issue that include high level resolution steps.         |  All       |
|Guidance     |  Link to article detailing the issue, impact, and recommended resolution. actions.       |  All       |


## Best practice rules used by PowerApps checker


|Solution component  |Rule name  |Rule Description  |
|---------|---------|---------|
|Plug-in or workflow activity   | [il-specify-column](http://go.microsoft.com/fwlink/?LinkID=398563&error=il-specify-column&client=PAChecker&source=featuredocs)  | Avoid selecting all columns via Dynamics 365 for Customer Engagement query APIs.     |
|Plug-in or workflow activity   | [meta-remove-dup-reg](http://go.microsoft.com/fwlink/?LinkID=398563&error=meta-remove-dup-reg&client=PAChecker&source=featuredocs)     | Avoid duplicate Dynamics 365 for Customer Engagement plug-in registrations.     |
|Plug-in or workflow activity   |         |         |
|Plug-in or workflow activity   |         |         |
|Plug-in or workflow activity   |         |         |
|Plug-in or workflow activity   |         |         |
|Plug-in or workflow activity   |         |         |
|Plug-in or workflow activity   |         |         |
|Plug-in or workflow activity   |         |         |
|Plug-in or workflow activity   |         |         |
|Plug-in or workflow activity   |         |         |
|Plug-in or workflow activity   |         |         |
|Row13     |         |         |
|Row14     |         |         |
|Row15     |         |         |
|Row16     |         |         |
|Row17     |         |         |
|Row18     |         |         |
|Row19     |         |         |
|Row20     |         |         |
|Row21     |         |         |
|Row22     |         |         |
|Row23     |         |         |
|Row24     |         |         |
|Row25     |         |         |
|Row26     |         |         |
|Row27     |         |         |
|Row28     |         |         |



## See also
[Understand experimental and preview features in PowerApps](../canvas-apps/working-with-experimental.md) <br/>
[Guidance and best practices for building PowerApps solutions](https://docs.microsoft.com/dynamics365/customer-engagement/guidance/)
