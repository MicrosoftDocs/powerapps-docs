---
title: "Interact with HTTP and HTTPS resources asynchronously | MicrosoftDocs"
description: "You should interact with HTTP and HTTPS resources asynchronously when writing JavaScript client extensions for model driven apps."
services: ''
suite: powerapps
documentationcenter: na
author: jowells
manager: austinj
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 02/20/2018
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Interact with HTTP and HTTPS resources asynchronously

**Category**: Performance

**Impact potential**: High

<a name='symptoms'></a>

## Symptoms

Synchronous requests block the execution of other scripts, which can cause the following:

- Unresponsive model-driven and canvas apps
- Slow client interactions

<a name='guidance'></a>

## Guidance

Interact asynchronously with HTTP and HTTPS resources whenever possible. Users should notice improvements in the actual page load time or the perceived speed of the page load. The responsiveness of the page should also increase.

The following options are available in modern browsers for interacting with services asynchronously.

> [!NOTE]
> Adding asynchronous interactions requires a different style of design than synchronous interactions. Callbacks can execute in a non-deterministic order, which means you must give more thought to ensure that the page flow and integrity are correct at all times. For example, you'll often need to put measures in place to ensure that controls aren't enabled until all dependent service calls have returned. Taking a few additional steps can help ensure a more enjoyable user experience.

- Traditionally, ribbon rules were written with synchronous requests since true/false needed to be returned. Unified Interface supports returning a promise rather than a boolean, which allows ribbon rules to issue asynchronous network requests. For more information, see [Define ribbon enable rules](../../define-ribbon-enable-rules.md#custom-rule).

- [`XMLHttpRequest`](https://developer.mozilla.org/docs/Web/API/XMLHttpRequest) with the async parameter omitted or set to true

  ```javascript
  // Missing the async parameter, which is the third parameter. It defaults to true, which is the value you want.
  var requestXhr = new XMLHttpRequest();
  requestXhr.open('GET', '/test/test.txt');

  // Explicitly setting the async parameter.
  requestXhr.open('GET', '/test/test.txt', true);
  ```

- [Fetch](https://developer.mozilla.org/docs/Web/API/Fetch_API) API usage

  > [!IMPORTANT]
  > Before proceeding with this option, ensure that support is available for the browsers that are being used to interact with your customizations. Review the [Fetch](https://developer.mozilla.org/docs/Web/API/Fetch_API) documentation's **Browser compatibility** section.

<a name='problem'></a>

## Problematic patterns

There are multiple ways to interact with the server or request resources. Common approaches that allow for synchronous communications include the following:

> [!WARNING]
> These scenarios should be avoided.

- Usage of the `XMLHttpRequest` object passing in `false` for the value of the `async` parameter for the `open` function call

  ```javascript
  var requestXhr = new XMLHttpRequest();

  // Explicitly setting the async parameter to false or supplying a variable with a value of false will force this as a synchronous call.
  requestXhr.open('GET', '/test/test.txt', false);
  ```

- Usage of the [`jQuery`](https://www.jquery.com) [`ajax` function](https://api.jquery.com/jquery.ajax/), passing in `false` for the value of the `async` parameter

  ```javascript
  // Explicitly setting the async parameter to false or supplying a variable with a value of false will force this as a synchronous call.
  var requestAjax = $.ajax({ async: false, url: '/test/test.txt' });
  ```

- Specific to interactions with the Dynamics 365 services, there are JavaScript libraries that provide explicit operations for common interactions with the product. Common libraries include (but aren't limited to): [`SDK.REST.js`](/previous-versions/dynamicscrm-2015/developers-guide/gg334427(v=crm.7)#BKMK_SDKREST), [`SDK.Soap.js`](https://code.msdn.microsoft.com/sdksoapjs-9b51b99a) and [`XrmServiceToolkit.js`](https://github.com/XrmServiceToolkit/XrmServiceToolkit).
  - For these, there are some functions that only support synchronous operations; others require passing in a callback function as a parameter to set async to true. The default behavior for most is to set the underlying async parameter to false for the open call of the `XMLHttpRequest` object.

<a name='additional'></a>

## Additional information

### Performance

A browser interprets script on a single thread. If that thread is being used to execute a process synchronously, the browser will stop responding to the user's interactions ("freeze") while it waits for the process to be completed. Synchronous calls also remove the ability to perform more than one interaction simultaneously, forcing all calls to be serial in nature. In many cases, this leads to the frustration of your users. Optimize user responsiveness by incorporating asynchronous service calls.

### Browser support

The specification for `XMLHttpRequest` states that synchronous usage is being removed from the standard because it's now deprecated. Currently, browsers are only presenting warnings, but an `InvalidAccessError` exception might be thrown in the future when a value of false is passed to the async parameter. Modern browsers have declared synchronous requests executed on the main thread as deprecated.

> [!NOTE]
> Modern APIs are being introduced that will no longer provide an option for synchronous operations. Refer to documentation of the [Fetch API](https://developer.mozilla.org/docs/Web/API/Fetch_API) for more details.

### window.setTimeout

Although including script blocks as a parameter to the `window.setTimeout` function does break the normal synchronous flow of the page execution, it doesn't accomplish parallel processing.

```javascript
window.setTimeout(
    function () {
        var oReq = new XMLHttpRequest();
        oReq.open('GET', '/test/action', false);
    }, 0);
```

The approach in this example still processes on the main browser UI thread, locking the browser.

<a name='seealso'></a>

### See also

[Define ribbon enable rules](../../define-ribbon-enable-rules.md#custom-rule)
[XMLHttpRequest](/microsoft-edge/dev-guide/performance/xmlhttprequest)<br />
[XMLHttpRequest specification (with synchronous deprecation statement)](https://xhr.spec.whatwg.org/#the-open()-method)<br />
[Fetch API specification](https://fetch.spec.whatwg.org/#fetch-api)<br />
[Fetch API](https://developer.mozilla.org/docs/Web/API/Fetch_API)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]