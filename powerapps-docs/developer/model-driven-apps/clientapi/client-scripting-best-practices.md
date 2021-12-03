---
title: "Best practices: Client scripting in model-driven apps| MicrosoftDocs"
ms.date: 10/19/2020
ms.service: powerapps
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 16271bd8-cfa8-4a7f-802a-60fbff7c3722
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Best practices: Client scripting in model-driven apps

The following are some of the tips you could consider while writing your JavaScript code for model-driven apps.

## Define unique JavaScript function names

When you write functions that will be used in JavaScript libraries, your functions may be loaded into a form with other JavaScript libraries. If another library contains a function that has the same name as a function you provide, whichever function is loaded last is defined for the page. To avoid having your functions overwritten by functions in another library, you should make sure that your functions have unique names. You can use of the following strategies:

- **Unique function prefix**: Define each of your functions using the standard syntax with a consistent name that includes a unique naming convention, as shown in the following example.
    ```JavaScript
    function MyUniqueName_performMyAction()
     {
    // Code to perform your action.
       }
    ```
- **Namespaced library names**:  As a best practice, you should always create namespaced JavaScript libraries to avoid having your functions overridden by functions in another library. More information: [Write you first JavaScript](walkthrough-write-your-first-client-script.md)
    ```JavaScript
    var Sdk = window.Sdk || {};
    (function () {
    this.formOnLoad = function () {
      // Code to perform your actions.
       }
    this.attributeOnChange = function () {
    // Code to perform your actions.
      } 
     this.formOnSave = function () {
    // Display an alert dialog
    }
    }). call(Sdk);
    ```

    Then when you use your function you can specify the full name. The following example shows this.

    ```JavaScript
    Sdk.attributeOnChange();
    ```


## Avoid using unsupported methods

On the Internet, you can find many examples or suggestions that describe using unsupported methods. These may include leveraging undocumented internal function for page controls. These methods may work but because they are not supported, you can’t expect that they will continue to work in future versions of model-driven apps.

## Avoid using jQuery for form scripts

You should not use jQuery in form scripts and ribbon commands. Most of the benefit provided by jQuery is that it allows for easy cross-browser manipulation of the DOM. This is explicitly unsupported within form scripts and ribbon commands. Restrict your scripts to use the objects/methods available in the [Xrm object model](understand-clientapi-object-model.md). If there are different versions of jQuery used by the platform and/or among components on the page your script runs on, there can be conflicts that cause issues. Since the platform and other components may change their version at any time, you may encounter an issue at any time by using jQuery.

If you are still considering using jQuery despite the risks, consider the following:

- For best performance, don’t load jQuery in the page if you do not need it.
- Using **$.ajax** to perform requests against the model-driven apps web services is supported, but there are alternatives. The alternative to using **$.ajax** is to use the browsers **XMLHttpRequest** object directly. The jQuery **$.ajax** method is just a wrapper for this object. If you use the native **XMLHttpRequest** object directly, you do not need to load jQuery.
- Each version of jQuery that is loaded in a page can be a different version. Different versions of jQuery have different behaviors and these can cause problems when multiple versions of jQuery are loaded on the same page. There is a technique to mitigate this, but it depends on editing the jQuery library and any other libraries that depend on jQuery.


## Write your code for multiple browsers

Model-driven apps support multiple browsers. Make sure that any scripts that you use will work with all supported browsers. Most of the significant differences between Internet Explorer and other browser have to do with HTML and XML DOM manipulation. Because HTML DOM manipulation is not supported, if script logic is only performing supported actions and using the [Xrm object model](understand-clientapi-object-model.md), the changes required to support other browsers could be small. 


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
