## Available for

Model-driven apps, canvas apps, & portals.

## Syntax

`getOutputSchema(context)`

## Remarks

The output will contain JSON schema for each property of type object defined in the manifest. 

For example, if the manifest has an output property of type object called `MyOutputObject`, and your control should return an object like this for value of `MyOutputObject` property: 

```json
{ 
  "ProductName": "sample name", 
  "Value": 123.4 
} 
```

Then you should return:

```json
{ 

  "MyOutputObject": { 
    "$schema": "http://json-schema.org/draft-04/schema#", 
    "type": "object", 
    "properties": { 
      "ProductName": { 
        "type": "string" 
      }, 
      "Value": { 
        "type": "number" 
      } 
    } 
  } 
} 
```

The return schema is a subset of the [JSON schema](https://json-schema.org).
Supported types and keyword for JSON schema:

- `string`
- `integer`
- `number`
- `array`
   - `items`
- `object`
   - `properties`
- `boolean`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|context|[Context](../context.md)|yes|The *Input Properties* containing the parameters, component metadata and interface functions.|


## Example

Control has an object type output property called `MyOutputObject` and the value looks like this:

```json
{ 
  id: 10, 
  productDetails: { 
    name: "Test Product", 
    price: 100.23, 
  }, 
  itemList: [ 
    { 
      itemId: 1, 
      name: "Item-1", 
      value: 123, 
      active: true, 
    }, 
    { 
      itemId: 2, 
      name: "Item-2", 
      value: 234, 
      active: false, 
    } 
  ] 
}; 
```

`GetOutputSchema` implementation:

```typescript
public async getOutputSchema(context: ComponentFramework.Context<IInputs>): 
Promise<Record<string, unknown>> { 
  return Promise.resolve({ 
    MyOutputObject: { 
      "$schema": "http://json-schema.org/draft-04/schema#", 
      "type": "object", 
      "properties": { 
        "id": { 
          "type": "integer" 
        }, 
        "productDetails": { 
          "type": "object", 
          "properties": { 
            "name": { 
              "type": "string" 
            }, 
            "price": { 
              "type": "number" 
            } 
          } 
        }, 
        "itemList": { 
          "type": "array", 
          "items": 
          { 
            "type": "object", 
            "properties": { 
              "itemId": { 
                "type": "integer" 
              }, 
              "name": { 
                "type": "string" 
              }, 
              "value": { 
                "type": "integer" 
              }, 
              "active": { 
                "type": "boolean" 
              }, 
            } 
          } 
        } 
      } 
    } 
  }); 
} 
```