---
title: "Set column values using parameters passed to a form (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can set default values for new records created by users by specifying values in the URL that is used to open the form." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Set column values using parameters passed to a form

You can set default values for new records created by users by specifying values in the URL that is used to open the form. By default, these values are set in the form, but can be changed by users before they save the record.  
  
<a name="BKMK_PassingParameters"></a>   

## Pass parameters to set column record values  
  
> [!NOTE]
> You can pass parameter values to the form to set column values using the `Xrm.Navigation.`[openForm](clientapi/reference/Xrm-Navigation/openForm.md) function. For example, see [Example: Use Xrm.Navigation.openForm to 0pen a new window](set-field-values-using-parameters-passed-form.md#BKMK_ExampleXrmNavigationOpentForm).  
  
 When you open a new form by using the URL address, you can include arguments in the `extraqs` parameter to set column values. The following requirements must be met:  
  
- You must encode the parameters passed in the `extraqs` parameter. To encode the parameters, use [encodeURIComponent](https://msdn.microsoft.com/library/aeh9cef7\(VS.85\).aspx).  To use special characters like "=" or "&" in the parameter values, you must double encode (e.g. to set `name` to `A=B&C`, it would be `extraqs=name%3DA%253DB%2526C`).
  
- The names of the query string arguments must match or include the names of columns for the table.  
  
- The values passed must be valid.  
  
- The value can’t be a script.  
  
- Any attempt to pass an invalid parameter or value will result in an error.  
  
- For Boolean columns, use either an integer value of `0` or `1`, or a text value of `true` or `false` to set the value.  
  
- For DateTime columns, use the text value of the date.  
  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

## Example: Set the value for string columns  

The following sample sets the value for the **Name** column of a new account record to "New Account".  
  
The unencoded value for the `extraqs` parameter is “name=New Account”.  
  
```  
/main.aspx?etn=account&extraqs=name%3DNew%20Account&pagetype=entityrecord  
```  

## Set values for lookup columns  
 The following table describes five types of lookup columns. For examples using lookup columns, see [Example: Set the value for lookup columns](set-field-values-using-parameters-passed-form.md) and [Example: Use Xrm.Navigation.openForm to open a new window](set-field-values-using-parameters-passed-form.md#BKMK_ExampleXrmNavigationOpentForm).  
  
|Lookup Type|Description|  
|-----------------|-----------------|  
|simple lookup|Allows for a single reference to one type of table.|  
|customer lookup|Allows for a single reference to either an account or a contact record.|  
|owner lookup|Allows for a single reference to either a team or a system user record.|  
|partylist lookup|Allows for multiple references to multiple tables.|  
|regarding lookup|Allows for a single reference to multiple tables.|  
  
 The following guidelines apply when setting the value of a lookup on a form using a query string argument:  
  
-   For simple lookups you must set the value and the text to display in the lookup. Use the suffix “name” with the name of the column to set the value for the text.  
  
     Don’t use any other arguments.  
  
-   For customer and owner lookups you must set the value and the name in the same way you set them for simple lookups. In addition you must use the suffix “type” to specify the type of table. Allowable values are account, contact, systemuser, and team.  
  
-   You can’t set the values for partylist or regarding lookups.  
  
## Example: Set the value for lookup columns  
 To set values for lookup columns, use the data value, the name value, and for customer or owner lookups only, specify the type value for the respective column. The following sample sets the owner column to a user named “Mark Folkerts”.  
  
 The unencoded value for the `extraqs` parameter is “**ownerid**={B8C6E040-656E-DF11-B414-00155DB1891A}&**owneridname**=Mark Folkerts&**owneridtype**=systemuser”.  
  
```  
/main.aspx?etn=lead&pagetype=entityrecord&extraqs=ownerid%3D%7bB8C6E040-656E-DF11-B414-00155DB1891A%7d%26owneridname%3DMark%20Folkerts%26owneridtype%3Dsystemuser  
```  
  
 The following sample sets the primary contact column to a user named “Yvonne McKay (sample)”.The unencoded value for the `extraqs` parameter is “**primarycontactid**={43b58571-eefa-e311-80c1-00155d2a68c4}&**primarycontactidname**=Yvonne McKay (sample)”.  
  
```  
/main.aspx?etn=account&pagetype=entityrecord&extraqs=primarycontactid%3D%7B43b58571-eefa-e311-80c1-00155d2a68c4%7D%26primarycontactidname%3DYvonne%20McKay%20(sample)  
```  
  
> [!NOTE]
> For a simple lookup like this, you don’t have to set a type value.  
  

## Example: Set the value for date columns  
 The following sample sets the **Est. Close Date** column for a new opportunity to January 31, 2011. The unencoded value for the `extraqs` parameter is “estimatedclosedate=01/31/11”.  
  
```  
/main.aspx?etn=opportunity&extraqs=estimatedclosedate%3D01%2F31%2F11&pagetype=entityrecord  
```  
  

## Example: Set the value for choice columns  

To set the value for a **Choice** column, set the integer value for the option. The following sample sets the **Role** column value to “Decision Maker” in a new contact record.  
  
 The unencoded value for the `extraqs` parameter is “accountrolecode=1”.  
  
```  
/main.aspx?etn=contact&extraqs=accountrolecode%3D1&pagetype=entityrecord  
``` 

## Example: Set the value for choices columns

To set the value for **Choices** column, Specify integer values for the options in the URL that is used to open the form. For example, to set the options for the **Hobbies** column, the unencoded value for the extraqs parameter will be “hobbies=[1,3,4]”.   

```  
/main.aspx?etn=contact&extraqs=hobbies%3D%5B1%2C3%2C4%5D&pagetype=entityrecord   
``` 
  
<a name="BKMK_ExampleXrmNavigationOpentForm"></a>   

## Example: Use Xrm.Navigation.openForm to open a new window  

 The following sample sets default values on several different columns and shows how to use the `Xrm.Navigation`.[openForm](clientapi/reference/Xrm-Navigation/openForm.md) function. It is equivalent to the previous example that used the `window.open` method.  
  
```Javascript  
function OpenNewContact() {  
 var parameters = {};  
 //Set the Parent Customer column value to “Contoso”.  
 parameters["parentcustomerid"] = "2878282E-94D6-E111-9B1D-00155D9D700B";  
 parameters["parentcustomeridname"] = "Contoso";  
 parameters["parentcustomeridtype"] = "account";  
 //Set the Address Type to “Primary”.  
 parameters["address1_addresstypecode"] = "3";  
 //Set text in the Description column.  
 parameters["description"] = "Default values for this record were set programmatically.";  
 //Set Do not allow E-mails to "Do Not Allow".  
 parameters["donotemail"] = "1";  
  
 // Define the table name to open the form  
 var entityFormOptions = {};
 entityFormOptions["entityName"] = "contact";

// Open the form
 Xrm.Navigation.openForm(entityFormOptions, parameters).then(
    function (success) {
        console.log(success);
    },
    function (error) {
        console.log(error);
    });  
}  
```  
  
<a name="BKMK_ExampleWindowOpen"></a>   

## Example: Use window.open to open a new window  
 The following sample sets default values on several different columns and shows how to use [encodeURIComponent](https://msdn.microsoft.com/library/aeh9cef7\(VS.85\).aspx) to encode the value of the `extraqs` parameter. If you use the [window.open](https://msdn.microsoft.com/library/ms536651\(VS.85\).aspx) method, you can control the features of the window that is opened.  
  
```Javascript  
function OpenNewContact() {  
    //Set the Parent Customer column value to “Contoso”.  
    var extraqs = "parentcustomerid={F01F3F6D-896E-DF11-B414-00155DB1891A}";  
    extraqs += "&parentcustomeridname=Contoso";  
    extraqs += "&parentcustomeridtype=account";  
    //Set the Address Type to “Primary”.  
    extraqs += "&address1_addresstypecode=3";  
    //Set text in the Description column.  
    extraqs += "&description=Default values for this record were set programatically.";  
    //Set Do not allow E-mails to "Do Not Allow".  
    extraqs += "&donotemail=1";  
    //Set features for how the window will appear.  
    var features = "location=no,menubar=no,status=no,toolbar=no";  
    // Open the window.  
    window.open("/main.aspx?etn=contact&pagetype=entityrecord&extraqs=" +  
     encodeURIComponent(extraqs), "_blank", features, false);  
}  
```  
  
### See also  

 [Open forms and views with a URL](open-forms-views-dialogs-reports-url.md)   
 [openForm](clientapi/reference/Xrm-Navigation/openForm.md)  
 [Configure a form to accept custom querystring parameters](configure-form-accept-custom-querystring-parameters.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]