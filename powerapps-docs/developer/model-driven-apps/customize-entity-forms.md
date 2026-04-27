---
title: "Customize Forms (Model-Driven Apps)"
description: "Learn how to customize forms in model-driven apps programmatically. Use the form designer and SystemForm table to create, view, and edit table records efficiently."
author: MitiJ
ms.author: mijosh
ms.date: 03/27/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
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

## Form properties  

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
|`Type`|`<forms>` element `type` parameter|Valid values for forms are:<br /><br /> - 2: `main`<br />-5: `mobile`<br />-6: `quick`<br />-7: `quickCreate`|

<a name="BKMK_CreateAndEditForms"></a>   

## Create and edit forms  

 You can create new forms only for tables where [EntityMetadata.CanCreateForms](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanCreateForms) allows it.  

 Create new forms by creating them directly or by using the `CopySystemForm` message. Use the [SDK for .NET CopySystemFormRequest class](xref:Microsoft.Crm.Sdk.Messages.CopySystemFormRequest) or the [Web API CopySystemForm action](xref:Microsoft.Dynamics.CRM.CopySystemForm). When you use the `CopySystemForm` message or **Save As** in the form editor, there's no inheritance between forms. Therefore, changes to the base form don't automatically apply to any forms created from it.  

 You can edit form definitions by exporting a managed solution, editing the form definitions, and then reimporting the solution. When you manually edit forms, use an XML editor that supports schema validation. For more information, see [Edit the customizations XML file with schema validation](edit-customizations-xml-file-schema-validation.md).  

## Open main form in a dialog by using client API

To open the main form in a dialog by using client API, call the [Xrm.Navigation.navigateTo](./clientapi/reference/xrm-navigation/navigateto.md) method. The [Xrm.Navigation.navigateTo](./clientapi/reference/xrm-navigation/navigateto.md) API method opens the dialog with several options, including the size and position.


> [!NOTE]
> The [Xrm.Navigation.openForm](./clientapi/reference/xrm-navigation/openform.md) method doesn't support opening a main form as a dialog.

## Example: Open a new record

In this example, the dialog opens a new account form for creating a new record. The dialog pops up in the center by using up to 50% of the available window as a modal on top of the form it was invoked or called from.

```JavaScript
var pageInput = {
    pageType: "entityrecord",
    entityName: "account",
    formType: 2,
};
var navigationOptions = {
    target: 2,
    width: {value: 50, unit:"%"},
    position: 1
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions);
```

:::image type="content" source="media/open-new-record-mfd.png" alt-text="Open a new record.":::

## Example: Open an existing record

In this example, the dialog opens an existing account record by using the account ID value over the contact form. Replace the ID with any record ID value to open the record in the dialog.

```JavaScript
var pageInput = {
    pageType: "entityrecord",
    entityName: "account",
    formType: 2,
    entityId: "00aa00aa-bb11-cc22-dd33-44ee44ee44ee" //replace with actual ID
};
var navigationOptions = {
    target: 2,
    width: {value: 80, unit:"%"},
    position: 1
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions);
```
:::image type="content" source="media/open-existing-record-mfd.png" alt-text="Open an existing record.":::

## Example: Open a new record on the side pane

In this example, the dialog opens a new record in the right corner of the window. You can achieve this behavior by using the pixel options.

```JavaScript
var pageInput = {
    pageType: "entityrecord",
    entityName: "account",
    formType: 2,
};
var navigationOptions = {
    target: 2,
    width: {value: 500, unit:"px"},
    position: 2
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions);
```

:::image type="content" source="media/open-record-side-pane-mfd.png" alt-text="Open an existing record on side pane.":::

## Example: Open main form in a dialog with callback method

This example shows how to invoke a main form dialog with a callback method after saving a record and closing the dialog.

```Javascript
var pageInput = {
    pageType: "entityrecord",
    entityName: "account",
    formType: 2
};
var navigationOptions = {
    target: 2,
    width: {value: 80, unit:"%"},
    position: 2  
};
Xrm.Navigation.navigateTo(pageInput, navigationOptions).then(
    function success(result) {
            console.log("Record created with ID: " + result.savedEntityReference[0].id + 
            " Name: " + result.savedEntityReference[0].name)
            // Handle dialog closed
    },
    function error() {
            // Handle errors
    }
);
```

### See also  

[Create and design forms](../../maker/model-driven-apps/create-design-forms.md)   
[SystemForm table](../data-platform/reference/entities/systemform.md)  
[Form XML schema](form-xml-schema.md)<br/>
[Xrm.Navigation.navigateTo](./clientapi/reference/xrm-navigation/navigateto.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
