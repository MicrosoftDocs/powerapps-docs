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

When you complete the steps in this tutorial you will understand how to create a code component that defines custom events and also how to use the events in a canvas and model driven app.

Canvas App

<video controls src="media/event_canvas_example.mp4" title="Events in a Canvas App"></video>

Model Driven App

<video controls src="media/event_mda_example.mp4" title="Events in a Model Driven App"></video>

## Prerequisites

<!-- Explain what the reader should already have or know before they start this tutorial.  -->

## Edit the manifest

<!-- 
We don't want long set of numbered instructions. Since this entire article is a tutorial, break the steps down into logical parts and give each part a heading 

-->

1. Create a new component using this command:

  `pac pcf init -n EventSample -ns SampleNamespace -t field -fw react -npm`

1. Edit the manifest..

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

<!-- 
We never have screenshots of code. You need to add the actual code here.
Consider using the Before & After tabs if the instructions are to modify an existing area.

-->

```typescript
import * as React from 'react';
etc...
```


## Modify updateview method

```typescript
YOUR CODE GOES HERE
etc...
```

## Build and package

1. First step
1. Second step
1. Third step

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