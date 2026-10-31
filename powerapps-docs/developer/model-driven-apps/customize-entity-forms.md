---
title: "Customize Forms (Model-Driven Apps)"
description: "Learn how to customize forms in model-driven apps programmatically. Use the form designer and SystemForm table to create, view, and edit table records efficiently."
author: MitiJ
ms.author: mijosh
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
ai-usage: ai-assisted
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Customize forms in model-driven apps

Forms in model-driven apps provide the user interface (UI) that people use to create, view, or edit table records. This article explains how to create or edit forms programmatically by using the [`SystemForm`](../data-platform/reference/entities/systemform.md) table and form designer in customization tools. You learn how to access form definitions, understand form properties, and implement forms through code examples.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

<a name="BKMK_AccessingFormDefinitions"></a>   

## Access form definitions  

The [`SystemForm`](../data-platform/reference/entities/systemform.md) table stores forms along with dashboards and visualizations. You can inspect the form definitions for a table in two ways:  

- Include the table in an unmanaged solution and export the solution.  

- Query the `SystemForm` table.  

<a name="BKMK_ViewingFormXml"></a>   

### View FormXML from an exported table  

 An exported managed solution includes only definitions of system forms that you customize. To view the definition of a system form, you must either change the form or create a new form by saving the existing form with a new name.  

 After you export the solution, extract the contents and view the `customizations.xml` file. You find the definition of the forms in `ImportExportXml` > `Entities` > `Entity` > `FormXml`. 
 In the `<FormXml>` node, each type of form is grouped in a `<forms>` element with the `type` parameter specifying the type of form.  

<a name="BKMK_FormProperties"></a>   

## SystemForm table form properties  

 The following table describes key `SystemForm` table columns and the corresponding data included in the XML elements exported with the solution.  


|SystemForm property|FormXML element|Description|
|----|----|----|
|`AncestorFormId`|`<ancestor>`|Unique identifier of the parent form. Set this property when you create a new form by using **Save As** for an existing form or by using the SDK for .NET [CopySystemFormRequest class](xref:Microsoft.Crm.Sdk.Messages.CopySystemFormRequest) or Web API [CopySystemForm action](xref:Microsoft.Dynamics.CRM.CopySystemForm).|
|`CanBeDeleted`|`<CanBeDeleted>`|Information that specifies whether this component can be deleted. This managed property only applies if you create the form by importing a managed solution.|
|`Description`|`<Descriptions>`| `Description` is a string and `<Descriptions>` contains any localized labels for the description of the form.<br /><br /> You can retrieve the localized labels by using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveLocLabelsRequest>. |
| `FormActivationState` |`<FormActivationState>`|Specifies the state of the form.<br /><br /> Only forms of type "main" can be deactivated.<br /><br /> Valid values:<br /><br /> -0: `Inactive`<br />-1: `Active`|
|`FormId`|`<formid>`|Unique identifier of the form|
|`FormPresentation`|`<FormPresentation>`|Specifies whether this form is in the updated UI layout in Microsoft Dataverse.|
|`FormXml`|`<form>`|XML representation of the form layout.|
|`IntroducedVersion`|`<IntroducedVersion>`|Version of the solution that the form was added in.|
|`IsAIRMerged`|N/A|Specifies whether this form is merged with the updated UI layout in Dataverse.|
|`IsCustomizable`|`<IsCustomizable>`|Information that specifies whether this component can be customized.<br /><br /> This managed property only applies if you create the form by importing a managed solution.|
|`IsDefault`|N/A|Information that specifies whether the form or the dashboard is the system default.|
|`Name`|`<LocalizedNames>`|`Name` is a string and `<LocalizedNames>` contains any localized labels for the name of the form.<br /><br /> You can retrieve the localized labels by using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveLocLabelsRequest>.|
|`ObjectTypeCode`| The form is a descendant of the `Entity` element. |The `ObjectTypeCode` value is the table logical name.|
|`Type`|`<forms>` element `type` parameter|Valid values for forms are:<br /><br /> -2: `main`<br />-5: `mobile`<br />-6: `quick`<br />-7: `quickCreate`|

<a name="BKMK_CreateAndEditForms"></a>   

## Create and edit forms  

 You can create new forms only for tables where [EntityMetadata.CanCreateForms](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanCreateForms) allows it.  

 Create new forms by creating them directly or by using the `CopySystemForm` message. Use the [SDK for .NET CopySystemFormRequest class](xref:Microsoft.Crm.Sdk.Messages.CopySystemFormRequest) or the [Web API CopySystemForm action](xref:Microsoft.Dynamics.CRM.CopySystemForm). When you use the `CopySystemForm` message or **Save As** in the form editor, there's no inheritance between forms. Therefore, changes to the base form don't automatically apply to any forms created from it.  

 You can edit form definitions by exporting a managed solution, editing the form definitions, and then reimporting the solution. When you manually edit forms, use an XML editor that supports schema validation. For more information, see [Edit the customizations XML file with schema validation](edit-customizations-xml-file-schema-validation.md).  

## Related content

[Create and design forms](../../maker/model-driven-apps/create-design-forms.md)   
[SystemForm table](../data-platform/reference/entities/systemform.md)  
[Form XML schema](form-xml-schema.md)<br/>
[Open main form in a dialog by using client API](open-main-form-dialog.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
