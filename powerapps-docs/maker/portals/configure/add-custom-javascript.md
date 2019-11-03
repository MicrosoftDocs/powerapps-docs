---
title: "Use custom JavaScript for a portal | MicrosoftDocs"
description: "Instructions to add custom JavaScript to a form in a portal"
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/04/2019
ms.author: shjais
ms.reviewer:
---

# Add custom JavaScript

The Web Form Step record contains a field named **Custom JavaScript** that can be used to store JavaScript code to allow you to extend or modify the form's visual display or function.

The custom block of JavaScript will be added to the bottom of the page just before the closing form tag element.

## Form fields

The HTML input ID of an entity field is set to the logical name of the attribute. This makes selecting a field, setting values, or other client-side manipulation easy by with [jQuery](http://jquery.com/).  

```JavaScript
$(document).ready(function() {
   $("#address1_stateorprovince").val("Saskatchewan");
});
```

## Additional client-side field validation
Sometimes you might need to customize the validation of fields on the form. The following example demonstrates adding a custom validator. This example forces the user to specify an email only if the other field for preferred method of contact is set to Email.

> [!NOTE]
> The client-side field validation is not supported in a subgrid.

```JavaScript
if (window.jQuery) {
   (function ($) {
      $(document).ready(function () {
         if (typeof (Page_Validators) == 'undefined') return;
         // Create new validator
         var newValidator = document.createElement('span');
         newValidator.style.display = "none";
         newValidator.id = "emailaddress1Validator";
         newValidator.controltovalidate = "emailaddress1";
         newValidator.errormessage = "<a href='#emailaddress1_label'>Email is a required field.</a>";
         newValidator.validationGroup = ""; // Set this if you have set ValidationGroup on the form
         newValidator.initialvalue = "";
         newValidator.evaluationfunction = function () {
            var contactMethod = $("#preferredcontactmethodcode").val();
            if (contactMethod != 2) return true; // check if contact method is not 'Email'.
            // only require email address if preferred contact method is email.
            var value = $("#emailaddress1").val();
            if (value == null || value == "") {
            return false;
            } else {
               return true;
            }
         };
 
         // Add the new validator to the page validators array:
         Page_Validators.push(newValidator);
 
         // Wire-up the click event handler of the validation summary link
         $("a[href='#emailaddress1_label']").on("click", function () { scrollToAndFocus('emailaddress1_label','emailaddress1'); });
      });
   }(window.jQuery));
}
```

## General validation

On click of the **Next**/**Submit** button, a function named **webFormClientValidate** is executed. You can extend this method to add custom validation logic.

```JavaScript
if (window.jQuery) {
   (function ($) {
      if (typeof (webFormClientValidate) != 'undefined') {
         var originalValidationFunction = webFormClientValidate;
         if (originalValidationFunction && typeof (originalValidationFunction) == "function") {
            webFormClientValidate = function() {
               originalValidationFunction.apply(this, arguments);
               // do your custom validation here
               // return false; // to prevent the form submit you need to return false
               // end custom validation.
               return true;
            };
         }
      }
   }(window.jQuery));
}
```
### See also

[Configure a portal](configure-portal.md)  
[Define entity forms](entity-forms.md)  
[Web Form steps for portals](web-form-steps.md)  
[Load Form/Load Tab step type](load-form-step.md)  
[Redirect step type](add-redirect-step.md)  
[Conditional step type](add-conditional-step.md)
