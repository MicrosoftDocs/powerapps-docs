---
title: Define Events
description: Explains how to define new events with PowerApps Component Framework (PCF) controls.
author: anuitz
ms.author: anuitz
ms.date: 02/05/2025
ms.reviewer: jdaly
ms.topic: article
ms.subservice: pcf
contributors:
 - JimDaly
---
# Define Events

A common requirement when building custom components with the Power Apps Component Framework is the ability to react to events generated within the control. These events can be invoked either due to user interaction or programmatically via code. For example, an application can have a code component that lets a user build a product bundle and this component can also raise an event which could show product information in another area of the application.

## Component Data Flow

The common data flow for a code component is data flowing from the hosting application into the control as inputs and updated data flowing out of the control to the hosting form or page.

:::image type="content" source="media/component-events-onchange-example.png" alt-text="Shows that data update from the code component to the binding field would cause OnChange event to be triggered":::

The diagram above shows the standard pattern of data flow for a typical PCF component, such that that the data update from the code component to the bound field would cause `OnChange` event to be triggered. For most of component scenarios this suffices and makers just add a handler to trigger subsequent actions. However, there are cases when a more complicated control requires events to be raised which are not the field updates. The new event mechanism allows a code components to define events which can have separate event handlers. 

## Using events

The event mechanism in PCF is based on the standard event model in JavaScript. The component can define events in the manifest file and raise these events in the code. The hosting application can then listen to these events and react to them. 

To do this the component needs to define the [Events](reference/events.md) in the manifest file which will allow these to be reacted to depending on the hosting application (Canvas or Model-driven app).

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
This will allow the canvas app to react to the custom event by adding pfx

:::image type="content" source="media\custom-events-in-canvas-designer.png" alt-text="Shows the custom events in the canvas apps designer":::

or for Model Driven Apps for event handlers to be added to react to the events

```js
  const controlName1 = "cr116_personid";

  this.onLoad = function (executionContext) {
    const formContext = executionContext.getFormContext();

    const sampleControl1 = formContext.getControl(controlName1);
    sampleControl1.addEventHandler("customEvent1", this.onSampleControl1CustomEvent1);
    sampleControl1.addEventHandler("customEvent2", this.onSampleControl1CustomEvent2);
  }
```
> [!NOTE]
> These the events are treated separately for each instance of the control added to the Canvas App Page or Model-driven App Form

## Passing payload in events

For Model Driven Applications there is the additional ability to pass a payload with the event allowing for more complex scenarios for example in the diagram below the component passes a call back function in the event allowing the script handling to call back to the component.

:::image type="content" source="media/passing-payload-in-events.png" alt-text="TODO Explain this diagram":::
<!-- See source \media\src\pcf_events_dependencies_diagrams.vsdx -->

```js
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

[Tutorial: Define a custom event in a component](tutorial-define-event.md)   
[Events](reference/events.md)   
