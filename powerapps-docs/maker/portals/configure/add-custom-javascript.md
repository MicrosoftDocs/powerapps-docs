---
title: Add custom JavaScript to a form
description: Learn how to add custom JavaScript to a form in a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 07/15/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - Professor Kendrick
---

# Add custom JavaScript to a form

Both the [basic form](entity-forms.md) and [advanced form](web-form-properties.md) step records contain a field named **Custom JavaScript** that can be used to store JavaScript code to allow you to extend or modify the form's visual display or function.

The custom block of JavaScript will be added to the bottom of the page just before the closing form tag element.

## Form fields

The HTML input ID of a table field is set to the logical name of the attribute. Selecting a field, setting values, or other client-side manipulation easy by with [jQuery](https://jquery.com/).  

```JavaScript
$(document).ready(function() {
   $("#address1_stateorprovince").val("Saskatchewan");
});
```

> [!Important]
> Adding a choice column to model-driven form to be used in an advanced form step or a basic form will appear on the portal page as a drop-down server control. Using custom JavaScript to add additional values to the control will result in an “Invalid postback or callback argument” message on the page submission.

## Additional client-side field validation
Sometimes you might need to customize the validation of fields on the form. This example forces the user to specify an email only if the other field for preferred method of contact is set to Email.

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
         newValidator.errormessage = "<a href='#emailaddress1_label' referencecontrolid='emailaddress1 ' onclick='javascript:scrollToAndFocus(\"emailaddress1 _label\",\" emailaddress1 \");return false;'>Email is a required field.</a>";
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

      });
   }(window.jQuery));
}
```

## General validation

On click of the **Next**/**Submit** button, a function named **entityFormClientValidate** is executed. You can extend this method to add custom validation logic.

```JavaScript
if (window.jQuery) {
   (function ($) {
      if (typeof (entityFormClientValidate) != 'undefined') {
         var originalValidationFunction = entityFormClientValidate;
         if (originalValidationFunction && typeof (originalValidationFunction) == "function") {
            entityFormClientValidate = function() {
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

- [Configure a portal](configure-portal.md)  
- [Define basic forms](entity-forms.md)  
- [Advanced Form steps for portals](web-form-steps.md)  
- [Load Form/Load Tab step type](load-form-step.md)  
- [Redirect step type](add-redirect-step.md)  
- [Conditional step type](add-conditional-step.md)
- [Extend Power Apps portals with scripts](/training/modules/extend-power-app-portals/3-portal-javascript)
- [Advanced client-side development](/training/modules/extend-power-app-portals/5-advanced-portal-development)
