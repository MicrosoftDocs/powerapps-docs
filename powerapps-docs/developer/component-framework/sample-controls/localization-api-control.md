---
title: " Localization API component| Microsoft Docs" 
description: "Implementing localization api component" 
ms.custom: ""
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "article"
ms.author: "nabuthuk" 
author: Nkrb
---

# Implementing localization API component

This sample showcases how localization is done for code components. In this sample, we use the [Increment component](increment-control.md) to localize the text that is displayed on the increment button based on the user’s selected language. 

Power Apps component framework uses the concept of implementing String(resx) web resources that is used to manage the localized strings shown on any user interface. More information: [String(Resx) Webresources](https://docs.microsoft.com/dynamics365/customer-engagement/developer/resx-web-resources). You can download the sample component from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/TS_LocalizationAPI).

> [!div class="mx-imgBorder"]
> ![Localization API component](../media/localization-api-control.png "Localization API component")

## Available for 

Model-driven apps and canvas apps (public preview) 

## Manifest 

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest>
	<control namespace="SampleNamespace" constructor="TSLocalizationAPI" version="1.0.0" display-name-key="TS_LocalizationAPI_Display_Key" description-key="TS_LocalizationAPI_Desc_Key" control-type="standard">
		<type-group name="numbers">
			<type>Whole.None</type>
			<type>Currency</type>
			<type>FP</type>
			<type>Decimal</type>
		</type-group>
		<property name="value" display-name-key="value_Display_Key" description-key="value_Desc_Key" of-type-group="numbers" usage="bound" required="true" />
		<resources>
			<code path="index.ts" order="1" />
			<css path="css/TS_LocalizationAPI.css" order="1" />
			<resx path="strings/TSLocalizationAPI.1033.resx" version="1.0.0" />
			<resx path="strings/TSLocalizationAPI.1035.resx" version="1.0.0" />
			<resx path="strings/TSLocalizationAPI.3082.resx" version="1.0.0" />
		</resources>
	</control>
</manifest>
```

## Code

```TypeScript
import { IInputs, IOutputs } from "./generated/ManifestTypes";
export class TSLocalizationAPI
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
      "PCF_LocalizationSample_ButtonLabel"
    );
    this.button.classList.add("LocalizationSample_Button_Style");
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
    // This method would re render the control with the updated values after we call NotifyOutputChanged
    //set the value of the field control to the raw value from the configured field
    this._value = context.parameters.value.raw;
    this.label.value = this._value != null ? this._value.toString() : "";
    if (context.parameters.value.error) {
      this.label.classList.add("LocalizationSample_Input_Error_Style");
    } else {
      this.label.classList.remove("LocalizationSample_Input_Error_Style");
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
.SampleNamespace\.TSLocalizationAPI button.LocalizationSample_Button_Style {
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

.SampleNamespace\.TSLocalizationAPI
  button.LocalizationSample_Input_Error_Style {
  color: red;
}
```

```xml
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
<data name="PCF_LocalizationSample_ButtonLabel" xml:space="preserve">
<value>Increment</value>
<comment>Label for TSLocalizationAPI's Button</comment>
</data>
<data name="TS_LocalizationAPI_Display_Key" xml:space="preserve">
<value>Sample Localization Control</value>
<comment>Localization Sample Localized Control Name</comment>
</data>
<data name="TS_LocalizationAPI_Desc_Key" xml:space="preserve">
<value>This control showcases usage of localization.</value>
<comment>Localization Sample Localized Control Description</comment>
</data>
<data name="value_Display_Key" xml:space="preserve">
<value>Value</value>
<comment>Localization Sample Control Main Property Localized Name</comment>
</data>
<data name="value_Desc_Key" xml:space="preserve">
<value>Shows the field that the control is mapped to.</value>
<comment>Localization Sample Control Main Property Localized Description</comment>
</data>
</root>
```

```xml
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
<data name="PCF_LocalizationSample_ButtonLabel" xml:space="preserve">
<value>lisäys</value>
<comment>Label for TSLocalizationAPI's Button</comment>
</data>
<data name="TS_LocalizationAPI_Display_Key" xml:space="preserve">
<value>Esimerkki lokalisointi valvonnasta</value>
<comment>Localization Sample Localized Control Name</comment>
</data>
<data name="TS_LocalizationAPI_Desc_Key" xml:space="preserve">
<value>Tämä ohjaus objekti esittelee lokalisoinnin käyttöä.</value>
<comment>Localization Sample Localized Control Description</comment>
</data>
<data name="value_Display_Key" xml:space="preserve">
<value>Arvo</value>
<comment>Localization Sample Control Main Property Localized Name</comment>
</data>
<data name="value_Desc_Key" xml:space="preserve">
<value>Näyttää kentän, johon ohjaus objekti on yhdistetty.</value>
<comment>Localization Sample Control Main Property Localized Description</comment>
</data>
</root>
```

```xml
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
<data name="PCF_LocalizationSample_ButtonLabel" xml:space="preserve">
<value>Incremento</value>
<comment>Label for TSLocalizationAPI's Button</comment>
</data>
<data name="TS_LocalizationAPI_Display_Key" xml:space="preserve">
<value>Control de localización de muestras</value>
<comment>Localization Sample Localized Control Name</comment>
</data>
<data name="TS_LocalizationAPI_Desc_Key" xml:space="preserve">
<value>Este control muestra el uso de la localización.</value>
<comment>Localization Sample Localized Control Description</comment>
</data>
<data name="value_Display_Key" xml:space="preserve">
<value>Valor</value>
<comment>Localization Sample Control Main Property Localized Name</comment>
</data>
<data name="value_Desc_Key" xml:space="preserve">
<value>Muestra el campo al que se asigna el control.</value>
<comment>Localization Sample Control Main Property Localized Description</comment>
</data>
</root>
```

To localize an existing project, all you need to do is to create additional resource(resx) files, one each for a specific language as mentioned in the string web resources and include them as part of the control’s manifest file under the [resources](../reference/resources.md) node.  

Power Apps component framework identifies the user’s language and returns the strings from that language-specific resource file when you try to access the string using `context.resources.getString` method.

In this sample, two languages `Spanish` and `Finnish` with the language codes 3082 and 1035 respectively defined. We made a copy of the `Increment component` sample and renamed it to `Localization API`. All the corresponding files including the files in the subfolders are renamed accordingly.

In the strings folder under `TS_LocalizationAPI`, two additional resx files with the suffixes corresponding to Spanish and Finnish as 3082 and 1035 are added. The new files created should have their file names ending as `{filename}.3082.resx` and `{filename}.1035.resx` because the framework relies on this naming convention to identify which resource file should be picked for reading the strings for the user.

Ensure that the keys used for strings in all these resource files share the same name across all the languages. Now, when the component is rendered on the UI, we see in the code that we retrieve the value to be displayed on the button using `context.resources.getString("PCF_LocalizationSample_ButtonLabel")`.

When this line of code is executed, the Power Apps component framework automatically identifies the language of the user and picks up the value for the button label using the key provided in the corresponding language file we defined. Below is the text you see for each of the 3 languages we support for this sample component.
  
|LanguageCode |Value Displayed |
|---|---|
|3082 |Incremento |
|1033 |Increment |
|1035 |lisäys | 

### Related topics

[Download sample components](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework)<br/>
[How to use the sample components](../use-sample-components.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework manifest schema reference](../manifest-schema-reference/index.md)