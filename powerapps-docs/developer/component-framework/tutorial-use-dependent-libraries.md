---
title: "Tutorial: Use dependent libraries in a component"
description: "In this tutorial, learn how to use dependent libraries with a model-driven app."
author: anuitz
ms.author: anuitz
ms.date: 02/05/2025
ms.reviewer: jdaly
ms.topic: tutorial
ms.subservice: pcf
contributors:
 - JimDaly
---
# Tutorial: Use dependent libraries in a component

This tutorial shows how to build a code component that uses libraries that are defined in another component.
[Learn more about dependent libraries](dependent-libraries.md)

## Goal

When you complete the steps in this tutorial...

<!-- 
Explain the end goal. Don't make them scroll to the bottom to figure out what success will look like.

There appear to be two different scenarios

 -->

## Prerequisites

<!-- Explain what the reader should already have or know before they start this tutorial.  -->

## Dependency as a library in another component

This example uses a library named `myLib-v_0_0_1.js` that has a single `sayHello` function.

```javascript
TODO Add code here
```

You will also need a d.ts file for the the libray. For `myLib-v_0_0_1.js` it might look like this `myLib.d.ts` file:

```typescript
TODO Add code here
```

TODO: I'd like to avoid unnecessary screenshots. If we can describe how to do this without a screenshot, lets do that.

1. Add `myLib-v_0_0_1.js` file to your project
1. Add the `myLib.d.ts` to your project



## Dependency as on demand load of a component
