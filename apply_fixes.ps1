Set-Location 'c:\Users\mkaur\Downloads\github\powerapps-docs-pr'

# Step 1: Restore from git
$files = @(
    'powerapps-docs/maker/canvas-apps/media/data-platform-create-app-scratch/close-data.png',
    'powerapps-docs/maker/canvas-apps/media/data-platform-create-app-scratch/gallery-items.png',
    'powerapps-docs/maker/canvas-apps/media/data-platform-create-app-scratch/final-browse.png',
    'powerapps-docs/maker/canvas-apps/media/data-platform-create-app-scratch/field-list.png'
)
foreach ($f in $files) {
    if (Test-Path $f) {
        git checkout HEAD -- $f
        Write-Host "Restored: $f"
    } else {
        Write-Warning "File not found for restore: $f"
    }
}

Add-Type -AssemblyName System.Drawing

# Step 2: Crop top 50 px from close-data.png and gallery-items.png
$base = 'c:\Users\mkaur\Downloads\github\powerapps-docs-pr\powerapps-docs\maker\canvas-apps\media\data-platform-create-app-scratch'
foreach ($name in @('close-data.png','gallery-items.png')) {
    $p = Join-Path $base $name
    $img = [System.Drawing.Image]::FromFile($p)
    $cY = 50
    $rect = New-Object System.Drawing.Rectangle 0, $cY, $img.Width, ($img.Height - $cY)
    $bmp = New-Object System.Drawing.Bitmap $rect.Width, $rect.Height
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.DrawImage($img, (New-Object System.Drawing.Rectangle 0,0,$rect.Width,$rect.Height), $rect, [System.Drawing.GraphicsUnit]::Pixel)
    $g.Dispose(); $img.Dispose()
    $bmp.Save($p, [System.Drawing.Imaging.ImageFormat]::Png)
    Write-Host "Cropped: $name -> $($bmp.Width)x$($bmp.Height)"
    $bmp.Dispose()
}

# Step 3: Draw red rectangles using explicit per-file calls
function Draw-Box([string]$path, [int]$x, [int]$y, [int]$w, [int]$h, [int]$thickness = 5) {
    $img = [System.Drawing.Image]::FromFile($path)
    $bmp = New-Object System.Drawing.Bitmap $img
    $img.Dispose()
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $pen = New-Object System.Drawing.Pen ([System.Drawing.Color]::Red), $thickness
    $g.DrawRectangle($pen, $x, $y, $w, $h)
    $pen.Dispose()
    $g.Dispose()
    $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    Write-Host "Box drawn on $(Split-Path $path -Leaf) at ($x,$y) ${w}x${h} thickness=$thickness"
    $bmp.Dispose()
}

function Get-Dim([string]$path) {
    $img = [System.Drawing.Image]::FromFile($path)
    $dim = "$($img.Width)x$($img.Height)"
    $img.Dispose()
    return $dim
}

Write-Host ""
Write-Host "=== Current Dimensions ==="
foreach ($n in @('close-data.png','gallery-items.png','final-browse.png','field-list.png')) {
    $p = Join-Path $base $n
    Write-Host "$n size: $(Get-Dim $p)"
}

# Draw boxes
Draw-Box (Join-Path $base 'close-data.png') 284 50 32 28 5
Draw-Box (Join-Path $base 'gallery-items.png') 370 0 610 22 5
Draw-Box (Join-Path $base 'final-browse.png') 4 4 80 28 4
Draw-Box (Join-Path $base 'field-list.png') 2 2 240 40 4

# Verify red pixels exist
Write-Host ""
Write-Host "=== Verification ==="
function Check([string]$name, [int]$x, [int]$y) {
    $p = Join-Path $base $name
    $bm = New-Object System.Drawing.Bitmap $p
    $px = $bm.GetPixel($x, $y)
    Write-Host "$name ($x,$y) = R$($px.R) G$($px.G) B$($px.B)"
    $bm.Dispose()
}
Check 'close-data.png' 284 50
Check 'gallery-items.png' 500 0
Check 'final-browse.png' 4 20
Check 'field-list.png' 2 20
