---
title: " Increment component| Microsoft Docs" 
description: "Implementing a increment component" 
ms.custom: ""
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "article"
ms.author: "nabuthuk" 
author: Nkrb
---

# Implementing increment component

This sample component shows how to bind data with Power Apps component framework and error handling. This component renders as a textbox with an `Increment` button in the runtime. The text box shows the current value and the `Increment` button is clickable. Whenever you click on the button, the value within the textbox is increased by 1. The increment value can be changed to any number you wish.

To implement this component, the first thing you need to define the [Manifest](../manifest-schema-reference/manifest.md) file, and then implement the custom logic in TypeScript. You can download the sample component from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/TS_IncrementControl).

> [!div class="mx-imgBorder"]
> ![Increment component](../media/increment-control.png "Increment component")

## Available for 

Model-driven apps and canvas apps (experimental preview) 

## Manifest

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
  <control namespace="SampleNamespace" constructor="TSIncrementControl" version="1.0.0" display-name-key="TSIncrementControl_Display_Key" description-key="TSIncrementControl_Desc_Key" control-type="standard">
    <type-group name="numbers">
      <type>Whole.None</type>
      <type>Currency</type>
      <type>FP</type>
      <type>Decimal</type>
    </type-group>
    <property name="value" display-name-key="value_Display_Key" description-key="value_Desc_Key" of-type-group="numbers" usage="bound" required="true" />
    <resources>
      <code path="index.ts" order="1" />
	    <css path="css/TS_IncrementControl.css" order="1" />
      <resx path="strings/TSIncrementControl.1033.resx" version="1.0.0" />
    </resources>
  </control>
</manifest>
```

## Code

```TypeScript
import { IInputs, IOutputs } from "./generated/ManifestTypes";
export class TSIncrementControl
  implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  // Value of the field is stored and used inside the control
  private _value: number;
  // Power Apps component framework framework delegate which will be assigned to this object which would be called whenever an update happens.
  private _notifyOutputChanged: () => void;
  // label element created as part of this control
  private label: HTMLInputElement;
  // button element created as part of this control
  private button: HTMLButtonElement;
  // reference to the control container HTMLDivElement
  // This element contains all elements of our custom control example
  private _container: HTMLDivElement;
  /**
   * Empty constructor.
   */
  constructor() {}
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
    // Creating the label for the control and setting the relevant values.
    this.label = document.createElement("input");
    this.label.setAttribute("type", "label");
    this.label.addEventListener("blur", this.onInputBlur.bind(this));
    //Create a button to increment the value by 1.
    this.button = document.createElement("button");
    // Get the localized string from localized string
    this.button.innerHTML = context.resources.getString(
      "TS_IncrementControl_ButtonLabel"
    );
    this.button.classList.add("SimpleIncrement_Button_Style");
    this._notifyOutputChanged = notifyOutputChanged;
    //this.button.addEventListener("click", (event) => { this._value = this._value + 1; this._notifyOutputChanged();});
    this.button.addEventListener("click", this.onButtonClick.bind(this));
    // Adding the label and button created to the container DIV.
    this._container = document.createElement("div");
    this._container.appendChild(this.label);
    this._container.appendChild(this.button);
    container.appendChild(this._container);
  }
  /**
   * Button Event handler for the button created as part of this control
   * @param event
   */
  private onButtonClick(event: Event): void {
    this._value = this._value + 1;
    this._notifyOutputChanged();
  }
  /**
   * Input Blur Event handler for the input created as part of this control
   * @param event
   */
  private onInputBlur(event: Event): void {
    let inputNumber = Number(this.label.value);
    this._value = isNaN(inputNumber)
      ? ((this.label.value as any) as number)
      : inputNumber;
    this._notifyOutputChanged();
  }
  /**
   * Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
   * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
   */
  public updateView(context: ComponentFramework.Context<IInputs>): void {
    // This method would render the control with the updated values after we call NotifyOutputChanged
    //set the value of the field control to the raw value from the configured field
    this._value = context.parameters.value.raw;
    this.label.value = this._value != null ? this._value.toString() : "";
    if (context.parameters.value.error) {
      this.label.classList.add("SimpleIncrement_Input_Error_Style");
    } else {
      this.label.classList.remove("SimpleIncrement_Input_Error_Style");
    }
  }
  /**
   * It is called by the framework prior to a control receiving new data.
   * @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
   */
  public getOutputs(): IOutputs {
    // custom code goes here - remove the line below and return the correct output
    let result: IOutputs = {
      value: this._value
    };
    return result;
  }
  /**
   * Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
   * i.e. canceling any pending remote calls, removing listeners, etc.
   */
  public destroy(): void {}
}
```

## Resources

```css
.SampleNamespace\.TSIncrementControl button.SimpleIncrement_Button_Style {
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  margin: 4px 6px;
  cursor: pointer;
  color: white;
  border-radius: 0px;
  background-color: rgb(59, 121, 183);
  border: none;
  padding: 5px;
  text-align: center;
}
.SampleNamespace\.TSIncrementControl button.SimpleIncrement_Input_Error_Style {
  color: red;
}
```

```XML
<?xml version="1.0" encoding="utf-8"?>
<root>
<xsd:schema id="root" xmlns="" xmlns:xsd="https://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
<xsd:import namespace="https://www.w3.org/XML/1998/namespace" />
<xsd:element name="root" msdata:IsDataSet="true">
  <xsd:complexType>
	<xsd:choice maxOccurs="unbounded">
	  <xsd:element name="metadata">
		<xsd:complexType>
		  <xsd:sequence>
			<xsd:element name="value" type="xsd:string" minOccurs="0" />
		  </xsd:sequence>
		  <xsd:attribute name="name" use="required" type="xsd:string" />
		  <xsd:attribute name="type" type="xsd:string" />
		  <xsd:attribute name="mimetype" type="xsd:string" />
		  <xsd:attribute ref="xml:space" />
		</xsd:complexType>
	  </xsd:element>
	  <xsd:element name="assembly">
		<xsd:complexType>
		  <xsd:attribute name="alias" type="xsd:string" />
		  <xsd:attribute name="name" type="xsd:string" />
		</xsd:complexType>
	  </xsd:element>
	  <xsd:element name="data">
		<xsd:complexType>
		  <xsd:sequence>
			<xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
			<xsd:element name="comment" type="xsd:string" minOccurs="0" msdata:Ordinal="2" />
		  </xsd:sequence>
		  <xsd:attribute name="name" type="xsd:string" use="required" msdata:Ordinal="1" />
		  <xsd:attribute name="type" type="xsd:string" msdata:Ordinal="3" />
		  <xsd:attribute name="mimetype" type="xsd:string" msdata:Ordinal="4" />
		  <xsd:attribute ref="xml:space" />
		</xsd:complexType>
	  </xsd:element>
	  <xsd:element name="resheader">
		<xsd:complexType>
		  <xsd:sequence>
			<xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
		  </xsd:sequence>
		  <xsd:attribute name="name" type="xsd:string" use="required" />
		</xsd:complexType>
	  </xsd:element>
	</xsd:choice>
  </xsd:complexType>
</xsd:element>
</xsd:schema>
<resheader name="resmimetype">
<value>text/microsoft-resx</value>
</resheader>
<resheader name="version">
<value>2.0</value>
</resheader>
<resheader name="reader">
<value>System.Resources.ResXResourceReader, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
</resheader>
<resheader name="writer">
<value>System.Resources.ResXResourceWriter, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
</resheader>
<data name="TS_IncrementControl_ButtonLabel" xml:space="preserve">
<value>Increment</value>
<comment>Label for TS_IncrementControl's Button</comment>
</data>
</root>
```

When you click on the button, the value in the text box is increased by 1. The updated value will flow to Power Apps component framework through `notifyOutputChanged` method.

> [!NOTE]
> You can change the increment value when you are configuring the component to the field on the form.

Edit the value in the text box, and if it is a valid integer, then it updates the value to Power Apps component framework. You can continuously click the `Increment` button and update it. If it’s an invalid integer, an error message pops out.

### Related topics

[Download sample components](https://go.microsoft.com/fwlink/?linkid=2088525)<br/>
[How to use the sample components](../use-sample-components.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework manifest schema reference](../manifest-schema-reference/index.md)