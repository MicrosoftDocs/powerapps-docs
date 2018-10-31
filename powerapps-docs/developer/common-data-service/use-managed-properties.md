---
title: "Use managed properties (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Managed properties help you define which of the managed solution components can be customized" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Use managed properties

You can control which of your managed solution components are customizable by using managed properties. You should allow as much customization as possible for those solution components that represent business entities. This lets organizations customize your           solution to their requirements. Limit or eliminate customization of critical solution components that provide the core functionality of your solution so that you can predictably support and maintain it.  
  
 Managed properties are intended to protect your solution from modifications that may cause it to break. Managed properties do not provide digital rights management (DRM), or capabilities to license your solution or control who may install it.  
  
## Apply managed properties  
 You apply managed properties when the solution is unmanaged. The managed properties will take effect after you package the managed solution and install it in a different organization. After the managed solution is installed, the managed properties cannot be              updated except by an update of the solution by the original publisher.  
  
 Most solution components have a **Managed Properties** button when viewing a list of solution components. You can view or update the managed properties for a solution component when you click this button. To access managed properties for solutions that do not display this button, select **Managed Properties** from the **More Actions** drop-down list.  
  
 By default, all custom solution components are customizable. To change the managed properties for a solution component, click the **Managed Properties** button in the toolbar for the solution component. Each solution component has a **Can be customized**(                 `IsCustomizable`) property. As long as this property is true, more properties specific to the type of solution component can be specified. If you set the              `IsCustomizable.Value`property to false, after the solution is installed as a managed solution the solution component will not be customizable. The following table lists the managed properties for each solution component.  
  
|Component|Display Name|Property|  
|---------------|------------------|--------------|  
|Entity|Can be customized|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsCustomizable>.                                 `Value`|  
|Entity|Display name can be modified|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsRenameable>.                              `Value`|  
|Entity|Can be related entity in relationship|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanBeRelatedEntityInRelationship>.                                 `Value`(Read Only)|  
|Entity|Can be primary entity in relationship|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanBePrimaryEntityInRelationship>.                                 `Value`(Read Only)|  
|Entity|Can be in many-to-many relationship|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanBeInManyToMany>.                               `Value`(Read Only)|  
|Entity|New forms can be created|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanCreateForms>.                              `Value`|  
|Entity|New charts can be created|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanCreateCharts>.                               `Value`|  
|Entity|New views can be created|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanCreateViews>.                              `Value`|  
|Entity|Can change any other entity properties not represented by a managed property|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanModifyAdditionalSettings>.                                `Value`|  
|Field (Attribute)|Can be customized|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsCustomizable>.                                 `Value`|  
|Field (Attribute)|Display name can be modified|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsRenameable>.                              `Value`|  
|Field (Attribute)|Can change requirement level|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.RequiredLevel>.                                `CanBeChanged`<br /><br /> Note:<br /><br /> `RequiredLevel`is the only managed property to use the                                     `CanBeChanged`property.|  
|Field (Attribute)|Can change any other attribute properties not represented by a managed property|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.CanModifyAdditionalSettings>.                                 `Value`|  
|Entity Relationship|Can be customized|<xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase.IsCustomizable>.                              `Value`|  
|Form|Can be customized|`SystemForm.IsCustomizable.Value`|  
|Chart|Can be customized|`SavedQueryVisualization.IsCustomizable.Value`|  
|View|Can be customized|`SavedQuery.IsCustomizable.Value`|  
|Option Set|Can be customized|<xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadataBase.IsCustomizable>.                              `Value`|  
|Web Resource|Can be customized|`WebResource.IsCustomizable.Value`|  
|Workflow|Can be customized|`Workflow.IsCustomizable.Value`|  
|Assembly|Can be customized|`SdkMessageProcessingStep.IsCustomizable.Value`|  
|Assembly Registration|Can be customized|`ServiceEndpoint.IsCustomizable.Value`|  
|E-mail Template|Can be customized|`Template.IsCustomizable.Value`|  
|KB Article Template|Can be customized|`KbArticleTemplate.IsCustomizable.Value`|  
|Contract Template|Can be customized|`ContractTemplate.IsCustomizable.Value`|  
|Mail Merge Template|Can be customized|`MailMergeTemplate.IsCustomizable.Value`|  
|Dashboard|Can be customized|`SystemForm.IsCustomizable.Value`|  
|Security Roles|Can be customized|`Role.IsCustomizable.Value`|  
  
### Update managed properties  
 After you release your managed solution, you may decide that you want to change the managed properties. You can only change managed properties to make them less restrictive. For example, after your initial release you can decide to allow customization of an                      entity.  
  
 You update managed properties for your solution by releasing an update to your solution with the changed managed properties. Your managed solution can only be updated by another managed solution associated with the same publisher record as the original managed                       solution. If your update includes a change in managed properties to make them more restrictive, those managed property changes will be ignored but other changes in the update will be applied.  
  
 Because the original publisher is a requirement to update managed properties for a managed solution, any unmanaged solution cannot be associated with a publisher that has been used to install a managed solution.  
  
> [!NOTE]
>  This means you will not be able to develop an update for your solution by using an organization where your managed solution is installed.  
  
## Check managed properties  
 Use the                <xref:Microsoft.Crm.Sdk.Messages.IsComponentCustomizableRequest>to check whether a solution component is customizable. Alternatively, you can check the solution component properties but you must consider that the ultimate determination of                 the meaning depends on the values of several properties. Each solution component has an                 `IsCustomizable`property. When a solution component is installed as part of a managed solution, the                 `IsManaged`property will be true. Managed properties are only enforced for managed solutions. When checking managed properties to determine if an individual solution component is customizable, you must check both the                `IsCustomizable`and                 `IsManaged`properties. A solution component where               `IsCustomizable`is false and                `IsManaged`is false, is customizable.  
  
 Entity and attribute have more managed properties in addition to               `IsCustomizable`. These managed properties are not updated if               `IsCustomizable`is set to false. This means that in addition to checking the individual managed property, you must also check the               `IsCustomizable`property to see if the managed property is being enforced.  
  
### See also  
 [Managed properties](/dynamics365/customer-engagement/developer/introduction-solutions#BKMK_ManagedProperties)   
 [Plan For Solution Development](/dynamics365/customer-engagement/developer/plan-solution-development)   
 [Maintain Managed Solutions](maintain-managed-solutions.md)   
 [Package and Distribute Extensions with Dynamics 365 Solutions](/dynamics365/customer-engagement/developer/package-distribute-extensions-use-solutions)   
 <xref:Microsoft.Crm.Sdk.Messages.IsComponentCustomizableRequest>