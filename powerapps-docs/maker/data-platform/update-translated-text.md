---
title: Update existing localized labels with Power Apps
description: Learn how to update model-driven app form and column labels that are translated using Power Apps.
ms.custom: ""
ms.date: 10/09/2023
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: how-to
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Update localized labels for forms

This article describes how to update existing localized labels that were created following the steps in the article [Translate localizable text for model-driven apps](../model-driven-apps/translate-localizable-text.md).

## Updating localized labels overview

When you create a new model-driven app form and add columns to the form, the form creates a copy of the localized labels for those columns in the base language. Once a form is created, changing the localized label text for a column in the base language doesn't update the localized label on the form. However, you can change the column, tab, and section labels that can be localized for a form using the form designer. For more information about customized text, go to [Configure column properties on a form](../model-driven-apps/add-move-or-delete-fields-on-form.md#configure-column-properties-on-a-form).

To update localized labels for forms through the export translations Excel file, you need to correctly identify the object ID corresponding to each tab, section, or column. The following sections explain how to do this.

## Identify the object ID for form labels

1. Create a solution and add the form as part of this new solution.
1. Export the solution as managed.
1. Unzip the solution file and open the customizations.xml file with an XML or text editor.
1. Find the tab, section, or column of the form that has the localized label you want to update.  
1. Once you find the tab, section, or column, check if there's `labelid` property defined. If yes, then the value of `labelid` attribute is the object ID for the localized label. If not, then the value of the ID attribute is the object ID for localized label.

For example, say you want to find the object ID for attribute `websiteurl`. Search for that attribute in the customizations.xml file in the `formxml` section.

```xml
<row> 
<cell id="{e6441984-4343-813a-aa7e-e2747ad35390}" showlabel="true" labelid="{aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb}"> 
<labels> 
<label description="Website" languagecode="1033" /> 
</labels> 
<control id="websiteurl" classid="{71716B6C-711E-476c-8AB8-5D11542BFB47}" datafieldname="websiteurl" disabled="false" /> 
</cell> 
</row>
```

In the example, since the `labelid` property is defined, the object ID is *aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb*.

Now that you have the object ID, you can follow the steps to export the translations file. Open the file, to locate the object ID to make your localized text updates for the tab, section, or column. For more information about how to translate the customized text into another language, go to [Translate customized table, form, and column text into other languages](export-customized-entity-field-text-translation.md).

### What if you can't find the asset in customizations XML?

When you export a model-driven form, only the diff between the active layer and last managed layer is exported. If you don't make any changes to the tab, section, or column, the asset doesn't appear in the customizations.xml.

You can modify the label or any other property of the asset using the form designer, and then export the changes to find the object ID.

## Alternate way to find the object ID of a localized label

There are two alternative ways to find the object ID for a localized label:

- Find the full form XML of the form by viewing the **Properties** page for the solution layers of the model-driven app form. For more information about solution layers, go to [View the solution layers for a component](solution-layers.md#view-the-solution-layers-for-a-component).
- You can also make an OData call to retrieve the form xml if you know the form ID.
  - `[environmentURL]/api/data/v9.0/systemforms(b0742891-2411-494b-bfe7-93bc20356399)?$select=formxml`

## See also

[Overview of the model-driven form designer](../model-driven-apps/form-designer-overview.md)
