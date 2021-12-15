---
title: "Configure a form to accept custom querystring parameters (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about configuring a form to accept custom querystring parameters. Use these parameters to set default values when you create a new record in the application." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: article
ms.assetid: 89287d32-0d16-8f7d-e0b6-8cc208212cff
author: Nkrb # GitHub ID
ms.subservice: mda-developer
ms.author: nabuthuk # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Configure a form to accept custom querystring parameters

The ability to pass values to a web page by using query strings represents a concern for security. Model-driven apps applies the best practice of always comparing any parameter passed as a query string against a list of expected parameter names and data types.  
  
 By default, model-driven apps allows a specified set of query string parameters to be passed to a form. You use these parameters to set default values when you create a new record in the application. Each parameter must use a standard naming convention that includes a reference to the column logical name. More information: [Set column values using parameters passed to a form](set-field-values-using-parameters-passed-form.md).  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

 In your applications, you may want to pass custom query string parameters to a form. This article provides information about how you can define a set of specific parameter names and data types that can be accepted for a specific form.  
  
## Define allowed query string parameters  

 There are two ways to specify which query string parameters will be accepted by the form:  
  
- Edit form properties  
  
- Edit form XML  
  
### Edit form properties  

 When you edit a form, on the **Home** tab in the **Form** group, select **Form Properties**. In the **Form Properties** dialog box, select the **Parameters** tab.  
  
 Use this tab to modify the names and data types that the form allows.  
  
### Edit FormXml  

 Within the exported solution customizations.xml file, immediately following the footer element, you can add a `<formparameters>` element. In the `<formparameters>` element, add `<querystringparameter>` elements to specify which parameters will be allowed.  
  
 The following describes the `querystringparameter` element parameters, `name` and `type`:  
  
- **name**. Each name column must contain at least one underscore ('\_') character, but the name of the query string parameter cannot begin with an underscore. The name also can’t start with “crm\_”. We strongly recommend that you use the customization prefix of the solution publisher as the naming convention. It's also recommended not to have the name  (querystringparameter name) be the same as the name of a column on the table. A valid `querystringparameter` name value is “myISV_contact_specialvalue”.  
  
    > [!IMPORTANT]
    >  If a `querystringparameter` element name is not unique, it may be overwritten by another parameter definition using a different data type.  
  
- **Type**. Match the data type values with the parameter values so that invalid data is not passed with the parameter. The following are valid data types:  
  
    -   Boolean  
  
    -   DateTime  
  
    -   Double  
  
    -   EntityType  
  
    -   Integer  
  
    -   Long  
  
    -   PositiveInteger  
  
        > [!NOTE]
        >  PositiveInteger includes “0” in the range of valid values.  
  
    -   SafeString  
  
    -   UniqueId  
  
    -   UnsignedInt  
  
### See also  

 [Set column values using parameters passed to a form](set-field-values-using-parameters-passed-form.md)   
 [Open forms and views with a URL](open-forms-views-dialogs-reports-url.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]