---
title: Use solution checker to validate your apps in Power Apps | Microsoft Docs
description: Use the solution checker to validate your solution.
author: Mattp123
manager: kvivek
ms.service: powerapps
ms.component: cds
ms.topic: article
ms.date: 07/09/2019
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Use solution checker to validate your model-driven apps in PowerApps

To deliver on complex business requirements, model-driven app makers often can end up with highly advanced solutions that customize and extend the Common Data Service platform. With advanced implementations comes an increased risk where performance, stability, and reliability issues become introduced, which can negatively impact the user experience. Identifying and understanding how to resolve these issues can be complicated and time consuming. With the solution checker feature, you can perform a rich static analysis check on your solutions against a set of best practice rules and quickly identify these problematic patterns. After the check completes, you receive a detailed report that lists the issues identified, the components and code affected, and links to documentation that describes how to resolve each issue.

The solution checker analyzes these solution components: 
- Common Data Service plug-ins
- Common Data Service custom workflow activities 
- Common Data Service web resources (HTML and JavaScript)
- Common Data Service configurations, such as SDK message steps 

Solution checker works with unmanaged solutions that can be exported from an environment. 

> [!NOTE]
> - This topic explains how to run solution checker from the Power Apps maker portal. A PowerShell module is also available that you can use to interact directly with the service. The Microsoft.PowerApps.Checker.PowerShell module can be used for analysis of managed and unmanaged solutions for supported versions of on-premises and online environments, or to automate and integrate the service into your build and release pipelines. More information: [Microsoft.PowerApps.Checker.PowerShell Overview]( /powershell/powerapps/overview?view=pa-ps-latest#get-started-using-the-microsoftpowerappscheckerpowershell-module) 
> - Solution checker doesn't work with solutions that contain JavaScript using ECMAScript 6 (2015) or later versions. When JavaScript using one of these versions is detected, a JS001 syntax issue for the web resource is reported.

## Enable the solution checker
The Solution checker is enabled by default in every Common Data Service environment. A **Solution checker** menu item is available when you select an unmanaged solution in the **Solutions** area of Power Apps. If the **Run** option is not available in the **Solution checker** menu,  you can enable it by installing the Power Apps checker solution. To install it, follow these steps:   

1. Sign in to [PowerApps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select the Common Data Service environment where you want to enable the solution checker. 
2. On the left navigation pane, select **Solutions**.
3. On the toolbar, select **Solution checker** and then select **Install** – this opens the Microsoft AppSource page. You need to allow pop-up windows if your browser blocks the page from opening. 

   > [!div class="mx-imgBorder"]
   > ![Install solution checker](media/solution-checker-install.png "Install solution checker")

4. Select **Free Trial** on the AppSource page. 

5. If you agree, accept the terms and conditions and select the environment to install the Power Apps checker solution. 
6. When the installation is complete, refresh the **Solution** list on the Power Apps site to verify that the solution checker is available.  
7. To check a solution, [Run the solution checker](#run-the-solution-checker).


<!-- ### Components created with the Power Apps checker
When you install the Power Apps checker these solution specific components are created. 
- Entities: The entities that are created are required to store the results of solution analysis and the status of analysis jobs in your environment.
   - Analysis Component
   - Analysis Job
   - Analysis Result
- System job: A system job is created so admins can remove solution analysis data from the environment. The job contains a configuration value, currently set to remove the solution analysis data after 60 days, which an administrator can override. 
- Security Roles: Two security roles, **Export Customizations**, and **Solution Checker** are created. These roles are required to export the solution for analysis, and storing the analysis results to the entities in your environment.
- User principle: The **Power Apps Advisor** user is created that allows the checker to authenticate with your Common Data Service environment and assign the two security roles, Export Customizations and Solution Checker. The Power Apps Advisor is an application user and does not consume a license.  -->

## Run the solution checker
After you install the Power Apps checker in your environment, a **Solution checker** menu item is available when you select an unmanaged solution in the **Solutions** area of Power Apps. 

1. Sign in to [PowerApps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. In the left pane, select **Solutions**. 
3. Next to the unmanaged solution that you want to analyze, select **...**, point to **Solution checker**, and then select **Run**. 

   > [!div class="mx-imgBorder"]
   > ![Run solution checker command](media/solution-checker-run.png "Run solution checker command")

4.	The status pane located on the upper right of the **Solutions** page displays **Solution checker running**. 

    > [!div class="mx-imgBorder"]
    > ![Solution checker status](media/solution-checker-status.png "Solution checker status")
   
    Note the following:
    - The solution checker can take a few minutes to complete the analysis. 
    
    - During this time you will notice a **Running…** state in the **Solution check** column of the **Solution** list. 
    
    - You'll receive an email notification and a notification in the **Notifications** area of the Power Apps site when the check is completed.  

5.	[View the report](#review-the-solution-checker-report) when the check is completed.

## Cancel a check

After you submit a solutions check in your environment, the check can be canceled through the status pane on the upper right area of the **Solutions** page. 

When you cancel a check, the solution check stops running and the solution check status returns to the previous state. 

## Solution checker states
When you install the solution checker in your environment, the **Solution check** column becomes available in the **Solutions** list. This column displays the solution analysis states for a solution. 

|State  |Description  |
|---------|---------|
|Hasn’t been run    | The solution has never been analyzed.        |
|Running     | The solution is being analyzed.       |
|Couldn’t be completed     |  Solution analysis was requested but the analysis did not complete successfully.       |
|Results as of *date and time*   | Solution analysis completed and results are available for download.      |
|Couldn’t be completed. Result as of *date and time*     | The latest analysis request did not complete successfully. The last successful results can be downloaded.         |
|Checked by Microsoft     | This is a Microsoft-managed solution. Solution analysis is not permitted on these solutions.         |
|Checked by Publisher     | This is a third-party-managed solution. Currently, solution analysis is not available for these solutions.        |


## Review the solution checker report
When a solution check is completed, you can view the analysis report in the portal or you can download the report from your web browser. In the portal, you have options to filter, group results by **Issue**, **Location** or by **Severity** and view detailed information for issues detected in your solution. 

1. In the left pane, select **Solutions**.
2. Next to the unmanaged solution where you want to view the solution checker report, select **...**, point to **Solution checker**, and then select **View results**.  
3. Select an Issue to view the details and guidance on how to resolve.

    > [!div class="mx-imgBorder"] 
    > ![](media/solution-checker-viewresults.png "Solution checker view results")

The solution check results are also available for download. The solution checker zip file is downloaded to the folder specified by your web browser.The download report is in [!INCLUDE [pn-excel-short](../../includes/pn-excel-short.md)] format and contains several visualizations and columns that assist you in identifying the impact, type, and location of each issue detected in your solution. A link to detailed guidance about how to resolve the issue is also provided. 

1. In the left pane, select **Solutions**.
2. Next to the unmanaged solution where you want to download the solution checker report, select **...**, point to **Solution checker**, and then select **Download results**.  
3. The solution checker zip file is downloaded to the folder specified by your web browser.

Here's a summary of each column in the report.

|Report field |Description  |Applies-to component   |
|---------|---------|---------|
|Issue     |   The title of the issue identified in the solution.      | All        |
|Category     | The categorization of the issue identified, such as **Performance**, **Usage**, or **Supportability**.      |  All     |
|Severity     | Represents the potential impact of the issue identified. Available impact types are **High**, **Medium**, **Low**, and **Informational**.         |  All       |
|Guidance     |  Link to article detailing the issue, impact, and recommended action.       |  All       |
|Component     |  The solution component where the issue was identified.        |   All      |
|Location     |  The location and/or source file of the component where the issue that was identified occurred, such as the assembly or JavaScript file name.        |  All       |
|Line  #     |  The line number reference of the issue in the impacted web resource component.       |  Web resources       |
|Module     | Module name where the issue identified in the assembly was detected.     |   Plug-in or custom workflow activity      |
|Type     | Type of the issue identified in the assembly.        | Plug-in or custom workflow activity        |
|Member     |  Member of the issue identified in the assembly.      | Plug-in or custom workflow activity        |
|Statement     | The code statement or configuration that resulted in the issue.        |  All       |
|Comments     | Details about the issue that include high-level resolution steps.         |  All       |


## Best practice rules used by solution checker

|Solution component  |Rule name  |Rule description  |
|---------|---------|---------|
|Plug-in or workflow activity   | [il-specify-column](https://go.microsoft.com/fwlink/?LinkID=398563&error=il-specify-column&client=PAChecker&source=featuredocs)  | Avoid selecting all columns via Common Data Service query APIs.     |
|Plug-in or workflow activity   | [meta-remove-dup-reg](https://go.microsoft.com/fwlink/?LinkID=398563&error=meta-remove-dup-reg&client=PAChecker&source=featuredocs)     | Avoid duplicate Common Data Service plug-in registrations.     |
|Plug-in or workflow activity   | [il-turn-off-keepalive](https://go.microsoft.com/fwlink/?LinkID=398563&error=il-turn-off-keepalive&client=PAChecker&source=featuredocs)   | Set KeepAlive to false when interacting with external hosts in a Common Data Service plug-in.     |
|Plug-in or workflow activity   | [il-avoid-unpub-metadata](https://go.microsoft.com/fwlink/?LinkID=398563&error=il-avoid-unpub-metadata&client=PAChecker&source=featuredocs)   | Avoid retrieving unpublished Common Data Service metadata.     |
|Plug-in or workflow activity   | [il-avoid-batch-plugin](https://go.microsoft.com/fwlink/?LinkID=398563&error=il-avoid-batch-plugin&client=PAChecker&source=featuredocs)   | Avoid using batch request types in Common Data Service plug-ins and workflow activities.    |
|Plug-in or workflow activity   | [meta-avoid-reg-no-attribute](https://go.microsoft.com/fwlink/?LinkID=398563&error=meta-avoid-reg-no-attribute&client=PAChecker&source=featuredocs)  | Include filtering attributes with Common Data Service plug-in registrations.    |
|Plug-in or workflow activity   | [meta-avoid-reg-retrieve](https://go.microsoft.com/fwlink/?LinkID=398563&error=meta-avoid-reg-retrieve&client=PAChecker&source=featuredocs)  | Use caution with Common Data Service plug-ins registered for Retrieve and RetrieveMultiple messages.    |
|Plug-in or workflow activity   | [meta-remove-inactive](https://go.microsoft.com/fwlink/?LinkID=398563&error=meta-remove-inactive&client=PAChecker&source=featuredocs)    | Remove inactive configurations in Common Data Service.    |
|Plug-in or workflow activity   | [il-meta-avoid-crm2011-depr-message](https://go.microsoft.com/fwlink/?LinkID=398563&error=il-avoid-crm2011-depr-message&client=PAChecker&source=featuredocs)  | Don't use Microsoft Dynamics CRM 2011 deprecated messages.     |
|Plug-in or workflow activity   | [meta-avoid-crm4-event](https://go.microsoft.com/fwlink/?LinkID=398563&error=meta-avoid-crm4-event&client=PAChecker&source=featuredocs) | Don't use Microsoft Dynamics CRM 4.0 plug-in registration stage.    |
|Plug-in or workflow activity   | [il-avoid-specialized-update-ops](https://go.microsoft.com/fwlink/?LinkID=398563&error=il-avoid-specialized-update-ops&client=PAChecker&source=featuredocs)  | Don't use specialized update operation requests in Common Data Service.    | 
| Plug-in or workflow activity |  [il-use-autonumber-feature](https://go.microsoft.com/fwlink/?LinkID=398563&error=il-use-autonumber-feature&client=PAChecker)  |Use the auto number feature instead of a custom auto numbering solution. | 
| Plug-in or workflow activity  | [il-avoid-parallel-plugin](https://go.microsoft.com/fwlink/?LinkID=398563&error=il-avoid-parallel-plugin&client=PAChecker)  | The usage of parallel patterns should be avoided within plug-ins.  |
| Plug-in or workflow activity  | [il-avoid-lock-plugin](https://go.microsoft.com/fwlink/?LinkID=398563&error=il-avoid-lock-plugin&client=PAChecker)  | Avoid lock of static members in plug-ins.  |
| Plug-in or workflow activity  | [meta-avoid-retrievemultiple-annotation](https://go.microsoft.com/fwlink/?LinkID=398563&error=meta-avoid-retrievemultiple-annotation&client=PAChecker)  | Avoid registering a plugin on RetrieveMultiple of annotation.  |
|Web Resources  | [web-use-async](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-use-async&client=PAChecker&source=featuredocs)  |  Interact with HTTP and HTTPS resources asynchronously.   |
|Web Resources  | [meta-remove-invalid-form-handler](https://go.microsoft.com/fwlink/?LinkID=398563&error=meta-remove-invalid-form-handler&client=PAChecker&source=featuredocs)  | Correct or remove invalid Common Data Service form event registrations.   |
|Web Resources  | [meta-remove-orphaned-form-element](https://go.microsoft.com/fwlink/?LinkID=398563&error=meta-remove-orphaned-form-element&client=PAChecker&source=featuredocs)  | Correct or remove orphaned Common Data Service form event registrations.   |
|Web Resources  | [web-avoid-modals](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-avoid-modals&client=PAChecker&source=featuredocs)  | Avoid using modal dialogs.   |
|Web Resources  | [web-avoid-crm2011-service-odata](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-avoid-crm2011-service-odata&client=PAChecker&source=featuredocs)   | Don't target the Microsoft Dynamics CRM 2011 OData 2.0 endpoint.     |
|Web Resources  | [web-avoid-crm2011-service-soap](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-avoid-crm2011-service-soap&client=PAChecker&source=featuredocs)  | Don't target the Microsoft Dynamics CRM 2011 SOAP services.   |
|Web Resources  | [web-avoid-browser-specific-api](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-avoid-browser-specific-api&client=PAChecker&source=featuredocs) | Don't use Internet Explorer legacy APIs or browser plug-ins.   |
|Web Resources  | [web-avoid-2011-api](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-avoid-2011-api&client=PAChecker&source=featuredocs)  | Don't use the deprecated Microsoft Dynamics CRM 2011 object model.  |
|Web Resources  | [web-use-relative-uri](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-use-relative-uri&client=PAChecker&source=featuredocs)   | Don't use absolute Common Data Service endpoint URLs.    |
|Web Resources  | [web-use-client-context](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-use-client-context&client=PAChecker&source=featuredocs)  | Use client contexts.   |
|Web Resources  | [web-use-dialog-api-param](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-use-dialog-api-param&client=PAChecker&source=featuredocs)   | Use dialog API parameters.   |
|Web Resources  | [web-use-org-setting](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-use-org-setting&client=PAChecker&source=featuredocs)   | Use organization settings.   |
|Web Resources  | [web-use-grid-api](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-use-grid-api&client=PAChecker&source=featuredocs)   | Use the grid APIs.    |
|Web Resources  | [web-avoid-isActivityType](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-avoid-isActivityType&client=PAChecker&source=featuredocs)   | Replace Xrm.Utility.isActivityType method with new Xrm.Utility.getEntityMetadata and don't use in ribbon rules.    |
|Web Resources  | [meta-avoid-silverlight](https://go.microsoft.com/fwlink/?LinkID=398563&error=meta-avoid-silverlight&client=PAChecker&source=featuredocs)   | Silverlight web resource usage is deprecated.   |
| Web Resources  | [web-remove-debug-script](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-remove-debug-script&client=PAChecker)  | Avoid including debug script in non-development environments.  | 
| Web Resources  | [web-use-strict-mode](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-use-strict-mode&client=PAChecker)  | Use strict mode when possible.  | 
| Web Resources  | [web-use-strict-equality-operators](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-use-strict-equality-operators&client=PAChecker)  | Use strict equality operators.  | 
| Web Resources  | [web-avoid-eval](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-avoid-eval&client=PAChecker)  | Don't use the 'eval' function or its functional equivalents.  | 


### See also
[Best practices and guidance for the Common Data Service](../../developer/common-data-service/best-practices/index.md)<br />
[Best practices and guidance for model-driven apps](../../developer/model-driven-apps/best-practices/index.md)<br />
[Common issues and resolutions for Solution Checker](common-issues-resolutions-solution-checker.md)<br />
