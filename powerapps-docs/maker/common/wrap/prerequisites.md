# Prerequisites:

1.  Maker/User needs to create an Apple account enrolled in Apple Developer Program or Apple Enterprise Developer program

2.  Maker/User needs to create a distribution certificate and either Ad-hoc Provisioning Profile or Enterprise provisioning profile.

3.  Azure AD Subscription to create Key Vault.

4.  Admin Tenant access

# Steps:

1.  Create Service Principal for 1P AAD app - 4e1f8dc5-5a42-45ce-a096-700fa485ba20 ( WrapKeyVaultAccessApp) using the Admin Tenant account.

<https://docs.microsoft.com/en-us/powershell/azure/create-azure-service-principal-azureps?view=azps-8.0.0#create-a-service-principal>

2.  Make sure to add a role to the above Service Principal in the subscription where the KeyVault is going to exist. https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-steps

3.  Create KeyVault with below tags and value.

#### <u>KeyVault Tags Structure for iOS</u>

| <h4 id="tag-name">Tag Name</h4> | Tag Value | Notes |
|-------------------------|-------------------------|-------------------------|
| &lt;BundleID&gt;.cert | Should refer to the KeyVault certificate name to which the iOS certificate was uploaded. | <ul></br><li>IOS Certificate extension (p12) should be renamed to **.pfx as** KeyVault does not accept other formats.</li></br><li>Same iOS Certificate can be used by multiple bundle ids.</li></br></ul> |
| &lt;BundleID&gt;.profile | Should refer to the KeyVault secret name to which the **base64 encoded provisioning profile string** was added. | <ul></br><li>Provisioning profiles are unique for each bundle id.</li></br><li>Command to base64 encode</li></br></ul></br>Mac: base64 -i example.mobileprovision</br>Windows: certutil -encode data.txt tmp.b64 |


#### <u>KeyVault Tags Structure for Android</u>

| Tag Name | Tag Value | Notes |
|-------------------------|-------------------------|-------------------------|
| &lt;BundleID&gt;.keystore | Should refer to the KeyVault certificate name to which the .pfx keystore file is uploaded. | <ul></br><li>Command to create a .pfx keystore</li></br></ul></br>keytool -genkey -alias wrap -keyalg RSA -keystore wrapStore.pfx -keysize 2048 -validity 10000 -storepass Password |

