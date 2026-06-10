---
title: "Set column values using parameters passed to a form (model-driven apps)"
description: "You can set default values for new records created by users by specifying values in the URL that is used to open the form."
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
# Set column values by using parameters you pass to a form

Set default values for new records by specifying values in the URL that opens the form. By default, the form sets these values, but users can change them before saving the record.  
  
<a name="BKMK_PassingParameters"></a>   

## Pass parameters to set column record values  
  
> [!NOTE]
> Use the `Xrm.Navigation.`[openForm](clientapi/reference/Xrm-Navigation/openForm.md) function to pass parameter values to the form to set column values. For an example, see [Example: Use Xrm.Navigation.openForm to open a new window](#example-use-xrmnavigationopenform-to-open-a-new-window).  
  
When you open a new form by using the URL address, include arguments in the `extraqs` parameter to set column values. The following requirements must be met:  
  
- Encode the parameters you pass in the `extraqs` parameter. To encode the parameters, use [encodeURIComponent](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent).  To use special characters like `=` or `&` in the parameter values, double encode them. For example, to set `name` to `A=B&C`, use `extraqs=name%3DA%253DB%2526C`.
- The names of the query string arguments must match or include the names of columns for the table.  
- The values you pass must be valid.  
- The value can't be a script.  
- Any attempt to pass an invalid parameter or value results in an error.  
- For Boolean columns, use either an integer value of `0` or `1`, or a text value of `true` or `false` to set the value.  
- For DateTime columns, use the text value of the date.

## Example: Set the value for string columns  

The following sample sets the value for the **Name** column of a new account record to "New Account".  
  
The unencoded value for the `extraqs` parameter is `name=New Account`.  
  
```  
/main.aspx?etn=account&extraqs=name%3DNew%20Account&pagetype=entityrecord  
```  

## Set values for lookup columns

The following table describes five types of lookup columns. For examples using lookup columns, see [Example: Set the value for lookup columns](set-field-values-using-parameters-passed-form.md) and [Example: Use Xrm.Navigation.openForm to open a new window](#example-use-xrmnavigationopenform-to-open-a-new-window).  
  
|Lookup Type|Description|  
|-----------------|-----------------|  
|Simple lookup|Single reference to one type of table.|  
|Customer lookup|Single reference to either an account or a contact record.|  
|owner lookup|Single reference to either a team or a system user record.|  
|Partylist lookup|Multiple references to multiple tables.|  
|Regarding lookup|Single reference to multiple tables.|  
  
 The following guidelines apply when setting the value of a lookup on a form by using a query string argument:  
  
- For simple lookups, set the value and the text to display in the lookup. Use the suffix `name` with the name of the column to set the value for the text.  
  
     Don't use any other arguments.  
  
- For customer and owner lookups, set the value and the name in the same way you set them for simple lookups. In addition, use the suffix `type` to specify the type of table. Acceptable values are `account`, `contact`, `systemuser`, and `team`.  
  
- You can't set the values for partylist or regarding lookups.  
  
## Example: Set the value for lookup columns

To set values for lookup columns, use the data value, the name value, and for customer or owner lookups only, specify the type value for the respective column. The following sample sets the owner column to a user named "Mark Folkerts".  

The unencoded value for the `extraqs` parameter is "**ownerid**={B8C6E040-656E-DF11-B414-00155DB1891A}&**owneridname**=Mark Folkerts&**owneridtype**=systemuser".  
  
```  
/main.aspx?etn=lead&pagetype=entityrecord&extraqs=ownerid%3D%7bB8C6E040-656E-DF11-B414-00155DB1891A%7d%26owneridname%3DMark%20Folkerts%26owneridtype%3Dsystemuser  
```  
  
 The following sample sets the primary contact column to a user named "Yvonne McKay (sample)".The unencoded value for the `extraqs` parameter is "**primarycontactid**={43b58571-eefa-e311-80c1-00155d2a68c4}&**primarycontactidname**=Yvonne McKay (sample)".  
  
```  
/main.aspx?etn=account&pagetype=entityrecord&extraqs=primarycontactid%3D%7B43b58571-eefa-e311-80c1-00155d2a68c4%7D%26primarycontactidname%3DYvonne%20McKay%20(sample)  
```  
  
> [!NOTE]
> For a simple lookup like this, you don't need to set a type value.  
  

## Example: Set the value for date columns

The following sample sets the **Est. Close Date** column for a new opportunity to January 31, 2011. The unencoded value for the `extraqs` parameter is `estimatedclosedate=01/31/11`.  
  
```  
/main.aspx?etn=opportunity&extraqs=estimatedclosedate%3D01%2F31%2F11&pagetype=entityrecord  
```  
  

## Example: Set the value for choice columns  

To set the value for a **Choice** column, set the integer value for the option. The following sample sets the **Role** column value to "Decision Maker" in a new contact record.  
  
 The unencoded value for the `extraqs` parameter is `accountrolecode=1`.  
  
```  
/main.aspx?etn=contact&extraqs=accountrolecode%3D1&pagetype=entityrecord  
``` 

## Example: Set the value for choices columns

To set the value for a **Choices** column, specify integer values for the options in the URL that you use to open the form. For example, to set the options for the **Hobbies** column, the unencoded value for the `extraqs` parameter is `hobbies=[1,3,4]`.   

```  
/main.aspx?etn=contact&extraqs=hobbies%3D%5B1%2C3%2C4%5D&pagetype=entityrecord   
``` 
  
<a name="BKMK_ExampleXrmNavigationOpentForm"></a>   

## Example: Use Xrm.Navigation.openForm to open a new window  

The following `openNewContactExample` function sets default values on several different columns and shows how to use the [`Xrm.Navigation.openForm`](clientapi/reference/Xrm-Navigation/openForm.md) function. It's equivalent to the previous example that used the `window.open` method.  

```javascript
/**
 * Opens a new contact form with pre-populated default values
 * @returns {Promise<void>}
 */
async function openNewContactExample() {
    // Define form parameters with default values
    const formParameters = {
        parentcustomerid: "2878282E-94D6-E111-9B1D-00155D9D700B",
        parentcustomeridname: "Contoso",
        parentcustomeridtype: "account",
        address1_addresstypecode: "3", // Primary address type
        description: "Default values for this record were set programmatically.",
        donotemail: "1" // Do not allow emails
    };

    // Configure form options
    const entityFormOptions = {
        entityName: "contact"
    };

    try {
        const result = await Xrm.Navigation.openForm(entityFormOptions, formParameters);
        console.log("Form opened successfully:", result);
    } catch (error) {
        console.error("Failed to open contact form:", error);
        throw error; // Re-throw to allow caller to handle if needed
    }
}  
```  
  
<a name="BKMK_ExampleWindowOpen"></a>   

## Example: Use window.open to open a new window

The following `openNewContactExample` function sets default values on several different columns and shows how to use [encodeURIComponent](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) to encode the value of the `extraqs` parameter. If you use the [window.open](https://developer.mozilla.org/docs/Web/API/Window/open) method, you can control the features of the window that opens.
  
```javascript  
/**
 * Opens a new contact form in a new window with pre-populated default values
 * @returns {Window|null} Reference to the opened window or null if blocked
 */
function openNewContactExample() {
    // Define form parameters with default values
    const formParameters = {
        parentcustomerid: "{F01F3F6D-896E-DF11-B414-00155DB1891A}",
        parentcustomeridname: "Contoso",
        parentcustomeridtype: "account",
        address1_addresstypecode: "3", // Primary address type
        description: "Default values for this record were set programmatically.",
        donotemail: "1" // Do not allow emails
    };

    // Build query string using URLSearchParams for better handling
    const params = new URLSearchParams(formParameters);
    const extraqs = params.toString();

    // Configure window features
    const windowFeatures = "location=no,menubar=no,status=no,toolbar=no";
    
    // Build the URL
    const baseUrl = "/main.aspx";
    const url = `${baseUrl}?etn=contact&pagetype=entityrecord&extraqs=${encodeURIComponent(extraqs)}`;
    
    try {
        // Open the window
        const newWindow = window.open(url, "_blank", windowFeatures, false);
        
        if (!newWindow) {
            console.warn("Window opening was blocked by the browser");
            return null;
        }
        
        return newWindow;
    } catch (error) {
        console.error("Failed to open contact form window:", error);
        throw error;
    }
}  
```  
  
### See also  

[Open forms and views with a URL](open-forms-views-dialogs-reports-url.md)   
[openForm](clientapi/reference/Xrm-Navigation/openForm.md)  
[Configure a form to accept custom querystring parameters](configure-form-accept-custom-querystring-parameters.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
