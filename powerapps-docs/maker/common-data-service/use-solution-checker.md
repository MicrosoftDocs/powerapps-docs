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

Solution checker is a Microsoft solution that helps app makers follow best practices when customizing and extending solutions that use the Common Data Service (CDS) for Apps platform. Using best practice rulesets for solution development, solution checker analyzes a solutions’ components within an environment and generates a report of potential issues or violations. 

The solution checker analyzes these solution components. 
- CDS for Apps plug-ins
- CDS for Apps custom workflow activities 
- CDS for Apps web resources (HTML and JavaScript)
- CDS for Apps configurations, such as SDK message steps 

> [!NOTE]
> Solution checker works with unmanaged solutions. 

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
- User principle: A user is created automatically that allows the solution checker to authenticate with your CDS for Apps environment. The user is required to export the solution for analysis, and the subsequent storing of the analysis results to the solution checker entities in your environment. The solution checker user is an application user and does not consume a license.


## Run the solution checker
After you have installed the solution checker in your environment, the solution checker menu will be made available in the **Solutions** area of PowerApps. 

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
When a check is completed, the analysis report will be available for download from your web browser. The report is in CSV format and contains several columns that assist you in identifying the impact, type, and location of each issue detected in your solution. A link to detailed guidance about how to resolve the issue is also provided. 


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

|Solution component  |Rule description |
|---------|---------|
|Plug-in or workflow activity     | Avoid selecting all columns via Dynamics 365 for Customer Engagement query APIs.        |
|Plug-in or workflow activity     | Improve Microsoft Dynamics 365 for Customer Engagement service channel allocation performance.       |
|Plug-in or workflow activity     | Set KeepAlive to false when interacting with external hosts in a Dynamics 365 for Customer Engagement plug-in.        |
|Plug-in or workflow activity     | Avoid retrieving unpublished Dynamics 365 for Customer Engagement metadata.        |
|Plug-in or workflow activity     | Avoid using batch request types in Dynamics 365 Customer Engagement plug-ins and workflow activities.       |
|Plug-in or workflow activity     | Use InvalidPluginExecutionException in Dynamics 365 for Customer Engagement plug-ins and workflow activities.        |
|Plug-in or workflow activity     | Use ITracingService in Dynamics 365 for Customer Engagement plug-ins.        |
|Plug-in or workflow activity     | Don't implement Microsoft Dynamics CRM 4.0 plug-ins.        |
|Plug-in or workflow activity     | Don't implement Microsoft Dynamics CRM 4.0 workflow activities.        |
|Plug-in or workflow activity     | Don't reference Microsoft Dynamics CRM 4.0 SDK assemblies.        |
|Plug-in or workflow activity     | Don't target .NET CLR version 2.0.50727.        |
|Plug-in or workflow activity     | Don't use Microsoft Dynamics CRM 2011 deprecated messages.       |
|Plug-in or workflow activity     | Don't use specialized update operation requests in Dynamics 365 for Customer Engagement.       |
|SDK message step     | Configuration issue. Avoid duplicate Dynamics 365 for Customer Engagement plug-in registrations.        |
|SDK message step     | Configuration issue. Correct or remove invalid Dynamics 365 for Customer Engagement form event registrations.        |
|SDK message step     | Configuration issue. Include filtering attributes with Dynamics 365 for Customer Engagement plugin registrations.       |
|SDK message step     | Configuration issue. Use caution with Dynamics 365 for Customer Engagement plug-ins registered for Retrieve and RetrieveMultiple messages.     |
|SDK message step     | Configuration issue. Remove inactive configurations in Dynamics 365 for Customer Engagement.        |
|SDK message step     | Configuration issue. Correct or remove orphaned Dynamics 365 for Customer Engagement form event registrations.        |
|SDK message step     | Don't use Microsoft Dynamics CRM 4.0 plug-in registration stage.        |
|Web Resources     | JavaScript issue. Don't directly access the HTML Document Object Model (DOM) of Dynamics 365 for Customer Engagement application pages and entity forms.       |
|Web Resources     | JavaScript issue. Don't directly handle HTML Document Object Model (DOM) events for Dynamics 365 Customer Engagement application pages and entity forms.      |
|Web Resources     | JavaScript issue. Don't use unpublished object model members or components of Dynamics 365 for Customer Engagement        |
|Web Resources     | JavaScript issue. Avoid using modal dialogs.        |
|Web Resources     | JavaScript issue. Don't assume that the parent window is the Dynamics 365 for Customer Engagement form.       |
|Web Resources     | JavaScript issue. Don't target the Microsoft Dynamics CRM 2011 OData 2.0 endpoint.      |
|Web Resources     | JavaScript issue. Don't target the Microsoft Dynamics CRM 2011 SOAP services.     |
|Web Resources     | JavaScript issue. Don't target the Microsoft Dynamics CRM 4.0 web services        |
|Web Resources     | JavaScript issue. Don't use Internet Explorer legacy APIs or browser plug-ins.        |
|Web Resources     | JavaScript issue. Don't use the deprecated Microsoft Dynamics CRM 2011 object model.       |
|Web Resources     | JavaScript issue. Don't use the deprecated Microsoft Dynamics CRM 4.0 object model.        |
|Web Resources     | HTML issue. Dynamics 365 for Customer Engagement web resource URL is invalid.      |
|Web Resources     | JavaScript issue. Do not use absolute Dynamics 365 for Customer Engagement endpoint URLs.        |
|Web Resources     | JavaScript issue. Dynamics 365 for Customer Engagement web resource URL is invalid.        |
|Web Resources     | JavaScript issue. Prefer Xrm.Utility dialogs in Dynamics 365 for Customer Engagement form and ribbon commands.       |
|Web Resources     | Interact with HTTP and HTTPS resources asynchronously.        |
|Web Resources     | Avoid using window.top.        |
|Web Resources     | Use client contexts.        |
|Web Resources     | Use dialog API parameters.       |
|Web Resources     | Use organization settings.        |
|Web Resources     | Use the grid APIs.        |
|Web Resources     | Replace Xrm.Utility.isActivityType method with new Xrm.Utility.getEntityMetadata, and do not use in ribbon rules.        |
|Web Resources     | Silverlight web resource usage is deprecated.        |


## See also
[Guidance and best practices for building PowerApps solutions](https://docs.microsoft.com/dynamics365/customer-engagement/guidance/)
