---
title: "What are code components? | MicrosoftDocs"
description: "Use the PowerApps component framework to create code components to provide enhanced user experience for users to view and work with data in forms, views, and dashboards."
manager: kvivek
ms.date: 09/05/2019
ms.service: "powerapps"
ms.topic: "article"
ms.assetid: 135481cd-4583-4e49-8f58-02f32a9b054a
ms.author: "nabuthuk"
author: Nkrb
---

# What are code components

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Code components are a type of solution components, which means they can be included in a solution file and installed in different environments. More information: [Package and distribute extensions using solutions](https://docs.microsoft.com/dynamics365/customer-engagement/developer/package-distribute-extensions-use-solutions).

You add code components by including them in a solution and then importing it into Common Data Service. Once they are in Common Data Service, system administrator and system customizers can configure on fields, sub-grids, views, and dashboard sub-grids to use them in place of default component.  You can also add these code components in canvas apps. 

Code components are comprised of three components:

1. [Manifest](#manifest)
2. [Component implementation library](#component-implementation-library)
3. [Resources](#resources)

## Manifest

Manifest is the metadata file that defines a component. It is an XML document that describes:

- The namespace and name of the component.
- The kind of data it can be configured, either a field or a data-set.
- Any properties that can be configured in the application when the component is added.
- A list of resource files that the component needs. 
- The name of the TypeScript function in the component implementation library that returns an object that applies the required component interface.

When someone configures a component in the application, the data in the manifest filters out available component so that only valid component for the context are available for configuration. The properties defined in the manifest for a component are rendered as configuration fields so that the person configuring the component can specify values. These property values are then available to your component function at run time. More information: [Manifest file reference](manifest-schema-reference/index.md)

## Component implementation library

[!INCLUDE [component-implementation-library](control-implementation-library.md)]

### Page load

When the page loads, the application requires an object to work. Using the data from the manifest, the code gets the object by calling

```js
var obj =  new ["namespace on manifest"].["constructor on manifest"]();
```

If the namespace and constructor values from the manifest were `MyNameSpace` and `LinearInputControl` respectively, the code to instantiate the object would be this:

```js
var controlObj = new MyNameSpace.LinearInputControl();
```

When the page is ready, it initializes the component by calling the [init](reference/control/init.md) function with a set of parameters.

```js
controlObj.init(context,notifyOutputChanged,state,container);
```

|Parameter|Description|
|---|---|
|context| Contains all the information about how the component is configured and all the parameters that can be used within the component along with the [framework APIs](reference/index.md). For example, the `context.parameters.["property name from manifest"]` can be used to access the input property.|
|notifyOutputChanged |Alerts the framework whenever the code component has new outputs ready to be retrieved asynchronously.|
|state|Contains component data from the previous page load in the current session if component explicitly stored it earlier using `setControlState API`.|
|container|An HTML div element to which you can append the HTML elements for the UI that defines your component. To display the value in the UI, you must get the data from `context.parameters.controlValue object`.|

### User changes data

After the page loads, the component displays the data until the user interacts with the component to change the data. When this occurs, you can manage it any way you like, but you must call the function passed in as **notifyOutputChanged** parameter in the [init](reference/control/init.md) function. When you use this method, the platform then responds by calling the [getOutputs](reference/control/getoutputs.md) method. The [getOutputs](reference/control/getoutputs.md) method returns values that has the changes user had made. For a field component, this would typically be the new value for the component.

### App changes data

If the platform changes the data, it calls out the [updateView](reference/control/updateview.md) method of the component and passes a new context object as a parameter. This method  should be implemented and use it to update the values displayed in the component.

### Page close

Whenever a user goes away from the page, code component loses the scope and all the memory allocated in that page for the objects in the component will be cleared. However, some methods based on the browser implementation mechanism might stay and consume memory. Typically, these are event handlers. If the user wants to store the information, they should implement the `setControlState` method so that the information is given next time within the same session.

Developers should implement the [destroy](reference/control/destroy.md) method which is called when the page closes, and use it to remove any cleanup code such as removing any event handlers.

## Resources

Each code component should have a resource file to construct its visualization. You can define a resource file in the manifest. The resource node in the manifest file refers to the resources that the component requires to implement its visualization. More information: [Resources](manifest-schema-reference/resources.md)

### Related topics

[Create code components](create-custom-controls-using-pcf.md)
