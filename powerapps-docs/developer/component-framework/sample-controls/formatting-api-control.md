---
title: Formatting API component | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 3b875f06-0fd9-49fa-bc34-939d00e17185
---

# Implementing formatting API component

This sample component explores the various methods available as part of the PowerApps component framework formatting API. In this sample, you create a series of input elements which calls into the respective methods of the formatting API that matches with the value displayed.

> [!div class="mx-imgBorder"]
> ![Formatting API component](../media/formatting-api.png "Formatting API component")

## Available for 

Model-driven apps and canvas apps (experimental preview) 

## Manifest

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
	<control namespace="SampleNamespace" constructor="FormattingAPI" version="1.0.0" display-name-key="TS_FormattingAPI_Display_Key" description-key="TS_FormattingAPI_Desc_Key" control-type="standard">
		<property name="controlValue" display-name-key="controlValue_Display_Key" description-key="controlValue_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" />
		<resources>
			<code path="index.ts" order="1" />
			<css path="css/TS_FormattingAPI.css" order="1" />
		</resources>
	</control>
</manifest>
```

## Code

```TypeScript
import { IInputs, IOutputs } from "./generated/ManifestTypes";
export class FormattingAPI
  implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  // PowerApps component framework framework delegate which will be assigned to this object which would be called whenever an update happens.
  private _notifyOutputChanged: () => void;
  // Reference to the div element that holds together all the HTML elements that we are creating as part of this control
  private divElement: HTMLDivElement;
  // Reference to HTMLTableElement rendered by control
  private _tableElement: HTMLTableElement;
  // Reference to the control container HTMLDivElement
  // This element contains all elements of our custom control example
  private _container: HTMLDivElement;
  // Reference to ComponentFramework Context object
  private _context: ComponentFramework.Context<IInputs>;
  // Flag if control view has been rendered
  private _controlViewRendered: Boolean;
  /**
   * Used to initialize the control instance. Controls can kick off remote server calls and other initialization actions here.
   * Data-set values are not initialized here, use updateView.
   * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to property names defined in the manifest, as well as utility functions.
   * @param notifyOutputChanged A callback method to alert the framework that the control has new outputs ready to be retrieved asynchronously.
   * @param state A piece of data that persists in one session for a single user. Can be set at any point in a controls life cycle by calling 'setControlState' in the Mode interface.
   * @param container If control is marked control-type='standard', it receives an empty div element within which it can render its content.
   */
  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
  ) {
    this._notifyOutputChanged = notifyOutputChanged;
    this._controlViewRendered = false;
    this._context = context;
    this._container = document.createElement("div");
    this._container.classList.add("TSFormatting_Container");
    container.appendChild(this._container);
  }
  /**
   * Helper method to create an HTML Table Row Element
   * @param key : string value to show in left column cell
   * @param value : string value to show in right column cell
   * @param isHeaderRow : true if method should generate a header row
   */
  private createHTMLTableRowElement(
    key: string,
    value: string,
    isHeaderRow: boolean
  ): HTMLTableRowElement {
    let keyCell: HTMLTableCellElement = this.createHTMLTableCellElement(
      key,
      "FormattingControlSampleHtmlTable_HtmlCell_Key",
      isHeaderRow
    );
    let valueCell: HTMLTableCellElement = this.createHTMLTableCellElement(
      value,
      "FormattingControlSampleHtmlTable_HtmlCell_Value",
      isHeaderRow
    );
    let rowElement: HTMLTableRowElement = document.createElement("tr");
    rowElement.setAttribute(
      "class",
      "FormattingControlSampleHtmlTable_HtmlRow"
    );
    rowElement.appendChild(keyCell);
    rowElement.appendChild(valueCell);
    return rowElement;
  }
  /**
   * Helper method to create an HTML Table Cell Element
   * @param cellValue : string value to inject in the cell
   * @param className : class name for the cell
   * @param isHeaderRow : true if method should generate a header row cell
   */
  private createHTMLTableCellElement(
    cellValue: string,
    className: string,
    isHeaderRow: boolean
  ): HTMLTableCellElement {
    let cellElement: HTMLTableCellElement;
    if (isHeaderRow) {
      cellElement = document.createElement("th");
      cellElement.setAttribute(
        "class",
        "FormattingControlSampleHtmlTable_HtmlHeaderCell " + className
      );
      let textElement: Text = document.createTextNode(cellValue);
      cellElement.appendChild(textElement);
    } else {
      cellElement = document.createElement("td");
      cellElement.setAttribute(
        "class",
        "FormattingControlSampleHtmlTable_HtmlCell " + className
      );
      let textElement: Text = document.createTextNode(cellValue);
      cellElement.appendChild(textElement);
    }
    return cellElement;
  }
  /**
   * Helper method to create an HTML Text Input Element
   * @param cellValue : string value to inject in the cell
   * @param className : class name for the cell
   */
  private createHTMLTextInputElement(
    cellValue: string,
    className: string
  ): HTMLInputElement {
    let cellElement: HTMLInputElement;
    cellElement = document.createElement("input");
    cellElement.setAttribute("type", "text");
    cellElement.setAttribute(
      "class",
      "FormattingControlSampleHtmlTable_HtmlCell " + className
    );
    cellElement.setAttribute("value", cellValue);
    return cellElement;
  }
  /**
   * Creates an HTML Table that showcases examples of basic methods available to the custom control
   * The left column of the table shows the method name or property that is being used
   * The right column of the table shows the result of that method name or property
   */
  private createHTMLTableElement(): HTMLTableElement {
    // Create HTML Table Element
    let tableElement: HTMLTableElement = document.createElement("table");
    tableElement.setAttribute(
      "class",
      "FormattingControlSampleHtmlTable_HtmlTable"
    );
    // Create header row for table
    let key: string = "Example Method";
    let value: string = "Result";
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, true));
    // Example use of formatCurrency() method
    // Change the default currency and the precision or pass in the precision and currency as additional parameters.
    key = "formatCurrency()";
    value = this._context.formatting.formatCurrency(10250030);
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    // Example use of formatDecimal() method
    // Change the settings from user settings to see the output change its format accordingly
    key = "formatDecimal()";
    value = this._context.formatting.formatDecimal(123456.2782);
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    // Example use of formatInteger() method
    // change the settings from user settings to see the output change its format accordingly.
    key = "formatInteger()";
    value = this._context.formatting.formatInteger(12345);
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    // Example use of formatLanguage() method
    // Install additional languages and pass in the corresponding language code to see its string value
    key = "formatLanguage()";
    value = this._context.formatting.formatLanguage(1033);
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    // Example of formatDateYearMonth() method
    // Pass a JavaScript Data object set to the current time into formatDateYearMonth method to format the data
    // and get the return in Year, Month format
    key = "formatDateYearMonth()";
    value = this._context.formatting.formatDateYearMonth(new Date());
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    // Example of getWeekOfYear() method
    // Pass a JavaScript Data object set to the current time into getWeekOfYear method to get the value for week of the year
    key = "getWeekOfYear()";
    value = this._context.formatting.getWeekOfYear(new Date()).toString();
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    return tableElement;
  }
  /**
   * Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
   * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
   */
  public updateView(context: ComponentFramework.Context<IInputs>): void {
    if (!this._controlViewRendered) {
      // Render and add HTMLTable to the custom control container element
      let tableElement: HTMLTableElement = this.createHTMLTableElement();
      this._container.appendChild(tableElement);
      this._controlViewRendered = true;
    }
  }
  /**
   * It is called by the framework prior to a control receiving new data.
   * @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
   */
  public getOutputs(): IOutputs {
    // no-op: method not leveraged by this example custom control
    return {};
  }
  /**
   * Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
   * i.e. canceling any pending remote calls, removing listeners, etc.
   */
  public destroy() {}
}
```

## Resources

```CSS
.SampleNamespace\.FormattingAPI {
  font-family: "SegoeUI-Semibold", "Segoe UI Semibold", "Segoe UI Regular",
    "Segoe UI";
}
.SampleNamespace\.FormattingAPI .TSFormatting_Container {
  overflow-x: auto;
}
.SampleNamespace\.FormattingAPI .FormattingControlSampleHtmlTable_HtmlRow {
  background-color: #ffffff;
}
.SampleNamespace\.FormattingAPI
  .FormattingControlSampleHtmlTable_HtmlHeaderCell {
  text-align: center;
}
.SampleNamespace\.FormattingAPI .FormattingControlSampleHtmlTable_HtmlCell,
.SampleNamespace\.FormattingAPI
  .FormattingControlSampleHtmlTable_HtmlHeaderCell {
  border: 1px solid black;
  padding-left: 3px;
  padding-right: 3px;
}
.SampleNamespace\.FormattingAPI
  .FormattingControlSampleHtmlTable_HtmlInputTextCell {
  border: 1px solid black;
  padding: 0px;
}
.SampleNamespace\.FormattingAPI
  .FormattingControlSampleHtmlTable_HtmlHeaderCell {
  font-weight: bold;
  font-size: 16px;
}
.SampleNamespace\.FormattingAPI .FormattingControlSampleHtmlTable_HtmlCell_Key {
  color: #1160b7;
}
.SampleNamespace\.FormattingAPI
  .FormattingControlSampleHtmlTable_HtmlCell_Value {
  color: #1160b7;
  text-align: center;
}
```

### Related topics

[Download sample components](https://go.microsoft.com/fwlink/?linkid=2088525)<br/>
[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Manifest Schema Reference](../manifest-schema-reference/index.md)


