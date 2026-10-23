---
title: "Dataverse action and function methods for generative pages"
description: "Learn how to use the dataApi action and function methods in generative pages."
ms.date: 10/19/2026
author: jasongre
ms.author: jasongre
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
  - ruxyrezidenttm
ai-usage: ai-assisted
---
# Dataverse action and function methods for generative pages

Use the action and function methods of the `dataApi` object to invoke [Dataverse custom APIs](../../../data-platform/custom-api.md) bound to the page.

> [!NOTE]
> Action and function methods are optional in the shared `dataApi` contract. Some hosts don't implement them, so check that a method exists before calling it. A method being present doesn't mean the operation is bound to the page, enabled for the runtime, or permitted for the current user. Unlike connector methods, these methods never throw for expected failures; they resolve with `ok: false` and an error code instead. Handle the result's `ok` and `error` properties explicitly.
>
> `listBoundActions` returns the actions and functions the current runtime configuration allows for the page when that discovery is enabled; it isn't a guarantee that the current user holds the Dataverse privileges needed to execute every listed operation.

|Method|Description|
|---|---|
|[`executeAction`](#executeaction-method)|Invokes a Dataverse custom API bound to the page as an action.|
|[`executeFunction`](#executefunction-method)|Invokes a Dataverse custom API bound to the page as a function.|
|[`listBoundActions`](#listboundactions-method)|Lists the Dataverse custom APIs (actions and functions) bound to the page.|

## `executeAction` method

Invokes a Dataverse custom API that a maker bound to the page as an action (a message that might change data).

### Parameters

Set a value for this required parameter.

| Name | Type | Description |
|------|------|-------------|
| `request` | [DataverseActionRequest](#dataverseactionrequest) | The action to invoke and its input parameters. |

#### DataverseActionRequest

| Name | Type | Description |
|------|------|-------------|
| `name` | `string` | The unique name of the custom API, publisher-prefixed, such as `new_ApproveExpenseReport`. |
| `parameters` | `object` | (Optional) The input parameters required by the action, keyed by parameter unique name. |
| `boundTo` | `object` | (Optional) A target row reference (`entityName` and `id`) for entity-bound actions. Omit for global (unbound) actions. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing a [DataverseActionResult](#dataverseactionresult). This method never throws for expected failures (such as a 403 permission error, a 400 bad parameter, or the operation not being bound or enabled) — check the `ok` property instead.

#### DataverseActionResult

| Name | Type | Description |
|------|------|-------------|
| `ok` | `boolean` | Indicates whether the action succeeded. |
| `status` | `number` | The HTTP status code returned by Dataverse, or `0` when no HTTP status is available. A `0` status can mean the runtime rejected the call before sending it (for example, `not_enabled`, `not_bound`, `not_permitted`, `wrong_operation_kind`, `invalid_parameter`, or `invalid_bound_to`), the request failed without an HTTP response, or the outcome is unknown (`indeterminate` is `true`). Use `error.code` and `indeterminate` to tell these cases apart. |
| `outputs` | `object` | The output parameters returned by the action, keyed by unique name. Empty for actions with no outputs. |
| `indeterminate` | `boolean` | (Optional) `true` when a timeout or other post-dispatch failure means the server might have committed the action; don't automatically retry. |
| `error` | `object` | (Optional) Error details when `ok` is `false`, including a machine-readable `code` and a sanitized `message`. `code` is one of `not_enabled`, `not_bound`, `not_permitted`, `wrong_operation_kind`, `invalid_parameter`, `invalid_bound_to`, `indeterminate`, or `network`, or the action's HTTP status code as a string (for example, `"404"`) when Dataverse returned an error response, or `"0"` when no HTTP status was available. `not_permitted` means the action or function isn't on the environment's allow list for generative pages — it doesn't indicate whether the current user holds the Dataverse privileges to run it. A privilege failure typically surfaces as `status: 403` with error code `"403"`; if the host can't determine the HTTP status, it returns `status: 0` instead. |

### executeAction example

```typescript
if (!dataApi.executeAction) {
  throw new Error("executeAction isn't available on this page.");
}

const result = await dataApi.executeAction({
  name: "new_ApproveExpenseReport",
  parameters: { comments: "Approved by manager" },
  boundTo: { entityName: "new_expensereport", id: "30dc51e9-947d-47d8-ad48-4fc48fba4a95" },
});

if (result.ok) {
  console.log(result.outputs);
}
else {
  console.log(result.error?.code);
}
```

## `executeFunction` method

Invokes a Dataverse custom API that a maker bound to the page as a function (a read-only message with GET semantics).

### Parameters

Set a value for this required parameter.

| Name | Type | Description |
|------|------|-------------|
| `request` | [DataverseFunctionRequest](#dataversefunctionrequest) | The function to invoke and its input parameters. |

#### DataverseFunctionRequest

| Name | Type | Description |
|------|------|-------------|
| `name` | `string` | The unique name of the custom API, publisher-prefixed, such as `new_GetExchangeRate`. |
| `parameters` | `object` | (Optional) The input parameters required by the function, keyed by parameter unique name. |
| `boundTo` | `object` | (Optional) A target row reference (`entityName` and `id`) for entity-bound functions. Omit for global (unbound) functions. |

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing a [DataverseActionResult](#dataverseactionresult). As with `executeAction`, this method never throws for expected failures — check the `ok` property instead.

### executeFunction example

```typescript
if (!dataApi.executeFunction) {
  throw new Error("executeFunction isn't available on this page.");
}

const result = await dataApi.executeFunction({
  name: "new_GetExchangeRate",
  parameters: { currencyCode: "EUR" },
});

if (result.ok) {
  console.log(result.outputs);
}
```

## `listBoundActions` method

Lists the Dataverse custom APIs (actions and functions) that a maker bound to the page.

### Parameters

None.

### Returns

A [promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) containing an array of [DataverseActionInfo](#dataverseactioninfo) entries. Returns an empty array when discovery isn't enabled for the runtime.

#### DataverseActionInfo

`DataverseActionInfo` reflects what the page's maker bound for this action or function, not live Dataverse metadata. Don't use it to build input forms or validate outputs — verify parameter requirements and output shapes against the actual Dataverse custom API definition.

| Name | Type | Description |
|------|------|-------------|
| `name` | `string` | The unique (logical) name of the Dataverse custom API. |
| `displayName` | `string` | The display name of a custom API. |
| `isFunction` | `boolean` | `true` if the Dataverse custom API is a function (read-only); `false` if it's an action, including when this value wasn't recorded at binding time. |
| `bindingType` | `string` | The binding type: `"Global"` or `"Entity"`. |
| `boundEntityLogicalName` | `string` | (Optional) The table the action or function is bound to, when `bindingType` is `"Entity"`. |
| `parameters` | `Object[]` | The input parameters recorded when the Dataverse custom API was bound to the page, each with a `name` and `declaredKind`. `type` is always `"unknown"` and `optional` is always `false` — neither reflects the Dataverse custom API's actual metadata. |
| `outputs` | `Object[]` | Always an empty array. Binding discovery doesn't record output parameters. |

### `listBoundActions` example

```typescript
const actions = await dataApi.listBoundActions?.();
```
