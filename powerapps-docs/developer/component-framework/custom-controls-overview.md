---
title: Code Components
description: "Explore code components in the Power Apps component framework to build enhanced data experiences for model-driven apps, canvas apps, and Power Pages."
author: anuitz
ms.author: anuitz
ms.date: 08/25/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: pcf
contributors:
 - JimDaly
---

# Code components

Code components are solution components that you can package in a solution file and import into different environments. Use them to distribute enhanced app experiences across environments. [Learn how to package and distribute extensions using solutions](/power-platform/alm/solution-concepts-alm).

:::image type="content" source="media/code-components.gif" alt-text="Screenshot of a code component that lets users view and work with app data.":::

You can include code components in a solution and then import the solution into a Microsoft Dataverse environment. After you import the solution containing code components, system administrators and system customizers can configure columns, subgrids, views, and dashboard subgrids to use instead of default components. You can add these code components to both **model-driven and canvas apps**. 

Code components consist of three elements:

- [Manifest](#manifest)
- [Component implementation](#component-implementation)
- [Resources](#resources)

> [!NOTE]
> The definition and implementation of code components by using Power Apps component framework is the same for both model-driven and canvas apps. The only difference between both apps is the configuration part. 

## Manifest

The manifest is the `ControlManifest.Input.xml` metadata file that defines a component. It's an XML document that describes:

- The name of the component.
- The kind of data that you can configure, either a `field` or a `dataset`.
- Any properties that you can configure in the application when you add the component.
- A list of resource files that the component needs.

When a user configures a code component, the data in the manifest file filters the available components so that only valid components for the context are available for configuration. The properties defined in the manifest file for a component render as configuration columns so that the user configuring the component can specify the values. These property values are then available to the component at runtime. For more information, see [Manifest schema reference](manifest-schema-reference/index.md).

## Component implementation

Use TypeScript to implement code components. Each code component must include an object that implements the methods described in the code component interface. The [Power Platform CLI](/power-platform/developer/cli/introduction) auto-generates an `index.ts` file that includes stubbed implementations for these methods. Use the [pac pcf init](/power-platform/developer/cli/reference/pcf#pac-pcf-init) command to generate this file, which includes main stub methods.

The object implements the following methods:

- [init](reference/control/init.md) (Required)
- [updateView](reference/control/updateview.md) (Required)
- [getOutputs](reference/control/getoutputs.md) (Optional)
- [destroy](reference/control/destroy.md) (Required)

These methods control the lifecycle of the code component.

### Page load

When the page loads, the application needs an object to work with. Using the data from the manifest file, the code gets the object by calling:

```js
var obj =  new <"namespace on manifest">.<"constructor on manifest">();
```

If the namespace and constructor values from the manifest are `SampleNameSpace` and `LinearInputComponent` respectively, the code to instantiate the object looks like this:

```js
var controlObj = new SampleNameSpace.LinearInputComponent();
```

When the page is ready, it initializes the component by calling the [init](reference/control/init.md) method with a set of parameters.

```js
controlObj.init(context,notifyOutputChanged,state,container);
```

|Parameter|Description|
|---|---|
| context | Contains all the information about how the component is configured and all the parameters that you can use within the component along with the [Power Apps component framework APIs](reference/index.md). For example, use `context.parameters.<"property name from manifest">` to access the input property. |
| notifyOutputChanged | Alerts the framework whenever the code component has new outputs ready to be retrieved asynchronously. |
| state | Contains component data from the previous page load in the current session if the component explicitly stored it earlier by using the [setControlState](reference/mode/setcontrolstate.md) method. |
| container | An HTML div element to which developers and app makers can append the HTML elements for the UI that defines the component. |

### User changes data

When a user interacts with your components to change data, your component must call the method passed in as *notifyOutputChanged* parameter in the [init](reference/control/init.md) method. When you use this method, the platform responds by calling the [getOutputs](reference/control/getoutputs.md) method. The [getOutputs](reference/control/getoutputs.md) method returns values that include the changes made by the user. For a `field` component, this value is typically the new value for the component.

### App changes data

If the platform changes the data, it calls the [updateView](reference/control/updateview.md) method of the component and passes the new context object as a parameter. Implement this method to update the values displayed in the component.

### Page close

When a user steps away from the page, the code component loses the scope and clears all the memory allocated in that page for the objects. However, some methods might stay and consume memory, based on the browser implementation mechanism. Typically, these methods are event handlers. If the user wants to store this information, they should implement the [setControlState](reference/mode/setcontrolstate.md) method so that the information is available next time within the same session.

Developers should implement the [destroy](reference/control/destroy.md) method, which is called when the page closes, to remove any cleanup code such as event handlers.

## Resources

The resource node in the manifest file refers to the resources that the component requires to implement its visualization. Each code component must have a resource file to construct its visualization. The tooling generates the `index.ts` file as a `code` resource. There must be at least one code resource.

Define additional resource files in the manifest to include:

- CSS files
- image web resources
- resx web resources for localization

 More information: [resources element](manifest-schema-reference/resources.md)

### Related articles

[Create and build a code component](create-custom-controls-using-pcf.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
