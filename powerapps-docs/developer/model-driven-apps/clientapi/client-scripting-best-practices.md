---
title: "Best practices: Client scripting in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 16271bd8-cfa8-4a7f-802a-60fbff7c3722
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Best practices: Client scripting in model-driven apps



These are some of the best practice tips you could consider while writing your JavaScript code for model-driven apps.

## Define unique JavaScript function names

When you write functions that will be used in JavaScript libraries, your functions may be loaded into a form with other JavaScript libraries. If another library contains a function that has the same name as a function you provide, whichever function is loaded last is defined for the page. To avoid having your functions overwritten by functions in another library, you should make sure that your functions have unique names. You can use of the following strategies:

- **Unique function prefix**: Define each of your functions using the standard syntax with a consistent name that includes a unique naming convention, as shown in the following example.
    ```JavaScript
    function MyUniqueName_performMyAction()
    {
        // Code to perform your action.
    }
    ```
- **Namespaced library names**: Associate each of your functions with a JavaScript object to create a kind of namespace to use when you call your functions as shown in the following example.
    ```JavaScript
    //If the MyUniqueName namespace object isn’t defined, create it.
    if (typeof (MyUniqueName) == "undefined")
       { MyUniqueName = {}; }
       // Create Namespace container for functions in this library;
       MyUniqueName.MyFunctions = {
         performMyAction: function(){
         // Code to perform your action.
         //Call another function in your library
         this.anotherAction();
       },
       anotherAction: function(){
         // Code in another function
      }
    };
    ```

    Then when you use your function you can specify the full name. The following example shows this.

    ```JavaScript
    MyUniqueName.MyFunctions.performMyAction();
    ```

    If you call a function within another function you can use the this keyword as a shortcut to the object that contains both functions. However, if your function is being used as an event handler, the this keyword will refer to the object that the event is occurring on.

## Avoid using unsupported methods

On the Internet, you can find many examples or suggestions that describe using unsupported methods. These may include leveraging undocumented internal function for page controls. These methods may work but because they are not supported, you can’t expect that they will continue to work in future versions of model-driven apps.

## Avoid using jQuery for form scripts

We do not recommend using jQuery in form scripts and ribbon commands. Most of the benefit provided by jQuery is that it allows for easy cross-browser manipulation of the DOM. This is explicitly unsupported within form scripts and ribbon commands. Restrict your scripts to use the objects/methods avaailable in the [Xrm object model](understand-clientapi-object-model.md). 

If you decide to use the remaining capabilities of jQuery that are useful with model-driven apps and include the ability to use **$.ajax**, consider the following:

- For best performance, don’t load jQuery in the page if you do not need it.
- Using **$.ajax** to perform requests against the model-driven apps web services is supported, but there are alternatives. The alternative to using **$.ajax** is to use the browsers **XMLHttpRequest** object directly. The jQuery **$.ajax** method is just a wrapper for this object. If you use the native **XMLHttpRequest** object directly, you do not need to load jQuery.
- Each version of jQuery that is loaded in a page can be a different version. Different versions of jQuery have different behaviors and these can cause problems when multiple versions of jQuery are loaded on the same page. There is a technique to mitigate this, but it depends on editing the jQuery library and any other libraries that depend on jQuery.


## Write your code for multiple browsers

Model-driven apps support multiple browsers. You should make sure that any scripts that you use will work with all supported browsers. Most of the significant differences between Internet Explorer and other browser have to do with HTML and XML DOM manipulation. Because HTML DOM manipulation is not supported, if script logic is only performing supported actions and using the [Xrm object model](understand-clientapi-object-model.md), the changes required to support other browsers could be small. 
