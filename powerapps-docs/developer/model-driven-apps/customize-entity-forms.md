---
title: "Customize entity forms (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Forms provide the user interface (UI) that people use to create, view, or edit entity records. Use the form designer in the customization tools to create and edit entity forms. This topic will provide information necessary to create or edit forms programmatically." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: e6a25bbe-e484-cfe9-9ad9-20ac6f19336a
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Customize entity forms

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/customize-dev/customize-entity-forms -->

Forms provide the user interface (UI) that people use to create, view, or edit entity records. Use the form designer in the customization tools to create and edit entity forms. More information: [Create and design forms](../../maker/model-driven-apps/create-design-forms.md) for information about tasks related to working with forms in the application.  

 This topic will provide information necessary to create or edit forms programmatically.  

<a name="BKMK_AccessingFormDefinitions"></a>   

## Access form definitions  
 Entity forms are stored in the `SystemForm` entity along with dashboards and visualizations. There are two ways that you can inspect the form definitions for an entity:  

-   Include the entity in an unmanaged solution and export the solution.  

-   Query the `SystemForm` entity  

<a name="BKMK_ViewingFormXml"></a>   

### View FormXML from an exported entity  
 Only definitions of system entity forms that have been customized are included in exported managed solution. To view the definition of a system entity form, you must either change it in some way, or create a new form by saving the existing form with a new name.  

 After you export the solution, extract the contents and view the customizations.xml file. You’ll find the definition of the forms in `ImportExportXml` > `Entities` > `Entity` > `FormXml`. 
 In the `<FormXml>` node, you’ll find each type of form is grouped in a `<forms>` element with the `type` attribute specifying the type of form.  

<a name="BKMK_FormProperties"></a>   
## Form properties  
 The following table describes key `SystemForm` entity attributes and the corresponding data included in the XML elements exported with the solution.  


|  SystemForm property  |                 FormXML element                 |                                                                                                              Description                                                                                                              |
|-----------------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   `AncestorFormId`    |                  `<ancestor>`                   |                      Unique identifier of the parent form. This is set when you create a new form by using **Save As** for an existing form or by using <xref:Microsoft.Crm.Sdk.Messages.CopySystemFormRequest>.                      |
|    `CanBeDeleted`     |                `<CanBeDeleted>`                 |                                    Information that specifies whether this component can be deleted.This managed property is only applied if the form was created by importing a managed solution.                                    |
|     `Description`     |                `<Descriptions>`                 | `Description` is a string and `<Descriptions>` contains any localized labels for the description of the form.<br /><br /> The localized labels can be retrieved using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveLocLabelsRequest>. |
| `FormActivationState` |             `<FormActivationState>`             |                                  Specifies the state of the form.<br /><br /> Only forms of type “main” can be deactivated.<br /><br /> Valid Values:<br /><br /> -   0: Inactive<br />-   1: Active                                  |
|       `FormId`        |                   `<formid>`                    |                                                                                                     Unique identifier of the form                                                                                                     |
|  `FormPresentation`   |              `<FormPresentation>`               |                                     Specifies whether this form is in the updated UI layout in [!INCLUDE[pn_dynamics_crm_online](../../includes/pn-dynamics-crm-online.md)] Common Data Service for Apps.                                      |
|       `FormXml`       |                    `<form>`                     |                                                                                                XML representation of the form layout.                                                                                                 |
|  `IntroducedVersion`  |              `<IntroducedVersion>`              |                                                                                          Version of the solution that the form was added in.                                                                                          |
|     `IsAIRMerged`     |                       N/A                       |                                           Specifies whether this form is merged with the updated UI layout in [!INCLUDE[pn_dynamics_crm_online](../../includes/pn-dynamics-crm-online.md)].                                           |
|   `IsCustomizable`    |               `<IsCustomizable>`                |                            Information that specifies whether this component can be customized.<br /><br /> This managed property is only applied if the form was created by importing a managed solution.                            |
|      `IsDefault`      |                       N/A                       |                                                                          Information that specifies whether the form or the dashboard is the system default.                                                                          |
|        `Name`         |               `<LocalizedNames>`                |       `Name` is a string and `<LocalizedNames>` contains any localized labels for the name of the form.<br /><br /> The localized labels can be retrieved using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveLocLabelsRequest>.       |
|   `ObjectTypeCode`    | The form is a decedent of the `Entity` element. |                                                                                        The `ObjectTypeCode` value is the entity logical name.                                                                                         |
|        `Type`         |       `<forms>` element `type` attribute        |                                                       Valid values for forms are:<br /><br /> -   2: `main`<br />-   5: `mobile`<br />-   6: `quick`<br />-   7: `quickCreate`                                                        |

<a name="BKMK_CreateAndEditForms"></a>   
## Create and edit forms  
 You can only create new forms for an entity where <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>. <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanCreateForms> allows it.  

 You can create new forms using either a <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or the <xref:Microsoft.Crm.Sdk.Messages.CopySystemFormRequest>. When using <xref:Microsoft.Crm.Sdk.Messages.CopySystemFormRequest> or using **Save As** in the form editor, note that there is no inheritance between forms. Therefore, changes to the base form aren’t automatically applied to any forms created from it.  

 Editing the form definitions from an exported managed solution and then re-importing the solution is a supported method to edit entity forms. When manually editing forms we strongly recommend you use an XML editor that allows for schema validation. More information: [Edit the Customizations XML File with Schema Validation](edit-customizations-xml-file-schema-validation.md)  

### See also  
 [Customize Microsoft Dynamics 365](/dynamics365/customer-engagement/developer/customize-dev/customize-applications)   <!-- TODO need to fic the link-->
 [Create and design forms](../../maker/model-driven-apps/create-design-forms.md)   
 [SystemForm Entity](../common-data-service/reference/entities/systemform.md)  
 [Create or edit how business rules are initiated](create-edit-how-business-rules-initiated.md)   
 [Form XML Schema](form-xml-schema.md)