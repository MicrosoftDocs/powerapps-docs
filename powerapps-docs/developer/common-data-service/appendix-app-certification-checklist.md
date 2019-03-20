---
title: "Appendix: App certification checklist (PowerApps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use the app design checklist to evaluate your app design in PowerApps." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 02/25/2019
ms.reviewer: "kvivek"
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

<table>
<tbody>
<tr>
<th>Modules included</th>
<th>Validation Type</th>
<th>Certification checklist</th>
</tr>
<tr>
<td rowspan=5><strong>Dynamics 365 for Customer Engagement apps</strong> + <strong>PowerApps</strong> + <strong>Microsoft Flow</strong><br/><br/><strong>Dynamics 365 for Customer Engagement apps</strong> includes Dynamics 365 for Sales, Dynamics 365 for Customer Service, Dynamics 365 for Field Service, Dynamics 365 for Project Service Automation, and Dynamics 365 for Marketing.
</td>
<td>Sanity Check</td>
<td><ul>
<li>Check for app registration type: Free, Trial or Contact me. If registered in Contact me then publisher need to enable test drive.</li>
<li>Verify the submitted <a href="https://docs.microsoft.com/powerapps/developer/common-data-service/create-package-app-appsource">package</a> contains all the artifacts required to publish on AppSource.</li>
<li>Download the end-to-end (E2E) functional document from Cloud Partner Portal and validate if document is updated with functional scenarios and user/admin journey.</li>
</ul>
</td>
</tr>
<tr>
<td>Code Validation</td>
<td>
<ul>
<li>Code validation for Canvas apps will be done through <a href="https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/accessibility-checker">Accessibility Checker tool</a> in PowerApps to check for the following:
<ul>
<li>Static formula errors and warnings: If any issues found then certification team will share the feedback to resolve and resubmit to AppSource.</li>
<li>Runtime errors: May occur once the app is opened in Run mode to view. Any issues found will be reported through email.</li>
<li>Accessibility errors and warnings: All Accessibility errors should be resolved as per Solution Checker guidelines.</li>
</ul></li>
<li>Code Validation for Common Data Service solution will be done through <a href="https://experienceisv.microsoftcrmportals.com/precertification/#/">OnDemand Code Analysis (ODCA)</a> tool.</li>
<li>Issues reported from ODCA will be manually validated for correctness and false positive issues will be reduced to low severity.</li>
<li>Generated report is shared with the publisher through email.</li>
</ul>
</td>
</tr>
<tr>
<td>Deployment Validation</td>
<td>
<ul>
<li>CRM solution will be installed to a PowerApps studio using Dynamics Package Deployer. Installed canvas apps will be manually located on the CRM solution as well as on Apps section after installation and will make sure the app is opened in edit and run mode. Canvas App will be manually deleted from PowerApps studio to validate successful uninstallation</li>
<li>Check the canvas app successfully connects through the connectors provided by the publishers. For example, Common Data Service (CDS) for Apps or any other connections.</li>
<li>Check all Common Data Model (CDM) components (entities, web resources, plug-ins and other components) are available in the solution.</li>
<li>Manually uninstall the solution and check if all the components associated to the managed solution is removed.</li>
</ul>
</td>
</tr>
<tr>
<td>Functionality Validation</td>
<td>
<ul>
<li>Validate the functionality of the app based on the functional document shared by the publisher. All the features that are implemented in the app should pass.</li>
<li>Publisher should submit E2E functional document through Cloud Partner Portal or can share video links through emails.</li>
<li>If app requires any license configuration, certification team will share the instance details for publisher to update the required license.</li>
</ul></td>
</tr>
<tr>
<td>Security Validation</td>
<td>
<ul>
<li>Check whether canvas app connects to any external data source or connections that require access, and proper connection details to be shared in E2E document.</li>
<li>Check canvas app connects to any external connections out of PowerApps connectors.</li>
<li>Check any custom code provided inside Package Deployer. Validate the code before approving the app to AppSource.</li>
<li>Manually validate the code to see if the custom code is retrieving any customer data from target environment.</li>
</ul>
</td>
</tr>
<tr>
<td rowspan=5><strong>Canvas App
</td>
<td>Sanity Check</td>
<td><ul>
<li>Check for app registration type: Free, Trial or Contact me. If registered in Contact me then publisher need to enable test drive.</li>
<li>Verify the submitted <a href="https://docs.microsoft.com/powerapps/developer/common-data-service/create-package-app-appsource">package</a> contains all the artifacts required to publish on AppSource.</li>
<li>Download the end-to-end (E2E) functional document from Cloud Partner Portal and validate if document is updated with functional scenarios and user/admin journey.</li>
</ul>
</td>
</tr>
<tr>
<td>Code Validation</td>
<td>
<ul>
<li>Code validation for Canvas apps will be done through <a href="https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/accessibility-checker">Accessibility Checker tool</a> in PowerApps to check for the following:
<ul>
<li>Static formula errors and warnings: If any issues found then certification team will share the feedback to resolve and resubmit to AppSource.</li>
<li>Runtime errors: May occur once the app is opened in Run mode to view. Any issues found will be reported through email.</li>
<li>Accessibility errors and warnings: All Accessibility errors should be resolved as per Solution Checker guidelines.</li>
</ul></li>
<li>Code Validation for Common Data Service solution will be done through <a href="https://experienceisv.microsoftcrmportals.com/precertification/#/">OnDemand Code Analysis (ODCA)</a> tool.</li>
<li>Issues reported from ODCA will be manually validated for correctness and false positive issues will be reduced to low severity.</li>
<li>Generated report is shared with the publisher through email.</li>
</ul>
</td>
</tr>
<tr>
<td>Deployment Validation</td>
<td>
<ul>
<li>CRM solution will be installed to a PowerApps studio using Dynamics Package Deployer. Installed canvas apps will be manually located on the CRM solution as well as on Apps section after installation and will make sure the app is opened in edit and run mode. Canvas App will be manually deleted from PowerApps studio to validate successful uninstallation</li>
<li>Check the canvas app successfully connects through the connectors provided by the publishers. For example, Common Data Service (CDS) for Apps or any other connections.</li>
<li>Check all Common Data Model (CDM) components (entities, web resources, plug-ins and other components) are available in the solution.</li>
<li>Manually uninstall the solution and check if all the components associated to the managed solution is removed.</li>
</ul>
</td>
</tr>
<tr>
<td>Functionality Validation</td>
<td>
<ul>
<li>Validate the functionality of the app based on the functional document shared by the publisher. All the features that are implemented in the app should pass.</li>
<li>Publisher should submit E2E functional document through Cloud Partner Portal or can share video links through emails.</li>
<li>If app requires any license configuration, certification team will share the instance details for publisher to update the required license.</li>
</ul></td>
</tr>
<tr>
<td>Security Validation</td>
<td>
<ul>
<li>Check whether canvas app connects to any external data source or connections that require access, and proper connection details to be shared in E2E document.</li>
<li>Check canvas app connects to any external connections out of PowerApps connectors.</li>
<li>Check any custom code provided inside Package Deployer. Validate the code before approving the app to AppSource.</li>
<li>Manually validate the code to see if the custom code is retrieving any customer data from target environment.</li>
</ul>
</td>
</tr>
</tbody>
</table>


For information on best practices for creating Canvas apps, see [Canvas App Coding Standard and Guidelines](https://aka.ms/powerappscanvasguidelines).

  




  

