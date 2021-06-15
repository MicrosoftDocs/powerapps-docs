---
title: "Appendix: App certification checklist (PowerApps) | Microsoft Docs"
description: "The app certification checklist provides you information about the checks that your model-driven, canvas apps and flows have to go through before it can be published on AppSource."
ms.custom: ""
ms.date: 03/20/2019
ms.reviewer: "pehecke"
ms.service: "powerapps"
ms.topic: "article"
author: "omarcdoc" 
ms.author: "omarc" 
manager: "AnnBe" 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Appendix: App certification checklist


The following checklist provides the list of validations performed by Microsoft during the certification process after you [submit](next-steps-submit-app-cloud-partner-portal.md) your app. 

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

<table>
<tbody>
<tr>
<th>Apps</th>
<th>Validation Type</th>
<th>Certification checklist</th>
</tr>
<tr>
<td rowspan=5><a href="/powerapps/maker/model-driven-apps/model-driven-app-overview">Model-driven apps</a>, <a href="/powerapps/maker/canvas-apps/getting-started">canvas apps</a>, and <a href="/power-automate/getting-started">flows</a> that connect to Microsoft Dataverse<br/></td>
<td>Sanity Check</td>
<td><ul>
<li>Check for app registration type: Free, Trial or Contact me.</li>
<li>Verify the submitted <a href="/powerapps/developer/data-platform/create-package-app-appsource">package</a> contains all the artifacts required to publish on AppSource.</li>
<li>Download the end-to-end (E2E) functional document from <a href="https://partner.microsoft.com/dashboard">Partner Center</a> and validate if document is updated with functional scenarios and user/admin journey.</li>
</ul>
</td>
</tr>
<tr>
<td>Code Validation</td>
<td>
<ul>
<li>Code validation for canvas apps will be done through <a href="/powerapps/maker/canvas-apps/accessibility-checker">Accessibility Checker tool</a> in Power Apps to check for the following:
<ul>
<li>Static formula errors and warnings: If any issues found then certification team will share the feedback to resolve and resubmit to AppSource.</li>
<li>Runtime errors: May occur once the app is opened in Run mode to view. Any issues found will be reported through email.</li>
<li>Accessibility errors and warnings: All Accessibility errors should be resolved as per Solution Checker guidelines.</li>
</ul></li>
<li>Code Validation for Dataverse solution will be done utilizing <a href="/power-platform/alm/checker-api/overview">Power Apps Checker</a>.</li>
<li>Issues reported from Power Apps Checker will be manually validated for correctness and false positive issues will be reduced to low severity.</li>
<li>The quality of the solution and packages are validated against the AppSource certification <a href="/power-platform/alm/checker-api/retrieve-rulesets">ruleset</a>. 
<li>Generated report is shared with the publisher through email.</li>
</ul>
</td>
</tr>
<tr>
<td>Deployment Validation</td>
<td>
<ul>
<li>Solution will be installed to a Power Apps studio using <a href="/power-platform/alm/package-deployer-tool">Package Deployer</a>. Installed canvas apps will be manually located in the solution as well as on Apps section after installation and will make sure the app is opened in edit and run mode. Canvas App will be manually deleted from Power Apps studio to validate successful uninstallation</li>
<li>Check the canvas app successfully connects through the connectors provided by the publishers. For example, Dataverse or any other connections.</li>
<li>Check all Dataverse components (tables, web resources, plug-ins and other components) are available in the solution.</li>
<li>Manually uninstall the solution and check if all the components associated to the managed solution is removed.</li>
</ul>
</td>
</tr>
<tr>
<td>Functionality Validation</td>
<td>
<ul>
<li>Validate the functionality of the app based on the functional document shared by the publisher. All the features that are implemented in the app should pass.</li>
<li>Publisher should submit E2E functional document through <a href="https://partner.microsoft.com/dashboard">Partner Center</a>  or can share video links through emails.</li>
<li>If app requires any license configuration, certification team will share the instance details for publisher to update the required license.</li>
</ul></td>
</tr>
<tr>
<td>Security Validation</td>
<td>
<ul>
<li>Check whether canvas app connects to any external data source or connections that require access, and proper connection details to be shared in E2E document.</li>
<li>Check canvas app connects to any external connections out of Power Apps connectors.</li>
<li>Check any custom code provided inside Package Deployer. Validate the code before approving the app to AppSource.</li>
<li>Manually validate the code to see if the custom code is retrieving any customer data from target environment.</li>
</ul>
</td>
</tr>
<tr>
<td rowspan=5><a href="/powerapps/maker/canvas-apps/getting-started">Canvas apps</a> and <a href="/power-automate/getting-started">flows</a> that connect to data sources <i>other</i> than Dataverse
</td>
<td>Sanity Check</td>
<td><ul>
<li>Check canvas app contains a valid .msapp file.</li>
<li>Check the package folder has all required components like manifest, Jason and other image components.</li>
</ul>
</td>
</tr>
<tr>
<td>Code Validation</td>
<td><ul>
<li>Same as explained earlier for model-driven apps, canvas apps, and flows that connect to Dataverse</li></ul>
</td>
</tr>
<tr>
<td>Deployment Validation</td>
<td>
<ul>
<li>Canvas app will be manually installed to a Power Apps studio using import Apps feature. Installed canvas apps will be manually located in the Apps section after installation and will make sure the app is opened in edit and run mode. Canvas app will be manually deleted from Power Apps studio to validate successful uninstallation.</li>
<li>Check that the canvas app successfully connects the connectors provided by the publishers.</li>
</ul>
</td>
</tr>
<tr>
<td>Functionality Validation</td>
<td>
<ul>
<li>Same as explained earlier for model-driven apps, canvas apps, and flows that connect to Dataverse</li></ul></td>
</tr>
<tr>
<td>Security Validation</td>
<td>
<ul>
<li>Same as explained earlier for model-driven apps, canvas apps, and flows that connect to Dataverse</li></ul>
</td>
</tr>
</tbody>
</table>

For information on best practices for creating:
- Canvas apps, see [Canvas App Coding Standard and Guidelines](https://aka.ms/powerappscanvasguidelines)
- Model-driven apps, see [Understand model-driven app components](../../maker/model-driven-apps/model-driven-app-components.md)

### See also

[Partner Center documentation](/partner-center/)




  



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
