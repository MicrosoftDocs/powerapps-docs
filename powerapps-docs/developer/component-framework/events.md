---
title: Define Events (preview)
description: Explains how to define new events with Power Apps Component Framework (PCF) controls.
author: anuitz
ms.author: anuitz
ms.date: 03/24/2025
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: pcf
contributors:
 - JimDaly
 - kierantpetrie
---
# Define Events (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

A common requirement when building custom components with the Power Apps Component Framework is the ability to react to events generated within the control. These events can be invoked either due to user interaction or programmatically via code. For example, an application can have a code component that lets a user build a product bundle. This component can also raise an event which could show product information in another area of the application.

## Component Data Flow

The common data flow for a code component is data flowing from the hosting application into the control as inputs and updated data flowing out of the control to the hosting form or page. This diagram shows the standard pattern of data flow for a typical PCF component:

:::image type="content" source="media/component-events-onchange-example.png" alt-text="Shows that data update from the code component to the binding field triggers the `OnChange` event":::

The data update from the code component to the bound field triggers the `OnChange` event. For most component scenarios, this is enough and makers just add a handler to trigger subsequent actions. However, a more complicated control might require events to be raised that aren't field updates. The event mechanism allows code components to define events that have separate event handlers.

## Using events

The event mechanism in PCF is based on the standard event model in JavaScript. The component can define events in the manifest file and raise these events in the code. The hosting application can listen to these events and react to them.

The component defines events using the [event element](manifest-schema-reference/event.md) in the manifest file. This data allows the respective hosting application to react to events in different ways.

```xml
<property
  name="sampleProperty"
  display-name-key="Property_Display_Key"
  description-key="Property_Desc_Key"
  of-type="SingleLine.Text"
  usage="bound"
  required="true"
/>
<event
  name="customEvent1"
  display-name-key="customEvent1"
  description-key="customEvent1"
/>
<event
  name="customEvent2"
  display-name-key="customEvent2"
  description-key="customEvent2"
/>
```

Canvas apps react to the event using Power Fx expressions:

:::image type="content" source="media\custom-events-in-canvas-designer.png" alt-text="Shows the custom events in the canvas apps designer":::

Model Driven Apps use the [addEventHandler method](../model-driven-apps/clientapi/reference/controls/addeventhandler.md) to associate event handlers to custom events for a component.

```javascript
  const controlName1 = "cr116_personid";

  this.onLoad = function (executionContext) {
    const formContext = executionContext.getFormContext();

    const sampleControl1 = formContext.getControl(controlName1);
    sampleControl1.addEventHandler("customEvent1", this.onSampleControl1CustomEvent1);
    sampleControl1.addEventHandler("customEvent2", this.onSampleControl1CustomEvent2);
  }
```

> [!NOTE]
> These events occur separately for each instance of the code component in the app.

## Defining an event for model-driven apps

For model-driven apps you can pass a payload with the event allowing for more complex scenarios. For example in the diagram below the component passes a callback function in the event allowing the script handling to call back to the component.

:::image type="content" source="media/passing-payload-in-events.png" alt-text="In this example, the component passes a callback function in the event allowing the script handling to call back to the component":::

<!-- See source \media\src\pcf_events_dependencies_diagrams.vsdx -->

```javascript
this.onSampleControl1CustomEvent1 = function (params) {
   //alert(`SampleControl1 Custom Event 1: ${params}`);
   alert(`SampleControl1 Custom Event 1`);
}.bind(this);

this.onSampleControl2CustomEvent2 = function (params) {
alert(`SampleControl2 Custom Event 2: ${params.message}`);
// prevent the default action for the event
params.callBackFunction();
}
```

## Defining an event for canvas apps

Makers configure an event using Power Fx on the PCF control in the properties pane.

### Calling an event

See how to call an event in [Events](reference/events.md).

### Next steps

> [!div class="nextstepaction"]
> [Tutorial: Define a custom event in a component](tutorial-define-event.md)
