---
title: "Troubleshoot issues with Zscaler (preview)"
description: "Use this guide when `pac code add-data-source` repeatedly fails behind a Zscaler[^1] (or similar SSL‑inspecting) proxy."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 11/13/2025
ms.reviewer: 
ms.topic: article
contributors:

---

# Troubleshoot Zscaler-related issues (preview)

This article provides troubleshooting steps for when the PAC CLI (Power Apps Command Line Interface)  [pac code add-data-source](/power-platform/developer/cli/reference/code#pac-code-add-data-source) repeatedly fails behind a behind Zscaler[^1] or similar SSL-inspecting proxies.

## Symptoms

| Symptom                     | Example Message / Pattern                                                                       |
| --------------------------- | ----------------------------------------------------------------------------------------------- |
| Fetch Failed                | `TypeError: fetch failed` / `[AddDataSource.ServiceCall.GetConnector.Failure] ... fetch failed` |
| Empty Request Failed        | `Error: Request failed: {}` (no body)                                                           |
| TLS Handshake / Cert errors | `UNABLE_TO_VERIFY_LEAF_SIGNATURE` / `SELF_SIGNED CERT IN CHAIN` (if debug enabled)              |
| Works off corporate network | Command succeeds when disconnected from Zscaler                                                 |

## Prerequisites Checklist
1. Verify you have the [latest Power Platform CLI installed](/power-platform/developer/cli/introduction#install-microsoft-power-platform-cli). Update it if you aren't sure.
2. Verify you are authenticated to the correct environment. Use [`pac auth create`](/power-platform/developer/cli/reference/auth#pac-auth-create) and [`pac auth list`](/power-platform/developer/cli/reference/auth#pac-auth-list) commands.
3. Verify you have installed Node.js ≥ 22 (older versions have stricter / differing trust behavior).
4. Verify your ability to read user certificate store (no locked‑down profile restrictions).
5. Verify your corporate policy permits adding Zscaler root CA to user trust for developer tooling.

## Troubleshooting steps

### Step 1: Validate Baseline (Eliminate Non‑Proxy Causes)

Run the [`pac env who`](/power-platform/developer/cli/reference/env#pac-env-who) command.

If this succeeds, general connectivity is fine; failures are isolated to data source calls.

### Step 2: Confirm Proxy Interception

Optionally inspect certificate chain (PowerShell):
```powershell
Invoke-WebRequest https://api.powerplatform.com -UseBasicParsing | Select-Object -ExpandProperty RawContent
```
If Zscaler injects its cert, you'll see Zscaler issuer instead of Microsoft.[^2]

### Step 3: Export Zscaler Root CA to PEM

```powershell
$cert = Get-ChildItem Cert:\CurrentUser\Root | Where-Object { $_.Subject -like "*Zscaler*" } | Select-Object -First 1
$pem  = "-----BEGIN CERTIFICATE-----`n" + [System.Convert]::ToBase64String($cert.RawData,[System.Base64FormattingOptions]::InsertLineBreaks) + "`n-----END CERTIFICATE-----"
Set-Content -Path "$env:USERPROFILE\.zscaler-root-ca.pem" -Value $pem
```
Result: `~\.zscaler-root-ca.pem` created.[^3]

> [!CAUTION]
> **Protect the PEM file:** Ensure proper file permissions on the exported certificate. If a malicious actor can replace this file, they could intercept HTTPS traffic from Node.js processes. Recommended hardening (removes inheritance then grants read-only):[^4]
> ```powershell
> icacls "$env:USERPROFILE\.zscaler-root-ca.pem" /inheritance:r /grant:r "$env:USERNAME:(R)"
> ```
> If removing inheritance conflicts with corporate policy or triggers endpoint protection controls, skip `/inheritance:r` and only grant explicit read permission:
> ```powershell
> icacls "$env:USERPROFILE\.zscaler-root-ca.pem" /grant:r "$env:USERNAME:(R)"
> ```

### Step 4: Instruct Node.js to trust the certificate

```powershell
[System.Environment]::SetEnvironmentVariable('NODE_EXTRA_CA_CERTS', "$env:USERPROFILE\.zscaler-root-ca.pem", 'User')
```
Close & reopen terminal / VS Code to propagate.[^5]

> [!CAUTION]
> **Scope impact:** This environment variable affects ALL Node.js processes run by your user account. If the PEM file is tampered with, every Node.js application (not just PAC CLI) will trust the modified certificate authority. Verify the file hash periodically and keep it secured.

### Step 5: Re‑run the Command

```cmd
pac code add-data-source -a <apiId> -c <connectionId> [-t <tableName>] [-d <dataset|siteUrl>]
```
Expect connector retrieval success instead of fetch failure.

### (Avoid) Insecure Workaround

> [!DANGER]
> **Security Risk:** This completely disables SSL certificate validation for all Node.js HTTPS connections in the current session. Any attacker with network access can perform man-in-the-middle (MITM) attacks. Use ONLY for one-time diagnostic to prove certificate trust is the root cause.[^6] Never commit to scripts; never use in production environments; immediately unset after testing.

```powershell
$env:NODE_TLS_REJECT_UNAUTHORIZED = "0"
```

To unset after testing:
```powershell
Remove-Item Env:\NODE_TLS_REJECT_UNAUTHORIZED
```

## Validation

After applying the solution, retry your command. Look for successful connector retrieval:
```
[AddDataSource.ServiceCall.GetConnector.Start] { apiId: 'shared_office365users' }
[AddDataSource.ServiceCall.GetConnector.Success] { apiId: 'shared_office365users' }
```
Instead of:
```
[AddDataSource.ServiceCall.GetConnector.Failure] { apiId: 'shared_office365users', error: 'fetch failed' }
```

## Troubleshooting Matrix

### `fetch failed` persists
Reconfirm `NODE_EXTRA_CA_CERTS` set after restarting shell; ensure PEM not zero bytes. Run Quick Checks below to validate file exists and environment variable is properly set.

### Multiple Zscaler certs
If `Get-ChildItem Cert:\CurrentUser\Root | Where-Object { $_.Subject -like "*Zscaler*" }` returns multiple certificates, identify the root CA (typically named "Zscaler Root CA"). Modify Step 3 to select the correct one by issuer name or thumbprint.

### Different proxy product
The solution works for any corporate proxy that performs SSL inspection (Blue Coat, Forcepoint, Netskope, etc.), but Step 3 searches for `*Zscaler*` in the certificate subject. Adapt the filter to match your proxy:
```powershell
# For Blue Coat:
$cert = Get-ChildItem Cert:\CurrentUser\Root | Where-Object { $_.Subject -like "*Blue Coat*" } | Select-Object -First 1
# For Forcepoint:
$cert = Get-ChildItem Cert:\CurrentUser\Root | Where-Object { $_.Subject -like "*Forcepoint*" } | Select-Object -First 1
```
Then complete Steps 3-4 with the matched certificate.

### Works outside VPN only

This indicates network-level blocking, not certificate trust issues. Corporate split-tunnel VPN configurations may route Power Platform API traffic through on-premises firewalls that block Node.js/CLI tools or apply restrictive policies to non-browser traffic.[^7] The `NODE_EXTRA_CA_CERTS` fix won't help here. Engage your network/security team to:
- Allowlist PAC CLI traffic to `*.powerplatform.com`, `*.dynamics.com`, `*.azure.net`
- Allow direct HTTPS (port 443) from developer workstations to Microsoft cloud services
- Configure split-tunnel rules to bypass inspection/filtering for trusted Microsoft endpoints

### `SELF_SIGNED CERT IN CHAIN`

Certificate chain is incomplete. Either export the full certificate chain (root + intermediates) or request your network team to provide the complete root CA bundle. Some proxies require both root and intermediate CAs to be trusted.

## Quick Checks

```powershell
Test-Path "$env:USERPROFILE\.zscaler-root-ca.pem"            # Should be True
[System.Environment]::GetEnvironmentVariable('NODE_EXTRA_CA_CERTS','User')
Get-Content "$env:USERPROFILE\.zscaler-root-ca.pem" -TotalCount 2  # Begins with -----BEGIN CERTIFICATE-----
```

## Notes

- Repeat export if Zscaler rotates certificates.
- Change affects only current user scope (no system‑wide risk).
- Safe: adds trust; does not disable validation.
- Use a dedicated dev machine if policy restricts certificate export.


## Escalation Data (Collect Before Filing Issue)

Provide:
- PAC CLI version: `pac --version`
- Node.js version: `node --version`
- OS + shell (e.g. Windows PowerShell 7 / Windows CMD)
- Full command executed (sanitized)
- Sanitized error block (first occurrence)
- Value of `NODE_EXTRA_CA_CERTS` (PowerShell: `[System.Environment]::GetEnvironmentVariable('NODE_EXTRA_CA_CERTS','User')`)
- Presence & hash of PEM file (e.g. `Get-FileHash $env:USERPROFILE\.zscaler-root-ca.pem`)

## References

[Power Platform connectivity requirements](/power-platform/admin/online-requirements)

[Node.js NODE_EXTRA_CA_CERTS documentation](https://nodejs.org/api/cli.html#node_extra_ca_certsfile)

[^1]: **Zscaler SSL Inspection**: Zscaler is a cloud-based security platform that performs SSL/TLS inspection by decrypting and re-encrypting HTTPS traffic. It acts as a man-in-the-middle (by design) to inspect content for threats. See [Zscaler SSL Inspection Overview](https://help.zscaler.com/zia/about-ssl-inspection)

[^2]: **SSL Certificate Interception**: When a proxy like Zscaler intercepts HTTPS traffic, it replaces the original server certificate with its own certificate signed by a corporate root CA. This allows the proxy to decrypt, inspect, and re-encrypt traffic. Browsers trust this because the corporate root CA is installed in the system trust store. See [How HTTPS Interception Works](https://www.eff.org/deeplinks/2017/02/https-interception-weakens-web-security)

[^3]: **Windows Certificate Store & PEM Format**: `Get-ChildItem Cert:\CurrentUser\Root` accesses the Windows Certificate Store via PowerShell's certificate provider. PEM (Privacy Enhanced Mail) is a Base64-encoded format for certificates. The conversion is necessary because Node.js requires PEM format while Windows stores certificates in DER format. See [PowerShell Certificate Provider](powershell/module/microsoft.powershell.security/about/about_certificate_provider) and [PEM Format RFC](https://datatracker.ietf.org/doc/html/rfc7468)

[^4]: **Windows icacls Command**: `icacls` (Integrity Control Access Control List) is a Windows command-line utility for managing file permissions. The parameters used: `/inheritance:r` removes inherited permissions, `/grant:r` replaces existing permissions with read-only access for the specified user. See [icacls Documentation](/windows-server/administration/windows-commands/icacls)

[^5]: **NODE_EXTRA_CA_CERTS Environment Variable**: This Node.js environment variable specifies a file containing additional trusted Certificate Authorities beyond Node.js's built-in list (Mozilla's CA bundle). When set, Node.js will trust certificates signed by CAs in both the built-in list and the specified file. See [Node.js CLI Environment Variables](https://nodejs.org/api/cli.html#node_extra_ca_certsfile)

[^6]: **Disabling TLS Validation (`NODE_TLS_REJECT_UNAUTHORIZED=0`)**: This forces Node.js to accept any presented certificate (including self-signed or spoofed certificates), removing all authenticity and integrity guarantees of HTTPS. It exposes sessions to MITM attacks, credential harvesting, and content tampering. Never use outside a short-lived diagnostic session.

[^7]: **Split‑Tunnel / Allowlisting Guidance**: Some enterprise VPNs route only a subset of traffic directly while forcing other destinations through inspection gateways. Power Platform endpoints must be reachable without blocking or SSL interception conflicts. See Microsoft connectivity requirements for [endpoint allowlisting guidance](/power-platform/admin/online-requirements).

