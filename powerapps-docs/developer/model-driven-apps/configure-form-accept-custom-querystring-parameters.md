---
title: "Configure Form Query String Parameters in Model-Driven Apps"
description: "Configure custom query string parameters for model-driven app forms to securely set default values when creating records. Learn how to customize your forms."
author: MitiJ
ms.author: mijosh
ms.date: 08/25/2026
ms.reviewer: jdaly
ms.topic: article
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Configure a form to accept custom query string parameters

Custom query string parameters let you pass expected values to model-driven app forms while validating parameter names and data types. This article explains how to configure allowed parameters so you can securely set default values when creating records.  
  
By default, model-driven apps allows a specified set of query string parameters to be passed to a form. You use these parameters to set default values when you create a new record in the application. Each parameter must use a standard naming convention that includes a reference to the column logical name. For more information, see [Set column values using parameters passed to a form](set-field-values-using-parameters-passed-form.md).  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

 In your applications, you might want to pass custom query string parameters to a form. This article provides information about how you can define a set of specific parameter names and data types that you can accept for a specific form.  
  
## Define allowed query string parameters  

 There are two ways to specify which query string parameters the form will accept:  
  
- Edit form properties with the classic editor
- Edit form XML  
  
### Edit form properties  

When you edit a form by using the modern form editor as described in [Open the model-driven app form editor](../../maker/model-driven-apps/open-form-editor.md), select the ellipse in the menu, and then select **Switch to classic**.


1. On the **Home** tab, in the **Form** group, select **Form Properties**. 

   :::image type="content" source="media/form-properties-button.png" alt-text="Screenshot of the Form Properties button on the classic form editor Home tab.":::

1. In the **Form Properties** dialog box, select the **Parameters** tab.

   :::image type="content" source="media/form-properties-parameters-tab.png" alt-text="Screenshot of the Parameters tab in the Form Properties dialog box.":::
  
   Use this tab to modify the names and data types that the form allows. 

Learn more about: 
- [The classic form editor](../../maker/model-driven-apps/form-editor-user-interface-legacy.md)
- [Model-driven app form properties](../../maker/model-driven-apps/form-properties-legacy.md)
  
### Edit FormXml  

 Within the exported solution customizations.xml file, immediately following the footer element, you can add a `<formparameters>` element. In the `<formparameters>` element, add `<querystringparameter>` elements to specify which parameters are allowed.  
  
 The following table describes the `querystringparameter` element parameters, `name` and `type`:  
  
#### `name`

Each name column must contain at least one underscore (`_`) character, but the name of the query string parameter can't begin with an underscore. The name also can't start with `crm_`. Use the customization prefix of the solution publisher as the naming convention. Don't use the same name for the `querystringparameter` as the name of a column on the table. A valid `querystringparameter` name value is `myISV_contact_specialvalue`.  
  
> [!IMPORTANT]
>  If a `querystringparameter` element name isn't unique, another parameter definition that uses a different data type might overwrite it.  
  
#### `Type`

Match the data type values with the parameter values so that the parameter doesn't pass invalid data. The following data types are valid:  
  
- `Boolean`  
- `DateTime`  
- `Double`  
- `EntityType`  
- `Integer`  
- `Long`  
- `PositiveInteger`  (Includes "0" in the range of valid values)
- `SafeString`  
- `UniqueId`  
- `UnsignedInt`  
  
### See also  

[Set column values using parameters passed to a form](set-field-values-using-parameters-passed-form.md)   
[Open forms and views with a URL](open-forms-views-dialogs-reports-url.md)    
[Classic form editor overview](../../maker/model-driven-apps/form-editor-user-interface-legacy.md)   
[Model-driven app form properties](../../maker/model-driven-apps/form-properties-legacy.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
