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
Sometimes you might need to customize the validation of fields on the form. The following example demonstrates adding a custom validator. This example forces the user to specify an email with a specific domain.

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
         newValidator.id = "adx_contactemailValidator";
         newValidator.controltovalidate = "adx_contactemail"; // Replace with the logical name of the form field
         newValidator.errormessage = "<a href='#adx_contactemail_label' referencecontrolid='adx_contactemail' onclick='javascript:scrollToAndFocus(\"adx_contactemail_label\",\"adx_contactemail\");return false;'>Email has to end with Microsoft domain.</a>";
         newValidator.initialvalue = "";
         newValidator.evaluationfunction = function () {
            var email = $("#adx_contactemail").val();
            var domain = "microsoft.com";
            if (email.endsWith(domain)) {
                return true;
            } else {
                return false;
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
- [Microsoft Learn: Extend Power Apps portals with scripts](/learn/modules/extend-power-app-portals/3-portal-javascript)
- [Microsoft Learn: Advanced client-side development](/learn/modules/extend-power-app-portals/5-advanced-portal-development)

