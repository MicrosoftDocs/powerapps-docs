---
title: Build business logic 
description: Build business logic in Power Apps.
author: lancedMicrosoft 
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 10/22/2024
ms.subservice: canvas-maker
ms.author: lanced
search.audienceType: 
  - maker
contributors:
  - mduelae
  - benapple
  - gregli-msft
  - lancedMicrosoft 
---

# Build business logic

Power Platform offers various capabilities for makers to build business logic for Power Apps. In this article, you find an overview of the key methods and offer guidance to help determine the most suitable approach building business logic for Power Apps.

## Use Power Fx in your app

Power Fx is the low code functional programming language shared by Excel and Power Platform. When used with Power Platform connectors, makers can access data and create custom app logic. Power Fx supports the following characteristics:

- **Live** – Canvas apps recalculate just as Excel spreadsheets do. As users interact with the app, Power Fx is in the background making data requests and keeping the state of the app up to date with Dataverse.

- **Delegation** – Power Fx optimizes data handling by delegating operations to the server whenever possible. Functions like [Filter()](/power-platform/power-fx/reference/function-filter-lookup), [Lookup()](/power-platform/power-fx/reference/function-filter-lookup), and [Search()](/power-platform/power-fx/reference/function-filter-lookup) enable server-side data filtering, ensuring that only the necessary data is retrieved to support the app's functionality and user experience. In cases where delegation isn't possible, functions run locally within the JavaScript environment of the browser.

- **Optimized for Dataverse** – Dataverse serves as the primary data storage option for Power Apps, offering direct, and low-latency access due to fewer intermediary layers. Power Fx is also compatible with Dataverse's diverse relationship types, including many-to-one and one-to-many associations.

- **Offline** – The [Power Apps mobile app](../../mobile/canvas-mobile-offline-overview.md) enables offline use of Dataverse data, allowing users to use the app in the field allowing a seamless connection. Any changes made offline are synchronized when internet connection is available. The app's predefined business logic remains operational, even without an internet connection.

## Use cloud flows in your app

Power Automate is a low code workflow service built on top of the Power Platform connector ecosystem. Power Automate adds the following capabilities when building Power Apps:

- **Asynchronous** – A Power Automate cloud flow is inherently asynchronous. This means that when a flow is initiated, it's using a queuing system to manage the various subtasks. The asynchronous nature of Power Automate means makes it well-suited for longer running complex sequences of logic.

- **Detailed logging** – All flows create a record of what happened when they executed in the form of [Run History](/power-automate/dataverse/cloud-flow-run-metadata) providing traceability and ensuring auditing record for what happened and why.

- **Multi-connector** – Although it's possible to create multi-connector Power Apps logic, due to the live nature of Power Apps, as you increase the number of connectors performance degrades. These complex multi-connector scenarios are a great place to use Power Automate which can offload these cases from live execution in the app.

## Choose between Power Fx and cloud flows for your app

We recommend using Power Fx for developing business logic in Power Apps. While it's a powerful tool, there are scenarios where integrating other tools might be more appropriate.

### Low latency use cases

Power Fx excels in delivering low latency for Power Apps, making it the go to choice for developing responsive business logic. However, the actual latency experienced can vary based on the complexity of the operations and the volume of data being processed. It's crucial to understand that while Power Fx can facilitate swift interactions, the design, and objectives of your application play a pivotal role in its overall performance. For more information, see [performance and optimization articles](create-performant-apps-overview.md) earlier in this section.

When it comes to accessing data efficiently, the combination of Dataverse and Power Fx offers the quickest solution.

For more information, see [Data call flow with Microsoft Dataverse](execution-phases-data-flow.md?#data-call-flow-with-microsoft-dataverse).

### Complex sequences and use of multiple connectors

When dealing with complex sequences of action that span various connectors, Power Automate serves as an effective asynchronous solution to delegate processing away from Power Apps. This asynchronous capability lets Power Apps kick off a workflow and proceed with other tasks without having to pause for a response.

## Design app experience around inherent task latency

When designing user experiences, it's essential to consider the latency that comes with executing complex tasks.

There are two strategies:

1. Pause the user experience until the task finishes, providing a visual indicator of progress.

2. Offload the complex task to Power Automate, allowing the user experience to continue uninterrupted.

## Related content

[Overview of creating performant apps](create-performant-apps-overview.md)
