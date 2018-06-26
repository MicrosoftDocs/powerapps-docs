---
title: "Create and design forms | MicrosoftDocs"
ms.custom: ""
ms.date: 03/21/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: 99c795e0-9165-4112-85b1-6b5e1a4aa5ec
caps.latest.revision: 33
ms.author: "rdubois"
manager: "brycho"
tags: 
 - "Links to topic not migrated"
---
# Create and design forms 

With PowerApps, forms provide the user interface that people use to interact with the data they need to do their work. It's important that the forms people use are designed to allow them to find or enter the information they need efficiently. 

In the default solution or an unmanaged solution, you can create new forms or edit existing forms for all entities that allow form customization. 
In an unmanaged solution, you can edit the managed properties for an unmanaged custom entity that was created for the solution.
If you’re viewing a managed solution, you can’t create new forms or edit existing forms for entities. However, if the managed properties for an entity in the managed solution are set to allow customization, you can add or edit forms to that entity. 
  

<a name="BKMK_TypesOfForms"></a> 
## Type of forms
There are several types of forms:  
|Form type|Description|More information|  
|---------------|-----------------|-----------------|  
|**Main**|Used in PowerApps apps, the Dynamics 365 customer engagement web application, Dynamics 365 for tablets, and Dynamics 365 for Outlook.<br /><br /> These forms provide the main user interface for interacting with entity data.|[Design considerations for main forms](design-considerations-main-forms.md)|  
|**Mobile**|Used for the Dynamics 365 for phones pages. This simplified form is designed to be used for mobile devices.|[Customize the mobile app](https://docs.microsoft.com/dynamics365/customer-engagement/customize/customize-phones-tablets)  |  
|**Quick Create**|Used in PowerApps apps, the Dynamics 365 customer engagement web application, Dynamics 365 for tablets, and Dynamics 365 for Outlook.<br /><br /> For updated entities, these forms provide a basic form optimized for creating new records.|[Create and edit quick create forms](create-edit-quick-view-forms.md) |  
|**Quick View**|Used in PowerApps apps, the Dynamics 365 customer engagement web application, Dynamics 365 for tablets, and Dynamics 365 for Outlook.<br /><br /> For updated entities, these forms appear within the main form to display additional data for a record that is referenced by a lookup field in the form.|[Create and edit quick view forms](create-edit-quick-view-forms.md)|  

While each form type has specific needs, when working with forms you use the Form Editor. More information: [Overview of the form editor user interface](form-editor-user-interface-legacy.md)
  
<a name="BKMK_FormDifferencesByEntity"></a>   
## Updated versus classic entities  
PowerApps provides many options for designing forms. With Unified Interface, most entities were updated to better suit the responsive interface. Updated entities as well as your own custom entities include support for the Dynamics 365 for tablets client, business process flows, and business rules. When you use these entities, you can design once and deploy to all clients.  
  
There are still a number of entities, referred to here as classic entities, that retain the appearance and capabilities from earlier versions. These entities are used less often. They are listed here:  
  
||||||  
|-|-|-|-|-|  
|Address|Article|Article Comment|Bulk Delete Operation|Connection|  
|Discount|Discount List|Document Location|Email Attachment|Follow|  
|Goal|Goal Metric|Import Source File|Invoice Product|Order Product|  
|Price List|Queue Item|Quote Product|Rollup Field|Rollup Query|  
|Saved View|Service|Service Activity|SharePoint Site|Site|  
|Territory|Unit|Unit Group|||  
  
### Next steps  
    
[Assign form order](assign-form-order.md) <br />
[Control access to forms](control-access-forms.md) <br />
[How main forms appear in different clients](main-form-presentations.md) <br />
