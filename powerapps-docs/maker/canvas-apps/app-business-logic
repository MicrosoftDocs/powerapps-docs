---
title: Guidance for building Power Apps business logic 
description: Guidance for building Power Apps business logic.
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: benapple
ms.date: 07/11/2024
ms.subservice: canvas-maker
ms.author: benapple
search.audienceType: 
  - maker
contributors:
  - mduelae
  - benapple
---

# Guidance for building Power Apps business logic 

There are a range of capabilities available through Power Platform that enable makers to create business logic for Power Apps. The following outline the primary methods along with guidance to determine which one to use:

**Power Apps with Power Fx** – Power Fx is the low code functional programming language shared by Excel and Power Platform. Combined with Power Platform connectors, makers can access data as well as create custom app logic. Power Fx supports the following characteristics:

1. **Live** – Canvas apps "recalc" just as Excel spreadsheets do. As end users interact with the app, Power Fx is in the background making data requests and keeping the state of the app up to date with Dataverse.

2. **Delegation** – Power Fx optimizes data handling by "delegating" operations to the server whenever possible. Functions like Filter(), Lookup(), and Search() enable server-side data filtering, ensuring that only the necessary data is retrieved to support the app's functionality and user experience. In cases where delegation isn't possible, functions run locally within the JavaScript environment of the browser.

3. **Optimized for Dataverse** – Dataverse serves as the primary data storage option for Power Apps, offering direct and low-latency access due to fewer intermediary layers.  Power Fx is also compatible with Dataverse's diverse relationship types, including many-to-one and one-to-many associations.

4. **Offline** – The [Power Apps mobile app](../../mobile/canvas-mobile-offline-overview.md) enables offline use of Dataverse data, allowing users to use the app in the field allowing a seamless connection. Any changes made offline are synchronized when internet connection is available. The app's predefined business logic remains operational, even without an internet connection.


**Power Automate** – A low code workflow service built on top of the Power Platform connector ecosystem. Power Automate adds the following capabilities when building Power Apps:

1. **Asynchronous** – A Power Automate cloud flow is inherently asynchronous. This means that when a flow is initiated, it is leveraging a queuing system to manage the various subtasks. The asynchronous nature of Power Automate means that it is well suited for longer running complex sequences of logic.

2. **Detailed logging** – All flows create a record of what happened when they executed, called the **Run History**. This provides traceability and ensures there's an auditing record for what happened and why.

3. **Multi-connector** – Although it is possible to create multi-connector Power Apps logic, due to the live nature of Power Apps, as you increase the number of connectors performance will degrade. These complex multi-connector scenarios are a great place to leverage Power Automate which can offload these cases from live execution in the app.

## When to use Power Fx vs Power Automate in Power Apps?

**Using Power Fx is the recommended approach for developing business logic in Power Apps**. While it's a powerful tool, there are scenarios where integrating other tools might be more appropriate.

### Low latency use cases

**Power Fx excels in delivering low latency for Power Apps**, making it the go-to choice for developing responsive business logic. However, the actual latency experienced can vary based on the complexity of the operations and the volume of data being processed. It's crucial to understand that while Power Fx can facilitate swift interactions, the design and objectives of your application play a pivotal role in its overall performance. For deeper insights, refer to [Performance considerations with PowerApps](https://powerapps.microsoft.com/en-us/blog/performance-considerations-with-powerapps/).

When it comes to accessing data efficiently, the combination of Dataverse and Power Fx offers the quickest solution.


![](media/image1.png)

### Complex sequences and multi-connector

When dealing with complex sequences of action that span various connectors, **Power Automate serves as an effective asynchronous solution to delegate processing away from the Power App**. This asynchronous capability lets Power Apps kick off a workflow and proceed with other tasks without having to pause for a response.

![A diagram of a software project Description automatically generated](media/image2.png)

&lt;more to add here&gt;

## Designing app experiences around inherent task latency

When designing user experiences, it's essential to consider the latency that comes with executing complex tasks.

There are two strategies:

1. Pause the user experience until the task finishes, providing a visual indicator of progress.

2. Offload the complex task to Power Automate, allowing the user experience to continue uninterrupted.

