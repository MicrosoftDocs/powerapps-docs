---
title: Common field properties in PowerApps | MicrosoftDocs
description: Understand the Common field properties for Main form in Dynamics 365 for Customer Engagement
Keywords: Main form; Common field properties; Dynamics 365
author: Mattp123
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: Mattp123
ms.author: matp
manager: kvivek
ms.date: 06/18/2018
ms.service: crm-online
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: 2b91ee28-7f09-435e-9fae-5225aa698e22
---
# Common field properties

 Fields in a form display controls people use to view or edit data in an entity record. Fields can be formatted to occupy up to four columns within a section.  

You can access **Common field properties** in solution explorer. Under **Components**, expand **Entities**, expand the entity you want, and then select **Forms**. In the list of forms, open the form of type **Main**. Then double-click one of the fields to view Common field properties.

![common-field-properties](media/common-field-properties.png)
  
The following table describes properties that all fields have. Certain types of fields have special properties. These are described in [Special field properties](special-field-properties-legacy.md).  
  
|Tab|Property|Description|  
|---------|--------------|-----------------|  
|**Display**|**Label**|**Required**: By default the label will match the display name of the field. You can override that name for the form by entering a different label here.|  
||**Display label on the form**|You can choose not to display the label at all.|  
||**Field Behavior**|Specify the field level behavior using the check boxes.|  
||**Locking**|This will prevent the field from being removed from the form accidentally. This will prevent any configuration you have applied to the field, such as event handlers, from being cleared if the field were removed. To remove this field a customizer would need to clear this setting first.|  
||**Visibility**|Showing the field is optional and can be controlled using scripts. [!INCLUDE[proc_more_information]../../includes/proc-more-information.md)] [Visibility options](visibility-options-legacy.md)|  
||**Availability**|Choose if you want the tab to be available on the phone.|
|**Formatting**|**Select the number of columns the control occupies**|When the section containing the fields has more than one column you can set the field to occupy up to the number of columns that the section has.|  
|**Details**|**Display Name**, **Name**, and **Description**|These read-only fields are for reference. Click the **Edit** button for convenient access to the field definition if you want to edit it.<br /><br /> Each instance of a field in the form has a name property so that they can be referenced in form scripts, but this name is managed by the application. The first instance of the field is the name of the field specified when it was created. More information: [Create and edit fields](../common-data-service/create-edit-fields.md)<br /><br /> For each additional time that a field is included in a form, the name appends a number starting with 1 to the end. So if the field name is ‘new_cost’, the first instance is ‘new_cost’, the second is ‘new_cost1’, and so on for each instance of the field in the form.<br /><br />**Note:** The field **Description** value provides tooltip text for the field when people place their cursor over it.|  
|**Events**|**Form Libraries**|Specify any JavaScript web resources that will be used in the field `OnChange` event handler.<br /><br />|  
||**Event Handlers**|Configure the functions from the form libraries that should be called for the field `OnChange` event. More information: [Configure Event Handlers](configure-event-handlers-legacy.md)|  
|**Business Rules**|**Business Rules**|View and manage any business rules that reference this field. More information: [Create business rules and recommendations](create-business-rules-recommendations-apply-logic-form.md)|  
|**Controls**|**Controls**|Add controls and specify their availability on Web, Phone and Tablet .|  

## Next steps

[Use the Main form and its components](use-main-form-and-components.md)
