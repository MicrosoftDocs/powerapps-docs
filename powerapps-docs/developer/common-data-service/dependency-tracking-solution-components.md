---
title: "Dependency tracking for solution components (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Solution component dependencies help make sure you have a reliable experience working with solutions. They can be viewed in the application by clicking Show Dependencies" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Dependency tracking for solution components

Solutions are made of solution components. You’ll use the **Solutions** area in Common Data Service for Apps to create or add solution components. You can perform these actions programmatically by using the <xref:Microsoft.Crm.Sdk.Messages.AddSolutionComponentRequest> message or any messages that create or update solution components that include a `SolutionUniqueName` parameter.  
  
 Solution components often depend on other solution components. You can’t delete any solution component that has dependencies on another solution component. For example, a customized ribbon typically requires image or script web resources to display icons and perform actions using scripts. As long as the customized ribbon is in the solution, the specific web resources it uses are required. Before you can delete the web resources you must remove references to them in the customized ribbon. These solution component dependencies can be viewed in the application by clicking **Show Dependencies**.  
  
 This topic describes the types of solution components you can include in your solutions and how they depend on each other.  
  
<a name="bkmk_SolutionComponents"></a>   

## All solution components  
 The complete list of available solutions component types is located in the system `componenttype` global option set. The supported range of values for this property is available by including the file SampleCode\CS\HelperCode\OptionSets.cs or SampleCode\VB\HelperCode\OptionSets.vb in your project. However, many of the solution component types listed there are for internal use only and the list doesn’t provide information about the relationships between solution components.  
  
<a name="BKMK_SolutionComponentDependencies"></a>   

## Solution component dependencies  
 Solution component dependencies help make sure you have a reliable experience working with solutions. They prevent actions that you normally perform from unintentionally breaking customizations defined in a solution. These dependencies are what allow a managed solution to be installed and uninstalled simply by importing or deleting a solution.  
  
 The solutions framework automatically tracks dependencies for solution components. Every operation on a solution component automatically calculates any dependencies to other components in the system. The dependency information is used to maintain the integrity of the system and prevent operations that could lead to an inconsistent state.  
  
 As a result of dependency tracking the following behaviors are enforced:  
  
- Deletion of a component is prevented if another component in the system depends on it.  
  
- Export of a solution warns the user if there are any missing components that could cause failure when importing that solution in another system.  
  
   Warnings during export can be ignored if the solution developer intends that the solution is only to be installed in an organization where dependent components are expected to exist. For example, when you create a solution that is designed to be installed over a pre-installed ”base” solution.  
  
- Import of a solution fails if all required components aren’t included in the solution and also don’t exist in the target system.  
  
  -   Additionally, when you import a managed solution all required components must match the package type of the solution. A component in a managed solution can only depend on another managed component.  
  
  There are three types of solution component dependencies:  
  
  **Solution Internal**  
  Internal dependencies are managed by CDS for Apps. They exist when a particular solution component can’t exist without another solution component.  
  
  **Published**  
  Published dependencies are created when two solution components are related to each other and then published. To remove this type of dependency, the association must be removed and the entities published again.  
  
  **Unpublished**  
  Unpublished dependencies apply to the unpublished version of a publishable solution component that is being updated. After the solution component is published, it becomes a published dependency.  
  
  Solution internal dependencies are dependencies where actions with a solution component require an action for another solution component. For example, if you delete an entity, you should expect that all the entity attributes will be deleted with it. Any entity relationships with other entities will also be deleted.  
  
  However, an internal dependency may lead to a published dependency and still require manual intervention. For example, if you include a lookup field on an entity form and then delete the primary entity in the relationship, you can’t complete that deletion until you remove the lookup field from the related entity form and then publish the form.  
  
  When you perform actions programmatically with solutions, you can use messages related to the `Dependency` entity. See [Dependency Entity](/reference/entities/dependency.md) for messages you can use to identify dependencies that may exist before you delete a component or uninstall a solution.  
  
<a name="BKMK_CheckForSolutionComponentDependencies"></a>   
## Check for solution component dependencies  
 When you edit solutions you may find that you can’t delete a solution component because it has a published dependency with another solution component. Or, you may not be able to uninstall a managed solution because one of the components in the managed solution has been used in a customization in another unmanaged solution.  
  
 The following table lists the messages that you can use to retrieve data about solution component dependencies.  
  
|Message|Description|  
|-------------|-----------------|  
|<xref:Microsoft.Crm.Sdk.Messages.RetrieveDependentComponentsRequest>|Returns a list of dependencies for solution components that directly depend on a solution component.<br /><br /> For example, when you use this message for a global option set solution component, dependency records for solution components representing any option set attributes that reference the global option set solution component are returned.<br /><br /> When you use this message for the solution component record for the account entity, dependency records for all of the solution components representing attributes, views, and forms used for that entity are returned.|  
|<xref:Microsoft.Crm.Sdk.Messages.RetrieveRequiredComponentsRequest>|Returns a list of the dependencies for solution components that another solution component directly depends on. This message provides the reverse of the `RetrieveDependentComponentsRequest` message.|  
|<xref:Microsoft.Crm.Sdk.Messages.RetrieveDependenciesForDeleteRequest>|Returns a list of all the dependencies for solution components that could prevent deleting a solution component.|  
|<xref:Microsoft.Crm.Sdk.Messages.RetrieveDependenciesForUninstallRequest>|Returns a list of all the dependencies for solution components that could prevent uninstalling a managed solution.|  
  
<a name="BKMK_RootSolutionComponents"></a>   
## Common Solution components  
 These are the solution components displayed in the application and the components that you’ll work with directly when adding or removing solution components using the solution page. Each of the other types of solution components will depend on one or more of these solution components to exist.  
  
||||  
|-|-|-|  
|[Application Ribbons (RibbonCustomization)](dependency-tracking-solution-components.md#BKMK_RibbonCustomization)|[Entity (Entity)](dependency-tracking-solution-components.md#BKMK_Entity)|[Report (Report)](dependency-tracking-solution-components.md#BKMK_Report)|  
|[Article Template (KBArticleTemplate)](dependency-tracking-solution-components.md#BKMK_KBArticleTemplate)|[Field Security Profile (FieldSecurityProfile)](dependency-tracking-solution-components.md#BKMK_FieldSecurityProfile)|[SDK Message Processing Step (SDKMessageProcessingStep)](dependency-tracking-solution-components.md#BKMK_SDKMessageProcessingStep)|  
|[Connection Role (ConnectionRole)](dependency-tracking-solution-components.md#BKMK_ConnectionRole)|[Mail Merge Template (MailMergeTemplate)](dependency-tracking-solution-components.md#BKMK_MailMergeTemplate)|[Security Role (Role)](dependency-tracking-solution-components.md#BKMK_Role)|  
|[Contract Template (ContractTemplate)](dependency-tracking-solution-components.md#BKMK_ContractTemplate)|[Option Set (OptionSet)](dependency-tracking-solution-components.md#BKMK_OptionSet)|[Service Endpoint (ServiceEndpoint)](dependency-tracking-solution-components.md#BKMK_ServiceEndpoint)|  
|[Dashboard or Entity Form (SystemForm)](dependency-tracking-solution-components.md#BKMK_SystemForm)|[Plug-in Assembly (PluginAssembly)](dependency-tracking-solution-components.md#BKMK_PluginAssembly)|[Site Map (SiteMap)](dependency-tracking-solution-components.md#BKMK_SiteMap)|  
|[Email Template (EmailTemplate)](dependency-tracking-solution-components.md#BKMK_EmailTemplate)|[Process (Workflow)](dependency-tracking-solution-components.md#BKMK_Workflow)|[Web Resource (WebResource)](dependency-tracking-solution-components.md#BKMK_WebResource)|  
  
<a name="BKMK_RibbonCustomization"></a>   
### Application ribbons (RibbonCustomization)  
 Ribbon customizations for the application ribbon and entity ribbon templates. Application ribbons don’t include definitions of ribbons at the entity or form level.  
  
 Custom application ribbons frequently have published dependencies on web resources. Web resources are used to define ribbon button icons and JavaScript functions to control when ribbon elements are displayed or what actions are performed when a particular ribbon control is used. Dependencies are only created when the ribbon definitions use the `$webresource:` directive to associate the web resource to the ribbon. More information: [$webresource directive](/dynamics365/customer-engagement/developer/web-resources#BKMK_WebResourceDirective)  
  
<a name="BKMK_KBArticleTemplate"></a>   
### Article template (KBArticleTemplate)  
 Template that contains the standard attributes of an article. There is always an internal dependency between the article template and the KbArticle entity.  
  
<a name="BKMK_ConnectionRole"></a>   
### Connection role (ConnectionRole)  
 Role describing a relationship between a two records. Each connection role defines what types of entity records can be linked using the connection role. This creates a published dependency between the connection role and the entity.  
  
<a name="BKMK_ContractTemplate"></a>   
### Contract template (ContractTemplate)  
 Template that contains the standard attributes of a contract. There is always an internal dependency between the contract template and the contract entity.  
  
<a name="BKMK_SystemForm"></a>   
### Dashboard or entity form (SystemForm)  
 System form entity records are used to define dashboards and entity forms. When a SystemForm is used as an entity form there is an internal dependency on the entity. When a SystemForm is used as a dashboard there are no internal dependencies. Both entity forms and dashboards commonly have published dependencies related to their content. An entity form may have lookup fields that depend on an entity relationship. Both dashboards and entity forms may contain charts or subgrids that will create a published dependency on a view, which then has an internal dependency on an entity. A published dependency on web resources can be created because of content displayed within the dashboard or form or when a form contains JavaScript libraries. Entity forms have published dependencies on any attributes that are displayed as fields in the form.  
  
<a name="BKMK_EmailTemplate"></a>   

### Email template (EmailTemplate)  
 Template that contains the standard attributes of an email message. An email template typically includes fields that insert data from specified entity attributes. An email template can be linked to a specific entity when it is created so there can be an internal dependency on the entity. A global email template isn’t associated with a specific entity, but it may have published dependencies on entity attributes used to provide data. A process (workflow) frequently is configured to send an email using an email template creating a published dependency with the workflow.  
  
<a name="BKMK_Entity"></a>   

### Entity (Entity)  
 The primary structure used to model and manage data in CDS for Apps. Charts, forms, entity relationships, views, and attributes associated with an entity are deleted automatically when the entity is deleted because of the internal dependencies between them. Entities frequently have published dependencies with processes, dashboards, and email templates.  
  
<a name="BKMK_FieldSecurityProfile"></a>   
### Field security profile (FieldSecurityProfile)  
 Profile that defines the access level for secured attributes.  
  
<a name="BKMK_MailMergeTemplate"></a>   
### Mail merge template (MailMergeTemplate)  
 Template that contains the standard attributes of a mail merge document. A mail merge template has a published dependency on the entity it’s associated with.  
  
<a name="BKMK_OptionSet"></a>   
### Option set (OptionSet)  
 An option set defines a set of options. A picklist attribute uses an option set to define the options provided. Several picklist attributes may use a global option set so that the options they provide are always the same and can be maintained in one place. A published dependency occurs when a picklist attribute references a global option set. You can’t delete a global option set that is being used by a picklist attribute.  
  
<a name="BKMK_PluginAssembly"></a>   
### Plug-in assembly (PluginAssembly)  
 Assembly that contains one or more plug-in types. Plug-ins are registered to events that are typically associated with an entity. This creates a published dependency.  
  
<a name="BKMK_Workflow"></a>   
### Process (Workflow)  
 Set of logical rules that define the steps necessary to automate a specific business process, task, or set of actions to be performed. Processes provide a wide range of actions that create published dependencies on any other solution component referenced by the process. Each process also has a published dependency on the entity it’s associated with.  
  
<a name="BKMK_Report"></a>   
### Report (Report)  
 Data summary in an easy-to-read layout. A report has published dependencies on any entity or attribute data included in the report. Each report must also be associated with a Report category creating an internal dependency on a solution component called Report Related Category (ReportCategory). Reports may be configured to be subreports creating a published dependency with the parent report.  
  
<a name="BKMK_SDKMessageProcessingStep"></a>   
### SDK message processing step (SDKMessageProcessingStep)  
 Stage in the execution pipeline that a plug-in is to execute.  
  
<a name="BKMK_Role"></a>   
### Security role (Role)  
 Grouping of security privileges. Users are assigned roles that authorize their access to the CDS for Apps system. Entity forms can be associated with specific security roles to control who can view the form. This creates a published dependency between the security role and the form.  
  
> [!NOTE]
>  Only security roles from the organization business unit can be added to a solution. Only a user with read access to those security roles can add them to a solution.  
  
<a name="BKMK_ServiceEndpoint"></a>   
### Service endpoint (ServiceEndpoint)  
 Service endpoint that can be contacted.  
  
<a name="BKMK_SiteMap"></a>   
### Site map (SiteMap)  
 XML data used to control the application navigation pane. The site map may be linked to display an HTML web resource or an icon in the site map may use an image web resource. When the `$webresource:` directive is used to establish these associations a published dependency is created. More information: [$webresource directive](/dynamics365/customer-engagement/developer/web-resources#BKMK_WebResourceDirective)  
  
<a name="BKMK_WebResource"></a>   
### Web resource (WebResource)  
 Data equivalent to files used in web development. Web resources provide client-side components that are used to provide custom user interface elements. Web resources may have published dependencies with entity forms, ribbons and the SiteMap. When the `$webresource:` directive is used to establish associations in a ribbon or the SiteMap, a published dependency is created. For more information, see [$webresource directive](/dynamics365/customer-engagement/developer/web-resources#BKMK_WebResourceDirective).  
  
> [!NOTE]
>  Web resources may depend on other web resources based on relative links. For example, an HTML web resource may use a CSS or script web resource. A Silverlight web resource displayed outside of an entity form or chart must have an HTML web resource to host it. These dependencies aren’t tracked as solution dependencies.  
  
### See also  
 [Package and Distribute Extensions with Dynamics 365 Solutions](/dynamics365/customer-engagement/developer/package-distribute-extensions-use-solutions)   
 [Introduction to Solutions](introduction-solutions.md)   
 [Plan For Solution Development](/dynamics365/customer-engagement/developer/plan-solution-development)   
 [Create, Export, or Import an Unmanaged Solution](create-export-import-unmanaged-solution.md)   
 [Create, install, and update a managed solution](create-install-update-managed-solution.md)   
 [Create, Install, and Update a Managed Solution](create-install-update-managed-solution.md)   
 [Uninstall or Delete a solution](uninstall-delete-solution.md)   
 [Solution entities](/dynamics365/customer-engagement/developer/solution-entities)