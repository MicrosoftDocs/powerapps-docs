---
title: Manifest | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 31af2963-b4ca-4347-98f6-4a3f6277f43a

---
Manifest is the metadata file that defines a component. It is an `XML` document that describes:

- The namespace of the component.
- The kind of data it can be bound to, either a field or a data-set.
- Any properties that can be configured in the application when the component is added.
- A list of web resource files that the component needs. 
  - One of them must be a JavaScript web resource. This JavaScript must include a function that will instantiate an object. This implements an interface that exposes methods that are required for the component to work. This is called the component implementation library.
- The name of a JavaScript function in the component implementation library that will return an object that applies the required component interface.

When someone configures a component in the application, the data in the manifest will filter out available components so that only valid components for the context are available for configuration. The properties defined in the manifest for a component are rendered as configuration fields so that the person configuring the component can specify values. These property values are then available to your component function at run time.