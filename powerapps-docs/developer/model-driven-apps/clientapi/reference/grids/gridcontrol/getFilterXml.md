# getFilterXml (Client API reference)

[!INCLUDE[./includes/getFilterXml-description.md](./includes/getFilterXml-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`var result = gridContext.getFilterXml();`

## Return Value

**Type**: String

**Description**: The FilterXML applied to the grids dataset.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext) 

## Example

The following example displays the retrieved Filter XML of the Contacts subgrid in the console:

```JavaScript
function myFunction(executionContext) {
    var formContext = executionContext.getFormContext(); // get the form context
    var gridContext = formContext.getControl("Contacts"); // get the grid context
    var retrieveFilterXML = function () {
        var result = gridContext.getFilterXml();
        console.log(result)
    };
}
```

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
