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

A common requirement when building custom components with the Power Apps Component Framework is the ability to react to events generated within the control. These events can be invoked either due to user interaction or programmatically via code. For example, an application can have a code component that lets a user build a product bundle and this component can also raise an event which could show product information in another area of the application. In this article we will look at how to build a code component that defines events, raises them and have the hosting application react to them.

## Component Data Flow

The common data flow for a code component is data flowing from the hosting application into the control as inputs and updated data flowing out of the control to the hosting form or page.

:::image type="content" source="media/component-events-onchange-example.png" alt-text="Shows that data update from the code component to the binding field would cause OnChange event to be triggered":::

Diagram above shows that data update from the code component to the binding field would cause `OnChange` event to be triggered. For most of component scenarios this suffices and makers just add a handler to trigger subsequent actions. However, there are cases when a more complicated control requires events to be raised which are not the field updates. The new event mechanism allows a code components to define events which can have separate event handlers. 

## Passing payload in events

TODO: There were some concepts demonstrated in the example, such as passing payload in events. These should be explained here. Never explain concepts in a tutorial.

:::image type="content" source="media/passing-payload-in-events.png" alt-text="TODO Explain this diagram":::
<!-- See source media/src/passing-payload-in-events.vsdx -->

[Tutorial: Define a custom event in a component](tutorial-define-event.md)   
[Events](reference/events.md)