---
title: "Client API Form Context in Model-Driven Apps"
description: "Learn how the Client API form context provides a reference to forms and form items in model-driven apps. Use formContext instead of deprecated Xrm.Page for better development practices."
author: MitiJ
ms.author: mijosh
ms.date: 03/27/2026
ms.reviewer: jdaly
ms.topic: article
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
  - tahoon-ms
---
# Client API form context

The Client API form context (**formContext**) provides a reference to the form or to an item on the form, such as a quick view control or a row in an editable grid, against which the current code is executed.

Earlier, you used the global **Xrm.Page** object to represent a form or an item on the form. In the latest version, the **Xrm.Page** object is [deprecated](/dynamics365/get-started/whats-new/customer-engagement/important-changes-coming#some-client-apis-are-deprecated). Instead, use the [getFormContext](reference/executioncontext/getFormContext.md) method of the passed-in execution context object to return a reference to the appropriate form or an item on the form. 

> [!IMPORTANT]
> *Deprecated* means that Microsoft intends to remove a feature or capability from a future major release of model-driven apps. The feature or capability continues to work and is fully supported until it's officially removed. Microsoft makes a public announcement at least six months before removal, in the documentation, on the official blog, and in many other places.<br/><br/>To maintain backward compatibility with existing scripts, use of the **Xrm.Page** object as a static access to the primary form context is *still* supported and won't be removed as soon as some other client API methods listed in the [Client API deprecation](/dynamics365/get-started/whats-new/customer-engagement/important-changes-coming#some-client-apis-are-deprecated) section. Use the new **formContext** object instead of the **Xrm.Page** object in your code targeting version 9.0 or later where possible. Also, by using the **formContext** object, you can create common event handlers that can operate either on a form or in an editable grid depending on where it's called. For more information, see [getFormContext (Client API reference)](reference/executioncontext/getFormContext.md).<br><br>Getting the **formContext** object for JavaScript functions for ribbon actions is different from how you get it in form scripting. For more information, see [Form and grid context in ribbon actions](../pass-data-page-parameter-ribbon-actions.md#form-and-grid-context-in-ribbon-actions).

> [!NOTE]
> Form contexts are only valid during the event where they're passed. [The same restrictions apply as with execution contexts](clientapi-execution-context.md#using-context-objects-asynchronously).

## Use the formContext object instead of the Xrm.Page object 

It's easy to convert existing code that uses **Xrm.Page** to use the new **formContext** object. For example, consider the following script that uses the **Xrm.Page** object:

```JavaScript
function displayName()
{
   var firstName = Xrm.Page.getAttribute("firstname").getValue();
   var lastName = Xrm.Page.getAttribute("lastname").getValue();
   console.log(firstName + " " + lastName);
}
```

Here's the updated script that uses the passed-in execution context to retrieve the **formContext** object instead of using the static **Xrm.Page** object:

```JavaScript
function displayName(executionContext)
{
   var formContext = executionContext.getFormContext(); // get formContext

   // use formContext instead of Xrm.Page   
   var firstName = formContext.getAttribute("firstname").getValue(); 
   var lastName = formContext.getAttribute("lastname").getValue();
   console.log(firstName + " " + lastName);
}
```

>[!IMPORTANT]
>Select the **Pass execution context as first parameter** option in the **Handler Properties** dialog while defining your event handlers to use the **formContext** object. For more information, see [Client API execution context](clientapi-execution-context.md).

## formContext object model

Use the **data** and **ui** objects under the **formContext** object to programmatically manipulate data and user interface elements in model-driven apps.

![formContext object model.](../media/ClientAPI-formContextModel.png)

[!INCLUDE[cc-terminology](../../data-platform/includes/cc-terminology.md)]

### data object

Provides properties and methods to work with the data on a form, including table data and data in the business process flow control. Contains the following objects:


| Object   | Description|
|----------|-------------------------------------------------------------------------------------------------------------------|
|`attributes`|Collection of non-table data on the form. Items in this collection are of the same type as the column collection, but they aren't columns of the form table. <br/>More information: [Collections](reference/collections.md)|
|`entity`|Provides methods to retrieve information specific to the record displayed on the page, the save method, and a collection of all the columns included on the form. Column data is limited to columns represented on the form. <br/>More information: [formContext.data.entity](reference/formContext-data-entity.md)|
|`process`|Provides objects and methods to interact with the business process flow data on a form.<br/>More information: [formContext.data.process](reference/formContext-data-process.md)|

It also provides an **attributes** collection for accessing non-table bound control. See the **Collections in the formContext object model** section later in this article.

More information: [formContext.data](reference/formContext-data.md) 

### ui object

Provides methods to retrieve information about the user interface, in addition to collections for several subcomponents of the form or grid. Contains the following objects:

| Object| Description|
|----|----|
|`formSelector`|Provides an items collection that you can use to query the forms available for the current user. Use the `navigate` method to close the current form and open a different one.|
|`navigation`|Doesn't contain any methods. Provides access to navigation items through the items collection. See the next section on collections for more information.|
|`process`|Provides methods to interact with the business process flow control on a form.|

More information: [formContext.ui](reference/formContext-ui.md)

## Collections in the formContext object model

The following table describes the collections in the **Xrm** object model. For
information about the methods available for collections in general, see [Collections (Client API reference)](reference/collections.md).

|Collection| Description|
|----|----|
| [attributes](reference/attributes.md)  | Two objects contain a column collection:<br/><br/>- **formContext.data.attributes** collection provides access to non-table bound columns.<br/><br/>- **formContext.data.entity.attributes** collection provides access to each table column that's available on the form. Only those columns added to the form are available.| 
| [controls](reference/controls.md)  | Three objects contain a controls collection:<br/><br/> - **formContext.ui.controls**: Provides access to each control present on the form.<br/><br/>- **formContext.data.entity.attribute.controls**: Because a column might have more than one control on the form, this collection provides access to each of them. This collection contains only one item unless multiple controls for the column are added to the form.<br/><br/>- **formContext.ui.tabs.sections.controls**: This collection only contains the controls found in the section.|
|**formContext.data.process.**[stages](reference/formContext-data-process/process/getStages.md) and **formContext.data.process**.[steps](reference/formContext-data-process/stage/getSteps.md)| Provides access to stages and steps collection in a business process flow. These also allow for adding and removing of items from the collection.|
|**formContext.ui.formSelector.**[items](reference/formContext-ui-formselector.md)|When multiple forms are provided for a table, you can associate each form with security roles. When the security roles associated with a user enable them to see more than one form, the **formContext.ui.formSelector.items** collection provides access to each form definition available to that user.|
|**formContext.ui.navigation.**[items](reference/formContext-ui-navigation.md)|The **formContext.ui.navigation.items** collection provides access to navigation items that are defined using the navigation area of the form editor. People navigate to these items by using the command bar.|
|**formContext.ui.**[quickForms](reference/formContext-ui-quickForms.md) | Provides methods to access all the quick view controls and its constituent controls on the forms.|
|**formContext.ui.**[tabs](reference/formContext-ui-tabs.md) | You can organize each form by using one or more tabs. This collection provides access to each of these tabs.|
|**formContext.ui Tab.**[sections](reference/formContext-ui-tab-sections.md) | You can organize each form tab by using one or more sections. The tab **sections** collection provides access to each of these sections. You need to define the tab that contains the desired section or iterate through each tab to find the relevant section.|


  
### Related articles

[getFormContext method](reference/executioncontext/getFormContext.md)   
[getGlobalContext method](reference/xrm-utility/getGlobalContext.md)   
[getAttribute method](reference/attributes.md)   
[getControl method](reference/controls/getcontrol.md)   
[Execution context methods](reference/execution-context.md) 


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
