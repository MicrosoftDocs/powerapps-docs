---
title: "Developer Guide for model-driven apps| MicrosoftDocs"
description: "This SDK contains a wealth of resources, including code samples, which are designed to help you build powerful vertical applications using the Customer Engagement platform. It is a guide for developers writing solutions, server-side code, client applications and extensions, custom business logic, plug-ins, integration modules, custom workflow modules and more. The SDK contains an architectural overview of Customer Engagement, the entity model, security model, web services, and sample code."
ms.custom: ""
ms.date: 12/15/2017
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - D365CE
---
# Developer Guide for Model-driven apps

<!--[!INCLUDE[](../includes/cc_applies_to_update_9_0_0.md)]

Welcome to the [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] Customer Engagement Developer Guide (formerly referred to as the Dynamics 365 SDK). This documentation is for version 9.0, known as [!INCLUDE[pn_crm_9_0_0_online](../includes/pn-crm-9-0-0-online.md)], which is an online only release.

<table>
<tr>
<td>

<h2> Get started </h2>
<li><a href="get-started-sdk.md" data-raw-source="[Get started with the SDK](get-started-sdk.md)">Get started with the SDK</a></li>
<li><a href="developer-tools.md" data-raw-source="[Developer tools](developer-tools.md)">Developer tools</a></li>
<li><a href="choose-development-style.md" data-raw-source="[Choose your development style](choose-development-style.md)">Choose your development style</a></li>
<li><a href="security-dev/security-model.md" data-raw-source="[Understand security model](security-dev/security-model.md)">Understand security model</a></li>
</td>
<td>

<h2> Connect </h2>

<li><a href="connect-customer-engagement-web-services-using-oauth.md" data-raw-source="[Using OAuth](connect-customer-engagement-web-services-using-oauth.md)">Using OAuth</a></li>
<li><a href="oauth-cross-origin-resource-sharing-connect-single-page-application.md" data-raw-source="[Using Oauth with CORS](oauth-cross-origin-resource-sharing-connect-single-page-application.md)">Using Oauth with CORS</a></li>
<li><a href="active-directory-claims-based-authentication.md" data-raw-source="[Active Directory and claims-based auth](active-directory-claims-based-authentication.md)">Active Directory and claims-based auth</a></li>
<li><a href="build-windows-client-applications-xrm-tools.md" data-raw-source="[XRM tooling](build-windows-client-applications-xrm-tools.md)">XRM tooling</a></li>
<li><a href="build-web-applications-server-server-s2s-authentication.md" data-raw-source="[Server-to-Server (S2S) auth](build-web-applications-server-server-s2s-authentication.md)">Server-to-Server (S2S) auth</a></li>
</td>
</tr>

<tr>
<td>
<h2> Manage customer data </h2>

<li><a href="model-business-data.md" data-raw-source="[Model your business data](model-business-data.md)">Model your business data</a></li>
<li><a href="audit-entity-data-changes.md" data-raw-source="[Audit data changes](audit-entity-data-changes.md)">Audit data changes</a></li>
<li><a href="detect-duplicate-data-for-developers.md" data-raw-source="[Detect duplicate data](detect-duplicate-data-for-developers.md)">Detect duplicate data</a></li>
<li><a href="import-data.md" data-raw-source="[Import data](import-data.md)">Import data</a></li>
<li><a href="virtual-entities/get-started-ve.md" data-raw-source="[Virtual entities](virtual-entities/get-started-ve.md)">Virtual entities</a></li>
</td>
<td>
<h2> Use web services</h2>

<li><a href="use-microsoft-dynamics-365-web-api.md" data-raw-source="[Web API](use-microsoft-dynamics-365-web-api.md)">Web API</a></li>
<li><a href="org-service/get-started-managed-code-application-development.md" data-raw-source="[Organization service](org-service/get-started-managed-code-application-development.md)">Organization service</a></li>
<li><a href="use-discovery-service.md" data-raw-source="[Discovery service](use-discovery-service.md)">Discovery service</a></li>
<li><a href="online-management-api.md" data-raw-source="[Online Management API](online-management-api.md)">Online Management API</a></li>
</td>
</tr>

<tr>
<td>
<h2> Extend </h2>
<li><a href="create-manage-custom-business-apps-using-code.md" data-raw-source="[Custom business apps](create-manage-custom-business-apps-using-code.md)">Custom business apps</a></li>
<li><a href="write-plugin-extend-business-processes.md" data-raw-source="[Plug-ins](write-plugin-extend-business-processes.md)">Plug-ins</a></li>
<li><a href="automate-business-processes-customer-engagement.md" data-raw-source="[Automate business processes](automate-business-processes-customer-engagement.md)">Automate business processes</a></li>
<li><a href="asynchronous-service.md" data-raw-source="[Asynchronous service](asynchronous-service.md)">Asynchronous service</a></li>
<li><a href="azure-extensions.md" data-raw-source="[Azure extensions](azure-extensions.md)">Azure extensions</a></li>
<li><a href="use-webhooks.md" data-raw-source="[Webhooks](use-webhooks.md)">Webhooks</a></li>
<li><a href="clientapi/client-scripting.md" data-raw-source="[Client scripting (Client API)](clientapi/client-scripting.md)">Client scripting (Client API)</a></li>
</td>
<td>

<h2> Customize </h2>

<li><a href="customize-dev/customize-entity-forms.md" data-raw-source="[Entity forms](customize-dev/customize-entity-forms.md)">Entity forms</a></li>
<li><a href="customize-dev/customize-entity-views.md" data-raw-source="[Entity views](customize-dev/customize-entity-views.md)">Entity views</a></li>
<li><a href="customize-dev/customize-visualizations-dashboards.md" data-raw-source="[Visualizations and dashboards](customize-dev/customize-visualizations-dashboards.md)">Visualizations and dashboards</a></li>
<li><a href="customize-dev/customize-commands-ribbon.md" data-raw-source="[Commands and the ribbon](customize-dev/customize-commands-ribbon.md)">Commands and the ribbon</a></li>
<li><a href="customize-dev/when-edit-customization-file.md" data-raw-source="[Edit customizations file](customize-dev/when-edit-customization-file.md)">Edit customizations file</a></li>
</td>
</tr>

<tr>
<td>
<h2> Package extensions and customizations </h2>
<li><a href="package-distribute-extensions-use-solutions.md" data-raw-source="[Use solutions](package-distribute-extensions-use-solutions.md)">Use solutions</a></li>
<li><a href="create-packages-package-deployer.md" data-raw-source="[Use Package Deployer](create-packages-package-deployer.md)">Use Package Deployer</a></li>
<li><a href="compress-extract-solution-file-solutionpackager.md" data-raw-source="[Use SolutionPackager](compress-extract-solution-file-solutionpackager.md)">Use SolutionPackager</a></li>
<li><a href="publish-app-appsource.md" data-raw-source="[Publish your app on AppSource](publish-app-appsource.md)">Publish your app on AppSource</a></li>
</td>

<td>
<h2> Programming reference </h2>

<li><a href="about-entity-reference.md" data-raw-source="[Entity Reference](about-entity-reference.md)">Entity Reference</a></li>
<li><a href="/dynamics365/customer-engagement/web-api/about" data-raw-source="[Web API Reference](/dynamics365/customer-engagement/web-api/about)">Web API Reference</a></li>
<li><a href="https://docs.microsoft.com/dotnet/api/?view=dynamics-general-ce-9" data-raw-source="[Organization Service Reference](https://docs.microsoft.com/dotnet/api/?view=dynamics-general-ce-9)">Organization Service Reference</a></li>
<li><a href="clientapi/reference.md" data-raw-source="[Client API Reference](clientapi/reference.md)">Client API Reference</a></li>
</td>
</tr>

<tr>
<td>
<h2> Additional resources </h2>

<li><a href="../field-service/developer/connected-field-service-developer-guide.md" data-raw-source="[Developer Guide for Connected Field Service](../field-service/developer/connected-field-service-developer-guide.md)">Developer Guide for Connected Field Service</a></li>
<!--<li>[Developer Guide for Dynamics 365 for Marketing](../marketing/developer/marketing-developer-guide.md)</li>-->

</td>

<td>

</td>
</tr>


</table>


### See also

[Administrator Guide](../admin/admin-guide.md)

[Customization Guide](../customize/overview.md)

[Unified Service Desk Guide](../unified-service-desk/unified-service-desk.md)-->


