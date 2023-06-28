---
title: Use solution checker to validate your solutions | Microsoft Docs
description: Use the solution checker to validate your solution.
author: Mattp123
ms.component: cds
ms.topic: article
ms.date: 05/16/2023
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# Use solution checker to validate your solutions

To deliver on complex business requirements, makers often can end up with highly advanced solutions that customize and extend the Microsoft Dataverse platform. With advanced implementations come an increased risk where performance, stability, and reliability issues become introduced, which can negatively impact the user experience. Identifying and understanding how to resolve these issues can be complicated and time consuming. With the solution checker feature, you can perform a rich static analysis check on your solutions against a set of best practice rules and quickly identify these problematic patterns. After the check completes, you receive a detailed report that lists the issues identified, the components and code affected, and links to documentation that describes how to resolve each issue.

The solution checker analyzes these solution components: 
- Dataverse custom workflow activities 
- Dataverse web resources (HTML and JavaScript)
- Dataverse configurations, such as SDK message steps
- Power Automate flows (via [flow checker](/power-automate/error-checker))
- Power Fx expressions (via [app checker](https://powerapps.microsoft.com/en-us/blog/new-app-checker-helps-you-fix-errors-and-make-accessible-apps/))

Solution checker works with unmanaged solutions that can be exported from an environment. 

> [!NOTE]
> - This topic explains how to run solution checker from the Power Apps maker portal. A PowerShell module is also available that you can use to interact directly with the service. The Microsoft.PowerApps.Checker.PowerShell module can be used for analysis of unmanaged solutions for Power Apps environments, or to automate and integrate the service into your build and release pipelines. More information: [Microsoft.PowerApps.Checker.PowerShell Overview]( /powershell/powerapps/get-started-powerapps-checker?view=pa-ps-latest&preserve-view=true) 
> - Solution checker supports global variables for ECMAScript 2015 (ES6) and up to ECMAScript 2018 (ES9) syntax. When JavaScript is detected using global variables later than ES6 or syntax later than ES9, a web-unsupported-syntax issue for the web resource is reported.
> - Use of solution checker does not guarantee that a solution import will be successful. The static analysis checks performed against the solution do not know the configured state of the destination environment and import success may be dependent on other solutions or configurations in the environment. 

## Run the solution checker

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2. In the left pane, select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
3. Next to the unmanaged solution that you want to analyze, select **...**, point to **Solution checker**, and then select **Run**. 

   > [!div class="mx-imgBorder"]
   > ![Run solution checker command.](media/solution-checker-run.png "Run solution checker command")

4.	The **Solution checker** command button has a loading indicator, and you'll notice a **Running…** state in the **Solution check** column of the **Solution** list. 

    > [!div class="mx-imgBorder"]
    > ![Solution checker status.](media/solution-checker-status.png "Solution checker status")
   
    Note the following:
    - The solution checker can take a few minutes to complete the analysis. 
    
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
|Couldn’t be completed     |  Solution analysis was requested but the analysis didn't complete successfully.       |
|Results as of *date and time*   | Solution analysis completed and results are available for download.      |
|Couldn’t be completed. Result as of *date and time*     | The latest analysis request didn't complete successfully. The last successful results can be downloaded.         |
|Checked by Microsoft     | This is a Microsoft-managed solution. Solution analysis isn't permitted on these solutions.         |
|Checked by Publisher     | This is a third-party-managed solution. Currently, solution analysis isn't available for these solutions.        |


## Review the solution checker report

When a solution check is completed, you can view the analysis report in the portal, or you can download the report from your web browser. In the portal, you have options to sort results by **Issue**, **Location** or by **Severity** and view detailed information for issues detected in your solution. 

1. In the left pane, select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
2. Next to the unmanaged solution where you want to view the solution checker report, select **...**, point to **Solution checker**, and then select **View results**.  
3. Select an issue to view the details and guidance on how to resolve.

    > [!div class="mx-imgBorder"] 
    > ![Solution checker view results.](media/solution-checker-viewresults.png "Solution checker view results")

The solution check results are also available for download. The solution checker zip file is downloaded to the folder specified by your web browser. The download report is in [!INCLUDE [pn-excel-short](../../includes/pn-excel-short.md)] format and contains several visualizations and columns that assist you in identifying the impact, type, and location of each issue detected in your solution. A link to detailed guidance about how to resolve the issue is also provided. 

1. In the left pane, select **Solutions**. [!INCLUDE [cc_navigate-solution-from-powerapps-portal](../../includes/left-navigation-pane.md)]
2. Next to the unmanaged solution where you want to download the solution checker report, select **...**, point to **Solution checker**, and then select **Download results**.  
3. The solution checker zip file is downloaded to the folder specified by your web browser.

Here's a summary of each column in the report.

|Report column |Description  |Applies-to component   |
|---------|---------|---------|
|Issue     |   The title of the issue identified in the solution.      | All        |
|Category     | The categorization of the issue identified, such as **Performance**, **Maintainability**, **Usage**, **Supportability**, **Design**, **Security**, **Accessibility**, or **Upgrade readiness**.      |  All     |
|Severity     | Represents the potential impact of the issue identified. Available impact types are **Critical**, **High**, **Medium**, **Low**, and **Informational**.         |  All       |
|Guidance     |  Link to article detailing the issue, impact, and recommended action.       |  All       |
|Component     |  The solution component where the issue was identified.        |   All      |
|Location     |  The location and/or source file of the component where the issue that was identified occurred, such as the assembly or JavaScript file name.        |  All       |
|Line  #     |  The line number reference of the issue in the impacted web resource component.       |  Web resources       |
|Module     | Module name where the issue identified in the assembly was detected.     |   Custom workflow activity      |
|Type     | Type of the issue identified in the assembly.        | Custom workflow activity        |
|Member     |  Member of the issue identified in the assembly.      | Custom workflow activity        |
|Statement     | The code statement or configuration that resulted in the issue.        |  All       |
|Comments     | Details about the issue that include high-level resolution steps.         |  All       |


## Run solution checker rules locally

You can run solution checker rules in your development environment to detect issues much sooner as you create your solution resources.  This is currently supported for web resources (JavaScript and [TypeScript](https://typescript-eslint.io/)). For more details, go to the NPM package [@microsoft/eslint-plugin-power-apps](https://www.npmjs.com/package/@microsoft/eslint-plugin-power-apps).

## Best practice rules used by solution checker

The following table lists the component type, rule description, severity, and category. Critical violations are blocked or warned when configured for solution checker enforcement with managed environments. More information: [Use solution checker in Managed Environments (preview)](/power-platform/admin/managed-environment-solution-checker)

> [!IMPORTANT]
> Solution checker enforcement with managed environments is a preview feature.

|Solution component  |Rule name  |Rule description  | Severity  | Category |
|---------|---------|---------|---------|---------|
|Plug-in or workflow activity   | [meta-remove-dup-reg](../../developer/data-platform/best-practices/business-logic/do-not-duplicate-plugin-step-registration.md?client=PAChecker&error=meta-remove-dup-reg&source=featuredocs)     | Avoid duplicate Dataverse plug-in registrations.     | Critical  | Performance |
|Plug-in or workflow activity   | [meta-avoid-reg-no-attribute](../../developer/data-platform/best-practices/business-logic/include-filtering-attributes-plugin-registration.md?client=PAChecker&error=meta-avoid-reg-no-attribute&source=featuredocs)  | Include filtering attributes with Dataverse plug-in registrations.    | Medium | Performance |
|Plug-in or workflow activity   | [meta-avoid-reg-retrieve](../../developer/data-platform/best-practices/business-logic/limit-registration-plugins-retrieve-retrievemultiple.md?client=PAChecker&error=meta-avoid-reg-retrieve&source=featuredocs)  | Use caution with Dataverse plug-ins registered for Retrieve and RetrieveMultiple messages.    | Medium | Performance |
|Plug-in or workflow activity   | [meta-remove-inactive](../../developer/model-driven-apps/best-practices/business-logic/remove-deactivated-disabled-configurations.md?client=PAChecker&error=meta-remove-inactive&source=featuredocs)    | Remove inactive configurations in Dataverse.    | Low | Maintainability |
|Plug-in or workflow activity   | [meta-avoid-crm4-event](../../developer/model-driven-apps/best-practices/index.md?client=PAChecker&error=meta-avoid-crm4-event&source=featuredocs) | Don't use Microsoft Dynamics CRM 4.0 plug-in registration stage.    | Medium | Upgrade readiness |
|Plug-in or workflow activity  | [meta-avoid-retrievemultiple-annotation](../../developer/data-platform/best-practices/index.md?client=PAChecker&error=meta-avoid-retrievemultiple-annotation)  | Avoid registering a plugin on RetrieveMultiple of annotation.  | High  | Usage |
|Web Resources  | [use-async](./powerapps-checker/rules/web/use-async.md)  |  Interact with HTTP and HTTPS resources asynchronously.   | Critical | Performance |
|Web Resources  | [avoid-modals](./powerapps-checker/rules/web/avoid-modals.md)  | Avoid using modal dialogs.   | High  | Supportability |
|Web Resources  | [avoid-dom-form](./powerapps-checker/rules/web/avoid-dom-form.md)  | | High  | Supportability |
|Web Resources  | [avoid-dom-form-event](./powerapps-checker/rules/web/avoid-dom-form-event.md)  | | High | Supportability |
|Web Resources  | [avoid-crm2011-service-odata](./powerapps-checker/rules/web/avoid-crm2011-service-odata.md) | Don't target the Microsoft Dynamics CRM 2011 OData 2.0 endpoint.     | Critical | Upgrade readiness |
|Web Resources  | [avoid-crm2011-service-soap](./powerapps-checker/rules/web/avoid-crm2011-service-soap.md)  | Don't target the Microsoft Dynamics CRM 2011 SOAP services.   | Critical | Upgrade readiness |
|Web Resources  | [avoid-loadtheme](./powerapps-checker/rules/web/avoid-loadtheme.md)  | Don't use `loadTheme` Fluent v8 API.   | Low | Supportability |
|Web Resources  | [avoid-browser-specific-api](./powerapps-checker/rules/web/avoid-browser-specific-api.md) | Don't use Internet Explorer legacy APIs or browser plug-ins. | Critical  | Upgrade readiness |
|Web Resources  | [avoid-unpub-api](./powerapps-checker/rules/web/avoid-unpub-api.md) |  | High | Supportability |
|Web Resources  | [avoid-window-top](./powerapps-checker/rules/web/avoid-window-top.md) | | High | Supportability |
|Web Resources  | [avoid-2011-api](./powerapps-checker/rules/web/avoid-2011-api.md)  | Don't use the deprecated Microsoft Dynamics CRM 2011 object model. Instead follow [Dataverse Web API](/powerapps/developer/data-platform/webapi/overview) documentation. | High  | Upgrade readiness |
|Web Resources  | [use-relative-uri](./powerapps-checker/rules/web/use-relative-uri.md)   | Don't use absolute Dataverse endpoint URLs.    | Medium  | Maintainability |
|Web Resources  | [use-cached-webresource](./powerapps-checker/rules/web/use-cached-webresource.md)   |  | Medium  | Performance |
|Web Resources  | [use-client-context](./powerapps-checker/rules/web/use-client-context.md)  | Use client contexts.   | Medium  | Upgrade readiness |
|Web Resources  | [use-navigation-api](./powerapps-checker/rules/web/use-navigation-api.md)   | Use navigation API parameters.   | Medium  | Upgrade readiness |
|Web Resources  | [use-offline](./powerapps-checker/rules/web/use-offline.md)   |  | Medium  | Upgrade readiness |
|Web Resources  | [do-not-make-parent-assumption](./powerapps-checker/rules/web/do-not-make-parent-assumption.md)   |  | High  | Design |
|Web Resources  | [use-org-setting](./powerapps-checker/rules/web/use-org-setting.md)   | Use organization settings.   | Medium  | Upgrade readiness |
|Web Resources  | [use-global-context](./powerapps-checker/rules/web/use-global-context.md)   |  | Medium  | Upgrade readiness |
|Web Resources  | [use-grid-api](./powerapps-checker/rules/web/use-grid-api.md)   | Use the grid APIs.    | Medium  | Upgrade readiness |
|Web Resources  | [use-utility-dialogs](./powerapps-checker/rules/web/use-utility-dialogs.md)   |    | Medium  | Usage |
|Web Resources  | [avoid-isActivityType](./powerapps-checker/rules/web/avoid-isactivitytype.md)   | Replace Xrm.Utility.isActivityType method with new Xrm.Utility.gettableMetadata and don't use in ribbon rules.    | Medium  | Upgrade readiness |
|Web Resources  | [meta-avoid-silverlight](/power-platform/important-changes-coming?client=PAChecker&error=meta-avoid-silverlight&source=featuredocs)   | Silverlight web resource usage is deprecated.   | Medium | Upgrade readiness |
| Web Resources  | [remove-debug-script](../../developer/model-driven-apps/best-practices/index.md?client=PAChecker&error=web-remove-debug-script)  | Avoid including debug script in non-development environments.  | Medium  | Usage |
| Web Resources  | [use-strict-mode](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-use-strict-mode&client=PAChecker)  | Use strict mode when possible.  | Medium   | Usage |
| Web Resources  | [use-strict-equality-operators](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-use-strict-equality-operators&client=PAChecker)  | Use strict equality operators.  | Medium  | Usage |
| Web Resources  | [avoid-eval](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-avoid-eval&client=PAChecker)  | Don't use the 'eval' function or its functional equivalents.  | Critical  | Security |
| Web Resources  | [avoid-with](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-avoid-with&client=PAChecker)  | Don't use the 'with' operator.  | High  | Performance |
| Web Resources  | [remove-alert](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-remove-alert&client=PAChecker)  | Don't use the 'alert' function or its functional equivalents.  | Medium  | Usage |
| Web Resources  | [remove-console](https://go.microsoft.com/fwlink/?LinkID=398563&error=web-remove-console&client=PAChecker)  | Avoid using methods on console.  | Medium  | Usage |
| Web Resources  | [avoid-ui-refreshribbon](./powerapps-checker/rules/web/avoid-ui-refreshribbon.md)  | Avoid using refreshRibbon in form onload and EnableRule. | Critical  | Performance |
| Web Resources  | [use-getsecurityroleprivilegesinfo](./powerapps-checker/rules/web/use-getsecurityroleprivilegesinfo.md)  | Avoid userSettings.securityRolePrivileges. Use userSettings.getSecurityRolePrivilegesInfo instead. | High  | Performance |
| Web Resources  | [web-sdl-no-cookies](https://github.com/microsoft/eslint-plugin-sdl/blob/main/docs/rules/no-cookies.md) | HTTP cookies are an old client-side storage mechanism with inherent risks and limitations. Use Web Storage, IndexedDB or other modern methods instead. | Medium | Security |
| Web Resources  | [web-sdl-no-document-domain](https://github.com/microsoft/eslint-plugin-sdl/blob/main/docs/rules/no-document-domain.md) | Writes to document.domain property must be reviewed to avoid bypass of same-origin checks. Usage of top level domains such as azurewebsites.net is strictly prohibited. | Medium | Security |
| Web Resources  | [web-sdl-no-document-write](https://github.com/microsoft/eslint-plugin-sdl/blob/main/docs/rules/no-document-write.md) | Calls to document.write or document.writeln manipulate DOM directly without any sanitization and should be avoided. Use document.createElement() or similar methods instead. | Medium | Security |
| Web Resources  | [web-sdl-no-html-method](https://github.com/microsoft/eslint-plugin-sdl/blob/main/docs/rules/no-html-method.md) | Direct calls to method html() often (e.g. in jQuery framework) manipulate DOM without any sanitization and should be avoided. Use document.createElement() or similar methods instead. | Medium | Security |
| Web Resources  | [web-sdl-no-inner-html](https://github.com/microsoft/eslint-plugin-sdl/blob/main/docs/rules/no-inner-html.md) |Assignments to innerHTML or outerHTML properties manipulate DOM directly without any sanitization and should be avoided. Use document.createElement() or similar methods instead. | Medium | Security |
| Web Resources  | [web-sdl-no-insecure-url](https://github.com/microsoft/eslint-plugin-sdl/blob/main/docs/rules/no-insecure-url.md) | Insecure protocols such as HTTP or FTP should be replaced by their encrypted counterparts (HTTPS, FTPS) to avoid sending potentially sensitive data over untrusted networks in plaintext. | Medium | Security |
| Web Resources  | [web-sdl-no-msapp-exec-unsafe](https://github.com/microsoft/eslint-plugin-sdl/blob/main/docs/rules/no-msapp-exec-unsafe.md) | Calls to MSApp.execUnsafeLocalFunction() bypass script injection validation and should be avoided. | Medium | Security |
| Web Resources  | [web-sdl-no-postmessage-star-origin](https://github.com/microsoft/eslint-plugin-sdl/blob/main/docs/rules/no-postmessage-star-origin.md) | Always provide specific target origin, not * when sending data to other windows using postMessage to avoid data leakage outside of trust boundary. | Medium | Security |
| Web Resources  | [web-sdl-no-winjs-html-unsafe](https://github.com/microsoft/eslint-plugin-sdl/blob/main/docs/rules/no-winjs-html-unsafe.md) | Calls to WinJS.Utilities.setInnerHTMLUnsafe() and similar methods do not perform any input validation and should be avoided. Use WinJS.Utilities.setInnerHTML() instead. | Medium | Security |
| Canvas App  | [app-formula-issues-high](https://go.microsoft.com/fwlink/?LinkID=398563&error=app-formula-issues-high&client=PAChecker)  | Refer to Power Apps formula references for additional details.  | Critical  | Design |
| Canvas App  | [app-formula-issues-medium](https://go.microsoft.com/fwlink/?LinkID=398563&error=app-formula-issues-medium&client=PAChecker)  | Refer to Power Apps formula references for additional details.  |  Medium  | Design |
| Canvas App  | [app-formula-issues-low](https://go.microsoft.com/fwlink/?LinkID=398563&error=app-formula-issues-low&client=PAChecker)  | Refer to Power Apps formula references for additional details. |  Low  | Design |
| Canvas App  | [app-use-delayoutput-text-input](https://go.microsoft.com/fwlink/?LinkID=398563&error=app-use-delayoutput-text-input&client=PAChecker)  | Use delayed load in some scenarios to improve performance. |  Medium  | Performance |
| Canvas App  | [app-reduce-screen-controls](https://go.microsoft.com/fwlink/?LinkID=398563&error=app-reduce-screen-controls&client=PAChecker)  | Limit the number of app controls for improved performance.  |  Medium  | Performance |
| Canvas App  | [app-include-accessible-label](https://go.microsoft.com/fwlink/?LinkID=398563&error=app-include-accessible-label&client=PAChecker)  | Use explicit labels to improve app accessibility. |  Medium  | Accessibility |
| Canvas App  | [app-include-alternative-input](https://go.microsoft.com/fwlink/?LinkID=398563&error=app-include-alternative-input&client=PAChecker)  | Ensure all interactive elements are accessible to alternative inputs.  |  Medium  | Accessibility |
| Canvas App  | [app-avoid-autostart](https://go.microsoft.com/fwlink/?LinkID=398563&error=app-avoid-autostart&client=PAChecker)  | Avoid using autostart on players within an app.  |  Medium  | Accessibility |

### See also

[Best practices and guidance for the Dataverse](../../developer/data-platform/best-practices/index.md)<br />
[Best practices and guidance for model-driven apps](../../developer/model-driven-apps/best-practices/index.md)<br />
[Common issues and resolutions for Solution Checker](common-issues-resolutions-solution-checker.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
