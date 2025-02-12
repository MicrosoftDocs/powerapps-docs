---
title: "Tutorial: Define a custom event in a component"
description: "In this tutorial, learn how to define a custom event in a PCF control and use it in canvas and model-driven apps."
author: anuitz
ms.author: anuitz
ms.date: 02/05/2025
ms.reviewer: jdaly
ms.topic: tutorial
ms.subservice: pcf
contributors:
 - JimDaly
---
# Tutorial: Define a custom event in a component

This tutorial shows how to build a code component with two buttons which each raise separate independent events which the hosting application will react to. You can add these to canvas & model-driven apps and show how these events can be utilized to perform actions like updating a field or showing a notification message. [Learn more about custom events](events.md).

:::image type="content" source="media/define-custom-event-tutorial-diagram.png" alt-text="Diagram shows the goal of this sample to define two custom events":::
<!-- See source in media/src/define-custom-event-tutorial-diagram.vdx -->

## Goal

When you complete the steps in this tutorial you will understand how to create a code component that defines custom events and also how to use the events in a canvas and model-driven app.

Canvas App

<video controls src="media/event_canvas_example.mp4" title="Events in a Canvas App"></video>

Model-driven App

<video controls src="media/event_mda_example.mp4" title="Events in a Model Driven App"></video>

## Prerequisites

You should be with familiar with the following:-

[Create and build a code component](create-custom-controls-using-pcf.md)
[Package a code component](import-custom-controls.md)
[Add code components to a model-driven app](add-custom-controls-to-a-field-or-entity.md#add-a-code-component-to-a-column)
[Add cpmponents to a canvas app](component-framework-for-canvas-apps.md#add-components-to-a-canvas-app)

## Create a new Control

<!-- 
We don't want long set of numbered instructions. Since this entire article is a tutorial, break the steps down into logical parts and give each part a heading 

-->

1. Create a new component using this command:

  `pac pcf init -n EventSample -ns SampleNamespace -t field -fw react -npm`

1. Edit the manifest to add the new events

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
<event name="customEvent1"
   display-name-key="customEvent1"
   description-key="customEvent1"/>
<event name="customEvent2"
   display-name-key="customEvent2"
   description-key="customEvent2"/>
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

---

## Define events

In the control file `EventSample\HelloWorld.tsx`, define two events in the interface and bind the events to two different buttons. Also update the import to include `DefaultButton` as shown below.

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

// this component renders two buttons each one will trigger an event passed via props

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

Now modify the `EventSample\Index.ts`, modify updateView method to add handlers for the two button events. This will add the two events defined in the manifest to the events in the context passed to the control.

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

[Create and build a code component](create-custom-controls-using-pcf.md)
[Package a code component](import-custom-controls.md)

## Use in a canvas app

1. First step
1. Second step
1. Third step

## Use in a model-driven app


> [!NOTE]
> These steps refer to instructions described in [Walkthrough: Write your first client script](../model-driven-apps/clientapi/walkthrough-write-your-first-client-script.md).

1. [Upload your code as a web resource](../model-driven-apps/clientapi/walkthrough-write-your-first-client-script.md#step-3-upload-your-code-as-a-web-resource)
1. [Add the component](code-components-model-driven-apps.md#add-code-components-to-model-driven-apps) to the model-driven form.
1. [Associate](../model-driven-apps/clientapi/walkthrough-write-your-first-client-script.md#step-4-associate-your-web-resource-to-a-form) the Web resource to the Form
1. [Configure](../model-driven-apps/clientapi/walkthrough-write-your-first-client-script.md#configure-form-on-load-event) the On load event.


## Passing payload in events

As described in [Passing payload in events](events.md#passing-payload-in-events), you can pass payload in events. You can modify this example in the following way to achieve this.


:::image type="content" source="media/passing-payload-in-events.png" alt-text="TODO Explain this diagram":::
<!-- See source media/src/passing-payload-in-events.vsdx -->


1. First step
1. Second step
1. Third step