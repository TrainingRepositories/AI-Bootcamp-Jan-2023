# File to lock
$fileName = "lockedfile.txt"

# Open the file in read only mode and locked
$file = [System.io.File]::Open($fileName, 'Open', 'Read', 'None')

# Wait in the locked state until the user presses a key
Write-Host "The lockedfile.txt file is open exclusively by this script."
Write-Host "When you're done testing, press a key to unlock it again."
$null = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Close and unlock the file
$file.Close()