---
title: "Tutorial: Define a custom event in a component"
description: "In this tutorial, learn how to define a custom event in a PCF control and use it in canvas and model-driven apps."
author: anuitz
ms.author: anuitz
ms.date: 02/14/2025
ms.reviewer: jdaly
ms.topic: tutorial
ms.subservice: pcf
contributors:
 - JimDaly
---
# Tutorial: Define a custom event in a component

In this tutorial, you will build a code component that uses custom events and test it using both canvas and model-driven apps. [Learn more about custom events](events.md).

## Goal

The steps in this tutorial guide you to create a code component with two buttons which raise different events for the hosting application can react to. You will define two events: `customEvent1` and `customEvent2`. Then, the code component will expose two buttons that will cause these events to occur. 

### Canvas App

The canvas app will use Power Fx expressions on these events to toggle the visible and display mode properties of a control:

:::image type="content" source="media/define-custom-event-tutorial-diagram.png" alt-text="Diagram shows the goal of this sample to define two custom events":::
<!-- See source in media/src/define-custom-event-tutorial-diagram.vdx -->

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=9a59542b-cff6-4de5-a347-5da92aae2c9a]

### Model-driven App

The model-driven app will use client-side JavaScript to show an alert when the respective events occur.

**TODO**: add video or images for mda showing final result

## Prerequisites

You should already know how to:

- [Create and build a code component](create-custom-controls-using-pcf.md)
- [Package a code component](import-custom-controls.md)
- [Add code components to a model-driven app](add-custom-controls-to-a-field-or-entity.md#add-a-code-component-to-a-column)
- [Add components to a canvas app](component-framework-for-canvas-apps.md#add-components-to-a-canvas-app)

## Create a new Control

<!-- 
We don't want long set of numbered instructions. Since this entire article is a tutorial, break the steps down into logical parts and give each part a heading 

-->

1. Create a new component using this command:

   `pac pcf init -n EventSample -ns SampleNamespace -t field -fw react -npm`

2. Edit the manifest to add the new events

#### [Before](#tab/before)

<!-- Formatting the XML this way helps make sure it is readable on learn.microsoft.com without having to scroll -->

```xml
<property name="sampleProperty"
   display-name-key="Property_Display_Key"
   description-key="Property_Desc_Key"
   of-type="SingleLine.Text"
   usage="bound"
   required="true" />
<resources>
   <code path="index.ts"
      order="1"/>
   <platform-library name="React"
      version="16.8.6" />
   <platform-library name="Fluent"
      version="8.29.0" />
   <!-- UNCOMMENT TO ADD MORE RESOURCES
   <css path="css/SampleEventPCF.css" order="1" />
   <resx path="strings/SampleEventPCF.1033.resx" version="1.0.0" />
   -->
</resources>
```

#### [After](#tab/after)

```xml
<property name="sampleProperty"
   display-name-key="Property_Display_Key"
   description-key="Property_Desc_Key"
   of-type="SingleLine.Text"
   usage="bound"
   required="true" />
<resources>
   <code path="index.ts"
      order="1"/>
   <platform-library name="React"
      version="16.8.6" />
   <platform-library name="Fluent"
      version="8.29.0" />
   <!-- UNCOMMENT TO ADD MORE RESOURCES
   <css path="css/SampleEventPCF.css" order="1" />
   <resx path="strings/SampleEventPCF.1033.resx" version="1.0.0" />
   -->
</resources>
<event name="customEvent1"
   display-name-key="customEvent1"
   description-key="customEvent1"/>
<event name="customEvent2"
   display-name-key="customEvent2"
   description-key="customEvent2"/>
```

<!-- 
TODO: Is it OK that I've shown the event elements AFTER/BELOW the resources element? It is easier to see the difference this way 
-->

---

## Define events

In the `EventSample\HelloWorld.tsx` control file, define two events in the interface and bind the events to two different buttons. Also update the import to include `DefaultButton` as shown below.

#### [Before](#tab/before)

```typescript
import * as React from 'react';
import { Label } from '@fluentui/react';

export interface IHelloWorldProps {
  name?: string;
}

export class HelloWorld extends React.Component<IHelloWorldProps> {
  public render(): React.ReactNode {
    return (
      <Label>
        {this.props.name}
      </Label>
    )
  }
}
```

#### [After](#tab/after)

```typescript
import * as React from 'react';
import { Label, DefaultButton } from '@fluentui/react';

// This component renders two buttons each one will trigger an event passed via props

export interface IHelloWorldProps {
  onCustomEvent1: () => void;
  onCustomEvent2: () => void;
}

export const HelloWorld: React.FunctionComponent<IHelloWorldProps> = (props: IHelloWorldProps) => {
  return (
    <div>
      <Label>Control with event</Label>
      <DefaultButton onClick={props.onCustomEvent1}>Trigger event 1</DefaultButton>
      <DefaultButton onClick={props.onCustomEvent2}>Trigger event 2</DefaultButton>
    </div>
  );
};
```

---

## Modify updateview method

In `EventSample\Index.ts`, modify [the updateView method ](reference/react-control/updateview.md) to add handlers for the two button events. This will add the two events defined in the manifest to the events in the context passed to the control.

#### [Before](#tab/before)

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): React.ReactElement {
   const props: IHelloWorldProps = { name: 'Hello, World!' };
   return React.createElement(
      HelloWorld, props
   );
}
```

#### [After](#tab/after)

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): React.ReactElement {
   const props: IHelloWorldProps = {
      onCustomEvent1: ()=> {
            context.events.customEvent1()
      },
      onCustomEvent2: () => {
            context.events.customEvent2()
      }
   };
   return React.createElement(
      HelloWorld, props
   );
}
```
---

## Build and package

As usual, you need to complete these steps to use this control:

1. [Create and build the code component](create-custom-controls-using-pcf.md)
1. [Package the code component](import-custom-controls.md)
1. [Deploy the code component](import-custom-controls.md#deploying-code-components)

---

## Use in a canvas app

1. [Create a new blank Canvas App](../../maker/canvas-apps/create-blank-app.md)
1. [Add the new component to the canvas app](component-framework-for-canvas-apps.md#add-components-to-a-canvas-app)
1. [Add a new control](../../maker/canvas-apps/add-configure-controls.md) in this example use a simple text control.

   :::image type="content" source="media/event_canvas_sample_app.png" alt-text="Image of the Canvas App with controls added ":::

1. Add two variables to the app `isVisible` and `canEdit` and set these as the properties `DisplayMode`.

   :::image type="content" source="media/event_canvas_sample_app_displaymode.png" alt-text="Image of the DisplayMode property of the text control":::

   And the `Visible` property of the text control.

   :::image type="content" source="media/event_canvas_sample_app_visible.png" alt-text="Image of the Visible property of the text control":::

1. Set custom actions on the new custom control to update the `isVisible` and `canEdit` variables when the buttons are clicked.

   :::image type="content" source="media/event_canvas_sample_app_customevents.png" alt-text="Image of the Custom Event properties of the new component":::

   |Event|Power FX expression|
   |---|---|
   |customEvent1|`If(isVisible, Set (isVisible, false), Set (isVisible, true))`|
   |customEvent2|`If(canEdit = DisplayMode.Edit, Set(canEdit, DisplayMode.Disabled), Set (canEdit, DisplayMode.Edit))`|

1. Test the Canvas app. When you press `Trigger event 1` the text control should toggle between visible and hidden and when you press `Trigger event 2` the text control should toggle between editable and read only.

## Use in a model-driven app

> [!NOTE]
> These steps refer to instructions described in [Walkthrough: Write your first client script](../model-driven-apps/clientapi/walkthrough-write-your-first-client-script.md).

1. Create a new JavaScript web resource to run on the `onLoad` event of a form. This will bind two simple event handlers to the new events for the controls on load of the form.

   ```javascript
   /* eslint-disable */
   "use strict";

   var MyScriptsNameSpace = window.MyScriptsNameSpace || {};
   (function () {

   const controlName1 = "cr116_personid";

   this.onLoad = function (executionContext) {
      const formContext = executionContext.getFormContext();

      const sampleControl1 = formContext.getControl(controlName1);
      sampleControl1.addEventHandler("customEvent1", this.onSampleControl1CustomEvent1);
      sampleControl1.addEventHandler("customEvent2", this.onSampleControl1CustomEvent2);
   };

   this.onSampleControl1CustomEvent1 = function (params) {
      alert(`SampleControl1 Custom Event 1`);
   }.bind(this);

   this.onSampleControl1CustomEvent2 = function (params) {
      alert(`SampleControl1 Custom Event 2`);
   }.bind(this);

   }).call(MyScriptsNameSpace);
   ```

1. [Upload your new JavaScript file as a web resource](../model-driven-apps/clientapi/walkthrough-write-your-first-client-script.md#step-3-upload-your-code-as-a-web-resource).
1. [Add the component to the model-driven form](code-components-model-driven-apps.md#add-code-components-to-model-driven-apps).
1. [Associate the webresource to the form](../model-driven-apps/clientapi/walkthrough-write-your-first-client-script.md#step-4-associate-your-web-resource-to-a-form).
1. [Configure the On Load event](../model-driven-apps/clientapi/walkthrough-write-your-first-client-script.md#configure-form-on-load-event).

   :::image type="content" source="media/event_mda_sample_jsbinding.png" alt-text="Image of the JavaScript binding for the Model Driven App Form":::

1. Test your app. When you navigate to the form and press **Trigger event 1**, an alert displays `SampleControl1 Custom Event 1`. When you press **Trigger event 2**, an alert displays `SampleControl1 Custom Event 2`.

## Passing payload in events

As described in [Passing payload in events](events.md#passing-payload-in-events), you can pass payload in events in model-driven apps. You can modify this example in the following way to achieve this.

<!-- TODO: I don't fully understand this diagram. Does it need more explanation? -->
:::image type="content" source="media/passing-payload-in-events.png" alt-text="Diagram shows multiple controls generating multiple events with a call back being made":::
<!-- See source media/src/passing-payload-in-events.vsdx -->

### Pass payload with event


Change the `EventSample\index.ts` so that the events will pass a message payload and in the second event also pass a callback function that changes an internal variable

#### [Before](#tab/before)

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): React.ReactElement {
   const props: IHelloWorldProps = {
      onCustomEvent1: ()=> {
            context.events.customEvent1()
      },
      onCustomEvent2: () => {
            context.events.customEvent2()
      }
   };
   return React.createElement(
      HelloWorld, props
   );
}
```

#### [After](#tab/after)

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): React.ReactElement {
   const props: IHelloWorldProps = {
      onCustomEvent1: () => {
            // Trigger event with a string as payload 
            context.events.customEvent1("Hello from event 1")
      },
      onCustomEvent2: () => {
            let defaultPrevented = false;
            // Trigger event with a payload object and a preventDefault function
            context.events.customEvent2({ message: "Hello from event 2", preventDefault: () => { defaultPrevented = true } })

            // Check if the event was prevented
            if (defaultPrevented) {
               alert("Event 2 prevented default!");
            } else {
               alert("Event 2 default NOT prevented");
            }
      }
   };
   return React.createElement(
      HelloWorld, props
   );
}
```

---

Then:

1. [Rebuild and Deploy the component](tutorial-define-event.md#build-and-package).
1. Add another field to the form used [before](tutorial-define-event.md#use-in-a-model-driven-app) and also set that to use the new component.

   :::image type="content" source="media/event_mda_sample_param.png" alt-text="Diagram shows multiple controls added to the form":::

### Use the payload in the event handler

Update the `onLoad` function to set the event handlers on the custom controls to react to events from both controls and also to make use of the parameters being passed

#### [Before](#tab/before)

```javascript
/* eslint-disable */
"use strict";

var MyScriptsNameSpace = window.MyScriptsNameSpace || {};
(function () {

const controlName1 = "cr116_personid";

this.onLoad = function (executionContext) {
   const formContext = executionContext.getFormContext();

   const sampleControl1 = formContext.getControl(controlName1);
   sampleControl1.addEventHandler("customEvent1", this.onSampleControl1CustomEvent1);
   sampleControl1.addEventHandler("customEvent2", this.onSampleControl1CustomEvent2);
};

this.onSampleControl1CustomEvent1 = function (params) {
   alert(`SampleControl1 Custom Event 1`);
}.bind(this);

this.onSampleControl1CustomEvent2 = function (params) {
   alert(`SampleControl1 Custom Event 2`);
}.bind(this);

}).call(MyScriptsNameSpace);
```

#### [After](#tab/after)

```javascript
/* eslint-disable */
"use strict";

var MyScriptsNameSpace = window.MyScriptsNameSpace || {};
(function () {

const controlName1 = "cr116_personid";
const controlName2 = "cr116_haircolor";

this.onLoad = function (executionContext) {
   const formContext = executionContext.getFormContext();

   const sampleControl1 = formContext.getControl(controlName1);
   sampleControl1.addEventHandler("customEvent1", this.onSampleControl1CustomEvent1);
   sampleControl1.addEventHandler("customEvent2", this.onSampleControl1CustomEvent2);

   const sampleControl2 = formContext.getControl(controlName2);
   if (sampleControl2) {
      sampleControl2.addEventHandler("customEvent1", this.onSampleControl2CustomEvent1);
      sampleControl2.addEventHandler("customEvent2", this.onSampleControl2CustomEvent2);
   }
};

this.onSampleControl1CustomEvent1 = function (params) {
   alert(`SampleControl1 Custom Event 1: ${params.message}`);
}.bind(this);

this.onSampleControl1CustomEvent2 = function (params) {
   alert(`SampleControl1 Custom Event 2: ${params.message}`);
}.bind(this);

this.onSampleControl2CustomEvent1 = function (params) {
   alert(`SampleControl2 Custom Event 1: ${params}`);
}

this.onSampleControl2CustomEvent2 = function (params) {
   alert(`SampleControl2 Custom Event 2: ${params.message}`);
   // prevent the default action for the event
   params.preventDefault();
}*/
}).call(MyScriptsNameSpace);
```

---

### Test your app

1. When you navigate to the form and press `Trigger event 1` on the first field a pop up should display `SampleControl1 Custom Event 1: Hello from event 1` and when you press `Trigger event 2` on the first field a pop up should display `SampleControl1 Custom Event 2: Hello from event 2` followed by another alert from the first control saying `Event 2 default NOT prevented`.
1. When you navigate to the form and press `Trigger event 1` on the second field a pop up should display `SampleControl2 Custom Event 1: Hello from event 1` and when you press `Trigger event 2` on the second field a pop up should display `SampleControl2 Custom Event 2: Hello from event 2` followed by another alert from the second control saying `Event 2 default prevented`.


### Related articles

[Define Events](events.md)